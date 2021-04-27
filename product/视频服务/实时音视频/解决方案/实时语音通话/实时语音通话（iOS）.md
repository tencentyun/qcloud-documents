## 效果展示

<table>
<tr>
   <th>主动呼叫</th>
   <th>被叫接听</th>
 </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/call.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/recv.gif"/></td>
</tr>
</table>


如需快速实现语音通话功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCCalling 组件并实现自定义 UI 界面。

>! 我们之前提供了  TRTCAudioCall 组件，旧版本组件已经移动到 [组件仓库](https://github.com/tencentyun/LiteAVClassic) 中。TRTCCalling 组件使用了 IM 信令的接口，将不再与旧组件兼容。

[](id:ui)

## 复用 Demo 的 UI 界面

[](id:ui.step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如 `TestVideoCall` ，单击【创建】。

>! 本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。

[](id:ui.step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 Demo 源码。
2. 下载完成后，单击【已下载，下一步】。
![](https://main.qcloudimg.com/raw/3b115019ddfd0866108ed1add30810d8.png)

[](id:ui.step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `iOS/TRTCScenesDemo/TXLiteAVDemo/Debug/GenerateTestUserSig.h` 文件。
3. 设置 `GenerateTestUserSig.h` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为0，请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</ul>
<img src="https://main.qcloudimg.com/raw/dc51102e39c2a913aacb6789e06c25e4.png">
4. 粘贴完成后，单击【已复制粘贴，下一步】即创建成功。
5. 编译完成后，单击【回到控制台概览】即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui.step4)

### 步骤4：运行 Demo

使用 Xcode（11.0及以上的版本）打开源码工程 `iOS/TRTCScenesDemo/TXLiteAVDemo.xcworkspace`，单击【运行】即可开始调试本 Demo。

[](id:ui.step5)

### 步骤5：修改 Demo 源代码

源码文件夹 `TRTCCallingDemo` 中包含两个子文件夹 ui 和 model，其中 ui 文件夹中均为界面代码：

|              文件或文件夹              | 功能描述                                                 |
| ------------------------------------ | ------------------------------------------------------- |
|  TRTCCallingVideoViewController.swift  | 展示视频通话的主界面，通话的接听和拒绝在这个界面中完成。 |
|  TRTCCallingAudioViewController.swift  | 展示语音通话的主界面，通话的接听和拒绝在这个界面中完成。 |
| TRTCCallingContactViewController.swift | 用于展示搜索联系人的界面。                               |


[](id:model)

## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/TRTCScenesDemo/TXLiteAVDemo/TRTCCallingDemo) 文件夹 `TRTCCallingDemo` 中包含两个子文件夹 ui 和 model，其中 model 文件夹中包含了我们实现的可重用开源组件 TRTCCalling，您可以在  `TRTCCalling.h`  文件中看到该组件提供的接口函数。
![](https://main.qcloudimg.com/raw/36220937e8689dac4499ce9f2f187889.png)

您可以使用开源组件 TRTCCalling 实现自己的 UI 界面，即只复用 model 部分，自行实现 UI 部分。

[](id:model.step1)

### 步骤1：集成 SDK

通话组件 TRTCCalling 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

- **方法一：通过 cocoapods 仓库依赖**
```
pod 'TXIMSDK_iOS'
pod 'TXLiteAVSDK_TRTC'
```
>?两个 SDK 产品的最新版本号，可以在 [实时音视频](https://github.com/tencentyun/TRTCSDK) 和 [即时通信 IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
- **方法二：通过本地依赖**
  如果您的开发环境访问 cocoapods 仓库较慢，可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。
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

在 info.plist 文件中需要添加 `Privacy - Camera Usage Description`，`Privacy - Microphone Usage Description` 申请摄像头和麦克风权限。

[](id:model.step3)

### 步骤3：导入 TRTCCalling 组件

拷贝以下目录中的所有文件到您的项目中：
```
iOS/TRTCSceneDemo/TXLiteAVDemo/TRTCCallingDemo/model 
```

[](id:model.step4)

### 步骤4：初始化并登录组件

1. 设置推送相关信息。
```
[TRTCCalling shareInstance].imBusinessID = your business ID;
[TRTCCalling shareInstance].deviceToken =  deviceToken;
```
2. 调用 `login(sdkAppID: UInt32, user: String, userSig: String, success: @escaping (() -> Void), failed: @escaping ((_ code: Int, _ message: String) -> Void))` 完成组件的登录，其中几个关键参数的填写请参考下表：
 <table>
<tr><th>参数名</th><th>作用</th></tr>
<tr>
<td>sdkAppID</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr><tr>
<td>user</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
</tr><tr>
<td>userSig</td>
<td> <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
</tr></table>
<dx-codeblock>
::: Objective-C Objective-C
// 登录
[[TRTCCalling shareInstance] login:SDKAPPID user:userID userSig:userSig success:^{
        NSLog(@"Audio call login success.");
} failed:^(int code, NSString *error) {
        NSLog(@"Audio call login failed.");
}];
:::
</dx-codeblock>

[](id:model.step5)
### 步骤5：实现 1v1 通话

1. 发起方调用 TRTCCalling 的 `call(userId, callType)` 方法，`userId` 参数为用户 ID，`callType` 传入语音类型 `CallType_Audio`，就能够发起语音通话的请求。
2. 接收方收到 `onInvited` 事件，此时可以通过 `accept` 方法接听此次通话，也可以选择用 `reject` 方法拒绝通话。
3. 发起方收到 `onUserEnter` 的回调，说明接收方已经进入通话。
<dx-codeblock>
::: Objective-C Objective-C
// 1.监听回调
[[TRTCCalling shareInstance] addDelegate:delegate];

// 接听/拒绝
// 此时 B 如果也登录了IM系统，会收到 onInvited(A, null, false) 回调
// 可以调用 TRTCCalling的accept方法接受 / TRTCCalling的reject 方法拒绝
-(void)onInvited:(NSString *)sponsor
         userIds:(NSArray<NSString *> *)userIds
     isFromGroup:(BOOL)isFromGroup
        callType:(CallType)callType {
    [[TRTCCalling shareInstance] accept];
}

// 2.调用组件的其他功能函数发起通话或挂断等
// 注意：必须在登录后才可以正常调用
// 发起视频通话
[[TRTCCalling shareInstance] call:@"目标用户" type:CallType_Audio];
// 挂断
[[TRTCCalling shareInstance] hangup];
// 拒绝
[[TRTCCalling shareInstance] reject];
:::
</dx-codeblock>

[](id:model.step6)
### 步骤6：实现多人通话

1. 发起方：多人语音通话需要调用 `TRTCCalling ` 中的 `groupCall()` 函数，，并传入用户列表（userIdList）、群组 IM ID（groupId）、通话类型（callType），其中 userIdList 为必填参数，groupId 为选填参数，`callType` 传入语音类型`CallType_Audio`，就能发起多人语音通话。
2. 接收端：通过 `onInvited()` 回调能够接收到此次请求。
3. 接收端：收到回调后可以调用 `accept()` 方法接听此次通话，也可以选择用 `reject()` 方法拒绝通话。
4. 如果超过一定时间（默认30s）没有回复，接收方会收到 `onCallingTimeOut()` 的回调，发起方会收到 `onNoResp(String userId)` 回调。通话发起方在多个接收均未应答时 `hangup()` ， 每个接收方均会收到 `onCallingCancel()` 回调。
5. 如果需要离开当前多人通话可以调用 `hangup()` 方法。
6. 如果通话中有用户中途加入或离开，那么其他用户均会接收到 `onUserEnter()` 或 `onUserLeave()` 回调。

```Objective-C
// 前面省略...
// 拼凑需要拨打的用户列表
NSArray *callList = @[];
[callList addObject:@"b"];
[callList addObject:@"c"];
[callList addObject:@"d"];
// 如果您不是在一个 IM 群里发起的, groupId 可以传一个空串；
[[TRTCCalling shareInstance] groupCall:callList type:CallType_Video groupID:@""];
```

>?您可以通过 一系列的监听回调，例如 `onReject`、`onCancel` 等事件来做对应的 UI 提示。

[](id:offline)
### 步骤7：实现离线接听

>?如果您的业务定位是在线客服等不需要离线接听功能的场景，那么完成上述 [步骤1](#model.step1) - [步骤6](#model.step6) 的对接即可。但如果您的业务定位是社交场景，建议实现离线接听。

IM SDK 支持离线推送，您需要进行相应的设置才能达到可用标准。

1. 申请 Apple 推送证书，具体操作请参见 [Apple 推送证书申请](https://cloud.tencent.com/document/product/269/3898)。
2. 在后台及客户端配置离线推送，具体操作请参见 [离线推送（iOS）](https://cloud.tencent.com/document/product/269/9154)。
3. 修改 login 函数中的 `param.busiId` 为对应证书 ID。

[](id:api)
## 组件 API 列表

TRTCCalling 组件的 API 接口列表如下：

| 接口函数        | 接口功能                                                 |
| --------------- | -------------------------------------------------------- |
| addDelegate     | 设置 TRTCCalling 代理回调，用户可以通过该回调获取状态通知 |
| login           | 登录 IM，所有功能需要先进行登录后才能使用                |
| logout          | 登出 IM，登出后无法再进行拨打操作                        |
| call            | C2C 邀请通话，被邀请方会收到 onInvited 的回调            |
| groupCall       | IM 群组邀请通话，被邀请方会收到 onInvited 的回调          |
| accept          | 作为被邀请方接听来电                                     |
| reject          | 作为被邀请方拒绝来电                                     |
| hangup          | 结束通话                                                 |
| startRemoteView | 将远端用户的摄像头数据渲染到指定的 UIView 中             |
| stopRemoteView  | 停止渲染某个远端用户的摄像头数据                         |
| openCamera      | 开启摄像头，并渲染在指定的 TXCloudVideoView 中           |
| closeCamera     | 关闭摄像头                                               |
| switchCamera    | 切换前后摄像头                                           |
| setMicMute      | 是否静音 mic                                             |
| setHandsFree    | 是否开启免提                                             |
