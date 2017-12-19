## 1. 接口描述

本接口 (DeleteMessage) 用于删除已经被消费过的消息，消费者需将上次消费后得到的 ReceiptHandle 作为参数来定位要删除的消息。本操作只有在 NextVisibleTime 之前执行才能成功；如果过了 NextVisibleTime，消息重新变回 Active 状态，ReceiptHandle 就会失效，删除失败，需重新消费获取新的 ReceiptHandle。并发消费时，如果消息被其中一个消费者删除了，其他的消费者再也无法获取得到被删除的消息。

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
| receiptHandle | 是| String| 上次消费返回唯一的消息句柄，用于删除消息。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 0：表示成功，others：错误，详细错误见下表。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|


<table class="t">
<tbody><tr>
<th> <b>错误代码</b>
</th><th> <b>模块错误代码</b>
</th><th> <b>英文提示</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> 4430
</td><td> 10260
</td><td> receipt handle is invalid
</td><td> 消息句柄无效。句柄失效原因，详见<a href="https://cloud.tencent.com/doc/api/431/5840">删除消息</a>。
</td></tr>
<tr>
<td> 4000
</td><td> 10470
</td><td> receiptHandle error
</td><td> receiptHandle错误。receiptHandle是字符串化
</td></tr>

</tbody></table>

注意：上表所列错误码是接口特有错误码，如果您要查找的错误码不在其中，可能在[公共错误码](https://cloud.tencent.com/document/product/406/5903)中。

## 4. 示例

输入：

<pre>
 https://domain/v2/index.php?Action=DeleteMessage
 &queueName=test-queue-123
 &receiptHandle=3423452345
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555"
}
```






