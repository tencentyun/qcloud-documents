## 操作场景
Active Directory Federation Services（ADFS）是 Microsoft's 推出的 Windows Server 活动目录联合服务 (ADFS). ADFS是一种能够用于一次会话过程中多个 Web 应用用户认证的新技术。您可以使用用户 SSO 将 ADFS 与腾讯云进行集成，从而实现 ADFS 帐户管理腾讯云控制台管理腾讯云的资源。

## 前提条件

1. 拥有一台  Windows Server 服务器。如您需要购买服务器，请参见 [云服务器-购买指南](https://cloud.tencent.com/document/product/213/2179)。
2. 在服务器内进行以下搭建工作。
 - DNS 服务器：将身份认证请求解析到正确的 Federation Service 上。
 - Active Directory域服务（AD DS）：提供对域用户和域设备等对象的创建、查询和修改等功能。
 - Active Directory Federation Service（AD FS）：提供配置 SSO 信赖方的功能，并对配置好的信赖方提供 SSO 认证。



## 操作步骤
### 变更系统基础信息
在云服务器内，进入控制面板>系统和安全>系统，在计算机名、域和工作组设置项，单击**更改设置**，修改计算机名、计算机全名、计算机描述、域信息，本文示例中信息如下：`adserver、adserver.testdomain.com、adserver、testdomain.com`。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c41f7a934bcf4465a4ccaecc1efe8318.png" />


### 安装部署 Microsoft AD
1. 在云服务器内，进入 **Server Manager** > **Dashboard**，单击 **Add roles and features**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7282333d3f5dcb39ab54fbf574c26c16.png)
2. 一直单击 **Next** 直到单击 **Install** 完成安装，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ae0a94b9c597c91a3dcd8c7043de0f68.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e1ccd1b440e38a71992e880e67d2cf0f.png)
![](https://qcloudimg.tencent-cloud.cn/raw/7a6b39a2eeb2524ecf67a2771879312a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ad7a3b63617e198cc516b93eac7b9f16.png)
![](https://qcloudimg.tencent-cloud.cn/raw/48b762e0a998df71e8491b30b6a54645.png)
3. 安装完成后单击 **Promote this server to a domain controller**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f4890c5542e5857fbb156ad7cf40fc40.png)
4. 在 Deployment Configuration 页面选择 **Add a new forest** 补充 Root domain name 信息为 testdomain.com，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f794b35d93cfb4f63bdef21cc00b2d2f.png)
5. 在 Domain Controller Options 中补充 Password 信息，如下图所示，完成后一直单击**Next**，单击 **Install** 完成安装
![](https://qcloudimg.tencent-cloud.cn/raw/a7f1048c48ed1b960fd5adf09944c0db.png)
6. 安装完成后，服务器将重启，重启完成后，进入 **Start Menu** > **Active Directory Users and Computers**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/be4bbd5369280d1e1ff09ff33c174faa.png)
7. 在 Active Directory Users and Computers 页面，新建 Org 及 Users 信息，其中 **Users 名称需与后续腾讯云创建的子用户保持一致**如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fbc448ea146fa90b420bc27ced0ea758.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f4d5dff6e43175cd1d39747ea053b397.png)
![](https://qcloudimg.tencent-cloud.cn/raw/7aed7ed564c0f391d3580514c0c259d9.png)

### 安装 CA
1.在云服务器内，进入 **Server Manager** > **Dashboard**，单击 **Add roles and features**，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/6e62daaad1474f3c251869f4b0f749a2.png" />
2. 一直单击 **Next** 直到 Server Roles 页面，Roles 选择 Active Directory Certificate Services，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f3ea0086af560b353f6922f6b869958a.png)
3. 一直单击 **Next** 直到 AD CS-Server Roles 页面，Server Roles 选择 Certification Authority、Certification Authority Web Enrollment，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/83b7ae2d0628e3efb742f00f938bfc33.png)
4. 一直单击 **Next** 直到 Results 页面，单击下图信息配置 AD CS Configuration，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/eca91d47edbacb80103559342e64a8e6.png)
![](https://qcloudimg.tencent-cloud.cn/raw/fd151accd04a688cd4934c4884af88bb.png)
5. 单击 **Next** 在 Server Roles，勾选下图信息，单击 **Next**，
![](https://qcloudimg.tencent-cloud.cn/raw/0af21d35a7fdc50d501fc7e6a94e3105.png)
6. 在 Setup Type 页面，选择 Enterprise CA，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7127bb86027acb91b69d35aef98cde0d.png)
7. 在 CA Type 页面，选择 Root CA，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/68c8da2d506bf7f42f3597de0a32e1e4.png)
8. 在 Private Key 页面，选择 Create a new private key，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9e6fe449caf50343a0a0ff1909f40db5.png)
![](https://qcloudimg.tencent-cloud.cn/raw/117ff97b6629d01560aa5f97a49066f8.png)
![](https://qcloudimg.tencent-cloud.cn/raw/aeb9d6d7e6a482cad0814737c20d9354.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ca35bb8a5c357ea45f9a63eca0c9dee7.png)
9. 在 Certificate Database 页面，补充信息，单击**下一步**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b99c953c26ee7e543f9882be4e60b5fb.png)
![](https://qcloudimg.tencent-cloud.cn/raw/607d5fd44544c8c9cd30dfbe47c22a8b.png)
10. 访问  `http://localhost/certsrv ` 确保 CA 安装成功，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f6325f01c184edcf715a69f0e22fde15.png)

### 安装 ADFS 服务
在配置前您需要给计算机或者指定的用户或者计算机授权证书颁发。安装 ADFS 前，需要创建和配置证书，本文中通过 IIS 进行证书申请。
1. 在云服务器内，单击<img style="width:30px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/25ae05d89cef53ae9435f530939f75ec.png" />，在弹出的窗口单击**工具**，选择 “IIS 管理器” 。
![](https://qcloudimg.tencent-cloud.cn/raw/44199407b6c4393cd152f16800999f68.png)
2. 在 IIS 管理器中，单击**服务器证书**，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/0b49f4664cd74f8a8a1b1bc270748c31.png" />
3. 进入服务器证书页面，单击 **创建证书申请**，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/a59d8264e9d2edb1e990379d1a22b6b2.png" />

 ![](https://qcloudimg.tencent-cloud.cn/raw/d14676f50d1dedf2455e39f2a3a2824f.png)
 ![](https://qcloudimg.tencent-cloud.cn/raw/e070da5b0a06b6f77dab3e91122702a7.png)
 ![](https://qcloudimg.tencent-cloud.cn/raw/a5b997c70e6a0fb86c5eed5cd3e47f14.png)
4. 访问  `http://localhost/certsrv`，单击**申请证书 > 高级证书申请 > 使用 base64 编码**，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c9cad1c83817099ca2a385a7a220d444.png" />
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/37ab1c3364acddef651b339d5233f7ff.png" />
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c5a8ec1e1b22e15b406bfbd5bd52fa7c.png" />
5. 在弹出的提交证书申请页面，将申请证书保存的证书文件内容复制之后补充至以下输入框，证书模板选择 Web 服务器，单击**提交**。如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/15080a1c59c6390f17ca2247edebb5f5.png" />
6. 提交之后，单击 **下载证书**，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/a3301bacb18d0c646932a89c65f7fea0.png" />
7. 在服务器证书页面，单击 **完成证书申请**，在弹出的页面选择步骤 5 下载的证书，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/e31ca79c7ff60614837b049071e5cfa3.png" />

 ![](https://qcloudimg.tencent-cloud.cn/raw/2b044468721d83d7a1fbb123c0f2e847.png)
8. 在网站 > Default Web Site 主页，右键单击 **编辑绑定**，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/1a8ab8e9b388d9ad0567fb1e843eb858.png" />
9. 在弹出的网站绑定页面，单击 **添加**，选择类型为 https，IP 地址为全部未分配，端口为 80，SSL 证书为 test.cert，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/00dff679c9a49898799cd4c138c8b3a2.png" />
10. 在管理工具页面，单击 **证书颁发机构**，如下图所示：
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/2ba5c07e2fceaf021938e746478f3927.png" />
11. 在证书颁发机构页面，选择证件模板，右键单击**管理**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/eece2b526f8afc306ace6c8c1531e7c0.png)
12. 参考下图进项配置：
![](https://qcloudimg.tencent-cloud.cn/raw/e32f38f87bd880f9c5c2e72e0edcdbcb.png)
![](https://qcloudimg.tencent-cloud.cn/raw/a03cf0fd0c7d21418302f4efea26a55c.png)
![](https://qcloudimg.tencent-cloud.cn/raw/07c86f1a9a9a96a9bc7017ec60183b7f.png)
![](https://qcloudimg.tencent-cloud.cn/raw/6408b6679e3f5f346522617177796289.png)
![](https://qcloudimg.tencent-cloud.cn/raw/9de59ddf2e267f3dbbc2978477156e41.png)
13. 进入服务器管理器 > 仪表板页面，单击 **添加角色和功能**，按照默认选择一直单击 **下一步** 直到服务器角色选择页面，勾选 Active Directory Federation Services，一直单击 **下一步**，直至安装完成。
14. 在安装完成页面，单击 **在此服务器上配置联合身份验证服务**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4768be5b92a649761e23dd4111998fd4.png)
15. 在弹出的向导页面，单击 **下一步**，
![](https://qcloudimg.tencent-cloud.cn/raw/28a6be78ac00cb795387a126425298ef.png)
设置指定服务属性，选择并填写好所需数据，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/2f217dc6e860eba5816a13e4b378b857.png)
设置指定服务账户，选择使用现有的域用户账户或组托管服务账户，单击**选择**。
![](https://qcloudimg.tencent-cloud.cn/raw/72fc15b1b9b0a26e60d8971f8afda629.png)
选择指定账户后，单击**确认**，确认后直至安装完成。
![](https://qcloudimg.tencent-cloud.cn/raw/a6e1fbb6810ef5f078107d0530568e80.png)

### 用户SSO配置
1. 在服务器内浏览器访问 `https://adserver.testdomain.com/FederationMetadata/2007-06/FederationMetadata.xml`，将源数据 XML 下载至本地。
2. 进入 [访问管理-用户 SSO 控制台](https://console.cloud.tencent.com/cam/idp/usersso)，单击右侧 **编辑**，设置 SSO 协议为 SAML，上传第 1 步保存的 XML 文件。
3. 在服务器内进入 ADFS 管理页面，选择**信任关系** > **信赖方信任**，右键选择添加信赖方信任，单击 **启动**，补充联合元数据地址，元数据地址从第 2 步中获取，一直单击 **下一步**，如下图所示：
<img style="width:950px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/dafbb1d955917735ed1cb0174c56aa34.png" />
<img style="width:950px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/69349b04b2398a9c886eb6ecafe53b71.png" />
<img style="width:950px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/31b0bf40310bd5f54a38ac9036aafdcb.png" />

4. 配置完后，效果如下图所示：
 <img style="width:950px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/de077296157333014f2c73b2ada876ad.png" />

### 为腾讯云 SP 配置 SAML 断言属性
为保证腾讯云 SAML 响应定位到正确的子用户，SAML 断言中的 NameID 字段需要是腾讯云子用户名。SAML 断言中的 NameID 默认传入为（TESTDOMAIN\子用户名）格式，需正则表达式去除原有配置 TESTDOMAIN，仅保留子用户名（TESTDOMAIN 是前面的默认 NETBIOS 名）。
自定义规则为：**安装 ADFS 服务**中步骤3 申请证书所在文件内的txt内容。
![](https://qcloudimg.tencent-cloud.cn/raw/1f3b77256d1baefd8e27e7c50145ed25.png)
 <img style="width:950px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/8521e2aef41f0dea752886f179e05b36.png" />
 <img style="width:950px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/78b3222e20690715071a77040ac8722f.png" />
>?若出现请求终止，无法创建 SSL/TLS 安全通道时，可通过 powershell 执行方式后重启服务器解决。
32位机器：
Set-ItemProperty -Path 'HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NetFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value '1' -Type DWord
64位机器：
Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\.NetFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value '1' -Type DWord

### 用户 SSO 登录
1. 浏览器输入 `https://adserver.testdomain.com/adfs/ls/idpinitiatedsignon`。
2. 输入用户名、密码信息，即可完成登录，如下图所示：
 <img style="width:950px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/5d430cb8e87af118bc839322401dac44.png" />


