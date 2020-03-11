初次使用对象存储 COS，建议您先了解 COS [基本概念](https://cloud.tencent.com/document/product/436/6222)、[规格与限制](https://cloud.tencent.com/document/product/436/14518) 和  [常见问题](https://cloud.tencent.com/document/product/436/30748)。

COSBrowser 是腾讯云对象存储 COS 推出的可视化界面工具，提供 Windows、macOS、Linux、Android 和 iOS 版本，让您可以使用更简单的交互，轻松实现对 COS 资源的查看、传输和管理。
本文以 Windows 平台的 COSBrowser 为例，为您详细介绍如何创建存储桶、上传文件、以及生成文件链接。


## 前提条件

腾讯云账号已开通 COS 服务。


## 步骤1：下载安装 COSBrowser


<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-setup-latest.exe" target="_blank"  style="color: white; font-size:16px;">点此下载 COSBrowser</a></div><br>

Windows 版 COSBrowser 的系统要求：Windows 7 32/64位以上、Windows Server 2008 R2 64位以上。其它系统版本 COSBrowser ，请前往  [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366) 下载。


## 步骤2：获取 API 密钥 


<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/cam/capi" target="_blank"  style="color: white; font-size:16px;">点此获取 API 密钥</a></div><br>


COSBrowser 工具使用 API 密钥登录，若未创建 API 密钥，请先创建 API 密钥。


## 步骤3：登录 COSBrowser

使用 API 密钥，登录 COSBrowser。


## 步骤4：创建存储桶

1. 单击左上角的【添加桶】。
2. 在弹出的窗口中，输入存储桶信息。
 - 名称：存储桶名称，此处我们输入 examplebucket。
 - 所属地域：存储桶存放地域，选择与您最近的一个地区，例如我在 “深圳”，地域可以选择 “广州”。
 - 访问权限：存储桶访问权限，此处我们选择“私有读写”。
![](https://main.qcloudimg.com/raw/bb6520123783e7398a7848e8c0330d18.jpg)
3. 单击【确定】，即可创建存储桶。


## 步骤5：上传文件

1. 单击步骤4创建的存储桶名称，进入存储桶管理页。
2. 选择【上传】>【选择文件】，选择需要上传至存储桶的文件，例如 exampleobjext.txt。
3. 单击【上传】，即可将 exampleobjext.txt 上传至存储桶。


## 步骤6：生成文件链接

存在 COS 中的每个文件均可通过特定的链接来进行访问，若文件是私有读权限，则可通过请求临时签名的方式生成带有时效的临时访问链接。

1. 在文件的右侧，单击【**...**】，在下拉菜单中，单击【分享】。
![](https://main.qcloudimg.com/raw/0866f3ee75a68082ff767205e6796b11.jpg)
>?COSBrowser 支持以网格和列表两种视图展示文件，您可单击右上角的视图切换按钮，进行切换。
2. 在弹出的自定义复制链接窗口中，配置文件链接。此处文件为私有读写权限，则需要选择【复制带签名的临时链接....】，链接在指定的时间内有效。
![](https://main.qcloudimg.com/raw/86ad4bd873bf67ac9b4e0a944946a014.jpg)
3. 单击【复制】，复制文件链接。您即可通过该链接访问文件。





## 遇到问题？

非常抱歉您在使用时遇到问题，您可以第一时间通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。



## 相关文档

了解更多 COSBrowser 功能，例如设置存储桶访问权限、设置版本控制等，请参见以下文档。
- [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)
- [桌面端使用说明](https://cloud.tencent.com/document/product/436/38103)
- [移动端使用说明](https://cloud.tencent.com/document/product/436/38105)


