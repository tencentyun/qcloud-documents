## API Description
This API (ReplaceCert) is used to replace the certificate used in a load balancer instance.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is ReplaceCert.
 
| Parameter Name | Required | Type | Description |
|----------------------|-----------------|------------------|-------------------|---------------|
| oldCertId | Yes | String | ID of the certificate to be replaced. This can be the ID of a server certificate, or a client certificate. |
| newCertId | No | String | ID of the new certificate. newCertContent and newCertName are required if this is left empty. For a server certificate, newCertKey must be set. |
| newCertContent | No | String | Content of the new certificate. newCertId is required if this is left empty. |
| newCertName | No | String | Name of the new certificate. newCertId is required if this is left empty. |
| newCertKey | No | String | Private key of the new certificate. newCertId is required if this parameter does not exist for the server certificate. |


## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Description of task execution status. |

## Example
 
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ReplaceCert
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&oldCertId=4b9fc92b
&newCertId=e2b6d555
</pre>
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}

```


