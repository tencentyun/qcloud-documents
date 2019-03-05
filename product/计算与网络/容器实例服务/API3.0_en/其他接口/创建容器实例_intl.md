## 1. API Description

Domain name for API request: cis.tencentcloudapi.com.

This API (CreateContainerInstance) is used to create a container instance.

The default limit on the requests made to the API is 20 requests per second.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/858/17764).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateContainerInstance |
| Version | Yes | String | Common parameter. The value used for this API: 2018-04-08 |
| Region | Yes | String | Common parameter. For more information, see the [list of regions](/document/api/858/17764#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Zone | Yes | String | Availability zone |
| VpcId | Yes | String | VPC ID |
| SubnetId | Yes | String | Subnet ID |
| InstanceName | Yes | String | It is composed of lowercase letters, numbers and "-", with a length not more than 40 characters. It begins with a lowercase letter and ends with a lowercase letter or a number. |
| RestartPolicy | Yes | String | Restart policy (Always, OnFailure, and Never) |
| Containers.N | Yes | Array of [Container](/document/api/858/17776#Container) | Container list |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceId | String | Container instance ID |
| RequestId | String | The unique request ID, which is returned for each request. The RequestId is required for troubleshooting. |

## 4. Error Codes

The following only lists the error codes related to this API. For other error codes, see [Common Error Codes](/document/api/858/17766#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error. |
| InvalidParameter | Incorrect parameter. |

## 5. Example

### Example 1 Create a container instance named "cis-dev"

#### Input example

```
https://cis.tencentcloudapi.com/?Action=CreateContainerInstance
&Zone=ap-chengdu-1
&VpcId=vpc-mjmab5g2
&SubnetId=subnet-bwyqjag9
&InstanceName=cis-dev
&RestartPolicy=Never
&Containers.0.Name=sshd
&Containers.0.Image=jdeathe/centos-ssh:centos-7
&Containers.0.Cpu=0.25
&Containers.0.Memory=0.25
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "InstanceId": "cis-abcdefgh",
    "RequestId": "701c8a35-ed66-fc79-3795-5a1fa72cdbf1"
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

