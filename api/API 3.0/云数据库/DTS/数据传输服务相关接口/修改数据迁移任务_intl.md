## 1. API Description

Domain name for API request: dts.tencentcloudapi.com

This API is used to modify a data migration task. 
This API can be called when the migration task is in the following statuses: Creating a migration task; Created; Verification successful; Verification failed; Migration failed. 
The types of both source and destination instances as well as the region of destination instance cannot be modified.

For Finance Zone linkage, please use this domain name: dts.ap-shenzhen-fsi.tencentcloudapi.com

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: dts.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/571/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyMigrateJob |
| Version | Yes |  String | Common parameter. The value used for this API: 2018-03-30 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/571/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| JobId | Yes | String | ID of a data migration task to be modified |
| JobName | No | String | Name of a data migration task |
| MigrateOption | No | [MigrateOption](/document/api/571/##MigrateOption) | Migration task configuration options |
| SrcAccessType | No | String | Connection type of the source instance: extranet (a public network instance), cvm (a self-built CVM instance), dcg (an instance connected via Direct Connect), vpncloud (an instance connected via Tencent Cloud VPN), vpnselfbuild (an instance connected via self-built VPN), or cdb (a CDB instance) |
| SrcInfo | No | [SrcInfo](/document/api/571/##SrcInfo) | Source instance information depending on the migration task type |
| DstAccessType | String | Connection type of the destination instance: extranet (a public network instance), cvm (a self-built CVM instance), dcg (an instance connected via Direct Connect), vpncloud (an instance connected via Tencent Cloud VPN), vpnselfbuild (an instance connected via self-built VPN), or cdb (a CDB instance). Only CDB is supported. |
| DstInfo | No | [DstInfo](/document/api/571/##DstInfo) | Information on the destination instance. The region cannot be modified. |
| DatabaseInfo | No | String | When migrating 'a specified database table', you need to set the information of the source database table to be migrated, which should be described as a JSON array of strings, as shown below.<br/><br/> For two-level structure "database-table":<br/>[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]<br/>For three-level structure "database-schema-table":<br/>[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]<br/><br/>This field is ignored for the migration of "the entire instance". |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/571/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| FailedOperation.NotAllowOperation | Prohibits the operation. |
| InternalError.DatabaseError | Access to the database on the migration platform failed. |
| InternalError.DuplicateJob | Migration task conflict. |
| InternalError.ProtocolError | Communication protocol error. |
| InvalidParameter | Parameter error |
| ResourceNotFound.JobNotExist | The migration task does not exist. |

## 5. Example

### Example 1 Modify a data migration task

#### Input example

```
https://dts.tencentcloudapi.com/?Action==ModifyMigrateJob
&JobId=dts-1kl0iy0v
&JobName=userdts
&DatabaseInfo=[{"Database":"test","Table":["user","log"]}]
&MigrateOption.RunMode=1
&MigrateOption.MigrateType=2
&MigrateOption.MigrateObject=2
&MigrateOption.ConsistencyType=5
&MigrateOption.IsOverrideRoot=0
&DstInfo.ReadOnly=0
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "27ef2b7c-a786-48b4-9404-2f9baf3f4916"
  }
}
```


## 6. Other Resources

Cloud API 3.0 comes with the following development tools to make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

