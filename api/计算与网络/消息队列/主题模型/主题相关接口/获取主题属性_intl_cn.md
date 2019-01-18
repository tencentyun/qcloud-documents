## 1. 接口描述

本接口 (GetTopicAttributes) 用于获取某个已创建主题的属性。返回属性除了创建主题时设置的可设置属性外，还可以取到主题创建时间，最后一次修改主题属性时间，以及主题中消息的统计数据（近似值）。

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


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 0：表示成功，4440：主题不存在，其他返回值的含义可以参考 [错误码](/doc/api/431/5903)。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求 Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| msgCount| Int| 当前该主题中消息数目（消息堆积数)。|
| maxMsgSize| Int| 消息最大长度。取值范围1024-65536 Byte（即1-64K），默认值65536。|
| msgRetentionSeconds| Int| 消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天(86400秒)，该属性不能修改。|
| createTime| Int| 主题的创建时间。返回Unix时间戳，精确到秒。|
| lastModifyTime| Int| 最后一次修改主题属性的时间。返回Unix时间戳，精确到秒。|
|filterType|Int|描述用户创建订阅时选择的过滤策略：<br>filterType =0 表示用户使用filterTag 标签过滤；<br>filterType = 1 表示用户使用bindingKey 过滤。|

## 4. 示例

输入：

```
 https://domain/v2/index.php?Action=GetTopicAttributes
 &topicName=test-topic-123
 &<公共请求参数>
```

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"msgCount":234
"maxMsgSize": 65536,
"msgRetentionSeconds": 1296000,
"createTime":1462268960,
"lastModifyTime": 1462269960,
"filterType":0
}
```






