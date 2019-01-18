
## 1. 接口描述

本接口(UpdateInstanceVpcConfig)用于修改实例vpc属性，如私有网络ip。
* 此操作默认会关闭实例，完成后再启动。
* 不支持跨VpcId操作。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见[公共请求参数](/document/api/213/15692)。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Action | 是 | String | 公共参数，本接口取值：UpdateInstanceVpcConfig |
| Version | 是 | String | 公共参数，本接口取值：2017-03-12 |
| InstanceId | 是 | String | 待操作的实例ID。可通过[`DescribeInstances`](document/api/213/9388)接口返回值中的`InstanceId`获取。 |
| VirtualPrivateCloud | 是 | [VirtualPrivateCloud](/document/api/213/15753#VirtualPrivateCloud) | 私有网络相关信息配置。通过该参数指定私有网络的ID，子网ID，私有网络ip等信息。 |
| ForceStop | 否 | Boolean | 是否对运行中的实例选择强制关机。默认为TRUE。 |

## 3. 输出参数



| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。 |

## 4. 错误码



| 错误码 | 描述 |
|---------|---------|
| EniNotAllowedChangeSubnet | 弹性网卡不允许跨子网操作。 |
| InvalidParameterValue | 无效参数值。参数值格式错误或者参数值不被支持等。 |
| VpcAddrNotInSubNet | 私有网络ip不在子网内。 |
| VpcIdNotMatch | VpcId与实例所在VpcId不匹配。 |
| VpcIpIsUsed | 私有网络ip已经被使用。 |

## 5. 示例


        