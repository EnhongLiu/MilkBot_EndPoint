import numpy as np
import matplotlib.pyplot as plt

def predict_milk_yield(dim_range, posterior_parameters):
    scale_posterior, ramp_posterior, decay_posterior, offset_posterior = posterior_parameters

    milk_pred = []
    for dim in dim_range:
        milk_yield = (scale_posterior * 
                        np.exp(-decay_posterior * dim) * 
                        (1 - np.exp((offset_posterior - dim) / ramp_posterior) / 2))
        milk_pred.append(milk_yield)
    return milk_pred


par_result = {
            "1":[parity1_para['predictions']['scale'], parity1_para['predictions']['ramp'], parity1_para          ['predictions']['decay'], parity1_para['predictions']['offset']], 
            "2":[parity2_para['predictions']['scale'], parity2_para['predictions']['ramp'], parity2_para['predictions']['decay'], parity2_para['predictions']['offset']],
            "3+":[parity3_para['predictions']['scale'], parity3_para['predictions']['ramp'], parity3_para['predictions']['decay'], parity3_para['predictions']['offset']]
}

# Prepare raw data
milk_data = pd.read_csv('path/xxxxxxx')
integer_columns = ['DaysInMilk',  'LactationNumber']
milk_data[integer_columns] = milk_data[integer_columns].apply(pd.to_numeric, errors='coerce').astype('Int64')
float_columns = ['MilkYieldKg']
milk_data[float_columns] = milk_data[float_columns].apply(pd.to_numeric, errors='coerce').astype('float')
str_columns = ['AnimalIdentifier', 'Year',	'HerdIdentifier','Breed']
milk_data[str_columns] = milk_data[str_columns].astype(str)

milk_data_p1 = milk_data[milk_data['LactationNumber']==1].dropna()
milk_data_p2 = milk_data[milk_data['LactationNumber']==2].dropna()
milk_data_p3 = milk_data[milk_data['LactationNumber']>2].dropna()

milk_data_p1_agg = milk_data_p1.groupby('DaysInMilk')['MilkYieldKg'].mean()
milk_data_p2_agg = milk_data_p2.groupby('DaysInMilk')['MilkYieldKg'].mean()
milk_data_p3_agg = milk_data_p3.groupby('DaysInMilk')['MilkYieldKg'].mean()


# Plot predicted vs. true milk yield
dim_range = np.arange(1, 306, 1)

plt.figure(figsize=(10, 6))

plt.plot(dim_range, predict_milk_yield(dim_range,par_result['1']), color="red", label="Predicted Milk - Parity 1")
plt.plot(dim_range, predict_milk_yield(dim_range,par_result['2']), color="blue", label="Predicted Milk - Parity 2")
plt.plot(dim_range, predict_milk_yield(dim_range,par_result['3+']), color="green", label="Predicted Milk - Parity 3+")

plt.scatter(milk_data_p1_agg.index, milk_data_p1_agg.values, color="red", s=10, label="True Milk - Parity 1")
plt.scatter(milk_data_p2_agg.index, milk_data_p2_agg.values, color="blue", s=10, label="True Milk - Parity 2")
plt.scatter(milk_data_p3_agg.index, milk_data_p3_agg.values, color="green", s=10, label="True Milk - Parity 3+")

plt.title('Predicted and True Milk Yield vs Days in Milk for Parity 1, 2, and 3+')
plt.xlabel('Days in Milk')
plt.ylabel('Milk Yield (Kg)')
plt.legend()
plt.grid(True)
plt.show()
