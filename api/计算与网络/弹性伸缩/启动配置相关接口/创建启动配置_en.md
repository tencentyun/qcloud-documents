## 1. API Description
This API (CreateScalingConfiguration) is used to create launch configurations.
Domain name for API request: scaling.api.qcloud.com

1) The CVM instance specification specified in the launch configuration must be consistent with the instance specification of the active launch configurations in the scaling group.

2) The launch configuration cannot be edited or modified. If you want to use a new launch configuration, you must create one.

3) When you create a launch configuration, an image must be selected to determine the system disk configuration for the instance to be created. The image contains the operating system and application software configuration. After the instance is created based on the image, the system disk of this instance is the full clone of the image.

4) When you create a launch configuration, a security group must be specified. The number of instances in the same security group cannot exceed 1,000. Otherwise, if you specify the security group when creating an instance, a failure screen will appear.

5) When an instance is created, the system assigns a system disk of an appropriate size to the system based on the specified image.

6) The system disk type is the same as the data disk type.

7) A maximum of 20 launch configurations can be created for each project. For more information, please see <a href="/doc/product/377/3120" title="Use Limits">Use Limits</a>.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateScalingConfiguration.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| scalingConfigurationName | Yes | String | Launch configuration name defined by the user. |
| imageId | Yes | String | Image ID. Please fill in the unImgId (unified ID of image) field returned by the <a href="/doc/api/229/查询可用的镜像列表" title="/doc/api/229/查询可用的镜像列表">Query Available Image List</a> (DescribeImages) API. |
| cpu | Yes | Int | Number of CPU cores, which may vary in different regions. For more information, please see [CVM Instance Configuration](https://cloud.tencent.com/doc/product/213/2177).
| mem | Yes | Int | Memory size (in GB), which may vary in different regions. For more information, please see [CVM Instance Configuration](https://cloud.tencent.com/doc/product/213/2177).
| storageType | Yes | Int | Type of data disk. Only three values are available: 1 means local disk; 2 means cloud disk; 3 means local SSD; 5 means cloud SSD. |
| storageSize | Yes | Int | Data disk size (GB). The increment is 10 GB. For local disks, the available range is 0-500 G; for cloud disks, the available range is 0-4,000 G. |
| bandwidthType | Yes | String | Bandwidth type. Only two values are available: PayByHour: Bill by bandwidth usage time; PayByTraffic: Bill by traffic. |
| bandwidth | Yes | Int | Public network bandwidth (in Mbps). 0 means that public network bandwidth is not enabled. To modify the bandwidth, use the <a href="/doc/api/229/调整按量计费实例带宽" title="Adjust the bandwidth of public network of postpaid instances">UpdateInstanceBandwidthHour</a> API after the instance is created. |
| imageType | Yes | Int | Image type. Value range: <br>1: Private image; <br>2: Public image; <br>3: Service marketplace image. |
| rootSize | No | Int | System disk size (in GB). For Linux, the default is 50 GB and the increment is 1GB. For Windows, it is always 50 GB. |
| keyId | No | String | Key ID. It can be queried by calling the <a href="/doc/api/229/查询密钥">Query Keys</a> (DescribeKeyPairs) API. |
| password | No | String | Instance password. It will be generated randomly if not set. Password rules for Linux server: A combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, $, %, ^, \, *, ()). Password rules for Windows server: A combination of 12-16 characters comprised of at least three of the following types: uppercase letters, lowercase letters, numbers, special characters (!, @, #, \, *).**Note: Key and password cannot be specified at the same time.** |
| needMonitorAgent | No | Int | Whether to enable the Cloud Monitor service. Only two values are available: 1: Enable (default); 0: Disable. |
| needSecurityAgent | No | Int | Whether to enable the cloud security service. Only two values are available: 1: enabled; 0: disabled. The default is 1. |
| wanIp | No | Int | Whether to enable public IP. Only two values are available: 1: Enable (default); 0: Disable. |
| sgId | No | String | Safety group ID. It can be queried by calling the <a href="/doc/api/229/查询安全组列表">Query Security Group List</a> API.
| projectId | No | String | Project ID. If not specified, 0 means default project. To specify other projects, you can call the <a href="/doc/api/403/4400" title="Query Project List">Query Project List</a> (DescribeProject) API to query. |
| dataSnapshotId | No | String | Data disk snapshot ID. If you want to use the data disk snapshot feature, the data disk type (`storageType`) must be cloud disk, and the capacity of the data disk snapshot must be less than that of the data disk (`storageSize`). |
| cvmType | No | String | Select CVM type. Three values are available: 11 means Standard CVM; 21 means High IO CVM; 31 means Memory CVM. If not specified, this field is 11 (Standard CVM) by default. |

The launch configurations support three CVMs, including Standard CVM, High IO CVM and Memory CVM (subject to the actual available types in each region). For more information about the CPUs and memories sizes supported by launch configurations, please see [CVM Instance Configuration](https://cloud.tencent.com/doc/product/213/2177).



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> in the Error Codes page.|
| codeDesc | String | Error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned. |
| message | String | Module error message description depending on API.|
| data | Array | Output results, including the information of the created launch configuration list. |

Parameter data is composed of only one element: `scalingConfigurationIdSet`.

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingConfigurationIdSet | Array | ID of each created launch configuration. |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, please see [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

| Error Code | Description |
|----|------|
| QuotaExceeded.ScallingConfiguration | Launch configurations to be added exceed the limit |
| NameDuplicate.ScallingConfiguration | Launch configuration name already exists |
| InvalidParameter.SecurityGroupId | Security group ID is incorrect |
| IInvalidParameter.CbsNotMatchCpu | 1C1G can only be configured with cloud disks |
| InvalidParameter.storageType | Storage type error |
| QuotaExceeded.storageSize | Data disk size is out of range |
| QuotaExceeded.rootSize | System disk size is out of range |
| OprationFail.CpuOrMemNotExsit | The model for this CPU and MEME is sold out or does not exist |


## 5. Example
###Input

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingConfigurationName=test
&imageType=2
&imageId=img-xxx
&cpu=1
&mem=1
&storageType=1
&storageSize=10
&bandwidthType=PayByTraffic
&bandwidth=1
&projectId=102135
&cvmType=11
```
###Output:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
    "data":{
        "scalingConfigurationIdSet":[
            "xxxxxx"
        ]
    }
}
```

