## API Description

This API (BindSubDomain) is used to bind a custom domain name to a service.
Each service in the API gateway provides a default domain name for users to call. If you wants to use an existing domain name, the custom domain name can be bound to the service. After cname of the default domain name is done, the custom domain name can be called directly.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ---------------------------- | ---- | ------ | ---------------------------------------- |
| serviceId | Yes | String | The unique ID of the service. |
| subDomain | Yes | String | The custom domain name to be bound. |
| certificateId | No | String | The unique ID of the certificate of the custom domain name to be bound. |
| isDefaultMapping | No | String | Whether to use the default path mapping. The default is TRUE. FALSE indicates that a custom path mapping is used, and pathMappingSet is required. |
| pathMappingSet.n.path | No | Object | The path of the custom path mapping. When using the custom mapping, you can map only one path to one environment, or map several paths to several environments. Once the custom mapping is used, only the custom mapping path is effective instead of the default mapping rule. |
| pathMappingSet.n.environment | No | Object | The environment name of the custom path mapping. |

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
&Action=BindSubDomain
&serviceId=service-XXXX
&subDomain=testSubDomain
&certificate=testcertificate
&pathMapping.0.path=/test
&pathMapping.0.environment=release
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
}
```





