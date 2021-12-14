## 效果展示
您可以[下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验多人视频会议的效果，包括聊天室、屏幕分享、美颜、低延时会议等 TRTC 在多人视频会议场景下的相关能力。

## 复用 App 的 UI 界面
如需快速接入多人视频会议功能，您可以直接基于我们提供的 App 进行修改适配，也可以使用的 App 内的 Module 模块实现自定义 UI 界面。

### 步骤1：下载 App 源码
单击进入 [MeetingApp](https://github.com/tencentyun/TUIMeeting)，Clone 或者下载源码。

### 步骤2：配置 App 文件
1. 找到并打开 `Windows\MeetingApp\utils\usersig\win\GenerateTestUserSig.h` 文件。
2. 设置 `GenerateTestUserSig.h` 中的参数：
	- SDKAPPID， 默认为0，请设置为实际的 SDKAPPID。
	- SECRETKEY，默认为空，请设置为实际的 SECRETKEY。
![](https://main.qcloudimg.com/raw/3e83f6ed266617afbe637edc51eb0543.png)
>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤3：配置并运行 App
1. 编译环境使用 Virtual Studio （最低为2015版本）。
2. App 的 UI 使用的是当前主流的 Qt 框架，版本为5.9版本，请下载并安装 Qt，配置 Qt 工具到 VS 中。或者根据您的版本，修改 App 工程中 Qt 配置，即可完成配置。
3. 打开 MeetingApp 源码工程，编译并运行程序。

### 步骤4：修改 App 源代码
1. Module 层为对 TRTC 和 IM 的封装，实现了基础的逻辑控制，并提供了功能接口，方便 UI 层调用。
2. App 模块是 UI 模块，包含了界面的功能实现，您可以根据需求进行二次开发，或者替换整体 UI。

## 体验应用
>! 体验应用至少需要两台设备。
### 登录界面
输入房间号和用户名（请确保用户名唯一性，不能与其他用户重复）并登录，如图示：
![](https://qcloudimg.tencent-cloud.cn/raw/0e43ef455bfd83da3694f38062bbba1f.png)

### 设备检测页面
此处您可以进行设备检测，或根据需求，设置进入房间使用的设备，设置美颜效果等。
![](https://qcloudimg.tencent-cloud.cn/raw/684ce3ce91252ccd7f2361e6ceccbfeb.png)

### 主界面
第一个进入房间的为主持人，主界面包括麦上列表，底部工具栏，顶部工具栏等。
![](https://qcloudimg.tencent-cloud.cn/raw/9916f5e550f9d09b0434fb40511520d5.png)

### 麦上列表
麦上列表可以展示当前房间内的成员，对方打开摄像头和麦克风后可以看到对方的画面，听到对方的声音。

### 底部工具栏
实现了控制自己的麦克风/摄像头，打开屏幕共享，成员列表，聊天室等功能。

### 顶部控制栏
实现了网络信息，设置页面，麦上列表布局的功能。

### 设置窗口
设置窗口可以对选择设备，设置美颜等参数。
![](https://qcloudimg.tencent-cloud.cn/raw/8554f7904403ef2b2f40f9ba48f057ea.png)

### 聊天室
- 聊天室可以进行群成员聊天。
- 主持人可以对全员进行禁言/解除禁言。

![](https://qcloudimg.tencent-cloud.cn/raw/198aff7b09cb93c2658eae922fe0a64b.png)

### 退出房间
主持人退出房间时可以有两种选择：
- **解散房间**，即会议结束，所有人都需要退出。
- **自己离开房间**，将房间主持人权限转交给其他用户作为主持人。

![](https://qcloudimg.tencent-cloud.cn/raw/7ceacac7a6817ffe80927af35e0df9c4.png)

## 实现自定义 UI 界面
源码中的 Module 模块包含了 对 TRTCSDK 以及 IMSDK 的封装，您可以在 `ITXMediaCore.h`、`TXMediaCoreCallback.h`、 `TXMediaDef.h` 等文件中查看改模块提供的接口函数以及其他定义，并使用对应接口实现自定义 UI 界面。

### 步骤1：集成 SDK
从官网下载 [TRTCSDK](https://cloud.tencent.com/document/product/647/32689) 和 [IMSDK](https://cloud.tencent.com/document/product/269/36887)，替换外层的 SDK 目录中 IMSDK 和 LiteAVSDK 目录下的文件。

| SDK   |  下载页面  | 集成指引 |
|------|------|------|
|TRTC SDK   |[DOWNLOAD](https://cloud.tencent.com/document/product/647/32689)|[集成文档](https://cloud.tencent.com/document/product/647/32178)|
|IM SDK   |[DOWNLOAD](https://cloud.tencent.com/document/product/269/36887)|[集成文档](https://cloud.tencent.com/document/product/269/33489)|

### 步骤2：工程配置 SDK 目录以及库文件
在 VS 中配置头文件目录，静态库目录，以及依赖的静态库文件。

### 步骤3：创建并登录
1. 使用 `ITXMediaCore::Instance` 接口创建并使用 ITXMediaCore 单例。
2. 调用 AddCallback 接口设置回调类，接受 SDK 的回调通知。
3. 调用 Login 接口进行登录。

|   参数名   |   说明   |
|   --|   --  |
|sdk_appid|您可以在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 中查看 SDKAppID |  
|user_id|当前用户的 ID，字符串类型，只允许包含英文字母（a-z、A-Z）、数字（0-9）、连词符（-）和下划线（\_）|
|user_sig|腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)|

### 步骤4：设置昵称
登录成功后，调用 SetUserName 设置用户昵称。

### 步骤5：创建房间
1. 成员调用 CreateRoom 接口创建新的会议，房间创建成功后以主持人身份进入房间，包括聊天室与 TRTC 房间。
2. 成员调用 StartCameraPreview 接口开始本地视频的采集与显示。

![](https://qcloudimg.tencent-cloud.cn/raw/34da84fb08994e12eb13aa988260acfd.png)

### 步骤6：解散房间
1. 主持人调用 DestoryRoom 接口解散房间，解散 IM 群聊，退出 TRTC 房间。
2. 成员端会收到 OnExitRoom 回调消息，通知群解散，退出 TRTC 房间。

### 步骤7：转让房间
1. 主持人调用 TransferRoomMasterToOther 接口将房间转让给其他人，用于离开房间的操作。
2. 成员端会收到 OnRoomMasterChanged 回调消息，通知房间主持人更改。
3. 更改后的主持人获取到主持人权限，可以对群成员进行控制

### 步骤8：加入房间
1. 加入房间流程与创建流程基本一致，成员在进入房间时都需要先去创建房间，当创建失败后以成员身份进入房间。
2. 创建房间失败后会先获取房间信息，然后再进入房间。
3. 其他成员会收到 OnRemoteUserEnterRoom 回调，通知有成员进入房间。

![](https://qcloudimg.tencent-cloud.cn/raw/dd5b8895b4b5d98fee456b5c833ec821.png)

### 步骤9：离开房间
1. 成员调用 LeaveRoom 接口退出 IM 房间和 TRTC 房间。
2. 其他成团端收到 OnRemoteUserLeaveRoom 回调，通用有成员离开房间。

### 步骤10：屏幕分享
1. 调用 StartScreenCapture 接口进行屏幕分享。
2. 其他成员收到 OnRemoteUserScreenVideoAvailable 回调，通知有成员正在分享屏幕。

>? 屏幕分享模块需要做窗口选择的逻辑，具体实现请参考 App 中的 `ScreenShareWindow.h` 的实现。

### 步骤11：实现文字聊天和禁言消息
1. 调用 SendChatMessage 接口发送文字，房间内的成员可以收到 OnRecevieChatMessage 回调消息，获取聊天消息并显示。
2. 主持人可以调用 MuteUserMessage 接口进行聊天禁言或者解除禁言，成员端收到 OnMuteChatMessage 回调，UI 层做对应的处理。



