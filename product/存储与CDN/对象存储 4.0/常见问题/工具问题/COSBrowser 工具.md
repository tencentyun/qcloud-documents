### 什么是 COSBrowser 工具？

COSBrowser 是腾讯云对象存储 COS 推出的可视化界面工具，让您可以使用更简单的交互轻松实现对 COS 资源的查看、传输和管理。目前 COSBrowser 提供桌面端（Windows、macOS、Linux）和移动端（Android、iOS），详细介绍请参见 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)。


### 如何下载 COSBrowser 工具?

下载地址和使用说明请参见 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366) 。


### 子账号登录 COSBrowser，为什么不显示存储路径？

1. 请确认子账号是否有访问 COS 的相关权限，相关文档可参见 [授权子账号访问 COS](https://cloud.tencent.com/document/product/436/11714)。
2. 若子账号只有某个存储桶或存储桶下某个目录的权限，则子账号在登录 COSBrowser 工具时，需要手动添加存储路径和选择存储桶所在的地域。存储格式路径为 Bucket 或 Bucket/Object-prefix，例如 examplebucket-1250000000。
![](https://main.qcloudimg.com/raw/22a255293a563599d7fb8edecd9ef346.jpg)


### 如何提高大量文件情况下的传输速度？

以 Windows COSBrowser 工具为例，可进入【高级设置】，调整【上传】、【下载】的文件并发数和分块数来提高传输速度。
![](https://main.qcloudimg.com/raw/ad8be3a2089d5af1734b4784d546cfdb.jpg)
