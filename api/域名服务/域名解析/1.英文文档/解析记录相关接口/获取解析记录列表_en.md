## 1. API Description
This API (RecordList) is used to obtain resolution records of domain name.
Domain name for API request: cns.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is RecordList.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| domain | Yes | String | Domain name to be operated on (Primary domain name only, without "www". For example: qcloud.com) |
| offset | No | Int | Offset. Default is 0. For more information, please see the relevant section in the API Introduction. |
| length | No | Int | Returned number. Default is 20. Maximum is 100. For more information, please see the relevant section in the API Introduction. |
| subDomain | No | String | (Filter condition) Filter by sub-domain name. |
| recordType | No | String | (Filter condition) Filter by record type.
| qProjectId | No | Int | (Filter condition) Project ID. |

## 3. Output Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> in the Error Codes page.|
| message | String | Module error message description depending on API.|
| data | Array | Data returned by the API. |

"data" field contains domain name information, number of resolution records and details about the records, where

"domain" is domain name information. The field is described as follows:

| Parameter | Type | Description |
|---------|---------|---------|
| id | String | Domain name ID |
| name | String | Domain name |
| punycode | String | punycode encoded domain name |
| grade | String | Domain name grade |
| owner | String | Mailbox account of the domain name owner |
| ext_status | String | Domain name extension status. "notexist", "dnserror" and "" indicate "domain name is not registered", "DNS setup error" and "normal" respectively. |
| ttl | Int | Default TTL value in resolution record under the domain name. |
| min_ttl | Int | Minimum TTL allowed for the current domain name |
| dnspod_ns | Array | DNS address which should be configured for the domain name |
| status | String | Domain name status. "enable", "pause", "spam", "lock" indicate "normal", "resolution paused", "blocked" and "locked" respectively. |
| q_project_id | Int | ID of project for the domain name |


"info" is the number of resolution records for the domain name. The field is described as follows:

| Parameter | Type | Description |
|---------|---------|---------|
| sub_domains | String | Total number of resolution records |
| record_total | String | Number of records actually returned when filter condition are used. |

"records" contains details about each resolution record. The field is described as follows:

| Parameter | Type | Description |
|---------|---------|---------|
| id | Int | Resolution record ID
| ttl | Int | Record TTL value |
| value | String | Record value |
| enabled | Int | Record status. 1: enabled. 0: paused. |
| updated_on | String | Last modification time of resolution record |
| q_project_id | Int | ID of project to which the resolution record belongs |
| name | String | Sub-domain name |
| line | String | Line name of resolution record |
| line_id | String | Line number of resolution record |
| type | String | Resolution record type |
| remark | String | Remarks of resolution record |
| mx | Int | MX record priority. The value is "0" for non-MX records. |


## 4. Example
```
https://cns.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=RecordList
&offset=0
&length=20
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
			"name": "yizeroapitest.com",
			"punycode": "yizeroapitest.com",
			"grade": "DP_Free",
			"owner": "909619400@qq.com",
			"ext_status": "dnserror",
			"ttl": 600,
			"min_ttl": 600,
			"dnspod_ns": ["f1g1ns1.dnspod.net", "f1g1ns2.dnspod.net"],
			"status": "enable",
			"q_project_id": 0
		},
		"info": {
			"sub_domains": "4",
			"record_total": "4"
		},
		"records": [
            {
				"id": 281628246,
				"ttl": 86400,
				"value": "f1g1ns1.dnspod.net.",
				"enabled": 1,
				"status": "enabled",
				"updated_on": "2017-02-20 10:15:47",
				"q_project_id": 0,
				"name": "@",
				"line": "\u9ed8\u8ba4",
				"line_id": "0",
				"type": "NS",
				"remark": "",
				"mx": 0,
				"hold": "hold"
			},
            {
				"id": 281628247,
				"ttl": 86400,
				"value": "f1g1ns2.dnspod.net.",
				"enabled": 1,
				"status": "enabled",
				"updated_on": "2017-02-20 10:15:47",
				"q_project_id": 0,
				"name": "@",
				"line": "\u9ed8\u8ba4",
				"line_id": "0",
				"type": "NS",
				"remark": "",
				"mx": 0,
				"hold": "hold"
			},
            {
				"id": 281817767,
				"ttl": 600,
				"value": "119.29.18.115",
				"enabled": 1,
				"status": "enabled",
				"updated_on": "2017-02-20 20:00:39",
				"q_project_id": 0,
				"name": "www",
				"line": "\u9ed8\u8ba4",
				"line_id": "0",
				"type": "A",
				"remark": "",
				"mx": 0
			},
            {
				"id": 281817768,
				"ttl": 600,
				"value": "203.195.160.18",
				"enabled": 1,
				"status": "enabled",
				"updated_on": "2017-02-20 20:00:39",
				"q_project_id": 0,
				"name": "www",
				"line": "\u9ed8\u8ba4",
				"line_id": "0",
				"type": "A",
				"remark": "",
				"mx": 0
			}
		]
	}
}
```

