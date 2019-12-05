## 1. 接口描述

本接口 (SetQueueAttributes) 用于修改消息队列的属性。<font color="red">需要注意的是，队列名称不可以修改</font>

外网接口请求域名：<font style="color:red">cmq-queue-region.api.qcloud.com</font>

内网接口请求域名：<font style="color:red">cmq-queue-region.api.tencentyun.com</font>

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
| maxMsgHeapNum| 否| Int| 最大堆积消息数。取值范围在公测期间为 `1,000,000 - 10,000,000`，正式上线后范围可达到 `1000,000-1000,000,000`。默认取值在公测期间为 `10,000,000`，正式上线后为 `100,000,000`。|
| pollingWaitSeconds| 否| Int| 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。|
| visibilityTimeout| 否| Int| 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。|
| maxMsgSize| 否| Int| 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。|
| msgRetentionSeconds| 否| Int| 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。|
| rewindSeconds | 否|Int|消息最长回溯时间，取值范围0-msgRetentionSeconds，消息的最大回溯之间为消息在队列中的保存周期，0表示不开启消息回溯。|
|deadLetterPolicy|否|string|可选参数，死信队列策略配置参数，不填默认不开启死信队列功能。必须是Json格式的字符串（json.dump后的值），包含参数有：deadLetterQueue、policy、maxReceiveCount、maxTimeToLive，具体定义如下字段描述。|
|deadLetterPolicy:: deadLetterQueue|是|string|死信队列的名称，条件：必须是同地域、同帐号下的队列；该队列本身没有设置死信队列（不允许嵌套）；该队列被指定为其他队列的死信队列的次数未达到上限，目前上限为6个队列。|
|deadLetterPolicy::policy|是|int|死信策略，0：消息被多次消费未删除；1：Time-To-Live 过期。|
|deadLetterPolicy:: maxReceiveCount|否|int|Policy=0时是必填参数。最大接收次数，支持设定值为1-1000次。|
|deadLetterPolicy:: maxTimeToLive|否|int|Policy=1时是必填参数。最大未消费过期时间，允许设置5min-12小时，单位为秒，且必须小于消息保留周期msgRetentionSeconds的值。|

## 3. 输出参数

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
|deadLetterPolicy|string|可选参数，死信队列策略配置参数，不填默认不开启死信队列功能。必须是Json格式的字符串（json.dump后的值），包含参数有：deadLetterQueue、policy、maxReceiveCount、maxTimeToLive，具体定义如下字段描述。|
|deadLetterPolicy:: deadLetterQueue|string|死信队列的Id|
|deadLetterPolicy::policy|int|死信策略，0：消息被多次消费未删除；1：Time-To-Live 过期。|
|deadLetterPolicy:: maxReceiveCount|int|最大接收次数，支持设定值为1-1000次。|
|deadLetterPolicy:: maxTimeToLive|int|最大未消费过期时间，允许设置5min-12小时，单位为秒，且必须小于消息保留周期msgRetentionSeconds的值。|

## 4. 示例

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






