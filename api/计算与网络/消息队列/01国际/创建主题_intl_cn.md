## 1. 接口描述

本接口 (CreateTopic) 用于在用户账户下创建一个新主题。

外网接口请求域名：<font style="color:red">cmq-topic-region.api.qcloud.com</font>

内网接口请求域名：<font style="color:red">cmq-topic-region.api.tencentyun.com</font>

> 注：任何时候，包括内测期间，如果使用外网域名产生公网下行流量，都会收取流量费用。 所以强烈建议服务在腾讯云上的用户使用**内网**域名，内网不会产生流量费用。

- region 需用具体地域替换：gz（广州），sh（上海），bj（北京）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。
- 外网域名请求既支持 http，也支持 https；内网请求仅支持 http。
- 输入参数有些是可选的，不填则取默认值。
- 成功情况下，所有输出参数都会返回给用户；失败情况下，至少会返回 code、message及 requestId。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/doc/api/431/5883)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| topicName| 是| String| 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。|
| maxMsgSize| 否| Int| 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。|
|filterType|否|Int|用于指定主题的消息匹配策略：<br>filterType =1或为空， 表示该主题下所有订阅使用 filterTag 标签过滤；<br>filterType =2 表示用户使用 bindingKey 过滤。<br>注：该参数设定之后不可更改。|
## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int |  0：表示成功，others：错误，详细错误见下表。|
| message | String | 错误提示信息。|
| requestId| String| 服务器生成的请求Id。出现服务器内部错误时，用户可提交此 Id 给后台定位问题。|
| topicId| String| 主题的唯一标识Id。但是注意，云API接口都是通过名字而非ID去调用的。|

## 4. 错误码
<table class="t">
<tbody><tr>
<th> <b>错误代码</b>
</th><th> <b>模块错误代码</b>
</th><th> <b>英文提示</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> 4460
</td><td> 10550
</td><td> topic is already existed
</td><td> 同一帐号下存在同名 Topic
</td></tr>
<tr>
<td> 4000
</td><td> 10590
</td><td> topic name format error
</td><td> Topic 名字格式错误
</td></tr>
<tr>
<td> 4450
</td><td> 10610
</td><td> number of topics has reached the limit
</td><td> Topic 数量已经到达上限。目前最多是 1000 个。
</td></tr>
<tr>
<td> 6040
</td><td> 10660
</td><td> It will take some time to release resources of previous topic before you can create a new topic with the same name. Please try later.
</td><td> 创建同名主题失败。因为刚才删除同名主题需要释放资源，目前CMQ为了保证数据一致性，在删除主题之后，十秒内不能创建同名主题。
</td></tr>
</tbody></table>

注意：上表所列错误码是接口特有错误码，如果您要查找的错误码不在其中，可能在[公共错误码](https://cloud.tencent.com/document/product/406/5903)中。

## 5. 示例

输入：

```
 https://domain/v2/index.php?Action=CreateTopic
 &topicName=test-topic-123
 &<公共请求参数>
```

输出：

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"topicId":"topic-ajksdfasdowe"
}
```






