本文介绍 PC 端 TUIRoom 组件，是一款布局灵活、适用性强的音视频沟通协作工具，可用于协同办公、远程招聘、远程问诊、保险理赔、在线客服、视频面试、数字政务、金融数字化、在线会议、在线教育等场景。与各行业场景深度融合，助力企业降本增效，加快数字化转型，提升竞争力。

- 您可以下载并安装 [Windows](https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Win_Demo.exe) 或者 [Mac](https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Mac_Demo.tar.bz2) 平台的 App 进行体验。

### 效果展示

<img src="https://qcloudimg.tencent-cloud.cn/raw/13e8da39567148855f38bb9c4542f87e.png" width="600" height="300"/>

<img src="https://qcloudimg.tencent-cloud.cn/raw/b1ea46a940b51ed51a5ef8ba350f9a34.png" width="600" height="340"/>

## 方案优势
- 集成了超低延时音视频通话、聊天室、屏幕共享、美颜、设备检测、数据统计等能力，覆盖多人音视频房间常见功能。
- 根据需求二次开发，可以快速实现自定义 UI 界面和布局，助力业务快速上线。
- 封装了 TRTC 和 IM 基础 SDK，实现基础的逻辑控制，并提供接口方便调用。

## 接入指引
为了让您快速接入多人音视频房间功能，这边有两种推荐的接入方式，您可以选择适合您的方式进行二次开发。
- 外部进程启动
- 实现自定义 UI 界面

### 环境准备：

#### Windows环境 ：
- Visual Studio 2015及以上集成开发环境。
- QT5.9.1及以上版本的Qt开发库。
- VS下的QT开发插件Qt Visual Studio Tools 2.2.0及以上。
- 最低支持系统：Windows 8。
- 请确保您的集成开发环境能够正常开发。

#### Mac环境：
- QT5.9.1及以上版本的QT开发库。
- QtCreator集成开发环境，在安装QT时选择同时安装QtCreator即可，版本跟随QT官方安装包。
- 请确保您的QtCreator集成开发环境能够正常开发。

### 外部进程启动
#### 一、编译RoomApp程序
- 使用外部进程启动RoomApp的方式，依赖原RoomApp的运行程序，需要提前进行编译。
- 可以单击进入[RoomApp](https://github.com/tencentyun/TUIRoom)，Clone 源码，配置工程并编译生成RoomApp。

#### 二、Windows平台新建TestApp工程

- 打开VS，选择Qt Widgets Application工程类型，创建TestApp工程。

<img src="https://qcloudimg.tencent-cloud.cn/raw/7abfdb9e19032b959f55ffb175a647e4.png" width="450" height="300"/>

- 编写启动进程的程序，并在合适的位置调用LoadRoomApp函数

```C++
#include <QProcess>
#include <QApplication>
void LoadRoomApp() {
    QString executable_file_path = QApplication::applicationDirPath();
    QString app_path = executable_file_path + "/RoomApp.exe";
    QProcess::startDetached(app_path);
}
```

<img src="https://qcloudimg.tencent-cloud.cn/raw/4154f689381829d73233c4e7de10afc7.png" width="450" height="220"/>

- 编译项目，并将RoomApp编译的成果物复制到当前可执行程序目录(以release,x86程序为例：复制TUIRoom\Windows-Mac\RoomApp\bin\Win32\Release 目录下所有文件到当前程序目录下)
- 执行程序，启动TestApp的同时启动RoomApp。

#### 三、Mac平台新建TestApp工程
- 打开QtCreator，选择Qt Widgets Application工程，新建项目，创建TestApp工程。

<img src="https://qcloudimg.tencent-cloud.cn/raw/407c4185841c901cd7beb12514d7219e.png" width="450" height="250"/>

- 编写启动进程的程序，并在合适的位置调用LoadRoomApp函数

```C++
#include <QProcess>
#include <QApplication>
void LoadRoomApp() {
    QString executable_file_path = QApplication::applicationDirPath();
    QString app_path = executable_file_path + "/../../../RoomApp.app/Contents/MacOS/RoomApp";
    QProcess::startDetached(app_path);
}
```

<img src="https://qcloudimg.tencent-cloud.cn/raw/9ecb1bca7306982ef285ed52f25cfd7f.png" width="450" height="220"/>

- 编译项目，并将RoomApp编译的产物 `RoomApp.app` 拷贝到与当前项目的产物同级目录下(以上图创建的项目路径为例：拷贝 `RoomApp.app` 到 `/Users/mac/Desktop/TestApp/build-TestApp-Desktop_Qt_5_9_1_clang_64bit-Release` 目录下)。
- 执行程序，启动TestApp的同时启动RoomApp。

### 实现自定义 UI 界面
- 您可以直接基于我们提供的 App 进行修改适配，也可以使用 App 源码中的 Module 模块实现自定义 UI 界面
- 源码中的 Module 模块包含了对 TRTC SDK 以及 IM SDK 的封装，您可以在 `TUIRoomCore.h`、`TUIRoomCoreCallback.h`、`TUIRoomDef.h` 等文件中查看该模块提供的接口函数以及其他定义，并使用对应接口实现自定义 UI 界面
- App目录包含了 UI 相关的设计与逻辑，您可以根据需求，修改RoomApp源码进行二次开发，主要功能点如下：


| 功能点      | 文件目录                                              |
| ---------- | ----------------------------------------------------- |
| 首页登录    | Windows-Mac\RoomApp\App\LoginViewController.cpp       |
| 设备检测    | Windows-Mac\RoomApp\App\PresetDeviceController.cpp    |
| 主页面      | Windows-Mac\RoomApp\App\MainWindow.cpp                |
| 麦上列表    | Windows-Mac\RoomApp\App\StageListController.cpp       |
| 成员列表    | Windows-Mac\RoomApp\App\MemberListViewController.cpp  |
| 设置页面    | Windows-Mac\RoomApp\App\SettingViewController.cpp     |
| 聊天室      | Windows-Mac\RoomApp\App\ChatRoomViewController.cpp    |
| 屏幕分享    | Windows-Mac\RoomApp\App\ScreenShareWindow.cpp         |
| 底部工具栏  | Windows-Mac\RoomApp\App\BottomBarController.cpp       |

## 常见问题

>? 更多帮助信息，详见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)，欢迎加入 QQ 群：592465424，进行技术交流和反馈~