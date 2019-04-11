## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeDBInstances) is used to query the list of database instances, and supports filtering instances by project ID, instance ID, access address, and instance status, etc.

1. If you do not specify any filter condition, 20 instance records will be returned by default. A maximum of 100 instance records will be returned for a single request.
2. Master instances, disaster recovery instances, and read-only instances can be queried via this API.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDBInstances |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| ProjectId | No | Integer | Project ID, which can be queried via API [Query Project List](https://cloud.tencent.com/document/product/378/4400). |
| InstanceTypes.N | No | Array of Integer | Instance type. Available values: 1 - Master instance; 2 - Disaster recovery instance; 3 - Read-only instance. |
| Vips.N | No | Array of String | Private IP of an instance |
| Status.N | No | Array of Integer | Instance status. Available values: 0 - Creating; 1 - Running; 4 - Isolating; 5 - Isolated |
| Offset | No | Integer | Record offset. Default is 0. |
| Limit | No | Integer | Number of results returned for a single request. Default is 20, and maximum is 2000. |
| SecurityGroupId | No | String | Security group ID |
| PayTypes.N | No | Array of Integer | Billing method. Available values: 0 - Prepaid; 1 - Billing on an hourly basis |
| InstanceNames.N | No | Array of String | Instance name |
| TaskStatus.N | No | Array of Integer | Instance task status. Available values: <br>0 - No task<br>1 - Upgrading<br>2 - Importing data<br>3 - Opening slave<br>4 - Enabling access over public network<br>5 - Performing batch operation<br>6 - Rolling back<br>7 - Disabling access over public network<br>8 - Modifying password<br>9 - Modifying instance name<br>10 - Restarting<br>12 - Under self-built migration<br>13 - Deleting database table<br>14 - Creating disaster recovery instance synchronization |
| EngineVersions.N | No | Array of String | Version of instance database engine. Available values: 5.1, 5.5, 5.6 and 5.7 |
| VpcIds.N | No | Array of Integer | VPC IDs |
| ZoneIds.N | No | Array of Integer | Availability zone IDs |
| SubnetIds.N | No | Array of Integer | Subnet IDs |
| CdbErrors.N | No | Array of Integer | Queries whether an instance is read-only |
| OrderBy | No | String | Sorting field. Available values: "InstanceId", "InstanceName", "CreateTime" and "DeadlineTime" |
| OrderDirection | No | String | Sorting order. Available values: "ASC" and "DESC" |
| WithSecurityGroup | No | Integer | Indicates whether to query security group information |
| WithExCluster | No | Integer | Indicates whether to query exclusive cluster information |
| ExClusterId | No | String | Exclusive cluster ID |
| InstanceIds.N | No | Array of String | Instance IDs |
| InitFlag | No | Integer | Initialization mark. Available values: 0 - Uninitialized; 1 - Initialized |
| WithDr | No | Integer | Indicates whether to query disaster recovery instances |
| WithRo | No | Integer | Indicates whether to query read-only instances |
| WithMaster | No | Integer | Indicates whether to query master instances |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances that meet the condition |
| Items | Array of [InstanceInfo](/document/api/236/##InstanceInfo) | Instance details |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| CdbError | Backend error or process error. |
| InternalError.DatabaseAccessError | Database's internal error. |
| InternalError.DesError | System's internal error. |
| InvalidParameter | Parameter error. |
| InvalidParameter.InstanceNotFound | The instance does not exist. |
| OperationDenied.WrongStatus | The backend task status is invalid. |

## 5. Example

### Example 1 Query the instance list

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeDBInstances
&InstanceIds.0=cdb-eb2w7dto
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Items": [
      {
        "AutoRenew": 0,
        "CdbError": 0,
        "CreateTime": "2017-04-20 21:58:50",
        "DeadlineTime": "2017-05-20 21:58:50",
        "DeployMode": 0,
        "DeviceType": "CUSTOM",
        "DrInfo": [
          {
            "InstanceId": "cdb-0e5e4aqi",
            "InstanceName": "cdb154861",
            "InstanceType": 2,
            "Region": "ap-guangzhou",
            "Status": 0,
            "SyncStatus": 0,
            "Zone": "ap-guangzhou-1"
          }
        ],
        "EngineVersion": "5.6",
        "InitFlag": 1,
        "InstanceId": "cdb-eb2w7dto",
        "InstanceName": "cdb154861_ok",
        "InstanceType": 1,
        "MasterInfo": null,
        "Memory": 4000,
        "PayType": 0,
        "ProjectId": 0,
        "ProtectMode": 0,
        "Region": "ap-guangzhou",
        "RoGroups": [
          {
            "CreateTime": "2017-04-20 21:58:50",
            "GroupName": "rg-1234",
            "IsKickOut": 1,
            "MaxDelay": 5,
            "MinCount": 2,
            "RoInstances": [
              {
                "InstanceId": "cdbro-22s95l84",
                "Region": "ap-guangzhou",
                "Status": 1,
                "Zone": "ap-guangzhou-2"
              }
            ],
            "UGroupId": "rg-1234",
            "UpdateTime": "2017-04-20 21:58:50",
            "Vip": "10.66.10.10",
            "Vport": 15558
          }
        ],
        "RoVipInfo": {
          "RoSubnetId": 0,
          "RoVip": "10.66.101.173",
          "RoVipStatus": 2,
          "RoVpcId": 0,
          "RoVport": 3306
        },
        "SlaveInfo": {
          "First": {
            "Region": "ap-guangzhou",
            "Vip": "",
            "Vport": 0,
            "Zone": "ap-guangzhou-2"
          },
          "Second": null
        },
        "Status": 1,
        "SubnetId": 0,
        "TaskStatus": 0,
        "Vip": "10.66.2.164",
        "Volume": 100,
        "VpcId": 0,
        "Vport": 3306,
        "WanDomain": "",
        "WanPort": 0,
        "WanStatus": 0,
        "Zone": "ap-guangzhou-2"
      }
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "TotalCount": 1
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

