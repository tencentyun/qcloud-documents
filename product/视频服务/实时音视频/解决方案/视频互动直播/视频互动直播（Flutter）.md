如需快速接入视频互动直播功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCLiveRoom 组件并实现自定义 UI 界面。

[](id:DemoUI)

## 复用 Demo 的 UI 界面

[](id:ui.step1)

### 步骤1：创建新的应用

1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如  `TestLive`  ，单击【创建】。

>! 本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。



[](id:ui.step2)
### 步骤2：下载 SDK 和 Demo 源码

1. 根据实际业务需求下载 SDK 及配套的 Demo 源码。
2. 下载完成后，单击【已下载，下一步】。
![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

[](id:ui.step3)
### 步骤3：配置 Demo 工程文件

1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `/example/lib/debug/GenerateTestUserSig.dart` 文件。
3. 设置 `GenerateTestUserSig.dart` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为PLACEHOLDER，请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为PLACEHOLDER，请设置为实际的密钥信息。</ul>
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

源码中的 TRTCLiveRoom 文件夹包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述                             |
| ------------ | ------------------------------------ |
| base         | UI 使用的基础类。                    |
| list         | 列表页和创建房间页。                 |
| room         | 主房间页面，包括主播和观众两种界面。 |

[](id:model)

## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TRTCFlutterScenesDemo) 中的 TRTCLiveRoom 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCLiveRoom，您可以在 `TRTCLiveRoom.dart` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。

[](id:model.step1)

### 步骤1：集成 SDK

互动直播组件 TRTCLiveRoom 依赖 [TRTC SDK](https://pub.dev/packages/tencent_trtc_cloud) 和 [IM SDK](https://pub.dev/packages/tencent_im_sdk_plugin)，您可以通过配置 `pubspec.yaml` 自动下载更新。

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

### 步骤3：导入 TRTCLiveRoom 组件

拷贝以下目录中的所有文件到您的项目中：

```
lib/TRTCLiveRoom/model/
```

[](id:model.step4)

### 步骤4：创建并登录组件

1. 调用 `sharedInstance` 接口可以创建一个 TRTCLiveRoom 组件的实例对象。
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
<tr>
<td>useCDNFirst</td>
<td>用于设置观众观看方式。true 表示普通观众通过 CDN 观看，计费便宜但延时较高。false 表示普通观众通过低延时观看，计费价格介于 CDN 和连麦之间，但延迟可控制在1s以内。</td>
</tr>
<tr>
<td>CDNPlayDomain</td>
<td>在 useCDNFirst 设置为 true 时才会生效，用于指定 CDN 观看的播放域名，您可以登录直播控制台 >【<a href="https://console.cloud.tencent.com/live/domainmanage">域名管理</a>】页面中进行设置。</td>
</tr>
</table>

[](id:model.step5)
### 步骤5：主播端开播

1. 主播执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 主播在开播前可先调用 `startCameraPreview` 开启摄像头预览，界面上可以配置美颜调节按钮调用，通过 `getBeautyManager` 进行美颜设置。
>?非企业版 SDK 不支持变脸和贴图挂件功能。
3. 主播调整美颜效果后，可以调用 `createRoom` 创建新的直播间。
4. 主播调用 `startPublish` 开始推流。如需支持 CDN 观看，请在 login 时传入的 `TRTCLiveRoomConfig` 参数中指定 `useCDNFirst` 和 `CDNPlayDomain` 并在 `startPublish` 时指定直播拉流用的 streamID。

![](https://main.qcloudimg.com/raw/754450346c831a792a0cc7a06b2c7d31.png)

[](id:model.step6)
### 步骤6：观众端观看

1. 观众端执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 观众端向业务后台获取最新的直播房间列表。
>?Demo 中的直播间列表仅做演示使用，直播间列表的业务逻辑千差万别，腾讯云暂不提供直播间列表的管理服务，请自行管理您的直播间列表。
3. 观众端调用 `getRoomInfos` 获取房间的详细信息，该信息是在主播端调用 `createRoom` 创建直播间时设置的简单描述信息。
 >!如果您的直播间列表包含了足够全面的信息，可跳过调用 `getRoomInfos` 相关步骤。
4. 观众选择一个直播间，调用 `enterRoom` 并传入房间号即可进入该房间。
5. 调用 `startPlay` 并传入主播的 userId 开始播放。
 - 若直播间列表已包含主播端的 userId 信息，观众端可直接调用 `startPlay` 并传入主播的 userId 即可开始播放。
 - 若在进房前暂未获取主播的 userId，观众端在进房后会收到主播 `onAnchorEnter` 的事件回调，该回调中携带主播的 userId 信息，调用 `startPlay` 即可播放。 

![](https://main.qcloudimg.com/raw/70320746e332252cddbb842e280c95a5.png)

[](id:model.step7)
### 步骤7：观众与主播连麦上下麦

1. 观众端调用 `requestJoinAnchor` 向主播端发起连麦请求。
2. 主播端会收到 `TRTCLiveRoomDelegate#onRequestJoinAnchor`（即有观众请求与您连麦）的事件通知。
3. 主播端可以通过调用`responseJoinAnchor` 决定是否接受来自观众端的连麦请求。
4. 观众端会收到`onAnchorAccepted`事件通知，该通知会携带来自主播端的处理结果。
5. 如果主播同意连麦请求，观众端可调用 `startCameraPreview` 开启本地摄像头，随后调用 `startPublish` 启动观众端的推流。
6. 主播端会在观众端启动通知后收到 `TRTCLiveRoomDelegate#onAnchorEnter` （即另一路音视频流已到来）通知，该通知会携带观众端的 userId。
7. 主播端调用 `startPlay` 即可看到连麦观众的画面。

![](https://main.qcloudimg.com/raw/743009e16a89eb6ff8d708b4564d8a91.png)


[](id:model.step8)

### 步骤8：主播与主播 PK

1. 主播 A 调用 `requestRoomPK` 向主播 B 发起 PK 请求。
2. 主播 B 会收到 `TRTCLiveRoomDelegate onRequestRoomPK` 回调通知。
3. 主播 B 调用 `responseRoomPK` 决定是否接受主播 A 的 PK 请求。
4. 主播 B 接受主播 A 的要求，等待 `TRTCLiveRoomDelegate onAnchorEnter` 通知，调用 `startPlay` 显示主播 A。
5. 主播 A 收到 `onRoomPKAccepted`回调通知，PK 请求是否被同意。
6. 主播 A 请求被同意，等待 `TRTCLiveRoomDelegate onAnchorEnter` 通知，调用 `startPlay` 显示主播 B。

![](https://main.qcloudimg.com/raw/8e3868af20a2cd4f968b673da107e227.png)

[](id:model.step9)
### 步骤9：实现文字聊天和弹幕消息
- 通过 `sendRoomTextMsg` 可以发送普通的文本消息，所有在该房间内的主播和观众均可以收到 `onRecvRoomTextMsg` 回调。
  即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
<dx-codeblock>
::: dart dart
// 发送端：发送文本消息
trtcLiveCloud.sendRoomTextMsg("Hello Word!");
   
// 接收端：监听文本消息
onListenerFunc(type, params) async {
  switch (type) {
    case TRTCLiveRoomDelegate.onRecvRoomTextMsg:
          //收到群文本消息，可以用作文本聊天室
      break;
  }
}
:::
</dx-codeblock>
- 通过 `sendRoomCustomMsg` 可以发送自定义（信令）的消息，所有在该房间内的主播和观众均可以收到 `onRecvRoomCustomMsg` 回调。
  自定义消息常用于传输自定义信令，例如用于点赞消息的发送和广播。
