## 组件介绍

TUILiveRoom 是一个开源的音视频 UI 组件，通过在项目中集成 TUILiveRoom 组件，您只需要编写几行代码就可以为您的 App 添加“视频互动直播”等场景。TUILiveRoom 同时支持 [Android](https://cloud.tencent.com/document/product/647/43182)、[Flutter](https://cloud.tencent.com/document/product/647/57388)等平台，基本功能如下图所示：

<table>
<tr>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/beauty.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/join.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/msg.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/pk.gif"/></td>
</tr>
</table>

## 组件集成

### 步骤一：下载并导入 TUILiveRoom 组件
在您的 xcode 工程 `Podfile` 文件同一级目录下创建 `TUILiveRoom` 文件夹，将 [Github仓库 iOS 目录](https://github.com/One-time/TUILiveRoom/tree/main/iOS) 下的 [TXAppBasic](https://github.com/One-time/TUILiveRoom/tree/main/iOS/TXAppBasic)、[TCBeautyKit](https://github.com/One-time/TUILiveRoom/tree/main/iOS/TCBeautyKit)、[Resources](https://github.com/One-time/TUILiveRoom/tree/main/iOS/Resources)、[Source](https://github.com/One-time/TUILiveRoom/tree/main/iOS/Source)、[TUIVoiceRoom.podspec](https://github.com/One-time/TUILiveRoom/blob/main/iOS/TUILiveRoom.podspec) 等文件拷贝至您在自己工程创建的 `TUILiveRoom` 目录下。并完成如下导入动作：
- 打开工程的 Podfile 文件，引入TUILiveRoom.podspec，参考如下：
```
# :path => "指向TXAppBasic.podspec所在目录的相对路径"
pod 'TXAppBasic', :path => "TUILiveRoom/TXAppBasic/"

# :path => "指向TCBeautyKit.podspec所在目录的相对路径"
pod 'TCBeautyKit', :path => "TUILiveRoom/TCBeautyKit/"

# :path => "指向TUILiveRoom.podspec所在目录的相对路径"
pod 'TUILiveRoom', :path => "TUILiveRoom/", :subspecs => ["TRTC"]
```
- 终端进入 Podfile 所在的目录下，执行 `pod install`，参考如下：
```
pod install
```

### 步骤二：配置权限及混淆规则
在 info.plist 文件中依次添加 `Privacy > Microphone Usage Description` 申请麦克风权限、`Privacy > Camera Usage Description`申请相机权限。

```plist
<key>NSMicrophoneUsageDescription</key>
<string>LiveRoom需要访问您的麦克风权限，开启后录制的视频才会有声音</string>
<key>NSCameraUsageDescription</key>
<string>LiveRoom需要访问您的相机权限，开启后录制的视频才会有画面</string>
```

### 步骤三：初始化并登录
```Swift
 let mTRTCLiveRoom = TRTCLiveRoom()
 //useCDNFirst：true 表示普通观众通过 CDN 观看，false 表示普通观众通过低延时观看
 //CDNPlayDomain：表示 CDN 观看时配置的播放域名
 let config = TRTCLiveRoomConfig(useCDNFirst: useCDNFirst, cdnPlayDomain: yourCDNPlayDomain)
 mTRTCLiveRoom.login(SDKAPPID, userID, userSig, config) { (code, error) in
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

### 步骤四：实现视频互动直播间
1. **主播端开播 [TRTCLiveRoom#createRoom](https://cloud.tencent.com/document/product/647/43390#createroom)**
```Swift
// 1.主播设置昵称和头像
 mTRTCLiveRoom.setSelfProfile(name: "A", avatarURL: "faceUrl", callback: nil)

 // 2.主播开播前预览并设置美颜参数
 let view = UIView()
 parentView.add(view)
 mTRTCLiveRoom.startCameraPreview(frontCamera: true, view: view, callback: nil)
 mTRTCLiveRoom.getBeautyManager().setBeautyStyle(.nature)
 mTRTCLiveRoom.getBeautyManager().setBeautyLevel(6)

 // 3.主播创建房间
 let param = TRTCCreateRoomParam(roomName: "测试房间", coverUrl: "")
 mTRTCLiveRoom.createRoom(roomID: 123456789, roomParam: param) { [weak self] (code, error) in
  if code == 0 {
    // 4.主播开启推流并将流发布到 CDN
    self?.mTRTCLiveRoom.startPublish(streamID: mSelfUserId + "_stream", callback: nil)
  }
}
```
2. **观众端观看 [TRTCLiveRoom#enterRoom](https://cloud.tencent.com/document/product/647/43390#enterroom)**
```Swift
// 1.假定您从业务后台获取房间列表为 roomList
 var roomList: [UInt32] = GetRoomList()

 // 2.通过调用 getRoomInfos 获取房间的详细信息
 mTRTCLiveRoom.getRoomInfos(roomIDs: roomList, callback: { (code, msg, list) in
    if code == 0 {
      // 获取到房间详细信息后，您可以在主播列表页面展示主播昵称、头像等相关信息
    }
 })

 // 3.选择房间 roomid 进入
 mTRTCLiveRoom.enterRoom(roomID: roomID, callback: callback)

 // 4.观众收到主播进房通知，开始播放
 public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onAnchorEnter userID: String) {
   // 5.观众播放主播画面
   mTRTCLiveRoom.startPlay(userID: userID, view: renderView, callback: nil) 
 }
```
3. **观众与主播连麦 [TRTCLiveRoom#requestJoinAnchor](https://cloud.tencent.com/document/product/647/43390#requestjoinanchor)**
```Swift
// 观众端：
  // 1.观众端发起连麦请求
  mTRTCLiveRoom.requestJoinAnchor(reason: mSelfUserId + "请求和您连麦", responseCallback: { [weak self] (agreed, reason) in 
      // 4.主播接受了观众的请求
       if agreed {
        // 5.观众启动预览，开启推流
        self?.mTRTCLiveRoom.startCameraPreview(frontCamera: true, view: localView, callback: nil)
        self?.mTRTCLiveRoom.startPublish(streamID: streamID, callback: nil)
       }        
  }, callback: callback)

  // 主播端：
  // 2.主播端收到连麦请求
  public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onRequestJoinAnchor user: TRTCLiveUserInfo, reason: String?, timeout: Double) {
    // 3.同意对方的连麦请求
    mTRTCLiveRoom.responseJoinAnchor(userID: userID, agree: true, reason: "同意连麦")
  }

  // 6.主播收到连麦观众的上麦通知
  public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onAnchorEnter userID: String) {
    // 7.主播播放观众画面
    mTRTCLiveRoom.startPlay(userID: userID, view: view, callback: nil)
  }
```
4. **主播与主播 PK [TRTCLiveRoom#requestRoomPK](https://cloud.tencent.com/document/product/647/43390#requestroompk)**
```Swift
// 主播 A:
// 主播 A 创建12345的房间
mTRTCLiveRoom.createRoom(roomID: 12345, roomParam: param, callback: nil)

// 1.主播 A 向主播 B 发起 PK 请求
mTRTCLiveRoom.requestRoomPK(roomID: 54321, userID: "B", responseCallback: { (agree, reason) in
  // 5.收到是否同意的回调
  if agree {
  }       
}, callback: callback)

// 主播 A 收到主播 B 进入回调
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onAnchorEnter userID: String) {
  // 6.收到 B 进房的通知，播放 B 的画面
  mTRTCLiveRoom.startPlay(userID: userID, view: view, callback: callback)
}

// 主播 B：
// 主播 B 创建54321的房间
mTRTCLiveRoom.createRoom(roomID: 54321, roomParam: param, callback: nil)

// 2.主播 B 收到主播 A 的消息
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onRequestRoomPK user: TRTCLiveUserInfo, timeout: Double) {
  // 3.主播 B 回复主播 A 接受请求
  mTRTCLiveRoom.responseRoomPK(userID: userID, agree: true, reason: reason)
}

public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onAnchorEnter userID: String) {
  // 4.主播 B 收到主播 A 进房的通知，播放主播 A 的画面
  mTRTCLiveRoom.startPlay(userID: userID, view: view, callback: callback)
}
```
5. **实现文字聊天  [TRTCLiveRoom#sendRoomTextMsg](https://cloud.tencent.com/document/product/647/43390#sendroomtextmsg)**
```Swift
// 发送端：发送文本消息
mTRTCLiveRoom.sendRoomTextMsg(message: "Hello Word!", callback: callback)
// 接收端：监听文本消息
mTRTCLiveRoom.delegate = self
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onRecvRoomTextMsg message: String, fromUser user: TRTCLiveUserInfo) {
  debugPrint("收到来自\(user.userName)的文本消息:\(message)")
}
```
6. **实现弹幕消息 [TRTCLiveRoom#sendRoomCustomMsg](https://cloud.tencent.com/document/product/647/43390#sendroomcustommsg)**
```Swift
// 发送端：您可以通过自定义Cmd来区分弹幕和点赞消息
// eg:"CMD_DANMU"表示弹幕消息，"CMD_LIKE"表示点赞消息
mTRTCLiveRoom.sendRoomCustomMsg(command: "CMD_DANMU", message: "Hello world", callback: nil)
mTRTCLiveRoom.sendRoomCustomMsg(command: "CMD_LIKE", message: "", callback: nil)
// 接收端：监听自定义消息
mTRTCLiveRoom.delegate = self
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoom, onRecvRoomCustomMsg command: String, message: String, fromUser user: TRTCLiveUserInfo) {
  if "CMD_DANMU" == command {
    // 收到弹幕消息
    debugPrint("收到来自\(user.userName)的弹幕消息:\(message)")
  } else if "CMD_LIKE" == command {
    // 收到点赞消息
    debugPrint("\(user.userName)给您点了个赞！")
  }
}
```


## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
