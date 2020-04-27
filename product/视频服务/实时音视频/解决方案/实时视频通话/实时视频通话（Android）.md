## 效果展示

<table>
<tr>
   <th>主动呼叫</th>
   <th>呼叫接听</th>
 </tr>
<tr>
<td><img src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/videocall/group-call.gif"/></td>
<td><img src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/videocall/group-recv.gif"/></td>
</tr>
</table>

如需快速实现视频通话功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCVideoCall 组件并实现自定义 UI 界面。

<span id="ui"> </span>
## 复用 Demo 的 UI 界面
<span id="ui.step1"></span>
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如 `TestVideoCall` ，单击【创建应用】。

>! 本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。

<span id="ui.step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/Android)】跳转至 Github（或单击【[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Android_latest.zip)】），下载相关 SDK 及配套的 Demo 源码。
 ![](https://main.qcloudimg.com/raw/c3067ef0d7244bfdd3bc31eef191c5fc.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。

<span id="ui.step3"></span>
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#ui.step2) 中下载的源码包。
2. 找到并打开 `Android/TRTCDemo/debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java` 文件。
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
使用 Android Studio（3.5 以上的版本）打开源码工程 `TRTCDemo`，单击【运行】即可开始调试本 Demo。

<span id="ui.step5"></span>
### 步骤5：修改 Demo 源代码
源码文件夹 `trtcvideocalldemo` 中包含两个子文件夹 ui 和 model，其中 ui 文件夹中均为界面代码：

| 文件或文件夹 | 功能描述 |
|:-------:|:--------|
| TRTCVideoCallActivity.java | 展示视频通话的主界面，通话的接听和拒绝就是在这个界面中完成的。 | 
| SelectContactActivity.java| 用于展示选择联系人的界面。 |
| TRTCVideoCallHistoryActivity.java| 用于展示历史联系人的界面。 |
| videolayout | 用于完成视频影像画面的渲染和排布逻辑。 | 

<span id="model"> </span>
## 实现自定义 UI 界面

源码文件夹 `trtcvideocalldemo` 中包含两个子文件夹 ui 和 model，其中 model 文件夹中包含了我们实现的可重用开源组件 TRTCVideoCall，您可以在  `ITRTCVideoCall.java`  文件中看到该组件提供的接口函数。
![](https://main.qcloudimg.com/raw/1a75796f96e4d715372f68338d5651c9.jpg)

您可以使用开源组件 TRTCVideoCall 实现自己的 UI 界面，即只复用 model 部分，自行实现 UI 部分。

<span id="model.step1"> </span>
### 步骤1：集成 SDK
视频通话组件 TRTCVideoCall 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

**方法一：通过 Maven 仓库依赖**
1. 在 dependencies 中添加 TRTCSDK 和 IMSDK 的依赖。
```
dependencies {
	complie "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
    complie 'com.tencent.imsdk:imsdk:latest.release'

	// 由于我们使用到了 gson 解析，所以还需要依赖 google 的 Gson
    complie 'com.google.code.gson:gson:latest.release'
}
```
>?两个 SDK 产品的最新版本号，可以在 [实时音视频](https://github.com/tencentyun/TRTCSDK) 和 [即时通信 IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
    ndk {
        abiFilters "armeabi-v7a"
    }
}
```
3. 单击【Sync Now】同步 SDK。
 >?若您的网络连接 jcenter 没有问题，SDK 会自动下载集成到工程里。


**方法二：通过本地 AAR 依赖**
如果您的开发环境访问 maven 仓库较慢，可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。

| SDK | 下载页面 | 集成指引 |
|---------|---------|---------|
| TRTC SDK | [DOWNLOAD](https://cloud.tencent.com/document/product/647/32689) | [集成文档](https://cloud.tencent.com/document/product/647/32175) |
| IM SDK | [DOWNLOAD](https://cloud.tencent.com/document/product/269/36887) | [集成文档](https://cloud.tencent.com/document/product/269/32679) |

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
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```
-keep class com.tencent.** { *; }
```

<span id="model.step3"> </span>
### 步骤3：导入 TRTCVideoCall 组件

拷贝以下目录中的所有文件到您的项目中：
```
trtcvideocalldemo/src/main/java/com/tencent/liteav/trtcvideocalldemo/model 
```

![](https://main.qcloudimg.com/raw/82f9ccdb79eac798025905c18ddff142.gif)

<span id="model.step4"> </span>
### 步骤4：初始化并登录组件
1. 调用 `TRTCVideoCallImpl.sharedInstance(context)` 获取组件实例。
2. 调用 `init()` 初始化组件。
3. 调用 `login(SDKAppID, userId, userSig, callback)` 完成组件的登录，其中几个关键参数的填写请参考下表：
 <table>
<tr>
<th>参数名</th>
<th>作用</th>
</tr>
<tr>
<td>SDKAppID</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。</td>
</tr>
<tr>
<td>userId</td>
<td>当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）。</td>
</tr>
<tr>
<td>userSig</td>
<td>腾讯云设计的一种安全保护签名，计算方式请参考 <a href="https://cloud.tencent.com/document/product/647/17275">如何计算 UserSig</a>。</td>
</tr>
</table>
<pre>
// 初始化
sCall = TRTCVideoCallImpl.sharedInstance(context);
sCall.init();
sCall.login(1400000123, "userA", "xxxx", new ActionCallback());
</pre>


<span id="model.step5"> </span>
### 步骤5：实现 1v1 视频通话
1. 发起方：调用 `ITRTCVideoCall` 的 `call()` 方法并指定对方的 userid 发起视频通话的请求。
2. 接收方：当接收方处于已登录状态时，会收到名为 `onInvited()` 的事件通知。如果希望接收方在不处于登录状态时也能收到通话请求，请参考 [离线接听](#model.offline)。
3. 接收方：如果希望接听电话，接收方可以调用 `accept()`函数，并同时调用 `openCamera()` 函数打开自己本地的摄像头。接收方也可以调用 reject() 拒绝此次通话。
4. 当双方的音视频通道建立完成后，通话的双方都会接收到名为  `onUserVideoAvailable()` 的事件通知，表示对方的视频画面已经拿到。此时双方用户均可以调用`startRemoteView()` 展示远端的视频画面。远端的声音默认是自动播放的。

```
ITRTCVideoCall sCall = TRTCVideoCallImpl.sharedInstance(context);
//1. 初始化 TRTCVideoCall 组件
sCall.init();
//2. 注册监听器
sCall.addListener(new TRTCVideoCallListener() {
    //...省略一些监听代码
    public void onInvited(String sponsor, final List<String> userIdList, boolean isFromGroup, int callType) {
        // 收到来自 sponsor 发过来的通话请求，此处代码选择接听，您也可以调用 reject() 拒绝之。
        sCall.accept();
        // 接受通话请求之后，即可打开自己的摄像头
        TXCloudVideoView localView = new TXCloudVideoView(mContext);
        mParentView.add(localView);
        sCall.openCamera(true, localView);
    }
		
    public void onUserVideoAvailable(final String userId, boolean isVideoAvailable) {
        if (isVideoAvailable) {
            //表示对方的视频画面已经拿到，此时可以展示对方的视频影像
            TXCloudVideoView remoteView = new TXCloudVideoView(mContext);
            mParentView.add(remoteView);
            sCall.startRemoteView(userId, remoteView);
        } else {
            sCall.stopRemoteView(userId);
        }
    }
});

//3. 完成组件的登录，登录成功后才可以调用组件的其他功能函数
sCall.login(sdkappid, "aaa", usersig, new ActionCallback() {
    public void onSuccess() {
        //4. 此处为实例代码：我们在组件登录成功后即打开摄像头并呼叫用户“aaa”
        TXCloudVideoView localView = new TXCloudVideoView(mContext);
        mParentView.add(localView);
        sCall.openCamera(true, localView);
        sCall.call("aaa", ITRTCVideoCall.TYPE_VIDEO_CALL);
    }
});
}
```

<span id="model.step6"> </span>
### 步骤6：实现多人视频通话
1. 发起方：多人视频通话需要调用 `ITRTCVideoCall` 中的 `groupCall()` 函数，并传入用户列表（userIdList）和 IM 群组 ID（groupId），其中 userIdList 为必填参数，groupId 为选填参数。
2. 接收端：通过名为 `onInvited()` 事件通知能够接收到此呼叫请求。
3. 接收端：收到事件通知后可以调用 `accept()` 方法接听此次通话，也可以选择用 `reject()` 方法拒绝通话。
4. 如果超过一定时间（默认30s）没有回复，接收方会收到 `onCallingTimeOut()` 的事件通知，发起方会收到 `onNoResp(String userId)` 事件通知。通话发起方在多个接收均未应答时 `hangup()` ， 每个接收方均会收到 `onCallingCancel()` 事件通知。
5. 如果需要离开当前多人通话可以调用 `hangup()` 方法。
6. 如果通话中有用户中途加入或离开，那么其他用户均会接收到 `onUserEnter()` 或  `onUserLeave()` 事件通知。

>?接口 `groupCall()` 中的 `groupID` 参数是 IM SDK 中的群组 ID，如果填写该参数，那么通话请求消息是通过群消息系统广播出去的，这种消息广播方式比较简单可靠。如果不填写，那么 `TRTCVideoCall` 组件会采用单发消息逐一通知。

```
// 前面省略...
// 拼凑需要拨打的用户列表
List<String> callList = new ArrayList();
callList.add("bbb");
callList.add("ccc");
callList.add("ddd");
// 如果您不是在一个 IM 群里发起的, groupId 可以传一个空串；
sCall.groupCall(callList, ITRTCVideoCall.TYPE_VIDEO_CALL, "");
//打开自己的摄像头
TXCloudVideoView localView = new TXCloudVideoView(mContext);
mParentView.add(localView);
sCall.openCamera(true, txCloudVideoView);
```

<span id="model.offline"> </span>
### 步骤7：实现离线接听
>?如果您的业务定位是在线客服等不需要离线接听功能的场景，那么完成上述 [步骤1](#model.step1) - [步骤6](#model.step6) 的对接即可。但如果您的业务定位是社交场景，建议实现离线接听。

IM SDK 支持离线推送，但是 Android 端各个手机厂商均有各自的离线推送服务，因此接入复杂度要高于 iOS 平台，您需要进行相应的设置才能达到可用标准。
1. 申请对应厂商的推送渠道需要的证书等，并将其配置到即时通信 IM 控制台中，按照推送要求增加证书和 ID 等，详细的操作步骤请参见 [即时通信 IM > 离线推送（Android） ](https://cloud.tencent.com/document/product/269/9234)。
2. 修改配置 `TRTCVideoCallImpl`  的 `sendModel` 函数中被注释的部分。
 ![](https://main.qcloudimg.com/raw/371a95b662389f849345e77820a2296d.png)


<span id="api"> </span>
## 组件 API 列表
TRTCVideoCall 组件的 API 接口列表如下：

| 接口函数 | 接口功能 |
|---------|---------|
| init | 在使用所有功能之前，需要调用该函数进行必要的初始化 | 
| destroy | 销毁实例 |
| addListener | 增加 TRTCVideoCallListener 监听器，用户可以通过该监听器获取状态通知 |
| removeListener | 移除监听器 |
| login | 登录 IM，所有功能需要先进行登录后才能使用 |
| logout | 登出 IM，登出后无法再进行拨打操作 |
| call | C2C 邀请通话，被邀请方会收到 onInvited 的事件通知 |
| groupCall | IM 群组邀请通话，被邀请方会收到 onInvited 的事件通知 |
| accept | 作为被邀请方接听来电 |
| reject | 作为被邀请方拒绝来电 |
| hangup | 结束通话 |
| startRemoteView | 将远端用户的摄像头数据渲染到指定的 TXCloudVideoView 中 |
| stopRemoteView | 停止渲染某个远端用户的摄像头数据 |
| openCamera | 开启摄像头，并渲染在指定的 TXCloudVideoView 中 |
| closeCamera | 关闭摄像头 |
| switchCamera | 切换前后摄像头 |
| setMicMute | 是否静音 mic |
| setHandsFree | 是否开启免提 |
