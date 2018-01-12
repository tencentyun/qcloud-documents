## 1. 接口描述

本接口 (PublishMessage) 用于发布一条消息到指定的主题。

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
| msgBody| 是| String| 消息正文。至少 1 Byte，最大长度受限于设置的主题消息最大长度属性。|
| msgTag.n|否| String| 消息过滤标签。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与[Subscribe](https://cloud.tencent.com/document/api/406/7414)接口的filterTag参数配合使用，规则：1）如果filterTag没有设置，则无论msgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果filterTag数组有值，则只有数组中至少有一个值在msgTag数组中也存在时（即filterTag和msgTag有交集），订阅才接收该发布到Topic的消息；3）如果filterTag数组有值，但msgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时filterTag和msgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。|
|routingKey|否|String|长度<=64字节，该字段用于表示发送消息的路由路径，最多含有15个“.”，即最多16个词组。<br>消息发送到topic类型的exchange上时不能随意指定routingKey。需要符合上面的格式要求，一个由订阅者指定的带有routingKey的消息将会推送给所有BindingKey能与之匹配的消费者，这种匹配情况有两种关系：<br>1 \*（星号），可以替代一个单词（一串连续的字母串）； <br>2 #（井号）：可以匹配一个或多个字符。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 0：表示成功，others：错误，详细错误见下表。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 Id，出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| msgId| String| 服务器生成消息的唯一标识 Id。|

## 4. 错误码
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
<td> 6030
</td><td> 10730
</td><td> no bindingKey or filterTag matches the routingKey or msgTag
</td><td> 没有订阅与本次发布的消息标签或者routingKey匹配，因此本次发布的消息不会投递给订阅者。
</td></tr>

<tr>
<td> 6030
</td><td> 10650
</td><td> topic has no subscription, please create a subscription before publishing message
</td><td> 本主题没有订阅者，在发布消息之前请创建订阅者。
</td></tr>
<tr>
<td> 4000
</td><td> 10700
</td><td> parameters lack of routingKey
</td><td> 缺少参数routingKey。
</td></tr>
<tr>
<td> 4000
</td><td> 10720
</td><td> too many msgTag
</td><td> msgTag太多。
</td></tr>

</tbody></table>

注意：上表所列错误码是接口特有错误码，如果您要查找的错误码不在其中，可能在[公共错误码](https://cloud.tencent.com/document/product/406/5903)中。

## 5. 示例

输入：

```
https://domain/v2/index.php?Action=PublishMessage
&topicName=test-topic-123
&msgBody=helloworld
&<公共请求参数>

```

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"msgId":"123345346"
}
```
