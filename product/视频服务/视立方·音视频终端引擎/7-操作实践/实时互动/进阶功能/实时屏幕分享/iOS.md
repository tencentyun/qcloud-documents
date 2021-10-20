## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 功能说明
腾讯云视立方音视频通话 TRTC 在 iOS 平台下支持两种不同的屏幕分享方案：

- **应用内分享**
即只能分享当前 App 的画面，该特性需要 iOS 13 及以上版本的操作系统才能支持。由于无法分享当前 App 之外的屏幕内容，因此适用于对隐私保护要求高的场景。
- **跨应用分享**
基于苹果的 Replaykit 方案，能够分享整个系统的屏幕内容，但需要当前 App 额外提供一个 Extension 扩展组件，因此对接步骤也相对应用内分享要多一点。

## 支持的平台

| iOS | Android | Mac OS | Windows |Electron| 微信小程序 | Chrome 浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  &#10003; |  &#10003; |  &#10003;  |&#10003;  |   &#10003;  |   ×   |  &#10003;  |

## 应用内分享

应用内分享的方案非常简单，只需要调用音视频通话 TRTC SDK 提供的接口 [startScreenCaptureInApp](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a16d30ca3f89863da2581ff3872bf31f0) 并传入编码参数`TRTCVideoEncParam` 即可。该参数可以设置为 nil，此时 SDK 会沿用开始屏幕分享之前的编码参数。

我们推荐的用于 iOS 屏幕分享的编码参数是：

| 参数项 | 参数名称 | 常规推荐值 |  文字教学场景 |
|---------|---------|---------|-----|
| 分辨率 | videoResolution | 1280 × 720 | 1920 × 1080 |
| 帧率 | videoFps | 10 FPS | 8 FPS |
| 最高码率 | videoBitrate| 1600 kbps | 2000 kbps |
| 分辨率自适应 | enableAdjustRes | NO | NO |

- 由于屏幕分享的内容一般不会剧烈变动，所以设置较高的 FPS 并不经济，推荐10 FPS即可。
- 如果您要分享的屏幕内容包含大量文字，可以适当提高分辨率和码率设置。
- 最高码率（videoBitrate）是指画面在剧烈变化时的最高输出码率，如果屏幕内容变化较少，实际编码码率会比较低。


## 跨应用分享

### 示例代码
我们在 [Github](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/TRTC-API-Example-OC) 中的 **ScreenShare** 目录下放置了一份跨应用分享的示例代码，其包含如下一些文件：

```
├─ TRTC-API-Example-OC              // TRTC API Example 
|  ├─ Basic                   // 演示跨应用屏幕分享功能
|  |  ├─ ScreenShare                   // 演示跨应用屏幕分享功能
|  |  |  ├── ScreenAnchorViewController.h
|  |  |  ├── ScreenAnchorViewController.m       // 主播录屏状态显示界面
|  |  |  ├── ScreenAnchorViewController.xib
|  |  |  ├── ScreenAudienceViewController.h
|  |  |  ├── ScreenAudienceViewController.m     // 观众观看录播界面
|  |  |  ├── ScreenAudienceViewController.xib
|  |  |  ├── ScreenEntranceViewController.h
|  |  |  ├── ScreenEntranceViewController.m     // 功能入口界面
|  |  |  ├── ScreenEntranceViewController.xib
|  |  |  ├── TRTCBroadcastExtensionLauncher.h
|  |  |  ├── TRTCBroadcastExtensionLauncher.m   // 用于唤起系统录屏的辅助代码
|  |  |  ├── TXReplayKit_Screen   // 录屏进程 Broadcast Upload Extension 代码详见步骤2
|  |  |  │   ├── Info.plist
|  |  |  │   ├── SampleHandler.h
|  |  |  │   └── SampleHandler.m                // 用于接收来自系统的录屏数据
```

您可以通过 [README](https://github.com/tencentyun/TRTCSDK/blob/master/iOS/TRTC-API-Example-OC/README.md) 中的指引跑通该示例 Demo。


### 对接步骤

iOS 系统上的跨应用屏幕分享，需要增加 Extension 录屏进程以配合主 App 进程进行推流。Extension 录屏进程由系统在需要录屏的时候创建，并负责接收系统采集到屏幕图像。因此需要：

1. 创建 App Group，并在 XCode 中进行配置（可选）。这一步的目的是让 Extension 录屏进程可以同主 App 进程进行跨进程通信。
2. 在您的工程中，新建一个 Broadcast Upload Extension 的 Target，并在其中集成 SDK 压缩包中专门为扩展模块定制的 `TXLiteAVSDK_ReplayKitExt.framework`。
3. 对接主 App 端的接收逻辑，让主 App 等待来自 Broadcast Upload Extension 的录屏数据。
4. 使用 Demo 中预先实现的一个 helper class ( `RPSystemBroadcastPickerView`) ，实现类似腾讯会议 iOS 版中点击一个按钮即可唤起屏幕分享的效果（可选）。

>! 如果跳过步骤1，也就是不配置 App Group（接口传 nil），屏幕分享依然可以运行，但稳定性要打折扣，故虽然步骤较多，但请尽量配置正确的 App Group 以保障屏幕分享功能的稳定性。

[](id:createGroup)
#### 步骤1：创建 App Group
使用您的帐号登录 [**https://developer.apple.com/**](https://developer.apple.com/) ，进行以下操作，**注意完成后需要重新下载对应的 Provisioning Profile**。

1. 单击【Certificates, IDs & Profiles】。
2. 在右侧的界面中单击加号。
3. 选择【App Groups】，单击【Continue】。
4. 在弹出的表单中填写 Description 和 Identifier, 其中 Identifier 需要传入接口中的对应的 AppGroup 参数。完成后单击【Continue】。
 ![](https://main.qcloudimg.com/raw/43dd60f5053b21c167ee3a8dbe7d16f9/Create_AppGroup.jpg)
5. 回到 Identifier 页面，左上边的菜单中选择【App IDs】，然后单击您的 App ID（主 App 与 Extension 的 AppID 需要进行同样的配置）。
6. 选中【App Groups】并单击【Edit】。
7. 在弹出的表单中选择您之前创建的 App Group，单击【Continue】返回编辑页，单击【Save】保存。
 ![](https://main.qcloudimg.com/raw/962c1b705433aa62c9617f90d28238c5/Apply_AppGroup.jpg)
8. 重新下载 Provisioning Profile 并配置到 XCode 中。

[](id:createExtension)
#### 步骤2：创建 Broadcast Upload Extension
1. 在 Xcode 菜单依次单击【File】、【New】 、【Target...】，选择【Broadcast Upload Extension】。
2. 在弹出的对话框中填写相关信息，**不用**勾选"【Include UI Extension】，单击【Finish】完成创建。
3. 将下载到的 SDK 压缩包中的 TXLiteAVSDK_ReplayKitExt.framework 拖动到工程中，勾选刚创建的 Target。
4. 选中新增加的 Target，依次单击【+ Capability】，双击【App Groups】，如下图：
 ![AddCapability](https://main.qcloudimg.com/raw/a2b38f1581a495f2a966f6eaf464e057.png)
    操作完成后，会在文件列表中生成一个名为 `Target名.entitlements` 的文件，如下图所示，选中该文件并单击 + 号填写上述步骤中的 App Group 即可。
    ![AddGroup](https://main.qcloudimg.com/raw/b4904a8b425cf55e58497b35c0700966.png)
5. 选中主 App 的 Target ，**并按照上述步骤对主 App 的 Target 做同样的处理。**
6. 在新创建的 Target 中，Xcode 会自动创建一个名为 "SampleHandler.m" 的文件，用如下代码进行替换。**需将代码中的 APPGROUP 改为上文中的创建的 App Group Identifier**。
<dx-codeblock>
::: iOS object-c
#import "SampleHandler.h"
@import TXLiteAVSDK_ReplayKitExt;

#define APPGROUP @"group.com.tencent.liteav.RPLiveStreamShare"

@interface SampleHandler() <TXReplayKitExtDelegate>
@end

@implementation SampleHandler
// 注意：此处的 APPGROUP 需要改成上文中的创建的 App Group Identifier。
- (void)broadcastStartedWithSetupInfo:(NSDictionary<NSString *,NSObject *> *)setupInfo {
    [[TXReplayKitExt sharedInstance] setupWithAppGroup:APPGROUP delegate:self];
    }

- (void)broadcastPaused {
    // User has requested to pause the broadcast. Samples will stop being delivered.
    }

- (void)broadcastResumed {
    // User has requested to resume the broadcast. Samples delivery will resume.
    }

- (void)broadcastFinished {
    [[TXReplayKitExt sharedInstance] finishBroadcast];
    // User has requested to finish the broadcast.
    }

#pragma mark - TXReplayKitExtDelegate
- (void)broadcastFinished:(TXReplayKitExt *)broadcast reason:(TXReplayKitExtReason)reason
{
    NSString *tip = @"";
    switch (reason) {
        case TXReplayKitExtReasonRequestedByMain:
            tip = @"屏幕共享已结束";
            break;
        case TXReplayKitExtReasonDisconnected:
            tip = @"应用断开";
            break;
        case TXReplayKitExtReasonVersionMismatch:
            tip = @"集成错误（SDK 版本号不相符合）";
            break;
    }

    NSError *error = [NSError errorWithDomain:NSStringFromClass(self.class)
                                         code:0
                                     userInfo:@{
                                         NSLocalizedFailureReasonErrorKey:tip
                                     }];
    [self finishBroadcastWithError:error];
}

- (void)processSampleBuffer:(CMSampleBufferRef)sampleBuffer withType:(RPSampleBufferType)sampleBufferType {
    switch (sampleBufferType) {
        case RPSampleBufferTypeVideo:
            [[TXReplayKitExt sharedInstance] sendVideoSampleBuffer:sampleBuffer];
            break;
        case RPSampleBufferTypeAudioApp:
            // Handle audio sample buffer for app audio
            break;
        case RPSampleBufferTypeAudioMic:
            // Handle audio sample buffer for mic audio
            break;
            
        default:
            break;
    }
    }
    @end
    :::
    </dx-codeblock>

[](id:receive)
#### 步骤3：对接主 App 端的接收逻辑
按照如下步骤，对接主 App 端的接收逻辑。也就是在用户触发屏幕分享之前，要让主 App 处于“等待”状态，以便随时接收来自 Broadcast Upload Extension 进程的录屏数据。
1. 确保 TRTCCloud 已经关闭了摄像头采集，如果尚未关闭，请调用 [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01ee967e3180a5e2fc0e37e9e99e85b3) 关闭摄像头采集。
2. 调用 [startScreenCaptureByReplaykit:appGroup:](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a92330045ce479f3b5e5c6b366731c7ff) 方法，并传入 [步骤1](#createGroup) 中设置的 AppGroup，让 SDK 进入“等待”状态。
3. 等待用户触发屏幕分享。如果不实现 [步骤4](#launch) 中的“触发按钮”，屏幕分享就需要用户在 iOS 系统的控制中心，通过长按录屏按钮来触发，这一操作步骤如下图所示：
![](https://main.qcloudimg.com/raw/4082c8bcc7f41328a17f7ede78577bd9.png)
4. 通过调用 [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa8ea0235691fc9cde0a64833249230bb) 接口可以随时中止屏幕分享。
<dx-codeblock>
::: iOS object-c
// 开始屏幕分享，需要将 APPGROUP 替换为上述步骤中创建的 App Group Identifier。
- (void)startScreenCapture {
    TRTCVideoEncParam *videoEncConfig = [[TRTCVideoEncParam alloc] init];
    videoEncConfig.videoResolution = TRTCVideoResolution_1280_720;
    videoEncConfig.videoFps = 10;
    videoEncConfig.videoBitrate = 2000;
    //需要将 APPGROUP 替换为上述步骤中创建的 App Group Identifier:
    [[TRTCCloud sharedInstance] startScreenCaptureByReplaykit:videoEncConfig
                                                     appGroup:APPGROUP];
    }

// 停止屏幕分享
- (void)stopScreenCapture {
    [[TRTCCloud sharedInstance] stopScreenCapture];
    }

// 屏幕分享的启动事件通知，可以通过 TRTCCloudDelegate 进行接收
- (void)onScreenCaptureStarted {
    [self showTip:@"屏幕分享开始"];
    }
    :::
    </dx-codeblock>

[](id:launch)
#### 步骤4：增加屏幕分享的触发按钮（可选）
截止到 [步骤3](#receive)，我们的屏幕分享还必须要用户从控制中心中长按录屏按钮来手动启动。您可通过下述方法实现类似腾讯会议的单击按钮即可触发的效果：
![](https://main.qcloudimg.com/raw/4a759043c613a558400cce8b539fd7d9.png)

1. 在 [Demo](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/TRTC-API-Example-OC/Basic/ScreenShare) 中寻找 `TRTCBroadcastExtensionLauncher` 这个类，并将其加入到您的工程中。
2. 在您的界面上放置一个按钮，并在按钮的响应函数中调用 `TRTCBroadcastExtensionLauncher` 中的 `launch` 函数，就可以唤起屏幕分享功能了。
<dx-codeblock>
::: code 
// 自定义按钮响应方法
- (IBAction)onScreenButtonTapped:(id)sender {
    [TRTCBroadcastExtensionLauncher launch];
}
:::
</dx-codeblock>

>!
>- 苹果在 iOS 12.0 中增加了 `RPSystemBroadcastPickerView` 可以从应用中弹出启动器供用户确认启动屏幕分享，到目前为止, `RPSystemBroadcastPickerView` 尚不支持自定义界面，也没有官方的唤起方法。
>- TRTCBroadcastExtensionLauncher 的原理就是遍历 `RPSystemBroadcastPickerView` 的子 View 寻找 UIButton 并触发了其点击事件。
> - **但该方案不被苹果官方推荐，并可能在新一轮的系统更新中失效，因此 [步骤4](#launch) 只是一个可选方案，您需要自行承担风险来选用此方案。**

## 观看屏幕分享
- **观看 Mac / Windows 屏幕分享**
  当房间里有一个 Mac / Windows 用户启动了屏幕分享，会通过辅流进行分享。房间里的其他用户会通过 TRTCCloudDelegate 中的 [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a52ad5b09959df6e940aec7fb9615de9c) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a5c153269c676a12b20327f9600f9206d) 接口来启动渲染远端用户辅流画面。

- **观看 Android / iOS 屏幕分享**
  若用户通过 Android / iOS 进行屏幕分享，会通过主流进行分享。房间里的其他用户会通过 TRTCCloudDelegate 中的 [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) 接口来启动渲染远端用户主流画面。







