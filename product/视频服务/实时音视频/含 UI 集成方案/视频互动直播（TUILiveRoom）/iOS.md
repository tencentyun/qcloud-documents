## 组件介绍

TUILiveRoom 是一个开源的视频直播 `UI` 组件，通过在项目中集成 TUILiveRoom 组件，您只需要编写几行代码就可以为您的 App 添加“视频互动直播”场景。TUILiveRoom包含 Android、iOS、小程序等平台的源代码，基本功能如下图所示：

>?TUIKit 系列组件同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信IM服务。即时通信 IM 服务详细计费规则请参见 [即时通信 - 价格说明](https://cloud.tencent.com/document/product/269/11673)，TRTC 开通会默认关联开通 IM SDK 的体验版，仅支持100个 DAU。

![](https://qcloudimg.tencent-cloud.cn/raw/ee1755293e9f4040a6f1433f4c8af73e.png)

[](id:model)
## 组件集成

[](id:model.step1)
### 步骤一：导入 TUILiveRoom 组件

**通过 cocoapods 导入组件**，具体步骤如下：
1. 在您的工程 `Podfile` 文件同一级目录下创建 `TUILiveRoom` 文件夹。
2. 单击进入 [**Github/TUILiveRoom**](https://github.com/tencentyun/TUILiveRoom) ，选择克隆/下载代码，然后将 [**TUILiveRoom/iOS/**](https://github.com/tencentyun/TUILiveRoom/tree/main/iOS) 目录下的 `Source`、`Resources` 、`TUIBeauty`、`TUIAudioEffect`、`TUIBarrage`、`TUIGift`、`TXAppBasic`文件夹 和 `TUILiveRoom.podspec` 文件拷贝到您在 `步骤1` 创建的 TUILiveRoom 文件夹下。
3. 在您的 Podfile 文件中添加以下依赖，之后执行 `pod install` 命令，完成导入。
```
# :path => "指向TUILiveRoom.podspec的相对路径"
pod 'TUILiveRoom', :path => "./TUILiveRoom/TUILiveRoom.podspec", :subspecs => ["TRTC"]
# :path => "指向TXAppBasic.podspec的相对路径"
pod 'TXAppBasic', :path => "./TUILiveRoom/TXAppBasic/"
# :path => "指向TUIBeauty.podspec的相对路径"
pod 'TUIBeauty', :path => "./TUILiveRoom/TUIBeauty/"
# :path => "指向TUIAudioEffect.podspec的相对路径"
pod 'TUIAudioEffect', :path => "./TUILiveRoom/TUIAudioEffect/", :subspecs => ["TRTC"]
# :path => "指向TUIBarrage.podspec的相对路径"
pod 'TUIBarrage', :path => "./TUILiveRoom/TUIBarrage/"
# :path => "指向TUIGift.podspec的相对路径"
pod 'TUIGift', :path => "./TUILiveRoom/TUIGift/"
```

>!  
>- `Source`、`Resources` 文件夹 和 `TUILiveRoom.podspec` 文件必需在同一目录下。
- TXAppBasic.podspec 在 TXAppBasic 文件夹下。

[](id:model.step2)
### 步骤二：配置权限

使用音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。

```
<key>NSCameraUsageDescription</key>
<string>RoomApp需要访问您的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>RoomApp需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
```
![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)

[](id:model.step3)
### 步骤三：初始化并登录组件

<dx-codeblock>
:::  Objective-C ObjectiveC
@import TUILiveRoom;
@import TUICore;

// 1.组件登录
[TUILogin login:@"您的SDKAppID" userID:@"您的UserID" userSig:@"您的UserSig" succ:^{
        
} fail:^(int code, NSString *msg) {
        
}];
// 2.初始化TUILiveRoom实例
TUILiveRoom *mLiveRoom = [TUILiveRoom sharedInstance];
```
:::
::: Swift Swift
import TUILiveRoom
import TUICore

// 1.组件登录
TUILogin.login("您的SDKAppID", userID: "您的UserID", userSig: "您的UserSig") {
        
} fail: { code, msg in
        
}
// 2.初始化TUILiveRoom实例
let mLiveRoom = TUILiveRoom.sharedInstance
```
:::
</dx-codeblock>

**参数说明**：
- **SDKAppID**：**TRTC 应用 ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3d6ebfa2a1e4ae5d3af3ecd564fb1463.png)
- **SecretKey**：**TRTC 应用密钥**，和 SDKAppID 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **UserID**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **UserSig**：根据 SDKAppId、UserID，SecretKey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [TUILiveRoom 示例工程](https://github.com/tencentyun/TUILiveRoom/blob/main/iOS/Example/Debug/GenerateTestUserSig.swift#L42) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。


[](id:model.step4)
### 步骤四：实现视频互动直播间
1. **主播端开播**
<dx-codeblock>
:::  Objective-C Objc
[mLiveRoom createRoomWithRoomId:123 roomName:@"test room" coverUrl:@""];

:::
:::  Swift Swift
mLiveRoom.createRoom(roomId: 123, roomName: "test room", coverUrl:"")
:::
</dx-codeblock>
2. **观众端观看**
<dx-codeblock>
:::  Objective-C Objc
[mLiveRoom enterRoomWithRoomId:123];

:::
:::  Swift Swift
mLiveRoom.createRoom(roomId: 123)
:::
</dx-codeblock>

3. **观众与主播连麦 [TRTCLiveRoom#requestJoinAnchor](https://cloud.tencent.com/document/product/647/43390#requestjoinanchor)**
<dx-codeblock>
:::  Objective-C Objc
// 1.观众端发起连麦请求
[TRTCLiveRoom shareInstance].delegate = self;
// @param mSelfUserId String 当前用户id
NSString *mSelfUserId = @"1314";
[[TRTCLiveRoom shareInstance] requestJoinAnchor:[NSString stringWithFormat:@"%@ 请求和你连麦", mSelfUserId] timeout:30 responseCallback:^(BOOL agreed, NSString * _Nullable reason) {
    if (agreed) {
        // 主播接受了观众的请求
      UIView *playView = [UIView new];
            [self.view addSubView:playView];
        // 观众启动预览，开启推流
      [[TRTCLiveRoom shareInstance] startCameraPreviewWithFrontCamera:YES view:playView callback:nil];
      [[TRTCLiveRoom shareInstance] startPublishWithStreamID:[NSString stringWithFormat:@"%@_stream", mSelfUserId] callback:nil];
    }            
}];

// 2.主播端收到连麦请求
#pragma mark - TRTCLiveRoomDelegate
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom onRequestJoinAnchor:(TRTCLiveUserInfo *)user reason:(NSString *)reason {
    // 同意对方的连麦请求
    [[TRTCLiveRoom shareInstance] responseJoinAnchor:user.userId agree:YES reason:@"同意连麦"];
}

- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom onAnchorEnter:(NSString *)userID {
    // 主播收到连麦观众的上麦通知
    UIView *playView = [UIView new];
    [self.view addSubview:playView];
    // 主播播放观众画面
    [[TRTCLiveRoom shareInstance] startPlayWithUserID:userID view:playView callback:nil];
}

:::
:::  Swift Swift
// 1.观众端发起连麦请求
TRTCLiveRoom.shareInstance().delegate = self
let mSelfUserId = "1314"
TRTCLiveRoom.shareInstance().requestJoinAnchor(reason: mSelfUserId + "请求和您连麦", timeout: 30) {  [weak self] (agree, msg) in
    guard let self = self else { return }
  if agree {
        // 主播接受了观众的请求
        let playView = UIView()
        self.view.addSubView(playView)
        // 观众启动预览，开启推流
        TRTCLiveRoom.shareInstance().startCameraPreview(frontCamera: true, view: playView)
        TRTCLiveRoom.shareInstance().startPublish(streamID: mSelfUserId + "_stream")
  }
}

// 2.主播端收到连麦请求
extension ViewController: TRTCLiveRoomDelegate {
    
    func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onRequestJoinAnchor user: TRTCLiveUserInfo, reason: String?) {
        // 同意对方的连麦请求
        TRTCLiveRoom.shareInstance().responseRoomPK(userID: user.userId, agree: true, reason: "同意连麦")
    }
    
    func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onAnchorEnter userID: String) {
        // 主播收到连麦观众的上麦通知
        let playView = UIView()
        view.addSubview(playView)
        // 主播播放观众画面
        TRTCLiveRoom.shareInstance().startPlay(userID: userID, view: playView);
    }
}
:::
</dx-codeblock>

4. **主播与主播 PK [TRTCLiveRoom#requestRoomPK](https://cloud.tencent.com/document/product/647/43390#requestroompk)**
<dx-codeblock>
:::  Objective-C Objc
// 主播 A 创建12345的房间
[[TUILiveRoom sharedInstance] createRoomWithRoomId:12345 roomName:@"roomA" coverUrl:@"roomA coverUrl"];
// 主播 B 创建54321的房间
[[TUILiveRoom sharedInstance] createRoomWithRoomId:54321 roomName:@"roomB" coverUrl:@"roomB coverUrl"];

// 主播 A
// 主播 A 向 主播 B 发起PK请求
[[TRTCLiveRoom shareInstance] requestRoomPKWithRoomID:543321 userID:@"roomB userId" timeout:30 responseCallback:^(BOOL agreed, NSString * _Nullable reason) {
    if (agreed) {
        // 用户B接受
    } else {
        // 用户B拒绝
    }
}];

// 主播 B：
// 2.主播 B 收到主播 A 的消息
#pragma mark - TRTCLiveRoomDelegate
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom onRequestRoomPK:(TRTCLiveUserInfo *)user {
    // 3.主播 B 回复主播 A 接受请求
    [[TRTCLiveRoom shareInstance] responseRoomPKWithUserID:user.userId agree:YES reason:@""];
}

- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom onAnchorEnter:(NSString *)userID {
    // 4.主播 B 收到主播 A 进房的通知，播放主播 A 的画面
    [[TRTCLiveRoom shareInstance] startPlayWithUserID:userID view:playAView callback:nil];
}

:::
:::  Swift Swift
// 主播 A 创建12345的房间
TUILiveRoom.sharedInstance.createRoom(roomId: 12345, roomName: "roomA")
// 主播 B 创建54321的房间
TUILiveRoom.sharedInstance.createRoom(roomId: 54321, roomName: "roomB")

// 主播 A
// 主播 A 向 主播 B 发起PK请求
TRTCLiveRoom.shareInstance().requestRoomPK(roomID: 543321, userID: "roomB userId", timeout: 30) { [weak self] (agreed, msg) in
     guard let self = self else { return }
    if agreed {
        // 用户B接受
    } else {
        // 用户B拒绝
    }
}

// 主播 B：
// 2.主播 B 收到主播 A 的消息
extension ViewController: TRTCLiveRoomDelegate {
    func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onRequestRoomPK user: TRTCLiveUserInfo) {
        // 3.主播 B 回复主播 A 接受请求
        TRTCLiveRoom.shareInstance().responseRoomPK(userID: user.userId, agree: true, reason: "")
    }
    
    func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onAnchorEnter userID: String) {
        // 4.主播 B 收到主播 A 进房的通知，播放主播 A 的画面
        TRTCLiveRoom.shareInstance().startPlay(userID: userID, view: playAView);
    }
}
:::
</dx-codeblock>

### 步骤五：美颜特效（可选）
TUILiveRoom 美颜使用了 [腾讯特效 SDK](https://cloud.tencent.com/document/product/616)，在使用美颜功能时，需要先设置 XMagic License，XMagic License 申请请参见 [XMagic License 申请指引](https://cloud.tencent.com/document/product/616/65878)。
<dx-codeblock>
:::  Objective-C Objc
@import TUIBeauty;

- (void)setXMagicLicense {
    [[TUIBeautyView getBeautyService] setLicenseUrl:@"XMagicLicenseURL" key:@"XMagicLicenseKey" completion:^(NSInteger authResult, NSString * _Nonnull errorMsg) {
            
    }];
}

:::
:::  Swift Swift
import TUIBeauty

func setXMagicLicence() {
      // [Option] Tencent Effect: XMagic Beauty License
      TUIBeautyView.getBeautyService().setLicenseUrl(XMagicLicenseURL, key: XMagicLicenseKey) { code, msg in
          debugPrint("auth result code:\(code) msg:\(msg)")
      }
}
:::
</dx-codeblock>

## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
