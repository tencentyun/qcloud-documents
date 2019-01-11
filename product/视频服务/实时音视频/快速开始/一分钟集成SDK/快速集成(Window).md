本文介绍如何快速地将腾讯云的 TRTC SDK(Window) 集成到项目中，只要按照如下步骤进行操作，可以轻松完成 SDK 的集成工作。

## 开发环境要求

- 操作系统：最低要求是 Windows 7。
- 开发环境：最低版本要求是 Visual Studio 2010，推荐使用 Visual Studio 2015。

## 集成 TRTC SDK

下面通过创建一个简单的 MFC 项目，介绍如何在 Visual Studio 工程中集成 SDK。

### 1. 下载  SDK

[下载 SDK](https://github.com/TencentVideoCloudTRTC/TRTCSDK/blob/master/SDK%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80.md)，解压并打开，包含以下几个部分：

| 目录名  | 说明                                   |
| ------- | -------------------------------------- |
| include | 带有详细接口注释的 API 头文件          |
| lib     | 编译用的 .lib 文件和运行时加载的 .dll 文件 |

### 2. 新建工程

打开Visual Studio，新建一个名字叫 TRTCDemo 的 MFC 应用程序，如下图所示：
![](https://main.qcloudimg.com/raw/645623e01a65858e23123af52ec15bc2.png)

为了便于介绍如何快速集成，在向导的**应用程序类型**页面，我们选择比较简单的**基于对话框**类型，如下图所示：
![](https://main.qcloudimg.com/raw/b561d5d514266a5ab222f4e398ebbc11.png)

其他的向导配置，请选择默认的配置即可。

### 3. 拷贝文件

将解压后的 LiteAVSDK 文件夹拷贝到 TRTCDemo.vcxproj 所在目录下，如下图所示：
![](https://main.qcloudimg.com/raw/a5bfd73b6a7d805f6bbb6e0155687e0f.png)

### 4. 修改工程配置

打开 TRTCDemo 属性页，在【解决方案资源管理器】 >【TRTCDemo 工程的右键菜单】>【属性】，请按照以下步骤进行配置：

- **添加包含目录**
在【C/C++】>【常规】>【附件包含目录】，添加 SDK 头文件目录 $(ProjectDir)LiteAVSDK\include，如下图所示：
![](https://main.qcloudimg.com/raw/ca5fcb65bad66a57b6b7446e6c92c986.png)

- **添加库目录**
在【链接器】>【常规】>【附加库目录】，添加 SDK 库目录 $(ProjectDir)LiteAVSDK\lib，如下图所示：
![](https://main.qcloudimg.com/raw/55ec832996c5355acc9215f67351fed2.png)

- **添加库文件**
在【链接器】>【输入】>【附加依赖项】，添加 SDK 库文件 liteav.lib，如下图所示：
![](https://main.qcloudimg.com/raw/2d78d5e833668ac009f5d2c04f9ec7aa.png)

- **添加 copy 命令**
在【生成事件】>【后期生成事件】>【命令行】，添加拷贝命令 copy /Y "$(ProjectDir)LiteAVSDK\lib\\\*.dll" "\$(OutDir)"，能够在编译完成后，自动将 SDK 的 .dll 文件拷贝到程序的运行目录下，如下图所示：
![](https://main.qcloudimg.com/raw/f6d626301b74d85dd6e7eb8577648988.png)

### 5. 打印 SDK 版本号

- 在 CTRTCDemoDlg::OnInitDialog 函数中，添加下面的测试代码：

```c++
TXString version = TRTCCloud::getSDKVersion();

CString szText;
szText.Format(L"SDK version: %hs", version.c_str());

CWnd *pStatic = GetDlgItem(IDC_STATIC);
pStatic->SetWindowTextW(szText);
```

- 按键盘 F5 运行，打印 SDK 的版本号，如下图所示：
![](https://main.qcloudimg.com/raw/6851ab7f24d95ae8115fdf5f69e36a3b.png)

## 常见问题

- 出现以下错误，请按照前面的工程配置，检查 SDK 头文件的目录是否正确添加。
```
fatal error C1083: 无法打开包括文件: “TRTCCloud.h”: No such file or directory
```

- 出现以下错误，请按照前面的工程配置，检查 SDK 库目录和库文件是否正确添加。
```
error LNK2019: 无法解析的外部符号 "__declspec(dllimport) public: static class TXString __cdecl TRTCCloud::getSDKVersion(void)" (__imp_?getSDKVersion@TRTCCloud@@SA?AVTXString@@XZ)，该符号在函数 "protected: virtual int __thiscall CTRTCDemoDlg::OnInitDialog(void)" (?OnInitDialog@CTRTCDemoDlg@@MAEHXZ) 中被引用
```

