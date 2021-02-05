## 操作场景

该任务指导您通过 API 网关控制台创建后端对接 Mock 的 API。

>!后端对接 Mock 仅能返回固定数据，建议您在测试过程中使用，不建议在真实业务场景中使用。


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
![](https://main.qcloudimg.com/raw/a02b6d507c93458f90a7d52d00b180e4.png)

> ?
> - 请求协议为 HTTPS 时，需要请求中携带 SNI 标识，为了保障请求安全，API 网关会拒绝不携带 SNI 标识的请求。
> - SNI（Server Name Indication）是 TLS 的一个扩展协议，用于解决一个服务器拥有多个域名的情况，在 TLSv1.2 开始得到协议的支持。之前的 SSL 握手信息中没有携带客户端要访问的目标地址，如果一台服务器有多个虚拟主机，且每个主机的域名不一样，使用了不一样的证书，此时会无法判断返回哪一个证书给客户端，SNI 通过在 Client Hello 中补上 Host 信息解决该问题。

### 步骤3：后端配置对接 Mock

Mock 会对 API 请求返回固定配置的响应。Mock 常用于测试开发，可以在后端服务还未完成的情况下预先完成 API 配置和响应。对接 Mock 时，只需要配置您的返回数据，单击【完成】即可。
![](https://main.qcloudimg.com/raw/4e1f9bfb605e9051ad08e8f331cbd90d.png)
