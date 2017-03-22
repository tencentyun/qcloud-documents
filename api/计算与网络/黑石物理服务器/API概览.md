
## 1. 地域相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询地域以及可用区 | [DescribeRegions](/doc/api/456/6634) | 用于查询黑石物理服务器可用区的详细信息。 |

## 2. 物理服务器相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 购买服务器 | [BuyDevice](/doc/api/456/6638) |  用于购买黑石物理服务器。 |
| 查询服务器 | [DescribeDevice](/doc/api/456/6728) | 用于查询已购买的黑石物理服务器详细信息。 |
| 查询操作系统列表 | [DescribeOs](/doc/api/456/6727) | 用于查询指定物理服务器机型已支持的操作系统列表。 |
| 查询RAID列表 | [DescribeDeviceClassRaid](/doc/api/456/6640) | 用于查询指定黑石物理服务器机型已支持的RAID类型列表。 |
| 查询设备型号 | [DescribeDeviceClass](/doc/api/456/6636) | 用于查询当前售卖的黑石物理服务器机型列表。 |
| 查询设备操作日志 | [DescribeDeviceOperationLog](/doc/api/456/6637) | 用于查询黑石物理机服务器操作日志。 |
| 查询异步任务状态 | [DescriptionOperationResult](/doc/api/456/6644) | 用于查询黑石物理机服务器异步任务的当前状态。 |
| 重置密码 | [ResetDevicePasswd](/doc/api/456/6641) | 用于重置黑石物理服务器的root密码。 |
| 修改服务器名称 | [ModifyDeviceAlias](/doc/api/456/6643) | 用于批量修改黑石物理服务器的别名。 |
| 重装操作系统 | [ReloadDeviceOs](/doc/api/456/6642) | 用于重装黑石物理服务器的操作系统。 |
| 开启服务器 | [StartDevice](/doc/api/456/6726) | 用于开启黑石物理服务器。 |
| 关闭服务器 | [ShutdownDevice](/doc/api/456/6639) | 用于关闭黑石物理服务器。 |
| 重启服务器 | [RebootDevice](/doc/api/456/6729) | 用于重启黑石物理服务器。 |

## 3. 带外相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 获取带外VPN信息 | [GetOutBandVPNAuthInfo](/doc/api/456/6679) |  用于查询黑石物理服务器带外VPN认证用户名密码等信息。 |
| 获取带外登录信息 | [GetDeviceOutBandInfo](/doc/api/456/6678) |  用于查询黑石登录物理服务器带外页面时用户名密码等信息。 |
| 重置带外VPN密码 | [SetOutBandVPNAuthPwd](/doc/api/456/6680) | 用于重置黑石物理服务器的带外VPN认证用户名密码信息。 |

## 4. 私有网络相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询私有网络列表 | [DescribeBmVpcEx](/doc/api/456/6646) | 用于查询黑石私有网络VPC列表。 |
| 查询子网列表 | [DescribeBmSubnetEx](/doc/api/456/6648) | 用于查询黑石私有网络子网列表。 |
| 申请内网IP | [ApplyIps](/document/product/386/7337) | 用于申请黑石VPC内的子网IP。 |
| 退还子网IP | [ReturnIps](/document/product/386/7338) | 用于退还黑石VPC内的子网IP。 |
| 注册子网IP | [RegisterBatchIp](/document/product/386/7925) | 用于注册黑石VPC内的子网IP。 |


## 5. 负载均衡相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询负载均衡价格 | [InquiryBmLBPrice](/doc/api/456/6652) | 用于查询负载均衡价格。 |
| 获取负载均衡实例列表 | [DescribeBmLoadBalancers](/doc/api/456/6658) | 用于获取负载均衡实例列表。 |
| 创建负载均衡 | [CreateBmLoadBalancer](/doc/api/456/6651) | 用于创建负载均衡。 |
| 删除负载均衡 | [DeleteBmLoadBalancers](/doc/api/456/6665) | 用于删除负载均衡。 |
| 绑定后端服务器到负载均衡 | [RegisterInstancesWithBmLoadBalancer](/doc/api/456/6654) | 用于将物理服务器绑定到负载均衡。 |
| 解绑后端服务器到负载均衡 | [DeregisterInstancesFromBmLoadBalancer](/doc/api/456/6660) | 用于解绑已绑定至物理服务器的负载均衡。 |
| 修改负载均衡属性信息 | [ModifyBmLoadBalancerAttributes](/doc/api/456/6663) | 用于修改负载均衡属性信息。 |
| 获取负载均衡后端服务器列表 | [DescribeBmLoadBalancerBackends](/doc/api/456/6656) | 用于获取负载均衡绑定的物理服务器列表。 |
| 获取服务器关联的负载均衡 | [DescribeBmLoadBalancersByInstances](/doc/api/456/6655) | 用于获取黑石物理服务器关联的负载均衡。 |
| 获取负载均衡监听器列表 | [DescribeBmLoadBalancerListeners](/doc/api/456/6657) | 用于获取负载均衡监听器列表。 | 
| 创建负载均衡监听器 | [CreateBmLoadBalancerListeners](/doc/api/456/6653) | 用于创建负载均衡监听器。 |
| 删除负载均衡监听器 | [DeleteBmLoadBalancerListeners](/doc/api/456/6664) | 用于删除负载均衡监听器。 |
| 修改负载均衡监听器 | [ModifyBmLoadBalancerListener](/doc/api/456/6661) | 用于修改负载均衡监听器。 |
| 查询负载均衡健康状态 | [DescribeBmLBHealthStatus](/doc/api/456/6659) | 用于查询负载均衡健康状态。 |
| 修改负载均衡器后端服务器权重 | [ModifyBmLoadBalancerBackends](/doc/api/456/6662) | 修改负载均衡器后端服务器权重。 |
| 查询负载均衡异步任务状态 | [DescribeBmLoadBalancersTaskResult](/doc/api/456/6666) | 查询黑石负载均衡异步任务状态。 |


## 6. 弹性公网IP（EIP）相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询EIP列表 | [DescribeEipBm](/doc/api/456/6671) | 用于查询黑石弹性公网IP列表。
| 查询EIP限额 | [DescribeEipBmQuota](/doc/api/456/6668) | 用于查询黑石弹性公网IP申请限额。
| 创建EIP | [EipBmApply](/doc/api/456/6669) | 用于创建黑石弹性公网IP。
| 绑定服务器EIP | [EipBmBindRs](/doc/api/456/6673) | 用于绑定黑石弹性公网IP到黑石物理服务器。
| 解绑服务器EIP | [EipBmUnbindRs](/doc/api/456/6674) | 用于解绑黑石物理服务器上的弹性公网IP。
| 绑定EIP到VPCIP | [EipBmBindVpcIp](/document/product/386/8684) | 用于绑定黑石弹性公网IP到黑石VPC的IP地址（多用于虚拟化）。
| 从VPCIP解绑EIP | [EipBmUnbindVpcIp](/document/product/386/8685) | 用于解绑黑石VPC的IP地址上的弹性公网IP（多用于虚拟化）。
| 释放EIP | [EipBmDelete](/doc/api/456/6676) | 用于释放黑石弹性公网IP。
| 更新EIP名称 | [ModifyEipAlias](/doc/api/456/6672) | 用于更新黑石弹性公网IP名称。
| 修改EIP计费模式 | [EipBmModifyCharge](/doc/api/456/6675) | 用于修改黑石弹性公网IP计费模式。
| 查询EIP任务状态 | [EipBmQueryTask](/doc/api/456/6670) | 用于查询黑石弹性公网IP异步任务状态。

