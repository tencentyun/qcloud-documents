## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验实时音视频通话的效果。
<table>
<tr>
   <th>主动呼叫</th>
   <th>被叫接听</th>
 </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/video1.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/video2.gif"/></td>
</tr>
</table>


>! 为方便您快速实现音视频通话功能，我们对 TUICalling 组件进行了改造，通话UI在TUICalling 组件内部实现，您可以无需关注UI。

[](id:ui)

## 运行并体验 App

[](id:ui.step1)

### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助>[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 输入应用名称，例如 `TestVideoCall` ，单击 **创建**。
3. 单击 **已下载，下一步**，跳过此步骤。

![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)
>!本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。


[](id:ui.step2)
### 步骤2：下载 App 源码
单击进入 [TUICalling](https://github.com/tencentyun/TUICalling)，Clone 或者下载源码。

[](id:ui.step3)
### 步骤3：配置 App 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Android/Debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java` 文件。
3. 设置 `GenerateTestUserSig.java` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为占位符（PLACEHOLDER），请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为占位符（PLACEHOLDER），请设置为实际的密钥信息。</ul>
<img src="https://main.qcloudimg.com/raw/f9b23b8632058a75b78d1f6fdcdca7da.png">
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui.step4)
### 步骤4：运行 App

使用 Android Studio（3.5 以上的版本）打开源码工程 `TUICalling`，单击 **运行** 即可开始调试本 App。



## 体验应用
>! 体验应用至少需要两台设备。

### 用户 A
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
<img src="https://main.qcloudimg.com/raw/a0c73f6904ac152a84cdf4d619171fc4.png" width="320"/>
2. 输入要拨打的 userId，单击搜索，如下图示：
<img src="https://main.qcloudimg.com/raw/61edd11a23197ebce26e91863f9fef63.png" width="320"/>
3. 单击 **呼叫**，选择拨打 **视频通话** （**请确保被叫方保持在应用内，否则可能会拨打失败**）。<br>
<img src="https://main.qcloudimg.com/raw/450e50dd4bb58e2950d6574ab88715e2.png" width="320"/>

### 用户 B
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
<img src="https://main.qcloudimg.com/raw/94fcd741becbcfe4cca97778e180e4ca.png" width="320"/>
2. 进入主页，等待接听来电。



[](id:model)
## 具体接入流程

[源码](https://github.com/tencentyun/TUICalling/tree/master/Android/Source/src/main/java/com/tencent/liteav/trtccalling) 文件夹 `Source` 中包含两个子文件夹 ui 和 model，其中 model 文件夹中包含了我们对外暴露的开源组件 TUICallingManager，您可以在  `TUICalling.java`  文件中看到该组件提供的接口函数。
![](https://main.qcloudimg.com/raw/18e2e6fd62ade4a8bac560d45f4fbab4.png)


您直接使用开源组件 TUICalling 的 TUICallingManager 即可轻松实现音视频通话功能，而无需再自己实现复杂的通话 UI 界面和逻辑。

[](id:model.step1)
### 步骤1：集成 SDK

音视频通话组件 TUICalling 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

#### 方法一：通过 Maven 仓库依赖

1. 在 dependencies 中添加 TRTCSDK 和 IMSDK 的依赖。
<dx-codeblock>
::: java java
dependencies {
    compile "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
    compile 'com.tencent.imsdk:imsdk:latest.release'

    // 由于我们使用到了 gson 解析，所以还需要依赖 google 的 Gson
    compile 'com.google.code.gson:gson:latest.release'
}
:::
</dx-codeblock>
>?两个 SDK 产品的最新版本号，可以在 [实时音视频](https://github.com/tencentyun/TRTCSDK) 和 [即时通信 IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
<dx-codeblock>
::: java java
defaultConfig {
      ndk {
            abiFilters "armeabi-v7a"
      }
}
:::
</dx-codeblock>
3. 单击 **Sync Now** 同步 SDK。
>?若您的网络连接 jcenter 没有问题，SDK 会自动下载集成到工程里。


#### 方法二：通过本地 AAR 依赖
如果您的开发环境访问 Maven 仓库较慢，可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。

| SDK      | 下载页面                                                     | 集成指引                                                     |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| TRTC SDK | [DOWNLOAD](https://cloud.tencent.com/document/product/647/32689) | [集成文档](https://cloud.tencent.com/document/product/647/32175) |
| IM SDK   | [DOWNLOAD](https://cloud.tencent.com/document/product/269/36887) | [集成文档](https://cloud.tencent.com/document/product/269/32679) |

[](id:model.step2)

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

[](id:model.step3)

### 步骤3：导入 TUICalling 组件

include App下的 Source 到您的项目中：

```
include ':Source'
```

[](id:model.step4)

### 步骤4：初始化并登录组件

1. 调用 `TUICallingManager.sharedInstance()` 进行组件初始化。
2. 调用 `TUILogin.init(context, SDKAppID, config, listener)` 进行登录初始化。
3. 调用 `TUILogin.login(userId, userSig, callback)` 完成组件的登录，其中几个关键参数的填写请参考下表：
 <table>
<tr><th>参数名</th><th>作用</th></tr>
<tr>
<td>SDKAppID</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr><tr>
<td>userId</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
</tr><tr>
<td>userSig</td>
<td>腾讯云设计的一种安全保护签名，计算方式请参考 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
</tr>
</tr><tr>
<td>config</td>
<td>SDK配置。用于设置日志级别和日志回调（也可传null），详情可参考下方示例代码。</td>
</tr><tr>
</tr><tr>
<td>listener</td>
<td>IM监听器。用于接收一些必要的系统回调通知，比如：被踢下线、userSig过期等，详情可参考下方示例代码。</td>
</tr><tr>
</tr><tr>
<td>callback</td>
<td>登录结果监听器。通知登录是否成功，详情可参考下方示例代码。</td>
</tr><tr>
</table>
<dx-codeblock>
::: java java
     // 组件初始化
     TUICallingManager manager = TUICallingManager.sharedInstance();
  // 登录
  V2TIMSDKConfig config = new V2TIMSDKConfig();
  config.setLogLevel(V2TIMSDKConfig.V2TIM_LOG_DEBUG);
  config.setLogListener(new V2TIMLogListener() {
        @Override
        public void onLog(int logLevel, String logContent) {
                
        }
  });
  TUILogin.init(this, ${您的SDKAPPID}, config, new V2TIMSDKListener() {

            @Override
            public void onKickedOffline() {  // 登录被踢下线通知
                mIsKickedOffline = true;
                checkUserStatus();
            }

            @Override
            public void onUserSigExpired() { // suerSig过期通知
                mIsUserSigExpired = true;
                checkUserStatus();
            }
  });
  TUILogin.login("${您的userId}", "${您的userSig}", new V2TIMCallback() {
            @Override
            public void onError(int code, String msg) {
                Log.d(TAG, "code: " + code + " msg:" + msg);
            }

            @Override
            public void onSuccess() {
                Log.d(TAG, "onSuccess");
            }
  });

:::
</dx-codeblock>

[](id:model.step5)

### 步骤5：实现音视频通话

1. 发起方：调用 TUICallingManager 的 `call();` 方法发起通话的请求, 并传入用户 ID数组（userids）和通话类型（type），通话类型参数传入`TUICalling.Type.AUDIO`（音频通话）或者`TUICalling.Type.VIDEO`（视频通话）。如果用户 ID数组（userids）只有1个userId时视为单人通话，如果用户 ID数组（userids）有多个userId时（>=2）视为多人通话。
2. 接收方：当接收方处于已登录状态时，会自动启动相应的界面。如果希望接收方在不处于登录状态时也能收到通话请求，请参见 [离线接听](#model.offline)。


<dx-codeblock>
::: java java
// 1. 初始化组件
TUICallingManager manager = TUICallingManager.sharedInstance();
// 2. 注册监听器
manager.setCallingListener(new TUICalling.TUICallingListener() {
            @Override
            public boolean shouldShowOnCallView() {
                return true;
            }

            @Override
            public void onCallStart(String[] userIDs, TUICalling.Type type, TUICalling.Role role, final View tuiCallingView) {
                if (!shouldShowOnCallView() || null == tuiCallingView) {
                    return;
                }
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT);
                        mCallingView = tuiCallingView;
                        addContentView(tuiCallingView, params);
                    }
                });
            }

            @Override
            public void onCallEnd(String[] userIDs, TUICalling.Type type, TUICalling.Role role, long totalTime) {
                removeView();
            }

            @Override
            public void onCallEvent(TUICalling.Event event, TUICalling.Type type, TUICalling.Role role, String message) {
                if (TUICalling.Event.CALL_FAILED == event) {
                    removeView();
                }
            }
});
// 3.拨打电话
manager.call(userIDs, TUICalling.Type.VIDEO);
:::
</dx-codeblock>

[](id:model.offline)

### 步骤6：实现离线接听

>?如果您的业务定位是在线客服等不需要离线接听功能的场景，那么完成上述 [步骤1](#model.step1) - [步骤5](#model.step5) 的对接即可。但如果您的业务定位是社交场景，建议实现离线接听。

IM SDK 支持离线推送，但是 Android 端各个手机厂商均有各自的离线推送服务，因此接入复杂度要高于 iOS 平台，您需要进行相应的设置才能达到可用标准。

1. 申请对应厂商的推送渠道需要的证书等，并将其配置到即时通信 IM 控制台中，按照推送要求增加证书和 ID 等，详细的操作步骤请参见 [即时通信 IM > 离线推送（Android） ](https://cloud.tencent.com/document/product/269/44516)。
2. 目前在 TRTCCallingImpl 的 sendModel 信令发送函数中已经集成了离线发送的函数，当配置好 App 的离线推送后，消息就可实现离线推送。

[](id:api)

## 组件 API 列表

TUICalling 组件的 API 接口列表如下：

| 接口函数        | 接口功能                                                  |
| --------------- | --------------------------------------------------------- |
| call            | C2C 邀请通话         |
| receiveAPNSCalled          | 作为被邀请方接听来电                                      |
| setCallingListener          | 设置监听器                                     |
| setCallingBell          | 设置铃声(建议在30s以内)                                                 |
| enableMuteMode | 开启静音模式    |
| enableCustomViewRoute      | 开启自定义视图， 开启后，会在呼叫/被叫开始回调中，接收到 CallingView 的实例，由开发者自行决定展示方式。注意：必须全屏或者与屏幕等比例展示，否则会有展示异常            |

