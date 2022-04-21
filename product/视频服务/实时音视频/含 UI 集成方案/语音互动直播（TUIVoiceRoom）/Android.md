## 组件介绍

TUIVoiceRoom 是一个开源的音视频 UI 组件，通过在项目中集成 TUIVoiceRoom 组件，您只需要编写几行代码就可以为您的 App 添加“多人语音聊天”等场景，TUIVoiceRoom 同时支持 [iOS](https://cloud.tencent.com/document/product/647/45753)、[小程序](https://cloud.tencent.com/document/product/647/65386) 等平台，基本功能如下图所示：

<table class="tablestyle">
<tbody><tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/797f59f998491b6ba9cc00164c076b18.jpg" width="250"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/0e4a8e5fb6d42f1c2f721195023f58bd.jpg" width="250"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/5b95135f19fbcba7acc030621107b13a.jpg" width="250"></td>
</tr>
</tbody></table>

## 组件集成

### 步骤一：下载并导入 TUIVoiceRoom 组件
单击进入 [Github](https://github.com/tencentyun/TUIVoiceRoom) ，选择克隆/下载代码，然后拷贝 Android/Source 目录到您的工程中，并完成如下导入动作：
- 在 `setting.gradle` 中完成导入，参考如下：
```
include ':Source'
```
- 在 app 的 build.gradle 文件中添加对 Source 的依赖：
```
api project(':Source')
```
- 在根目录的`build.gradle`文件中添加`TRTC SDK`和`IM SDK`的依赖：
```
ext {
    liteavSdk = "com.tencent.liteav:LiteAVSDK_TRTC:latest.release"
    imSdk = "com.tencent.imsdk:imsdk-plus:latest.release"
}
```

### 步骤二：配置权限及混淆规则
在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请麦克风权限等）：

```
<uses-permission android:name="android.permission.INTERNET" />              
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：

```
-keep class com.tencent.** { *; }
```

### 步骤三：初始化并登录
```java
    // 1.初始化，
    TRTCVoiceRoom mTRTCVoiceRoom = TRTCVoiceRoom.sharedInstance(this);
    mTRTCVoiceRoom.setDelegate(new TRTCVoiceRoomDelegate() {
    );
		  // 2.登录，
    mTRTCVoiceRoom.login(SDKAppID, userId, userSig, new TRTCVoiceRoomCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
            //登录成功
            }
        }
    });
```

**参数说明：**
- **SDKAppID**：**TRTC 应用 ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cf6de5f10b77be75174d0ba359101f60.png)
- **Secretkey**：**TRTC 应用密钥**和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。建议结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的userSig，也可以参照我们的 [示例工程](https://github.com/tencentyun/TUIVoiceRoom/blob/main/Android/Debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java#L88) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

### 步骤四：实现语音聊天房间
1. **实现房主创建语音聊天房间 [TRTCVoiceRoom#createRoom](https://cloud.tencent.com/document/product/647/45979#createroom)**
```java
// 1.房主调用创建房间
int roomId = 12345; //房间id
final TRTCVoiceRoomDef.RoomParam roomParam = new TRTCVoiceRoomDef.RoomParam();
roomParam.roomName = "房间名称";
roomParam.needRequest = false; // 上麦是否需要房主确认
roomParam.seatCount = 7; // 房间座位数，这里一共7个座位，房主占了一个后听众剩下6个座位
roomParam.coverUrl = "房间封面图的 URL 地址";
mTRTCVoiceRoom.createRoom(roomId, roomParam, new TRTCVoiceRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
				//创建成功
        }
    }
});
```
2. **实现听众加入语音聊天房间 [TRTCVoiceRoom#enterRoom](https://cloud.tencent.com/document/product/647/45979#enterroom)**
```java
// 1.听众调用加入房间
mTRTCVoiceRoom.enterRoom(roomId, new TRTCVoiceRoomCallback.ActionCallback() {
        @Override
        public void onCallback(int code, String msg) {
            if (code == 0) {
            //进房成功
            }
        }
});
```
3. **实现听众主动上麦 [TRTCVoiceRoom#enterSeat](https://cloud.tencent.com/document/product/647/45979#enterseat)**
```java
// 1: 听众调用上麦
int seatIndex = 2; //麦位的index
mTRTCVoiceRoom.enterSeat(seatIndex, new TRTCVoiceRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
        //操作成功
        }
    }
});

// 2.收到 onSeatListChange 回调，刷新您的麦位列表
@Override
public void onSeatListChange(final List<TRTCVoiceRoomDef.SeatInfo> seatInfoList) {
}
```
4. **实现房主抱人上麦 [TRTCVoiceRoom#pickSeat](https://cloud.tencent.com/document/product/647/45979#pickseat)**
```java
// 1: 房主调用抱人麦位
int seatIndex = 2; //麦位的index
String userId = "123"; //需要上麦的用户id
mTRTCVoiceRoom.pickSeat(1, userId, new TRTCVoiceRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
				//操作成功
        }
    }
});

// 2.收到 onSeatListChange 回调，刷新您的麦位列表
@Override
public void onSeatListChange(final List<TRTCVoiceRoomDef.SeatInfo> seatInfoList) {
}
```
5. **实现听众申请上麦 [TRTCVoiceRoom#sendInvitation](https://cloud.tencent.com/document/product/647/45979#sendinvitation)**
```java
// 听众端视角
// 1.听众调用申请上麦
String seatIndex = "1"; //麦位的index
String userId = "123"; //用户id
String inviteId = mTRTCVoiceRoom.sendInvitation("takeSeat", userId, seatIndex, null);

// 2.收到邀请的同意请求, 正式上麦
@Override
public void onInviteeAccepted(String id, String invitee) {
    if(id.equals(inviteId)) {
        mTRTCVoiceRoom.enterSeat(index, null);
    }
}

// 房主端视角
// 1.房主收到请求
 @Override
public void onReceiveNewInvitation(final String id, String inviter, String cmd, final String content) {
    if (cmd.equals("takeSeat")) {
        // 2.房主同意听众请求
         mTRTCVoiceRoom.acceptInvitation(id, null);
    }
}
```
6. **实现房主邀请上麦 [TRTCVoiceRoom#sendInvitation](https://cloud.tencent.com/document/product/647/45979#sendinvitation)**
```java
// 房主端视角
// 1.房主调用请求抱人上麦
String seatIndex = "1"; //麦位的index
String userId = "123"; //用户id
String inviteId = mTRTCVoiceRoom.sendInvitation("pickSeat", userId, seatIndex, null);

// 2.收到邀请的同意请求, 正式上麦
@Override
public void onInviteeAccepted(String id, String invitee) {
    if(id.equals(inviteId)) {
        mTRTCVoiceRoom.pickSeat(index, null);
    }
}

// 听众端视角
// 1.听众收到请求
 @Override
public void onReceiveNewInvitation(final String id, String inviter, String cmd, final String content) {
    if (cmd.equals("pickSeat")) {
        // 2.听众同意房主请求
         mTRTCVoiceRoom.acceptInvitation(id, null);
    }
}
```
7. **实现文字聊天 [TRTCVoiceRoom#sendRoomTextMsg](https://cloud.tencent.com/document/product/647/45979#sendroomtextmsg)**
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
8. **实现弹幕消息 [TRTCVoiceRoom#sendRoomCustomMsg](https://cloud.tencent.com/document/product/647/45979#sendroomcustommsg)**
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

## 常见问题
更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
