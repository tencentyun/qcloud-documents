>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (RunInstancesHour) 用于创建一个或多个指定配置的按量计费实例。

接口请求域名：cvm.api.qcloud.com

* API创建的实例遵循 [CVM 实例购买限制](https://cloud.tencent.com/doc/product/213/CVM%E5%AE%9E%E4%BE%8B%E8%B4%AD%E4%B9%B0%E9%99%90%E5%88%B6) 文档所描述的数量限制，和官网所创建的实例共用配额。
* CPU与内存具体的**配比限制**参见 [CVM 实例配置](https://cloud.tencent.com/document/product/213/11518)。
* 实例的创建需要一定时间，本接口不会立刻返回实例结果。而是返回一个InstanceId，在此期间可以通过 [DescribeInstances](/doc/api/229/831) 接口查询该实例的状态。如果状态由“创建中”变为“正在运行”，则为创建成功。  
* 实例创建成功后为“正在运行”的状态，无需再次调用 [StartInstances](/doc/api/229/1249) 来启动。
* 不支持带宽包用户购买按量计费实例。
* 如需要更改带宽，请在实例创建成功后，使用接口 [UpdateInstanceBandwidthHour](https://cloud.tencent.com/doc/api/229/1345) 更改，**公网带宽不指定默认为0**。
* 本接口暂不支持在创建实例的同时绑定安全组，所创建的实例默认所有端口都放通，建议用户在创建实例之后使用[ModifySecurityGroupsOfInstance](https://cloud.tencent.com/document/api/213/1367) 接口给对应云服务器关联的安全组。
* 支持的实例类型：

|机型	|系列1|系列2|
|---------|---------|---------|
|标准型|CVM.S1|CVM.S2
|高IO型|CVM.I1|CVM.I2
|内存型|CVM.M1|CVM.M2
|计算型|－|CVM.C2 

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/document/api/213/6976) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| zoneId| 是| Int|[可用区](https://cloud.tencent.com/doc/product/213/497#2.-.E5.8F.AF.E7.94.A8.E5.8C.BA) ID。|
| cpu| 是| Int| CPU核数，具体限制见上。 |
| mem| 是| Int| 内存大小(GB)，具体限制见上。 |
| imageId| 是| String| 镜像ID。可通过 [DescribeImages](https://cloud.tencent.com/doc/api/229/查询可用的镜像列表) 接口(链接包含公共镜像名称ID对应表)返回字段中的 unImgId 获取。|
|storageSize| 是| Int| 数据盘大小（GB）。最小调整步长为10G，此参数默认值为0，表示不购买数据盘。其所分配数据盘的类型与 `storageType` 所指定的一致。关于不同类型数据盘的特性与容量限制请参考 [硬盘产品简介](https://cloud.tencent.com/doc/product/213/498)。|
|instanceType|否|String| 实例类型（例如高 IO 型等）。默认为`CVM.S1`。更多实例类型，可在上文查看“实例类型”一节。
| imageType| 否| Int| 镜像类型。1：私有镜像、2：公有镜像、3：镜像市场、4：共享镜像。默认为2。如果您指定非公有镜像的`ImageId`，则必须指定ImageType，如使用公有镜像，则无需`ImageType`参数。|
| bandwidthType| 否| String|带宽的类型。`PayByHour`：按带宽使用时长计费；PayByTraffic：按流量计费。 默认为按使用时长计费。网络计费模式的区别可以参看 [购买网络带宽](https://cloud.tencent.com/doc/product/213/509)。|
| bandwidth| 否| Int| 公网带宽(Mbps)，当按流量计费时为公网带宽峰值。默认为0|
| wanIp| 否| Int| 是否开通公网IP。1：开通，0：不开通。`bandwidth`大于0，可自由选择开通与否，默认开通公网 IP；`bandwidth`为0，则不分配公网IP。|
| vpcId| 否| String|[私有网络](https://cloud.tencent.com/document/product/215/20046) ID。私有网络下为必填，不填则为基础网络。
| subnetId| 否| String| [子网](https://cloud.tencent.com/document/product/215/20046#.E5.AD.90.E7.BD.91) ID，私有网络下为必填（必须保证此`subnetId`在本可用区内）。|
| isVpcGateway| 否| Int| 是否是 [公网网关](https://cloud.tencent.com/document/product/215/20185)。0：非公网网关；1：公网网关；默认为0。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。|
| storageType| 否| Int| 硬盘类型。硬盘类型。1:本地硬盘、2:普通云硬盘、3:本地 SSD 硬盘；默认为本地硬盘。关于硬盘类型的选择请参考 [硬盘产品简介](https://cloud.tencent.com/document/product/213/4953)，可选硬盘类型受到实例类型（InstanceType）限制。另外允许购买的最大容量也因硬盘类型的不同而有所差异。|
| rootSize| 否| Int| 系统盘大小（GB）。Linux/BSD 系统调整范围为20~50G，最小调整步长为10G，默认免费分配20G。Windows 不可调整，默认为免费分配50G。系统盘类型须与 `storageType` 所指定的一致。|
| password| 否| String| 实例密码。未设置则为随机产生，并通过站内信下发。linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9] 和 [( ) &#96; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' , . ? / ]中的特殊符号。Windows 实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) &#96; ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符号。|
| keyId| 否| String| [密钥](https://cloud.tencent.com/doc/product/213/503) ID。关联密钥后可使用密钥登录实例，`keyId` 可通过接口 [DescribeKeyPairs](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AF%86%E9%92%A5) 获取，密钥与密码不能同时指定，同时 Windows 操作系统不支持指定密钥。|
| needSecurityAgent| 否| Int|开启 [云安全服务](https://cloud.tencent.com/doc/product/296/2222)。0：不开通，1：开通。默认开通。|
| needMonitorAgent| 否| Int|开启 [云监控服务](https://cloud.tencent.com/doc/product/248/967)。0：不开通，1：开通。默认开通。|
| projectId| 否| Int| [项目 ID](https://cloud.tencent.com/doc/api/403/4398)，不填为默认项目。|
| instanceName| 否| String| 实例名称，可任意命名，但不得超过60个字符。默认为“未命名”。|
| goodsNum| 否| Int| 购买实例数量。默认为1, 最大100。|
|clientToken|否|String| 保证此 API 幂等的`Token`，最多64字符。不同的 API 请求携带相同的 `Token` 视为同一请求，可以防止客户端请求API时因为网络异常而重试，导致多次创建实例的情况。|
|privateIpAddresses.n|否|array of Strings|私有子网 IP 数组，目前只支持一个 IP。在创建实例、修改实例 VPC 属性操作中可使用此参数。|

## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的 [模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| unInstanceIds| Array| 系统自动生成实例的ID，命名格式为“ins-xxxxxxxx”，可使用此 ID 通过 [DescribeInstances](/doc/api/229/831) API 查询实例的详细信息。|

## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见 [CVM 错误码](/document/product/213/6982)页面。

|错误码|描述|
|---|---|
|InvalidParameter.PasswordNotConformSpecs|密码不合规范|
|InvalidParameter.InvaildZoneId|zoneId 不合法
|InnerError.VpcError|内部错误 VPC|
|OperationConstraints.AccountBalanceNotEnough|您的余额不足，请先充值
|OperationFail.SystemBusy|资源购买繁忙
|InvalidParameter.InvalidIpFormat|ip格式不正确
|InvalidParameter.NotSupportReservedIp|保留 IP 不可使用
|InvalidParameter.IpNotInCidrRange|IP 不在子网内
|InvalidParameter.IpInUse|IP 已经被使用

## 5. 示例
 
输入
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=RunInstancesHour
  &imageId=img-3wnd9xpl
  &bandwidth=1
  &cpu=1
  &mem=2
  &storageType=1
  &storageSize=50
  &goodsNum=1
  &zoneId=100001
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
	"code": 0,
	"message": "ok",
	"unInstanceIds": [
		"xxxx1",
		"xxxx2"
	]
}
```
