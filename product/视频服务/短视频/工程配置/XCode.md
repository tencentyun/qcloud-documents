
## 短视频licence集成
- 获取到短视频基础版 SDK License后，需要重命名为TXUgcSDK.licence， 然后将重命名后的 licence 链接到 Xcode 工程中，当您的 licence 过期了，可以登录腾讯云点播控制台获取最新的licence，替换您应用中的licence即可。
- 需要注意的是：licence名称为“TXUgcSDK.licence” ， licence 被链接进了Xcode工程，保证SDK内部能读取到 licence 信息。

## Xcode工程设置

### 支持平台

+ SDK支持iOS 8.0以上系统

### 开发环境

+ Xcode 9或更高版本
+ OS X 10.10或更高版本

### Xcode工程设置

下面通过一个简单的iOS Application工程，说明如和在Xcode工程中配置SDK。

#### 拷贝SDK文件

在本例中，新建一个名字叫做HelloSDK的iOS工程，将下载下来的`TXLiteAVSDK_UGC.framework`拷贝至工程目录。目录结构如下图所示：

![](//mc.qcloudimg.com/static/img/d2b95540742662c006039adabb44188a/RTX20170811-210804.png)

#### 添加Framework

在工程中添加`TXLiteAVSDK_UGC.framework`，同时还要添加以下系统依赖库

> 1. libz.tbd
> 2. Accelerate.framework
> 3. Bugly.framework

所有添加完毕，工程依赖如下图所示：

![](//mc.qcloudimg.com/static/img/98f026d48d92df36eaa23f8304b84eaf/image.png)

#### 添加头文件
在Build Settings->Search Paths->User Header Search Paths中添加头文件搜索路径。注意此项不是必须的，如果您没有添加TXLiteAVSDK_UGC的头文件搜索路径，则在引用SDK的相关头文件时，需要在头文件前增加"TXLiteAVSDK_UGC/"，如下所示：

```	objc
#import "TXLiteAVSDK_UGC/TXUGCRecord.h"
```

#### 添加 -ObjC
SDK用到了一些类别的方法，加载类别方法需要在工程配置：Build Settings -> Linking -> Other Linker Flags 添加 -ObjC ，否则在程序运行的过程中可能因为找不到类别方法而报错

#### 验证

下面在HelloSDK的代码中，调用SDK的接口，获取SDK版本信息，以验证工程设置是否正确。

##### 引用头文件

在ViewController.m开头引用SDK的头文件：

```	objc
#import "TXLiteAVSDK_UGC/TXLiveBase.h"
```

#### 添加调用代码

在viewDidLoad方法中添加代码：

```	objc
- (void)viewDidLoad {
    [super viewDidLoad];
    // 打印SDK的版本信息
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
```

#### 编译运行

如果前面各个步骤都操作正确的话，HelloSDK工程应该可以顺利编译通过。在Debug模式下运行APP，Xcode的Console窗格会打印出SDK的版本信息。

> 2017-09-26 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 3.4.1761 

至此，工程配置完成。

## LOG打印
在  TXLiveBase 中可以设置 log 是否在控制台打印以及log的级别，具体代码如下：
- **setConsoleEnabled**
设置是否在 xcode 的控制台打印 SDK 的相关输出。

- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到当前App的 **Documents/logs** 文件夹下。
如果您需要我们的技术支持，建议将次开关打开，在重现问题后提供 log 文件，非常感谢您的支持。

- **Log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。

```	objc
[TXLiveBase setConsoleEnabled:YES];
[TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```