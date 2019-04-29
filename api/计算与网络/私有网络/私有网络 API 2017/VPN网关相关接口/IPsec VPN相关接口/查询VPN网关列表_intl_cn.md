## 1. 接口描述

本接口(DescribeVpnGw)用于查询VPN网关列表。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font> 

 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeVpnGw。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 否 | String | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-amhnnao5，可选项。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 |
| vpnGwId | 否 | String | 系统分配的VPN网关ID值，可使用vpnGwId或unVpnGwId，建议unVpnGwId，例如：vpngw-dystbrkv，可选项。 |
| vpnGwName | 否 | String | vpn网关名称，支持模糊搜索。|
| dealId | 否 | String | 购买VPN网关的订单号，可以按订单号查询购买的VPN网关信息。|
| offset | 否 | Int | 初始行的偏移量，默认为0。 |
| limit | 否 | Int | 每页行数，默认为20，最大支持50。 |
| orderField | 否 | String | 按某个字段排序，目前仅支持createTime,vpnGwName排序，默认按createTime排序。 |
| orderDirection | 否 | String | 升序（asc）还是降序（desc），默认：desc。 |

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |
|  totalCount |   Int | 返回结果中VPN网关总数量。|
| data.n | array  | 返回的数组。|
| data.n.vpcId | String | 系统分配的私有网络ID，例如：gz_vpc_8849。 |
| data.n.unVpcId | String | 系统分配的新的私有网络ID，建议使用新ID，例如：vpc-0ox8fuhw。 |
| data.n.vpnGwId | Int | 系统分配的vpn网关ID，例如：122。 |
| data.n.unVpnGwId | String | 系统分配的新的vpn网关ID，建议使用新ID，例如：vpngw-nhg87nmg。 |
| data.n.vpnGwName | String | vpn网络名称。 |
| data.n.bandwidth | Int | VPN网关带宽。 |
| data.n.vpnGwStatus | Int |  VPN网关操作状态，0:待付款 1:付款错误 2:发货中 3:发货错误 4:销毁中 5:销毁错误 6:运行。 |
| data.n.vpnGwAddress | String | VPN网关公网IP。 |
| data.n.dealId | String | vpn网关生产订单ID。 |
| data.n.isAutoRenewals | Int | 是否开启自动续费，1:开启，0:未开启。 |
| data.n.expireTime | String | vpn网关到期时间，到期后vpn网关将被系统销毁，请及时续费，例如：2015-11-06 20:55:12。 |
| data.n.createTime | String | vpn网关创建时间，例如：2015-11-06 20:55:12。 |

## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC 。|
| InvalidVpnGw.NotFound | 无效的vpn网关。vpn网关资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpnGw
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
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

