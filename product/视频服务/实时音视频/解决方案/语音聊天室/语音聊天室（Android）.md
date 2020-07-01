## 效果展示
您可以 [下载](https://cloud.tencent.com/document/product/647/17021) 安装我们的 Demo 体验语音聊天室的能力，包括麦位管理、低延时语音互动、文字聊天等 TRTC 在语音聊天场景下的相关能力。
<table>
     <tr>
         <th>主播麦位操作</th>  
         <th>观众麦位操作</th>  
     </tr>
<tr>
<td><img src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/gif/voiceroom_pick_seat.gif"/></td>
<td><img src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/gif/voiceroom_enter_seat.gif"/></td>
</tr>
</table>

如需快速接入语音聊天室功能，您可以直接基于我们提供的 Demo 进行修改适配，也可以使用我们提供的 TRTCVoiceRoom 组件并实现自定义 UI 界面。

<span id="DemoUI"> </span>
## 复用 Demo 的 UI 界面

<span id="ui.step1"></span>
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如 `TestVoiceRoom` ，单击【创建应用】。

>?本功能需同时使用 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PAAS 服务，开通实时音视频后会同步开通即时通信 IM 服务。

<span id="ui.step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/Android)】跳转至 Github（或单击【[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Android_latest.zip)】），下载相关 SDK 及配套的 Demo 源码。
 ![](https://main.qcloudimg.com/raw/c3067ef0d7244bfdd3bc31eef191c5fc.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。

<span id="ui.step3"></span>
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#ui.step2) 中下载的源码包。
2. 找到并打开`Android/TRTCScenesDemo/debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java`文件。
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
使用 Android Studio（3.5以上的版本）打开源码工程`TRTCScenesDemo`，单击【运行】即可开始调试本 Demo。

<span id="ui.step5"></span>
### 步骤5：修改 Demo 源代码
源码中的 trtcvoiceroomdemo 文件夹包含两个子文件夹 ui 和 model，ui 文件夹中均为界面代码，如下表格列出了各个文件或文件夹及其所对应的 UI 界面，以便于您进行二次调整：

| 文件或文件夹 | 功能描述 |
|-------|--------|
| base | UI 使用的基础类。 |
| list | 列表页和创建房间页。 |
| room | 主房间页面，包括主播和观众两种界面。 |
| widget | 通用控件。 |

<span id="model"> </span>
## 实现自定义 UI 界面

[源码](https://github.com/tencentyun/TRTCSDK/tree/master/Android/TRTCScenesDemo/trtcvoiceroomdemo/src/main/java/com/tencent/liteav/trtcvoiceroom) 中的 trtcvoiceroomdemo 文件夹包含两个子文件夹 ui 和 model，model 文件夹中包含可重用的开源组件 TRTCVoiceRoom，您可以在`TRTCVoiceRoom.java`文件中看到该组件提供的接口函数，并使用对应接口实现自定义 UI 界面。
![](https://main.qcloudimg.com/raw/0ebcbb27843bf03a790a945a8c92d560.png)

<span id="model.step1"> </span>
### 步骤1：集成 SDK
语音聊天组件 TRTCVoiceRoom 依赖 TRTC SDK 和 IM SDK，您可以按照如下步骤将两个 SDK 集成到项目中。

**方法一：通过 Maven 仓库依赖**
1. 在 dependencies 中添加 TRTCSDK 和 IMSDK 的依赖。
```
dependencies {
       complie "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
       complie 'com.tencent.imsdk:imsdk:latest.release'
       compile 'com.google.code.gson:gson:2.3.1'
}
```
>?两个 SDK 的最新版本号，可以在 [TRTC](https://github.com/tencentyun/TRTCSDK) 和 [IM](https://github.com/tencentyun/TIMSDK) 的 Github 首页获取。
>
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
      ndk {
          abiFilters "armeabi-v7a"
      }
}
```
3. 单击【Sync Now】，自动下载 SDK 并集成到工程里。

**方法二：通过本地 AAR 依赖**
若您的开发环境访问 maven 仓库较慢，您可以直接下载 ZIP 包，并按照集成文档手动集成到您的工程中。
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
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
```

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```
-keep class com.tencent.** { *; }
```

<span id="model.step3"> </span>
### 步骤3：导入 TRTCVoiceRoom 组件
拷贝以下目录中的所有文件到您的项目中：
```
trtcvoiceroomdemo/src/main/java/com/tencent/liteav/trtcvoiceroom/model
```

<span id="model.step4"> </span>
### 步骤4：创建并登录组件
1. 调用`sharedInstance`接口可以创建一个 TRTCVoiceRoom 组件的实例对象。
2. 调用`setDelegate`函数注册组件的事件通知。
3. 调用`login`函数完成组件的登录，请参考下表填写关键参数：
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
<td>callback</td>
<td>登录回调，成功时 code 为0。</td>
</tr>
</table>

<pre>
TRTCVoiceRoom mTRTCVoiceRoom = TRTCVoiceRoom.sharedInstance(this);
mTRTCVoiceRoom.setDelegate(this);
mTRTCVoiceRoom.login(SDKAPPID, userId, userSig, new TRTCVoiceRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            //登录成功
        }
    }
});
</pre>

<span id="model.step5"> </span>
### 步骤5：主播端开播
1. 主播执行 [步骤4](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 主播调用`createRoom`创建新的语音聊天室，此时传入房间 ID、上麦是否需要房主确认、麦位数等房间属性信息。
3. 主播创建房间成功后，调用`enterSeat`进入座位。
4. 主播收到组件的`onSeatListChange`麦位表变化事件通知，此时可以将麦位表变化刷新到 UI 界面上。
5. 主播还会收到麦位表有成员进入的`onAnchorEnterSeat`的事件通知，此时会自动打开麦克风采集。

![](https://main.qcloudimg.com/raw/628f0aa3f0c15e53fec6ac904c8d3943.png)

```java
// 1.主播设置昵称和头像
mTRTCVoiceRoom.setSelfProfile("my_name", "my_face_url", null);

// 2.主播调用 createRoom 创建房间
final TRTCVoiceRoomDef.RoomParam roomParam = new TRTCVoiceRoomDef.RoomParam();
roomParam.roomName = "房间名称";
roomParam.needRequest = false; // 上麦是否需要房主确认
roomParam.seatCount = 7; // 房间座位数，这里一共7个座位，房主占了一个后观众剩下6个座位
roomParam.coverUrl = "房间封面图的 URL 地址";
mTRTCVoiceRoom.createRoom(mRoomId, roomParam, new TRTCVoiceRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            //3. 占0号座位
            mTRTCVoiceRoom.enterSeat(0, new TRTCVoiceRoomCallback.ActionCallback() {
                @Override
                public void onCallback(int code, String msg) {
                    if (code == 0) {
                    }
                }
            });
        }
    }
});

// 4.占座成功后，收到 onSeatListChange 事件通知
@Override
public void onSeatListChange(final List<TRTCVoiceRoomDef.SeatInfo> seatInfoList) {
    // 展示您的麦位列表
}

// 5. 收到 onAnchorEnterSeat 事件通知
@Override
public void onAnchorEnterSeat(TRTCVoiceRoomDef.UserInfo userInfo) {
}
```

<span id="model.step6"> </span>
### 步骤6：观众端观看
1. 观众端执行 [步骤4](#model.step4) 登录后，可以调用`setSelfProfile`设置自己的昵称和头像。
2. 观众端向业务后台获取最新的语音聊天室房间列表。
 >?Demo 中的语音聊天室列表仅做演示使用，语音聊天室列表的业务逻辑千差万别，腾讯云暂不提供语音聊天室列表的管理服务，请自行管理您的语音聊天室列表。
 >
3. 观众端调用`getRoomInfoList`获取房间的详细信息，该信息是在主播端调用`createRoom`创建语音聊天室时设置的简单描述信息。
 >!如果您的语音聊天室列表包含了足够全面的信息，可跳过调用`getRoomInfoList`相关步骤。
4. 观众选择一个语音聊天室，调用`enterRoom`并传入房间号即可进入该房间。
5. 进房后会收到组件的`onRoomInfoChange`房间属性变化事件通知，此时可以记录房间属性并做相应改变，例如 UI 展示房间名、记录上麦是否需要请求主播同意等。
6. 进房后会收到组件的`onSeatListChange`麦位表变化事件通知，此时可以将麦位表变化刷新到 UI 界面上。
7. 进房后还会收到麦位表有主播进入的`onAnchorEnterSeat`的事件通知。

![](https://main.qcloudimg.com/raw/6e36bc8029a8abbeed69b43e197ba3c0.png)

```java
// 1.观众设置昵称和头像
mTRTCVoiceRoom.setSelfProfile("my_name", "my_face_url", null);

// 2.假定您从业务后台获取房间列表为 roomList
List<Integer> roomList = GetRoomList();

// 3.通过调用 getRoomInfoList 获取房间的详细信息
mTRTCVoiceRoom.getRoomInfoList(roomList, new TRTCVoiceRoomCallback.RoomInfoCallback() {
    @Override
    public void onCallback(int code, String msg, List<TRTCVoiceRoomDef.RoomInfo> list) {
        if (code == 0) {
            // 此时可以刷新您自己的 UI 房间列表
        }
    }
});

// 4.选择语音聊天室后，传入 roomid 进入房间
mTRTCVoiceRoom.enterRoom(roomId, new TRTCVoiceRoomCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
                //进房成功
            }
        }
});

// 5.进房成功后，收到 onRoomInfoChange 事件通知
@Override
public void onRoomInfoChange(TRTCVoiceRoomDef.RoomInfo roomInfo) {
    mNeedRequest = roomInfo.needRequest;
    mRoomName = roomInfo.roomName;
    // UI 可以展示标题等
}

// 6.进房成功后，收到 onSeatListChange 事件通知
@Override
public void onSeatListChange(final List<TRTCVoiceRoomDef.SeatInfo> seatInfoList) {
    // 展示您的麦位列表
}

// 7. 收到 onAnchorEnterSeat 事件通知
@Override
public void onAnchorEnterSeat(TRTCVoiceRoomDef.UserInfo userInfo) {
}
```

<span id="model.step7"> </span>
### 步骤7：麦位管理
主播端：
1. `pickSeat`传入对应的麦位和观众 userId, 可以抱人上麦，房间内所有成员会收到`onSeatListChange`和`onAnchorEnterSeat`的事件通知。
2. `kickSeat`传入对应麦位后，可以踢人下麦，房间内所有成员会收到`onSeatListChange`和`onAnchorLeaveSeat`的事件通知。
3. `muteSeat`传入对应麦位后，可以静音/解除静音，房间内所有成员会收到 `onSeatListChange` 和 `onSeatMute` 的事件通知。
4. `closeSeat`传入对应麦位后，可以封禁/解禁某个麦位，封禁后观众端将不能再上麦，房间内所有成员会收到`onSeatListChange`和`onSeatClose`的事件通知。

![](https://main.qcloudimg.com/raw/299e62ae7d20d10622197ad8685d4639.png)

观众端：
1. `enterSeat`传入对应的麦位后，可以进行上麦，房间内所有成员会收到`onSeatListChange`和`onAnchorEnterSeat`的事件通知。
2. `leaveSeat`主动下麦，房间内所有成员会收到`onSeatListChange`和`onAnchorLeaveSeat`的事件通知。

![](https://main.qcloudimg.com/raw/3ac11818d7d23f61104600ea7235867d.png)

麦位操作后的事件通知顺序如下：
callback > onSeatListChange > onAnchorEnterSeat 等独立事件

```java
// case1: 主播抱人上1号麦位
mTRTCVoiceRoom.pickSeat(1, "123", new TRTCVoiceRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        // 2.收到 callback 回调
        if (code == 0) {
        }
    }
});

// 3.收到 onSeatListChange 回调，刷新您的麦位列表
@Override
public void onSeatListChange(final List<TRTCVoiceRoomDef.SeatInfo> seatInfoList) {
}

// 4.单个麦位变化的通知，可以在这里判断观众是不是真的上麦成功
public void onAnchorEnterSeat(int index, TRTCVoiceRoomDef.UserInfo user) {
}
```

```java
// case2: 观众主动上2号麦位
mTRTCVoiceRoom.enterSeat(2, new TRTCVoiceRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        // 2.收到 callback 回调
        if (code == 0) {
        }
    }
});

// 3.收到 onSeatListChange 回调，刷新您的麦位列表
@Override
public void onSeatListChange(final List<TRTCVoiceRoomDef.SeatInfo> seatInfoList) {
}

// 4.单个麦位变化的通知，可以在这里判断是不是自己并进行相应处理
public void onAnchorEnterSeat(int index, TRTCVoiceRoomDef.UserInfo user) {
}
```

<span id="model.step8"> </span>
### 步骤8：邀请信令的使用
在 [麦位管理](#model.step7) 中，观众上下麦、主播抱人上麦都不需要经过对方的同意就可以直接操作。
如果您的 App 需要对方同意才能进行下一步操作的业务流程，那么邀请信令可以提供相应支持。
如果您的观众上麦需要申请：
1. 观众端调用`sendInvitation`传入主播的 userId 和业务的自定义命令字等，此时函数会返回一个 inviteId，记录该 inviteId。
2. 主播端收到`onReceiveNewInvitation`的事件通知，此时 UI 可以弹窗并询问主播是否同意。
3. 主播选择同意后，调用`acceptInvitation`并传入 inviteId。
4. 观众端收到`onInviteeAccepted`的事件通知，调用`enterSeat`进行上麦。

![](https://main.qcloudimg.com/raw/e2b97c645590c835b54fffbf0ff4ebfd.png)

```java
// 观众端视角
// 1.调用 sendInvitation，请求上1号麦位
String inviteId = mTRTCVoiceRoom.sendInvitation("ENTER_SEAT", ownerUserId, "1", null);

// 4.收到邀请的同意请求, 正式上麦
@Override
public void onInviteeAccepted(String id, String invitee) {
    if(id.equals(inviteId)) {
        mTRTCVoiceRoom.enterSeat(1, null);
    }
}

// 主播端视角
// 2.主播收到请求
 @Override
public void onReceiveNewInvitation(final String id, String inviter, String cmd, final String content) {
    if (cmd.equals("ENTER_SEAT")) {
        // 3.主播同意观众请求
         mTRTCVoiceRoom.acceptInvitation(id, null);
    }
}
```

如果您的主播需要发送邀请才能抱观众上麦：
1. 主播端调用`sendInvitation`传入观众的 userId 和业务的自定义命令字等，此时函数会返回一个 inviteId，记录该 inviteId。
2. 观众端收到`onReceiveNewInvitation`的事件通知，此时 UI 可以弹窗并询问观众是否同意上麦。
3. 观众选择同意后，调用`acceptInvitation`并传入 inviteId。
4. 主播端收到`onInviteeAccepted`的事件通知，调用`pickSeat`抱观众上麦。

![](https://main.qcloudimg.com/raw/e68e2dd9a8056ad8496cbe3dcfe634f1.png)

```java
// 主播端视角
// 1.主播调用 sendInvitation，请求抱观众123上2号麦
String inviteId = mTRTCVoiceRoom.sendInvitation("PICK_SEAT", "123", "2", null);

// 4.收到邀请的同意请求, 正式上麦
@Override
public void onInviteeAccepted(String id, String invitee) {
    if(id.equals(inviteId)) {
        mTRTCVoiceRoom.pickSeat(2, null);
    }
}

// 观众端视角
// 2.观众收到请求
 @Override
public void onReceiveNewInvitation(final String id, String inviter, String cmd, final String content) {
    if (cmd.equals("PICK_SEAT")) {
        // 3.观众同意主播请求
         mTRTCVoiceRoom.acceptInvitation(id, null);
    }
}
```

<span id="model.step9"> </span>
### 步骤9：实现文字聊天和弹幕消息
- 通过`sendRoomTextMsg`可以发送普通的文本消息，所有在该房间内的主播和观众均可以收到`onRecvRoomTextMsg`回调。
 即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
```java
// 发送端：发送文本消息
mTRTCVoiceRoom.sendRoomTextMsg("Hello Word!", null);
// 接收端：监听文本消息
mTRTCVoiceRoom.setDelegate(new TRTCVoiceRoomDelegate() {
    @Override
    public void onRecvRoomTextMsg(String message, TRTCVoiceRoomDef.UserInfo userInfo) {
        Log.d(TAG, "收到来自" + userInfo.userName + "的消息:" + message);
    }
});
```
- 通过`sendRoomCustomMsg`可以发送自定义（信令）的消息，所有在该房间内的主播和观众均可以收到`onRecvRoomCustomMsg`回调。
自定义消息常用于传输自定义信令，例如用于点赞消息的发送和广播。
```java
// 发送端：您可以通过自定义 Cmd 来区分弹幕和点赞消息
// eg:"CMD_DANMU"表示弹幕消息，"CMD_LIKE"表示点赞消息
mTRTCVoiceRoom.sendRoomCustomMsg("CMD_DANMU", "Hello world", null);
mTRTCVoiceRoom.sendRoomCustomMsg("CMD_LIKE", "", null);
// 接收端：监听自定义消息
mTRTCVoiceRoom.setDelegate(new TRTCVoiceRoomDelegate() {
    @Override
    public void onRecvRoomCustomMsg(String cmd, String message, TRTCVoiceRoomDef.UserInfo userInfo) {
        if ("CMD_DANMU".equals(cmd)) {
            // 收到弹幕消息
            Log.d(TAG, "收到来自" + userInfo.userName + "的弹幕消息:" + message);
        } else if ("CMD_LIKE".equals(cmd)) {
            // 收到点赞消息
            Log.d(TAG, userInfo.userName + "给您点了个赞！");
        }
    }
});
```
