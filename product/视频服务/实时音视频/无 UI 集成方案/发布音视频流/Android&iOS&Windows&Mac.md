本文档主要介绍主播如何发布自己的音视频流，所谓“发布”，也就是打开麦克风和摄像头，让自己的声音和视频能够被房间中其他用户听到和看到的意思。

![](https://qcloudimg.tencent-cloud.cn/raw/b887b390411aef1396bd593ccdd9eb0e.png)
## 调用指引

[](id:step1)
### 步骤1：完成前序步骤

请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/32173) 完成 SDK 的导入和 App 权限的配置。

[](id:step2)
### 步骤2：打开摄像头预览
您可以调用 **startLocalPreview** 接口打开摄像头预览，此时 SDK 会向系统申请摄像头的使用权限，需要用户授权通过后才会开启摄像头的采集流程。

如果您希望设置本地画面的渲染参数，可以通过调用 **setLocalRenderParams** 接口来设置本地预览的渲染参数。为防止先开启预览再设置预览参数会出现画面跳动，如果您需要设置预览参数，推荐在开启预览之前调用。

如果您希望控制摄像头的各种控制参数，可以用过调用 **TXDeviceManager** 接口来完成“切换前后摄像头”、“设置对焦模式“、“打开、关闭闪光灯”等一系列操作。

如果您希望调节美颜效果和画面质量，我们会分别在 [开启美颜磨皮](https://cloud.tencent.com/document/product/647/68505) 和 [设定画面质量](https://cloud.tencent.com/document/product/647/32236) 中进行详细介绍。

<dx-codeblock>
::: Android  java
// 设置本地画面的预览模式：开启左右镜像，设置画面为填充模式
TRTCCloudDef.TRTCRenderParams param = new TRTCCloudDef.TRTCRenderParams();
param.fillMode   = TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FILL;
param.mirrorType = TRTCCloudDef.TRTC_VIDEO_MIRROR_TYPE_AUTO;
mCloud.setLocalRenderParams(param);

// 启动本地摄像头的预览（localCameraVideo 是用于渲染本地渲染画面的控件）
TXCloudVideoView cameraVideo = findViewById(R.id.txcvv_main_local);
mCloud.startLocalPreview(true, cameraVideo);

// 通过 TXDeviceManager 开启自动对焦并将闪光灯打开
TXDeviceManager manager = mCloud.getDeviceManager();
if (manager.isAutoFocusEnabled()) {
    manager.enableCameraAutoFocus(true);
}
manager.enableCameraTorch(true);
:::
::: iOS  ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
// 设置本地画面的预览模式：开启左右镜像，设置画面为填充模式
TRTCRenderParams *param = [[TRTCRenderParams alloc] init];
param.fillMode   = TRTCVideoFillMode_Fill;
param.mirrorType = TRTCVideoMirrorTypeAuto;
[self.trtcCloud setLocalRenderParams:param];

// 启动本地摄像头的预览（localCameraVideoView 是用于渲染本地渲染画面的控件）
[self.trtcCloud startLocalPreview:YES view:localCameraVideoView];

// 通过 TXDeviceManager 开启自动对焦并将闪光灯打开
TXDeviceManager *manager = [self.trtcCloud getDeviceManager];
if ([manager isAutoFocusEnabled]) {
    [manager enableCameraAutoFocus:YES];
}
[manager enableCameraTorch:YES];
:::
::: Mac  ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
// 设置本地画面的预览模式：开启左右镜像，设置画面为填充模式
TRTCRenderParams *param = [[TRTCRenderParams alloc] init];
param.fillMode   = TRTCVideoFillMode_Fill;
param.mirrorType = TRTCVideoMirrorTypeAuto;
[self.trtcCloud setLocalRenderParams:param];

// 启动本地摄像头的预览（localCameraVideoView 是用于渲染本地渲染画面的控件）
[self.trtcCloud startLocalPreview:localCameraVideoView];
:::
::: Windows  C++
// 设置本地画面的预览模式：开启左右镜像，设置画面为填充模式
liteav::TRTCRenderParams render_params;
render_params.mirrorType = liteav::TRTCVideoMirrorType_Enable;
render_params.fillMode = TRTCVideoFillMode_Fill;
trtc_cloud_->setLocalRenderParams(render_params);

// 启动本地摄像头的预览（view 是用于渲染本地渲染画面的控件句柄）
liteav::TXView local_view = (liteav::TXView)(view);
trtc_cloud_->startLocalPreview(local_view);
:::
</dx-codeblock>


[](id:step3)
### 步骤3：打开麦克风采集
您可以调用 **startLocalAudio** 来开启麦克风采集，该接口需要您通过 `quality` 参数确定采集模式。虽然这个参数的名字叫做 quality，但并不是说质量越高越好，不同的业务场景有最适合的参数选择（这个参数更准确的含义是 scene）。

- **SPEECH**
该模式下的 SDK 音频模块会专注于提炼语音信号，尽最大限度的过滤周围的环境噪音，同时该模式下的音频数据也会获得最好的差质量网络的抵抗能力，因此该模式特别适合于“视频通话”和“在线会议”等侧重于语音沟通的场景。
- **MUSIC**
该模式下的 SDK 会采用很高的音频处理带宽以及立体式模式，在最大限度地提升采集质量的同时也会将音频的 DSP 处理模块调节到最弱的级别，从而最大限度地保证音质。因此该模式适合“音乐直播”场景，尤其适合主播采用专业的声卡进行音乐直播的场景。
- **DEFAULT**
该模式下的 SDK 会启用智能识别算法来识别当前环境，并针对性地选择最佳的处理模式。不过再好的识别算法也总是有不准确的时候，如果您非常清楚自己的产品定位，更推荐您在专注语音通信的 SPEECH 和专注音乐音质的 MUSIC 之间二选一。

<dx-codeblock>
::: Android  java
// 开启麦克风采集，并设置当前场景为：语音模式（高噪声抑制能力、强弱网络抗性）
mCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_SPEECH );

// 开启麦克风采集，并设置当前场景为：音乐模式（高保真采集、低音质损失，推荐配合专业声卡使用）
mCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_MUSIC);
:::
::: iOS&Mac  ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
// 开启麦克风采集，并设置当前场景为：语音模式（高噪声抑制能力、强弱网络抗性）
[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];

// 开启麦克风采集，并设置当前场景为：音乐模式（高保真采集、低音质损失，推荐配合专业声卡使用）
[self.trtcCloud startLocalAudio:TRTCAudioQualityMusic];
:::
::: Windows  C++
// 开启麦克风采集，并设置当前场景为：语音模式（高噪声抑制能力、强弱网络抗性）
trtc_cloud_->startLocalAudio(TRTCAudioQualitySpeech);

// 开启麦克风采集，并设置当前场景为：音乐模式（高保真采集、低音质损失，推荐配合专业声卡使用）
trtc_cloud_->startLocalAudio(TRTCAudioQualityMusic);
:::
</dx-codeblock>

[](id:step4)
### 步骤4：进入 TRTC 房间

参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74634) 让当前用户进入 TRTC 房间。一旦进入房间后，SDK 便会开始向房间中的其他用户发布自己的音频流。

>! 当然，您可以在进入房间（enterRoom）后再启动摄像头预览和麦克风采集，不过在直播场景下，我们需要先给主播一个测试麦克风和调整美颜的时间，所以更常见的做法是先启动摄像头和麦克风再进入房间。

<dx-codeblock>
::: Android  java
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
::: iOS&Mac  ObjC
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

// 组装 TRTC 进房参数，请将 TRTCParams 中的各字段都替换成您自己的参数
// Please replace each field in TRTCParams with your own parameters
liteav::TRTCParams params;
params.sdkAppId = 1400000123;  // Please replace with your own SDKAppID
params.userId = "denny";       // Please replace with your own userid  
params.roomId = 123321;        // Please replace with your own room number
params.userSig = "xxx";        // Please replace with your own userSig
params.role = TRTCCloudDef.TRTCRoleAnchor;

// 如果您的场景是“在线直播”，请将应用场景设置为 TRTC_APP_SCENE_LIVE
// If your application scenario is a video call between several people, please use "TRTC_APP_SCENE_LIVE"
trtc_cloud_->enterRoom(params, liteav::TRTCAppSceneLIVE);
:::
</dx-codeblock>


[](id:step5)
### 步骤5：角色和角色的切换

**TRTC 中的“角色”**
- 在“视频通话”（TRTC_APP_SCENE_VIDEOCALL ） 和 “语音通话”（TRTC_APP_SCENE_AUDIOCALL）这两个场景中，您无需要在进入房间时设置角色，因为在这两个模式下每个用户默认都是主播（Anchor）。
- 在“视频直播”（TRTC_APP_SCENE_LIVE） 和 “语音直播”（TRTC_APP_SCENE_VOICE_CHATROOM）这两个场景中，每个用户在进入房间时都需要指定自己的“角色”，要么是“主播（Anchor）”，要么是“观众（Audience）”。

**角色的切换”**
在 TRTC 中，只有“主播（Anchor）”才有权限发布音视频流，“观众（Audience）”是不能发布音视频流的。
因此，如果您在进房时使用的角色是“观众（Audience）”，需要先调用 **switchRole** 接口将角色切换成“主播（Anchor）”，才能发布音视频流（也就是俗称的“上麦”）。

<dx-codeblock>
::: Android java
// 如果您当前的角色是观众（Audience），需要先调用 switchRole 切换到主播（Anchor）
// If your current role is 'audience', you need to call switchRole to switch to 'anchor' first
mCloud.switchRole(TRTCCloudDef.TRTCRoleAnchor);
mCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_DEFAULT);
mCloud.startLocalPreview(true, cameraVide);

// 如果切换角色失败，onSwitchRole 回调的错误码便不是 0
// If switching operation failed, the error code of the 'onSwitchRole' is not zero
@Override
public void onSwitchRole(final int errCode, final String errMsg) {
    if (errCode != 0) {
        Log.d(TAG, "Switching operation failed...");
    }   
}
:::
::: iOS ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
// 如果您当前的角色是观众（Audience），需要先调用 switchRole 切换到主播（Anchor）
// If your current role is 'audience', you need to call switchRole to switch to 'anchor' first
[self.trtcCloud switchRole:TRTCRoleAnchor];
[self.trtcCloud startLocalAudio:TRTCAudioQualityDefault];
[self.trtcCloud startLocalPreview:YES view:localCameraVideoView];

// 如果切换角色失败，onSwitchRole 回调的错误码便不是 0
// If switching operation failed, the error code of the 'onSwitchRole' is not zero
- (void)onSwitchRole:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg {
    if (errCode != 0) {
        NSLog(@"Switching operation failed... ");
    }   
}
:::
::: Mac ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
// 如果您当前的角色是观众（Audience），需要先调用 switchRole 切换到主播（Anchor）
// If your current role is 'audience', you need to call switchRole to switch to 'anchor' first
[self.trtcCloud switchRole:TRTCRoleAnchor];
[self.trtcCloud startLocalAudio:TRTCAudioQualityDefault];
[self.trtcCloud startLocalPreview:localCameraVideoView];

// 如果切换角色失败，onSwitchRole 回调的错误码便不是 0
// If switching operation failed, the error code of the 'onSwitchRole' is not zero
- (void)onSwitchRole:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg {
    if (errCode != 0) {
        NSLog(@"Switching operation failed... ");
    }   
}
:::
::: Windows C++
// 如果您当前的角色是观众（Audience），需要先调用 switchRole 切换到主播（Anchor）
// If your current role is 'audience', you need to call switchRole to switch to 'anchor' first
trtc_cloud_->switchRole(liteav::TRTCRoleAnchor);
trtc_cloud_->startLocalAudio(TRTCAudioQualityDefault);
trtc_cloud_->startLocalPreview(hWnd);

// 切换角色失败，onSwitchRole 回调的错误码便不是 ERR_NULL（即0）
// If switching operation failed, the error code of the 'onSwitchRole' is not zero
void onSwitchRole(TXLiteAVError errCode, const char* errMsg) {
    if (errCode != ERR_NULL) {
        printf("Switching operation failed...");
    }
}
:::
</dx-codeblock>

**注意：** 如果房间中已有的主播已经太多，会导致 switchRole 角色切换失败，并通过 TRTC 的 onSwitchRole 将错误码回调通知您。所以，当您不再需要发布音视频流（也就是俗称的“下麦”）时，就需要您再次调用 switchRole 并切换为“观众（Audience）”。

>? 您可以能有一个疑问，既然只要主播才能发布音视频流，那我是不是可以让每一个用户都用主播的角色进入房间呢？答案肯定是不行的，原因需要看进阶指引 [一个房间中同时最多可以有多少路音频和视频？](#speed1)

## 进阶指引

[](id:speed1)
### 1. 一个房间中同时最多可以有多少路音频和视频？
一个 TRTC 房间中最多允许同时有 **50** 路音视频流，超出的音视频流会按照“先到先得”的原则被放弃掉。
在绝大多数场景下，小到两个人之间的视频通话，大到几万人同时观看的在线直播，50 路的音视频流都能满足应用场景的需求，但前提是您要做好**角色管理**。

所谓的“角色管理”就是您需要为进入房间的用户分配角色。
- 如果一个用户本身就是直播场景中的“主播”，或者是在线教育场景中的“老师”，抑或是在线会议场景中的“主持人”，都可以分配给“主播（Anchor）”这个角色。
- 如果一个用户本身就是直播场景中的“观众”，或者是在线教育场景中的“学生”，抑或是在线会议场景中的“旁听者”，应当分配为“观众（Audience）”这个角色，否则他们庞大的人数会瞬间将主播的人数限制“挤爆”。

只有当“观众”需要发布音视频流（“上麦”）时，才需要通过 switchRole 切换成“主播”角色，等不再需要发布音视频流（“下麦”）时，则需要立刻切回观众角色"。

通过合理得角色管理，您会发现房间中同时需要发布音视频流的“主播”是通常不会超过 50 路的，否则整个房间中就会“乱糟糟”，毕竟同时说话的人声一旦超过 6 路，普通人就很难从声音中辨识出当前究竟是谁在说话了。









