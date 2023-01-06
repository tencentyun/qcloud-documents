
COSBrowser 是腾讯云对象存储（Cloud Object Storage，COS）推出的可视化界面工具，界面交互更简单，操作更便捷，支持桌面端和移动端。通过该工具您可轻松实现对 COS 资源的查看、传输和管理。关于 COSBrowser 的更多介绍，请参见 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)。

本文将为您简单介绍如何通过 COSBrowser 工具快速创建存储桶，并完成对象上传、下载和分享操作。


## 前提条件

1. 已通过腾讯云账号开通 COS 服务。
>?
>- 若无腾讯云账号，可参见 [账号相关文档](https://cloud.tencent.com/document/product/378) 进行创建。
>- 若未开通 COS 服务，请前往 [COS 控制台](https://console.cloud.tencent.com/cos5)，按照提示进行开通。
2. 初次使用 COS，建议您先了解以下基本概念：
 - [存储桶（Bucket）](https://cloud.tencent.com/document/product/436/13312)：是对象的载体，可理解为存放对象的“容器”。一个存储桶可容纳无数个对象。
 - [对象（Object）](https://cloud.tencent.com/document/product/436/13324)：是对象存储的基本单元，可理解为任何格式类型的数据，例如图片、文档和音视频文件等。
 - [地域（Region）](https://cloud.tencent.com/document/product/436/6224)：是腾讯云托管机房的分布地区，对象存储 COS 的数据存放在这些地域的存储桶中。


## 步骤1：下载并安装 COSBrowser


1. 以 Windows 版本 COSBrowser 为例，[单击下载 COSBrowser](https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-setup-latest.exe)。
2. 下载完成后，直接双击打开安装包，并按照提示安装即可。


>?
>- Windows 版本 COSBrowser 的系统要求：Windows 7 32/64位以上、Windows Server 2008 R2 64位以上。
>- 如需下载其他系统版本 COSBrowser，请前往  [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366) 下载。



## 步骤2：登录 COSBrowser

Windows 版本 COSBrowser 支持多种登录方式，包括 API 密钥登录、腾讯云账号登录、共享链接登录。此处我们选择腾讯云账号登录方式。


## 步骤3：创建存储桶

1. 登录成功后，在工具界面中单击左上方的**创建桶**。
2. 在弹出的窗口中，输入存储桶信息。
![](https://qcloudimg.tencent-cloud.cn/raw/cb247e5503e220e935ac093249b75470.png)
 - 存储桶名称：自定义存储桶名称，此处我们输入 examplebucket。
 - 地域：指存储桶的所属地域，选择与您最近的一个地区。例如，您在深圳，地域可以选择广州，即 ap-guangzhou。
 - 访问权限：指存储桶的访问权限，此处我们选择“私有读写”。
 - 存储桶标签/多 AZ 特性为可选项，此处忽略。
3. 单击**确定**，即可完成创建。在存储桶列表中可看到已创建的存储桶。


## 步骤4：上传对象

1. 单击刚创建的存储桶，进入存储桶管理页。
2. 选择**上传 > 选择文件**，选择需要上传至存储桶的本地文件，例如 exampleobject.txt。
3. 单击**上传**，即可将 exampleobject.txt 上传至存储桶。


## 步骤5：下载对象

选择想要下载的文件，并右键单击**下载**即可。

## 步骤6：分享对象

COSBrowser 支持通过文件链接或二维码的方式进行文件分享，下面以文件链接分享方式为例。

1. 选择想要分享的文件，并单击右侧的<img src="https://main.qcloudimg.com/raw/37acaeb370eb77e1bb0c792d542792e2.jpg"  style="margin:0;">，即可快速生成分享链接。
>?由于文件继承存储桶的私有读写权限，因此生成的分享 URL 属于临时访问的链接，有效期为2小时。
2. 将生成的分享链接发送给接收者，即可在线访问或下载。
>?
>默认情况下，如果分享的文件支持浏览器直接打开，那么访问临时链接将直接在线查看，而不是下载。


## 更多功能

除以上功能外，COSBrowser 还拥有其他更丰富的功能，例如修改存储桶访问权限，文件预览等，详情请参见 [桌面端功能列表](https://cloud.tencent.com/document/product/436/11366#.E6.A1.8C.E9.9D.A2.E7.AB.AF.E5.8A.9F.E8.83.BD.E5.88.97.E8.A1.A8) 文档。

## 遇到问题？

非常抱歉您在使用时遇到问题，您可查看 [常见问题](https://cloud.tencent.com/document/product/436/43356) 或 [联系我们](https://cloud.tencent.com/document/product/436/37708)。

## 相关文档

了解移动端（iOS、Android）的 COSBrowser，请参见以下文档。

- [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)
- [移动端使用说明](https://cloud.tencent.com/document/product/436/38105)
