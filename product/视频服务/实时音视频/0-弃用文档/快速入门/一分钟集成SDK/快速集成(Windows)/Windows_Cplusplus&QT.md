本文介绍如何快速地将腾讯云 TRTC SDK（Windows C++ 版本）集成到 QT 项目中。

## 开发环境要求
- 操作系统：Windows 7及以上版本。
- 开发环境：Visual Studio 2010及以上版本，推荐使用 Visual Studio 2015。
- 确保本地已经安装了 [QT](https://download.qt.io/archive/qt/5.9/5.9.1/qt-opensource-windows-x86-5.9.1.exe) 和 [VS 开发插件](https://download.qt.io/archive/vsaddin/2.6.0/qt-vsaddin-msvc2015-2.6.0.vsix) 的相关插件环境。

[](id:using_cpp)
## 通过 QT 项目集成 C++ SDK
本节通过创建一个简单的 QT 项目，介绍如何在 Visual Studio 工程中集成 C++ SDK。

[](id:using_cpp_qt_step1)
### 步骤1：下载 SDK
1. [下载 SDK](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_latest.zip)，解压并打开。
本文示例中，您只需要引用 SDK 目录下 C++ 版的 SDK 文件即可。以64位为例，其 SDK 位置为 `./SDK/CPlusPlus/Win64/` 下，主要包含以下几个部分：
<table>
<thead>
<tr>
<th>目录名</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>include</td>
<td>带有详细接口注释的 API 头文件</td>
</tr>
<tr>
<td>lib</td>
<td>编译用的 .lib 文件和运行时加载的 .dll 文件</td>
</tr>
</tbody></table>

### 步骤2：新建工程[](id:using_cpp_qt_step2)
以 Visual Studio 2015 为例，在确保本地已经安装了 [QT](https://download.qt.io/archive/qt/5.9/5.9.1/qt-opensource-windows-x86-5.9.1.exe) 和 [VS 开发插件](https://download.qt.io/archive/vsaddin/2.6.0/qt-vsaddin-msvc2015-2.6.0.vsix) 的前提下，打开 Visual Studio。新建一个名字叫 `TRTCDemo` 的 QT 应用程序，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/17f1d06f0b14108318cf167048e1887a.png)
为了便于介绍如何快速集成，在向导中我们选择 **Qt Widgets Application** 类型，单击**确定**，在之后的页面中单击 **Next** 直到工程创建完成即可。

### 步骤3：拷贝文件[](id:using_cpp_qt_step3)
将解压后的 SDK 文件夹拷贝到 TRTCDemo.vcxproj 所在目录下，如下图所示：
>?当前只需要 C++ SDK，可以将 SDK 路径下的 CSharp 目录删除。
>
![](https://qcloudimg.tencent-cloud.cn/raw/ba31b4ac0c00c1749b95bbf40f4065a5.png)

### 步骤4：修改工程配置[](id:using_cpp_qt_step4)
打开 TRTCDemo 属性页，在**解决方案资源管理器** >**TRTCDemo 工程的右键菜单** > **属性**，请按照以下步骤进行配置：
1. **添加包含目录：**
在 **C/C++** > **常规** > **附件包含目录**，以64位为例，添加 SDK 头文件目录 `$(ProjectDir)SDK\CPlusPlus\Win64\include` 和 `$(ProjectDir)SDK\CPlusPlus\Win64\include\TRTC`，如下图所示：
>?如果为32位，则需要将 SDK 头文件目录设为 `$(ProjectDir)SDK\CPlusPlus\Win32\include` 和 `$(ProjectDir)SDK\CPlusPlus\Win32\include\TRTC`。
>
![](https://qcloudimg.tencent-cloud.cn/raw/91adc6849773ef65225968121a15a78a.png)
2. **添加库目录：**
在**链接器** > **常规** > **附加库目录**，以64位为例，添加 SDK 库目录 `$(ProjectDir)SDK\CPlusPlus\Win64\lib`，如下图所示：
>?如果为32位，则需要将 SDK 库目录设为 `$(ProjectDir)SDK\CPlusPlus\Win32\lib` 。
>
![](https://qcloudimg.tencent-cloud.cn/raw/f81588ede225cb468fcdaf9d5a57ab12.png)
3. **添加库文件：**
在**链接器** > **输入** > **附加依赖项**，添加 SDK 库文件 `liteav.lib`，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6502fa3ebc5b5f5c6e4b62500a2d227e.png)
4. **添加 copy 命令：**
在**生成事件** > **后期生成事件** > **命令行**，添加拷贝命令 `copy /Y $(ProjectDir)SDK\CPlusPlus\Win64\lib\*.dll  $(OutDir)`，能够在编译完成后，自动将 SDK 的 .dll 文件拷贝到程序的运行目录下，如下图所示：
>?如果为32位，则添加拷贝命令为 `copy /Y $(ProjectDir)SDK\CPlusPlus\Win32\lib\*.dll  $(OutDir)` 。
>
![](https://qcloudimg.tencent-cloud.cn/raw/3ca8cdbfbc5bfc31ae87bad68a872261.png)

### 步骤5：打印 SDK 版本号[](id:using_cpp_qt_step5)
1. 在 `TRTCDemo.cpp` 文件顶部增加头文件引入，代码如下：
``` c++
#include "ITRTCCloud.h"
#include <QLabel>
```
2. 在 `TRTCDemo.cpp` 文件的 `TRTCDemo::TRTCDemo` 构造函数中，添加下面的测试代码：
```C++
ITRTCCloud * pTRTCCloud = getTRTCShareInstance();
std::string version(pTRTCCloud->getSDKVersion());

QString sdk_version = QString("SDK Version: %1").arg(version.c_str());
QLabel* label_text = new QLabel(this);
label_text->setAlignment(Qt::AlignCenter);
label_text->resize(this->width(), this->height());
label_text->setText(sdk_version);
```
3. 按键盘 F5 运行，打印 SDK 的版本号，如下图所示：  
![](https://qcloudimg.tencent-cloud.cn/raw/bc1ddf818e5f0571c72d34ba212691c7.png)

## 常见问题
- 若出现以下错误，请按照前面的工程配置，检查 SDK 头文件的目录是否正确添加。
```
fatal error C1083: 无法打开包括文件: “TRTCCloud.h”: No such file or directory
```

- 若出现以下错误，请按照前面的工程配置，检查 SDK 库目录和库文件是否正确添加。
```
error LNK2019: 无法解析的外部符号 "__declspec(dllimport) public: static class TXString __cdecl TRTCCloud::getSDKVersion(void)" (__imp_?getSDKVersion@TRTCCloud@@SA?AVTXString@@XZ)，该符号在函数 "protected: virtual int __thiscall CTRTCDemoDlg::OnInitDialog(void)" (?OnInitDialog@CTRTCDemoDlg@@MAEHXZ) 中被引用
```
