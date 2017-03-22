## 1. API Description
 ReplaceCert API is used to replace certificate used by the cloud load balancer instance.
 
Domain for API access: lb.api.qcloud.com


## 2. Request Parameters

   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is ReplaceCert.
 
| Parameter Name | Required | Type | Description |
|----------------------|-----------------|------------------|-------------------|---------------|
| oldCertId | Yes | String | ID of the certificate to be replaced. This can be the ID of a server certificate, or a client certificate. |
| newCertId | No | String | ID of the new certificate. If this is left empty, you must enter newCertContent and newCertName. In addition, if it's a server certificate, you must enter newCertKey. |
| newCertContent | No | String | Content of the new certificate. If this item doesn't exist, you must enter newCertId. |
| newCertName | No | String | Name of the new certificate. If this item doesn't exist, you must enter newCertId. |
| newCertKey | No | String | Private key of the new certificate. If this item doesn't exist for the server certificate, you must enter newCertId. |


## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Description regarding the operation status of the task. |

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ReplaceCert
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&oldCertId=4b9fc92b
&newCertId=e2b6d555
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}

```



