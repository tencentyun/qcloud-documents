
本文档将指导您如何在 Windows10 系统下为 Thunderbird 配置邮件（[S/MIME](https://cloud.tencent.com/document/product/1325/49418)）证书，本文以 Thunderbird 78.3.3 版本为例进行说明。

## 前提条件
- 已在 Windows10 系统上安装 Thunderbird 客户端。
- 已 [申请购买邮件（S/MIME）证书](https://cloud.tencent.com/apply/p/cn69mmv599k)。


## 操作步骤
### 步骤1：安装证书文件
1. 购买邮件（S/MIME）证书并信息审核通过后，线下业务人员将发送给您邮件证书压缩包，获取邮件证书压缩包至 Windows10 系统中，并进行解压。
2. 在 Windows10 中，双击 \*.fpx 后缀证书文件。
[](id:step1)
3. 在弹出的“证书导入向导”中，如果需要设置密码，可将私钥密码输入，单击**下一步**，即可设置成功。
<img src="https://main.qcloudimg.com/raw/09eb20202ccd941c6e66a6997a7f0df7.png" style="zoom:90%;" />

### 步骤2：Thunderbird 客户端 S/MIME 证书配置
1. 打开 Thunderbird 客户端，在需要配置的邮箱账户上方，单击鼠标右键，并单击**设置**。
![](https://main.qcloudimg.com/raw/ff6ce309d0b32eb4232223dfe3f133d2.png)
2. 在设置的左侧导航中，单击**端到端加密**，并在“端到端加密”页面，单击**管理 S/MIME 证书**。
![](https://main.qcloudimg.com/raw/a668b9f99051d68915537e89d60f1564.png)
3. 在证书管理器窗口，单击**导入**，在资源管理器中，选择对应证书并输入 [步骤1](#step1) 中设置的密码。
![](https://main.qcloudimg.com/raw/82cea23ea74c6f68246e831ff02bb705.png)
4. 单击**确定**，证书导入成功。
![](https://main.qcloudimg.com/raw/12e79a2a60b1c9eb7247098c1406385f.png)
5. 分别选择邮箱的“个人数字签名证书”及“个人加密证书”，并单击**确定**即可完成设置。
![](https://main.qcloudimg.com/raw/ed9595561fe4416fd5a4b08a5f314c80.png)

### 步骤3：发送邮件

- **发送签名邮件**
 新建邮件，编辑内容后，在上方导航中，选择**安全** > **对此消息数字签名**，即可发送签名邮件。
![](https://main.qcloudimg.com/raw/e8fc67d2dfae39a10f56744369232a83.png)
- **发送加密邮件**
新建邮件，编辑内容后，在上方导航中，选择**安全** > **要求加密**及**对此消息数字签名**，即可发送加密邮件。
>!发送加密邮件需要对方公钥信息，如果需要对方的公钥信息，可让对方先发送一封签名邮件到您的邮箱帐户中，即可给对方发送加密邮件。
>
![](https://main.qcloudimg.com/raw/82fbbdfc82e4b7211de52b9c0386fe9e.png)
