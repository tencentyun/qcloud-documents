## API Description
This API (CreateCdbDataSyncTask) is used to create a data synchronization task in the region where the master instance resides.
Domain name for API request: <font style='color:red'>cdb.api.qcloud.com</font>

1. After creating a data synchronization task using this API, use the API [Verify Data Synchronization Task](/document/product/236/7931) to initiate a verification to verify whether the source and the destination MySQL instances meet the synchronization conditions.
2. After initiating the verification, use the API [Query Data Synchronization Task List](/document/product/236/7933) to query the real-time verification result.
3. If the verification succeeds, use the API [Start Data Synchronization Task](/document/product/236/7930) to start the synchronization task.

## Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters>Common Request Parameters</a> page. The Action field of this API is CreateCdbDataSyncTask, and the Region field of this API is the region value of the source instance (master instance).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobName | Yes | String | Name of data synchronization task |
| srcInfo | Yes | Array | Source MySQL instance (master instance) information |
| dstInfo | Yes | Array | Destination MySQL instance (disaster recovery instance) information |

Parameter srcInfo is composed as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbUInstanceId | Yes | String | Master instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained via the API [Query Instance List](/doc/api/253/1266). Its value equals uInstanceId field value in the output parameters. |
| dbInfo | Yes | Array | Information on the source database table to be synchronized. If you need to synchronize the entire instance, this field can be left empty. Each element is composed as shown in the table below. |
| isOverrideRoot | Yes | Int | Whether to overwrite the Root account of destination database with that of source database. Values include: 0 - Do not overwrite; 1 - Overwrite. Default is 0 when the database table is selected. |

Parameter dbInfo is used to specify the information on the database table to be synchronized. Each element in the array is an Object and is composed as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| database | Yes | String | Database name |
| table | No | Array | Name of the table under the current database. If you need to synchronize all the tables of the current database, this field can be left empty. |

Parameter dstInfo is composed as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbUInstanceId | Yes | String | Disaster recovery instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained via the API [Query Instance List](/doc/api/253/1266). Its value equals uInstanceId field value in the output parameters. |
| region | Yes | String | Region ID of disaster recovery instance. For more information, please see [<a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>](/doc/api/229/6976). |


## Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Object | Task details |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobId | Int | ID of data synchronization task |


## Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Invalid parameter |
| 9013 | InternalError | System internal error |
| 9572 | InstanceNotExists | Instance does not exist |
| 30000 | InvalidParameter | Invalid synchronization parameter |
| 30001 | InvalidParameter | Invalid synchronization type |
| 30002 | InvalidParameter | Invalid run mode of synchronization |
| 30004 | InvalidParameter | Invalid parameter in source instance information |
| 30005 | InvalidParameter | Invalid parameter in destination instance information |
| 30009 | InvalidParameter | Synchronization task does not exist |
| 30010 | OperationDenied | Synchronization task is in progress and cannot be modified |
| 30011 | InvalidParameter | Invalid CVM information |
| 30012 | OperationDenied | The availability zone does not support disaster recovery |
| 30013 | InvalidParameter | Invalid region of instance |
| 30016 | InvalidParameter | The operation is not allowed in the current synchronization status |
| 30016 | InvalidParameter | The operation is not allowed in the current synchronization status |


## Example
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


