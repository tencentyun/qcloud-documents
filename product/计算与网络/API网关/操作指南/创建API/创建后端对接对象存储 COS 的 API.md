## 操作场景

该任务指导您通过 API 网关控制台创建后端对接 [对象存储 COS](https://console.cloud.tencent.com/cos) 的 API。

## 方案优势
- API 网关和对象存储 COS 之间采用内网对接，性能优，且不收取公网流量费用；
- API 网关支持计算对象存储 COS 签名，避免改造客户端。

## 前提条件
- 已完成 API 网关 [服务创建](https://cloud.tencent.com/document/product/628/11787)。
- 已完成对象存储 COS [存储桶创建](https://cloud.tencent.com/document/product/436/13309) 和 [对象上传](https://cloud.tencent.com/document/product/436/13321)。

## 操作步骤
### 步骤1：新建通用 API

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏单击**服务**。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击**管理 API** 标签页，根据后端业务类型选择创建**通用 API**。
4. 单击**新建**，进行后续配置。

### 步骤2：前端配置

API 的前端配置指提供给外界访问的相关配置，包括 API 名称、前端类型、请求协议、HTTP 方法、URL 路径和入参的定义。具体需要填写的字段如下：
<table>
<thead>
<tr>
<th>参数</th>
<th>是否必填</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>API 名称</td>
<td>必填</td>
<td>您创建的 API 的名称，在当前服务内具有唯一性，支持最长60个字符。</td>
</tr>
<tr>
<td>前端类型</td>
<td>必填</td>
<td>客户端访问 API 网关的协议，API 网关支持 HTTP&amp;HTTPS、WS&amp;WSS 两种前端类型。</td>
</tr>
<tr>
<td>URL 路径（Path）</td>
<td>必填</td>
<td>您可以按需求写入合法 URL 路径。<br><strong>在路径中配置动态参数</strong>：请使用<code>{}</code>符号，并在其中填入参数名，例如<code>/user/{userid}</code>路径，申明了路径中的 userid 参数，此参数同时需要在入参中作为 Path 类型参数进行定义。Query 参数可以不用在 URL 路径中定义。<br><strong>路径支持正则表达式方式匹配</strong>：路径输入内容以<code>/user</code>为例：<br><code>=/user</code>：代表精确匹配，当存在多个 API 接口都有<code>/use</code>r时，优先匹配含有<code>=/user</code>的配置的 API 接口。<br> <code>/user/{id}</code>：代表路径上存在动态参数，当存在多个 API 接口都有<code>/user</code>时，优先级第三匹配含有动态参数的配置的 API 接口。<br><code>/user</code>：表示完全匹配或前缀匹配的方式访问，访问时<code>/user</code>、<code>/usertest</code>、<code>/user/test/a</code>都可以访问到<code>/user</code>路径的 API 接口。</td>
</tr>
<tr>
<td>请求方法</td>
<td>必填</td>
<td>可选择 GET、POST、PUT、DELETE、HEAD 方法。</td>
</tr>
<tr>
<td>鉴权类型</td>
<td>必填</td>
<td>API 鉴权类型，支持多种鉴权方式。</td>
</tr>
<tr>
<td>支持 CORS</td>
<td>必填</td>
<td>用于配置跨域资源共享（CORS），开启后将默认在响应头中添加 <code>Access-Control-Allow-Origin : *</code>。</td>
</tr>
<tr>
<td>入参</td>
<td>选填</td>
<td>入参包含了来源于 Header、Query、Path 的参数。其中 Path 参数对应于在 URL 路径中定义的动态参数。任一参数，均需要指定参数名，参数类型和参数数据类型；同时可以指明是否必填、默认值、示例数据和描述说明。利用这些配置，API 网关可以协助您完成入参的文档化和初步校验。</td>
</tr>
</tbody></table>
填写完成后，单击<b>下一步</b>，即可进行后端配置。

### 步骤3：后端配置对接对象存储 COS

API 的后端配置，是指的实际提供真实服务的配置。API 网关会将前端请求，依据后端配置进行转换后，转发调用到实际的服务上。当您的业务部署在对象存储 COS 上时，后端选用对象存储 COS 对接，此时需要选择您的后端类型为对象存储 COS。
配置说明：

| 参数 | 是否必填 | 说明 |
|---------|---------|---------|
| Action | 必填 | API 网关对接的 COS API，和前端配置的请求方法有联动关系，详情请参见 [**注意事项**](#notice)。 |
| 存储桶 | 必填 | 只支持对接和 API 网关同地域的存储桶。 |
| 计算 COS 签名 | 必填 | 打开后，将在 API 网关侧计算 COS 签名，无需请求客户端计算。 |
| 后端路径 | 必填 | 	必须以“/”开头，API 网关将根据路径匹配存储桶中的 Object |
| 路径匹配方式 | 必填 | **全路径匹配：**按前端路径和后端路径的组合匹配存储桶中的 Object，适合根据客户端传入不同路径操作不同 Object 的情况。具体匹配规则详情请参见 [**注意事项**](#notice)。</br>**后端路径匹配：**仅按后端路径匹配存储桶中的 Object，适合只需要操作一个固定 Object 的情况。无论客户端用什么路径访问，都只会转发到后端路径对应的 COS Object 上。 |

![](https://qcloudimg.tencent-cloud.cn/raw/33ed4a3bc8c24c6fdd09406253095b48.png)




[](id:notice)
## 注意事项
### 请求方法和 Action 的联动关系
请求方法和 Action 的联动关系详见下表：

| 前端配置中选择的请求方法 | 后端配置中的 Action |
|---------|---------|
| GET | GetObject |
| PUT | PutObject |
| POST | PostObject、AppendObject |
| HEAD | HeadObject |
| DELETE | DeleteObject |

### 全路径匹配规则
透传路径 = 后端路径 + 请求路径 - 前端路径，以下是四种情况的示例：

| 路径  | 情况1 | 情况2 | 情况3 | 情况4 |
|---------|---------|---------|---------|---------|
| 前端路径 | / | /a | /a | /a |
| 后端路径 | / | /b | / | /b |
| 请求路径 | /a/b | /a/b | /a/b | /a/c |
| 透传路径 | /a/b | /b/b | /b | /b/c |
