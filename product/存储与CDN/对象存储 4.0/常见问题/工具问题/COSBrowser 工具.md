### 什么是 COSBrowser 工具？

COSBrowser 是腾讯云对象存储 COS 推出的可视化界面工具，让您可以使用更简单的交互轻松实现对 COS 资源的查看、传输和管理。目前 COSBrowser 提供桌面端（Windows、macOS、Linux）和移动端（Android、iOS），详细介绍请参见 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)。


### 如何下载 COSBrowser 工具?

下载地址和使用说明请参见 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)。

### 如何登录 COSBrowser？

详细介绍可查看 [桌面端使用说明](https://cloud.tencent.com/document/product/436/38103) 或 [移动端使用说明](https://cloud.tencent.com/document/product/436/38105) 文档。

**桌面端登录**

COSBrowser 桌面端仅支持通过云 API 密钥进行登录使用。

参数说明：

1. API 密钥 **secretID** 和 **secretKey** ：通过访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取，成功登录后密钥将保存在历史密钥中，方便下次继续使用。
![](https://main.qcloudimg.com/raw/86bb9584670fa11656b80e8d91c5267b.png)
2. 存储桶/访问路径：使用主账号登录时可不填写，若使用子账号登录需填写已授权的路径。例如：`example-1250000000/test/`。
>!COSBrowser 不支持使用项目密钥进行登录。

**移动端登录**
COSBrowser 移动端支持以下三种登录方式：

- **微信快捷登录**：通过微信创建或关联了指定微信的腾讯云账号，可以使用微信快捷登录方式快速登录 COSBrowser。
- **邮箱登录**：通过邮箱创建或关联了指定邮箱的腾讯云账号，可以通过输入邮箱账号密码进行登录。
- **永久密钥登录**：用户可使用云 API 密钥 SecretId 和 SecretKey（不支持项目密钥）进行登录，该密钥可在访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取，登录后将永久保持该账号的登录状态。

>?
- 若用户的腾讯云账号为 QQ 帐号所创建的，同样可使用微信快捷登录方式登录，只需在跳转的微信小程序界面选择 QQ 登录即可。
- 子账号用户可以使用密钥或微信快捷登录方式登录，选择微信登录只需在跳转的微信小程序界面选择子账号即可。

了解更多详情内容，可参考 [COSBrowser 简介](https://cloud.tencent.com/document/product/436/11366)。

### 子账号登录 COSBrowser，为什么不显示存储路径？

1. 请确认子账号是否有访问 COS 的相关权限，相关文档可参见 [授权子账号访问 COS](https://cloud.tencent.com/document/product/436/11714)。
2. 若子账号只有某个存储桶或存储桶下某个目录的权限，则子账号在登录 COSBrowser 工具时，需要手动添加存储路径和选择存储桶所在的地域。存储格式路径为 Bucket 或 Bucket/Object-prefix，例如 examplebucket-1250000000。
   ![](https://main.qcloudimg.com/raw/22a255293a563599d7fb8edecd9ef346.jpg)

### COSBrowser 工具支持使用临时密钥登录吗？

不支持临时密钥登录。

### COSBrowser 工具体验版如何进入？

如需体验 COSBrowser 您可以单击 [活动](https://cloud.tencent.com/act/event/cosbrowser-trial?) 进入体验页面。

**体验须知**

**应用体验规则：**

- 进入应用的体验版本后，COSBrowser 会自动生成临时账号并登录，临时账号为一次性使用，退出后将自动注销并抹除所有数据。
- 临时账号的有效期为 24 小时，到期后如需继续体验，请在本页面重新点击体验。

**应用体验限制：**

体验版本仅提供了基本的数据管理能力，例如上传文件、下载文件、分享链接等。如需体验更多功能，请使用个人账号登录，可参阅 [COSBrowser 快速入门](https://cloud.tencent.com/document/product/436/40762) 文档进一步了解。

### CentOS 图形界面双击无法启动 COSBrowser 客户端？

可以通过在终端运行 `./cosbrowser.AppImage --no-sandbox` 命令启动客户端。

### 安装 COSBrowser 工具有系统要求吗？

目前 COSBrowser 有桌面端和移动端两种：

**桌面端**

- **Windows 系统要求**：Windows 7 32/64位以上、Windows Server 2008 R2 64位以上
- **macOS 系统要求**：macOS 10.13以上
- **Linux 系统要求**：需带有图形界面并支持 AppImage 格式


**移动端**

- **Android 系统要求**：Android 4.4以上	
- **iOS 系统要求**：iOS 11以上

下载地址及更多详情可参考 [COSBrowser 下载地址 ](https://cloud.tencent.com/document/product/436/11366#.E4.B8.8B.E8.BD.BD.E5.9C.B0.E5.9D.80)。

### COSBrowser 文件同步功能

可以通过 COSBrowser 桌面版**文件同步功能**，将指定本地文件夹中的文件自动实时地上传至存储桶中。详细操作请参见 [桌面端使用说明](https://cloud.tencent.com/document/product/436/38103#.E5.9F.BA.E6.9C.AC.E5.8A.9F.E8.83.BD) 中的文件同步功能。

### COSBrowser 的文件列表预览图能否直接一次性看到所有预览图？

COSBrowser 暂不支持直接预览所有文件。

### COSBrowser 手机端显示存储桶列表为什么只有三个？

COSBrowser 手机端的总览页默认显示三个存储桶列表的展示，您可以下滑总览页查看更多存储桶列表。

### COSBrowser 工具能不能直接上传对象为低频存储类型？

COSBrowser 默认上传为标准存储类型，您可以在上传对象时手动选择存储类型和访问权限。

### 如何提高大量文件情况下的传输速度？

以 Windows 版本 COSBrowser 工具为例，可进入【高级设置】，调整【上传】、【下载】的文件并发数和分块数来提高传输速度。
![](https://main.qcloudimg.com/raw/c2feed3f86f3d91854bb6840c6eeb26f.png)

### COSBrowser 怎么复制文件的链接？

通过以下方式复制文件链接：
1. 在文件列表中选择文件，右键单击【复制链接】，打开【自定义复制链接】窗口。
2. 在文件列表中单击【详情】，打开【文件详情】窗口，直接复制“对象地址”或“创建临时链接”，如下图。

![](https://main.qcloudimg.com/raw/3e83d732a69d2d5c50cca080ce133ea5.png)

>?
- 若文件为公有读权限，可以使用不带签名的链接即“对象地址”进行访问，且对象地址永久有效。
- 若文件为私有读权限，必须使用带有签名的链接才可访问，您可以在【自定义复制链接】窗口中自定义链接有效期，默认有效时间为2小时。


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

### 在执行 cosbrowser.exe 安装包过程中出现安装中止，该如何处理？

**出错原因**
这是由于之前安装过 COSBrowser，在系统中已存在这个应用，而后面手动删除应用但是没有清除系统痕迹，再次执行安装时，程序发现了有遗留痕迹却又没有实际的应用，便会中止安装。

**解决办法**
手动清除或使用一些清理工具（例如腾讯安全管家中的软件管理）去卸载清除 COSBrowser 应用的安装痕迹。

### COSBrowser 工具进入文件列表时提示域名解析出错，该如何处理？

此报错为域名解析的问题，您本地网络偶现无法解析 COS 域名，建议您可以更换本地 DNS 为 114.114.114.114 等公共 DNS 重试一下，或者更换网络环境测试。
