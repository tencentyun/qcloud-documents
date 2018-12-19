## 1. API Description

Domain name for API request: dts.tencentcloudapi.com

This API is used to query a data migration task.
For Finance Zone linkage, please use this domain name: https://dts.ap-shenzhen-fsi.tencentcloudapi.com

A maximum of 50 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: dts.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/571/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeMigrateJobs |
| Version | Yes |  String | Common parameter. The value used for this API: 2018-03-30 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/571/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| JobId | No | String | ID of a data migration task |
| JobName | No | String | Name of a data migration task |
| Order | No | String | Sorting field, which can be JobId, Status, JobName, MigrateType, RunMode, or CreateTime. |
| OrderSeq | No | String | Sorting method. ASC indicates an ascending order, and DESC indicates a descending order. |
| Offset | No | Integer | Offset. Default is 0. |
| Limit | No | Integer | Number of returned instances. Default is 20, and valid value is between 1 and 100 (inclusive) |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of tasks |
| JobList | Array of [MigrateJobInfo](/document/api/571/##MigrateJobInfo) | Array of task details |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/571/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| FailedOperation.NotAllowOperation | Prohibits the operation. |
| InternalError.DatabaseError | Access to the database on the migration platform failed. |
| InternalError.ProtocolError | Communication protocol error. |
| InvalidParameter | Parameter error |

## 5. Example

### Example 1 Query a data migration task

#### Input example

```
https://dts.tencentcloudapi.com/?Action=DescribeMigrateJobs
&Order=CreateTime
&OrderSeq=DESC
&Offset=0
&Limit=2
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "JobList": [
      {
        "CreateTime": "2018-05-24 15:06:03",
        "DatabaseInfo": [],
        "Detail": {
          "CurrentStepProgress": "0",
          "MasterSlaveDistance": 0,
          "Progress": "0",
          "SecondsBehindMaster": 0,
          "StepAll": 0,
          "StepInfo": [],
          "StepNow": 0
        },
        "DstAccessType": "cdb",
        "DstDatabaseType": "mysql",
        "DstInfo": {
          "InstanceId": "cdb-l78e0nbv",
          "Ip": "",
          "Port": 0,
          "ReadOnly": 0,
          "Region": "ap-shanghai"
        },
        "EndTime": "0000-00-00 00:00:00",
        "JobId": "dts-1kl0iy0v",
        "JobName": "userdts",
        "MigrateOption": {
          "ConsistencyParams": {
            "SelectRowsPerTable": 0,
            "TablesSelectAll": 0,
            "TablesSelectCount": 0
          },
          "ConsistencyType": 5,
          "ExpectTime": "0000-00-00 00:00:00",
          "ExternParams": "[]",
          "IsOverrideRoot": 0,
          "MigrateObject": 2,
          "MigrateType": 2,
          "RunMode": 1
        },
        "SrcAccessType": "extranet",
        "SrcDatabaseType": "mysql",
        "SrcInfo": {
          "AccessKey": "",
          "CvmInstanceId": "",
          "InstanceId": "",
          "Ip": "9.18.84.24",
          "Password": "",
          "Port": 10304,
          "RdsInstanceId": "",
          "Region": "ap-guangzhou",
          "SubnetId": "",
          "UniqDcgId": "",
          "UniqVpnGwId": "",
          "User": "root",
          "VpcId": ""
        },
        "StartTime": "0000-00-00 00:00:00",
        "Status": 1
      },
      {
        "CreateTime": "2018-05-23 11:49:44",
        "DatabaseInfo": [],
        "Detail": {
          "CurrentStepProgress": "",
          "MasterSlaveDistance": 0,
          "Progress": "0",
          "SecondsBehindMaster": 0,
          "StepAll": 0,
          "StepInfo": [],
          "StepNow": 0
        },
        "DstAccessType": "cdb",
        "DstDatabaseType": "mysql",
        "DstInfo": {
          "InstanceId": "cdb-m78e0nnv",
          "Ip": "",
          "Port": 0,
          "ReadOnly": 0,
          "Region": "ap-shanghai"
        },
        "EndTime": "0000-00-00 00:00:00",
        "JobId": "dts-dau5czmd",
        "JobName": "apitest",
        "MigrateOption": {
          "ConsistencyParams": {
            "SelectRowsPerTable": 0,
            "TablesSelectAll": 0,
            "TablesSelectCount": 0
          },
          "ConsistencyType": 5,
          "ExpectTime": "",
          "ExternParams": "[]",
          "IsOverrideRoot": 0,
          "MigrateObject": 2,
          "MigrateType": 2,
          "RunMode": 1
        },
        "SrcAccessType": "extranet",
        "SrcDatabaseType": "mysql",
        "SrcInfo": {
          "AccessKey": "",
          "CvmInstanceId": "",
          "InstanceId": "",
          "Ip": "9.18.81.3",
          "Password": "",
          "Port": 11401,
          "RdsInstanceId": "",
          "Region": "ap-guangzhou",
          "SubnetId": "",
          "UniqDcgId": "",
          "UniqVpnGwId": "",
          "User": "root",
          "VpcId": ""
        },
        "StartTime": "0000-00-00 00:00:00",
        "Status": 5
      }
    ],
    "RequestId": "c032aab5-b56a-428d-9cf7-e5f324ee408b",
    "TotalCount": 2
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

