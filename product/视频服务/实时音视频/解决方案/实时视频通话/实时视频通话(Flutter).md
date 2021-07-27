如需快速实现视频通话功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCCalling 组件并实现自定义 UI 界面。

## 复用 Demo 的 UI 界面

### 步骤1：创建新的应用

1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如 `TestVideoCall` ，单击【创建】。

>!本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。


[](id:ui.step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 [Demo 源码](https://github.com/tencentyun/TRTCFlutterScenesDemo)。
2. 下载完成后，单击【已下载，下一步】。
![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

[](id:ui.step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `/example/lib/debug/GenerateTestUserSig.dart` 文件。
3. 设置 `GenerateTestUserSig.dart` 文件中的相关参数：
<ul><li/>SDKAPPID：默认为 PLACEHOLDER ，请设置为实际的 SDKAppID。
	<li/>SECRETKEY：默认为 PLACEHOLDER ，请设置为实际的密钥信息。</ul>
	<img src="https://main.qcloudimg.com/raw/fba60aa9a44a94455fe31b809433cfa4.png"/>
4. 粘贴完成后，单击【已复制粘贴，下一步】即创建成功。
5. 编译完成后，单击【回到控制台概览】即可。
>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui.step4)

### 步骤4：运行 Demo

>! Android 端需要在真机下运行，不支持模拟器调试。

1. 执行 `flutter pub get`。
2. 编译运行调试：
<dx-tabs>
:::  Android\s端
1. 执行 `flutter run`。
2. 使用 Android Studio（3.5及以上的版本）打开源码工程，单击【运行】即可。
:::
::: iOS\s端
1. 使用 XCode（11.0及以上的版本）打开源码目录下的 `/ios工程`。
2. 编译并运行 Demo 工程即可。
:::
</dx-tabs>

[](id:ui.step5)
### 步骤5：修改 Demo 源代码
[源码](https://github.com/tencentyun/TRTCFlutterScenesDemo) 文件夹 `TRTCCallingDemo` 中包含两个子文件夹 ui 和 model，其中 ui 文件夹中均为界面代码：

| 文件或文件夹            | 功能描述                                                     |
| ----------------------- | ------------------------------------------------------------ |
| TRTCCallingVideo.dart   | 展示音视频通话的主界面，通话的接听和拒绝就是在这个界面中完成的 |
| TRTCCallingContact.dart | 用于展示选择联系人的界面，可以通过此界面搜索已注册用户，发起通话 |

[](id:model)
## 实现自定义 UI 界面
[源码](https://github.com/tencentyun/TRTCFlutterScenesDemo) 文件夹 `TRTCCallingDemo` 中包含两个子文件夹 ui 和 model，其中 model 文件夹中包含了我们实现的可重用开源组件 TRTCCalling，您可以在  `TRTCCalling.dart`  文件中看到该组件提供的接口函数。
![](https://main.qcloudimg.com/raw/36220937e8689dac4499ce9f2f187889.png)

您可以使用开源组件 TRTCCalling 实现自己的 UI 界面，即只复用 model 部分，自行实现 UI 部分。

[](id:model.step1)
### 步骤1：集成 SDK
音视频通话组件 TRTCCalling 依赖 [TRTC SDK](https://pub.dev/packages/tencent_trtc_cloud) 和 [IM SDK](https://pub.dev/packages/tencent_im_sdk_plugin)，您可以通过配置 `pubspec.yaml` 自动下载更新。

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
需要在 `Info.plist` 中加入对相机和麦克风的权限申请：
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
### 步骤3：导入 TRTCCalling 组件
拷贝以下目录中的所有文件到您的项目中：
```
/lib/TRTCCallingDemo/model
```

[](id:model.step4)
### 步骤4：初始化并登录组件
1. 调用 `TRTCCalling.sharedInstance()` 获取组件实例。
2. 调用 `login(SDKAppID, userId, userSig)` 完成组件的登录，其中几个关键参数的填写请参考下表：
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
</tr></table>
<dx-codeblock>
::: java 
// 初始化
sCall = await TRTCCalling.sharedInstance();
sCall.login(1400000123, "userA", "xxxx");
:::
</dx-codeblock>

[](id:model.step5)
### 步骤5：实现 1v1 视频通话
1. 发起方：调用 `TRTCCalling` 的 `call()` 方法发起通话的请求, 并传入用户 ID（userid）和通话类型（type），通话类型参数传入`TRTCCalling.typeVideoCall`。
2. 接收方：当接收方处于已登录状态时，会收到名为 `onInvited()` 的事件通知，回调中 `callType` 的参数是发起方填写的通话类型，您可以通过此参数启动相应的界面。
3. 接收方：如果希望接听电话，接收方可以调用 `accept()` 函数，并同时调用 `openCamera()` 函数打开自己本地的摄像头。接收方也可以调用 `reject()` 拒绝此次通话。
4. 当双方的音视频通道建立完成后，通话的双方都会接收到名为  `onUserVideoAvailable()` 的事件通知，表示对方的视频画面已经拿到。此时双方用户均可以调用`startRemoteView()` 展示远端的视频画面。远端的声音默认是自动播放的。


[](id:api)
## 组件 API 列表
TRTCCalling 组件的 API 接口列表如下：

| 接口函数           | 接口功能                                                  |
| ------------------ | --------------------------------------------------------- |
| registerListener   | 增加 TRTCCalling 监听器，用户可以通过该监听器获取状态通知 |
| unRegisterListener | 移除监听器                                                |
| destroy            | 销毁实例                                                  |
| login              | 登录 IM，所有功能需要先进行登录后才能使用                 |
| logout             | 登出 IM，登出后无法再进行拨打操作                         |
| call               | C2C 邀请通话，被邀请方会收到 onInvited 的事件通知         |
| accept             | 作为被邀请方接听来电                                      |
| reject             | 作为被邀请方拒绝来电                                      |
| hangup             | 结束通话                                                  |
| startRemoteView    | 将远端用户的摄像头数据渲染到指定的 TXCloudVideoView 中    |
| stopRemoteView     | 停止渲染某个远端用户的摄像头数据                          |
| openCamera         | 开启摄像头，并渲染在指定的 TXCloudVideoView 中            |
| closeCamera        | 关闭摄像头                                                |
| switchCamera       | 切换前后摄像头                                            |
| setMicMute         | 是否静音 mic                                              |
| setHandsFree       | 是否开启免提                                              |

