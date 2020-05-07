## 1. API Description
This API (CdbTdsqlGetSpecList) is used to query instance specifications.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is CdbTdsqlGetSpecList.

None.


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| data | Array | Returned specification information |
| data.spec | Array | Specification list | 
| data.spec.specinfos | Array | Specification information | 
| data.spec.specinfos.machine | String | Model | 
| data.spec.specinfos.specid | Int | Specification ID | 
| data.spec.specinfos.mem | Int | Memory (in MB) | 
| data.spec.specinfos.data_disk | Int | Disk (in MB) | 
| data.spec.specinfos.log_disk | Int | Log disk (in MB) | 
| data.spec.specinfos.title | String | Specification name | 
| data.spec.specinfos.typeName | String | Specification edition | 
| data.spec.specinfos.tdsqlVersion | String | Database version | 
| data.spec.specinfos.suitInfo | String | Scenarios where the product is applicable | 
| data.spec.specinfos.qps | Int | Request count per second | 
| data.spec.specinfos.pid | Int | Product model ID | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetSpecList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "spec":[
            {
                "machine":"Z3",
                "specinfos":[
                    {
                        "machine":"Z3",
                        "specid":"1",
                        "mem":"48000",
                        "data_disk":"800000",
                        "log_disk":"200000",
                        "title":"Extra-large",
                        "typeName":"Standard",
                        "tdsqlVersion":"Compatible with MySQL 5.5/5.6",
                        "suitInfo":"Extra-large applications with daily independent users at 1,000k level",
                        "qps":"36300",
                        "pid":"10554"
                    },
                    {
                        "machine":"Z3",
                        "specid":"2",
                        "mem":"24000",
                        "data_disk":"400000",
                        "log_disk":"100000",
                        "title":"Large",
                        "typeName":"Standard",
                        "tdsqlVersion":"Compatible with MySQL 5.5/5.6",
                        "suitInfo":"Large applications with daily independent users at 1,000k level",
                        "qps":"19300",
                        "pid":"10553"
                    },
                    {
                        "machine":"Z3",
                        "specid":"4",
                        "mem":"12000",
                        "data_disk":"200000",
                        "log_disk":"50000",
                        "title":"Medium",
                        "typeName":"Standard",
                        "tdsqlVersion":"Compatible with MySQL 5.5/5.6",
                        "suitInfo":"Medium and large applications with daily independent users at 100k level",
                        "qps":"6800",
                        "pid":"10552"
                    },
                    {
                        "machine":"Z3",
                        "specid":"8",
                        "mem":"6000",
                        "data_disk":"100000",
                        "log_disk":"25000",
                        "title":"Small",
                        "typeName":"Standard",
                        "tdsqlVersion":"Compatible with MySQL 5.5/5.6",
                        "suitInfo":"Medium applications with daily independent users at 10k level",
                        "qps":"4100",
                        "pid":"10551"
                    },
                    {
                        "machine":"Z3",
                        "specid":"16",
                        "mem":"3000",
                        "data_disk":"50000",
                        "log_disk":"12500",
                        "title":"Extra-small",
                        "typeName":"Standard",
                        "tdsqlVersion":"Compatible with MySQL 5.5/5.6",
                        "suitInfo":"For service feature test",
                        "qps":"2500",
                        "pid":"10555"
                    }
                ]
            }
        ]
    }
}
```


