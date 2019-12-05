## 1. 接口描述

本接口 (SetSubscriptionAttributes) 用于修改消息订阅的属性。

外网接口请求域名：<font style="color:red">cmq-topic-region.api.qcloud.com</font>

内网接口请求域名：<font style="color:red">cmq-topic-region.api.tencentyun.com</font>

> 任何时候，包括内测期间，如果使用外网域名产生公网下行流量，都会收取流量费用。 所以强烈建议服务在腾讯云上的用户使用**内网**域名，内网不会产生流量费用。

- region 需用具体地域替换：gz（广州），sh（上海），bj（北京）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。
- 外网域名请求既支持http，也支持https。内网请求仅支持http。
- 输入参数有些是可选的，不填取默认值。
- 输出参数在成功情况下所有出参都会返回给用户；失败情况下，至少会有code, message, requestId返回。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/doc/api/431/5883)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| topicName| 是| String| 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| subscriptionName| 是| String| 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| notifyStrategy| 否| String| 向endpoint推送消息出现错误时，CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s...由于Topic消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是EXPONENTIAL_DECAY_RETRY。|
| notifyContentFormat| 否| String| 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果protocol是queue，则取值必须为SIMPLIFIED。如果protocol是http，两个值均可以，默认值是JSON。|
| filterTag.n|否| String| 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与[(Batch)PublishMessage](https://cloud.tencent.com/document/api/406/7411)的msgTag参数配合使用，规则：1）如果filterTag没有设置，则无论msgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果filterTag数组有值，则只有数组中至少有一个值在msgTag数组中也存在时（即filterTag和msgTag有交集），订阅才接收该发布到Topic的消息；3）如果filterTag数组有值，但msgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时filterTag和msgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。|
|bindingKey.n|是|String 数组|bindingKey数量不超过5个， 每个bindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个bindingKey最多含有15个“.”， 即最多16个词组。|
## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int |0：表示成功，others：错误，详细错误见下表。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|

<table class="t">
<tbody><tr>
<th> <b>错误代码</b>
</th><th> <b>模块错误代码</b>
</th><th> <b>英文提示</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> 4000
</td><td> 10490
</td><td> number of filterTag exceed limit
</td><td> filterTag 数量超过限制。目前最多是 5 个。
</td></tr>
<tr>
<td> 4000
</td><td> 10520
</td><td> undefined notify retry stragety
</td><td> 未定义的消息推送重试策略。请检查拼写是否有误。
</td></tr>
<tr>
<td> 4000
</td><td> 10530
</td><td> undefined notify content format
</td><td> 未定义的消息推送格式。请检查拼写是否有误。
</td></tr>

</tbody></table>

注意：上表所列错误码是接口特有错误码，如果您要查找的错误码不在其中，可能在[公共错误码](https://cloud.tencent.com/document/product/406/5903)中。

## 4. 示例

输入：

```
 https://domain/v2/index.php?Action=SetSubscriptionAttributes
 &topicName=test-Topic-123
 &subscriptionName=test-subscription-123
 &filterTag.0=football
 &<公共请求参数>
```

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555"
}
```






