## 1. API Description

Domain name for API request: cis.tencentcloudapi.com.

This API (DescribeContainerInstance) is used to get details about a container instance.

The default limit on the requests made to the API is 20 requests per second.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/858/17764).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeContainerInstance |
| Version | Yes | String | Common parameter. The value used for this API: 2018-04-08 |
| Region | Yes | String | Common parameter. For more information, see the [list of regions](/document/api/858/17764#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceName | Yes | String | Container instance name |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| ContainerInstance | [ContainerInstance](/document/api/858/17776#ContainerInstance) | Details about a container instance |
| RequestId | String | The unique request ID, which is returned for each request. The RequestId is required for troubleshooting. |

## 4. Error Codes

The following only lists the error codes related to this API. For other error codes, see [Common Error Codes](/document/api/858/17766#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error. |
| InvalidParameter | Incorrect parameter. |

## 5. Example

### Example 1 Get details about the container instance "sshdlogt"

#### Input example

```
https://cis.tencentcloudapi.com/?Action=DescribeContainerInstance
&InstanceName=sshdlog
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "ContainerInstance": {
      "Containers": [
        {
          "Args": null,
          "Command": null,
          "ContainerId": "c782aa6a7dd3df431ed2094256e90b82f59f39733a794ea294ed11037e4e2477",
          "Cpu": 0.25,
          "CurrentState": {
            "StartTime": "2018-05-18 14:34:03",
            "State": "Running"
          },
          "EnvironmentVars": null,
          "Image": "jdeathe/centos-ssh:centos-7",
          "Memory": 0.25,
          "Name": "sshd",
          "PreviousState": null,
          "RestartCount": 0,
          "WorkingDir": null
        }
      ],
      "CreateTime": "2018-05-18 14:33:40",
      "InstanceId": "cis-1a082ocw",
      "InstanceName": "sshdlog",
      "LanIp": "10.0.2.20",
      "RestartPolicy": "Never",
      "StartTime": "2018-05-18 14:33:40",
      "State": "Running",
      "SubnetCidr": "10.0.2.0/24",
      "SubnetId": "subnet-r0t1xm4e",
      "SubnetName": "zone4",
      "VpcCidr": "10.0.0.0/16",
      "VpcId": "vpc-3p4hvnmx",
      "VpcName": "ddtest",
      "Zone": "ap-guangzhou-4"
    },
    "RequestId": "07b9d257-ba2c-4a4f-b78a-600d225eb3b2"
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

