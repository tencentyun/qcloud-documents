## 1. 接口描述

本接口（ResetVpnConnSA）用于重置 VPN 通道。
接口请求域名：vpc.api.qcloud.com
 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数"> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 ResetVpnConnSA。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | string | 私有网络 ID，可使用 vpcId 或 unVpcId，建议使用 unVpcId，例如：vpc-03vihbk9，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx"> DescribeVpcEx </a>接口查询。 | 
| vpnGwId | 是 | String | 系统分配的 VPN 网关 ID，可使用 vpnGwId 或 unVpnGwId，建议 unVpnGwId，例如：vpngw-dystbrkv。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw"> DescribeVpnGw </a>接口查询。 |
| vpnConnId | 是 | String | 系统分配的 VPN 通道 ID，可使用 vpnConnId 或 unVpnConnId，建议使用 unVpnConnId，例如：vpnx-ol6bcqp0。可通过<a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn"> DescribeVpnConn </a>接口查询。 | 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码"> VPC 错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx"> DescribeVpcEx </a>接口查询 VPC。 |
| InvalidVpnGw.NotFound | 无效的 VPN 网关。VPN 网关资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw"> DescribeVpnGw </a>接口查询 VPN 网关。 |
| InvalidVpnGw.NotFound | 无效的 VPN 通道。VPN 通道资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn"> DescribeVpnConn </a>接口查询 VPN 通道。 |
 

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=ResetVpnConnSA
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=vpc-03vihbk9
  &vpnGwId=vpngw-kfldykuz
  &vpnConnId=vpnx-ol6bcqp0

</pre>

输出

```

{
    "code": 0,
    "message": ""
}

```
