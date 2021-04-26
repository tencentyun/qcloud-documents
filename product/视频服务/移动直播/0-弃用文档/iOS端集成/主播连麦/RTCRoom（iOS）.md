## RTCRoom

| 名称                                       | 描述                                |
| :------------------------------------: | :------------------------------: |
| @property (nonatomic, weak) id < RTCRoomListener > delegate;       | 设置rtcroom回调   |
| - (void)login:(NSString*)serverDomain loginInfo:(LoginInfo *)loginInfo withCompletion:(ILoginCompletionHandler)completion             | 登录到RoomService后台  |
| -(void)logout:(ILogoutCompletionHandler)completion                                                                    | 从RoomService后台登出                       |
| - (void)getRoomList:(int)index cnt:(int)cnt withCompletion:(IGetRoomListCompletionHandler)completion | 获取房间列表（非必须，可选择使用您自己的房间列表）                       |
| - (void)createRoom:(NSString *)roomID roomInfo:(NSString *)roomInfo withCompletion:(ICreateRoomCompletionHandler)completion | 会议创建者：创建房间 （roomID 可不填）|
| - (void)enterRoom:(NSString *)roomID withCompletion:(IEnterRoomCompletionHandler)completion | 会议参与者：进入房间   |
| - (void)exitRoom:(IExitRoomCompletionHandler)completion    | 会议创建者 OR 会议参与者：退出房间    |
| - (void)startLocalPreview:(UIView *)view   | 会议创建者 OR 会议参与者：开启摄像头预览      |
| - (void)stopLocalPreview                                                | 停止摄像头预览                                  |
| - (void)addRemoteView:(UIView *)view withUserID:(NSString *)userID playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError                                                                                            | 播放会议参与者的远程视频画面   |
| - (void)deleteRemoteView:(NSString *)userID                  | 停止播放会议参与者的远程视频画面    |
| - (void)sendRoomTextMsg:(NSString *)textMsg    | 发送文本（弹幕）消息    |
| - (void)switchToBackground:(UIImage *)pauseImage                     | App 从前台切换到后台                              |
| - (void)switchToForeground                     | App 从后台切换到前台                             |
| - (void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel                     | 设置美颜                             |
| - (void)switchCamera                           | 切换前后置摄像头，支持在推流中动态切换               |
| - (void)setMute:(BOOL)isMute                            | 静音              |

## RTCRoomListener

| 名称                                    | 描述                  |
| ------------------------------------- | ------------------- |
| - (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray  | 通知：房间里已有的推流者列表（也就是当前有几路远程画面）      |
| - (void)onPusherJoin:(PusherInfo *)pusherInfo;      | 通知：新的推流者加入进来（也就是通知您多了一路远程画面）              |
| - (void)onPusherQuit:(PusherInfo *)pusherInfo      | 通知：有推流者离开房间 （也就是通知您少了一路远程画面）            |
| - (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar textMsg:(NSString *)textMsg     |  聊天室：收到文本消息  |
|- (void)onRoomClose:(NSString *)roomID               | 通知：房间解散通知              |
| - (void)onDebugMsg:(NSString *)msg                         | LOG：日志回调         |
| - (void)onError:(int)errCode errMsg:(NSString *)errMsg   | ERROR：错误回调        |



## RTCRoom 接口详情

### 1.setDelegate

- 接口定义：@property (nonatomic, weak) id < RTCRoomListener> delegate
- 接口说明：设置 RTCRoomListener 回调 ，具体回调函数请参考 RTCRoomListener 的接口说明
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| delegate | RTCRoomListener | rtcroom 回调接口 |

- 示例代码：

```
[self.rtcRoom setDelegate:self];
```

### 2.login

- 接口定义：- (void)login:(NSString*)serverDomain loginInfo:(LoginInfo *)loginInfo withCompletion:(ILoginCompletionHandler)completion
- 接口说明：登录到 RoomService 后台，通过参数 serverDomain 可以指定是使用腾讯云的 RoomService 还是使用自建的 RoomService。
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| serverDomain | NSString | RoomService 的服务器地址，这部分可以参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)。 |
| loginInfo | LoginInfo | 登录参数，这部分可以参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)。 |
| completion | ILoginCompletionHandler | 登录成功与否的回调 |

- 示例代码：

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
          [weakSelf alertTips:@"rtcRoom init失败" msg:errMsg];
        }
  }];
```



### 3.logout 

- 接口定义：-(void)logout:(ILogoutCompletionHandler)completion
- 接口说明：从 RoomService 后台注销
- 示例代码：

```
[self.rtcRoom logout:nil];
```


### 4.getRoomList

- 接口定义：- (void)getRoomList:(int)index cnt:(int)cnt withCompletion:(IGetRoomListCompletionHandler)completion
- 接口说明：拉取房间列表，index 和 cnt 两个参数用于做分页处理，表示：从序号 index 的房间开始拉取 cnt 个房间。这并非一个必须调用的 API，如果您已经有自己的房间列表服务模块，可以继续使用。

- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| index | int | 从第几个房间开始拉取 |
| cnt | int | 希望 RoomService 返回的房间个数 |
| completion | IGetRoomListCompletionHandler | 拉取房间列表的回调 |

- 示例代码：

```
//拉取序号0开始，拉取20个房间
[self.rtcRoom getRoomList:0 cnt:20 withCompletion:^(int errCode, NSString *errMsg, NSArray<RoomInfo *> *roomInfoArray) {
    NSLog(@"getRoomList errCode[%d] errMsg[%@]", errCode, errMsg);
 }];
```


### 5. createRoom

- 接口定义：- (void)createRoom:(NSString *)roomID roomInfo:(NSString *)roomInfo withCompletion:(ICreateRoomCompletionHandler)completion 
- 接口说明：在 RoomService 后台创建一个直播房间。
- 参数说明：

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| roomID        | NSString  | 您可以通过 roomID 参数指定新房间的 ID，也可以不指定。如果您不指定房间 ID，RoomService 会自动生成一个新的 roomID 并通过 CreateRoomCallback 返回给你您。        |
| roomInfo    | NSString  | 由创建者自定义。在getRoomList中返回该信息 |
| completion | ICreateRoomCompletionHandler  | 创建房间结果回调 |

- 示例代码：

```
[self.rtcRoom createRoom:@"" roomInfo:@"roomName" withCompletion:^(int errCode, NSString *errMsg) {
   NSLog(@"createRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
}];
```

### 6. enterRoom

- 接口定义：- (void)enterRoom:(NSString *)roomID withCompletion:(IEnterRoomCompletionHandler)completion 

- 接口说明：（会议参与者）进入直播间。

- 示例代码：

```
[self.rtcRoom enterRoom:roomID withCompletion:^(int errCode, NSString *errMsg) {
   NSLog(@"enterRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
}]; 

```

### 7. exitRoom

- 接口定义：- (void)exitRoom:(IExitRoomCompletionHandler)completion

- 接口说明：（会议创建者 OR 会议参与者）退出房间。

- 示例代码：

```
[self.rtcRoom exitRoom:^(int errCode, NSString *errMsg) {
    NSLog(@"exitRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
 }];
```


### 8. startLocalPreview

- 接口定义：- (void)startLocalPreview:(UIView *)view
- 接口说明：（会议创建者 OR 会议参与者）启动摄像头预览，默认是使用前置摄像头，可以通过switchCamera切换前后摄像头
- 示例代码：

```
[self.rtcRoom startLocalPreview:pusherView];
```


### 9. stopLocalPreview

- 接口定义：- (void)stopLocalPreview;
- 接口说明：（会议创建者 OR 会议参与者）关闭摄像头预览。
- 示例代码：

```
[self.rtcRoom stopLocalPreview];
```

### 10.addRemoteView

- 接口定义：- (void)addRemoteView:(UIView *)view withUserID:(NSString *)userID playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError
- 接口说明：（会议创建者 OR 会议参与者）播放会议参与者的远程视频画面 ，一般在收到 onPusherJoin（新会议参与者进入通知）时调用。
- 示例代码：

```
[self.rtcRoom addRemoteView:playerView withUserID:userID playBegin:nil playError:^(int errCode, NSString *errMsg) {
    //to do
}];
```

### 11.deleteRemoteView

- 接口定义：- (void)deleteRemoteView:(NSString *)userID
- 接口说明：停止播放某个会议参与者视频，一般在收到 onPusherQuit （会议参与者离开）时调用。
- 示例代码： 

```
[self.rtcRoom deleteRemoteView:userID];
```

### 12.sendRoomTextMsg

- 接口定义：- (void)sendRoomTextMsg:(NSString *)textMsg
- 接口说明：发送文本消息，房间里的其他人会收到 onRecvRoomTextMsg 通知。
- 示例代码： 

```
[self.rtcRoom sendRoomTextMsg:textMsg];
```

### 13.switchToBackground

- 接口定义：- (void)switchToBackground:(UIImage *)pauseImage
- 接口说明：从前台切换到后台，关闭采集摄像头数据，推送默认 pauseImage 图片


### 14.switchToForeground

- 接口定义：- (void)switchToForeground
- 接口说明：由后台切换到前台，开启摄像头数据采集。


### 15.setBeautyStyle

- 接口定义：- (void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel
- 接口说明：设置美颜风格、磨皮程度、美白级别和红润级别。
- 参数说明：

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| beautyStyle          | int  | 磨皮风格：  0：光滑  1：自然  2：朦胧                  |
| beautyLevel    | int  | 磨皮等级： 取值为 0-9.取值为 0 时代表关闭美颜效果.默认值: 0,即关闭美颜效果 |
| whitenessLevel | int  | 美白等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果 |
| ruddinessLevel     | int  | 红润等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果 |

- 示例代码：
  
```
 [self.rtcRoom setBeautyStyle: beautyStyle beautyLevel: beautyLevel whitenessLevel: whitenessLevel ruddinessLevel: ruddinessLevel];
```


### 16.switchCamera

- 接口定义：- (void)switchCamera
- 接口说明：切换摄像头，前置摄像头时调用后变成后置，后置摄像头时调用后变成前置。该接口在启动预览 startCameraPreview 后调用才能生效，预览前调用无效。SDK启动预览默认使用前置摄像头。


### 17.setMute

- 接口定义：- (void)setMute:(BOOL)isMute
- 接口说明：设置静音接口。设置为静音后SDK不再推送麦克风采集的声音，而是推送静音。
- 参数说明：

| 参数   | 类型      | 说明   |
| ---- | ------- | ---- |
| isMute | BOOL | 是否静音 |

## RTCRoomListener 接口详情

### 1. onGetPusherList

- 接口定义：- (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray
- 接口说明：当新会议参与者加入房间时，会收到房间已存在的会议者列表。回调中您可以调用 addRemoteView 播放其他会议人员的视频。

- 示例代码：

```
- (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray {
    dispatch_async(dispatch_get_main_queue(), ^{
        // 播放其他人的画面
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

- 接口定义：- (void)onPusherJoin:(PusherInfo *)pusherInfo
- 接口说明：当新的会议参与者加入房间时，房间中其他的会议参与者都会收到该通知。回调中您可以调用 addRemoteView 播放这个新来的会议参与者的视频。

- 示例代码：

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

- 接口定义：- (void)onPusherQuit:(PusherInfo *)pusherInfo
- 接口说明：当会议参与者离开房间时，房间的其他会议参与者都会收到该通知。回调中您可以调用 deleteRemoteView 停止播放这个会议参与者的视频。
- 示例代码：

```
- (void)onPusherQuit:(PusherInfo *)pusherInfo {
    dispatch_async(dispatch_get_main_queue(), ^{
        UIView *playerView = [_playerViewDic objectForKey:pusherInfo.userID];
        [playerView removeFromSuperview];
    });
}
```


### 4. onRecvRoomTextMsg

- 接口定义：- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar textMsg:(NSString *)textMsg
- 接口说明：当会议参与者调用sendRoomTextMsg时，房间内的其他会议参与者都会收到该通知。
- 示例代码： 

```
- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar textMsg:(NSString *)textMsg {
    //to do
}
```

### 5. onRoomClosed

- 接口定义：- (void)onRoomClose:(NSString *)roomID
- 接口说明：当房间销毁时，会议参与者会收到该通知。需要在回调中退出房间。
- 示例代码：

```
- (void)onRoomClose:(NSString *)roomID {
    [self alertTips:@"提示" msg:@"会话已被解散" completion:^{
        [self.navigationController popViewControllerAnimated:YES];
    }];
}

```

### 6. onDebugMsg

- 接口定义：- (void)onDebugMsg:(NSString *)msg
- 接口说明：直播间日志回调。可以在回调中将日志保存到文件中，方便问题分析。
- 示例代码：

```
- (void)onDebugMsg:(NSString *)msg {
    NSLog(@"%@",msg);
}
```


### 7. onError

- 接口定义：- (void)onError:(int)errCode errMsg:(NSString *)errMsg
- 接口说明：直播间错误回调
- 示例代码：

```
- (void)onError:(int)errCode errMsg:(NSString *)errMsg {
    [self alertTips:@"提示" msg:errMsg completion:^{
        [self.navigationController popViewControllerAnimated:YES];
    }];
}
```
