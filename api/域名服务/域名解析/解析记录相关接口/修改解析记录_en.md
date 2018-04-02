## 1. API Description
This API (RecordModify) is used to modify resolution record.
Domain name for API request: cns.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DomainList.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| domain | Yes | String | Domain name to be operated on (Primary domain name only, without "www". For example: qcloud.com) |
| recordId | Yes | Int | Resolution record ID.
| subDomain | Yes | String | Sub-domain name. For example: www |
| recordType | Yes | String | Record type. Available record types are: "A", "CNAME", "MX", "TXT", "NS", "AAAA", "SRV"
| recordLine | Yes | String | Name of record line. For example: "Default". |
| value | Yes | String | Record value. For example, IP:192.168.10.2, CNAME: cname.dnspod.com., MX: mail.dnspod.com.
| ttl | No | Int | TTL value. Range: 1-604,800. Minimum TTL is different for domain names of different grades (default is 600).
| mx | No | Int | MX priority. Range: 0-50. This is required when record type is MX.

## 3. Output Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> in the Error Codes page.|
| message | String | Module error message description depending on API.|
| data | Array | Data returned by the API. |

If record is successfully modified, the "data" field is returned which contains record information, where

"record" field is the basic information returned after record is modified:

| Parameter | Type | Description |
|---------|---------|---------|
| id | String | Resolution record ID |
| name | String | Sub-domain name |
| value | String | Record value |
| status | String | Resolution record status |
| weight | Int | Resolution record weight. Default: null. |

## 4. Example
```
https://cns.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=RecordModify
&domain=qcloud.com
&recordId=371466
&subDomain=www
&recordType=CNAME
&recordLine=Default
&value=cloud.tencent.com
```

The returned results are as below:
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"record": {
			"id": 282529938,
			"name": "yizeronew1487857638",
			"value": "112.112.21.21",
			"status": "enable",
			"weight": null
		}
	}
}
```

