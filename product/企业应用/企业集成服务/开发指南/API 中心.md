各大企业每天都有大量的 API 增长，同时越来越多公司开始公开 Web API，API 的使用场景正在累积。现在，每日 API 调用量在不断飙升，如何能够安全有效将这些 API 管理起来对于企业而言并不容易。

千帆鹊桥 iPaaS 提供 API 发布功能，可以一键将已发布的应用打包生成 API，方便用户进行管理和调用；同时提供了 API 管理能力，可以针对 API 进行访问权限管控和流量调度。


## API 管理主页

登录 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，在左侧导航栏单击 **API中心** > **API管理**，即可进入 API 管理的主页。

在 API 管理主页，您可以创建或查看 API，API 列表中展示有 API 服务名称、API 服务状态、API 服务域名、API 更新时间、API服务的数据统计、endpoint 统计、API 服务的鉴权方式以及操作等内容。同时，每个API服务均可展开，查看下属的endpoint的信息和状态。
![](https://qcloudimg.tencent-cloud.cn/raw/75687966673ac207cb3f43516dd69cc7.png)


## 创建 API 服务[](id:service)

API 管理功能支持 3.0.0 版本的 OpenAPI 规范。OpenAPI 3.0.0 规范的对象定义请参考 [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。用户可以通过单击**创建 API 服务**进入 API 创建界面。

创建 API 服务可以通过 API 描述文件创建，也可以通过页面手动创建。

<dx-tabs>
::: 通过 API 描述文件创建
1. 在 [API 管理](https://console.cloud.tencent.com/eis/apimanage) 页面，单击**创建API服务**，在基本配置中配置以下信息，完成后单击**下一步：策略信息**。
	- 创建方式：选择“创建自配置文件”
	- 上传描述文件：上传 YAML 或 JSON 格式的文件，大小100KB以内
	- 支持格式：YAML、JSON 
![](https://qcloudimg.tencent-cloud.cn/raw/d37cfc07e742b001ceaa91310d8fbb24.png)
2. 若解析成功，单击**完成**，则可以直接通过此文件生成对应的 API 服务。
:::
::: 通过页面手动创建
1. 在 [API 管理](https://console.cloud.tencent.com/eis/apimanage) 页面，单击**创建API服务**，在基本配置中配置以下信息，完成后单击**下一步：策略信息**。
 - 创建方式：选择“手动创建”
 - API名称：请输入 API 名称
 - 协议：支持 HTTP、HTTPS、HTTP&HTTPS 协议类型
 - 版本：请输入版本号
 - 描述（选填）：对此 API服 务的一些简单描述
 - 标签（选填）：如果有分组的需要，希望日后可以通过标签来进行快速的 API 服务筛选工作，还可以配置标签信息
<img src="https://qcloudimg.tencent-cloud.cn/raw/d3faa08d6cc37aeeec7e7e2d595409ee.png" width="70%">
2. 在策略信息中配置以下信息，单击**完成**即可创建一个 API 服务。
 - 配置鉴权策略：支持 BasicAuth、OAuth2.0 和无验证（即不填写检测策略）
 - 配置黑白名单：您可以按需开启，开启后可以输入多条 IP 进行黑白名单的访问限制
 - 开启访问限制：
	 - 请求频率策略：从配置时间起，每单位时间内允许的最大请求次数，填写范围为1 - 1000
	 - 访问限制策略：从配置时间算起，每单位自然时间内允许的最大访问次数，填写范围为1 - 1000
<img src="https://qcloudimg.tencent-cloud.cn/raw/c62f9eceec444ad5951d5872415c84ae.png" width="80%">

:::
</dx-tabs>



## 创建 API Endpoint[](id:endpoint)

当我们创建好一个 API 服务之后，则代表此 API 已经生成，可以开始编辑其具体行为。
API Endpoint 指一个 API 服务可以连接的后端服务信息，包括 API 的访问路径（API Path）、API 的调用方式、分组、API Endpoint 绑定的后端服务类型，最近修改时间以及一些操作。
![](https://qcloudimg.tencent-cloud.cn/raw/5c7cab2e6650f031c68ef5afc703e405.png)


默认新创建好的 API 服务是没有已绑定的 Endpoint 信息的，需要进行创建完成首次的绑定工作。
1. 在 [API 管理](https://console.cloud.tencent.com/eis/apimanage) 页面，单击目标 API 服务名称，进入服务详情页。
2. 单击**添加API Endpoint**，进行 API Endpoint 基本配置，完成后单击**下一步：策略信息**。
	- 访问路径：访问路径必须要以“/”开头
	- 后端服务：支持选择现成的集成流或者绑定第三方服务BASE URL
	 - 当选择的后端服务为“集成流”模式时，集成流只可以选择已发布的，并且配置了拥有 HTTP 监听能力组件的流。
	 - 当选择“第三方服务BASE URL”时，在资源路径处输入资源链接
	- 描述：选填<br>
	<img src="https://qcloudimg.tencent-cloud.cn/raw/2436999ee9cebd9feb56ba97b96ed9cc.png" width="70%">
3. 在策略信息页面，配置以下信息，完成后单击**下一步：参数信息**。
>?
>- 与API服务的策略信息配置方式类似，允许用户在此endpoint所归属的API服务的策略限制基础上，配置第二层策略限制。两层限制共同生效。
>- 配置鉴权策略：您可以单击“同步服务策略”，一键同步上层的API服务策略，或者手动填写新的管理策略。
>此处可选择的鉴权策略范围为上层 API 服务的鉴权策略，即若上层 API 服务只允许 OAuth 2.0 的鉴权方式，则下层的 API Endpoint 只允许配置 OAuth 2.0，而不能配置 Basic Auth。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/3743e26a9506a736d88b43cd9e43105d.png" width="80%">
4. 在参数信息页面，您可以配置访问此 API Endpoint 时可以选用的方法（API Method）和每种方法对应的调用参数信息。
   - API 调用方法可以多选，若想取消，则可以反选想要删除的方法。
   - 每一个参数后都提供了一系列操作，分别为：向上移动、向下移动、删除此参数，为此参数添加备注以及选择该参数是否必填。
![](https://qcloudimg.tencent-cloud.cn/raw/f060a8f46eb8a7685a2e16a04e79b661.png)
5. 当上述配置全部完成后，单击**完成**，则会返回 API 列表，同时已经创建好的 Endpoint 信息将会展现在此。


## API 测试与运维 

千帆鹊桥 iPaaS  API 管理平台同时还提供了完整的运维方案。查看步骤如下：
1. 在 [API 管理](https://console.cloud.tencent.com/eis/apimanage) 页面，找到目标 API 服务，单击操作列的数据统计图标，进入运维页面。
![](https://qcloudimg.tencent-cloud.cn/raw/4a5abe9aed6974a72b1aaa5e8bd27cf9.png)
2. 在运维页面，您可以查看此 API 在规定时间范围内的请求记录和状态汇总。
![](https://qcloudimg.tencent-cloud.cn/raw/651244e1f921534fbf49ef8d637c2a02.png)

同时，为了方便用户对配置完成的API进行在线的调试，我们还提供了通过控制台实时发送测试请求并且获取模拟测试结果的机制。操作步骤如下：
1. 在 [API 管理](https://console.cloud.tencent.com/eis/apimanage) 页面，单击目标 API 服务名称前面的![](https://qcloudimg.tencent-cloud.cn/raw/d04f6623eab2d6d840ecd8b54f986fe2.png)，显示访问路径。
2. 在访问路径中，单击操作列的**调试**，进入 API调试页面。
![](https://qcloudimg.tencent-cloud.cn/raw/bf5175bc271b36caaeb2164802bc30ad.png)
3. 在 API调试页面，您可以配置此 API Endpoint 的请求 Header 和 Body 内容，并单击**发送请求**。
![](https://qcloudimg.tencent-cloud.cn/raw/9b2f590152d6d03f7295c76a5d5e8792.png)
随后即可获取到测试的结果。我们会将后端服务返回的 Response 状态码和结果返回给用户，方便进行进一步的调试工作。
![](https://qcloudimg.tencent-cloud.cn/raw/89ba06b81a08f9fed3f1822b78e9f2a1.png)

## API 用户中心

千帆鹊桥 iPaaS 会根据用户已经配置完成的 API 服务（包括其 Endpoint）生成用户可以调用的开放 API。在 API 用户中心中，我们将会帮助您更好的管理每个 API 服务的用户，以及分配用户对于 API 的使用权限。

[API用户中心](https://console.cloud.tencent.com/eis/apiusercenter) 首页是以列表的形式展示当前可以配置的所有 API 服务信息，但是展示维度与“API管理”略有不同。
![](https://qcloudimg.tencent-cloud.cn/raw/d407877d42b4639133effd9bef8696d8.png)


### 用户管理

用户管理功能允许API的提供者帮助其用户添加及管理账号、分配权限，并获取请求API时所需要的所有必要信息。

API 服务提供方可以将会以类似管理者的视角去统一管理用户，允许查看用户的OAuth信息并分享给用户以便用户调用，或者进行用户的封禁和启用。
![](https://qcloudimg.tencent-cloud.cn/raw/fa00eaf3f54208a7599bcca3e4680623.png)

添加用户的时候需要提供以下用户信息，以便能够更好的记录和维护。同时，此处的用户名称和用户密码也将作为对应 API 服务的 Basic Auth 验证方式。
<img src="https://qcloudimg.tencent-cloud.cn/raw/f31e590cd3c5850d56b478e7a2be849f.png" width="50%">

当创建好用户之后，则可以通过“查看详细信息”按钮获取到用户的client ID，client Secret等内容
<img src="https://qcloudimg.tencent-cloud.cn/raw/d9a6d082efadb0d1a65092176f5e3bbe.png" width="50%">

>?当前仅支持 API 服务提供方手动帮助客户添加成员信息和账户信息，客户的自助注册的能力暂不支持。


## 使用流程

1. 创建 API 服务及其 API Endpoint。（具体操作请参考[创建 API 服务](#service)、[创建 API Endpoint](#endpoint)）
2. 获取 API 请求地址。
  1. 在 API 服务列表中获取 API 服务的域名。
![](https://qcloudimg.tencent-cloud.cn/raw/7446bbcc7d139f9f3e03c90426857839.png)
  2. 在 API Endpoint 列表中获取需要请求的 Endpoint 路径。
![获取路径](https://qcloudimg.tencent-cloud.cn/raw/28c050b0218db15495270a6b148836ca.png)
  3. 将 Endpoint 路径拼接在 API 服务域名后面，即可获取完整的 API 请求域名。**请将此域名保存，[步骤4](#step4) 中会用到**。

3. 获取用户请求 API 的权限。
 1. 在 [API用户中心](https://console.cloud.tencent.com/eis/apiusercenter) 首页单击**用户管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/d8789aac761181e4cb9d7f987df12027.png)
 2. 单击**添加用户**，并配置以下信息。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/6d7108fc269981726fb16ee4d145e079.png" width="50%">
 3. 帮助用户填写必要信息，并选择需要访问的 API 服务名称。
![](https://qcloudimg.tencent-cloud.cn/raw/0503bace32b1f91bec4c6c9057833777.png)
 4. 绑定好 API 服务之后，返回用户管理列表获取此用户的 OAuth 信息（当前系统会默认给添加的用户进行自动审批，所以无需手动审批操作），并复制保存 OAuth 的 Token 获取地址、Client ID、Client Secret 等信息，连同用户的账号和密码一同分享给用户。
![](https://qcloudimg.tencent-cloud.cn/raw/4000fb147f3cc74338b744f61ac64aa0.png)

4. 从用户侧调用 API（以 postman 为例）。[](id:step4)
API 服务无需验证的情况：
![](https://qcloudimg.tencent-cloud.cn/raw/f964a769a60ac3a8b9c366460073fc6a.png)
API 服务需要 Basic Auth 的情况：
![](https://qcloudimg.tencent-cloud.cn/raw/d6c4943a83fddb32ae4600ac37dbda3c.png)
API 服务需要 OAuth2.0的情况：
 1. 在用户信息处获取 Client ID 和 Client Secret，在待访问的 API 服务页面获取 Access Token URL。 
<dx-tabs>
::: 获取 OAuth 信息
	 ![获取OAuth信息](https://qcloudimg.tencent-cloud.cn/raw/1af24df69318189138461b114fec41cb.png)
:::
::: 获取 token 地址
![获取token地址](https://qcloudimg.tencent-cloud.cn/raw/77aeacb3f8a34540e209742a6910b3cb.png)
token 地址如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/5cb8ef3f3b714faea702772b0212ca2e.png" width="80%">
:::
</dx-tabs>
   2. 复制之后，在 postman 中创建一个新的请求，填写入上方的 token 获取地址并使用“GET”方法（此处的鉴权方式应为“NoAuth”）。随后选择 Params 标签页，输入 client 信息。输入方式：
    - 第一列：key 为 client_id，value 为从上方复制的 Client ID 对应的内容
    - 第二列：key 为 client_sectet，value 为从上方复制的 Client Secret 对应的内容
	 ![](https://qcloudimg.tencent-cloud.cn/raw/2dbb2bfc7c8cef369a1b3333cc559692.png)
   3. 单击 **send**，从界面下方的“body”处复制“access_token”字段的值。此即为本次调用时需要用到的 token 信息。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/bb1f4a7aa010bd164ecd13aed816911a.png)  
   4. 重新打开一个请求界面，填入需要请求的 API 域名，并选择 Bearer Token 模式。在右侧的“Token”处输入前面获得的token，单击 **send**，即可看到访问结果。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/3a0e8f51315868c916703bd8b7aa65cb.png)
   




   
