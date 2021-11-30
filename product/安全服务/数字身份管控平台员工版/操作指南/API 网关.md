## 步骤1：创建服务
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏中，单击 【服务】 >【基本信息】，进入服务基本信息页面。
![](https://main.qcloudimg.com/raw/0d9f6e20f1b440aef056778fff28e758.png)
2. 在服务基本信息页面，单击【新建】，弹出新建服务弹窗。
3. 在新建服务弹窗中，根据页面提示填写或选择所需内容。
>?
>- 前端类型：“建议为“HTTP”或“HTTPS”；
>- 访问方式：固定为“公网”；
>- 其他项根据实际填写或选择即可。
>
![](https://main.qcloudimg.com/raw/b2854cd8afe2b5bd634c8f80cb4bc5a0.png)
4. 单击【提交】，即可完成服务创建。

## 步骤2：创建 API
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏中，单击 【服务】 >【基本信息】，进入服务基本信息页面。
![](https://main.qcloudimg.com/raw/0d9f6e20f1b440aef056778fff28e758.png)
2. 在服务基本信息页面，选择之前所创建的服务，单击“服务名”，进入该服务的 API 管理界面。
![](https://main.qcloudimg.com/raw/fdcf0f86b205be47aca38c90ecd1676a.png)
3. 在 API 管理界面，单击【新建】，进入新建 API 页面。
![](https://main.qcloudimg.com/raw/c7c55c76d19a56e5c2cb0727dfb03b25.png)
4. 在新建 API 页面，根据页面提示配置所需内容。
 1. 前端配置：根据页面提示填写或选择所需内容，单击【下一步】。
>?
>- 前端类型：建议为“HTTP”或“HTTPS”；
>- 鉴权类型：请选择“EIAM 认证”；
>- 接入方式：
>  - 如选择“新建 EIAM 应用”，会在 EIAM 侧同步创建“云 API 网关”类型的应用；
>  - 如选择“选择已有 EIAM 应用”，下方会出现“选择 EIAM 应用”下拉选择框，需在下拉选择框中选择指定的应用；
>- 认证与鉴权：如选在“只认证不鉴权”，则 API 调用时不检验 API 调用权限。
>- EIAM 应用类型：
>  - 如选择“非 Web 客户端”，则同步创建对应的“授权 API”；
>  - 如选择“Web 客户端”，则通过 Web 客户端首次访问该 API 时，会自动重定向到 EIAM 进行身份认证；
>- Token 有效期，id_token 的有效时间，单位为秒，默认为600，最小值为10，最大值为86400；
>- 其他项根据实际填写或选择即可。
 2. 后端配置：选择合适的后端类型后，填写相关信息，单击【下一步】。
 ![](https://main.qcloudimg.com/raw/e313b466d8997ed17d24cf6ae394129c.png)
 3. 发布服务：无需填写响应结果内容，单击【完成】，选择发布环境和输入备注信息，单击【发布服务】或【稍后自行发布】。
 ![](https://main.qcloudimg.com/raw/80887c1c123e073ff98a02533d57e3b3.png)
 
## 步骤3：创建 API 网关应用（可选）
创建 API 时，如选择“选择已有 EIAM 应用”，则需要 EIAM 侧创建“云 API 网关”类型的应用，才能在下拉选择框中选择应用。
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam)，在左侧导航栏中，单击 【应用管理】，进入应用管理页面。
![](https://main.qcloudimg.com/raw/d483dae8c65854f4f42100aa77469a1e.png)
2. 在应用管理页面，单击【新建应用】，进入新建应用页面，选择“云 API 网关”，单击【下一步】。
![](https://main.qcloudimg.com/raw/2cc3336dea857461fc1ead89e5035f70.png)
3. 在应用管理页面，根据页面提示，一次上传应用图标、输入应用名称、Access_token 有效期，单击【保存】。
![](https://main.qcloudimg.com/raw/ec9564e5e57d8c63548e045e11eaeefc.png)
4. 在应用管理页面，单击【完成】，即可创建 API 网关应用。

## 步骤4：资源级授权（可选）
创建API时，如选择“既认证又鉴权”，则需要 EIAM 侧对 API 进行授权。
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam)，在左侧导航栏中，单击 【授权管理】>【资源级授权】>【组织机构授权】，进入组织机构授权页面。
>?
>- 可根据实际需求，按“组织机构”、“用户组”、“用户”三种维度进行 API 授权。
>- 本文以“组织机构”维度为例，如需从“用户组”或“用户”维度进行 API 授权，可单击【用户组授权】或【用户授权】切换至相应页面，进行以下操作即可。
>
![](https://main.qcloudimg.com/raw/3d2b89974088b22b21f0c20560278a80.png)
2. 在组织机构授权页面，在资源级授权下拉框中选择所需应用。
![](https://main.qcloudimg.com/raw/3f2514412cb201d47dc71ef44341ec4a.png)
3. 在组织机构授权页面，单击【新增授权】，进入新增授权页面，。
![](https://main.qcloudimg.com/raw/f898710169c3870b67c4f37ed17e8fd3.png)
4. 在新增授权页面，选择区域和 API 接口后，单击【下一步：选择组织机构】，
![](https://main.qcloudimg.com/raw/3c686d574c386c21c855980a9f0d2e0a.png)
5. 在新增授权页面，请选择组织机构后，单击【下一步：完成】。
![](https://main.qcloudimg.com/raw/1392b1b44aa0d945194e45a4d6f65269.png)
6. 在新增授权页面，单击【完成】， 即可授权添加成功。

## 步骤5：调用 API
### Web 客户端调用 API
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏中，单击 【服务】 >【基本信息】，进入服务基本信息页面。
![](https://main.qcloudimg.com/raw/0d9f6e20f1b440aef056778fff28e758.png)
2. 在服务基本信息页面，选择之前所创建的服务，单击“服务名”，进入该服务的 API 管理界面。
![](https://main.qcloudimg.com/raw/fdcf0f86b205be47aca38c90ecd1676a.png)
3. 在 API 管理界面，选择所需的ID，单击“ID/名称”，进入该 ID 的基本信息页面。
![](https://main.qcloudimg.com/raw/46d885bfb05ea1291976f09816aab649.png) 
4. 在基本信息页面，取 API 访问地址，如下：
![](https://main.qcloudimg.com/raw/80baae4ef49903c4add76f67708eb741.png)
5. 通过浏览器发起访问 API，自动跳转到 EIAM 认证门户登录页面，输入帐号和密码，单击【登录】，成功登录后会返回 API 输出信息。
![](https://main.qcloudimg.com/raw/da4fd0e126e02fb4078ce4280d49fa78.png)
![](https://main.qcloudimg.com/raw/7c97e3e49ddf22240af9f5bf042928f7.png)

### 非 Web 客户端调用 API
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏中，单击 【服务】 >【基本信息】，进入服务基本信息页面。
![](https://main.qcloudimg.com/raw/0d9f6e20f1b440aef056778fff28e758.png)
2. 在服务基本信息页面，选择之前所创建的服务，单击“服务名”，进入该服务的 API 管理界面。
![](https://main.qcloudimg.com/raw/fdcf0f86b205be47aca38c90ecd1676a.png)
3. 在 API 管理界面，选择所需的ID，单击“ID/名称”，进入该 ID 的基本信息页面。
![](https://main.qcloudimg.com/raw/46d885bfb05ea1291976f09816aab649.png) 
4. 在基本信息页面，取 API 访问地址，如下：
![](https://main.qcloudimg.com/raw/80baae4ef49903c4add76f67708eb741.png)
5. 通过后端程序、postman 等方式，携带 username、password 参数发起访问授权 API，获取返回的 JWT 格式的 id_token，如下：
![](https://main.qcloudimg.com/raw/b879e11025301df554021ad64471c0b9.png)
6. 通过后端程序、postman 等方式，在 HTTP 头部 Authorization 域携带 id_token 参数，以及其他业务参数，访问业务API，如下：
![](https://main.qcloudimg.com/raw/367ec0843cd5d0a37db5f1781f04de11.png)
