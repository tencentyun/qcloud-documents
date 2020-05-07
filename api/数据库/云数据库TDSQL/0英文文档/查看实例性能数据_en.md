## 1. API Description
This API (CdbTdsqlGetPerformanceInfo) is used to view the current performance data of a database instance.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlGetPerformanceInfo.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| shardId | No | Int | Shard ID. 0 indicates acquiring the monitoring data of the entire cluster or standalone instance |
| startTime | Yes | date | Start date. Format: yyyy-mm-dd |
| endTime | Yes | date | End date. Format: yyyy-mm-dd |

## 3. Output Parameters
The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976). The following only provides the formats of returned values for the "data" field.

Returned values are in the form of array of performance data.
Data values for different time periods are returned in chronological order. If a value is same over consecutive time periods, the value is returned in the form of [number of periods, value]. For example, [2,3] indicates the value is 3 over two continuous time periods. The length of each time period depends on the difference between the start time and end time of the request. The length of time period is 5 minutes for requests shorter than a day, 30 minutes for requests longer than a day but shorter than 7 days, and 2 hours for those longer than 7 days.

Metrics

| Metric | Description |
|------|-----|
| conn_active | Number of active connections |
| delete_total | Count of DELETE operations |
| disk_iops | I/O count per second for the disk |
| insert_total | Count of INSERT operations |
| is_master_switched | Whether a switching between master and slave occurs. 1: Yes. 0: No |
| long_query | Number of slow logs |
| mem_hit_rate | Cache hit rate |
| select_total | Count of SELECT operations |
| update_total | Count of UPDATE operations |
| slave_delay | Delay between master and slave |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| BaradError | Barad error |
| NoInstanceFound | Instance does not exist |
| InnerSystemError | Internal system error (unrelated to service) |
| InstanceStatusError | Instance status error |
| ShardNotExist | Shard does not exist |
| MetricNotExist | Specified metric does not exist |
| OssOpertaionFailed | OSS internal failure|
| MakeRequestFailed | Failed to join parameters into request |
| BadRequest | Failed to initiate request |
| ReadDataFailed | Failed to read returned data |
| NoDataFetched | No data is fetched |
| JsonUnmarshaFailed | Json resolution failed |
| NoDataFetched | No data is fetched |
| BaradError | Barad data consolidation error |


## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlGetPerformanceInfo
&cdbInstanceId=40732
&startTime=2016-07-17
&endTime=2016-07-18
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "conn_active": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    5,
                    6
                ],
                7,
                [
                    26,
                    6
                ],
                7,
                [
                    182,
                    6
                ],
                [
                    5,
                    7
                ],
                [
                    9,
                    10
                ],
                [
                    2,
                    12
                ],
                [
                    6,
                    13
                ],
                [
                    2,
                    14
                ],
                16,
                17,
                [
                    2,
                    19
                ],
                [
                    2,
                    21
                ],
                20,
                22,
                [
                    3,
                    25
                ],
                [
                    5,
                    24
                ],
                26,
                [
                    2,
                    24
                ],
                [
                    30,
                    null
                ]
            ]
        },
        "delete_total": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    258,
                    0
                ],
                [
                    30,
                    null
                ]
            ]
        },
        "disk_iops": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                3.76,
                4.81,
                4.16,
                3.83,
                5.15,
                4.48,
                4.18,
                6.8,
                3.83,
                3.5,
                4.39,
                4.16,
                4.7,
                3.91,
                6,
                3.75,
                3.68,
                3.67,
                4.57,
                6.24,
                3.6,
                8.24,
                6.24,
                5.52,
                3.64,
                3.34,
                4.88,
                3.91,
                7.43,
                3.51,
                8.57,
                9.54,
                6.48,
                4.54,
                4.16,
                6.78,
                3.6,
                3.59,
                8.75,
                4.39,
                4.72,
                6.28,
                4.16,
                4.26,
                4.7,
                4.86,
                3.34,
                4.71,
                4.21,
                8.09,
                7.87,
                8.06,
                4.56,
                3.28,
                4.15,
                3.65,
                3.84,
                5.76,
                4.48,
                4.96,
                3.59,
                4.08,
                4,
                3.76,
                7.07,
                3.44,
                8.44,
                3.79,
                3.84,
                2.94,
                4.96,
                3.6,
                3.44,
                4.64,
                6.39,
                3.57,
                4.48,
                6.89,
                3.5,
                3.04,
                3.68,
                5.36,
                7.49,
                3.26,
                8.01,
                6.08,
                3.44,
                4.08,
                3.12,
                4.04,
                4,
                7.98,
                4.64,
                3.68,
                2.87,
                2.8,
                3.27,
                3.36,
                4.48,
                5.26,
                3.76,
                3.51,
                5.52,
                4.62,
                4.7,
                3.99,
                4.81,
                3.28,
                4.23,
                3.83,
                4.48,
                3.76,
                8.12,
                7.5,
                4.65,
                3.72,
                3.66,
                4.72,
                3.6,
                3.28,
                4.87,
                3.04,
                4.4,
                3.76,
                8.15,
                4.16,
                3.56,
                4.15,
                4.08,
                7.84,
                6.17,
                6.3,
                2.72,
                4.33,
                3.37,
                7.64,
                3.68,
                4.07,
                4.48,
                4.32,
                7.68,
                [
                    2,
                    3.75
                ],
                5.99,
                10.09,
                4.16,
                5.26,
                5.29,
                4,
                7.77,
                3.84,
                3.8,
                3.87,
                4.78,
                8.68,
                5.36,
                3.75,
                3.48,
                3.75,
                3.44,
                8.1,
                3.6,
                3.47,
                6.21,
                3.5,
                7.93,
                5.18,
                3.92,
                3.5,
                4.16,
                3.98,
                4.9,
                [
                    2,
                    3.92
                ],
                3.34,
                4.41,
                4.08,
                7.96,
                3.35,
                3.73,
                3.04,
                6.95,
                4.55,
                3.28,
                4.88,
                5.03,
                2.64,
                3.28,
                10.39,
                3.51,
                7.59,
                3.17,
                6.38,
                4.48,
                3.44,
                3.84,
                3.85,
                8.56,
                4.08,
                4.22,
                7.69,
                3.36,
                3.91,
                7.37,
                3.59,
                5.02,
                5.11,
                7.5,
                4.16,
                3.04,
                7.43,
                4,
                [
                    2,
                    3.52
                ],
                4.07,
                2.72,
                5.52,
                3.09,
                4.48,
                7.28,
                3.93,
                4.22,
                4.09,
                5.58,
                3.44,
                4.96,
                5.6,
                3.28,
                5.34,
                2.79,
                3.5,
                100.05,
                3.02,
                8.47,
                3.29,
                4.7,
                6.63,
                2.72,
                3.75,
                3.36,
                3.03,
                3.73,
                3.74,
                5.73,
                6.64,
                2.79,
                3.39,
                9.06,
                4.48,
                7.5,
                3.59,
                4.56,
                3.26,
                3.84,
                3.03,
                5.28,
                3.36,
                2.64,
                [
                    30,
                    null
                ]
            ]
        },
        "insert_total": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    258,
                    0
                ],
                [
                    30,
                    null
                ]
            ]
        },
        "is_master_switched": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    258,
                    0
                ],
                [
                    30,
                    null
                ]
            ]
        },
        "long_query": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    231,
                    0
                ],
                6,
                [
                    26,
                    0
                ],
                [
                    30,
                    null
                ]
            ]
        },
        "mem_hit_rate": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    258,
                    99
                ],
                [
                    30,
                    null
                ]
            ]
        },
        "select_total": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                1.45,
                1.55,
                [
                    2,
                    1.47
                ],
                1.45,
                1.53,
                1.55,
                1.45,
                1.43,
                [
                    3,
                    1.55
                ],
                [
                    2,
                    1.45
                ],
                [
                    2,
                    1.55
                ],
                1.53,
                1.45,
                1.42,
                1.47,
                1.43,
                1.42,
                [
                    2,
                    1.45
                ],
                1.42,
                1.53,
                1.52,
                1.43,
                [
                    4,
                    1.45
                ],
                1.42,
                1.43,
                1.42,
                1.45,
                [
                    2,
                    1.47
                ],
                1.45,
                1.55,
                [
                    2,
                    1.45
                ],
                1.43,
                [
                    3,
                    1.42
                ],
                [
                    2,
                    1.43
                ],
                [
                    2,
                    1.42
                ],
                [
                    2,
                    1.45
                ],
                1.42,
                1.43,
                1.47,
                1.43,
                1.45,
                1.53,
                1.5,
                1.47,
                1.43,
                1.42,
                1.45,
                1.55,
                1.45,
                1.47,
                1.45,
                1.47,
                1.45,
                [
                    2,
                    1.47
                ],
                1.55,
                [
                    5,
                    1.45
                ],
                [
                    3,
                    1.42
                ],
                [
                    2,
                    1.43
                ],
                [
                    3,
                    1.45
                ],
                1.43,
                1.42,
                [
                    2,
                    1.43
                ],
                [
                    4,
                    1.42
                ],
                1.43,
                1.5,
                1.53,
                1.55,
                1.52,
                [
                    2,
                    1.55
                ],
                1.5,
                1.43,
                1.42,
                [
                    3,
                    1.45
                ],
                1.47,
                1.45,
                [
                    2,
                    1.47
                ],
                1.42,
                [
                    2,
                    1.55
                ],
                1.42,
                1.45,
                1.43,
                1.42,
                1.45,
                1.42,
                1.43,
                [
                    2,
                    1.45
                ],
                1.55,
                1.53,
                [
                    3,
                    1.55
                ],
                1.47,
                [
                    3,
                    1.45
                ],
                1.47,
                1.42,
                1.45,
                1.5,
                1.53,
                1.5,
                1.43,
                [
                    2,
                    1.47
                ],
                [
                    2,
                    1.43
                ],
                [
                    2,
                    1.47
                ],
                1.45,
                [
                    6,
                    1.42
                ],
                [
                    3,
                    1.53
                ],
                1.42,
                [
                    2,
                    1.45
                ],
                [
                    2,
                    1.53
                ],
                1.45,
                1.47,
                [
                    3,
                    1.45
                ],
                1.42,
                [
                    2,
                    1.55
                ],
                1.53,
                1.55,
                [
                    2,
                    1.47
                ],
                1.42,
                1.45,
                1.55,
                [
                    2,
                    1.47
                ],
                1.42,
                1.45,
                [
                    3,
                    1.47
                ],
                [
                    2,
                    1.45
                ],
                1.47,
                1.43,
                [
                    2,
                    1.45
                ],
                [
                    2,
                    1.47
                ],
                1.43,
                1.42,
                1.53,
                1.55,
                [
                    2,
                    1.47
                ],
                [
                    2,
                    1.42
                ],
                1.47,
                1.55,
                [
                    2,
                    1.53
                ],
                1.55,
                1.45,
                [
                    2,
                    1.42
                ],
                1.43,
                1.42,
                1.43,
                [
                    3,
                    1.55
                ],
                [
                    3,
                    1.45
                ],
                [
                    2,
                    1.53
                ],
                [
                    2,
                    1.55
                ],
                1.45,
                1.47,
                1.52,
                1.43,
                1.42,
                1.43,
                1.52,
                1.53,
                1.55,
                [
                    2,
                    1.42
                ],
                1.47,
                1.42,
                1.52,
                1.48,
                1.47,
                1.43,
                1.45,
                [
                    2,
                    1.47
                ],
                1.45,
                1.47,
                1.45,
                1.48,
                1.45,
                1.5,
                1.47,
                1.45,
                1.48,
                1.55,
                1.45,
                [
                    3,
                    1.42
                ],
                1.45,
                [
                    2,
                    1.43
                ],
                1.5,
                1.47,
                1.48,
                [
                    30,
                    null
                ]
            ]
        },
        "update_total": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    258,
                    0
                ],
                [
                    30,
                    null
                ]
            ]
        }
    }
}
```


