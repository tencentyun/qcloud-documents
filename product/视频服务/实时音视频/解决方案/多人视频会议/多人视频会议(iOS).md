## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 Demo 体验多人视频会议的效果，包括屏幕分享、美颜、低延时会议等 TRTC 在多人视频会议场景下的相关能力。

<table>
     <tr>
         <th>进入会议</th>  
         <th>屏幕分享</th>  
     </tr>
<tr>
<td><img src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/gif/enterroom.gif"/></td>
<td><img src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/gif/screencapture.gif"/></td>
</tr>
</table>

如需快速接入多人视频会议功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCMeeting 组件并实现自定义 UI 界面。

## 复用 Demo 的 UI 界面

### 步骤1：创建新的应用

1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如 `TestMeetingRoom` ，单击【创建应用】。

>? 本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。



### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/iOS)】跳转至 Github（或单击【[ZIP](https://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_iOS_latest.zip)】），下载相关 SDK 及配套的 Demo 源码。
 ![](https://main.qcloudimg.com/raw/716b5af9207ad2b11835dec4e2d15da0.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。

### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#ui.step2) 中下载的源码包。
2. 找到并打开 `iOS/TRTCScenesDemo/TXLiteAVDemo/Debug/GenerateTestUserSig.h` 文件。
3. 设置 `GenerateTestUserSig.h` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
    <img src="https://main.qcloudimg.com/raw/15d986c5f4bc340e555630a070b90d63.png">
4. 返回实时音视频控制台，单击【粘贴完成，下一步】。
5. 单击【关闭指引，进入控制台管理应用】。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：运行 Demo
使用 Xcode（11.0及以上的版本）打开源码工程 `iOS/TRTCScenesDemo/TXLiteAVDemo.xcworkspace`，单击【运行】即可开始调试本 Demo。

### 步骤5：修改 Demo 源代码
源码中的 ``trtcmeetingdemo`` 中包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
| SegmentVC | 设置界面相关 UI 实现代码。 |
| TRTCBroadcastExtensionLauncher.swift | 录屏弹窗相关 UI 实现代码。 |
| TRTCMeetingNewViewController | 视频会议创建界面 UI 实现代码。 |
| TRTCMeetingMainViewController | 视频房间界面 UI 实现代码。 |
| TRTCMeetingMemberViewController | 成员列表界面 UI 实现代码。 |
| TRTCMeetingMoreViewController | 设置界面相关 UI 实现代码。 |


<span id="model"> </span>
## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/TRTCScenesDemo/TXLiteAVDemo/TRTCMeetingDemo) 中的 trtcmeetingdemo 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCMeeting，您可以在`TRTCMeeting.h`文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/bee48f1b790fd81a60f73d07fdb5ecc5.png)


<span id="model.step1"> </span>
### 步骤1：集成 SDK
多人视频会议组件 TRTCMeeting 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

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
### 步骤3：导入 TRTCMeeting 组件
拷贝`iOS/LiteAVDemo/TXLiteAVDemo/TRTCMeetingDemo/model`目录中的所有文件到您的项目中。

<span id="model.step4"> </span>
### 步骤4：创建并登录组件
1. 调用`sharedInstance`接口可以创建一个 TRTCMeeting 组件的实例对象。
2. 调用`setDelegate`函数注册组件的事件通知。
3. 调用`login`函数完成组件的登录，请参考下表填写关键参数：
<table> 
<tr>
<th>参数名</th>
<th>作用</th>
</tr><tr>
<td>sdkAppId</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr><tr>
<td>userId</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z、A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
</tr><tr>
<td>userSig</td>
<td>腾讯云设计的一种安全保护签名，获取方式请参考 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
</tr><tr>
<td>callback</td>
<td>登录回调，成功时 code 为0。</td>
</tr>
</table>

```swift
let userID = ProfileManager.shared().curUserID()
let userSig = GenerateTestUserSig.genTestUserSig(userID)

TRTCMeeting.sharedInstance().login(SDKAPPID, userId: userID, userSig: userSig, callback: { code, message in
    if code == 0 {
        //登录成功
    }
})
```

<span id="model.step5"> </span>
### 步骤5：创建多人会议
1. 主持人执行 [步骤4](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 主持人调用`setDelegate`可以进行事件调用`createMeeting`创建新的会议房间。
3. 主持人可以调用`startCameraPreview`进行视频画面的采集，也可以调用`startMicrophone`进行声音的采集。
4. 如果主持人有美颜的需求，界面上可以配置美颜调节按钮调用，通过`getBeautyManager`进行美颜设置。
>? 非企业版 SDK 不支持变脸和贴图挂件功能。

![](https://main.qcloudimg.com/raw/6e0cf097f46a8953cbebcf9995ba28c1.png)

```swift
// 1.主播设置昵称和头像
trtcMeeting.setSelfProfile(name: "A", avatarURL: "faceUrl", callback: nil)

// 2.主播创建房间
trtcMeeting.createMeeting(roomId) { (code, msg) in
 if code == 0 {
   // 创建房间成功
  let localPreviewView=getRenderView(userId: selfUserId)!
  TRTCMeeting.sharedInstance().startCameraPreview(true, view: localPreviewView)
  TRTCMeeting.sharedInstance().startMicrophone();
  
  // 使用默认的美颜参数
  beautyPannel.resetAndApplyValues()
  return;
 }
}
```

<span id="model.step6"> </span>
### 步骤6：参会成员进入多人会议
1. 参会成员执行 [步骤4](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 参会成员调用`enterMeeting`并传入会议房间号即可进入会议房间。
3. 参会成员可以调用`startCameraPreview`进行视频画面的采集，调用`startMicrophone`进行声音的采集。
4. 如果有其他的参会成员打开了摄像头，会收到`onUserVideoAvailable`的事件，此时可以调用`startRemoteView`并传入 userId 开始播放。

![](https://main.qcloudimg.com/raw/d8b796bbe41c9da1af40740916e84d70.png)

```swift
// 1.参会成员设置昵称和头像
trtcMeeting.setSelfProfile(name: "A", avatarURL: "faceUrl", callback: nil)

// 2.enterMeeting 函数实现
trtcMeeting.enterMeeting(roomId) { (code, msg) in
   if code == 0{
     trtcMeeting.startCameraPreview(true, view: localPreviewView)
     trtcMeeting.startMicrophone()
   } else {
      self.view.makeToast("会议进入失败：" + msg!)
   }
}
```

```swift
let renderView = getRenderView(userId: userId)
if available && renderView != nil {
  //收到回调，并调用 startRemoteView，传入 userId 开始播放
  TRTCMeeting.sharedInstance().startRemoteView(userId, view: renderView!) { (code, message) in
   debugPrint("startRemoteView" + "\(code)" + message!)
  }
} else {
 TRTCMeeting.sharedInstance().stopRemoteView(userId) { (code, message) in
   debugPrint("stopRemoteView" + "\(code)" + message!)
  }
}
//刷新当前界面
renderView?.refreshVideo(isVideoAvailable: available)
```

<span id="model.step7"> </span>
### 步骤7：屏幕分享
1. 调用 `startScreenCapture`，传入编码参数和录屏过程中的悬浮窗即可实现屏幕分享功能，具体信息请参见 [TRTC SDK](http://doc.qcloudtrtc.com/group__TRTCCloud__ios.html#a59b16baa51d86cc0465dc6edd3cbfc97)。
2. 会议中其他成员会收到 `onUserVideoAvailable` 的事件通知。

>!屏幕分享和摄像头采集是两个互斥的操作，如果需要打开屏幕分享功能，请先调用`stopCameraPreview`关闭摄像头采集。

```swift
// 1.按钮点击实现屏幕分享
if #available(iOS 12.0, *) {
  // 录屏前必须先关闭摄像头采集
  self.setLocalVideo(isVideoAvailable: false)
  
  // 屏幕分享
  let params = TRTCVideoEncParam()
  params.videoResolution = TRTCVideoResolution._1280_720
  params.videoFps = 10
  params.videoBitrate = 1800
  TRTCMeeting.sharedInstance().startScreenCapture(params)
  TRTCBroadcastExtensionLauncher.launch()
} else {
  self.view.makeToast("系统版本低于12.0，请升级系统")
}     
```

<span id="model.step8"> </span>
### 步骤8：实现文字聊天和禁言消息
- 通过`sendRoomTextMsg`可以发送普通的文本消息，所有在该房间内的主播和观众均可以收到`onRecvRoomTextMsg`回调。
即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。

```swift
// 发送端：发送文本消息
TRTCMeeting.sharedInstance().sendRoomTextMsg("Hello Word!") { (code, message) in
  debugPrint("send result: ", code)
}

// 接收端：监听文本消息
func onRecvRoomTextMsg(_ message: String?, userInfo: TRTCMeetingUserInfo) {
  debugPrint("收到来自:\(String(describing: userInfo.userId))的消息\(String(describing: message))")
}
```

- 通过`sendRoomCustomMsg`可以发送自定义（信令）的消息，所有在该房间内的主持人和与会观众均可以收到`onRecvRoomCustomMsg`回调。
自定义消息常用于传输自定义信令，例如用于禁言之类的会场控制等。

```swift
// 发送端：您可以通过自定义 Cmd 来区分禁言通知
// eg:"CMD_MUTE_AUDIO"表示禁言通知
TRTCMeeting.sharedInstance().sendRoomCustomMsg("CMD_MUTE_AUDIO", message: "1") { (code, message) in
  debugPrint("send result: ", code)
}

// 接收端：监听自定义消息
func onRecvRoomCustomMsg(_ cmd: String?, message: String?, userInfo: TRTCMeetingUserInfo) {
  if cmd == "CMD_MUTE_AUDIO" {
    debugPrint("收到来自:\(String(describing: userInfo.userId))的禁言通知:\(String(describing: message))")
    TRTCMeeting.sharedInstance().muteLocalAudio(message == "1")
  }
}
```

