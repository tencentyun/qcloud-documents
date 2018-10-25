## 1. 接口描述

本接口(AssociateRouteTable)用于修改子网关联的路由表。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font> 

一个子网只能关联一个路由表。

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为AssociateRouteTable。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 子网所属的私有网络ID，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-amhnnao5。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 |
| subnetId | 是 | String | 要关联的子网ID值，可使用subnetId或unSubnetId，建议使用unsubnetId，例如：subnet-3x5lf5q0。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>接口查询。这里也支持批量，例如subnetId.0=subnet-3x5lf5q0。 |
| routeTableId | 是 | String | 系统分配的路由表ID，可使用routeTableId或unRouteTableId，建议使用unRouteTableId，例如：rtb-rqndayhs。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>接口查询。 |


 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|

  ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>接口查询子网。 |
| InvalidRouteTableId.NotFound | 无效的路由表。路由表ID不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>接口查询。 | 

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=AssociateRouteTable
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=vpc-amhnnao5
  &routeTableId=rtb-rqndayhs
  &subnetId=subnet-3x5lf5q0
</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

