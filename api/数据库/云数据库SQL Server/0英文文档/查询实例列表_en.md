## 1. API Description
This API (GetInstanceList) is used to query list of instances.
Domain for API request: sqlserver.api.qcloud.com

* The **Instance Status** field indicates the current status of an instance, including the following:
 
| Status ID | Status Name |
|--------|-------|
| 1 | Applying |
| 2 | Running |
| 3 | Running with limits (master/slave switching) |
| 4 | Isolated | 
| 5 | Reclaiming |
| 6 | Reclaimed |
| 7 | Task running (operations such as backing up or rolling back instances) |
| 8 | Offline |
| 9 | Expanding instance |
| 10| Migrating instance |

* The **Region ID** field indicates the int value for region mapping, including the following values:
 
| Region ID | Region Name |
|---------|---------|
| 1 | Guangzhou |
| 4 | Shanghai |
| 5 | Hong Kong |
| 7 | Shanghai Finance | 
| 8 | Beijing |
| 11 | Shenzhen Finance |

* The "Availability Zone ID" field indicates the int value for availability zone mapping, including the following values:

| Availability Zone ID | Availability Zone Name |
|---------|---------|
| 100002 | Guangzhou Zone 2 |
| 100003 | Guangzhou Zone 3 |
| 200001 | Shanghai Zone 1 |
| 300001 | Hong Kong Zone 1 |
| 700001 | Shanghai Finance Zone 1 | 
| 800001 | Beijing Zone 1 |
| 110001 | Shenzhen Finance Zone 1 |


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/238/7328' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetInstanceList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| projectId | No | Int | Project ID, which can be queried via API [Query Project List](/doc/api/229/1330) |
| resourceIds.n | No | String | One or more instance IDs (n represents array subscript starting with 0). Instance ID takes a format such as: mssql-si2823jyl |
| regionId | No | Int | Region ID. Use API [View Region ID List](/doc/api/238/9144) |
| zoneId | No | Int | Availability zone ID. Use API [View Availability Zone ID List](/doc/api/238/9144) |
| status | No | Int | Instance status value. Use API [View Instance Status List](/doc/api/238/9144) |
| pageNo | No | Int | Page number. Default is 0 |
| pageSize | No | Int | Number of results returned per page. Default is 50 |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/238/7334#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned data |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Number of instances |
| details | Array | List of instance details |

Parameter details is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| resourceId | String | Instance ID |
| name | String | Instance name |
| projectId | Int | ID of the project to which the instance belongs. You can use API [Query Project List](/doc/api/229/1330) to obtain the project ID |
| regionId | Int | ID of the region to which the instance belongs |
| zoneId | Int | ID of the availability zone to which the instance belongs |
| vpcId | Int | ID of the VPC to which the instance belongs. Use API [Query VPC List](/doc/api/245/1372) |
| subnetId | Int | Subnet ID of the VPC to which the instance belongs. Use API [Query VPC List](/doc/api/245/1372) |
| status | Int | Instance status. Use API [View Instance Status List](/doc/api/238/9144) |
| vip | String |Instance access IP |
| vport | Int | Instance access port |
| createTime | String | Creation time of instance |
| updateTime | String | Update time of instance |
| startTime | String | Start time of billing period for the instance |
| endTime | String | End time of billing period for the instance |
| isolateTime | String | Isolation time of instance |
| memory | Int | Size of instance memory (in GB) |
| used | Int | Storage space occupied by the instance (in GB) |
| storage | Int | Size of instance storage (in GB) |
| versionName | String | Instance version |
| renewFlag | Int | Instance renewal flag. 0: Normal renewal. 1: Auto renewal. 2: No renewal upon expiration |
| model | Int | High availability mode. 1: Dual. 2: Standalone |


## 4. Output Parameters

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 1000 | SystemError | System error. Contact customer service. |
| 1002 | DBConnectError | Database connection error |
| 1004 | OssError | Oss API error |


## 5. Example
Input
<pre>
https://sqlserver.api.qcloud.com/v2/index.php?Action=GetInstanceList
&<<a href="https://cloud.tencent.com/doc/api/238/7328">Common request parameters</a>>
&regionId=1
&resourceIds.0=mssql-pf20sran
&pageSize=20
&pageNo=0
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCount": 1,
        "details": [
            {
                "resourceId": "mssql-pf20sran",
                "name": "ab43d155-41e0-4f8d-b586-51fd3b362518",
                "projectId": 0,
                "regionId": 1,
                "zoneId": 100002,
                "vpcId": 0,
                "subnetId": 0,
                "status": 2,
                "vip": "10.66.19.118",
                "vport": 1433,
                "createTime": "2017-03-16 17:35:38",
                "updateTime": "2017-03-16 18:58:13",
                "startTime": "2017-03-16 18:58:13",
                "endTime": "2017-04-16 18:58:13",
                "isolateTime": "0000-00-00 00:00:00",
                "memory": 2,
                "used": 1,
                "storage": 50,
                "versionName": "SQL Server 2008 R2",
                "renewFlag": 0,
                "model": 1
            }
        ]
    }
}
```


