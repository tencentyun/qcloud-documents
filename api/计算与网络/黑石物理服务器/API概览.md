
## 1. 地域相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询地域以及可用区 | [DescribeRegions]() | 用于查询黑石物理服务器可用区的详细信息。 |

## 2. 物理服务器相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 购买服务器 | [BuyDevice](/doc/api/456/6638) |  用于购买黑石物理服务器。 |
| 查询服务器 | [DescribeDevice]() | 用于查询已购买的黑石物理服务器详细信息。 |
| 查询操作系统列表 | [DescribeOs]() | 用于查询指定物理服务器机型已支持的操作系统列表。 |
| 查询RAID列表 | [DescribeDeviceClassRaid]() | 用于查询指定黑石物理服务器机型已支持的RAID类型列表。 |
| 查询设备型号 | [DescribeDeviceClass]() | 用于查询当前售卖的黑石物理服务器机型列表。 |
| 查询可执行的操作类型 | [DescribeDeviceOperationLog]() | 用于查询黑石物理机服务器操作日志。 |
| 查询异步任务状态 | [DescriptionOperationResult](/doc/api/456/6644) | 用于查询黑石物理机服务器异步任务的当前状态。 |
| 重置密码 | [ResetDevicePasswd](/doc/api/456/6641) | 用于重置黑石物理服务器的root密码。 |
| 修改服务器名称 | [ModifyDeviceAlias]() | 用于批量修改黑石物理服务器的别名。 |
| 重装操作系统 | [ReloadDeviceOs](/doc/api/456/6642) | 用于重装黑石物理服务器的操作系统。 |
| 开启服务器 | [StartDevice]() | 用于开启黑石物理服务器。 |
| 关闭服务器 | [ShutdownDevice](/doc/api/456/6639) | 用于关闭黑石物理服务器。 |
| 重启服务器 | [RebootDevice]() | 用于重启黑石物理服务器。 |

## 3. 带外相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询带外VPN信息 | [GetOutBandVPNAuthInfo]() |  用于查询黑石物理服务器带外VPN认证用户名密码等信息。 |
| 重置带外VPN密码 | [SetOutBandVPNAuthPwd]() | 用于重置黑石物理服务器的带外VPN认证用户名密码信息。 |

## 4. 网络相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 申请VPC内网IP | [ApplyIps]() | 用于申请黑石VPC内的子网IP。 |
| 释放VPC内网IP | [ReturnIps]() | 用于释放黑石VPC内的子网IP。 |

## 5. 负载均衡相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询负载均衡价格 | [InquiryBm负载均衡Price]() | 用于查询负载均衡价格。 |
| 获取负载均衡实例列表 | [DescribeBmLoadBalancers]() | 用于获取负载均衡实例列表。 |
| 创建负载均衡 | [CreateBmLoadBalancer]() | 用于创建负载均衡。 |
| 删除负载均衡 | [DeleteBmLoadBalancers]() | 用于删除负载均衡。 |
| 绑定服务器到负载均衡 | [RegisterInstancesWithBmLoadBalancer]() | 用于将物理服务器绑定到负载均衡。 |
| 解绑服务器到负载均衡 | [DeregisterInstancesFromBmLoadBalancer]() | 用于解绑已绑定至物理服务器的负载均衡。 |
| 修改负载均衡属性信息 | [ModifyBmLoadBalancerAttributes]() | 用于修改负载均衡属性信息。 |
| 获取负载均衡服务器列表 | [DescribeBmLoadBalancerBackends]() | 用于获取负载均衡绑定的物理服务器列表。 |
| 获取服务器关联的负载均衡 | [DescribeBmLoadBalancersByInstances]() | 用于获取黑石物理服务器关联的负载均衡。 |
| 获取负载均衡监听器列表 | [DescribeBmLoadBalancerListeners]() | 用于获取负载均衡监听器列表。 | 
| 创建负载均衡监听器 | [CreateBmLoadBalancerListeners]() | 用于创建负载均衡监听器。 |
| 删除负载均衡监听器 | [DeleteBmLoadBalancerListeners]() | 用于删除负载均衡监听器。 |
| 修改负载均衡监听器 | [ModifyBmLoadBalancerListener]() | 用于修改负载均衡监听器。 |
| 查询负载均衡健康状态 | [DescribeBmLBHealthStatus]() | 用于查询负载均衡健康状态。 |
| 修改负载均衡器后端服务器权重 | [ModifyBmLoadBalancerBackends]() | 修改负载均衡器后端服务器权重。 |


## 6. 弹性公网IP（EIP）相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询EIP列表 | [DescribeEipBm]() | 用于查询黑石弹性公网IP列表。
| 查询EIP限额 | [DescribeEipBmQuota]() | 用于查询黑石弹性公网IP申请限额。
| 创建EIP | [EipBmApply]() | 用于创建黑石弹性公网IP。
| 绑定服务器EIP | [EipBmBindRs]() | 用于绑定黑石弹性公网IP到黑石物理服务器。
| 解绑服务器EIP | [EipBmUnbindRs]() | 用于解绑黑石物理服务器上的弹性公网IP。
| 释放EIP | [EipBmDelete]() | 用于释放黑石弹性公网IP。
| 更新EIP名称 | [ModifyEipAlias]() | 用于更新黑石弹性公网IP名称。
| 修改EIP计费模式 | [EipBmModifyCharge]() | 用于修改黑石弹性公网IP计费模式。
| 查询EIP任务状态 | [EipBmQueryTask]() | 用于查询黑石弹性公网IP异步任务状态。

