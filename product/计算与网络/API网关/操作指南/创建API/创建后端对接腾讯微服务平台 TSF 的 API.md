## 操作场景

该任务指导您通过 API 网关控制台创建后端对接腾讯微服务平台 TSF 的 API。


## 前提条件
已完成 [服务创建](https://cloud.tencent.com/document/product/628/11787)。


## 操作步骤
### 步骤1：新建微服务 API

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) 。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击**管理 API** 标签页。
4. 单击**新建**，进行后续配置。

### 步骤2：前端配置
- **API 名称**：您创建的 API 的名称，在当前服务内具有唯一性，支持最长60个字符。
- **API 类型**：可选择通用API、微服务API。根据支持的后端类型判断，此处应选择微服务API。
- **前端类型**：可支持 HTTP&HTTPS、WS&WSS 两种前端类型。
- **路径**：您可以按需求写入合法 URL 路径。如需要在路径中配置动态参数，请使用`{}`符号，并在其中填入参数名，例如`/user/{userid}`路径，申明了路径中的 userid 参数，此参数同时需要在入参中作为 Path 类型参数进行定义。Query 参数不是必须在 URL 路径中定义的。
  **路径支持正则表达式方式匹配**，路径输入内容以`/user`为例：
	- `=/user`：代表精确匹配，当存在多个 API 接口都有`/use`r时，优先匹配含有`=/user`的配置的 API 接口。
	- `/user/{id}`：代表路径上存在动态参数，当存在多个 API 接口都有`/user`时，优先级第三匹配含有动态参数的配置的 API 接口。
	- `/user`：表示完全匹配或前缀匹配的方式访问，访问时`/user`、`/usertest`、`/user/test/a`都可以访问到`/user`路径的 API 接口。
- **请求方法**：可选择 GET、POST、PUT、DELETE、HEAD 、ANY方法。
- **鉴权类型**：支持 [免认证](https://cloud.tencent.com/document/product/628/11820)、[应用认证](https://cloud.tencent.com/document/product/628/55088)、[OAuth 2.0](https://cloud.tencent.com/document/product/628/38393)、[EIAM认证](https://cloud.tencent.com/document/product/628/59669)、[密钥对认证](https://cloud.tencent.com/document/product/628/11819) 鉴权类型。
- **支持 CORS**：用于配置跨域资源共享（CORS），开启后将默认在响应头中添加 `Access-Control-Allow-Origin : *`。

	<img src="https://qcloudimg.tencent-cloud.cn/raw/aca73c22b3d18fe267ff07c10eb5b950.png" width=900/>

#### 前端参数配置

   **入参**包含了来源于 Header、Query、Path 的参数。其中 Path 参数对应于在 URL 路径中定义的动态参数。
   任一参数均需要指定参数名、参数类型和参数数据类型，同时可以指明是否必填、默认值、示例数据和描述说明。利用这些配置，API 网关可以协助您完成入参的文档化和初步校验。
   在调用时需要传入 X-NameSpace-Code 和 X-MicroService-Name 两个必选参数，这两个参数控制 API 网关的请求发往哪个微服务，可放置在 Header、Path、Query 中，若放在 Path 中，则与通用 API 类似，需要在路径中配置路径参数，例如 `/{X-NameSpace-Code}/{X-MicroService-Name}`，若变量 X-NameSpace-Code=crgt，X-MicroService-Name=coupon-activity，则访问的 URL 为`https://访问域名/crgt/coupon-activity/`。除了这两个固定参数。其他参数配置均与通用 API 一致。

	- X-NameSpace-Code 路径参数是后端配置中所选择的命名空间在 [腾讯微服务平台](https://console.cloud.tencent.com/tsf/namespace) 命名空间中配置的 code 值。
<img src="https://qcloudimg.tencent-cloud.cn/raw/4fb77be70fce5e90b6dc7b4a5626f617.png" width=900/>

- X-MicroService-Name 路径参数是后端配置中所选择的集群在 [腾讯微服务平台](https://console.cloud.tencent.com/tsf/service) 服务治理中配置的微服务名称。

<img src="https://qcloudimg.tencent-cloud.cn/raw/5b257720fdfa7096684046022eadac86.png" width=900/>

单击**下一步**，进行后端配置。

### 步骤3：后端配置对接腾讯微服务平台 TSF

1. 选择所对接微服务的 **集群** 和 **命名空间** 。
2. 选择微服务。API 发布者可在一个 API 中对接多个微服务。
   请确保添加的服务可以被 API 网关访问，包括 cvm 部署的微服务，容器部署的微服务（公网访问和 NodePort 访问）。

	 <img src="https://qcloudimg.tencent-cloud.cn/raw/7af280c4550f0af6e912acd267713c67.png" width=900/>

	> ?目前 API 网关只支持将请求转发到 TSF 同一种部署类型（虚拟机或容器）的服务实例上。如果一个服务下既有虚拟机部署、又有容器部署的微服务实例，则不支持将 API 网关作为请求入口。

3. 配置后端路径。
   具体的后端服务请求路径。如果需要在路径中配置动态参数，请使用`{}` 符号，并在其中填入参数名，此参数名将用于在参数映射的配置中配置为来源于前端配置的入参。这里的路径可与前端不同，做路径映射。为真正服务的请求路径。
4. 选择负载均衡方式。
5. 设置会话保持。
6. 设置后端超时。
   在 API 网关发起到后端服务调用的超时时间。超时时间的最大限制为30秒。在 API 网关调用后端服务，未在超时时间内获得响应时，API 网关将终止此次调用，并返回相应的错误信息。
5. 设置参数。

	- 后端参数：X-NameSpace-Code、X-MicroService-Name这两个参数为固定参数，不可做映射，用户配置的其他参数均可做映射。
  如果您的 Body 参数仅有表单格式，则可直接在前后端参数配置时映射。若为 JSON 格式，则 JSON 参数 API 网关会直接透传。
	- 映射参数：参数映射用于将前端的入参映射为实际后端服务的参数。映射参数默认会将入参以相同名字和参数位置进行映射。同时，您可以根据需求，变更参数的映射方式，例如将来源于 Path 的入参，映射为后端服务中 Query 参数。
	- 常量参数：您可以根据需要，加入自行定义的常量参数。常量参数在每次 API 调用中都保持不变。同时，您可以利用系统参数，将所需的部分系统信息，传递给后端服务。

8. 单击**下一步**，配置响应结果。

### 步骤4：响应配置

API 响应配置：包括 API 响应数据配置和 API 错误码配置。
API 响应数据配置：用于指明返回数据类型，包括成功调用的数据示例和失败调用的数据示例。
API 的错误码定义：用于指明额外的错误码、错误信息和描述。

> ?目前 API 网关对于响应结果不做处理，直接透传给请求者。在生成 SDK 文档时，填写的响应示例也会一并展示在文档中，它将会更好的帮助使用者理解接口含义。

## 使用说明

当通过 API 网关访问后端微服务时，需要放通对应后端服务所在的虚拟机的安全组。用户可以设置安全组访问的来源、协议端口和访问策略。
设置访问来源时，至少需要放通 API 网关所在网段 9.0.0.0/8 以及100.64.0.0/10，其他来源随客户需求确定。

- 对于虚拟机部署的应用，要放通虚拟机上对应的服务端口。对于容器上部署的应用，需要放通的是容器所在虚拟机的服务端口，而不是 nodeport 端口。
- 对于容器应用，常常发生 IP 漂移的情况，建议将集群中的所有机器都放通容器上运行的需要对外暴露的服务端口。
