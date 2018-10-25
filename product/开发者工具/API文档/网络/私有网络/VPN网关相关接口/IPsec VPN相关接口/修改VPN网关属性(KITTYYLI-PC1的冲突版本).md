## 1. 接口描述

本接口(ModifyVpnGw)用于修改VPN网关属性。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font> 

 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifyVpnGw。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-amhnnao5。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 |
| vpnGwId | 是 | String | 要修改的VPN网关ID值，可使用vpnGwId或unVpnGwId，建议unVpnGwId，例如：vpngw-dystbrkv。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>接口查询。 |
| vpnGwName | 否 | String | 修改后网关名称，取值：1-25个中文、英文大小写的字母、数字和下划线分隔符，同一个VPC下名称不可重复。 |
| isAutoRenewals | 否 | Int | 是否开启自动续费。0：:不自动续费；1：自动续费。 |

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0: 成功，其他值: 失败。 |
| message | String | 错误信息。 |

## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidVpnGw.NotFound | 无效的vpn网关。vpn网关资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw">DescribeVpnGw</a>接口查询vpn网关。 |
| InvalidVpnGwState | vpn网关状态不对 |
| InvalidVpnGwName | 网络ACL名称不合法。ACL 名称取值范围：1-60个中文、英文大小写的字母、数字和下划线分隔符。 |
| InvalidVpnGwName.InUse | 网络ACL名称已被VPC下其他网络ACL使用。同一个 VPC 内网络ACL名称不能重复。 |

## 5. 示例
 
输入
```
  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpnGw
  &<公共请求参数>
  &vpcId=vpc-amhnnao5
  &vpnGwId=vpngw-dystbrkv
  &vpnGwName=test-9910
  &isAutoRenewals=0

```

输出
```

{
    "code": 0,
    "message": ""
}

```

