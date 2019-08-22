>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>



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
| 查询服务器所在位置 | [DescribeDevicePosition](/document/product/386/9242) | 查询服务器所在位置。 |
| 修改服务器自动续费标志位 | [ModifyDeviceAutoRenewFlag](/document/product/386/9670) | 修改服务器自动续费标志位。 |
| 查询设备硬件配置信息 | [DescribeDeviceHardwareInfo](/document/product/386/12008) | 查询设备硬件配置信息。 |


## 3. 带外相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 获取带外VPN信息 | [GetOutBandVPNAuthInfo](/doc/api/456/6679) |  用于查询黑石物理服务器带外VPN认证用户名密码等信息。 |
| 获取带外登录信息 | [GetDeviceOutBandInfo](/doc/api/456/6678) |  用于查询黑石登录物理服务器带外页面时用户名密码等信息。 |
| 重置带外VPN密码 | [SetOutBandVPNAuthPwd](/doc/api/456/6680) | 用于重置黑石物理服务器的带外VPN认证用户名密码信息。 |

## 4. 私有网络相关接口
| 接口功能             | Action ID                                | 功能描述                      |
| ---------------- | ---------------------------------------- | ------------------------- |
| 删除黑石私有网络         | [DeleteBmVpc](https://cloud.tencent.com/document/product/386/17140) | 用于删除黑石私有网络                |
| 查询私有网络列表         | [DescribeBmVpcEx](https://cloud.tencent.com/doc/api/456/6646) | 用于查询黑石私有网络 VPC 列表。          |
| 查询子网列表           | [DescribeBmSubnetEx](https://cloud.tencent.com/doc/api/456/6648) | 用于查询黑石私有网络子网列表。           |
| 申请子网 IP           | [ApplyIps](https://cloud.tencent.com/document/product/386/7337) | 用于申请黑石 VPC 内的子网 IP。          |
| 退还子网 IP           | [ReturnIps](https://cloud.tencent.com/document/product/386/7338) | 用于退还黑石 VPC 内的子网 IP。          |
| 注册子网 IP           | [RegisterBatchIp](https://cloud.tencent.com/document/product/386/7925) | 用于注册黑石 VPC 内的子网 IP。          |
| 创建子网             | [CreateBmSubnet](https://cloud.tencent.com/document/product/386/9263) | 用于创建黑石 VPC  子网。              |
| 删除子网             | [DeleteBmSubnet](https://cloud.tencent.com/document/product/386/9264) | 用于删除黑石 VPC  子网。              |
| 物理机加入子网          | [CreateBmInterface](https://cloud.tencent.com/document/product/386/9265) | 用于黑石物理机加入其虚拟子机所在子网。       |
| 物理机移除子网          | [DelBmInterface](https://cloud.tencent.com/document/product/386/9266) | 用于黑石物理机从其虚拟子机所在子网移除。      |
| 查询任务状态           | [QueryBmTaskResult](https://cloud.tencent.com/document/product/386/9267) | 用于查询黑石物理机加入、移除子网等操作任务的状态。 |
| 查询子网 IP 分配列表       | [DescribeBmSubnetIps](https://cloud.tencent.com/document/product/386/9318) | 用于查询黑石 VPC 子网 IP 分配列表。        |
| 查询子网未分配 IP 列表    | [DescribeBmSubnetAvailableIp](https://cloud.tencent.com/document/product/386/17019) | 用于查询黑石 VPC 子网未分配的 IP 列表       |
| 查询加入子网的物理机列表     | [DescribeBmCpmBySubnetId](https://cloud.tencent.com/document/product/386/9319) | 用于查询加入到子网的所有物理机列表。        |
| 查询物理机加入的子网列表     | [DescribeBmSubnetByCpmId](https://cloud.tencent.com/document/product/386/9320) | 用于查询物理机加入的子网列表。           |
| 查询黑石 NAT 网关列表      | [DescribeBmNatGateway](https://cloud.tencent.com/document/product/386/9355) | 用于查询黑石 NAT 网关。              |
| 查询 NAT 网关的操作状态     | [QueryBmNatGatewayProductionStatus](https://cloud.tencent.com/document/product/386/9356) | 用于查询黑石 NAT 网关的操作状态。         |
| 创建黑石 NAT 网关        | [CreateBmNatGateway](https://cloud.tencent.com/document/product/386/9348) | 用于创建黑石 NAT 网关。              |
| 删除黑石 NAT 网关        | [DeleteBmNatGateway](https://cloud.tencent.com/document/product/386/9349) | 用于删除黑石 NAT 网关。              |
| NAT 网关绑定 EIP       | [EipBindBmNatGateway](https://cloud.tencent.com/document/product/386/9350) | 用于黑石 NAT 网关绑定 EIP。           |
| NAT 网关解绑 EIP       | [EipUnBindBmNatGateway](https://cloud.tencent.com/document/product/386/9351) | 用黑石于 NAT 网关解绑 EIP。           |
| NAT网关绑定子网        | [SubnetBindBmNatGateway](https://cloud.tencent.com/document/product/386/9352) | 用于黑石 NAT 网关绑定子网。            |
| NAT 网关解绑子网        | [SubnetUnBindBmNatGateway](https://cloud.tencent.com/document/product/386/9353) | 用黑石于 NAT 网关解绑子网。            |
| NAT 网关绑定子网部分 IP    | [BindIpsToBmNatGateway](https://cloud.tencent.com/document/product/386/10738) | 用于将子网的部分 IP 绑定到 NAT 网关        |
| NAT 网关解绑子网部分 IP    | [UnbindIpsToBmNatGateway](https://cloud.tencent.com/document/product/386/10739) | 用于将子网的部分 IP 从 NAT 网关中解绑       |
| 查询 NAT 网关绑定的子网     | [DescribeBmNatBindSubnets ](https://cloud.tencent.com/document/product/386/13871) | 用于查询黑石 NAT 网关绑定的子网信息      |
| 查看 NAT 网关部分子网绑定的 IP | [DescribeBmNatPartSubnetBindIps](https://cloud.tencent.com/document/product/386/13872) | 用于查询黑石 NAT 网关部分子网下绑定的 IP 信息   |
| 升级 NAT 网关规格        | [UpgradeBmNatGateway](https://cloud.tencent.com/document/product/386/9354) | 用于升级黑石 NAT 网关规格。            |
| 修改子网 Dhcp Relay 属性 | [ModifySubnetDhcpRelayFlag](https://cloud.tencent.com/document/product/386/10175) | 用于修改子网 Dhcp Relay 属性。       |


## 5. 负载均衡相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询负载均衡异步任务状态 | [DescribeBmLoadBalancersTaskResult](/document/product/386/9308) | 查询黑石负载均衡异步任务状态。 |
| 获取主机的负载均衡绑定详情 | [DescribeBmBindInfo](/document/product/386/9309) | 获取主机的负载均衡绑定详情。 |
| 获取负载均衡端口信息 | [DescribeBmVportInfo](/document/product/386/9310) | 获取负载均衡端口信息。 |
| 创建负载均衡 | [CreateBmLoadBalancer](/document/product/386/9303) | 创建负载均衡。 |
| 获取负载均衡实例列表 | [DescribeBmLoadBalancers](/document/product/386/9306) | 获取负载均衡实例列表。|
| 修改负载均衡属性信息 | [ModifyBmLoadBalancerAttributes](/document/product/386/9302) | 修改负载均衡属性信息。 |
| 删除负载均衡 | [DeleteBmLoadBalancers](/document/product/386/9304) | 删除负载均衡。 |
| 查询负载均衡价格 | [InquiryBmLBPrice](/document/product/386/9305) | 查询负载均衡价格。 |
| 创建负载均衡四层监听器 | [CreateBmListeners](/document/product/386/9292) | 创建负载均衡四层监听器。 |
| 获取负载均衡四层监听器 | [DescribeBmListeners](/document/product/386/9296) | 获取负载均衡四层监听器。 |
| 获取负载均衡四层监听器详细信息 | [DescribeBmListenerInfo](/document/product/386/9298) | 获取负载均衡四层监听器详细信息。 |
| 修改负载均衡四层监听器 | [ModifyBmListener](/document/product/386/9289) | 修改负载均衡四层监听器。 |
| 绑定物理服务器到四层监听器 | [BindBmL4ListenerRs](/document/product/386/9294) | 绑定物理服务器到四层监听器。 |
| 绑定虚机IP到负载均衡四层监听器 | [BindBmL4ListenerVmIp](/document/product/386/9295) | 绑定虚机IP到负载均衡四层监听器。 |
| 获取负载均衡四层监听器绑定的主机列表 | [DescribeBmL4ListenerBackends](/document/product/386/9297) | 获取负载均衡四层监听器绑定的主机列表。 |
| 修改负载均衡四层监听器后端实例权重 | [ModifyBmL4ListenerBackendWeight](/document/product/386/9290) | 修改负载均衡四层监听器后端实例权重。 |
| 修改负载均衡四层监听器后端实例端口 | [ModifyBmL4ListenerBackendPort](/document/product/386/9291) | 修改负载均衡四层监听器后端实例端口。 |
| 解绑负载均衡四层监听器物理服务器 | [UnbindBmL4ListenerRs](/document/product/386/9299) | 解绑负载均衡四层监听器物理服务器。 |
| 解绑负载均衡四层监听器虚机IP | [UnbindBmL4ListenerVmIp](/document/product/386/9300) | 解绑负载均衡四层监听器虚机IP。 |
| 删除负载均衡四层监听器 | [DeleteBmListeners](/document/product/386/9293) | 删除负载均衡四层监听器。 |
| 创建负载均衡七层监听器 | [CreateBmForwardListeners](/document/product/386/9277) | 创建负载均衡七层监听器。|
| 获取负载均衡七层监听器 | [DescribeBmForwardListeners](/document/product/386/9283) | 获取负载均衡七层监听器。|
| 获取负载均衡七层监听器详细信息 | [DescribeBmForwardListenerInfo](/document/product/386/9284) | 获取负载均衡七层监听器详细信息。|
| 修改负载均衡七层监听器 | [ModifyBmForwardListener](/document/product/386/9273) | 修改负载均衡七层监听器。|
| 创建负载均衡七层转发规则 | [CreateBmForwardRules](/document/product/386/9278) | 创建负载均衡七层转发规则。|
| 获取负载均衡七层转发规则 | [DescribeBmForwardRules](/document/product/386/9285) | 获取负载均衡七层转发规则。 |
| 修改负载均衡七层转发路径 | [ModifyBmForwardLocation](/document/product/386/9274) | 修改负载均衡七层转发路径。|
| 绑定物理服务器到七层转发路径 | [BindBmLocationInstances](/document/product/386/9281) | 绑定物理服务器到七层转发路径。|
| 绑定虚机IP到负载均衡七层转发路径 | [BindBmL7LocationVmIp](/document/product/386/9282) | 绑定虚机IP到负载均衡七层转发路径。|
| 获取负载均衡七层转发路径绑定的主机列表 | [DescribeBmLocationBackends](/document/product/386/9286) | 获取负载均衡七层转发路径绑定的主机列表。 |
| 修改负载均衡七层转发路径后端实例权重 | [ModifyBmLocationBackendWeight](/document/product/386/9275) | 修改负载均衡七层转发路径后端实例权重。|
| 修改负载均衡七层转发路径后端实例端口 | [ModifyBmLocationBackendPort](/document/product/386/9276) | 修改负载均衡七层转发路径后端实例端口。|
| 解绑物理服务器到七层转发路径 | [UnbindBmLocationInstances](/document/product/386/9287) | 解绑物理服务器到七层转发路径。 |
| 解绑负载均衡七层转发路径虚机IP | [UnbindBmL7LocationVmIp](/document/product/386/9288) | 解绑负载均衡七层转发路径虚机IP。 |
| 删除负载均衡七层转发规则 | [DeleteBmForwardRules](/document/product/386/9280) | 删除负载均衡七层转发规则。|
| 删除负载均衡七层转发域名 | [DeleteBmForwardDomains](/document/product/386/9279) | 删除负载均衡七层转发域名。|
| 创建负载均衡证书 | [UploadBmCert](/document/product/386/9312) | 创建负载均衡证书。 |
| 获取负载均衡证书详情 | [GetBmCertDetail](/document/product/386/9314) | 获取负载均衡证书详情。 |
| 更新负载均衡证书 | [ReplaceBmCert](/document/product/386/9313) | 更新负载均衡证书。 |


## 6. 弹性公网IP（EIP）相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询EIP列表 | [DescribeEipBm](/doc/api/456/6671) | 用于查询黑石弹性公网IP列表。
| 查询EIP限额 | [DescribeEipBmQuota](/doc/api/456/6668) | 用于查询黑石弹性公网IP申请限额。
| 创建EIP | [EipBmApply](/doc/api/456/6669) | 用于创建黑石弹性公网IP。
| 绑定服务器EIP | [EipBmBindRs](/doc/api/456/6673) | 用于绑定黑石弹性公网IP到黑石物理服务器。
| 解绑服务器EIP | [EipBmUnbindRs](/doc/api/456/6674) | 用于解绑黑石物理服务器上的弹性公网IP。
| 绑定EIP到VPCIP | [EipBmBindVpcIp](/document/product/386/8684) | 用于绑定黑石弹性公网IP到黑石VPC的IP地址（多用于虚拟化）。
| 从VPCIP解绑EIP | [EipBmUnBindVpcIp](/document/product/386/8685) | 用于解绑黑石VPC的IP地址上的弹性公网IP（多用于虚拟化）。
| 释放EIP | [EipBmDelete](/doc/api/456/6676) | 用于释放黑石弹性公网IP。
| 更新EIP名称 | [ModifyEipAlias](/doc/api/456/6672) | 用于更新黑石弹性公网IP名称。
| 修改EIP计费模式 | [EipBmModifyCharge](/doc/api/456/6675) | 用于修改黑石弹性公网IP计费模式。
| 查询EIP任务状态 | [EipBmQueryTask](/doc/api/456/6670) | 用于查询黑石弹性公网IP异步任务状态。
