## 1. 接口描述
 
本接口(AssociateVip)用于私用网络云服务器绑定 VIP，将预先分配的内网 VIP 绑定到指定的子机，便于多台子机做主备功能。

<font style="color:red">本接口实现的功能已经用弹性网卡功能代替，不推荐使用该接口。</font>

新接口调用方式及使用场景详见 [VPC内通过 keepalived 搭建高可用主备集群 >>](https://cloud.tencent.com/document/product/215/20186)

接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

1) 目前 VIP 需要联系在线客服申请。
2) 云服务器必须是VPC内的。

 

## 2. 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为AssociateVip。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络ID，支持升级前的vpcId，也支持升级后的unVpcId，例如：vpc-2ari9m7h。 |
| vipId | 是 | Int | VIP的ID，例如：12，VIP ID需要联系在线客服申请 |
| lanIp | 是 | String | 云服务器内网IP，例如：10.0.0.1。查询云服务器IP详见<a href="https://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="查看实例列表">查看实例列表</a> |
 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
 
 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVipId.NotFound | vipId不存在，目前vip需要人工分配，如果您忘记vipId或者第一次绑定，请联系在线客服找回或者申请。 |
| InvalidLanIp.NotFound | 云服务器不存在，请核实您填写的lanIp是否正确，查询vpc下云服务器详见<a href="https://cloud.tencent.com/doc/api/229/831" title="查看云服务器实例列表">查看云服务器实例列表</a>。 |
| InvalidVpc.NotFound | 无效的vpc。vpc资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
 
输入
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=AssociateVip
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=vpc-2ari9m7h
	&vipId=1
	&lanIp=10.0.0.2
</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

