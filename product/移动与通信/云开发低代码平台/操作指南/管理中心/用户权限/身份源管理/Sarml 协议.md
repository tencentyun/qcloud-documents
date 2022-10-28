当企业或组织已有自己的账号体系，同时希望管理组织内成员可以直接使用微搭开发的应用资源。微搭提供适配单点登录 OAuth、SAML 2.0标准协议的集成配置能力，可以快速打通第三方用户身份，集成后可复用已有账号体系来登录使用对应的微搭应用，帮助企业用户通过一套用户账号即可访问所有内外部应用。本文通过微搭 SSO 集成操作并以 Github 为例对身份源管理进行讲解。

<dx-steps>
-[在**微搭**开发平台创建一个 saml 协议的身份源](#step1)
-[在 **samltest** 里上传微搭的元数据链接 ](#step2)
-[在 **微搭** > 创建一个自定义应用，**编辑器** > **登录设置**里选中 samltest 身份源 ](#step3) 
-[在应用发布后使用](#step4) 
-[第五步（可选）：复制第三方用户的 role，在**微搭** > **角色权限里**创建一个角色，粘贴到角色标识应用发布后使用](#step5)
</dx-steps>


## 操作步骤
[](id:step1)
### 步骤1：在微搭开发平台创建一个 saml 协议的身份源
1. 选择认证源协议为 saml。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/565b35bf750139e7d1f782843ab86833.png"  style = "width:80%"> 
2.  在**微搭** > **身份源管理**上传 **samltest** 元数据。
先单击下载 [**第三方元数据**](https://samltest.id/download/) 。
 -  [**SAMLTest IdP only**](https://samltest.id/saml/idp) 
下载 idp 文档后上传到微搭。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/153e461744a7941df6be06694dfda54e.png"  style = "width:80%"> 


[](id:step2)
### 步骤2：在 samltest 里上传微搭的元数据链接
1. 复制**微搭的元数据 URL**。<dx-codeblock>
:::  html
https://lowcode-1gf52uyb34bc16a7.ap-shanghai.tcb-api.tencentcloudapi.com/auth/v1/saml/sp/metadata/smaltest
:::
</dx-codeblock> 
2. 进入到第三方 idp 里上传，url 粘贴后直接单击 [fetch](https://samltest.id/upload.php)。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/884439fd36d9e01dfb61489c03a68ec6.png"  style = "width:80%">   
3. 上传完成。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/12fa6ae15e2937bd4bb5cc35e9ba1a83.jpg"  style = "width:80%">  
4. 账号关联。
 账号关联目前的策略暂无匹配规则，无需配置。 
<img src = "https://qcloudimg.tencent-cloud.cn/raw/eb63d7ffaf23a826dcba20615cb35c7a.png"  style = "width:80%">  
5. 创建完成。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/37b289f71be1191ac2038073b73aed6e.png"  style = "width:80%">  


[](id:step3)
### 步骤3：在微搭创建一个自定义应用
**编辑器** > **登录设置**里选中 samltest 身份源。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/77b51480096e0a1d7b588b3e21760d7b.png"  style = "width:80%">   





[](id:step4)
### 步骤4：应用发布后使用
<img src = "https://qcloudimg.tencent-cloud.cn/raw/4516ffeb43f697409ab026831003bb81.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/23cd95d69ad8e33345ac2f8e32dd42d4.png" style = "width:80%">  
[点击跳转登录 - 腾讯云微搭低代码](https://lowcode-1gf52uyb34bc16a7-1302542649.tcloudbaseapp.com/app-ZTUbBDqY/production/) 
<img src = "https://qcloudimg.tencent-cloud.cn/raw/243ec4a34b5c454dd26c4970520d53c7.png" style = "width:80%">  
跳转到第三方 idp 登录页面。
用测试账号登录测试：sheldon。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/7e82c7dbe9b49c6c23c01e53c900e01b.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/ca74d18adbfbedbe40bf043388b4525f.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/0cdf92ea9e87c844cc74fff381c7cfac.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/e3364ed5e98d47a7d85870271a47499d.png" style = "width:80%"> 






[](id:step5)
### 步骤5（可选）：复制第三方用户的 role，在【微搭】-【角色权限里】创建一个角色，粘贴到角色标识

1.如果此处不设置，则默认按照登录设置里的统一角色访问应用
<img src = "https://qcloudimg.tencent-cloud.cn/raw/3dbd36f3a6cf427b9cea07b1fadb296a.png" style = "width:80%">  
2.如果对应用户想按照明确角色访问微搭应用，则需要定义
 - 复制第三方的角色 ID：
<dx-codeblock>
:::  html
mailto:employee@samltest.id
:::
</dx-codeblock>

<img src = "https://qcloudimg.tencent-cloud.cn/raw/75a682d70eef7a4f0aed9812a281451b.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/86ca6ffb8604c2a759eb0c58b5466eef.png" style = "width:80%">  
默认此角色没有访问权限 
<img src = "https://qcloudimg.tencent-cloud.cn/raw/b3dbdcb102af981f65a409440f1d1eb4.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/5f3e5b9aa7b7d8fdaf4335ae9a2272cf.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/0e942e8530ef0d6e25f6bf8a537079fc.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/b7b6b104406ac9fc91016abadcca60e5.png" style = "width:80%">  
<img src = "https://qcloudimg.tencent-cloud.cn/raw/a139320538210aa2a565ac55e4b5066e.png" style = "width:80%"> 




<dx-codeblock>
:::  html
 { 
    "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjExY2U1ZGEwLThjN2ItNGFiNS05NWEwLWU0ZmNkNWZmOTZjOSJ9.eyJpc3MiOiJodHRwczovL2xvd2NvZGUtMWdmNTJ1eWIzNGJjMTZhNy5hcC1zaGFuZ2hhaS50Y2ItYXBpLnRlbmNlbnRjbG91ZGFwaS5jb20iLCJzdWIiOiJzbWFsdGVzdDpzaGVsZG9uIiwiYXVkIjoiQU9KOHlBQUJVR05HajB6TTdEWSIsImV4cCI6MTY1NTE1OTUzMiwiaWF0IjoxNjU1MTIzNTMyLCJub25jZSI6IjM2ZTM0MDAzLTk5ODctNDNlNy1iODk1LTZhN2YwMjIxYTJiMiIsImF0X2hhc2giOiJ2Y1hSNlFCR1JTeVZJWlhZOGwwYmNBIiwibmFtZSI6IlNoZWxkb3IiLCJlbWFpbCI6InNjb29wZXJAc2FtbHRlc3QuaWQiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGhvbmVfbnVtYmVyIjoiKzEgNTU1NTU1NTUxNSIsInBob25lX251bWJlcl92ZXJpZmllZCI6dHJ1ZSwic2NvcGUiOiJjdXN0b20gdXNlciBzc28iLCJwcm9qZWN0X2lkIjoibG93Y29kZS0xZ2Y1MnV5YjM0YmMxNmE3IiwicHJvdmlkZXIiOiJzbWFsdGVzdDpzY29vcGVyQHNhbWx0ZXN0LmlkIiwiZ3JvdXBzIjpbImVtcGxveWVlQHNhbWx0ZXN0LmlkIl19.X3VzNj5HjUpphm42JG_kVOgg8ILvISFJlJvvTtzwKw9wCb3E5hRHrI3fuWpKZDNAm6ilszZPDsTJbJ6Mp9Q3KYTabrgoGgooUTaSfEUVMixL2KLfOcOt3pcCYH4uh3y9rZJa18r9u5drCCs4x_6tEdiRklwDDTWSh2OOPivjYmDd0Gd9TFDjCnXWNCERA2Td6dtL2rrEYOXdDNYTLsL-rNcJU5jxOI9P3niitavTLe_5PuYlNClkdOPzxiQ4e5KJIlozov1qp8IMDCoZWJ6B9XIINyoLMIUS6uI6gp3sTS6Vycr3XrHVjNYjoEoJAW9AnP3RsmmCZO33ePn8x1ImWA", 
   "expires_in": 36000, 
   "scope": "custom user sso", 
   "sub": "smaltest:sheldon", 
   "groups": [
     "mailto:employee@samltest.id"
   ],
   "expires_at": "2022-06-13T22:31:42.815Z" 
 } 

:::
</dx-codeblock>
