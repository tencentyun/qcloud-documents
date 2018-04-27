
## 短视频licence集成
- 获取到短视频基础版 SDK License 后，需要重命名为 TXUgcSDK.licence， 然后将重命名后的 licence 链接到 Xcode 工程中，当您的 licence 过期了，可以登录腾讯云点播控制台获取最新的 licence，替换您应用中的 licence 即可。
- 需要注意的是：licence 名称为 “TXUgcSDK.licence” ， licence 被链接进了 Xcode 工程，保证 SDK 内部能读取到 licence 信息。

## Xcode 工程设置

### 支持平台

+ SDK 支持 iOS 8.0 以上系统

### 开发环境

+ Xcode 9 或更高版本
+ OS X 10.10 或更高版本

### Xcode工程设置

下面通过一个简单的 iOS Application 工程，说明如和在 Xcode 工程中配置 SDK。

#### 拷贝 SDK 文件

在本例中，新建一个名字叫做 HelloSDK 的 iOS 工程，将下载下来的 `TXLiteAVSDK_UGC.framework` 拷贝至工程目录。目录结构如下图所示：
![](//mc.qcloudimg.com/static/img/d2b95540742662c006039adabb44188a/RTX20170811-210804.png)

#### 添加 Framework

在工程中添加 `TXLiteAVSDK_UGC.framework`，同时还要添加以下系统依赖库：

> 1. libz.tbd
> 2. Accelerate.framework
> 3. Bugly.framework

所有系统依赖库添加完毕，工程依赖如下图所示：
![](//mc.qcloudimg.com/static/img/98f026d48d92df36eaa23f8304b84eaf/image.png)

#### 添加头文件
在 Build Settings->Search Paths->User Header Search Paths 中添加头文件搜索路径。注意此项不是必须的，如果您没有添加 TXLiteAVSDK_UGC 的头文件搜索路径，则在引用 SDK 的相关头文件时，需要在头文件前增加 "TXLiteAVSDK_UGC/"，如下所示：

```	objc
#import "TXLiteAVSDK_UGC/TXUGCRecord.h"
```

#### 短视频发布功能集成

短视频发布功能以源码形式对外提供，您需要手动集成源代码到您的工程中。

- 拷贝上传源代码目录 Demo/TXLiteAVDemo/VideoUpload 到您的工程目录中。

- 将VideoUpload目录拖拽到xcode工程中的合适位置，在弹出的对话框中选择Added floders:Create groups，选择添加到的target，然后点finish。
![](https://main.qcloudimg.com/raw/39a08faa6d2d98049c894ba8a2d371d5.png)

- 添加如下系统库

> 1. CoreTelephony
> 2. Foundation
> 3. SystemConfiguration
> 4. libstdc++.tbd

#### 添加 -ObjC
SDK 用到了一些类别的方法，加载类别方法需要在工程配置：Build Settings -> Linking -> Other Linker Flags 添加 -ObjC ，否则在程序运行的过程中可能因为找不到类别方法而报错。

 
#### 验证
下面在 HelloSDK 的代码中，调用 SDK 的接口，获取 SDK 版本信息，以验证工程设置是否正确。

##### 引用头文件

在 ViewController.m 开头引用 SDK 的头文件：

```	objc
#import "TXLiteAVSDK_UGC/TXLiveBase.h"
```

#### 添加调用代码

在 viewDidLoad 方法中添加代码：

```	objc
- (void)viewDidLoad {
    [super viewDidLoad];
    // 打印SDK的版本信息
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
```

#### 编译运行

如果前面各个步骤都操作正确的话，HelloSDK 工程就可以顺利编译通过。在 Debug 模式下运行APP，Xcode 的 Console 窗格会打印出 SDK 的版本信息。

> 2017-09-26 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 3.4.1761 

至此，工程配置完成。

## LOG 打印
在  TXLiveBase 中可以设置 log 是否在控制台打印以及 log 的级别，具体代码如下：
- **setConsoleEnabled**
设置是否在 xcode 的控制台打印 SDK 的相关输出。

- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到当前 App 的 **Documents/logs** 文件夹下。
如果您需要我们的技术支持，建议将次开关打开，在重现问题后提供 log 文件，非常感谢您的支持。

- **Log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。

```	objc
[TXLiveBase setConsoleEnabled:YES];
[TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```
