

## 简介

HTTP Request 连接器作为 HTTP 客户端，可以发起 HTTP 请求并将得到的响应作为消息传递给下一个组件。

## 连接器配置
- 基本配置：HTTP Request 连接器基本配置中包括描述、请求域名、请求协议、请求端口、最大重定向次数以及公共请求路径，其中请求域名、请求协议、请求端口、最大重定向次数、公共请求路径为必填项。
![](https://main.qcloudimg.com/raw/0d256b0db4d9846d6499144be429132f.png)
- 高级配置：HTTP Request 连接器高级配置中包括安全网关配置，用于内网域名/IP 请求。
![image-20210325195344105](https://main.qcloudimg.com/raw/7c3e99e63748c9907d8f9891527da748/image-20210325195344105.png)
- 上述连接器配置参数相关描述如下表所示：

| 参数         | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ------------ | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 请求域名     | string   | 对应的请求域名                                               | 是           | 无         |
| 请求协议     | string   | 下拉框选择请求协议 HTTPS/HTTP                                 | 是           | HTTPS      |
| 请求端口     | string   | 请求端口，1-65535，默认443，与请求协议联动，HTTP 协议默认会是80 | 是           | 443        |
| 最大重定向数 | int      | 重定向次数，最小值0，最大值1                             | 是           | 1          |
| 公共请求路径 | string     | 请求的公共路径，多次请求的路径中相同的部分可配置为公共请求路径                           | 是           | /         |
| 安全网关名称 | string   | 直接请求内网域名/IP 时，需要绑定安全网关                      | 否           | 无         |

## 操作说明

HTTP Request 操作配置包括基本配置、高级配置两项：
![image-20210426210924935](https://main.qcloudimg.com/raw/5ab2b4ee6ca98f500bdf202bf41ea74d/image-20210426210924935.png)

<dx-tabs>
::: 基础配置参数描述
<table>
<thead>
<tr>
<th>参数</th>
<th>参数类型</th>
<th>描述</th>
<th><strong>是否必填</strong></th>
<th><strong>默认值</strong></th>
</tr>
</thead>
<tbody><tr>
<td>请求路径</td>
<td>string/表达式</td>
<td>用于指定发送请求的路径</td>
<td>是</td>
<td>/</td>
</tr>
<tr>
<td>请求方法</td>
<td>string</td>
<td>下拉单选指定发送请求的方法，全集为：GET、POST、PUT、PATCH、DELETE、HEAD</td>
<td>是</td>
<td>GET</td>
</tr>
<tr>
<td>请求头</td>
<td>表达式</td>
<td>用于指定发送请求的请求头，结构为：dict&lt;string,list<string>&gt;</string></td>
<td>否</td>
<td>无</td>
</tr>
<tr>
<td>请求参数</td>
<td>表达式</td>
<td>用于指定发送请求的请求参数，结构为：dict&lt;string,string&gt;</td>
<td>否</td>
<td>无</td>
</tr>
<tr>
<td>请求体</td>
<td>string/表达式</td>
<td>用于指定发送请求的请求体，非 GET、HEAD 方法是设置，支持字面量和表达式，默认是消息的 payload</td>
<td>否</td>
<td>无</td>
</tr>
</tbody></table>

:::
::: 高级配置参数描述
| 参数         | 参数类型 | 描述                                                         | 是否必填 | 默认值     |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ---------- |
| 消息属性     | string   | 下拉框选择输出消息绑定的属性，HTTP Request 只支持绑定 payload  | 否       | payload    |
| 类型选择     | string   | 下拉框选择输出消息 payload 绑定的数据类型，包括 message 内置数据类型和自定义数据类型 | 否       | 空         |
| 数据消费模式 | string   | 下拉框选择是否对消息数据进行持久化处理：<br/>repeatable：默认处理方式，消息数据可在一次触发中持续重复使用<br/>non-repeatable：数据一次性消费，用于大文件数据的流式高效处理，暂时支持 JSON 数组类型，其超过5M时建议选择该模式 | 否       | repeatable |
:::
</dx-tabs>


## 输出

HTTP Request 请求的响应返回后，会将响应结果生成对应的消息传递给下一个组件。其中，响应的基本信息、Header、Query 参数、Path 参数会放到消息的 attributes 中，响应的 body 会放到消息的 payload 中。

**HTTP Request 输出消息描述**

<table>
<thead>
<tr>
<th>消息属性</th>
<th>值</th>
</tr>
</thead>
<tbody><tr>
<td>payload</td>
<td>响应 body 保存在 payload 中，支持所有内置消息类型和自定义消息类型，其中 application/json、application/xml、application/yaml、application/x-www-form-urlencoded、multipart/form-data 等结构的 payload 支持在表达式中结构化访问</td>
</tr>
<tr>
<td>error</td>
<td>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息</td>
</tr>
<tr>
<td>attributes</td>
<td>保存响应的属性值，具体包括：<br>statusCode：响应的状态码，例如：200<br>reasonPhrase：响应的文本描述，例如：OK<br>headers：响应的 header，结构为： dict&lt;string,list<string>&gt;<br>cookies：响应的 cookie，结构为： dict&lt;string,string&gt;，解析 Cookies 逻辑比较常见，可通过该数据直接读取</string></td>
</tr>
<tr>
<td>variables</td>
<td>默认为空</td>
</tr>
</tbody></table>

## 案例

1. 组件筛选 HTTP Request。
![image-20210426211753938](https://main.qcloudimg.com/raw/8db8b3da512cc211fc8f0dda96f1b586/image-20210426211753938.png)
2. 新建并配置 HTTP Request 连接器，请求域名`www.qq.com`。
![image-20210426211917399](https://main.qcloudimg.com/raw/5d3d30dde98c734555b4099f6a3ce978/image-20210426211917399.png)
![image-20210426212034829](https://main.qcloudimg.com/raw/e72c3ac6c91d37d0111df93d6c081da7/image-20210426212034829.png)
3. 使用操作配置。
![image-20210426212147841](https://main.qcloudimg.com/raw/78af82d495104beca974fe9c73ed22d5/image-20210426212147841.png)
4. 发布并触发。浏览器访问触发对应流，可以直接跳转至腾讯首页。
![](https://main.qcloudimg.com/raw/1b04a28805e20f3871622c26836cb782.png)
 - 同时，应用测试模式下可以看到 HTTP Request 对应的 attributes。
![](https://main.qcloudimg.com/raw/4a7099444248e9c65bb8abee04adeff5/image-20210426212733856.png)
