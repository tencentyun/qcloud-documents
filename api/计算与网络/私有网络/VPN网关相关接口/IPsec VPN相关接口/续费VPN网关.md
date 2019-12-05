## 1. 接口描述

本接口（RenewVpn）用于续费 VPN。
接口请求域名：`vpc.api.qcloud.com`

 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 RenewVpn。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | string | 网络ID或者统一ID，建议使用统一ID，示例：vpc-aa3z6vxo，可通过 <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> 接口查询。 |
| vpnGwId | 是 | string | 要修改的 VPN 网关 ID 值，可使用 vpnGwId 或 unVpnGwId，建议 unVpnGwId，示例：vpngw-nhg87nmg，可通过 <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw </a>接口查询 |
| period | 是 | Int | 续费时长，单位月，最大36个月 | 

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |

 ## 4. 错误码表
 该接口没有业务错误码，公共错误码详见 <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码">vpc 错误码</a>。

## 5. 示例
 
输入
<pre>
https://domain/v2/index.php?Action=RenewVpn
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=gz_vpc_1111
&period=1
&vpnGwId=1
</pre>

输出
```
{
	"code": 0,
	"message": "ok"
}
```

