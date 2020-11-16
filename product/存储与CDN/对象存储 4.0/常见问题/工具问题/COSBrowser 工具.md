### 什么是 COSBrowser 工具？

COSBrowser 是腾讯云对象存储 COS 推出的可视化界面工具，让您可以使用更简单的交互轻松实现对 COS 资源的查看、传输和管理。目前 COSBrowser 提供桌面端（Windows、macOS、Linux）和移动端（Android、iOS），详细介绍请参见 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)。


### 如何下载 COSBrowser 工具?

下载地址和使用说明请参见 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)。


### 子账号登录 COSBrowser，为什么不显示存储路径？

1. 请确认子账号是否有访问 COS 的相关权限，相关文档可参见 [授权子账号访问 COS](https://cloud.tencent.com/document/product/436/11714)。
2. 若子账号只有某个存储桶或存储桶下某个目录的权限，则子账号在登录 COSBrowser 工具时，需要手动添加存储路径和选择存储桶所在的地域。存储格式路径为 Bucket 或 Bucket/Object-prefix，例如 examplebucket-1250000000。
![](https://main.qcloudimg.com/raw/22a255293a563599d7fb8edecd9ef346.jpg)


### 如何提高大量文件情况下的传输速度？

以 Windows 版本 COSBrowser 工具为例，可进入【高级设置】，调整【上传】、【下载】的文件并发数和分块数来提高传输速度。
![](https://main.qcloudimg.com/raw/ad8be3a2089d5af1734b4784d546cfdb.jpg)


### 系统是 macOS，当 COSBrowser 弹出提示“更新失败，权限被拒绝”该如何处理？
![](https://main.qcloudimg.com/raw/92e858abfde48fd0738459bd31c8da7f.png)

**出错原因**
在`/Users/username/Library/Caches/`目录下，有`com.tencent.cosbrowser`和`com.tencent.cosbrowser.ShipIt`两个文件。当这两个文件的所有者分别为 root 用户和 user 用户时，会因为权限问题导致更新失败。

**解决方法**
在 Mac 的终端中执行以下命令行：
```plaintext
sudo chown $USER ~/Library/Caches/com.tencent.cosbrowser.ShipIt/
```

### 如果弹出错误  “no such file or directory, stat 'C:\Users\XXX\AppData\Local\Temp\cosbrowser\logs\cosbrowser.log'” 并且应用无法使用怎么办？

![](https://main.qcloudimg.com/raw/42629a0686b7a892fef8946e547c9ef6.png)

**解决方法**：建议下载版本 2.1.x 以上的版本。

### 在执行 cosbrowser.exe 安装包过程中出现安装中止，怎么办？

**出错原因**
这是由于之前安装过 COSBrowser，在系统中已存在这个应用，而后面手动删除应用但是没有清除系统痕迹，再次执行安装时，程序发现了有遗留痕迹却又没有实际的应用，便会中止安装。

**解决办法**
手动清除或使用一些清理工具（例如腾讯安全管家中的软件管理）去卸载清除 COSBrowser 应用的安装痕迹。

