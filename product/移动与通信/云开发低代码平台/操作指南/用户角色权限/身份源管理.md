当企业或组织已有自己的账号体系，同时希望管理组织内成员可以直接使用微搭开发的应用资源。微搭提供适配单点登录 OAuth、SAML 2.0标准协议的集成配置能力，可以快速打通第三方用户身份，集成后可复用已有账号体系来登录使用对应的微搭应用，帮助企业用户通过一套用户账号即可访问所有内外部应用。本文通过微搭 SSO 集成操作并以 Github 为例对身份源管理进行讲解。

<dx-steps>
-[在**微搭**创建一个自定义应用](#step1)
-[在 **GitHub** 开发平台创建一个 OAuth 应用 ](#step2)
-[在**微搭** > **身份源管理**创建一个身份源，填入 GitHub OAuth 应用配置](#step3) 
-[在微搭创建的自定义应用的**编辑器** > **登录设置**里选中 Github 身份源](#step4) 
-[应用发布后使用](#step5)
</dx-steps>




## 操作步骤
[](id:step1)
### 步骤1：创建自定义应用
1. 进入腾讯云微搭低代码控制台 [**创建新应用**](https://console.cloud.tencent.com/lowcode/create/) 页面，选择**新建自定义应用**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/d568bb9f7a6d0df37c2e098da10a51c7.png"  style = "width:80%"> 
2. 单击后需填写**应用基础信息** 。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/8d4031606e9ee6da4917e5d8af6f3096.png"  style = "width:80%"> 
<dx-alert infotype="explain" title="">
**应用基础信息**包括应用名称、应用描述和应用环境，应用环境本质为云开发环境，主要用于存放应用。
</dx-alert>
3. [](id:step1_3)进入 [**应用**](https://console.cloud.tencent.com/lowcode/app) 页面，找到新建应用，单击**应用详情**进入详情页获取**访问地址**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/0511b55e96ffa86967c7f05106f9cac2.png"  style = "width:80%">  






[](id:step2)
### 步骤2：在 GitHub 开发平台创建 OAuth 应用

1. 登录 GitHub 并进入 [Developer settings](https://github.com/settings/developers) 页面。单击 **Register a new application**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/e1fb9a2e36002d12596fe4c2c81b3cce.png"  style = "width:80%">  
<dx-alert infotype="notice" title="">
用户或组织最多可以拥有100个 OAuth 应用程序。
</dx-alert>
2. [](id:step2_2)填写相应基础信息后单击 **Register application**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/66ff0dc7563b24be3622f5cf54ef448b.png"  style = "width:80%">  
	- Application name：可以填写中英文。
	- Homepage URL：可在 [步骤1.3](#step1_3) 中的应用详情里获取。
	- Authorization callback URL：微搭会提供回调地址，在 [步骤3.4](#step3_4) 的**认证源基础配置**里复制回调 URL，粘贴至上方输入框。



<dx-alert infotype="notice" title="">
GitHub 里创建 OAuth 应用保存，需要完成 [步骤3.3](#step3_3) 的**认证源基础配置**才能完成。
</dx-alert>




[](id:step3)
### 步骤3：创建身份源并配置 GitHub OAuth 应用

1. 进入**用户权限** > [**身份源管理**](https://console.cloud.tencent.com/lowcode/permission/identity/index) 页面。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/6e962ad96652cd7b09d493fad844b526.png"  style = "width:80%">   
2. 单击**新建认证源**，**选择认证源**为 **OAuth 2.0**并单击**下一步**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/1d57ecdef254e63441da6f0970883f32.png"  style = "width:80%">   
3. 填写认证源名称及 logo 等相关信息，单击**下一步**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/7f64f5d8c67c18974d64d82b006ac1bd.png"  style = "width:80%">  
4. [](id:step3_4)认证源基础配置：
<img src = "https://qcloudimg.tencent-cloud.cn/raw/5da773c42572c5c4b03497ea055bd936.png"  style = "width:80%">    
	1. 首先复制**回调 URL** 到上面 [步骤2.2](#step2_2) 的 Authorization callback URL 里，然后保存，会生成对应的 **Client ID** 和 **Client secrets**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/6ec82f5a6a9e80fe6f425183ad0e5bc8.png"   style = "width:80%">  
	2. 复制 **GitHub** 的 **Client ID** 和 **Client secrets** 到**认证源基础配置**页面中，填写相关信息后单击**下一步**。
		 - **授权 URL**：`https://github.com/login/oauth/authorize`  
		 - **Token URL**：`https://github.com/login/oauth/access_token`
		 - **用户信息URL**：`https://api.github.com/user`
>? 更多详情请参见 [**GitHub 授权 OAuth 应用程序操作指引**](https://docs.github.com/cn/developers/apps/building-oauth-apps/authorizing-oauth-apps) 。
5. 账号关联目前的策略暂无匹配规则，无需配置。 
<img src = "https://qcloudimg.tencent-cloud.cn/raw/8c0838c947e2b4094d4ccab831c2896d.png"  style = "width:80%">   
6. 新建完成后可在**身份源管理**页面中查看。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/30a5d392915894c2b5d95ee5d0571d66.png"  style = "width:80%">   



[](id:step4)
### 步骤4：在微搭自定义应用选择 GitHub 身份源

1. 找到 [步骤1](#step1) 中新建的自定义应用，单击**编辑应用**进入应用编辑器，并在左上方单击**登录设置**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/8c00f37207a181cafc12341cbb90c996.png">  
2. 进入**登录页设置**里勾选 GitHub。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/fe54e3fcefe01e2831b95955ef8ad570.png" style = "width:80%">  
3. 访问授权里选择**需登录后访问应用**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/10798df78225323770582d86b9a51e19.png" style = "width:80%">  
4. 安全设置为应用自动退出登录的时间，默认无需设置。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/27e5a0279a4266ba0842a57921d5f352.png" style = "width:80%">  
5. 单击**保存**后返回应用编辑器页面，单击右上角**发布**应用。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/c69a8dea76ddeab5777e9d8e25519be6.png" style = "width:80%">  


[](id:step5)
### 步骤5：登录应用
1. 通过 [步骤1.3](#step1_3) 中的**访问链接**进入应用登录界面。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/2daae4acac1d317c81bb7dd97071f7b3.png" style = "width:80%"> 
2. 填写好 GitHub 账号和密码进行登录认证。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/003ff426317461f4e7a66122270c91dd.jpg" style = "width:80%">  
3. 认证成功后即可访问应用。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/ea68087d5b11f54a527e48f147bbe457.png" style = "width:80%">  

