## 操作场景

GME iOS SDK 已升级到2.9版本，如果您将 GME 升级到2.9版本，需要在工程中做以下几个步骤：



## 升级步骤

### 1. 下载 SDK 

新版本中将 SDK 进行动态库拆分，多出以下几个文件：

- libgmefdkaac.framework
- libgmeogg.framework
- libgmelamemp3.framework
- libgmesoundtouch.framework

确保下载下来的 SDK 中包含这几个文件。下载后与 GMESDK.framework 放与工程目录下。Release-iphoneos 为真机使用的SDK文件，Release-iphonesimulator 为模拟器使用的 SDK 文件。

![](https://qcloudimg.tencent-cloud.cn/raw/b31614d427f232785e14d3d75da301a2.png)


### 2. 工程导入 SDK

在工程中导入所有的 framework。如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/e786eb0a7a10f3052a88b75128c8ac1f.png)


### 3. 设置 framework 并签名

1. 在 xcode 工程中，单击 **Build Phases**，将 Link Binary With Libraries 展开，将 GME 的所有 framework 导入。
2. 将 Embed Framework 展开，将 GME 的所有 framework 导入，勾选 **Code Sign On Copy**。

![](https://qcloudimg.tencent-cloud.cn/raw/5088e0cbe90b9810379fcc35d1e58cda.png)


### 4. rpath 改动

需要在 rpath 增加 @executable_path/Frameworks。如果已经增加，便无需再修改。

![](https://qcloudimg.tencent-cloud.cn/raw/1c897166cdd706f7356058612e5062e8.png)
