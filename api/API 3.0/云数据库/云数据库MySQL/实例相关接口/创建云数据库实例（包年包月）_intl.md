## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (CreateDBInstance) is used to create prepaid database instances (including master instances, disaster recovery instances and read-only instances) by passing such information as instance specification, MySQL version number, purchased usage period and quantity.

You can also query instance details using the API [Query Instance List](https://cloud.tencent.com/document/api/236/15872).

1. Please first use the API [Query Supported Database Specifications](https://cloud.tencent.com/document/api/236/17229) to query the supported specifications, and then use the API [Query Price (Prepaid)](https://cloud.tencent.com/document/api/236/1332) to query the price of supported instances.

2. A maximum of 100 instances can be created at one time with a maximum validity period of 36 months.

3. MySQL 5.5, 5.6 and 5.7 versions are supported.

4. Master instances, read-only instances, and disaster recovery instances can be created via this API.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateDBInstance |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Memory | Yes | Integer | Instance memory size (in MB). You can obtain supported memory specifications using the API [Query Supported Database Specifications](https://cloud.tencent.com/document/api/236/17229). |
| Volume | Yes | Integer | Instance disk size (in GB). You can obtain supported disk size ranges using the API [Query Supported Database Specifications](https://cloud.tencent.com/document/api/236/17229). |
| Period | Yes | Integer | Instance validity period (in month). Supported values: [1,2,3,4,5,6,7,8,9,10,11,12,24,36] |
| GoodsNum | Yes | Integer | Number of instances. Default is 1, minimum is 1, and maximum is 100. |
| Zone | No | String | Availability zone information. If this is left empty, an availability zone will be selected automatically. You can obtain supported availability zones using the API [Query Supported Database Specifications](https://cloud.tencent.com/document/api/236/17229). |
| UniqVpcId | No | String | VPC ID. If this is left empty, the default is basic network. You can obtain the VPC ID using the API [Query VPC List](/document/api/215/15778). |
| UniqSubnetId | No | String | Subnet ID under a VPC. If UniqVpcId is set, UniqSubnetId is required. You can obtain the subnet ID using the API [Query Subnet List](/document/api/215/15784). |
| ProjectId | No | Integer | Project ID. If this is left empty, default project is used. You can obtain the project ID using the API [Query Project List](https://cloud.tencent.com/document/product/378/4400). |
| Port | No | Integer | Custom port. Supported value range: [1024-65535] |
| InstanceRole | No | String | Instance type. Default is master. Supported values include: master - master instance, dr - disaster recovery instance, and ro - read-only instance. |
| MasterInstanceId | No | String | Instance ID, which is required when you purchase read-only instances. This field indicates the master instance ID of read-only instances. You can query the database instance ID using the API [Query Instance List](https://cloud.tencent.com/document/api/236/15872). |
| EngineVersion | No | String | MySQL version. Values include: 5.5, 5.6 and 5.7. You can obtain supported instance versions using the API [Query Supported Database Specifications](https://cloud.tencent.com/document/api/236/17229). |
| Password | No | String | Password of root account, which should be a combination of 8-64 characters comprised of at least two of the following types: letters, numbers, and special characters (_, +, -, &, =, !, @, #, $, %, ^, *, ()). This parameter can be specified when you purchase master instances, but it should be ignored when you purchase read-only instances or disaster recovery instances. |
| ProtectMode | No | Integer | Data replication mode. Default is 0. Supported values: 0 - Async replication; 1 - Semisync replication; 2 - Strongsync replication |
| DeployMode | No | Integer | Multiple availability zones. Default is 0. Supported values include: 0 - single availability zone, 1 - multiple availability zones |
| SlaveZone | No | String | Availability zone information of slave 1. Default is the value of "zone" |
| ParamList.N | No | Array of [ParamInfo](/document/api/236/##ParamInfo) | Parameter list. Format: ParamList.0.Name=auto_increment&ParamList.0.Value=1. You can query supported parameters using the API [Query Parameter List](/document/product/236/6369). |
| BackupZone | No | String | Availability zone ID of slave 2. Default is 0. This parameter can be specified when you purchase master instances, but it should be ignored when you purchase read-only instances or disaster recovery instances. |
| AutoRenewFlag | No | Integer | Auto renewal flag. Supported values: 0- Disable auto renewal; 1- Enable auto renewal |
| MasterRegion | No | String | Region information of the master instance, which is required when you purchase disaster recovery instances |
| SecurityGroup.N | No | Array of String | Security group parameter |
| RoGroup | No | [RoGroup](/document/api/236/##RoGroup) | Read-only instance parameter |
| InstanceName | No | String | Instance name |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DealIds | Array of String | Order ID, which is used to call Cloud APIs, such as [Acquire Order Information](https://cloud.tencent.com/document/api/403/4392)|. |
| InstanceIds | Array of String | Instance ID list |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.DatabaseAccessError | Database's internal error. |
| InternalError.DfwError | Security group operation error. |
| InternalError.TradeError | Internal error with trading system. |
| InternalError.VpcError | VPC or subnet error. |
| InvalidParameter | Parameter error. |
| OperationDenied.ActionNotSupport | Unsupported operation. |
| OperationDenied.WrongPassword | Incorrect password or verification failed. |

## 5. Example

### Example 1 Purchase a master instance

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=CreateDBInstance
&Memory=1000
&Volume=25
&Period=1
&GoodsNum=1
&Zone=ap-guangzhou-3
&UniqVpcId=vpc-0akbol5v
&UniqSubnetId=subnet-fyrtjbqw
&ProjectId=0
&InstanceRole=master
&EngineVersion=5.6
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "DealIds": [
      "20171201110011"
    ],
    "InstanceIds": [
      "cdb-pn6gd5jp"
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
  }
}
```

### Example 2 Purchase a read-only instance

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=CreateDBInstance
&MasterInstanceId=cdb-fn3f9xpx
&Period=1
&GoodsNum=1
&Memory=4000
&Volume=100
&InstanceRole=ro
&RoGroup.roGroupMode=allinone
&RoGroup.roGroupName=jersey_test
&RoGroup.roOfflineDelay=1
&RoGroup.roMaxDelayTime=5
&RoGroup.minRoInGroup=1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "DealIds": [
      "20171205110051"
    ],
    "InstanceIds": [
      "cdbro-hlpl4ik9"
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

