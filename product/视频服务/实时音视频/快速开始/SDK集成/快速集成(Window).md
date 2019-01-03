本文主要介绍如何快速地将腾讯云 TRTC SDK 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求

- 操作系统最低要求是Windows 7。

- Visual Studio 最低版本要求是2008，推荐使用 Visual Studio 2015。


## 集成 TRTC SDK

通过一个简单的 MFC 项目，介绍如何在 Visual Studio 工程中配置和使用 SDK。

#### **1. 下载解压  TRTC-SDK**

去官网下载 SDK，如 LiteAVSDK_TRTC_1.1.82.zip，解压后得到 LiteAVSDK 目录，里面主要包含include目录、dll目录、lib目录，目录清单如下：

| 目录名称 | 说明                                                       |
| -------- | ---------------------------------------------------------- |
| include  | 包含 TRTC SDK API 相关头文件。                             |
| lib      | 包含 TRTC SDK 用于编译链接的.lib文件和运行加载的.dll文件。 |

**2. 新建工程**

在本例中，用Visual Studio 新建一个名为 TRTCDemo 的 MFC 基于对话框的工程。

**3. 拷贝文件**

将解压的 LiteAVSDK 文件夹拷贝到 TRTCDemo.vcxproj 所在目录，并保持 LiteAVSDK 内部原目录清单不变。

**4.修改工程配置**

将工程配置改为debug模式，平台选择：x86。按以下步骤配置 SDK 的工程环境：

- 配置头文件，在[右键工程]->[属性]->[配置属性]->[C/C++]->[常规]->[附件包含目录] 添加SDK API的头文件引用：

```
$(ProjectDir)LiteAVSDK\include   //(注：$(ProjectDir)是TRTCDemo.vcxproj所在目录宏)
```

- 配置lib库，在[右键工程]->[属性]->[配置属性]->[链接器]->[常规]->[附加库目录] 添加 SDK Lib库：

```
$(ProjectDir)LiteAVSDK\lib
```

​       在[右键工程]->[属性]->[配置属性]->[链接器]->[输入]->[附加依赖项] 添加：liteav.lib。

- 将dll动态拷贝到运行程序的bin目录：在[右键工程]->[属性]->[配置属性]->[生成事件]->[后期生成事件]->[命令行] 添加 拷贝命令：

```
copy /Y "$(ProjectDir)LiteAVSDK\lib\*.dll" "$(OutDir)"
```

**5.简单使用SDK功能**

```
#include <string.h>
#include "TRTCCloud.h"
TRTCCloud mTrtcSDK;

void TRTCMainViewController::onBtnTestTrtcSDK()
{
 	std::string version = mTrtcSDK.getSDKVersion();
}


```

## 常见问题

- 出现以下错误，请检查SDK的头文件引用配置是否正确：

```
fatal error C1083: 无法打开包括文件: “TRTCCloud.h”: No such file or directory
```

- 出现以下错误，请检查SDK的lib库配置是否正确：

```
error LNK2019: 无法解析的外部符号 "__declspec(dllimport) public: __thiscall TRTCCloud::~TRTCCloud(void)" (__imp_??1TRTCCloud@@QAE@XZ)，该符号在函数 "public: virtual __thiscall TRTCMainViewController::onBtnTestTrtcSDK(void)" (??1TRTCMainViewController@@UAE@XZ) 中被引用
```

