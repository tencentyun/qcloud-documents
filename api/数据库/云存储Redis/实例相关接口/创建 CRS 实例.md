## 1. 接口描述
本接口(CreateRedis)用于创建实例。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>

1) 实例容量单位：MB， 取值为1024的整数倍， 范围以 [查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口返回的规格为准， 取值范围[data.types.minMemSize, data.types.maxMemSize]， 主从版默认取值范围[1024MB, 61440MB]， 集群版默认配置为：[1024MB, 307200MB]
2) 单次购买实例数量以 [查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口返回的规格为准， 取值范[data.types.minBuyNum, data.types.maxBuyNum]， 默认值为： [1, 100]
3) 购买时长单位：月， 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
4) 密码规则： 长度为8-16个字符；至少包含字母、数字和字符（!@#%^()）中的两种
5) 如果需要购买某可用区的实例，请通过[工单](https://console.cloud.tencent.com/workorder/create?level1_id=10&level2_id=103&level1_name=%E6%95%B0%E6%8D%AE%E5%BA%93&level2_name=%E4%BA%91%E5%AD%98%E5%82%A8Redis%20CRS)提起申请


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/api/239/7200' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为CreateRedis。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| zoneId | 是 | UInt | 实例所属的可用区ID |
| typeId | 是 | UInt | 实例类型：1 – 集群版，2 – 主从版 |
| memSize | 是 | UInt | 实例容量，单位MB， 取值大小以 [查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口返回的规格为准， 取值范围[data.types.minMemSize, data.types.maxMemSize] |
| goodsNum | 是 | UInt | 实例数量，单次购买实例数量以 [查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口返回的规格为准， 取值范[data.types.minBuyNum, data.types.maxBuyNum]|
| period | 是 | UInt | 购买时长，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]|
| password | 是 | String | 实例密码，密码规则：1.长度为8-16个字符；2:至少包含字母、数字和字符（!@#%^()）中的两种 |
| vpcId | 否 | UInt | 历史原因，仍保留该参数，推荐使用下面参数unVpcId。 私有网络ID，如果不传则默认选择基础网络。|
| unVpcId | 否 | String | 私有网络ID，如果不传则默认选择基础网络，请使用[私有网络列表](https://cloud.tencent.com/doc/api/245/1372) 查询 返回的unVpcId为准，如：vpc-kd7d06of|
| subnetId | 否 | UInt | 历史原因，仍保留该参数，推荐使用下面参数unSubnetId。私有网络下的子网ID，如果设置了 vpcId，则 subnetId 必填。|
| unSubnetId | 否 | String | 基础网络下， subnetId无效； VPC子网下，取值以查询[查询子网列表](https://cloud.tencent.com/document/product/215/1371) 返回的unSubnetId为准，如：subnet-3lzrkspo|
| projectId | 否 | UInt | 项目ID，取值以用户账户>用户账户相关接口查询>[项目列表](https://cloud.tencent.com/doc/api/403/4400)返回的projectId为准|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| data | Array |返回的订单数组|

data 数组的结构：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.dealId | String | 订单号，通过 [DescribeRedisDealDetail](https://cloud.tencent.com/doc/api/260/5329) 可以查询订单详情 |

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11052|UserNotInWhiteList|用户不在白名单中|
|10000|NoRedisService|请求的区域暂时不提供redis服务|
|11062|NoTypeIdRedisService|请求的区域暂时不提供请求类型的redis服务|
|11053|InvalidInstanceTypeId|请求购买的实例类型错误（TypeId 1:集群版；2:主从版,即原主从版)|
|10703|InvalidMemSize| 请求的容量不在售卖规格中（memSize应为1024的整数倍，单位：MB）|
|11063|MemSizeNotInRange|请求的容量不在售卖容量范围内（请用[查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口查询售卖容量限制）|
|11065|PeriodExceedMaxLimit|购买时长超过最大时长限制|
|11066|PeriodLessThanMinLimit|购买时长小于最小时长限制|
|11064|GoodsNumNotInRange| 一次购买的实例数超过售卖数量限制（请用[查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口查询购买实例数限制）|
|11067|OnlyVPCOnSpecZoneId|请求的地区目前只提供VPC网络下的redis服务|
|11054|InvalidSubnetId|VPC网络下的子网ID不存在|
|10501|PasswordEmpty|密码为空|
|11058|PasswordRuleError|密码规则错误，密码必须是8-16位字符，且至少包含字母、数字和字符（!@#%^*()）中的两种|
|100207|OperationConstraints.AccountBalanceNotEnough|账号余额不足，请充值|

## 5. 示例
输入
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=CreateRedis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&zoneId=100002
&typeId=1
&memSize=1024
&goodsNum=1
&period=2
&password=49A2d!e@f12e
</pre>
输出
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
	"data":{
		"dealId":"432583"
	}
}
```
