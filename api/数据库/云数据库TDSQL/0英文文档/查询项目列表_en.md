## 1. API Description
This API (CdbTdsqlGetProjectList) is used to query the list of projects.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlGetProjectList.
None.


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| data | Array | Returned data |
| data.projectId | Int | Project ID | 
| data.ownerUin | Int | Owner | 
| data.appid | Int | Application ID | 
| data.name | String | Project name | 
| data.creatorUin | Int | Creator | 
| data.srcPlat | String | Source platform Tencent Cloud | 
| data.srcAppid | Int | Source application ID | 
| data.status | Int | Project status. 0: Normal; -1: Closed. For default project, the value is 3 | 
| data.createTime | String | Creation time | 
| data.isDefault | Int | Whether it is default project. 1: Yes; 0: No | 
| data.info | String | Project information | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetProjectList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "projectId":"0",
            "ownerUin":"0",
            "appid":"0",
            "name":"Default project",
            "creatorUin":"0",
            "srcPlat":"qcloud",
            "srcAppid":"0",
            "status":"3",
            "createTime":"0000-00-00 00:00:00",
            "isDefault":"1",
            "info":"Default project"
        },
        {
            "projectId":"1006677",
            "ownerUin":"909619400",
            "appid":"1251001049",
            "name":"cjcj",
            "creatorUin":"909619400",
            "srcPlat":"qcloud",
            "srcAppid":"1351000042",
            "sourceAppkey":"",
            "sourceAppId":"",
            "class":"",
            "onlinestatus":"0",
            "servicestatus":"0",
            "status":"0",
            "createTime":"2016-05-16 15:21:39",
            "isDefault":"0",
            "info":""
        }
    ]
}
```


