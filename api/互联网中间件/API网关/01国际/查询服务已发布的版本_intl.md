## API Description

This API (DescribeServiceReleaseVersion) is used to query the list of all published versions under a service.
A service is always published with several versions. This API can be used to query the published versions.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| --------- | ---- | ------ | ----------- |
| serviceId | Yes | String | The unique ID of the service to be queried. |
| limit | No | Int | Number of results to be returned. |
| offset | No | Int | Offset. |
## Output Parameters
| Parameter Name | Type | Description |
| ----------- | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| totalCount | String | The total number of published versions. |
| versionList | List of Array | The list of versions. |

versionList is a list of historical versions, which is an array of versionAttribute. versionAttribute is composed as follows:

| Parameter Name | Type | Description |
| ------------ | -------------- | ------------- |
| versionName | String | The version number. |
| versionDesc | String | Description of the version. |
| environments | List of String | The list of environments that the version is published to. |
| createTime | Time | Creation time of the version. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeServiceReleaseVersion
&serviceId=service-XX
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"totalCount":2,
	"versionList":[
		{
			"versionName":"version-20170904xx",
			"versionDesc":"desc",
			"environments":
				[
					"test",
					"prepub"
				],
			"createTime":"2017-09-27 00:00::00"
		},
		{
			"versionName":"version-20170905xx",
			"versionDesc":"desc",
			"environments":
				[
					"release",
				],
			createTime":"2017-09-27 00:00::00"
		}
	]
}
```





