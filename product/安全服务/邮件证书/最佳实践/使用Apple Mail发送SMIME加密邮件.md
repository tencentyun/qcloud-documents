

本文档将指导您如何在 macOS 系统下使用 Apple Mail 发送 [S/MIME](https://cloud.tencent.com/document/product/1325/49418) 加密邮件，本文以 macOS 10.13.6 版本为例进行说明。

## 前提条件
已 [申请购买邮件（S/MIME）证书](https://cloud.tencent.com/apply/p/cn69mmv599k)。

## 操作步骤
### 步骤1：安装证书文件
1. 购买邮件（S/MIME）证书并通过信息审核后，线下业务人员将发送给您邮件证书压缩包，获取邮件证书压缩包至 macOS 系统，并进行解压。
2. 在 Finder 中，双击 \*.p12 后缀文件，打开“钥匙串访问”应用程序。（文件扩展名是 .p12）。
3. 在提示框中，输入\*.p12 后缀证书文件的使用密码，单击**OK**。
>?密码可在邮件证书压缩包中获取。
>
<img src="https://main.qcloudimg.com/raw/94f054027a84ee37acae781dab45ffea.png" style="zoom:60%;" />
4. 该证书现已安装在您的计算机上，可供 Apple Mail 和其他应用程序使用。如下图所示：
<img src="https://main.qcloudimg.com/raw/8b9bc734475fe67fbe469976b539c1ed.png" style="zoom:65%;" />


### 步骤2：邮件发送
1.	打开 Apple Mail 邮件。 
>!如果在安装证书时，已打开邮件，请重新启动。
2.	创建一个新的电子邮件。 
>?
>- 如果在“邮件”中配置了多个电子邮件地址，请确保已在“发件人”行中，选择为其颁发证书的地址。 
>- 如果证书已正确安装，则在“主题”行右侧，应出现带有复选标记的蓝色<img src="https://main.qcloudimg.com/raw/3367f4add79bd4be7e154ba8c48f57db.png" style="margin:0;">图标，表明该消息已签名。 如果您不想对消息进行签名，则可以单击<img src="https://main.qcloudimg.com/raw/3367f4add79bd4be7e154ba8c48f57db.png" style="margin:0;">，以取消选中。
>- 如果您有收件人的公共密钥，则在“主题”行右侧，单击<img src="https://main.qcloudimg.com/raw/8bf8f64ad6d6247ce2795dcce059c35f.png" style="margin:0;">，将锁闭合锁，表示您的邮件将被加密。 如果由于某种原因不想加密电子邮件，请单击<img src="https://main.qcloudimg.com/raw/9d0ff6ef0ef2cbea82c1cfcf62e791eb.png" style="margin:0;">，将锁打开表示不对邮件进行加密。
>
![](https://main.qcloudimg.com/raw/6403d0d268d0328f8eebaef1288bc504.png)
4. 编辑完邮件，单击**发送**即可。
>?
>- 若发送加密邮件，将弹出提示窗口，需输入 Mac 登录密码，授予 Mail 使用私钥对消息签名的权限， 并单击 **Allow** 或 **Always Allow**。如果您单击 **Always Allow** ，下一次使用证书签名电子邮件时，将不会提示您输入密码。
>- 如果您使用的是安装在 YubiKey 上的证书，将提示您输入 PIN 码而不是登录密码。
>
<img src="https://main.qcloudimg.com/raw/8b886f29a5a95289de8b6debaf1b32ba.png" style="zoom:65%;" />
