## 1. 接口描述

本接口(CreateNetworkAcl)用于创建网络ACL。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

1) 网络ACL是针对某个子网设置的网络安全策略，跟云主机里面的安全组是有区别的。安全组是针对某个云主机做网络安全策略设置。
2) 如果云主机配置了安全组策略同时所在子网也设置了网络 ACL 策略，云主机入站方向请求优先匹配网络 ACL 策略，然后再匹配安全组；出站方向请求优先匹配安全组策略，然后再匹配网络ACL。
3) 云主机的安全组是有状态的，而网络ACL是无状态的。
 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateNetworkAcl。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 子网所属的私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-4n9efgju。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 |
| networkAclName | 是 | String | 网络ACL名称，可任意命名，但不得超过60个字符。|

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0: 成功，其他值: 失败。 |
| message | String | 错误信息。 |
| data.networkAclId | String | 网络ACL ID，例如：acl-4n9efgju。 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidNetworkAclName | 网络ACL名称不合法。可任意命名，但不得超过60个字符。 |
| NetworkAclLimitExceeded | 创建的网络 ACL 数量超过上限。如果需要更多资源，请联系客服申请。更多 VPC 资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>。 |
 

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=CreateNetworkAcl
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=gz_vpc_266
  &networkAclName=dgdgadgd

</pre>

输出
```

{
    "code": 0,
    "message": "",
    "data": {
        "networkAclId": "acl-4n9efgju"
    }
}

```

