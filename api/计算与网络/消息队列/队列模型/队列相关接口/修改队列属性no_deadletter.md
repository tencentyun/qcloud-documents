## 接口描述

本接口 (SetQueueAttributes) 用于修改消息队列的属性。

**请参照下面说明将域名中的 {$region} 替换成相应地域：**
- 外网接口请求域名：`http(s)://cmq-queue-{$region}.api.qcloud.com`
- 内网接口请求域名：`http://cmq-queue-{$region}.api.tencentyun.com`

>**注意：**
>- 队列名称不可以修改。
>- 任何时候，包括内测期间，如果使用外网域名产生公网下行流量，都会收取流量费用。 所以强烈建议服务在腾讯云上的用户使用 **内网** 域名，内网不会产生流量费用。

**说明：**
- {$region}需用具体地域替换：gz（广州），sh（上海），bj（北京），shjr（上海金融），szjr（深圳金融），hk（香港）,ca(北美)，cd（成都），usw（美西），sg（新加坡）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。
- 外网域名请求既支持 http，也支持 https。内网请求仅支持 http。
- 输入参数有些是可选的，不填取默认值。
- 输出参数在成功情况下所有出参都会返回给用户；失败情况下，至少会有 code, message, requestId 返回。

## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| queueName| 是| String| 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| maxMsgHeapNum| 否| Int| 最大堆积消息数。取值范围在公测期间为 `1,000,000 - 10,000,000`，正式上线后范围可达到 `1000,000-1000,000,000`。默认取值在公测期间为 `10,000,000`，正式上线后为 `100,000,000`。|
| pollingWaitSeconds| 否| Int| 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。|
| visibilityTimeout| 否| Int| 消息可见性超时。取值范围 1-43200 秒（即 12 小时内），默认值 30。|
| maxMsgSize| 否| Int| 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。|
| msgRetentionSeconds| 否| Int| 消息保留周期。取值范围 60-1296000 秒（1min-15 天），默认值 345600 (4 天)。|
| rewindSeconds | 否|Int|消息最长回溯时间，取值范围 0-msgRetentionSeconds，消息的最大回溯之间为消息在队列中的保存周期，0 表示不开启消息回溯。|


## 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 0：表示成功，4440：队列不存在，其他返回值的含义可以参考 [错误码](/doc/api/431/5903)。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| maxMsgHeapNum| Int| 更改后的最大堆积消息数。|
| pollingWaitSeconds| Int| 更改后的消息接收长轮询等待时间。|
| visibilityTimeout| Int| 更改后的消息可见性超时。|
| maxMsgSize| Int| 更改后的消息最大长度。|
| msgRetentionSeconds| Int| 更改后的消息保留周期。|
| rewindSeconds |Int|更改后的最长消息回溯时间。|


## 示例

输入：

<pre>
 https://domain/v2/index.php?Action=SetQueueAttributes
 &queueName=test-queue-123
 &pollingWaitSeconds=20
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"queueId":"queue-ajksdfasdowe",
"maxMsgHeapNum":10000000,
"pollingWaitSeconds":20,
"visibilityTimeout":0,
"maxMsgSize":65536,
"msgRetentionSeconds":345600
}
```






