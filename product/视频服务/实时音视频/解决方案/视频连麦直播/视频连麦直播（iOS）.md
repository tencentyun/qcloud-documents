## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 Demo 体验互动直播的能力效果，包括互动连麦、主播 PK、低延时观看、弹幕聊天等 TRTC 在互动直播场景下的相关能力。

<table>
<tr>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcliveroom/beauty.gif"/></td>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcliveroom/join.gif"/></td>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcliveroom/msg.gif"/></td>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcliveroom/pk.gif"/></td>
</tr>
</table>

如需快速接入视频互动直播功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCLiveRoom 组件并实现自定义 UI 界面。

<span id="DemoUI"> </span>
## 复用 Demo 的 UI 界面

<span id="ui.step1"></span>
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如 `TestLiveRoom` ，单击【创建应用】。

>?本功能需同时使用 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。

<span id="ui.step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/iOS)】跳转至 Github（或单击【[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_iOS_latest.zip)】），下载相关 SDK 及配套的 Demo 源码。
 ![](https://main.qcloudimg.com/raw/716b5af9207ad2b11835dec4e2d15da0.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。

<span id="ui.step3"></span>
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#ui.step2) 中下载的源码包。
2. 找到并打开 `iOS/TRTCScenesDemo/TRTCScenesDemo/debug/GenerateTestUserSig.h` 文件。
3. 设置 `GenerateTestUserSig.h` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为占位符，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为占位符，请设置为实际的密钥信息。</li></ul> 
    <img src="https://main.qcloudimg.com/raw/15d986c5f4bc340e555630a070b90d63.png">
4. 返回实时音视频控制台，单击【粘贴完成，下一步】。
5. 单击【关闭指引，进入控制台管理应用】。

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

<span id="ui.step4"></span>
### 步骤4：运行 Demo
使用 Xcode（11.0及以上的版本）打开源码工程 `TRTCScenesDemo`，单击【运行】即可开始调试本 Demo。

<span id="ui.step5"></span>
### 步骤5：修改 Demo 源代码
源码中的 trtcliveroomdemo 文件夹包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个 swift 文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
| Anchor | 主播端相关 UI 的实现代码。 | 
| Audience | 观众端相关 UI 的实现代码。 | 
| ChatRoom | 文字聊天室以及弹幕消息的 UI 实现代码。 | 
| Common | 可复用的一些 UI 组件的实现代码。 | 
| StatusView | 状态浮层，会覆盖在视频画面上面，用于显示日志信息和视频加载动画。 | 
| LiveRoomMainViewController.swift | 视频互动直播主页面 UI。 | 


<span id="model"> </span>
## 实现自定义 UI 界面
源码中的 trtcliveroomdemo 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCLiveRoom，您可以在`TRTCLiveRoom.swift` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/b0c39e5b7ce3a6b1decb1fbbf7ec4ff1.png)


<span id="model.step1"> </span>
### 步骤1：集成 SDK
视频通话组件 TRTCLiveRoom 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

**方法一：通过 cocoapods 仓库依赖**
```
pod 'TXIMSDK_iOS'
pod 'TXLiteAVSDK_TRTC'
```
>?两个 SDK 产品的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。

**方法二：通过本地依赖**
如果您的开发环境访问 cocoapods 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。

| SDK | 下载页面 | 集成指引 |
|---------|---------|---------|
| TRTC SDK | [DOWNLOAD](https://cloud.tencent.com/document/product/647/32689) | [集成文档](https://cloud.tencent.com/document/product/647/32175) |
| IM SDK | [DOWNLOAD](https://cloud.tencent.com/document/product/269/36887) | [集成文档](https://cloud.tencent.com/document/product/269/32679) |

<span id="model.step2"> </span>
### 步骤2：配置权限
在 info.plist 文件中需要添加 Privacy > Camera Usage Description， Privacy > Microphone Usage Description 申请摄像头和麦克风权限。

<span id="model.step3"> </span>
### 步骤3：导入 TRTCLiveRoom 组件
拷贝`iOS/TRTCScenesDemo/TRTCScenesDemo/TRTCLiveRoomDemo/model`目录中的所有文件到您的项目中。

<span id="model.step4"> </span>
### 步骤4：创建并登录组件
1. 调用 TRTCLiveRoomImpl 的`init`接口可以创建一个 TRTCLiveRoom 组件的实例对象。
2. 创建一个`TRTCLiveRoomConfig`对象，该对象可以设置  useCDNFirst 和 CDNPlayDomain 属性：
 - useCDNFirst 属性：用于设置观众观看方式。true 表示普通观众通过 CDN 观看，计费便宜但延时较高。false 表示普通观众通过低延时观看，计费价格介于 CDN 和连麦之间，但延迟可控制在1s以内。
 - CDNPlayDomain 属性：在 useCDNFirst 设置为 true 时才会生效，用于指定 CDN 观看的播放域名，您可以登录直播控制台 >【[域名管理](https://console.cloud.tencent.com/live/domainmanage)】页面中进行设置。
3. 调用`login`函数完成组件的登录，请参考下表填写关键参数：
<table>	
<tr>
<th>参数名</th>
<th>作用</th>
</tr>
<tr>
<td>sdkAppId</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr>
<tr>
<td>userId</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z、A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
</tr>
<tr>
<td>userSig</td>
<td>腾讯云设计的一种安全保护签名，获取方式请参考 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
</tr>
<tr>
<td>config</td>
<td>全局配置信息，请在登录时初始化，登录之后不可变更。<ul style="margin:0;">
<li>useCDNFirst 属性：用于设置观众观看方式。true 表示普通观众通过 CDN 观看，计费便宜但延时较高。false 表示普通观众通过低延时观看，计费价格介于 CDN 和连麦之间，但延迟可控制在1s以内。</li>
<li>CDNPlayDomain 属性：在 useCDNFirst 设置为 true 时才会生效，用于指定 CDN 观看的播放域名，您可以登录直播控制台 >【<a href="https://console.cloud.tencent.com/live/domainmanage">域名管理</a>】页面中进行设置。</li>
</ul></td>
</tr>
<tr>
<td>callback</td>
<td>登录回调，成功时 code 为0。</td>
</tr>
</table>
<pre>
class LiveRoomController: UIViewController {
	let mLiveRoom = TRTCLiveRoomImpl()
}
//useCDNFirst：true 表示普通观众通过 CDN 观看，false 表示普通观众通过低延时观看
//CDNPlayDomain：表示 CDN 观看时配置的播放域名
let config = TRTCLiveRoomConfig(useCDNFirst: useCDNFirst, cdnPlayDomain: yourCDNPlayDomain)
mLiveRoom.login(SDKAPPID, userID, userSig, config) { (code, error) in
	if code == 0 {
		//登录成功
	}
}
</pre>

<span id="model.step5"> </span>
### 步骤5：主播端开播
1. 主播执行 [步骤四](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 主播在开播前可先调用`startCameraPreview`开启摄像头预览，界面上可以配置美颜调节按钮调用，通过`getBeautyManager`进行美颜设置。
 >?非企业版 SDK 不支持变脸和贴图挂件功能。
 >
3. 主播调整美颜效果后，可以调用`createRoom`创建新的直播间。
4. 主播调用`startPublish`开始推流。如需支持 CDN 观看，请在 login 时传入的`TRTCLiveRoomConfig`参数中指定`useCDNFirst`和`CDNPlayDomain`并在`startPublish`时指定直播拉流用的 streamID。

![](https://main.qcloudimg.com/raw/754450346c831a792a0cc7a06b2c7d31.png)

```swift
// 1.主播设置昵称和头像
mLiveRoom.setSelfProfile(name: "A", avatarURL: "faceUrl", callback: nil)

// 2.主播开播前预览并设置美颜参数
let view = UIView()
parentView.add(view)
mLiveRoom.startCameraPreview(frontCamera: true, view: view, callback: nil)
mLiveRoom.getBeautyManager().setBeautyStyle(.nature)
mLiveRoom.getBeautyManager().setBeautyLevel(6)

// 3.主播创建房间
let param = TRTCCreateRoomParam(roomName: "测试房间", coverUrl: "")
mLiveRoom.createRoom(roomID: 123456789, roomParam: param) { [weak self] (code, error) in
	if code == 0 {
		// 4.主播开启推流并将流发布到 CDN
		self?.mLiveRoom.startPublish(streamID: mSelfUserId + "_stream", callback: nil)
	}
}
```

<span id="model.step6"> </span>
### 步骤6：观众端观看
1. 观众端执行 [步骤四](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 观众端向业务后台获取最新的直播房间列表。
 >?Demo 中的直播间列表仅做演示使用，直播间列表的业务逻辑千差万别，腾讯云暂不提供直播间列表的管理服务，请自行管理您的直播间列表。
 >
3. 观众端调用`getRoomInfos`获取房间的详细信息，该信息是在主播端调用`createRoom`创建直播间时设置的简单描述信息。
 >!如果您的直播间列表包含了足够全面的信息，可跳过调用`getRoomInfos`相关步骤。
 >
4. 观众选择一个直播间，调用`enterRoom`并传入房间号即可进入该房间。
5.  调用`startPlay`并传入主播的 userId 开始播放。
 - 若直播间列表已包含主播端的 userId 信息，观众端可直接调用`startPlay`并传入主播的 userId 即可开始播放。
 - 若在进房前暂未获取主播的 userId，观众端在进房后会收到主播`onAnchorEnter`的事件回调，该回调中携带主播的 userId 信息，调用`startPlay`即可播放。 


![](https://main.qcloudimg.com/raw/70320746e332252cddbb842e280c95a5.png)

```swift
// 1.假定您从业务后台获取房间列表为 roomList
var roomList: [UInt32] = GetRoomList()

// 2.通过调用 getRoomInfos 获取房间的详细信息
mliveRoom.getRoomInfos(roomIDs: roomList, callback: { (code, msg, list) in
if code == 0 {
		// 获取到房间详细信息后，您可以在主播列表页面展示主播昵称、头像等相关信息
	}
})

// 3.选择房间 roomid 进入
mliveRoom.enterRoom(roomID: roomID, callback: callback)

// 4.观众收到主播进房通知，开始播放
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onAnchorEnter userID: String) {
	// 5.观众播放主播画面
	mliveRoom.startPlay(userID: userID, view: renderView, callback: nil) 
}
```

<span id="model.step7"> </span>
### 步骤7：观众与主播连麦
1. 观众端调用`requestJoinAnchor`向主播端发起连麦请求。
2. 主播端会收到`TRTCLiveRoomDelegate#onRequestJoinAnchor`（即有观众请求与您连麦）的事件通知。
3. 主播端可以通过调用`responseJoinAnchor`决定是否接受来自观众端的连麦请求。
4. 观众端会收到`TRTCLiveRoomDelegate#responseCallback`事件通知，该通知会携带来自主播端的处理结果。
5. 如果主播同意连麦请求，观众端可调用`startCameraPreview`开启本地摄像头，随后调用`startPublish`启动观众端的推流。
6. 主播端会在观众端启动通知后收到 `TRTCLiveRoomDelegate#onAnchorEnter` （即另一路音视频流已到来）通知，该通知会携带观众端的 userId。
7. 主播端调用`startPlay`即可看到连麦观众的画面。

![](https://main.qcloudimg.com/raw/743009e16a89eb6ff8d708b4564d8a91.png)

```swift
// 观众端：
// 1.观众端发起连麦请求
mliveRoom.requestJoinAnchor(reason: mSelfUserId + "请求和您连麦", responseCallback: { [weak self] (agreed, reason) in 
	  // 4.主播接受了观众的请求
     if agreed {
     	 // 5.观众启动预览，开启推流
     	 self?.mliveRoom.startCameraPreview(frontCamera: true, view: localView, callback: nil)
     	 self?.mliveRoom.startPublish(streamID: streamID, callback: nil)
     }        
}, callback: callback)

// 主播端：
// 2.主播端收到连麦请求
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onRequestJoinAnchor user: TRTCLiveUserInfo, reason: String?, timeout: Double) {
	// 3.同意对方的连麦请求
	mliveRoom.responseJoinAnchor(userID: userID, agree: true, reason: "同意连麦")
}

// 6.主播收到连麦观众的上麦通知
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onAnchorEnter userID: String) {
	// 7.主播播放观众画面
	mliveRoom.startPlay(userID: userID, view: view, callback: nil)
}
```

<span id="model.step8"> </span>
### 步骤8：主播与主播 PK
1. 主播 A 调用`requestRoomPK`向主播 B 发起 PK 请求。
2. 主播 B 会收到`TRTCLiveRoomDelegate onRequestRoomPK`回调通知。
3. 主播 B 调用`responseRoomPK`决定是否接受主播 A 的 PK 请求。
4. 主播 B 接受主播 A 的请求，等待`TRTCLiveRoomDelegate onAnchorEnter`通知，调用`startPlay`显示主播 A。
5. 主播 A 收到`responseCallback`回调通知，PK 请求是否被同意。
6. 主播 A 请求被同意，等待`TRTCLiveRoomDelegate onAnchorEnter`通知，调用`startPlay`显示主播 B。

![](https://main.qcloudimg.com/raw/8e3868af20a2cd4f968b673da107e227.png)

```swift
// 主播 A:
// 主播 A 创建12345的房间
mLiveRoom.createRoom(roomID: 12345, roomParam: param, callback: nil)

// 1.主播 A 向主播 B 发起 PK 请求
mLiveRoom.requestRoomPK(roomID: 54321, userID: "B", responseCallback: { (agree, reason) in
	// 5.收到是否同意的回调
	if agree {
	}       
}, callback: callback)

// 主播 A 收到主播 B 进入回调
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onAnchorEnter userID: String) {
	// 6.收到 B 进房的通知，播放 B 的画面
	mLiveRoom.startPlay(userID: userID, view: view, callback: callback)
}

// 主播 B：
// 主播 B 创建54321的房间
mLiveRoom.createRoom(roomID: 54321, roomParam: param, callback: nil)

// 2.主播 B 收到主播 A 的消息
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onRequestRoomPK user: TRTCLiveUserInfo, timeout: Double) {
	// 3.主播 B 回复主播 A 接受请求
	mLiveRoom.responseRoomPK(userID: userID, agree: true, reason: reason)
}

public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onAnchorEnter userID: String) {
	// 4.主播 B 收到主播 A 进房的通知，播放主播 A 的画面
	mLiveRoom.startPlay(userID: userID, view: view, callback: callback)
}
```

<span id="model.step9"> </span>
### 步骤9：实现文字聊天和弹幕消息
- 通过`sendRoomTextMsg`可以发送普通的文本消息，所有在该房间内的主播和观众均可以收到`onRecvRoomTextMsg`回调。
即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
```swift
// 发送端：发送文本消息
mLiveRoom.sendRoomTextMsg(message: "Hello Word!", callback: callback)
// 接收端：监听文本消息
mLiveRoom.delegate = self
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onRecvRoomTextMsg message: String, fromUser user: TRTCLiveUserInfo) {
	debugPrint("收到来自\(user.userName)的文本消息:\(message)")
}
```
- 通过`sendRoomCustomMsg`可以发送自定义（信令）的消息，所有在该房间内的主播和观众均可以收到`onRecvRoomCustomMsg`回调。
 自定义消息常用于传输自定义信令，例如用于点赞消息的发送和广播。
```swift
// 发送端：您可以通过自定义Cmd来区分弹幕和点赞消息
// eg:"CMD_DANMU"表示弹幕消息，"CMD_LIKE"表示点赞消息
mLiveRoom.sendRoomCustomMsg(command: "CMD_DANMU", message: "Hello world", callback: nil)
mLiveRoom.sendRoomCustomMsg(command: "CMD_LIKE", message: "", callback: nil)
// 接收端：监听自定义消息
mLiveRoom.delegate = self
public func trtcLiveRoom(_ trtcLiveRoom: TRTCLiveRoomImpl, onRecvRoomCustomMsg command: String, message: String, fromUser user: TRTCLiveUserInfo) {
	if "CMD_DANMU" == command {
		// 收到弹幕消息
		debugPrint("收到来自\(user.userName)的弹幕消息:\(message)")
	} else if "CMD_LIKE" == command {
		// 收到点赞消息
		debugPrint("\(user.userName)给您点了个赞！")
	}
}
```
