本文介绍如何快速地将腾讯云的 IM SDK 集成到项目中，只要按照如下步骤进行操作，可以轻松完成 IM SDK 的集成工作。

## 开发环境要求
- 操作系统：最低要求是 Windows 7。
- 开发环境：最低版本要求是 Visual Studio 2010，推荐使用 Visual Studio 2015。

## 集成 IM SDK
下面通过创建一个简单的 MFC 项目，介绍如何在 Visual Studio 2015 工程中集成 SDK。

### 1. 下载 IM SDK

- 在 [Github](https://github.com/tencentyun/TIMSDK) 下载 Windows IM SDK，Windows IM SDK 所在目录：
![](https://main.qcloudimg.com/raw/e2064273916c99845e16d58c107d078d.png)
- 下载并打开 IM SDK 文件夹，包含以下几个部分：

| 目录名       | 说明                                             |
| ------------ | ------------------------------------------------ |
| includes     | 接口头文件                                      |
| libs\Debug   | **Debug模式**，采用/MTd 编译生成的 .lib 静态库文件和 dll 动态库文件 |
| libs\Release | **Release模式**，采用/MT 编译生成的 .lib 静态库文件和 dll 动态库文件 |


### 2. 新建工程
打开 Visual Studio，新建一个名字叫 IMDemo 的【MFC 应用程序】，如下图所示：
![](https://main.qcloudimg.com/raw/0968bf8f93c69212760bd4651839d29f.png)

为了便于快速集成，在向导的【应用程序类型】页面，请选择比较简单的【基于对话框】类型，其他的向导配置，请选择默认的配置即可。如下图所示：
![](https://main.qcloudimg.com/raw/8a6372d71853148fe6a6c5073f1512b3.png)


### 3. 拷贝文件
将解压后的 IM SDK 文件夹拷贝到 IMDemo.vcxproj 所在目录下，如下图所示：
![](https://main.qcloudimg.com/raw/4b13837ffc2662cea6a09f7a6fa5bda4.png)

### 4. 修改工程配置

IM SDK 提供了 **Debug** 和 **Release** 两种编译生成的静态库，针对这两种有些地方要专门配置。打开 IMDemo 属性页，在【解决方案资源管理器】>【IMDemo工程的右键菜单】>【属性】。

**Debug模式**下，请按照以下步骤进行配置：

- **a. 添加包含目录**
  在 【C/C++】>【常规】>【附件包含目录】，添加 IM SDK 头文件目录 $(ProjectDir)ImSDK\includes，如下图所示：
  ![](https://main.qcloudimg.com/raw/7b3dddadf6d3993ab3f83522e7e1f869.png)

- **b. 添加库目录**
  在 【链接器】>【常规】>【附加库目录】，添加 IM SDK 库目录 $(ProjectDir)ImSDK\lib\ 
  ![](https://main.qcloudimg.com/raw/40e2d19d9dbf6c1db7e05ac0051367c0.png)

- **c. 添加库文件**
  在 【链接器】>【输入】>【附加依赖项】，添加 IM SDK 库文件 imsdk.lib ，如下图所示：
  ![](https://main.qcloudimg.com/raw/e4e180c8867bb4ad6e7fa09f69c2ff0e.png)
  
- **d. 拷贝 DLL 到执行目录**  
  在【生成事件】>【预先生成事件】>【命令行】，输入 `xcopy /E /Y "$(ProjectDir)ImSDK\lib\Debug" "$(OutDir)"`，拷贝 imsdk.dll 动态库文件到程序生成目录，如下图所示：
  ![](https://main.qcloudimg.com/raw/3fc1828ee8bc4bab7197092ff1d73c45.png)
  
- **e. 指定源文件的编码格式**
  由于 IM SDK 的头文件采用 UTF-8 编码格式，部分编译器按默认系统编码格式编译源文件，可能导致编译无法通过，设置此参数可指定编译器按照 UTF-8 的编码格式编译源文件。
  在 【C/C++】>【命令行】>【其他选项】，输入`/source-charset:.65001`，如下图所示：
  ![](https://main.qcloudimg.com/raw/0c9ab7746d643594fa7cf20e93c60860.png)

**Release 模式**，跟 **Debug 模式**设置大部分相同，不同在于 IM SDK 的库目录，其他的与 **Debug 模式**一样。具体设置如下：

- **a. 添加库目录**
  在 【链接器】>【常规】>【附加库目录】，添加 IM SDK 库目录 $(ProjectDir)ImSDK\lib\Release，如下图所示：
  ![](https://main.qcloudimg.com/raw/92422bab96a1f2585671f7a5225106e4.png)
  
- **b. 拷贝 DLL 到执行目录**  
  在【生成事件】 >【预先生成事件】>【命令行】，输入 `xcopy /E /Y "$(ProjectDir)ImSDK\lib\Release" "$(OutDir)"`，拷贝 imsdk.dll 动态库文件到程序生成目录，如下图所示：
  ![](https://main.qcloudimg.com/raw/8ddf5dd09c24a77a9b8dcbd7c33f292e.png)
  
  
### 5. 打印 IM SDK 版本号

- 在 IMDemo.cpp 文件中，添加头文件包含：
```c++
#include "TIMCloud.h"
```

- 在 CIMDemoDlg::OnInitDialog 函数中，添加下面的测试代码：
```c++
std::string version = TIMGetSDKVersion();
CString szText;
szText.Format(L"SDK version: %hs", version.c_str());
CWnd* pStatic = GetDlgItem(IDC_STATIC);
pStatic->SetWindowTextW(szText);
```

- 按键盘 F5 键运行，打印 IM SDK 的版本号，如下图所示：
![](https://main.qcloudimg.com/raw/b045866bba49344cc587cc3e406b6024.png)

## 常见问题

- 出现以下错误，请按照前面的工程配置，检查 IM SDK 头文件的目录是否正确添加：
```
fatal error C1083: 无法打开包括文件: “TIMCloud.h”: No such file or directory
```

- 出现以下错误，请按照前面的工程配置，检查 IM SDK 库目录和库文件是否正确添加：
```
LINK : fatal error LNK1104: 无法打开文件“imsdk.lib”
```
```
error LNK2019: 无法解析的外部符号 __imp__TIMGetSDKVersion，该符号在函数 "protected: virtual int __thiscall CIMDemoDlg::OnInitDialog(void)" (?OnInitDialog@CIMDemoDlg@@MAEHXZ) 中被引用
```

- 出现以下错误，请按照前面的工程配置，检查 IM SDK 的 DLL 是否拷贝到执行目录：
![](https://main.qcloudimg.com/raw/5d829626978836db0ac9cc1937f7fc27.png)
