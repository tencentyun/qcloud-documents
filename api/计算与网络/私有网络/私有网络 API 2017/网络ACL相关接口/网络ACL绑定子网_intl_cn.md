## 1. 接口描述

本接口(CreateSubnetAclRule)用于网络ACL绑定子网。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font> 
 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateSubnetAclRule。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 子网所属的私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-erxok83l。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 |
| networkAclId | 是 | String | 系统分配的网络ACL ID，例如：acl-e9dbyl8s。可通过<a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>接口查询。 | 
| subnetIds.n | 是 | Array | 系统分配的子网ID列表，兼容subnetId或unSubnetId，建议使用unsubnetId，例如：subnet-i6mdq6ra。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>接口查询。 | 

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0: 成功，其他值: 失败。 |
| message |  String | 错误信息。 |


  ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidNetworkAclID.NotFound | 无效的网络 ACL ID。网络 ACL ID不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>接口查询。 |

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=CreateSubnetAclRule
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=vpc-erxok83l
  &networkAclId=acl-e9dbyl8s
  &subnetIds.0=subnet-i6mdq6ra

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

