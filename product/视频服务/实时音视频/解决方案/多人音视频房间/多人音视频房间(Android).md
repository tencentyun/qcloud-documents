## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验多人音视频通话的效果，包括屏幕分享、美颜、低延时视频通话等 TRTC 在多人音视频场景下的相关能力。
<table>
     <tr>
         <th>进入房间</th>  
         <th>屏幕分享</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/tuiroom_demo.gif" width="300px" height="640px"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/screencapture.gif" width="300px" height="640px"/></td>
</tr>
</table>

## 方案优势
- 集成了超低延时音视频通话、屏幕共享、美颜等能力，覆盖多人音视频房间常见功能。
- 根据需求二次开发，可以快速实现自定义 UI 界面和布局，助力业务快速上线。
- 封装了 TRTC 和 IM 基础 SDK，实现基础的逻辑控制，并提供接口方便调用。

## 接入指引
如需快速接入多人音视频房间功能，您可以直接基于我们提供的 App 进行修改适配，也可以使用的 App 内的 Module 模块实现自定义 UI 界面。

[](id:step1_1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助** > [**快速跑通Demo**](https://console.cloud.tencent.com/trtc/quickstart)。
2. 输入应用名称，例如 `TestTUIRoom` ，单击 **创建**。
3. 单击 **已下载，下一步**，跳过此步骤。

![](https://qcloudimg.tencent-cloud.cn/raw/823ef8e4989f4af2e0a632f6ff7f5ab2.png)

>!本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。

[](id:step1_2)
### 步骤2：下载 App 源码
单击进入 [TUIRoom](https://github.com/tencentyun/TUIRoom)，Clone 或者下载源码。

[](id:step1_3)
### 步骤3：配置 App 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Android/Debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java` 文件。
3. 设置 `GenerateTestUserSig.java` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为占位符（PLACEHOLDER），请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为占位符（PLACEHOLDER），请设置为实际的密钥信息。</ul>
<img src="https://main.qcloudimg.com/raw/f9b23b8632058a75b78d1f6fdcdca7da.png">
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。

>? 
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:step1_4)
### 步骤4：运行 App
使用 Android Studio（3.5以上的版本）打开源码工程 `TUIRoom`，单击 **运行** 即可开始调试本 App。

[](id:step1_5)
### 步骤5：修改工程源代码
源码文件夹 `Source` 中包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
| remote | 远端用户的列表界面 |
| widget | 通用的 UI 组件 |
| CreateRoomActivity.java | 创建音视频房间的界面 |
| RoomMainActivity.java | 音视频房间的主界面 |
| RoomVideoView.java | 封装了 TRTC 的 TXCloudVideoView，用于展示自己和远端用户的视频数据 |
| MemberEntity.java | UI 层的用户数据 |
| MemberListAdapter.java | 音视频房间主界面的 Adapter |

## 体验应用
>! 体验应用至少需要两台设备。
### 入口界面
请选择“创建房间”或“加入房间”，如图示。
<img src="https://qcloudimg.tencent-cloud.cn/raw/fbb6286ef73d5c8a079703efed44586b.png" width=300px>

### 创建房间页面
A 用户创建，房间号会默认生成，单击 **创建房间** 可以进入主页面。
<img src="https://qcloudimg.tencent-cloud.cn/raw/30b6a5bf3e8b153bdbecca5f3fedc3d6.png" width=300px>

### 加入房间页面
B 用户输入 A 用户的房间号，单击 **加入房间** 可以进入主页面。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7b81436bb76f59a72a6e90c7708788dc.png" width=300px>

### 主页面（A 用户）
<img src="https://qcloudimg.tencent-cloud.cn/raw/ca935d1dacb0f80b82905ef783b86154.png" width=300px>

### 麦上列表
麦上列表可以展示当前房间内的成员，对方打开摄像头和麦克风后可以看到对方的画面，听到对方的声音。

### 顶部控制栏
实现了耳麦切换，前后摄像头切换，房间信息，退出的功能。

### 底部工具栏
实现了控制自己的麦克风/摄像头，美颜，成员列表，设置等功能。

### 美颜
可在直播中针对画面进行美颜和特效展示。
<img src="https://qcloudimg.tencent-cloud.cn/raw/43233beb75d20fcc8727835f7bca579b.png" width=300px>

### 设置窗口
可对音视频相关参数进行设置，支持开启 **屏幕共享**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/b2fd0255e1077ec3f35272a77aa1e780.png" width=300px>

### 退出房间
- **主持人**：解散房间，即所有人退出房间。
- **非主持人**：自己离开房间。

## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TUIRoom) 中的 `Source` 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TUIRoomCore，您可以在 `TUIRoomCore.java` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![#600px](https://qcloudimg.tencent-cloud.cn/raw/26d50df38b49c1aa36446ce909aa9ce4.png)

[](id:step2_1)
### 步骤1：集成 SDK
多人音视频房间组件 TUIRoomCore 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

- **方法一：通过 Maven 仓库依赖**
	1. 在 dependencies 中添加 TRTCSDK 和 IMSDK 的依赖。
```java
dependencies {
	 compile "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
	 compile 'com.tencent.imsdk:imsdk:latest.release'
}
```
>?两个 SDK 的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
	2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
```java
defaultConfig {
	ndk {
			abiFilters "armeabi-v7a"
	}
}
```
	3. 单击 **Sync Now** ，自动下载 SDK 并集成到工程里。
- **方法二：通过本地 AAR 依赖**
若您的开发环境访问 Maven 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。
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

[](id:step2_2)
### 步骤2：配置权限及混淆规则
1. 在 `AndroidManifest.xml` 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请相机、读取存储权限）：
```java
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
2. 在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```java
-keep class com.tencent.** { *; }
```

[](id:step2_3)
### 步骤3：导入 TUIRoomCore 组件
拷贝以下目录中的所有文件到您的项目中：
```java
src/main/java/com/tencent/liteav/tuiroom/model
```

[](id:step2_4)
### 步骤4：创建并登录组件
1.  调用 TUICore 中的 TUILogin 进行登录，请参考如下示例：
```java
TUILogin.init(this, "sdkAppid", null, new V2TIMSDKListener() {

		@Override
		public void onKickedOffline() {

		}

		@Override
		public void onUserSigExpired() {

		}
	});
TUILogin.login("userId", "userSig", new V2TIMCallback() {
	@Override
	public void onError(int code, String msg) {

	}

	@Override
	public void onSuccess() {

	}
});
``` 

[](id:step2_5)
### 步骤5：设置昵称
登录成功后，调用 setSelfProfile 设置用户信息。

[](id:step2_6)
### 步骤6：创建房间
1. 成员调用 createRoom 接口创建新的房间，房间创建成功后以主持人身份进入房间，包括聊天室与 TRTC 房间。
```java
TUIRoomCore tuiRoomCore = TUIRoomCore.getInstance(context);
tuiCore.setListener(listener);
tuiCore.createRoom("roomId", TUIRoomCoreDef.SpeechMode.FREE_SPEECH,
        new TUIRoomCoreCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
            // 创建房间成功
            } else {
		}
	}
});

```
2. 调用 startCameraPreview 接口开始本地视频的采集与显示。
![](https://qcloudimg.tencent-cloud.cn/raw/e286295b14f04efb4f52be0da991ab56.png)

[](id:step2_7)
### 步骤7：解散房间
- 主持人调用 destoryRoom 接口解散房间，解散 IM 群聊，退出 TRTC 房间。
- 成员端会收到 onDestroyRoom 回调消息，通知群解散，退出 TRTC 房间。

[](id:step2_8)
### 步骤8：加入房间
1. 加入房间流程与创建流程基本一致，成员需要调用 enterRoom 接口进入房间。
2. 其他成员会收到 onRemoteUserEnter 回调，通知有成员进入房间。
```java
TUIRoomCore tuiRoomCore = TUIRoomCore.getInstance(context);
tuiCore.setListener(listener);
tuiCore.enterRoom("roomId", new TUIRoomCoreCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
            // 进入房间成功
            } else {
		}
	}
});
``` 
![](https://qcloudimg.tencent-cloud.cn/raw/bc320a6fbd044ddad021aed0a488c298.png)

[](id:step2_9)
### 步骤9：离开房间
1. 成员调用 leaveRoom 接口退出 IM 房间和 TRTC 房间。
2. 其他成团端收到 onRemoteUserLeave 回调，通知有成员离开房间。

[](id:step2_10)
### 步骤10：屏幕分享

1. 屏幕分享功能需向系统需要申请悬浮窗权限，需要您在 UI 中实现具体的逻辑。
2. 调用 TUIRoomCore的`startScreenCapture`实现分享，传入编码参数和录屏过程中的悬浮窗即可实现屏幕分享功能，具体信息请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58)。
3. 房间中其他成员会收到 onRemoteUserScreenVideoAvailable 的事件通知。

>! 屏幕分享和摄像头采集是两个互斥的操作，如果需要打开屏幕分享功能，请先调用 stopCameraPreview 关闭摄像头采集。

<dx-codeblock>
::: java java
// 1.在 AndroidManifest.xml 文件中添加 SDK 录屏功能的 activity 和权限
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
<application>
    <activity
        android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity"
        android:theme="@android:style/Theme.Translucent" />
</application>
:::
</dx-codeblock>
<dx-codeblock>
::: java java
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
        mTUIRoom.stopCameraPreview();
        mTUIRoom.startScreenCapture(encParams, params);
}
:::
</dx-codeblock>
