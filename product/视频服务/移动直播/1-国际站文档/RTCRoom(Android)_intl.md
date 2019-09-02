## RTCRoom

| Name | Description |
| :------------------------------------: | :------------------------------: |
| setRTCRoomListener(IRTCRoomListener listener) | Sets rtcroom callback |
| login(serverDomain, loginInfo, loginCallback) | Logs in to the RoomService backend |
| logout() | Logs out of the RoomService backend |
| getRoomList(int index, int count, GetRoomListCallback callback) | Gets the room list (optional, you can select your room list.) |
| createRoom(String roomID, String roomInfo, CreateRoomCallback cb) | Meeting initiator: Creates a room (roomID can be left blank.) |
| enterRoom(String roomID, EnterRoomCallback cb) | Meeting participant: Enters a room |
| exitRoom(ExitRoomCallback callback) | Meeting initiator or meeting participant: Exits a room |
| startLocalPreview(TXCloudVideoView videoView) | Meeting initiator or meeting participant: Enables camera preview |
| stopLocalPreview() | Disables camera preview |
| addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback) | Plays back the remote video images of the meeting participant |
| deleteRemoteView(PusherInfo pusherInfo) | Stops playing back the remote video images of the meeting participant |
| sendRoomTextMsg(String message, SendTextMessageCallback callback) | Sends a text (on-screen comment) message |
| sendRoomCustomMsg(String cmd, String message, SendCustomMessageCallback callback) | Sends a custom message (gives a "Like" or flower) |
| switchToBackground() | App switches from foreground to background |
| switchToForeground() | App switches from background to foreground |
| setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel) | Sets beauty filter effects |
| switchCamera() | Switches between front and rear cameras. Dynamic switching is supported during push |
| setMute(mute) | Enables Mute |
| setMirror(enable) | Sets mirroring for images (this API works on the effect at the viewer end only; the pusher end always has the mirroring effect available) |
| playBGM(String path) | Starts background music ("path" indicates the path to the music file) |
| stopBGM() | Stops background music |
| pauseBGM() | Pauses background music |
| resumeBGM() | Resumes background music |
| setMicVolume(x) | Sets microphone volume for audio mixing |
| setBGMVolume(x) | Sets background music volume for audio mixing |
| getMusicDuration(fileName) | Gets background music duration |
| setBitrateRange(minBitrate, maxBitrate) | Sets video bitrate range |
| setPauseImage(bitmap) | Sets the images to be pushed when switching to the background |

## IRTCRoomListener

| Name | Description |
| ------------------------------------- | ------------------- |
| onGetPusherList(pusherList) | Notification: The list of existing pushers in the room (the number of remote video streams) |
| onPusherJoin(pusherInfo) | Notification: A new pusher joined the room (notifies you of addition of a remote video stream) |
| onPusherQuit(pusherInfo) | Notification: A pusher left the room (notifies you of subtraction of a remote video stream) |
| onRecvRoomTextMsg(roomID, userID, userName, userAvatar, message) | Chat room: Receives a text message |
| onRecvRoomCustomMsg(roomID, userID, userName, userAvatar, cmd, message) | Chat room: Receives a custom message |
| onRoomClosed(roomID) | Notification: Notifies you of the room being closed |
| onDebugLog(log) | LOG: Log callback |
| onError(errorCode, errorMessage) | ERROR: Error callback |



## Details of RTCRoom APIs

### 1. setRTCRoomListener

- API definition: void setRTCRoomListener(IRTCRoomListener listener)
- API description: Sets IRTCRoomListener callback. For the callback function, please see the IRTCRoomListener API description.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| listener | IRTCRoomListener | An rtcroom callback API |

- Sample code:

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

### 2. login

- API definition: void login(String serverDomain, final LoginInfo loginInfo, final LoginCallback callback) 
- API description: Logs in to the RoomService backend. You can specify whether to use the Tencent Cloud RoomService or the user-deployed RoomService.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| serverDomain | String | Server address of RoomService. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| loginInfo | LoginInfo | The login parameter. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| callback | LoginCallback | Callback to verify whether the login is successful |

- Sample code:

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
    //The userId is returned upon successful login.
    }
});
```



### 3. logout 

- API definition: void logout();
- API description: Logs out of the RoomService backend
- Sample code:

```
mRTCRoom.logout();
```


### 4. getRoomList

- API definition: void getRoomList(int index, int count, GetRoomListCallback callback)
- API description: Pulls the room list. The parameters index and count are used to handle paging, which means you can pull "count" rooms from the room numbered "index". This API is not required to be called, and you can continue using it if you already have your own room list service modules.

- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| index | int | The index of the room from which pull starts |
| count | int | Number of rooms to be returned via RoomService |
| callback | GetRoomListCallback | Callback of pulling a room list |

- Sample code:

```
//The pulling begins from the number 0, and ends when 20 rooms are pulled.
mRTCRoom.getRoomList(0, 20, new RTCRoom.GetRoomListCallback() {
    @Override
    public void onSuccess(ArrayList<RoomInfo> data) {
        //For information on each room, please see the definition of RoomInfo.
    }

    @Override
    public void onError(int errCode, String e) {
    }
});
```


### 5. createRoom

- API definition: void createRoom(final String roomID, final String roomInfo, final CreateRoomCallback cb) 
- API description: Creates a room at RoomService backend.
- Parameter description:

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| roomID | String | You can specify an ID for a new room with the parameter roomID, or leave it unspecified. If you do not specify an ID for the room, RoomService will automatically create a new roomID and return it to you through CreateRoomCallback. |
| roomInfo | String | To be customized by the creator. This information is returned via getRoomList |
| cb | CreateRoomCallback | Creates room creation result callback |

- Sample code:

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
	        Log.w(TAG,String.format("Room %s created successfully", roomId));
	    }
	
	    @Override
	    public void onError(int errCode, String e) {
	        Log.w(TAG,String.format("Error while creating the room, code=%s,error=%s", errCode, e));
	    }
	});
```

### 6. enterRoom

- API definition: void enterRoom(String roomID, EnterRoomCallback cb) 

- API description: (Meeting participant) enters a room.

- Sample code:

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

- API definition: void exitRoom(final ExitRoomCallback cb)) 

- API description: (Meeting initiator or meeting participant) exits a room.

- Sample code:

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

- API definition: void startLocalPreview(TXCloudVideoView view) 
- API description: (A meeting initiator or meeting participant) enables camera preview. The front camera is used by default, and switchCamera is used to switch between front and rear cameras.
- Sample code:

```
TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mRTCRoom.startLocalPreview(mCaptureView);
```


### 9. stopLocalPreview

- API definition: void stopLocalPreview(boolean isNeedClearLastImg)
- API description: (Meeting initiator or meeting participant) disables camera preview.
- Sample code:

```
mRTCRoom.stopLocalPreview();
```

### 10. addRemoteView

- API definition: void addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback)
- API description: (A meeting initiator or meeting participant) plays the remote video image of a meeting participant. This API is called when onPusherJoin (notification of new meeting participant entering the room) is received.
- Sample code:

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

### 11. deleteRemoteView

- API definition: void deleteRemoteView(final PusherInfo pusherInfo)
- API description: Stops playing the video of a meeting participant. This API is called when onPusherQuit (a meeting participant leaves) is received.
- Sample code: 

```
public void onPusherQuit(PusherInfo pusherInfo) {
    ......
    mRTCRoom.deleteRemoteView(pusherInfo);
    ......
}
```

### 12. sendRoomTextMsg

- API definition: void sendRoomTextMsg(@NonNull String message, final SendTextMessageCallback callback)
- API description: Sends a text message. Other members in the room will receive a notification via onRecvRoomTextMsg.
- Sample code: 

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

### 13. sendRoomCustomMsg

- API definition: void sendRoomCustomMsg(@NonNull String cmd, @NonNull String message, final SendCustomMessageCallback callback)
- API description: Sends a custom message. Other members in the room will receive a notification via onRecvRoomCustomMsg.
- Sample code: 

```
mRTCRoom.sendRoomCustomMsg(String.valueOf(TCConstants.IMCMD_DANMU), 
                        "hello ", new RTCRoom.SendCustomMessageCallback() {
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


### 14. switchToBackground

- API definition: void switchToBackground()
- API description: Switches from foreground to background, stops collecting camera data, and pushes default pictures.


### 15. switchToForeground

- API definition: void switchToForeground()
- API description: Switches from background to foreground, and starts collecting camera data.


### 16. setBeautyFilter

- API definition: boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel)
- API description: Sets beauty filter style, dermabrasion level, whitening level, and blushing level.
- Parameter description:

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| style | int | Dermabrasion style: 0: Smooth 1: Natural 2: Hazy |
| beautyLevel | int | Dermabrasion level: Value range: 0-9. 0 means disabling beauty filter. Default is 0, i.e., disabling beauty filter |
| whiteningLevel | int | Whitening level: Value range: 0-9. 0 means disabling whitening. Default is 0, i.e., disabling whitening |
| ruddyLevel | int | Blushing level: Value range: 0-9. 0 means disabling blushing. Default is 0, i.e., disabling blushing |

- Sample code:
  
```
mRTCRoom.setBeautyFilter(mBeautyStyle, mBeautyLevel, mWhiteningLevel, mRuddyLevel);
```


### 17. switchCamera

- API definition: void switchCamera()
- API description: Switches between cameras. When the front camera is in use, calling this API enables a switch from the front camera to the rear camera, and vice versa. This API takes effect only if it is called after camera preview (startCameraPreview(TXCloudVideoView)) is enabled. The front camera is used by default when the SDK enables camera preview.


### 18. setMute

- API definition: void setMute(mute)
- API description: Enables Mute Once Mute is enabled, the SDK shifts from pushing microphone-collected sounds to pushing mute.
- Parameter description:

| Parameter | Type | Description |
| ---- | ------- | ---- |
| mute | boolean | Whether to enable Mute |


### 19. setMirror

- API definition: void setMirror(boolean enable)
- API description: Sets horizontal mirroring at the viewer end. Note that this API only works on the viewer end, not the pusher end. The mirroring effect is always seen from the pusher end. The image is seen as mirrored from the pusher end when the front camera is in use, and non-mirrored when the rear camera is in use.
- Parameter description:

| Parameter | Type | Description |
| ------ | ------- | -------------------------------------- |
| enable | boolean | "true" indicates the image is seen as mirrored, and "false" indicates the image is seen as non-mirrored. |

- Sample code: 

```
//The image is seen as mirrored at the viewer end
mRTCRoom.setMirror(true);
```

### 20. playBGM

- API definition: boolean playBGM(String path)
- API description: Starts background music. This API is used for audio mixing, for example, mixing background music with sounds collected from the microphone for playback. If the playback is successful, a value of "true" is returned. If the playback fails, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ------ | ---------------- |
| path | String | The background music file is located in the absolute path in the phone |


### 21. stopBGM

- API definition: boolean stopBGM()
- API description: Stops background music. If the playback ends successfully, a value of "true" is returned. If the playback fails to end, a value of "false" is returned.

### 22. pauseBGM

- API definition: boolean pauseBGM()
- API description: Pauses background music. If the playback pauses successfully, a value of "true" is returned. If the playback fails to pause, a value of "false" is returned.


### 23. resumeBGM

- API definition: boolean resumeBGM()
- API description: Resumes background music. If the playback resumes successfully, a value of "true" is returned. If the playback fails to resume, a value of "false" is returned.


### 24. setMicVolume

- API definition: boolean setMicVolume(float x)
- API description: Sets microphone volume for audio mixing. If the microphone volume is set successfully, a value of "true" is returned. If the microphone volume fails to be set, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| x | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |



### 25. setBGMVolume

- API definition: boolean setBGMVolume(float x)
- API description: Sets background music volume for audio mixing. If the background music volume is set successfully, a value of "true" is returned. If the background music volume fails to be set, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| x | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |


### 26. getMusicDuration

- API definition: int getMusicDuration(String path)
- API description: Gets background music duration. The returned value is in seconds.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| path | String | Gets the duration of the current music if path == null and the duration of music under the path if path != null |


### 27. setBitrateRange

- API definition: void setBitrateRange(int minBitrate, int maxBitrate)
- API description: Sets video bitrate range, which is 400-800 for two persons, and 200-400 for more than two persons.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| minBitrate | int | The minimum video bitrate |
| maxBitrate | int | The maximum video bitrate |

### 28. setPauseImage

- API definition: void setPauseImage(Bitmap bitmap)
- API description: Sets the images to be pushed when switching from foreground to background.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| bitmap | Bitmap | Background image bitmap |


## Details of IRTCRoomListener APIs

### 1. onGetPusherList

- API definition: void onGetPusherList(List\<PusherInfo> pusherList)
- API description: A new meeting participant will receive the current list of meeting participants when entering a room. In the callback, you can call addRemoteView to playback the video of other meeting participants.

- Sample code:

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

- API definition: void onPusherJoin(PusherInfo pusherInfo)
- API description: When a new meeting participant enters a room, the other meeting participants in the room will receive this notification. In the callback, you can call addRemoteView to playback the video of this new meeting participant.

- Sample code:

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

- API definition: void onPusherQuit(PusherInfo pusherInfo)
- API description: The other meeting participants in the room will receive this notification when a meeting participant leaves a room. In the callback, you can call deleteRemoteView to stop the video of this meeting participant.
- Sample code:

```
public void onPusherQuit(PusherInfo pusherInfo) {
	......
	mRTCRoom.deleteRemoteView(pusherInfo);
	......
}
```


### 4. onRecvRoomTextMsg

- API definition: void onRecvRoomTextMsg(String roomID, String userID, String userName, String userAvatar, String message)
- API description: When a meeting participant calls sendRoomTextMsg, the other meeting participants in the room will receive this notification.
- Sample code: 

```
public void onRecvRoomTextMsg(String roomid, String userid, String userName, String userAvatar, String message) {
	//do nothing
}
```



### 5. onRecvRoomCustomMsg

- API definition: void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
- API description: When a meeting participant calls sendRoomCustomMsg, the other meeting participants in the room will receive this notification.


### 6. onRoomClosed

- API definition: void onRoomClosed(String roomID)
- API description: When a room is terminated, meeting participants in the room will receive this notification. Exit the room in the callback.
- Sample code:

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

- API definition: void onDebugLog(String log)
- API description: Live room log callback. You can save the logs as a file in the callback, so as to make it easy to analyze problems.
- Sample code:

```
public void onDebugLog(String line) {
   Log.i(TAG,line);
}
```


### 8. onError

- API definition: void onError(int errorCode, String errorMessage)
- API description: Live room error callback
- Sample code:

```
public void onError(final int errorCode, final String errorMessage) {
	 mRTCRoom.exitRoom(null);
    new AlertDialog.Builder(mActivity)
            .setTitle("Live room error")
            .setMessage(errorMessage + "[" + errorCode + "]")
            .setNegativeButton("OK", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    
                }
   				}).show();
}
```

