## 1. 接口描述
本接口(CreateVpcPeeringConnectionEx)用于创建跨地域对等连接。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

1) 跨地域对等连接用于打通两个不同地域下的私有网络，需要互通的两个私有网络网段不能重叠，更多信息详见<a href="https://cloud.tencent.com/doc/product/215/1685" title="对等连接">对等连接介绍</a>。
2) 跨账户的对等连接需要对端接受才生效，同账户的立即生效。
3) 跨域互通带宽可以设置，创建后如果需要调整请联系客服申请。
4) 跨地域互通目前支持的地域、支持的带宽上限、收费标准详见<a href="https://cloud.tencent.com/doc/product/215/1685" title="对等连接">对等连接产品介绍</a>。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateVpcPeeringConnectionEx。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。|
| peerVpcId | 是 | String | 接受方私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。|
| peerUin | 是 | String | 接收方腾讯云唯一账号标识，您可以联系接收方去用户中心的个人信息中查看，<a href="https://cloud.tencent.com/document/product/215/5000#.E6.9F.A5.E7.9C.8B.E5.AF.B9.E7.AB.AF.E8.B4.A6.E5.8F.B7id21">点击查看操作指南</a>。|
| peeringConnectionName | 是 | String | 对等连接名称,可任意命名，但不得超过60个字符。|
| peerRegion | 是 | String | 接收方地域，目前支持的地域详见<a href="https://cloud.tencent.com/document/product/215/4927#.E5.9C.B0.E5.9F.9F.EF.BC.88region.EF.BC.895" title="对等连接">地域介绍</a>。 |
| bandwidth | 是 | String | 对等连接带宽上限，单位Mbps，默认不限制。具体数值详见<a href="https://cloud.tencent.com/document/product/215/5000#.E5.90.8C.E5.9C.B0.E5.9F.9F.E5.AF.B9.E7.AD.89.E8.BF.9E.E6.8E.A5-.E5.92.8C-.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E8.B7.A8.E5.9C.B0.E5.9F.9F.E5.AF.B9.E7.AD.89.E8.BF.9E.E6.8E.A5.EF.BC.88.E5.8D.B3.EF.BC.9A.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E8.B7.A8.E5.9C.B0.E5.9F.9F.E4.BA.92.E8.81.94.EF.BC.893" title="对等连接">对等连接产品介绍</a>。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0：成功，其他值：失败。|
| message | String | 错误信息。|
| taskId | Int | 任务ID，创建结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。 |


 ## 4. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidPeeringConnectionName | 对等连接名称不合法。可任意命名，但不得超过60个字符。 |
| PeeringConnectionVpcConflict | 对等连接之间VPC网段冲突 |
| PeeringConnectionLimitExceeded | 您已经达到指定区域对等连接资源申请数量上限。如果需要更多资源，请联系客服申请。更多vpc资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>。 |
| InvalidVpc.NotFound | 无效的vpc，vpc资源不存在。请再次核实您输入的资源信息是否正确。 |


## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateVpcPeeringConnectionEx
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=gz_vpc_226
&peerVpcId=gz_vpc_89
&peerUin=2407912486
&peeringConnectionName=tses
&peerRegion=gz
&bandwidth=20
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "taskId":112245
}
```

