## API Description

This API (ModifySubDomain) is used to modify the path mapping in the custom domain name settings of the service. The path mapping rule can be modified before it is bound to the custom domain name.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ---------------------------- | ---- | ------ | ---------------------------------------- |
| serviceId | Yes | String | The unique ID of the service. |
| subDomain | Yes | String | The custom domain name of the path mapping to be modified. |
| isDefaultMapping | Yes | String | Whether to modify to use the default path mapping. TRUE: Using the default path mapping; FALSE: Using the custom path mapping. |
| pathMappingSet.n.path | No | Object | The path of the modified custom path mapping. |
| pathMappingSet.n.environment | No | Object | The environment name of the modified custom path mapping. |

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
&Action=ModifySubDomain
&serviceId=service-XXXX
&subDomain=testSubDomain
&isDefaultMapping=FALSE
&pathMapping.0.path=/test
&pathMapping.0.environment=release
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"
}
```





