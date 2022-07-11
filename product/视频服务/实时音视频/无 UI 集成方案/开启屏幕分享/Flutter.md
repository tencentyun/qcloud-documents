## 基于 Android 平台
腾讯云 TRTC 在 Android 系统上支持屏幕分享，即将当前系统的屏幕内容通过 TRTC SDK 分享给房间里的其他用户。关于此功能，有两点需要注意：

- 移动端 TRTC Android 8.6 之前的版本屏幕分享并不像桌面端版本一样支持“辅路分享”，因此在启动屏幕分享时，摄像头的采集需要先被停止，否则会相互冲突；8.6 及之后的版本支持“辅路分享”，则不需要停止摄像头的采集。
- 当一个 Android 系统上的后台 App 在持续使用 CPU 时，很容易会被系统强行杀掉，而且屏幕分享本身又必然会消耗 CPU。要解决这个看似矛盾的冲突，我们需要在 App 启动屏幕分享的同时，在 Android 系统上弹出悬浮窗。由于 Android 不会强杀包含前台 UI 的 App 进程，因此该种方案可以让您的 App 可以持续进行屏幕分享而不被系统自动回收。如下图所示：
![](https://main.qcloudimg.com/raw/e7dad1db0a99add95ac372634bddc2bf.png)

### 启动屏幕分享
要开启 Android 端的屏幕分享，只需调用 `TRTCCloud` 中的  [startScreenCapture()](https://pub.dev/documentation/tencent_trtc_cloud/latest/trtc_cloud/TRTCCloud/startScreenCapture.html) 接口即可。但如果要达到稳定和清晰的分享效果，您需要关注如下三个问题：

#### 添加 Activity
在 manifest 文件中粘贴如下 activity（若项目代码中存在则不需要添加）。
```xml
<activity 
    android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity" 
    android:theme="@android:style/Theme.Translucent"/>
```

#### 设定视频编码参数
通过设置 [startScreenCapture()](https://pub.dev/documentation/tencent_trtc_cloud/latest/trtc_cloud/TRTCCloud/startScreenCapture.html)  中的首个参数 `encParams` ，您可以指定屏幕分享的编码质量。如果您指定 `encParams` 为 null，SDK 会自动使用之前设定的编码参数，我们推荐的参数设定如下：

| 参数项 | 参数名称 | 常规推荐值 |  文字教学场景 |
|---------|---------|---------|-----|
| 分辨率 | videoResolution | 1280 × 720 | 1920 × 1080 |
| 帧率 | videoFps | 10 FPS | 8 FPS |
| 最高码率 | videoBitrate| 1600 kbps | 2000 kbps |
| 分辨率自适应 | enableAdjustRes | NO | NO |
>?
 - 由于屏幕分享的内容一般不会剧烈变动，所以设置较高的 FPS 并不经济，推荐10 FPS即可。
 - 如果您要分享的屏幕内容包含大量文字，可以适当提高分辨率和码率设置。
 - 最高码率（videoBitrate）是指画面在剧烈变化时的最高输出码率，如果屏幕内容变化较少，实际编码码率会比较低。

#### 弹出悬浮窗以避免被强杀
从 Android 7.0 系统开始，切入到后台运行的普通 App 进程，但凡有 CPU 活动，都很容易会被系统强杀掉。 所以当 App 在切入到后台默默进行屏幕分享时，通过弹出悬浮窗的方案，可以避免被系统强杀掉。 同时，在手机屏幕上显示悬浮窗也有利于告知用户当前正在做屏幕分享，避免用户泄漏个人隐私。

##### 方案：弹出普通的悬浮窗
要弹出类似“腾讯会议”的迷你悬浮窗，您只需要参考示例代码 [tool.dart](https://github.com/c1avie/trtc_demo/blob/master/lib/page/trtcmeetingdemo/tool.dart) 中的实现即可：
```
//屏幕分享时弹出小浮窗，防止切换到后台应用被杀死
  static void showOverlayWindow() {
    SystemWindowHeader header = SystemWindowHeader(
      title: SystemWindowText(
          text: "屏幕分享中", fontSize: 14, textColor: Colors.black45),
      decoration: SystemWindowDecoration(startColor: Colors.grey[100]),
    );
    SystemAlertWindow.showSystemWindow(
      width: 18,
      height: 95,
      header: header,
      margin: SystemWindowMargin(top: 200),
      gravity: SystemWindowGravity.TOP,
    );
  }
```

## 基于 iOS 平台
- **[应用内分享](#Internal)**
即只能分享当前 App 的画面，该特性需要 iOS 13 及以上版本的操作系统才能支持。由于无法分享当前 App 之外的屏幕内容，因此适用于对隐私保护要求高的场景。
- **[跨应用分享](#Cross)**
基于苹果的 Replaykit 方案，能够分享整个系统的屏幕内容，但需要当前 App 额外提供一个 Extension 扩展组件，因此对接步骤也相对应用内分享要多一点。

[](id:Internal)
### 方案1：iOS 平台应用内分享

应用内分享的方案非常简单，只需要调用 TRTC SDK 提供的接口 [startScreenCapture](https://pub.flutter-io.cn/documentation/tencent_trtc_cloud/latest/trtc_cloud/TRTCCloud/startScreenCapture.html) 并传入编码参数`TRTCVideoEncParam`和 参数`appGroup`设置为`''`。`TRTCVideoEncParam` 参数可以设置为 null，此时 SDK 会沿用开始屏幕分享之前的编码参数。

我们推荐的用于 iOS 屏幕分享的编码参数是：

| 参数项 | 参数名称 | 常规推荐值 |  文字教学场景 | 
|---------|---------|---------|-----|
| 分辨率 | videoResolution | 1280 × 720 | 1920 × 1080 | 
| 帧率 | videoFps | 10 FPS | 8 FPS |
| 最高码率 | videoBitrate| 1600 kbps | 2000 kbps |
| 分辨率自适应 | enableAdjustRes | NO | NO |

>?
- 由于屏幕分享的内容一般不会剧烈变动，所以设置较高的 FPS 并不经济，推荐10 FPS即可。
- 如果您要分享的屏幕内容包含大量文字，可以适当提高分辨率和码率设置。
- 最高码率（videoBitrate）是指画面在剧烈变化时的最高输出码率，如果屏幕内容变化较少，实际编码码率会比较低。

[](id:Cross)
### 方案2：iOS 平台跨应用分享

#### 示例代码
我们在 [Github](https://github.com/c1avie/trtc_demo) 中的 **trtc_demo/ios** 目录下放置了一份跨应用分享的示例代码，其包含如下一些文件：

```
├── Broadcast.Upload        //录屏进程 Broadcast Upload Extension 代码详见步骤2
│   ├── Broadcast.Upload.entitlements       //用于设置进程间通信的 AppGroup 信息
│   ├── Broadcast.UploadDebug.entitlements  //用于设置进程间通信的 AppGroup 信息（debug环境）
│   ├── Info.plist
│   └── SampleHandler.swift     // 用于接收来自系统的录屏数据
├── Resource                    // 资源文件
├── Runner                      // TRTC 精简化 Demo
├── TXLiteAVSDK_ReplayKitExt.framework      //TXLiteAVSDK_ReplayKitExt SDK
```

您可以通过 [README](https://github.com/c1avie/trtc_demo/blob/master/README.md) 中的指引跑通该示例 Demo。


#### 对接步骤
iOS 系统上的跨应用屏幕分享，需要增加 Extension 录屏进程以配合主 App 进程进行推流。Extension 录屏进程由系统在需要录屏的时候创建，并负责接收系统采集到屏幕图像。因此需要：
1. 创建 App Group，并在 XCode 中进行配置（可选）。这一步的目的是让 Extension 录屏进程可以同主 App 进程进行跨进程通信。
2. 在您的工程中，新建一个 Broadcast Upload Extension 的 Target，并在其中集成 SDK 压缩包中专门为扩展模块定制的 `TXLiteAVSDK_ReplayKitExt.framework`。
3. 对接主 App 端的接收逻辑，让主 App 等待来自 Broadcast Upload Extension 的录屏数据。
4. 编辑 `pubspec.yaml` 文件引入 `replay_kit_launcher` 插件 ，实现类似TRTC Demo Screen中点击一个按钮即可唤起屏幕分享的效果（可选）。
```
# 引入 trtc sdk和replay_kit_launcher
dependencies:
  tencent_trtc_cloud: ^0.2.1
  replay_kit_launcher: ^0.2.0+1
```

>! 如果跳过 [步骤1](#Step1)，也就是不配置 App Group（接口传 null），屏幕分享依然可以运行，但稳定性要打折扣，故虽然步骤较多，但请尽量配置正确的 App Group 以保障屏幕分享功能的稳定性。

[](id:createGroup)[](id:Step1)
#### 步骤1：创建 App Group
使用您的帐号登录 [**https://developer.apple.com/**](https://developer.apple.com/)，进行以下操作，**注意完成后需要重新下载对应的 Provisioning Profile**。

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
1. 在 Xcode 菜单依次单击【File】>【New】 >【Target...】，选择【Broadcast Upload Extension】。
2. 在弹出的对话框中填写相关信息，**不用**勾选"【Include UI Extension】，单击【Finish】完成创建。
3. 将下载到的 SDK 压缩包中的 TXLiteAVSDK_ReplayKitExt.framework 拖动到工程中，勾选刚创建的 Target。
4. 选中新增加的 Target，依次单击【+ Capability】，双击【App Groups】，如下图：
 ![AddCapability](https://main.qcloudimg.com/raw/a2b38f1581a495f2a966f6eaf464e057.png)
 操作完成后，会在文件列表中生成一个名为 `Target名.entitlements` 的文件，如下图所示，选中该文件并单击 + 号填写上述步骤中的 App Group 即可。
 ![AddGroup](https://main.qcloudimg.com/raw/b4904a8b425cf55e58497b35c0700966.png)
5. 选中主 App 的 Target ，**并按照上述步骤对主 App 的 Target 做同样的处理。**
6. 在新创建的 Target 中，Xcode 会自动创建一个名为 "SampleHandler.swift" 的文件，用如下代码进行替换。**需将代码中的 APPGROUP 改为上文中的创建的 App Group Identifier**。
<dx-codeblock>
::: iOS swift

import ReplayKit
import TXLiteAVSDK_ReplayKitExt


let APPGROUP = "group.com.tencent.comm.trtc.demo"

class SampleHandler: RPBroadcastSampleHandler, TXReplayKitExtDelegate {

    let recordScreenKey = Notification.Name.init("TRTCRecordScreenKey")
    
    override func broadcastStarted(withSetupInfo setupInfo: [String : NSObject]?) {
        // User has requested to start the broadcast. Setup info from the UI extension can be supplied but optional.
        TXReplayKitExt.sharedInstance().setup(withAppGroup: APPGROUP, delegate: self)
    }
    
    override func broadcastPaused() {
        // User has requested to pause the broadcast. Samples will stop being delivered.
    }
    
    override func broadcastResumed() {
        // User has requested to resume the broadcast. Samples delivery will resume.
    }
    
    override func broadcastFinished() {
        // User has requested to finish the broadcast.
        TXReplayKitExt.sharedInstance() .finishBroadcast()
    }
    
    func broadcastFinished(_ broadcast: TXReplayKitExt, reason: TXReplayKitExtReason) {
        var tip = ""
        switch reason {
        case TXReplayKitExtReason.requestedByMain:
            tip = "屏幕共享已结束"
            break
        case TXReplayKitExtReason.disconnected:
            tip = "应用断开"
            break
        case TXReplayKitExtReason.versionMismatch:
            tip = "集成错误（SDK 版本号不相符合）"
            break
        default:
            break
        }
        
        let error = NSError(domain: NSStringFromClass(self.classForCoder), code: 0, userInfo: [NSLocalizedFailureReasonErrorKey:tip])
        finishBroadcastWithError(error)
    }
    
    override func processSampleBuffer(_ sampleBuffer: CMSampleBuffer, with sampleBufferType: RPSampleBufferType) {
        switch sampleBufferType {
        case RPSampleBufferType.video:
            // Handle video sample buffer
            TXReplayKitExt.sharedInstance() .sendVideoSampleBuffer(sampleBuffer)
            break
        case RPSampleBufferType.audioApp:
            // Handle audio sample buffer for app audio
            break
        case RPSampleBufferType.audioMic:
            // Handle audio sample buffer for mic audio
            break
        @unknown default:
            // Handle other sample buffer types
            fatalError("Unknown type of sample buffer")
        }
    }
}
:::
</dx-codeblock>

[](id:receive)
#### 步骤3：对接主 App 端的接收逻辑
按照如下步骤，对接主 App 端的接收逻辑。也就是在用户触发屏幕分享之前，要让主 App 处于“等待”状态，以便随时接收来自 Broadcast Upload Extension 进程的录屏数据。
1. 确保 TRTCCloud 已经关闭了摄像头采集，如果尚未关闭，请调用 [stopLocalPreview](https://pub.flutter-io.cn/documentation/tencent_trtc_cloud/latest/trtc_cloud/TRTCCloud/stopLocalPreview.html) 关闭摄像头采集。
2. 调用 [startScreenCapture](https://pub.flutter-io.cn/documentation/tencent_trtc_cloud/latest/trtc_cloud/TRTCCloud/startScreenCapture.html) 方法，并传入 [步骤1](#createGroup) 中设置的 AppGroup，让 SDK 进入“等待”状态。
3. 等待用户触发屏幕分享。如果不实现 [步骤4](#launch) 中的“触发按钮”，屏幕分享就需要用户在 iOS 系统的控制中心，通过长按录屏按钮来触发，这一操作步骤如下图所示：
![](https://tccweb-1258344699.cos.ap-nanjing.myqcloud.com/sdk/trtc/trtcdemo/01.png)
4. 通过调用 [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa8ea0235691fc9cde0a64833249230bb) 接口可以随时中止屏幕分享。
<dx-codeblock>
::: dart 
// 开始屏幕分享，需要将 APPGROUP 替换为上述步骤中创建的 App Group 
trtcCloud.startScreenCapture(
    TRTCVideoEncParam(
        videoFps: 10,
        videoResolution: TRTCCloudDef.TRTC_VIDEO_RESOLUTION_1280_720,
        videoBitrate: 1600,
        videoResolutionMode: TRTCCloudDef.TRTC_VIDEO_RESOLUTION_MODE_PORTRAIT,
    ),
    iosAppGroup,
);

// 停止屏幕分享
await trtcCloud.stopScreenCapture();


// 屏幕分享的启动事件通知，可以通过 TRTCCloudListener 进行接收
onRtcListener(type, param){
    if (type == TRTCCloudListener.onScreenCaptureStarted) {
      //屏幕分享开始
    }
}
:::
</dx-codeblock>

[](id:launch)
#### 步骤4：增加屏幕分享的触发按钮（可选）
截止到 [步骤3](#receive)，我们的屏幕分享还必须要用户从控制中心中长按录屏按钮来手动启动。您可通过下述方法实现类似 TRTC Demo Screen 的单击按钮即可触发的效果：
![](https://tccweb-1258344699.cos.ap-nanjing.myqcloud.com/sdk/trtc/trtcdemo/2.png)

1. 将 `replay_kit_launcher` 插件加入到您的工程中。
2. 在您的界面上放置一个按钮，并在按钮的响应函数中调用 `ReplayKitLauncher.launchReplayKitBroadcast(iosExtensionName);` 函数，就可以唤起屏幕分享功能了。
```
// 自定义按钮响应方法
onShareClick() async {
   if (Platform.isAndroid) {
      if (await SystemAlertWindow.requestPermissions) {
        MeetingTool.showOverlayWindow();
      }
    } else {
      //屏幕分享功能只能在真机测试
      ReplayKitLauncher.launchReplayKitBroadcast(iosExtensionName);
    }
}
```

## 观看屏幕分享
- **观看 Android / iOS 屏幕分享**
  若用户通过 Android / iOS 进行屏幕分享，会通过主流进行分享。房间里的其他用户会通过 TRTCCloudListener 中的 [onUserVideoAvailable](https://pub.flutter-io.cn/documentation/tencent_trtc_cloud/latest/trtc_cloud_listener/TRTCCloudListener-class.html) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteView](https://pub.flutter-io.cn/documentation/tencent_trtc_cloud/latest/trtc_cloud/TRTCCloud/startRemoteView.html) 接口来启动渲染远端用户主流画面。

## 常见问题
 **一个房间里可以同时有多路屏幕分享吗？**
目前一个 TRTC 音视频房间只能有一路屏幕分享。
