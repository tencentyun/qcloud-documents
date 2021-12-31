## 操作场景
OneLogin 是一家云身份访问管理解决方案提供商，可以通过其身份认证系统一键登录企业内部所有需要的系统平台。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是 OneLogin 等许多身份验证提供商（Identity Provider，IdP）使用的一种开放标准。使用身份提供商可实现联合单点登录（Federated Single Sign-on，SSO），管理者可以授权通过联合身份验证的用户登录腾讯云管理控制台或调用腾讯云 API 操作，而不必为企业或组织中的每一个成员都创建一个 CAM 子用户。
本教程为 OneLogin 单点登录至腾讯云的配置指南。
## 操作步骤
### 创建 OneLogin 企业应用程序
>?
> - 您可以通过本步骤创建 OneLogin 企业应用程序。如您已经有正在使用的应用程序，请忽略本操作，进行 [配置 CAM](#cam)。
> - 本文中应用程序名称以 “test” 为示例。
> 
1. 登录并访问 [OneLogin 网站](https://app.onelogin.com/login)，单击【Applications】，进入应用管理页。<span id="app"></span>
2. 在应用管理页，单击右上角【ADD APP】。
3. 在搜索框中输入 “SAML”，按 “Enter”，并在结果列表中单击【 Pilot Catastrophe SAML( IdP )】。如下图所示：
![](https://main.qcloudimg.com/raw/2f80d98e0a6f05a589bd6a87323e56f7.png)
4. 在 “Display Name” 中输入应用名 ，并单击右上角【SAVE】，即可完成应用程序的创建。如下图所示：
![](https://main.qcloudimg.com/raw/a1bf87f51c2ff62838a1253e9e035bd1.png)

<span id="cam"></span>
### 配置 CAM
>? 
>- 您可以通过本步骤配置 OneLogin 和腾讯云之间的信任关系使之相互信任。
> - 本示例中 SAML 身份提供商以及角色名称均为 “test”。
> 
1. 在 [OneLogin 应用管理页](#app)，选择您已创建的应用【test】。
2. 单击右上角【MORE ACTION】，选择【SAML Matedata】，下载 IDP 云数据文档。如下图所示：
![](https://main.qcloudimg.com/raw/b109cd83a34d2f264a3697257d281715.png)
3. 创建腾讯云 CAM 身份提供商以及角色，详细操作请参考 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)、[创建角色](https://cloud.tencent.com/document/product/598/19381)-为身份提供商创建角色。

### 配置 OneLogin 单点登录
>?您可以通过本步骤将 OneLogin 应用程序属性映射到腾讯云的属性，建立OneLogin 应用程序和腾讯云的互信关系。
>
1. 在 [OneLogin 应用管理页](#app)，单击已创建的 “test” 应用，跳转至应用编辑页。
2. 选择【Configuration】页签，输入以下内容，单击【SAVE】。如下图所示：
![](https://main.qcloudimg.com/raw/2211da7f372415f536a81795d3a02207.png)

>?
> - 如果您的腾讯云账号所在站点为中国站，请按照如下信息进行配置：
SAML Consumer URL：https://cloud.tencent.com/login/saml
SAML Audience：https://cloud.tencent.com
SAML Recipient：https://cloud.tencent.com/login/saml
> - 如果您的腾讯云账号所在站点为 International ，请按照如下信息进行配置：
SAML Consumer URL：https://intl.cloud.tencent.com/login/saml
SAML Audience：https://intl.cloud.tencent.com
SAML Recipient：https://intl.cloud.tencent.com/login/saml
>
3. 单击【Parameters】，选择【Add parameter】，添加以下两条配置信息。
<table>
	<tr>
		<th>Field name</th>
		<th>Flags</th>
		<th>Value</th>
		<th>源属性</th>
	</tr>
	<tr>
		<td>https://cloud.tencent.com/SAML/Attributes/Role</td>
		<td>Include in SAML assertion</td>
		<td>Macro</td>	<td>qcs::cam::uin/{AccountID}:roleName/{RoleName1};qcs::cam::uin/{AccountID}:roleName/{RoleName2},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName}</td>
	</tr>
		<tr>
		<td>https://cloud.tencent.com/SAML/Attributes/RoleSessionName</td>
		<td>Include in SAML assertion</td>
		<td>Macro</td>
		<td>Test</td>
	</tr>
</table>

>?在 Role 源属性中 {AccountID}，{RoleName} ，{ProviderName} 分别替换内容下：
>- {AccountID} 替换为您的腾讯云帐户 ID，可前往 [账号信息 - 控制台](https://console.cloud.tencent.com/developer) 查看。
>- {RoleName} 替换您在腾讯云创建的角色名称，可前往 [角色 - 控制台](https://console.cloud.tencent.com/cam/role) 查看。
>- {ProviderName} 替换您在腾讯云创建的 SAML 身份提供商名称，可前往  [身份提供商 - 控制台](https://console.cloud.tencent.com/cam/idp) 查看。
>
4. 单击右上角【SAVE】保存配置。

### 配置 OneLogin 用户

1. 登录并访问 [OneLogin 网站](https://app.onelogin.com/login)，单击【Users】，进入用户管理页面。
2. 单击右上角【NEW USER】，跳转至新建用户页。
3. <span id="step3"></span>输入 “First Name” 、“Last Name”、“Email”、“Username”，单击【SAVE USER】保存。如下图所示：
![](https://main.qcloudimg.com/raw/847476e48740284fb0754cf3e5d4e616.png)

>?此帐户密码可查看 Email，或单击【MORE ACTIONS】选择【change password】修改密码。
>
4. 单击用户编辑页【 Applications 】，选择右侧的<image style="margin:0;" src="https://main.qcloudimg.com/raw/98a24d12696834b52f559d0abe490fd2.png">。如下图所示：
![](https://main.qcloudimg.com/raw/08ca65469c69a49b83c973ecfde2dc82.png)
5. 在弹出对话框选择您已创建的 SAML 应用 “test”，单击【CONITINUE】。如下图所示：
![](https://main.qcloudimg.com/raw/5f653c7aea898a1648702ca35562fc6e.png)
6. 在编辑页面，单击【 SAVE 】。如下图所示：
![](https://main.qcloudimg.com/raw/4e86052f6fc499ba368459bab532cc7a.png)
7. 使用 [步骤3](#step3) 创建的帐户登录 OneLogin ，访问上述创建的 SAML 应用 “test”。即可跳转至腾讯云控制台。
