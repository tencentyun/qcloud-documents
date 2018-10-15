## 1. API Description

Domain name for API request: cis.tencentcloudapi.com.

This API (DescribeContainerInstances) is used to query the container instance list.

The default limit on the requests made to the API is 20 requests per second.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/858/17764).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeContainerInstances |
| Version | Yes | String | Common parameter. The value used for this API: 2018-04-08 |
| Region | Yes | String | Common parameter. For more information, see the [list of regions](/document/api/858/17764#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Offset | No | Integer | Offset. It is 0 by default. |
| Limit | No | Integer | Number of returned items. It is 10 by default. |
| Filters.N | No | Array of [Filter](/document/api/858/17776#Filter) | Filter conditions.<br/> - Zone - String - Required: No - (Filter condition) Filter by availability zone.<br/> - VpcId - String - Required: No - (Filter condition) Filter by VpcId.<br/> - InstanceName - String - Required: No - (Filter condition) Fuzzy querying by instance name. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| ContainerInstanceList | Array of [ContainerInstance](/document/api/858/17776#ContainerInstance)  | Container instance list |
| TotalCount | Integer | Total number of container instances |
| RequestId | String | The unique request ID, which is returned for each request. The RequestId is required for troubleshooting.

## 4. Error Codes

The following only lists the error codes related to this API. For other error codes, see [Common Error Codes](/document/api/858/17766#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error. |
| InvalidParameter | Incorrect parameter. |

## 5. Example

### Example 1 Query the container instance list

#### Input example

```
https://cis.tencentcloudapi.com/?Action=DescribeContainerInstances
&Offset=0&Limit=10
&Filters.0.Name=InstanceName
&Filters.0.ValueList.0=hello
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "ContainerInstanceList": [
      {
        "Containers": [
          {
            "Args": [
              "hello world"
            ],
            "Command": "echo",
            "ContainerId": "7aa85b70a3e1e1856718cbb7f1de0dba236272380da2854f059dd489d4d967cd",
            "Cpu": 0.25,
            "CurrentState": {
              "ExitCode": 0,
              "FinishTime": "2018-05-17 11:16:42",
              "Reason": "Completed",
              "StartTime": "2018-05-17 11:16:42",
              "State": "Terminated"
            },
            "EnvironmentVars": null,
            "Image": "alpine:latest",
            "Memory": 0.25,
            "Name": "helloworld",
            "PreviousState": null,
            "RestartCount": 0,
            "WorkingDir": null
          }
        ],
        "CreateTime": "2018-05-17 11:14:28",
        "InstanceId": "cis-h2ud12sa",
        "InstanceName": "helloworld",
        "LanIp": "10.0.2.11",
        "RestartPolicy": "Never",
        "StartTime": "2018-05-17 11:16:23",
        "State": "Succeeded",
        "SubnetCidr": "10.0.2.0/24",
        "SubnetId": "subnet-r0t1xm4e",
        "SubnetName": "zone4",
        "VpcCidr": "10.0.0.0/16",
        "VpcId": "vpc-3p4hvnmx",
        "VpcName": "ddtest",
        "Zone": "ap-guangzhou-4"
      },
      {
        "Containers": [
          {
            "Args": [
              "hello world"
            ],
            "Command": "echo",
            "ContainerId": "11e66fc00ed8c653e256ede6885a8b428731387443331eeef7f12d7f77ceaf39",
            "Cpu": 0.25,
            "CurrentState": {
              "ExitCode": 0,
              "FinishTime": "2018-05-18 14:41:11",
              "Reason": "Completed",
              "StartTime": "2018-05-18 14:41:11",
              "State": "Terminated"
            },
            "EnvironmentVars": null,
            "Image": "busybox:latest",
            "Memory": 0.25,
            "Name": "echo",
            "PreviousState": null,
            "RestartCount": 0,
            "WorkingDir": null
          }
        ],
        "CreateTime": "2018-05-18 14:40:57",
        "InstanceId": "cis-esmfjhek",
        "InstanceName": "helloworld2",
        "LanIp": "10.0.2.24",
        "RestartPolicy": "Never",
        "StartTime": "2018-05-18 14:40:57",
        "State": "Succeeded",
        "SubnetCidr": "10.0.2.0/24",
        "SubnetId": "subnet-r0t1xm4e",
        "SubnetName": "zone4",
        "VpcCidr": "10.0.0.0/16",
        "VpcId": "vpc-3p4hvnmx",
        "VpcName": "ddtest",
        "Zone": "ap-guangzhou-4"
      }
    ],
    "RequestId": "7695ee56-77d2-43b1-bc7d-d85f411d44c6",
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
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

