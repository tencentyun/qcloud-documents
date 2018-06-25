## 1. API Description

This API (UpdateInstanceVpcConfig) is used to modify VPC attributes, such as IP.

Domain name for API request: cvm.api.qcloud.com


* Instances are shut down by default when you perform this operation. Restart the instances upon completion of the operation.
* This operation cannot be performed under different VPC IDs.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceId | String | Yes | ID of the instance you want to modify. It can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/9388). |
| VirtualPrivateCloud | [VirtualPrivateCloud](/document/api/213/9451#virtualprivatecloud) object | Yes | Configuration information of VPC. This parameter is used to specify VPC ID, subnet ID, VPC IP, etc. |
| ForceStop | Boolean | No | Whether to forced shutdown a running instance. Default is TRUE. |

## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique "requestId" is returned for each request. In case of a failed call to the API, "requestId" needs to be provided when you contact the developer at backend. |


### Example of the Parameter Returned When the API Performs Normally
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```
## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidParameterValue | Parameter value is in an incorrect format or is not supported. |
| VpcAddrNotInSubNet | VPC IP is not in the subnet. |
| VpcIpIsUsed | This VPC IP is already occupied. |
| VpcIdNotMatch | This VpcId is different with that of the instance. |
| EniNotAllowedChangeSubnet | Operations on ENI cannot be performed in different subnets. |

