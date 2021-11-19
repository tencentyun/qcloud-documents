## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 效果展示

您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验多人视频会议的效果，包括屏幕分享、美颜、低延时会议等 TRTC 在多人视频会议场景下的相关能力。
<table>
     <tr>
         <th>进入会议</th>  
         <th>屏幕分享</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/meeting1.gif" width="300px" height="640px"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/screencapture.gif" width="300px" height="640px"/></td>
</tr>
</table>

如需快速接入多人视频会议功能，您可以直接基于我们提供的 App 进行修改适配，也可以使用我们提供的 TUIMeeting 组件并实现自定义 UI 界面。

## 复用 App 的 UI 界面
[](id:ui_step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助>[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 输入应用名称，例如 `TestMeetingRoom` ，单击 **创建**。
3. 单击 **已下载，下一步**，跳过此步骤。

![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)
>!本功能同时使用了腾讯云视立方音视频通话 TRTC 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。

[](id:ui_step2)
### 步骤2：下载 App 源码
单击进入 [TUIMeeting](https://github.com/tencentyun/TUIMeeting)，Clone 或者下载源码。

[](id:ui_step3)
### 步骤3：配置 App 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `TUIMeeting/Debug/GenerateTestUserSig.swift` 文件。
3. 设置 `GenerateTestUserSig.swift` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为0，请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</ul>
<img src="https://main.qcloudimg.com/raw/0f2dcf7189d07670343bc8ab9f9697e6.png">
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：运行工程
使用 Xcode（11.0及以上的版本）打开源码工程 `TUIMeeting/TUIMeetingApp.xcworkspace`，单击 **运行** 即可开始调试本 App。

[](id:ui_step5)
### 步骤5：修改工程源代码
源码中的 `Source` 中包含两个子文件夹 Source 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
| TRTCMeetingNewViewController.swift | 视频会议创建界面 UI 实现代码，此类为对 Pods 对外暴露的公共类。 |
| SegmentVC | 设置界面相关 UI 实现代码。 |
| TRTCBroadcastExtensionLauncher.swift | 录屏弹窗相关 UI 实现代码，此类为 Pods 私有类。 |
| TRTCMeetingMainViewController.swift | 视频房间界面 UI 实现代码，此类为 Pods 私有类。 |
| TRTCMeetingMemberViewController.swift | 成员列表界面 UI 实现代码，此类为 Pods 私有类。 |
| TRTCMeetingMoreViewController.swift | 设置界面相关 UI 实现代码，此类为对 Pods 对外暴露的公共类。 |


## 体验应用
>! 体验应用至少需要两台设备。

### 用户 A
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
![](https://main.qcloudimg.com/raw/aacadc7ee6d1267f334fd1d155dcf415.png)
2. 输入会议号，单击 **进入会议**，如下图示：
![](https://main.qcloudimg.com/raw/cce4f1ff06fb55f37b6dffcf819e95c6.png)
3. 输入房间主题，单击 **开始交谈**。

### 用户 B
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
![](https://main.qcloudimg.com/raw/9ac6eb6a300a8f401389008c411f5ed8.png)
2. 输入用户 A 创建的会议号，单击 **进入会议**。
![](https://main.qcloudimg.com/raw/cce4f1ff06fb55f37b6dffcf819e95c6.png)

[](id:model)
## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TUIMeeting) 中的 `Source` 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCMeeting，您可以在`TRTCMeeting.h`文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/bee48f1b790fd81a60f73d07fdb5ecc5.png)


[](id:model.step1)
### 步骤1：集成 SDK
多人视频会议组件 TUIMeeting 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

**方法一：通过 cocoapods 仓库依赖**
<dx-codeblock>
::: swift
 pod 'TXIMSDK_iOS'
 pod 'TXLiteAVSDK_TRTC'
:::
</dx-codeblock>

>? 两个 SDK 产品的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。

**方法二：通过本地依赖**
如果您的开发环境访问 cocoapods 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。

| SDK | 下载页面 | 集成指引 |
|---------|---------|---------|
| TRTC SDK | [DOWNLOAD](https://cloud.tencent.com/document/product/647/32689) | [集成文档](https://cloud.tencent.com/document/product/647/32175) |
| IM SDK | [DOWNLOAD](https://cloud.tencent.com/document/product/269/36887) | [集成文档](https://cloud.tencent.com/document/product/269/32679) |

[](id:model.step2)
### 步骤2：配置权限
在 info.plist 文件中需要添加 `Privacy > Camera Usage Description`， `Privacy > Microphone Usage Description` 申请摄像头和麦克风权限。

[](id:model.step3)
### 步骤3：导入 TUIMeeting 组件
您可通过 **cocoapods 导入组件**，具体步骤如下：
1. 将工程目录下的 `Source`、`Resources`、`TCBeautyKit`、`TXAppBasic` 文件夹、`TUIMeeting.podspec` 文件拷贝到您的工程目录下。
2. 在您的 `Podfile` 文件中添加以下依赖。之后执行`pod install` 命令，完成导入。
<dx-codeblock>
::: swift
 pod 'TXAppBasic', :path => "TXAppBasic/"
 pod 'TCBeautyKit', :path => "TCBeautyKit/"
 pod 'TXLiteAVSDK_TRTC'
 pod 'TUIMeeting', :path => "./", :subspecs => ["TRTC"] 
:::
</dx-codeblock>

[](id:model.step4)
### 步骤4：创建并登录组件
1. 调用 `sharedInstance` 接口可以创建一个 TRTCMeeting 组件的实例对象。
2. 调用 `setDelegate` 函数注册组件的事件通知。
3. 调用 `login` 函数完成组件的登录，请参考下表填写关键参数：
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

<dx-codeblock>
::: swift swift
let userID = ProfileManager.shared().curUserID()
let userSig = GenerateTestUserSig.genTestUserSig(userID)

TRTCMeeting.sharedInstance().login(SDKAPPID, userId: userID, userSig: userSig, callback: { code, message in
    if code == 0 {
        //登录成功
    }
})
:::
</dx-codeblock>

[](id:model.step5)
### 步骤5：创建多人会议
1. 主持人执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 主持人调用 `setDelegate` 可以进行事件调用 `createMeeting` 创建新的会议房间。
3. 主持人可以调用 `startCameraPreview` 进行视频画面的采集，也可以调用 `startMicrophone` 进行声音的采集。
4. 如果主持人有美颜的需求，界面上可以配置美颜调节按钮调用，通过 `getBeautyManager` 进行美颜设置。
>? 非企业版 SDK 不支持变脸和贴图挂件功能。

![](https://main.qcloudimg.com/raw/6e0cf097f46a8953cbebcf9995ba28c1.png)

<dx-codeblock>
::: swift swift
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
:::
</dx-codeblock>

[](id:model.step6)
### 步骤6：参会成员进入多人会议
1. 参会成员执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 参会成员调用 `enterMeeting` 并传入会议房间号即可进入会议房间。
3. 参会成员可以调用 `startCameraPreview` 进行视频画面的采集，调用 `startMicrophone` 进行声音的采集。
4. 如果有其他的参会成员打开了摄像头，会收到 `onUserVideoAvailable` 的事件，此时可以调用 `startRemoteView` 并传入 userId 开始播放。

![](https://main.qcloudimg.com/raw/d8b796bbe41c9da1af40740916e84d70.png)

<dx-codeblock>
::: swift swift
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
:::
</dx-codeblock>

<dx-codeblock>
::: swift swift
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
:::
</dx-codeblock>

[](id:model.step7)
### 步骤7：屏幕分享
1. 调用 `startScreenCapture`，传入编码参数和录屏过程中的悬浮窗即可实现屏幕分享功能，具体信息请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a59b16baa51d86cc0465dc6edd3cbfc97)。
2. 会议中其他成员会收到 `onUserVideoAvailable` 的事件通知。

>!屏幕分享和摄像头采集是两个互斥的操作，如果需要打开屏幕分享功能，请先调用`stopCameraPreview` 关闭摄像头采集。

<dx-codeblock>
::: swift swift
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
:::
</dx-codeblock>

[](id:model.step8)
### 步骤8：实现文字聊天和禁言消息
- 通过 `sendRoomTextMsg` 可以发送普通的文本消息，所有在该房间内的主播和观众均可以收到 `onRecvRoomTextMsg` 回调。
即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
<dx-codeblock>
::: swift swift
// 发送端：发送文本消息
TRTCMeeting.sharedInstance().sendRoomTextMsg("Hello Word!") { (code, message) in
  debugPrint("send result: ", code)
}

// 接收端：监听文本消息
func onRecvRoomTextMsg(_ message: String?, userInfo: TRTCMeetingUserInfo) {
  debugPrint("收到来自:\(String(describing: userInfo.userId))的消息\(String(describing: message))")
}
:::
</dx-codeblock>
- 通过`sendRoomCustomMsg`可以发送自定义（信令）的消息，所有在该房间内的主持人和与会观众均可以收到`onRecvRoomCustomMsg`回调。
自定义消息常用于传输自定义信令，例如用于禁言之类的会场控制等。
<dx-codeblock>
::: swift swift
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
:::
</dx-codeblock>
