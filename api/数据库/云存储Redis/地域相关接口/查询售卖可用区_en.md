## 1. API Description
This API (DescribeRedisZones) is used to query supported availability zones.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

This API can be used to create the list of availability zones where the Redis can be created. An availability zone where the CRS instance is not available for the user will not be included in the returned list. You can apply for the purchase of the whitelist of a region by submitting a [Ticket](https://console.cloud.tencent.com/workorder/create?level1_id=10&level2_id=103&level1_name=%E6%95%B0%E6%8D%AE%E5%BA%93&level2_name=%E4%BA%91%E5%AD%98%E5%82%A8Redis%20CRS).

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/api/239/7200' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is DescribeRedisZones.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| None | None | None | None |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Array |  |
| data.zones | Array | List of all the availability zones | 
| data.zones.100002 | String | The availability zone name corresponding to the availability zone ID. For example, for the availability zone ID 10002, the availability zone name is Guangzhou Zone 2 | 

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11052 | UserNotInWhiteList |The user is not in the whitelist |

## 5. Example
Input
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=DescribeRedisZones
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
</pre>
Output
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
    "data":{
        "zones":[
            {
                "100002":"Guangzhou Zone 2"
            },
            {
                "200001":"Shanghai Zone 1"
            },
            {
                "300001":"Hong Kong Zone 1"
            },
            {
                "400001":"North America Zone 1"
            }
        ]
    },
}
```
