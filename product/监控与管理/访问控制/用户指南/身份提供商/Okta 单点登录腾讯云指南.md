## 操作场景
Okta 是身份识别与访问管理解决方案提供商。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。您可以通过基于 SAML 2.0 联合身份验证将 Okta 与腾讯云进行集成，从而实现 Okta 帐户自动登录（单一登录）腾讯云控制台管理腾讯云的资源，不必为企业或组织中的每一个成员都创建一个 CAM 子用户。

## 操作步骤
### <span id="stepCREATE"></span>创建 Okta 应用程序
>?您可以通过本步骤创建 Okta 应用程序，如您已经有正在使用的应用程序，可忽略本操作，进行 [配置 CAM](#stepCAM)。

1. 登录进入 [Okta 网站](https://www.okta.com)，单击右上角【用户名称】>【Your Org】，如下图所示：
![](https://main.qcloudimg.com/raw/29d6e0d2803dfe96284d9745571df382.png)
2. 在 Okta 主页，单击右上角【管理员】，进入管理员界面<span id="stepadmin"></span>。
3. 在管理员页面，选择 Applications，进入应用管理页面<span id="stepapp"></span>。如下图所示：
![](https://main.qcloudimg.com/raw/5d55782d704ed50fac661603a30aa0d3.jpg)
4. 在应用管理页面，单击【Add Application】。进入添加应用页面。
5. 在添加应用页面，单击【Create New APP】。如下图所示：
![](https://main.qcloudimg.com/raw/c79f6042d72f01434555222f9e6079fd.png)
6. 在弹出的创建应用程序/Create a New Application Integration 窗口，选择 Platform 及 Sign on method，其中 Sign on method 设置为 SAML 2.0，单击【Create】，如下图所示：
![](https://main.qcloudimg.com/raw/8126a0a697e4014e64138d7e8b0e5cab.png)
7. 在通用设置/General Settings 页面，补充 App name、App logo（可选）、App visibility（可选）信息，单击【Next】，此应用程序可以用于和腾讯云进行集成，实现 Okta 帐户自动登录（单一登录）腾讯云控制台管理腾讯云的资源。


### <span id="stepCAM"></span>为 Okta 应用程序配置 SAML
>?
> - 您可以通过本步骤将 Okta 应用程序属性映射到腾讯云的属性，建立 Okta 和腾讯云之间的信任关系使之相互信任。
> -  如您是参考 [创建 Okta 应用程序](#stepCREATE)  创建的应用程序，可直接进行操作 [步骤3](#stepbuzhou3) 。

1. 前往 [应用管理页面](#stepapp) ，单击您创建的应用程序名称。
2. 在通用/GENERAL 页面，单击 SAML Settings 栏下的【Edit】，确认当前 App name、App logo（可选）、App visibility（可选）信息，单击【Next】，进入配置 SAML/Configure SAML 页面。
3. <span id="buzhou3"></span>在配置 SAML/Configure SAML 页面将 GENERAL 下 Single sign on URL 和 Audience URL(SP Entity ID)补充为以下信息，如下图所示：
![](https://main.qcloudimg.com/raw/43a621945ad09042a40986abaea67962.png)

>?
> - 如果您的腾讯云账号所在站点为中国站，请按照如下信息进行配置：
 Single sign on URL：https://cloud.tencent.com/login/saml
Audience URL(SP Entity ID)：cloud.tencent.com
> - 如果您的腾讯云账号所在站点为 International ，请按照如下信息进行配置：
 Single sign on URL：https://intl.cloud.tencent.com/login/saml
Audience URL(SP Entity ID)：intl.cloud.tencent.com

4. 在配置 SAML/Configure SAML 页面将 GENERAL 下 ATTRIBUTE STATEMENTS 补充为以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/7114ab440ba1a593111296871fc807f9.png)

| Name | Name format | Value |
|---------|---------|---------|
| https://cloud.tencent.com/SAML/Attributes/Role | Unspecified| qcs::cam::uin/{AccountID}:roleName/{RoleName},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName}
| https://cloud.tencent.com/SAML/Attributes/RoleSessionName | Unspecified| okta |

>? 
>在 Value 中 {AccountID}，{RoleName}，{ProviderName} 分别替换内容下：
 - {AccountID} 替换为您的腾讯云帐户 ID，可前往 [账号信息 - 控制台](https://console.cloud.tencent.com/developer) 查看。
 - {RoleName}替换您在腾讯云为身份提供商所创建的角色名称（单击查看如何在腾讯云  [为身份提供商创建的角色](https://cloud.tencent.com/document/product/598/19381#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.88.9B.E5.BB.BA)），角色名称可前往 [角色 - 控制台](https://console.cloud.tencent.com/cam/role) 查看，如需要添加更多可按照该格式添加：qcs::cam::uin/{AccountID}:roleName/{RoleName} ，以 ; 隔开。
 - {ProviderName} 替换您在腾讯云创建的 SAML 身份提供商名称，可前往  [身份提供商 - 控制台](https://console.cloud.tencent.com/cam/idp) 查看。
>
5. 单击【Next】，进入反馈/Feedback 页面，选择以下信息之后单击【Finish】，完成配置 CAM 操作。如下图所示：
![](https://main.qcloudimg.com/raw/a360cd597c75039a234b16608ca69e6c.png)

### 为 Okta 应用程序配置 SAML 集成
>?您可以通过本步骤配置 Okta 和腾讯云之间的信任关系使之相互信任。

1. 登录进入 [管理员界面](#stepadmin)，选择 Applications，进入应用管理页面。
2. 在应用管理页面，单击您创建的应用程序名称，进入应用详情页，单击【Sign On】。如下图所示：
![](https://main.qcloudimg.com/raw/3f43a5c67075b28f2ef649e93bfb9b8a.png)
3. 在 Sign On 页面，单击【Identity Provider metadata】查看身份提供商元数据。如下图所示：
![](https://main.qcloudimg.com/raw/14e34ce4819d848c056fefa145b11060.png)
4. 获取身份提供商元数据之后可在查看页面右键保存至本地。
5. 在腾讯云创建 SAML 身份提供商及角色，详细操作请参考 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)。


### 配置 Okta 用户
>?您可以通过本步骤分配用户访问权限，向 Okta 用户分配腾讯云的 SSO 访问权限。

1. 登录进入 [管理员界面](#stepadmin)，单击 Directory 下的【people】，进入用户管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/28eb0bceaebf2de3f073a72ed5bdd6c8.jpg)
2. 在用户管理页面，单击左上角的【Everyone】，找到您需要授权的用户。如下图所示：
![](https://main.qcloudimg.com/raw/cc2022608165d39e0eeb3de495c5b07a.png)
3. 单击用户名称，进入用户详情页，单击左上角【Assigned Applications】。如下图所示：
![](https://main.qcloudimg.com/raw/7ed74fd59d8d757dabcc2c82a7983582.png)
4. 在弹出的设置窗口中，单击【Done】，完成配置 Okta 用户操作。如下图所示：
![](https://main.qcloudimg.com/raw/2d80e92964f5e7be9849c82ad4017ea7.jpg)
5. 前往 [应用管理页面](#stepapp) ，单击您创建的应用程序名称，进入应用详情页。
6. 在应用详情页，选择 GENERAL，复制 App Embed Link 栏下的 EMBED LINK，登录腾讯云控制台。
