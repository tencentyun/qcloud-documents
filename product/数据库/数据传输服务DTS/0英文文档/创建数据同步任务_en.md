## 1. API Description
This API (CreateCdbDataSyncTask) is used to create a data synchronization task in the region where the master instance resides in.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>

1. After creating a data synchronization task via the API, you need to use API [Verify Data synchronization Task](/document/product/236/7931) to initiate a verification to verify whether the source MySQL and the destination instance meet the synchronization conditions.
2. After initiating the verification, you can use API [Query List of Data synchronization Tasks](/document/product/236/7933) to query the real-time verification result.
3. If the verification succeeds, you can use API [Start Data synchronization Task](/document/product/236/7930) to start the synchronization task.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field of this API is CreateCdbDataSyncTask, and the Region field of this API is the region value of the source instance (master instance).

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| jobName | Yes | String | Name of data synchronization task |
| srcInfo | Yes | Array | Source MySQL instance (master instance) information |
| dstInfo | Yes | Array | Destination MySQL instance (disaster recovery instance) information |

Parameter srcInfo is composed of the following parameters:

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbUInstanceId | Yes | String | Master instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266) API. Its value equals to the uInstanceId field value in the output parameter. |
| dbInfo | Yes | Array | Information on the source database table to be synchronized. If you need to synchronize the entire instance, this field can be left empty. The composition of each element is shown in the table below |
| isOverrideRoot | Yes | Int | Whether to overwrite destination database with Root account of source database. Values include: 0 - Do not overwrite; 1 - overwrite. Default is 0 when the database table is selected |

dbInfo is used to specify the information on the database table to be synchronized. Each element in the array is an Object, which is composed as follows:

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| database | Yes | String | Database name |
| table | No | Array | Name of the table under the current database. If you need to synchronize all the tables of the current database, this field can be left empty |

Parameter dstInfo is composed of the following parameters:

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbUInstanceId | Yes | String | Disaster recovery instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the value of the field uInstanceId in the output parameter. |
| region | Yes | String | Region ID of a disaster recovery instance, refer to [<a href='/document/product/236/6921' title='Common Request Parameters'> Common Request Parameters</a>](/doc/api/229/6976). |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Object | Task details |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobId | Int | ID of a data synchronization task |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9013 | InternalError | System internal error |
| 9572 | InstanceNotExists | Instance does not exist |
| 30000 | InvalidParameter | Incorrect synchronization parameter |
| 30001 | InvalidParameter | Incorrect synchronization type |
| 30002 | InvalidParameter | Incorrect run mode of synchronization |
| 30004 | InvalidParameter | Incorrect parameter in source instance information |
| 30005 | InvalidParameter | Incorrect parameter in destination instance information |
| 30009 | InvalidParameter | Synchronization task does not exist |
| 30010 | OperationDenied | Synchronization task is in progress and is not allowed to be modified |
| 30011 | InvalidParameter | Incorrect CVM information |
| 30012 | OperationDenied | The availability zone does not support disaster recovery |
| 30013 | InvalidParameter | Incorrect region information of instance |
| 30016 | InvalidParameter | The operation is not allowed in the current synchronization status |
| 30016 | InvalidParameter | The operation is not allowed in the current synchronization status |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=CreateCdbDataSyncTask
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&jobName=myJobName
&srcInfo.0.cdbUInstanceId=cdb-c1nl9rpv
&srcInfo.0.dbInfo.0.database=myDB
&srcInfo.0.dbInfo.0.table.0=myTable0
&srcInfo.0.dbInfo.0.table.1=myTable1
&srcInfo.0.isOverrideRoot=0
&dstInfo.0.cdbUInstanceId=cdb-d2sagyed
&dstInfo.0.regionId=sh
&dstInfo.0.zoneId=200001
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


