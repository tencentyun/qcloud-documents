## 1. API Description
This API (CreateCdbDataMigrationTask) is used to create a data migration task.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>

1. After creating a data migration task via the API, you need to use API [Verify Data Migration Task](/document/product/236/7726) to initiate a verification to verify whether the source MySQL and the destination instance meet the migration conditions.
2. After initiating the verification, you can use API [Query Data Migration Task List](/document/product/236/7461) to query the real-time verification result.
3. If the verification succeeds, you can use API [Start Data Migration Task](/document/product/236/7712) to start the migration task.
4. If the verification fails, you can use API [Modify Data Migration Task](/document/product/236/7725) to modify task parameters, and then return to Step 1 to initiate the task verification again.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CreateCdbDataMigrationTask, and the Region field for this API is the region value of the destination instance.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobName | Yes | String | Name of data migration task |
| runMode | Yes | Int | Run mode of task. Values include: 1 - immediate execution; 2 - scheduled execution |
| expectTime | No | String | Expected execution time. When the runMode = 2, the field is required. Format: yyyy-mm-dd hh: mm: ss|
| migrateType | Yes | Int |Data migration type. Values include: <br>1 - structural migration; <br>2 - full migration; <br>3 - full + incremental migration |
| type | Yes | Int | Task type. Values include: <br> 1 - source instance is self-built MySQL in public network; <br>2 - source instance is self-built MySQL in basic network; <br>3 - source instance is self-built MySQL in VPC ; <br>4 - Source instance is connected through Direct Connect; <br>5 - source instance is connected through Cloud VPN; <br>6 - source instance is connected through self-built VPN|
| srcInfo | Yes | Array | Source instance information depending on the migration task type|
| dstInfo | Yes | Array | Destination instance information. It only contains attribute cdbUInstanceId with a format of cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained via API [Query List of Instances](/doc/api/253/1266). Its value equals the uInstanceId field value in the output parameter. |

The composition of parameters type and srcInfo can be divided into six types, depending on the migration task type.

1) If the source instance is a self-built MySQL in public network, type = 1 and srcInfo is composed of the following parameters:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| mysqlIp | Yes | String | IP address of self-built MySQL instance in public network |
| mysqlPort | Yes | Int | Port of self-built MySQL instance in public network |
| mysqlUser | Yes | String | User name of self-built MySQL instance in public network |
| mysqlPwd | Yes | String | Password of self-built MySQL instance in public network |
| dbInfo | No | Array | Information on the source database table to be migrated. If you need to migrate the entire instance, this field can be left empty. The composition of each element is shown in the table below |
| IsOverrideRoot | Yes | Int | Whether to overwrite destination database with Root account of source database. Values include: 0 - Do not overwrite; 1 - overwrite. Default is 0 when the database table or structural migration is selected |

2) If the source instance is a self-built MySQL on CVM in basic network, type = 2 and srcInfo is composed of the following parameters: 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cvmUInstanceId | Yes | String | Short ID of CVM instance, such as: ins-olgl89y8. It is identical to the instance ID displayed in the CVM console page |
| mysqlIp | Yes | String | IP address of self-built MySQL instance on CVM |
| mysqlPort | Yes | Int | Port of self-built MySQL instance on CVM |
| mysqlUser | Yes | String | User name of self-built MySQL instance on CVM |
| mysqlPwd | Yes | String | Password of self-built MySQL instance on CVM |
| dbInfo | No | Array | Information on the source database table to be migrated. If you need to migrate the entire instance, this field can be left empty. The composition of each element is shown in the table below |
| IsOverrideRoot | Yes | Int | Whether to overwrite destination database with Root account of source database. Values include: 0 - Do not overwrite; 1 - overwrite. Default is 0 when the database table or structural migration is selected |

3)  If the source instance is a self-built MySQL on CVM in VPC, type = 3 and srcInfo is composed of the following parameters:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cvmUInstanceId | Yes | String | Short ID of CVM instance, such as: ins-olgl89y8. It is identical to the instance ID displayed in the CVM console page |
| vpcId | Yes | Int | VPC ID |
| subnetId | Yes | Int | ID of subnet in VPC |
| mysqlIp | Yes | String | IP address of self-built MySQL instance on CVM |
| mysqlPort | Yes | Int | Port of self-built MySQL instance on CVM |
| mysqlUser | Yes | String | User name of self-built MySQL instance on CVM |
| mysqlPwd | Yes | String | Password of self-built MySQL instance on CVM |
| dbInfo | No | Array | Information on the source database table to be migrated. If you need to migrate the entire instance, this field can be left empty. The composition of each element is shown in the table below |
| IsOverrideRoot | Yes | Int | Whether to overwrite destination database with Root account of source database. Values include: 0 - Do not overwrite; 1 - overwrite. Default is 0 when the database table or structural migration is selected |

4)  If the source instance is connected through Direct Connect, type = 4 and srcInfo is composed of the following parameters:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| uniqDcgId | Yes | String | Direct Connect gateway ID assigned by the system |
| vpcId | Yes | Int | VPC ID |
| subnetId | Yes | Int | ID of subnet in VPC |
| mysqlIp | Yes | String | IP address of self-built MySQL instance |
| mysqlPort | Yes | Int | Port of self-built MySQL instance |
| mysqlUser | Yes | String | User name of self-built MySQL instance |
| mysqlPwd | Yes | String | Password of self-built MySQL instance |
| dbInfo | No | Array | Information on the source database table to be migrated. If you need to migrate the entire instance, this field can be left empty. The composition of each element is shown in the table below |
| IsOverrideRoot | Yes | Int | Whether to overwrite destination database with Root account of source database. Values include: 0 - Do not overwrite; 1 - overwrite. Default is 0 when the database table or structural migration is selected |

5)  If the source instance is connected through Cloud VPN, type = 5 and srcInfo is composed of the following parameters:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| uniqVpnGwId | Yes | String | VPN gateway ID assigned by the system |
| vpcId | Yes | Int | VPC ID |
| subnetId | Yes | Int | ID of subnet in VPC |
| mysqlIp | Yes | String | IP address of self-built MySQL instance |
| mysqlPort | Yes | Int | Port of self-built MySQL instance |
| mysqlUser | Yes | String | User name of self-built MySQL instance |
| mysqlPwd | Yes | String | Password of self-built MySQL instance |
| dbInfo | No | Array | Information on the source database table to be migrated. If you need to migrate the entire instance, this field can be left empty. The composition of each element is shown in the table below |
| IsOverrideRoot | Yes | Int | Whether to overwrite destination database with Root account of source database. Values include: 0 - Do not overwrite; 1 - overwrite. Default is 0 when the database table or structural migration is selected |

6)  If the source instance is connected through self-built VPN, type = 6 and srcInfo is composed of the following parameters:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cvmUInstanceId | Yes | String | Short ID of CVM instance, such as: ins-olgl89y8. It is identical to the instance ID displayed in the CVM console page |
| vpnSelfBuildIP | Yes | String | IP address of self-built VPN gateway |
| vpcId | Yes | Int | VPC ID |
| subnetId | Yes | Int | ID of subnet in VPC |
| mysqlIp | Yes | String | IP address of self-built MySQL instance |
| mysqlPort | Yes | Int | Port of self-built MySQL instance |
| mysqlUser | Yes | String | User name of self-built MySQL instance |
| mysqlPwd | Yes | String | Password of self-built MySQL instance |
| dbInfo | No | Array | Information on the source database table to be migrated. If you need to migrate the entire instance, this field can be left empty. The composition of each element is shown in the table below |
| IsOverrideRoot | Yes | Int | Whether to overwrite destination database with Root account of source database. Values include: 0 - Do not overwrite; 1 - overwrite. Default is 0 when the database table or structural migration is selected |

Parameter dbInfo is used to specify the information on the database table to be migrated. Each element in the array is an Object, which is composed as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| database | Yes | String | Database name |
| table | No | Array | Name of the table under the current database. If you need to migrate all the tables of the current database, the field can be left empty |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Object | Task details |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobId | Int | ID of data migration task |

## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9013 | InternalError | System internal error |
| 9572 | InstanceNotExists | Instance does not exist |
| 30000 | InvalidParameter | Incorrect migration parameter |
| 30001 | InvalidParameter | Incorrect migration type |
| 30002 | InvalidParameter | Incorrect run mode of migration |
| 30004 | InvalidParameter | Incorrect parameter in source instance information |
| 30005 | InvalidParameter | Incorrect parameter in destination instance information |
| 30009 | InvalidParameter | Migration task does not exist |
| 30010 | OperationDenied | Migration task is in progress and is not allowed to be modified |
| 30011 | InvalidParameter | Incorrect CVM information |
| 30012 | OperationDenied | The availability zone does not support disaster recovery |
| 30013 | InvalidParameter | Incorrect region information of instance |
| 30016 | InvalidParameter | The operation is not allowed in the current migration status |
| 30016 | InvalidParameter | The operation is not allowed in the current migration status |

## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=CreateCdbDataMigrationTask
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&jobName=myJobName
&runMode=1
&type=2
&migrateType=3
&srcInfo.0.cvmUInstanceId=ins-olgl89y8
&srcInfo.0.mysqlIp=127.0.0.1
&srcInfo.0.mysqlPort=3306
&srcInfo.0.mysqlUser=root
&srcInfo.0.mysqlPwd=password
&srcInfo.0.dbInfo.0.database=myDB
&srcInfo.0.dbInfo.0.table.0=myTable0
&srcInfo.0.dbInfo.0.table.1=myTable1
&srcInfo.0.isOverrideRoot=1
&dstInfo.0.cdbUInstanceId=cdb-d2sagyed
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "jobId":206
    }
}
```
