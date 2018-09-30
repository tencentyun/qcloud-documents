
## 短视频 licence 集成
- 在 [控制台](https://console.cloud.tencent.com/video/license) 填写完信息后，会拿到 key 和 url，见下图。
  ![](https://main.qcloudimg.com/raw/59ccde1fa75b2903aeb7147f6538089c.png)
  在您的应用中使用短视频功能之前（建议在 AppDelegate 中）把拿到的 key 和 url 设置到下面接口中

```objc
[TXUGCBase setLicenceURL:url key:key];
```

- 您可以选择是否打包 licence 到应用中：如果不选择打包，SDK 第一次使用需要访问网络；如果选择打包，把 TXUgcSDK.licence（名称要正确）拷贝到 App 中即可。
- 当您的 licence 过期了，可以登录腾讯云点播控制台进行续费，SDK 会自动续期，不需要您的应用做任何操作。
- 如果您的 licence 校验失败，您可以调用下面代码查看 licence 信息是否填写错误。

```objc
NSLog(@"%@", [TXUGCBase getLicenceInfo]);
```

- 对于使用 4.7 版本 licence 的用户，如果您升级了 SDK 到 4.9 版本了，您可以登录控制台，单击下图的 **切换到新版License** 按钮生成对应的 key 和 url，按照上述操作集成即可。
  ![](https://main.qcloudimg.com/raw/71ab2d47c9a01b2f514210e54f2b82fc.png)


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

> 1. Accelerate.framework
> 2. SystemConfiguration.farmework
> 3. libstdc++.tbd
> 4. libsqlite3.tbd
> 5. libz.tbd

所有系统依赖库添加完毕，工程依赖如下图所示：    
![](https://main.qcloudimg.com/raw/a5fe16ca046a0aad84224e1ffa766a42.jpg)

#### 添加 -ObjC
SDK 用到了一些类别的方法，加载类别方法需要在工程配置：Build Settings -> Linking -> Other Linker Flags 添加 -ObjC ，否则在程序运行的过程中可能因为找不到类别方法而报错。

#### 引用头文件
在需要使用SDK的文件中引用SDK，如下所示：

- 5.0开始的SDK支持clang module, 可以直接使用@import来引入

  ```	objc
  @import TXLiteAVSDK_UGC;
  ```

- 5.0之前的版本SDK需要单独引用使用到的头文件，比如

  ``` objc
  #import <TXLiteAVSDK_UGC/TXUGCBase.h>
  ```


#### 短视频发布功能集成

短视频发布功能以源码形式对外提供，您需要手动集成源代码到您的工程中。

- 拷贝上传源代码目录 Demo/TXLiteAVDemo/VideoUpload 到您的工程目录中。

- 将 VideoUpload 目录拖拽到 xcode 工程中的合适位置，在弹出的对话框中选择 Added floders:Create groups，选择添加到的 target，然后单击 finish。
![](https://main.qcloudimg.com/raw/39a08faa6d2d98049c894ba8a2d371d5.png)

#### 验证
下面在 HelloSDK 的代码中，调用 SDK 的接口，获取 SDK 版本信息，以验证工程设置是否正确。

##### 引用头文件

在 ViewController.m 开头引用 SDK：

```	objc
@import TXLiteAVSDK_UGC；
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

如果前面各个步骤都操作正确的话，HelloSDK 工程就可以顺利编译通过。在 Debug 模式下运行 App，Xcode 的 Console 窗格会打印出 SDK 的版本信息。

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
