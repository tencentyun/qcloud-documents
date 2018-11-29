## 1. API Description
This API (DomainCreate) is used to add domain names.
Domain name for API request: cns.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DomainList.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| domain | Yes | String | Domain name to be added. (Primary domain name only, without "www". For example: qcloud.com) |
| projectId | No | Int | Project ID. "Default project" is used if it is left blank. |

## 3. Output Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> in the Error Codes page.|
| message | String | Module error message description depending on API.|
| data | Array | Data returned by the API. |

If domain name is successfully added, the "data" field is returned which contains domain name information, where

"domain" field is the basic information returned after domain name is added:

| Parameter | Type | Description |
|---------|---------|---------|
| id | String | Domain name ID |
| punycode | String | punycode encoded domain name |
| domain | String | Domain name |

## 4. Example
```
https://cns.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DomainCreate
&domain=qcloud.com
&projectId=0
```


The returned results are as below:
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"domain": {
			"id": "55309561",
			"punycode": "qcloud.com",
			"domain": "qcloud.com"
		}
	}
}
```

