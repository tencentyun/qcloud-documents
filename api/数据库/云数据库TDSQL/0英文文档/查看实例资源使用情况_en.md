## 1. API Description
This API (CdbTdsqlGetResourceUsageInfo) is used to view the usage information of database instance resource.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlGetResourceUsageInfo.

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
| binlog_disk_available | Available space of binlog disk (in GB) |
| cpu_usage_rate | CPU utilization |
| mem_available | Available memory (in GB) |
| data_disk_available | Available disk space (in GB) |
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
| OssOpertaionFailed | OSS internal failure |
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
&Action=CdbTdsqlGetResourceUsageInfo
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
        "binlog_disk_available": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    161,
                    20.89
                ],
                [
                    91,
                    20.88
                ],
                [
                    36,
                    null
                ]
            ]
        },
        "cpu_usage_rate": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                37,
                28,
                [
                    4,
                    39
                ],
                42,
                41,
                42,
                41,
                42,
                [
                    2,
                    40
                ],
                39,
                [
                    2,
                    40
                ],
                43,
                39,
                45,
                [
                    3,
                    39
                ],
                44,
                43,
                [
                    3,
                    39
                ],
                [
                    2,
                    40
                ],
                42,
                41,
                [
                    2,
                    40
                ],
                [
                    4,
                    39
                ],
                40,
                39,
                42,
                39,
                42,
                [
                    4,
                    22
                ],
                31,
                28,
                26,
                27,
                29,
                42,
                7,
                22,
                19,
                [
                    3,
                    5
                ],
                18,
                15,
                21,
                5,
                15,
                [
                    3,
                    5
                ],
                6,
                [
                    3,
                    5
                ],
                6,
                [
                    10,
                    5
                ],
                6,
                5,
                6,
                [
                    5,
                    5
                ],
                6,
                [
                    8,
                    5
                ],
                6,
                [
                    5,
                    5
                ],
                6,
                [
                    51,
                    5
                ],
                12,
                [
                    2,
                    5
                ],
                20,
                23,
                21,
                25,
                5,
                27,
                20,
                [
                    2,
                    23
                ],
                21,
                20,
                21,
                19,
                39,
                33,
                29,
                [
                    5,
                    39
                ],
                42,
                40,
                44,
                40,
                41,
                39,
                42,
                39,
                43,
                [
                    2,
                    39
                ],
                [
                    2,
                    41
                ],
                39,
                41,
                42,
                46,
                [
                    2,
                    39
                ],
                41,
                40,
                39,
                41,
                45,
                40,
                43,
                44,
                40,
                46,
                [
                    2,
                    39
                ],
                [
                    2,
                    40
                ],
                41,
                44,
                39,
                40,
                41,
                [
                    2,
                    40
                ],
                [
                    2,
                    39
                ],
                34,
                [
                    3,
                    40
                ],
                39,
                [
                    2,
                    40
                ],
                37,
                39,
                40,
                37,
                39,
                31,
                38,
                33,
                34,
                30,
                6,
                22,
                23,
                24,
                [
                    2,
                    22
                ],
                19,
                18,
                6,
                14,
                6,
                [
                    2,
                    5
                ],
                [
                    36,
                    null
                ]
            ]
        },
        "data_disk_available": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    252,
                    100
                ],
                [
                    36,
                    null
                ]
            ]
        },
        "mem_available": {
            "StartTime": "2016-07-17 00:00:00",
            "EndTime": "2016-07-18 23:59:59",
            "Data": [
                [
                    231,
                    3.91
                ],
                [
                    21,
                    3.9
                ],
                [
                    36,
                    null
                ]
            ]
        }
    }
}
```


