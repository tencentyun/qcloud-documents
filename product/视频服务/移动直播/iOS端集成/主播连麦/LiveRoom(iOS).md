## 功能介绍

**直播+连麦** 是在 **秀场直播** 和 **在线教育** 场景中经常使用的直播模式，它既能支持高并发和低成本的在线直播，又能通过连麦实现主播和观众之间的视频通话互动，具有极强的场景适用性。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/aacdf8cdfa825f64f34af9c3c3e4154e.jpg" />


腾讯云基于 [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606) 组件实现“直播 + 连麦”功能，它分成 Client 和 Server 两个部分（都是开源的），对接攻略请参考 [DOC](https://cloud.tencent.com/document/product/454/14606)，本文档主要是详细列出了 Client 端的 API 列表：

## LiveRoom

| 名称                                       | 描述                                |
| :------------------------------------: | :------------------------------: |
| LiveRoomListener      | liveroom 回调  |
| - (void)login:(NSString*)serverDomain loginInfo:(LoginInfo *)loginInfo withCompletion:(ILoginCompletionHandler)completion;             | 登录到RoomService后台  |
| -(void)logout:(ILogoutCompletionHandler)completion                                                                   | 从RoomService后台登出                       |
| - (void)getRoomList:(int)index cnt:(int)cnt withCompletion:(IGetRoomListCompletionHandler)completion | 获取房间列表（非必须，可选择使用您自己的房间列表）                       |
| - (void)getAudienceList:(NSString *)roomID  withCompletion:(IGetAudienceListCompletionHandler)completion | 获取某个房间里的观众列表（最多返回最近加入的 30 个观众）  |
| - (void)createRoom:(NSString *)roomID roomInfo: (NSString *)roomInfo withCompletion:(ICreateRoomCompletionHandler)completion | 主播：创建房间 （roomID 可不填）|
| - (void)enterRoom:(NSString *)roomID withView:(UIView *)view withCompletion:(IEnterRoomCompletionHandler)completion | 观众：进入房间   |
| - (void)exitRoom:(IExitRoomCompletionHandler)completion    | 主播 OR 观众：退出房间    |
| - (void)startLocalPreview:(UIView *)view   | 主播 OR 连麦观众：开启摄像头预览      |
| - (void)stopLocalPreview                                                | 停止摄像头预览                                  |
| - (void)requestJoinPusher:(NSInteger)timeout withCompletion:(IRequestJoinPusherCompletionHandler)completion     | 观众：发起连麦请求      |
| - (void)joinPusher:(IJoinPusherCompletionHandler)completion                      | 观众：进入连麦状态      |
| - (void)quitPusher:(IQuitPusherCompletionHandler)completion                      | 观众：退出连麦状态      |
|- (void)acceptJoinPusher:(NSString *)userID                                 | 主播：接受来自观众的连麦请求 |
| - (void)rejectJoinPusher:(NSString *)userID reason:(NSString *)reason            | 主播：拒绝来自观众的连麦请求 |
| - (void)kickoutSubPusher:(NSString *)userID                                | 主播：踢掉连麦中的某个观众          |
| - (void)getOnlinePusherList:(IGetOnlinePusherListCompletionHandler)completion| 主播PK：获取在线的主播列表|
| - (void)startPlayPKStream:(NSString *)playUrl view:(UIView *)view playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError| 主播PK：开始播放对方的视频流|
| - (void)stopPlayPKStream | 主播PK：结束播放对方的视频流|
| - (void)sendPKReques:(NSString *)userID timeout:(NSInteger)timeout withCompletion:(IRequestPKCompletionHandler)completion | 主播PK：发送PK请求|
| - (void)sendPKFinishRequest:(NSString *)userID | 主播PK：发送结束PK的请求 |
| - (void)acceptPKRequest:(NSString *)userID | 主播PK：授受PK请求 |
| - (void)rejectPKRequest:(NSString *)userID reason:(NSString *)reason | 主播PK：拒绝PK请求 |
| - (void)addRemoteView:(UIView *)view withUserID:(NSString *)userID playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError                                                                                           | 主播：播放连麦观众的远程视频画面   |
| - (void)deleteRemoteView:(NSString *)userID                  | 主播：移除连麦观众的远程视频画面    |
| - (void)sendRoomTextMsg:(NSString *)textMsg    | 发送文本（弹幕）消息    |
| - (void)sendRoomCustomMsg:(NSString *)cmd msg:(NSString *)msg  | 发送自定义格式的消息（点赞，送花）          |
| - (void)switchToBackground:(UIImage *)pauseImage                     | App 从前台切换到后台                              |
| - (void)switchToForeground                    | App 从后台切换到前台                             |
| - (void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel                    | 设置美颜                             |
| - (void)switchCamera                           | 切换前后置摄像头，支持在推流中动态切换               |
| - (void)setMute:(BOOL)isMute                            | 静音              |
| - (void)setMirror:(BOOL)isMirror                        | 画面镜像（此接口仅影响观众端效果，主播一直保持镜像效果）                         |
| - (BOOL)playBGM:(NSString *)path                  | 开始播放背景音乐 （path 一定要是app对应的document目录下面的路径）           |
| - (BOOL)stopBGM                                  | 停止播放背景音乐                          |
| - (BOOL)pauseBGM                               | 暂停播放背景音乐                          |
| - (BOOL)resumeBGM                             | 继续播放背景音乐                          |
| - (BOOL)setMicVolume:(float)volume                           | 设置混音时麦克风的音量大小                     |
| - (BOOL)setBGMVolume:(float)volume                         | 设置混音时背景音乐的音量大小                    |
| - (void)startRecord          | 开始视频录制                            |
| - (void)stopRecord                             | 停止视频录制                            |
| TXLiveRecordListener | 视频录制回调    |

## LiveRoomListener

| 名称                                    | 描述                  |
| ------------------------------------- | ------------------- |
| - (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray  | 通知：房间里已有的推流者列表（也就是当前有几路远程画面）      |
| - (void)onPusherJoin:(PusherInfo *)pusherInfo      | 通知：新的推流者加入进来（也就是通知您多了一路远程画面）              |
| - (void)onPusherQuit:(PusherInfo *)pusherInfo      | 通知：有推流者离开房间 （也就是通知您少了一路远程画面）            |
| - (void)onRecvJoinPusherRequest:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic | 通知：主播收到观众的连麦请求         |
| - (void)onKickout           | 观众：收到被大主播踢开的消息           |
| - (void)onRecvPKRequest:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar streamUrl:(NSString *)streamUrl | 收到PK请求 |
| - (void)onRecvPKFinishRequest:(NSString *)userID | 收到结束PK的请求 |
| - (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic textMsg:(NSString *)textMsg     |  聊天室：收到文本消息  |
| - (void)onRecvRoomCustomMsg:(NSString *)roomID userID:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic cmd:(NSString *)cmd msg:(NSString *)msg   | 聊天室：收到自定义消息|
| - (void)onRoomClose:(NSString *)roomID               | 通知：房间解散通知              |
| - (void)onDebugMsg:(NSString *)msg                        | LOG：日志回调         |
| - (void)onError:(int)errCode errMsg:(NSString *)errMsg   | ERROR：错误回调        |



## LiveRoom 接口详情

### 1.setLiveRoomListener

- 接口定义：@property (nonatomic, weak) id < LiveRoomListener > delegate;
- 接口说明：设置 LiveRoomListener 代理回调 ，具体回调函数请参考 LiveRoomListener 的接口说明
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| delegate | LiveRoomListener | liveroom 回调接口 |

- 示例代码：

```
self.liveRoom.delegate = self(回调监听者)
```

### 2.login

- 接口定义：- (void)login:(NSString*)serverDomain loginInfo:(LoginInfo *)loginInfo withCompletion:(ILoginCompletionHandler)completion 
- 接口说明：登录到 RoomService 后台，通过参数 serverDomain 可以指定是使用腾讯云的 RoomService 还是使用自建的 RoomService。
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| serverDomain | String | RoomService 的服务器地址，这部分可以参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)。 |
| loginInfo | LoginInfo | 登录参数，这部分可以参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)。 |
| completion | ILoginCompletionHandler | 登录成功与否的回调 |

- 示例代码：

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



### 3.logout 

- 接口定义：-(void)logout:(ILogoutCompletionHandler)completion
- 接口说明：从 RoomService 后台注销
- 示例代码：

```
  [self.liveRoom logout:^(int errCode, NSString *errMsg) {
     // to do
  }];
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
 [self.liveRoom getRoomList:0 cnt:20 withCompletion:^(int errCode, NSString *errMsg, 
                                                      NSArray<RoomInfo *> *roomInfoArray) {
    if (errCode == 0) {
        //拉取成功         
     } else {
        //拉取失败
     }
 }];
```

### 5.getAudienceList 
- 接口定义：- (void)getAudienceList:(NSString *)roomID  withCompletion:(IGetAudienceListCompletionHandler)completion
- 接口说明：获取某个房间里的观众列表，只返回最近进入房间的 30 位观众。
- 参数说明：

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| roomID | NSString | 房间roomID |
| completion | IGetAudienceListCompletionHandler | 拉取房间观众列表的回调 |
- 示例代码：

```
  //获取房间的观众列表
  [_liveRoom getAudienceList: roomID withCompletion:^(int errCode, NSString *errMsg,
	                                    NSArray<AudienceInfo *> *audienceInfoArray) {
       //to do 
  }];
```
其中 audienceInfoArray 是一个观众信息的数组，其结构定义为：

```
// 普通观众信息
@interface AudienceInfo : NSObject
  @property (nonatomic, copy)   NSString*   userID;
  @property (nonatomic, copy)   NSString*   userInfo;
@end
```
  

### 6.createRoom

- 接口定义：- (void)createRoom:(NSString *)roomID roomInfo: (NSString *)roomInfo withCompletion:(ICreateRoomCompletionHandler)completion 
- 接口说明：在 RoomService 后台创建一个直播房间。
- 参数说明：

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| roomID        | String  | 您可以通过 roomID 参数指定新房间的 ID，也可以不指定。如果您不指定房间 ID，RoomService 会自动生成一个新的 roomID 并通过 ICreateRoomCompletionHandler 返回给你您。        |
| roomInfo    | String  | 由创建者自定义。在getRoomList中返回该信息 |
| completion | ICreateRoomCompletionHandler  | 创建房间结果回调 |

- 示例代码：

```
  [self.liveRoom createRoom:@"" roomInfo:@"创建房间者相关信息" withCompletion:^(int errCode, NSString *errMsg) {
     NSLog(@"createRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
  }];
```

### 7.enterRoom

- 接口定义：- (void)enterRoom:(NSString *)roomID withView:(UIView *)view withCompletion:(IEnterRoomCompletionHandler)completion 

- 接口说明：（观众）进入直播间。

- 示例代码：

```
  [_liveRoom enterRoom:groupid withView:videoParentView withCompletion:^(int errCode, NSString *errMsg) {
     NSLog(@"enterRoom: errCode[%d] errMsg[%@]", errCode, errMsg);    
  }];
```

### 8.exitRoom

- 接口定义：- (void)exitRoom:(IExitRoomCompletionHandler)completion 

- 接口说明：（主播 OR 观众）退出房间。

- 示例代码：

```
  [self.liveRoom exitRoom:^(int errCode, NSString *errMsg) {
      NSLog(@"exitRoom: errCode[%d] errMsg[%@]", errCode, errMsg);
  }];
```


### 9.startLocalPreview

- 接口定义：- (void)startLocalPreview:(UIView *)view
- 接口说明：（主播 OR 连麦观众）启动摄像头预览，默认是使用前置摄像头，可以通过switchCamera切换前后摄像头
- 示例代码：

```
  [self.liveRoom startLocalPreview:videoParentView];
```


### 10.stopLocalPreview

- 接口定义：- (void)stopLocalPreview
- 接口说明：（主播 OR 连麦观众）关闭摄像头预览。
- 示例代码：

```
  [self.liveRoom stopLocalPreview]; 
```


### 11.requestJoinPusher

- 接口定义：- (void)requestJoinPusher:(NSInteger)timeout withCompletion:(IRequestJoinPusherCompletionHandler)completion
- 接口说明：（观众）请求和主播连麦时调用该接口。
- 示例代码：

```
  [self.liveRoom requestJoinPusher:20 withCompletion:^(int errCode, NSString *errMsg) {
     if (errCode == 0) {
        [TCUtil toastTip:@"主播接受了您的连麦请求，开始连麦" parentView:self.view];      
     }
     else {
        [TCUtil toastTip:errMsg parentView:self.view];
     }
  }];
```



### 12.joinPusher

- 接口定义：- (void)joinPusher:(IJoinPusherCompletionHandler)completion
- 接口说明：（观众）开始推流，并进入连麦状态，是否最终连麦成功，要看 IJoinPusherCompletionHandler 的回调结果。
- 示例代码：

```
  [self.liveRoom joinPusher:^(int errCode, NSString *errMsg) {
      //连麦结果回调
   }];
```


### 13.quitPusher
- 接口定义：- (void)quitPusher:(IQuitPusherCompletionHandler)completion
- 接口说明：（观众）主动退出连麦状态。
- 示例代码：

```
  [self.liveRoom quitPusher:^(int errCode, NSString *errMsg) {
      //退出连麦状态结果回调
  }];
```


### 14.acceptJoinPusher

- 接口定义：- (void)acceptJoinPusher:(NSString *)userID
- 接口说明：（主播）同意观众的连麦请求。
- 示例代码：

```
  [self.liveRoom acceptJoinPusher: userID];
```

### 15.rejectJoinPusher

- 接口定义：- (void)rejectJoinPusher:(NSString *)userID reason:(NSString *)reason
- 接口说明：（主播）拒绝观众的连麦请求。
- 示例代码：

```
  [self.liveRoom rejectJoinPusher:userID reason:@"主播端连麦人数超过最大限制"];
```

### 16.kickoutSubPusher

- 接口定义：- (void)kickoutSubPusher:(NSString *)userID
- 接口说明：主播：踢掉连麦中的某个观众。
- 示例代码：

```
  [self.liveRoom kickoutSubPusher:userID];
```

### 17.getOnlinePusherList

- 接口定义：- (void)getOnlinePusherList:(IGetOnlinePusherListCompletionHandler)completion
- 接口说明：主播PK：获取在线的主播列表
- 示例代码：

```
[_liveRoom getOnlinePusherList:^(NSArray<PusherInfo *> *pusherInfoArray) {

}];
```

### 18.startPlayPKStream

- 接口定义：- (void)startPlayPKStream:(NSString *)playUrl view:(UIView *)view playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError
- 接口说明：主播PK：开始播放对方的流
- 示例代码：

```
[_liveRoom startPlayPKStream:playUrl view:playerView playBegin:^{

} playError:^(int errCode, NSString *errMsg) {

 }];
```

### 19.stopPlayPKStream

- 接口定义：- (void)stopPlayPKStream
- 接口说明：主播PK：结束播放对方的流
- 示例代码：

```
[_liveRoom stopPlayPKStream];
```

### 20.sendPKRequest

- 接口定义：- (void)sendPKReques:(NSString *)userID timeout:(NSInteger)timeout withCompletion:(IRequestPKCompletionHandler)completion
- 接口说明：主播PK：发送PK请求
- 示例代码：

```
 [_liveRoom sendPKReques:userID timeout:10 withCompletion:^(int errCode, NSString *errMsg, NSString *streamUrl) {
            
}];
```

### 21.sendPKFinishRequest

- 接口定义：- (void)sendPKFinishRequest:(NSString *)userID
- 接口说明：主播PK：发送结束PK的请求
- 示例代码：

```
[_liveRoom sendPKFinishRequest:userID];
```

### 22.acceptPKRequest

- 接口定义：- (void)acceptPKRequest:(NSString *)userID
- 接口说明：主播PK：授受PK请求
- 示例代码：

```
[_liveRoom acceptPKRequest:userID];
```

### 23.rejectPKRequest

- 接口定义：- (void)rejectPKRequest:(NSString *)userID reason:(NSString *)reason
- 接口说明：主播PK：拒绝PK请求
- 示例代码：

```
[_liveRoom rejectPKRequest];
```

### 24.addRemoteView

- 接口定义：- (void)addRemoteView:(UIView *)view withUserID:(NSString *)userID playBegin:(IPlayBegin)playBegin playError:(IPlayError)playError
- 接口说明：（主播）播放连麦观众的远程视频画面 ，一般在收到 onPusherJoin（新进连麦通知）时调用。
- 示例代码：

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
        //播放成功
    } playError:^(int errCode, NSString *errMsg) {
        //播放失败
    }];
}
```

### 25.deleteRemoteView

- 接口定义：- (void)deleteRemoteView:(NSString *)userID
- 接口说明：停止播放某个连麦主播视频，一般在收到 onPusherQuit （连麦者离开）时调用。
- 示例代码： 

```
  [self.liveRoom deleteRemoteView:userID];
```

### 26.sendRoomTextMsg

- 接口定义：- (void)sendRoomTextMsg:(NSString *)textMsg
- 接口说明：发送文本消息，直播间里的其他人会收到 onRecvRoomTextMsg 通知。
- 示例代码： 

```
  [[TCLiveRoomMgr getSharedLiveRoom] sendRoomTextMsg:textMsg];
```

### 27.sendRoomCustomMsg

- 接口定义：- (void)sendRoomCustomMsg:(NSString *)cmd msg:(NSString *)msg;
- 接口说明：发送自定义消息。直播间其他人会收到 onRecvRoomCustomMsg 通知。
- 示例代码： 

```
  [[TCLiveRoomMgr getSharedLiveRoom] sendRoomCustomMsg:[@(TCMsgModelType_DanmaMsg) stringValue] msg:textMsg];
```

### 28.switchToBackground

- 接口定义：- (void)switchToBackground:(UIImage *)pauseImage
- 接口说明：从前台切换到后台，关闭采集摄像头数据，推送默认图片


### 29.switchToForeground

- 接口定义：- (void)switchToForeground
- 接口说明：由后台切换到前台，开启摄像头数据采集。


### 30.setBeautyStyle

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
   [self.liveRoom setBeautyStyle:0 beautyLevel:_beauty_level whitenessLevel:_whitening_level ruddinessLevel:0];
```


### 31.switchCamera

- 接口定义：- (void)switchCamera
- 接口说明：切换摄像头，前置摄像头时调用后变成后置，后置摄像头时调用后变成前置。该接口在启动预览startLocalPreview 后调用才能生效，预览前调用无效。SDK启动预览默认使用前置摄像头。


### 32.setMute

- 接口定义：- (void)setMute:(BOOL)isMute
- 接口说明：设置静音接口。设置为静音后SDK不再推送麦克风采集的声音，而是推送静音。
- 参数说明：

| 参数   | 类型      | 说明   |
| ---- | ------- | ---- |
| isMute | BOOL | 是否静音 |


### 33.setMirror

- 接口定义：- (void)setMirror:(BOOL)isMirror
- 接口说明：设置播放端水平镜像。注意这个只影响播放端效果，不影响推流主播端。推流端看到的镜像效果是始终存在的，使用前置摄像头时推流端看到的是镜像画面，使用后置摄像头时推流端看到的是非镜像。
- 参数说明：

| 参数     | 类型      | 说明                                     |
| ------ | ------- | -------------------------------------- |
| isMirror | BOOL | YES 表示播放端看到的是镜像画面，false表示播放端看到的是非镜像画面 |

- 示例代码： 

```
  //观众端播放看到的是镜像画面
  [self.liveRoom setMirror:YES];
```

### 34.playBGM

- 接口定义：- (BOOL)playBGM:(NSString *)path
- 接口说明：播放背景音乐。该接口用于混音处理，比如将背景音乐与麦克风采集到的声音混合后播放。返回结果中，true 表示播放成功，false 表示播放失败。
- 参数说明：

| 参数   | 类型     | 说明               |
| ---- | ------ | ---------------- |
| path | NSString | 背景音在app对应的document目录下面的路径 |


### 35.stopBGM

- 接口定义：- (BOOL)stopBGM
- 接口说明：停止播放背景音乐。返回结果中，YES 表示停止播放成功，NO 表示停止播放失败。

### 36.pauseBGM

- 接口定义：- (BOOL)pauseBGM
- 接口说明：暂停播放背景音乐。返回结果中，YES 表示暂停播放成功，NO 表示暂停播放失败。


### 37.resumeBGM

- 接口定义：- (BOOL)resumeBGM
- 接口说明：恢复播放背景音乐。返回结果中，YES 表示恢复播放成功，NO 表示恢复播放失败。


### 38.setMicVolume

- 接口定义：- (BOOL)setMicVolume:(float)volume
- 接口说明：设置混音时麦克风的音量大小。返回结果中，true 表示设置麦克风的音量成功，false 表示设置麦克风的音量失败。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| volume    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |

### 39.setBGMVolume

- 接口定义：- (BOOL)setBGMVolume:(float)volume
- 接口说明：设置混音时背景音乐的音量大小。返回结果中，true 表示设置背景音的音量成功，false 表示设置背景音的音量失败。
- 参数说明：

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| volume    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |

### 40.startRecord

- 接口定义： - (void)startRecord
- 接口说明：开始录制视频。该接口用于播放端将播放的实时视频保存到本地文件。
- 特别注意：该接口需要在 enterRoom 成功后调用
- 返回结果：接口返回 0 启动录制成功；-1 表示正在录制，忽略这次录制启动；-2 videoRecorder初始化失败
- 示例代码：

```
  [self.liveRoom startRecord];
```

### 41.stopRecord

- 接口定义： - (void)stopRecord
- 接口说明：停止录制视频。录制结果会通过录制回调异步通知出来。


### 42.TXLiveRecordListener

- 接口定义： @property (nonatomic, weak) id < TXLiveRecordListener > recordDelegate
- 接口说明：设置视频录制回调，用于接收视频录制进度及录制结果。
- 参数说明：

| 参数       | 类型                                    | 说明     |
| -------- | ------------------------------------- | ------ |
| recordDelegate | TXLiveRecordListener | 视频录制回调 |

- 示例代码：

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


## LiveRoomListener 接口详情

### 1. onGetPusherList

- 接口定义：- (void)onGetPusherList:(NSArray<PusherInfo *> *)pusherInfoArray
- 接口说明：房间里已有的推流者列表（也就是当前有几路远程画面）。当新的连麦者加入房间时，新的连麦者会收到该通知。回调中您可以调用 addRemoteView 播放房间里已有连麦者的视频。

- 示例代码：

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

- 接口定义：- (void)onPusherJoin:(PusherInfo *)pusherInfo
- 接口说明：当新的连麦者加入房间时，大主播和其他的连麦者都会收到该通知。回调中您可以调用 addRemoteView 播放这个新来的连麦者的视频。

- 示例代码：

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

- 接口定义：- (void)onPusherQuit:(PusherInfo *)pusherInfo
- 接口说明：当连麦者离开房间时，大主播和其他的连麦者都会收到该通知。回调中您可以调用 deleteRemoteView 停止播放这个连麦者的视频。
- 示例代码：

```
- (void)onPusherQuit:(PusherInfo *)pusherInfo
{
    NSString* userID = pusherInfo.userID;
    //混流：减少一路
    [self.liveRoom deleteRemoteView:userID];
}
```


### 4. onRecvJoinPusherRequest

- 接口定义：- (void)onRecvJoinPusherRequest:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic
- 接口说明：当观众向主播申请连麦时，主播收到该通知。主播可以在回调中接受（acceptJoinPusher）或者拒绝（rejectJoinPusher）申请。
- 示例代码：

```
- (void)onRecvJoinPusherRequest:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic
{
    if ([_setLinkMemeber count] >= MAX_LINKMIC_MEMBER_SUPPORT) {
        [TCUtil toastTip:@"主播端连麦人数超过最大限制" parentView:self.view];
        [self.liveRoom rejectJoinPusher:userID reason:@"主播端连麦人数超过最大限制"];
    }
    else if (_userIdRequest && _userIdRequest.length > 0) {
        [TCUtil toastTip:@"请稍后，主播正在处理其它人的连麦请求" parentView:self.view];
        [self.liveRoom rejectJoinPusher:userID reason:@"请稍后，主播正在处理其它人的连麦请求"];
    }
    else {
        //接受连麦
        _userIdRequest = userID;
        [self.liveRoom acceptJoinPusher:_userIdRequest];
    }
}
```

### 5. onKickOut

- 接口定义：- (void)onKickout
- 接口说明：当主播把一个连麦者踢出连麦状态后，对应的连麦者会收到该通知。在回调中您可以停止本地预览以及退出直播。
- 示例代码： 

```
- (void)onKickout
{
    [TCUtil toastTip:@"不好意思，您被主播踢开" parentView:self.view];
    [self.liveRoom stopLocalPreview];
}
```

### 6. onRecvPKRequest

- 接口定义：- (void)onRecvPKRequest:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar streamUrl:(NSString *)streamUrl
- 接口说明：当一个主播调用sendPKRequest向另一个主播发起PK请求的时候；另一个主播会收到该回调通知。在该回调中，您可以展示一个收到PK请求的提示框，询问用户是接受还是拒绝。
- 示例代码：

```
- (void)onRecvPKRequest:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar streamUrl:(NSString *)streamUrl {
    NSString *msg = [NSString stringWithFormat:@"[%@]请求PK", userName];
    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"提示" message:msg preferredStyle:UIAlertControllerStyleAlert];
    [alertController addAction:[UIAlertAction actionWithTitle:@"拒绝" style:UIAlertActionStyleDefault handler:^(UIAlertAction * _Nonnull action) {
        [_liveRoom rejectPKRequest:userID reason:@"主播不同意您的PK"];
    }]];
    [alertController addAction:[UIAlertAction actionWithTitle:@"接受" style:UIAlertActionStyleDefault handler:^(UIAlertAction * _Nonnull action) {
        [_liveRoom acceptPKRequest:userID];
        [_liveRoom startPlayPKStream:playUrl view:playerView playBegin:^{

        } playError:^(int errCode, NSString *errMsg) {

        }];
    }]];
        
    [self.navigationController presentViewController:alertController animated:YES completion:nil];
}
```

### 7. onRecvPKFinishRequest

- 接口定义：- (void)onRecvPKFinishRequest:(NSString *)userID
- 接口说明：当一个主播调用sendPKFinishRequest通知另一个主播结束PK的时候；另一个主播会收到该回调通知。在该回调中，您需要调用stopPlayPKStream结束PK，并做好相关清理工作。
- 示例代码：

```
- (void)onRecvPKFinishRequest:(NSString *)userID {
    [_liveRoom stopPlayPKStream];
}
```

### 8. onRecvRoomTextMsg

- 接口定义：- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID nickName:(NSString *)nickName headPic:(NSString *)headPic textMsg:(NSString *)textMsg
- 接口说明：当主播或者观众端调用sendRoomTextMsg时，房间内的主播或者观众都会收到该通知。
- 示例代码： 

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

- 接口定义：void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
- 接口说明：当主播或者观众端调用sendRoomCustomMsg时，房间内的主播或者观众都会收到该通知。
- 示例代码： 

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

- 接口定义：- (void)onRoomClose:(NSString *)roomID
- 接口说明：当房间销毁时，观众会收到该通知。需要在回调中退出房间。
- 示例代码：

```
- (void)onRoomClose:(NSString *)roomID
{
    NSLog(@"onRoomClose, roomID:%@", roomID);
}
```

### 11. onDebugMsg

- 接口定义：- (void)onDebugMsg:(NSString *)msg
- 接口说明：直播间日志回调。可以在回调中将日志保存到文件中，方便问题分析。
- 示例代码：

```
- (void)onDebugMsg:(NSString *)msg
{
    NSLog(@"onDebugMsg:%@", msg);
}

```


### 12. onError

- 接口定义：- (void)onError:(int)errCode errMsg:(NSString *)errMsg
- 接口说明：直播间错误回调
- 示例代码：

```
- (void)onError:(int)errCode errMsg:(NSString *)errMsg;
{
    NSLog(@"onError:%d, %@", errCode, errMsg);
}
```
