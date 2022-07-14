各大企业每天都有大量的 API 增长，同时越来越多公司开始公开 Web API，API 的使用场景正在累积。现在，每日 API 调用量在不断飙升，如何能够安全有效将这些 API 管理起来对于企业而言并不容易。

腾讯云数据连接器提供 API 发布功能，可以一键将已发布的应用打包生成 API，方便用户进行管理和调用；同时提供了 API 管理能力，可以针对 API 进行访问权限管控和流量调度。


## API 管理主页

登录 [腾讯云数据连接器控制台](https://ipaas.cloud.tencent.com/apimanage)，在左侧导航栏单击 **集成开发** > **API管理**，即可进入 API 管理的主页。

在 API 管理主页，您可以创建或查看 API，API 列表中展示有 API 服务名称、API 服务状态、API 服务域名、API 更新时间、API服务的数据统计、endpoint 统计、API 服务的鉴权方式用户数量以及操作等内容。同时，每个 API 服务均可展开，查看下属的 endpoint 的信息和状态。
![](https://qcloudimg.tencent-cloud.cn/raw/e2ae555cc4321dcb2a2c601c90ac3ecf.png)


## 创建 API 服务[](id:service)

API 管理功能支持 3.0.0 版本的 OpenAPI 规范。OpenAPI 3.0.0 规范的对象定义请参考 [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。用户可以通过单击**创建 API 服务**进入 API 创建界面。

创建 API 服务可以通过 API 描述文件创建，也可以通过页面手动创建。

<dx-tabs>
::: 通过 API 描述文件创建
1. 在 [API 管理](https://ipaas.cloud.tencent.com/apimanage) 页面，单击**创建API服务**，在基本配置中配置以下信息，完成后单击**下一步：策略信息**。
	- 创建方式：选择“创建自配置文件”
	- 上传描述文件：上传 YAML 或 JSON 格式的文件，大小100KB以内
	- 支持格式：YAML、JSON 
>?如果您需要更多帮助，如获取API描述文档样例文件，请参考 [API描述文件样例](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/API%E7%AE%A1%E7%90%86%EF%BC%88%E6%96%B0%EF%BC%89/case.yaml)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/df19c01382aa8cc8453c1705d9536e40.png)
2. 在策略信息中配置以下信息，单击**完成**即可创建一个 API 服务。
 - 配置鉴权策略：支持 BasicAuth、OAuth2.0 和无验证（即不填写检测策略）
 - 配置黑白名单：您可以按需开启，开启后可以输入多条 IP 进行黑白名单的访问限制
 - 开启访问限制：
	 - 请求频率策略：从配置时间起，每单位时间内允许的最大请求次数，填写范围为1 - 1000
	 - 访问限制策略：从配置时间算起，每单位自然时间内允许的最大访问次数，填写范围为1 - 1000
![](https://qcloudimg.tencent-cloud.cn/raw/2f41891374cfb709dcc65036e4a3730d.png)
:::
::: 通过页面手动创建
1. 在 [API 管理](https://ipaas.cloud.tencent.com/apimanage) 页面，单击**创建API服务**，在基本配置中配置以下信息，完成后单击**下一步：策略信息**。
 - 创建方式：选择“手动创建”
 - API名称：请输入 API 名称
 - 协议：支持 HTTP、HTTPS、HTTP&HTTPS 协议类型
 - 版本：请输入版本号
 - 描述（选填）：对此 API服 务的一些简单描述
 - 标签（选填）：如果有分组的需要，希望日后可以通过标签来进行快速的 API 服务筛选工作，还可以配置标签信息
![](https://qcloudimg.tencent-cloud.cn/raw/bdafd02e426294352fc2f6238492afef.png)
2. 在策略信息中配置以下信息，单击**完成**即可创建一个 API 服务。
 - 配置鉴权策略：支持 BasicAuth、OAuth2.0 和无验证（即不填写检测策略）
 - 配置黑白名单：您可以按需开启，开启后可以输入多条 IP 进行黑白名单的访问限制
 - 开启访问限制：
	 - 请求频率策略：从配置时间起，每单位时间内允许的最大请求次数，填写范围为1 - 1000
	 - 访问限制策略：从配置时间算起，每单位自然时间内允许的最大访问次数，填写范围为1 - 1000
![](https://qcloudimg.tencent-cloud.cn/raw/e3210000dae28d43482ffb1a1345fca8.png)

:::
</dx-tabs>



## 创建 API Endpoint[](id:endpoint)

当我们创建好一个 API 服务之后，则代表此 API 已经生成，可以开始编辑其具体行为。
API Endpoint 指一个 API 服务可以连接的后端服务信息，包括 API 的访问路径（API Path）、API 的调用方式、分组、API Endpoint 绑定的后端服务类型，最近修改时间以及一些操作。
![](https://qcloudimg.tencent-cloud.cn/raw/5c7cab2e6650f031c68ef5afc703e405.png)


默认新创建好的 API 服务是没有已绑定的 Endpoint 信息的，需要进行创建完成首次的绑定工作。
1. 在 [API 管理](https://ipaas.cloud.tencent.com/apimanage) 页面，单击目标 API 后**添加API Endpoint**，进行 API Endpoint 基本配置。完成后单击**下一步：策略信息**。
	- 访问路径：访问路径必须要以“/”开头
	- 后端服务：支持选择现成的集成流或者绑定第三方服务 BASE URL
	 - 当选择的后端服务为“集成流”模式时，集成流只可以选择已发布的，并且配置了拥有 HTTP 监听能力组件的流。
	 - 当选择“第三方服务BASE URL”时，在资源路径处输入资源链接
	- 描述：选填<br>
	![](https://qcloudimg.tencent-cloud.cn/raw/33a3849ac726749f82a97486873417c1.png)
2. 在策略信息页面，配置以下信息，完成后单击**下一步：参数信息**。
>?
>- 与 API 服务的策略信息配置方式类似，允许用户在此 Endpoint 所归属的 API 服务的策略限制基础上，配置第二层策略限制。两层限制共同生效。
>- 配置鉴权策略：您可以单击“同步服务策略”，一键同步上层的API服务策略，或者手动填写新的管理策略。
>此处可选择的鉴权策略范围为上层 API 服务的鉴权策略，即若上层 API 服务只允许 OAuth 2.0 的鉴权方式，则下层的 API Endpoint 只允许配置 OAuth 2.0，而不能配置 Basic Auth。
>
![](https://qcloudimg.tencent-cloud.cn/raw/cafb0cc228b1766be4864bb418ca5308.png)
3. 在参数信息页面，您可以配置访问此 API Endpoint 时可以选用的方法（API Method）和每种方法对应的调用参数信息。
   - API 调用方法可以多选，若想取消，则可以反选想要删除的方法。
   - 每一个参数后都提供了一系列操作，分别为：向上移动、向下移动、删除此参数，为此参数添加备注以及选择该参数是否必填。
![](https://qcloudimg.tencent-cloud.cn/raw/e2f260674377db120f64d46f1b1dba2d.png)
4. 当上述配置全部完成后，单击**完成**，则会返回 API 列表，同时已经创建好的 Endpoint 信息将会展现在此。

## API 测试与运维 

腾讯云数据连接器 API 管理平台同时还提供了完整的运维方案。查看步骤如下：
1. 在 [API 管理](https://ipaas.cloud.tencent.com/apimanage) 页面，找到目标 API 服务，单击操作列的数据统计图标，进入运维页面。
![](https://qcloudimg.tencent-cloud.cn/raw/fc7e776439c689793aca416b6d7b3331.png)
2. 在运维页面，您可以查看此 API 在规定时间范围内的请求记录和状态汇总。
![](https://qcloudimg.tencent-cloud.cn/raw/b64777c12ce31aca0a4995c027526d22.png)

同时，为了方便用户对配置完成的 API 进行在线的调试，我们还提供了通过控制台实时发送测试请求并且获取模拟测试结果的机制。操作步骤如下：
1. 在 [API 管理](https://ipaas.cloud.tencent.com/apimanage) 页面，单击目标 API 服务名称前面的![](https://qcloudimg.tencent-cloud.cn/raw/d04f6623eab2d6d840ecd8b54f986fe2.png)，显示访问路径。
2. 在访问路径中，单击操作列的**调试**，进入 API调试页面。
![](https://qcloudimg.tencent-cloud.cn/raw/0722a1ea4cc694741e22ab8f067331c2.png)
3. 在 API 调试页面，您可以配置此 API Endpoint 的请求 Header 和 Body 内容，并单击**发送请求**。
![](https://qcloudimg.tencent-cloud.cn/raw/9b7a502d2542a2cce7ac4e6843da4fc1.png)
随后即可获取到测试的结果。我们会将后端服务返回的 Response 状态码和结果返回给用户，方便进行进一步的调试工作。
![](https://qcloudimg.tencent-cloud.cn/raw/0a55c29f24282a66d94d70f1e6c0b3f4.png)

## API 用户管理
### 功能概述
用户管理功能允许 API 的提供者帮助其用户添加及管理账号、分配权限，并获取请求 API 时所需要的所有必要信息。
在 [API 管理](https://ipaas.cloud.tencent.com/apimanage) 页面，找到目标 API 服务，单击**用户数量**，进入用户管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/4a619b5393472eb059c71976f088c3ae.png)
API 服务提供方可以将会以类似管理者的视角去统一管理用户，允许查看用户的 OAuth 信息并分享给用户以便用户调用，或者进行用户的封禁和启用。
![](https://qcloudimg.tencent-cloud.cn/raw/d652a42e627aa354df47e28d69e68b38.png)

添加用户的时候需要提供以下用户信息，以便能够更好的记录和维护。同时，此处的用户名称和用户密码也将作为对应 API 服务的 Basic Auth 验证方式。
![](https://qcloudimg.tencent-cloud.cn/raw/9a887b6eca815885896527cd2c4b448c.png)

当创建好用户之后，则可以通过**查看详细信息**按钮获取到用户的 client ID、client Secret等内容
![](https://qcloudimg.tencent-cloud.cn/raw/b4d6ad0301ea46b60a1e21927c5ecc7f.png)

>?当前仅支持 API 服务提供方手动帮助客户添加成员信息和账户信息，客户的自助注册的能力暂不支持。

### 使用流程
#### 步骤1：创建 API 服务及其 API Endpoint
具体操作请参考 [创建 API 服务](#service) 、[创建 API Endpoint](#endpoint)。

#### 步骤2：获取 API 请求地址
1. 在 API 服务列表中获取 API 服务的域名。
![](https://qcloudimg.tencent-cloud.cn/raw/33daea97aa1ea5bc9132ecbfa4dd43ea.png)
2. 在 API Endpoint 列表中获取需要请求的 Endpoint 路径。
![](https://qcloudimg.tencent-cloud.cn/raw/4a5fb20d1006717e302c4772548c3007.png)
3. 将 Endpoint 路径拼接在 API 服务域名后面，即可获取完整的 API 请求域名。**请将此域名保存，[步骤4](#step4) 中会用到**。

#### 步骤3：获取用户请求 API 的权限
1. 在 [API 管理](https://ipaas.cloud.tencent.com/apimanage) 页面，找到目标 API 服务，单击**用户数量**，进入用户管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/4a619b5393472eb059c71976f088c3ae.png)
2. 单击**添加/编辑**，并配置以下信息。<br>
![](https://qcloudimg.tencent-cloud.cn/raw/9a887b6eca815885896527cd2c4b448c.png)
3. 帮助用户填写必要信息，默认选择用户进入入口的目标 API 服务名称。
![](https://qcloudimg.tencent-cloud.cn/raw/9a887b6eca815885896527cd2c4b448c.png)
4. 绑定好 API 服务之后，返回用户管理列表获取此用户的 OAuth 信息（当前系统会默认给添加的用户进行自动审批，所以无需手动审批操作），并复制保存 OAuth 的 Token 获取地址、Client ID、Client Secret 等信息，连同用户的账号和密码一同分享给用户。
![](https://qcloudimg.tencent-cloud.cn/raw/c3f0d78f35767df1201052c5d01afd16.png)

[](id:step4)
#### 步骤4：从用户侧调用 API（以 postman 为例）
API 服务无需验证的情况：
![](https://qcloudimg.tencent-cloud.cn/raw/f964a769a60ac3a8b9c366460073fc6a.png)
API 服务需要 Basic Auth 的情况(对应API服务的 Endpoint 安全策略需要绑定Basic Auth)：
![](https://qcloudimg.tencent-cloud.cn/raw/36e5f6eef4b7e646a3820b475cc9a959.png)
API 服务需要 OAuth2.0的情况（对应 API 服务的 Endpoint 安全策略需要绑定OAuth2.0）：
1. 在用户信息处获取 Client ID 和 Client Secret，在待访问的 API 服务页面获取 Access Token URL。 
<dx-tabs>
::: 获取 OAuth 信息
	![](https://qcloudimg.tencent-cloud.cn/raw/a36e2451969708e9cb60a50443acf75f.png)
:::
::: 获取 token 地址
![](https://qcloudimg.tencent-cloud.cn/raw/23196e5b182e85c91e2597d66b0ece5c.png)
token 地址如下：
![](https://qcloudimg.tencent-cloud.cn/raw/01e63bf123e4ed43baccb1095d0ab16d.png)
:::
</dx-tabs>

2. 复制之后，在 postman 中创建一个新的请求，填写入上方的 token 获取地址并使用“GET”方法（此处的鉴权方式应为“NoAuth”）。随后选择 Params 标签页，输入 client 信息。输入方式：
	- 第一列：key 为 client_id，value 为从上方复制的 Client ID 对应的内容
	- 第二列：key 为 client_sectet，value 为从上方复制的 Client Secret 对应的内容
	
![](https://qcloudimg.tencent-cloud.cn/raw/bb936f5bc3090384e45c56df5e4a354f.png)

3. 单击 **send**，从界面下方的“body”处复制“access_token”字段的值。此即为本次调用时需要用到的 token 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/44b750b810cf09c5a6e182a785bbe2bf.png)

4. 重新打开一个请求界面，填入需要请求的 API 域名，并选择 Bearer Token 模式。在右侧的“Token”处输入前面获得的token，单击 **send**，即可看到访问结果。
![](https://qcloudimg.tencent-cloud.cn/raw/388ff8dbc3f595e44a2c6342e74d4707.png)
