## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 Demo 体验多人视频会议的效果，包括屏幕分享、美颜、低延时会议等 TRTC 在多人视频会议场景下的相关能力。
<table>
     <tr>
         <th>进入会议</th>  
         <th>屏幕分享</th>  
     </tr>
<tr>
<td><img src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/gif/enterroom.gif"/></td>
<td><img src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/gif/screencapture.gif"/></td>
</tr>
</table>

如需快速接入多人视频会议功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCMeeting 组件并实现自定义 UI 界面。

<span id="DemoUI"> </span>
## 复用 Demo 的 UI 界面
<span id="ui.step1"></span>
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如 `TestMeetingRoom` ，单击【创建应用】。

>?本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。



<span id="ui.step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/Android)】跳转至 Github（或单击【[ZIP](https://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Android_latest.zip)】），下载相关 SDK 及配套的 Demo 源码。
 ![](https://main.qcloudimg.com/raw/c3067ef0d7244bfdd3bc31eef191c5fc.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。

<span id="ui.step3"></span>
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#ui.step2) 中下载的源码包。
2. 找到并打开 `Android/TRTCScenesDemo/debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java` 文件。
3. 设置 `GenerateTestUserSig.java` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
    <img src="https://main.qcloudimg.com/raw/345c3e8915ef988eb158833d1655d0c5.png">
4. 返回实时音视频控制台，单击【粘贴完成，下一步】。
5. 单击【关闭指引，进入控制台管理应用】。

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

<span id="ui.step4"></span>
### 步骤4：运行 Demo
使用 Android Studio（3.5以上的版本）打开源码工程 `TRTCScenesDemo`，单击【运行】即可开始调试本 Demo。

<span id="ui.step5"></span>
### 步骤5：修改 Demo 源代码
源码文件夹 `trtcmeetingdemo` 中包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
| remote | 远端用户的列表界面 |
| widget | 通用的 UI 组件 |
| CreateMeetingActivity.java | 创建会议的界面 |
| MeetingMainActivity.java | 视频会议的主界面 |
| MeetingVideoView.java | 封装了 TRTC 的 TXCloudVideoView，用于展示自己和远端用户的视频数据 |
| MemberEntity.java | UI 层的用户数据 |
| MemberListAdapter.java | 视频会议主界面的 Adapter |

<span id="model"> </span>
## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TRTCSDK/tree/master/Android/TRTCScenesDemo/trtcmeetingdemo/src/main/java/com/tencent/liteav/meeting) 中的 trtcmeetingdemo 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCMeeting，您可以在`TRTCMeeting.java` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/bee48f1b790fd81a60f73d07fdb5ecc5.png)

<span id="model.step1"> </span>
### 步骤1：集成 SDK
多人视频会议组件 TRTCMeeting 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

**方法一：通过 Maven 仓库依赖**
1. 在 dependencies 中添加 TRTCSDK 和 IMSDK 的依赖。
```
dependencies {
       compile "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
       compile 'com.tencent.imsdk:imsdk:latest.release'
}
```
>?两个 SDK 的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
>
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
      ndk {
          abiFilters "armeabi-v7a"
      }
}
```
3. 单击【Sync Now】，自动下载 SDK 并集成到工程里。

**方法二：通过本地 AAR 依赖**
若您的开发环境访问 maven 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。
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
### 步骤2：配置权限及混淆规则
在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请相机、读取存储权限）：
```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-feature android:name="android.hardware.camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```
-keep class com.tencent.** { *; }
```

<span id="model.step3"> </span>
### 步骤3：导入 TRTCMeeting 组件
拷贝以下目录中的所有文件到您的项目中：
```
src/main/java/com/tencent/liteav/meeting/model
```

<span id="model.step4"> </span>
### 步骤4：创建并登录组件
1. 调用`sharedInstance`接口可以创建一个 TRTCMeeting 组件的实例对象。
2. 调用`setDelegate`函数注册组件的事件通知。
3. 调用`login`函数完成组件的登录，请参考下表填写关键参数：
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
<tr>
<td>callback</td>
<td>登录回调，成功时 code 为0。</td>
</tr>
</table>
<pre>
TRTCMeeting trtcMeeting = TRTCMeeting.sharedInstance(this);
trtcMeeting.login(SDKAPPID, userId, userSig, new TRTCMeetingCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            //登录成功
        }
    }
});
</pre>

<span id="model.step5"> </span>
### 步骤5：创建多人会议
1. 主持人执行 [步骤4](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 主持人调用`setDelegate`可以进行事件调用`createMeeting`创建新的会议房间。
3. 主持人可以调用`startCameraPreview`进行视频画面的采集，也可以调用`startMicrophone`进行声音的采集。
4. 如果主持人有美颜的需求，界面上可以配置美颜调节按钮调用，通过`getBeautyManager`进行美颜设置。
>?非企业版 SDK 不支持变脸和贴图挂件功能。
>
![](https://main.qcloudimg.com/raw/6e0cf097f46a8953cbebcf9995ba28c1.png)

```java
// 1.主持人设置昵称和头像
trtcMeeting.setSelfProfile("my_name", "my_avatar", null);

// 2.主持人创建房间
trtcMeeting.createMeeting(roomId, new TRTCMeetingCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            // 3.打开摄像头和音频采集
            TXCloudVideoView txCloudVideoView = new TXCloudVideoView(TestMeetingActivity.this);
            parentView.add(view);
            trtcMeeting.startCameraPreview(true, txCloudVideoView);
            trtcMeeting.startMicrophone();
            // 4.设置美颜
            trtcMeeting.getBeautyManager().setBeautyStyle(1);
            trtcMeeting.getBeautyManager().setBeautyLevel(6);
        }
    }
});
```

<span id="model.step6"> </span>
### 步骤6：参会成员进入多人会议
1. 参会成员执行 [步骤4](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 参会成员调用`enterMeeting`并传入会议房间号即可进入会议房间。
3. 参会成员可以调用`startCameraPreview`进行视频画面的采集，调用`startMicrophone`进行声音的采集。
4. 如果有其他的参会成员打开了摄像头，会收到`onUserVideoAvailable`的事件，此时可以调用`startRemoteView`并传入 userId 开始播放。

![](https://main.qcloudimg.com/raw/d8b796bbe41c9da1af40740916e84d70.png)

```java
// 1.参会成员设置昵称和头像
trtcMeeting.setSelfProfile("my_name", "my_avatar", null);

// 2.参会成员调用 enterMeeting 进入会议房间号
trtcMeeting.enterMeeting(roomId, new TRTCMeetingCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            // 3.进房成功，打开自己的摄像头和麦克风，同时可以打开美颜功能
            TXCloudVideoView txCloudVideoView = new TXCloudVideoView(TestMeetingActivity.this);
            parentView.add(view);
            trtcMeeting.startCameraPreview(true, txCloudVideoView);
            trtcMeeting.startMicrophone();
            trtcMeeting.getBeautyManager().setBeautyStyle(1);
            trtcMeeting.getBeautyManager().setBeautyLevel(6);
        }
    }
});

// 4.参会成员收到其他成员摄像头打开的通知，开始播放
trtcMeeting.setDelegate(new TRTCMeetingDelegate() {
    @Override
    public void onUserVideoAvailable(String userId, boolean available) {
        if (available) {
            TXCloudVideoView txCloudVideoView = new TXCloudVideoView(TestMeetingActivity.this);
            parentView.add(view);
            trtcMeeting.startRemoteView(userId, txCloudVideoView);
        } else {
            trtcMeeting.stopRemoteView(userId, null);
        }
    }
});
```

<span id="model.step7"> </span>
### 步骤7：屏幕分享

1. 屏幕分享功能需向系统需要申请悬浮窗权限，需要您在 UI 中实现具体的逻辑。
2. 调用 `startScreenCapture`，传入编码参数和录屏过程中的悬浮窗即可实现屏幕分享功能，具体信息请参见 [TRTC SDK](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58)。
3. 会议中其他成员会收到 `onUserVideoAvailable` 的事件通知。
>!屏幕分享和摄像头采集是两个互斥的操作，如果需要打开屏幕分享功能，请先调用`stopCameraPreview`关闭摄像头采集。

```java
// 1.在 AndroidManifest.xml 文件中添加 SDK 录屏功能的 activity 和权限
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
<application>
    <activity
        android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity"
        android:theme="@android:style/Theme.Translucent" />
</application>
// 2.在您的界面中申请悬浮窗的权限
if (Build.VERSION.SDK_INT >= 23) {
    if (!Settings.canDrawOverlays(getApplicationContext())) {
        Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION, Uri.parse("package:" + getPackageName()));
        startActivityForResult(intent, 100);
    } else {
        startScreenCapture();
    }
} else {
    startScreenCapture();
}

// 3.系统回调结果
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == 100) {
        if (Build.VERSION.SDK_INT >= 23) {
            if (Settings.canDrawOverlays(this)) {
                // 用户成功授权
                startScreenCapture();
            } else {
            }
        }
    }
}
// 4.打开屏幕分享
private void startScreenCapture() {
        TRTCCloudDef.TRTCVideoEncParam encParams = new TRTCCloudDef.TRTCVideoEncParam();
        encParams.videoResolution = TRTCCloudDef.TRTC_VIDEO_RESOLUTION_1280_720;
        encParams.videoResolutionMode = TRTCCloudDef.TRTC_VIDEO_RESOLUTION_MODE_PORTRAIT;
        encParams.videoFps = 10;
        encParams.enableAdjustRes = false;
        encParams.videoBitrate = 1200;

        TRTCCloudDef.TRTCScreenShareParams params = new TRTCCloudDef.TRTCScreenShareParams();
        mTRTCMeeting.stopCameraPreview();
        mTRTCMeeting.startScreenCapture(encParams, params);
}
```

<span id="model.step8"> </span>
### 步骤8：实现文字聊天和禁言消息
- 通过`sendRoomTextMsg`可以发送普通的文本消息，所有在该房间内的主播和观众均可以收到`onRecvRoomTextMsg`回调。
 即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
```java
// 发送端：发送文本消息
trtcMeeting.sendRoomTextMsg("Hello Word!", null);
// 接收端：监听文本消息
trtcMeeting.setDelegate(new TRTCMeetingDelegate() {
    @Override
    public void onRecvRoomTextMsg(
		    String message, TRTCMeetingDef.UserInfo userInfo) {
        Log.d(TAG, "收到来自" + userInfo.userName + "的消息:" + message);
    }
});
```
- 通过`sendRoomCustomMsg`可以发送自定义（信令）的消息，所有在该房间内的主持人和与会观众均可以收到`onRecvRoomCustomMsg`回调。
自定义消息常用于传输自定义信令，例如用于禁言之类的会场控制等。
```java
// 发送端：您可以通过自定义 Cmd 来区分禁言通知
// eg:"CMD_MUTE_AUDIO"表示禁言通知
trtcMeeting.sendRoomCustomMsg("CMD_MUTE_AUDIO", "1", null);
// 接收端：监听自定义消息
trtcMeeting.setDelegate(new TRTCMeetingDelegate() {
    @Override
    public void onRecvRoomCustomMsg(String cmd, 
		    String message, TRTCMeetingDef.UserInfo userInfo) {
        if ("CMD_MUTE_AUDIO".equals(cmd)) {
            // 收到禁言通知
            Log.d(TAG, "收到来自" + userInfo.userName + "的禁言通知:" + message);
            trtcMeeting.muteLocalAudio("1".equals(message));
        }
    }
});
```
