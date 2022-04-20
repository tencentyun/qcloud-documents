## 简介

HTTP Request 连接器作为 HTTP 客户端，可以发起 HTTP 请求并将得到的响应作为消息传递给下一个组件。

## 配置说明
根据您创建应用的时间不同，HTTP Request 连接器配置也不相同，具体如下：

| 配置方法 | 适用场景 | 配置入口 |
|---------|---------|---------|
| [方法一](#method1) | 在2021年9月2日前创建的应用 | 在新建连接配置页面进行基本配置和高级配置|
| [方法二](#method2) | 在2021年9月2日及之后创建的应用 | 直接在右侧弹出的配置界面中即可进行基本配置和高级配置 |
| [方法三](#method3) | 在2022年4月8日及之后创建的应用 | 配置连接 > 配置请求信息 |

与方案一相比，方案二和方案三的优化内容如下：
- 方法二优化内容：此项优化不影响原有和现有应用的配置和使用，只是在配置操作上进行了优化，更方便客户填写对应信息。
- 方法三优化内容：HTTP Request 连接器支持连接配置的统一管理。

##  方法一（2021年9月2日前创建的应用）[](id:method1)

### 参数介绍

- 基本配置：HTTP Request 连接器基本配置中包括描述、请求域名、请求协议、请求端口、最大重定向次数以及公共请求路径，其中请求域名、请求协议、请求端口、最大重定向次数、公共请求路径为必填项。
	<img src="https://qcloudimg.tencent-cloud.cn/raw/6ba85ca7403e9e9578c58a63e6effd90.png" width="656px">
- 高级配置：HTTP Request 连接器高级配置中包括安全网关配置，用于内网域名/IP 请求。
	![](https://qcloudimg.tencent-cloud.cn/raw/4568549a34bab7f46e448c27f9e60598.png)
- 上述连接器配置参数相关描述如下表所示：

| 参数         | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ------------ | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 请求域名     | string   | 对应的请求域名                                               | 是           | 无         |
| 请求协议     | string   | 下拉框选择请求协议 HTTPS/HTTP                                | 是           | HTTPS      |
| 请求端口     | string   | 请求端口，1-65535，默认443，与请求协议联动，HTTP 协议默认会是80 | 是           | 443        |
| 最大重定向数 | int      | 重定向次数，最小值0，最大值1                                 | 是           | 1          |
| 公共请求路径 | string   | 请求的公共路径，多次请求的路径中相同的部分可配置为公共请求路径 | 是           | /          |
| 安全网关名称 | string   | 直接请求内网域名/IP 时，需要绑定安全网关                     | 否           | 无         |

### 配置说明

HTTP Request 操作配置包括基本配置、高级配置两项：
![](https://qcloudimg.tencent-cloud.cn/raw/99edf9cbf505ffb91e77a6b8b79344f2.png)

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
| 消息属性     | string   | 下拉框选择输出消息绑定的属性，HTTP Request 只支持绑定 payload | 否       | payload    |
| 类型选择     | string   | 下拉框选择输出消息 payload 绑定的数据类型，包括 message 内置数据类型和自定义数据类型 | 否       | 空         |
| 数据消费模式 | string   | 下拉框选择是否对消息数据进行持久化处理：<br/>repeatable：默认处理方式，消息数据可在一次触发中持续重复使用<br/>non-repeatable：数据一次性消费，用于大文件数据的流式高效处理，暂时支持 JSON 数组类型，其超过5M时建议选择该模式 | 否       | repeatable |

:::
</dx-tabs>


## 方法二（2021年9月2日及之后创建的应用）[](id:method2)

### 参数介绍

- 基本配置：HTTP Request 连接器基本配置中包括请求 URL、请求协议、请求方法、请求头、请求参数、最大重定向次数以及请求超时时间，其中请求URL、请求方法、最大重定向次数为必填项。
- 高级配置：HTTP Request 连接器高级配置中输出消息绑定自定义数据类型，可用于自定义输出消息数据类型。绑定安全网关，用于内网域名/IP 请求。
  ![](https://qcloudimg.tencent-cloud.cn/raw/cfe068b13cd0ca9fb8fd67681f7c7e37.png)

### 配置说明

HTTP Request 操作配置包括基本配置、高级配置两项：
![](https://qcloudimg.tencent-cloud.cn/raw/cfe068b13cd0ca9fb8fd67681f7c7e37.png)

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
<td>请求URL</td>
<td>string/表达式</td>
<td>用于指定发送请求的URL</td>
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
<td>最大重定向数</td>
<td>init/表达式</td>
<td>用于指定发送请求的请求体</td>
<td>否</td>
<td>1</td>
</tr>
<tr>
<td>请求超时时间</td>
<td>string/表达式</td>
<td>用于设置请求超时时间</td>
<td>否</td>
<td>1</td>
</tr>
</tbody></table>

:::
::: 高级配置参数描述

| 参数         | 参数类型 | 描述                                                         | 是否必填 | 默认值     |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ---------- |
| 消息属性     | string   | 下拉框选择输出消息绑定的属性，HTTP Request 只支持绑定 payload | 否       | payload    |
| 类型选择     | string   | 下拉框选择输出消息 payload 绑定的数据类型，包括 message 内置数据类型和自定义数据类型 | 否       | 空         |
| 数据消费模式 | string   | 下拉框选择是否对消息数据进行持久化处理：<br/>repeatable：默认处理方式，消息数据可在一次触发中持续重复使用<br/>non-repeatable：数据一次性消费，用于大文件数据的流式高效处理，暂时支持 JSON 数组类型，其超过5M时建议选择该模式 | 否       | repeatable |
| 安全网关名称 | string   | 直接请求内网域名/IP 时，需要绑定安全网关                     | 否       | 空         |

:::
</dx-tabs>

### 输出

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

### 案例

1. 组件筛选 HTTP Request。
   ![image-20210426211753938](https://main.qcloudimg.com/raw/8db8b3da512cc211fc8f0dda96f1b586/image-20210426211753938.png)
2. 新建并配置 HTTP Request 连接器，请求域名`www.qq.com`。(此案例参考方法一进行配置)
	 ![](https://qcloudimg.tencent-cloud.cn/raw/75ccb00a01b280d8f60f668e8ea0805c.png)
配置界面如下：
	 <img src="https://qcloudimg.tencent-cloud.cn/raw/445b76941a8972b72d8e7c96d9a71dd1.png" width="460px">
3. 使用操作配置。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/1be07272c919112ff4c4ef7c280f1d3f.png)
4. 发布并触发。浏览器访问触发对应流，可以直接跳转至腾讯首页。
   ![](https://main.qcloudimg.com/raw/1b04a28805e20f3871622c26836cb782.png)

- 同时，应用测试模式下可以看到 HTTP Request 对应的 attributes。
  ![](https://main.qcloudimg.com/raw/4a7099444248e9c65bb8abee04adeff5/image-20210426212733856.png)


## 方法三（2022年4月8日后创建的应用）[](id:method3)
### 连接配置

- HTTP Request 连接器连接配置中包括 Base URL、证书验证、最大重定向次数及安全网关名称。
	<img src="https://qcloudimg.tencent-cloud.cn/raw/9352c689297e924767abbc9d49bd8753.png" width="500px">
- 上述连接器配置参数相关描述如下表所示：
<table>
<thead>
<tr>
<th>参数</th>
<th>数据类型</th>
<th>描述</th>
<th><strong>是否必填</strong></th>
<th><strong>默认值</strong></th>
</tr>
</thead>
<tbody><tr>
<td>Base URL</td>
<td>string</td>
<td>一般配置请求地址的公共部分</td>
<td>否</td>
<td>无</td>
</tr>
<tr>
<td>证书验证</td>
<td>string</td>
<td>开启后则请求HTTP服务时跳过证书验证</td>
<td>是</td>
<td>HTTPS</td>
</tr>
<tr>
<td>最大重定向数</td>
<td>int</td>
<td>重定向次数，最小值1，最大值10</td>
<td>否</td>
<td>1</td>
</tr>
<tr>
<td>请求超时时间</td>
<td>string</td>
<td>设置请求的超时时间，最大5分钟，最小1分钟</td>
<td>否</td>
<td>1</td>
</tr>
<tr>
<td>安全网关名称</td>
<td>string</td>
<td>直接请求内网域名/IP 时，需要绑定安全网关</td>
<td>否</td>
<td>无</td>
</tr>
</tbody></table>

### 配置说明

HTTP Request 操作配置包括基本配置、高级配置两项：
	<img src="https://qcloudimg.tencent-cloud.cn/raw/a29d95bb638966fc1bf1ce7e899f2616.png" width="500px">
![]()
### 参数介绍

- 基本配置：HTTP Request 连接器基本配置中包括请求URL、请求方法、URL参数、请求头、请求体，其中请求URL、请求方法为必填项。
- 高级配置：HTTP Request 连接器高级配置中输出消息绑定自定义数据类型，可用于自定义输出消息数据类型。
	<img src="https://qcloudimg.tencent-cloud.cn/raw/7885e6ad39ec2a436eb3426abc4bc7a6.png" width="500px">

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
<td>请求URL</td>
<td>string/表达式</td>
<td>如果在连接配置中配置了BaseUrl,请配置相对URL.否则配置完整的请求URL</td>
<td>是</td>
<td>/</td>
</tr>
<tr>
<td>请求方法</td>
<td>string</td>
<td>下拉单选指定发送请求的方法，全集为：GET、POST、PUT、PATCH、DELETE、HEAD、OPTIONS</td>
<td>是</td>
<td>GET</td>
</tr>
<tr>
<td>URL参数</td>
<td>表达式</td>
<td>用于指定发送请求的URL参数，结构为：dict&lt;string,string&gt;</td>
<td>否</td>
<td>无</td>
</tr>
<tr>
<td>请求头</td>
<td>表达式</td>
<td>用于指定发送请求的请求头，结构为：dict&lt;string,list<string>&gt;</string></td>
<td>否</td>
<td>无</td>
</tr>
<tr>
<td>请求体</td>
<td>string/表达式</td>
<td>用于设置发送请求的消息体</td>
<td>否</td>
<td>无</td>
</tr>
</tbody></table>

:::
::: 高级配置参数描述

| 参数         | 参数类型 | 描述                                                         | 是否必填 | 默认值     |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ---------- |
| 消息属性     | string   | 下拉框选择输出消息绑定的属性，HTTP Request 只支持绑定 payload | 否       | payload    |
| 类型选择     | string   | 下拉框选择输出消息 payload 绑定的数据类型，包括 message 内置数据类型和自定义数据类型 | 否       | 空         |
| 数据消费模式 | string   | 下拉框选择是否对消息数据进行持久化处理：<br/>repeatable：默认处理方式，消息数据可在一次触发中持续重复使用<br/>non-repeatable：数据一次性消费，用于大文件数据的流式高效处理，暂时支持 JSON 数组类型，其超过5M时建议选择该模式 | 否       | repeatable |
:::
</dx-tabs>

### 输出

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

### 案例

1. 新增组件时，筛选 HTTP Request。
   ![image-20210426211753938](https://main.qcloudimg.com/raw/8db8b3da512cc211fc8f0dda96f1b586/image-20210426211753938.png)
2. 新建并配置 HTTP Request 连接器，BaseURL 配置为：`https://cloud.tencent.com`。
<img src="https://qcloudimg.tencent-cloud.cn/raw/2e326e775a2de19b629d2e06b4f64ead.png" width="550px"><br>配置界面如下：
	 <img src="https://qcloudimg.tencent-cloud.cn/raw/492be263a6ecd47a48f0ed78559731ae.png" width="550px">

3. 使用操作配置。
	 <img src="https://qcloudimg.tencent-cloud.cn/raw/2c9b624b96807491ed3244ceee23fde4.png" width="550px">

4. 发布并触发。浏览器访问触发对应流，可以直接跳转至腾讯云首页。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c08dc624a13544050ef932513d196b72.png)
   集成流如下：
![](https://qcloudimg.tencent-cloud.cn/raw/217c65d6d1680e60f0cb59e7a2c9685a.png)
同时，应用测试模式下可以看到 HTTP Request 对应的 payload、 attributes。
 - payload：<br>
 	 <img src="https://qcloudimg.tencent-cloud.cn/raw/fb567e9854d91907538b4eac47349c0e.png" width="550px">

 - attributes：<br>
  	 <img src="https://qcloudimg.tencent-cloud.cn/raw/28c4e6aee227333badd2602136fdb0da.png" width="550px">
