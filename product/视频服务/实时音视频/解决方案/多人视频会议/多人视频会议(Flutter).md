您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验多人视频会议的效果，包括屏幕分享、美颜、低延时会议等 TRTC 在多人视频会议场景下的相关能力。

[](id:DemoUI)
## 复用 App 的 UI 界面
[](id:ui.step1)
### 步骤1：创建新的应用

1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如 `TestMeetingRoom`，单击【创建】。
3. 单击【已下载，下一步】，跳过此步骤。

![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

>! 本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。

[](id:ui.step2)
### 步骤2：下载 App 源码

单击进入 [TRTCFlutterScenesDemo](https://github.com/tencentyun/TRTCFlutterScenesDemo)，Clone 或者下载源码。

[](id:ui.step3)
### 步骤3：配置 App 文件

1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `/lib/debug/GenerateTestUserSig.dart` 文件。
3. 设置 `GenerateTestUserSig.dart` 文件中的相关参数：
<ul style="margin:0">
    <li>SDKAPPID：默认为PLACEHOLDER，请设置为实际的 SDKAppID。</li>
    <li>SECRETKEY：默认为PLACEHOLDER，请设置为实际的密钥信息。</li>
</ul>
<img src="https://main.qcloudimg.com/raw/fba60aa9a44a94455fe31b809433cfa4.png">
4. 粘贴完成后，单击【已复制粘贴，下一步】即创建成功。
5. 编译完成后，单击【回到控制台概览】即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui.step4)
### 步骤4：编译运行

>! Android 端需要在真机下运行，不支持模拟器调试。

1. 执行 `flutter pub get`。
2. 编译运行调试：
<dx-tabs>
::: iOS\s端
1. 使用 XCode（11.0及以上的版本）打开源码目录下的 `/ios工程`。
2. 编译并运行 Demo 工程即可。
:::
::: Android\s端
1. 执行 `flutter run`。
2. 使用 Android Studio（3.5及以上的版本）打开源码工程，单击【运行】即可。
:::

</dx-tabs>

[](id:ui.step5)
### 步骤5：修改 Demo 源代码

源码中的 TRTCMeetingDemo 文件夹包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|-------|--------|
| TRTCMeetingIndex.dart | 创建或进入会议界面 |
| TRTCMeetingRoom.dart | 视频会议的主界面 |
| TRTCMeetingMemberList.dart | 参会人员列表界面 |
| TRTCMeetingSetting.dart | 视频会议相关参数设置界面 |

[](id:model)
## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TRTCFlutterScenesDemo) 中的 TRTCMeetingDemo 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCMeeting，您可以在 `TRTCMeeting.dart` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/bee48f1b790fd81a60f73d07fdb5ecc5.png)

[](id:model.step1)
### 步骤1：集成 SDK

互动直播组件 TRTCMeeting 依赖 [TRTC SDK](https://pub.dev/packages/tencent_trtc_cloud) 和 [IM SDK](https://pub.dev/packages/tencent_im_sdk_plugin)，您可以通过配置 `pubspec.yaml` 自动下载更新。

在项目的 `pubspec.yaml` 中写如下依赖：
```
dependencies:
  tencent_trtc_cloud: 最新版本号
  tencent_im_sdk_plugin: 最新版本号
```

[](id:model.step2)
### 步骤2：配置权限及混淆规则

<dx-tabs>
::: iOS\s端
1. 需要在 `Info.plist` 中加入对相机和麦克风的权限申请：
```
<key>NSMicrophoneUsageDescription</key>
<string>授权麦克风权限才能正常语音通话</string>
```
:::
::: Android\s端
1. 打开 `/android/app/src/main/AndroidManifest.xml` 文件。
2. 将 `xmlns:tools="http://schemas.android.com/tools"` 加入到 manifest 中。
3. 将 `tools:replace="android:label"` 加入到 application 中。
>? 若不执行此步，会出现 [Android Manifest merge failed 编译失败](https://cloud.tencent.com/document/product/647/51623#que6) 问题。

![图示](https://main.qcloudimg.com/raw/7a37917112831488423c1744f370c883.png)
:::
</dx-tabs>

[](id:model.step3)
### 步骤3：导入 TRTCMeeting 组件

拷贝以下目录中的所有文件到您的项目中：
```
lib/TRTCMeetingDemo/model/
```

[](id:model.step4)
### 步骤4：创建并登录组件

1. 调用 `sharedInstance` 接口可以创建一个 TRTCMeeting 组件的实例对象。
2. 调用 `registerListener` 函数注册组件的事件通知。
3. 调用 `login` 函数完成组件的登录，请参考下表填写关键参数：
<table>
    <tr>
        <th>参数名</th>
        <th>作用</th>
    </tr>
    <tr>
        <td>sdkAppId</td>
        <td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
    </tr>
    <tr>
        <td>userId</td>
        <td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z、A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
    </tr>
    <tr>
        <td>userSig</td>
        <td>腾讯云设计的一种安全保护签名，获取方式请参考 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
    </tr>
</table>

<dx-codeblock>
::: dart dart
TRTCMeeting trtcMeeting = TRTCMeeting.sharedInstance();
trtcMeeting.registerListener(onListener);
ActionCallback res = await trtcMeeting.login(
    GenerateTestUserSig.sdkAppId,
    userId,
    GenerateTestUserSig.genTestSig(userId),
);
if (res.code == 0) {
    // 登录成功
}
:::
</dx-codeblock>

[](id:model.step5)
### 步骤5：创建多人会议

1. 主持人执行 [步骤4](#model.step4) 登录后，可以调用 setSelfProfile 设置自己的昵称和头像。
2. 主持人调用 createMeeting 创建新的会议房间。
3. 主持人可以调用 startCameraPreview 进行视频画面的采集，也可以调用 startMicrophone 进行声音的采集。
4. 如果主持人有美颜的需求，界面上可以配置美颜调节按钮调用，通过 getBeautyManager 进行美颜设置。
>? 非企业版 SDK 不支持变脸和贴图挂件功能。

![](https://main.qcloudimg.com/raw/6e0cf097f46a8953cbebcf9995ba28c1.png)

<dx-codeblock>
::: dart dart
// 1. 主持人设置昵称和头像
trtcMeeting.setSelfProfile('my_name', 'my_avatar');

// 2. 主持人创建会议
ActionCallback res = await trtcMeeting.createMeeting(roomId);
if (res.code == 0) {
    // 创建会议成功
    // 3. 打开摄像头和音频采集
    trtcMeeting.startCameraPreview(true, TRTCCloudVideoViewId);
    trtcMeeting.startMicrophone();
    // 4. 设置美颜
    trtcMeeting.getBeautyManager().setBeautyStyle(TRTCCloudDef.TRTC_BEAUTY_STYLE_PITU);
    trtcMeeting.getBeautyManager().setBeautyLevel(6);
}
:::
</dx-codeblock>

[](id:model.step6)
### 步骤6：参会成员进入多人会议

1. 参会成员执行 [步骤4](#model.step4) 登录后，可以调用 setSelfProfile 设置自己的昵称和头像。
2. 参会成员调用 enterMeeting 并传入会议房间号即可进入会议房间。
3. 参会成员可以调用 startCameraPreview 进行视频画面的采集，也可以调用 startMicrophone 进行声音的采集。
4. 如果有其他的参会成员打开了摄像头，会收到 onUserVideoAvailable 的事件，此时可以调用 startRemoteView 并传入 userId 开始播放。

![](https://main.qcloudimg.com/raw/d8b796bbe41c9da1af40740916e84d70.png)

<dx-codeblock>
::: dart dart
// 1. 参会成员设置昵称和头像
trtcMeeting.setSelfProfile('my_name', 'my_avatar');

// 2. 参会成员调用 enterMeeting 进入会议房间
ActionCallback res = await trtcMeeting.enterMeeting(roomId);
if (res.code == 0) {
    // 进入会议成功
    // 3. 打开摄像头和音频采集
    trtcMeeting.startCameraPreview(true, TRTCCloudVideoViewId);
    trtcMeeting.startMicrophone();
    // 4. 设置美颜
    trtcMeeting.getBeautyManager().setBeautyStyle(TRTCCloudDef.TRTC_BEAUTY_STYLE_PITU);
    trtcMeeting.getBeautyManager().setBeautyLevel(6);
}

// 5. 参会成员收到其他成员摄像头打开的通知，开始播放
trtcMeeting.registerListener(onListener);
onListener(TRTCMeetingDelegate type, param) {
    switch (type) {
        case TRTCMeetingDelegate.onUserVideoAvailable:
            if (param['available']) {
                trtcMeeting.startCameraPreview(
                    param['userId'],
                    TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG,
                    TRTCCloudVideoViewId
                );
            } else {
                trtcMeeting.stopRemoteView(
                    param['userId'],
                    TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG
                );
            }
            break;
    }
}
:::
</dx-codeblock>

[](id:model.step7)
### 步骤7：屏幕分享

1. 屏幕分享功能需向系统申请悬浮窗权限，需要您在 UI 中实现具体的逻辑。
2. 调用 startScreenCapture，传入编码参数和录屏过程中的悬浮窗即可实现屏幕分享功能，具体信息请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58)。
3. 会议中其他成员会收到 onUserVideoAvailable 的事件通知。

>! 屏幕分享和摄像头采集是两个互斥的操作，如果需要打开屏幕分享功能，请先调用 stopCameraPreview 关闭摄像头采集。详情请参见 [TRTC SDK](https://cloud.tencent.com/document/product/647/53877)。

<dx-codeblock>
::: dart dart
await trtcMeeting.stopCameraPreview();
trtcMeeting.startScreenCapture(
    videoFps: 10,
    videoBitrate: 1600,
    videoResolution: TRTCCloudDef.TRTC_VIDEO_RESOLUTION_1280_720,
    videoResolutionMode: TRTCCloudDef.TRTC_VIDEO_RESOLUTION_MODE_PORTRAIT,
    appGroup: iosAppGroup,
);
:::
</dx-codeblock>

[](id:model.step8)
### 步骤8：实现文字聊天和禁言消息

- 通过 sendRoomTextMsg 可以发送普通的文本消息，所有在该会议内的参会人员均可以收到 onRecvRoomTextMsg 回调。即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
<dx-codeblock>
::: dart dart
// 发送端：发送文本消息
trtcMeeting.sendRoomTextMsg('Hello Word!');
// 接收端：监听文本消息
trtcMeeting.registerListener(onListener);
onListener(TRTCMeetingDelegate type, param) {
    switch (type) {
        case TRTCMeetingDelegate.onRecvRoomTextMsg:
            print('收到来自' + param['userName'] + '的消息：' + param['message']);
            break;
    }
}
:::
</dx-codeblock>

- 通过 sendRoomCustomMsg 可以发送自定义（信令）的消息，所有在该会议内的参会人员均可以收到 onRecvRoomCustomMsg 回调。自定义消息常用于传输自定义信令，例如用于禁言之类的会场控制等。
<dx-codeblock>
::: dart dart
// 发送端：您可以通过自定义 cmd 来区分禁言通知
// eg: "CMD_MUTE_AUDIO"表示禁言通知
trtcMeeting.sendRoomCustomMsg('CMD_MUTE_AUDIO', '1');
// 接收端：监听自定义消息
trtcMeeting.registerListener(onListener);
onListener(TRTCMeetingDelegate type, param) {
    switch (type) {
        case TRTCMeetingDelegate.onRecvRoomCustomMsg:
            if (param['command'] == 'CMD_MUTE_AUDIO') {
                // 收到禁言通知
                print('收到来自' + param['userName'] + '的禁言通知：' + param['message']);
                trtcMeeting.muteLocalAudio(message == '1');
            }
            break;
    }
}
:::
</dx-codeblock>
