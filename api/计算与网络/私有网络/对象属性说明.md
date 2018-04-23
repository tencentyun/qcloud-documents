## 1. 私有网络相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| vpcId | String | 系统分配的vpcId，例如：gz_vpc_266 |
| unVpcId | String | 系统分配新的vpcID，由vpcId升级而来，为了兼容这两种ID系统都支持，推荐使用新的ID，例如：vpc-2ari9m7h |
| vpcName | String | VPC名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| cidrBlock | String | VPC网段,可选值 10.0.0.0/16、172.16.0.0/16和192.168.0.0/16及它们包含的子网，详见VPC网段规划说明 |
| createTime | String | 私有网络创建时间，例如：2016-05-18 15:01:46 |

## 2. 子网相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| subnetId | String | 系统分配的子网ID，例如：gz_subnet_18720 |
| unSubnetId | String | 系统分配新的子网ID，由子网ID升级而来，为了兼容这两种ID系统都支持，推荐使用这种新的ID，例如：subnet-2ari9m7h |
| subnetName | String | VPC名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符,例如：计费平台私有网络 |
| cidrBlock | String | VPC网段,可选值 10.0.0.0/16、172.16.0.0/16和192.168.0.0/16及它们包含的子网，详见VPC网段规划说明 |
| zoneId | String | 可用区ID，详见可用区管理 |
| createTime | String | 子网创建时间，例如：2016-05-18 15:01:46 |

## 3. 路由表相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| routeTableName | String | 路由表名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| destinationCidrBlock | String | 目的网段，取值不能在私有网络网段内，例如：112.20.51.0/24 |
| nextType | String | 下一跳类型，目前我们支持的类型有：0：公网网关；1：vpn网关； 3：专线网关；4：对等连接；7：sslvpn;8:nat网关 |
| nextHub | String | 下一跳地址，这里只需要指定不同下一跳类型的网关ID（推荐使用新ID），系统会自动匹配到下一跳地址。 |

## 4. 网络ACL相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| networkAclId | String | 系统分配的网络AclID，例如：acl-4n9efgju |
| networkAclName | String | 网络Acl名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| ruleDirection | Int | 网络Acl策略方向，0：出方向；1：入方向 |
| networkAclEntrySet | Array | acl策略，详见网络ACL接口文档 |


## 5. IPsec vpn网关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| vpnGwId | String | 系统分配的vpn网关ID，例如：95 |
| unVpnGwId | String | 系统分配新的vpn网关ID，由vpnGwId升级而来，为了兼容这两种ID系统都支持，推荐使用新的网关ID，例如：vpngw-nhg87nmg |
| vpnGwName | String | VPN网关名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| vpnGwAddress | String | VPN网关公网IP地址，例如：115.159.26.189 |
| bandwidth | Int | vpn网关带宽,例如5,10,20...，单位Mb,详见vpn网关规格说明文档 |
| expireTime | String | VPN网关到期时间 |
| isAutoRenewals | Bool | 是否开启自动续费。true:开启；false:不开启。默认是true |
| state | Int | vpn网关状态；0：创建中；1：创建失败；2：修改中；3：修改失败；4：删除中；5：删除失败；6：运行中 |
| createTime | String | vpn网关创建时间，例如：2016-05-18 15:01:46 |


## 6. vpn通道属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| vpnConnId | String | 系统分配的VPN通道ID，例如：534 |
| unVpnConnId | String | 系统分配新的VPN通道ID，由vpnConnId升级而来，为了兼容这两种ID系统都支持，推荐使用新的通道ID，例如：vpnx-pvjmedgm |
| vpnConnName | String | VPN通道，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| preSharedKey | String | 预共享密钥 |
| spdAcl | Array | SPD策略规则,细粒度的流量配置，详见VPN通道接口文档 |
| IKE | Array | IKE配置，详见VPN通道接口文档 |
| IPsec | Array | IPsec配置，详见VPN通道接口文档 |
| state | Int | vpn通道状态；0：创建中；1：创建失败；2：修改中；3：修改失败；4：删除中；5：删除失败；6：运行中 |
| createTime | String | VPN通道创建时间，例如：2016-05-18 15:01:46 |

## 7. 对端网关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| userGwId | String | 系统分配的对端网关ID，例如：404 |
| unUserGwId | String | 系统分配新的对端网关ID，由userGwId升级而来，为了兼容这两种ID系统都支持，推荐使用新的对端网关ID，例如：cgw-7ihaps8r |
| userGwName | String | 对端网关名称 |
| userGwAddr | String | 对端网关公网IP地址,不能是私有地址，也不能是广播地址或者组播地址 |
| createTime | String | 对端网关创建时间，例如：2016-05-18 15:01:46 |


## 8. SSL VPN网关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| sslVpnId | String | 系统分配的SSL VPN网关ID，例如：vpngw-nhg87nmg |
| sslVpnName | String | SSL VPN名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| sslVpnAddress | String |SSL VPN网关公网IP地址，例如：115.159.26.189 |
| bandwidth | Int | SSL VPN网关带宽,支持5,10,20,50,100，单位Mb,详见VPN网关规格说明文档 |
| sslVpnPort | String | SSL VPN端口 |
| ipPool.n | Array | SSL VPN终端IP池，终端IP会从这个IP池分配IP，例如ipPool.0=183.162.10.1 |
| acl | Array | SSL VPN域的acl策略信息,详见SSL VPN接口文档 |
| expireTime | String |SSL VPN网关到期时间 |
| isAutoRenewals | Bool | 是否开启自动续费。true:开启；false:不开启。默认是true |
| state | Int | ssl SSL VPN状态；0：创建中；1：创建失败；2：修改中；3：修改失败；4：删除中；5：删除失败；6：运行中 |
| createTime | String | ssl SSL VPN创建时间，例如：2016-05-18 15:01:46 |

## 9. 对等连接相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| peeringConnectionId | String | 系统分配的对等连接ID，例如：pcx-55i0gr4s |
| peeringConnectionName | String | 对等连接名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| vpcId | String | 发起方vpcId，例如：vpc-55i0gr4s |
| uin | String | 发起方QQ号码 |
| region | String | 发起方地域，支持的地域详见对等连接接口文档 |
| peerVpcId | String | 接收方vpcId，例如：vpc-55i0gr4s |
| peerUin | String | 接收方QQ号码 |
| peerRegion | String | 接收方地域，支持的地域详见对等连接接口文档 |
| bandwidth | String | 对等连接带宽，支持的带宽详见对等连接接口文档 |
| state | Int | 对等连接状态；0：待接收；1：运行中；2：过期；3：拒绝；4：删除中；5：创建失败 |
| createTime | String | 对等连接创建时间，例如：2016-05-18 15:01:46 |

## 10. 专线网关相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| directConnectGatewayId | String | 专线网关ID，例如：dcg-rw6a1ozr |
| directConnectGatewayName | String | 对等连接名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| type | Int | 专线网关类型，0:非nat；1：nat，默认为非nat网关 |
| natRule | Array | 网络地址转换规则，详见专线网关接口文档 |
| aclRule | Array | 网络acl策略组，详见专线网关接口文档 |
| createTime | String | 专线网关创建时间，例如：2016-05-18 15:01:46 |

## 11. NAT网关相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| natId | String | 系统分配的NAT网关ID，例如：nat-dhfpwhtm |
| natName | String | NAT网关名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| maxConcurrent | Int | 网关并发连接上限，例如：100、300、1000，单位为万 |
| bandwidth | Int | 网关最大外网出带宽(单位:Mbps)，详见NAT网关接口文档 |
| state | Int | NAT网关状态；0：运行中；1：不可用；2：欠费停服； |
| createTime | String | NAT网关创建时间，例如：2016-05-18 15:01:46 |

## 12. 弹性网卡相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| networkInterfaceId | String | 系统分配的弹性网卡ID，例如：eni-9r7vukmh |
| eniName | String | 弹性网卡名称，支持1-60个中文、英文大小写的字母、数字和下划线分隔符 |
| eniDescrption | String | 弹性网卡描述，25个字符以内 |
| primary | Bool | 弹性网卡类型，true:主网卡；false:普通网卡 |
| macAddress | String | 弹性网卡mac地址，例如：02:81:60:cb:27:37 |
| vpcId | String | 弹性网卡所属的私有网络ID，例如：vpc-2ari9m7h |
| subnetId | String | 弹性网卡所属的子网ID，例如：subnet-2ari9m7h |
| createTime | String | 弹性网卡创建时间，例如：2016-05-18 15:01:46 |

## 13. 私有网络与基础网络互通相关属性
| 属性 | 类型 | 说明 |
|---------|---------|---------|
| classicLinkId | String | 系统分配的互通ID，例如：vcx-8kbdxt2h |
| vpcId | String | 私有网络ID，例如：gz_vpc_164 |
| instanceId | String | 与VPC互通的基础网络云主机资源ID，例如：ins-dgd54d |
| createTime | String | 基础网络设备与vpc互通创建时间，例如：2016-05-18 15:01:46 |

## 14. 流日志相关属性

| 属性 | 类型 | 说明 |
|---------|---------|---------|
| vpcId | String | 系统分配的vpcId，例如：gz_vpc_266 |
| flowLogName | String | 流日志名称。|
| flowLogDescription | String | 流日志描述，默认为"",可选项。|
| resourceType | String | 流日志所属资源类型，VPC\|SUBNET\|NETWORKINTERFACE。|
| resourceId | String | 资源唯一ID，例如vpc-puz6fg, subnet-5o8ycyt, eni-08dhim。 |
| trafficType | String | 流日志采集类型，ACCEPT\|REJECT\|ALL。 | 
| cloudLogId | String | 流日志存储ID, 暂时只支持日志服务ID，例如d44e4cf0-c3e2-48d9-bb64-c5f0337ef2b0。|
| flowLogId | String | 流日志唯一ID，示例：fl-q1b26f3d。|
| createdTime | String | 流日志创建时间。|

