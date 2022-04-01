本文介绍 PC 端 TUIRoom 组件，是一款布局灵活、适用性强的音视频沟通协作工具，可用于协同办公、远程招聘、远程问诊、保险理赔、在线客服、视频面试、数字政务、金融数字化、在线会议、在线教育等场景。与各行业场景深度融合，助力企业降本增效，加快数字化转型，提升竞争力。
您可以下载并安装 [Windows](https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Win_Demo.exe) 或者 [Mac](https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Mac_Demo.tar.bz2) 平台的 App 进行体验。

## 效果展示
<table>
<tr><td><img src="https://qcloudimg.tencent-cloud.cn/raw/13e8da39567148855f38bb9c4542f87e.png" width="600" height="300"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/b1ea46a940b51ed51a5ef8ba350f9a34.png" width="600" height="340"></td>
</tr></table>


## 方案优势
- 集成了超低延时音视频通话、聊天室、屏幕共享、美颜、设备检测、数据统计等能力，覆盖多人音视频房间常见功能。
- 根据需求二次开发，可以快速实现自定义 UI 界面和布局，助力业务快速上线。
- 封装了 TRTC 和 IM 基础 SDK，实现基础的逻辑控制，并提供接口方便调用。

## 接入指引
为了让您快速接入多人音视频房间功能，这边有两种推荐的接入方式，您可以选择适合您的方式进行二次开发。
- [外部进程启动](#start)
- [实现自定义 UI 界面](#ui)

### 环境准备
- **Windows环境** ：
	- Visual Studio 2015及以上集成开发环境。
	- QT5.9.1及以上版本的 QT 开发库。
	- VS 下的 QT 开发插件 Qt Visual Studio Tools 2.2.0及以上。
	- 最低支持系统：Windows 8。
	- 请确保您的集成开发环境能够正常开发。
- **Mac环境**：
	- QT5.9.1及以上版本的 QT 开发库。
	- QtCreator 集成开发环境，在安装 QT 时选择同时安装 QtCreator 即可，版本跟随 QT 官方安装包。
	- 请确保您的 QtCreator 集成开发环境能够正常开发。

### 外部进程启动[](id:start)
1. **编译 RoomApp 程序**
	- 使用外部进程启动 RoomApp 的方式，依赖原 RoomApp 的运行程序，需要提前进行编译。
	- 可以单击进入 [RoomApp](https://github.com/tencentyun/TUIRoom)，Clone 源码，配置工程并编译生成 RoomApp。
2. **新建 TestApp 工程**
<dx-tabs>
::: Windows 平台
1. 打开 VS，选择 Qt Widgets Application 工程类型，创建 TestApp 工程。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7abfdb9e19032b959f55ffb175a647e4.png" width="600">
2. 编写启动进程的程序，并在合适的位置调用 LoadRoomApp 函数。
```C++
#include <QProcess>
#include <QApplication>
void LoadRoomApp() {
    QString executable_file_path = QApplication::applicationDirPath();
    QString app_path = executable_file_path + "/RoomApp.exe";
    QProcess::startDetached(app_path);
}
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/4154f689381829d73233c4e7de10afc7.png" width="600">
3. 编译项目，并将 RoomApp 编译的成果物复制到当前可执行程序目录，以 release x86 程序为例：
复制 `TUIRoom\Windows-Mac\RoomApp\bin\Win32\Release` 目录下所有文件到当前程序目录下。
4. 执行程序，启动 TestApp 的同时启动 RoomApp。
:::
::: Mac 平台
1. 打开 QtCreator，选择 Qt Widgets Application 工程，新建项目，创建 TestApp 工程。
<img src="https://qcloudimg.tencent-cloud.cn/raw/407c4185841c901cd7beb12514d7219e.png" width="600">
2. 编写启动进程的程序，并在合适的位置调用 LoadRoomApp 函数。
```C++
#include <QProcess>
#include <QApplication>
void LoadRoomApp() {
    QString executable_file_path = QApplication::applicationDirPath();
    QString app_path = executable_file_path + "/../../../RoomApp.app/Contents/MacOS/RoomApp";
    QProcess::startDetached(app_path);
}
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/9ecb1bca7306982ef285ed52f25cfd7f.png" width="600">
3. 编译项目，并将 RoomApp 编译的产物 `RoomApp.app` 拷贝到与当前项目的产物同级目录下，以上图创建的项目路径为例：
拷贝 `RoomApp.app` 到 `/Users/mac/Desktop/TestApp/build-TestApp-Desktop_Qt_5_9_1_clang_64bit-Release` 目录下。
4. 执行程序，启动 TestApp 的同时启动 RoomApp。
:::
</dx-tabs>


### 实现自定义 UI 界面[](id:ui)
- 您可以直接基于我们提供的 App 进行修改适配，也可以使用 App 源码中的 Module 模块实现自定义 UI 界面
- 源码中的 Module 模块包含了对 TRTC SDK 以及 IM SDK 的封装，您可以在 `TUIRoomCore.h`、`TUIRoomCoreCallback.h`、`TUIRoomDef.h` 等文件中查看该模块提供的接口函数以及其他定义，并使用对应接口实现自定义 UI 界面
- App 目录包含了 UI 相关的设计与逻辑，您可以根据需求，修改 RoomApp 源码进行二次开发，主要功能点如下：
<table>
<thead>
<tr>
<th>功能点</th>
<th>文件目录</th>
</tr>
</thead>
<tbody><tr>
<td>首页登录</td>
<td>Windows-Mac\RoomApp\App\LoginViewController.cpp</td>
</tr>
<tr>
<td>设备检测</td>
<td>Windows-Mac\RoomApp\App\PresetDeviceController.cpp</td>
</tr>
<tr>
<td>主页面</td>
<td>Windows-Mac\RoomApp\App\MainWindow.cpp</td>
</tr>
<tr>
<td>麦上列表</td>
<td>Windows-Mac\RoomApp\App\StageListController.cpp</td>
</tr>
<tr>
<td>成员列表</td>
<td>Windows-Mac\RoomApp\App\MemberListViewController.cpp</td>
</tr>
<tr>
<td>设置页面</td>
<td>Windows-Mac\RoomApp\App\SettingViewController.cpp</td>
</tr>
<tr>
<td>聊天室</td>
<td>Windows-Mac\RoomApp\App\ChatRoomViewController.cpp</td>
</tr>
<tr>
<td>屏幕分享</td>
<td>Windows-Mac\RoomApp\App\ScreenShareWindow.cpp</td>
</tr>
<tr>
<td>底部工具栏</td>
<td>Windows-Mac\RoomApp\App\BottomBarController.cpp</td>
</tr>
</tbody></table>

## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
