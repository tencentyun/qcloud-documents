
## 1. API Description

This API (UpdateInstanceVpcConfig) is used to modify VPC attributes, such as IP.
* Instances are shut down by default when you perform this operation. Restart the instances upon completion of the operation.
* This operation cannot be performed under different VPC IDs.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: UpdateInstanceVpcConfig |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceId | Yes | String | ID of instance to work with. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](document/api/213/9388). |
| VirtualPrivateCloud | Yes | [VirtualPrivateCloud](/document/api/213/15753#VirtualPrivateCloud) | Configuration information of VPC. This parameter is used to specify VPC ID, subnet ID, VPC IP, etc. |
| ForceStop | No | Boolean | Indicate whether a forced shutdown is performed to running instances. Default is TRUE. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| EniNotAllowedChangeSubnet | Operations on ENI cannot be performed in different subnets. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| VpcAddrNotInSubNet | VPC IP is not in the subnet. |
| VpcIdNotMatch | VPC ID is different from that of the instance. |
| VpcIpIsUsed | VPC IP is already occupied. |

## 5. Example


        
