本文介绍如何快速地将腾讯云 TRTC SDK（Windows C#版本）集成到项目中。

## 开发环境要求

- 操作系统：Windows 7及以上版本。
- 开发环境：Visual Studio 2010及以上版本，推荐使用 Visual Studio 2015。
- 开发框架：.Net Framework 4.0及以上版本。

## 集成 TRTC SDK

本文以创建一个简单的 Winform 项目为例，介绍如何在 Visual Studio 工程中集成 C# SDK。

### 步骤1：下载  Windows SDK

[下载 SDK](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Win_latest.zip)，解压并打开文件，包含以下部分：

| 目录名  | 说明                                   |
| ------- | -------------------------------------- |
| xxxDemo | C++ Demo 源码和 C# Demo 源码 |
| CPlusPlus | C++版32位/64位依赖的 SDK 库文件 |
| CSharp | C#版32位/64位依赖的 SDK 库文件 |

本文示例中，您只需要引用 SDK 目录下 C# 版的 SDK 文件即可。

### 步骤2：新建工程

打开 Visual Studio，新建名为`TRTCCSharpDemo`的 Winform 应用程序。
 ![](https://main.qcloudimg.com/raw/b0f7a80d2f86e73b4cc277bd05c73fd9.png)

### 步骤3：拷贝文件

将解压后的 SDK 文件夹拷贝至`TRTCCSharpDemo.csproj`所在目录。
>?当只需要 C# SDK时，可以将 SDK 路径下的 CPlusPlus 目录删除。

![](https://main.qcloudimg.com/raw/dbd90fce988853c26a832930cef2e9a6.png)

<span id="Step4"></span>
### 步骤4：修改工程配置
**步骤4.1：添加引用**
1. 在 Visual Studio 的【生成】目录下找到【配置管理器】并打开。
<span id="step4_1_2"></span>
2. 在【活动解决方案平台】下拉框中选择【新建】，弹出【新建解决方案平台】对话框。
<span id="step4_1_3"></span>
3. 输入或选择新平台，单击【确定】。
 ![](https://main.qcloudimg.com/raw/75f07143f2c6a83a4d22e3f95f8f3864.png)
4. 根据实际需求重复 [步骤2](#step4_1_2) - [步骤3](#step4_1_3)  新建需要支持的解决方案平台。
 ![](https://main.qcloudimg.com/raw/e7d906cbc18d32848a25cce38f50d20c.png)
5. 打开 TRTCCSharpDemo 项目所在的文件夹，并用文本编辑器编辑`TRTCCSharpDemo.csproj`文件。
6. 在`TRTCCSharpDemo.csproj`文件中的标签 `<itemGroup>`下添加以下内容：
  ```
  //添加对不同平台下的引用
  <Reference Include="ManageLiteAV" Condition="'$(Platform)' == 'x64'">
		<HintPath>SDK\CSharp\Win64\lib\ManageLiteAV.dll</HintPath>
  </Reference>
  <Reference Include="ManageLiteAV" Condition="'$(Platform)' == 'AnyCPU'">
		<HintPath>SDK\CSharp\Win64\lib\ManageLiteAV.dll</HintPath>
  </Reference>
  <Reference Include="ManageLiteAV" Condition="'$(Platform)' == 'x86'">
		<HintPath>SDK\CSharp\Win32\lib\ManageLiteAV.dll</HintPath>
  </Reference>
  ```
  ![](https://main.qcloudimg.com/raw/a76052df7be5fb54cfbcdedc7a5afc58.png)

**步骤4.2：添加 copy 命令**
1. 打开 TRTCCSharpDemo 属性页，选择【解决方案资源管理器】>【TRTCCSharpDemo 工程的右键菜单】>【属性】。
2. 在【生成事件】>【后期生成事件命令行】中添加以下命令，实现在编译完成后自动将不同平台下的 SDK 的 .dll 文件拷贝到程序的运行目录下，如下图所示：
```
set Platform=Win64
SETLOCAL ENABLEDELAYEDEXPANSION
if $(PlatformName)==x86 ( 
  set Platform=Win32
)
copy /Y "$(ProjectDir)SDK\CSharp\!Platform!\lib\*.dll" "$(ProjectDir)$(OutDir)"
ENDLOCAL
```
![](https://main.qcloudimg.com/raw/1939c8a6702da356fe58d9945c40a60c.png)

**步骤4.3：修改调试环境**
打开 TRTCDemo 属性页，选择【生成】，将【平台(M)】与顶部菜单栏中的解决方案平台设置为一致，如下图所示：
![](https://main.qcloudimg.com/raw/23462af7ca105e5f78c5b5cbd3242063.png)

### 步骤5：打印 SDK 版本号
1. 在 Form1.cs 的设计器中添加一个 label 控件，如下图所示：
 ![](https://main.qcloudimg.com/raw/fec574b76a4250a3e948816b7cc1728d.png)
2. 打开 Form1.cs 代码文件，添加以下代码：
	```c#
	using System.Windows.Forms;
	using ManageLiteAV;   // 1.添加命名空间引用

	namespace TRTCCSharpDemo
	{
			public partial class Form1 : Form
			{
					public Form1()
					{
							InitializeComponent();
							// 2.获取 ITRTCCloud 实例，打印 SDK 版本号
							ITRTCCloud lTRTCCloud = ITRTCCloud.getTRTCShareInstance(); 
							this.label1.Text = "SDK version : " + lTRTCCloud.getSDKVersion();
							// 3.结束使用时需手动摧毁 ITRTCCloud 实例
							ITRTCCloud.destroyTRTCShareInstance();
					}
			}
	}
	```
3.  按 F5 运行，打印 SDK 的版本号，如下图所示：
 ![](https://main.qcloudimg.com/raw/9bfebaac4fa339af6b7c74b0413cde1d.png)


## 常见问题

- 若出现以下错误，请按照 [修改工程配置](#Step4)，检查 SDK 引用是否添加到工程中。
```
错误 CS0246 未能找到类型或命名空间名“ManageLiteAV”(是否缺少 using 指令或程序集引用?)
```
- 若出现以下错误，请按照 [修改工程配置](#Step4)，检查是否修改工程运行平台环境为解决方案当前目标平台 。
```
System.BadImageFormatException:“未能加载文件或程序集“ManageLiteAV, Version=2.0.7152.18518, Culture=neutral, PublicKeyToken=null”或它的某一个依赖项。试图加载格式不正确的程序。”
```
- 若出现以下错误，请按照 [修改工程配置](#Step4)，检查是否正确添加生成事件到运行目录中。
```
System.IO.FileNotFoundException:“未能加载文件或程序集“ManageLiteAV.dll”或它的某一个依赖项。找不到指定的模块。”
```
- 由于 Windows 不同版本可能存在兼容性问题，目前在 C# SDK 中新增了解决兼容性问题的 dll 文件，文件清单如下图所示。
	![](https://main.qcloudimg.com/raw/1467310c3f5b2ab7271376902d23a2be.png)
