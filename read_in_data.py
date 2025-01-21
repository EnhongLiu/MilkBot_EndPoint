import pandas as pd


def read_data_for_api(file_path):
    milk_data = pd.read_csv(file_path)

    # Fix Data Types
    integer_columns = ['DaysInMilk', 'LactationNumber']
    milk_data[integer_columns] = milk_data[integer_columns].apply(pd.to_numeric, errors='coerce').astype('Int64')

    float_columns = ['MilkYieldKg']
    milk_data[float_columns] = milk_data[float_columns].apply(pd.to_numeric, errors='coerce').astype('float')

    str_columns = ['AnimalIdentifier', 'Year', 'HerdIdentifier', 'Breed']
    milk_data[str_columns] = milk_data[str_columns].astype(str)

    # Keep only relevant columns
    milk_data = milk_data[['LactationNumber', 'DaysInMilk', 'MilkYieldKg']]

    # Split the data into dataframes for parity 1, 2, and 3+
    milk_data_p1 = milk_data[milk_data['LactationNumber'] == 1].dropna()
    milk_data_p2 = milk_data[milk_data['LactationNumber'] == 2].dropna()
    milk_data_p3 = milk_data[milk_data['LactationNumber'] > 2].dropna()

    # Downsample dataframes to reduce computation burden
    def sample_data(milk_data, num_samples=10):
        sampled_data = milk_data.groupby('DaysInMilk').apply(lambda group: group.sample(min(len(group), num_samples)))
        sampled_data = sampled_data.reset_index(drop=True)  # Reset index after sampling
        return sampled_data

    milk_data_p1_sampled = sample_data(milk_data_p1)
    milk_data_p2_sampled = sample_data(milk_data_p2)
    milk_data_p3_sampled = sample_data(milk_data_p3)

    # Format the data for API input
    def prepare_api_payload(dataframe):
        payload = {
            "dataframe_split": {
                "columns": list(dataframe.columns),  # Use the column names from the DataFrame
                "data": dataframe.values.tolist()   # Convert values to a list of lists
            }
        }
        return payload

    # Prepare API payloads for each parity group
    api_payload_p1 = prepare_api_payload(milk_data_p1_sampled)
    api_payload_p2 = prepare_api_payload(milk_data_p2_sampled)
    api_payload_p3 = prepare_api_payload(milk_data_p3_sampled)

    return api_payload_p1, api_payload_p2, api_payload_p3

