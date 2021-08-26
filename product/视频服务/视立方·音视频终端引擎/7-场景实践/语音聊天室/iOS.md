## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 效果展示

您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验语音聊天室的能力，包括麦位管理、低延时语音互动、文字聊天等音视频通话 TRTC 在语音聊天场景下的相关能力。
<table>
     <tr>
         <th>房主麦位操作</th>  
         <th>听众麦位操作</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/voiceroom_pick_seat.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/voiceroom_enter_seat.gif"/></td>
</tr>
</table>

如需快速接入语音聊天室功能，您可以直接基于我们提供的 App 进行修改适配，也可以使用我们提供的 TUIVoiceRoom 组件并实现自定义 UI 界面。

[](id:DemoUI)
## 复用 App 的 UI 界面

[](id:ui.step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助** > **[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 输入应用名称，例如  `TestVoiceRoom`，单击 **创建**。
3. 单击 **已下载，下一步**，跳过此步骤。

![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

>?本功能同时使用了腾讯云视立方音视频通话 TRTC 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。



[](id:ui.step2)
### 步骤2：下载 App 源码
单击进入 [TUIVoiceRoom](https://github.com/tencentyun/TUIVoiceRoom)，Clone 或者下载源码。

[](id:ui.step3)
### 步骤3：配置 App 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `TUIVoiceRoom/Debug/GenerateTestUserSig.swift` 文件。
3. 设置 `GenerateTestUserSig.swift` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为0，请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</ul>
<img src="https://main.qcloudimg.com/raw/a226f5713e06e014515debd5a701fb63.png">
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui.step4)
### 步骤4：运行 App
使用 Xcode（11.0及以上的版本）打开源码工程 `TUIVoiceRoom/TUIVoiceRoomApp.xcworkspace`，单击 **运行** 即可开始调试本 App。

[](id:ui.step5)
### 步骤5：修改 App 源代码
源码中的 `Source` 文件夹包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码以及涉及界面相关的逻辑，如下表格列出了各个 swift 文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
|TRTCVoiceRoomEnteryControl.swift|该文件包含所有 ViewController 的初始化获取方法，您可以通过该实例，快速获取 ViewController 对象。|
| TRTCCreateVoiceRoomViewController | 创建语音聊天室页面逻辑。 |
| TRTCVoiceRoomViewController | 主房间页面，包括房主和听众两种界面。 |

每个 `TRTC'XXXX'ViewController` 文件夹下均包含 `ViewController`、`RootView` 和 `ViewModel`，各个文件的作用如下表所示：

| 文件 | 功能描述 |
|:-------:|:--------|
| ViewController.swift | 页面控制器，负责页面路由工作，以及 RootView 和 ViweModel 的绑定工作。 |
| RootView.swift | 视图，所有的视图布局。 |
| ViewModel.swift | 视图控制器，负责响应视图交互，返回视图响应状态。 |

## 体验应用
>! 体验应用至少需要两台设备。

### 用户 A

1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
![](https://main.qcloudimg.com/raw/aacadc7ee6d1267f334fd1d155dcf415.png)
2. 单击 **创建房间**，如下图示：
![](https://main.qcloudimg.com/raw/a3b5fbb862612c7200253a55f703e7b7.png)
2. 输入房间主题，单击 **开始交谈**。

### 用户 B
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
![](https://main.qcloudimg.com/raw/9ac6eb6a300a8f401389008c411f5ed8.png)
2. 输入用户 A 创建的房间号，单击 **进入房间**。
![](https://main.qcloudimg.com/raw/bd2945dfe6e9b586c2f71aa94cde18d8.png)

>! 房间号在用户 A 的房间顶部查看，如下图示：
![](https://main.qcloudimg.com/raw/02d44e3839798d6ab6aebf55de8cc273.png)

[](id:model)
## 实现自定义 UI 界面
[源码](https://github.com/tencentyun/TUIVoiceRoom) 中的 `Source` 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCVoiceRoom，您可以在 `TRTCVoiceRoom.h` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/0ebcbb27843bf03a790a945a8c92d560.png)


[](id:model.step1)
### 步骤1：集成 SDK
语音聊天组件 TRTCVoiceRoom 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

- **方法一：通过 cocoapods 仓库依赖**
   <dx-codeblock>
   ::: swift
   pod 'TXIMSDK_iOS'
   pod 'TXLiteAVSDK_TRTC'
   :::
   </dx-codeblock>
>?两个 SDK 产品的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 GitHub 首页获取。
- **方法二：通过本地依赖**
如果您的开发环境访问 cocoapods 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。
<table>
<tr><th>SDK</th><th>下载页面</th><th>集成指引</th></tr>
<tr>
<td>TRTC SDK</td>
<td><a href="https://cloud.tencent.com/document/product/647/32689">DOWNLOAD</a></td>
<td><a href="https://cloud.tencent.com/document/product/647/32175">集成文档</a></td>
</tr><tr>
<td>IM SDK</td>
<td><a href="https://cloud.tencent.com/document/product/269/36887">DOWNLOAD</a></td>
<td><a href="https://cloud.tencent.com/document/product/269/32679">集成文档</a></td>
</tr></table>

[](id:model.step2)
### 步骤2：配置权限
在 info.plist 文件中需要添加 `Privacy > Camera Usage Description`， `Privacy > Microphone Usage Description` 申请麦克风权限。

[](id:model.step3)
### 步骤3：导入 TUIVoiceRoom 组件
**通过 cocoapods 导入组件**，具体操作如下：
1. 将工程目录下的 `Source`、`Resources`、`TXAppBasic` 文件夹、`TUIVoiceRoom.podspec` 文件拷贝到您的工程目录下。
2. 在您的 `Podfile` 文件中添加以下依赖。之后执行 `pod install` 命令，完成导入。
<dx-codeblock>
::: swift
pod 'TXAppBasic', :path => "TXAppBasic/"
pod 'TXLiteAVSDK_TRTC'
pod 'TUIVoiceRoom', :path => "./", :subspecs => ["TRTC"] 
:::
</dx-codeblock>

[](id:model.step4)
### 步骤4：创建并登录组件
1. 调用 TRTCVoiceRoom 的 `sharedInstance` 类方法可以创建一个遵守 TRTCVoiceRoom 协议的实例对象。也可以使用调用 `shared` 类方法，获取 TRTCVoiceRoomImp实例对象直接使用，二者在 TRTCVoiceRoom 的接口使用上没有任何区别。
2. 调用 `setDelegate` 函数注册组件的事件回调通知。
3. 调用 `login` 函数完成组件的登录，请参考下表填写关键参数：
<table>    
<tr><th>参数名</th><th>作用</th></tr><tr>
<td>sdkAppId</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr><tr>
<td>userId</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z、A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
</tr><tr>
<td>userSig</td>
<td>腾讯云设计的一种安全保护签名，获取方式请参见 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
</tr></tr>
<tr>
<td>callback</td>
<td>登录回调，成功时 code 为0。</td>
</tr></table>

<dx-codeblock>
::: Swift Swift
// Swift 示例
// 您代码里负责业务逻辑的类
class YourController {
    // 计算属性获取单例对象
    var voiceRoom: TRTCVoiceRoomImp {
        return TRTCVoiceRoomImp.shared()
    }
    
    // 其他代码逻辑
    ......
}
// 设置 voiceroom 代理
self.vocieRoom. setDelegate(delegate: voiceRoomDelegate)

// 调用方式如下,闭包内建议使用 weak self 防止循环引用（下面示例代码省略 weak self 示例）
self.vocieRoom.login(sdkAppId: sdkAppID, userId: userId, userSig: userSig) { [weak self] (code, message) in
    guard let `self` = self else { return }
    // 您的回调业务逻辑        
}
:::
</dx-codeblock>

[](id:model.step5)
### 步骤5：房主端开播
1. 房主执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 房主调用 `createRoom` 创建新的语音聊天室，此时传入房间 ID、上麦是否需要房主确认、麦位数等房间属性信息。
3. 房主创建房间成功后，调用 `enterSeat` 进入座位。
4. 房主收到组件的 `onSeatListChange` 麦位表变化事件通知，此时可以将麦位表变化刷新到 UI 界面上。
5. 房主还会收到麦位表有成员进入的 `onAnchorEnterSeat` 的事件通知，此时会自动打开麦克风采集。

![](https://main.qcloudimg.com/raw/178d40c1ae247fbf7d5171dc4cee1a5a.png)

示例代码：
<dx-codeblock>
::: swift
// 1.房主设置昵称和头像
self.voiceRoom.setSelfProfile(userName: userName, avatarUrl: avatarURL) { (code, message) in
    // 结果回调           
}

// 2.房主端创建房间
let param = VoiceRoomParam.init()
param.roomName = "房间名称"
param.needRequest = true // 听众上麦是否需要房主同意
param.coverUrl = "封面URL"
param.seatCount = 7 // 房间座位数，这里一共7个座位，房主占了一个后听众剩下6个座位
param.seatInfoList = []

for _ in 0..< param.seatCount {
    let seatInfo = VoiceRoomSeatInfo.init()
    param.seatInfoList.append(seatInfo)
}

self.voiceRoom.createRoom(roomID: yourRoomID, roomParam: param) { (code, message) in
    guard code == 0 else { reutrn }
    // 创建房间成功后开始占座
    self.voiceRoom.enterSeat(seatIndex: 0) { [weak self] (code, message) in
        guard let `self` = self else { return }
        if code == 0 {
            // 房主占座成功
        } else {
            // 房主占座失败
        }
    }
}

// 3.占座成功后，收到 onSeatListChange 事件通知
func onSeatListChange(seatInfoList: [VoiceRoomSeatInfo]) {
    // 刷新您的麦位列表
}

// 4. 收到 onAnchorEnterSeat 事件通知
func onAnchorEnterSeat(index: Int, user: VoiceRoomUserInfo) {
  // 处理房主上麦事件
}

:::
</dx-codeblock>

[](id:model.step6)
### 步骤6：听众端观看
1. 听众端执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 听众端向业务后台获取最新的语音聊天室房间列表。
>?App 中的语音聊天室列表仅做演示使用，语音聊天室列表的业务逻辑千差万别，腾讯云暂不提供语音聊天室列表的管理服务，请自行管理您的语音聊天室列表。
3. 听众端调用 `getRoomInfoList` 获取房间的详细信息，该信息是在房主端调用`createRoom`创建语音聊天室时设置的简单描述信息。
>!如果您的语音聊天室列表包含了足够全面的信息，可跳过调用 `getRoomInfoList` 相关步骤。
4. 听众选择一个语音聊天室，调用 `enterRoom` 并传入房间号即可进入该房间。
5. 进房后会收到组件的 `onRoomInfoChange` 房间属性变化事件通知，此时可以记录房间属性并做相应改变，例如 UI 展示房间名、记录上麦是否需要请求房主同意等。
6. 进房后会收到组件的 `onSeatListChange` 麦位表变化事件通知，此时可以将麦位表变化刷新到 UI 界面上。
7. 进房后还会收到麦位表有主播进入的 ` onAnchorEnterSeat` 的事件通知。

![](https://main.qcloudimg.com/raw/78fd2cc28f7f336de6fa58248b28cc14.png)


<dx-codeblock>
::: Swift Swift
// 1.听众设置昵称和头像
self.voiceRoom.setSelfProfile(userName: userName, avatarUrl: avatarURL) { (code, message) in
    // 结果回调           
}

// 2.假定您从业务后台获取房间列表为 roomList
let roomList: [Int] = getRoomIDList() // 您获取房间ID列表的函数

// 3.通过调用 getRoomInfoList 获取房间的详细信息
self.voiceRoom.getRoomInfoList(roomIdList: roomIdsInt) { (code, message, roomInfos: [VoiceRoomInfo]) in
    // 获取结果，此时可以刷新UI
}

// 4.选择语音聊天室后，传入 roomId 进入房间
self.voiceRoom.enterRoom(roomID: roomInfo.roomID) { (code, message) in
    // 进入房间结果回调
    if code == 0 {
       // 进房成功
    }
}

// 5.进房成功后，收到 onRoomInfoChange 事件通知
func onRoomInfoChange(roomInfo: VoiceRoomInfo) {
    // 可以更新房间名称等信息
}

// 6.进房成功后，收到 onSeatListChange 事件通知
func onSeatListChange(seatInfoList: [VoiceRoomSeatInfo]) {
    // 刷新麦位列表
}

// 7. 收到 onAnchorEnterSeat 事件通知
func onAnchorEnterSeat(index: Int, user: VoiceRoomUserInfo) {
    // 处理上麦事件
}
:::
</dx-codeblock>

[](id:model.step7)
### 步骤7：麦位管理
<dx-tabs>
::: 房主端
1. `pickSeat` 传入对应的麦位和听众 userId，可以抱人上麦，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorEnterSeat` 的事件通知。
2. `kickSeat` 传入对应麦位后，可以踢人下麦，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorLeaveSeat` 的事件通知。
3. `muteSeat` 传入对应麦位后，可以静音/解除静音，房间内所有成员会收到 `onSeatListChange` 和 `onSeatMute` 的事件通知。
4. `closeSeat` 传入对应麦位后，可以封禁/解禁某个麦位，封禁后听众端将不能再上麦，房间内所有成员会收到` onSeatListChange` 和 `onSeatClose` 的事件通知。
![](https://main.qcloudimg.com/raw/78a1d790bf994786f5beac8b97660000.png)
:::
::: 听众端
1. `enterSeat`传入对应的麦位后，可以进行上麦，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorEnterSeat` 的事件通知。
2. `leaveSeat` 主动下麦，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorLeaveSeat` 的事件通知。

![](https://main.qcloudimg.com/raw/356fddebf48c7a4ef918104e8f6e64eb.png)

麦位操作后的事件通知顺序如下：callback > onSeatListChange > onAnchorEnterSeat 等独立事件。

<dx-codeblock>
::: swift
// case1: 房主抱人上1号麦位
self.voiceRoom.pickSeat(seatIndex: 1, userId: "123") { (code, message) in
    // 结果回调
}

// 3.收到 onSeatListChange 回调，刷新您的麦位列表
func onSeatListChange(seatInfoList: [VoiceRoomSeatInfo]) {
    // 刷新的麦位列表
}

// 4.单个麦位变化的通知，可以在这里判断听众是不是真的上麦成功
func onAnchorEnterSeat(index: Int, user: VoiceRoomUserInfo) {
    // 处理上麦事件
}
:::
</dx-codeblock>

<dx-codeblock>
::: swift
// case2: 听众主动上2号麦位
voiceRoom.enterSeat(seatIndex: 2) { (code, message) in
    // 上麦结果回调
}

// 3.收到 onSeatListChange 回调，刷新您的麦位列表
func onSeatListChange(seatInfoList: [VoiceRoomSeatInfo]) {
    // 刷新的麦位列表
}

// 4.单个麦位变化的通知，可以在这里判断是不是自己并进行相应处理
func onAnchorEnterSeat(index: Int, user: VoiceRoomUserInfo) {
    // 处理上麦事件
}
:::
</dx-codeblock>
:::
</dx-tabs>

[](id:model.step8)
### 步骤8：邀请信令的使用
在 [麦位管理](#model.step7) 中，听众上下麦、房主抱人上麦都不需要经过对方的同意就可以直接操作。
如果您的 App 需要对方同意才能进行下一步操作的业务流程，那么邀请信令可以提供相应支持。
<dx-tabs>
::: 听众主动申请上麦
1. 听众端调用 `sendInvitation` 传入房主的 userId 和业务的自定义命令字等，此时函数会返回一个 inviteId，记录该 inviteId。
2. 房主端收到 `onReceiveNewInvitation` 的事件通知，此时 UI 可以弹窗并询问房主是否同意。
3. 房主选择同意后，调用 `acceptInvitation` 并传入 inviteId。
4. 听众端收到 `onInviteeAccepted` 的事件通知，调用 `enterSeat` 进行上麦。

![](https://main.qcloudimg.com/raw/9419f9ae95c89b3bedb0839846e7565c.png)

<dx-codeblock>
::: Swift Swift
// 听众端视角
// 1.调用 sendInvitation，请求上1号麦位
let inviteId = self.voiceRoom.sendInvitation(cmd: "ENTER_SEAT", userId: ownerUserId, content: "1") { (code, message) in
    // 发送结果回调
}
// 2.收到邀请的同意请求, 正式上麦
func onInviteeAccepted(identifier: String, invitee: String) {
    if identifier == selfID {
        self.voiceRoom.enterSeat(seatIndex: ) { (code, message) in
            // 上麦结果回调
        }
    }
}

// 房主端视角
// 1.房主收到请求
func onReceiveNewInvitation(identifier: String, inviter: String, cmd: String, content: String) {
    if cmd == "ENTER_SEAT" {
        // 2.房主同意听众请求
        self.voiceRoom.acceptInvitation(identifier: identifier, callback: nil)
    }
}
:::
</dx-codeblock>
:::
::: 房主邀请听众上麦
1. 房主端调用 `sendInvitation` 传入听众的 userId 和业务的自定义命令字等，此时函数会返回一个 inviteId，记录该 inviteId。
2. 听众端收到 `onReceiveNewInvitation` 的事件通知，此时 UI 可以弹窗并询问听众是否同意上麦。
3. 听众选择同意后，调用 `acceptInvitation` 并传入 inviteId。
4. 房主端收到 `onInviteeAccepted` 的事件通知，调用 `pickSeat` 抱听众上麦。

![](https://main.qcloudimg.com/raw/9a22e5d5f4be720775091bfd3ffef48a.png)

<dx-codeblock>
::: java java
// 房主端视角
// 1.房主调用 sendInvitation，请求抱听众“123”上2号麦
let inviteId = self.voiceRoom.sendInvitation(cmd: "PICK_SEAT", userId: ownerUserId, content: "2") { (code, message) in
    // 发送结果回调
}

// 2.收到邀请的同意请求, 正式上麦
func onInviteeAccepted(identifier: String, invitee: String) {
    if identifier == selfID {
        self.voiceRoom.pickSeat(seatIndex: ) { (code, message) in
            // 上麦结果回调
        }
    }
}

// 听众端视角
// 1.听众收到请求
func onReceiveNewInvitation(identifier: String, inviter: String, cmd: String, content: String) {
    if cmd == "PICK_SEAT" {
        // 2.听众同意房主请求
        self.voiceRoom.acceptInvitation(identifier: identifier, callback: nil)
    }
}
:::
</dx-codeblock>
:::
</dx-tabs>

[](id:model.step9)
### 步骤9：实现文字聊天和弹幕消息
- 通过` sendRoomTextMsg` 可以发送普通的文本消息，所有在该房间内的主播和听众均可以收到 `onRecvRoomTextMsg` 回调。
  即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
  <dx-codeblock>
  ::: Swift Swift
  // 发送端：发送文本消息
  self.voiceRoom.sendRoomTextMsg(message: message) { (code, message) in
         

}
// 接收端：监听文本消息
func onRecvRoomTextMsg(message: String, userInfo: VoiceRoomUserInfo) {
    //收到的message信息处理方法        
}
:::
</dx-codeblock>
- 通过 `sendRoomCustomMsg` 可以发送自定义（信令）的消息，所有在该房间内的主播和听众均可以收到 `onRecvRoomCustomMsg` 回调。
 自定义消息常用于传输自定义信令，例如用于点赞消息的发送和广播。
  <dx-codeblock>
  ::: Swift Swift
  // 例如：发送端：您可以通过自定义Cmd来区分弹幕和点赞消息
  // eg:"CMD_DANMU"表示弹幕消息，"CMD_LIKE"表示点赞消息
  self.vocieRoom.sendRoomCustomMsg(cmd: “CMD_DANMU”, message: "hello world", callback: nil)
  self.voiceRoom.sendRoomCustomMsg(cmd: "CMD_LIKE", message: "", callback: nil)
  // 接收端：监听自定义消息
  func onRecvRoomCustomMsg(cmd: String, message: String, userInfo: VoiceRoomUserInfo) {
    if cmd == "CMD_DANMU" {
        // 收到弹幕消息
    }
    if cmd == "CMD_LIKE" {
        // 收到点赞消息
    }
  }
  :::
  </dx-codeblock>
