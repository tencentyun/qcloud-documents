本文介绍如何快速地将腾讯云的 TRTC SDK(Windows C#版本) 集成到项目中，只要按照如下步骤进行操作，可以轻松完成 C# SDK 的集成工作。

## 开发环境要求

- 操作系统：最低要求是 Windows 7。
- 开发环境：最低版本要求是 Visual Studio 2010，推荐使用 Visual Studio 2015。
- 开发框架：.Net Framework 4.0+。

## 集成 TRTC SDK

下面通过创建一个简单的 Winform 项目，介绍如何在 Visual Studio 工程中集成 C# SDK。

### 1. 下载  Windows SDK

[下载 SDK](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Win_latest.zip)，解压并打开，包含以下部分：

| 目录名  | 说明                                   |
| ------- | -------------------------------------- |
| C++ | 包含的是C++版 32位/64位 依赖的SDK库文件 |
| C#   | 包含的是C#  版 32位  依赖的SDK库文件 |

这里您只需要引用C#版的 SDK 文件即可。

### 2. 新建工程

打开 Visual Studio，新建一个名字叫 TRTCCSharpDemo 的 Winform 应用程序，如下图所示：
 ![](https://main.qcloudimg.com/raw/5c2213a2bf04335c039a588556876299.png)

### 3. 拷贝文件

将解压后的 LiteAVSDK 文件夹拷贝到 TRTCCSharpDemo.csproj 所在目录下，如果只需要 C# SDK，可以将 LiteAVSDK 目录下的 C++ 目录删除，如下图所示：
![](https://main.qcloudimg.com/raw/701e4239409ff1fb988fc604b07ed9bf.png)

### 4. 修改工程配置

- **添加引用**

  在【解决方案资源管理器】 > 【TRTCCSharpDemo】> 【引用的右键菜单】 > 【添加引用】，进入界面后选择【浏览】，选择当前项目下 LiteAVSDK\win32\lib 文件夹下的 ManageLiteAV.dll 文件并点击【添加】，如下图所示：

 ![](https://main.qcloudimg.com/raw/22dd93cfeb4bad65d23152f63adbb2bf.png)

  然后在【引用管理器】界面进行选择 ManageLiteAV.dll 并点击确定，如下图所示：

 ![](https://main.qcloudimg.com/raw/1aa24f55a51cb685d4293fdc64415921.png)

- **添加 copy 命令**

  打开 TRTCDemo 属性页，在【解决方案资源管理器】 >【TRTCDemo 工程的右键菜单】>【属性】，在【生成事件】>【后期生成事件命令行】，添加拷贝命令 copy /Y "$(ProjectDir)LiteAVSDK\CSharp\Win32\lib\\*.dll" "$(ProjectDir)$(OutDir)"，能够在编译完成后，自动将 SDK 的 .dll 文件拷贝到程序的运行目录下，如下图所示：
 ![](https://main.qcloudimg.com/raw/6611bfb008a4e76d5b90820f53053f98.png)
  
- **修改调试环境**

  打开 TRTCDemo 属性页，在【生成】中，修改【常规】下的平台目标为【x86】，如下图所示：

 ![](https://main.qcloudimg.com/raw/acc59604347ad68993a371228a6bf9a6.png)

### 5. 打印 SDK 版本号

- 在 Form1.cs 的设计器中添加一个 label 控件，如下图所示：

 ![](https://main.qcloudimg.com/raw/fde3ee1202ca63b49c11b4c215fcd9c2.png)

- 打开 Form1.cs 代码文件，添加以下代码：

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
              // 2.获取ITRTCCloud实例，打印SDK版本号
              ITRTCCloud lTRTCCloud = ITRTCCloud.getTRTCShareInstance(); 
              this.label1.Text = "SDK version : " + lTRTCCloud.getSDKVersion();
              // 3.结束使用时需手动摧毁ITRTCCloud实例
              ITRTCCloud.destroyTRTCShareInstance();
          }
      }
  }
  ```

- 按键盘 F5 运行，打印 SDK 的版本号，如下图所示：

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

