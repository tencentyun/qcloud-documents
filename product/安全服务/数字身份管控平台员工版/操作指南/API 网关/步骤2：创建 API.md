## 前提条件
已经开通腾讯云 [API 网关服务](https://console.cloud.tencent.com/apigateway/index?rid=1) 和[ 数字身份管控平台（员工版）服务](https://cloud.tencent.com/document/product/1442/56964)。

## 操作步骤
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏中，单击 【服务】 >【基本信息】，进入服务基本信息页面。
![](https://main.qcloudimg.com/raw/0d9f6e20f1b440aef056778fff28e758.png)
2. 在服务基本信息页面，选择之前所创建的服务，单击“服务名”，进入该服务的 API 管理界面。
![](https://main.qcloudimg.com/raw/fdcf0f86b205be47aca38c90ecd1676a.png)
3. 在 API 管理界面，单击【新建】，进入新建 API 页面。
![](https://main.qcloudimg.com/raw/c7c55c76d19a56e5c2cb0727dfb03b25.png)
4. 在新建 API 页面，根据页面提示配置所需内容。
 1. 前端配置：根据页面提示填写或选择所需内容，单击【下一步】。
>?
>- 前端类型：建议为“HTTP”或“HTTPS”。
>- 鉴权类型：请选择“EIAM 认证”。
>- 接入方式：
>  - 如选择“新建 EIAM 应用”，会在 EIAM 侧同步创建“云 API 网关”类型的应用。
>  - 如选择“[选择已有 EIAM 应用](https://cloud.tencent.com/document/product/1442/60135)”，下方会出现“选择 EIAM 应用”下拉选择框，需在下拉选择框中选择指定的应用。
>- 认证与鉴权：
>  - 如选“只认证不鉴权”，则 API 调用时不检验 API 调用权限。
>  - 如选“[既认证又鉴权](https://cloud.tencent.com/document/product/1442/60136)”，则 API 调用时需检验 API 调用权限。
>- EIAM 应用类型：
>  - 如选择“非 Web 客户端”，则同步创建对应的“授权 API”。
>  - 如选择“Web 客户端”，则通过 Web 客户端首次访问该 API 时，会自动重定向到 EIAM 进行身份认证。
>- Token 有效期，id_token 的有效时间，单位为秒，默认为600，最小值为10，最大值为86400。
>- 其他项根据实际填写或选择即可。
 2. 后端配置：选择合适的后端类型后，填写相关信息，单击【下一步】。
 ![](https://main.qcloudimg.com/raw/e313b466d8997ed17d24cf6ae394129c.png)
 3. 发布服务：无需填写响应结果内容，单击【完成】，选择发布环境和输入备注信息，单击【发布服务】或【稍后自行发布】。
 ![](https://main.qcloudimg.com/raw/80887c1c123e073ff98a02533d57e3b3.png)
