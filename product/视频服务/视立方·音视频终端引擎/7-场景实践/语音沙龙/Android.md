## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 效果展示

您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 App 体验语音沙龙的能力，包括语音聊天、上下麦、低延时语音互动等音视频通话 TRTC 在语音聊天场景下的相关能力。

<table>
     <tr>
         <th>房主麦位操作</th>  
         <th>听众麦位操作</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/chatsalon_anchor.gif"/ style="max-height:700px;"></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/chatsalon_audicence.gif"/  style="max-height:700px;"></td>
</tr>
</table>


如需快速接入语音沙龙功能，您可以直接基于我们提供的 App 进行修改适配，也可以使用我们提供的 TRTCChatSalon 组件并实现自定义 UI 界面。

[](id:DemoUI)
## 复用 App 的 UI 界面

[](id:ui.step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如  `TestChatSalon`  ，单击【创建】。
3. 单击【已下载，下一步】，跳过此步骤。

![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)
>!本功能同时使用了腾讯云视立方音视频通话 TRTC 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。



[](id:ui.step2)
### 步骤2：下载 App 源码
单击进入 [TUIChatSalon](https://github.com/tencentyun/TUIChatSalon)，Clone 或者下载源码。

[](id:ui.step3)

### 步骤3：配置 App 工程文件

1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Android/Debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java` 文件。
3. 设置 `GenerateTestUserSig.java` 文件中的相关参数：
<ul style="margin:0"><li/>SDKAPPID：默认为占位符（PLACEHOLDER），请设置为实际的 SDKAppID。
<li/>SECRETKEY：默认为占位符（PLACEHOLDER），请设置为实际的密钥信息。</ul>
<img src="https://main.qcloudimg.com/raw/09a7c2e06bb792e1c3d651a61aff4000.png">
4. 粘贴完成后，单击【已复制粘贴，下一步】即创建成功。
5. 编译完成后，单击【回到控制台概览】即可。


>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 App 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:ui.step4)
### 步骤4：运行 App
使用 Android Studio（3.5以上的版本）打开源码工程 `TUIChatSalon`，单击【运行】即可开始调试本 App。

[](id:ui.step5)
### 步骤5：修改 App 源代码
源码中的 Source 文件夹包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述                             |
| ------------ | ------------------------------------ |
| base         | UI 使用的基础类。                    |
| list         | 创建房间页。                 |
| room         | 主房间页面，包括房主和听众两种界面。 |
| widget       | 通用控件。                           |


## 体验应用
>! 体验应用至少需要两台设备。

### 用户 A

1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
<img src="https://main.qcloudimg.com/raw/a0c73f6904ac152a84cdf4d619171fc4.png" width="320"/>
2. 进入后，单击【创建房间】，如下图示：
<img src="https://main.qcloudimg.com/raw/1a56b06671c6958a83b748450c93d6a6.png" width="320"/>
3. 输入房间主题，单击【开始交谈】。

### 用户 B
1. 输入用户名（**请确保用户名唯一性，不能与其他用户重复**）并登录，如图示：
<img src="https://main.qcloudimg.com/raw/94fcd741becbcfe4cca97778e180e4ca.png" width="320"/>
2. 输入用户 A 创建的房间号，单击【进入房间】。<br>
<img src="https://main.qcloudimg.com/raw/ae041395a8488725f405819491646f99.png" width="320"/>

>! 房间号在用户 A 的房间顶部查看，如下图示：
<img src="https://main.qcloudimg.com/raw/4a3e66a9a01f446fd4d2fe0b39b16a2c.png" width="320"/>


[](id:model)
## 实现自定义 UI 界面
[源码](https://github.com/tencentyun/TUIChatSalon/tree/main/Android/Source/src/main/java/com/tencent/liteav/trtcchatsalon) 中的 Source 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCChatSalon，您可以在 `TRTCChatSalon.java` 文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/fcf694c8550664623414604d14ffcd94.png)

[](id:model.step1)
### 步骤1：集成 SDK

语音沙龙组件 Source 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

[](id:model.step1_m1)
#### 方法一：通过 Maven 仓库依赖
1. 在 dependencies 中添加 TRTCSDK 和 IMSDK 的依赖。
<dx-codeblock>
::: java java
dependencies {
       complie "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
       complie 'com.tencent.imsdk:imsdk:latest.release'
       compile 'com.google.code.gson:gson:2.3.1'
}
:::
</dx-codeblock>
>?两个 SDK 的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 GitHub 首页获取。
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
3. 单击【Sync Now】，自动下载 SDK 并集成到工程里。



[](id:model.step1_m2)
#### 方法二：通过本地 AAR 依赖
若您的开发环境访问 Maven 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。

<table>
<tr><th>SDK</th><th>下载页面</th><th>集成指引</th>
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


[](id:model.step2)
### 步骤2：配置权限及混淆规则

在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态读取存储权限）：
```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
```

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：

<dx-codeblock>
::: java java
-keep class com.tencent.** { *; }
:::
</dx-codeblock>

[](id:model.step3)
### 步骤3：导入 TRTCChatSalon 组件
拷贝以下目录中的所有文件到您的项目中：
<dx-codeblock>
::: java java
Source/src/main/java/com/tencent/liteav/trtcchatsalon/model
:::
</dx-codeblock>

[](id:model.step4)
### 步骤4：创建并登录组件
1. 调用 `sharedInstance` 接口可以创建一个 TRTCChatSalon 组件的实例对象。
2. 调用 `setDelegate` 函数注册组件的事件通知。
3. 调用 `login` 函数完成组件的登录，请参考下表填写关键参数：
 <table>
<tr><th>参数名</th><th>作用</th></tr>
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
<dx-codeblock>
::: java java
TRTCChatSalon mTRTCChatSalon = TRTCChatSalon.sharedInstance(this);
mTRTCChatSalon.setDelegate(this);
mTRTCChatSalon.login(SDKAPPID, userId, userSig, new TRTCChatSalonCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            //登录成功
        }
    }
});
:::
</dx-codeblock>

[](id:model.step5)
### 步骤5：房主端开播

1. 房主执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 房主调用 `createRoom` 创建新的语音沙龙，此时传入房间 ID、上麦是否需要房主确认、房间类型等房间属性信息。
3. 房主会收到有成员进入的 `onAnchorEnterSeat` 的事件通知，此时会自动打开麦克风采集。

![](https://main.qcloudimg.com/raw/bfdc392413adacb05325b065bc691c82.png)
<dx-codeblock>
::: java java
// 1.房主设置昵称和头像
mTRTCChatSalon.setSelfProfile("my_name", "my_face_url", null);

// 2.房主调用 createRoom 创建房间
final TRTCChatSalonDef.RoomParam roomParam = new TRTCChatSalonDef.RoomParam();
roomParam.roomName = "房间名称";
roomParam.needRequest = true; // 上麦是否需要房主确认
roomParam.coverUrl = "房间封面图的 URL 地址";
mTRTCChatSalon.createRoom(mRoomId, roomParam, new TRTCChatSalonCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            // 3.占座位
            mTRTCChatSalon.enterSeat(new TRTCChatSalonCallback.ActionCallback() {
                @Override
                public void onCallback(int code, String msg) {
                    if (code == 0) {
                    }
                }
            });
        }
    }
});

// 4.占座成功后， 收到 onAnchorEnterSeat 事件通知
@Override
public void onAnchorEnterSeat(TRTCChatSalonDef.UserInfo userInfo) {
}
:::
</dx-codeblock>

[](id:model.step6)

### 步骤6：听众端观看

1. 听众端执行 [步骤4](#model.step4) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 听众端向业务后台获取最新的语音沙龙房间列表。
>?App 中的语音沙龙列表仅做演示使用，语音沙龙列表的业务逻辑千差万别，腾讯云暂不提供语音沙龙列表的管理服务，请自行管理您的语音沙龙列表。
3. 听众端调用 `getRoomInfoList` 获取房间的详细信息，该信息是在房主端调用 `createRoom` 创建语音沙龙时设置的简单描述信息。
>!如果您的语音沙龙列表包含了足够全面的信息，可跳过调用 `getRoomInfoList` 相关步骤。
4. 听众选择一个语音沙龙，调用 `enterRoom` 并传入房间号即可进入该房间。
5. 进房后会收到组件的 `onRoomInfoChange` 房间属性变化事件通知，此时可以记录房间属性并做相应改变，例如 UI 展示房间名、记录上麦是否需要请求房主同意等。
6. 进房后还会收到麦位表有主播进入的 `onAnchorEnterSeat` 的事件通知。

![](https://main.qcloudimg.com/raw/24ba699e25f8a8cb2f892fbbf8d7fa00.png)

<dx-codeblock>
::: java java
// 1.听众设置昵称和头像
mTRTCChatSalon.setSelfProfile("my_name", "my_face_url", null);

// 2.假定您从业务后台获取房间列表为 roomList
List<Integer> roomList = GetRoomList();

// 3.通过调用 getRoomInfoList 获取房间的详细信息
mTRTCChatSalon.getRoomInfoList(roomList, new TRTCChatSalonCallback.RoomInfoCallback() {

    @Override
    public void onCallback(int code, String msg, List<TRTCChatSalonDef.RoomInfo> list) {
        if (code == 0) {
            // 此时可以刷新您自己的 UI 房间列表
        }
    }

});

// 4.传入 roomId 进入房间
mTRTCChatSalon.enterRoom(roomId, new TRTCChatSalonCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
                //进房成功
            }
        }
});

// 5.进房成功后，收到 onRoomInfoChange 事件通知
@Override
public void onRoomInfoChange(TRTCChatSalonDef.RoomInfo roomInfo) {
    mNeedRequest = roomInfo.needRequest;
    mRoomName = roomInfo.roomName;
    // UI 可以展示标题等
}

// 6.收到 onAnchorEnterSeat 事件通知
@Override
public void onAnchorEnterSeat(TRTCChatSalonDef.UserInfo userInfo) {
}
:::
</dx-codeblock>

[](id:model.step7)
### 步骤7：上下麦

<dx-tabs>
::: 房主端
1. `pickSeat` 传入听众 userId, 可以抱人上麦，房间内所有成员会收到 `onAnchorEnterSeat` 的事件通知。
2. `kickSeat` 传入对应用户的 userId 后，可以踢人下麦，房间内所有成员会收到 `onAnchorLeaveSeat` 的事件通知。

![](https://main.qcloudimg.com/raw/6e23550a49c88b823dca96941c638394.png)
麦位操作后的事件通知顺序如下：callback > onAnchorEnterSeat 等独立事件。
<dx-codeblock>
::: java java
// 1.房主抱人上麦位
mTRTCChatSalon.pickSeat("123", new TRTCChatSalonCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        // 2.收到 callback 回调
        if (code == 0) {
        }
    }
});

// 3.听众成为主播，进入麦位通知，可以在这里判断听众是不是真的上麦成功
public void onAnchorEnterSeat(TRTCChatSalonDef.UserInfo user) {
}
:::
</dx-codeblock>
:::
::: 听众端
1. `enterSeat` 可以进行上麦，房间内所有成员会收到 `onAnchorEnterSeat` 的事件通知。
2. `leaveSeat` 主动下麦，房间内所有成员会收到 `onAnchorLeaveSeat` 的事件通知。

![](https://main.qcloudimg.com/raw/d6a618277eb66ba629e9172844c57a60.png)
麦位操作后的事件通知顺序如下：callback  > onAnchorEnterSeat 等独立事件。
<dx-codeblock>
::: java java
// 1.听众主动上麦
mTRTCChatSalon.enterSeat(new TRTCChatSalonCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        // 2.收到 callback 回调
        if (code == 0) {
        }
    }
});

// 3.听众成为主播，进入麦位通知，可以在这里判断是不是自己并进行相应处理
public void onAnchorEnterSeat(int index, TRTCChatSalonDef.UserInfo user) {
}
:::
</dx-codeblock>
:::
</dx-tabs>


[](id:model.step8)
### 步骤8：邀请信令的使用
如果您的 App 需要对方同意才能进行下一步操作的业务流程，那么邀请信令可以提供相应支持。

<dx-tabs>
::: 听众主动申请上麦
1. 听众端调用 `sendInvitation` 传入房主的 userId 和业务的自定义命令字等，此时函数会返回一个 inviteId，记录该 inviteId。
2. 房主端收到 `onReceiveNewInvitation` 的事件通知，此时 UI 可以弹窗并询问房主是否同意。
3. 房主选择同意后，调用 `acceptInvitation` 并传入 inviteId。
4. 听众端收到 `onInviteeAccepted` 的事件通知，调用 `enterSeat` 进行上麦。

![](https://main.qcloudimg.com/raw/1553acebea8b5a35b1b8e82365bdec3c.png)

<dx-codeblock>
::: java java
// 听众端视角
// 1.调用 sendInvitation，请求上麦
String inviteId = mTRTCChatSalon.sendInvitation("ENTER_SEAT", ownerUserId, "123", null);

// 2.收到邀请的同意请求, 正式上麦
@Override
public void onInviteeAccepted(String id, String invitee) {
    if(id.equals(inviteId)) {
        mTRTCChatSalon.enterSeat(null);
    }
}

// 房主端视角
// 1.房主收到请求
 @Override
public void onReceiveNewInvitation(final String id, String inviter, String cmd, final String content) {
    if (cmd.equals("ENTER_SEAT")) {
        // 2.房主同意听众请求
         mTRTCChatSalon.acceptInvitation(id, null);
    }
}
:::
</dx-codeblock>
:::
::: 房主邀请听众上麦
1. 房主端调用 `sendInvitation` 传入听众的 userId 和业务的自定义命令字等，此时函数会返回一个 inviteId，记录该 inviteId。
2. 听众端收到 `onReceiveNewInvitation` 的事件通知，此时 UI 可以弹窗并询问听众是否同意上麦。
3. 听众选择同意后，调用 `acceptInvitation` 并传入 inviteId。
4. 房主端收到 `onInviteeAccepted` 的事件通知，调用`pickSeat`抱听众上麦。

![](https://main.qcloudimg.com/raw/7b920cb763f049c4d90a84c72ab4c87e.png)

<dx-codeblock>
::: java java
// 房主端视角
// 1.房主调用 sendInvitation，请求抱听众“123”上麦
String inviteId = mTRTCChatSalon.sendInvitation("PICK_SEAT", ownerUserId, "123", null);

// 2.收到邀请的同意请求, 正式上麦
@Override
public void onInviteeAccepted(String id, String invitee) {
    if(id.equals(inviteId)) {
        mTRTCChatSalon.pickSeat(null);
    }
}

// 听众端视角
// 1.听众收到请求
 @Override
public void onReceiveNewInvitation(final String id, String inviter, String cmd, final String content) {
    if (cmd.equals("PICK_SEAT")) {
        // 2.听众同意房主请求
         mTRTCChatSalon.acceptInvitation(id, null);
    }
}
:::
</dx-codeblock>
:::
</dx-tabs>


[](id:model.step9)
### 步骤9：实现文字聊天和弹幕消息
- 通过 `sendRoomTextMsg` 可以发送普通的文本消息，所有在该房间内的主播和听众均可以收到 `onRecvRoomTextMsg` 回调。
  即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
  <dx-codeblock>
  ::: java java
  // 发送端：发送文本消息
  mTRTCChatSalon.sendRoomTextMsg("Hello Word!", null);
  // 接收端：监听文本消息
  mTRTCChatSalon.setDelegate(new TRTCChatSalonDelegate() {
   @Override
   public void onRecvRoomTextMsg(String message, TRTCChatSalonDef.UserInfo userInfo) {
       Log.d(TAG, "收到来自" + userInfo.userName + "的消息:" + message);
   }
  });
  :::
  </dx-codeblock>
- 通过 `sendRoomCustomMsg` 可以发送自定义（信令）的消息，所有在该房间内的主播和听众均可以收到 `onRecvRoomCustomMsg` 回调。
  自定义消息常用于传输自定义信令，例如用于点赞消息的发送和广播。
  <dx-codeblock>
  ::: java java
  // 发送端：您可以通过自定义 Cmd 来区分弹幕和点赞消息
  // eg:"CMD_DANMU"表示弹幕消息，"CMD_LIKE"表示点赞消息
  mTRTCChatSalon.sendRoomCustomMsg("CMD_DANMU", "Hello world", null);
  mTRTCChatSalon.sendRoomCustomMsg("CMD_LIKE", "", null);
  // 接收端：监听自定义消息
  mTRTCChatSalon.setDelegate(new TRTCChatSalonDelegate() {
    @Override
    public void onRecvRoomCustomMsg(String cmd, String message, TRTCChatSalonDef.UserInfo userInfo) {
        if ("CMD_DANMU".equals(cmd)) {
            // 收到弹幕消息
            Log.d(TAG, "收到来自" + userInfo.userName + "的弹幕消息:" + message);
        } else if ("CMD_LIKE".equals(cmd)) {
            // 收到点赞消息
            Log.d(TAG, userInfo.userName + "给您点了个赞！");
        }
    }
  });
  :::
  </dx-codeblock>
