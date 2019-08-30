## 操作场景
Okta 是身份识别与访问管理解决方案提供商。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。您可以通过基于 SAML 2.0 联合身份验证将 Okta 与腾讯云进行集成，从而实现 Okta 帐户自动登录（单一登录）腾讯云控制台管理腾讯云的资源，不必为企业或组织中的每一个成员都创建一个 CAM 子用户。

## 操作步骤
### <span id="stepCREATE"></span>创建 Okta 应用程序
>?您可以通过本步骤创建 Okta 应用程序，如您已经有正在使用的应用程序，可忽略本操作，进行 [配置 CAM](#stepCAM)。
>
1. 登录进入 [Okta 网站](https://qqyu-admin.okta.com/admin/dashboard)，选择 Applications，进入应用管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/5d55782d704ed50fac661603a30aa0d3.jpg)
2. 在应用管理页面，单击【Add Application】。进入添加应用页面。
3. 在添加应用页面，单击【Create New APP】。如下图所示：
![](https://main.qcloudimg.com/raw/c79f6042d72f01434555222f9e6079fd.png)
4. 在 通用设置/General Settings 页面，补充 App name、App logo（可选）、App visibility（可选）信息，单击【Next】，此应用程序可以用于和腾讯云进行集成，实现 Okta 帐户自动登录（单一登录）腾讯云控制台管理腾讯云的资源。


### <span id="stepCAM"></span>为 Okta 应用程序配置 SAML
>?
> - 您可以通过本步骤将 Okta 应用程序属性映射到腾讯云的属性，建立 Okta 和腾讯云之间的信任关系使之相互信任。
> -  如您是参考 [创建 Okta 应用程序](#stepCREATE)  创建的应用程序，可直接进行操作 [步骤3](#stepCREATE) 。
>
1. 前往 [应用管理页面](https://qqyu-admin.okta.com/admin/apps/active) ，单击您创建的应用程序名称。
2. 在通用/GENERAL 页面，单击 SAML Settings 栏下的【Edit】，确认当前 App name、App logo（可选）、App visibility（可选）信息，单击【Next】，进入配置 SAML/Configure SAML 页面。
2. 在配置 SAML/Configure SAML 页面补充 GENERAL、ATTRIBUTE STATEMENTS 的以下信息。如下图所示：

| Name | Name format | Value |
|---------|---------|---------|
| https://cloud.tencent.com/SAML/Attributes/Role | Unspecified| qcs::cam::uin/{AccountID}:roleName/{RoleName},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName}
| https://cloud.tencent.com/SAML/Attributes/RoleSessionName | Unspecified| okta |
>?在 Value 中 {AccountID}，{RoleName}，{ProviderName} 分别替换内容下：
>- {AccountID} 替换为您的腾讯云帐户 ID，可前往 [账号信息 - 控制台](https://console.cloud.tencent.com/developer) 查看。
>- {RoleName}替换您在腾讯云为身份提供商所创建的角色名称（点击查看如何  [在腾讯云为身份提供商创建的角色](https://cloud.tencent.com/document/product/598/19381#.E4.B8.BA.E8.BA.AB.E4.BB.BD.E6.8F.90.E4.BE.9B.E5.95.86.E5.88.9B.E5.BB.BA.E8.A7.92.E8.89.B22) ），角色名称可前往 角色 - 控制台 查看，如需要添加更多可按照该格式添加：qcs::cam::uin/{AccountID}:roleName/{RoleName} ，以 ; 隔开。
>- {ProviderName} 替换您在腾讯云创建的 SAML 身份提供商名称，可前往  [身份提供商 - 控制台](https://console.cloud.tencent.com/cam/idp) 查看。
>
![](https://main.qcloudimg.com/raw/81053cfb0863aa625912eb375dea857f.png)
3. 单击【Next】，进入 Feedback 页面，选择以下信息之后单击【Finish】，完成配置 CAM 操作。如下图所示：
![](https://main.qcloudimg.com/raw/6e927753d30a0707f2c41304f63f1729.png)

### 为 Okta 应用程序配置 SAML 集成
>?您可以通过本步骤配置 Okta 和腾讯云之间的信任关系使之相互信任。
>
1. 登录进入 [Okta 网站](https://qqyu-admin.okta.com/admin/dashboard)，选择 Applications，进入应用管理页面。
2. 在应用管理页面，单击您创建的应用程序名称，进入应用详情页，单击【Sign On】。如下图所示：
![](https://main.qcloudimg.com/raw/3f43a5c67075b28f2ef649e93bfb9b8a.png)
3. 在 Sign On 页面，单击【Identity Provider metadata】查看身份提供商元数据。如下图所示：
![](https://main.qcloudimg.com/raw/ef361bbd2084642ffced8d339ccdeba0.jpg)
4. 获取身份提供商元数据之后可在查看页面右键保存至本地。
5. 在腾讯云创建 SAML 身份提供商及角色，详细操作请参考 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)。


### 配置 Okta 用户
>?您可以通过本步骤分配用户访问权限，向 Okta 用户分配腾讯云的 SSO 访问权限。
>
1. 登录进入 [Okta 网站](https://qqyu-admin.okta.com/admin/dashboard)，单击 Directory 下的【people】，进入用户管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/28eb0bceaebf2de3f073a72ed5bdd6c8.jpg)
2. 在用户管理页面，单击左上角的【Everyone】，找到您需要授权的用户。如下图所示：
![](https://main.qcloudimg.com/raw/cc2022608165d39e0eeb3de495c5b07a.png)
3. 单击用户名称，进入用户详情页，单击左上角【Assigned Applications
】。如下图所示：
![](https://main.qcloudimg.com/raw/7ed74fd59d8d757dabcc2c82a7983582.png)
4. 在弹出的设置窗口中，单击【Done】，完成配置 Okta 用户操作。如下图所示：
![](https://main.qcloudimg.com/raw/2d80e92964f5e7be9849c82ad4017ea7.jpg)
5. 前往 [应用管理页面](https://qqyu-admin.okta.com/admin/apps/active) ，单击您创建的应用程序名称，进入应用详情页。
6. 在应用详情页，选择 GENERAL，复制 App Embed Link 栏下的 EMBED LINK，登录
腾讯云控制台。如下图所示：
![](https://main.qcloudimg.com/raw/b427625b73dd112f53862d98fc1e9b1a.png)
