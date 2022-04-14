## 组件介绍

`TUIPusher` 组件是一套开源的、完整的视频直播互动推流组件，它基于腾讯云 [直播 Live SDK](https://cloud.tencent.com/document/product/454/19074) 和 [即时通信 IM SDK](https://cloud.tencent.com/document/product/269/1498) ，实现直播推流，直播 PK 等功能，同时支持弹幕、点赞、美颜等外挂插件，使用 `TUIPusher` 组件您可以快速搭建诸如秀场直播、电商直播等场景化解决方案。
<img src="https://qcloudimg.tencent-cloud.cn/raw/56974460aea1eff23adb1ab6410c910d.png" width="900"/>

## 组件集成

### 步骤一：下载并导入 TUIPusher 组件

1. 单击进入 [**Github**](https://github.com/tencentyun/XiaoZhiBo) ，选择克隆或者下载小直播工程代码。
2. 拷贝 Android/tuipusher 、Android/tuiaudioeffect、Android/tuibeauty、Android/tuibarrage、Android/tuigift 等文件夹到您的工程中。
3. 在 `setting.gradle` 中完成导入，参考如下：
```
include ':tuipusher'
include ':tuiaudioeffect'
include ':tuibeauty'
include ':tuibarrage' 
include ':tuigift' 
```
4. 在 `app` 的 `build.gradle` 文件中添加对 `tuipusher` 等 moudle 的依赖：
```
api project(':tuipusher')
api project(':tuiaudioeffect')
api project(':tuibeauty')
api project(':tuibarrage')
api project(':tuigift')
```

### 步骤二：配置权限及混淆规则

1. 在 `AndroidManifest.xml` 中配置 `App` 的权限，`SDK` 需要以下权限（6.0以上的 Android 系统需要动态申请相机、麦克风权限等）：
```
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
```
2. 在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```
-keep class com.tencent.** { *; }
```


### 步骤三：初始化&创建组件

如果您未开通腾讯云直播相关服务，请先按照如下步骤开通相关服务：
-   [开通云直播服务](https://console.cloud.tencent.com/live/livestat)，并在 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 页面中配置推流域名和拉流域名。
-  [创建应用并绑定 License](https://console.cloud.tencent.com/live/license) ，并记录下 `LICENSEURL`、`LICENSEURLKEY` 等关键信息。
```java
// 1. 初始化直播服务
V2TXLivePremier.setLicence(this, "您的LICENSEURL", "您的LICENSEURLKEY");

// 2. 创建TUIPusher组件
TUIPusherView mTUIPusherView = new TUIPusherView(Context);

// 3. 设置诸如推流开始、推流结束等事件监听
mTUIPusherView.setTUIPusherViewListener(new TUIPusherViewListener() {
        ...
}
```

### 步骤四：有互动直播推流
1.  **服务开通**
因为连麦& PK 时需要更低的延时需求，需要在腾讯云直播控制台控制台开通对应的连麦应用服务，如果您未开通，请登录**云直播管理控制台**选择 **[应用管理](https://console.cloud.tencent.com/live/micro/appmanage)** ，单击**新建连麦应用**输入应用名称（例如 `TUIPusher`），然后在该应用的对应操作栏中，选择**应用信息**进入应用管理页，查看并记录应用的 **SDKAppID** 和 **SECRETKEY（密钥）**。
![img](https://qcloudimg.tencent-cloud.cn/raw/cb2b2381b92994404dfece3cdaf77608.png)
>! 因为在连麦/PK过程中，观众端还是需要正常观看CDN流，所以需要进入 **CDN 观看配置**页，开启旁路推流，推荐全局自动旁路。
>![](https://qcloudimg.tencent-cloud.cn/raw/4273ee28f1416417d56402ae4d8cf7ed.png)
2. **组件登录**
因为 `PK` 服务，需要主播间相互通信，所以需要进行单独登录，登录流程如下：
```java
  TUILogin.init(this, "您的SDKAppId", config, new V2TIMSDKListener() {
            @Override
            public void onKickedOffline() {  // 登录被踢下线通知（示例：账号在其他设备登录）
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
```
**登录组件参数说明：**
	- **SDKAppID**：即服务开通中记录到的 **SDKAppID** 信息。
	-  **SECRETKEY**： 即服务开通中记录到的 **SECRETKEY（密钥）**。
	-  **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
	-  **userSig**：根据 SDKAppId、userId，SECRETKEY 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [示例工程](https://github.com/tencentyun/XiaoZhiBo/blob/main/Android/debug/src/main/java/com/tencent/liteav/debug/GenerateGlobalConfig.java#L118) 自行计算，更多信息请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/454/14548)。
3. **开始推流**
基于 `RTC` 协议的推流 `URL` 的生成，可以参考 [示例工程](https://github.com/tencentyun/XiaoZhiBo/blob/main/Android/app/src/main/java/com/tencent/liteav/demo/utils/URLUtils.java#L33) 中封装好的 Utils 方法，基本示例如下，具体参数信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
```java
mTUIPusherView.start(String url);
```
4. **停止推流**
```java
mTUIPusherView.stop();
```
5. **发起 PK 请求**
调用 `mTUIPusherView.sendPKRequest()` 后会向接收方发起 Pk 请求，请求超时发送方设置的 `mTUIPusherView.setTUIPusherViewListener` 回调中， `onPKTimeout` 回调会收到超时通知。
```java
mTUIPusherView.sendPKRequest(String userId);
 
public void onPKTimeout(TUIPusherView pusherView) {
    Toast.makeText(mContext, "PK request timed out", Toast.LENGTH_SHORT).show();
}
```
6.  **接受 PK 请求**
接收方设置的 `mTUIPusherView.setTUIPusherViewListener` 回调中，`onReceivePKRequest` 回调会通知接收方收到 PK 请求，可在此回调中处理 PK 请求。
``` java
public void onReceivePKRequest(TUIPusherView pushView, String userId, ResponseCallback callback) {
                showPKDialog(userId, callback);
}

private void showPKDialog(String userId, final TUIPusherViewListener.ResponseCallback callback) {
    if (mPKDialog == null) {
        final TextView textView = new TextView(this);
        textView.setText(userId + “invited linkMic”));
        mPKDialog = new AlertDialog.Builder(this, R.style.PKDialogTheme)
                .setView(textView)
                .setPositiveButton("confirm", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        callback.response(true);
                    }
                })
                .setNegativeButton("cacel", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        callback.response(false);
                    }
                }).create();
    }
    mPKDialog.show();
}
```


### 步骤五：无互动直播推流

如果您的应用中无连麦或 `PK` 等互动场景，可以选择标准的 `RMTP` 协议进行推流，具体步骤如下：

- **开始推流**
基于 RTMP 推流 URL 的生成，可以参考 [示例工程](https://github.com/tencentyun/XiaoZhiBo/blob/main/Android/app/src/main/java/com/tencent/liteav/demo/utils/URLUtils.java#L33) 中封装好的 Utils 方法，基本规则如下图，具体参数信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
```java
mTUIPusherView.start(String url);
```
- **停止推流**
```java
mTUIPusherView.stop();
```

## 交流&反馈

更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
