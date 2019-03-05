## 1. 接口描述

本接口(DescribeSSLVpnDomain)用于查询sslVPN域。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font> 

 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeSSLVpnDomain。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | Int | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 |
| sslVpnId | 是 | Int | 系统分配的SSLvpn网关ID，例如：vpngw-l2tlvgb9。可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2sslVPN?viewType=preview" title="DescribeSSLVpn">DescribeSSLVpn</a>接口查询。 |

 

## 3. 输出参数

| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0: 成功，其他值: 失败。 |
| message | String | 错误信息。 |
| data.n | Array | 返回的ssl vpn域信息 |
| data.n.groupId | String | 工作组ID，例如：ugrp-8zbvqpea。|
| data.n.ipPool | Array | 终端IP段。|
| data.n.acl.n | Array | acl策略信息数组。|

acl策略信息数组

| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| acl.n.proto | String | acl协议，例如tcp。|
| acl.n.action | String | ACL策略，0：允许，1：拒绝。|
| acl.n.destinationPort | String | 目的端口。|
| acl.n.sourceCidr | String | 源IP或源网段。|
| acl.n.destinationCidr | String | 目的IP或目的网段。|

## 4. 错误码表
 该接口没有业务错误码，公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码">vpc错误码</a>
 
## 5. 示例
 
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeSSLVpnDomain
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=93
&sslVpnId=vpngw-l2tlvgb9
&groupId=dgdgd
&sslVpnPort=442
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "data": [
        {
            "groupId": "ugrp-8zbvqpea",
            "ipPool": [
                "172.23.138.16-172.23.138.20"
            ],
            "acl": [
                {
                    "proto": "all",
                    "action": 1,
                    "destinationPort": 0,
                    "sourceCidr": "0.0.0.0\/0",
                    "destinationCidr": "0.0.0.0\/0"
                }
            ]
        }
    ]
}
```

