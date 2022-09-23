## 组件介绍
TUIRoom 是一个开源的音视频 UI 组件，通过在项目中集成 TUIRoom 组件，您只需要编写几行代码就可以为您的 App 添加屏幕分享、美颜、低延时视频通话等。TUIRoom 同时支持 [Android](https://cloud.tencent.com/document/product/647/45667)、[Windows](https://cloud.tencent.com/document/product/647/63494)，[Mac](https://cloud.tencent.com/document/product/647/63494) 等平台，基本功能如下图所示：

>?TUIKit 系列组件同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信IM服务。即时通信 IM 服务详细计费规则请参见 [即时通信 - 价格说明](https://cloud.tencent.com/document/product/269/11673)，TRTC 开通会默认关联开通 IM SDK 的体验版，仅支持100个 DAU。

![](https://qcloudimg.tencent-cloud.cn/raw/fc82f1fa6c4e6841cda00f8ee6578b5d.png)

## 组件集成

### 步骤一：导入 TUIRoom 组件

**通过 cocoapods 导入组件**，具体步骤如下：
1. 在您的工程 `Podfile` 文件同一级目录下创建 `TUIRoom` 文件夹。
2. 单击进入 [**Github/TUIRoom**](https://github.com/tencentyun/TUIRoom) ，选择克隆/下载代码，然后将 [**TUIRoom/iOS/**](https://github.com/tencentyun/TUIRoom/tree/main/iOS) 目录下的 `Source`、`Resources` 、`TUIBeauty`、`TXAppBasic`文件夹 和 `TUIRoom.podspec` 文件拷贝到您在 `步骤1` 创建的 TUIRoom 文件夹下。
3. 在您的 Podfile 文件中添加以下依赖，之后执行 `pod install` 命令，完成导入。
```
# :path => "指向TUIRoom.podspec的相对路径"
pod 'TUIRoom', :path => "./TUIRoom/TUIRoom.podspec", :subspecs => ["TRTC"]
# :path => "指向TXAppBasic.podspec的相对路径"
pod 'TXAppBasic', :path => "./TUIRoom/TXAppBasic/"
# :path => "指向TUIBeauty.podspec的相对路径"
pod 'TUIBeauty', :path => "./TUIRoom/TUIBeauty/"
```

>!  `Source`、`Resources` 文件夹 和`TUIRoom.podspec`文件必需在同一目录下。
>-  TXAppBasic.podspec 在 TXAppBasic 文件夹下。
>-  TUIBeauty.podspec 在 TCBeautyKit 文件夹下。

### 步骤二：配置权限

使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。

```
<key>NSCameraUsageDescription</key>
<string>RoomApp需要访问您的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>RoomApp需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
```
![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)

### 步骤三：创建并初始化 TUI 组件库

<dx-codeblock>
:::  Objective-C ObjectiveC
@import TUIRoom;
@import TUICore;

// 1.组件登录
[TUILogin login:@"您的SDKAppID" userID:@"您的UserID" userSig:@"您的UserSig" succ:^{
        
} fail:^(int code, NSString *msg) {
        
}];
// 2.初始化TUIRoom实例
TUIRoom *tuiRoom = [TUIRoom sharedInstance];
```
:::
::: Swift Swift
import TUIRoom
import TUICore

// 1.组件登录
TUILogin.login("您的SDKAppID", userID: "您的UserID", userSig: "您的UserSig") {
        
} fail: { code, msg in
        
}

// 2.初始化TUIRoom实例
let tuiRoom = TUIRoom.sharedInstance
```
:::
</dx-codeblock>

**参数说明**：
- **SDKAppID**：**TRTC 应用ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3d6ebfa2a1e4ae5d3af3ecd564fb1463.png)
- **SecretKey**：**TRTC 应用密钥**，和 SDKAppID 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **UserID**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **UserSig**：根据 SDKAppId、UserID，SecretKey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [TUIRoom示例工程](https://github.com/tencentyun/TUIRoom/blob/main/iOS/Example/Debug/GenerateTestUserSig.swift#L42) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。


### 步骤四：实现多人音视频互动
1. **实现房主创建多人音视频互动房间**。
<dx-codeblock>
:::  Objective-C ObjectiveC
@import TUIRoom;

[tuiRoom createRoomWithRoomId:12345 speechMode:TUIRoomFreeSpeech isOpenCamera:YES isOpenMicrophone:YES];
:::
::: Swift Swift
import TUIRoom

tuiRoom.createRoom(roomId: 12345, speechMode: .freeSpeech, isOpenCamera: true, isOpenMicrophone: true)
```
:::
</dx-codeblock>
2. **实现其他成员加入音视频房间**。
<dx-codeblock>
:::  Objective-C ObjectiveC
@import TUIRoom;

[tuiRoom enterRoomWithRoomId:12345 isOpenCamera:YES isOpenMicrophone:YES]
:::
::: Swift Swift
import TUIRoom

tuiRoom.enterRoom(roomId: 12345, isOpenCamera: true, isOpenMicrophone: true)
```
:::
</dx-codeblock>

### 步骤五：房间管理（可选）
1. **房主解散房间 [TUIRoomCore#destroyRoom](https://cloud.tencent.com/document/product/647/45680#destroyroom)**。
<dx-codeblock>
:::  Objective-C ObjectiveC
@import TUIRoom;

[[TUIRoomCore shareInstance] destroyRoom:^(NSInteger code, NSString * _Nonnull message) {
            
}];
```
:::
::: Swift Swift
import TUIRoom

TUIRoomCore.shareInstance().destroyRoom { [weak self] _, _ in
    guard let self = self else { return }
    self.navigationController?.popViewController(animated: true)
}
```
:::
</dx-codeblock>
2. **成员离开房间 [TUIRoomCore#leaveRoom](https://cloud.tencent.com/document/product/647/45680#leaveroom)**。
<dx-codeblock>
:::  Objective-C ObjectiveC
@import TUIRoom;

[[TUIRoomCore shareInstance] leaveRoom:^(NSInteger code, NSString * _Nonnull message) {
            
}];
```
:::
::: Swift Swift
import TUIRoom

TUIRoomCore.shareInstance().leaveRoom { [weak self] _, _ in
    guard let self = self else { return }
    self.navigationController?.popViewController(animated: true)
}
```
:::
</dx-codeblock>

### 步骤六：屏幕分享（可选）
实现屏幕分享  [TUIRoomCore#startScreenCapture](https://cloud.tencent.com/document/product/647/45680#startscreencapture)。屏幕分享工程配置请参见 [实时屏幕分享(iOS)](https://cloud.tencent.com/document/product/647/45750)。
<dx-codeblock>
:::  Objective-C ObjectiveC
@import TUIRoom;
@import TXLiteAVSDK_Professional;

TRTCVideoEncParam *params = [[TRTCVideoEncParam alloc] init];
params.videoResolution = TRTCVideoResolution_1280_720;
params.resMode = TRTCVideoResolutionModePortrait;
params.videoFps = 10;
params.enableAdjustRes = NO;
params.videoBitrate = 1500;

[[TUIRoomCore shareInstance] startScreenCapture:param];
```
:::
::: Swift  Swift
import TUIRoom

 // 屏幕分享
let params = TRTCVideoEncParam()
params.videoResolution = TRTCVideoResolution._1280_720
params.resMode = TRTCVideoResolutionMode.portrait
params.videoFps = 10
params.enableAdjustRes = false
params.videoBitrate = 1500
TUIRoomCore.shareInstance().startScreenCapture(params)

```
:::
</dx-codeblock>


## 常见问题

### CocoaPods 如何安装？

在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```

更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
