## 1. API Description

This API (CreateScalingConfiguration) is used to create new scaling configurations. Domain for API request: scaling.api.qcloud.com

1) The specified CVM instance specification must be consistent with the instance specification of the active scaling configurations in the scaling group.

2) The scaling configuration cannot be edited or modified. If you want to use a new scaling configuration, you must recreate one.

3) When creating a scaling configuration, an image must be selected to determine the system disk configuration of the new created instance. The image contains the operating system and application software configuration. After the instance is created based on the image, the system disk of this instance is the full clone of the image.

4) When creating a scaling configuration, a security group must be specified. The number of instances in the same security group can not exceed 1000. Otherwise, if you specify the security group when creating an instance, a failure screen will appear.

5) When creating an instance, the system shall allocate a system disk of the corresponding size to the system based on the specified image.

6) The system disk type is the same as the data disk type.

7) A maximum of 20 scaling configurations can be created for each project. For more information, refer to [Service Limits]().

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](). The Action field for this API is CreateScalingConfiguration.

| Parameter Name           | Required | Type   | Description                                                  |
| ------------------------ | -------- | ------ | ------------------------------------------------------------ |
| scalingConfigurationName | Yes      | String | Scaling configuration name defined by the user.              |
| imageId                  | Yes      | String | Image ID. Please fill in the unImgId (unified ID of image) field returned by [Query Image]() (DescribeImages) API. |
| cpu                      | Yes      | Int    | The number of CPU cores, whose optional number may vary in different regions. For more information, refer to [CVM Instance Configuration](https://cloud.tencent.com/doc/product/213/2177). |
| mem                      | Yes      | Int    | The size of memory (in GB), whose optional size may vary in different regions. For more information, refer to [CVM Instance Configuration](https://cloud.tencent.com/doc/product/213/2177). |
| storageType              | Yes      | Int    | Data disk type. Only five values are available: 1 means local disk; 2 means cloud disk; 3 means local SSD; 5 means cloud SSD; 6 means premium cloud disk. |
| storageSize              | Yes      | Int    | Data disk size (GB). The increment is 10 GB. For local disks, the optional range is 0-500 G; for cloud disks, the optional range is 0-4000 G. The specific restrictions for details[Categories](/document/product/362/2353)|
| bandwidthType            | Yes      | String | Bandwidth type. Only two values are available: PayByHour indicating charge by bandwidth usage time and PayByTraffic indicating charge by traffic. If it is a bandwidth package user, the value of this parameter will be ignored. |
| bandwidth                | Yes      | Int    | Public network bandwidth (in Mbps). 0 means that public network bandwidth is not enabled. The upper limit of the bandwidth of different models is inconsistent. For details, see the [Public Network Bandwidth Limit](/document/product/213/12523). If it is a bandwidth package user, this parameter ranges from 0-200 or 65535. 65535 indicates that there is no upper limit for bandwidth. |
| imageType                | Yes      | Int    | Image type. Only three values are available: A value of 1 indicates that it is a private image; A value of 2 indicates that it is a public image. |
| rootSize                 | No       | Int    | Size of system disk (in GB). Default size for Linux is 50 GB, and the increment is 1 GB. Adjustment is not supported for Windows. The default size is 50 GB. |
| keyId                    | No       | String | ID of key. It can be queried by calling [Query Keys]() (DescribeKeyPairs) API. |
| password                 | No       | String | Instance password. It will be generated randomly if not set. Password rules for Linux host: which should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, $, %, ^, \, *, ()).  Password rules for Windows host: which should be a combination of 12-16 characters comprised of at least three of the following types: uppercase letters, lowercase letters, numbers, special characters (!, @, #, \, *).** Note: Key and password cannot both be specified at the same time.** |
| needMonitorAgent         | No       | Int    | Activate cloud monitor service or not. Only two values are available: 1: activated; 0: deactivated. Default is 1. |
| needSecurityAgent        | No       | Int    | Whether to activate cloud security service. Only two values are available: 1: activated; 0: deactivated. Default is 1. |
| wanIp                    | No       | Int    | Whether to activate the public IP. Only two values are available: 1: activated; 0: deactivated. Default is 1. |
| sgId                     | No       | String | Safety group ID. It can be queried by calling API [Query Security Group List ](). |
| projectId                | No       | String | Project ID. If not specified, 0 means default project. To specify other projects, you can call API [Query Project List]() (DescribeProject) to query. |
| dataSnapshotId           | No       | String | Data disk snapshot ID. If you want to use the data disk snapshot function, the data disk type (storageType) must be cloud disk, and the capacity of data disk snapshot must be less than that of the data disk (storageSize). |
| cvmType                  | No       | String | Select CVM type. Only seven values are available: 11 means Standard CVM; 12 means Standard CVM Series 2; 21 means High IO CVM; 22 means High IO CVM Series 2; 31 means Memory CVM.  32 means Memory CVM Series 2 42 means Calculation CVM. If not specified, the default of this field is 11 (Standard CVM). |
| userdata                 | No       | String | Base64-encoded User Data text, the length limit is 16KB.     |

Currently, the scaling configurations support three CVMs, including Standard CVM, High IO CVM and Memory CVM (subject to the actual available types in each region). For more information about the CPUs and memories sizes supported by scaling configurations, refer to [CVM Instance Configuration](https://cloud.tencent.com/doc/product/213/2177).

## 3. Output Parameters

| Parameter Name | Type   | Description                                                  |
| -------------- | ------ | ------------------------------------------------------------ |
| code           | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Code page. |
| codeDesc       | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message        | String | Module error message description depending on API.           |
| data           | Array  | Output results. It contains the scaling configuration list information that was created successfully. |

Parameter data is composed of only one element: scalingConfigurationIdSet.

| Parameter Name            | Type  | Description                            |
| ------------------------- | ----- | -------------------------------------- |
| scalingConfigurationIdSet | Array | Each scaling configuration ID created. |

## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

| Error Code                          | Description                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| QuotaExceeded.ScallingConfiguration | Scaling configurations to be added exceed the limit          |
| NameDuplicate.ScallingConfiguration | Scaling configuration name already exists                    |
| InvalidParameter.SecurityGroupId    | Security group ID is incorrect                               |
| IInvalidParameter.CbsNotMatchCpu    | 1C1G can only configure cloud disks                          |
| InvalidParameter.storageType        | Storage type error                                           |
| QuotaExceeded.storageSize           | Data disk size exceeds the range                             |
| QuotaExceeded.rootSize              | System disk size exceeds the range                           |
| OprationFail.CpuOrMemNotExsit       | The model for this cpu and mem are sold out or not available |

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingConfigurationName=configuration_test
&imageType=2
&imageId=img-50mr2ow7
&cpu=1
&mem=2
&storageType=6
&storageSize=100
&bandwidthType=PayByTraffic
&bandwidth=1
&projectId=0
&cvmType=12
```

Example of returned result is as below:

```

{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
    "data":{
        "scalingConfigurationIdSet":[
            "asc-4jwggk1l"
        ]
    }
}
```
