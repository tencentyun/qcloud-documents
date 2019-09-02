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
