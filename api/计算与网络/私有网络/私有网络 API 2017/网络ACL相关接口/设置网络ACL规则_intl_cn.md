## 1. 接口描述

本接口（ModifyNetworkAclEntry）用于设置ACL规则。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

支持入站方向和出站方向的网络 ACL 策略设置；

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifyNetworkAclEntry。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 子网所属的私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-jk7weyp2。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 |
| networkAclId | 是 | String | 系统分配的网络ACL ID，例如：acl-jk7weyp2。可通过<a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>接口查询。 | 
| ruleDirection | 是 | Int | 网络ACL方向，1：入站，0：出站。 | 
| networkAclEntrySet.n | 是 | Array | 网络ACL策略信息数组。 | 
| networkAclEntrySet.n.desc | 是 | String | 备注。 |
| networkAclEntrySet.n.ipProtocol | 是 | String | 协议，例如tcp。 |
| networkAclEntrySet.n.cidrIp | 是 | String | 源IP或者源网段，支持IP或者CIDR，例如：10.20.3.0或者10.0.0.2/24。 |
| networkAclEntrySet.n.portRange | 是 | String | 源端口，支持单个接口或者端口段，例如：80或者90-100。 |
| networkAclEntrySet.n.action | 是 | Int | 策略，0:允许，1:拒绝。 |

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0: 成功，其他值: 失败。 |
| message | String | 错误信息。 |

 ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidNetworkAclID.NotFound | 无效的网络 ACL ID。V网络 ACL ID不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>接口查询。 |
| NetworkAclInLimitExceeded | 创建的网络 ACL 入站规则数量超过上限。如果需要更多资源，请联系客服申请。更多vpc资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>。 |
| NetworkAclOutLimitExceeded | 创建的网络 ACL 出站规则数量超过上限。如果需要更多资源，请联系客服申请。更多vpc资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>。 |

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyNetworkAclEntry
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=vpc-erxok83l
  &networkAclId=acl-jk7weyp2
  &ruleDirection=1
  &networkAclEntrySet.0.desc=test
  &networkAclEntrySet.0.ipProtocol=all
  &networkAclEntrySet.0.cidrIp=0.0.0.0/0
  &networkAclEntrySet.0.portRange=ALL
  &networkAclEntrySet.0.action=1
</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

