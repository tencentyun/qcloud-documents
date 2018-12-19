## 1. API Description
This API (GetCdbReadOnlyInstances) is used to query the list of read-only instances associated with master instances, and supports the query based on multiple master instance IDs.
You can also use API [Query List of Instances](/doc/api/253/1266) to query the list of master instances and disaster recovery instances.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbReadOnlyInstances.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds.n | Yes | String | One or more master instance IDs (n represents array subscript starting with 0). Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Read-only instance data |
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| masterCdbInstanceId | String | Master instance ID of read-only instances. Please use API [Query List of Instances](/doc/api/253/1266) to query instance ID |
| groupId | Int | ID of read-only instance group. Each master instance currently supports three read-only instance groups |
| groupName | String | Name of read-only instance group |
| cdbVersion | String | Version number of read-only instance database engine. Possible returned values include: 5.5 and 5.6 |
| cdbType | String | Read-only instance specifications description. For example: CUSTOM. Please use API [Query Specifications of Creatable Instances](/doc/api/253/1333) to query the details of cdbType |
| status | Int | Read-only instance status. Possible returned values include: <br>0-Creating<br>1-Running<br>4-Deleting<br>5-Isolated |
| vip | String | Read-only instance access IP |
| vport | Int | Read-only instance access port |
| vpcId | Int | VPC ID of the read-only instance. Please use [Query VPC List](/doc/api/245/1372) |
| subnetId | Int | VPC subnet ID of the read-only instance. Please use [Query VPC List](/doc/api/245/1372) |
| addTimeStamp | Int | Creation time of read-only instance group. Format: yyyy-mm-dd hh:mm:ss |
| modTimeStamp | Int | Last modification time of read-only instance group. Format: yyyy-mm-dd hh:mm:ss |
| roList| Int | List of read-only instances contained in read-only instance group. Each read-only instance group currently supports one read-only instance |
Parameter roList is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| groupId | Int | ID of read-only instance group of the read-only instance | 
| cdbInstanceId | String | Read-only instance UUID (deprecated). It is recommended to use uInstanceId instead. The ID will only be returned after the instance is created. For the creating instance, it will only return uInstanceId.  |
| uInstanceId | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| cdbInstanceName | String | Read-only instance name | 
| status | Int | Read-only instance status. Possible returned values include: <br>0-Creating<br>1-Running<br>4-Deleting<br>5-Isolated | 
| taskStatus | Int | Read-only instance task status. Possible returned values include: <br>0-No tasks<br>-Upgrading<br>2-Importing Data<br>3-Opening Slave<br>4-Enabling Public Network Access<br>5-Performing Batch Operations<br>6-Rollback<br>7-Disabling Public Network Access<br>8-Modifying Password<br>9-Modifying Instance Name<br>10-Modifying Parameters<br>11-Initializing<br>12-Creating Migration | 
| cdbVersion | String | Version number of read-only instance database engine. Possible returned values include: 5.5 and 5.6 | 
| cdbType | String | Read-only instance specifications description. For example: CUSTOM | 
| typeName | String | Name of read-only instance type, such as: High IO | 
| initFlag | Int | Read-only instance initialization mark. Possible returned values include: 0-Uninitialized; 1-Initialized | 
| autoRenewFlag | Int | Automatic renewal mark of read-only instance. Possible returned values include: 0 indicates that the instance is not automatically renewed; 1 indicates that the instance is automatically renewed | 
| dealId | String | Order ID of read-only instance | 
| payType | Int | Billing type of read-only instance. Possible returned values include: 0-Annual or Monthly Plan; 1-Pay by Usage; 2-Postpaid Billing on a Monthly Basis | 
| cdbMem | Int | Capacity of read-only instance memory (in MB) | 
| cdbVolume | Int | Capacity of read-only instance disk (in GB) | 
| cdbQps | Int | Maximum number of queries for read-only instances per second (times/second) | 
| zoneId | Int | Availability zone ID of the read-only instance | 
| deadline | String | Expiry time of read-only instance. If the instance is in pay by usage mode, then the field value is 0000-00-00 00:00:00. Format: yyyy-mm-dd hh:mm:ss | 
| modTimeStamp | String | Modification time of read-only instance. Format: yyyy-mm-dd hh:mm:ss | 
| addTimeStamp | String | Creation time of read-only instance. Format: yyyy-mm-dd hh:mm:ss | 
| binlogSize | Int | Size of binlog (in GB) |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbReadOnlyInstances
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceIds.0=cdb-c1nl9rpv
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "groupId": 46,
            "groupName": "Rogroup_86216464",
            "cdbVersion": "5.6",
            "cdbType": "CUSTOM",
            "status": 1,
            "vip": "10.66.149.97",
            "vport": 3306,
            "vpcId": 0,
            "subnetId": 0,
            "addTimeStamp": "2016-10-11 11:58:28",
            "modTimeStamp": "2016-10-11 11:58:30",
            "roList": [
                {
                    "groupId": 46,
                    "status": 1,
                    "cdbVersion": "5.6",
                    "cdbType": "CUSTOM",
                    "taskStatus": 0,
                    "initFlag": 1,
                    "autoRenewFlag": 0,
                    "deadline": "2016-10-11 12:58:28",
                    "modTimeStamp": "2016-11-04 18:30:05",
                    "addTimeStamp": "2016-10-11 11:58:28",
                    "dealId": "86216464",
                    "payType": 1,
                    "uInstanceId": "cdbro-quaopawc",
                    "cdbMem": 4000,
                    "cdbVolume": 110,
                    "zoneId": 800001,
                    "cdbQps": 4400,
                    "typeName": "High IO",
                    "type": "CUSTOM",
                    "cdbInstanceId": "qcdbfbde368e4f3d549f5eeef81b411bb541",
                    "cdbInstanceName": "cdb_ro_46"
                }
            ],
            "masterCdbInstanceId": "cdb-c1nl9rpv"
        },
        {
            "groupId": 56,
            "groupName": "Rogroup_12561826",
            "cdbVersion": "5.6",
            "cdbType": "CUSTOM",
            "status": 1,
            "vip": "10.66.186.93",
            "vport": 3306,
            "vpcId": 0,
            "subnetId": 0,
            "addTimeStamp": "2016-11-04 18:25:30",
            "modTimeStamp": "2016-11-04 18:25:31",
            "roList": [
                {
                    "groupId": 56,
                    "status": 1,
                    "cdbVersion": "5.6",
                    "cdbType": "CUSTOM",
                    "taskStatus": 0,
                    "initFlag": 1,
                    "autoRenewFlag": 0,
                    "deadline": "2016-11-04 19:25:30",
                    "modTimeStamp": "2016-11-04 18:26:32",
                    "addTimeStamp": "2016-11-04 18:25:30",
                    "dealId": "12561826",
                    "payType": 1,
                    "uInstanceId": "cdbro-oio5hxy8",
                    "cdbMem": 4000,
                    "cdbVolume": 100,
                    "zoneId": 800001,
                    "cdbQps": 4400,
                    "typeName": "High IO",
                    "type": "CUSTOM",
                    "cdbInstanceId": "qcdb521128295126d5f62d88322e92eb0436",
                    "cdbInstanceName": "cdb_ro_56"
                }
            ],
            "masterCdbInstanceId": "cdb-c1nl9rpv"
        }
    ]
}
```


