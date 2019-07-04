本文将指导您完成在 iOS 端下实时音视频客户端功能的 SDK 集成。
 ## 源码下载
 在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
 [Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_import.zip)
## 操作步骤
### 创建 iOS 工程
> 如果您已经有一个工程待集成，请直接跳到下一步[ 集成 SDK](#.E9.9B.86.E6.88.90-sdk)。

首先，使用 Xcode 创建一个新的工程用来集成我们的 SDK。
打开 Xcode，【 File 】-【 New 】-【 Project 】：
<img src="https://main.qcloudimg.com/raw/145fb381bfa9b5752fb78618a1801c48.png"/>

选择【 Signle View App 】

<img src="https://main.qcloudimg.com/raw/9a73593d5b7749bbb5bbbdc7b0720202.png" width = "730" height = "476"/><br>

设置工程名为 Demo01\_集成 SDK，语言选择为 Objective-C，Team、Organization Name 和 Organization Identifier 根据自身情况填写（也可随便填写）,然后选择下一步选择项目存放地址，单击 【 create 】即可 。

### 集成 SDK

#### 获取SDK

>ILiveSDK 其实是一套SDK的集合，其中包含了以下一些子 SDK：
> - BeautySDK：提供美颜预处理功能
> - IMSDK：提供 IM 即时通讯功能
> - AVSDK：提供底层音视频功能
> - ILiveSDK：在 AVSDK 基础上封装而成，提供更简单易用的音视频功能接口
> - TILLiveSDK：在 ILiveSDK 的基础上，针对直播场景相关接口进行的封装，方便快速实现直播相关功能

我们先在工程目录中新建一个名为 ILiveSDK 的文件夹，用来存放我们的 SDK，由于 ILiveSDK 包含若干个子 SDK，所以我们提供了一个 [SDK 下载脚本](https://github.com/zhaoyang21cn/iLiveSDK_iOS_Suixinbo/blob/master/suixinbo/Frameworks/LoadSDK.sh)方便获取所有的SDK。

单击下载脚本，将其放置于刚才创建的 ILiveSDK 文件夹下：

![输入图片说明](https://gitee.com/uploads/images/2018/0327/142610_5af5b739_1839574.png "在这里输入图片标题")

运行下载脚本（ 打开终端，cd 命令进入 Frameworks 目录下，运行命令 `sh LoadSDK.sh` ），就会自动下载所有SDK，下载完成之后会自动解压，并删除下载的压缩包，稍等片刻即可，解压完成之后文件目录如下：

![输入图片说明](https://gitee.com/uploads/images/2018/0327/144510_f76b525e_1839574.png "在这里输入图片标题")

[最新版本说明](https://github.com/zhaoyang21cn/iLiveSDK_iOS_Suixinbo)

#### 导入SDK
下载完成后，我们需将 SDK 导入工程，在工程根目录上单击右键->【 Add Files to "Demo01\_集成SDK" 】：

![输入图片说明](https://gitee.com/uploads/images/2018/0327/153534_7f4c7553_1839574.png "在这里输入图片标题")

在弹出的目录选择框中选择我们刚刚创建的【 ILiveSDK 文件夹 】->【 Add 】：

![输入图片说明](https://gitee.com/uploads/images/2018/0327/145257_16ed9532_1839574.png "在这里输入图片标题")

添加完成后的工程目录：

![输入图片说明](https://gitee.com/uploads/images/2018/0327/145423_13d923dd_1839574.png "在这里输入图片标题")
　　

#### 添加系统依赖库

ILiveSDK 中的 SDK 依赖了一些系统库，我们还需要将这些系统库添加到项目中来。

单击【 项目文件 】-【 targets 】-【 Genaeral 】- 拉到最下面的 Linked Frameworks and Libraries 区域 - 单击【 + 】号 - 输入系统库名称 - 单击【 add 】添加。

![输入图片说明](https://gitee.com/uploads/images/2018/0327/150647_c34068ff_1839574.png "在这里输入图片标题")

|需添加的系统库清单|
|---|
|Accelerate.framework|
|AssetsLibrary.framework|
|AVFoundation.framework|
|CoreGraphics.framework|
|CoreMedia.framework|
|CoreTelephony.framework|
|CoreVideo.framework|
|ImageIO.framework|
|JavaScriptCore.framework|
|OpenAL.framework|
|OpenGLES.framework|
|QuartzCore.framework|
|SystemConfiguration.framework|
|VideoToolbox.framework|
|libbz2.tbd|
|libc++.tbd|
|libiconv.tbd|
|libicucore.tbd|
|libprotobuf.tbd|
|libresolv.tbd|
|libsqlite3.tbd|
|libstdc++.6.tbd|
|libstdc++.tbd|
|libz.tbd|

添加系统库后，项目中会多出一个 Frameworks 文件夹，里面放的就是我们添加的系统库，由于需要添加的系统库较多，一个方便的方法是，直接在文末下载我们给出的 Demo 代码（[单击下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_import.zip)），将其中的系统库直接拖拽到您的工程中（ 从 Frameworks 文件夹直接拖到您的项目的 Linked Frameworks and Libraries 区域 ）。


#### 工程配置

为了能够正常使用 SDK，还需要进行一些工程配置：

1. -ObjC 配置
【 Build Settings 】 -> 【 Other Linker Flags 】 -> 【 -ObjC （注意大小写）】：
![输入图片说明](https://gitee.com/uploads/images/2018/0327/151817_09a88486_1839574.png "在这里输入图片标题")

2. Bitcode 配置
【 Build Settings 】 ->【 Enable Bitcode 】 -> 【 NO（设置为 NO）】：
![输入图片说明](https://gitee.com/uploads/images/2018/0327/151840_ca903f1e_1839574.png "在这里输入图片标题")

### 运行检查

如果以上步骤均无错误，这时我们就能正常使用 ILiveSDK 了，在 ViewController.m 的  viewDidLoad 函数中添加获取版本号的代码：
```
//导入头文件
#import <ILiveSDK/ILiveCoreHeader.h>
```

```
//获取版本号
NSLog(@"ILiveSDK version:%@",[[ILiveSDK getInstance] getVersion]);
NSLog(@"AVSDK version:%@",[QAVContext getVersion]);
NSLog(@"IMSDK version:%@",[[TIMManager sharedInstance] GetVersion]);
```

```
//打印结果
2018-03-27 15:22:37.187181+0800 Demo01_集成SDK[8182:16625633] ILiveSDK version:1.8.3.13017
2018-03-27 15:22:37.187692+0800 Demo01_集成SDK[8182:16625633] AVSDK version:1.9.6.47.OpenSDK_1.9.6- 34109
2018-03-27 15:22:37.189444+0800 Demo01_集成SDK[8182:16625633] IMSDK version:v2.5.6.11389.11327
```

恭喜，至此说明`ILiveSDK`已经成功集成。
