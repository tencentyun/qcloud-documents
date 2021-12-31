本文档将指导您如何在 macOS 系统下为 Outlook 配置邮件（[S/MIME](https://cloud.tencent.com/document/product/1325/49418)）证书，本文以 macOS 10.13.6、Outlook 2013 版本为例进行说明。

## 前提条件
- 已在 macOS 系统上安装 Outlook 客户端。
- 已 [申请购买邮件（S/MIME）证书](https://cloud.tencent.com/apply/p/cn69mmv599k)。


## 操作步骤
### 步骤1：密钥导入
1. 购买邮件（S/MIME）证书并信息审核通过后，线下业务人员将发送给您邮件证书压缩包，获取邮件证书压缩包至 macOS 系统，并进行解压。
2. 在 Finder 中，双击 \*.p12 后缀证书文件，打开“钥匙串访问”应用程序。
3. 在提示框中，输入\*.p12 后缀证书文件的使用密码，单击**确定**，即可安装完成。
>?密码可在邮件证书压缩包中获取。
>
![](https://main.qcloudimg.com/raw/fbbcbf62ce83c2c6e4d249e4a4dabec0.png)
4. 安装完成后，可在计算机中进行查看证书，并可供 Apple Mail 和其他应用程序使用。
<img src="https://main.qcloudimg.com/raw/fb8d9f2d48881fe626baa6555e19ffe5.png" style="zoom:75%;" />


### 步骤2：Outlook 配置 S/MIME 证书

1. 打开 Outlook ，在上方菜单中选择**工具** > **帐户**。
![](https://main.qcloudimg.com/raw/5444887ab05df957cb12ab19ba7d43ab.png)
2. 选择您的证书所属的帐户，然后单击**高级**。
<img src="https://main.qcloudimg.com/raw/1861297dddb7953025020219d24fc62d.png" style="zoom:75%;" />
3. 单击**安全性**标签，勾选并选择相关信息，配置可参考下图方式进行选择。
>?签名算法 SHA-1 比 SHA256 兼容性好，SHA256 更加安全。
>
<img src="https://main.qcloudimg.com/raw/1c29ff63825ac15ec031afc8b553803c.png" style="zoom:75%;" /><br>
字段说明：
	- **数字签名**：
		- **证书**：请选择您导入证书名称。
		- **签名算法**：可选择 SHA-1 或 SHA-256，建议选择 SHA-256 兼容性与安全性更好。
		- **给待发邮件签名**：如需使用邮件证书完成功能，请勾选此处。
		- **以明文方式发送带有数字签名的邮件**：如需使用邮件证书完成功能，请勾选此处。
		- **在签名邮件中包含我的证书**：如需使用邮件证书完成功能，请勾选此处。
	- **加密**：
		- **证书**：请选择您导入证书名称。
		- **加密算法**：建议选择 AES-256 ，安全性更好。
		-  **加密待发邮件**：可根据实际情况进行勾选。
	- **证书身份验证**：
**客户端证书**： 不进行选择。
4. 单击**确认**，保存设置。<br>
<img src="https://main.qcloudimg.com/raw/2e4d2c38052c9d91b6162fccbdc5305f.png" style="zoom:75%;" />

### 步骤3：发送邮件
- **发送签名文件**
新建邮件，编辑内容后，在上方导航中，单击**签名**，即可将邮件添加数字签名。
![](https://main.qcloudimg.com/raw/0e75fba53850abcf0dbde92d02294f02.png)
- **发送加密文件**
新建邮件，编辑内容后，在上方导航中，单击**加密**及**签名**，即可将邮件添加数字签名并进行加密。
>!发送加密邮件需要拥有对方公钥信息，否则加密邮件无法发送成功。如果需要对方的公钥信息，可让对方先发送一封签名邮件到您的邮箱帐户中，即可给对方发送加密邮件。
>
![](https://main.qcloudimg.com/raw/976e331178c06a2ebbfca9ce3ae32404.png)
