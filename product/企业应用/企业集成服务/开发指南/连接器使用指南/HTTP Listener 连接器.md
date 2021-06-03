

## 简介

HTTP Listener 连接器可以接收 HTTP 请求并生成消息，从而作为 Trigger 触发集成流。

## 连接器配置
- 基本配置：HTTP Listener 连接器基本配置中包括描述和监听域名两项，其中监听域名为必填项。
![image-20210325113903169](https://main.qcloudimg.com/raw/563b20e4f97052d140765120acbd8ca1/image-20210325113903169.png)
- 高级配置：HTTP Listener 连接器高级配置中包括 IP 白名单和认证配置两项。
![image-20210325113953686](https://main.qcloudimg.com/raw/e36433e9aef2d83faf013de192e5f1de/image-20210325113953686.png)
- 上述连接器配置参数相关描述如下表所示：

| 参数     | 数据类型              | 描述                                                         | 是否必填 | 默认值|
| :------- | :-------------------- | :----------------------------------------------------------- | :----------- | :--------- |
| 监听域名 | string                | Listener 的监听域名，只支持由大小写字母、数字组成，不得超过15个字符。此处指定的为域名前缀，完整的域名取决于部署集群的配置，例如：配置域名为 prefix，则发布之后域名为`prefix-$appId.ipaas.$region.myqcloud.com`，应用测试域名为`prefix-$appId.ipaas.sandbox.myqcloud.com`，其中 $appId 为当前用户 appId，$region 表示发布的地域，例如：发布地域选择“天津”时， $region 为“ap-tianjin” | 是           | 无         |
| IP 白名单 | CIRD/点分十进制字符串 | 客户端 IP 白名单限制                                           | 否           | 无         |
| 认证配置 | 账号&密码字符串       | HTTP 身份认证，默认 Basic 模式                                  | 否           | 无         |

## 操作说明

HTTP Listener 操作配置包括基本配置、高级配置、响应配置三项：
![image-20210426110043222](https://main.qcloudimg.com/raw/9f94faac33be924c77a68236234d81d7/image-20210426110043222.png)

<dx-tabs>
::: 基础配置参数描述
| 参数     | 参数类型 | 描述                                                         | 是否必填 | 默认值 |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 监听路径 | string   | Listener 通过监听路径区分不同的 URI，同时支持三种模式路径匹配：通配符 * 、变量匹配、精确匹配。例如：监听路径设置为 /user/{userId}/\*时，可以匹配 /user/123/testpath，也可以匹配 /user/123 和 /user/123/testpath/testpath1，即{}可以匹配一级目录，*"*"匹配多级目录。当多个请求同时匹配一个模式时，会优先匹配更具体的，同等条件下，优先匹配第一个。 | 是           | “/”        |
| 请求方法 | string   | 下拉框多选，全集为：全部、GET、POST、PUT、PATCH、DELETE、HEAD | 是           | 全部       |
:::
::: 高级配置参数描述
| 参数         | 参数类型 | 描述                                                         | 是否必填 | 默认值     |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ---------- |
| 消息属性     | string   | 下拉框选择输出消息绑定的属性，HTTP Listener 只支持绑定 payload | 否       | payload    |
| 类型选择     | string   | 下拉框选择输出消息 payload 绑定的数据类型，包括 message 内置数据类型和自定义数据类型 | 否       | 空         |
| 数据消费模式 | string   | 下拉框选择是否对消息数据进行持久化处理：<br/>repeatable：默认处理方式，消息数据可在一次触发中持续重复使用<br/>non-repeatable：数据一次性消费，用于大文件数据的流式高效处理，暂时支持 JSON 数组类型，其超过5M时建议选择该模式 | 否       | repeatable |
:::
::: 响应配置参数描述
| 正常响应/错误响应 | 参数类型                     | 描述             | 是否必填 | 默认值                         |
| ----------------- | ---------------------------- | ---------------- | ------------ | ---------------------------------- |
| 状态码            | int/表达式                   | 响应的 HTTP 状态码 | 否           | 正常：200，错误：500               |
| 响应头            | 表达式，仅支持 dict 和 multimap | 响应的 HTTP 头     | 否           | 无                                 |
| 响应体            | 表达式                       | 响应的 body 体     | 否           | 正常：msg.payload，错误：msg.error |

:::
</dx-tabs>


## 输出

HTTP Listener 生成的消息中，会将接收到请求的基本信息、Header、Query 参数以及 Path 参数保存在消息的 attributes；接收到请求的 body 保存在消息的 payload；执行失败后，错误信息会保存在生成消息的 error。

**HTTP Listener 输出消息描述：**

| 消息属性   | 值                                                           |
| ---------- | ------------------------------------------------------------ |
| payload    | 请求 body 保存在 payload 中，支持所有内置消息类型和自定义消息类型，其中 application/json、application/xml、application/yaml、application/x-www-form-urlencoded、multipart/form-data 等结构的 payload 支持在表达式中结构化访问 |
| error      | 保存集成流执行结果中的错误，执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attributes | 保存接收到请求的属性值，具体如下个表格所示 |
| variables  | 默认为空                                                     |

**attributes 接收请求属性描述：**

<table>
<thead>
<tr>
<th>属性</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>header</td>
<td>请求的 header，结构为：dict&lt;string,list<string>&gt;</string></td>
</tr>
<tr>
<td>cookies</td>
<td>请求的 cookies，结构为：dict&lt;string,string&gt;，解析 Cookies 逻辑比较常见，可通过该数据直接读取</td>
</tr>
<tr>
<td>host</td>
<td>请求的 Host，例如：<code>xxx-$appId.ipaas.sadbox.qcloud.com</code></td>
</tr>
<tr>
<td>method</td>
<td>请求的 method，例如：GET、POST</td>
</tr>
<tr>
<td>requestUri</td>
<td>请求的原始 URI，包括 query 参数，例如：/api/v1/foo？sss=bbb</td>
</tr>
<tr>
<td>requestPath</td>
<td>请求的 Path，例如：/api/v1/foo</td>
</tr>
<tr>
<td>remoteAddr</td>
<td>请求是来源 IP，例如：127.0.0.1:1111</td>
</tr>
<tr>
<td>queryParams</td>
<td>请求的 query 参数，即 URI 中“？”后面的参数，结构为 dict&lt;string,list<string>&gt;</string></td>
</tr>
<tr>
<td>uriParams</td>
<td>请求的 path 参数，当监听路径中包含 {varName} 变量时，可以从该参数中获取，结构为 dict&lt;string,string&gt;</td>
</tr>
</tbody></table>


## 案例
1. Trigger 配置选择 HTTP Listener。
![image-20210426120942806](https://main.qcloudimg.com/raw/2a9d1ce396e84949d7adaa248061b515/image-20210426120942806.png)
2. 新建并配置 HTTP Listener 连接器。
![image-20210426121234475](https://main.qcloudimg.com/raw/896f5ee0a507a22f0274262a945d5d90/image-20210426121234475.png)
3. 配置必填项监听路径和监听方法。
![image-20210426121422813](https://main.qcloudimg.com/raw/13cddf55b9beefb501e03b5cc043bb41/image-20210426121422813.png)
4.发布并触发。
使用 POST 请求对应的 Listener，将请求 body 设置成 JSON 格式的{"key":"value"}，HTTP Listener 会默认响应 body 为消息的 payload，同时也是接收请求的 body：
![image-20210426122040758](https://main.qcloudimg.com/raw/ae5a566473b140cae97ce3ed62be5e1b/image-20210426122040758.png)
 - 应用测试模式下，可以清楚看到 payload 内容：
![image-20210426122435612](https://main.qcloudimg.com/raw/86c2400ba58b31a8c6079eafac526e6c/image-20210426122435612.png)
 - attributes：
![image-20210426122411179](https://main.qcloudimg.com/raw/3c601b1994094c29d7f604b7f557bb52/image-20210426122411179.png)

## 附录
HTTP Listener 错误描述如下： 

| 错误码 | 错误类型                              | 错误描述                  |
| :----- | ------------------------------------- | ------------------------- |
| 401    | HTTP:LISTENER_AUTHENTICATION_REQUIRED | 身份认证异常              |
| 403    | HTTP:LISTENER_CLIENT_IP_NOT_ALLOWED   | 请求 IP 白名单异常          |
| 404    | HTTP:LISTENER_NOT_FOUND               | 请求 URL 错误               |
| 500    | HTTP:SYSTEM_ERROR                     | 系统异常                  |
| 500    | HTTP:LISTENER_MODULE_ERROR            | 获取模块失败              |
| 500    | HTTP:LISTENER_RESOURCE_LIMIT_ERROR    | 资源管控                  |
| 500    | HTTP:LISTENER_OUT_OF_QUOTA            | 频率限制                  |
| 500    | HTTP:LISTENER_CONFIG_REF_ERROR        | 获取连接器配置异常        |
| 500    | HTTP:LISTENER_HEADERS_EVAL_ERROR      | 响应配置 Header 表达式异常  |
| 500    | HTTP:LISTENER_HEADERS_TYPE_ERROR      | 响应配置 Header 类型错误    |
| 500    | HTTP:LISTENER_SET_COOKIE_EVAL_ERROR   | 响应配置 Cookies 表达式异常 |
| 500    | HTTP:LISTENER_BODY_EVAL_ERROR         | 响应配置 Body 表达式异常    |



