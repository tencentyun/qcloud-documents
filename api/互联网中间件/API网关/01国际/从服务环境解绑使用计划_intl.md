## API Description

This API (UnBindEnvironment) is used to unbind usage plans from a specified environment.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| -------------- | ---- | -------------- | --------------- |
| usagePlanIds.n | Yes | List Of String | List of the unique IDs of the usage plans to be unbound. |
| serviceId | Yes | String | The unique ID of the service to be unbound. |
| environment | Yes | String | The service environment to be unbound. |
| bindType | No | String | Binding type. Value range: API and SERVICE. Default is SERVICE. |
| apiIds.n | No | List of String | An array of unique API Ids. This parameter is required if bindType=API. |

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
&Action=UnBindEnvironment
&usagePlanId.0=usagePlan-XX
&usagePlanId.1=usagePlan-XXX
&serviceId=sevice-XX
&environment=test
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
}
```

```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=UnBindEnvironment
&usagePlanId.0=usagePlan-XX
&usagePlanId.1=usagePlan-XXX
&serviceId=sevice-XX
&apiIds.0=api-2yuua008
&bindType=API
&environment=test
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
}
```



