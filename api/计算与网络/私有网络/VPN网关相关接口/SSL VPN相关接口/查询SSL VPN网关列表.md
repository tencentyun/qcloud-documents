## 1. 接口描述

本接口（DescribeSSLVpn）用于查询 sslVPN。
接口请求域名：vpc.api.qcloud.com 

 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数"> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 DescribeSSLVpn。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------| 
| vpcId | 否 | String | 私有网络 ID 值，可使用 vpcId 或 unVpcId，建议使用 unVpcId，例如 vpc-amhnnao5，可选项。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx"> DescribeVpcEx </a>接口查询。 |
| sslVpnId | 否 | String | 系统分配的 SSL VPN 网关 ID，例如 vpngw-dystbrkv，可选项。 |
| sslVpnName | 否 | String | SSL VPN 网关名称，支持模糊搜索。|
| offset | 否 | Int | 初始行的偏移量，默认为0。 |
| limit | 否 | Int | 每页行数，默认为20，最大支持50。 |
| orderField | 否 | String | 按某个字段排序，目前仅支持 createTime，sslVpnName 排序，默认按 createTime 排序。 |
| orderDirection | 否 | String | 升序（asc）还是降序（desc），默认：desc。 |
 

## 3. 输出参数

| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |
|  totalCount |   Int | 返回的 SSL VPN 总数量。|
| sslVpnSet.n | array  | 返回的数组。|
| sslVpnSet.n.sslVpnId | Int | 系统分配的 SSL VPN 网关 ID，例如 vpngw-l2tlvgb9。 |
| sslVpnSet.n.sslVpnName | String | SSL VPN 网络名称。 |
| sslVpnSet.n.sslVpnStatus | Int | SSL VPN 网关操作状态，0：待付款，1：付款错误，2：发货中，3：发货错误，4：销毁中，5：销毁错误，6：运行中。 |
| sslVpnSet.n.vpnGwStatus | Int |  VPN 网关操作状态，0:待付款 1:付款错误 2:发货中 3:发货错误 4:销毁中 5:销毁错误 6:运行。 |
| sslVpnSet.n.bandwidth | Int | SSL VPN 带宽。 |
| sslVpnSet.n.sslVpnPort | String | SSL VPN 端口。 |
| sslVpnSet.n.sslVpnDomainAclNum | Int | SSL VPN 域 ACL 策略数。 |
| sslVpnSet.n.isAutoRenewals | Int | 是否开启自动续费，1:开启，0:未开启。 |
| sslVpnSet.n.expireTime | String | VPN 网关到期时间，到期后 VPN 网关将被系统销毁，请及时续费，例如2015-11-06 20:55:12。 |
| sslVpnSet.n.createTime | String | VPN 网关创建时间，例如2015-11-06 20:55:12。 |

## 4. 错误码表
该接口没有业务错误码，公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码"> VPC 错误码</a>。

## 5. 示例
 
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeSSLVpn
&<公共请求参数>
&openid=12345
&openkey=12345
&pf=qzone
&appid=12345
&format=json
&userip.0=10.0.0.1

</pre>

输出
```
{
    "code": 0,
    "message": "",
    "totalCount": 2,
    "sslVpnSet": [
        {
            "sslVpnName": "test",
            "sslVpnStatus": 6,
            "sslVpnId": "vpngw-l2tlvgb9",
            "sslVpnQuota": "mini",
            "bandwidth": 5,
            "vpcId": "gz_vpc_93",
            "isAutoRenewals": 1,
            "expireTime": "2016-11-17 15:33:03",
            "sslVpnAddress": "183.60.249.91",
            "sslVpnPort": 8000,
            "sslVpnDomainAclNum": 3,
            "unVpcId": "vpc-dsp338hz",
            "dealId": "2015991116"
        },
        {
            "sslVpnName": "test",
            "sslVpnStatus": 6,
            "sslVpnId": "vpngw-2csvvdob",
            "sslVpnQuota": "mini",
            "bandwidth": 5,
            "vpcId": "gz_vpc_75",
            "isAutoRenewals": 1,
            "expireTime": "2016-11-04 10:20:28",
            "sslVpnAddress": "183.60.249.44",
            "sslVpnPort": 8080,
            "sslVpnDomainAclNum": 2,
            "unVpcId": "vpc-fj1msp8l",
            "dealId": "20150718"
        }
    ]
}

```

