## 1. SDK Directories and Files

The directories and files contained in the SDK are as follows:

**bin**

This directory stores SDK dynamic libraries (dll files) and audio/video parameter configuration files required for the SDK to run. The dynamic libraries include two versions: Debug and Release. Details:

- Dynamic libraries:

qavsdk.dll: Audio/video engine library.

AdvVideoDev.dll, IntelDec.dll, IntelEnc.dll, IntelUtil.dll, MediaEngine.dll, QQAudioHook.dll, QQAudioHookService.dll, TcHevcDec.dll, TcHevcEnc.dll, TcVpxDec.dll, TcVpxEnc.dll, TRAE.dll, VP8.dll, xPlatform.dll:
The audio/video engine library depends on these libraries.

libtim.dll: IM library for text/images. It contains module for account login/logout.

- Parameter configuration files:

EngineCfg.ini, Udtcfg.ini: Audio/video parameter configuration files required for audio/video messaging.

**demo**

This directory stores the SDK demo. The demo is used for customers to try out the actual effects of audio/video messaging based on this SDK so that developers can get started with SDK development easier and faster. It contains usage examples of each SDK API. The directory contains demo source files, emo executable files, the demo VS2010 project, etc., as show below:

- src: Directory containing demo source files.

SdkWrapper.cpp: SDK API wrapper source file. The simple wrappers for SDK APIs in this file can be considered as usage examples for SDK APIs.

DialogQAVSDKDemo.cpp: Source file of demo main window. This contains key codes of the demo, including those on how to call SDK APIs and how to handle SDK events.

DialogAddAccount.cpp: Source file for adding test accounts. The demo allows adding test accounts for trail uses by users, and this file is used to adding such test accounts.

DialogAddAppConfig.cpp: Source file for adding App configuration information. The demo allows adding various audio/video messaging scenario configurations for trail uses by different users, and this file is used to adding such configurations.

ConfigInfoMgr.cpp: Allow a simple management for test accounts, App configurations and other information used in the demo.

VideoRender.cpp: Source file for rendering videos which provides simple video rendering features.

Other source files are less important and will not be discussed here.

- Debug/Release: Demo executable files generated when the demo VS2010 project is run.

Directory containing QAVSDKDemo.exe. The ConfigInfo.ini file contains information used in the demo such as test accounts and App configurations.

- QAVSDKDemo.sln and QAVSDKDemo.vcxproj: VS2010 workspace and project for the demo.


**doc**

This directory contains SDK development and usage-related documents, including documents on SDK APIs, SDK integrated development and how to get started with SDK development.

**include**

This directory contains SDK header files. Under the timsdk directory are the header files for the IM library "libtim.dll" of text/images. Other header files are used for audio/video engine library "qavsdk.dll". Developers need to add the header files when using the two libraries.

**lib**

This directory contains lib files for qavsdk.dll and libtim.dll: qavsdk.lib and libtim.lib (Debug and Release versions). Developers need to add corresponding lib files when using qavsdk.dll and libtim.dll for development. Otherwise compilation and linkage will fail.

**sysdll**

This directory contains Windows system libraries required for running the executable demo file QAVSDKDemo.exe. Some Windows PCs cannot run QAVSDKDemo.exe without these libraries. This directory provides system libraries for different architectures.

If you are prompted that system library is missing when attempting to run QAVSDKDemo.exe, you can acquire the system library for the relevant architecture from this directory and place it under the directory where QAVSDKDemo.exe is located to make QAVSDKDemo.exe run normally.

## SDK Integration

**Development Platform and Integrated Development Environment**

Development platform: Mainstream Windows platforms such as Windows 7, Windows XP.

Integrated development environment: VS2010 (Visual Studio 2010). Currently you can only use VS2010 for development.

**Start Integration**

The following shows how to use VS2010 to create a new project and use the SDK.

We assume that the SDK is stored under D:\QAVSDK, and the new VS2010 project is placed under D:\QAVSDKDemoProj, as shown below.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-1.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-2.png)

**a) Create VS2010 project**

Open VS2010 and create an MFC Application project named "QAVSDKDemo", which is placed under the D:\QAVSDKDemoProj\ directory, as shown below.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-3.png)

**b) Modify project configuration**

Modify project configuration. In this case, Debug version is taken as an example.

First, right-click the project name and select "Properties" to open the project property configuration window.

Then, under Configuration Properties\VC++ Directories\Include Directories, add SDK header file path: D:\QAVSDK\include;D:\QAVSDK\include\timsdk.

Next, under Configuration Properties\VC++ Directories\Library Directories, add SDK library file path: D:\QAVSDK\libs\Debug.

Lastly, under Configuration Properties\Linker\Input\Additional Dependencies, add the lib file required for linking: qavsdk.lib;libtim.lib.

as shown below.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-4.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-5.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-6.png)



**c) Write code**

To use the APIs provided by the SDK, you need to reference SDK header files and namespaces in the code, as shown below:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-7.png)

Then you can start development using the SDK. For more information about how to use each SDK API, please see the provided demo source program and relevant documents.

**d) Run**

SDK's dynamic library dll files and audio/video parameter configuration files are required for running the executable. For this purpose, copy all the dll files and configuration files of the Debug or Release versions (under D:\QAVSDK\bin\) to the directory where the executable is located, as shown below. 

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/WindowsC++kehuduanjicheng-8.png)

## Developer Document

For more information, please see [Audio/Video Messaging Guide](http://cloud.tencent.com/wiki/%E9%9F%B3%E8%A7%86%E9%A2%91%E9%80%9A%E4%BF%A1%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)
