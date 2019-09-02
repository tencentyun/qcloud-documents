## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (UpgradeDBInstanceEngineVersion) is used to upgrade the version of a database instance. Master instances, disaster recovery instances and read-only instances can be upgraded via this API.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: UpgradeDBInstanceEngineVersion |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv or cdbro-c1nl9rpv. It is identical to the instance ID displayed in the database console page and can be obtained using API [Query Instance List](https://cloud.tencent.com/document/api/236/15872). Its value equals the InstanceId field value in the output parameters. |
| EngineVersion | Yes | String | Version of the master instance database engine. Supported values: 5.6 and 5.7. |
| WaitSwitch | No | Integer | The method of switching to the new instance. Default is 0. This parameter can be specified when you upgrade master instances, but it should be ignored when you upgrade read-only instances or disaster recovery instances. Supported values: 0 - Switch now; 1 - Switch during certain time window. If 1 is passed, the switch will be performed in a time window during the upgrade. You can also call the API [Switch to New Instance](https://cloud.tencent.com/document/api/403/4392) to initiate the switch. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| AsyncRequestId | String | Asynchronous task ID. You can query the execution status of the task using the API [Query task list](https://cloud.tencent.com/document/api/236/8010). |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.DatabaseAccessError | Database's internal error. |
| InternalError.TradeError | Internal error with trading system. |
| InvalidParameter | Parameter error. |
| InvalidParameter.InstanceNotFound | The instance does not exist. |

## 5. Example

### Example 1 Upgrade the version of a database instance

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=UpgradeDBInstanceEngineVersion
&InstanceId=cdb-8qrg9t04
&EngineVersion=5.7
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "AsyncRequestId": "d2baf2fb-cbae62df-7dd0d736-9cbd3e31",
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

