## SDK 目录及文件介绍

SDK 包含的主要目录和文件如下：

**bin**

这个目录存放了 SDK 的动态库(dll 文件)及运行所需的音视频参数配置文件，这些动态库分为 Debug 版和 Release 版。具体如下：

- 动态库：

qavsdk.dll：音视频引擎库。

AdvVideoDev.dll, IntelDec.dll, IntelEnc.dll, IntelUtil.dll, MediaEngine.dll, QQAudioHook.dll, QQAudioHookService.dll, TcHevcDec.dll, TcHevcEnc.dll, TcVpxDec.dll, TcVpxEnc.dll, TRAE.dll, VP8.dll, xPlatform.dll：
音视频引擎库所依赖的各个库。

libtim.dll：文本/图片的即时通信库，它包含账号登录/登出模块。

- 参数配置文件：

EngineCfg.ini, Udtcfg.ini：进行音视频通信所需的音视频参数配置文件。

**demo**

这个目录存放了 SDK demo。这个 Demo 主要是用来给客户体验基于该 SDK 的音视频通信效果及便于开发人员更快上手 SDK 开发，demo 里面包含 SDK 各个接口的使用示例。这个目录包含了 Demo 的源文件、emo 可执行文件、demo VS2010 工程等，详细如下：

- src：demo 源文件目录

SdkWrapper.cpp：SDK 接口封装源文件。该文件对 SDK 各个接口的简单封装，可以认为是 SDK 各个接口的使用示例文件。

DialogQAVSDKDemo.cpp：demo 主窗口源文件。demo 的主要代码均在此，包括如何调用 SDK 接口、如何处理 SDK 的事件等。

DialogAddAccount.cpp：添加测试账户源文件。为了便于体验，demo 提供了添加测试号的功能，这个文件的主要功能就在于此。

DialogAddAppConfig.cpp：添加 App 配置信息源文件。为了便于不同客户体验，demo 提供了添加各种音视频通信场景配置的功能，这个文件的主要功能就在于此。

ConfigInfoMgr.cpp：对 Demo 中用到的测试帐号、APP 配置等进行简单管理。

VideoRender.cpp：视频渲染的源文件，实现了简单的视频渲染功能。

其他源文件相对简单次要，这边就不做介绍。

- Debug/Release：运行 Demo VS2010 工程所生成的 Demo 可执行文件

QAVSDKDemo.exe 的存放目录。其中的 ConfigInfo.ini 文件存放了 Demo 所使用的测试帐号和 App 配置等信息。

- QAVSDKDemo.sln 和 QAVSDKDemo.vcxproj：demo 的 VS2010 工作空间和工程。


**doc**

这个目录存放了 SDK 开发和使用相关文档，主要包括 SDK API 文档、SDK 集成开发文档和 SDK 开发入门文档等。

**include**

这个目录存放了 SDK 头文件，其中 timsdk 目录下存放的是文本/图片的即时通信库 libtim.dll 对应的头文件，其他头文件是音视频引擎库 qavsdk.dll 对应的头文件。开发人员在使用这两个库时，需要添加对应的头文件。

**lib**

存放 qavsdk.dll 和 libtim.dll 所对应的 lib 文件：qavsdk.lib 和 libtim.lib，分为 Debug 版和 Release 版。在使用 qavsdk.dll 和 libtim.dll 进行开发时，需要添加对应的 lib 文件，否则编译链接不会通过。

**sysdll**

存放运行 Demo 可执行文件 QAVSDKDemo.exe 所需的 Windows 系统库。对于一些 Windows 电脑，没有这些库，就无法运行 QAVSDKDemo.exe，这边附带各个架构的系统库，

当运行 QAVSDKDemo.exe，如果提示缺少系统库，可以从这边获取对应架构的系统库放到 QAVSDKDemo.exe 所在目录，即可让 QAVSDKDemo.exe 正常运行。

## SDK 集成

**开发平台与集成开发环境**

开发平台：Windows 主流平台，Windows 7、Windows XP 等。

集成开发环境：VS2010(Visual Studio 2010)。目前仅支持使用 VS2010 来开发。

**开始集成**

下面开始介绍如何使用 VS2010 来新建一个工程并使用 SDK。

这边假设 SDK 存放在 D:\QAVSDK 目录下，并将新建的 VS2010 工程存放在 D:\QAVSDKDemoProj 目录下。如下图所示。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-1.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-2.png)

**a)新建 VS2010 工程**

打开 VS2010，新建一个 MFC Applicatin 工程，工程名为 QAVSDKDemo，存放在 D:\QAVSDKDemoProj\目录下。如下图所示。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-3.png)

**b)修改工程配置**

修改工程配置，这边以 Debug 版为例。

首先，在工程名上单击右键，选择 Properties，打开工程属性设置窗口。

接着，在 Configuration Properties\VC++ Directories\Include Directories 添加 SDK 头文件路径：D:\QAVSDK\include;D:\QAVSDK\include\timsdk;

然后，在 Configuration Properties\VC++ Directories\Library Directories 添加 SDK 库文件路径：D:\QAVSDK\libs\Debug;

最后，在 Configuration Properties\Linker\Input\Additional Dependencies 添加链接时依赖的 lib 文件：qavsdk.lib;libtim.lib。

如下图所示。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-4.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-5.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-6.png)



**c)开始写代码**

写代码时，为了使用 SDK 所提供接口，需要在代码中引用 SDK 的头文件及命名空间，如下：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-7.png)

然后，就可以开始使用 SDK 进行开发了。具体如何使用 SDK 所提供的每个接口，请参考我们提供的 Demo 源程序及相关文档，在这边就不做细说了。

**d)运行**

运行时，可执行程序需要用到 SDK 的动态库 dll 文件和音视频参数配置文件，请将 D:\QAVSDK\bin\目录下 Debug 版或 Release 版的所有 dll 文件和配置文件复制到可执行程序所在目录，即可运行它。如下图所示。 

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-8.png)

## 开发者文档

详情参考[音视频通信开发指南](http://cloud.tencent.com/wiki/%E9%9F%B3%E8%A7%86%E9%A2%91%E9%80%9A%E4%BF%A1%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)