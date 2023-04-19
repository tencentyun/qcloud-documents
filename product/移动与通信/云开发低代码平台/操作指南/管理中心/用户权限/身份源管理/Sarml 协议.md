<dx-steps>
-[创建 saml 协议身份源 ](#step1)
-[在 samltest 里上传微搭元数据链接 ](#step2)
-[在编辑器 - 登录设置选中 samltest 身份源](#step3) 
-[应用发布后使用第三方认证源登录](#step4) 
-[复制第三方用户的角色 ID，创建角色](#step5)
</dx-steps>


## 操作步骤
[](id:step1)
### 步骤1：创建 saml 协议身份源 
登录 **[微搭低代码](https://console.cloud.tencent.com/lowcode/overview/index)** > **身份源管理** > **新建认证源**，创建 saml 协议身份源。
1. 选择认证源协议为 saml。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/565b35bf750139e7d1f782843ab86833.png"  style = "width:80%"> 
2. 在**微搭** > **身份源管理**上传 **samltest** 元数据。先单击下载 [**第三方元数据**](https://samltest.id/download/) 。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/97ccbf7c04b87abc1b79602076c9b494.png"  style = "width:80%"> 
再下载  [**SAMLTest IdP only**](https://samltest.id/saml/idp)  文档后上传到微搭。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/153e461744a7941df6be06694dfda54e.png"  style = "width:80%"> 


[](id:step2)
### 步骤2：在 samltest 里上传微搭元数据链接
在 **samltest** 里上传微搭元数据链接。 
1. 复制**微搭的元数据 URL**。<dx-codeblock>
:::  html
https://lowcode-1gf52uyb34bc16a7.ap-shanghai.tcb-api.tencentcloudapi.com/auth/v1/saml/sp/metadata/smaltest
:::
</dx-codeblock> 
2. 进入到第三方 idp 里上传，URL 粘贴后直接单击 [fetch](https://samltest.id/upload.php)。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/884439fd36d9e01dfb61489c03a68ec6.png"  style = "width:80%">   
3. 上传完成。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/12fa6ae15e2937bd4bb5cc35e9ba1a83.jpg"  style = "width:80%">  
4. 账号关联。
 账号关联目前的策略暂无匹配规则，无需配置。 
<img src = "https://qcloudimg.tencent-cloud.cn/raw/eb63d7ffaf23a826dcba20615cb35c7a.png"  style = "width:80%">  
5. 创建完成。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/02c918019c7100a0d0b54e86ab6a984b.png"  style = "width:80%">  

[](id:step3)
### 步骤3：在编辑器 - 登录设置选中 samltest 身份源
在**微搭**创建一个自定义应用。在**编辑器** > **登录设置**里选中 samltest 身份源。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/77b51480096e0a1d7b588b3e21760d7b.png"  style = "width:80%">   


[](id:step4)
### 步骤4：应用发布后使用第三方认证源登录
1. 发布应用。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/a9cd5919453edd6c6755dace760ebd1c.png" style = "width:80%"> 
2. 访问应用时直接进入登录页，单击第三方认证源。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/243ec4a34b5c454dd26c4970520d53c7.png" style = "width:80%">  
3. 跳转到第三方 idp 登录页面。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/ca74d18adbfbedbe40bf043388b4525f.png" style = "width:80%">  
4. 用测试账号登录。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/0cdf92ea9e87c844cc74fff381c7cfac.png" style = "width:80%">  
5. 登录成功后，选择 **Accept**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/e3364ed5e98d47a7d85870271a47499d.png" style = "width:80%"> 


[](id:step5)
### 步骤5（可选）：复制第三方用户的角色 ID，创建角色
复制第三方用户的角色 ID，创建角色。
1. 如果此处不设置，则默认按照登录设置里的统一角色访问应用。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/f9008566bd6b8de3cf4294eb948163ec.png" style = "width:80%">  
2. 如果对应用户想按照明确角色访问微搭应用，则需要定义微搭角色，复制第三方的角色 ID：
<dx-codeblock>
:::  html
mailto:employee@samltest.id
:::
</dx-codeblock>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/ff3e15e29776f34acb953c1162b7a3ab.png" style = "width:60%"><br>
粘贴第三方的角色 ID 到微搭角色标识。<br>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/86ca6ffb8604c2a759eb0c58b5466eef.png" style = "width:50%">  <br>
默认此角色没有访问权限。<br>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/b3dbdcb102af981f65a409440f1d1eb4.png" style = "width:80%">  <br>
登录成功后直接进入微搭应用首页。<br>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/b7b6b104406ac9fc91016abadcca60e5.png" style = "width:80%"> <br>
可以查看到登录后的第三方用户信息。<br>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/a139320538210aa2a565ac55e4b5066e.png" style = "width:80%"> 
