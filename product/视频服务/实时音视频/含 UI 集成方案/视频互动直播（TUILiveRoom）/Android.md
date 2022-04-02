## 组件介绍

`TUILiveRoom` 是一个开源的视频直播 `UI` 组件，通过在项目中集成 `TUILiveRoom` 组件，您只需要编写几行代码就可以为您的 `App` 添加“视频互动直播”等场景。`TUILiveRoom`包含 `Android`、`iOS`、小程序等平台的源代码，基本功能如下图所示：
<table>
<tr>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/beauty.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/join.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/msg.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/pk.gif"/></td>
</tr>
</table>

[](id:model)
## 组件集成
[](id:model.step1)
### 步骤一：下载并导入 TUILiveRoom 组件
单击进入 [Github](https://github.com/tencentyun/TUILiveRoom) ，选择克隆/下载代码，然后拷贝 `Android/Beauty` ，`Android/Debug` 和 `Android/Source` 目录到您的工程中，并完成如下导入动作：

- 在 `setting.gradle` 中完成导入，参考如下：
```
include ':Beauty'
include ':Source'
include ':Debug'
```
- 在 `app` 的 `build.gradle` 文件中添加对 `Source` 的依赖：
```
api project(":Source")
```

[](id:model.step2)
### 步骤二：配置权限及混淆规则
在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请相机、读取存储权限）：
<dx-codeblock>
::: java java
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
:::
</dx-codeblock>

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
<dx-codeblock>
::: java java
-keep class com.tencent.** { *; }
:::
</dx-codeblock>

[](id:model.step3)
### 步骤三：初始化并登录组件
<dx-codeblock>
::: java java
TRTCLiveRoom mLiveRoom = TRTCLiveRoom.sharedInstance(this);
//useCDNFirst：true 表示普通观众通过 CDN 观看，false 表示普通观众通过低延时观看
//yourCDNPlayDomain：表示 CDN 观看时配置的播放域名
TRTCLiveRoomDef.TRTCLiveRoomConfig config = 
    new TRTCLiveRoomDef.TRTCLiveRoomConfig(useCDNFirst, yourCDNPlayDomain);
mLiveRoom.login(SDKAPPID, userId, userSig, config, 
    new TRTCLiveRoomCallback.ActionCallback() {
            @Override
            public void onCallback(int code, String msg) {
                if (code == 0) {
                    //登录成功
                }
            }
});
:::
</dx-codeblock>

**参数说明：**
- **SDKAppID**：**TRTC 应用 ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cf6de5f10b77be75174d0ba359101f60.png)
- **Secretkey**：**TRTC 应用密钥**和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。建议结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的userSig，也可以参照我们的 [示例工程](https://github.com/tencentyun/TUIRoom/blob/main/Android/Debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java#L88) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。
- **config**：全局配置信息，请在登录时初始化，登录之后不可变更。
- **useCDNFirst** ：用于设置观众观看方式。true 表示普通观众通过 CDN 观看，计费便宜但延时较高。false 表示普通观众通过低延时观看，计费价格介于 CDN 和连麦之间，但延迟可控制在1s以内。
- **CDNPlayDomain**：在 useCDNFirst 设置为 true 时才会生效，用于指定 CDN 观看的播放域名，您可以登录**直播控制台** > [域名管理](https://console.cloud.tencent.com/live/domainmanage) 页面中进行设置。
- **callback**：登录回调，成功时 code 为0。



[](id:model.step4)
### 步骤四：主播端开播
1. 主播执行 [步骤三](#model.step3) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 主播在开播前可先调用 `startCameraPreview` 开启摄像头预览，界面上可以配置美颜调节按钮调用，通过 `getBeautyManager` 进行美颜设置。
>?非企业版 SDK 不支持变脸和贴图挂件等高级美颜功能。
3. 主播调整美颜效果后，可以调用 [createRoom](https://cloud.tencent.com/document/product/647/43391#createroom) 创建新的直播间。
4. 主播调用 `startPublish` 开始推流。如需支持 CDN 观看，请在 login 时传入的 `TRTCLiveRoomConfig` 参数中指定 `useCDNFirst` 和 `CDNPlayDomain` 并在 `startPublish` 时指定直播拉流用的 streamID。

![](https://main.qcloudimg.com/raw/754450346c831a792a0cc7a06b2c7d31.png)
<dx-codeblock>
::: java java
// 1.主播设置昵称和头像
mLiveRoom.setSelfProfile("A", "your_face_url", null);

// 2.主播开播前预览并设置美颜参数
TXCloudVideoView view = new TXCloudVideoView(context);
parentView.add(view);
mLiveRoom.startCameraPreview(true, view, null);
mLiveRoom.getBeautyManager().setBeautyStyle(1);
mLiveRoom.getBeautyManager().setBeautyLevel(6);

// 3.主播创建房间
TRTCLiveRoomDef.TRTCCreateRoomParam param = new TRTCLiveRoomDef.TRTCCreateRoomParam();
param.roomName = "测试房间";
mLiveRoom.createRoom(123456789, param, new TRTCLiveRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            // 4.主播开启推流并将流发布到 CDN
            mLiveRoom.startPublish(mSelfUserId + "_stream", null);
        }
    }
});
:::
</dx-codeblock>

[](id:model.step5)
### 步骤五：观众端观看
1. 观众端执行 [步骤三](#model.step3) 登录后，可以调用 `setSelfProfile` 设置自己的昵称和头像。
2. 观众端向业务后台获取最新的直播房间列表。
>?App 中的直播间列表仅做演示使用，直播间列表的业务逻辑千差万别，腾讯云暂不提供直播间列表的管理服务，请自行管理您的直播间列表。
3. 观众端调用 `getRoomInfos` 获取房间的详细信息，该信息是在主播端调用 `createRoom` 创建直播间时设置的简单描述信息。
>!如果您的直播间列表包含了足够全面的信息，可跳过调用`getRoomInfos`相关步骤。
4. 观众选择一个直播间，调用 [enterRoom](https://cloud.tencent.com/document/product/647/43391#enterroom) 并传入房间号即可进入该房间。
5. 调用 `startPlay` 并传入主播的 userId 开始播放。
 - 若直播间列表已包含主播端的 userId 信息，观众端可直接调用 `startPlay` 并传入主播的 userId 即可开始播放。
 - 若在进房前暂未获取主播的 userId，观众端在进房后会收到主播 `onAnchorEnter` 的事件回调，该回调中携带主播的 userId 信息，调用 `startPlay` 即可播放。 

![](https://main.qcloudimg.com/raw/70320746e332252cddbb842e280c95a5.png)

```java
// 1.假定您从业务后台获取房间列表为 roomList
List<Integer> roomList = GetRoomList();

// 2.通过调用 getRoomInfos 获取房间的详细信息
mLiveRoom.getRoomInfos(roomList, new TRTCLiveRoomCallback.RoomInfoCallback() {
    @Override
    public void onCallback(int code, String msg, List<TRTCLiveRoomDef.TRTCLiveRoomInfo> list) {
        if (code == 0) {
            // 获取到房间详细信息后，您可以在主播列表页面展示主播昵称、头像等相关信息
        }
    }
})

// 3.选择房间 roomid 进入
mLiveRoom.enterRoom(roomid, null);

// 4.观众收到主播进房通知，开始播放
mLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onAnchorEnter(final String userId) {  
        // 5.观众播放主播画面
        mLiveRoom.startPlay(userId, mTXCloudVideoView, null);
    }
});
```

[](id:model.step6)
### 步骤六：观众与主播连麦
1. 观众端调用 [requestJoinAnchor](https://cloud.tencent.com/document/product/647/43391#requestjoinanchor) 向主播端发起连麦请求。
2. 主播端会收到 TRTCLiveRoomDelegate#onRequestJoinAnchor（即有观众请求与您连麦）的事件通知。
3. 主播端可以通过调用 responseJoinAnchor 决定是否接受来自观众端的连麦请求。
4. 观众端会收到 `TRTCLiveRoomDelegate#responseCallback` 事件通知，该通知会携带来自主播端的处理结果。
5. 如果主播同意连麦请求，观众端可调用 `startCameraPreview` 开启本地摄像头，随后调用 startPublish 启动观众端的推流。
6. 主播端会在观众端启动通知后收到 `TRTCLiveRoomDelegate#onAnchorEnter` （即另一路音视频流已到来）通知，该通知会携带观众端的 userId。
7. 主播端调用 startPlay 即可看到连麦观众的画面。

![](https://main.qcloudimg.com/raw/743009e16a89eb6ff8d708b4564d8a91.png)

<dx-codeblock>
::: java java
// 1.观众端发起连麦请求
mLiveRoom.requestJoinAnchor(mSelfUserId + "请求和您连麦", 
    new TRTCLiveRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            // 4.主播接受了观众的请求
            TXCloudVideoView view = new TXCloudVideoView(context);
            parentView.add(view);
            // 5.观众启动预览，开启推流
            mLiveRoom.startCameraPreview(true, view, null);
            mLiveRoom.startPublish(mSelfUserId + "_stream", null);
        }
    }
});

// 2.主播端收到连麦请求
mLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onRequestJoinAnchor(final TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, 
        String reason, final int timeout) {
        // 3.同意对方的连麦请求
        mLiveRoom.responseJoinAnchor(userInfo.userId, true, "同意连麦");
    }

    @Override
    public void onAnchorEnter(final String userId) {
        // 6.主播收到连麦观众的上麦通知
        TXCloudVideoView view = new TXCloudVideoView(context);
        parentView.add(view);
        // 7.主播播放观众画面
        mLiveRoom.startPlay(userId, view, null);
    }
});
:::
</dx-codeblock>

[](id:model.step7)
### 步骤七：实现文字聊天
- 通过 [sendRoomTextMsg](https://cloud.tencent.com/document/product/647/43391#sendroomtextmsg) 可以发送普通的文本消息，所有在该房间内的主播和观众均可以收到 `onRecvRoomTextMsg` 回调。
 即时通信 IM 后台有默认的敏感词过滤规则，被判定为敏感词的文本消息不会被云端转发。
  <dx-codeblock>
  ::: java java
  // 发送端：发送文本消息
  mLiveRoom.sendRoomTextMsg("Hello Word!", null);
  // 接收端：监听文本消息
  mLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onRecvRoomTextMsg(String roomId, 
        String message, TRTCLiveRoomDef.TRTCLiveUserInfo userInfo) {
        Log.d(TAG, "收到来自" + userInfo.userName + "的消息:" + message);
    }
  });
  :::
  </dx-codeblock>

[](id:model.step8)
### 步骤八：实现弹幕消息
- 通过 [sendRoomCustomMsg](https://cloud.tencent.com/document/product/647/43391#sendroomcustommsg) 可以发送自定义（信令）的消息，所有在该房间内的主播和观众均可以收到 `onRecvRoomCustomMsg` 回调。
自定义消息常用于传输自定义信令，例如用于点赞消息的发送和广播。
<dx-codeblock>
::: java java// 发送端：您可以通过自定义 Cmd 来区分弹幕和点赞消息
// eg:"CMD_DANMU"表示弹幕消息，"CMD_LIKE"表示点赞消息
mLiveRoom.sendRoomCustomMsg("CMD_DANMU", "Hello world", null);
mLiveRoom.sendRoomCustomMsg("CMD_LIKE", "", null);
// 接收端：监听自定义消息
mLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onRecvRoomCustomMsg(String roomId, String cmd, 
        String message, TRTCLiveRoomDef.TRTCLiveUserInfo userInfo) {
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

[](id:model.step9)
### 步骤九：主播与主播 PK
1. 房间状态监听&PK 列表接入（不需要 PK 列表请跳过此步骤）
房间状态可使用 `LiveRoomManager` 进行监听，如下：
<dx-codeblock>
::: java java
LiveRoomManager.getInstance().addCallback(new LiveRoomManager.RoomCallback() {
    /**
     * 房间创建
     * @param roomId
     * @param callback  用于通知内部处理的结果
     */
    @Override
    public void onRoomCreate(int roomId, final LiveRoomManager.ActionCallback callback) {
        // doSomething
    }

    /**
     * 房间销毁
     * @param roomId
     * @param callback  用于通知内部处理的结果
     */
    @Override
    public void onRoomDestroy(int roomId, final LiveRoomManager.ActionCallback callback) {
        // doSomething
    }

    /**
     * 获取房间列表
     * @param callback
     */
    @Override
    public void onGetRoomIdList(final LiveRoomManager.GetCallback callback) {
        // 获取房间列表，需自行维护，用于用户之间的 PK
        if(callback != null) {
            if(success) {
                // 回调成功，传入房间列表
                callback.onSuccess(roomList);
            } else {
                // 房间列表获取失败
                callback.onError(code, message);
            }
        }
    }
});
:::
</dx-codeblock>
采用 Callback 方式进行回调是为了方便用户接入，例如获取房间列表可能需要进行异步操作，采用 Callback 方式将更加灵活。
2. 主播 A 调用 [requestRoomPK](https://cloud.tencent.com/document/product/647/43391#requestroompk) 向主播 B 发起 PK 请求。
3. 主播 B 会收到 `TRTCLiveRoomDelegate onRequestRoomPK`回调通知。
4. 主播 B 调用 `responseRoomPK` 决定是否接受主播 A 的 PK 请求。
5. 主播 B 接受主播 A 的要求，等待 `TRTCLiveRoomDelegate onAnchorEnter`通知，调用 `startPlay` 显示主播 A。
6. 主播 A 收到 `responseCallback` 回调通知，PK 请求是否被同意。
7. 主播 A 请求被同意，等待 `TRTCLiveRoomDelegate onAnchorEnter` 通知，调用 `startPlay` 显示主播 B。

![](https://main.qcloudimg.com/raw/8e3868af20a2cd4f968b673da107e227.png)

<dx-codeblock>
::: java java
// 主播 A:
// 主播 A 创建12345的房间
mLiveRoom.createRoom(12345, param, null);

mLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onAnchorEnter(final String userId) {
        // 6.收到 B 进房的通知
        mLiveRoom.startPlay(userId, mTXCloudVideoView, null);
    }
});

// 1.主播 A 向主播 B 发起 PK 请求
mLiveRoom.requestRoomPK(54321, "B", 
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

// 主播 B：
// 主播 B 创建54321的房间
mLiveRoom.createRoom(54321, param, null);

// 2.主播 B 收到主播 A 的消息
mLiveRoom.setDelegate(new TRTCLiveRoomDelegate() {
    @Override
    public void onRequestRoomPK(
       final TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, final int timeout) {
        // 3.主播 B 回复主播 A 接受请求
        mLiveRoom.responseRoomPK(userInfo.userId, true, "");
    }
    @Override
    public void onAnchorEnter(final String userId) {
        // 4.主播 B 收到主播 A 进房的通知，播放主播 A 的画面
        mLiveRoom.startPlay(userId, mTXCloudVideoView, null);
    }
});
:::
</dx-codeblock>

## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。

