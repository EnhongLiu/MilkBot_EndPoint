# MilkBot Endpoint

Welcome to the **MilkBot Endpoint** documentation. This guide provides detailed instructions on how to use the endpoint effectively, including data preparation, making requests, and handling results.

---

## 1. Data Preparation

Before using the endpoint, ensure your data is in the following JSON format:

```json
{
  "dataframe_split": {
    "columns": ["LactationNumber", "DaysInMilk", "MilkYieldKg"],  
    "data": [
        [1, 50, 27.2],
        [2, 65, 34.9],
        [3, 60, 42.1]
    ]  
  }
}
```

The above JSON format is derived from a Pandas DataFrame that should look similarly like this:

| LactationNumber |DaysInMilk| MilkYieldKg |
|-----------------|----------|-------------|
| 1               | 50       | 27.2        |
| 2               | 65       | 34.9        |
| 3               | 60       | 42.1        |

Tip: If your data is stored in Excel or CSV format and follow the same format as above, you can use the script `read_in_data.py` to read and convert it into the required JSON format.


## 2. Endpoint Usage
End point is hosted @ https://adb-65044996157806.6.azuredatabricks.net/serving-endpoints/milkbot_python/invocations

You can refer to [`main_request.py`](https://github.com/EnhongLiu/MilkBot_EndPoint/blob/1c7b3717540f54a8c808177cab7c5c1bfc3bd84e/main_request.py) on making requests to the endpoint

Note: Run calculations for parities 1, 2, and 3+ separately to avoid potential crashes. If the endpoint still crashes, re-run the code. This often resolves the issue.


## 3. Post-Processing and Visualization

After completing the calculations via the endpoint, you can follow the example `visual_result.py` to visualize the results. Due to the Bayesian nature of the model and computation power limit, suboptimal results may occur. If this happens, re-running the process often yields better outcomes.
Upon completing the process, you may see a similar graph as below.

<img src ='https://github.com/EnhongLiu/MilkBot_EndPoint/blob/6ce5bd5dddf801da7469fe1136c6dfd3bbce235a/milkbot%20fitted%20line.png' width="700">
