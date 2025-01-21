# MilkBot_EndPoint

## 1. 

Before using the endpoint, ensure your data is in the following JSON format:

{
  "dataframe_split": {
        "columns": list(dataframe.columns),  
        "data": dataframe.values.tolist()  
    }
}

where the dataframe example is demonstrated from a Pandas DataFrame, and it should look like this:

| LactationNumber |DaysInMilk| MilkYieldKg |
|-----------------|----------|-------------|
| 1               | 50       | 27.2        |
| 2               | 65       | 34.9        |
| 3               | 60       | 42.1        |

If your data is saved in Excel or CSV format, you can use the function xxxxx to read and convert it into the required JSON format


## 2. 
End point is hosted @ https://adb-65044996157806.6.azuredatabricks.net/serving-endpoints/milkbot_python/invocations

You can refer to xxx on making requests to the endpoint

Note: Run calculations for parities 1, 2, and 3+ separately to avoid potential crashes. If the endpoint still crashes, re-run the code. This often resolves the issue.

## 3. 

After completing the calculations via the endpoint, you can follow the example xxx to visualize the results. Due to the Bayesian nature of the model, suboptimal results may occasionally occur. If this happens, re-running the process often yields better outcomes.
