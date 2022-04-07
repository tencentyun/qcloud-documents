## 组件介绍

TUIVoiceRoom 是一个开源的音视频 UI 组件，通过在项目中集成 TUIVoiceRoom 组件，您只需要编写几行代码就可以为您的 App 添加“多人语音聊天”等场景。TUIVoiceRoom 同时支持 [Android](https://cloud.tencent.com/document/product/647/45737)、[小程序](https://cloud.tencent.com/document/product/647/65386) 等平台，基本功能如下图所示：

<table class="tablestyle">
<tbody><tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/797f59f998491b6ba9cc00164c076b18.jpg" width="250"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/0e4a8e5fb6d42f1c2f721195023f58bd.jpg" width="250"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/5b95135f19fbcba7acc030621107b13a.jpg" width="250"></td>
</tr>
</tbody></table>

## 组件集成
### 步骤一：下载并导入 TUIVoiceRoom 组件

在您的 xcode 工程 `Podfile` 文件同一级目录下创建 `TUIVoiceRoom` 文件夹，将 [Github仓库 iOS 目录](https://github.com/One-time/TUIVoiceRoom/tree/main/iOS) 下的 [TXAppBasic](https://github.com/One-time/TUIVoiceRoom/tree/main/iOS/TXAppBasic)、[Resources](https://github.com/One-time/TUIVoiceRoom/tree/main/iOS/Resources)、[Source](https://github.com/One-time/TUIVoiceRoom/tree/main/iOS/Source)、[TUIVoiceRoom.podspec](https://github.com/One-time/TUIVoiceRoom/blob/main/iOS/TUIVoiceRoom.podspec) 等文件拷贝至您在自己工程创建的 `TUIVoiceRoom` 目录下。并完成如下导入动作：
- 打开工程的 Podfile 文件，引入 TUIVocieRoom.podspec，参考如下：
```
# path 为TXAppBasic.podspec相对于Podfile文件的相对路径
pod 'TXAppBasic', :path => "TUIVoiceRoom/TXAppBasic/"
# path 为TUIVoiceRoom.podspec相对于Podfile文件的相对路径
pod 'TUIVoiceRoom', :path => "TUIVoiceRoom/", :subspecs => ["TRTC"]    
```
- 终端进入 Podfile 所在的目录下，执行 `pod install`，参考如下：
```
pod install
```

### 步骤二：配置权限及混淆规则
在 info.plist 文件中需要添加 `Privacy > Microphone Usage Description` 申请麦克风权限。

```plist
<key>NSMicrophoneUsageDescription</key>
<string>VoiceRoomApp需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
```

### 步骤三：初始化并登录

```Swift
// 初始化
let mTRTCVoiceRoom = TRTCVoiceRoom.shared()
// 登录
mTRTCVoiceRoom.login(sdkAppID: SDKAppID, userId: userId, userSig: userSig) { code, message in
    if code == 0 {
        //登录成功
    }
}
```
**参数说明：**
- **SDKAppID**：**TRTC 应用 ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cf6de5f10b77be75174d0ba359101f60.png)
- **Secretkey**：**TRTC 应用密钥**和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。建议结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的userSig，也可以参照我们的 [示例工程](https://github.com/tencentyun/TUIRoom/blob/main/Android/Debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java#L88) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。




### 步骤四：实现语音聊天房间
1. **实现房主创建语音聊天房间 [TRTCVoiceRoom#createRoom](https://cloud.tencent.com/document/product/647/47928#createroom)**
```Swift
// 初始化语聊房参数
let roomParam = VoiceRoomParam()
roomParam.roomName = "房间名称"
roomParam.needRequest = false // 听众上麦是否需要房主同意
roomParam.coverUrl = "房间封面图的 URL 地址"
roomParam.seatCount = 7 // 房间座位数，这里一共7个座位，房主占了一个后听众剩下6个座位
roomParam.seatInfoList = []
// 初始化麦位信息
for _ in 0..< param.seatCount {
    let seatInfo = VoiceRoomSeatInfo()
    param.seatInfoList.append(seatInfo)
}
// 房主端创建房间
mTRTCVoiceRoom.createRoom(roomID: yourRoomID, roomParam: roomParam) { (code, message) in
    if code == 0 {
        // 创建成功
    }
}
```
2. **实现听众加入语音聊天房间 [TRTCVoiceRoom#enterRoom](https://cloud.tencent.com/document/product/647/47928#enterroom)**
```Swift
// 1.听众调用加入房间
mTRTCVoiceRoom.enterRoom(roomID: roomID) { (code, message) in
    // 进入房间结果回调
    if code == 0 {
       // 进房成功
    }
}
```
3. **实现听众主动上麦 [TRTCVoiceRoom#enterSeat](https://cloud.tencent.com/document/product/647/47928#enterseat)**
```Swift
// 1: 听众调用上麦
let seatIndex = 2; //麦位的index
mTRTCVoiceRoom.enterSeat(seatIndex: 2) { (code, message) in
    if code == 0 {
        // 上麦成功
    }
}

// 2.收到 onSeatListChange 回调，刷新您的麦位列表
@Override
func onSeatListChange(seatInfoList: [VoiceRoomSeatInfo]) {
    // 刷新的麦位列表
}
```
4. **实现房主抱人上麦 [TRTCVoiceRoom#pickSeat](https://cloud.tencent.com/document/product/647/47928#pickseat)**
```Swift
// 1: 房主调用抱人麦位
let seatIndex = 2; //麦位的index
let userId = "123"; //需要上麦的用户id
mTRTCVoiceRoom.pickSeat(seatIndex: 1, userId: "123") { (code, message) in
    if code == 0 {
    }
}

// 2.收到 onSeatListChange 回调，刷新您的麦位列表
func onSeatListChange(seatInfoList: [VoiceRoomSeatInfo]) {
    // 刷新的麦位列表
}
```
5. **实现听众申请上麦  [TRTCVoiceRoom#sendInvitation](https://cloud.tencent.com/document/product/647/47928#sendinvitation)**
```Swift
// 听众端视角
// 1.听众调用申请上麦
let seatIndex = "1"; //麦位的index
let userId = "123"; //用户id
let inviteId = mTRTCVoiceRoom.sendInvitation(cmd: "takeSeat", userId: ownerUserId, content: "1") { (code, message) in
    // 发送结果回调
}

// 2.收到邀请的同意请求, 正式上麦
func onInviteeAccepted(identifier: String, invitee: String) {
    if identifier == selfID {
        self.mTRTCVoiceRoom.enterSeat(seatIndex: ) { (code, message) in
            // 上麦结果回调
        }
    }
}

// 房主端视角
// 1.房主收到请求
func onReceiveNewInvitation(identifier: String, inviter: String, cmd: String, content: String) {
    if cmd == "takeSeat" {
        // 2.房主同意听众请求
        self.mTRTCVoiceRoom.acceptInvitation(identifier: identifier, callback: nil)
    }
}
```
6. **实现房主邀请上麦  [TRTCVoiceRoom#sendInvitation](https://cloud.tencent.com/document/product/647/47928#sendinvitation)**
```Swift
// 房主端视角
// 1.房主调用 sendInvitation，请求抱听众“123”上2号麦
let inviteId = self.mTRTCVoiceRoom.sendInvitation(cmd: "pickSeat", userId: ownerUserId, content: "2") { (code, message) in
    // 发送结果回调
}

// 2.收到邀请的同意请求, 正式上麦
func onInviteeAccepted(identifier: String, invitee: String) {
    if identifier == selfID {
        self.mTRTCVoiceRoom.pickSeat(seatIndex: ) { (code, message) in
            // 上麦结果回调
        }
    }
}

// 听众端视角
// 1.听众收到请求
func onReceiveNewInvitation(identifier: String, inviter: String, cmd: String, content: String) {
    if cmd == "pickSeat" {
        // 2.听众同意房主请求
        self.mTRTCVoiceRoom.acceptInvitation(identifier: identifier, callback: nil)
    }
}
```
7. **实现文字聊天  [TRTCVoiceRoom#sendRoomTextMsg](https://cloud.tencent.com/document/product/647/47928#sendroomtextmsg)**
```Swift
// 发送端：发送文本消息
self.mTRTCVoiceRoom.sendRoomTextMsg(message: message) { (code, message) in
         
}

// 接收端：监听文本消息
func onRecvRoomTextMsg(message: String, userInfo: VoiceRoomUserInfo) {
    //收到的message信息处理方法        
}
```
8. **实现弹幕消息 [TRTCVoiceRoom#sendRoomCustomMsg](https://cloud.tencent.com/document/product/647/47928#sendroomcustommsg)**
```Swift
// 例如：发送端：您可以通过自定义Cmd来区分弹幕和点赞消息
// eg:"CMD_DANMU"表示弹幕消息，"CMD_LIKE"表示点赞消息
self.mTRTCVoiceRoom.sendRoomCustomMsg(cmd: “CMD_DANMU”, message: "hello world", callback: nil)
self.mTRTCVoiceRoom.sendRoomCustomMsg(cmd: "CMD_LIKE", message: "", callback: nil)

// 接收端：监听自定义消息
func onRecvRoomCustomMsg(cmd: String, message: String, userInfo: VoiceRoomUserInfo) {
    if cmd == "CMD_DANMU" {
        // 收到弹幕消息
    }
    if cmd == "CMD_LIKE" {
        // 收到点赞消息
    }
}
```


## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
