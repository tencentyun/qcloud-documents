本文档将指导您如何在 Windows10 系统下为 Outlook 配置邮件（[S/MIME](https://cloud.tencent.com/document/product/1325/49416)）证书，本文以 Outlook 1902 版本为例进行说明。

## 前提条件
- 已在 Windows10 系统上安装 Outlook 客户端。
- 已 [申请购买邮件（S/MIME）证书](https://cloud.tencent.com/apply/p/cn69mmv599k)。


## 操作步骤
### 步骤1：安装证书文件

1. 购买邮件（S/MIME）证书并信息审核通过后，线下业务人员将发送给您邮件证书压缩包，获取邮件证书压缩包至 Windows10 系统中，并进行解压。
2. 在 Windows10 中，双击 \*.pfx 后缀证书文件。
[](id:step1)
3. 在弹出的“证书导入向导”中，如果需要设置密码，可将私钥密码输入，单击**下一步**，即可设置成功。
<img src="https://main.qcloudimg.com/raw/09eb20202ccd941c6e66a6997a7f0df7.png" style="zoom:90%;" />

### 步骤2：配置 Outlook 客户端
1. 打开 Outlook ，在主菜单中，单击**文件**。
2. 在左侧导航中，单击**选项**。
![](https://main.qcloudimg.com/raw/077f862d101bab03bb91723780f1f700.png)
3. 在“Outlook 选项”窗口的左侧导航中，单击**信任中心**，在“Microsoft Outlook 信任中心”模块，单击**信任中心设置**。
<img src="https://main.qcloudimg.com/raw/2402e883dc9bc8bf19a25b5d62c2a10f.png" style="zoom:80%;" />
4. 在“信任中心”窗口的左侧导航中，单击**电子邮件安全**，并在“数字标识（证书）模块”，单击**导入/导出** 。
<img src="https://main.qcloudimg.com/raw/7278d60e65350675496ec11087364545.png" style="zoom:80%;" />
5. 在“导入/导出数字标识”窗口中，勾选“从某文件导入现有的数字标识” ，然后单击**浏览...**，选取证书文件，单击**确定**。
<img src="https://main.qcloudimg.com/raw/dc0317ac8538a41f8206eb7d74c5ae70.png" style="zoom:85%;" />
6. 输入在 [步骤1](#step1) 中设置的证书密码，单击**确定**。
![](https://main.qcloudimg.com/raw/63d686290224a13677b1970a430960dd.png)
7.  在弹出的安全对话框中，单击**确定**。
![](https://main.qcloudimg.com/raw/745ecde27ac78d68a9405c9e086367eb.png)


### 步骤3：电子邮件证书配置
1. 打开 Outlook ，在主菜单中，单击**文件**。
2. 在左侧导航中，单击**选项**。
![](https://main.qcloudimg.com/raw/077f862d101bab03bb91723780f1f700.png)
3. 在“Outlook 选项”窗口的左侧导航中，单击**信任中心**，在“Microsoft Outlook 信任中心”模块，单击**信任中心设置**。
<img src="https://main.qcloudimg.com/raw/2402e883dc9bc8bf19a25b5d62c2a10f.png" style="zoom:80%;" />
4. 在“信任中心”窗口的左侧导航中，单击**电子邮件安全**，并在“加密电子邮件模块”，单击**设置**。
<img src="https://main.qcloudimg.com/raw/0df60ac7733954755ccffbdea0325daa.png" style="zoom:85%;" />
5. 在“更改安全设置”窗口中，选择“安全设置名称”并勾选“该安全邮件格式的默认加密设置”与“所有安全邮件的默认加密设置”。
![](https://main.qcloudimg.com/raw/736d6deb38c62ae3ee1e46681063f432.png)
6. 在签名证书右侧，单击**选择**，选择签名证书。
![](https://main.qcloudimg.com/raw/164606f638ccd8d8351809b319c8e65c.png)
7. 弹出的确认对话框中，单击**确定**。
![](https://main.qcloudimg.com/raw/4ef20c14b64cf3199af0df548ebdd04c.png)
8. 在加密证书右侧，单击**选择**，选择加密证书，单击**确定**，关闭“更改安全设置”窗口即可。
![](https://main.qcloudimg.com/raw/f3e751651b96a0f200b6b5ab776a4c80.png)


### 步骤4：S/MIME 加密邮件配置
如果需要发送加密邮件，电子邮件安全中默认配置需调整操作步骤如下：
1. 打开 Outlook ，在主菜单中，单击**文件**。
2. 在左侧导航中，单击**选项**。
![](https://main.qcloudimg.com/raw/077f862d101bab03bb91723780f1f700.png)
3. 在“Outlook 选项”窗口的左侧导航中，单击**信任中心**，在“Microsoft Outlook 信任中心”模块，单击**信任中心设置**。
<img src="https://main.qcloudimg.com/raw/2402e883dc9bc8bf19a25b5d62c2a10f.png" style="zoom:80%;" />
4. 在“信任中心”窗口的左侧导航中，单击**电子邮件安全**，并在“加密电子邮件模块”，勾选“加密待发邮件的内容和附件”“给待发邮件添加数字签名”及“对所有 S/MIME 签名邮件要求 S/MIME 回执”。
![](https://main.qcloudimg.com/raw/9658b335b0d8314a11e74241e030704f.png)

### 步骤5：发送邮件

- **签名邮件发送**
新建邮件，编辑内容后，在上方导航中，单击**签署**，即可发送签名邮件。
![](https://main.qcloudimg.com/raw/bb344668421a775ebbbff8dc08a1c0c6.png)
- **加密邮件发送**
新建邮件，编辑内容后，在上方导航中，单击**加密**及**签署**，即可发送加密邮件。
>!发送加密邮件需要对方公钥信息，如果需要对方的公钥信息，可让对方先发送一封签名邮件到您的邮箱帐户中，即可给对方发送加密邮件。
>
![](https://main.qcloudimg.com/raw/babf4da18119abdf05fbbe38b7860636.png)

