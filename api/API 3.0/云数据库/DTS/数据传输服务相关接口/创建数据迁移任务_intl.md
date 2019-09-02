## 1. API Description

Domain name for API request: dts.tencentcloudapi.com

This API is used to create a data migration task.

For Finance Zone linkage, please use this domain name: dts.ap-shenzhen-fsi.tencentcloudapi.com

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: dts.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/571/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateMigrateJob |
| Version | Yes |  String | Common parameter. The value used for this API: 2018-03-30 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/571/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| JobName | Yes | String | Name of a data migration task |
| MigrateOption | Yes | [MigrateOption](/document/api/571/##MigrateOption) | Migration task configuration options |
| SrcDatabaseType | Yes | String | Database type of the source instance: mysql, redis, or mongodb |
| SrcAccessType | Yes | String | Connection type of the source instance: extranet (a public network instance), cvm (a self-built CVM instance), dcg (an instance connected via Direct Connect), vpncloud (an instance connected via Tencent Cloud VPN), vpnselfbuild (an instance connected via self-built VPN), or cdb (a CDB instance) |
| SrcInfo | Yes | [SrcInfo](/document/api/571/##SrcInfo) | Source instance information depending on the migration task type |
| DstDatabaseType | Yes | String | Database type of the destination instance: mysql, redis, or mongodb |
| DstAccessType | Yes | String | Connection type of the destination instance: extranet (a public network instance), cvm (a self-built CVM instance), dcg (an instance connected via Direct Connect), vpncloud (an instance connected via Tencent Cloud VPN), vpnselfbuild (an instance connected via self-built VPN), or cdb (a CDB instance). Only CDB is supported. |
| DstInfo | Yes | [DstInfo](/document/api/571/##DstInfo) | Information on the destination instance |
| DatabaseInfo | No | String | Information on the source database table to be migrated, which should be described as a JSON array of strings.<br/> For two-level structure "database-table":<br/>[{Database:db1,Table:[table1,table2]},{Database:db2}]<br/>For three-level structure "database-schema-table":<br/>[{Database:db1,Schema:s1<br/>Table:[table1,table2]},{Database:db1,Schema:s2<br/>Table:[table1,table2]},{Database:db2,Schema:s1<br/>Table:[table1,table2]},{Database:db3},{Database:db4<br/>Schema:s1}] |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| JobId | String | ID of a data migration task |
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
| LimitExceeded.MaxUnusedJobs | The number of idle migration tasks exceeds the limit. |

## 5. Example

### Example 1 Create a data migration task

#### Input example

```
https://dts.tencentcloudapi.com/?Action=CreateMigrateJob
&JobName=usertest
&SrcDatabaseType=mysql
&SrcAccessType=extranet
&DstDatabaseType=mysql
&DstAccessType=cdb
&MigrateOption.RunMode=1
&MigrateOption.MigrateType=1
&MigrateOption.MigrateObject=1
&MigrateOption.ConsistencyType=1
&MigrateOption.IsOverrideRoot=0
&SrcInfo.Ip=14.17.22.36
&SrcInfo.Port=10301
&SrcInfo.User=root
&SrcInfo.Supplier=others
&SrcInfo.Password=123456
&SrcInfo.Region=ap-guangzhou
&DstInfo.InstanceId=cdb-e78e0nnv
&DstInfo.Region=ap-shanghai
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "JobId": "dts-1kl0iy0v",
    "RequestId": "2201c42a-714f-4faa-915b-a51cc09f5cec"
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

