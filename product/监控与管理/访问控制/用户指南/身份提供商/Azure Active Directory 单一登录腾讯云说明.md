## 操作场景
Azure Active Directory （Azure AD） 是 Microsoft 推出的基于云的标识和访问管理服务，可帮助员工管理内外部资源。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。您可以通过基于 SAML 2.0 联合身份验证将 Azure Active Directory 与腾讯云进行集成，从而实现 Azure AD 帐户自动登录（单一登录）腾讯云控制台管理腾讯云的资源，不必为企业或组织中的每一个成员都创建一个 CAM 子用户。

## 操作步骤
### 创建 Azure AD 企业应用程序
>?您可以通过本步骤创建 Azure AD 企业应用程序，如您已经有正在使用的应用程序，可忽略本操作，进行 [配置 CAM](#stepCAM)。


1. 进入 [Azure AD 门户页](https://portal.azure.com/#home)，单击左侧导航栏中【Azure Active Directory】。如下图所示：
![](https://main.qcloudimg.com/raw/69bac51131949b7c9e471b5e1afdab86.png)
2. 单击【企业应用程序】，选择【所有应用程序】。如下图所示：
![](https://main.qcloudimg.com/raw/14c757580dd69950b7ce6352aaadcafc.png)
3. 单击【新建应用程序】打开“添加应用程序”窗口，选择【非库应用程序】。如下图所示：
![](https://main.qcloudimg.com/raw/2612274fc991eaebaec4e102048b29fe.png)
4. 填写【名称】，单击【添加】，即可完成 Azure AD 应用程序的创建。如下图所示：
![](https://main.qcloudimg.com/raw/94c765a2f385e47e641f9befbcb538bf.png)

### <span id="stepCAM"></span>配置 CAM
>?您可以通过本步骤配置 Azure AD 和腾讯云之间的信任关系使之相互信任。
>
1. 在左侧导航栏中，选择【Azure Active Directory】>【企业应用程序】> 您创建的应用程序 ，进入应用程序概览页面。
2. 单击【单一登录】，打开“选择单一登录方法”页面。
3. 在打开的“选择单一登录方法”页面，选择【SAML】。如下图所示：
![](https://main.qcloudimg.com/raw/103a22a9aed1c2a8f87f7c8fdcb38297.png)
4. 在 “SAML 单一登录”的预览页面，下载【SAML签名证书】中的【联合元数据 XML】文件。如下图所示：
![](https://main.qcloudimg.com/raw/e14e13b4f0d8a6d376e71036ed3888f9.png)
5. 在腾讯云创建 SAML 身份提供商及角色，详细操作请参考 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)、[创建角色](https://cloud.tencent.com/document/product/598/19381)-为身份提供商创建角色。

### 配置 Azure AD 的单一登录
>?您可以通过本步骤将 Azure AD 应用程序属性映射到腾讯云的属性，建立 Azure AD 应用程序和腾讯云的互信关系。
>
1. 在 “SAML 单一登录”概览界面，单击“基本 SAML 配置”右上角的<image style="margin:0;" src="https://main.qcloudimg.com/raw/836588594e0a214b5951ee5207fc2353.png">。如下图所示：
![](https://main.qcloudimg.com/raw/abeffc5c30a39561448523a5fc29b8ee.png)
2. 在“基本 SAML 配置”编辑页面填写以下信息，并单击【保存】。如下图所示：
![](https://main.qcloudimg.com/raw/a0161d7c8eeddcf00dab05d6a65dd2d7.png)
>?
> - 如果您的腾讯云账号所在站点为中国站，请按照如下信息进行配置：
标识符（实体 ID）：cloud.tencent.com
回复 URL（断言使用者服务 URL）：https://cloud.tencent.com/login/saml
> - 如果您的腾讯云账号所在站点为 International ，请按照如下信息进行配置：
标识符（实体 ID）：intl.cloud.tencent.com
回复 URL（断言使用者服务 URL）：https://intl.cloud.tencent.com/login/saml
>
3. 在 “SAML 单一登录”概览界面，单击“用户属性和声明”右上角的<image style="margin:0;" src="https://main.qcloudimg.com/raw/836588594e0a214b5951ee5207fc2353.png">，打开“用户属性声明”编辑页面。如下图所示：
![](https://main.qcloudimg.com/raw/012441d7e961f9f784e05cc347c66294.png)
4. 在“用户属性和声明”编辑页面，单击【添加新的声明】，进入“管理用户声明”页面。如下图所示：
![](https://main.qcloudimg.com/raw/4116fdd96ea5815f79db7c4aef508289.png)
5. 在“管理用户声明”页面，增加以下两条声明，并单击【保存】。如下图所示：
<table>
<thead>
<tr>
<th>名称</th>
<th>命名空间</th>
<th>源</th>
<th>源属性</th>
</tr>
</thead>
<tbody><tr>
<td>Role</td>
<td>https://cloud.tencent.com/SAML/Attributes</td>
<td>属性</td>
<td>qcs::cam::uin/{AccountID}:roleName/{RoleName},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName}</td>
</tr>
<tr>
<td>RoleSessionName</td>
<td>https://cloud.tencent.com/SAML/Attributes</td>
<td>属性</td>
<td>Azure</td>
</tr>
</tbody></table>

>?在 Role 源属性中 {AccountID}，{RoleName} ，{ProviderName} 分别替换内容下：
>- {AccountID} 替换为您的腾讯云帐户 ID，可前往 [账号信息 - 控制台](https://console.cloud.tencent.com/developer) 查看。
>- {RoleName} 替换您在腾讯云为身份提供商所创建的角色名称（单击查看如何在腾讯云  [为身份提供商创建的角色](https://cloud.tencent.com/document/product/598/19381#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.88.9B.E5.BB.BA)），角色名称可前往 [角色 - 控制台](https://console.cloud.tencent.com/cam/role) 查看，如需要添加更多可按照该格式添加：qcs::cam::uin/{AccountID}:roleName/{RoleName} ，以 ; 隔开。
>- {ProviderName} 替换您在腾讯云创建的 SAML 身份提供商名称，可前往  [身份提供商 - 控制台](https://console.cloud.tencent.com/cam/idp) 查看。
>
![](https://main.qcloudimg.com/raw/01b51dd563c366e82fc3f15ec31a5747.png)


### 配置 Azure AD 用户
>?您可以通过本步骤分配用户访问权限，向 Azure AD 用户分配腾讯云的 SSO 访问权限。
>
1.	单击左侧导航栏【Azure Active Directory】，单击【用户】，打开【所有用户】。如下图所示：
![](https://main.qcloudimg.com/raw/7ca36c24562a867451312e003c4afd25.png)
2. <span id="step2"></span>单击左上角【新建用户】，在“用户”页面填写【姓名】、【用户名】，勾选【显示密码】，信息无误后单击下方【创建】完成创建。如下图所示：
![](https://main.qcloudimg.com/raw/a67ec799cdcd060f34c86193f1e2ab7a.png)

>?用户名格式为：用户名@域名。您可以自定义用户名，域名可以单击左侧导航栏【Azure Active Directory】，打开概述页，查看您之前设置的【初始域名】。您可以复制保存用户名、密码留用。
>
3. 在左侧导航栏中，选择【Azure Active Directory】>【企业应用程序】> 您创建的应用程序，进入应用程序概览页面，并单击【用户和组】。如下图所示：
![](https://main.qcloudimg.com/raw/0fbc968bbdcdc1b1378e79a5e116d28a.png)
4. 单击【添加用户】，打开【用户和组】，选择 [步骤2](#step2) 您创建的用户，单击【选择】。如下图所示：
![](https://main.qcloudimg.com/raw/bd12f9c49ef1fd01bafc1d88566798e7.png)
5. 跳转到“添加分配”页面，确认后单击【分配】。如下图所示：
![](https://main.qcloudimg.com/raw/6e463c38b9bd16bb36b053f41550727d.png)
6. 在左侧导航栏中，选择【Azure Active Directory】>【企业应用程序】> 您创建的应用程序 ，进入应用程序概览页面。
7. 单击【单一登录】，打开 “SAML 单一登录”概览界面，单击【测试】。如下图所示：
![](https://main.qcloudimg.com/raw/18869ef276217645b1ac03ab92ed3ab7.png)
8. 在“测试单一登录”界面，选择【以其他用户的身份登录】。
9. 输入 [步骤2](#step2) 保存的用户名、密码，登录腾讯云控制台。
