# 多人视频会议（windows）
## 效果展示
您可以[下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验多人视频会议的效果，包括聊天室、屏幕分享、美颜、低延时会议等 TRTC 在多人视频会议场景下的相关能力。
## 复用 App 的 UI 界面
如需快速接入多人视频会议功能，您可以直接基于我们提供的 App 进行修改适配，也可以使用的App内的Module模块实现自定义 UI 界面。
#### 步骤1 下载App源码
单击进入[MeetingApp](https://github.com/tencentyun/TUIMeeting)，Clone或者下载源码。
#### 步骤2 配置App文件
1.找到并打开 Windows\MeetingApp\utils\usersig\win\GenerateTestUserSig.h文件。
2.设置GenerateTestUserSig.h中的参数
- SDKAPPID， 默认为0，请设置为实际的SDKAPPID
- SECRETKEY，默认为空，请设置为实际的SECRETKEY
>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

#### 步骤3 配置并运行App
1. 编译环境使用Virtual Studio(最低为2015版本)。
2. App的Ui使用的是当前主流的qt框架，版本为5.9版本，请下载并安装qt，配置qt工具到VS中。或者根据您的版本，修改App工程中qt配置，即可完成配置。
3. 打开MeetingApp源码工程，编译并运行程序。

#### 步骤4 修改App源代码
1. Module层为对TRTC和IM的封装，实现了基础的逻辑控制，并提供了功能接口，方便UI层调用。
2. App模块是UI模块，包含了界面的功能实现，您可以根据需求进行二次开发，或者替换整体UI。

## 体验应用
>! 体验应用至少需要两台设备。
#### 1.登录界面
输入房间号和用户名（请确保用户名唯一性，不能与其他用户重复）并登录，如图示。

![](https://qcloudimg.tencent-cloud.cn/raw/0e43ef455bfd83da3694f38062bbba1f.png)

#### 2.设备检测页面
此处您可以进行设备检测，或根据需求，设置进入房间使用的设备，设置美颜效果等。

![](https://qcloudimg.tencent-cloud.cn/raw/684ce3ce91252ccd7f2361e6ceccbfeb.png)

####	3.主界面
第一个进入房间的为主持人，主界面包括麦上列表，底部工具栏，顶部工具栏等。

![](https://qcloudimg.tencent-cloud.cn/raw/9916f5e550f9d09b0434fb40511520d5.png)

#### 4.麦上列表
麦上列表可以展示当前房间内的成员，对方打开摄像头和麦克风后可以看到对方的画面，听到对方的声音。
#### 5.底部工具栏
实现了控制自己的麦克风/摄像头，打开屏幕共享，成员列表，聊天室等功能。
#### 6.顶部控制栏
实现了网络信息，设置页面，麦上列表布局的功能。
#### 7.设置窗口
设置窗口可以对选择设备，设置美颜等参数。

![](https://qcloudimg.tencent-cloud.cn/raw/8554f7904403ef2b2f40f9ba48f057ea.png)

#### 8.聊天室
聊天室可以进行群成员聊天。
主持人可以对全员进行禁言/解除禁言。

![](https://qcloudimg.tencent-cloud.cn/raw/198aff7b09cb93c2658eae922fe0a64b.png)

#### 9.退出房间
主持人退出房间时可以有两种选择。
一种是解散房间，即会议结束，所有人都需要退出。
另一种为自己离开房间，将房间主持人权限转交给其他用户作为主持人。

![](https://qcloudimg.tencent-cloud.cn/raw/7ceacac7a6817ffe80927af35e0df9c4.png)

## 实现自定义UI界面
源码中的Module模块包含了对TRTCSDK以及IMSDK的封装，您可以在ITXMediaCore.h，TXMediaCoreCallback.h，TXMediaDef.h等文件中查看改模块提供的接口函数以及其他定义，并使用对应接口实现自定义UI界面。

#### 1.集成SDK
从官网下载[TRTCSDK](https://cloud.tencent.com/document/product/647/32689)和[IMSDK](https://cloud.tencent.com/document/product/269/36887)，替换外层的SDK目录中ImSDK和LiteAVSDK目录下的文件。

SDK|下载页面|集成指引
--|--|--
TRTC SDK|[DOWNLOAD](https://cloud.tencent.com/document/product/647/32689)|[集成文档](https://cloud.tencent.com/document/product/647/32178)
IM SDK|[DOWNLOAD](https://cloud.tencent.com/document/product/269/36887)|[集成文档](https://cloud.tencent.com/document/product/269/33489)

#### 2.工程配置SDK目录以及库文件
在vs中配置头文件目录，静态库目录，以及依赖的静态库文件。

#### 3.创建并登录
1. 使用ITXMediaCore::Instance接口创建并使用ITXMediaCore单例。
2. 调用AddCallback接口设置回调类，接受SDK的回调通知。
3. 调用Login接口进行登录。

参数名|说明
--|--
sdk_appid|您可以在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 中查看 SDKAppID
user_id|当前用户的 ID，字符串类型，只允许包含英文字母（a-z、A-Z）、数字（0-9）、连词符（-）和下划线（_）。
user_sig|腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)

#### 4.设置昵称
登录成功后，调用SetUserName设置用户昵称。

#### 5.创建房间
1. 成员调用CreateRoom接口创建新的会议，房间创建成功后以主持人身份进入房间，包括聊天室与TRTC房间。
2. 成员调用StartCameraPreview接口开始本地视频的采集与显示。

![](https://qcloudimg.tencent-cloud.cn/raw/34da84fb08994e12eb13aa988260acfd.png)

#### 6.解散房间
1. 主持人调用DestoryRoom接口解散房间，解散IM群聊，退出TRTC房间
2. 成员端会收到OnExitRoom回调消息，通知群解散，退出TRTC房间

#### 7.转让房间
1. 主持人调用TransferRoomMasterToOther接口将房间转让给其他人，用于离开房间的操作。
2. 成员端会收到OnRoomMasterChanged回调消息，通知房间主持人更改。
3. 更改后的主持人获取到主持人权限，可以对群成员进行控制

#### 8.加入房间
1. 加入房间流程与创建流程基本一致，成员在进入房间时都需要先去创建房间，当创建失败后以成员身份进入房间。
2. 创建房间失败后会先获取房间信息，然后再进入房间。
3. 其他成员会收到OnRemoteUserEnterRoom回调，通知有成员进入房间。

![](https://qcloudimg.tencent-cloud.cn/raw/dd5b8895b4b5d98fee456b5c833ec821.png)

#### 9.离开房间
1. 成员调用LeaveRoom接口退出IM房间和TRTC房间。
2. 其他成团端收到OnRemoteUserLeaveRoom回调，通用有成员离开房间。

#### 10.屏幕分享
1. 调用StartScreenCapture接口进行屏幕分享。
2. 其他成员收到OnRemoteUserScreenVideoAvailable回调，通知有成员正在分享屏幕。

* 屏幕分享模块需要做窗口选择的逻辑，具体实现请参考App中的ScreenShareWindow.h的实现

#### 11.实现文字聊天和禁言消息
1. 调用SendChatMessage接口发送文字，房间内的成员可以收到OnRecevieChatMessage回调消息，获取聊天消息并显示。
2. 主持人可以调用MuteUserMessage接口进行聊天禁言或者解除禁言，成员端收到OnMuteChatMessage回调，Ui层做对应的处理。