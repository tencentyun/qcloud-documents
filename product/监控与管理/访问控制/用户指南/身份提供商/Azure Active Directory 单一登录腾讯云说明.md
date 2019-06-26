Azure Active Directory （Azure AD） 是 Microsoft 推出的基于云的标识和访问管理服务，可帮助员工管理内外部资源。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。您可以通过基于 SAML 2.0 联合身份验证将 Azure Active Directory 与腾讯云进行集成，从而实现 Azure AD 账户自动登录腾讯云控制台（单一登录）管理腾讯云的资源，而不必为企业或组织中的每一个成员都创建一个 CAM 子用户。

## 创建 Azure AD 企业应用程序
您可以通过本步骤创建 Azure AD 企业应用程序，如您已经有正在使用的应用程序，可忽略本操作，进行配置 CAM（跳转至目录 “配置 CAM”）。
1. 进入 [Azure AD 门户页](https://portal.azure.com/#home)，点击左侧导航面板中，单击【Azure Active Directory】。如下图所示：
![](https://main.qcloudimg.com/raw/69bac51131949b7c9e471b5e1afdab86.png)
2. 单击【企业应用程序】>【所有应用程序】。如下图所示：
![](https://main.qcloudimg.com/raw/14c757580dd69950b7ce6352aaadcafc.png)
3. 单击对话框顶部的【新建应用程序】，选择【非库应用程序】。如下图所示：
![](https://main.qcloudimg.com/raw/2612274fc991eaebaec4e102048b29fe.png)
4. 填写【名称】，单击下方【添加】，Azure AD 应用程序创建完成。如下图所示：
![](https://main.qcloudimg.com/raw/94c765a2f385e47e641f9befbcb538bf.png)

## 配置 CAM
您可以通过本步骤配置 Azure AD 和腾讯云之间的信任关系使之相互信任。您可以通过在 Azure AD 下载【联合元数据 XML】文件，上传至腾讯云完成验证。
1. 访问您已创建的 Azure AD 应用程序概览页（或通过单击左侧导航【Azure Active Directory】>【企业应用程序】>【所有应用程序】> 选择您已创建的应用程序）。
2. 单击【单一登录】打开单一登录方法页面，单击【SAML】。如下图所示：
![](https://main.qcloudimg.com/raw/103a22a9aed1c2a8f87f7c8fdcb38297.png)
3. 在 SAML 单一登录 - 预览版页界面，下载【SAML签名证书】中【联合元数据 XML】文件。如下图所示：
![](https://main.qcloudimg.com/raw/e2b9ed5ca753af40f8a3501d88168cec.png)
4. 在腾讯云创建 SAML 身份提供商及角色，详细请参考 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)。

## 配置 Azure AD 的单一登录
您可以通过本步骤将 Azure AD 应用程序属性映射到腾讯云的属性，建立 Azure AD 应用程序和腾讯云的互信关系。
1. 在 SAML 单一登录 - 预览版界面，编辑基本 SAML 配置。如下图所示：
![](https://main.qcloudimg.com/raw/abeffc5c30a39561448523a5fc29b8ee.png)
2. 填写以下信息：
 - 标识符（实体ID）：http://cloud.tencent.com
 - 回复URL（断言使用者服务URL）：https://cloud.tencent.com/login/saml
3. 单击左上角【保存】。如下图所示：
![](https://main.qcloudimg.com/raw/d13c71c27fe913bc2d9c21949f731a02.png)
4. 关闭基本 SAML 配置对话框，编辑【用户属性和声明】，点击左上角【添加新的声明】。如下图所示：
![](https://main.qcloudimg.com/raw/4116fdd96ea5815f79db7c4aef508289.png)
5. 增加两条声明，具体信息如下：

| 名称 | 命名空间 | 源 | 源属性 |
|---------|---------|---------|---------|
|Role | https://cloud.tencent.com/SAML/Attributes | 属性 |qcs::cam::uin/{AccountID}:roleName/{RoleName},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName}<sup>1</sup>|
|RoleSessionName| https://cloud.tencent.com/SAML/Attributes | 属性 | Test |
>?<sup>1</sup>在 Role 源属性中：
>- {AccountID} 替换为您的腾讯云帐户 ID，可前往腾讯云账号中心 - [账号信息](https://console.cloud.tencent.com/developer) 查看。
>- {RoleName} 替换您的 CAM 角色名称，可前往腾讯云 CAM 控制台 - 角色管理查看。
>- {ProviderName} 替换您在腾讯云填写的 SAML 身份提供商名称，可前往腾讯云 CAM 控制台 - [身份提供商](https://console.cloud.tencent.com/cam/idp) 查看。

6. 单击右上角【SAVE】保存配置。

## 配置 Azure AD 用户
您可以通过本步骤分配用户访问权限，向 Azure AD 用户分配腾讯云的 SSO 访问权限。
1.	单击左侧导航【Azure Active Directory】，单击【用户】>【所有用户】。如下图所示：
![](https://main.qcloudimg.com/raw/7ca36c24562a867451312e003c4afd25.png)
2. <span id="step2"></span>单击左上角【新建用户】，填写【姓名】、【用户名】<sup>1</sup>，勾选【显示密码】，单击下方【创建】完成创建。如下图所示：
![](https://main.qcloudimg.com/raw/511cc41e3da391d05ae1cf69daef4994.png)
3. 单击左侧导航【Azure Active Directory】>【企业应用程序】> 选择您之前创建的应用程序，单击【用户和组】。
![](https://main.qcloudimg.com/raw/0fbc968bbdcdc1b1378e79a5e116d28a.png)
4. 单击左上角【添加用户】，单击【用户和组】选择上一步骤创建的用户及您的 Microsoft 帐户，单击【选择】。如下图所示：
![](https://main.qcloudimg.com/raw/bd12f9c49ef1fd01bafc1d88566798e7.png)
5. 跳转到添加分配页面，确认后单击【分配】。
6. 在 SAML 单一登录 - 预览版界面（即单击左侧【Azure Active Directory】>【企业应用程序】> 选择您之前创建的应用程序，单击【单一登录】），单击底部【测试】。如下图所示：
![](https://main.qcloudimg.com/raw/3be1fec2ce529715a56f5a18ff6c20ce.png)
7. 跳转到测试单一登录界面，选择【以其他用户的身份登录】。
8. 输入之前 [步骤2](#step2) 保存的用户名、密码，登录腾讯云控制台。
>?<sup>1</sup>用户名格式为：用户名@域名，其中用户名您可以自定义，域名可以点击左侧【Azure Active Directory】> 概述，查看您之前设置的【初始域名】，您可以复制保存用户名、密码留用。
