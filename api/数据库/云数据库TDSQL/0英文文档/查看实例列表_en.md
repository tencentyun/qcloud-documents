## 1. API Description
This API (CdbTdsqlGetInstanceList) is used to view the list of instances.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlGetInstanceList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds.n (cdbInstanceIds is an array. The input parameters here are the array elements) | No | String | Specify instance IDs to be fetched, with n starting with 0 |
| originSerialIds.n (originSerialIds is an array. The input parameters here are the array elements) | No | String | Specify originSerialIds for query, with n starting with 0 |
| pageSize | No | Int | The maximum number of records displayed on each page, which is greater than 1 |
| pageNo | No | Int | The page numbers to which the data to be fetched belongs (subscript starts with 0) |
| orderBy | No | String | Sorting field (projectId, createtime or instancename) |
| orderByType | No | String | Sorting type (desc or asc) |
| searchKey | No | String | Used for fuzzy search for instance name |
| projectIds.n (projectIds is an array. The input parameters here are the array elements) | No | String | Filter by project ID, with n starting with 0 |
| isFilterVpc | No | Int | Whether to search based on VPC. 0: False; 1: True |
| vpcId | No | Int | VPC ID when IsFilterVpc is True |
| subnetId | No | Int | Subnet ID when IsFilterVpc is True |
| uuids.n (uuids is an array. The input parameters here are the array elements) | No | String | Filter by uuids, with n starting with 0 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| data | Array | Returned data packet field |
| data.instances | Array | List of instances | 
| data.instances.id | Int | Instance ID | 
| data.instances.uuid | String | The unique global uuid | 
| data.instances.instancename | String | Instance name | 
| data.instances.appid | Int | Application ID | 
| data.instances.originSerialId | Original instance ID | 
| data.instances.projectId | Int | Project ID | 
| data.instances.regionId | Int | Region ID | 
| data.instances.zoneId | Int | Zone ID | 
| data.instances.vpcId | Int | VPC ID | 
| data.instances.subnetId | Int | Subnet ID | 
| data.instances.status | Int | Instance status | 
| data.instances.vip | String | Private IP | 
| data.instances.vport | Int | Private network PORT | 
| data.instances.wanDomain | String | Public network domain | 
| data.instances.vip | String | Public IP | 
| data.instances.vip | String | Public network port | 
| data.instances.createtime | String | Creation time of instance | 
| data.instances.updatetime | String | Update time | 
| data.instances.autoRenewFlag | Int | Auto-renewal flag. 0: No; 1: Yes | 
| data.instances.specId | Int | Specification ID | 
| data.instances.periodendtime | String | Expiration time of instance | 
| data.instances.uin | String | QQ number | 
| data.instances.pid | String | Product type ID | 
| data.instances.tdsqlVersion | String | TDSQL version information | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| FenceError | Cage API error |
| IllegalExclusterID | Invalid exclusive cluster ID |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetInstanceList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&originSerialIds.0=set_1468822879_203063
&projectIds.0=0
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "totalCnt":"1",
        "instances":[
            {
                "id":"40734",
                "uuid":"tdsql-0gfryg60",
                "instancename":"tdsql40734",
                "appid":"1351000042",
                "originSerialId":"set_1468822879_203063",
                "projectId":"0",
                "regionId":"1",
                "zoneId":"100002",
                "vpcId":"0",
                "subnetId":"0",
                "status":"1",
                "vip":"10.66.17.243",
                "vport":"3306",
                "wanDomain":"",
                "wanVip":"",
                "wanPort":"0",
                "createtime":"2016-07-18 14:21:01",
                "updatetime":"2016-07-18 14:21:59",
                "autoRenewFlag":"0",
                "specId":"8",
                "periodendtime":"2016-10-18 14:21:01",
                "uin":"",
                "pid":10551,
                "tdsqlVersion":"Compatible with MySQL 5.5/5.6"
            }
        ]
    }
}
```


