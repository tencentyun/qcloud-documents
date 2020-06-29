## 1. 接口描述
本接口（InquiryRedisPrice）用于查询新购和续费实例价格， 查询升级实例的价格，请参考 [查询升级实例价格](http://cloud.tencent.com/doc/api/260/5327) 。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/api/239/7200' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为InquiryRedisPrice。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| zoneId | 是 | UInt | 实例所属可用区, 取值以[查询售卖可用区](http://cloud.tencent.com/doc/api/260/4951)返回值为准 |
| typeId | 是 | UInt | 实例类型：1 – 集群版，2 – 主从版|
| memSize | 是 | UInt | 容量大小, 1024的整数倍，单位：MB， 大小限制以[查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口返回为准 |
| goodsNum | 是 | UInt | 实例数量，数量限制以[查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口返回为准 |
| period | 是 | UInt | 购买或续费时长, 单位：月， 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| data | Array | 返回的价格数组 |

**data数组结构：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.price | Int | 购买或者续费实例的总费用，单位：分 | 

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11052|UserNotInWhiteList|用户不在白名单中|
|10000|NoRedisService|请求的区域暂时不提供redis服务|
|11062|NoTypeIdRedisService|请求的区域暂时不提供请求类型的redis服务|
|11053|InvalidInstanceTypeId|请求购买的实例类型错误（TypeId 1:集群版；2:主从版,即原主从版）|
|10703|InvalidMemSize| 请求的容量不在售卖规格中（memSize应为1024的整数倍，单位：MB）|
|11063|MemSizeNotInRange|请求的容量不在售卖容量范围内（请用[查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口查询售卖容量限制）|
|11065|PeriodExceedMaxLimit|购买时长超过最大时长限制|
|11066|PeriodLessThanMinLimit|购买时长小于最小时长限制|
|11064|GoodsNumNotInRange| 一次购买的实例数超过售卖数量限制（请用[查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口查询购买实例数限制）|


## 5. 示例
输入
```
https://redis.api.qcloud.com/v2/index.php?Action=InquiryRedisPrice
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&zoneId=100002
&typeId=1
&memSize=1024
&goodsNum=1
&period=2
```
输出
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
    "data":{
        "price": 16000
    }
}
```
