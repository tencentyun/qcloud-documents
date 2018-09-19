## 1. 接口描述

本接口(DescribeSubnet)用于查询子网属性。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font> 
 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeSubnet。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 子网所属的私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-piztzbpy。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 | 
| subnetId | 是 | String | 系统分配的子网ID，可使用subnetId或unSubnetId，建议使用unsubnetId，例如：subnet-piztzbpy。|


## 3. 输出参数

| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0: 成功，其他值: 失败。 |
| message | String | 错误信息。 |
| subnetId | String | 系统分配的子网ID，示例:subnetId_GZ_23。 |
| subnetName | String | 子网名称。|
| subnetCreateTime | String | 子网创建时间，例如：2015-10-30 16:10:49。|
| cidrBlock | String | 子网网段，示例:192.168.0.0/25。|
| routeTableId | String | 子网绑定的默认路由表ID，示例:gz_rtb_8751。|
| zoneId | String | 子网所在可用区ID,示例:200001。|
| totalIPNum | Int | 子网内IP数总量。|
| availableIPNum | Int | 子网内可分配IP总数。|

 ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>接口查询子网。 |

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeSubnet
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=gz_vpc_265
  &subnetId=subnet-piztzbpy
  &subnetName=apiSubnetTest
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "subnetId": "gz_subnet_18712",
    "subnetName": "apiSubnetTest",
    "subnetCreateTime": "2015-10-30 16:10:49",
    "routeTableId": "gz_rtb_8747",
    "cidrBlock": "10.100.100.0\/25",
    "zoneId": 800001,
    "totalIPNum": 125,
    "availableIPNum": 125
}

```

