## 1. 接口描述

本接口 (ReceiveMessage) 用于消费队列中的一条消息，ReceiveMessage 操作会将取得的消息状态变成 inactive，inactive 的时间长度由队列属性 visibilityTimeout 指定（详见[CreateQueue接口](/doc/api/431/5832)）。 建议消费者在 visibilityTimeout 时间内消费成功后需要调用 (batch)DeleteMessage 接口删除该消息，否则该消息将会重新变成为 active 状态，此消息又可被消费者重新消费。

外网接口请求域名：<font style="color:red">cmq-queue-region.api.qcloud.com</font>

内网接口请求域名：<font style="color:red">cmq-queue-region.api.tencentyun.com</font>

> 任何时候，包括内测期间，如果使用外网域名产生公网下行流量，都会收取流量费用。 所以强烈建议服务在腾讯云上的用户使用**内网**域名，内网不会产生流量费用。

- region 需用具体地域替换：gz（广州），sh（上海），bj（北京）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。
- 外网域名请求既支持http，也支持https。内网请求仅支持http。
- 输入参数有些是可选的，不填取默认值。
- 输出参数在成功情况下所有出参都会返回给用户；失败情况下，至少会有code, message, requestId返回。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/document/product/295/7279
)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| queueName| 是| String| 队列名字，在单个地域同一帐号下唯一。 队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| pollingWaitSeconds| 否| Int| 本次请求的长轮询等待时间。取值范围 0-30 秒，如果不设置该参数，则默认使用队列属性中的pollingWaitSeconds值。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int |0：表示成功，others：错误，详细错误见下表。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| msgBody| String| 本次消费的消息正文。|
| msgId| String| 本次消费的消息唯一标识 Id。|
| receiptHandle| String| 每次消费返回唯一的消息句柄。用于删除该消息，仅上一次消费时产生的消息句柄能用于删除消息。|
| enqueueTime| Int| 消费被生产出来，进入队列的时间。返回Unix时间戳，精确到秒。|
| firstDequeueTime| Int| 第一次消费该消息的时间。返回Unix时间戳，精确到秒。|
| nextVisibleTime| Int| 消息的下次可见（可再次被消费）时间。返回Unix时间戳，精确到秒。|
| dequeueCount| Int| 消息被消费的次数。|

<table class="t">
<tbody><tr>
<th> <b>错误代码</b>
</th><th> <b>模块错误代码</b>
</th><th> <b>英文提示</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> 7000
</td><td> 10200
</td><td> no message
</td><td> 队列没有消息。严格来说，这种不是错误，用户可以忽略该错误，继续接收。
</td></tr>

<tr>
<td> 6070
</td><td> 10690
</td><td> too many unacked(inactive messages or delayed messages)
</td><td> 队列中有太多不可见或者延时消息，这里建议用户稍等一会再继续消费。
</td></tr>

</tbody></table>

注意：上表所列错误码是接口特有错误码，如果您要查找的错误码不在其中，可能在[公共错误码](https://cloud.tencent.com/document/product/406/5903)中。

## 4. 示例

输入：

<pre>
 https://domain/v2/index.php?Action=ReceiveMessage
 &queueName=test-queue-123
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"msgBody":"helloworld1",
"msgId":"123345346",
"receiptHandle": "283748239349283",
"enqueueTime": 1462351990,
"firstDequeueTime": 1462352990,
"nextVisibleTime": 1462352999,
"dequeueCount": 2
}
```






