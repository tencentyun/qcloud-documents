## 操作场景

该任务指导您通过 API 网关控制台创建后端对接 VPC 内资源的 API。


## 前提条件
已完成 [服务创建](https://cloud.tencent.com/document/product/628/11787)。


## 操作步骤
### 步骤1：新建通用 API

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) ，在左侧导航栏单击【服务】。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击【管理 API】标签页，根据后端业务类型选择创建【通用 API】。
4. 单击【新建】，进行后续配置。

### 步骤2：前端配置

API 的前端配置指提供给外界访问的相关配置，包括 API 名称、前端类型、请求协议、HTTP 方法、URL 路径和入参的定义。

#### 前端基础信息配置

- **API 名称**：您创建的 API 的名称，在当前服务内具有唯一性，支持最长60个字符。
- **前端类型**：API 网关支持 HTTP&HTTPS、WS&WSS 两种前端类型。
- **URL 路径（Path）**：您可以按需求写入合法 URL 路径。如需要在路径中配置动态参数，请使用`{}`符号，并在其中填入参数名，例如`/user/{userid}`路径，申明了路径中的 userid 参数，此参数同时需要在入参中作为 Path 类型参数进行定义。Query 参数可以不用在 URL 路径中定义。
  **路径支持正则表达式方式匹配**，路径输入内容以`/user`为例：
	- `=/user`：代表精确匹配，当存在多个 API 接口都有`/use`r时，优先匹配含有`=/user`的配置的 API 接口。
	- `/user/{id}`：代表路径上存在动态参数，当存在多个 API 接口都有`/user`时，优先级第三匹配含有动态参数的配置的 API 接口。
	- `/user`：表示完全匹配或前缀匹配的方式访问，访问时`/user`、`/usertest`、`/user/test/a`都可以访问到`/user`路径的 API 接口。
- **请求方法**：可选择 GET、POST、PUT、DELETE、HEAD 方法。
- **鉴权类型**：支持 [免鉴权](https://cloud.tencent.com/document/product/628/11820)、[密钥对认证](https://cloud.tencent.com/document/product/628/11819)、[OAuth 2.0](https://cloud.tencent.com/document/product/628/38393) 三种鉴权类型。
- **支持 CORS**：用于配置跨域资源共享（CORS），开启后将默认在响应头中添加 `Access-Control-Allow-Origin : *`。

#### 前端参数配置

**入参**：入参包含了来源于 Header、Query、Path 的参数。其中 Path 参数对应于在 URL 路径中定义的动态参数。任一参数，均需要指定参数名，参数类型和参数数据类型；同时可以指明是否必填、默认值、示例数据和描述说明。利用这些配置，API 网关可以协助您完成入参的文档化和初步校验。
![](https://main.qcloudimg.com/raw/94699cd44a03405f5113f8b56748aa1f.png)

> ?
> - 请求协议为 HTTPS 时，需要请求中携带 SNI 标识，为了保障请求安全，API 网关会拒绝不携带 SNI 标识的请求。
> - SNI（Server Name Indication）是 TLS 的一个扩展协议，用于解决一个服务器拥有多个域名的情况，在 TLSv1.2 开始得到协议的支持。之前的 SSL 握手信息中没有携带客户端要访问的目标地址，如果一台服务器有多个虚拟主机，且每个主机的域名不一样，使用了不一样的证书，此时会无法判断返回哪一个证书给客户端，SNI 通过在 Client Hello 中补上 Host 信息解决该问题。

### 步骤3：后端配置对接 VPC 内资源

API 的后端配置，是指的实际提供真实服务的配置。API 网关会将前端请求，依据后端配置进行转换后，转发调用到实际的服务上。
当您的业务采用主机、容器实现在 VPC 内，希望通过 API 网关 + 内网 CLB 将服务能力开放出来时，后端选用对接 VPC 内资源。

1. 需要选择您的后端类型为 VPC 内资源。
2. 在后端配置中需要先选择所需对接的 VPC，目前API网关仅支持通过内网 CLB 对接 VPC 内资源。
   ![](https://main.qcloudimg.com/raw/9fcb47b8f6fb10bbe8f52bc8134e1703.png)
3. 选择后端域名的 CLB 及对应监听器。
   如您选择 HTTP 或 HTTPS 监听器，请确保后端 CVM 开通了公网带宽，否则可能会出现网络请求不通的问题（此策略产生的流量不计入公网出流量）。
4. 在后端域名处填写 `http://vip+port` 或 `https://vip+port`， 这里根据您填写的不同我们发往 CLB 的请求会分别为 HTTP 请求或 HTTPS 请求。此处的 VIP 是 CLB 的 VIP，您可在应用型内网 CLB 的基本信息中查询到（参考步骤1截图）。
5. 填写后端路径。

	- 如果您选择的是 HTTP/HTTPS 的 CLB 监听类型，在后端路径配置中，需要将后端路径配置为用户在 CLB 中监听器中配置的路径。
  [CLB](https://console.cloud.tencent.com/clb/index) 中监听器配置的域名及路径：
  ![](https://main.qcloudimg.com/raw/40b6cabcfb893cb6c1caf663ffa38e8c.png)
   API 网关中的后端路径，需要和 CLB 中的路径一致。
   此外，还需要在常量参数处配置一个名为 host 的参数，放在 header 中，参数值为 CLB 监听器中配置的域名。
  ![](https://main.qcloudimg.com/raw/38201ce524986c4aef2935df173c6756.png)
	- 如果您选择的是 TCP/UDP 的 CLB 监听类型，在后端配置中，需要将后端路径配置为 CLB 后端挂载 CVM 中业务所需的路径。
  如果您在 CVM 中配置了 host 校验，则如同使用七层监听器一样，需要在常量参数中配置名为 host 的参数，根据您自身的业务选择所需放置的地址。后续的配置与其他的 API 配置相同。

6. 当后端对接 CLB 时，需要将后端挂载的 CVM 上的安全组放通100.64.0.0/10、9.0.0.0/8 网段。

> ? 后端对接 VPC 内资源的完整配置流程可参考 [最佳实践 - 后端对接 VPC 内 CLB 资源](https://cloud.tencent.com/document/product/628/42937)。

### 步骤4：响应配置

API 响应配置：包括 API 响应数据配置和 API 错误码配置。
API 响应数据配置：用于指明返回数据类型，包括成功调用的数据示例和失败调用的数据示例。
API 的错误码定义：用于指明额外的错误码、错误信息和描述。

> ?目前 API 网关对于响应结果不做处理，直接透传给请求者。在生成 SDK 文档时，填写的响应示例也会一并展示在文档中，它将会更好的帮助使用者理解接口含义。
