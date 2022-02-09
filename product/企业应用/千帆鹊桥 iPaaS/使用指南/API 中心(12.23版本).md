各大企业每天都有大量的 API 增长，同时越来越多公司开始公开 Web API，API 的使用场景正在累积。日前，每日 API 调用量不断飙升，如何能够安全有效管理 API 对于企业而言并不容易。

千帆鹊桥 iPaaS 提供 API 发布功能，可以一键将已发布的应用打包生成 API，方便用户进行管理和调用；同时提供 API 管理能力，可以针对 API 进行访问权限管控和流量调度。

## API 管理主页
登录 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，单击左侧工具栏 **API 中心 > API 管理**，即可进入 API 管理的主页面。您可以创建或查看 API，API 列表中展示有 API 服务名称、API 服务状态、API 服务域名、API 更新时间、endpoint 统计、API 服务的鉴权方式以及操作等内容。
![](https://qcloudimg.tencent-cloud.cn/raw/a6335ca9e711cf0ce5ed4684966923c0.png)

## [创建 API 服务](id:create)
API 管理功能支持 3.0.0 版本的 OpenAPI 规范。OpenAPI 3.0.0 规范的对象定义请参考 [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。用户可以通过单击**创建 API 服务**进入 API 创建界面。

**创建步骤：**
1. 配置 API 服务的基本配置，包括 API 服务名称（必填）、API 服务支持的协议类型（必填）、版本号（必填）以及针对该 API 服务的简单描述（非必填）。
![](https://qcloudimg.tencent-cloud.cn/raw/b65b418cb292a017c85af4cdcb1be8ea.png)
2. 配置 API 服务的策略信息，包括 API 服务的鉴权策略和频控、流控策略。
 - 配置鉴权策略：暂时支持 basic Auth，OAuth2.0 和无验证（即不填写检测策略）。
 - 请求频率策略：指从配置时间起，每单位时间内允许的最大请求次数，填写范围为1-5000。
 - 访问限制策略：指从配置时间算起，每单位自然时间内允许的最大访问次数，填写范围为1-5000。
![](https://qcloudimg.tencent-cloud.cn/raw/77728457c7224d888d853dbf01698d02.png)

## [API Endpoint](id:manage)
当我们创建一个 API 服务后，则代表此 API 已经生成，可以开始编辑其具体行为。API Endpoint 指一个 API 服务可以连接的后端服务信息，包括 API 的访问路径（API Path）、API 的调用方式、API Endpoint 绑定的后端服务类型、最近修改时间以及相关操作。默认新创建好的 API 服务没有已绑定的 Endpoint 信息，需要进行创建完成首次的绑定工作。单击**添加 API Endpoint**，即可开启编辑工作。
![](https://qcloudimg.tencent-cloud.cn/raw/6d3bf89d8d0b8dc6e1d20b71cbab41bb.png)

**创建步骤：**
1. 基本配置：填写 Endpoint 的基本信息，包括访问路径、后端服务类型（支持选择现成的集成流或者绑定第三方服务 BASE URL）和后端服务地址。
![](https://qcloudimg.tencent-cloud.cn/raw/eee790c4a7fe213e90a0746bbe584a24.png)
>!
>- 访问路径必须以“/”开头。
>- 当选择的后端服务为“集成流”模式时，集成流只可以选择已发布的，并且配置了拥有 HTTP 监听能力组件的流。
2. 策略信息：与 API 服务的策略信息配置方式类似，允许用户在此 Endpoint 所归属的 API 服务的策略限制基础上，配置第二层策略限制。两层限制共同生效。
>!该处可选择的鉴权策略范围为上层 API 服务的鉴权策略，即若上层 API 服务只允许 OAuth 2.0 的鉴权方式，则下层的 API Endpoint 只允许配置 OAuth 2.0，而无法配置 Basic Auth。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/211c023b4c5eb1a44fea3b54a9392daa.png" width="650px">
3. 参数信息：该步骤允许用户配置访问此 API Endpoint 时可以选用的方法（API Method）和每种方法对应的调用参数信息。
  - API 调用方法可以多选，配置过参数信息的方法将会以浅蓝色底色标注。若想取消，则可以选中想要删除的方法之后，单击其格子内的**删除**即可取消选中。
  - 每一个参数后都提供了一系列操作，分别为：向上移动、向下移动、删除此参数、为该参数添加备注以及选择该参数是否必填。
 ![endpoint参数](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/API%E7%AE%A1%E7%90%86%EF%BC%88%E6%96%B0%EF%BC%89/endpoint%E5%8F%82%E6%95%B0.png)
4. 当上述三步全部配置完成后，单击**完成**，则会返回 Endpoint 列表，列表也会展示已经创建好的 Endpoint 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/d8daddab6c23abfde1023e57aa6b5b4a.png)

## API 用户中心
鹊桥平台会根据用户已经配置完成的 API 服务（包括其 Endpoint）生成用户可以调用的开放 API。在 API 用户中心中，我们将会帮助您更好地管理每个 API 服务的用户，以及分配用户对于 API 的使用权限。API 用户中心首页是以列表的形式展示当前可以配置的所有 API 服务信息，但是展示维度与“API 管理”略有不同。
![](https://qcloudimg.tencent-cloud.cn/raw/f6554e3c999089d7c24e03e8a8687180.png)


### 用户管理
- “用户管理”功能允许 API 的提供者帮助其用户添加及管理账号、分配权限，并获取请求 API 时所需要的所有必要信息。
- API 服务提供方可以将会以类似管理者的视角去统一管理用户，允许查看用户的 OAuth 信息并分享给用户以便用户调用，或者进行用户的封禁和启用。
![](https://qcloudimg.tencent-cloud.cn/raw/be84e1b7a83fed386afb58e0c2ff96fc.png)
- 添加用户时需提供以下用户信息，以便能够更好的记录和维护。同时，该处的用户名称和用户密码也将作为对应 API 服务的 basic auth 验证方式。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ac32936bf9ed1603491cbda6dceb3cb5.png" width="400px">
- 当创建好用户后，则可以通过单击 **OAuth 信息**获取用户的 client ID、client Secret 以及 Token 获取地址。
<img src="https://qcloudimg.tencent-cloud.cn/raw/d5f43f95ab2928d3d50bb1189ead1510.png" width="400px">
- 当前仅支持 API 服务提供方手动帮助客户添加成员信息和账户信息，而客户的自助注册的能力将在近期开放，敬请期待！


### 审批管理
当前版本暂不开放，后期将会随客户自助注册能力同时开放。


## 使用流程
1. [创建 API 服务](#create)及其 [API Endpoint](#manage)，流程参考上方。
2. 获取 API 请求地址。
 1. 在 API 服务列表中获取 API 服务的域名。![](https://qcloudimg.tencent-cloud.cn/raw/08e23ac17016f047fa5a7466bd5e4b52.png)
 2. 在 API Endpoint 列表中获取需要请求的 Endpoint 路径。![](https://qcloudimg.tencent-cloud.cn/raw/7d7c31eb072b541db869cab21a73e46b.png)
 
 3. 将 Endpoint 路径拼接在 API 服务域名后，即可获取完整的 API 请求域名。
3. 获取用户请求 API 的权限。
 1. 在 API 用户中心首页单击**用户管理**。![](https://qcloudimg.tencent-cloud.cn/raw/a0ffc2ebf03d2de849c65ac188f7ffd7.png)
 2. 添加用户。![](https://qcloudimg.tencent-cloud.cn/raw/35ce777ea819b7aa6f8aa1f0f3d26244.png)
 3. 帮助用户填写必要信息并选择需要访问的 API 服务名称。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/832d77131731065363b80158278564d4.png" width="400px">
 4. 绑定好 API 服务后，返回用户管理列表获取此用户的 OAuth 信息（当前系统会默认给添加的用户进行自动审批，所以无需手动审批操作），并复制保存 OAuth 的 Token 获取地址、Client ID、Client Secret 等信息，连同用户的账号和密码一同分享给用户。![](https://qcloudimg.tencent-cloud.cn/raw/3da79d3ca42f5f0e0702ccc40467126f.png)
4. 从用户侧调用 API，以 postman 为例：
   - API 服务无需验证的情况：![noauth](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/API%E7%AE%A1%E7%90%86%EF%BC%88%E6%96%B0%EF%BC%89/noauth.png)
   - API 服务需要 basic Auth 的情况：![](https://qcloudimg.tencent-cloud.cn/raw/bd4910f01fd651174684f1fcec633431.png)
   - API 服务需要 OAuth 2.0 的情况：
    1. 首先在用户信息处获取 Access Token URL、Client ID 和 Client Secret。<img src="https://qcloudimg.tencent-cloud.cn/raw/c5212631df8bfd170f51df150badd539.png" width="400px">
    2. 复制后，在 postman 中创建一个新的请求，填入上方的 token 获取地址并使用“GET”方法。**请注意，该处的鉴权方式应为“NoAuth”。**
    3. 选择 Params 标签页，输入 client 信息。输入方式：
       - 第一列 key 为 client_id，value 为从上方复制的 Client ID 对应的内容。
       - 第二轮 key 为 client_sectet，value 为从上方复制的 Client Secret 对应的内容。
![](https://qcloudimg.tencent-cloud.cn/raw/4fabe2c95abaa16184245302bbf90b6f.png)
    4. 单击 **send**，从界面下方的“body”处复制“access_token”字段的值，即为本次调用时需要用到的 token 信息。![](https://qcloudimg.tencent-cloud.cn/raw/2591f478c67f4d33fb93b3872afd7cf9.png)
    5. 重新打开一个请求界面，填入需要请求的 API 域名，并选择 Bearer Token 模式。在右侧的“Token”处输入前面获得的 token，单击 **send**，即可看到访问结果。![](https://qcloudimg.tencent-cloud.cn/raw/7d2f4676638e2a0e7b745b9b1b788557.png)
