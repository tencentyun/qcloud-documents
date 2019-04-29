## API Description
This API (DescribeUsagePlanSecretIds) is used to query the list of keys bound to a usage plan.
A usage plan can be bound to multiple key pairs in API Gateway. You can query the key pairs bound with the usage plan using this API.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ------ | ----------------- |
| usagePlanId | Yes | String | The unique ID of the usage plan to be queried. |
| limit | No | Int | Number of results to be returned. |
| offset | No | Int | Offset (from which key pair the query is started). |

## Output Parameters

| Parameter Name | Type | Description |
| ------------ | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| totalCount | String | Number of keys. |
| secretIdList | List of Array | List of key details. |

"secretIdList" is an array of "secretStatus", which is composed as follows:

| Parameter Name | Type | Description |
| ---------- | ------ | ------------------ |
| secretName | String | Key name. |
| secretId | String | Key ID. |
| status | Int | Key status. 0: Disabled; 1: Enabled. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeUsagePlanSecretIds
&usagePlanId=usagePlan-XX
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"totalCount":2
	"secretIdList":[
		{
			"secretName":"hwpwolmy",
			"secretId":"AKIDckpbbu0uogyngvbjuhn3z1mbqfy1db7h2cs9",
			"status":1
		},
		{
			"secretName":"8jsuxt2i",
			"secretId":"AKIDFD3ZD5rq48TQKH61Lh6l37m0w507rD3h79z",
			"status":0
		}
	]
}
```





