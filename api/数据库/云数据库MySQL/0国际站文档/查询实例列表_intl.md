## 1. API Description
This API (DescribeCdbInstances) is used to query the list of instances in cloud database, and supports to filter the instances by project ID, instance ID, access address, instance status, etc.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>

1. It can use project ID, instance ID, access address and instance status as filtering conditions to query the list of instances.
2. If you do not specify any filter condition, 20 instance records will be returned by default. A maximum of 100 instance records will be returned for a single request;
3. It supports querying the list of master instances and disaster recovery instances, but does not support querying the list of read-only instances. You can use API [Query Read-only Instance List](/doc/api/253/6417) to query the list of read-only instances.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeCdbInstances.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| projectId | No | Int | Project ID. You can use API Query Project List to query the project ID |
| cdbInstanceIds.n | No | String | One or more instance IDs (n represents array subscript starting with 0). Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query Instance List](/doc/api/253/1266). Its value equals the uInstanceId field value in the output parameter.  |
| cdbInstanceVips.n | No | String | One or more instance access addresses (n represents array subscript starting with 0). Please use API [Query List of Instances](/doc/api/253/1266) to query the instance access addresses of cloud database.
| status.n | No | Int | Instance status. Default is 1. One or more status values (n represents array subscript starting with 0). The value includes: <br>0-Creating<br>1-Running<br>4-Deleting<br>5-Isolated |
| offset | No | Int | Record offset; default is 0 |
| limit | No | Int | Number of records returned for a single request; default is 20; maximum is 100 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| totalCount | Int | Number of instances that meet the condition |
| cdbInstanceSet | Array | Returned instance information |
Parameter cdbInstanceSet is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| uInstanceId | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be used to query or operate instances. <font style="color:red">Recommended to use</font> |
| cdbInstanceId | String | Instance UUID (deprecated). It is recommended to use uInstanceId instead. The instance UUID will only be generated after the instance is created. For the creating instance, it will only contain uInstanceId.  |
| initFlag | Int | Instance initialization mark. Possible returned values include: 0-Uninitialized; 1-Initialized | 
| cdbInstanceType | Int | Instance type. Possible returned values include: 1-Master instance; 2-Disaster recovery instance |
| storageSize | Int | Instance storage capacity, which is same as the field value of volume. It is recommended to use the volume field (in GB) | 
| maxQueryCount | Int | Maximum number of queries per second (times/second) | 
| cdbInstanceName | String | Instance name | 
| cdbInstanceVip | String | Instance access IP | 
| cdbInstanceVport | Int | Instance access port | 
| cdbWanStatus  | Int | Status of public network access. Possible returned values include: <br>0-Not Enabled<br>1-Enabled<br>2-Disabled<br>3-Processing |
| cdbWanDomain | String | Domain name of public network access |
| cdbWanPort | Int | Port of public network access |
| status | Int | Instance status. Possible returned values include: <br>0-Creating<br>1-Running<br>4-Deleting<br>5-Isolated<br>101-Locked | 
| taskStatus | Int | Instance task status. Possible returned values include: <br>0-No tasks<br>1-Upgrading<br>2-Importing Data<br>3-Opening Slave<br>4-Enabling Public Network Access<br>5-Performing Batch Operations<br>6-Rollback<br>7-Disabling Public Network Access<br>8-Modifying Password<br>9-Modifying Instance Name<br>10-Rebooting<br>12-Creating Migration<br>13-Deleting Database Table<br>14-Creating Disaster Recovery Instance Synchronization | 
| engineVersion | String | Version number of instance database engine. Possible returned values include: 5.1, 5.5, and 5.6 | 
| cdbInstanceCreateTime | String | Instance creation time. Format: yyyy-mm-dd hh: mm: ss | 
| cdbInstanceDeadlineTime | String | Expiry time of instance. If the instance is in pay by usage mode, then the field value is 0000-00-00 00:00:00. Format: yyyy-mm-dd hh:mm:ss | 
| cdbTypeSet | String | Number of instance type, which can be used to purchase the instance of same type or query the renewal price of the instance of same type | 
| cdbType | String | Instance specifications description. For example: CUSTOM. Please use API [Query Specifications of Creatable Instances](/doc/api/253/1333) to query the details of cdbType | 
| memory | Int | Capacity of instance memory (in MB) | 
| volume | Int | Capacity of instance disk (in GB) | 
| autoRenew | Int | Automatic renewal mark. Possible returned values include: 0 indicates that the instance is not automatically renewed; 1 indicates that the instance is automatically renewed | 
| zoneId | Int | Availability zone ID of the instance | 
| vpcId | Int | VPC ID of the instance. Please use [Query VPC List](/doc/api/245/1372) | 
| subnetId | Int | VPC subnet ID of the instance. Please use [Query VPC List](/doc/api/245/1372) | 
| projectId | Int | Project ID of the instance. You can use API [Query Project List](/document/product/378/4400) to obtain the project ID | 
| payType | Int | Billing type of instance. Possible returned values include: 0-Annual or Monthly Plan; 1-Pay by Usage; 2-Postpaid Billing on a Monthly Basis | 
| masterInfo | Array | Master instance information. If the instance is a disaster recovery instance or a read-only instance, the information of its master instance is returned, otherwise null is returned|
| roInfo | Array | Read-only instance information |
| drInfo | Array | Disaster recovery instance information |
| protectMode | Int | Data protection mode |
| slaveZoneFirst | Int | Availability zone ID of slave 1 |
| slaveZoneSecond | Int | Availability zone ID of slave 2. If there is no slave 2, the value is 0 |
| slaveSecondVip | String | IP of slave 2. If there is no slave 2, the value is 0 |
| slaveSecondVport | Int | Port of slave 2. If there is no slave 2, the value is 0 |
| deployMode | Int | Deployment mode. 0-Single Availability Zone, 1-Multiple Availability Zones |
| binlogSize | Int | Size of binlog (in GB) |

Parameter masterInfo is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| region | String | Region ID. For details, see [<a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>](/doc/api/229/6976) |
| zoneId | Int | Availability zone ID of the instance |
| uInstanceId | String | Instance ID. Unique ID of the instance. The function is the same as the cdbInstanceId field. <font style="color:red">Recommended to use</font> |
| status | Int | Instance status. Possible returned values include: <br>0-Creating<br>1-Running<br>4-Deleting<br>5-Isolated |

Parameter roInfo is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| region | String | Region ID. For details, see [<a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>](/doc/api/229/6976) |
| zoneId | Int | Availability zone ID of the instance |
| uInstanceId | String | Instance ID. Unique ID of the instance. The function is the same as the cdbInstanceId field. <font style="color:red">Recommended to use</font> |
| status | Int | Read-only instance status. Possible returned values include: <br>0-Creating<br>1-Running<br>4-Deleting<br>5-Isolated |

Parameter drInfo is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| region | String | Region ID. For details, see [<a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>](/doc/api/229/6976) |
| zoneId | Int | Availability zone ID of the instance |
| uInstanceId | String | Instance ID. Unique ID of the instance. The function is the same as the cdbInstanceId field. <font style="color:red">Recommended to use</font> |
| status | Int | Instance status. Possible returned values include: <br>0-Creating<br>1-Running<br>4-Deleting<br>5-Isolated |
| syncStatus | Int | Sync status. Possible returned values include: <br>0-Not Synchronized<br>1-Creating Synchronization<br>2-Created Synchronization<br>3-Synchronization Failed<br>4-Repairing Synchronization |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9013 | InternalError | System internal error |
| 9016 | InternalError | System internal error |
| 9544 | OperationDenied | Instance does not exist |
| 9572 | InstanceNotExists | Instance does not exist |
| 9593 | IncorrectInstanceStatus | Abnormal instance status |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=DescribeCdbInstances
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceIds.0=cdb-c1nl9rpv
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": "71",
    "cdbInstanceSet": [
        {
            "cdbInstanceId": "qcdba886a764b05a5f79be07a2ddbcdb85d5",
            "uInstanceId": "cdb-lnmynajd",
            "initFlag": 1,
            "cdbInstanceType": 1,
            "storageSize": 100,
            "maxQueryCount": 4400,
            "cdbInstanceName": "cdb129402",
            "cdbInstanceVip": "10.66.189.110",
            "cdbInstanceVport": 3306,
            "cdbWanStatus": 0,
            "cdbWanDomain": "",
            "cdbWanPort": 0,
            "status": 1,
            "taskStatus": 6,
            "engineVersion": "5.6",
            "cdbInstanceCreateTime": "2016-11-21 16:37:40",
            "cdbInstanceDeadlineTime": "0000-00-00 00:00:00",
            "cdbTypeSet": "4000000100",
            "cdbType": "CUSTOM",
            "memory": 4000,
            "volume": 100,
            "autoRenew": 0,
            "zoneId": 100003,
            "vpcId": 0,
            "subnetId": 0,
            "projectId": 0,
            "payType": 1,
            "roInfo": [
                {
                    "region": "gz",
                    "zoneId": 100003,
                    "uInstanceId": "cdbro-41ralnrf",
                    "status": 1
                },
                {
                    "region": "gz",
                    "zoneId": 100003,
                    "uInstanceId": "cdbro-d0q1umpp",
                    "status": 1
                }
            ],
            "drInfo": [],
            "masterInfo": null
        },
        {
            "cdbInstanceId": "qcdb45f66d70c5867d1619921638dd6871bf",
            "uInstanceId": "cdb-boljtt5g",
            "initFlag": 1,
            "cdbInstanceType": 1,
            "storageSize": 25,
            "maxQueryCount": 1000,
            "cdbInstanceName": "ivansqwu-test",
            "cdbInstanceVip": "10.66.187.51",
            "cdbInstanceVport": 3306,
            "cdbWanStatus": 0,
            "cdbWanDomain": "",
            "cdbWanPort": 0,
            "status": 1,
            "taskStatus": 0,
            "engineVersion": "5.6",
            "cdbInstanceCreateTime": "2016-11-15 16:22:28",
            "cdbInstanceDeadlineTime": "2017-01-15 16:20:35",
            "cdbTypeSet": "1000000025",
            "cdbType": "CUSTOM",
            "memory": 1000,
            "volume": 25,
            "autoRenew": 0,
            "zoneId": 100002,
            "vpcId": 0,
            "subnetId": 0,
            "projectId": 1005722,
            "payType": 0,
            "roInfo": [],
            "drInfo": [
                {
                    "region": "bj",
                    "zoneId": 800001,
                    "uInstanceId": "cdb-qsb71ep1",
                    "status": 1,
                    "syncStatus": 2
                }
            ],
            "masterInfo": null
        }
    ]
}
```


