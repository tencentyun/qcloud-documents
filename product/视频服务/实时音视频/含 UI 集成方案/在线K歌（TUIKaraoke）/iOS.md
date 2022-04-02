## 一. 组件介绍

TUIKaraoke 是一个开源的音视频 UI 组件，通过在项目中集成 TUIKaraoke 组件，您只需要编写几行代码就可以为您的 App 添加在线K歌场景，体验K歌、麦位管理、收发礼物、文字聊天等 TRTC 在 KTV 场景下的相关能力。TUIKaraoke 支持 Android、iOS 平台的源代码，基本功能如下图所示：

<table>
     <tr>
         <th>聊天</th>  
         <th>点歌播放</th>  
         <th>音效管理</th>  
         <th>发送礼物</th>  
     </tr>
<tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/03ff7ceeebe570311fe631144546d36a.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/eb8260dd1eb5ef9128052a607596ee68.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/18c63d92b16f6bb6daaa65b2e59e40a6.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/26a685599659c27f5a3c99d20aefbc0b.png"/></td>
</tr>
</table>


## 二. 组件集成
### 步骤一：下载并导入 TUIKaraoke 组件

点击进入 [Github](https://github.com/tencentyun/TUIKaraoke) ，选择克隆/下载代码，然后拷贝 iOS目录下的 `Source`、`Resources`、`TXAppBasic`文件夹和 `TUIKaraoke.podspec`文件到您的工程中，并完成如下导入动作：

- 在您的 `Podfile` 文件内添加导入命令，参考如下：
```
pod 'TUIKaraoke', :path => "./", :subspecs => ["TRTC"]
pod 'TXLiteAVSDK_TRTC'
pod 'TXAppBasic', :path => "TXAppBasic/"
```
- 打开终端，进入`Podfile`文件所在目录下执行安装命令，参考如下：
```
pod install
```

### 步骤二：配置权限

在您的工程的 info.plist文件中配置 App 的权限，SDK 需要以下权限（iOS 系统需要动态申请麦克风）：

```
 <key>NSMicrophoneUsageDescription</key>
    <string>Karaoke 需要访问您的麦克风权限</string>
```


### 步骤三：初始化并登录 [TUIKaraoke](https://cloud.tencent.com/document/product/647/59405#sharedinstance)

```swift
  // 1.初始化
  let karaokeRoom = TRTCKaraokeRoom.shared()
  karaokeRoom.setDelegate(delegate: self)
  // 2.登录
  karaokeRoom.login(sdkAppID: Int32(SDKAPPID), userId: userId, userSig: ProfileManager.shared.curUserSig()) { code, message in
		if code == 0 {
			//登录成功
		}
  }
```
#### 3.1 参数说明
- **SDKAppID**：**TRTC 应用ID**，如果您未开通腾讯云 TRTC 服务，可以点击 [这里](https://console.cloud.tencent.com/trtc/app)，进入腾讯云实时音视频控制台，创建一个新的的TRTC应用后，点击应用信息，SDKAppID信息如下图所示；
 <img src="https://liteav.sdk.qcloud.com/app/doc/app_manager_sdk_secretkey.png" width="700">
	
- **Secretkey**：**TRTC 应用密钥**，和SDKAppId对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey信息如上图所示；

- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。

- **userSig**：根据SDKAppId、userId，Secretkey等信息计算得到的安全保护签名，您可以点击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的userSig，也可以参照我们的[TUIKaraoke示例工程](https://github.com/tencentyun/TUIKaraoke/blob/main/iOS/Debug/GenerateTestUserSig.swift#:~:text=public%20static%20String%20genTestUserSig(String%20userId)%20%7B)自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

### 步骤四：实现在线KTV场景

#### 4.1. 实现主播创建KTV房间 [TUIKaraoke.createRoom](https://cloud.tencent.com/document/product/647/59405#createroom)
```swift
int roomId = "房间ID";
let param = RoomParam.init()
param.roomName = "房间名称";
param.needRequest = false; // 上麦是否需要房主确认
param.seatCount = 8;       // 房间座位数，一共8个座位
param.coverUrl = "房间封面图URL";

karaokeRoom.createRoom(roomID: Int32(roomInfo.roomID), roomParam: param) { [weak self] (code, message) in
	guard let `self` = self else { return }
	if code == 0 {
        //创建成功
	}
}
```

#### 4.2. 实现听众进入KTV房间 [TUIKaraoke.enterRoom](https://cloud.tencent.com/document/product/647/59405#enterroom)
```swift
karaokeRoom.enterRoom(roomID: roomInfo.roomID) { [weak self] (code, message) in
	guard let `self` = self else { return }
	if code == 0 {
		//进房成功
	}
}
```
#### 4.3. 实现听众主动上麦成为副唱 [TUIKaraoke.enterSeat](https://cloud.tencent.com/document/product/647/59405#enterseat)
```swift
// 1.听众调用上麦
int seatIndex = 1; 
karaokeRoom.enterSeat(seatIndex: seatIndex) { [weak self] (code, message) in
	guard let `self` = self else { return }
	if code == 0 {
		//上麦成功
	}
}
// 2.收到 onSeatListChange 回调，刷新麦位列表
func onSeatListChange(seatInfoList: [SeatInfo]) {
}
```
>? 其他关于麦位管理的相关操作，您可参考 [TUIKaraoke接口文档](https://cloud.tencent.com/document/product/647/59405) 按需实现，或者可以参考我们的[TUIKaraoke示例工程](https://github.com/tencentyun/TUIKaraoke/)。

#### 4.4 实现音乐播放并体验KTV场景
您可以根据自己的业务获取音乐ID和URL链接，播放歌曲，[TUIKaraoke音乐播放接口](https://cloud.tencent.com/document/product/647/59405#.E9.9F.B3.E4.B9.90.E6.92.AD.E6.94.BE.E6.8E.A5.E5.8F.A32)
```swift
//播放音乐
karaokeRoom.startPlayMusic(musicID: musicID, originalUrl: muscicLocalPath, accompanyUrl: accompanyLocalPath);
//停止音乐
karaokeRoom.stopPlayMusic();
```

完成以上步骤，就可以实现KTV基本功能。如果您的业务还需要聊天、发送礼物等功能，可以接入以下能力。

### 步骤六：实现聊天功能（可选）
如果您需要实现各主播或听众之间文字聊天的功能，可以通过以下方法发送或接收聊天信息。
[TRTCKaraokeRoom.sendRoomTextMsg](https://cloud.tencent.com/document/product/647/59405#sendroomtextmsg)
```swift
// 发送端：发送文本消息
karaokeRoom.sendRoomTextMsg(message: message) { [weak self] (code, message) in
	if code == 0 {
		//发送成功
	}
}
// 接收端：监听文本消息
karaokeRoom.setDelegate(delegate: self)
func onRecvRoomTextMsg(message: String, userInfo: UserInfo) {
	debugPrint("收到来自：" + userInfo.userName + "的消息：" + message)
}
```

### 步骤七：实现礼物发送功能（可选）
如果您需要实现礼物发送和接收功能，可以通过以下方法发送礼物或接收礼物并展示。
```swift
// 发送端：通过自定义 "IMCMD_GIFT" 来区分礼物消息
karaokeRoom.sendRoomCustomMsg(cmd: kSendGiftCmd, message: message) { code, msg in
	if (code == 0) {
		//发送成功
	}
}

// 接收端：监听礼物消息
karaokeRoom.setDelegate(delegate: self)
func onRecvRoomCustomMsg(cmd: String, message: String, userInfo: UserInfo) {
	if cmd == kSendGiftCmd {
		debugPrint("收到来自：" + userInfo.userName + "的礼物：" + message)
	}
}
```

## 三. 常见问题

**Q: TUIKaraoke 组件支持变声、变调、混响等音效功能吗？**

A: 支持，具体可查看[TUIKaraoke示例工程](https://github.com/tencentyun/TUIKaraoke/blob/main/iOS/Source/ui/TRTCKTVViewController/SubViews/TRTCKaraokeSoundEffectAlert.swift)

>? 更多帮助信息，详见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)，欢迎加入 QQ 群：592465424，进行技术交流和反馈~
