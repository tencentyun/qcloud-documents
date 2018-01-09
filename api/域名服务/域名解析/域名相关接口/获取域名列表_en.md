## 1. API Description
This API (DomainList) is used to obtain domain names under the account.
Domain name for API request: cns.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DomainList.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| offset | No | Int | Offset. Default is 0. For more information, please see the relevant section in API Introduction. |
| length | No | Int | Number of results to be returned. Default is 20. Maximum is 100. For more information, please see the relevant section in API Introduction. |
| keyword | No | String | (Filter condition) Search domain names by keywords. |
| qProjectId | No | Int | (Filter condition) Project ID. |

## 3. Output Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> in the Error Codes page.|
| message | String | Module error message description depending on API.|
| data | Array | Data returned by the API. |

The "data" parameter contains the number of domain names under the account as well as the list of domain names, where

"info" is described as follows:

| Parameter | Type | Description |
|---------|---------|---------|
| domain_total | Int | Total number of domain names under the account. |

"domains" contains detailed information about each domain name. The fields are described as follows:

| Parameter | Type | Description |
|---------|---------|---------|
| domain_total | Int | Total number of domain names under the account |
| id | Int | Domain name ID |
| status | String | Domain name status. "enable", "pause", "spam", "lock" indicate "normal", "resolution paused", "blocked" and "locked" respectively. |
| group_id | String | Domain name group ID |
| searchengine_push | String | Whether search engine priority push is enabled. "yes": enabled, "no": disabled. |
| is_mark | String | Indicates whether the domain name is asterisked. "yes" and "no" means "asterisked" and "not asterisked" respectively. |
| ttl | String | Default TTL value in resolution record under the domain name |
| cname_speedup | String | "enable" or "disable". |
| remark | String | Remarks of domain name |
| created_on | String | Time when the domain name was added |
| updated_on | String | Last time when the domain name was modified |
| q_project_id | Int | ID of project for the domain name |
| punycode | String | punycode encoded domain name |
| ext_status | String | Domain name extension status. "notexist", "dnserror" and "" indicate "domain name is not registered", "DNS configuration error" and "normal" respectively. |
| src_flag | String | Domain name source flag. "QCLOUD", "DNSPOD" indicate "Tencent Cloud resolution" and "DNSPod", respectively. |
| name | String | Domain name |
| grade | String | Domain name grade |
| grade_title | String | Grade title of domain name |
| is_vip | String | Whether the domain name is a VIP domain. "yes" or "no". |
| owner | String | Email account of the domain name owner |
| records | String | Number of resolution records under the domain name |
| min_ttl | Int | Minimum TTL allowed for the current domain name |

## 4. Example
```
https://cns.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DomainList
&offset=0
&length=10
```


Return reference. `code` being 0 means success.
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "info": {
            "domain_total": 18
        },
        "domains": [
            {
                "id": 53980930,
                "status": "enable",
                "group_id": "1",
                "searchengine_push": "no",
                "is_mark": "no",
                "ttl": "600",
                "cname_speedup": "disable",
                "remark": "",
                "created_on": "2017-02-08 18:05:22",
                "updated_on": "2017-02-08 18:05:22",
                "q_project_id": 0,
                "punycode": "yizero.wang",
                "ext_status": "dnserror",
                "src_flag": "QCLOUD",
                "name": "yizero.wang",
                "grade": "DP_Free",
                "grade_title": "New free packages",
                "is_vip": "no",
                "owner": "100000@qq.com",
                "records": "2",
                "min_ttl": 600
            }
        ]
    }
}
```


