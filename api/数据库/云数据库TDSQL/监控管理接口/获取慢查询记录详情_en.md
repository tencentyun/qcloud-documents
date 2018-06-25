## 1. API Description
This API (CdbTdsqlGetSlowLogAnalysis) is used to acquire details of slow logs.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlGetSlowLogAnalysis.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| startTime | Yes | datetime | Start time for the query, such as: 2016-07-23 14:55:20 |
| endTime | Yes | datetime | End time for the query, such as: 2016-08-22 14:55:20 |
| db | Yes | String | Database name for the slow log statement to be queried |
| user | Yes | String | User name for the slow log statement to be queried |
| checkSum | Yes | String | Checksum of the slow log statement to be queried (obtained from the slow query log list) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data.StartTime | String | Start time of the slow log SQL |
| data.EndTime | String | End time of the slow log SQL |
| data.Data | Array | Detailed slow log data returned. Format: [Number of periods, value]. For example, [2,3] indicates the value is 3 over two continuous time periods. The length of each time period depends on the difference between the start time and end time of the request. The length of time period is 5 minutes for requests shorter than a day, 30 minutes for requests longer than a day but shorter than 7 days, and 2 hours for those longer than 7 days. |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| EINSTANCEDELETED | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| IllegalTime | Invalid time parameter |
| GetInstanceInfoFailed | Failed to acquire instance information |
| LogDBFailed | logDB API error |
| OssOpertaionFailed | OSS internal failure |
| InnerSystemError | Internal system error (unrelated to service) |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetSlowLogAnalysis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&cdbInstanceId=40746
&startTime=2016-08-05 18:20:00
&endTime=2016-08-06 18:30:50
&user=test_slow
&checkSum=17988922643135866314
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
    	"StartTime": "2016-08-06 02:31:55",
    	"EndTime": "2016-08-06 02:36:55",
    	"Data": [
        	[
            	1,
            	3
        	],
        	[
            	1,
            	9
        	]
    	]
	}
}
```


