本文档将指导您如何在 macOS 系统下，为 Thunderbird 配置邮件（[S/MIME](https://cloud.tencent.com/document/product/1325/49418)）证书，本文以 macOS 10.13.6 版本为例进行说明。

## 前提条件
- 已在 macOS 系统上安装 Thunderbird 客户端。
- 已 [申请购买邮件（S/MIME）证书](https://cloud.tencent.com/apply/p/cn69mmv599k)。


## 操作步骤
### 步骤1：对 Thunderbird 配置 S/MIME 证书

1. 购买邮件（S/MIME）证书并信息审核通过后，线下业务人员将发送给您邮件证书压缩包，获取邮件证书压缩包至 macOS 系统，并进行解压。
2. 在 macOS 首页，选择**Thunderbird** > **首选项**。
<img src="https://main.qcloudimg.com/raw/44dbe59860173a899a1984d7d5b1d956.png" style="zoom:65%;" />
3. 在弹框中选择证书标签，并单击**管理证书**。
![](https://main.qcloudimg.com/raw/03178521aaf92bfa95bff3f64c54c495.png)
4. 在证书管理器弹窗中，单击**导入**，选择对应邮箱 S/MIME 证书。
<img src="https://main.qcloudimg.com/raw/d5cdc44103defdd1234bf74525651c1e.png" style="zoom:90%;" />
5. 在弹出的密码输入框中，输入证书密码，单击**确定**，即可完成配置。
>?密码可在邮件证书压缩包中获取。
>
![](https://main.qcloudimg.com/raw/ba0719a9fa0fe691e900dc4f3f75684b.png)

### 步骤2：证书配置

1. 在 macOS 首页左上角，选择**工具** > **账户设置**。
![](https://main.qcloudimg.com/raw/fb142e74f050dfe4af90c1495341ebf6.png)
2. 在弹出框中选择需要配置证书的邮箱，单击**安全**，在“数字签名”及“加密”模块，单击**选择**，选择对应邮箱的证书。
<img src="https://main.qcloudimg.com/raw/a9efa3354d4e6afb89113dec057f5ced.png" style="zoom:90%;" />
3. 在弹框中选中对应证书，并将加密签发选项更改成如下图所示，单击**确认**，即可完成证书配置。
![](https://main.qcloudimg.com/raw/4dfd1b7512d63a10d7e5fde422feb47a.png)

### 步骤3：邮件加密签名配置
选择完成对应的签名和加密证书后，可将默认配置调整如下图所示：
<img src="https://main.qcloudimg.com/raw/82b3f5a24e3f5518ebfe8b03da0bf015.png" style="zoom:90%;" />

### 步骤4：邮件发送
- **签名邮件发送**
 新建邮件，编辑内容后，在上方导航中，选择**安全** > **对此消息数字签名**，即可发送签名邮件。
<img src="https://main.qcloudimg.com/raw/be94d832a3c4e615a332a24f73739f0e.png" style="zoom:60%;" />
- **加密邮件发送**
 新建邮件，编辑内容后，在上方导航中，选择**安全** > **加密此消息**和**对此消息数字签名**，即可发送签名邮件。
>!发送加密邮件需要对方公钥信息，如果需要对方的公钥信息，可让对方先发送一封签名邮件到您的邮箱帐户中，即可给对方发送加密邮件。
>
<img src="https://main.qcloudimg.com/raw/079ef436d084a0653cb19f5f5b8483da.png" style="zoom:60%;" />

