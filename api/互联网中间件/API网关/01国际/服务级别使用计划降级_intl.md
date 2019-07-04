## API Description

This API (DemoteServiceUsagePlan) is used to degrade the usage plan of a service in a given environment to the API level.
If the authentication is required for the service to take effect, you need to bind usage plans to this service. This API is used to query all usage plans bound to a service.
This operation is not allowed for a service with no API.
This operation is not allowed if the service has not been released in the given environment.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------------- | ---- | ------ | ------------------- |
| serviceId | Yes | String | The unique ID of the service to be queried. |
| environment | Yes | String | The environment name. |
| usagePlanId | Yes | String | Usage plan ID. |

## Output Parameters
| Parameter Name | Type | Description |
| ------------- | -------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |


## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DemoteServiceUsagePlan
&serviceId=service-XX
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"
}
```





