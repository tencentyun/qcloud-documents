## Feature Description

**LVB+Joint Broadcasting** is an LVB mode commonly used in the **Live Show** and **Online Education** scenarios. With a good applicability to many scenarios, it supports online live broadcasting featuring both high concurrency and low cost, but also enables video chats between VJs and viewers via joint broadcasting.

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/aacdf8cdfa825f64f34af9c3c3e4154e.jpg" />


Tencent Cloud provides "LVB+Joint Broadcasting" by using [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606), a component consisting of Client and Server (both open source). For more information on how to interface with it, please see [DOC](https://cloud.tencent.com/document/product/454/14606). This document displays the API list for Client:

## LiveRoom

| Name | Description |
| :------------------------------------: | :------------------------------: |
| setLiveRoomListener(ILiveRoomListener listener) | Sets liveroom callback |
| login(serverDomain, loginInfo, loginCallback) | Logs in to the RoomService backend |
| logout() | Logs out of the RoomService backend |
| getRoomList(int index, int count, GetRoomListCallback callback) | Gets the room list (optional, you can select your room list.) |
| getAudienceList(String roomID, final GetAudienceListCallback callback) | Gets a list of viewers in a room (a maximum of the last 30 viewers who entered the room are returned.) |
| createRoom(String roomID, String roomInfo, CreateRoomCallback cb) | VJ: Creates a room (roomID can be left blank.) |
| enterRoom(String roomID, TXCloudVideoView videoView, EnterRoomCallback cb) | Viewer: Enters a room |
| exitRoom(ExitRoomCallback callback) | VJ or viewer: Exits a room |
| startLocalPreview(TXCloudVideoView videoView) | VJ or joint broadcasting viewer: Enables camera preview |
| stopLocalPreview() | Disables camera preview |
| requestJoinPusher(int timeout, RequestJoinPusherCallback callback) | Viewer: Sends a joint broadcasting request |``
| joinPusher(final JoinPusherCallback cb) | Viewer: Joins joint broadcasting |
| quitPusher(final QuitPusherCallback cb) | Viewer: Quits joint broadcasting |
| acceptJoinPusher(String userID) | VJ: Accepts a joint broadcasting request from the viewer |
| rejectJoinPusher(String userID, String reason) | VJ: Rejects a joint broadcasting request from the viewer |
| kickoutSubPusher(String userID) | VJ: Kicks a viewer out of joint broadcasting |
| getOnlinePusherList(final GetOnlinePusherListCallback callback) | VJ PK: Gets a list of online VJs |
| startPlayPKStream(final String playUrl, TXCloudVideoView videoView, final PKStreamPlayCallback callback) | VJ PK: Starts playing back each other's video streams |
| stopPlayPKStream() | VJ PK: Stops playing back each other's video streams |
| sendPKRequest(String userID, int timeout, final RequestPKCallback callback) | VJ PK: Sends a PK request |
| sendPKFinishRequest(String userID) | VJ PK: Sends a request to finish PK |
| acceptPKRequest(String userID) | VJ PK: Accepts a PK request |
| rejectPKRequest(String userID, String reason) | VJ PK: Rejects a PK request |
| addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback) | VJ: Plays back the remote video images of the joint broadcasting viewer |
| deleteRemoteView(PusherInfo pusherInfo) | VJ: Removes the remote video images of the joint broadcasting viewer |
| sendRoomTextMsg(String message, SendTextMessageCallback callback) | Sends a text (on-screen comment) message |
| sendRoomCustomMsg(String cmd, String message, SendCustomMessageCallback callback) | Sends a custom message (gives a "Like" or flower) |
| startScreenCapture() | Starts screen capturing (only for Android) |
| stopScreenCapture() | Stops screen capturing (only for Android) |
| switchToBackground() | App switches from foreground to background |
| switchToForeground() | App switches from background to foreground |
| setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel) | Sets beauty filter effects |
| switchCamera() | Switches between front and rear cameras. Dynamic switching is supported during push |
| setMute(mute) | Enables Mute |
| setMirror(enable) | Sets mirroring for images (this API works on the effect at the viewer end only; the VJ end always has the mirroring effect available) |
| playBGM(String path) | Starts background music ("path" indicates the path to the music file) |
| stopBGM() | Stops background music |
| pauseBGM() | Pauses background music |
| resumeBGM() | Resumes background music |
| setMicVolume(x) | Sets microphone volume for audio mixing |
| setBGMVolume(x) | Sets background music volume for audio mixing |
| getMusicDuration(fileName) | Gets background music duration |
| startRecord(recordType) | Starts video recording |
| stopRecord() | Stops video recording |
| setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener) | Sets video recording callback |
| incCustomInfo(fieldName, count) | Increases the custom value (fieldName) of a room |
| decCustomInfo(fieldName, count) | Decreases the custom value (fieldName) of a room |
| updateSelfUserInfo(userName, userAvatar) | Updates user's information of liveroom |
| setPauseImage(bitmap) | Sets the images to be pushed when switching to the background |

## ILiveRoomListener

| Name | Description |
| ------------------------------------- | ------------------- |
| onGetPusherList(pusherList) | Notification: The list of existing pushers in the room (the number of remote video streams) |
| onPusherJoin(pusherInfo) | Notification: A new pusher joined the room (notifies you of addition of a remote video stream) |
| onPusherQuit(pusherInfo) | Notification: A pusher left the room (notifies you of subtraction of a remote video stream) |
| onRecvJoinPusherRequest(userID, userName, userAvatar) | Notification: VJ receives a joint broadcasting request from a viewer |
| onKickOut() | Viewer: Viewer gets notified of being kicked out by the primary VJ |
| onRecvPKRequest(String userID, String userName, String userAvatar, String streamUrl) | Receives a PK request |
| onRecvPKFinishRequest(String userID) | Receives a request to finish PK |
| onRecvRoomTextMsg(roomID, userID, userName, userAvatar, message) | Chat room: Receives a text message |
| onRecvRoomCustomMsg(roomID, userID, userName, userAvatar, cmd, message) | Chat room: Receives a custom message |
| onRoomClosed(roomID) | Notification: Notifies you of the room being closed |
| onDebugLog(log) | LOG: Log callback |
| onError(errorCode, errorMessage) | ERROR: Error callback |



## Details of LiveRoom APIs

### 1. setLiveRoomListener

- API definition: void setLiveRoomListener(ILiveRoomListener listener)
- API description: Sets the ILiveRoomListener callback. For the callback function, please see the ILiveRoomListener API description.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| listener | ILiveRoomListener | A liveroom callback API |

- Sample code:

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
    //The userId is returned upon successful login.
    }
});
```



### 3. logout 

- API definition: void logout();
- API description: Logs out of the RoomService backend
- Sample code:

```
mLiveRoom.logout();
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
mLiveRoom.getRoomList(0, 20, new LiveRoom.GetRoomListCallback() {
    @Override
    public void onSuccess(ArrayList<RoomInfo> data) {
        //For information on each room, please see the definition of RoomInfo.
    }

    @Override
    public void onError(int errCode, String e) {
    }
});
```

### 5. getAudienceList
- API definition: void getAudienceList(String roomID, final GetAudienceListCallback callback)
- API description: Gets the list of viewers in a room and returns only the last 30 viewers who entered the room.


### 6. createRoom

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
	mLiveRoom.createRoom("", roomInfo, new LiveRoom.CreateRoomCallback() {
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

### 7. enterRoom

- API definition: void enterRoom(String roomID, TXCloudVideoView videoView, EnterRoomCallback cb) 

- API description: (Viewer) enters a room.

- Sample code:

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

- API definition: void exitRoom(final ExitRoomCallback callback) 

- API description: VJ (or viewer) exits the room.

- Sample code:

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

- API definition: void startLocalPreview(TXCloudVideoView view) 
- API description: VJ (or joint broadcasting viewer) enables camera preview. The front camera is used by default, and switchCamera is used to switch between front and rear cameras.
- Sample code:

```
TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLiveRoom.startLocalPreview(mCaptureView);
```


### 10. stopLocalPreview

- API definition: void stopLocalPreview()
- API description: VJ (or viewer) disables camera preview.
- Sample code:

```
mLiveRoom.stopLocalPreview();
```


### 11. requestJoinPusher

- API definition: void requestJoinPusher(int timeout, RequestJoinPusherCallback callback)
- API description: This API is called when (viewer) sends a request for joint broadcasting with the VJ.
- Sample code:

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
                Toast.makeText(LivePlayActivity.this, "joint broadcasting failed:" + errInfo, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onSuccess() {
               
            }
        });
    }

    @Override
    public void onReject(String reason) {
        Toast.makeText(LivePlayActivity.this, "VJ rejected your joint broadcasting request", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onTimeOut() {
        Toast.makeText(LivePlayActivity.this, "Joint broadcasting request timed out, and the VJ made no response", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onError(int code, String errInfo) {
        Toast.makeText(LivePlayActivity.this, "Joint broadcasting request failed:" + errInfo, Toast.LENGTH_SHORT).show();
    }
});
```



### 12. joinPusher

- API definition: void joinPusher(final JoinPusherCallback cb)
- API description: (Viewer) begins pushing, and joins joint broadcasting, but whether the joint broadcasting can be successful depends on the callback result of JoinPusherCallback.
- Sample code:

```
mLiveRoom.joinPusher(new LiveRoom.JoinPusherCallback() {
    @Override
    public void onError(int errCode, String errInfo) {
        mLiveRoom.startLocalPreview(videoView);
        Toast.makeText(LivePlayActivity.this, "Joint broadcasting failed:" + errInfo, Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onSuccess() {
       
    }
});
```


### 13. quitPusher
- API definition: void quitPusher(final QuitPusherCallback cb)
- API description: (Viewer) quits joint broadcasting.
- Sample code:

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


### 14. acceptJoinPusher

- API definition: void acceptJoinPusher(String userID)
- API description: (VJ) accepts viewer's request for joint broadcasting.
- Sample code:

```
mLiveRoom.acceptJoinPusher(userId);
```

### 15. rejectJoinPusher

- API definition: void rejectJoinPusher(String userID, String reason)
- API description: (VJ) rejects viewer's request for joint broadcasting.
- Sample code:

```
mLiveRoom.rejectJoinPusher(userId, "");
```

### 16. kickoutSubPusher

- API definition: void kickoutSubPusher(String userID)
- API description: VJ kicks a viewer out of joint broadcasting.
- Sample code:

```
mLiveRoom.kickoutSubPusher(userId);
```

### 17. getOnlinePusherList

- API definition: void getOnlinePusherList(final GetOnlinePusherListCallback callback)
- API description: VJ PK: Gets a list of online VJs.
- Sample code:

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

### 18. startPlayPKStream

- API definition: void startPlayPKStream(final String playUrl, TXCloudVideoView videoView, final PKStreamPlayCallback callback)
- API description: VJ PK: Starts playing each other's streams
- Sample code:

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

### 19. stopPlayPKStream

- API definition: void stopPlayPKStream()
- API description: VJ PK: Stops playing each other's streams
- Sample code:

```
mLiveRoom.stopPlayPKStream()
```

### 20. sendPKRequest

- API definition: void sendPKRequest(String userID, int timeout, final RequestPKCallback callback)
- API description: VJ PK: Sends a PK request
- Sample code:

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

### 21. sendPKFinishRequest

- API definition: void sendPKFinishRequest(String userID)
- API description: VJ PK: Sends a request to end PK
- Sample code:

```
mLiveRoom.sendPKFinishRequest(userID)
```

### 22. acceptPKRequest

- API definition: void acceptPKRequest(String userID)
- API description: VJ PK: Accepts a PK request
- Sample code:

```
 mLiveRoom.acceptPKRequest(userID);
```

### 23. rejectPKRequest

- API definition: void rejectPKRequest(String userID, String reason)
- API description: VJ PK: Rejects a PK request
- Sample code:

```
 mLiveRoom.rejectPKRequest(userID, "");
```

### 24. addRemoteView

- API definition: void addRemoteView(TXCloudVideoView videoView, PusherInfo pusherInfo, RemoteViewPlayCallback callback)
- API description: (VJ) plays the remote video image of a viewer in joint broadcasting. This API is called when onPusherJoin (notification of new viewer joining joint broadcasting) is received.
- Sample code:

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

### 25. deleteRemoteView

- API definition: void deleteRemoteView(final PusherInfo pusherInfo)
- API description: Stops pushing the video stream of a viewer in joint broadcasting. This API is called when onPusherQuit (a viewer quits the joint broadcasting) is received.
- Sample code: 

```
public void onPusherQuit(PusherInfo pusherInfo) {
    ......
    mLiveRoom.deleteRemoteView(pusherInfo);
    ......
}
```

### 26. sendRoomTextMsg

- API definition: void sendRoomTextMsg(@NonNull String message, final SendTextMessageCallback callback)
- API description: Sends a text message. Other members in the room will receive a notification via onRecvRoomTextMsg.
- Sample code: 

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

### 27. sendRoomCustomMsg

- API definition: void sendRoomCustomMsg(@NonNull String cmd, @NonNull String message, final SendCustomMessageCallback callback)
- API description: Sends a custom message. Other members in the room will receive a notification via onRecvRoomCustomMsg.
- Sample code: 

```
mLiveRoom.sendRoomCustomMsg(String.valueOf(TCConstants.IMCMD_DANMU), 
                        "hello ", new LiveRoom.SendCustomMessageCallback() {
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


### 28. startScreenCapture

- API definition: void startScreenCapture()
- API description: Enables screen capturing. Since screencap is implemented based on the native capabilities of the Android system, for security reasons, Android will warn the user before the screencap is initiated by displaying a prompt: "an App will capture all the contents on your screen".

> Note: This API takes effect just on Android API 21. Screencap and camera preview are mutually exclusive, which means only one of them can be effective at a time.

### 29. stopScreenCapture

- API definition: void stopScreenCapture()
- API description: Stops screen capturing.


### 30. switchToBackground

- API definition: void switchToBackground()
- API description: Switches from foreground to background, stops collecting camera data, and pushes default pictures.


### 31. switchToForeground

- API definition: void switchToForeground()
- API description: Switches from background to foreground, and starts collecting camera data.


### 32. setBeautyFilter

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
mLiveRoom.setBeautyFilter(mBeautyStyle, mBeautyLevel, mWhiteningLevel, mRuddyLevel);
```


### 33. switchCamera

- API definition: void switchCamera()
- API description: Switches between cameras. When the front camera is in use, calling this API enables a switch from the front camera to the rear camera, and vice versa. This API takes effect only if it is called after camera preview (startCameraPreview(TXCloudVideoView)) is enabled. The front camera is used by default when the SDK enables camera preview.


### 34. setMute

- API definition: void setMute(mute)
- API description: Enables Mute Once Mute is enabled, the SDK shifts from pushing microphone-collected sounds to pushing mute.
- Parameter description:

| Parameter | Type | Description |
| ---- | ------- | ---- |
| mute | boolean | Whether to enable Mute |


### 35. setMirror

- API definition: void setMirror(boolean enable)
- API description: Sets horizontal mirroring at the viewer end. Note that this API only works on the viewer end, not the VJ (pusher) end. The mirroring effect is always seen from the pusher end. The image is seen as mirrored from the pusher end when the front camera is in use, and non-mirrored when the rear camera is in use.
- Parameter description:

| Parameter | Type | Description |
| ------ | ------- | -------------------------------------- |
| enable | boolean | "true" indicates the image is seen as mirrored, and "false" indicates the image is seen as non-mirrored. |

- Sample code: 

```
//The image is seen as mirrored at the viewer end
mLiveRoom.setMirror(true);
```

### 36. playBGM

- API definition: boolean playBGM(String path)
- API description: Starts background music. This API is used for audio mixing, for example, mixing background music with sounds collected from the microphone for playback. If the playback is successful, a value of "true" is returned. If the playback fails, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ------ | ---------------- |
| path | String | The background music file is located in the absolute path in the phone |


### 37. stopBGM

- API definition: boolean stopBGM()
- API description: Stops background music. If the playback ends successfully, a value of "true" is returned. If the playback fails to end, a value of "false" is returned.

### 38. pauseBGM

- API definition: boolean pauseBGM()
- API description: Pauses background music. If the playback pauses successfully, a value of "true" is returned. If the playback fails to pause, a value of "false" is returned.


### 39. resumeBGM

- API definition: boolean resumeBGM()
- API description: Resumes background music. If the playback resumes successfully, a value of "true" is returned. If the playback fails to resume, a value of "false" is returned.


### 40. setMicVolume

- API definition: boolean setMicVolume(float x)
- API description: Sets microphone volume for audio mixing. If the microphone volume is set successfully, a value of "true" is returned. If the microphone volume fails to be set, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| x | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |



### 41. setBGMVolume

- API definition: boolean setBGMVolume(float x)
- API description: Sets background music volume for audio mixing. If the background music volume is set successfully, a value of "true" is returned. If the background music volume fails to be set, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| x | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |


### 42. getMusicDuration

- API definition: int getMusicDuration(String path)
- API description: Gets background music duration. The returned value is in seconds.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| path | String | Gets the duration of the current music if path == null and the duration of music under the path if path != null |


### 43. startRecord

- API definition: int startRecord(int recordType)
- API description: Starts recording video. This API is used at the viewer end to save the videos the viewers are watching as a local file in real time.
- Note: This API can be called only after the enterRoom operation is successful. Additionally, the generated video files are managed by your application layer code, and the SDK does not clean them.
- If the recording starts successfully, "0" is returned. If the recording is in progress, "-1" is returned. If the pushing has not started and the recording fails to start, "-2" is returned.
- Parameter description:

| Parameter | Type | Description |
| ------------- | ------ | -------------------------------- |
| recordType | int | Recording type, only video-only recording is supported TXRecordCommon.RECORD_TYPE_STREAM_SOURCE |

- Sample code:

```
mLiveRoom.startRecord(TXRecordCommon.RECORD_TYPE_STREAM_SOURCE);
```

### 44. stopRecord

- API definition: int stopRecord()
- API description: Stops recording video. The recording result is asynchronously notified by means of recording callback.


### 45. setVideoRecordListener

- API definition: void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)
- API description: Sets video recording callback to receive the video recording progress and result.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------------------------- | ------ |
| listener | TXRecordCommon.ITXVideoRecordListener | Video recording callback |

- Sample code:

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

### 46. incCustomInfo

- API definition: void incCustomInfo(String fieldName, int count)
- API description: Increases the custom fieldName count. This API is used to count the number of "likes", gifts, and others of a room. The cumulative values can be obtained from the "custom" field of the "roominfo" parameter.
- Parameter description:

| Parameter | Type | Description |
| ------------- | ------ | -------------------------------- |
| fieldName | String | Field name that requires counting |
| count | int | Increment value for each count, which is typically 1 |

- Sample code:

```
mLiveRoom.incCustomInfo("praise",1); 
```

### 47. decCustomInfo

- API definition: void decCustomInfo(String fieldName, int count)
- API description: Decreases the custom fieldName count. This API is used to count the number of "likes", gifts, and others of a room. The cumulative values can be obtained from the "custom" field of the "roominfo" parameter.
- Parameter description:

| Parameter | Type | Description |
| ------------- | ------ | -------------------------------- |
| fieldName | String | Field name that requires counting |
| count | int | Decrement value for each count, which is typically 1 |


### 48. updateSelfUserInfo

- API definition: void updateSelfUserInfo(String userName, String userAvatar)
- API description: Updates the nickname and profile photo of a new user. This API is used to update the liveroom information in real time after the nickname and profile photo of a user are modified


### 49. setPauseImage

- API definition: void setPauseImage(Bitmap bitmap)
- API description: Sets the images to be pushed when switching from foreground to background.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| bitmap | Bitmap | Background image bitmap |


## Details of ILiveRoomListener APIs

### 1. onGetPusherList

- API definition: void onGetPusherList(List<PusherInfo> pusherList)
- API description: The list of existing pushers in the room (the number of remote video streams). New viewers will receive this notification when they enter the room. In the callback, you can call addRemoteView to playback the video of an existing viewer in the room.

- Sample code:

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

- API definition: void onPusherJoin(PusherInfo pusherInfo)
- API description: When a new viewer enters a room, the primary VJ and other viewers will receive this notification. In the callback, you can call addRemoteView to playback the video of this new viewer.

- Sample code:

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

- API definition: void onPusherQuit(PusherInfo pusherInfo)
- API description: The primary VJ and other viewers will receive this notification when a viewer exits the room. In the callback, you can call deleteRemoteView to stop playing back the video of this viewer.
- Sample code:

```
public void onPusherQuit(PusherInfo pusherInfo) {
	......
	mLiveRoom.deleteRemoteView(pusherInfo);
	......
}
```


### 4. onRecvJoinPusherRequest

- API definition: void onRecvJoinPusherRequest(String userID, String userName, String userAvatar)
- API description: The VJ receives this notification when a viewer requests joint broadcasting with this VJ. The VJ can either accept (acceptJoinPusher) or reject (rejectJoinPusher) the request in the callback.
- Sample code:

```
public void onRecvJoinPusherRequest(final String userId, String userName, String userAvatar) {
    final AlertDialog.Builder builder = new AlertDialog.Builder(mActivity)
		.setCancelable(true)
		.setTitle("Prompt")
		.setMessage(userName + "initiated a joint broadcasting request with you")
		.setPositiveButton("Accept", new DialogInterface.OnClickListener() {
		    @Override
		    public void onClick(DialogInterface dialog, int which) {
		        mLiveRoom.acceptJoinPusher(userId);
		        dialog.dismiss();
		    }
		})
		.setNegativeButton("Reject", new DialogInterface.OnClickListener() {
		    @Override
		    public void onClick(DialogInterface dialog, int which) {
		        mLiveRoom.rejectJoinPusher(userId, "VJ rejected your joint broadcasting request");
		        dialog.dismiss();
		    }
	});
}
```

### 5. onKickOut

- API definition: void onKickOut()
- API description: The viewer will receive this notification when he/she is kicked out of joint broadcasting by the VJ. In the callback, you can stop local preview and exit the live room.
- Sample code: 

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

- API definition: void onRecvPKRequest(String userID, String userName, String userAvatar, String streamUrl)
- API description: When a VJ calls sendPKRequest to send a PK request to another VJ, the another VJ will receive this callback notification. In this callback, you can display a pop-up window indicating the reception of a PK request and asking the user whether he/she will accept or reject it.
- Sample code:

```
@Override
public void onRecvPKRequest(final String userID, final String userName, final String userAvatar, final String streamUrl){
     final AlertDialog.Builder builder = new AlertDialog.Builder(mActivity)
            .setCancelable(true)
            .setTitle("Prompt")
            .setMessage(userName + "initiated a PK request with you")
            .setPositiveButton("Accept", new DialogInterface.OnClickListener() {
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
            .setNegativeButton("Reject", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    mLiveRoom.rejectPKRequest(userID, "VJ rejected your PK request");
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

- API definition: void onRecvPKFinishRequest(String userID)
- API description: When a VJ calls sendPKFinishRequest to notify another VJ that the PK has ended, the another VJ will receive this callback notification. In this callback, call stopPlayPKStream to end the PK and perform clean-up.
- Sample code:

```
@Override
public void onRecvPKFinishRequest(final String userID){
    mLiveRoom.stopPlayPKStream();
}
```

### 8. onRecvRoomTextMsg

- API definition: void onRecvRoomTextMsg(String roomID, String userID, String userName, String userAvatar, String message)
- API description: When sendRoomTextMsg is called at the VJ or viewer end, the VJ or viewers in the room will receive this notification.
- Sample code: 

```
public void onRecvRoomTextMsg(String roomid, String userid, String userName, String userAvatar, String message) {
	//do nothing
}
```



### 9. onRecvRoomCustomMsg

- API definition: void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
- API description: When sendRoomCustomMsg is called at the VJ or viewer end, the VJ or viewers in the room will receive this notification.

### 10. onRoomClosed

- API definition: void onRoomClosed(String roomID)
- API description: When a room is terminated, viewers in the room will receive this notification. Exit the room in the callback.
- Sample code:

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

- API definition: void onDebugLog(String log)
- API description: Live room log callback. You can save the logs as a file in the callback, so as to make it easy to analyze problems.
- Sample code:

```
public void onDebugLog(String line) {
   Log.i(TAG,line);
}
```


### 12. onError

- API definition: void onError(int errorCode, String errorMessage)
- API description: Live room error callback
- Sample code:

```
public void onError(final int errorCode, final String errorMessage) {
	 mLiveRoom.exitRoom(null);
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

