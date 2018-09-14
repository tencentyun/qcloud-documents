## Feature Overview

**LVB+Joint Broadcasting** is an LVB mode commonly used in the **Live Show** and **Online Education** scenarios. With a good applicability to many scenarios, it supports online live broadcasting featuring both high concurrency and low cost, but also enables video chats between VJs and viewers via joint broadcasting.

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/aacdf8cdfa825f64f34af9c3c3e4154e.jpg" />


Tencent Cloud implements "LVB+Joint Broadcasting" by using the component [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606), which involves Client and Server (available at an open-source basis on both). For more information on how to interface with the Client and Server, please see [DOC](https://cloud.tencent.com/document/product/454/14606). This document describes the APIs for Client:

## LiveRoom

| Name | Description |
| :------------------------------------: | :------------------------------: |
| LiveRoomListener | liveroom callback |
| - (void)login:(NSString*)serverDomain loginInfo:(LoginInfo *)loginInfo withCompletion:(ILoginCompletionHandler)completion;             | Logs in to the RoomService backend |
| - (void) logout: (ILogoutCompletionHandler) completion | Logs out of the RoomService backend |
| - (void) getRoomList: (int) index cnt: (int) cnt withCompletion: (IGetRoomListCompletionHandler) completion | Gets the room list (optional, you can select your room list.) |
| - (void)getAudienceList:(NSString *)roomID  withCompletion:(IGetAudienceListCompletionHandler)completion | Gets a list of viewers in a room (a maximum of the last 30 viewers who entered the room are returned.) |
| - (void) createRoom: (NSString *) roomID roomInfo: (NSString *) roomInfo withCompletion: (ICreateRoomCompletionHandler) completion | VJ: Creates a room (roomID can be left blank.) |
| - (void) enterRoom: (NSString *) roomID withView: (UIView *) view withCompletion: (IEnterRoomCompletionHandler) completion | Viewer: Enters a room |
| - (void) exitRoom: (IExitRoomCompletionHandler) completion | VJ or viewer: Exits a room |
| - (void) startLocalPreview: (UIView *) view | VJ or joint broadcasting viewer: Enables camera preview |
| - (void) stopLocalPreview | Disables camera preview |
| - (void) requestJoinPusher: (NSInteger) timeout withCompletion: (IRequestJoinPusherCompletionHandler) completion | Viewer: Initiates a joint broadcasting request |
| - (void) joinPusher: (IJoinPusherCompletionHandler) completion | Viewer: Joins joint broadcasting |
| - (void) quitPusher: (IQuitPusherCompletionHandler) completion | Viewer: Quits joint broadcasting |
| - (void) acceptJoinPusher: (NSString *) userID | VJ: Accepts a joint broadcasting request from the viewer |
| - (void) rejectJoinPusher: (NSString *) userID reason: (NSString *) reason | VJ: Rejects a joint broadcasting request from the viewer |
| - (void) kickoutSubPusher: (NSString *) userID | VJ: Kicks a viewer out of joint broadcasting |
| - (void) getOnlinePusherList: (IGetOnlinePusherListCompletionHandler) completion | VJ PK: Gets a list of online VJs |
| - (void) startPlayPKStream: (NSString *) playUrl view: (UIView *) view playBegin: (IPlayBegin) playBegin playError: (IPlayError) playError| VJ PK: Starts playing back each other's video streams |
| - (void) stopPlayPKStream | VJ PK: Stops playing back each other's video streams |
| - (void) sendPKReques: (NSString *) userID timeout: (NSInteger) timeout withCompletion: (IRequestPKCompletionHandler) completion | VJ PK: Sends a PK request |
| - (void) sendPKFinishRequest: (NSString *) userID | VJ PK: Sends a request to finish PK |
| - (void) acceptPKRequest: (NSString *) userID | VJ PK: Accepts a PK request |
| - (void) rejectPKRequest: (NSString *) userID reason: (NSString *) reason | VJ PK: Rejects a PK request |
| - (void) addRemoteView: (UIView *) view withUserID: (NSString *) userID playBegin: (IPlayBegin) playBegin playError: (IPlayError) playError | VJ: Plays remote video image of a viewer in joint broadcasting |
| - (void) deleteRemoteView: (NSString *) userID | VJ: Removes the remote video images of the joint broadcasting viewer |
| - (void) sendRoomTextMsg: (NSString *) textMsg | Sends a text (on-screen comment) message |
| - (void) sendRoomCustomMsg: (NSString *) cmd msg: (NSString *) msg | Sends a custom message (gives a "Like" or flower) |
| - (void) switchToBackground: (UIImage *) pauseImage | App switches from foreground to background |
| - (void) switchToForeground | App switches from background to foreground |
| - (void) setBeautyStyle: (int) beautyStyle beautyLevel: (float) beautyLevel whitenessLevel: (float) whitenessLevel ruddinessLevel: (float) ruddinessLevel | Sets beauty filter |
| - (void) switchCamera | Switches between front and rear cameras. Dynamic switching is supported during push |
| - (void) setMute: (BOOL) isMute | Enables Mute |
| - (void) setMirror: (BOOL) isMirror | Sets mirroring for images (this API works on the effect at the viewer end only; the VJ end always has the mirroring effect available) |
| - (BOOL) playBGM: (NSString *) path | Starts background music ("path" must be the one under the document directory corresponding to the app) |
| - (BOOL) stopBGM | Stops background music |
| - (BOOL) pauseBGM | Pauses background music |
| - (BOOL) resumeBGM | Resumes background music |
| - (BOOL) setMicVolume: (float) volume | Sets microphone volume for audio mixing |
| - (BOOL) setBGMVolume: (float) volume | Sets background music volume for audio mixing |
| - (void) startRecord | Starts video recording |
| - (void) stopRecord | Stops video recording |
| TXLiveRecordListener | Video recording callback |

## LiveRoomListener

| Name | Description |
| ------------------------------------- | ------------------- |
| - (void) onGetPusherList: (NSArray<PusherInfo *> *) pusherInfoArray | Notification: The list of existing pushers in the room (the number of remote video streams) |
| - (void) onPusherJoin: (PusherInfo *) pusherInfo | Notification: A new pusher joined the room (notifies you of addition of a remote video stream) |
| - (void) onPusherQuit: (PusherInfo *) pusherInfo | Notification: A pusher left the room (notifies you of subtraction of a remote video stream) |
| - (void) onRecvJoinPusherRequest: (NSString *) userID nickName: (NSString *) nickName headPic: (NSString *) headPic | Notification: VJ receives a joint broadcasting request from a viewer |
| - (void) onKickout | Viewer: Viewer gets notified of being kicked out by the primary VJ |
| - (void) onRecvPKRequest: (NSString *) userID userName: (NSString *) userName userAvatar: (NSString *) userAvatar streamUrl: (NSString *) streamUrl | Receives a PK request |
| - (void) onRecvPKFinishRequest: (NSString *) userID | Receives a request to finish PK |
| - (void) onRecvRoomTextMsg: (NSString *) roomID userID: (NSString *) userID nickName: (NSString *) nickName headPic: (NSString *) headPic textMsg: (NSString *) textMsg | Chat room: Receives a text message |
| - (void) onRecvRoomCustomMsg: (NSString *) roomID userID: (NSString *) userID nickName: (NSString *) nickName headPic: (NSString *) headPic cmd: (NSString *) cmd msg: (NSString *) msg | Chat room: Receives a custom message |
| - (void) onRoomClose: (NSString *) roomID | Notification: Notifies you of the room being closed |
| - (void) onDebugMsg: (NSString *) msg | LOG: Log callback |
| - (void) onError: (int) errCode errMsg: (NSString *) errMsg | ERROR: Error callback |



## Details of LiveRoom APIs

### 1. setLiveRoomListener

- API definition: @property (nonatomic, weak) id < LiveRoomListener > delegate;
- API description: Sets the LiveRoomListener proxy callback. For the callback function, please refer to the LiveRoomListener API description.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| delegate | LiveRoomListener | A liveroom callback API |

- Sample code:

```
self.liveRoom.delegate = self(Callback listener)
```

### 2. login

-  API definition: - (void) login: (NSString*) serverDomain loginInfo: (LoginInfo *) loginInfo withCompletion: (ILoginCompletionHandler) completion 
- API description: Logs in to the RoomService backend. You can specify whether to use the Tencent Cloud RoomService or the user-deployed RoomService.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| serverDomain | String | Server address of RoomService. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| loginInfo | LoginInfo | The login parameter. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| completion | ILoginCompletionHandler | Callback to verify whether the login is successful |

- Sample code:

```
  LoginInfo* initInfo = [LoginInfo new];
  initInfo.sdkAppID = sdkAppID;
  initInfo.userID = username;
  initInfo.headPicUrl = @"";
  initInfo.userSig = sign;
  initInfo.accType = accountType;
  [self.liveRoom login:kHttpServerAddrDomain loginInfo:initInfo withCompletion:^(int errCode, NSString *errMsg) {
     NSLog(@"errCode:%d, errMsg:%@", errCode, errMsg);
     if (errCode == ROOM_SUCCESS) {
            succ(username, hashPwd);
     }
     else {
            fail(errCode, errMsg);
     }
  }];
```



### 3. logout 

- API definition: - (void) logout: (ILogoutCompletionHandler) completion
- API description: Logs out of the RoomService backend
- Sample code:

```
  [self.liveRoom logout:^(int errCode, NSString *errMsg) {
     // to do
  }];
```


### 4. getRoomList

- API definition: - (void) getRoomList: (int) index cnt: (int) cnt withCompletion: (IGetRoomListCompletionHandler) completion
- API description: Pulls the room list. The parameters index and cnt are used to handle paging, which means you can pull "cnt" rooms from the room numbered "index". Call of this API is not required. If you already have your own room list, you can continue to use it.

- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| index | int | From which room the pulling begins |
| cnt | int | Number of rooms to be returned via RoomService |
| completion | IGetRoomListCompletionHandler | Callback of pulling a room list |

- Sample code:

```
//The pulling begins from the number 0, and ends when 20 rooms are pulled.
 [self.liveRoom getRoomList:0 cnt:20 withCompletion:^(int errCode, NSString *errMsg, 
                                                      NSArray<RoomInfo *> *roomInfoArray) {
    if (errCode == 0) {
        //Pull operation successful         
     } else {
        //Pull operation failed
     }
 }];
```

### 5. getAudienceList 
- API definition: - (void) getAudienceList: (NSString *) roomID withCompletion: (IGetAudienceListCompletionHandler) completion
- API description: Gets the list of viewers in a room. Only the last 30 viewers who entered the room are returned.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| roomID | NSString | roomID |
| completion | IGetAudienceListCompletionHandler | Callback of pulling the list of viewers in a room |
- Sample code:

```
  //Gets the list of viewers in a room
  [_liveRoom getAudienceList: roomID withCompletion:^(int errCode, NSString *errMsg,
	                                    NSArray<AudienceInfo *> *audienceInfoArray) {
       // to do 
  }];
```
"audienceInfoArray" is an array of viewer information whose structure is defined as follows:

```
// General viewer information
@interface AudienceInfo : NSObject
  @property (nonatomic, copy)   NSString*   userID;
  @property (nonatomic, copy)   NSString*   userInfo;
@end
```
  

### 6. createRoom

- API definition: - (void) createRoom: (NSString *) roomID roomInfo: (NSString *) roomInfo withCompletion: (ICreateRoomCompletionHandler) completion 
- API description: Creates a room at RoomService backend.
- Parameter description:

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| roomID | String | You can specify an ID for a new room with the parameter roomID, or leave it unspecified. If you do not specify an ID for the room, RoomService will automatically create a new roomID and return it to you through ICreateRoomCompletionHandler. |
| roomInfo | String | To be customized by the creator. This information is returned via getRoomList |
| completion | ICreateRoomCompletionHandler | Creates room creation result callback |

- Sample code:

```
  [self.liveRoom createRoom:@"" roomInfo:@"Room creator information" withCompletion:^(int errCode, NSString *errMsg) {
     NSLog(@"createRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
  }];
```

### 7. enterRoom

- API definition: - (void)enterRoom:(NSString *)roomID withView:(UIView *)view withCompletion:(IEnterRoomCompletionHandler)completion 

- API description: (Viewer) enters a room.

- Sample code:

```
  [_liveRoom enterRoom:groupid withView:videoParentView withCompletion:^(int errCode, NSString *errMsg) {
     NSLog(@"enterRoom: errCode[%d] errMsg[%@]", errCode, errMsg);    
  }];
```

### 8. exitRoom

- API definition: - (void)exitRoom:(IExitRoomCompletionHandler)completion 

- API description: VJ (or viewer) exits a room.

- Sample code:

```
  [self.liveRoom exitRoom:^(int errCode, NSString *errMsg) {
      NSLog(@"exitRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
  }];
```


### 9. startLocalPreview

- API definition: - (void)startLocalPreview:(UIView *)view
- API description: VJ (or joint broadcasting viewer) enables camera preview. The front camera is used by default, and switchCamera is used to switch between front and rear cameras.
- Sample code:

```
  [self.liveRoom startLocalPreview:videoParentView];
```


### 10. stopLocalPreview

- API definition: - (void)stopLocalPreview
- API description: VJ (or viewer) disables camera preview.
- Sample code:

```
  [self.liveRoom stopLocalPreview]; 
```


### 11. requestJoinPusher

- API definition: - (void)requestJoinPusher:(NSInteger)timeout withCompletion:(IRequestJoinPusherCompletionHandler)completion
- API description: This API is called when (viewer) sends a request for joint broadcasting with the VJ.
- Sample code:

```
  [self.liveRoom requestJoinPusher:20 withCompletion:^(int errCode, NSString *errMsg) {
     if (errCode == 0) {
        [TCUtil toastTip:@"VJ accepts your joint broadcasting request, and connection begins to be established" parentView:self.view];      
     }
     else {
        [TCUtil toastTip:errMsg parentView:self.view];
     }
  }];
```



### 12. joinPusher

- API definition: - (void)joinPusher:(IJoinPusherCompletionHandler)completion
- API description: (Viewer) begins pushing, and joins joint broadcasting, but whether the joint broadcasting can be successful depends on the callback result of IJoinPusherCompletionHandler.
- Sample code:

```
  [self.liveRoom joinPusher:^(int errCode, NSString *errMsg) {
      //Joint broadcasting result callback
   }];
```


### 13. quitPusher
- API definition: - (void)quitPusher:(IQuitPusherCompletionHandler)completion
- API description: (Viewer) quits joint broadcasting.
- Sample code:

```
  [self.liveRoom quitPusher:^(int errCode, NSString *errMsg) {
      //Joint broadcasting quitting result callback
  }];
```


### 14. acceptJoinPusher

- API definition: - (void)acceptJoinPusher:(NSString *)userID
- API description: (VJ) accepts viewer's request for joining joint broadcasting.
- Sample code:

```
  [self.liveRoom acceptJoinPusher: userID];
```

### 15. rejectJoinPusher

- API definition: - (void)rejectJoinPusher:(NSString *)userID reason:(NSString *)reason
- API description: (VJ) rejects viewer's request for joining joint broadcasting.
- Sample code:

```
  [self.liveRoom rejectJoinPusher:userID reason:@"Maximum number of joint broadcasting viewers at the VJ end is reached"];
```

### 16. kickoutSubPusher

- API definition: - (void)kickoutSubPusher:(NSString *)userID
- API description: VJ kicks a viewer out of joint broadcasting.
- Sample code:

```
  [self.liveRoom kickoutSubPusher:userID];
```

### 17. getOnlinePusherList

- API definition: - (void)getOnlinePusherList:(IGetOnlinePusherListCompletionHandler)completion
- API description: VJ PK: Gets a list of online VJs.
- Sample code:

```
[_liveRoom getOnlinePusherList:^(NSArray<PusherInfo *> *pusherInfoArray) {

}];
```

### 18. startPlayPKStream

- API definition: - (void)startPlayPKStream:(NSString *)playUrl view:(UIView *)view playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError
- API description: VJ PK: Starts playing each other's streams
- Sample code:

```
[_liveRoom startPlayPKStream:playUrl view:playerView playBegin:^{

} playError:^(int errCode, NSString *errMsg) {

 }];
```

### 19. stopPlayPKStream

- API definition: - (void)stopPlayPKStream
- API description: VJ PK: Stops playing each other's streams
- Sample code:

```
[_liveRoom stopPlayPKStream];
```

### 20. sendPKRequest

- API definition: - (void)sendPKReques:(NSString *)userID timeout:(NSInteger)timeout withCompletion:(IRequestPKCompletionHandler)completion
- API description: VJ PK: Sends a PK request
- Sample code:

```
 [_liveRoom sendPKReques:userID timeout:10 withCompletion:^(int errCode, NSString *errMsg, NSString *streamUrl) {
            
}];
```

### 21. sendPKFinishRequest

- API definition: - (void)sendPKFinishRequest:(NSString *)userID
- API description: VJ PK: Sends a request to end PK
- Sample code:

```
[_liveRoom sendPKFinishRequest:userID];
```

### 22. acceptPKRequest

- API definition: - (void)acceptPKRequest:(NSString *)userID
- API description: VJ PK: Accepts a PK request
- Sample code:

```
[_liveRoom acceptPKRequest:userID];
```

### 23. rejectPKRequest

- API definition: - (void)rejectPKRequest:(NSString *)userID reason:(NSString *)reason
- API description: VJ PK: Rejects a PK request
- Sample code:

```
[_liveRoom rejectPKRequest];
```

### 24. addRemoteView

- API definition: - (void)addRemoteView:(UIView *)view withUserID:(NSString *)userID playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError
- API description: (VJ) plays the remote video image of a viewer in joint broadcasting. This API is called when onPusherJoin (notification of new viewer joining joint broadcasting) is received.
- Sample code:

```
- (void)onPusherJoin:(PusherInfo *)pusherInfo
{
    NSString* userID = pusherInfo.userID;
    NSString* strPlayUrl = pusherInfo.playUrl;
    if (userID == nil || strPlayUrl == nil) {
        return;
    }
    __weak typeof(self) weakSelf = self;
    [self.liveRoom addRemoteView:videoView withUserID:userID playBegin:^{
        //Playback successful
    } playError:^(int errCode, NSString *errMsg) {
        //Playback failed
    }];
}
```

### 25. deleteRemoteView

- API definition: - (void)deleteRemoteView:(NSString *)userID
- API description: Stops pushing the video stream of a viewer in joint broadcasting. This API is called when onPusherQuit (a viewer quits the joint broadcasting) is received.
- Sample code: 

```
  [self.liveRoom deleteRemoteView:userID];
```

### 26. sendRoomTextMsg

- API definition: - (void)sendRoomTextMsg:(NSString *)textMsg
- API description: Sends a text message. Other members in the room will receive a notification via onRecvRoomTextMsg.
- Sample code: 

```
  [[TCLiveRoomMgr getSharedLiveRoom] sendRoomTextMsg:textMsg];
```

### 27. sendRoomCustomMsg

- API definition: - (void)sendRoomCustomMsg:(NSString *)cmd msg:(NSString *)msg;
- API description: Sends a custom message. Other members in the room will receive a notification via onRecvRoomCustomMsg.
- Sample code: 

```
  [[TCLiveRoomMgr getSharedLiveRoom] sendRoomCustomMsg:[@(TCMsgModelType_DanmaMsg) stringValue] msg:textMsg];
```

### 28. switchToBackground

- API definition: - (void)switchToBackground:(UIImage *)pauseImage
- API description: Switches from foreground to background, stops collecting camera data, and pushes default pictures.


### 29. switchToForeground

- API definition: - (void)switchToForeground
- API description: Switches from background to foreground, and starts collecting camera data.


### 30. setBeautyStyle

- API definition: - (void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel
- API description: Sets beauty filter style, dermabrasion level, whitening level, and blushing level.
- Parameter description:

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| beautyStyle | int | Dermabrasion style: 0: Smooth 1: Natural 2: Hazy |
| beautyLevel | int | Dermabrasion level: Value range: 0-9. 0 means disabling beauty filter. Default is 0, i.e., disabling beauty filter |
| whitenessLevel | int | Whitening level: Value range: 0-9. 0 means disabling whitening. Default is 0, i.e., disabling whitening |
| ruddinessLevel     | int  | Blushing level: Value range: 0-9. 0 means disabling blushing. Default is 0, i.e., disabling blushing |

- Sample code:
  
```
   [self.liveRoom setBeautyStyle:0 beautyLevel:_beauty_level whitenessLevel:_whitening_level ruddinessLevel:0];
```


### 31. switchCamera

- API definition: - (void)switchCamera
- API description: Switches between cameras. When the front camera is in use, calling this API enables a switch from the front camera to the rear camera, and vice versa. This API takes effect only if it is called after camera preview (startLocalPreview) is enabled. The front camera is used by default when the SDK enables camera preview.


### 32. setMute

- API definition: - (void)setMute:(BOOL)isMute
- API description: Enables Mute Once Mute is enabled, the SDK shifts from pushing microphone-collected sounds to pushing mute.
- Parameter description:

| Parameter | Type | Description |
| ---- | ------- | ---- |
| isMute | BOOL | Whether to enable Mute |


### 33. setMirror

- API definition: - (void)setMirror:(BOOL)isMirror
- API description: Sets horizontal mirroring at the viewer end. Note that this API only works on the viewer end, not the VJ (pusher) end. The mirroring effect is always seen from the pusher end. The image is seen as mirrored from the pusher end when the front camera is in use, and non-mirrored when the rear camera is in use.
- Parameter description:

| Parameter | Type | Description |
| ------ | ------- | -------------------------------------- |
| isMirror | BOOL | "YES" indicates the image is seen as mirrored, and "false" indicates the image is seen as non-mirrored. |

- Sample code: 

```
  //The image is seen as mirrored at the viewer end
  [self.liveRoom setMirror:YES];
```

### 34. playBGM

- API definition: - (BOOL)playBGM:(NSString *)path
- API description: Starts background music. This API is used for audio mixing, for example, mixing background music with sounds collected from the microphone for playback. If the playback is successful, a value of "true" is returned. If the playback fails, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ------ | ---------------- |
| path | NSString | The path to the background music under the document directory corresponding to the app |


### 35. stopBGM

- API definition: - (BOOL)stopBGM
- API description: Stops background music. If the playback ends successfully, a value of "YES" is returned. If the playback fails to end, a value of "NO" is returned.

### 36. pauseBGM

- API definition: - (BOOL)pauseBGM
- API description: Pauses background music. If the playback pauses successfully, a value of "YES" is returned. If the playback fails to pause, a value of "NO" is returned.


### 37. resumeBGM

- API definition: - (BOOL)resumeBGM
- API description: Resumes background music. If the playback resumes successfully, a value of "YES" is returned. If the playback fails to resume, a value of "NO" is returned.


### 38. setMicVolume

- API definition: - (BOOL)setMicVolume:(float)volume
- API description: Sets microphone volume for audio mixing. If the microphone volume is set successfully, a value of "true" is returned. If the microphone volume fails to be set, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| volume | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |

### 39. setBGMVolume

- API definition: - (BOOL)setBGMVolume:(float)volume
- API description: Sets background music volume for audio mixing. If the background music volume is set successfully, a value of "true" is returned. If the background music volume fails to be set, a value of "false" is returned.
- Parameter description:

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| volume | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |

### 40. startRecord

- API definition: - (void)startRecord
- API description: Starts recording video. This API is used at the viewer end to save real-time videos as a local file.
- Note: This API must be called after enterRoom is successful.
- If the recording starts successfully, "0" is returned. If the recording is in progress, "-1" is returned. If videoRecorder initialization fails, "-2" is returned.
- Sample code:

```
  [self.liveRoom startRecord];
```

### 41. stopRecord

- API definition: - (void)stopRecord
- API description: Stops recording video. The recording result is asynchronously notified by means of recording callback.


### 42. TXLiveRecordListener

- API definition: @property (nonatomic, weak) id < TXLiveRecordListener > recordDelegate
- API description: Sets video recording callback to receive the video recording progress and result.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------------------------- | ------ |
| recordDelegate | TXLiveRecordListener | Video recording callback |

- Sample code:

```
  self.liveRoom.recordDelegate = self;
  -(void) onRecordProgress:(NSInteger)milliSecond
  {
    if (!_videoRecordView.hidden) {
        float progress = (milliSecond/1000)/kMaxRecordDuration;
        [_videoRecordView setVideoRecordProgress:progress];
    }
  }

  -(void) onRecordComplete:(TXRecordResult*)result
  {
    if (_isResetVideoRecord) return;
    
    if (result.retCode == RECORD_RESULT_FAILED || result.retCode == RECORD_RESULT_OK_INTERRUPT) 
		{
        [TCUtil toastTip:result.descMsg parentView:self.view];
    } else {
        TCVideoPublishController *vc = [[TCVideoPublishController alloc] init:[TXLivePlayer new]
				           recordType:kRecordType_Play RecordResult:result TCLiveInfo:self.liveInfo];
        [self.navigationController pushViewController:vc animated:true];
    }
  }
```


## Details of LiveRoomListener APIs

### 1. onGetPusherList

- API definition: - (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray
- API description: The list of existing pushers in the room (the number of remote video streams). New viewers will receive this notification when they enter the room. In the callback, you can call addRemoteView to playback the video of an existing viewer in the room.

- Sample code:

```
- (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray {
    for (PusherInfo *pusherInfo in pusherInfoArray) {
        [_liveRoom addRemoteView:playerView withUserID:pusherInfo.userID playBegin:^{
                
        } playError:^(int errCode, NSString *errMsg) {
						
        }];
    }
}
```

### 2. onPusherJoin

- API definition: - (void)onPusherJoin:(PusherInfo *)pusherInfo
- API description: When a new viewer enters a room, the primary VJ and other viewers will receive this notification. In the callback, you can call addRemoteView to playback the video of this new viewer.

- Sample code:

```
- (void)onPusherJoin:(PusherInfo *)pusherInfo
{
    NSString* userID = pusherInfo.userID;
    NSString* strPlayUrl = pusherInfo.playUrl;
    if (userID == nil || strPlayUrl == nil) {
        return;
    }
    __weak typeof(self) weakSelf = self;
    [self.liveRoom addRemoteView:item.videoView withUserID:userID playBegin:^{
        //to do
    } playError:^(int errCode, NSString *errMsg) {
        //to do
    }];
}
```

### 3. onPusherQuit

- API definition: - (void)onPusherQuit:(PusherInfo *)pusherInfo
- API description: The primary VJ and other viewers will receive this notification when a viewer exits the room. In the callback, you can call deleteRemoteView to stop playing back the video of this viewer.
- Sample code:

```
- (void)onPusherQuit:(PusherInfo *)pusherInfo
{
    NSString* userID = pusherInfo.userID;
    //Stream mixing: Subtracts one stream
    [self.liveRoom deleteRemoteView:userID];
}
```


### 4. onRecvJoinPusherRequest

- API definition: - (void)onRecvJoinPusherRequest:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic
- API description: The VJ receives this notification when a viewer requests joint broadcasting with this VJ. The VJ can either accept (acceptJoinPusher) or reject (rejectJoinPusher) the request in the callback.
- Sample code:

```
- (void)onRecvJoinPusherRequest:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic
{
    if ([_setLinkMemeber count] >= MAX_LINKMIC_MEMBER_SUPPORT) {
        [TCUtil toastTip:@"Maximum number of joint broadcasting viewers at the VJ end is reached" parentView:self.view];
        [self.liveRoom rejectJoinPusher:userID reason:@"Maximum number of joint broadcasting viewers at the VJ end is reached"];
    }
    else if (_userIdRequest && _userIdRequest.length > 0) {
        [TCUtil toastTip:@"Please wait. The VJ is processing another joint broadcasting request." parentView:self.view];
        [self.liveRoom rejectJoinPusher:userID reason:@"Please wait. The VJ is processing another joint broadcasting request."];
    }
    else {
        //Accepts joint broadcasting
        _userIdRequest = userID;
        [self.liveRoom acceptJoinPusher:_userIdRequest];
    }
}
```

### 5. onKickOut

- API definition: - (void)onKickout
- API description: The viewer will receive this notification when he/she is kicked out of joint broadcasting by the VJ. In the callback, you can stop local preview and exit the live room.
- Sample code: 

```
- (void)onKickout
{
    [TCUtil toastTip:@"Sorry, you are kicked out by VJ." parentView:self.view];
    [self.liveRoom stopLocalPreview];
}
```

### 6. onRecvPKRequest

- API definition: - (void)onRecvPKRequest:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar streamUrl:(NSString *)streamUrl
- API description: When a VJ calls sendPKRequest to send a PK request to another VJ, the another VJ will receive this callback notification. In this callback, you can display a pop-up window indicating the reception of a PK request and asking the user whether he/she will accept or reject it.
- Sample code:

```
- (void)onRecvPKRequest:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar streamUrl:(NSString *)streamUrl {
    NSString *msg = [NSString stringWithFormat:@"[%@]RequestPK", userName];
    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"Prompt" message:msg preferredStyle:UIAlertControllerStyleAlert];
    [alertController addAction:[UIAlertAction actionWithTitle:@"Reject" style:UIAlertActionStyleDefault handler:^(UIAlertAction * _Nonnull action) {
        [_liveRoom rejectPKRequest:userID reason:@"The VJ rejected your PK request"];
    }]];
    [alertController addAction:[UIAlertAction actionWithTitle:@"Accept" style:UIAlertActionStyleDefault handler:^(UIAlertAction * _Nonnull action) {
        [_liveRoom acceptPKRequest:userID];
        [_liveRoom startPlayPKStream:playUrl view:playerView playBegin:^{

        } playError:^(int errCode, NSString *errMsg) {

        }];
    }]];
        
    [self.navigationController presentViewController:alertController animated:YES completion:nil];
}
```

### 7. onRecvPKFinishRequest

- API definition: - (void)onRecvPKFinishRequest:(NSString *)userID
- API description: When a VJ calls sendPKFinishRequest to notify another VJ that the PK has ended, the another VJ will receive this callback notification. In this callback, call stopPlayPKStream to end the PK and perform clean-up.
- Sample code:

```
- (void)onRecvPKFinishRequest:(NSString *)userID {
    [_liveRoom stopPlayPKStream];
}
```

### 8. onRecvRoomTextMsg

- API definition: - (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic textMsg:(NSString *)textMsg
- API description: When sendRoomTextMsg is called at the VJ or viewer end, the VJ or viewers in the room will receive this notification.
- Sample code: 

```
- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID nickName:(NSString *)nickName 
                  headPic:(NSString *)headPic textMsg:(NSString *)textMsg
{
    IMUserAble* info = [IMUserAble new];
    info.imUserId = userID;
    info.imUserName = nickName.length > 0? nickName : userID;
    info.imUserIconUrl = headPic;
    info.cmdType = TCMsgModelType_NormalMsg;
    [_logicView handleIMMessage:info msgText:textMsg];
}
```



### 9. onRecvRoomCustomMsg

- API definition: void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
- API description: When sendRoomCustomMsg is called at the VJ or viewer end, the VJ or viewers in the room will receive this notification.
- Sample code: 

```
- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID nickName:(NSString *)nickName
                  headPic:(NSString *)headPic textMsg:(NSString *)textMsg
{
    IMUserAble* info = [IMUserAble new];
    info.imUserId = userID;
    info.imUserName = nickName.length > 0? nickName : userID;
    info.imUserIconUrl = headPic;
    info.cmdType = TCMsgModelType_NormalMsg;
    [_logicView handleIMMessage:info msgText:textMsg];
}
```

### 10. onRoomClosed

- API definition: - (void)onRoomClose:(NSString *)roomID
- API description: When a room is terminated, viewers in the room will receive this notification. Exit the room in the callback.
- Sample code:

```
- (void)onRoomClose:(NSString *)roomID
{
    NSLog(@"onRoomClose, roomID:%@", roomID);
}
```

### 11. onDebugMsg

- API definition: - (void)onDebugMsg:(NSString *)msg
- API description: Live room log callback. You can save the logs as a file in the callback, so as to make it easy to analyze problems.
- Sample code:

```
- (void)onDebugMsg:(NSString *)msg
{
    NSLog(@"onDebugMsg:%@", msg);
}

```


### 12. onError

- API definition: - (void)onError:(int)errCode errMsg:(NSString *)errMsg
- API description: Live room error callback
- Sample code:

```
- (void)onError:(int)errCode errMsg:(NSString *)errMsg;
{
    NSLog(@"onError:%d, %@", errCode, errMsg);
}
```

