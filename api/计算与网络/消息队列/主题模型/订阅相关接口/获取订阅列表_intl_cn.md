## 1. 接口描述

本接口 (ListSubscriptionByTopic) 该接口用于列出用户某主题下的订阅列表，可分页获取数据。

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
| searchWord| 否| String| 用于过滤订阅列表，后台用模糊匹配的方式来返回符合条件的订阅列表。如果不填该参数，默认返回帐号下的所有订阅。|
| offset| 否| Int| 分页时本页获取订阅列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。取值范围0-1000。|
| limit| 否| Int| 分页时本页获取订阅的个数，该参数取值范围0-100。如果不传递该参数，则该参数默认为20。|

> <front style="color:red">offset，limit的含义与sql的offset，limit一致。</front>


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 请参考 [错误码](/doc/api/431/5903)|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| totalCount| Int| 用户帐号下本次请求返回的主题总数，而非分页后本页获取的主题数量。|
| subscriptionList| Array| 主题列表信息，每个元素表示一个主题的信息。|


topicList定义如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| subscriptionId| String| 订阅Id。订阅Id在拉取监控数据时会用到。|
| subscriptionName| String| 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| protocol| String| 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。|
| endpoint| String| 接收通知的endpoint，根据协议protocol区分：对于http，endpoint必须以“http://”开头，host可以是域名或IP；对于queue，则填queueName。|


## 4. 示例

输入：

```
 https://domain/v2/index.php?Action=ListSubscriptionByTopic
 &searchWord=abc
 &<公共请求参数>
```

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"totalCount":2
"topicList":
[
{
"subscriptionId":"subsc-sdkfl",
"subscriptionName":"test-sub2",
"protocol":"http"
"endpoint":"http://testhost/testpath"
}
,
{
"subscriptionId":"subsc-34lasdk",
"subscriptionName":"test-sub1",
"protocol":"queue"
"endpoint":"test-queue-name"
}
]
}
```






