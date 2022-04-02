## 组件介绍

TUIChorus 是一个开源的音视频 UI 组件，通过在项目中集成 TUIChorus 组件，您只需要编写几行代码就可以为您的应用添加在线合唱场景，体验低延时合唱、麦位管理、收发礼物、文字聊天等 TRTC 在合唱场景下的相关能力。TUIChorus 同时支持 Android 平台，基本功能如下图所示：

<table>
     <tr>
         <th  width=20%  style="text-align:center">聊天</th>  
         <th  width=20%  style="text-align:center">点歌</th>  
         <th  width=20%  style="text-align:center">合唱</th>  
         <th width=20%  style="text-align:center">发送礼物</th>  
     </tr>
<tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/8378a5d92873ebd82b42732162162bca.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/da60b4e1195b92800c0ccf8d80ac1afc.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/57f537c3112d69fbb358e2e19993db89.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/ad65196370bc058154bd2bcf5a3bb1df.png"/></td>
</tr>
</table>


## 二. 组件集成

### 步骤一：下载并导入 TUIChorus 组件
单击进入 [Github](https://github.com/tencentyun/TUIChorus) ，选择克隆/下载代码，然后拷贝`iOS`目录下的`Resources`、`Source`、`TXAppBasic`文件夹及`TUIChorus.podspec`文件到您的工程中，并完成如下导入动作：
- 在您的 `Podfile` 文件内添加导入命令，参考如下：
```
pod 'TUIChorus', :path => "./", :subspecs => ["Professional"]
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
    <string>Chorus 需要访问您的麦克风权限</string>
```

### 步骤三：初始化并登录 
相关接口说明请参见 [TUIChorus](https://cloud.tencent.com/document/product/647/61860#sharedinstance)。

```swift
// 1.初始化
let chorusRoom = TRTCChorusRoom.shared()
chorusRoom.setDelegate(delegate: self)

// 2.登录
chorusRoom.login(SDKAppID: Int32(SDKAppID), UserID: UserID, UserSig: ProfileManager.shared.curUserSig()) { code, message in
if code == 0 {
	//登录成功
}
}
```
**参数说明**：
- **SDKAppID**：**TRTC 应用ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3d6ebfa2a1e4ae5d3af3ecd564fb1463.png)
- **Secretkey**：**TRTC 应用密钥**，和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [TUICalling示例工程](https://github.com/tencentyun/TUICalling/blob/main/Android/App/src/main/java/com/tencent/liteav/demo/LoginActivity.java#L74)自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。


### 步骤四：开通推拉流服务
体验 TUIChorus 合唱场景您需要开通腾讯云推拉流服务，用于主播端推流，听众端拉流。您可参考 [推拉流URL](https://cloud.tencent.com/document/product/454/7915)，生成自己的推拉流地址并保存，可保存为 `pushUrl` 和 `playerUrl`。

### 步骤五：实现实时合唱场景
1. **主播创建房间 [TUIChorus.createRoom](https://cloud.tencent.com/document/product/647/61860#createroom)**
```swift
let roomId = "房间Id"
let param = ChorusParam.init()
param.roomName = "房间名称"
param.needRequest = false      // 上麦是否需要房主确认
param.coverUrl = "房间封面图URL"
param.seatCount = 2			   // 房间座位数，这里一共2个座位，主播及副唱，其他人进房为听众
param.rtmpPushURL = pushUrl    // 步骤三开通的推拉流地址
param.rtmpPlayURL = playUrl

chorusRoom.createRoom(roomID: roomId, roomParam: param) { [weak self] (code, message) in
	guard let `self` = self else { return }
	if code == 0 {
		//创建成功
	}
}
```
2. **听众进入房间 [TUIChorus.enterRoom](https://cloud.tencent.com/document/product/647/61860#enterroom)**
```swift
chorusRoom.enterRoom(roomID: roomInfo.roomID) { [weak self] (code, message) in
	guard let `self` = self else { return }
	if code == 0 {
       //进房成功      
	}
}
```
3. **听众主动上麦成为副唱 [TUIChorus.enterSeat](https://cloud.tencent.com/document/product/647/61860#enterseat)**
```swift
// 1.听众调用上麦
int seatIndex = 1 
chorusRoom.enterSeat(seatIndex: seatIndex) { [weak self] (code, message) in
	guard let `self` = self else { return }
	if code == 0 {                    
		//上麦成功
	}
}

// 2.收到 onSeatListChange 回调，刷新您的麦位列表
func onSeatListChange(seatInfoList seatInfolist: [ChorusSeatInfo]) {
}
```
>? 其他关于麦位管理的相关操作，您可参考 [TUIChorus接口文档](https://cloud.tencent.com/document/product/647/61860) 按需实现，或者可以参考我们的[TUIChorus示例工程](https://github.com/tencentyun/TUIChorus/)。
4. **实现音乐播放并合唱**
您可以根据自己的业务获取音乐 ID 和 URL 链接播放歌曲并合唱，相关接口说明请参见 [TUIChorus 音乐播放接口](https://cloud.tencent.com/document/product/647/61860#.E9.9F.B3.E4.B9.90.E6.92.AD.E6.94.BE.E6.8E.A5.E5.8F.A32)。
```swift
//播放音乐
chorusRoom.startPlayMusic(musicID: musicModel.musicID, url: musicModel.contentUrl)
//停止音乐
chorusRoom.stopPlayMusic()
```

完成以上步骤，就可以实现合唱基本功能。如果您的业务还需要聊天、发送礼物等功能，可以接入以下能力。

### 步骤六：文字聊天功能（可选）
如果您需要实现主播、副唱以及听众之间聊天的功能，可以通过以下方法发送或接收聊天信息。
相关接口说明请参见 [TRTCChorusRoom.sendRoomTextMsg](https://cloud.tencent.com/document/product/647/61860#sendroomtextmsg)。

```swift
// 发送端：发送文本消息
chorusRoom.sendRoomTextMsg(message: "Hello World") { [weak self] (code, message) in
	guard let `self` = self else { return }
	if (code == 0)  {
		//发送成功
	}
}

// 接收端：监听文本消息
chorusRoom.setDelegate(delegate: self)
func onRecvRoomTextMsg(message: String, userInfo: ChorusUserInfo) {
	debugPrint("收到来自：" + userInfo.userName + "的消息：" + message)
}
```

### 步骤七：礼物发送功能（可选）
如果您需要实现礼物发送和接收功能，可以通过以下方法发送礼物或接收礼物并展示。

```swift
// 发送端：通过自定义 "IMCMD_GIFT" 来区分礼物消息
chorusRoom.sendRoomCustomMsg(cmd: kSendGiftCmd, message: message) { code, msg in
	if (code == 0) {
		//发送成功
	}
}

// 接收端：监听礼物消息
chorusRoom.setDelegate(delegate: self)
func onRecvRoomCustomMsg(cmd: String, message: String, userInfo: ChorusUserInfo) {
	if cmd == kSendGiftCmd {
		debugPrint("收到来自：" + userInfo.userName + "的礼物：" + message)
	}
}
```


## 三. 常见问题
### TUIChorus 组件支持变声、变调、混响等音效功能吗？
支持，具体请参见 [TUIChorus 示例工程](https://github.com/tencentyun/TUIChorus/blob/main/iOS/Source/ui/TRTCChorusViewController/SubViews/TRTCChorusSoundEffectAlert.swift)。

>? 更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
