## 功能介绍

**直播+连麦** 是在 **秀场直播** 和 **在线教育** 场景中经常使用的直播模式，它既能支持高并发和低成本的在线直播，又能通过连麦实现主播和观众之间的视频通话互动，具有极强的场景适用性。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/aacdf8cdfa825f64f34af9c3c3e4154e.jpg" />


腾讯云基于 [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606) 组件实现“直播 + 连麦”功能，它分成 Client 和 Server 两个部分（都是开源的），对接攻略请参考 [DOC](https://cloud.tencent.com/document/product/454/14606)，本文档主要是详细列出了 Client 端的 API 列表：

## LiveRoom

| 名称                                       | 描述                                |
| :------------------------------------: | :------------------------------: |
| setLiveRoomListener(ILiveRoomListener listener)       | 设置liveroom回调   |
| login(serverDomain, loginInfo, loginCallback)             | 登录到RoomService后台  |
| logout()                                                                    | 从RoomService后台登出                       |
| getRoomList(int index, int count, GetRoomListCallback callback) | 获取房间列表（非必须，可选择使用您自己的房间列表）                       |
| getAudienceList(String roomID, final GetAudienceListCallback callback) | 获取某个房间里的观众列表（最多返回最近加入的 30 个观众）  |
| createRoom(String roomID, String roomInfo, CreateRoomCallback cb) | 主播：创建房间 （roomID 可不填）|
| enterRoom(String roomID, TXCloudVideoView videoView, EnterRoomCallback cb) | 观众：进入房间   |
| exitRoom(ExitRoomCallback callback)    | 主播 OR 观众：退出房间    |
| startLocalPreview(TXCloudVideoView videoView)   | 主播 OR 连麦观众：开启摄像头预览      |
| stopLocalPreview()                                                | 停止摄像头预览                                  |
| requestJoinPusher(int timeout, RequestJoinPusherCallback callback)     | 观众：发起连麦请求      |``
| joinPusher(final JoinPusherCallback cb)                      | 观众：进入连麦状态      |
| quitPusher(final QuitPusherCallback cb)                      | 观众：退出连麦状态      |
| acceptJoinPusher(String userID)                                 | 主播：接受来自观众的连麦请求 |
| rejectJoinPusher(String userID, String reason)            | 主播：拒绝来自观众的连麦请求 |
| kickoutSubPusher(String userID)                                | 主播：踢掉连麦中的某个观众          |
| getOnlinePusherList(final GetOnlinePusherListCallback callback)| 主播PK：获取在线的主播列表|
| startPlayPKStream(final String playUrl, TXCloudVideoView videoView, final PKStreamPlayCallback callback)| 主播PK：开始播放对方的视频流|
| stopPlayPKStream() | 主播PK：结束播放对方的视频流|
| sendPKRequest(String userID, int timeout, final RequestPKCallback callback) | 主播PK：发送PK请求|
| sendPKFinishRequest(String userID) | 主播PK：发送结束PK的请求 |
| acceptPKRequest(String userID) | 主播PK：授受PK请求 |
| rejectPKRequest(String userID, String reason) | 主播PK：拒绝PK请求 |
| addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback)                                                                                            | 主播：播放连麦观众的远程视频画面   |
| deleteRemoteView(PusherInfo pusherInfo)                  | 主播：移除连麦观众的远程视频画面    |
| sendRoomTextMsg(String message, SendTextMessageCallback callback)    | 发送文本（弹幕）消息    |
| sendRoomCustomMsg(String cmd, String message, SendCustomMessageCallback callback)  | 发送自定义格式的消息（点赞，送花）          |
| startScreenCapture()                             | 开始屏幕录制 （仅Android）            |
| stopScreenCapture()                             | 停止屏幕录制 （仅Android）           |
| switchToBackground()                     | App 从前台切换到后台                              |
| switchToForeground()                     | App 从后台切换到前台                             |
| setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel)                     | 设置美颜                             |
| switchCamera()                           | 切换前后置摄像头，支持在推流中动态切换               |
| setMute(mute)                            | 静音              |
| setMirror(enable)                        | 画面镜像（此接口仅影响观众端效果，主播一直保持镜像效果）                         |
| playBGM(String path)                  | 开始播放背景音乐 （path 指定音乐文件路径）           |
| stopBGM()                                  | 停止播放背景音乐                          |
| pauseBGM()                               | 暂停播放背景音乐                          |
| resumeBGM()                             | 继续播放背景音乐                          |
| setMicVolume(x)                           | 设置混音时麦克风的音量大小                     |
| setBGMVolume(x)                         | 设置混音时背景音乐的音量大小                    |
| getMusicDuration(fileName)                         | 获取背景音乐时长                    |
| startRecord(recordType)          | 开始视频录制                            |
| stopRecord()                              | 停止视频录制                            |
| setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener) | 设置视频录制回调    |
| incCustomInfo(fieldName, count)          |   增加房间自定义数值fieldName                          |
| decCustomInfo(fieldName, count)                              |   减少房间自定义数值fieldName                          |
| updateSelfUserInfo(userName, userAvatar)                              |   更新liveroom的用户信息                          |
| setPauseImage(bitmap)                         | 设置后台时推送的图片                    |

## ILiveRoomListener

| 名称                                    | 描述                  |
| ------------------------------------- | ------------------- |
| onGetPusherList(pusherList)  | 通知：房间里已有的推流者列表（也就是当前有几路远程画面）      |
| onPusherJoin(pusherInfo)      | 通知：新的推流者加入进来（也就是通知您多了一路远程画面）              |
| onPusherQuit(pusherInfo)      | 通知：有推流者离开房间 （也就是通知您少了一路远程画面）            |
| onRecvJoinPusherRequest(userID, userName, userAvatar) | 通知：主播收到观众的连麦请求         |
| onKickOut()           | 观众：收到被大主播踢开的消息           |
| onRecvPKRequest(String userID, String userName, String userAvatar, String streamUrl) | 收到PK请求 |
| onRecvPKFinishRequest(String userID) | 收到结束PK的请求 |
| onRecvRoomTextMsg(roomID, userID, userName, userAvatar, message)     |  聊天室：收到文本消息  |
| onRecvRoomCustomMsg(roomID, userID, userName, userAvatar, cmd, message)   | 聊天室：收到自定义消息|
| onRoomClosed(roomID)               | 通知：房间解散通知              |
| onDebugLog(log)                         | LOG：日志回调         |
| onError(errorCode, errorMessage)   | ERROR：错误回调        |



## LiveRoom 接口详情

### 1.setLiveRoomListener

- 接口定义：void setLiveRoomListener(ILiveRoomListener listener)
- 接口说明：设置 ILiveRoomListener 回调 ，具体回调函数请参考 ILiveRoomListener 的接口说明
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| listener | ILiveRoomListener | liveroom 回调接口 |

- 示例代码：

```
mLiveRoom.setLiveRoomListener(new ILiveRoomListener() {
    @Override
    void onPusherJoin(PusherInfo pusherInfo) {
        // ...
    }

    @Override
    void onPusherQuit(PusherInfo pusherInfo) {
        // ...
    }
    
    ......
});
```

### 2.login

- 接口定义：void login(String serverDomain, final LoginInfo loginInfo, final LoginCallback callback) 
- 接口说明：登录到 RoomService 后台，通过参数 serverDomain 可以指定是使用腾讯云的 RoomService 还是使用自建的 RoomService。
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| serverDomain | String | RoomService 的服务器地址，这部分可以参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)。 |
| loginInfo | LoginInfo | 登录参数，这部分可以参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)。 |
| callback | LoginCallback | 登录成功与否的回调 |

- 示例代码：

```
final String DOMAIN = "https://room.qcloud.com/weapp/live_room ";
LoginInfo loginInfo      = new LoginInfo();
loginInfo.sdkAppID       = sdkAppID;
loginInfo.userID         = userID;
loginInfo.userSig        = userSig;
loginInfo.accType        = accType;
loginInfo.userName       = userName;
loginInfo.userAvatar     = userAvatar;
mLiveRoom.login(DOMAIN, loginInfo, new LiveRoom.LoginCallback() {
    @Override
    public void onError(int errCode, String errInfo) {
    //
    }

    @Override
    public void onSuccess(String userId) {
    //登录成功,返回userId
    }
});
```



### 3.logout 

- 接口定义：void logout()
- 接口说明：从 RoomService 后台注销
- 示例代码：

```
mLiveRoom.logout();
```


### 4.getRoomList

- 接口定义：void getRoomList(int index, int count, GetRoomListCallback callback)
- 接口说明：拉取房间列表，index 和 count 两个参数用于做分页处理，表示：从序号 index 的房间开始拉取 count 个房间。这并非一个必须调用的 API，如果您已经有自己的房间列表服务模块，可以继续使用。

- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| index | int | 从第几个房间开始拉取 |
| count | int | 希望 RoomService 返回的房间个数 |
| callback | GetRoomListCallback | 拉取房间列表的回调 |

- 示例代码：

```
//拉取序号0开始，拉取20个房间
mLiveRoom.getRoomList(0, 20, new LiveRoom.GetRoomListCallback() {
    @Override
    public void onSuccess(ArrayList<RoomInfo> data) {
        //每个房间的信息请参考RoomInfo定义
    }

    @Override
    public void onError(int errCode, String e) {
    }
});
```

### 5.getAudienceList
- 接口定义：void getAudienceList(String roomID, final GetAudienceListCallback callback)
- 接口说明：获取某个房间里的观众列表，只返回最近进入房间的 30 位观众。


### 6. createRoom

- 接口定义：void createRoom(final String roomID, final String roomInfo, final CreateRoomCallback cb) 
- 接口说明：在 RoomService 后台创建一个直播房间。
- 参数说明：

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| roomID        | String  | 您可以通过 roomID 参数指定新房间的 ID，也可以不指定。如果您不指定房间 ID，RoomService 会自动生成一个新的 roomID 并通过 CreateRoomCallback 返回给你您。        |
| roomInfo    | String  | 由创建者自定义。在getRoomList中返回该信息 |
| cb | CreateRoomCallback  | 创建房间结果回调 |

- 示例代码：

```
	String roomInfo = mTitle;
	try {
	    roomInfo = new JSONObject()
	            .put("title", mTitle)
	            .put("frontcover", mCoverPicUrl)
	            .put("location", mLocation)
	            .toString();
	} catch (JSONException e) {
	    roomInfo = mTitle;
	}
	mLiveRoom.createRoom("", roomInfo, new LiveRoom.CreateRoomCallback() {
	    @Override
	    public void onSuccess(String roomId) {
	        Log.w(TAG,String.format("创建直播间%s成功", roomId));
	    }
	
	    @Override
	    public void onError(int errCode, String e) {
	        Log.w(TAG,String.format("创建直播间错误, code=%s,error=%s", errCode, e));
	    }
	});
```

### 7. enterRoom

- 接口定义：void enterRoom(String roomID, TXCloudVideoView videoView, EnterRoomCallback cb) 

- 接口说明：（观众）进入直播间。

- 示例代码：

```
mLiveRoom.enterRoom(mGroupId, mTXCloudVideoView, new LiveRoom.EnterRoomCallback() {
    @Override
    public void onError(int errCode, String errInfo) {
       TXLog.w(TAG, "enter room error : "+errInfo);
    }

    @Override
    public void onSuccess() {
       TXCLog.d(TAG, "enter room success ");
    }
});
```

### 8. exitRoom

- 接口定义：void exitRoom(final ExitRoomCallback callback) 

- 接口说明：（主播 OR 观众）退出房间。

- 示例代码：

```
mLiveRoom.exitRoom(new LiveRoom.ExitRoomCallback() {
    @Override
    public void onError(int errCode, String errInfo) {
        TXLog.w(TAG, "exit room error : "+errInfo);
    }

    @Override
    public void onSuccess() {
        TXCLog.d(TAG, "exit room success ");
    }
});
```


### 9. startLocalPreview

- 接口定义：void startLocalPreview(TXCloudVideoView view) 
- 接口说明：（主播 OR 连麦观众）启动摄像头预览，默认是使用前置摄像头，可以通过switchCamera切换前后摄像头
- 示例代码：

```
TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLiveRoom.startLocalPreview(mCaptureView);
```


### 10. stopLocalPreview

- 接口定义：void stopLocalPreview()
- 接口说明：（主播 OR 连麦观众）关闭摄像头预览。
- 示例代码：

```
mLiveRoom.stopLocalPreview();
```


### 11.requestJoinPusher

- 接口定义：void requestJoinPusher(int timeout, RequestJoinPusherCallback callback)
- 接口说明：（观众）请求和主播连麦时调用该接口。
- 示例代码：

```
mLiveRoom.requestJoinPusher(10, new LiveRoom.RequestJoinPusherCallback() {
    @Override
    public void onAccept() {
        mLiveRoom.startLocalPreview(videoView);
        mLiveRoom.setPauseImage(BitmapFactory.decodeResource(getResources(), R.drawable.pause_publish));
        mLiveRoom.setBeautyFilter(mBeautyStyle, mBeautyLevel, mWhiteningLevel, mRuddyLevel);
        mLiveRoom.joinPusher(new LiveRoom.JoinPusherCallback() {
            @Override
            public void onError(int errCode, String errInfo) {
                mLiveRoom.startLocalPreview(videoView);
                Toast.makeText(LivePlayActivity.this, "连麦失败：" + errInfo, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onSuccess() {
               
            }
        });
    }

    @Override
    public void onReject(String reason) {
        Toast.makeText(LivePlayActivity.this, "主播拒绝你的连麦请求", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onTimeOut() {
        Toast.makeText(LivePlayActivity.this, "连麦请求超时，主播没有做出回应", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onError(int code, String errInfo) {
        Toast.makeText(LivePlayActivity.this, "连麦请求失败：" + errInfo, Toast.LENGTH_SHORT).show();
    }
});
```



### 12.joinPusher

- 接口定义：void joinPusher(final JoinPusherCallback cb)
- 接口说明：（观众）开始推流，并进入连麦状态，是否最终连麦成功，要看 JoinPusherCallback 的回调结果。
- 示例代码：

```
mLiveRoom.joinPusher(new LiveRoom.JoinPusherCallback() {
    @Override
    public void onError(int errCode, String errInfo) {
        mLiveRoom.startLocalPreview(videoView);
        Toast.makeText(LivePlayActivity.this, "连麦失败：" + errInfo, Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onSuccess() {
       
    }
});
```


### 13.quitPusher
- 接口定义：void quitPusher(final QuitPusherCallback cb)
- 接口说明：（观众）主动退出连麦状态。
- 示例代码：

```
mLiveRoom.quitPusher(new LiveRoom.QuitPusherCallback() {
    @Override
    public void onError(int errCode, String errInfo) {

    }

    @Override
    public void onSuccess() {

    }
});
```


### 14.acceptJoinPusher

- 接口定义：void acceptJoinPusher(String userID)
- 接口说明：（主播）同意观众的连麦请求。
- 示例代码：

```
mLiveRoom.acceptJoinPusher(userId);
```

### 15.rejectJoinPusher

- 接口定义：void rejectJoinPusher(String userID, String reason)
- 接口说明：（主播）拒绝观众的连麦请求。
- 示例代码：

```
mLiveRoom.rejectJoinPusher(userId, "");
```

### 16.kickoutSubPusher

- 接口定义：void kickoutSubPusher(String userID)
- 接口说明：主播：踢掉连麦中的某个观众。
- 示例代码：

```
mLiveRoom.kickoutSubPusher(userId);
```

### 17.getOnlinePusherList

- 接口定义：void getOnlinePusherList(final GetOnlinePusherListCallback callback)
- 接口说明：主播PK：获取在线的主播列表
- 示例代码：

```
mLiveRoom.getOnlinePusherList(new LiveRoom.GetOnlinePusherListCallback() {
    @Override
    public void onError(int errCode, String errInfo) {

    }

    @Override
    public void onSuccess(final ArrayList<PusherInfo> pusherList) {
               
    }
});
```

### 18.startPlayPKStream

- 接口定义：void startPlayPKStream(final String playUrl, TXCloudVideoView videoView, final PKStreamPlayCallback callback)
- 接口说明：主播PK：开始播放对方的流
- 示例代码：

```
mLiveRoom.startPlayPKStream(streamUrl, videoView, new LiveRoom.PKStreamPlayCallback() {
     @Override
     public void onPlayBegin() {
												
     }

     @Override
     public void onPlayError() {
												
     }
});
```

### 19.stopPlayPKStream

- 接口定义：void stopPlayPKStream()
- 接口说明：主播PK：结束播放对方的流
- 示例代码：

```
mLiveRoom.stopPlayPKStream()
```

### 20.sendPKRequest

- 接口定义：void sendPKRequest(String userID, int timeout, final RequestPKCallback callback)
- 接口说明：主播PK：发送PK请求
- 示例代码：

```
mLiveRoom.sendPKRequest(userID, 10, new LiveRoom.RequestPKCallback() {
    @Override
    public void onAccept(String streamUrl) {

    }

    @Override
    public void onReject(String reason) {

    }

    @Override
    public void onTimeOut() {

    }

    @Override
    public void onError(int code, String errInfo) {

    }
});
```

### 21.sendPKFinishRequest

- 接口定义：void sendPKFinishRequest(String userID)
- 接口说明：主播PK：发送结束PK的请求
- 示例代码：

```
mLiveRoom.sendPKFinishRequest(userID)
```

### 22.acceptPKRequest

- 接口定义：void acceptPKRequest(String userID)
- 接口说明：主播PK：授受PK请求
- 示例代码：

```
 mLiveRoom.acceptPKRequest(userID);
```

### 23.rejectPKRequest

- 接口定义：void rejectPKRequest(String userID, String reason)
- 接口说明：主播PK：拒绝PK请求
- 示例代码：

```
 mLiveRoom.rejectPKRequest(userID, "");
```

### 24.addRemoteView

- 接口定义：void addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback)
- 接口说明：（主播）播放连麦观众的远程视频画面 ，一般在收到 onPusherJoin（新进连麦通知）时调用。
- 示例代码：

```
public void onPusherJoin(PusherInfo pusherInfo) {
    ......
    mLiveRoom.addRemoteView(videoView, pusherInfo, new LiveRoom.RemoteViewPlayCallback() {
        @Override
        public void onPlayBegin() {
        }

        @Override
        public void onPlayError() {
        }
    }); 
    ......
}
```

### 25.deleteRemoteView

- 接口定义：void deleteRemoteView(final PusherInfo pusherInfo)
- 接口说明：停止播放某个连麦主播视频，一般在收到 onPusherQuit （连麦者离开）时调用。
- 示例代码： 

```
public void onPusherQuit(PusherInfo pusherInfo) {
    ......
    mLiveRoom.deleteRemoteView(pusherInfo);
    ......
}
```

### 26.sendRoomTextMsg

- 接口定义：void sendRoomTextMsg(@NonNull String message, final SendTextMessageCallback callback)
- 接口说明：发送文本消息，直播间里的其他人会收到 onRecvRoomTextMsg 通知。
- 示例代码： 

```
mLiveRoom.sendRoomTextMsg("hello", new LiveRoom.SendTextMessageCallback() {
    @Override
    public void onError(int errCode, String errInfo) {
        Log.d(TAG, "sendRoomTextMsg error:");
    }

    @Override
    public void onSuccess() {
        Log.d(TAG, "sendRoomTextMsg success:");
    }
});
```

### 27.sendRoomCustomMsg

- 接口定义：void sendRoomCustomMsg(@NonNull String cmd, @NonNull String message, final SendCustomMessageCallback callback)
- 接口说明：发送自定义消息。直播间其他人会收到 onRecvRoomCustomMsg 通知。
- 示例代码： 

```
mLiveRoom.sendRoomCustomMsg(String.valueOf(TCConstants.IMCMD_DANMU), 
                        “hello ”, new LiveRoom.SendCustomMessageCallback() {
    @Override
    public void onError(int errCode, String errInfo) {
        Log.w(TAG, "sendRoomDanmuMsg error: "+errInfo);
    }

    @Override
    public void onSuccess() {
        Log.d(TAG, "sendRoomDanmuMsg success");
    }
});
```


### 28.startScreenCapture

- 接口定义：void startScreenCapture()
- 接口说明：启动屏幕录制。由于录屏是基于 Android 系统的原生能力实现的，处于安全考虑，Android 系统会在开始录屏前弹出一个提示，旨在告诫用户：“有 App 要截取您屏幕上的所有内容”。

> 注意：该接口在Android API 21接口才生效。录屏接口和摄像头预览（startCameraPreview）互斥，同时只能由一个生效

### 29.stopScreenCapture

- 接口定义：void stopScreenCapture()
- 接口说明：停止屏幕录制。


### 30.switchToBackground

- 接口定义：void switchToBackground()
- 接口说明：从前台切换到后台，关闭采集摄像头数据，推送默认图片


### 31.switchToForeground

- 接口定义：void switchToForeground()
- 接口说明：由后台切换到前台，开启摄像头数据采集。


### 32.setBeautyFilter

- 接口定义：boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel)
- 接口说明：设置美颜风格、磨皮程度、美白级别和红润级别。
- 参数说明：

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| style          | int  | 磨皮风格：  0：光滑  1：自然  2：朦胧                  |
| beautyLevel    | int  | 磨皮等级： 取值为 0-9.取值为 0 时代表关闭美颜效果.默认值: 0,即关闭美颜效果 |
| whiteningLevel | int  | 美白等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果 |
| ruddyLevel     | int  | 红润等级： 取值为 0-9.取值为 0 时代表关闭红润效果.默认值: 0,即关闭红润效果 |

- 示例代码：
  
```
mLiveRoom.setBeautyFilter(mBeautyStyle, mBeautyLevel, mWhiteningLevel, mRuddyLevel);
```


### 33.switchCamera

- 接口定义：void switchCamera()
- 接口说明：切换摄像头，前置摄像头时调用后变成后置，后置摄像头时调用后变成前置。该接口在启动预览startCameraPreview(TXCloudVideoView) 后调用才能生效，预览前调用无效。SDK启动预览默认使用前置摄像头。


### 34.setMute

- 接口定义：void setMute(mute)
- 接口说明：设置静音接口。设置为静音后SDK不再推送麦克风采集的声音，而是推送静音。
- 参数说明：

| 参数   | 类型      | 说明   |
| ---- | ------- | ---- |
| mute | boolean | 是否静音 |


### 35.setMirror

- 接口定义：void setMirror(boolean enable)
- 接口说明：设置播放端水平镜像。注意这个只影响播放端效果，不影响推流主播端。推流端看到的镜像效果是始终存在的，使用前置摄像头时推流端看到的是镜像画面，使用后置摄像头时推流端看到的是非镜像。
- 参数说明：

| 参数     | 类型      | 说明                                     |
| ------ | ------- | -------------------------------------- |
| enable | boolean | true 表示播放端看到的是镜像画面，false表示播放端看到的是非镜像画面 |

- 示例代码： 

```
//观众端播放看到的是镜像画面
mLiveRoom.setMirror(true);
```

### 36.playBGM

- 接口定义：boolean playBGM(String path)
- 接口说明：播放背景音乐。该接口用于混音处理，比如将背景音乐与麦克风采集到的声音混合后播放。返回结果中，true 表示播放成功，false 表示播放失败。
- 参数说明：

| 参数   | 类型     | 说明               |
| ---- | ------ | ---------------- |
| path | String | 背景音乐文件位于手机中的绝对路径 |


### 37.stopBGM

- 接口定义：boolean stopBGM()
- 接口说明：停止播放背景音乐。返回结果中，true 表示停止播放成功，false 表示停止播放失败。

### 38.pauseBGM

- 接口定义：boolean pauseBGM()
- 接口说明：暂停播放背景音乐。返回结果中，true 表示暂停播放成功，false 表示暂停播放失败。


### 39.resumeBGM

- 接口定义：boolean resumeBGM()
- 接口说明：恢复播放背景音乐。返回结果中，true 表示恢复播放成功，false 表示恢复播放失败。


### 40.setMicVolume

- 接口定义：boolean setMicVolume(float x)
- 接口说明：设置混音时麦克风的音量大小。返回结果中，true 表示设置麦克风的音量成功，false 表示设置麦克风的音量失败。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| x    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |



### 41.setBGMVolume

- 接口定义：boolean setBGMVolume(float x)
- 接口说明：设置混音时背景音乐的音量大小。返回结果中，true 表示设置背景音的音量成功，false 表示设置背景音的音量失败。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| x    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |


### 42.getMusicDuration

- 接口定义：int getMusicDuration(String path)
- 接口说明：获取背景音乐时长。返回结果单位为毫秒。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| path    | String | path == null 获取当前播放歌曲时长；path != null 获取path路径歌曲时长 |


### 43.startRecord

- 接口定义： int startRecord(int recordType)
- 接口说明：开始录制视频。该接口用于观众端将观看的视频实时保存到本地文件。
- 特别注意：该接口需要在 enterRoom 成功后调用，另外生成的视频文件由您的应用层代码负责管理，SDK不做清理。
- 返回结果：接口返回 0 启动录制成功；-1 表示正在录制，忽略这次录制启动；-2 表示还未开始推流，这次启动录制失败。
- 参数说明：

| 参数            | 类型     | 说明                               |
| ------------- | ------ | -------------------------------- |
| recordType | int | 录制类型，目前只支持纯视频录制TXRecordCommon.RECORD_TYPE_STREAM_SOURCE|

- 示例代码：

```
mLiveRoom.startRecord(TXRecordCommon.RECORD_TYPE_STREAM_SOURCE);
```

### 44.stopRecord

- 接口定义： int stopRecord()
- 接口说明：停止录制视频。录制结果会通过录制回调异步通知出来。


### 45.setVideoRecordListener

- 接口定义： void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)
- 接口说明：设置视频录制回调，用于接收视频录制进度及录制结果。
- 参数说明：

| 参数       | 类型                                    | 说明     |
| -------- | ------------------------------------- | ------ |
| listener | TXRecordCommon.ITXVideoRecordListener | 视频录制回调 |

- 示例代码：

```
mLiveRoom.setVideoRecordListener(new TXRecordCommon.ITXVideoRecordListener(){
    @Override
    public void onRecordEvent(int event, Bundle param) {
    }

    @Override
    public void onRecordProgress(long milliSecond) {
        Log.d(TAG, "record progress:" + milliSecond);
    }

    @Override
    public void onRecordComplete(TXRecordCommon.TXRecordResult result) {
        if (result.retCode == TXRecordCommon.RECORD_RESULT_OK) {
            String videoFile        = result.videoPath;
            String videoCoverPic    = result.coverPath;
        } else {
            Log.d(TAG, "record error:" + result.retCode + ", error msg:" + result.descMsg);
        }
    }
});
```

### 46.incCustomInfo

- 接口定义： void incCustomInfo(String fieldName, int count)
- 接口说明：增加自定义fieldName统计值。该接口用于统计房间的点赞，礼物等总数。最终的累计值可以通过房间信息roominfo的custom字段获得
- 参数说明：

| 参数            | 类型     | 说明                               |
| ------------- | ------ | -------------------------------- |
| fieldName | String | 需要统计的字段名称|
| count | int | 一次统计增加的值，一般一次增加1|

- 示例代码：

```
mLiveRoom.incCustomInfo(“praise”,1); 
```

### 47.decCustomInfo

- 接口定义： void decCustomInfo(String fieldName, int count)
- 接口说明：减少自定义fieldName统计值。该接口用于统计房间的点赞，礼物等总数。最终的累计值可以通过房间信息roominfo的custom字段获得
- 参数说明：

| 参数            | 类型     | 说明                               |
| ------------- | ------ | -------------------------------- |
| fieldName | String | 需要统计的字段名称|
| count | int | 一次统计减少的值，一般一次减少1|


### 48. updateSelfUserInfo

- 接口定义： void updateSelfUserInfo(String userName, String userAvatar)
- 接口说明：更新用户的昵称和头像信息。该接口主要用于用户修改昵称或者头像后实时更新liveroom的信息


### 49.setPauseImage

- 接口定义：void setPauseImage(Bitmap bitmap)
- 接口说明：设置从前台切换到后台时，推送的图片。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| bitmap    | Bitmap | 背景图片bitmap |


## ILiveRoomListener 接口详情

### 1. onGetPusherList

- 接口定义：void onGetPusherList(List<PusherInfo> pusherList)
- 接口说明：房间里已有的推流者列表（也就是当前有几路远程画面）。当新的连麦者加入房间时，新的连麦者会收到该通知。回调中您可以调用 addRemoteView 播放房间里已有连麦者的视频。

- 示例代码：

```
 public void onGetPusherList(List<PusherInfo> pusherList) {
	 	......
	 	for (PusherInfo pusherInfo : pusherInfoList) {
         	mLiveRoom.addRemoteView(videoView, pusherInfo, new LiveRoom.RemoteViewPlayCallback() {
			    @Override
			    public void onPlayBegin() {
			        //
			    }
			
			    @Override
			    public void onPlayError() {
			        
			    }
			});
     	}
	 	......
 }
```

### 2. onPusherJoin

- 接口定义：void onPusherJoin(PusherInfo pusherInfo)
- 接口说明：当新的连麦者加入房间时，大主播和其他的连麦者都会收到该通知。回调中您可以调用 addRemoteView 播放这个新来的连麦者的视频。

- 示例代码：

```
 public void onPusherJoin(final PusherInfo pusherInfo) {
	 ......
	 mLiveRoom.addRemoteView(videoView, pusherInfo, new LiveRoom.RemoteViewPlayCallback() {
	    @Override
	    public void onPlayBegin() {
	        //
	    }
	
	    @Override
	    public void onPlayError() {
	        
	    }
	});
	......
 }
```

### 3. onPusherQuit

- 接口定义：void onPusherQuit(PusherInfo pusherInfo)
- 接口说明：当连麦者离开房间时，大主播和其他的连麦者都会收到该通知。回调中您可以调用 deleteRemoteView 停止播放这个连麦者的视频。
- 示例代码：

```
public void onPusherQuit(PusherInfo pusherInfo) {
	......
	mLiveRoom.deleteRemoteView(pusherInfo);
	......
}
```


### 4. onRecvJoinPusherRequest

- 接口定义：void onRecvJoinPusherRequest(String userID, String userName, String userAvatar)
- 接口说明：当观众向主播申请连麦时，主播收到该通知。主播可以在回调中接受（acceptJoinPusher）或者拒绝（rejectJoinPusher）申请。
- 示例代码：

```
public void onRecvJoinPusherRequest(final String userId, String userName, String userAvatar) {
    final AlertDialog.Builder builder = new AlertDialog.Builder(mActivity)
		.setCancelable(true)
		.setTitle("提示")
		.setMessage(userName + "向您发起连麦请求")
		.setPositiveButton("接受", new DialogInterface.OnClickListener() {
		    @Override
		    public void onClick(DialogInterface dialog, int which) {
		        mLiveRoom.acceptJoinPusher(userId);
		        dialog.dismiss();
		    }
		})
		.setNegativeButton("拒绝", new DialogInterface.OnClickListener() {
		    @Override
		    public void onClick(DialogInterface dialog, int which) {
		        mLiveRoom.rejectJoinPusher(userId, "主播拒绝了您的连麦请求");
		        dialog.dismiss();
		    }
	});
}
```

### 5. onKickOut

- 接口定义：void onKickOut()
- 接口说明：当主播把一个连麦者踢出连麦状态后，对应的连麦者会收到该通知。在回调中您可以停止本地预览以及退出直播。
- 示例代码： 

```
public void onKickOut() {
	......
	mLiveRoom.stopLocalPreview();
   	mLiveRoom.quitPusher(new LiveRoom.QuitPusherCallback() {
        @Override
        public void onError(int errCode, String errInfo) {

        }

        @Override
        public void onSuccess() {

        }
	});
	......
}
```

### 6. onRecvPKRequest

- 接口定义：void onRecvPKRequest(String userID, String userName, String userAvatar, String streamUrl)
- 接口说明：当一个主播调用sendPKRequest向另一个主播发起PK请求的时候；另一个主播会收到该回调通知。在该回调中，您可以展示一个收到PK请求的提示框，询问用户是接受还是拒绝。
- 示例代码：

```
@Override
public void onRecvPKRequest(final String userID, final String userName, final String userAvatar, final String streamUrl){
     final AlertDialog.Builder builder = new AlertDialog.Builder(mActivity)
            .setCancelable(true)
            .setTitle("提示")
            .setMessage(userName + "向您发起PK请求")
            .setPositiveButton("接受", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    mLiveRoom.acceptPKRequest(userID);
                    mLiveRoom.startPlayPKStream(streamUrl, videoView, new LiveRoom.PKStreamPlayCallback() {
                        @Override
                        public void onPlayBegin() {
												
                        }

                        @Override
                        public void onPlayError() {
												
                        }
                    });
                    dialog.dismiss();
                }
            })
            .setNegativeButton("拒绝", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    mLiveRoom.rejectPKRequest(userID, "主播拒绝了您的PK请求");
                    dialog.dismiss();
                }
            });

    final AlertDialog alertDialog = builder.create();
    alertDialog.setCancelable(false);
    alertDialog.setCanceledOnTouchOutside(false);
    alertDialog.show();
}
```

### 7. onRecvPKFinishRequest

- 接口定义：void onRecvPKFinishRequest(String userID)
- 接口说明：当一个主播调用sendPKFinishRequest通知另一个主播结束PK的时候；另一个主播会收到该回调通知。在该回调中，您需要调用stopPlayPKStream结束PK，并做好相关清理工作。
- 示例代码：

```
@Override
public void onRecvPKFinishRequest(final String userID){
    mLiveRoom.stopPlayPKStream();
}
```

### 8. onRecvRoomTextMsg

- 接口定义：void onRecvRoomTextMsg(String roomID, String userID, String userName, String userAvatar, String message)
- 接口说明：当主播或者观众端调用sendRoomTextMsg时，房间内的主播或者观众都会收到该通知。
- 示例代码： 

```
public void onRecvRoomTextMsg(String roomid, String userid, String userName, String userAvatar, String message) {
	//do nothing
}
```



### 9. onRecvRoomCustomMsg

- 接口定义：void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
- 接口说明：当主播或者观众端调用sendRoomCustomMsg时，房间内的主播或者观众都会收到该通知。

### 10. onRoomClosed

- 接口定义：void onRoomClosed(String roomID)
- 接口说明：当房间销毁时，观众会收到该通知。需要在回调中退出房间。
- 示例代码：

```
public void onRoomClosed(String roomId) {
	......
	mLiveRoom.exitRoom(new LiveRoom.ExitRoomCallback() {
	    @Override
	    public void onSuccess() {
	        Log.i(TAG, "exitRoom Success");
	    }
	
	    @Override
	    public void onError(int errCode, String e) {
	        Log.e(TAG, "exitRoom failed, errorCode = " + errCode + " errMessage = " + e);
	    }
	});
	......
}
```



### 11. onDebugLog

- 接口定义：void onDebugLog(String log)
- 接口说明：直播间日志回调。可以在回调中将日志保存到文件中，方便问题分析。
- 示例代码：

```
public void onDebugLog(String line) {
   Log.i(TAG,line);
}
```


### 12. onError

- 接口定义：void onError(int errorCode, String errorMessage)
- 接口说明：直播间错误回调
- 示例代码：

```
public void onError(final int errorCode, final String errorMessage) {
	 mLiveRoom.exitRoom(null);
    new AlertDialog.Builder(mActivity)
            .setTitle("直播间错误")
            .setMessage(errorMessage + "[" + errorCode + "]")
            .setNegativeButton("确定", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    
                }
   				}).show();
}
```
