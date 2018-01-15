## 1. 接口描述

本接口 (BatchSendMessage) 用于发送批量（目前最多16条）消息到指定的队列。

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
| queueName| 是| String| 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| msgBody.n| 是| String| 消息正文。表示这一批量中的一条消息。目前批量消息数量不能超过 16 条。<br><br>为方便用户使用，n从0开始或者从1开始都可以，但必须连续，例如发送两条消息，可以是(msgBody.0, msgBody.1)，或者(msgBody.1, msgBody.2)。<br><br>注意：由于目前限制所有消息大小总和（不包含消息头和其他参数，仅msgBody）不超过 64k，所以建议提前规划好批量发送的数量。 |
|delaySeconds|否|int|单位为秒，表示该消息发送到队列后，需要延时多久用户才可见。（该延时对一批消息有效，不支持多对多映射）|
## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int |0：表示成功，others：错误，详细错误见下表。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 Id，出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| msgList| Array| 服务器生成消息的唯一标识 Id列表，每个元素是一条消息的信息。|

msgList定义如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| msgId| String| 服务器生成消息的唯一标识 Id。|

<table class="t">
<tbody><tr>
<th> <b>错误代码</b>
</th><th> <b>模块错误代码</b>
</th><th> <b>英文提示</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> 4400
</td><td> 10230
</td><td> exceed maximum message size
</td><td> 存在至少一条消息达到了最大消息大小限制。可以通过 <a  href="https://cloud.tencent.com/doc/api/431/5834">GetQueueAttributes</a> 接口查看队列的最大消息大小。
</td></tr>
<tr>
<td> 4000
</td><td> 10120
</td><td> message body can't be empty
</td><td> msgBody的消息体不能为空。至少是1Byte。
</td></tr>
<tr>
<td> 4410
</td><td> 10240
</td><td> reach maximum retention number of message
</td><td> 达到队列的最大消息堆积数。可以通过<a  href="https://cloud.tencent.com/doc/api/431/5834">GetQueueAttributes</a>接口查看队列的最大消息堆积数。
</td></tr>
<tr>
<td> 4470
</td><td> 10300
</td><td> total message size exceed 64k
</td><td> 所有消息体大小之和不能超过64k。在批量接口中，所有消息体大小之和（仅msgBody）可能超过64k，为减轻网络流量的压力和其他用户的使用体验，我们不得不对此进行限制。如果碰到此错误，建议减少批量的数量。
</td></tr>

</tbody></table>

注意：上表所列错误码是接口特有错误码，如果您要查找的错误码不在其中，可能在[公共错误码](https://cloud.tencent.com/document/product/406/5903)中。


## 4. 示例

输入：

<pre>
 https://domain/v2/index.php?Action=BatchSendMessage
 &queueName=test-queue-123
 &msgBody.1=helloworld1
 &msgBody.2=helloworld2
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"msgList":
  [
    {
      "msgId":"123345346"
    },
    {
       "msgId":"456436346"
    }
  ]
}
```






