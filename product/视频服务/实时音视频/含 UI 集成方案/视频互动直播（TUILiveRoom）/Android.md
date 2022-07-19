## 组件介绍

TUILiveRoom 是一个开源的视频直播 UI 组件，通过在项目中集成 TUILiveRoom 组件，您只需要编写几行代码就可以为您的 App 添加“视频互动直播”场景。TUILiveRoom 包含 Android、iOS、小程序等平台的源代码，基本功能如下图所示：

>?TUIKit 系列组件同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信IM服务。即时通信 IM 服务详细计费规则请参见 [即时通信 - 价格说明](https://cloud.tencent.com/document/product/269/11673)，TRTC 开通会默认关联开通 IM SDK 的体验版，仅支持100个 DAU。

![](https://qcloudimg.tencent-cloud.cn/raw/ee1755293e9f4040a6f1433f4c8af73e.png)

[](id:model)
## 组件集成
[](id:model.step1)
### 步骤一：下载并导入 TUILiveRoom 组件
单击进入 [Github](https://github.com/tencentyun/TUILiveRoom) ，选择克隆/下载代码，然后拷贝 `Android/debug` ，`Android/tuiaudioeffect` ， `Android/tuibarrage` ， `Android/tuibeauty` ， `Android/tuigift` 和 `Android/tuiliveroom` 目录到您的工程中，并完成如下导入动作：

- 在 `setting.gradle` 中完成导入，参考如下：
```
include ':debug'
include ':tuibeauty'
include ':tuibarrage'
include ':tuiaudioeffect'
include ':tuigift'
include ':tuiliveroom'
```
- 在 `app` 的 `build.gradle` 文件中添加对 `tuiliveroom` 的依赖：
```
api project(":tuiliveroom")
```
- 在根目录的 `build.gradle` 文件中添加 `TRTC SDK` 和 `IM SDK` 的依赖：
```
ext {
    liteavSdk = "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
    imSdk = "com.tencent.imsdk:imsdk-plus:latest.release"
}
```

[](id:model.step2)
### 步骤二：配置权限及混淆规则
1. 在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请相机、读取存储权限）：
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

[](id:model.step3)
### 步骤三：初始化并登录组件
```java
// 1.添加事件监听及登录
TUILogin.addLoginListener(new TUILoginListener() {
    @Override
    public void onConnecting() {      // 正在连接中
        super.onConnecting();
    }
    @Override
    public void onConnectSuccess() {  // 连接成功通知
        super.onConnectSuccess();
    }
    @Override
    public void onConnectFailed(int errorCode, String errorMsg) {  // 连接失败通知
        super.onConnectFailed(errorCode, errorMsg);
    }
    @Override
    public void onKickedOffline() {  // 登录被踢下线通知（示例：账号在其他设备登录）
        super.onKickedOffline();
    }
    @Override
    public void onUserSigExpired() { // userSig过期通知
        super.onUserSigExpired();
    }
});
TUILogin.login(mContext, "Your SDKAppID", "Your userId", "Your userSig", new TUICallback() {
    @Override
    public void onSuccess() {
    }
    @Override
    public void onError(int errorCode, String errorMsg) {
        Log.d(TAG, "errorCode: " + errorCode + " errorMsg:" + errorMsg);
    }
});

// 2.初始化TUILiveRoom组件
TUILiveRoom mLiveRoom = TUILiveRoom.sharedInstance(mContext);
```

**参数说明：**
- **SDKAppID**：**TRTC 应用 ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cf6de5f10b77be75174d0ba359101f60.png)
- **Secretkey**：**TRTC 应用密钥**和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。建议结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的userSig，也可以参照我们的 [示例工程](https://github.com/tencentyun/TUILiveRoom/blob/main/Android/debug/src/main/java/com/tencent/liteav/debug/GenerateGlobalConfig.java#L118) 自行计算，更多信息请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。


[](id:model.step4)
### 步骤四：实现视频互动直播间
1. **主播端开播**
```java
mLiveRoom.createRoom(int roomId, String roomName, String coverUrl);
```
2. **观众端观看**
```java
mLiveRoom.enterRoom(roomId);
```
3. **观众与主播连麦 [TRTCLiveRoom#requestJoinAnchor](https://cloud.tencent.com/document/product/647/43391#requestjoinanchor)**
```java
// 1.观众端发起连麦请求
// LINK_MIC_TIMEOUT为超时时间
TRTCLiveRoom mTRTCLiveRoom=TRTCLiveRoom.sharedInstance(mContext);
mTRTCLiveRoom.requestJoinAnchor(mSelfUserId + "请求和您连麦", LINK_MIC_TIMEOUT
    new TRTCLiveRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            // 主播接受了观众的请求
            TXCloudVideoView view = new TXCloudVideoView(context);
            parentView.add(view);
            // 观众启动预览，开启推流
            mTRTCLiveRoom.startCameraPreview(true, view, null);
            mTRTCLiveRoom.startPublish(mSelfUserId + "_stream", null);
        }
    }
});

// 2.主播端收到连麦请求
mTRTCLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onRequestJoinAnchor(final TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, 
        String reason, final int timeout) {
        // 同意对方的连麦请求
        mTRTCLiveRoom.responseJoinAnchor(userInfo.userId, true, "同意连麦");
    }

    @Override
    public void onAnchorEnter(final String userId) {
        // 主播收到连麦观众的上麦通知
        TXCloudVideoView view = new TXCloudVideoView(context);
        parentView.add(view);
        // 主播播放观众画面
        mTRTCLiveRoom.startPlay(userId, view, null);
    }
});
```
4. **主播与主播 PK [TRTCLiveRoom#requestRoomPK](https://cloud.tencent.com/document/product/647/43391#requestroompk)**
```java
// 主播 A 创建12345的房间
mLiveRoom.createRoom(12345, "roomA", "Your coverUrl");
// 主播 B 创建54321的房间
mLiveRoom.createRoom(54321, "roomB", "Your coverUrl");

// 主播 A:
TRTCLiveRoom mTRTCLiveRoom=TRTCLiveRoom.sharedInstance(mContext);

// 1.主播 A 向主播 B 发起 PK 请求
mTRTCLiveRoom.requestRoomPK(54321, "B", 
    new TRTCLiveRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {  
        // 5.收到是否同意的回调
        if (code == 0) {
            // 用户接受
        } else {
            // 用户拒绝
        }
    }
});

mTRTCLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onAnchorEnter(final String userId) {
        // 6.收到 B 进房的通知
        mTRTCLiveRoom.startPlay(userId, mTXCloudVideoView, null);
    }
});

// 主播 B：
// 2.主播 B 收到主播 A 的消息
mTRTCLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onRequestRoomPK(
       final TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, final int timeout) {
        // 3.主播 B 回复主播 A 接受请求
        mTRTCLiveRoom.responseRoomPK(userInfo.userId, true, "");
    }
    @Override
    public void onAnchorEnter(final String userId) {
        // 4.主播 B 收到主播 A 进房的通知，播放主播 A 的画面
        mTRTCLiveRoom.startPlay(userId, mTXCloudVideoView, null);
    }
});
```

### 步骤五：美颜特效（可选）
TUILiveRoom 美颜使用了 [腾讯特效 SDK](https://cloud.tencent.com/document/product/616)，在使用美颜功能时，需要先设置 XMagic License，XMagic License 申请请参见 [XMagic License 申请指引](https://cloud.tencent.com/document/product/616/65878)。
```java
TUIBeautyView.getBeautyService().setLicense(context, “XMagicLicenseURL”, “XMagicLicenseKey”);
```

## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。

