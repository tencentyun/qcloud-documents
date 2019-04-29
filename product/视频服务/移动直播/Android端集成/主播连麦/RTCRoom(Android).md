## RTCRoom

| 名称                                       | 描述                                |
| :------------------------------------: | :------------------------------: |
| setRTCRoomListener(IRTCRoomListener listener)       | 设置rtcroom回调   |
| login(serverDomain, loginInfo, loginCallback)             | 登录到RoomService后台  |
| logout()                                                                    | 从RoomService后台登出                       |
| getRoomList(int index, int count, GetRoomListCallback callback) | 获取房间列表（非必须，可选择使用您自己的房间列表）                       |
| createRoom(String roomID, String roomInfo, CreateRoomCallback cb) | 会议创建者：创建房间 （roomID 可不填）|
| enterRoom(String roomID, EnterRoomCallback cb) | 会议参与者：进入房间   |
| exitRoom(ExitRoomCallback callback)    | 会议创建者 OR 会议参与者：退出房间    |
| startLocalPreview(TXCloudVideoView videoView)   | 会议创建者 OR 会议参与者：开启摄像头预览      |
| stopLocalPreview()                                                | 停止摄像头预览                                  |
| addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback)                                                                                            | 播放会议参与者的远程视频画面   |
| deleteRemoteView(PusherInfo pusherInfo)                  | 停止播放会议参与者的远程视频画面    |
| sendRoomTextMsg(String message, SendTextMessageCallback callback)    | 发送文本（弹幕）消息    |
| sendRoomCustomMsg(String cmd, String message, SendCustomMessageCallback callback)  | 发送自定义格式的消息（点赞，送花）          |
| switchToBackground()                     | App 从前台切换到后台                              |
| switchToForeground()                     | App 从后台切换到前台                             |
| setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel)                     | 设置美颜                             |
| switchCamera()                           | 切换前后置摄像头，支持在推流中动态切换               |
| setMute(mute)                            | 静音              |
| setMirror(enable)                        | 画面镜像（此接口仅影响观众端效果，推流端一直保持镜像效果）                         |
| playBGM(String path)                  | 开始播放背景音乐 （path 指定音乐文件路径）           |
| stopBGM()                                  | 停止播放背景音乐                          |
| pauseBGM()                               | 暂停播放背景音乐                          |
| resumeBGM()                             | 继续播放背景音乐                          |
| setMicVolume(x)                           | 设置混音时麦克风的音量大小                     |
| setBGMVolume(x)                         | 设置混音时背景音乐的音量大小                    |
| getMusicDuration(fileName)                         | 获取背景音乐时长                    |
| setBitrateRange(minBitrate, maxBitrate)                         | 设置视频码率范围                    |
| setPauseImage(bitmap)                         | 设置后台时推送的图片                    |

## IRTCRoomListener

| 名称                                    | 描述                  |
| ------------------------------------- | ------------------- |
| onGetPusherList(pusherList)  | 通知：房间里已有的推流者列表（也就是当前有几路远程画面）      |
| onPusherJoin(pusherInfo)      | 通知：新的推流者加入进来（也就是通知您多了一路远程画面）              |
| onPusherQuit(pusherInfo)      | 通知：有推流者离开房间 （也就是通知您少了一路远程画面）            |
| onRecvRoomTextMsg(roomID, userID, userName, userAvatar, message)     |  聊天室：收到文本消息  |
| onRecvRoomCustomMsg(roomID, userID, userName, userAvatar, cmd, message)   | 聊天室：收到自定义消息|
| onRoomClosed(roomID)               | 通知：房间解散通知              |
| onDebugLog(log)                         | LOG：日志回调         |
| onError(errorCode, errorMessage)   | ERROR：错误回调        |



## RTCRoom 接口详情

### 1.setRTCRoomListener

- 接口定义：void setRTCRoomListener(IRTCRoomListener listener)
- 接口说明：设置 IRTCRoomListener 回调 ，具体回调函数请参考 IRTCRoomListener 的接口说明
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| listener | IRTCRoomListener | rtcroom 回调接口 |

- 示例代码：

```
mRTCRoom.setRTCRoomListener(new IRTCRoomListener() {
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
final String DOMAIN = "https://room.qcloud.com/weapp/rtc_room ";
LoginInfo loginInfo      = new LoginInfo();
loginInfo.sdkAppID       = sdkAppID;
loginInfo.userID         = userID;
loginInfo.userSig        = userSig;
loginInfo.accType        = accType;
loginInfo.userName       = userName;
loginInfo.userAvatar     = userAvatar;
mRTCRoom.login(DOMAIN, loginInfo, new RTCRoom.LoginCallback() {
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
mRTCRoom.logout();
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
mRTCRoom.getRoomList(0, 20, new RTCRoom.GetRoomListCallback() {
    @Override
    public void onSuccess(ArrayList<RoomInfo> data) {
        //每个房间的信息请参考RoomInfo定义
    }

    @Override
    public void onError(int errCode, String e) {
    }
});
```


### 5. createRoom

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
	mRTCRoom.createRoom("", roomInfo, new RTCRoom.CreateRoomCallback() {
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

### 6. enterRoom

- 接口定义：void enterRoom(String roomID, EnterRoomCallback cb) 

- 接口说明：（会议参与者）进入直播间。

- 示例代码：

```
mRTCRoom.enterRoom(mRoomId, new RTCRoom.EnterRoomCallback() {
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

### 7. exitRoom

- 接口定义：void exitRoom(final ExitRoomCallback cb)) 

- 接口说明：（会议创建者 OR 会议参与者）退出房间。

- 示例代码：

```
mRTCRoom.exitRoom(new RTCRoom.ExitRoomCallback() {
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


### 8. startLocalPreview

- 接口定义：void startLocalPreview(TXCloudVideoView view) 
- 接口说明：（会议创建者 OR 会议参与者）启动摄像头预览，默认是使用前置摄像头，可以通过switchCamera切换前后摄像头
- 示例代码：

```
TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mRTCRoom.startLocalPreview(mCaptureView);
```


### 9. stopLocalPreview

- 接口定义：void stopLocalPreview(boolean isNeedClearLastImg)
- 接口说明：（会议创建者 OR 会议参与者）关闭摄像头预览。
- 示例代码：

```
mRTCRoom.stopLocalPreview();
```

### 10.addRemoteView

- 接口定义：void addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback)
- 接口说明：（会议创建者 OR 会议参与者）播放会议参与者的远程视频画面 ，一般在收到 onPusherJoin（新会议参与者进入通知）时调用。
- 示例代码：

```
public void onPusherJoin(PusherInfo pusherInfo) {
    ......
    mRTCRoom.addRemoteView(videoView, pusherInfo, new RTCRoom.RemoteViewPlayCallback() {
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

### 11.deleteRemoteView

- 接口定义：void deleteRemoteView(final PusherInfo pusherInfo)
- 接口说明：停止播放某个会议参与者视频，一般在收到 onPusherQuit （会议参与者离开）时调用。
- 示例代码： 

```
public void onPusherQuit(PusherInfo pusherInfo) {
    ......
    mRTCRoom.deleteRemoteView(pusherInfo);
    ......
}
```

### 12.sendRoomTextMsg

- 接口定义：void sendRoomTextMsg(@NonNull String message, final SendTextMessageCallback callback)
- 接口说明：发送文本消息，房间里的其他人会收到 onRecvRoomTextMsg 通知。
- 示例代码： 

```
mRTCRoom.sendRoomTextMsg("hello", new RTCRoom.SendTextMessageCallback() {
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

### 13.sendRoomCustomMsg

- 接口定义：void sendRoomCustomMsg(@NonNull String cmd, @NonNull String message, final SendCustomMessageCallback callback)
- 接口说明：发送自定义消息。直播间其他人会收到 onRecvRoomCustomMsg 通知。
- 示例代码： 

```
mRTCRoom.sendRoomCustomMsg(String.valueOf(TCConstants.IMCMD_DANMU), 
                        “hello ”, new RTCRoom.SendCustomMessageCallback() {
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


### 14.switchToBackground

- 接口定义：void switchToBackground()
- 接口说明：从前台切换到后台，关闭采集摄像头数据，推送默认图片


### 15.switchToForeground

- 接口定义：void switchToForeground()
- 接口说明：由后台切换到前台，开启摄像头数据采集。


### 16.setBeautyFilter

- 接口定义：boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel)
- 接口说明：设置美颜风格、磨皮程度、美白级别和红润级别。
- 参数说明：

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| style          | int  | 磨皮风格：  0：光滑  1：自然  2：朦胧                  |
| beautyLevel    | int  | 磨皮等级： 取值为 0-9.取值为 0 时代表关闭美颜效果.默认值: 0,即关闭美颜效果 |
| whiteningLevel | int  | 美白等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果 |
| ruddyLevel     | int  | 红润等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果 |

- 示例代码：
  
```
mRTCRoom.setBeautyFilter(mBeautyStyle, mBeautyLevel, mWhiteningLevel, mRuddyLevel);
```


### 17.switchCamera

- 接口定义：void switchCamera()
- 接口说明：切换摄像头，前置摄像头时调用后变成后置，后置摄像头时调用后变成前置。该接口在启动预览startCameraPreview(TXCloudVideoView) 后调用才能生效，预览前调用无效。SDK启动预览默认使用前置摄像头。


### 18.setMute

- 接口定义：void setMute(mute)
- 接口说明：设置静音接口。设置为静音后SDK不再推送麦克风采集的声音，而是推送静音。
- 参数说明：

| 参数   | 类型      | 说明   |
| ---- | ------- | ---- |
| mute | boolean | 是否静音 |


### 19.setMirror

- 接口定义：void setMirror(boolean enable)
- 接口说明：设置播放端水平镜像。注意这个只影响播放端效果，不影响推流推流端。推流端看到的镜像效果是始终存在的，使用前置摄像头时推流端看到的是镜像画面，使用后置摄像头时推流端看到的是非镜像。
- 参数说明：

| 参数     | 类型      | 说明                                     |
| ------ | ------- | -------------------------------------- |
| enable | boolean | true 表示播放端看到的是镜像画面，false表示播放端看到的是非镜像画面 |

- 示例代码： 

```
//观众端播放看到的是镜像画面
mRTCRoom.setMirror(true);
```

### 20.playBGM

- 接口定义：boolean playBGM(String path)
- 接口说明：播放背景音乐。该接口用于混音处理，比如将背景音乐与麦克风采集到的声音混合后播放。返回结果中，true 表示播放成功，false 表示播放失败。
- 参数说明：

| 参数   | 类型     | 说明               |
| ---- | ------ | ---------------- |
| path | String | 背景音乐文件位于手机中的绝对路径 |


### 21.stopBGM

- 接口定义：boolean stopBGM()
- 接口说明：停止播放背景音乐。返回结果中，true 表示停止播放成功，false 表示停止播放失败。

### 22.pauseBGM

- 接口定义：boolean pauseBGM()
- 接口说明：暂停播放背景音乐。返回结果中，true 表示暂停播放成功，false 表示暂停播放失败。


### 23.resumeBGM

- 接口定义：boolean resumeBGM()
- 接口说明：恢复播放背景音乐。返回结果中，true 表示恢复播放成功，false 表示恢复播放失败。


### 24.setMicVolume

- 接口定义：boolean setMicVolume(float x)
- 接口说明：设置混音时麦克风的音量大小。返回结果中，true 表示设置麦克风的音量成功，false 表示设置麦克风的音量失败。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| x    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |



### 25.setBGMVolume

- 接口定义：boolean setBGMVolume(float x)
- 接口说明：设置混音时背景音乐的音量大小。返回结果中，true 表示设置背景音的音量成功，false 表示设置背景音的音量失败。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| x    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |


### 26.getMusicDuration

- 接口定义：int getMusicDuration(String path)
- 接口说明：获取背景音乐时长。返回结果单位为毫秒。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| path    | String | path == null 获取当前播放歌曲时长；path != null 获取path路径歌曲时长 |


### 27.setBitrateRange

- 接口定义：void setBitrateRange(int minBitrate, int maxBitrate)
- 接口说明：设置视频的码率区间。双人一般设为400到800；多人一般设为200到400
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| minBitrate    | int | 最小码率 |
| maxBitrate    | int | 最大码率 |

### 28.setPauseImage

- 接口定义：void setPauseImage(Bitmap bitmap)
- 接口说明：设置从前台切换到后台时，推送的图片。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| bitmap    | Bitmap | 背景图片bitmap |


## IRTCRoomListener 接口详情

### 1. onGetPusherList

- 接口定义：void onGetPusherList(List\<PusherInfo> pusherList)
- 接口说明：当新会议参与者加入房间时，会收到房间已存在的会议者列表。回调中您可以调用 addRemoteView 播放其他会议人员的视频。

- 示例代码：

```
public void onGetPusherList(List<PusherInfo> pusherInfoList) {
    for (PusherInfo pusherInfo : pusherInfoList) {
    		......
			mRTCRoom.addRemoteView(videoView, pusherInfo, new RTCRoom.RemoteViewPlayCallback() {
			@Override
			public void onPlayBegin() {
			    //
			}
				
			@Override
			public void onPlayError() {
			    
			}
		});
    }
}	
```

### 2. onPusherJoin

- 接口定义：void onPusherJoin(PusherInfo pusherInfo)
- 接口说明：当新的会议参与者加入房间时，房间中其他的会议参与者都会收到该通知。回调中您可以调用 addRemoteView 播放这个新来的会议参与者的视频。

- 示例代码：

```
 public void onPusherJoin(final PusherInfo pusherInfo) {
	 ......
	 mRTCRoom.addRemoteView(videoView, pusherInfo, new RTCRoom.RemoteViewPlayCallback() {
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
- 接口说明：当会议参与者离开房间时，房间的其他会议参与者都会收到该通知。回调中您可以调用 deleteRemoteView 停止播放这个会议参与者的视频。
- 示例代码：

```
public void onPusherQuit(PusherInfo pusherInfo) {
	......
	mRTCRoom.deleteRemoteView(pusherInfo);
	......
}
```


### 4. onRecvRoomTextMsg

- 接口定义：void onRecvRoomTextMsg(String roomID, String userID, String userName, String userAvatar, String message)
- 接口说明：当会议参与者调用sendRoomTextMsg时，房间内的其他会议参与者都会收到该通知。
- 示例代码： 

```
public void onRecvRoomTextMsg(String roomid, String userid, String userName, String userAvatar, String message) {
	//do nothing
}
```



### 5. onRecvRoomCustomMsg

- 接口定义：void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
- 接口说明：当会议参与者调用sendRoomCustomMsg时，房间内的其他会议参与者都会收到该通知。


### 6. onRoomClosed

- 接口定义：void onRoomClosed(String roomID)
- 接口说明：当房间销毁时，会议参与者会收到该通知。需要在回调中退出房间。
- 示例代码：

```
public void onRoomClosed(String roomId) {
	......
	mRTCRoom.exitRoom(new RTCRoom.ExitRoomCallback() {
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



### 7. onDebugLog

- 接口定义：void onDebugLog(String log)
- 接口说明：直播间日志回调。可以在回调中将日志保存到文件中，方便问题分析。
- 示例代码：

```
public void onDebugLog(String line) {
   Log.i(TAG,line);
}
```


### 8. onError

- 接口定义：void onError(int errorCode, String errorMessage)
- 接口说明：直播间错误回调
- 示例代码：

```
public void onError(final int errorCode, final String errorMessage) {
	 mRTCRoom.exitRoom(null);
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
