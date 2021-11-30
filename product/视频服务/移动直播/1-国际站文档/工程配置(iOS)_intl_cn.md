## SDK信息

您可以在腾讯云官网更新 [直播SDK](https://cloud.tencent.com/document/product/454/7873)，目前直播SDK有如下几下版本：

| 版本类型   | 功能                           |
| ------ | ---------------------------- |
| 直播精简版  | 支持推流、直播、点播                   |
| 独立播放器版 | 支持直播、点播                      |
| 短视频功能版 | 支持短视频和点播                     |
| 全功能专业版 | 支持推流、直播、点播、连麦、短视频            |
| 商用企业版  | 在全功能专业版基础上增加动效贴纸、美瞳瘦脸、绿幕抠图功能 |

以专业版为例，下载完的SDK解压后有以下几个部分：

![](//mc.qcloudimg.com/static/img/5ef04a5e101beea834813e58fc5115ec/androidzippkg.png)

| 文件名 | 说明 | 
|---------|---------|
| SDK | 包含 framework 的SDK目录| 
| Demo | 基于 framework 方式的简化 Demo，包含简单的 UI 界面和 SDK 的主要功能演示，使用xcode可以快速导入并体验。|
| iOS 开发包使用指引.pdf | 介绍SDK的基本功能 |

## Xcode工程设置

### 一、支持平台

+ SDK支持iOS 8.0以上系统

### 二、开发环境

+ Xcode 8或更高版本
+ OS X 10.10或更高版本

### 三、Xcode工程设置

下面通过一个简单的iOS Application工程，说明如和在Xcode工程中配置SDK。

### 1、拷贝SDK文件

在本例中，新建一个名字叫做HelloSDK的iOS工程，将下载下来的`TXLiteAVSDK_Professional.framework`拷贝至工程目录。目录结构如下图所示：

![](//mc.qcloudimg.com/static/img/d2b95540742662c006039adabb44188a/RTX20170811-210804.png)

### 2、添加Framework

在工程中添加`TXLiteAVSDK_Professional.framework`，同时还要添加以下系统依赖库

> 1. VideoToolbox.framework
> 2. SystemConfiguration.framework
> 3. CoreTelephony.framework
> 4. AVFoundation.framework
> 5. CoreMedia.framework
> 6. CoreGraphics.framework
> 7. libstdc++.tbd
> 8. libz.tbd
> 9. libiconv.tbd
> 10. libresolv.tbd

所有添加完毕，工程依赖如下图所示：

![](//mc.qcloudimg.com/static/img/0e012a7ab67e833eb33aec1e02f5d86b/image.jpg)

### 3、添加头文件
在Build Settings->Search Paths->User Header Search Paths中添加头文件搜索路径。注意此项不是必须的，如果您没有添加TXLiteAVSDK_Professional的头文件搜索路径，则在引用SDK的相关头文件时，需要在头文件前增加"TXLiteAVSDK_Professional/"，如下所示：
```
#import "TXLiteAVSDK_Professional/TXLivePush.h"
```

### 四、验证

下面在HelloSDK的代码中，调用SDK的接口，获取SDK版本信息，以验证工程设置是否正确。

### 1、引用头文件

在ViewController.m开头引用SDK的头文件：

```
#import "TXLiteAVSDK_Professional/TXLiveBase.h"
```

### 2、添加调用代码

在viewDidLoad方法中添加代码：

```
- (void)viewDidLoad {
    [super viewDidLoad];
    // 打印SDK的版本信息
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
```

### 3、编译运行

如果前面各个步骤都操作正确的话，HelloSDK工程应该可以顺利编译通过。在Debug模式下运行APP，Xcode的Console窗格会打印出SDK的版本信息。

> 2017-08-11 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 3.0.1185

至此，工程配置完成。

## LOG打印
在  TXLiveBase 中可以设置 log 是否在控制台打印以及log的级别，具体代码如下：
- **setConsoleEnabled**
设置是否在 xcode 的控制台打印 SDK 的相关输出。

- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到当前App的 **Documents/logs** 文件夹下。
如果您需要我们的技术支持，建议将次开关打开，在重现问题后提供 log 文件，非常感谢您的支持。

- **Log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。

```
[TXLiveBase setConsoleEnabled:YES];
[TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```
