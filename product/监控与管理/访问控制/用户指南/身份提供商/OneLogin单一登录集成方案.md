## 操作前景
OneLogin 是一家云身份访问管理解决方案提供商，可以通过其身份认证系统一键登录企业内部所有需要的系统平台。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是 OneLogin 等许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。使用身份提供商可实现联合单点登录（Federated Single Sign-on，SSO），管理者可以授权通过联合身份验证的用户登录腾讯云管理控制台或调用腾讯云 API 操作，而不必为企业或组织中的每一个成员都创建一个 CAM 子用户。本教程为 OneLogin 单点登录至腾讯云的配置指南。

## 操作步骤
### 创建 OneLogin 企业应用程序
>?您可以通过本步骤创建 OneLogin 企业应用程序。如您已经有正在使用的应用程序，请忽略本操作，进行[配置 CAM](#cam)。

1. 登录并访问 [OneLogin 应用管理页](https://xiaoyu.onelogin.com/apps)，单击右上角【ADD APP】。
2. 在搜索框中输入 “SAML”，按“Enter”。在结果列表中单击【 Pilot Catastrophe SAML( IdP )】。如下图所示：
![](https://main.qcloudimg.com/raw/2f80d98e0a6f05a589bd6a87323e56f7.png)
3. 输入 “ Display Name ” ，并单击右上角【SAVE】，即可完成应用程序的创建，（本文以 “test” 为示例）。如下图所示：
![](https://main.qcloudimg.com/raw/d600fb5d578a92f9a2bf5cba1605af46.png)


<span id="cam"></span>
### 配置 CAM
>? 
>- 您可以通过本步骤配置 OneLogin 和腾讯云之间的信任关系使之相互信任。
> - 本示例中 SAML 身份提供商以及角色名称均为 “test”。

1. 登录并访问 [OneLogin 应用管理页](https://xiaoyu.onelogin.com/apps)，选择您已创建的应用【test】。
2. 单击右上角【MORE ACTION】，选择【SAML Matedata】，下载 IDP 云数据文档，如下图所示：
![](https://main.qcloudimg.com/raw/a1c304fad4d9b7a898beceae9bf977f6.png)
3. 创建腾讯云 CAM 身份提供商以及角色，详细操作请参考 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)。

### 配置 OneLogin 单点登录
>?您可以通过本步骤将 OneLogin 应用程序属性映射到腾讯云的属性，建立 Azure AD 应用程序和腾讯云的互信关系。

1. 登录并访访问 [OneLogin 应用管理页](https://xiaoyu.onelogin.com/apps)，点击上述创建的 “test” 应用，跳转到应用编辑页。
2. 单击【 Configuration 】，输入以下内容，并单击【SAVE】。如下图所示：
 - SAML Consumer URL：https://cloud.tencent.com/login/saml
 - SAML Audience：https://cloud.tencent.com
 - SAML Recipient：https://cloud.tencent.com/login/saml
 ![](https://main.qcloudimg.com/raw/48dc612ebbd1a8572c3bf208c4411f51.png)
3. 单击【 Parameters 】，选择【 Add parameter 】，添加以下两条配置信息。如下图所示：

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
		<td>Macro</td>
	<td>qcs::cam::uin/{AccountID}:roleName/{RoleName},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName}</td>
	</tr>
		<tr>
		<td>https://cloud.tencent.com/SAML/Attributes/RoleSessionName</td>
		<td>Include in SAML assertion</td>
		<td>Macro</td>
		<td>Test</td>
	</tr>
</table>

>?在 Role 源属性中 {AccountID}，{RoleName} ，{ProviderName} 分别替换内容下：
> - {AccountID}：替换为您的腾讯云帐户 ID，可前往腾讯云账号中心 - [账号信息](https://console.cloud.tencent.com/developer)查看。
> - {RoleName}：替换您在腾讯云创建的角色名称，可前往腾讯云 CAM 控制台 - [角色管理](https://console.cloud.tencent.com/cam/role)查看。
> - {ProviderName}：替换您在腾讯云创建的 SAML 身份提供商名称，可前往腾讯云 CAM 控制台 - [身份提供商](https://console.cloud.tencent.com/cam/idp)查看。

![](https://main.qcloudimg.com/raw/bba88124da201efef6d27f8e18a9e442.png)
4. 单击右上角【SAVE】保存配置。

### 配置 OneLogin 用户
1. 登录并访问 [OneLogin 用户管理控制台](https://xiaoyu.onelogin.com/users)。
2. 单击右上角【NEW USER】，跳转至新建用户页。
3. <span id="step3"></span>输入 “First Name” 、“Last Name”、“Email”、“Username”，单击右上角【SAVE USER】保存。如下如所示：
>?此帐户密码可查看 Email，或单击右上角【MORE ACTIONS】选择【change password】修改密码。

![](https://main.qcloudimg.com/raw/ef4f738c88f3c97fe5980286ad383ffa.png)
4. 单击用户编辑页的【 Applications 】选择右侧的“+”图标。如下图所示：
![](https://main.qcloudimg.com/raw/d8e9053d445b3af6d9aaecd74a0952b7.png)
5. 在弹出对话框选择您已创建的 SAML 应用 “test”，单击【CONITINUE】按钮。如下图所示：
![](https://main.qcloudimg.com/raw/f7d3ecad4803cff72c62d665d4a2ec96.png)
6. 跳转至编辑页面，单击【 SAVE 】。如下图所示：
![](https://main.qcloudimg.com/raw/9d9389fbe5b821f23519524b30827c23.png)
7. 使用 [步骤3](#step3)创建的帐户登录 OneLogin ，访问上述创建的SAML应用 "test"。如下图所示：
![](https://main.qcloudimg.com/raw/3a45e770e6bcaa01fb9bc9ba22f25200.png)
9. 登录之后跳转至腾讯云控制台。如下图所示：
![](https://main.qcloudimg.com/raw/0245bd15e08651b6d7e641ed8e843aad.png)
