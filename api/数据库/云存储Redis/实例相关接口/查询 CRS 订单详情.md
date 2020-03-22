## 1. 接口描述
本接口(DescribeRedisDealDetail)用于查询订单详情。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为DescribeRedisDealDetail。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| dealIds.n | 是 | String | 订单号组成的数组，数组下标从0开始 |


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| dealDetails | Array | 返回的订单数组 |

**dealDetails数组结构：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| dealDetails.dealId | String | 订单号ID，调用云API时使用此ID |
| dealDetails.dealName | String | 长订单ID，反馈订单问题给官方客服使用此ID |
| dealDetails.zoneId | Int | 可用区ID|
| dealDetails.goodsNum | Int | 订单关联的实例数 |
| dealDetails.creater | String | 创建用户uin |
| dealDetails.creatTime | String | 订单创建时间 |
| dealDetails.overdueTime | String | 订单超时时间 |
| dealDetails.endTime | String | 订单完成时间 |
| dealDetails.status | Int | 订单状态<br>1：未支付<br>2:已支付，未发货<br>3:发货中<br>4:发货成功<br>5:发货失败<br>6:已退款<br>7:已关闭订单<br>8:订单过期<br>9:订单已失效<br>10:产品已失效<br>11:代付拒绝<br>12:支付中 |
| dealDetails.description | String | 订单状态描述 |
| dealDetails.price | Int | 订单实际总价，单位：分 |
| dealDetails.goodsDetail | Array | 返回的数组，不同订单的goodsDetail不相同 |

**创建实例goodsDetail数组：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| memSize| int | 实例容量， 单位:MB|
| timeSpan | int | 购买时长， 单位以：timeUnit为准|
| timeUnit | String | 购买时长单位， m- 月， d - 天|
| redisIds | Array | 关联的redisId列表|

**续费实例goodsDetail数组：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| curDeadline| String |  续费前，实例到期时间|
| memSize| int | 实例容量， 单位:MB|
| timeSpan | int | 购买时长， 单位以：timeUnit为准|
| timeUnit | String | 购买时长单位， m- 月， d - 天
| redisIds | Array | 关联的redisId列表|

**升级实例goodsDetail数组：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| oldMemSize | int | 升级前实例容量， 单位:MB|
| newMemsize | int | 升级后实例容量， 单位:MB|
| redisIds | Array | 关联的redisId列表|

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11059|DealIdNotFound|订单号不存在|

## 5. 示例
输入
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=DescribeRedisDealDetail
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&dealIds.0=432583
&dealIds.1=432586
&dealIds.2=432587
</pre>
输出
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success",
    "dealDetails": [
        {
            "dealId": "432583",
            "dealName": "20160712110021",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3227991405",
            "creatTime": "2016-07-12 21:10:11",
            "overdueTime": "2016-07-27 21:10:11",
            "endTime": "2016-07-12 21:11:17",
            "status": 4,
            "description": "发货成功",
            "price": 16000,
            "goodsDetail": {
                "memSize": 1024,
                "timeSpan": 2,
                "timeUnit": "m",
                "redisIds": [
                    "crs-ifmymj41"
                ]
            }
        },
        {
            "dealId": "432586",
            "dealName": "20160712110027",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3227991405",
            "creatTime": "2016-07-12 22:05:43",
            "overdueTime": "2016-07-27 22:05:43",
            "endTime": "2016-07-12 22:05:45",
            "status": 4,
            "description": "发货成功",
            "price": 8000,
            "goodsDetail": {
                "curDeadline": "2016-09-12 21:10:13",
                "memSize": 1024,
                "timeSpan": 1,
                "timeUnit": "m",
                "redisIds": [
                    "crs-ifmymj41"
                ]
            }
        },
        {
            "dealId": "432587",
            "dealName": "20160712110029",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3227991405",
            "creatTime": "2016-07-12 22:15:55",
            "overdueTime": "2016-07-27 22:15:55",
            "endTime": "2016-07-12 22:16:59",
            "status": 4,
            "description": "发货成功",
            "price": 24460,
            "goodsDetail": {
                "oldMemSize": 1024,
                "newMemsize": 2048,
                "redisIds": [
                    "crs-ifmymj41"
                ]
            }
        }
    ]
}
```
