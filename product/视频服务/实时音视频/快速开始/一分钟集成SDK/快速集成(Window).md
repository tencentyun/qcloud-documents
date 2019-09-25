本文介绍如何快速地将腾讯云 TRTC SDK（Windows C#版本）集成到项目中。

## 开发环境要求

- 操作系统：最低要求是 Windows 7。
- 开发环境：最低版本要求是 Visual Studio 2010，推荐使用 Visual Studio 2015。
- 开发框架：.Net Framework 4.0+。

## 集成 TRTC SDK

本文以创建一个简单的 Winform 项目为例，介绍如何在 Visual Studio 工程中集成 C# SDK。

### 步骤1：下载  Windows SDK

[下载 SDK](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Win_latest.zip)，解压并打开文件，包含以下部分：

| 目录名  | 说明                                   |
| ------- | -------------------------------------- |
| C++ | C++版32位/64位依赖的SDK库文件 |
| C#   | C#版32位依赖的SDK库文件 |

本文示例中，您只需要引用C#版的 SDK 文件即可。

### 步骤2：新建工程

打开 Visual Studio，新建名为`TRTCCSharpDemo`的 Winform 应用程序。
 ![](https://main.qcloudimg.com/raw/b0f7a80d2f86e73b4cc277bd05c73fd9.png)

### 步骤3：拷贝文件

将解压后的 LiteAVSDK 文件夹拷贝至`TRTCCSharpDemo.csproj`所在目录。
>?当只需要 C# SDK时，可以将 LiteAVSDK 路径下的 C++ 目录删除。
>
![](https://main.qcloudimg.com/raw/c2cc1d1672f3a7614dc69b3a2f94e556.png)

### 步骤4：修改工程配置

#### **4.1：添加引用**
 1. 打开 TRTCDemo 属性页，选择【解决方案资源管理器】 > 【TRTCCSharpDemo】> 【引用的右键菜单】 > 【添加引用】，单击【浏览】
 2. 选中当前项目下`LiteAVSDK\win32\lib`目录中的`ManageLiteAV.dll`文件并单击【添加】，如下图所示：
	![](https://main.qcloudimg.com/raw/1f7d800817b78998d0bb5ba6146cacaf.png)
 3. 在【引用管理器】界面进行选择`ManageLiteAV.dll`并单击【确定】，如下图所示：
	![](https://main.qcloudimg.com/raw/cc182d9e928f977c0c851177ce3efa12.png)

#### **4.2：添加 copy 命令**
打开 TRTCDemo 属性页，选择【解决方案资源管理器】 >【TRTCDemo 工程的右键菜单】>【属性】，在【生成事件】>【后期生成事件命令行】中添加以下命令，从而实现在编译完成后自动将 SDK 的 .dll 文件拷贝到程序的运行目录下，如下图所示：。
```
copy /Y "$(ProjectDir)LiteAVSDK\CSharp\Win32\lib\*.dll" "$(ProjectDir)$(OutDir)"
```
 ![](https://main.qcloudimg.com/raw/fde21a5e23115ba224e6ffb1e4c229c3.png)
 
#### **4.3：修改调试环境**
打开 TRTCDemo 属性页，选择【生成】，修改【常规】区域的【平台目标(G)】为【x86】，如下图所示：
![](https://main.qcloudimg.com/raw/3baac938f6a2e544d391614e7287f99e.png)

### 步骤5：打印 SDK 版本号
1. 在 Form1.cs 的设计器中添加一个 label 控件，如下图所示：
 ![](https://main.qcloudimg.com/raw/fec574b76a4250a3e948816b7cc1728d.png)
2. 打开 Form1.cs 代码文件，添加以下代码：
  ```c#
  using System.Windows.Forms;
  using ManageLiteAV;   // 1.添加命名空间引用
  
  namespace TRTCDemo
  {
      public partial class Form1 : Form
      {
          public Form1()
          {
              InitializeComponent();
              // 2.获取ITRTCCloud实例，打印 SDK 版本号
              ITRTCCloud lTRTCCloud = ITRTCCloud.getTRTCShareInstance(); 
              this.label1.Text = "SDK version : " + lTRTCCloud.getSDKVersion();
              // 3.结束使用时需手动摧毁 ITRTCCloud 实例
              ITRTCCloud.destroyTRTCShareInstance();
          }
      }
  }
  ```
3.  按 F5 运行，打印 SDK 的版本号，如下图所示：
 ![](https://main.qcloudimg.com/raw/f392bf1fdcce254800344045425ddec7.png)
 

## 常见问题

- 出现以下错误，请按照前面的工程配置，检查 SDK 引用是否添加到工程中。
```
错误 CS0246 未能找到类型或命名空间名“ManageLiteAV”(是否缺少 using 指令或程序集引用?)
```

- 出现以下错误，请按照前面的工程配置，检查是否修改工程运行平台环境为 x86 。
```
System.BadImageFormatException:“未能加载文件或程序集“ManageLiteAV, Version=2.0.7152.18518, Culture=neutral, PublicKeyToken=null”或它的某一个依赖项。试图加载格式不正确的程序。”
```

- 出现以下错误，请按照前面的工程配置，检查是否正确添加生成事件到运行目录中。
```
System.IO.FileNotFoundException:“未能加载文件或程序集“ManageLiteAV.dll”或它的某一个依赖项。找不到指定的模块。”
```

