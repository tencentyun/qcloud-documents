## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (UpgradeDBInstance) is used to upgrade database instances. Master instances, disaster recovery instances and read-only instances can be upgraded via this API.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: UpgradeDBInstance |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv or cdbro-c1nl9rpv. It is identical to the instance ID displayed in the database console page and can be obtained using API [Query Instance List](https://cloud.tencent.com/document/api/236/15872). Its value equals the InstanceId field value in the output parameters. |
| Memory | Yes | Integer | Memory size after upgrade (in MB). To ensure the validity of the passed Memory value, you can use API [Query Supported Specifications (supporting custom availability zones and configurations)](https://cloud.tencent.com/document/api/253/6109) to acquire the available memory specifications. |
| Volume | Yes | Integer | Disk size after upgrade (in GB). To ensure the validity of the passed Volume value, you can use API [Query Supported Specifications (supporting custom availability zones and configurations)](https://cloud.tencent.com/document/api/253/6109) to acquire the available disk size ranges. |
| ProtectMode | No | Integer | Data replication mode. Supported values include: 0 - Async replication; 1 - Semisync replication; 2 - Strongsync replication. This parameter can be specified when you upgrade master instances, but it should be ignored when you upgrade read-only instances or disaster recovery instances. |
| DeployMode | No | Integer | Deployment mode. Default is 0. Supported values include: 0 - Single availability zone, 1 - Multiple availability zones. This parameter can be specified when you upgrade master instances, but it should be ignored when you upgrade read-only instances or disaster recovery instances. |
| SlaveZone | No | String | Availability zone information of slave 1. Default is the "Zone" of the instance. This parameter can be specified when you upgrade master instances, but it should be ignored when you upgrade read-only instances or disaster recovery instances. You can query supported availability zones using the API<a href='/document/product/236/6921' title='Query supported availability zones'>Query Supported Database Specifications</a>. |
| EngineVersion | No | String | Version of the master instance database engine. Supported values: 5.5, 5.6 and 5.7. |
| WaitSwitch | No | Integer | The method of switching to the new instance. Default is 0. This parameter can be specified when you upgrade master instances, but it should be ignored when you upgrade read-only instances or disaster recovery instances. Supported values: 0 - Switch now; 1 - Switch during certain time window. If 1 is passed, the switch will be performed in a time window during the upgrade. You can also call the API [Switch to New Instance](https://cloud.tencent.com/document/api/403/4392) to initiate the switch. |
| BackupZone | No | String | Availability zone ID of slave 2. Default is 0. This parameter can be specified when you upgrade master instances, but it should be ignored when you upgrade read-only instances or disaster recovery instances. |
| InstanceRole | No | String | Instance type. Default is master. Supported values include: master - master instance, dr - disaster recovery instance, and ro - read-only instance. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DealIds | Array of String | Order ID, which is used to call Cloud APIs, such as [Acquire Order Information](https://cloud.tencent.com/document/api/403/4392)|.
| AsyncRequestId | String | ID of an async task request, which can be used to query the execution result of an async task. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.DatabaseAccessError | Database's internal error. |
| InternalError.TradeError | Internal error with trading system. |
| InvalidParameter | Parameter error. |

## 5. Example

### Example 1 Upgrade a database instance

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=UpgradeDBInstance
&InstanceId=cdb-6si6qy6p
&Memory=1000
&Volume=50
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "AsyncRequestId": "a6040589-3b098df5-b551d9e5-81c6bfdc",
    "DealIds": [
      "20171204110077"
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
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
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

