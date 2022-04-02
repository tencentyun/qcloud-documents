## 组件介绍
TUIRoom 是一个开源的音视频 UI 组件，通过在项目中集成 TUIRoom 组件，您只需要编写几行代码就可以为您的 App 添加屏幕分享、美颜、低延时视频通话等。TUIRoom 同时支持 [iOS](https://cloud.tencent.com/document/product/647/45681)、[Windows](https://cloud.tencent.com/document/product/647/63494)，[Mac](https://cloud.tencent.com/document/product/647/63494) 等平台，基本功能如下图所示：

<table class="tablestyle">
<tbody><tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/6edda9960c4f116bc0a513b8254e47ba.jpg" width="250"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/3d4e0b6e557177d76724abf7fdcf7748.jpg" width="250"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/2e9f739a3a1a1511da693bd453f25061.jpg" width="250"></td>
</tr>
</tbody></table>

## 组件集成
### 步骤一：下载并导入 TUIRoom 组件
单击进入 [Github](https://github.com/tencentyun/TUIRoom) ，选择克隆/下载代码，然后拷贝 Android 下的 Source、TUICore、Beauty 目录到您的工程中，并完成如下导入动作：
- 在 `setting.gradle` 中完成导入，参考如下：
```
include ':Source'
include ':TUICore'
include ':Beauty'
```
- 在 app 的 `build.gradle` 文件中添加对 Source，TUICore，Beauty 的依赖：
```
api project(':Source')
```
- 在根目录的`build.gradle`文件中添加`TRTC SDK`和`IM SDK`的依赖：
```
ext {
    liteavSdk = "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
    imSdk = "com.tencent.imsdk:imsdk-plus:latest.release"
}
```

### 步骤二：配置权限及混淆规则
1. 在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请麦克风权限等）：
```
<uses-permission android:name="android.permission.INTERNET" />              
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```
2. 在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```
-keep class com.tencent.** { *; }
```

### 步骤三：创建并初始化 TUI 组件库
```java
  // 1.组件登录，
  TUILogin.init(this, 您的SDKAppId, config, new V2TIMSDKListener() {
            @Override
            public void onKickedOffline() {  // 登录被踢下线通知（示例：账号再其他设备登录）
            }
            @Override
            public void onUserSigExpired() { // userSig过期通知
            }
  });
  TUILogin.login("您的userId", "您的userSig", new V2TIMCallback() {
            @Override
            public void onError(int code, String msg) {
                Log.d(TAG, "code: " + code + " msg:" + msg);
            }
            @Override
            public void onSuccess() {
            }
  });
  
  // 2.初始化TUIRoomCore实例
  TUIRoomCore mTUIRoomCore = TUIRoomCore.getInstance(context);
  mTUIRoomCore.setListener(listener);

```

#### 参数说明
- **SDKAppID**：**TRTC 应用 ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cf6de5f10b77be75174d0ba359101f60.png)
- **Secretkey**：**TRTC 应用密钥**和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。建议结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的userSig，也可以参照我们的 [示例工程](https://github.com/tencentyun/TUIRoom/blob/main/Android/Debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java#L88) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。


### 步骤四：实现多人音视频互动
1. **实现房主创建多人音视频互动房间 [TUIRoomCore#createRoom](https://cloud.tencent.com/document/product/647/45668#createroom)**。
```java
// 1.房主调用创建房间
int roomId = 12345; //房间id
mTUIRoomCore.createRoom(roomId, TUIRoomCoreDef.SpeechMode.FREE_SPEECH,
        new TUIRoomCoreCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
            // 创建房间成功
            }
        }
    }
});
```
2. **实现其他成员加入音视频房间 [TUIRoomCore#enterRoom](https://cloud.tencent.com/document/product/647/45668#enterroom)**。
```java
// 1.其它成员调用加入房间
mTUIRoomCore.enterRoom(roomId, new TUIRoomCoreCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
            // 进入房间成功
            }
        }
    }
});

// 2.收到远端用户是否开启音频上行回调，此时可以刷新房间显示列表
@Override
public void onRemoteUserEnterSpeechState(final String userId) {
}
```
3. **实现房主解散房间 [TUIRoomCore#destroyRoom](https://cloud.tencent.com/document/product/647/45668#destroyroom)**。
```java
// 1.房主调用解散房间
mTUIRoomCore.destroyRoom(new TUIRoomCoreCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
                    
    }
});

成员端会收到 onDestroyRoom 回调消息，通知房间解散
@Override
public void onDestroyRoom() {
    //房主解散，退出房间
}
```
4. **实现成员离开房间 [TUIRoomCore#leaveRoom](https://cloud.tencent.com/document/product/647/45668#leaveroom)**。
```java
// 1.非房主身份调用离开房间
mTUIRoomCore.leaveRoom(new TUIRoomCoreCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
                    
    }
});

成员端会收到 onRemoteUserLeave 回调消息，通知有人离开
@Override
public void onRemoteUserLeave(String userId) {
        Log.d(TAG, "onRemoteUserLeave userId: " + userId);
}
```
5. **实现屏幕分享 [TUIRoomCore#startScreenCapture](https://cloud.tencent.com/document/product/647/45668#startscreencapture)**。
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
        mTUIRoom.stopCameraPreview();
        mTUIRoom.startScreenCapture(encParams, params);
}
```

## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
