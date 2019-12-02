## 1. 接口描述
 
本接口(AssociateVip)用于私用网络云服务器绑定 VIP，将预先分配的内网 VIP 绑定到指定的子机，便于多台子机做主备功能。

<font style="color:red">本接口实现的功能已经用弹性网卡功能代替，不推荐使用该接口。</font>

新接口调用方式及使用场景详见 [VPC 内通过 keepalived 搭建高可用主备集群>> ](https://cloud.tencent.com/document/product/215/20186)。

接口请求域名：vpc.api.qcloud.com

1) 目前 VIP 需要联系在线客服申请。
2) 云服务器必须是 VPC 内的。

 

## 2. 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数"> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 AssociateVip。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络 ID，支持升级前的 vpcId，也支持升级后的 unVpcId，例如：vpc-2ari9m7h。 |
| vipId | 是 | Int | VIP的ID，例如：12，VIP ID 需要联系在线客服申请 |
| lanIp | 是 | String | 云服务器内网IP，例如：10.0.0.1。查询云服务器IP详见<a href="https://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="查看实例列表"> 查看实例列表 </a>。 |
 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/document/product/215/4781#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码"> 公共错误码 </a>。|
| message | String | 模块错误信息描述，与接口相关。|
 
 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码"> VPC 错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVipId.NotFound | vipId 不存在，目前 vip 需要人工分配，如果您忘记 vipId 或者第一次绑定，请联系在线客服找回或者申请。 |
| InvalidLanIp.NotFound | 云服务器不存在，请核实您填写的 lanIp 是否正确，查询 VPC 下云服务器详见<a href="https://cloud.tencent.com/doc/api/229/831" title="查看云服务器实例列表"> 查看云服务器实例列表 </a>。 |
| InvalidVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
 
输入
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=AssociateVip
	&<公共请求参数>
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

