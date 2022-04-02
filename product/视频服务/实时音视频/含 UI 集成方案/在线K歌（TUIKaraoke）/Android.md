## 组件介绍
TUIKaraoke 是一个开源的音视频 UI 组件，通过在项目中集成 TUIKaraoke 组件，您只需要编写几行代码就可以为您的应用添加在线 K 歌场景，体验 K 歌、麦位管理、收发礼物、文字聊天等 TRTC 在 KTV 场景下的相关能力。TUIKaraoke 同时支持 iOS 平台的源代码，基本功能如下图所示：

<table>
     <tr>
         <th width=20%  style="text-align:center">聊天</th>
         <th width=20%  style="text-align:center">点歌播放</th>
         <th width=20%  style="text-align:center">音效管理</th>
         <th width=20%  style="text-align:center">发送礼物</th>
     </tr>
<tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/819e86970cecabcb10143a49a4759b32.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/62952ca07b61d39ac57f2e261bfce015.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/19a4a38ff7107418d95625016a7beee3.png"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/95dcd260cea4b53d23f9648171df5fe6.png"/></td>
</tr>
</table>


## 组件集成
### 步骤一：下载并导入 TUIKaraoke 组件

单击进入 [Github](https://github.com/tencentyun/TUIKaraoke) ，选择克隆/下载代码，然后拷贝 Android目录下的 Source 和 Debug 目录到您的工程中，并完成如下导入动作：
- 在 `setting.gradle` 中完成导入，参考如下：
```
include ':Source'
include ':Debug'
```
- 在 app 的 build.gradle 文件中添加对 TUIKaraoke 的依赖：
```
api project(':Source')
```
- 在根目录的 `build.gradle` 文件中添加 `TRTC SDK` 和 `IM SDK` 的依赖：
```
ext {
    liteavSdk = "com.tencent.liteav:LiteAVSDK_TRTCl:latest.release"
    imSdk = "com.tencent.imsdk:imsdk-plus:latest.release"
}
```

### 步骤二：配置权限及混淆规则

在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请麦克风、读取存储权限等）：

```
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />        // 使用场景：悬浮窗功能需要此权限；
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />                  // 使用场景：使用蓝牙耳机时需要此权限；
```

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```
-keep class com.tencent.** { *; }
```

### 步骤三：初始化并登录 
相关接口详情请参见 [TUIKaraoke](https://cloud.tencent.com/document/product/647/59404#sharedinstance)。

```java
  // 1.初始化
  TRTCKaraokeRoom mTRTCKaraokeRoom = TRTCKaraokeRoom.sharedInstance(this);
  mTRTCKaraokeRoom.setDelegate(this);
  // 2.登录
  mTRTCKaraokeRoom.login(SDKAppID, UserID, UserSig, new TRTCKaraokeRoomCallback.ActionCallback() {
      @Override
      public void onCallback(int code, String msg) {
          if (code == 0) {
          //登录成功
          }
      }
  });
```
**参数说明**：
- **SDKAppID**：**TRTC 应用ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3d6ebfa2a1e4ae5d3af3ecd564fb1463.png)
- **Secretkey**：**TRTC 应用密钥**，和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [TUICalling示例工程](https://github.com/tencentyun/TUICalling/blob/main/Android/App/src/main/java/com/tencent/liteav/demo/LoginActivity.java#L74)自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

### 步骤四：实现在线KTV场景
1. **主播创建房间 [TUIKaraoke.createRoom](https://cloud.tencent.com/document/product/647/59404#createroom)**
```java
int roomId = "房间ID";
TRTCKaraokeRoomDef.RoomParam roomParam = new TRTCKaraokeRoomDef.RoomParam();
roomParam.roomName = "房间名称";
roomParam.needRequest = false; // 上麦是否需要房主确认
roomParam.seatCount = 8;       // 房间座位数，一共8个座位
roomParam.coverUrl = "房间封面图URL";
mTRTCKaraokeRoom.createRoom(roomId, roomParam, new TRTCKaraokeRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
      if (code == 0) {
        //创建成功
      }
    }
});
```
2. **听众进入房间 [TUIKaraoke.enterRoom](https://cloud.tencent.com/document/product/647/59404#enterroom)**
```java
mTRTCKaraokeRoom.enterRoom(roomId, new TRTCKaraokeRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
        //进房成功
        }
    }
});
```
3. **听众主动上麦 [TUIKaraoke.enterSeat](https://cloud.tencent.com/document/product/647/59404#enterseat)**
```java
// 1.听众调用上麦
int seatIndex = 1;
mTRTCKaraokeRoom.enterSeat(seatIndex, new TRTCKaraokeRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
        //上麦成功
        }
    }
});
// 2.收到 onSeatListChange 回调，刷新麦位列表
@Override
public void onSeatListChange(final List<TRTCKaraokeRoomDef.SeatInfo> seatInfoList) {
}
```
>? 其他关于麦位管理的相关操作，您可参考 [TUIKaraoke接口文档](https://cloud.tencent.com/document/product/647/59404) 按需实现，或者可以参考我们的 [TUIKaraoke示例工程](https://github.com/tencentyun/TUIKaraoke/)。
4. **实现音乐播放并体验 KTV 场景**
您可以根据自己的业务获取音乐 ID 和 URL链接播放歌曲，接口详情请参见 [TUIKaraoke 音乐播放接口](https://cloud.tencent.com/document/product/647/59404#.E9.9F.B3.E4.B9.90.E6.92.AD.E6.94.BE.E6.8E.A5.E5.8F.A32)。
```java
//播放音乐
mTRTCKaraokeRoom.startPlayMusic(musicID,url);
//停止音乐
mTRTCKaraokeRoom.stopPlayMusic();
```

完成以上步骤，您可以实现KTV基本功能。如果您的业务还需要文字聊天、发送礼物等功能，可以接入以下能力。

### 步骤五：文字聊天功能（可选）
如果您需要实现各主播或听众之间文字聊天的功能，可以通过以下方法发送或接收聊天信息。
相关接口详情请参见 [TRTCKaraokeRoom.sendRoomTextMsg](https://cloud.tencent.com/document/product/647/59404#sendroomtextmsg)。
```java
// 发送端：发送文本消息
mTRTCKaraokeRoom.sendRoomTextMsg("Hello Word!", new TRTCKaraokeRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            //发送成功
        }
    }
});
// 接收端：监听文本消息
mTRTCKaraokeRoom.setDelegate(new TRTCKaraokeRoomDelegate() {
  @Override
  public void onRecvRoomTextMsg(String message, TRTCKaraokeRoomDef.UserInfo userInfo) {
      Log.d(TAG, "收到来自" + userInfo.userName + "的消息:" + message);
  }
});
```

### 步骤六：礼物发送功能（可选）
如果您需要实现礼物发送和接收功能，可以通过以下方法发送或接收礼物并展示。
```java
// 发送端：通过自定义 "CMD_GIFT" 来区分礼物消息
mTRTCKaraokeRoom.sendRoomCustomMsg("CMD_GIFT",date, new TRTCKaraokeRoomCallback.ActionCallback() {
    @Override
    public void onCallback(int code, String msg) {
        if (code == 0) {
            //发送成功
        }
    }
});

// 接收端：监听礼物消息
mTRTCKaraokeRoom.setDelegate(new TRTCKaraokeRoomDelegate() {
    @Override
    public void onRecvRoomCustomMsg(String cmd, String message, TRTCKaraokeRoomDef.UserInfo userInfo) {
        if ("CMD_GIFT".equals(cmd)) {
            // 收到礼物消息
            Log.d(TAG, "收到来自" + userInfo.userName + "的礼物:" + message);
        }
    }
});
```

## 常见问题
### TUIKaraoke 组件支持变声、变调、混响等音效功能吗？
支持，具体请参见 [TUIKaraoke 示例工程](https://github.com/tencentyun/TUIKaraoke/blob/main/Android/Source/src/main/java/com/tencent/liteav/tuikaraoke/ui/audio/AudioEffectPanel.java)。

>? 更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
