本文档将指导您如何在 macOS 系统下为 OutLook 配置邮件（S/MIME）证书。

## 前提条件
- 已在 macOS 系统上安装 OutLook 客户端。（本文以 macOS 10.13.6、Outlook 2013 版本为例）
- 已 [申请购买邮件（S/MIME）证书]()。


## 操作步骤
### 步骤1：密钥导入
1. 购买邮件（S/MIME）证书后，线下业务人员将发送给您邮件证书压缩包，获取邮件证书压缩包至 macOS 系统，并进行解压。
2. 在 Finder 中，双击 \*.p12 后缀证书文件，打开“钥匙串访问”应用程序。
3. 在提示框中，输入\*.p12 后缀证书文件的使用密码，单击【确定】，即可安装完成。
>?密码可在邮件证书压缩包中获取。
>
![](https://main.qcloudimg.com/raw/15b434f0c971045ac87c857dd908aadb.png)
4. 安装完成后，可在计算机中进行查看证书，并可供 Apple Mail 和其他应用程序使用。
<img src="https://main.qcloudimg.com/raw/fb8d9f2d48881fe626baa6555e19ffe5.png" style="zoom:75%;" />


### 步骤2：OutLook 配置 SMIME 证书

1. 打开 Outlook ，在上方菜单中选择【工具】>【帐户】。
![](https://main.qcloudimg.com/raw/5444887ab05df957cb12ab19ba7d43ab.png)
2. 选择您的证书所属的帐户，然后单击【高级】按钮。
<img src="https://main.qcloudimg.com/raw/1861297dddb7953025020219d24fc62d.png" style="zoom:75%;" />
3. 单击【安全性】标签，选择数字证书和签名算法，加密证书及加密算法，签名项配置请按照以下方式选择。
>?签名算法 SHA-1 比 SHA26 兼容性好，SHA256 更加安全。
>
<img src="https://main.qcloudimg.com/raw/1c29ff63825ac15ec031afc8b553803c.png" style="zoom:75%;" />
4. 单击【确认】，保存设置。<br>
<img src="https://main.qcloudimg.com/raw/2e4d2c38052c9d91b6162fccbdc5305f.png" style="zoom:75%;" />

### 步骤3：发送邮件
- **发送签名文件**
新建邮件，编辑内容后，在上方导航中，单击【签名】，即可将邮件添加数字签名。
![](https://main.qcloudimg.com/raw/0e75fba53850abcf0dbde92d02294f02.png)
- **发送加密文件**
新建邮件，编辑内容后，在上方导航中，单击【加密】及【签名】，即可将邮件添加数字签名并进行加密。
>!发送加密邮件需要拥有对方公钥信息，否则加密邮件无法发送成功。如果需要对方的公钥信息，可让对方先发送一封签名邮件到您的邮箱帐户中，即可给对方发送加密邮件。
>
![](https://main.qcloudimg.com/raw/976e331178c06a2ebbfca9ce3ae32404.png)
