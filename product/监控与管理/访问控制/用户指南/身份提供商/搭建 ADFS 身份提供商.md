## 操作场景
Active Directory Federation Services（ADFS）是 Microsoft's 推出的 Windows Server 活动目录联合服务 (ADFS). ADFS是一种能够用于一次会话过程中多个Web应用用户认证的新技术。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。您可以通过基于 SAML 2.0 联合身份验证将 ADFS 与腾讯云进行集成，从而实现 ADFS 帐户自动登录（单一登录）腾讯云控制台管理腾讯云的资源，不必为企业或组织中的每一个成员都创建一个 CAM 子用户。
## 前提条件
> - 拥有一台 Windows Server 云服务器。如您需要购买服务器，请参阅 [云服务器-购买指南](https://cloud.tencent.com/document/product/213/2179)。
- 已进入服务器管理-仪表板页面。
- 拥有一个已完成实名认证的域名。如您需要购买域名，请参阅 [域名-购买指南](https://cloud.tencent.com/document/product/242/18873)。

## 操作步骤
### 安装 AD 域服务和 DNS 服务
1. 在仪表板管理页面，单击【添加角色和功能】，保持页面默认信息，一直单击【下一步】，进入添加角色和功能向导页面。
![](https://main.qcloudimg.com/raw/eff8daac45ecbf517218b05dbbaa5b26.png)
2. 在添加角色和功能向导页面， 保持页面默认信息，一直单击【下一步】，<span id="step1">在服务器角色信息栏勾选 Active Directory 域服务、DNS 服务器。如下图所示：
![](https://main.qcloudimg.com/raw/2321b831c4f25b4b19814f0f376a29d1.png)
3. 保持页面默认信息，一直单击【下一步】，单击【安装】。在完成安装成功界面，单击右上角![](https://main.qcloudimg.com/raw/32f3dcf3b4c58c0acb3485f2dab0f9a7.png)或在安装完成界面。如下图所示：
![](https://main.qcloudimg.com/raw/9a42db98e9175262e89b6557e302dc0e.png)
4. 单击【提升为域控制器】，进入部署配置页面，填写域名，本文中示例为：example.com。如下图所示：
![](https://main.qcloudimg.com/raw/87e596a7352c2b785ffea6996ed02196.png)
5. 单击【下一步】，完成安装后，输入密码。保持页面默认信息，一直单击【下一步】。如下图所示：
 ![](https://main.qcloudimg.com/raw/dd0bdc5a15909f22a0ce1a04c67e679a.png)
6. 单击【安装】，安装完成后重启服务器。如下图所示：
![](https://main.qcloudimg.com/raw/ad13922f6efa740ccb21998a46a4696f.png)
7. 完成 AD 域服务、DNS 服务安装，并将服务器提升为域控制器完毕。

### 安装 Web 服务器
1.参考安装 AD 域服务和 DNS 服务中 [步骤2](#step1)，进入服务器角色页面，在服务器角色信息栏勾选 Web 服务器。如下图所示：
![](https://main.qcloudimg.com/raw/ef45cf538ef55d86e98cbf8972379f0c.png)
2. 保持页面默认信息，一直单击【下一步】>【安装】，完成 Web 服务器安装。

### 申请证书
如您已拥有 SSL 证书，可直接进行 [安装 ADFS](#step0) 操作。

1. 单击左下角【Windows图标】，在搜索框输入“mmc”命令，回车执行，进入控制台1-[控制台根节点]页面。如下图所示：
![](https://main.qcloudimg.com/raw/613a00c1057b12ac0e5535e9dc40a292.png)
 
2. 在控制台1-[控制台根节点]页面，单击【文件】>【添加/删除管理单元】，在弹出的窗口中选择证书，单击【添加】>【完成】。如下图所示：
![](https://main.qcloudimg.com/raw/18ff77b7fa95202761a4a0aa5cae1ac8.png)

3. 单击【证书】，<span id="step3">在展开的目录中，右键单击【个人】，单击【所有任务】>【高级操作】>【创建自定义请求】。如下图所示：
![](https://main.qcloudimg.com/raw/313fe9dad2800ad49175a5079cd31655.png)

4. 保持页面默认信息，一直单击【下一步】，进入证书注册页面，单击【不使用注册策略继续】，如下图所示：
![](https://main.qcloudimg.com/raw/ab888353e868ee66f7a3918c9adbfa09.png)

5. 在自定义请求页面，选择以下信息，如下图所示：
> - 模板：（无模板）就密钥
> - 请求格式：PKCS#10
> 
![](https://main.qcloudimg.com/raw/df77e6971de87168df55694ab293807d.png)
6. 单击【详细信息】>【证书属性】，在常规栏补充友好名称、描述信息。如下图所示：
![](https://main.qcloudimg.com/raw/60e8c408a9797aa0e270d185e7037b33.png)
7. 在使用者栏，填写值信息，本次示例为（*.example.com），单击【添加】，如下图所示：
![](https://main.qcloudimg.com/raw/e98ab7fe0f4844cd03f4c1d09f47bfa9.png)

8. 在私钥栏下勾选 Microsoft RSA SChanel Cyptograhic Provider（加密）、使私钥可以导出。如下图所示：
![](https://main.qcloudimg.com/raw/4ab6622ae4a1806201d2806705bf3740.png)

9. 单击【确认】>【下一步】，选择需要保存的目录，保存证书，单击完成。如下图所示：
![](https://main.qcloudimg.com/raw/60210ccff431bdf90d5643a4cb6f0ca5.png)

### 安装 ADC(AD证书服务器)
1. 参考安装 AD 域服务和 DNS 服务中 [步骤2](#step1)，在服务器角色信息栏勾选 Active Directory 证书服务器。如下图所示：
![](https://main.qcloudimg.com/raw/47a75d3a22ba0f8ed2206d6a8bbc71cc.png)
2. 保持默认信息，一直单击【下一步】，在角色服务栏勾选证书颁发机构、证书颁发机构 Web 注册。如下图所示：
![](https://main.qcloudimg.com/raw/2280ea2d3ffbd00c9ea40baab3b53beb.png)
3. 单击【安装】，在完成安装成功界面，单击右上角![](https://main.qcloudimg.com/raw/32f3dcf3b4c58c0acb3485f2dab0f9a7.png)，单击【配置目标服务器的 Active Directory 证书服务】。如下图所示：
![](https://main.qcloudimg.com/raw/f2fef65b3e14eba197d47bdc6e44dc6a.png)
4. 保持页面默认信息，一直单击【下一步】，在角色服务栏勾选证书颁发机构、证书颁发机构 Web 注册。如下图所示：
![](https://main.qcloudimg.com/raw/3cb95189345827ea9da7a653bf83a243.png)
5. 保持页面默认信息，一直单击【下一步】，单击【配置】，完成安装 ADC。如下图所示：
![](https://main.qcloudimg.com/raw/cbf71552decaf46bf46d2768153eae17.png)

### 生成 SSL 证书
1. 访问 http://localhost/certsrv， 单击【申请证书】。如下图所示：
![](https://main.qcloudimg.com/raw/933bedf77c6968d5bf3e7edc6e61fb96.png)
2. 在申请一个证书页面，单击【高级证书申请】。如下图所示：
 ![](https://main.qcloudimg.com/raw/86c35da5ece4d53580d088ff4d3808c5.png)
 
3. 在高级证书申请页面，单击【使用 base64 编码的 CMC 或 PKCS#10 文件提交一个证书申请，或使用 base64 编码的 KCS#7 文件 续订证书申请】。如下图所示：
![](https://main.qcloudimg.com/raw/e7df649fe3184e9e9a046f19fafe29d4.png)
4. 将申请证书保存的证书文件内容复制之后补充至以下输入框，证书模板选择 Web 服务器，单击【提交】。如下图所示：
![](https://main.qcloudimg.com/raw/14c4b4690d0b760a3ebae699533851c7.png)
5. 申请成功，单击【下载】（两种格式均需下载）<span id="step5">。如下图所示：
![](https://main.qcloudimg.com/raw/b3579f3cdfd49db5ead182a6c27e44f6.png)
 
6. 参考申请证书的 [步骤 3](#step3)，右键单击【个人】，单击【所有任务】>【导入】。如下图所示：
![](https://main.qcloudimg.com/raw/72ca12debb15a4122d5f7ba72bcc2a7e.png)
7. 选择 [步骤 5](#step5) 保存的证书文件，保持页面默认信息，一直单击【下一步】>【完成】。
8. 参考申请证书的 [步骤 3](#step3)，右键单击【个人】，单击【所有任务】>【导出】。如下图所示：
![](https://main.qcloudimg.com/raw/460d0c31c83acc14e4b80a708bf994e4.png)
9.在证书导出向导页面，选择“是，导出私钥”，勾选“组或用户名（建议）”，单击下一步，完成导出保存文件。<span id="step9">如下图所示：
![](https://main.qcloudimg.com/raw/c35cd7d547864b496ba063ff4c332666.png)
![](https://main.qcloudimg.com/raw/febcb2723b415cab110bac765ecde927.png)

### 安装 ADFS
1. <span id="step0"> 参考安装 AD 域服务和 DNS 服务中 [步骤2](#step1)，进入服务器角色页面，勾选 Active Directory 联合身份验证服务。如下图所示：
![](https://main.qcloudimg.com/raw/24e6a6f7440644fa21425652eb393c0f.png)
2. 保持页面默认信息，一直单击【下一步】>【完成】，在结果页面，单击【在此服务器上配置联合身份验证服务】。如下图所示：
![](https://main.qcloudimg.com/raw/a68753820c34fef24ab06c1ced2ac729.png)
3. 保持页面默认信息，一直单击【下一步】，进入指定服务属性页面，填写导入以下信息
SSL 证书：导入在生成 SSL 证书中 [步骤 9](#step9) 保存的证书文件。
联合身份服务名称：目标服务器名称（与右上角信息保持一致）或 sts.域名或 adfs.域名。
联合身份验证服务显示名称：用户在登录时看到显示名称。
如下图所示：
![](https://main.qcloudimg.com/raw/cf2baeee1e1b4f32f706092f3a244788.png)
4. 在指定服务账户页面，输入账户名称、密码，<span id="step4">保持页面默认信息，一直单击【下一步】直到安装 ADFS 完成。如下图所示：
![](https://main.qcloudimg.com/raw/7a939e5705f4f1f3c23be50f11647665.png)

5. 访问以下链接下载 XML文件。
```
https://联合身份验证服务器名称/federationmetadata/2007-06/federationmetadata.xml
```

6. 在 powerShell 中执行 Set-AdfsProperties –EnableIdpInitiatedSignonPage $True，
访问以下入口进行登录。

```
https://联合身份验证服务器名称/adfs/ls/idpinitiatedSignOn.htm
```
7. 输入 [步骤4](#step4) 中的账号名称、密码登录。登录成功如下图所示：
![](https://main.qcloudimg.com/raw/a032933d0f3bedbfe31d1cea75459d5c.png)
>?如浏览器登录提示出现400 Bad Request，在 powerShell 中进行以下操作
首先获取启动 ADFS 服务的用户。然后打开 PowerShell，执行脚本 setspn -s http/ADFS 所在服务器的访问地址 域控\用户。例如，ADFS 所在服务器的全称为 172_21_0_13.weezer.club ，域控机器为WEEZER，用户为 Administrator，那么所执行的脚本就是 setspn -s http/172_21_0_13.weezer.club WEEZER\Administrator。

### 在腾讯云创建身份提供商
>?您可以通过本步骤配置 ADFS 和腾讯云之间的信任关系使之相互信任。

在腾讯云创建 SAML 身份提供商，命名格式为纯英文，保存您的身份提供商名称。<span id="step6"></span>详细操作请参阅 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)。
其中元数据文档您可以访问以下链接下载提供商的xml文件。

```
https://联合身份验证服务器名称/federationmetadata/2007-06/federationmetadata.xml
```

### 为身份提供商创建角色
>?您可以通过本步骤分配用户访问权限，向 ADFS 用户分配腾讯云的 SSO 访问权限。
>
为您的身份提供商创建角色，命名格式为纯英文，保存您的角色名称<span id="step7"></span>。详细操作请参阅 [为身份提供商创建角色](https://cloud.tencent.com/document/product/598/19381) 。
其中身份提供商选择在 [腾讯云创建身份提供商](#step6) 步骤中创建的身份提供商。

### 配置用户和用户组
1. 在服务器管理器仪表板页面，单击右上角工具，选择 Active Directory 用户和计算机。如下图所示：
![](https://main.qcloudimg.com/raw/b064eec1982149a015d8df9a569fbf91.png)
2. 在 Active Directory 用户和计算机页面，单击【操作】>【新建】>【组】。如下图所示：
![](https://main.qcloudimg.com/raw/a07fe66f3ed109266ac98162663029a7.png)
3. 在新建对象-组页面， 填写组名信息。如下图所示：
![](https://main.qcloudimg.com/raw/aa30bdf9deaec08ddceadcff44199a45.png)
>?
>-  <您的主账号 ID>替换为您的腾讯云帐户 ID，可前往 [账号信息 - 控制台](https://console.cloud.tencent.com/developer) 查看。
> - <腾讯云角色名>替换为您在腾讯云为身份提供商所创建的 [角色名称](#step7)。
4. 在 Active Directory 用户和计算机页面，单击【操作】>【新建】>【用户】。如下图所示：
![](https://main.qcloudimg.com/raw/8d1b51da00f307b4d2583ff3fe924186.png)
5.  新建员工，填写员工基本信息，以英文命名用户名称，保存用户名称。
6.  在 Active Directory 用户和计算机页面，在 Users 文件夹中找到新添加的用户，将用户添加至用户组。如下图所示：
![](https://main.qcloudimg.com/raw/a8219770c16113827ffa79b2d36c8146.png)
![](https://main.qcloudimg.com/raw/646f6de3266481463ac7b73099304982.png)

### 配置映射规则
1. 单击服务器管理器-ADFS 页面右上角【工具】。如下图所示：
![](https://main.qcloudimg.com/raw/0a1b8c8556dcf41f02e48c530326df82.png)
2. 选择 ADFS 管理，单击【添加信赖方】，如下图所示：
![](https://main.qcloudimg.com/raw/f4f59f90d2b90974428faa31cb4c6df6.png)
3. 在添加信赖方信任向导页面，选择“声明感知”，单击【启动】。如下图所示：
![](https://main.qcloudimg.com/raw/a90385d09c006b220c22d0fa342bca1b.png)

4. 访问以下链接下载腾讯云身份提供商的 XML 文件。

```
https://cloud.tencent.com/saml.xml
```
5. 导入腾讯云身份提供商的文件。如下图所示：
![](https://main.qcloudimg.com/raw/acecf94a4147dc77c7ade97bd2c98f12.png)
6. 保持页面默认信息，一直单击【下一步】>【完成】。
7. 单击【信赖方信任】>【添加规则】>【编辑声明颁发策略】。如下图所示：
![](https://main.qcloudimg.com/raw/1c34a7e2622257c74c7b6826e0c69d25.png)
8. 在添加转换声明规则向导页面，单击【选择规则类型】>【转换传入声明】>【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/cc5c6d362bbc8efe10dd63e90948ef3b.png)
9. 在编辑规则页面，补充规则信息，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/2f273e4888f5b22a898be0f8e38e819d.png)
>? 
> - 声明规则名称：补充为 NameID。
> - 传入声明类型： 选择 Windows 账户名。
> - 传出声明类型：选择名称 ID。
> - 传出名称 ID 格式：选择永久标识符。
> - 勾选传递所有声明值。
10. 在添加转换声明规则向导页面，单击【选择规则类型】>【使用自定义规则发送声明】>【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/3a0c83b3c1ea6cb8aed612e9998f95f1.png)

11.在编辑规则页面，补充规则信息，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/e7a380f00d3d26f89609fc84c510a625.png)
>? 
> - 声明规则名称：补充为 Get AD Groups。
> - 自定义规则： 补充以下信息
>```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => add(store = "Active Directory", types = ("http://temp/variable"), query = ";tokenGroups;{0}", param = c.Value);
```

12. 在添加转换声明规则向导页面，单击【选择规则类型】>【使用自定义规则发送声明】>【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/3a0c83b3c1ea6cb8aed612e9998f95f1.png)

13. 在编辑规则页面，补充规则信息，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/8bc620166e88e68f4963622a85ed398b.png)
>? 
> - 声明规则名称：补充为 Role。
> - 自定义规则： 补充以下信息
>```
c:[Type == "http://temp/variable", Value =~ "(?i)^Tencent-([\d]+)"]
 => issue(Type = "https://cloud.tencent.com/SAML/Attributes/Role", Value = RegExReplace(c.Value, "Tencent-([\d]+)-(.+)", "qcs::cam::uin/$1:roleName/$2,qcs::cam::uin/$1:saml-provider/身份提供商名称")); 
```
其中“身份提供商名称”替换为您在 [腾讯云创建身份提供商](#step6) 步骤创建的身份提供商名称。
14. 在添加转换声明规则向导页面，单击【选择规则类型】>【使用自定义规则发送声明】>【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/3a0c83b3c1ea6cb8aed612e9998f95f1.png)
15. 在编辑规则页面，补充规则信息，单击【确定】。如下图所示：
> - 声明规则名称：RoleSessionName。
> - 自定义规则： 补充以下信息
>```
c:[Type == "http://temp/variable", Value =~ "(?i)^Tencent-([\d]+)"]
 => issue(Type = "https://cloud.tencent.com/SAML/Attributes/RoleSessionName", Value = RegExReplace(c.Value, "Tencent-([\d]+)-(.+)", "test"));
 ```

### 账号登录
在您的服务器浏览器中输入以下网址，访问登录腾讯云。
```
https://联合身份验证服务器名称/adfs/ls/idpinitiatedSignOn.htm
```
>? 
> - 如您需要在ADFS服务器之外的浏览器单点登录腾讯云，可以在域名服务商配置子域名（您的联合身份验证服务器名称），然后在进行访问登录。
