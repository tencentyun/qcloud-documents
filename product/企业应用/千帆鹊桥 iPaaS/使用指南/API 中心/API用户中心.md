腾讯云数据连接器会根据用户已经配置完成的 API 服务（包括其 Endpoint）生成用户可以调用的开放 API。在 API 用户中心中，我们将会帮助您更好的管理每个 API 服务的用户，以及分配用户对于 API 的使用权限。

[API 用户中心](https://console.cloud.tencent.com/eis/apiusercenter) 首页是以列表的形式展示当前可以配置的所有 API 服务信息，但是展示维度与“API管理”略有不同。
![](https://qcloudimg.tencent-cloud.cn/raw/d407877d42b4639133effd9bef8696d8.png)


## 用户管理

用户管理功能允许 API 的提供者帮助其用户添加及管理账号、分配权限，并获取请求 API 时所需要的所有必要信息。

API 服务提供方可以将会以类似管理者的视角去统一管理用户，允许查看用户的 OAuth 信息并分享给用户以便用户调用，或者进行用户的封禁和启用。
![](https://qcloudimg.tencent-cloud.cn/raw/fa00eaf3f54208a7599bcca3e4680623.png)

添加用户的时候需要提供以下用户信息，以便能够更好的记录和维护。同时，此处的用户名称和用户密码也将作为对应 API 服务的 Basic Auth 验证方式。
<img src="https://qcloudimg.tencent-cloud.cn/raw/f31e590cd3c5850d56b478e7a2be849f.png" width="50%">

当创建好用户之后，则可以通过“查看详细信息”按钮获取到用户的client ID，client Secret等内容
<img src="https://qcloudimg.tencent-cloud.cn/raw/d9a6d082efadb0d1a65092176f5e3bbe.png" width="50%">

>?当前仅支持 API 服务提供方手动帮助客户添加成员信息和账户信息，客户的自助注册的能力暂不支持。


## 使用流程
### 步骤1：创建 API 服务及其 API Endpoint
具体操作请参考 [创建 API 服务](https://cloud.tencent.com/document/product/1270/62263#service)、[创建 API Endpoint](https://cloud.tencent.com/document/product/1270/62263#endpoint)。

### 步骤2：获取 API 请求地址
1. 在 API 服务列表中获取 API 服务的域名。
![](https://qcloudimg.tencent-cloud.cn/raw/7446bbcc7d139f9f3e03c90426857839.png)
2. 在 API Endpoint 列表中获取需要请求的 Endpoint 路径。
![获取路径](https://qcloudimg.tencent-cloud.cn/raw/28c050b0218db15495270a6b148836ca.png)
3. 将 Endpoint 路径拼接在 API 服务域名后面，即可获取完整的 API 请求域名。**请将此域名保存，[步骤4](#step4) 中会用到**。

### 步骤3：获取用户请求 API 的权限
1. 在 [API用户中心](https://console.cloud.tencent.com/eis/apiusercenter) 首页单击**用户管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/d8789aac761181e4cb9d7f987df12027.png)
2. 单击**添加用户**，并配置以下信息。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/6d7108fc269981726fb16ee4d145e079.png" width="50%">
3. 帮助用户填写必要信息，并选择需要访问的 API 服务名称。
![](https://qcloudimg.tencent-cloud.cn/raw/0503bace32b1f91bec4c6c9057833777.png)
4. 绑定好 API 服务之后，返回用户管理列表获取此用户的 OAuth 信息（当前系统会默认给添加的用户进行自动审批，所以无需手动审批操作），并复制保存 OAuth 的 Token 获取地址、Client ID、Client Secret 等信息，连同用户的账号和密码一同分享给用户。
![](https://qcloudimg.tencent-cloud.cn/raw/4000fb147f3cc74338b744f61ac64aa0.png)

[](id:step4)
### 步骤4：从用户侧调用 API（以 postman 为例）
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
   
