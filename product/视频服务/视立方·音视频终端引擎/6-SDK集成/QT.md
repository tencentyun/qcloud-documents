本文主要介绍如何快速地在 QT 端将腾讯云视立方 SDK 集成到您的项目中，腾讯云视立方 SDK QT 端仅**音视频通话 TRTC 版本**支持。按照如下步骤进行配置，就可以完成 SDK 在 QT 端的集成工作。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | - | - | - | &#10003; | - | - |
| SDK 下载 <div style="width: 90px"/>  | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。


## Mac 端集成
### 开发环境要求

- 操作系统：Mac10.10及以上版本。
- 开发环境：Qt Creator 4.10.3及以上版本，推荐使用 Qt Creator 4.13.3及以上。
- 开发框架：Based on Qt 5.10及以上。

### 操作步骤
本节以从0创建一个简单的 QTTest 项目为例，介绍如何在 Qt Creator 工程中集成 C++ 跨平台 SDK。

[](id:mac_step1)
#### 步骤1：下载 C++ 跨平台 SDK
1. 下载 [SDK](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Mac_latest.tar.bz2)，解压并打开文件。
2. 在您的QTTest同级目录下新建一个空的SDK文件夹，将第1步下载的`TXLiteAVSDKTRTCMacx.x.x/SDK/TXLiteAVSDKTRTC_Mac.framework` 拷贝到与您 QTTest 工程目录同级目录的 SDK 文件夹下。

[](id:mac_step2)
#### 步骤2：配置 QTTest.pro
打开 QTTest 工程目录，使用一任意文本编辑器打开 `QTTest.pro` 文件，然后添加 SDK 相关引用：

<dx-codeblock>
::: mac
INCLUDEPATH += $$PWD/.
DEPENDPATH += $$PWD/.

LIBS += "-F$$PWD/base/util/mac/usersig"
LIBS += "-F$$PWD/../SDK"
LIBS += -framework TXLiteAVSDK_TRTC_Mac
LIBS += -framework Accelerate
LIBS += -framework AudioUnit

INCLUDEPATH += $$PWD/../SDK/TXLiteAVSDK_TRTC_Mac.framework/Headers/cpp_interface

INCLUDEPATH += $$PWD/base/util/mac/usersig/include
DEPENDPATH += $$PWD/base/util/mac/usersig/include
:::
</dx-codeblock>

[](id:mac_step3)
#### 步骤3：授权摄像头和麦克风使用权限

因为 SDK 会使用您的摄像头和麦克风，所以您需要在对应的 `Info.plist` 添加对应的权限申请说明：
```none
NSMicrophoneUsageDescription : 申请使用麦克风
NSCameraUsageDescription : 申请使用摄像头
```
如下图所示：
![](https://main.qcloudimg.com/raw/eac2455042c11db8ce3de49920fa18c1.png)

[](id:mac_step4)
#### 步骤4：引用腾讯云视立方 TRTC SDK
1. 您可以通过头文件 `#include "ITRTCCloud.h"` 直接引用。
2. 使用命名空间：C++ 全平台接口的方法、类型等均定义在 trtc 命名空间中，为了让代码更加简洁，建议您直接使用 trtc 命名空间。

>? 至此您的集成工作已经完成，可以编译运行您的项目了。关于更多跨平台 SDK 的 API 使用 Demo，请下载 [QTDemo](https://github.com/tencentyun/TRTCSDK/tree/master/Mac) 详细参考。

## Windows 端集成
### 开发环境要求
- 操作系统：Windows 7及以上版本。
- 开发环境：Visual Studio 2015及以上版本，推荐使用 Visual Studio 2015，前提是您已经配置好 VS 相关的 QT 开发环境。
>? 如果您不熟悉配置 VS 相关 QT 开发环境的步骤，请参见 [README](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/QTDemo/README.md) 中的第2条内容。

### 操作步骤
本节以创建一个简单的 QTTest 项目为例，介绍如何在 Visual Studio 工程中集成 C++ 跨平台SDK。

[](id:win_step1)
#### 步骤1：下载 C++ 跨平台 SDK
1. 下载 [SDK](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_latest.zip)，解压并打开文件。
2. 您的 QTTest 同级目录下新建一个空的SDK文件夹，将第1步下载的 `TXLiteAVSDKTRTCWin_latest/SDK/CPlusPlus` 拷贝到与您 QTTest 工程目录同级目录的 SDK 文件夹下。

[](id:win_step2)
#### 步骤2：配置 QTTest 工程依赖环境
<dx-tabs>
:::  场景一：使用QtCreator配置依赖环境
打开 QTTest工程目录，使用一款任意文本编辑器（推荐 [Sublime Text](http://www.sublimetext.com/3)）打开 `QTTest.pro`（使用 Qt Creator 创建）文件，然后添加 SDK 相关引用：
<dx-codeblock>
::: windows 
INCLUDEPATH += $$PWD/.
               $$PWD/../SDK/CPlusPlus/Win32/include \
               $$PWD/../SDK/CPlusPlus/Win32/include/TRTC

DEPENDPATH += $$PWD/.
               $$PWD/../SDK/CPlusPlus/Win32/include \
               $$PWD/../SDK/CPlusPlus/Win32/include/TRTC

CONFIG += opengl
CONFIG += debug_and_release

debug {
	contains(QT_ARCH,i386) {
		LIBS += -L$$PWD/../SDK/CPlusPlus/Win32/lib -lliteav
	} else {
		LIBS += -L$$PWD/../SDK/CPlusPlus/Win64/lib -lliteav
	}
}

release {
	contains(QT_ARCH,i386) {
		LIBS += -L$$PWD/../SDK/CPlusPlus/Win32/lib -lliteav
	} else {
		LIBS += -L$$PWD/../SDK/CPlusPlus/Win64/lib -lliteav
	}
}
:::
</dx-codeblock>
:::
::: 场景二：使用VS配置依赖环境
如果您的工程已经是一个成熟的 VS 项目，您也可以在 VS 中的工程属性 `Properties->Linker->Input 和 General` 配置 SDK 库路径依赖信息，同时在 `Properties -> C/C++ -> General` 设置好 SDK 的头文件路径依赖信息。
:::
</dx-tabs>

[](id:win_step3)
#### 步骤3：拷贝文件
当使用 VS 打开 `QTTest.pro` 工程并自动生成相关的 `debug/release` 文件夹后，您需要将 `SDK/CPlusPlus/Win32/lib` 下的所有的 `.dll` 文件分别拷贝到工程目录下的 `debug/release` 文件夹下。

[](id:win_step4)
#### 步骤4：引用 TRTC SDK
1. 您可以通过头文件 `#include "ITRTCCloud.h"` 直接引用。
2. 使用命名空间：C++ 全平台接口的方法、类型等均定义在 trtc 命名空间中，为了让代码更加简洁，建议您直接使用 trtc 命名空间。

>? 至此您的集成工作已经完成，可以编译运行您的项目了。关于更多跨平台 SDK 的 API 使用 Demo，请下载 [QTDemo](https://github.com/tencentyun/TRTCSDK/tree/master/Windows) 详细参考。
