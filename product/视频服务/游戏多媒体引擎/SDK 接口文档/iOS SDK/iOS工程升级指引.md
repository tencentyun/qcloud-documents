# GME 2.9 版本 iOS 工程升级指引

将GME升级到 2.9 版本，需要在工程中做以下几个步骤：

### 1. 新版本SDK变化

新版本中将SDK进行动态库拆分，多出以下几个文件：

- libgme_fdkaac.framework
- libgme_ogg.framework
- libgme_lamemp3.framework
- libgme_soundtouch.framework

确保下载下来的 SDK 中包含这几个文件。下载后与 GMESDK.framework 放与工程目录下。Release-iphoneos 为真机使用的SDK文件，Release-iphonesimulator 为模拟器使用的SDK文件。

![](https://qcloudimg.tencent-cloud.cn/raw/b31614d427f232785e14d3d75da301a2.png)

### 2. 工程导入SDK

在工程中导入所有的framework。如下图所示。

![](https://qcloudimg.tencent-cloud.cn/raw/28bef4b06f862d20e2c8b72704f4b9c5.png)

### 3. 设置 framework 并签名

在xcode工程中，点击 Build Phases，将 Link Binary With Libraries 展开，将GME的所有 framework 导入。

将 Embed Framework 展开，将GME的所有 framework 导入，勾选 Code Sign On Copy。

![](https://qcloudimg.tencent-cloud.cn/raw/78ad024d8ec040d792264e7eb686181b.png)

### 4. rpath改动

需要在 rpath 增加 @executable_path/Frameworks。如果已经增加，便无需再修改。

![](https://qcloudimg.tencent-cloud.cn/raw/33567fe51c50e1855bebd34647963600.png)