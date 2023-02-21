>!
>- 试用公有云版本 API 管理需扫码申请（登录 [腾讯云数据连接器控制台](https://ipaas.cloud.tencent.com/)，单击 **API 管理**菜单即可申请）。
>- API 管理的独立环境与应用集成环境不互通。

## 操作场景
各大企业每天都有大量的 API 增长，同时越来越多公司开始公开 Web API，API 的使用场景正在累积。现在，每日 API 调用量在不断飙升，如何能够安全有效将这些 API 管理起来对于企业而言并不容易。
腾讯云数据连接器提供 API 发布功能，可以一键将已发布的应用打包生成 API，方便用户进行管理和调用；同时提供了 API 管理能力，可以针对 API 进行访问权限管控和流量调度。

## 操作步骤
### API 管理主页
登录 [腾讯云数据连接器控制台](https://ipaas.cloud.tencent.com/apimanage)，在左侧导航栏单击 **集成开发** > **API 管理**，即可进入 API 管理的主页。
在 API 管理主页，您可以创建或查看 API 服务、可以查看 API 目录、管理 API 订阅凭证，同时可对 API 服务进行审核管理。
![](https://qcloudimg.tencent-cloud.cn/raw/cc540644652384ec58f60a7d4d954d6c.png)


### API 服务列表
此页面可创建或查看 API 服务。创建完成的 API 服务展示在此列表，项目内所有成员都可查看。
![](https://qcloudimg.tencent-cloud.cn/raw/3bc3caee37b4106f9b76f17ebc0dfd29.png)
API 服务状态有三种：配置中、运行中、已停止。鼠标可 hover 到**服务域名**处查看该 API 服务的发布环境和域名。
API 服务支持的操作有：查看、新建 API、上架、下架、删除、查看描述文件、查看发布历史。

>!
>- 只有服务状态为**配置中**的 API 服务才可有新建 API 和删除的操作。
>- 只有服务状态为**运行中**的 API 服务才可进行上架和下架的操作。
>- 单击 API 服务的名称可跳转到 API 列表页。


### 创建 API 服务
API 管理功能支持 3.0.0 版本的 OpenAPI 规范。OpenAPI 3.0.0 规范的对象定义请参见 [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。用户可以通过单击**创建 API 服务**进入 API 创建界面。
![](https://qcloudimg.tencent-cloud.cn/raw/ab9b3cbc84a97eee6d0d8369d45c2277.png)
创建 API 服务一共有2个步骤。

#### 步骤一：配置服务名称，协议与描述。
服务名称和描述自定义即可，协议支持3种：HTTP、HTTPS、HTTP+HTTPS。分组可选择默认分组、新建分组。如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/7e6123d809d91d859a7298b7c01da47d.png)

#### 步骤二：配置策略信息
- 配置黑白名单：您可以按需开启，开启后可以输入多条 IP 进行黑白名单的访问限制。
- 基础流量控制：您可以按需开启，开启后可配置服务请求频率，每单位时间内允许的最大请求次数，填写范围为1 - 1000。

 当上述配置全部完成后，单击**完成**，则会返回 API 服务列表，同时已经创建好的 API 服务信息将会展示在此处。
![](https://qcloudimg.tencent-cloud.cn/raw/c8e9abab1210a87f83b625b5659db817.png)

### 新建 API
当我们创建好一个 API 服务之后，则代表此 API 已经生成，可以开始编辑其具体行为，包括 API 的请求路径（API Path）、请求方法、分组、鉴权策略、请求参数、策略配置、API 绑定的后端服务类型等操作。
新建 API 一共有3个步骤（附步骤四以 postman 为例从用户侧调用 API）。

#### 步骤一：API 的基础配置
![](https://qcloudimg.tencent-cloud.cn/raw/b66da9824787768c8851fc8fd229364b.png)
API 名称、描述支持自定义。分组可选择默认分组、新建分组。
- 请求方法支持：GET、POST、PATCH、PUT、DELETE、HEAD。
- 鉴权方式支持：NoAuth、BasicAuth、OAuth2.0、HMAC。
- 后端服务类型支持：集成流、第三方服务、数据库、Mock。集成流、第三方服务、Mock 的请求参数可自行添加，最多添加30条。
![](https://qcloudimg.tencent-cloud.cn/raw/c77ed08f54ff871e2b1703b0176f4bdc.png)
- 数据库类型支持新建或选择 MySQL 类型的数据源。
![](https://qcloudimg.tencent-cloud.cn/raw/eceac720481e715399bd36a566372857.png)


#### 步骤二：后端配置
![](https://qcloudimg.tencent-cloud.cn/raw/bfb79548c6642c9eb6f93f8886073bc2.png)
- 选择集成流时：需选择webhook触发的且在运行中的集成流。
- 后端超时时间：可默认系统预设的，也可自定义。
- 请求方法：根据用户需求选择即可。支持：GET、POST、PATCH、PUT、DELETE、HEAD。


#### 步骤三：配置响应示例
![](https://qcloudimg.tencent-cloud.cn/raw/bbe75cd876062ea62e04de343b606cfb.png)
当上述配置全部完成后，单击**完成**，则会返回 API 列表，同时已经创建好的 API 信息将会展示在此处。

  
### API 列表页
创建好的 API 会展示在 API 列表中，此页面可新建、查看和编辑 API。可发布 API、可设置、查看 API 描述文件和调用凭证，可查看 API 的订阅详情。
![](https://qcloudimg.tencent-cloud.cn/raw/d7a474d433639407627c7c8426c5e6b4.png)

左侧是 API 列表，右侧默认 tab 页是 API 的详细配置信息：API 的访问路径、请求方法、参数、后端服务类型等都可在此处查看。

1. 单击**调试** tab 页，进入 API 调试页面。在 API 调试页面，您可以配置此 API Endpoint 的请求 Header 和 Body 内容，并单击**发送请求**。
![](https://qcloudimg.tencent-cloud.cn/raw/4c6e02a83131298733637f10e37ae17f.png)
2. 随后即可获取到测试的结果。我们会将后端服务返回的 Response 状态码和结果返回给用户，方便进行进一步的调试工作。
3. 右上角单击**发布**，可发布此 API 到多个环境。
![](https://qcloudimg.tencent-cloud.cn/raw/cc24769c3cc2e708bd3d3e2506bb52f0.png)
4. 发布后，发布后的API状态为**运行中**。
5. 右上角的**复制**，可将当前版本覆盖到配置中的版本。复制后，API 服务可以再次发布。一个 API 服务可以发布到多个环境。
6. 可在 API 详情页可查看其日志和监控。日志与监控详细信息参见 [运维中心-监控管理](https://cloud.tencent.com/document/product/1270/80363) 和 [运维中心-运行日志](https://cloud.tencent.com/document/product/1270/80364)。
7. 发布后的 API 服务可停止服务。

### 描述文件
描述文件是针对当前 API 服务的说明，左侧展示 YAML/JSON 格式文件，右侧对应展示 Swagger 可视化内容。
![](https://qcloudimg.tencent-cloud.cn/raw/913f09c1af003898b973087d31f9fb44.png)

### 调用凭证
创建 API 服务时，若选择的鉴权策略为 NoAuth，则可忽略此选项，反之，若 API 服务需要鉴权，则需在此页面配置调用凭证。通过当前服务下的任意调用凭证，即可调用服务下任意 API。
![](https://qcloudimg.tencent-cloud.cn/raw/05c6c706d74599bec254ffdb115f4fb5.png)
上图为凭证列表页，创建好的凭证会展示在此处，选择**新建凭证**，即可创建新的凭证。自定义凭证的信息，保存即可。
![](https://qcloudimg.tencent-cloud.cn/raw/028b0fb94946848eb8af9efcabed0e14.png)


### 订阅详情
上架后的 API 服务，可以被该企业主 UIN 下的所有子 UIN 订阅并调用。该菜单可以查看当前 API 服务被订阅的情况。
![](https://qcloudimg.tencent-cloud.cn/raw/2944ef2958cf2ca4549f7139a88b3348.png)
此处可以看到订阅该 API 的所有用户名单，同时，可以移除某用户的订阅。

### 操作
#### 删除 API 服务
单击**删除**，可删除当前 API 服务。删除后，该 API 服务下的所有配置将被清空，且无法恢复。运行中的服务不可直接删除，需先停止再删除。
![](https://qcloudimg.tencent-cloud.cn/raw/397591f142a1c9053c34de29fae05345.png)


#### API 上架与下架
- 上架：运行中的API服务，可通过**上架**功能共享给企业的其他员工使用。在 **API 服务** > **操作** > **更多** > **上架**路径提交上架申请，提交后的 API 服务会被企业管理员审核，审核通过后可展示在 API 目录中，支持被当前主账号下的所有子账号订阅。
- 下架：上架后的 API 服务，若不想继续被其他员工订阅，则可通过下架来完成。在 **API 服务** > **操作** > **更多** > **下架**路径提交下架申请，提交申请后需联系系统管理员或该项目的项目管理员进行审核，审核通过后即可下架，API 下架后不能被订阅。下架后的 API 服务会移出 API 目录。
![](https://qcloudimg.tencent-cloud.cn/raw/b8db2e0df40fb88bc49d45a89d7351db.png)

#### 查看发布历史
发布后的 API 服务可以更改状态、环境等。在 **API 服务** > **操作** > **更多** > **查看发布历史**路径。此功能可查看到 API 服务发布后的历史情况（最多显示10条）。
![](https://qcloudimg.tencent-cloud.cn/raw/197a3e6e81907e85ceb89c11e1e9169c.png)

### API 目录
API 目录展示已上架的 API 服务。类似一个 API 服务市场，上架后的服务，不局限项目维度，可以被当前主账号下的所有子账号查看、订阅并调用。此页面可通过 API 服务的属性快速搜索服务。同时，可申请订阅或取消订阅 API 服务。
![](https://qcloudimg.tencent-cloud.cn/raw/74130b0116189a7731ef2d9eaf2d490b.png)

#### 申请订阅
申请订阅 API 服务时，需选择或新建订阅凭证。将凭证与 API 服务关联上。待系统管理员审核后，即可成功订阅。
![](https://qcloudimg.tencent-cloud.cn/raw/80fdb133fb109623ae360beb6bbde360.png)

#### 取消订阅
取消订阅后将不能调用该 API 服务，此操作无需系统管理员审核。
![](https://qcloudimg.tencent-cloud.cn/raw/c95e2ea0f3477a715f4d14ff13251cf9.png)

### 订阅凭证
此列表可展示或搜索所有的订阅凭证，同时，可新建凭证。订阅凭证用于订阅 API 目录中的服务。凭证即为某 API 服务的钥匙。在申请订阅 API 服务时将凭证与 API 服务关联上，调用的时候填写该凭证，即可成功调用该服务。同时，能看到该凭证各种鉴权类型的 Key 和 Secret，调用时直接复制即可使用。
![](https://qcloudimg.tencent-cloud.cn/raw/334ba7f48ee8d03e57810fb090944e83.png)
一个凭证支持与多个 API 服务关联。可在**订阅的 API** tab 页查看此凭证关联的所有 API 服务。
![](https://qcloudimg.tencent-cloud.cn/raw/d9e4d9e6e2ca191852a7d5bfaebe1336.png)
新建凭证时，自定义相关属性即可。
![](https://qcloudimg.tencent-cloud.cn/raw/d2d282b13cacce4bf686e8117d46d163.png)


### 审核管理
审核管理分两个功能：我提交的和我审核的。涉及到审核的事项都在此功能页处理。

- 我提交的：展示个人提交的所有审核信息。全部角色都可见。
![](https://qcloudimg.tencent-cloud.cn/raw/c5dfb388c642f7caff8d0c2938ab4c81.png)
- 我审核的：此页面展示需审核的信息。只有系统管理员和项目管理员角色能看到。其他角色访问页面数据为空。
 - 系统管理员审批全部项目 API 服务上下架或 API 服务订阅的请求。
 - 项目管理员审批所在项目内的 API 服务上下架或 API 服务订阅的请求。

 ![](https://qcloudimg.tencent-cloud.cn/raw/2fd53195b377dc997c427d9b2d063ed1.png)


## API 调用步骤
### 从用户侧用不同鉴权方式调用 API（以 postman 为例）
- API 服务无需验证的情况：
![](https://qcloudimg.tencent-cloud.cn/raw/c8f0989e13ad33d5180ae002220ded34.png)
- API 服务需要 Basic Auth 的情况：
  1. 复制 API 的调用地址（需先成功发布 API 服务）：
![](https://qcloudimg.tencent-cloud.cn/raw/9bb1700868352347cfbff6b88bc4a7bd.png)
  2. 进入 API 服务详情页面，新建或打开已有**调用凭证**，即可查看用于 Basic Auth 的AK/SK信息：
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c954c391d8cfa6a9574fd7d4ce3c6217.png" /><br>
  3. 打开 postman，将上述获取的 API 调用地址和用于 Basic Auth 的 AK/SK 信息分别填入：
![](https://qcloudimg.tencent-cloud.cn/raw/e008d5181b9bf331a89cbf3a0a82d851.png)
- API 服务需要 OAuth2.0 的情况：
  1. 复制 API 的调用地址（需先成功发布 API 服务），方法同上，不再附图。
  2. 进入 API 服务详情页面，新建或打开已有**调用凭证**，即可查看用于 OAuth2.0 的AK/SK信息：
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/e34861f87d6915fc9068b0e8fab432a9.png" />
  3. 进入 API 服务详情页面，单击并复制对应 API 的 **Token 获取链接**。
![](https://qcloudimg.tencent-cloud.cn/raw/e8954b2063a9749573d486668cecda77.png)
  4. 在 postman 中创建一个新的请求，来获取 accsee_token。
      1. 首先，在输入栏中输入第3步获取的 **Token 获取链接**，并选择 GET 请求方法。
      2. 其次，选择 Params 标签页，分别输入第2步获得的用于 OAuth2.0 的 AK/SK 信息（格式见下图）。
      3. 最后，单击 **send**，即可生成下图中的 access_token 内容，将其复制。

 <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/626b4f966d101dcea127d5f3a1e3ecb7.png" /><br>
  5. 在 postman 重新打开一个请求界面，填入第1步获取的 API 调用地址，Type 选择 OAuth2.0 模式。并在右侧填入第4步获取的 accsee_token，单击 **send**，即可看到访问结果（如果配置 API 时还设置了请求参数，这里也要按位置输入）。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/42574d10fdd12bd6092f75fc72876767.png" />
- API 服务需要 HMAC Auth 的情况：
 1. 复制 API 的调用地址（需先成功发布 API 服务），方法同上，不再附图。
 2. 进入 API 服务详情页面，新建或打开已有**调用凭证**，即可查看用于 HMAC 的 AK/SK 信息：
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/88237bff54654d53122ffe71f69a9d51.png" />
 3. 打开 postman，在输入框填入第1步获取的 API 调用地址。
 4. 将 postman 切换到 Pre-request Script 标签下，粘贴下方代码段（注意用第2步获取的 HMAC 的 Key 和 Secret，分别来替换代码段中的 hmac_key 和 hmac_secret 变量值）。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/44e914ad4e9e94e6402ba26b4c15dba3.png" />
 ```
var hmac_key = "2e4d0bbad47e3b5e3a0c";
var hmac_secret = "815ba6d666d58ef1e79b";

var time = new Date().toUTCString();
console.log("time:" + time)
var signed_headers_string = "";
signing_string= pm.request.method + "\n" + pm.request.url.getPath() + "\n" + pm.request.url.getQueryString() + "\n" + hmac_key + "\n" + time + "\n" + signed_headers_string;
console.log("signing_string:\n" + signing_string);

var signatureBytes = CryptoJS.HmacSHA256(signing_string, hmac_secret);
var requestSignatureBase64String = CryptoJS.enc.Base64.stringify(signatureBytes);
console.log("requestSignatureBase64String:" + requestSignatureBase64String)

//将下面变量记录下来，在请求的Header中进行引用
pm.globals.set("sign", requestSignatureBase64String); //hmac签名
pm.globals.set("hmac_key", hmac_key); //hmac key
pm.globals.set("date", time); //请求时间
```
 5. 将 postman 切换到 Headers 标签下，输入下图中的4个 KEY-VALUE 对。最后，单击 **send**，即可看到调用 API 的返回结果。<br>
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/623981d7d7761ea7e7c44e6d58264530.png" />
