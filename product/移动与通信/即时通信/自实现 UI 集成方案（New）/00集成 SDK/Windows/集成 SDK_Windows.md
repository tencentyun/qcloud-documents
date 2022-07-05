本文主要介绍如何快速将腾讯云即时通信 IM SDK 集成到您的 Windows 项目中。

## 开发环境要求
- 操作系统：最低要求是 Windows 7。
- 开发环境：最低版本要求是 Visual Studio 2010，推荐使用 Visual Studio 2019。

## 集成 IM SDK
下面通过创建一个简单的 MFC 项目，介绍如何在 Visual Studio 2019 工程中集成 SDK。
[](id:step1)
### 步骤1：下载 IM SDK
在 [Github](https://github.com/TencentCloud/TIMSDK/tree/master/Windows/IMSDK) 下载 Windows IM SDK，Windows IM SDK 的下载方式如下：
![](https://qcloudimg.tencent-cloud.cn/raw/dab3c3117d9198a5ef620c83f4abf1c7.png)

下载并解压 IM SDK，为方便可将解压后的文件夹重命名为 ImSDK，其中包含以下几个部分：

| 目录名       | 说明                                             |
| ------------ | ------------------------------------------------ |
| include     | 接口头文件                                      |
| lib\Win32 | **32 位 Release 模式**，采用 /MT 选项链接库文件 |
| lib\Win64 | **64 位 Release 模式**，采用 /MT 选项链接库文件 |


### 步骤2：新建工程
打开 Visual Studio，新建一个名为 IMDemo 的 MFC 应用程序（若 MFC 应用不在备选项前列，可借助上方的搜索模板进行查找），如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/93a8fdbce5266e95846c83f7fefc985f.png)
![](https://qcloudimg.tencent-cloud.cn/raw/bd5c02e2e4e0a39deaf5cdabde5001ec.png)

为了便于快速集成，在向导的 **应用程序类型** 页面，请选择比较简单的 **基于对话框** 类型，其他的向导配置，请选择默认的配置即可。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a601202a7ca2729cabe99be341bd2bbb.png)


### 步骤3：拷贝文件
将解压后的 IM SDK 文件夹（即 [步骤1](#step1) 中获取的 ImSDK 文件夹）拷贝到 IMDemo.vcxproj 所在目录下，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/20047b53b37d70cfc741413bed6448fd.png)

### 步骤4：修改工程配置

IM SDK 中提供了 **Release** 模式下 32 位和 64 位的静态库，针对这两类有些地方要专门配置。打开 IMDemo 属性页，在 **解决方案资源管理器** > **IMDemo 工程的右键菜单** > **属性**。

以 **32 位 Release 模式** 为例，请按照以下步骤进行配置：

1. 添加包含目录
  在 **C/C++** > **常规** > **附加包含目录**，添加 IM SDK 头文件目录 $(ProjectDir)ImSDK\include，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/27d960ff775ac72e92f77f608ec56762.png)
2. 添加库目录
  在 **链接器** > **常规** > **附加库目录**，添加 IM SDK 库目录 $(ProjectDir)ImSDK\lib\Win32
![](https://qcloudimg.tencent-cloud.cn/raw/8514a1324ef6e97987f34f51fcb0233b.png)
3.  添加库文件
  在 **链接器** > **输入** > **附加依赖项**，添加 IM SDK 库文件 ImSDK.lib ，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a6be71acbd655b6950bd577cbeaf57bb.png)
4.  拷贝 DLL 到执行目录
  在 **生成事件** > **生成前事件** > **命令行**，输入 `xcopy /E /Y "$(ProjectDir)ImSDK\lib\Win32" "$(OutDir)"`，拷贝 ImSDK.dll 动态库文件到程序生成目录，如下图所示：
 ![](https://qcloudimg.tencent-cloud.cn/raw/c1ed688ab8ab838e955b6ba8e95bf8a0.png)
5. 指定源文件的编码格式
  由于 IM SDK 的头文件采用 UTF-8 编码格式，部分编译器按默认系统编码格式编译源文件，可能导致编译无法通过，设置此参数可指定编译器按照 UTF-8 的编码格式编译源文件。
  在 **C/C++** > **命令行** > **其他选项**，输入 `/source-charset:.65001`，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9b9b1f0d715087060168febe1edf1a66.png)


**64 位 Release** 与 **32 位 Release** 的设置大部分都相同，不同在于 IM SDK 的库目录。具体如下：
1. 添加库目录
  - 在 **链接器** > **常规** > **附加库目录**，添加 IM SDK 库目录 $(ProjectDir)ImSDK\lib\Win64，如下图所示：
 ![](https://qcloudimg.tencent-cloud.cn/raw/b8e0812fdffb613ab2bf7edd6f677bff.png)
2. 拷贝 DLL 到执行目录
 - **Release 模式** 在 **生成事件** > **生成前事件** > **命令行**，输入 `xcopy /E /Y "$(ProjectDir)ImSDK\lib\Win64" "$(OutDir)"`，拷贝 ImSDK.dll 动态库文件到程序生成目录，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fc26d4ffaa5d6c73925ca84db1a81ceb.png)


### 步骤5：打印 IM SDK 版本号

- 在 IMDemoDlg.cpp 文件中，添加头文件包含：
```c++
#include "TIMCloud.h"
#include <string>
```

- 在 IMDemoDlg.cpp 文件中找到 CIMDemoDlg::OnInitDialog 函数，在 return 前添加下面的测试代码：
```c++
SetWindowText(L"IMDemo");
std::string version = TIMGetSDKVersion();
CString szText;
szText.Format(L"SDK version: %hs", version.c_str());
CWnd* pStatic = GetDlgItem(IDC_STATIC);
pStatic->SetWindowTextW(szText);
```

- 按键盘 F5 键运行，打印 IM SDK 的版本号，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f4f4f77249f255a479a3a5ff7b96c14e.png)

## 常见问题

- 出现以下错误，请按照前面的工程配置，检查 IM SDK 头文件的目录是否正确添加：
```
fatal error C1083: 无法打开包括文件: “TIMCloud.h”: No such file or directory
```

- 出现以下错误，请按照前面的工程配置，检查 IM SDK 库目录和库文件是否正确添加：
```
LINK : fatal error LNK1104: 无法打开文件“ImSDK.lib”
```
```
error LNK2019: 无法解析的外部符号 __imp__TIMGetSDKVersion，该符号在函数 "protected: virtual int __thiscall CIMDemoDlg::OnInitDialog(void)" (?OnInitDialog@CIMDemoDlg@@MAEHXZ) 中被引用
```

- 出现以下错误，请按照前面的工程配置，检查 IM SDK 的 DLL 是否拷贝到执行目录：
![](https://qcloudimg.tencent-cloud.cn/raw/fdd13a0e97a082a7e7f5d4acb0153409.png)

