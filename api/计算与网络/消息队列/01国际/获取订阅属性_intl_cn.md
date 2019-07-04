## 1. 接口描述

本接口 (GetSubscriptionAttributes) 用于获取某个已创建订阅的属性。

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
| topicName| 是| String| 主题名字，在单个地域同一帐号下唯一。 主题名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| subscriptionName| 是| String| 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 0：表示成功，其他返回值的含义可以参考 [错误码](/doc/api/431/5903)。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| topicOwner| String| 订阅拥有者的appid。|
| msgCount| Int| 该订阅待投递的消息数。|
| protocol|String| 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。|
| endpoint| String| 接收通知的endpoint，根据协议protocol区分：对于http，endpoint必须以“http://”开头，host可以是域名或IP；对于queue，则填queueName。|
| notifyStrategy| String| 向endpoint推送消息出现错误时，CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s...由于Topic消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是EXPONENTIAL_DECAY_RETRY。|
| notifyContentFormat| String| 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果protocol是queue，则取值必须为SIMPLIFIED。如果protocol是http，两个值均可以，默认值是JSON。|
| createTime| Int| 订阅的创建时间。返回Unix时间戳，精确到秒。|
| lastModifyTime| Int| 最后一次修改订阅属性的时间。返回Unix时间戳，精确到秒。|
|bindingKey|String 数组| 表示订阅接收消息的过滤策略。|



## 4. 示例

输入：

```
 https://domain/v2/index.php?Action=GetSubscriptionAttributes
 &topicName=test-topic-123
 &subscriptionName=test-subscription-123
 &<公共请求参数>
```

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"topicOwner":"1231884",
"msgCount":234,
"protocol":"http",
"endpoint":"http://testhost/testpath",
"notifyStrategy":"EXPONENTIAL_DECAY_RETRY",
"notifyContentFormat":"SIMPLIFIED",
"createTime":1462268960,
"lastModifyTime": 1462269960
}
```






