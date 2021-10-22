## 适用场景
TRTC 支持四种不同的进房模式，其中视频通话（VideoCall）和语音通话（VoiceCall）统称为 [通话模式](https://cloud.tencent.com/document/product/647/32221)，视频互动直播（Live）和语音互动直播（VoiceChatRoom）统称为直播模式。
直播模式下的 TRTC，支持单个房间最多10万人同时在线，具备小于300ms的连麦延迟和小于1000ms的观看延迟，以及平滑上下麦切换技术。适用低延时互动直播、十万人互动课堂、视频相亲、在线教育、远程培训、超大型会议等应用场景。
 
## 原理解析
TRTC 云服务由两种不同类型的服务器节点组成，分别是“接口机”和“代理机”：
- **接口机**
该类节点都采用最优质的线路和高性能的机器，善于处理端到端的低延时连麦通话，单位时长计费较高。
- **代理机**
该类节点都采用普通的线路和性能一般的机器，善于处理高并发的拉流观看需求，单位时长计费较低。

在直播模式下，TRTC 引入了角色的概念，用户被分成“主播”和“观众”两种角色，“主播”会被分配到接口机上，“观众”则被分配在代理机，同一个房间的观众人数上限为10万人。
如果“观众”要上麦，需要先切换角色（switchRole）为“主播”才能发言。切换角色的过程也伴随着用户从代理机到接口机的迁移，TRTC 特有的低延时观看技术和平滑上下麦切换技术，可以让整个切换时间变得非常短暂。

![](https://main.qcloudimg.com/raw/b88a624c0bd67d5d58db331b3d64c51c.gif)

## 示例代码
您可以登录 [Github](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/TRTC-API-Example-OC) 获取本文档相关的示例代码。
![](https://main.qcloudimg.com/raw/91ba84ef5cee887717ba69e97d939fcd.png)

>?如果访问 Github 较慢，您也可以直接下载 [TXLiteAVSDK_TRTC_iOS_latest.zip](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_iOS_latest.zip)。


## 操作步骤
[](id:step1)
### 步骤1：集成 SDK
您可以选择以下方式将 **TRTC SDK** 集成到项目中。
#### 方式一：使用 CocoaPods 集成
1. 安装 **CocoaPods** ，具体操作请参见 [CocoaPods 官网安装说明](https://guides.cocoapods.org/using/getting-started.html)。
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

1. 使用 [sharedInstance()](https://cloud.tencent.com/document/product/647/32258) 接口创建`TRTCCloud`实例。
<dx-codeblock>
::: iOS object-c
// 创建 trtcCloud 实例
_trtcCloud = [TRTCCloud sharedInstance];
_trtcCloud.delegate = self;
:::
</dx-codeblock>
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

>! 
>- TRTC 同一时间不支持两个相同的 userId 进入房间，否则会相互干扰。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。


[](id:step5)
### 步骤5：主播端开启摄像头预览和麦克风采音
1. 主播端调用 [startLocalPreview()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3fc1ae11b21944b2f354db258438100e) 可以开启本地的摄像头预览，SDK 会向系统请求摄像头使用权限。
2. 主播端调用 [setLocalViewFillMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a961596f832657bfca81fd675878a2d15) 可以设定本地视频画面的显示模式：
 - Fill 模式表示填充，画面可能会被等比放大和裁剪，但不会有黑边。
 - Fit 模式表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
3. 主播端调用 [setVideoEncoderParam()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a57938e5b62303d705da2ceecf119d74e) 接口可以设定本地视频的编码参数，该参数将决定房间里其他用户观看您的画面时所感受到的 [画面质量](https://cloud.tencent.com/document/product/647/32236)。
4. 主播端调用 [startLocalAudio()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3177329bc84e94727a1be97563800beb) 开启麦克风，SDK 会向系统请求麦克风使用权限。

<dx-codeblock>
::: iOS object-c
//示例代码：发布本地的音视频流
[self.trtcCloud startLocalPreview:_isFrontCamera view:self.view];

//设置本地视频编码参数
TRTCVideoEncParam *encParams = [TRTCVideoEncParam new];
encParams.videoResolution = TRTCVideoResolution_640_360;
encParams.videoBitrate = 550;
encParams.videoFps = 15;
    
[self.trtcCloud setVideoEncoderParam:encParams];
:::
</dx-codeblock>

[](id:step6)
### 步骤6：主播端设置美颜效果

1. 主播端调用 [getBeautyManager()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4fb05ae6b5face276ace62558731280a) 可以获取美颜设置接口 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#interfaceTXBeautyManager)。
2. 主播端调用 [setBeautyStyle()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#a8f2378a87c2e79fa3b978078e534ef4a) 可以设置美颜风格：
 - Smooth：光滑，效果比较明显，类似网红风格。
 - Nature：自然，磨皮算法更多地保留了面部细节，主观感受上会更加自然。
 - Pitu ：仅 [企业版](https://cloud.tencent.com/document/product/647/32689#Enterprise) 才支持。
3. 主播端调用 [setBeautyLevel()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#af864d9466d5161e1926e47bae0e3f027) 可以设置磨皮的级别，一般设置为5即可。
4. 主播端调用 [setWhitenessLevel()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#a199b265f6013e0cca0ff99f731d60ff4) 可以设置美白级别，一般设置为5即可。
5. 由于 iPhone 的摄像头调色默认偏黄，建议调用 [setFilter()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1b0c2a9e82a408881281c7468a74f2c0) 为主播增加美白特效，美白特效所对应的滤镜文件的下载地址：[滤镜文件](https://liteav.sdk.qcloud.com/doc/res/trtc/filter/filterPNG.zip)。

![](https://main.qcloudimg.com/raw/61ef817e3c12944665f1b7098c584ee3.jpg)

[](id:step7)
### 步骤7：主播端创建房间并开始推流
1. 主播端设置 [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCParams) 中的字段`role`为 **`TRTCRoleType.anchor`**，表示当前用户的角色为主播。
2. 主播端调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a96152963bf6ac4bc10f1b67155e04f8d) 即可创建 TRTCParams 参数字段`roomId`的值为房间号的音视频房间，并指定**`appScene`**参数：
 - TRTCAppScene.LIVE：视频互动直播模式，本文以该模式为例。
 - TRTCAppScene.voiceChatRoom：语音互动直播模式。
3. 房间创建成功后，主播端开始音视频数据的编码和传输流程。同时，SDK 会回调 [onEnterRoom(result)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6960aca54e2eda0f424f4f915908a3c5)  事件，参数`result`大于0时表示进房成功，具体数值为加入房间所消耗的时间，单位为毫秒（ms）；当`result`小于0时表示进房失败，具体数值为进房失败的错误码。

<dx-codeblock>
::: iOS object-c
- (void)enterRoom() {
    TRTCParams *params = [TRTCParams new];
    params.sdkAppId = SDKAppID;
    params.roomId = _roomId;
    params.userId = _userId;
    params.role = TRTCRoleAnchor;
    params.userSig = [GenerateTestUserSig genTestUserSig:params.userId];
    [self.trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE];
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

[](id:step8)
### 步骤8：观众端进入房间观看直播
1. 观众端设置 [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCParams) 中的字段`role`为**`TRTCRoleType.audience`**，表示当前用户的角色为观众。
2. 观众端调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a96152963bf6ac4bc10f1b67155e04f8d) 即可进入 TRTCParams 参数中`roomId`代指的音视频房间，并指定**`appScene`**参数：
 - TRTCAppScene.LIVE：视频互动直播模式，本文以该模式为例。
 - TRTCAppScene.voiceChatRoom：语音互动直播模式。
3. 观看主播的画面：
 - 如果观众端事先知道主播的 userId，直接在进房成功后使用主播`userId`调用 [startRemoteView(userId, view: view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) 即可显示主播的画面。
 - 如果观众端不知道主播的 userId，观众端在进房成功后会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80) 事件通知，使用回调中获取的主播`userId`调用 [startRemoteView(userId, view: view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) 便可显示主播的画面。


[](id:step9)
### 步骤9：观众跟主播连麦
1. 观众端调用 [switch(TRTCRoleType.TRTCRoleAnchor)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5f4598c59a9c1e66938be9bfbb51589c) 将角色切换为主播（TRTCRoleType.TRTCRoleAnchor）。
2. 观众端调用 [startLocalPreview()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3fc1ae11b21944b2f354db258438100e) 可以开启本地的画面。
3. 观众端调用 [startLocalAudio()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3177329bc84e94727a1be97563800beb) 开启麦克风采音。

<dx-codeblock>
::: iOS object-c
//示例代码：观众上麦
[self.trtcCloud switchRole:TRTCRoleAnchor];
[self.trtcCloud startLocalAudio:TRTCAudioQualityMusic];
[self.trtcCloud startLocalPreview:_isFrontCamera view:self.view];

//示例代码：观众下麦
[self.trtcCloud switchRole:TRTCRoleAudience];
[self.trtcCloud stopLocalAudio];
[self.trtcCloud stopLocalPreview];
:::
</dx-codeblock>

[](id:step10)
### 步骤10：主播间进行跨房连麦 PK

TRTC 中两个不同音视频房间中的主播，可以在不退出原来的直播间的场景下，通过“跨房通话”功能拉通连麦通话功能进行“跨房连麦 PK”。

1. 主播 A 调用 [connectOtherRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a062bc48550b479a6b7c1662836b8c4a5) 接口，接口参数目前采用 JSON 格式，需要将主播 B 的`roomId`和`userId`拼装成格式为`{"roomId": "978","userId": "userB"}`的参数传递给接口函数。
2. 跨房成功后，主播 A 会收到 [onConnectOtherRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a69e5b1d59857956f736c204fe765ea9a)  事件回调。同时，两个直播房间里的所有用户均会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80)  和 [onUserAudioAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8c885eeb269fc3d2e085a5711d4431d5) 事件通知。
 例如，当房间“001”中的主播 A 通过`connectOtherRoom()`与房间“002”中的主播 B 拉通跨房通话后， 房间“001”中的用户会收到主播 B 的`onUserVideoAvailable(B, available: true)`回调和`onUserAudioAvailable(B, available: true)`回调。 房间“002”中的用户会收到主播 A 的`onUserVideoAvailable(A, available: true)` 回调和`onUserAudioAvailable(A, available: true)`回调。
3. 两个房间里的用户通过调用 [startRemoteView(userId, view: view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) 即可显示另一房间里主播的画面，声音会自动播放。

<dx-codeblock>
::: iOS object-c
//示例代码：跨房连麦 PK
NSMutableDictionary * jsonDict = [[NSMutableDictionary alloc] init];
[jsonDict setObject:@([_otherRoomIdTextField.text intValue]) forKey:@"roomId"];
[jsonDict setObject:_otherUserIdTextField.text forKey:@"userId"];
NSData* jsonData = [NSJSONSerialization dataWithJSONObject:jsonDict options:NSJSONWritingPrettyPrinted error:nil];
NSString* jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
[self.trtcCloud connectOtherRoom:jsonString];
:::
</dx-codeblock>

[](id:step11)
### 步骤11：退出当前房间

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

