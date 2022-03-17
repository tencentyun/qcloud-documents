初次使用腾讯云对象存储（Cloud Object Storage，COS），建议您先了解 COS [存储桶](https://cloud.tencent.com/document/product/436/13312)、[对象](https://cloud.tencent.com/document/product/436/13324)、[规格与限制](https://cloud.tencent.com/document/product/436/14518) 和  [常见问题](https://cloud.tencent.com/document/product/436/30748)。

COSBrowser 是 COS 推出的可视化界面工具，提供 Windows、macOS、Linux、Android 和 iOS 版本，让您可以使用更简单的交互，轻松实现对 COS 资源的查看、传输和管理。
本文以 Windows 平台的 COSBrowser 为例，为您详细介绍如何创建存储桶、上传对象、下载对象以及如何分享对象。


## 前提条件

1. 腾讯云账号需开通 COS 服务。若未开通 COS 服务，请前往 [COS 控制台](https://console.cloud.tencent.com/cos5)，按照提示开通。
2. COSBrowser 工具使用 API 密钥登录，您需要先前往 [ API 密钥](https://console.cloud.tencent.com/cam/capi) 管理页面创建 API 密钥。


## 步骤1：下载安装 COSBrowser

Windows 版 COSBrowser 的系统要求：Windows 7 32/64位以上、Windows Server 2008 R2 64位以上。其它系统版本 COSBrowser ，请前往  [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366) 下载。


<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-setup-latest.exe" target="_blank"  style="color: white; font-size:16px;">点此下载 COSBrowser</a></div><br>



## 步骤2：登录 COSBrowser

使用 [API 密钥](https://console.cloud.tencent.com/cam/capi)，登录 COSBrowser。


## 步骤3：创建存储桶

1. 登录成功后，在工具界面中单击左上方的**添加桶**。
2. 在弹出的窗口中，输入存储桶信息。
![](https://main.qcloudimg.com/raw/1a3f4d103f53e495a9e46f5882258c46.png)
 - 名称：自定义存储桶名称，此处我们输入 examplebucket。
 - 所属地域：指存储桶的所属地域，选择与您最近的一个地区。例如，您在深圳，地域可以选择广州，即 ap-guangzhou。
 - 访问权限：指存储桶的访问权限，此处我们选择“私有读写”。
3. 单击**确定**，即可创建存储桶。


## 步骤4：上传对象

1. 单击步骤3刚创建的存储桶，进入存储桶管理页。
2. 选择**上传 > 选择文件**，选择需要上传至存储桶的本地文件，例如 exampleobjext.txt。
3. 单击**上传**，即可将 exampleobjext.txt 上传至存储桶。


## 步骤5：下载对象



#### 方式一


1. 单击 COSBrowser 工具右上角的<img src="https://main.qcloudimg.com/raw/b3de2bc7284b5aaba9b4f9af6c408205.jpg" style="margin:0;">，切换到列表视图（若已是在列表视图下，则无需进行此步骤）。
2. 在文件右侧的操作栏下，单击<img src="https://main.qcloudimg.com/raw/0631f784902fb5e146ac0d0f6befe346.jpg"  style="margin:0;">，即可下载文件。


#### 方式二

1. 鼠标右键单击文件，在下拉菜单中，单击**高级下载**。
2. COSBrowser 工具将弹出高级下载窗口，根据实际需求选择“重命名”、“覆盖” 或 “跳过”。
![](https://main.qcloudimg.com/raw/ff43f89b0e5817ebc0c4ff59973c0fb6.jpg)
3. 单击**立即下载**，COSBrowser 工具将按照您的选择下载文件。


## 步骤6：分享对象

存在 COS 中的每个文件均可通过特定的链接来进行访问，若文件是私有读权限，则可通过请求临时签名的方式生成带有时效的临时访问链接。以下是生成对象链接的两种方式：

#### 方式一

1. 单击 COSBrowser 工具右上角的<img src="https://main.qcloudimg.com/raw/b3de2bc7284b5aaba9b4f9af6c408205.jpg" style="margin:0;">，切换到列表视图（若已是在列表视图下，则无需进行此步骤）。
2. 在文件右侧的操作栏下，单击<img src="https://main.qcloudimg.com/raw/37acaeb370eb77e1bb0c792d542792e2.jpg"  style="margin:0;">。
3. COSBrowser 工具顶部显示**临时链接复制成功，链接2小时有效**，则说明链接生成并复制成功。
4. 您即可通过该链接访问文件。通过此方式生成的文件链接，有效期为两个小时，若您需要自定义有效期，可通过方式二实现。


#### 方式二

1. 单击 COSBrowser 工具右上角的<img src="https://main.qcloudimg.com/raw/b3de2bc7284b5aaba9b4f9af6c408205.jpg" style="margin:0;">，切换到列表视图（若已是在列表视图下，则无需进行此步骤）。
1. 在文件右侧的操作栏下，单击**...**，在下拉菜单中，单击**分享**。
![](https://main.qcloudimg.com/raw/7d168f33452645d934215639179a2097.png)
2. 在弹出的自定义复制链接窗口中，配置文件链接。此处文件为私有读写权限，则需要选择**复制带签名的临时链接....**，链接在指定的时间内有效。
![](https://main.qcloudimg.com/raw/e8317ff57b37391f2bcc0dfe88aabacc.jpg)
3. 单击**复制**，复制临时文件链接。您即可通过该链接访问文件。

## 更多功能

除以上功能外，COSBrowser 还拥有其它更丰富的功能，例如修改存储桶访问权限，文件预览等，详情请参见 [桌面端功能列表](https://cloud.tencent.com/document/product/436/11366#.E6.A1.8C.E9.9D.A2.E7.AB.AF.E5.8A.9F.E8.83.BD.E5.88.97.E8.A1.A8) 文档。

## 遇到问题？

非常抱歉您在使用时遇到问题，您可以 [联系我们](https://cloud.tencent.com/document/product/436/37708)。

## 相关文档

了解移动端（iOS、Android）的 COSBrowser ，请参见以下文档。

- [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)
- [移动端使用说明](https://cloud.tencent.com/document/product/436/38105)

