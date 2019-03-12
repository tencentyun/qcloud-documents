## API Description

This API (BindSecretIds) is used to bind keys to a usage plan.
To call the API of a service with a key, you need to bind the key to a usage plan using this API, and bind the usage plan to an environment where the service is released.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------- | ---- | -------------- | ------------- |
| usagePlanId | Yes | String | The unique ID of the usage plan to be bound. |
| secretIds | Yes | List of String | An array of key IDs to be bound. |

## Output Parameters
| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=BindSecretIds
&usagePlanId=usagePlan-XX
&secretIds.0=AKIDXXXXXXwEdsADQ
&secretIds.1=AKIDXXXXXXjkIjdDE
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
}
```





