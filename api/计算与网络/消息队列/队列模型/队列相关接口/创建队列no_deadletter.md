## 接口描述
本接口（CreateQueue）用于在用户账户下创建一个新队列。
- 外网接口请求域名：`https://cmq-queue-{$region}.api.qcloud.com`
- 内网接口请求域名：`http://cmq-queue-{$region}.api.tencentyun.com`

上述**域名中的{$region}需用具体地域替换**：gz（广州）、sh（上海）、bj（北京）、shjr（上海金融）、szjr（深圳金融）、hk（中国香港）、cd（成都）、ca(北美)、usw（美西）、sg（新加坡）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。

>!任何时候（包括内测期间），如果使用外网域名产生公网下行流量，都会收取流量费用。 因此强烈建议服务在腾讯云上的用户使用**内网**域名，内网不会产生流量费用。


## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/doc/api/431/5883) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| queueName| 是| String| 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。|
| maxMsgHeapNum| 否| Int| 最大堆积消息数。取值范围在公测期间为`1,000,000 - 10,000,000`，正式上线后范围可达到 `1000,000-1000,000,000`。默认取值在公测期间为`10,000,000`，正式上线后为 `100,000,000`。|
| pollingWaitSeconds| 否| Int| 消息接收长轮询等待时间。取值范围200ms - 30s，默认值200ms。|
| visibilityTimeout| 否| Int| 消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。|
| maxMsgSize| 否| Int| 消息最大长度。取值范围1024 - 1048576 Byte（即1 - 1024K），默认值65536。|
| msgRetentionSeconds| 否| Int| 消息生命周期。取值范围60 - 1296000秒（1min-15天），默认值345600 (4天)。|
|rewindSeconds|否|Int|队列是否开启回溯消息能力，该参数取值范围 0-msgRetentionSeconds，即最大的回溯时间为消息在队列中的保留周期，0表示不开启。|

## 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 0：表示成功，others：错误，详细错误见 [公共错误码](https://cloud.tencent.com/document/product/406/5903)。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 ID。出现服务器内部错误时，用户可提交此 ID 给后台定位问题。|
| queueId| String| 队列的唯一标识 ID。|

## 错误码
请查看 [公共错误码](https://cloud.tencent.com/document/product/406/5903)。


## 示例

输入：
<pre>
 https://domain/v2/index.php?Action=CreateQueue
 &queueName=test-queue-123
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出：
```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"queueId":"queue-ajksdfasdowe"
}
```






