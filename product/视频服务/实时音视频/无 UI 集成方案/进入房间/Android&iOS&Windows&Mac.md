本文档主要介绍如何进入 TRTC 房间中，只有在进入音视频房间后，用户才能订阅房间中其他用户的音视频流，或者向房间中的其他用户发布自己的音视频流。
![](https://qcloudimg.tencent-cloud.cn/raw/861153473c6e4679affdb2d24a71f775.png)

## 调用指引

[](id:step1)
### 步骤1：导入 SDK 并设置 App 权限
请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/32173) 完成 SDK 的导入工作。

[](id:step2)
### 步骤2：创建 SDK 实例并设置事件监听器
调用各平台的初始化接口创建 TRTC 的对象实例。
<dx-codeblock>
::: Android java
// 创建 SDK 实例（单例模式）并设置事件监听器
// Create trtc instance(singleton)  and set up event listeners
mCloud = TRTCCloud.sharedInstance(getApplicationContext());
mCloud.setListener(this);
:::
::: iOS&Mac ObjC
// 创建 SDK 实例（单例模式）并设置事件监听器
// Create trtc instance(singleton)  and set up event listeners
_trtcCloud = [TRTCCloud sharedInstance];
_trtcCloud.delegate = self;
:::
::: Windows C++
// 创建 SDK 实例（单例模式）并设置事件监听器
// Create trtc instance(singleton)  and set up event listeners
trtc_cloud_ = getTRTCShareInstance();
trtc_cloud_->addCallback(this);
:::
</dx-codeblock>

[](id:step3)
### 步骤3：监听 SDK 的事件
通过设置事件回调接口，您可以监听 SDK 在运行期间所发生的错误信息、警告信息、流量统计信息、网络质量信息以及各种音视频事件。
<dx-codeblock>
::: Android
我们可以让自己的类继承 **TRTCCloudListener**，并重载 onError 函数，最后将 this 指针通过 **setListener** 接口设置给 SDK，就可以在当前类中监听来自 SDK 的回调事件了。
```java
// 监听 SDK 的事件，并对“摄像头未被授权”等错误进行日志打印
// Listen to the "onError" event and print logs for errors such as "camera is not authorized"
mCloud = TRTCCloud.sharedInstance(getApplicationContext());
mCloud.setListener(this);

@Override
public void onError(int errCode, String errMsg, Bundle extraInfo) {
    if (errCode == TXLiteAVCode.ERR_CAMERA_NOT_AUTHORIZED) {
        Log.d(TAG, "Current application is not authorized to use the camera");
    }
}
```
:::
::: iOS&Mac ObjC
我们可以让自己的类继承 **TRTCCloudDelegate**，并重载 onError 函数，最后将 this 指针通过 TRTCCCloud 的 **delegate** 属性设置给 SDK，就可以在当前类中监听来自 SDK 的回调事件了。
```ObjectiveC
// 监听 SDK 的事件，并对“摄像头未被授权”等错误进行日志打印
// Listen to the "onError" event and print logs for errors such as "camera is not authorized"
_trtcCloud = [TRTCCloud sharedInstance];
_trtcCloud.delegate = self;

- (void)onError:(TXLiteAVError)errCode
         errMsg:(nullable NSString *)errMsg
        extInfo:(nullable NSDictionary *)extInfo{
    if (ERR_CAMERA_NOT_AUTHORIZED == errCode) {
        NSString *errorInfo = @"Current application is not authorized to use the camera：";
        errorInfo = [errorInfo stringByAppendingString errMsg];
        [self toastTip:errorInfo];
    }
}
```
:::
::: Windows C++
我们可以让自己的类继承 **ITRTCCloudCallback**，并重载 onError 函数，最后将 this 指针通过 **addCallback** 接口设置给 SDK，就可以在当前类中监听来自 SDK 的回调事件了。
```C++
// 监听 SDK 的事件，并对“摄像头未被授权”等错误进行日志打印
// Listen to the "onError" event and print logs for errors such as "camera is not authorized"
trtc_cloud_ = getTRTCShareInstance();
trtc_cloud_->addCallback(this);

// 重载 "onError" 函数
void onError(TXLiteAVError errCode, const char* errMsg, void* extraInfo) {
    if (errCode == ERR_CAMERA_NOT_AUTHORIZED) {
        printf("Current application is not authorized to use the camera");
    }
}
```
:::
</dx-codeblock>

[](id:step4)
### 步骤4：准备进房参数 TRTCParams
在调用 enterRoom 接口时需要填写两个关键参数，即 `TRTCParams` 和 `TRTCAppScene`，接下来进行详细介绍：

#### 参数一：TRTCAppScene
该参数用于指定您的应用场景，即**在线直播**还是**实时通话**：
- **实时通话：**
包含 `TRTCAppSceneVideoCall` 和 `TRTCAppSceneAudioCall` 两个可选项，分别是视频通话和语音通话，该模式适合 1对1 的音视频通话，或者参会人数在 300 人以内的在线会议。

- **在线直播：**
包含 `TRTCAppSceneLIVE` 和 `TRTCAppSceneVoiceChatRoom` 两个可选项，分别是视频直播和语音直播，该模式适合十万人以内的在线直播场景，但需要您在接下来介绍的 TRTCParams 参数中指定 **角色(role)** 这个字段，也就是将房间中的用户区分为 **主播(anchor)** 和 **观众(audience)** 两种不同的角色。

#### 参数二：TRTCParams
TRTCParams 由很多的字段构成，但通常您只需要关心如下几个字段的填写：

| 参数名称 | 字段含义 | 补充说明 | 数据类型 |填写示例 |
|---------|---------|---------|---------|---------|
| SDKAppID | 应用 ID | 您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中找到这个 SDKAppID，如果没有就单击“创建应用”按钮创建一个新的应用。| 数字 | 1400000123 |
| userId | 用户 ID | 即用户名，只允许包含大小写英文字母（a-z、A-Z）、数字（0-9）及下划线和连词符。注意 TRTC 不支持同一个 userId 在两台不同的设备上同时进入房间，否则会相互干扰。| 字符串 | “denny” 或者 “123321”|
| userSig | 进房鉴权票据 | 您可以使用 SDKAppID 和 userId 计算出 userSig，计算方法请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275) 。|字符串| eJyrVareCeYrSy1SslI... |
| roomId | 房间号 | 数字类型的房间号。注意如果您想使用字符串类型的房间号，请使用 **strRoomId** 字段，而不要使用 roomId 字段，因为 strRoomId 和 roomId 不可以混用。 | 数字 | 29834 |
| strRoomId | 房间号 | 字符串类型的房间号。注意 strRoomId 和 roomId 不可以混用，“123” 和 123 在 TRTC 后台服务看来并不是同一个房间。  | 字符串 | "29834" |
| role | 角色 | 分为“主播”和“观众”两种角色，只有当 TRTCAppScene 被指定为 `TRTCAppSceneLIVE` 或 `TRTCAppSceneVoiceChatRoom` 这两种直播场景时才需要指定该字段。| 枚举值 | TRTCRoleAnchor 或 TRTCRoleAudience   |

>!
>- TRTC 不支持同一个 userId 在两台不同的设备上同时进入房间，否则会相互干扰。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。


[](id:step5)
### 步骤5：进入房间（enterRoom）
在准备好步骤4中两个参数（TRTCAppScene 和 TRTCParams）后，就可以调用 enterRoom 接口函数进入房间了。

<dx-codeblock>
::: Android  Java
mCloud = TRTCCloud.sharedInstance(getApplicationContext());
mCloud.setListener(mTRTCCloudListener);

// 组装 TRTC 进房参数，请将 TRTCParams 中的各字段都替换成您自己的参数
// Please replace each field in TRTCParams with your own parameters
TRTCCloudDef.TRTCParams param = new TRTCCloudDef.TRTCParams();
params.sdkAppId = 1400000123;  // Please replace with your own SDKAppID
params.userId = "denny";       // Please replace with your own userid  
params.roomId = 123321;        // Please replace with your own room number
params.userSig = "xxx";        // Please replace with your own userSig
params.role = TRTCCloudDef.TRTCRoleAnchor;

// 如果您的场景是“在线直播”，请将应用场景设置为 TRTC_APP_SCENE_LIVE
// If your application scenario is a video call between several people, please use "TRTC_APP_SCENE_LIVE"
mCloud.enterRoom(param, TRTCCloudDef.TRTC_APP_SCENE_LIVE);        
:::

::: iOS&Mac  objectivec
self.trtcCloud = [TRTCCloud sharedInstance];
self.trtcCloud.delegate = self;

// 组装 TRTC 进房参数，请将 TRTCParams 中的各字段都替换成您自己的参数
// Please replace each field in TRTCParams with your own parameters
TRTCParams *params = [[TRTCParams alloc] init];
params.sdkAppId = 1400000123;  // Please replace with your own SDKAppID
params.roomId = 123321; // Please replace with your own room number
params.userId = @"denny";   // Please replace with your own userid  
params.userSig = @"xxx"; // Please replace with your own userSig
params.role = TRTCRoleAnchor;

// 如果您的场景是“在线直播”，请将应用场景设置为 TRTC_APP_SCENE_LIVE
// If your application scenario is a video call between several people, please use "TRTC_APP_SCENE_LIVE"
[self.trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE];
:::

::: Windows  C++
trtc_cloud_ = getTRTCShareInstance();
trtc_cloud_->addCallback(this);

// 组装 TRTC 进房参数，请将 TRTCParams 中的各字段都替换成您自己的参数
// Please replace each field in TRTCParams with your own parameters
liteav::TRTCParams params;
params.sdkAppId = 1400000123;  // Please replace with your own SDKAppID
params.userId = "denny";       // Please replace with your own userid  
params.roomId = 123321;        // Please replace with your own room number
params.userSig = "xxx";        // Please replace with your own userSig
params.role = liteav::TRTCRoleAnchor;

// 如果您的场景是“在线直播”，请将应用场景设置为 TRTC_APP_SCENE_LIVE
// If your application scenario is a video call between several people, please use "TRTC_APP_SCENE_LIVE"
trtc_cloud_->enterRoom(params, liteav::TRTCAppSceneLIVE);        
:::
</dx-codeblock>

**事件回调**
如果进入房间成功，SDK 会回调 onEnterRoom(result) 事件，其中 result 会是一个大于 0 的数值，代表加入房间所消耗的时间，单位为毫秒（ms）。
如果进入房间失败，SDK 同样会回调 onEnterRoom(result) 事件，但参数 `result` 会是一个负数，其数值为进房失败的错误码。
<dx-codeblock>
::: Android Java
// 监听 SDK 的 onEnterRoom 事件并获知是否成功进入房间
// Listen to the onEnterRoom event of the SDK and learn whether the room is successfully entered
@Override
public void onEnterRoom(long     result) {
    if (result > 0) {
        Log.d(TAG, "Enter room succeed");
    } else {
        Log.d(TAG, "Enter room failed");
    }
}
:::
::: iOS&Mac ObjC
// 监听 SDK 的 onEnterRoom 事件并获知是否成功进入房间
// Listen to the onEnterRoom event of the SDK and learn whether the room is successfully entered
- (void)onEnterRoom:(NSInteger)result {
    if (result > 0) {
        [self toastTip:@"Enter room succeed!"];
    } else {
        [self toastTip:@"Enter room failed!"];
    }
}
:::
::: Windows C++
// 监听 SDK 的 onEnterRoom 事件并获知是否成功进入房间
// override to the onEnterRoom event of the SDK and learn whether the room is successfully entered
void onEnterRoom(int result) {
    if (result > 0) {
        printf("Enter room succeed");
    } else {
        printf("Enter room failed");
    }
}
:::
</dx-codeblock>
