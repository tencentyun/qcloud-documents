COSBrowser 是腾讯云对象存储 COS 推出的可视化界面工具，让您可以使用更简单的交互轻松实现对 COS 资源的查看、传输和管理。目前 COSBrowser 有桌面端和移动端两种，详情可参见：

- [桌面端使用说明](https://cloud.tencent.com/document/product/436/38103)
- [移动端使用说明](https://cloud.tencent.com/document/product/436/38105)

## 下载地址

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
      <td>需带有图形界面并支持 <a href="https://appimage.org">AppImage</a> 格式<br>
          注意：CentOS 启动客户端需在终端执行 <code>./cosbrowser.AppImage --no-sandbox</code></td>
      <td><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-latest-linux.zip">Linux</a></td>
   </tr>
   <tr>
      <td rowspan=2>移动端</td>
      <td>Android</td>
      <td>Android 4.4以上</td>
      <td><a href="https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-latest.apk">Android</a></td>
   </tr>
   <tr>
      <td>iOS</td>
      <td>iOS 11以上</td>
      <td><a href="https://apps.apple.com/cn/app/id1469323992">iOS</a></td>
   </tr>
   <tr>
      <td>网页版</td>
      <td>Web</td>
      <td>Chrome/FireFox/Safari/IE10+等浏览器</td>
      <td><a href="https://cosbrowser.cloud.tencent.com/web">Web</a></td>
   </tr>
   <tr>
      <td>Uploader 插件</td>
      <td>Web</td>
      <td>Chrome 浏览器</td>
      <td><a href="https://chrome.google.com/webstore/detail/cosbrowser-uploader/mggpkimgmmdbdbakdkaebhjhgomcmlnd">应用商店</a>/<a href="https://cos5.cloud.tencent.com/cosbrowser/latest-chrome.zip">离线下载</a></td>
   </tr>
</table>

## 桌面端功能列表

COSBrowser 桌面端注重对资源的管理，用户可以通过 COSBrowser 批量的上传、下载数据。

> !COSBrowser 桌面端会使用系统配置的代理来尝试网络连接，请确保您的代理配置正常或请停用无法连接互联网的代理配置。
>
> - Windows 用户可在操作系统的“Internet 选项”中查询。
> - macOS 用户可在“网络偏好设置”中查询。
> - Linux 用户可在系统设置 > 网络 > 网络代理中查询。

COSBrowser 桌面端支持以下功能：

| 功能                                                         | 功能说明                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [创建/删除存储桶](https://cloud.tencent.com/document/product/436/38103#createordelete) | 支持创建、删除存储桶                                         |
| [查看存储桶详情](https://cloud.tencent.com/document/product/436/38103#viewbucket) | 支持查看存储桶基本信息                                       |
| [查看统计数据](https://cloud.tencent.com/document/product/436/38103#count)           | 支持查看存储桶的当前存储量及对象总数                         |
| [权限管理](https://cloud.tencent.com/document/product/436/38103#viewbucket) | 支持修改存储桶、对象的相关权限                               |
| [设置版本控制](https://cloud.tencent.com/document/product/436/38103#viewbucket) | 支持开启、暂停存储桶版本控制                                 |
| [添加访问路径](https://cloud.tencent.com/document/product/436/38103#addaccess) | 支持添加访问路径                                             |
| [上传文件/文件夹](https://cloud.tencent.com/document/product/436/38103#upload) | 支持单个上传、批量上传、增量上传文件或文件夹至存储桶         |
| [下载文件/文件夹 ](https://cloud.tencent.com/document/product/436/38103#download) | 支持单个下载、批量下载、增量下载文件或文件夹至本地           |
| [删除文件/文件夹](https://cloud.tencent.com/document/product/436/38103#delete) | 支持单个删除、批量删除存储桶中的文件或文件夹                 |
| [文件同步](https://cloud.tencent.com/document/product/436/38103#synchronization) | 支持将本地文件实时同步至存储桶中                             |
| [复制粘贴文件](https://cloud.tencent.com/document/product/436/38103#copy) | 支持单个复制、批量复制一个目录下的文件或文件夹至另一个目录   |
| [文件重命名](https://cloud.tencent.com/document/product/436/38103#rename) | 支持重命名存储桶中的文件                                     |
| [新建文件夹](https://cloud.tencent.com/document/product/436/38103#newfolder) | 支持在存储桶中新建文件夹                                     |
| [查看文件详情](https://cloud.tencent.com/document/product/436/38103#view) | 支持查看存储桶中的文件基本信息                               |
| [生成文件链接](https://cloud.tencent.com/document/product/436/38103#generatelinks) | 支持通过请求临时签名的方式生成带有时效的文件访问链接         |
| [文件/文件夹分享](https://cloud.tencent.com/document/product/436/38103#share) | 支持分享文件和文件夹，支持设置分享的有效时间         |
| [导出文件 URL](https://cloud.tencent.com/document/product/436/38103#export) | 支持批量导出文件 URL         |
| [文件预览](https://cloud.tencent.com/document/product/436/38103#preview) | 支持预览存储桶中的媒体文件（图片、视频、音频）               |
| [搜索文件](https://cloud.tencent.com/document/product/436/38103#searchfile) | 支持以前缀搜索的方式对存储桶中的文件进行搜索                 |
| [搜索存储桶](https://cloud.tencent.com/document/product/436/38103#searchbuckete) | 支持搜索已创建的存储桶                                       |
| [查看历史版本或文件碎片](https://cloud.tencent.com/document/product/436/38103#viewfiles) | <li>支持在已开启版本控制的存储桶中，查看文件的历史版本<br><li>支持查看存储桶内的文件碎片详情           |
| [设置网络代理](https://cloud.tencent.com/document/product/436/38103#sets) | 支持设置网络代理来访问 COS                                   |
| [设置传输并发数](https://cloud.tencent.com/document/product/436/38103#sets) | 支持设置文件上传、下载的传输并发数                           |
| [设置传输分块数](https://cloud.tencent.com/document/product/436/38103#sets) | 支持设置文件分块上传、下载的分块数                           |
| [设置传输失败重试数](https://cloud.tencent.com/document/product/436/38103#sets) | 支持设置文件上传、下载失败时的重试次数                       |
| [设置上传二次校验](https://cloud.tencent.com/document/product/436/38103#sets) | 支持对上传至存储桶中的文件进行二次校验                       |
| [设置单线程限速](https://cloud.tencent.com/document/product/436/38103#sets) | 支持设置单线程上传限速和下载限速 |
| [查看本地日志](https://cloud.tencent.com/document/product/436/38103#sets) | 支持将用户对 COSBrowser 的操作记录以本地日志的形式保存       |

## 移动端功能列表

COSBrowser 移动端注重对资源的查看及监控，用户可以随时随地监控 COS 的存储量、流量等数据。关于 COSBrowser 移动端所支持的功能，请参见 [移动端功能列表](https://cloud.tencent.com/document/product/436/38105)。

## 更新日志

- 桌面端更新日志：[changelog](https://github.com/tencentyun/cosbrowser/blob/master/changelog.md)。
- 移动端更新日志：[changelog_mobile](https://github.com/tencentyun/cosbrowser/blob/master/changelog_mobile.md)。

## 反馈和建议

如您在使用 COSBrowser 时有任何疑问或建议，欢迎反馈给我们：

- 桌面端反馈：[issues](https://github.com/tencentyun/cosbrowser/issues)。
- 移动端反馈：[issues_mobile](https://support.qq.com/embed/phone/67467)。
