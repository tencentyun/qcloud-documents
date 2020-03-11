初次使用对象存储 COS，建议您先了解 COS [基本概念](https://cloud.tencent.com/document/product/436/6222)、[规格与限制](https://cloud.tencent.com/document/product/436/14518) 和  [常见问题](https://cloud.tencent.com/document/product/436/30748)。

COSBrowser 是腾讯云对象存储 COS 推出的可视化界面工具，让您可以使用更简单的交互轻松实现对 COS 资源的查看、传输和管理。
通过 COSBrowser，您可以快速进行创建存储桶、上传/下载对象等操作，本文以 Windows 平台的 COSBrowser 为例，详细步骤如下。


## 前提条件

腾讯云账号已开通 COS 服务。


## 步骤1：下载安装COSBrowser


<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-setup-latest.exe" target="_blank"  style="color: white; font-size:16px;">点此下载 COSBrowser</a></div>

<br>

>?
>- 系统要求：Windows 7 32/64位以上、Windows Server 2008 R2 64位以上。
>- 其它系统的 COSBrowser 客户端，请前往  [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366) 下载。


<table>
   <tr>
      <th>COSBrowser 分类</td>
      <th>支持平台</td>
      <th>系统要求</td>
      <th>下载地址</td>
   </tr>
   <tr>
      <td rowspan=3>桌面端</td>
      <td>Windows</td>
      <td>Windows 7 32/64位以上、Windows Server 2008 R2 64位以上</td>
      <td><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-setup-latest.exe">Windows</a></td>
   </tr>
   <tr>
      <td>macOS</td>
      <td>macOS 10.13以上</td>
      <td><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-latest.dmg">macOS</a></td>
   </tr>
   <tr>
      <td>Linux</td>
      <td>需带有图形界面并支持 <a href="https://appimage.org">AppImage</a> 格式</td>
      <td><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-latest-linux.zip">Linux</a></td>
   </tr>
   <tr>
      <td rowspan=2>移动端</td>
      <td>Android</td>
      <td>Android 4.4以上</td>
      <td><a href="https://sj.qq.com/myapp/detail.htm?apkName=com.qcloud.cos.client">Android</a></td>
   </tr>
   <tr>
      <td>iOS</td>
      <td>iOS 11以上</td>
      <td><a href="https://apps.apple.com/cn/app/id1469323992">iOS</a></td>
   </tr>
</table>

## 步骤2：获取 API 密钥 
COSBrowser 工具使用 API 密钥登录，若未创建 API 密钥 

<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/cam/capi" target="_blank"  style="color: white; font-size:16px;">点此获取 API 密钥</a></div>


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


## 步骤5：上传对象

1. 单击步骤4创建的存储桶名称，进入存储桶管理页。
2. 选择【上传】>【选择文件】，选择需要上传至存储桶的文件，例如 exampleobjext.txt。
3. 单击【上传】，即可将 exampleobjext.txt 上传至存储桶。


## 步骤6：生成分享链接







## 遇到问题？

非常抱歉您在使用时遇到问题，您可以第一时间通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。



## 相关文档


- [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)
- [桌面端使用说明](https://cloud.tencent.com/document/product/436/38103)
- [移动端使用说明](https://cloud.tencent.com/document/product/436/38105)


