## 1. 接口描述
本接口（InquiryRedisPrice）用于查询新购和续费实例价格， 查询升级实例的价格，请参考 [查询升级实例价格](http://www.qcloud.com/doc/api/260/5327) 。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/260/1753' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为InquiryRedisPrice。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| zoneId | 是 | UInt | 实例所属可用区, 取值以[查询售卖可用区](http://www.qcloud.com/doc/api/260/4951)返回值为准 |
| typeId | 是 | UInt | 实例类型：1 – 集群版，2 – 单机版|
| memSize | 是 | UInt | 容量大小, 1024的整数倍，单位：MB， 大小限制以[查询售卖规格](http://www.qcloud.com/doc/api/260/4974)接口返回为准 |
| goodsNum | 是 | UInt | 实例数量，数量限制以[查询售卖规格](http://www.qcloud.com/doc/api/260/4974)接口返回为准 |
| period | 是 | UInt | 购买或续费时长, 单位：月， 范围 [1,36]|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| data | Array | 返回的价格数组 |

**data数组结构：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.price | Int | 购买或者续费实例的总费用，单位：分 | 

## 4. 示例
输入
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=InquiryRedisPrice
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&zoneId=100002
&typeId=1
&memSize=1024
&goodsNum=1
&period=2
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "price": 16000
    }
}
```