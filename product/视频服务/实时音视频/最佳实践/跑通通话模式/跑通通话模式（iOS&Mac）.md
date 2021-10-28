## 适用场景
TRTC 支持四种不同的进房模式，其中视频通话（VideoCall）和语音通话（AudioCall）统称为通话模式，视频互动直播（Live）和语音互动直播（VoiceChatRoom）统称为 [直播模式](https://cloud.tencent.com/document/product/647/35429)。
通话模式下的 TRTC，支持单个房间最多300人同时在线，支持最多50人同时发言。适合1对1视频通话、300人视频会议、在线问诊、远程面试、视频客服、在线狼人杀等应用场景。

## 原理解析
TRTC 云服务由两种不同类型的服务器节点组成，分别是“接口机”和“代理机”：
- **接口机**
该类节点都采用最优质的线路和高性能的机器，善于处理端到端的低延时连麦通话，单位时长计费较高。
- **代理机**
该类节点都采用普通的线路和性能一般的机器，善于处理高并发的拉流观看需求，单位时长计费较低。

在通话模式下，TRTC 房间中的所有用户都会被分配到接口机上，相当于每个用户都是“主播”，每个用户随时都可以发言（最高的上行并发限制为50路），因此适合在线会议等场景，但单个房间的人数限制为300人。
![](https://main.qcloudimg.com/raw/b88a624c0bd67d5d58db331b3d64c51c.gif)

## 示例代码
您可以登录 [Github](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/TRTC-API-Example-OC) 获取本文档相关的示例代码。
![](https://main.qcloudimg.com/raw/468128bcaf078183eed097f7ee5f9c21.png)

>?如果访问 Github 较慢，您也可以直接下载 [TXLiteAVSDK_TRTC_iOS_latest.zip](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_iOS_latest.zip)。

## 操作步骤
[](id:step1)
### 步骤1：集成 SDK
您可以选择以下方式将 **TRTC SDK** 集成到项目中。
#### 方式一：使用 CocoaPods 集成
1. 安装 **CocoaPods** ，具体操作请参考 [CocoaPods 官网安装说明](https://guides.cocoapods.org/using/getting-started.html)。
2. 打开您当前项目根目录下的`Podfile`文件，添加以下内容：
>?如果该目录下没有`Podfile`文件，请先执行`pod init`命令新建文件再添加以下内容。
>
```
target 'Your Project' do
        pod 'TXLiteAVSDK_TRTC'
end
```
3. 执行以下命令安装 **TRTC SDK** 。
```
pod install
```
安装成功后当前项目根目录下会生成一个 **xcworkspace** 文件。
4. 打开新生成的 **xcworkspace** 文件即可。

#### 方式二：下载 ZIP 包手动集成
如果您暂时不想安装 CocoaPods 环境，或者已经安装但是访问 CocoaPods 仓库比较慢，您可以直接下载 [ZIP 压缩包](https://cloud.tencent.com/document/product/647/32689)，并参考 [快速集成(iOS)](https://cloud.tencent.com/document/product/647/32173#.E6.89.8B.E5.8A.A8.E9.9B.86.E6.88.90) 将 SDK 集成到您的工程中。

[](id:step2)
### 步骤2：添加媒体设备权限
在`Info.plist`文件中添加摄像头和麦克风的申请权限：

| Key | Value |
|---------|---------|
| Privacy - Camera Usage Description | 描述使用摄像头权限的原因，例如，需要访问您的相机权限，开启后视频聊天才会有画面 |
| Privacy - Microphone Usage Description | 描述使用麦克风权限的原因，例如，需要访问您的麦克风权限，开启后聊天才会有声音 |

[](id:step3)
### 步骤3：初始化 SDK 实例并监听事件回调

1. 使用 [sharedInstance()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab6884975e069628328d05cf0e2c3dc67) 接口创建`TRTCCloud`实例。
```
// 创建 trtcCloud 实例
_trtcCloud = [TRTCCloud sharedInstance];
_trtcCloud.delegate = self;
```
2. 设置`delegate`属性注册事件回调，并监听相关事件和错误通知。
<dx-codeblock>
::: iOS object-c
// 错误通知是要监听的，需要捕获并通知用户
- (void)onError:(TXLiteAVError)errCode errMsg:(NSString *)errMsg extInfo:(NSDictionary *)extInfo {
    if (ERR_ROOM_ENTER_FAIL == errCode) {
        [self toastTip:@"进房失败"];
        [self.trtcCloud exitRoom];
    }
}
:::
</dx-codeblock>

[](id:step4)
### 步骤4：组装进房参数 TRTCParams
在调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a96152963bf6ac4bc10f1b67155e04f8d) 接口时需要填写一个关键参数 [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCParams)，该参数包含的必填字段如下表所示。

| 参数名称 | 字段类型 | 补充说明 |填写示例 | 
|---------|---------|---------|---------|
| sdkAppId | 数字 | 应用 ID，您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。|1400000123 | 
| userId | 字符串 | 只允许包含大小写英文字母（a-z、A-Z）、数字（0-9）及下划线和连词符。 | test_user_001 |
| userSig | 字符串 | 基于 userId 可以计算出 userSig，计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275) 。| eJyrVareCeYrSy1SslI... |
| roomId | 数字 | 数字类型的房间号。如果您想使用字符串形式的房间号，请使用 TRTCParams 中的 strRoomId。 | 29834 |

>! TRTC 同一时间不支持两个相同的 userId 进入房间，否则会相互干扰。

[](id:step5)
### 步骤5：创建并进入房间
1. 调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a96152963bf6ac4bc10f1b67155e04f8d) 即可加入 TRTCParams 参数中`roomId`代指的音视频房间。如果该房间不存在，SDK 会自动创建一个以字段`roomId`的值为房间号的新房间。
2. 请根据应用场景设置合适的**`appScene`**参数，使用错误可能会导致卡顿率或画面清晰度不达预期。
 - 视频通话，请设置为`TRTCAppScene.videoCall`。
 - 语音通话，请设置为`TRTCAppScene.audioCall`。
3. 进房成功后，SDK 会回调`onEnterRoom(result)`事件。其中，参数`result`大于0时表示进房成功，具体数值为加入房间所消耗的时间，单位为毫秒（ms）；当`result`小于0时表示进房失败，具体数值为进房失败的错误码。

<dx-codeblock>
::: iOS object-c
- (void)enterRoom() {
    TRTCParams *params = [TRTCParams new];
    params.sdkAppId = SDKAppID;
    params.roomId = _roomId;
    params.userId = _userId;
    params.role = TRTCRoleAnchor;
    params.userSig = [GenerateTestUserSig genTestUserSig:params.userId];
    [self.trtcCloud enterRoom:params appScene:TRTCAppSceneVideoCall];
}

- (void)onEnterRoom:(NSInteger)result {
    if (result > 0) {
        [self toastTip:@"进房成功"];
    } else {
        [self toastTip:@"进房失败"];
    }
}
:::
</dx-codeblock>

>! 
>- 如果进房失败，SDK 同时还会回调`onError`事件，并返回参数`errCode`（[错误码](https://cloud.tencent.com/document/product/647/32257)）、`errMsg`（错误原因）以及`extraInfo`（保留参数）。
>- 如果已在某一个房间中，则必须先调用`exitRoom()`退出当前房间，才能进入下一个房间。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。

[](id:step6)
### 步骤6：订阅远端的音视频流
SDK 支持自动订阅和手动订阅。

#### 自动订阅模式（默认）
在自动订阅模式下，进入某个房间之后，SDK 会自动接收房间中其他用户的音频流，从而达到最佳的“秒开”效果：
1. 当房间中有其他用户在上行音频数据时，您会收到 [onUserAudioAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8c885eeb269fc3d2e085a5711d4431d5) 事件通知，SDK 会自动播放这些远端用户的声音。
2. 您可以通过 [muteRemoteAudio(userId, mute: true)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afede3cc79a8d68994857b410fb5572d2) 屏蔽某一个 userId 的音频数据，也可以通过 [muteAllRemoteAudio(true)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a75148bf8a322c852965fe774cbc7dd14) 屏蔽所有远端用户的音频数据，屏蔽后 SDK 不再继续拉取对应远端用户的音频数据。
3. 当房间中有其他用户在上行视频数据时，您会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80) 事件通知，但此时 SDK 未收到该如何展示视频数据的指令，因此不会自动处理视频数据。您需要通过调用 [startRemoteView(userId, view: view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) 方法将远端用户的视频数据和显示`view`关联起来。
4. 您可以通过 [setRemoteViewFillMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afda6658d1bf7dc9bc1445838b95d21ff) 指定视频画面的显示模式：
 - Fill 模式：表示填充，画面可能会等比放大和裁剪，但不会有黑边。
 - Fit 模式：表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
5. 您可以通过 [stopRemoteView(userId)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2b7e96e4b527798507ff743c61a6a066) 可以屏蔽某一个 userId 的视频数据，也可以通过 [stopAllRemoteView()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aaa75cd1b98c226bb7b8a19412b204d2b) 屏蔽所有远端用户的视频数据，屏蔽后 SDK 不再继续拉取对应远端用户的视频数据。

<dx-codeblock>
::: iOS object-c
// 实例代码：根据通知订阅（或取消订阅）远端用户的视频画面
- (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available {
    UIView* remoteView = remoteViewDic[userId];
    if (available) {
        [_trtcCloud startRemoteView:userId streamType:TRTCVideoStreamTypeSmall view:remoteView];
    } else {
        [_trtcCloud stopRemoteView:userId streamType:TRTCVideoStreamTypeSmall];
    }
}
:::
</dx-codeblock>

>? 如果您在收到`onUserVideoAvailable()`事件回调后没有立即调用`startRemoteView()`订阅视频流，SDK 将会在5s内停止接收来自远端的视频数据。

#### 手动订阅模式
您可以通过 [setDefaultStreamRecvMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ada2e2155e0e7c3001c6bb6dca1d93048) 接口将 SDK 指定为手动订阅模式。在手动订阅模式下，SDK 不会自动接收房间中其他用户的音视频数据，需要您手动通过 API 函数触发。

1. 在**进房前**调用 [setDefaultStreamRecvMode(false, video: false)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ada2e2155e0e7c3001c6bb6dca1d93048) 接口将 SDK 设定为手动订阅模式。
2. 当房间中有其他用户在上行音频数据时，您会收到 [onUserAudioAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8c885eeb269fc3d2e085a5711d4431d5) 事件通知。此时，您需要通过调用 [muteRemoteAudio(userId, mute: false)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afede3cc79a8d68994857b410fb5572d2) 手动订阅该用户的音频数据，SDK 会在接收到该用户的音频数据后解码并播放。
3. 当房间中有其他用户在上行视频数据时，您会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80) 事件通知。此时，您需要通过调用 [startRemoteView(userId, view: view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) 方法手动订阅该用户的视频数据，SDK 会在接收到该用户的视频数据后解码并播放。

[](id:step7)
### 步骤7：发布本地的音视频流
1. 调用 [startLocalAudio()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3177329bc84e94727a1be97563800beb) 可以开启本地的麦克风采集，并将采集到的声音编码并发送出去。
2. 调用 [startLocalPreview()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3fc1ae11b21944b2f354db258438100e) 可以开启本地的摄像头，并将采集到的画面编码并发送出去。
3. 调用 [setLocalViewFillMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a961596f832657bfca81fd675878a2d15) 可以设定本地视频画面的显示模式：
 - Fill 模式表示填充，画面可能会被等比放大和裁剪，但不会有黑边。
 - Fit 模式表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
4. 调用 [setVideoEncoderParam()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a57938e5b62303d705da2ceecf119d74e) 接口可以设定本地视频的编码参数，该参数将决定房间里其他用户观看您的画面时所感受到的 [画面质量](https://cloud.tencent.com/document/product/647/32236)。

<dx-codeblock>
::: iOS object-c
//示例代码：发布本地的音视频流
[self.trtcCloud startLocalPreview:_isFrontCamera view:self.view];
[self.trtcCloud startLocalAudio:TRTCAudioQualityMusic];
:::
</dx-codeblock>

>! Mac 版 SDK 默认会使用当前系统默认的摄像头和麦克风。您可以通过调用 [setCurrentCameraDevice()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aae9955bb39985586f7faba841d2692fc) 和 [setCurrentMicDevice()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5141fec83e7f071e913bfc539c193ac6) 选择其他摄像头和麦克风。

[](id:step8)
### 步骤8：退出当前房间

调用 [exitRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a715f5b669ad1d7587ae19733d66954f3) 方法退出房间，SDK 在退房时需要关闭和释放摄像头、麦克风等硬件设备，因此退房动作并非瞬间完成的，需收到 [onExitRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6a98fcaac43fa754cf9dd80454897bea) 回调后才算真正完成退房操作。

<dx-codeblock>
::: iOS object-c
// 调用退房后请等待 onExitRoom 事件回调
[self.trtcCloud exitRoom];

- (void)onExitRoom:(NSInteger)reason {
    NSLog(@"离开房间: reason: %ld", reason)
}
:::
</dx-codeblock>

>! 如果您的 App 中同时集成了多个音视频 SDK，请在收到`onExitRoom`回调后再启动其它音视频 SDK，否则可能会遇到硬件占用问题。
