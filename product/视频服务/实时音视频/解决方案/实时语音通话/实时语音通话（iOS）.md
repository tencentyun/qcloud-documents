## 效果展示

<table>
<tr>
   <th>主动呼叫</th>
   <th>呼叫接听</th>
 </tr>
<tr>
<td><img src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/audiocall/call.gif"/></td>
<td><img src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/audiocall/recv.gif"/></td>
</tr>
</table>

如需快速实现语音通话功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCAudioCall 组件并实现自定义 UI 界面。

<span id="ui"> </span>
## 复用 Demo 的 UI 界面

<span id="ui.step1"></span>
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如 `TestAudioCall` ，单击【创建应用】。

>! 本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。

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
使用 Xcode（11.0及以上的版本）打开源码工程 `trtcScenesDemo`，单击【运行】即可开始调试本 Demo。

### 步骤5：修改 Demo 源代码
源码文件夹 `TRTCAudioCallDemo` 中包含两个子文件夹 ui 和 model，其中 ui 文件架中均为界面代码：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
| AudioCallViewController.swift | 展示语音通话的主界面，通话的接听和拒绝就是在这个界面中完成的。 | 
| AudioSelectContactViewController.swift | 用于展示选择联系人的界面。 |
| AudioCallMainViewController.swift | 用于展示历史联系人的界面，目前只有发起通话功能。 |
| AudioCallViewController+Data.swift | 用于通话过程中用户画面的渲染和排布逻辑。 | 

<span id="model"> </span>
## 实现自定义 UI 界面
源码文件夹 `TRTCAudioCallDemo` 中包含两个子文件夹 ui 和 model，其中 model 文件夹中包含了我们实现的可重用开源组件 TRTCAudioCall，您可以在  `ITRTCAudioCallInterface.swift `  文件中看到该组件提供的接口函数。
![](https://main.qcloudimg.com/raw/1a75796f96e4d715372f68338d5651c9.jpg)
您可以使用开源组件 TRTCAudioCall 实现自己的 UI 界面，即只复用 model 部分，自行实现 UI 部分。

<span id="model.step1"> </span>
### 步骤1：集成 SDK
语音通话组件 TRTCAudioCall 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。
- **方法一：通过 cocoapods 仓库依赖**
```
pod 'TXIMSDK_iOS'
pod 'TXLiteAVSDK_TRTC'
```
>?两个 SDK 产品的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
>
- **方法二：通过本地依赖**
如果您的开发环境访问 cocoapods 仓库较慢，可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。
<table>
<tr>
<th>SDK</th>
<th>下载页面</th>
<th>集成指引</th>
</tr>
<tr>
<td>TRTC SDK</td>
<td><a href="https://cloud.tencent.com/document/product/647/32689">DOWNLOAD</a></td>
<td><a href="https://cloud.tencent.com/document/product/647/32175">集成文档</a></td>
</tr>
<tr>
<td>IM SDK</td>
<td><a href="https://cloud.tencent.com/document/product/269/36887">DOWNLOAD</a></td>
<td><a href="https://cloud.tencent.com/document/product/269/32679">集成文档</a></td>
</tr>
</table>

<span id="model.step2"> </span>
### 步骤2：配置权限
在 info.plist 文件中需要添加 Privacy - Microphone Usage Description 申请麦克风权限。

<span id="model.step3"> </span>
### 步骤3：导入 TRTCAudioCall 组件

拷贝以下目录中的所有文件到您的项目中：
```
iOS/trtcScenesDemo/trtcScenes/TRTCAudioCallDemo/model
```

<span id="model.step4"> </span>
### 步骤4：初始化并登录组件
1. 调用 `setup()` 初始化组件。
2. 调用 `login(sdkAppID: UInt32, user: String, userSig: String, success: @escaping (() -> Void), failed: @escaping ((_ code: Int, _ message: String) -> Void))` 完成组件的登录，其中几个关键参数的填写请参考下表：
 <table>
<tr>
<th>参数名</th>
<th>作用</th>
</tr>
<tr>
<td>sdkAppID</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr>
<tr>
<td>user</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
</tr>
<tr>
<td>userSig</td>
<td>腾讯云设计的一种安全保护签名，计算方式请参考 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
</tr>
</table>
<pre>
// 初始化
TRTCAudioCall.shared.setup()
TRTCAudioCall.shared.login(sdkAppid, A, password, success, failed)
</pre>

<span id="model.step5"> </span>
### 步骤5：实现 1v1 语音通话
1. 发起方调用 `TRTCAudioCall` 的 `call()` 方法，就能够发起语音通话的请求。
2. 接收方收到 `onInvited()` 事件，此时可以通过 `accept()` 方法接听此次通话，也可以选择用 `reject()` 方法拒绝通话。
3. 发起方收到 `onUserEnter()` 的回调，说明接收方已经进入通话。

```
// 1.初始化
TRTCAudioCall.shared.setup()

// 2.监听回调
TRTCAudioCall.shared.delegate = self

// 接听/拒绝电话
// 此时 B 如果也登录了 IM 系统，会收到 onInvited(A, null, false) 回调
// 可以调用 TRTCAudioCall.shared.accept 接受 / TRTCAudioCall.shared.reject 拒绝
func onInvited(sponsor: String, userIds: [String], isFromGroup: Bool) {
	TRTCAudioCall.shared.accept()
}

// 3.完成组件的登录，登录成功后才可以调用组件的其他功能函数
TRTCAudioCall.shared.login(sdkAppID: sdkAppid, user: A, userSig: Sig, success: {
    // 给 B 拨打电话
    TRTCAudioCall.shared.call(B)
}) { (code, error) in
            
}

// 挂断
TRTCAudioCall.shared.hangup()
// 销毁实例
TRTCAudioCall.shared.destroy()
```

<span id="model.step6"> </span>
### 步骤6：实现多人语音通话
1. 发起方：多人语音通话需要调用 `TRTCAudioCall` 中的 `groupCall()` 函数，并传入用户列表（userIdList）和群组 ID（groupId），其中 userIdList 为必填参数，groupId 为选填参数。
2. 接收端：通过 `onInvited()` 回调能够接收到此次请求。
3. 接收端：收到回调后可以调用 `accept()` 方法接听此次通话，也可以选择用 `reject()` 方法拒绝通话。
4. 如果超过一定时间（默认30s）没有回复，接收方会收到 `onCallingTimeOut()` 的回调，发起方会收到 `onNoResp(String userId)` 回调。通话发起方在多个接收均未应答时 `hangup()` ， 每个接收方均会收到 `onCallingCancel()` 回调。
5. 如果需要离开当前多人通话可以调用 `hangup()` 方法。
6. 如果通话中有用户中途加入或离开，那么其他用户均会接收到 `onUserEnter()` 或  `onUserLeave()` 回调。

>?接口 `groupCall()` 中的 `groupID` 参数是 IM SDK 中的群组 ID，如果填写该参数，那么通话请求消息是通过群消息系统广播出去的，这种消息广播方式比较简单可靠。如果不填写，那么 `TRTCVideoCall` 组件会采用单发消息逐一通知。

```
// 前面省略...
// 拼凑需要拨打的用户列表
var callList: [String] = []
callList.append("b")
callList.append("c")
callList.append("d")
// 如果您不是在一个 IM 群里发起的, groupId 可以传一个空串；
TRTCAudioCall.shared.groupCall(userIDs: callList, groupID: "#groupId#")
```

<span id="offline"> </span>
### 步骤7：实现离线接听
>?如果您的业务定位是在线客服等不需要离线接听功能的场景，那么完成上述 [步骤1](#model.step1) - [步骤6](#model.step6) 的对接即可。但如果您的业务定位是社交场景，建议实现离线接听。

IM SDK 支持离线推送，您需要进行相应的设置才能达到可用标准。

1. 申请 Apple 推送证书，具体操作请参见 [Apple 推送证书申请](https://cloud.tencent.com/document/product/269/3898)。
2. 在后台以及客户端配置离线推送 [离线推送（iOS）](https://cloud.tencent.com/document/product/269/9154)。
3. 修改 login 函数中的 param.busiId 为对应证书 ID。

<span id="api"> </span>
## 组件 API 列表
TRTCAudioCall 组件的 API 接口列表如下：

| 接口函数 | 接口功能 |
|---------|---------|
| setup | 在使用所有功能之前，需要调用该函数进行必要的初始化 | 
| destroy | 销毁实例 |
| setDelegate | 设置 TRTCAudioCallDelegate 代理回调，用户可以通过该回调获取状态通知 |
| login | 登录 IM，所有功能需要先进行登录后才能使用 |
| logout | 登出 IM，登出后无法再进行拨打操作 |
| call | C2C 邀请通话，被邀请方会收到 onInvited 的回调 |
| groupCall | IM 群组邀请通话，被邀请方会收到 onInvited 的回调 |
| accept | 作为被邀请方接听来电 |
| reject | 作为被邀请方拒绝来电 |
| hangup | 结束通话 |
| setMicMute | 是否静音 mic |
| setHandsFree | 是否开启免提 |
