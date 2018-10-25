## 1. API Description
This API (SetDomainStatus) is used to set domain name status to "Paused" or "Enabled".
Domain name for API request: cns.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DomainList.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| domain | Yes | String | Domain name to be operated on (Primary domain name only, without "www". For example: qcloud.com) |
| status | Yes | String | Available values: "disable" and "enable" |

## 3. Output Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> in the Error Codes page.|
| message | String | Module error message description depending on API.|


## 4. Example
```
https://cns.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=SetDomainStatus
&domain=qcloud.com
&status=enable
```


The returned results are as below:
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success"
}
```
