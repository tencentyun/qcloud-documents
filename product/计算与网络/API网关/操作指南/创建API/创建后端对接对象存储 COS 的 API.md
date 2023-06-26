## 操作场景

该任务指导您通过 API 网关控制台创建后端对接 [对象存储 COS](https://console.cloud.tencent.com/cos) 的 API。

## 方案优势
- API 网关和对象存储 COS 之间采用内网对接，性能优，且不收取公网流量费用；
- API 网关支持计算对象存储 COS 签名，避免改造客户端。

## 前提条件
- 已完成 API 网关 [服务创建](https://cloud.tencent.com/document/product/628/11787)。
- 已完成对象存储 COS [存储桶创建](https://cloud.tencent.com/document/product/436/13309) 和 [上传对象](https://cloud.tencent.com/document/product/436/13321)。

## 操作步骤
### 步骤1：新建 API
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service) ，在左侧导航栏单击**服务**。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击**管理 API** 标签页。
4. 单击**新建**，进行后续配置。

### 步骤2：前端配置

API 的前端配置指提供给外界访问的相关配置，包括 API 名称、前端类型、请求协议、HTTP 方法、URL 路径和入参的定义。具体需要填写的字段如下：
#### 前端基本信息配置
- **API 名称**：您创建的 API 的名称，在当前服务内具有唯一性，支持最长60个字符。
- **API 类型**：可选择通用API、微服务API。根据支持的后端类型判断，此处应选择通用API。
- **前端类型**：可支持 HTTP&HTTPS、WS&WSS 两种前端类型。
- **路径**：您可以按需求写入合法 URL 路径。如需要在路径中配置动态参数，请使用`{}`符号，并在其中填入参数名，例如`/user/{userid}`路径，申明了路径中的 userid 参数，此参数同时需要在入参中作为 Path 类型参数进行定义。Query 参数不是必须在 URL 路径中定义的。
  **路径支持正则表达式方式匹配**，路径输入内容以`/user`为例：
	- `=/user`：代表精确匹配，当存在多个 API 接口都有`/use`r时，优先匹配含有`=/user`的配置的 API 接口。
	- `/user/{id}`：代表路径上存在动态参数，当存在多个 API 接口都有`/user`时，优先级第三匹配含有动态参数的配置的 API 接口。
	- `/user`：表示完全匹配或前缀匹配的方式访问，访问时`/user`、`/usertest`、`/user/test/a`都可以访问到`/user`路径的 API 接口。
- **请求方法**：可选择 GET、POST、PUT、DELETE、HEAD 方法。（ANY方法不支持COS后端）
- **鉴权类型**：支持 [免认证](https://cloud.tencent.com/document/product/628/11820)、[应用认证](https://cloud.tencent.com/document/product/628/55088)、[OAuth 2.0](https://cloud.tencent.com/document/product/628/38393)、[EIAM认证](https://cloud.tencent.com/document/product/628/59669)、[密钥对认证](https://cloud.tencent.com/document/product/628/11819) 鉴权类型。
- **支持 CORS**：用于配置跨域资源共享（CORS），开启后将默认在响应头中添加 `Access-Control-Allow-Origin : *`。

#### 前端参数配置
**入参**：入参包含了来源于 Header、Query、Path 的参数。其中 Path 参数对应于在 URL 路径中定义的动态参数。任一参数，均需要指定参数名，参数类型和参数数据类型；同时可以指明是否必填、默认值、示例数据和描述说明。利用这些配置，API 网关可以协助您完成入参的文档化和初步校验。
  <img src="https://qcloudimg.tencent-cloud.cn/raw/1ce50667bf6cf24923ae4d926ce20ea9.png" width=900/>
> ?
> - 请求协议为 HTTPS 时，需要请求中携带 SNI 标识，为了保障请求安全，API 网关会拒绝不携带 SNI 标识的请求。
> - SNI（Server Name Indication）是 TLS 的一个扩展协议，用于解决一个服务器拥有多个域名的情况，在 TLSv1.2 开始得到协议的支持。之前的 SSL 握手信息中没有携带客户端要访问的目标地址，如果一台服务器有多个虚拟主机，且每个主机的域名不一样，使用了不一样的证书，此时会无法判断返回哪一个证书给客户端，SNI 通过在 Client Hello 中补上 Host 信息解决该问题。

### 步骤3：后端配置对接对象存储 COS

API 的后端配置，是指的实际提供真实服务的配置。API 网关会将前端请求，依据后端配置进行转换后，转发调用到实际的服务上。当您的业务部署在对象存储 COS 上时，后端选用对象存储 COS 对接，此时需要选择您的后端类型为对象存储 COS。
配置说明：

| 参数 | 是否必填 | 说明 |
|------------------|-------------|----------------|
| Action | 必填 | API 网关对接的 COS API，和前端配置的请求方法有联动关系，详情请参见 [**注意事项**](#notice)。 |
| 存储桶 | 必填 | 只支持对接和 API 网关同地域的存储桶。 |
| 计算 COS 签名 | 必填 | 打开后，将在 API 网关侧计算 COS 签名，无需请求客户端计算。 |
| 后端路径 | 必填 | 	必须以“/”开头，API 网关将根据路径匹配存储桶中的 Object |
| 路径匹配方式 | 必填 | **全路径匹配：**按前端路径和后端路径的组合匹配存储桶中的 Object，适合根据客户端传入不同路径操作不同 Object 的情况。具体匹配规则详情请参见 [**注意事项**](#notice)。</br>**后端路径匹配：**仅按后端路径匹配存储桶中的 Object，适合只需要操作一个固定 Object 的情况。无论客户端用什么路径访问，都只会转发到后端路径对应的 COS Object 上。 |

<img src="https://qcloudimg.tencent-cloud.cn/raw/33ed4a3bc8c24c6fdd09406253095b48.png" width=900/>

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
