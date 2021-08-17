## 前提条件
已经开通腾讯云 [API 网关服务](https://console.cloud.tencent.com/apigateway/index?rid=1) 和[  数字身份管控平台（员工版）服务](https://cloud.tencent.com/document/product/1442/56964)。

## 操作步骤

### Web 客户端调用 API
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏中，单击 【服务】 >【基本信息】，进入服务基本信息页面。
![](https://main.qcloudimg.com/raw/0d9f6e20f1b440aef056778fff28e758.png)
2. 在服务基本信息页面，选择之前所创建的服务，单击“服务名”，进入该服务的 API 管理界面。
![](https://main.qcloudimg.com/raw/fdcf0f86b205be47aca38c90ecd1676a.png)
3. 在 API 管理界面，选择所需的ID，单击“ID/名称”，进入该 ID 的基本信息页面。
![](https://main.qcloudimg.com/raw/46d885bfb05ea1291976f09816aab649.png) 
4. 在基本信息页面，取 API 访问地址，如下：
![](https://main.qcloudimg.com/raw/80baae4ef49903c4add76f67708eb741.png)
5. 通过浏览器发起访问 API，自动跳转到 EIAM 认证门户登录页面输入帐号和密码，单击【登录】，成功登录后会返回 API 输出信息。
![](https://main.qcloudimg.com/raw/25e347f42bce46c0287f3445c58b7aec.png)
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
