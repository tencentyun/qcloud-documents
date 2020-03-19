## 操作场景
Active Directory Federation Services（ADFS）是 Microsoft's 推出的 Windows Server 2003 R2 活动目录联合服务 (ADFS). ADFS是一种能够用于一次会话过程中多个Web应用用户认证的新技术。腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。您可以通过基于 SAML 2.0 联合身份验证将 Azure Active Directory 与腾讯云进行集成，从而实现 ADFS 帐户自动登录（单一登录）腾讯云控制台管理腾讯云的资源，不必为企业或组织中的每一个成员都创建一个 CAM 子用户。
本教程为 ADFS 单点登录至腾讯云的配置指南。

## 前提条件
> - 拥有一台 Windows Server 2003 R2 云服务器。如您需要购买服务器，清参阅 [云服务器-购买指南](https://cloud.tencent.com/document/product/213/2179)。
- 已进入服务器管理-仪表板页面。
- 拥有一个已完成实名认证的域名。如您需要购买域名，请参阅 [域名-购买指南](https://cloud.tencent.com/document/product/242/18873)。

## 操作步骤
### 安装 AD 域服务和 DNS 服务
1. 在仪表板管理页面，单击【添加角色和功能】，保持页面默认信息，一直单击【下一步】，进入添加角色和功能向导页面。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318184337488.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
2. 在添加角色和功能向导页面， 保持页面默认信息，一直单击【下一步】，<span id="step1">在服务器角色信息栏勾选 Active Directory 域服务、DNS 服务器。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318184422382.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
3. 保持页面默认信息，一直单击【下一步】，单击【安装】。在完成安装成功界面，单击右上角![](https://main.qcloudimg.com/raw/32f3dcf3b4c58c0acb3485f2dab0f9a7.png)或在安装完成界面。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318184852544.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
4. 单击【提升为域控制器】，进入部署配置页面，填写域名，本文中示例为：example.com。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318184927548.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
5. 单击【下一步】，完成安装后，输入密码。保持页面默认信息不变，一直单击【下一步】。如下图所示：
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318185247466.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70) 
6. 单击【安装】，安装完成后重启服务器。如下图所示：
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318185526743.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
7. 完成 AD 域服务、DNS 服务安装，并将服务器提升为域控制器完毕。

### 安装 Web 服务器
1.参考安装 AD 域服务和 DNS 服务中 [步骤2](#step1)，进入服务器角色页面，在服务器角色信息栏勾选 Web 服务器。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318190638764.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
2. 保持页面默认信息不变，一直单击【下一步】>【安装】，完成 Web 服务器安装。

### 申请证书
如您已拥有 SSL 证书，可直接进行 [安装 ADFS](#step0) 操作。

1. 单击左下角【Windows图标】，在搜索框输入“mmc”命令，回车执行，进入控制台1-[控制台根节点]页面。如下图所示：
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318191733112.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
 
2. 在控制台1-[控制台根节点]页面，单击【文件】>【添加/删除管理单元】，在弹出的窗口中选择证书，单击【添加】>【完成】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318192045619.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

3. 单击【证书】，在展开的目录中，右键单击【个人】，单击【所有任务】>【高级操作】>【创建自定义请求】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318192351707.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

4. 保持页面默认信息不变，一直单击【下一步】，进入证书注册页面，单击【不使用注册策略继续】，如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020031820585614.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

5. 在自定义请求页面，选择以下信息，如下图所示：
> - 模板：（无模板）就密钥
> - 请求格式：PKCS#10
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318192428549.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
6. 单击【详细信息】>【证书属性】，在常规栏补充友好名称、描述信息。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318192915600.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
7. 在使用者栏，填写值信息，本次示例为（*.example.com），单击【添加】，如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318210128670.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

8. 在私钥栏下勾选 Microsoft RSA SChanel Cyptograhic Provider（加密）、使私钥可以导出。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318193734243.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

9. 单击【确认】>【下一步】，选择需要保存的目录，保存证书，单击完成。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318192512859.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

### 安装 ADC(AD证书服务器)
1. 参考安装 AD 域服务和 DNS 服务中 [步骤2](#step1)，在服务器角色信息栏勾选 Active Directory 证书服务器。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318194846791.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
2. 保持默认信息，一直单击【下一步】，在角色服务栏勾选证书颁发机构、证书颁发机构 Web 注册。如下图所示：
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/2020031819494054.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
 3. 单击【安装】，在完成安装成功界面，单击右上角![](https://main.qcloudimg.com/raw/32f3dcf3b4c58c0acb3485f2dab0f9a7.png)，单击【配置目标服务器的 Active Directory 证书服务】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318201736746.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
4.保持页面默认信息，一直单击【下一步】，在角色服务栏勾选证书颁发机构、证书颁发机构 Web 注册。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318201930415.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
5. 保持页面默认信息，一直单击【下一步】，单击【配置】，完成安装 ADC。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020031820211244.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

### 生成 SSL 证书
1. 访问 http://localhost/certsrv， 单击【申请证书】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318202315283.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
2. 在申请一个证书页面，单击【高级证书申请】。如下图所示：
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318202328820.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)、
 
3. 在高级证书申请页面，单击【使用 base64 编码的 CMC 或 PKCS#10 文件提交一个证书申请，或使用 base64 编码的 KCS#7 文件 续订证书申请】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020031820234780.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
4. 将申请证书保存的证书文件内容复制之后补充至以下输入框，证书模板选择 Web 服务器，单击【提交】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318202513846.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
5. 申请成功，单击【下载】（两种格式均需下载）。如下图所示：
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318202529897.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
 
6. 参考申请证书的第 3 步，右键单击【个人】，单击【所有任务】>【导入】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318204054988.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
7. 选择第 5 步保存的证书文件，保持页面默认信息，一直单击【下一步】>【完成】。
8. 参考申请证书的第 3 步，右键单击【个人】，单击【所有任务】>【导出】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318214746752.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
9.在证书导出想到页面，选择“是，导出私钥”，勾选“组或用户名名（建议）”，单击下一步，完成导出保存文件。<span id="step1">如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318214811676.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318214838629.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

### 安装 ADFS
1.<span id="step0"> 参考安装 AD 域服务和 DNS 服务中 [步骤2](#step1)，进入服务器角色页面，勾选 Active Directory 联合身份验证服务。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318191433342.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
2. 保持页面默认信息，一直单击【下一步】>【完成】，在结果页面，单击【在此服务器上配置联合身份验证服务】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318191612493.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
3. 保持页面默认信息，一直单击【下一步】，进入指定服务属性页面，填写导入以下信息
SSL 证书：导入生成 SSL 证书中 [步骤 9](#step9) 保存的证书文件。
联合身份服务名称：与右上角信息保持一致。
联合身份验证服务显示名称：用户在登录时看到显示名称。
如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318220107449.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

4. 在指定服务账户页面，输入账户名称、密码，<span id="step4">保持页面默认信息，一直单击【下一步】。如下图所示：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318220330470.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)

5.访问以下链接下载 XML文件。
```
https://域名/federationmetadata/2007-06/federationmetadata.xml
```

6.在 powerShell 中执行 Set-AdfsProperties –EnableIdpInitiatedSignonPage $True，
访问以下入口进行登录。

```
https://域名/adfs/ls/idpinitiatedSignOn.htm
```
7. 输入 [步骤4](#step4) 中的账号名称、密码登录，登录成功如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318222316599.png)

8.单击服务器管理器-ADFS 页面右上角【工具】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318222419833.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
9. 选择 ADFS 管理，单击【添加信赖方】，如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318222456530.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
10.在添加先来访新人想到页面，选择“声明感知”，单击【启动】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318223223654.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
11.访问以下链接下载腾讯云身份提供商的 XML 文件。

```
https://cloud.tencent.com/saml.xml
```
12.导入腾讯云身份提供商的文件。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318223441957.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
13.保持页面默认信息，一直单击【下一步】>【完成】。
14.单击【信赖方信任】>【添加规则】>【编辑声明颁发策略】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200319023517188.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
15.在选择规则模板页面，单击【选择规则类型】>【下一步】。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200319023531720.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200319023555423.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
	![在这里插入图片描述](https://img-blog.csdnimg.cn/20200319031612885.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)
	![在这里插入图片描述](https://img-blog.csdnimg.cn/20200319031658885.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RIRUFOQVJLSA==,size_16,color_FFFFFF,t_70)



