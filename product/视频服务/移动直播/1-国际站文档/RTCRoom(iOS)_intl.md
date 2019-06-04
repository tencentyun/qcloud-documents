## RTCRoom

| Name | Description |
| :------------------------------------: | :------------------------------: |
| @property (nonatomic, weak) id < RTCRoomListener > delegate;       | Sets rtcroom callback |
| - (void)login:(NSString*)serverDomain loginInfo:(LoginInfo *)loginInfo withCompletion:(ILoginCompletionHandler)completion             | Logs in to the RoomService backend |
| -(void)logout:(ILogoutCompletionHandler)completion  | Logs out of the RoomService backend |
| - (void)getRoomList:(int)index cnt:(int)cnt withCompletion:(IGetRoomListCompletionHandler)completion | Gets the room list (optional, you can select your room list.) |
| - (void)createRoom:(NSString *)roomID roomInfo:(NSString *)roomInfo withCompletion:(ICreateRoomCompletionHandler)completion | Meeting initiator: Creates a room (roomID is optional) |
| - (void)enterRoom:(NSString *)roomID withCompletion:(IEnterRoomCompletionHandler)completion | Meeting participant: Enters a room |
| - (void)exitRoom:(IExitRoomCompletionHandler)completion    | Meeting initiator/participant: Exits a room |
| - (void)startLocalPreview:(UIView *)view   | Meeting initiator/participant: Enables camera preview |
| - (void)stopLocalPreview  | Stops camera preview |
| - (void)addRemoteView:(UIView *)view withUserID:(NSString *)userID playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError  | Plays the remote video stream of a meeting participant |
| - (void)deleteRemoteView:(NSString *)userID                  | Stops playing the remote video stream of a meeting participant |
| - (void)sendRoomTextMsg:(NSString *)textMsg    | Sends a text message (on-screen comment) |
| - (void)switchToBackground:(UIImage *)pauseImage  | App switches from foreground to background |
| - (void)switchToForeground                     | App switches from background to foreground |
| - (void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel | Sets beauty filter |
| - (void)switchCamera | Switches between front and rear cameras. Dynamic switching is supported during push |
| - (void)setMute:(BOOL)isMute  | Enables Mute |

## RTCRoomListener

| Name | Description |
| ------------------------------------- | ------------------- |
| - (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray  | Notification: The list of existing pushers in the room (the number of remote video streams). |
| - (void)onPusherJoin:(PusherInfo *)pusherInfo;      | Notification: A new pusher joined the room (notifies you of the addition of a remote video stream) |
| - (void)onPusherQuit:(PusherInfo *)pusherInfo      | Notification: A pusher left the room (notifies you of the subtraction of a remote video stream) |
| - (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar textMsg:(NSString *)textMsg     | Chat room: Receives a text message |
|- (void)onRoomClose:(NSString *)roomID               | Notification: Room is closed |
| - (void)onDebugMsg:(NSString *)msg | LOG: Log callback |
| - (void)onError:(int)errCode errMsg:(NSString *)errMsg   | ERROR: Error callback |



## Details of RTCRoom APIs

### 1.setDelegate

- API definition: @property (nonatomic, weak) id < RTCRoomListener> delegate
- API Description: Sets RTCRoomListener callback. For the callback function, please see the RTCRoomListener API description.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| delegate | RTCRoomListener | rtcroom Callback API |

- Sample code:

```
[self.rtcRoom setDelegate:self];
```

### 2. login

- API definition: - (void)login:(NSString*)serverDomain loginInfo:(LoginInfo *)loginInfo withCompletion:(ILoginCompletionHandler)completion
- API description: Logs in to the RoomService backend. You can specify whether to use the Tencent Cloud RoomService or the user-deployed RoomService.
- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
Server address of | serverDomain | NSString | RoomService. Please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). | for more information.
| loginInfo | LoginInfo | Login parameter. Please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). | for more information.
| completion | ILoginCompletionHandler | Callback to verify whether the login is successful |

- Sample code:

```
  LoginInfo *loginInfo = [LoginInfo new];
  loginInfo.sdkAppID = sdkAppID;
  loginInfo.userID = userID;
  loginInfo.userName = userName;
  loginInfo.userAvatar = userAvatar;
  loginInfo.userSig = userSig;
  loginInfo.accType = accType;

  _weak __typeof(self) weakSelf = self;
  [weakSelf.rtcRoom login:kHttpServerAddrDomain loginInfo:loginInfo withCompletion:^(int errCode, NSString *errMsg) {
     NSLog(@"init RTCRoom errCode[%d] errMsg[%@]", errCode, errMsg);
       if (errCode == 0) {
          //success
        } else {
          [weakSelf alertTips:@"rtcRoom initFailed" msg:errMsg];
        }
  }];
```



### 3. logout 

- API definition: -(void)logout:(ILogoutCompletionHandler)completion
- API description: Logs out of the RoomService backend
- Sample code:

```
[self.rtcRoom logout:nil];
```


### 4.getRoomList

- API definition: - (void)getRoomList:(int)index cnt:(int)cnt withCompletion:(IGetRoomListCompletionHandler)completion
- API description: Pulls the room list. The parameters index and cnt are used to handle paging, which means you can pull "cnt" rooms from the room numbered "index". Call of this API is not required. If you already have your own room list, you can continue to use it.

- Parameter description:

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| index | int | The index of the room from which pull starts |
| cnt | int |  Number of rooms to be returned via RoomService |
| completion | IGetRoomListCompletionHandler | Callback of pulling a room list |

- Sample code:

```
//The pulling begins from the number 0, and ends when 20 rooms are pulled.
[self.rtcRoom getRoomList:0 cnt:20 withCompletion:^(int errCode, NSString *errMsg, NSArray<RoomInfo *> *roomInfoArray) {
    NSLog(@"getRoomList errCode[%d] errMsg[%@]", errCode, errMsg);
 }];
```


### 5. createRoom

- API definition: - (void)createRoom:(NSString *)roomID roomInfo:(NSString *)roomInfo withCompletion:(ICreateRoomCompletionHandler)completion 
- API description: Creates a room at RoomService backend.
- Parameter description:

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| roomID        | NSString  | You can specify an ID for a new room with the parameter roomID, or leave it unspecified. If you do not specify an ID for the room, RoomService will automatically create a new roomID and return it to you through CreateRoomCallback. |
| roomInfo    | NSString  | Defined by creator. This information is returned via getRoomList |
| completion | ICreateRoomCompletionHandler  | Callback of room creation result |

- Sample code:

```
[self.rtcRoom createRoom:@"" roomInfo:@"roomName" withCompletion:^(int errCode, NSString *errMsg) {
   NSLog(@"createRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
}];
```

### 6. enterRoom

- API definition: - (void)enterRoom:(NSString *)roomID withCompletion:(IEnterRoomCompletionHandler)completion 

- API description: (A meeting participant) enters a room.

- Sample code:

```
[self.rtcRoom enterRoom:roomID withCompletion:^(int errCode, NSString *errMsg) {
   NSLog(@"enterRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
}]; 

```

### 7. exitRoom

- API definition: - (void)exitRoom:(IExitRoomCompletionHandler)completion

- API description: (A meeting initiator/participant) exits a room.

- Sample code:

```
[self.rtcRoom exitRoom:^(int errCode, NSString *errMsg) {
    NSLog(@"exitRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
 }];
```


### 8. startLocalPreview

- API definition:- (void)startLocalPreview:(UIView *)view
- API description: (A meeting initiator or meeting participant) enables camera preview. The front camera is used by default, and switchCamera is used to switch between front and rear cameras.
- Sample code:

```
[self.rtcRoom startLocalPreview:pusherView];
```


### 9. stopLocalPreview

- API definition: - (void)stopLocalPreview;
- API description: (A meeting initiator/participant) disables camera preview.
- Sample code:

```
[self.rtcRoom stopLocalPreview];
```

### 10.addRemoteView

- API definition: - (void)addRemoteView:(UIView *)view withUserID:(NSString *)userID playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError
- API description: (A meeting initiator/participant) plays the remote video stream of a meeting participant. This API is called when onPusherJoin (notification of new meeting participant entering the room) is received.
- Sample code:

```
[self.rtcRoom addRemoteView:playerView withUserID:userID playBegin:nil playError:^(int errCode, NSString *errMsg) {
    //to do
}];
```

### 11.deleteRemoteView

- API definition: - (void)deleteRemoteView:(NSString *)userID
- API description: Stops playing the video of a meeting participant. This API is called when onPusherQuit (a meeting participant leaves) is received.
- Sample code: 

```
[self.rtcRoom deleteRemoteView:userID];
```

### 12.sendRoomTextMsg

- API definition: - (void)sendRoomTextMsg:(NSString *)textMsg
- API description: Sends a text message. Other members in the room will receive a notification via onRecvRoomTextMsg.
- Sample code: 

```
[self.rtcRoom sendRoomTextMsg:textMsg];
```

### 13.switchToBackground

- API definition: - (void)switchToBackground:(UIImage *)pauseImage
- API description: Switches from foreground to background, stops collecting camera data, and pushes the default pauseImage pictures.


### 14.switchToForeground

- API definition: - (void)switchToForeground
- API description: Switches from background to foreground, and starts collecting camera data.


### 15.setBeautyStyle

- API definition: - (void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel
- API description: Sets beauty filter style, dermabrasion level, whitening level, and blushing level.
- Parameter description:

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| beautyStyle          | int  | Dermabrasion style: 0: Smooth 1: Natural 2: Hazy |
| beautyLevel    | int  | Dermabrasion level: Value range: 0-9. 0 means disabling beauty filter. Default is 0, i.e., disabling beauty filter |
| whitenessLevel | int  | Whitening level: Value range: 0-9. 0 means disabling whitening. Default is 0, i.e., disabling whitening |
| ruddinessLevel     | int  | Blushing level: Value range: 0-9. 0 means disabling blushing. Default is 0, i.e., disabling blushing |

- Sample code:
  
```
 [self.rtcRoom setBeautyStyle: beautyStyle beautyLevel: beautyLevel whitenessLevel: whitenessLevel ruddinessLevel: ruddinessLevel];
```


### 16.switchCamera

- API definition: - (void)switchCamera
- API description: Switches between cameras. When the front camera is in use, calling this API enables a switch from the front camera to the rear camera, and vice versa. This API takes effect only if it is called after camera preview (startCameraPreview) is enabled. The front camera is used by default when the SDK enables camera preview.


### 17.setMute

- API definition: - (void)setMute:(BOOL)isMute
- API description: Enables Mute Once Mute is enabled, the SDK shifts from pushing microphone-collected sounds to pushing mute.
- Parameter description:

| Parameter | Type | Description |
| ---- | ------- | ---- |
| isMute | BOOL | Whether to enable Mute |

## Details of RTCRoomListener APIs

### 1. onGetPusherList

- API definition: - (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray
- API description: A new meeting participant will receive the current list of meeting participants when entering a room. In the callback, you can call addRemoteView to playback the video of other meeting participants.

- Sample code:

```
- (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray {
    dispatch_async(dispatch_get_main_queue(), ^{
        // Plays back the video of other participants
        UIView *playerView = [[UIView alloc] init];
        [playerView setBackgroundColor:UIColorFromRGB(0x262626)];
        [self.view addSubview:playerView];
            
        for (PusherInfo *pusherInfo in pusherInfoArray) {
            [self.rtcRoom addRemoteView:playerView withUserID:pusherInfo.userID playBegin:nil playError:^(int errCode, NSString *errMsg) {
                //to do
            }];
        }
    });
}
```

### 2. onPusherJoin

- API definition: - (void)onPusherJoin:(PusherInfo *)pusherInfo
- API description: When a new meeting participant enters a room, the other meeting participants in the room will receive this notification. In the callback, you can call addRemoteView to playback the video of this new meeting participant.

- Sample code:

```
- (void)onPusherJoin:(PusherInfo *)pusherInfo {
    dispatch_async(dispatch_get_main_queue(), ^{
        UIView *playerView = [[UIView alloc] init];
        [playerView setBackgroundColor:UIColorFromRGB(0x262626)];
        [self.view addSubview:playerView];
       
        [self.rtcRoom addRemoteView:playerView withUserID:pusherInfo.userID playBegin:nil playError:^(int errCode, NSString *errMsg) {
            //to do
        }];
    });
}
```

### 3. onPusherQuit

- API definition: - (void)onPusherQuit:(PusherInfo *)pusherInfo
- API description: The other meeting participants in the room will receive this notification when a meeting participant leaves a room. In the callback, you can call deleteRemoteView to stop the video of this meeting participant.
- Sample code:

```
- (void)onPusherQuit:(PusherInfo *)pusherInfo {
    dispatch_async(dispatch_get_main_queue(), ^{
        UIView *playerView = [_playerViewDic objectForKey:pusherInfo.userID];
        [playerView removeFromSuperview];
    });
}
```


### 4. onRecvRoomTextMsg

- API definition: - (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar textMsg:(NSString *)textMsg
- API description: When a meeting participant calls sendRoomTextMsg, the other meeting participants in the room will receive this notification.
- Sample code: 

```
- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar textMsg:(NSString *)textMsg {
    //to do
}
```

### 5. onRoomClosed

- API definition: - (void)onRoomClose:(NSString *)roomID
- API description: When a room is terminated, meeting participants in the room will receive this notification. Exit the room in the callback.
- Sample code:

```
- (void)onRoomClose:(NSString *)roomID {
    [self alertTips:@"Prompt" msg:@"Session ended" completion:^{
        [self.navigationController popViewControllerAnimated:YES];
    }];
}

```

### 6. onDebugMsg

- API definition: - (void)onDebugMsg:(NSString *)msg
- API description: Live room log callback. You can save the logs as a file in the callback, so as to make it easy to analyze problems.
- Sample code:

```
- (void)onDebugMsg:(NSString *)msg {
    NSLog(@"%@",msg);
}
```


### 7. onError

- API definition: - (void)onError:(int)errCode errMsg:(NSString *)errMsg
- API description: Live room error callback
- Sample code:

```
- (void)onError:(int)errCode errMsg:(NSString *)errMsg {
    [self alertTips:@"Prompt" msg:errMsg completion:^{
        [self.navigationController popViewControllerAnimated:YES];
    }];
}
```

