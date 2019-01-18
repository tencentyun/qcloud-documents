## API Description
This API (DescribeApiKeysStatus) is used to query the list of keys.
When you have created several key pairs, you can query the information of one or more API keys via this API which will not display the keys.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ---------------- | ---------------------------------------- |
| secretIds.n | No | Array of Strings | Queries by one or more API key IDs. If you do not enter the key ID, the information of the first 20 keys is returned by default |
| offset | No | Int | Offset. Default is 0. |
| limit | No | Int | Number of returned results. Default is 20. Maximum is 100. |
| orderby | No | String | Sorting field. |
| order | No | String | Sorting mode. |
| searchName | No | String | Conducts fuzzy search based on the key name. |
| searchId | No | String | Conducts exact search based on the unique ID of the key. |

## Output Parameters

| Parameter Name | Type | Description |
| --------------- | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Number of API keys that meet the condition. |
| apiKeyStatusSet | List of Array | List of API keys. |

"apiKeyStatusSet" is an array of "apiKeyStatus", which is composed as follows:

| Parameter Name | Type | Description |
| ------------ | --------- | ---------------------------------------- |
| secretId | String | ID of API key. |
| secretName | String | User-defined key name. |
| status | Boolean | Key status. 1: In use; 0: Disabled. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeApiKeysStatus
&secretIds.0=AKIDXXXXWKipDlK
&secretIds.1=AKIDXXXXAVd3EuW
&offet=0
&limit=2
&orderby=createdTime
&order=desc
&searchKey=aa
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
	"totalCount":2,
	"apiKeyStatusSet":[
		{
			"secretId":"AKIDXXXXWKipDlK",
			"secretName":"myTest",
			"status":1,
			"createdTime":"2017-08-07T00:00:00Z",
			"modifiedTime":"2017-08-07T00:00:00Z",
		},
		{
			"secretId":"AKIDXXXXAVd3EuW",
			"secretName":"myTest1",
			"status":0,
			"createdTime":"2017-08-07T00:10:00Z",
			"modifiedTime":"2017-08-07T00:10:00Z",
		}
	]
}
```





