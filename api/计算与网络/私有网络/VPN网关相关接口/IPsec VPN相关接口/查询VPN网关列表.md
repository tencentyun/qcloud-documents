## 1. 接口描述

本接口（DescribeVpnGw）用于查询 VPN 网关列表。
接口请求域名：vpc.api.qcloud.com

 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数"> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 DescribeVpnGw。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 否 | String | 私有网络 ID 值，可使用 vpcId 或 unVpcId，建议使用 unVpcId，例如 vpc-amhnnao5，可选项。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx"> DescribeVpcEx </a>接口查询。 |
| vpnGwId | 否 | String | 系统分配的 VPN 网关 ID 值，可使用 vpnGwId 或 unVpnGwId，建议 unVpnGwId，例如 vpngw-dystbrkv，可选项。 |
| vpnGwName | 否 | String | VPN 网关名称，支持模糊搜索。|
| dealId | 否 | String | 购买 VPN 网关的订单号，可以按订单号查询购买的 VPN 网关信息。|
| offset | 否 | Int | 初始行的偏移量，默认为0。 |
| limit | 否 | Int | 每页行数，默认为20，最大支持50。 |
| orderField | 否 | String | 按某个字段排序，目前仅支持 createTime，vpnGwName 排序，默认按 createTime 排序。 |
| orderDirection | 否 | String | 升序（asc）还是降序（desc），默认：desc。 |

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |
|  totalCount |   Int | 返回结果中 VPN 网关总数量。|
| data.n | array  | 返回的数组。|
| data.n.vpcId | String | 系统分配的私有网络 ID，例如 gz_vpc_8849。 |
| data.n.unVpcId | String | 系统分配的新的私有网络 ID，建议使用新 ID，例如 vpc-0ox8fuhw。 |
| data.n.vpnGwId | Int | 系统分配的 VPN 网关 ID，例如122。 |
| data.n.unVpnGwId | String | 系统分配的新的 VPN 网关 ID，建议使用新 ID，例如 vpngw-nhg87nmg。 |
| data.n.vpnGwName | String | VPN 网络名称。 |
| data.n.bandwidth | Int | VPN 网关带宽。 |
| data.n.vpnGwStatus | Int |  VPN 网关操作状态，0:待付款 1:付款错误 2:发货中 3:发货错误 4:销毁中 5:销毁错误 6:运行。 |
| data.n.vpnGwAddress | String | VPN 网关公网 IP。 |
| data.n.dealId | String | VPN 网关生产订单 ID。 |
| data.n.isAutoRenewals | Int | 是否开启自动续费，1:开启，0:未开启。 |
| data.n.expireTime | String | VPN 网关到期时间，到期后 VPN 网关将被系统销毁，请及时续费，例如2015-11-06 20:55:12。 |
| data.n.createTime | String | VPN 网关创建时间，例如2015-11-06 20:55:12。 |

## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码"> VPC 错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx"> DescribeVpcEx </a>接口查询 VPC 。|
| InvalidVpnGw.NotFound | 无效的 VPN 网关。VPN 网关资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpnGw
  &<公共请求参数>
  &vpcId=vpc-erxok83l

</pre>

输出
```

{
    "code": 0,
    "message": "",
    "totalCount": 3,
    "data": [
        {
            "vpcId": "sh_vpc_389",
            "unVpcId": "vpc-aa3z6vxo",
            "vpcName": "joezou",
            "vpcCidrBlock": "172.16.0.0\/16",
            "vpnGwId": 122,
            "unVpnGwId": "vpngw-nhg87nmg",
            "vpnGwName": "test001",
            "bandwidth": 5,
            "vpnGwStatus": 6,
            "vpnGwAddress": "115.159.26.189",
            "dealId": "896973",
            "localSlaIp": "169.254.97.7",
            "isAutoRenewals": true,
            "expireTime": "2015-12-23 19:04:40",
            "createTime": "2015-11-23 19:02:54"
        },
        {
            "vpcId": "sh_vpc_390",
            "unVpcId": "vpc-36dt60su",
            "vpcName": "joezou-2",
            "vpcCidrBlock": "172.17.0.0\/16",
            "vpnGwId": 121,
            "unVpnGwId": "vpngw-d77hr4r8",
            "vpnGwName": "roy_test",
            "bandwidth": 5,
            "vpnGwStatus": 6,
            "vpnGwAddress": "115.159.72.143",
            "dealId": "896725",
            "localSlaIp": "169.254.97.5",
            "isAutoRenewals": true,
            "expireTime": "2016-01-23 17:01:05",
            "createTime": "2015-11-23 16:59:23"
        },
        {
            "vpcId": "sh_vpc_314",
            "unVpcId": "vpc-4w87vv5s",
            "vpcName": "test",
            "vpcCidrBlock": "10.0.0.0\/16",
            "vpnGwId": 120,
            "unVpnGwId": "vpngw-4tu3v388",
            "vpnGwName": "roy_test",
            "bandwidth": 5,
            "vpnGwStatus": 6,
            "vpnGwAddress": "115.159.92.113",
            "dealId": "896720",
            "localSlaIp": "169.254.97.3",
            "isAutoRenewals": true,
            "expireTime": "2016-01-23 17:00:25",
            "createTime": "2015-11-23 16:58:32"
        }
    ]
}

```

