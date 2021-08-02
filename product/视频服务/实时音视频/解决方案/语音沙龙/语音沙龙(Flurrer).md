## 效果展示
<table>
     <tr>
         <th>房主麦位操作</th>  
         <th>听众麦位操作</th>  
     </tr>
<tr>
<td><img src="https://tccweb-1258344699.cos.ap-nanjing.myqcloud.com/sdk/trtc/chatsalon/pjckq-4zdgj.gif"/></td>
<td><img src="https://tccweb-1258344699.cos.ap-nanjing.myqcloud.com/sdk/trtc/chatsalon/new.gif"/></td>
</tr>
</table>


如需快速接入语音沙龙功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCChatSalon 组件并实现自定义 UI 界面。

[](id:DemoUI)

## 复用 Demo 的 UI 界面

[](id:ui.step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如  `TestChatSalon`  ，单击【创建】。

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
### 步骤4：编译运行

>! 安卓需要在真机下运行，不支持模拟器调试。

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
[源码](https://github.com/tencentyun/TRTCFlutterScenesDemo) 中的 trtcchatsalondemo 文件夹包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述                             |
| ------------ | ------------------------------------ |
| base         | UI 使用的基础类。                    |
| list         | 列表页和创建房间页。                 |
| room         | 主房间页面，包括房主和听众两种界面。 |
| widget       | 通用控件。                           |

[](id:model)
## 实现自定义 UI 界面
[源码](https://github.com/tencentyun/TRTCFlutterScenesDemo) 中的 trtcchatsalondemo 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCChatSalon，您可以在 `TRTCChatSalon.dart` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/fcf694c8550664623414604d14ffcd94.png)

[](id:model.step1)
### 步骤1：集成 SDK
语音沙龙组件 trtcchatsalondemo 依赖 [TRTC SDK](https://pub.dev/packages/tencent_trtc_cloud) 和 [IM SDK](https://pub.dev/packages/tencent_im_sdk_plugin)，您可以通过配置 `pubspec.yaml` 自动下载更新。

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
需要在 `Info.plist` 中加入对麦克风的权限申请：
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
### 步骤3：导入 TRTCChatSalon 组件
拷贝以下目录中的所有文件到您的项目中：
```
lib/TRTCChatSalonDemo/model/
```

[](id:model.step4)
### 步骤4：创建并登录组件
1. 调用 `sharedInstance` 接口可以创建一个 TRTCChatSalon 组件的实例对象。
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
TRTCChatSalon trtcVoiceRoom = await TRTCChatSalon.sharedInstance();
trtcVoiceRoom.registerListener(onVoiceListener);
ActionCallback resValue = await trtcVoiceRoom.login(
    GenerateTestUserSig.sdkAppId,
    userId,
    GenerateTestUserSig.genTestSig(userId),
);
if (resValue.code == 0) {
    //登录成功
}
:::
</dx-codeblock>

[](id:model.step5)

### 步骤5：房主端开播

1. 房主执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 房主调用 `createRoom` 创建新的语音沙龙，此时传入房间 ID、房间名等房间属性信息。
3. 房主会收到有成员进入的 `TRTCChatSalonDelegate.onAudienceEnter` 的事件通知，此时会自动打开麦克风采集。

![](https://main.qcloudimg.com/raw/bfdc392413adacb05325b065bc691c82.png)

<dx-codeblock>
::: java java
// 1.房主设置昵称和头像
trtcVoiceRoom.setSelfProfile("my_name", "my_face_url", null);

// 2.房主调用 createRoom 创建房间
ActionCallback resp = await trtcVoiceRoom.createRoom(
    roomId,
    RoomParam(
    coverUrl: '房间封面图的 URL 地址',
    roomName: '房间名称',
    ),
);
if (resp.code == 0) {
   //3.占座成功
}

// 4.占座成功后， 收到 TRTCChatSalonDelegate.onAudienceEnter 事件通知
onVoiceListener(type, param) async {
    switch (type) {
        case TRTCChatSalonDelegate.onAudienceEnter:
            //听众进入房间
            break;
    }
}
:::
</dx-codeblock>

[](id:model.step6)

### 步骤6：听众端观看

1. 听众端执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 听众端向业务后台获取最新的语音沙龙房间列表。
 >?Demo 中的语音沙龙列表仅做演示使用，语音沙龙列表的业务逻辑千差万别，腾讯云暂不提供语音沙龙列表的管理服务，请自行管理您的语音沙龙列表。
3. 听众端调用 `getRoomList` 获取房间的详细信息，该信息是在房主端调用  `createRoom` 创建语音沙龙时设置的简单描述信息。
> !如果您的语音沙龙列表包含了足够全面的信息，可跳过调用 `getRoomList` 相关步骤。 并传入房间号即可进入该房间。
4. 进房后会收到组件的 `TRTCChatSalonDelegate.onAudienceEnter` 和 `TRTCChatSalonDelegate.onAudienceExit` 听众进退房通知，监听到事件回调后可以将变化然后刷新到 UI 界面上。
5. 进房后还会收到麦位表有主播进入的 `TRTCChatSalonDelegate.onAnchorEnterMic` 和 `TRTCChatSalonDelegate.onAnchorLeaveMic` 的事件通知。

![](https://main.qcloudimg.com/raw/24ba699e25f8a8cb2f892fbbf8d7fa00.png)
<dx-codeblock>
::: dart dart
// 1.听众设置昵称和头像
trtcVoiceRoom.setSelfProfile("my_name", "my_face_url");

// 2.假定您从业务后台获取房间列表为 roomList
List<Integer> roomList = GetRoomList();

// 3.通过调用 getRoomInfoList 获取房间的详细信息
RoomInfoCallback resp = await trtcVoiceRoom.getRoomInfoList(roomList);
if (resp.code == 0) {
    //此时可以刷新您自己的 UI 房间列表
} 

// 4.传入 roomId 进入房间
ActionCallback enterRoomResp =
          await trtcVoiceRoom.enterRoom(_currentRoomId);
if (enterRoomResp.code == 0) {
    //进房成功
}
// 5.进房成功后，收到处理事件通知
onVoiceListener(type, param) async {
    switch (type) {
      case TRTCChatSalonDelegate.onAudienceEnter:
            //听众进入房间
        break;
      case TRTCChatSalonDelegate.onAudienceExit:
            //听众离开房间
        break;
      case TRTCChatSalonDelegate.onAnchorLeaveMic:
          //房主离开房间
        break;
      case TRTCChatSalonDelegate.onAnchorEnterMic:
          //房主进入房间
        break;
    }
}
:::
</dx-codeblock>

[](id:model.step7)
### 步骤7：上下麦
<dx-tabs>
::: 房主端
1.  `leaveMic` 主动下麦,房间内所有成员会收到 `onAnchorLeaveMic` 的事件通知。
2.  `kickMic` 传入对应用户的userId后，可以踢人下麦。房主踢人下麦，房间内所有成员会收到 `onAnchorLeaveMic` 的事件通知。

![](https://main.qcloudimg.com/raw/6e23550a49c88b823dca96941c638394.png)
<dx-codeblock>
::: dart dart
// 1.主动下麦
trtcVoiceRoom.leaveMic();

//2.踢人下麦
trtcVoiceRoom.kickMic(userId);
:::
</dx-codeblock>
:::
::: 听众端
1.  `enterMic` 可以进行上麦，房间内所有成员会收到 `onAnchorEnterMic` 的事件通知。
2.  `leaveMic` 主动下麦，房间内所有成员会收到 `onAnchorLeaveMic` 的事件通知。

![](https://main.qcloudimg.com/raw/d6a618277eb66ba629e9172844c57a60.png)
<dx-codeblock>
::: dart dart
// 1.听众主动上麦
trtcVoiceRoom.enterMic();

// 2.主动下麦
trtcVoiceRoom.leaveMic();

:::
</dx-codeblock>
:::
</dx-tabs>


[](id:model.step8)

### 步骤8：举手要求上麦信令的使用

如果您的 App 需要对方同意才能进行下一步操作的业务流程，那么邀请信令可以提供相应支持。

#### 听众主动申请上麦

1. 听众端调用 `raiseHand` 申请举手。
2. 房主端收到 `onRaiseHand` 的事件，此时 UI 可以弹窗并询问房主是否同意。
3. 房主选择同意后，调用 `agreeToSpeak` 并传入 userId。
4. 听众端收到 `onAgreeToSpeak` 的事件通知，调用 `enterMic` 进行上麦。

![](https://main.qcloudimg.com/raw/1553acebea8b5a35b1b8e82365bdec3c.png)
<dx-codeblock>
::: dart dart
// 听众端视角
// 1.调用 sendInvitation，请求上麦
trtcVoiceRoom.raiseHand();

// 2.收到邀请的同意请求, 正式上麦
onVoiceListener(type, param) async {
    switch (type) {
      case TRTCChatSalonDelegate.onRaiseHand:
           trtcVoiceRoom.enterMic();
        break;
    }
}

// 房主端视角
// 1.房主收到请求
onVoiceListener(type, param) async {
    switch (type) {
      case TRTCChatSalonDelegate.onAgreeToSpeak:
           trtcVoiceRoom.agreeToSpeak();
        break;
    }
}
:::
</dx-codeblock>

[](id:model.step9)

### 步骤9：实现文字聊天和弹幕消息
通过 `sendRoomTextMsg` 可以发送普通的文本消息，所有在该房间内的主播和听众均可以收到 `onRecvRoomTextMsg` 回调。
  即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
  <dx-codeblock>
  ::: dart dart
  // 发送端：发送文本消息
  trtcVoiceRoom.sendRoomTextMsg("Hello Word!");

// 接收端：监听文本消息
onVoiceListener(type, param) async {
    switch (type) {
      case TRTCChatSalonDelegate.onRecvRoomTextMsg:
            //收到群文本消息，可以用作文本聊天室
        break;
    }
}
:::
</dx-codeblock>
