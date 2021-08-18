TRTCCalling 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1和多人语音通话。TRTCCalling 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [实时语音通话（iOS）](https://cloud.tencent.com/document/product/647/42046)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。

 
<h2 id="TRTCCalling">TRTCCalling API 概览</h2>

### SDK 基础函数

| API                             | 描述                                             |
| ------------------------------- | ------------------------------------------------ |
| [shareInstance](#shareinstance) | 组件单例。                                       |
| [addDelegate](#adddelegate)     | 设置事件回调。                                   |
| [login](#login)                 | 登录组件接口，所有功能需要先进行登录后才能使用。 |
| [logout](#logout)               | 登出组件接口，登出后无法再进行拨打操作。         |


### 通话操作相关接口函数

| API                     | 描述           |
| ----------------------- | -------------- |
| [call](#call)           | 单人通话邀请。 |
| [groupCall](#groupcall) | 群聊通话邀请。 |
| [accept](#accept)       | 接受当前通话。 |
| [reject](#reject)       | 拒绝当前通话。 |
| [hangup](#hangup)       | 结束当前通话。 |

### 音频控制相关接口函数

| API                           | 描述                                   |
| ----------------------------- | -------------------------------------- |
| [setMicMute](#setmicmute)     | 静音本地音频采集。                     |
| [setHandsFree](#sethandsfree) | 设置免提。                             |

<h2 id="TRTCCallingDelegate">TRTCCallingDelegate API 概览</h2>

### 通用事件回调

| API                 | 描述       |
| ------------------- | ---------- |
| [onError](#onerror) | 错误回调。 |

### 邀请方回调

| API                       | 描述             |
| ------------------------- | ---------------- |
| [onReject](#onreject)     | 拒绝通话回调。   |
| [onNoResp](#onnoresp)     | 对方无回应回调。 |
| [onLineBusy](#onlinebusy) | 通话忙线回调。   |

### 被邀请方回调

| API                                   | 描述                 |
| ------------------------------------- | -------------------- |
| [onInvited](#oninvited)               | 被邀请通话回调。     |
| [onCallingCancel](#oncallingcancel)   | 当前通话被取消回调。 |
| [onCallingTimeOut](#oncallingtimeout) | 当前通话超时回调。   |

### 通用回调

| API                                                          | 描述                       |
| ------------------------------------------------------------ | -------------------------- |
| [onGroupCallInviteeListUpdate](#ongroupcallinviteelistupdate) | 群聊更新邀请列表回调。     |
| [onUserEnter](#onuserenter)                                  | 用户进入通话回调。         |
| [onUserLeave](#onuserleave)                                  | 用户离开通话回调。         |
| [onUserAudioAvailable](#onuseraudioavailable)                | 用户是否开启音频上行回调。 |
| [onUserVoiceVolume](#onuservoicevolume)                      | 用户通话音量回调。         |
| [onCallEnd](#oncallend)                                      | 通话结束回调。             |

## SDK 基础函数

### shareInstance

shareInstance 是 TRTCCalling 的组件单例。

```Objective-C
/// 单例对象
+ (TRTCCalling *)shareInstance;
```


### addDelegate

[TRTCCalling](https://cloud.tencent.com/document/product/647/42044) 事件回调，您可以通过 TRTCCallingDelegate 获得 [TRTCCalling](https://cloud.tencent.com/document/product/647/42044) 的各种状态通知。

```Objective-C
/// 设置TRTCCallingDelegate回调
/// @param delegate 回调实例
- (void)addDelegate:(id<TRTCCallingDelegate>)delegate;
```

### login

登录组件。

```Objective-C
typedef void(^CallingActionCallback)(void);
typedef void(^ErrorCallback)(int code, NSString *des);

/// 登录接口
/// @param sdkAppID SDK ID，可在腾讯云控制台获取
/// @param userID 用户ID
/// @param userSig 用户签名
/// @param success 成功回调
/// @param failed 失败回调
- (void)login:(UInt32)sdkAppID
         user:(NSString *)userID
      userSig:(NSString *)userSig
      success:(CallingActionCallback)success
       failed:(ErrorCallback)failed
NS_SWIFT_NAME(login(sdkAppID:user:userSig:success:failed:));
```

参数如下表所示：

| 参数     | 类型                  | 含义                                                         |
| -------- | --------------------- | ------------------------------------------------------------ |
| sdkAppID | UInt32                | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| user     | String                | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | String                | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| success  | CallingActionCallback | 登录成功回调。                                               |
| failed   | ErrorCallback         | 登录失败回调。                                               |

### logout

登出组件。

```Objective-C
/// 登出接口
/// @param success 成功回调
/// @param failed 失败回调
- (void)logout:(CallingActionCallback)success
        failed:(ErrorCallback)failed
NS_SWIFT_NAME(logout(success:failed:));
```

参数如下表所示：

| 参数    | 类型                  | 含义           |
| ------- | --------------------- | -------------- |
| success | CallingActionCallback | 登出成功回调。 |
| failed  | ErrorCallback         | 登出失败回调。 |


## 通话操作相关接口函数

### call

单人通话邀请，当前处于通话中也可继续调用邀请他人。

```Objective-C
/// 发起1v1通话接口
/// @param userID 被邀请方ID
/// @param type 通话类型：视频/语音
- (void)call:(NSString *)userID
        type:(CallType)type
NS_SWIFT_NAME(call(userID:type:));
```

参数如下表所示：

| 参数   | 类型     | 含义                  |
| ------ | -------- | --------------------- |
| userID | String   | 呼叫用户 ID。         |
| type   | CallType | 通话类型：视频/语音。 |

### groupCall

IM 群组邀请通话，被邀请方会收到 `onInvited` 回调。如果当前处于通话中，可以继续调用该函数继续邀请他人进入通话，同时正在通话的用户会收到 `onGroupCallInviteeListUpdate` 回调。

```Objective-C
/// 发起多人通话
/// @param userIDs 被邀请方ID列表
/// @param type 通话类型:视频/语音
/// @param groupID 群组ID，可选参数
- (void)groupCall:(NSArray *)userIDs
             type:(CallType)type
          groupID:(NSString * _Nullable)groupID
NS_SWIFT_NAME(groupCall(userIDs:type:groupID:));
```

参数如下表所示：

| 参数    | 类型     | 含义                  |
| ------- | -------- | --------------------- |
| userIDs | [String]   | 邀请 ID 列表。        |
| type    | CallType | 通话类型：视频/语音。 |
| groupID | String   | 群 ID。               |



### accept

接受当前通话。当您作为被邀请方收到 `onInvited` 的回调时，可以调用该函数接听来电。

```Objective-C
/// 接受当前通话
- (void)accept;
```



### reject

拒绝当前通话。当您作为被邀请方收到 `onInvited` 的回调时，可以调用该函数拒绝来电。

```Objective-C
/// 拒绝当前通话
- (void)reject;
```



### hangup

挂断当前通话。当您处于通话中，可以调用该函数结束通话。

```Objective-C
/// 主动挂断通话
- (void)hangup;
```

## 音频控制相关接口函数

### setMicMute

静音本地音频采集。

```Objective-C
///静音操作
- (void)setMicMute:(BOOL)isMute;
```

参数如下表所示：

| 参数   | 类型 | 含义                                  |
| ------ | ---- | ------------------------------------- |
| isMute | Bool | true：麦克风关闭，false：麦克风打开。 |

### setHandsFree

开启免提。

```Objective-C
///免提操作
- (void)setHandsFree:(BOOL)isHandsFree;
```

参数如下表所示：

| 参数        | 类型 | 含义                              |
| ----------- | ---- | --------------------------------- |
| isHandsFree | Bool | true：开启免提，false：关闭免提。 |

## TRTCCallingDelegate事件回调

## 通用事件回调

### onError

错误回调。

>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```Objective-C
/// sdk内部发生了错误 | sdk error
/// - Parameters:
///   - code: 错误码
///   - msg: 错误消息
-(void)onError:(int)code msg:(NSString * _Nullable)msg
NS_SWIFT_NAME(onError(code:msg:));

```

参数如下表所示：

| 参数 | 类型    | 含义       |
| ---- | ------- | ---------- |
| code | Int     | 错误码。   |
| msg  | String  | 错误信息。 |


## 邀请方回调

### onReject

拒绝通话回调。

```Objective-C
/// 拒绝通话回调-仅邀请者受到通知，其他用户应使用 onUserEnter |
/// reject callback only worked for Sponsor, others should use onUserEnter)
/// - Parameter uid: userid
-(void)onReject:(NSString *)uid
NS_SWIFT_NAME(onReject(uid:));
```

参数如下表所示：

| 参数 | 类型   | 含义            |
| ---- | ------ | --------------- |
| uid  | String | 拒绝用户的 ID。 |

### onNoResp

对方无回应回调。

```Objective-C
/// 无回应回调-仅邀请者受到通知，其他用户应使用 onUserEnter |
/// no response callback only worked for Sponsor, others should use onUserEnter)
/// - Parameter uid: userid
-(void)onNoResp:(NSString *)uid
NS_SWIFT_NAME(onNoResp(uid:));

```

参数如下表所示：

| 参数 | 类型   | 含义              |
| ---- | ------ | ----------------- |
| uid  | String | 无回应用户的 ID。 |

### onLineBusy

通话忙线回调。

```Objective-C
/// 通话占线回调-仅邀请者受到通知，其他用户应使用 onUserEnter |
/// linebusy callback only worked for Sponsor, others should use onUserEnter
/// - Parameter uid: userid
-(void)onLineBusy:(NSString *)uid
NS_SWIFT_NAME(onLineBusy(uid:));

```

参数如下表所示：

| 参数 | 类型   | 含义            |
| ---- | ------ | --------------- |
| uid  | String | 忙线用户的 ID。 |

## 被邀请方回调

### onInvited

被邀请通话回调。

```Objective-C
/// 被邀请通话回调 | invitee callback
/// - Parameter userIds: 邀请列表 (invited list)
-(void)onInvited:(NSString *)sponsor
         userIds:(NSArray<NSString *> *)userIds
     isFromGroup:(BOOL)isFromGroup
        callType:(CallType)callType
NS_SWIFT_NAME(onInvited(sponsor:userIds:isFromGroup:callType:));
```

参数如下表所示：

| 参数        | 类型     | 含义                  |
| ----------- | -------- | --------------------- |
| sponsor     | String   | 发起方的 ID。         |
| userIds     | [String]   | 邀请 ID 列表。        |
| isFromGroup | Bool     | 是否多人通话邀请。    |
| callType    | CallType | 通话类型：语音/视频。 |

### onCallingCancel

当前通话被取消回调。接收方未处理请求，邀请方取消后会收到此回调。

```Objective-C
/// 当前通话被取消回调 | current call had been canceled callback
-(void)onCallingCancel:(NSString *)uid
NS_SWIFT_NAME(onCallingCancel(uid:));
```



### onCallingTimeOut

当前通话超时回调。

```Objective-C
/// 通话超时的回调 | timeout callback
-(void)onCallingTimeOut;
```

## 通用回调

### onGroupCallInviteeListUpdate

群聊更新邀请列表回调。

```Objective-C
/// 群聊更新邀请列表回调 | update current inviteeList in group calling
/// - Parameter userIds: 邀请列表 | inviteeList
-(void)onGroupCallInviteeListUpdate:(NSArray *)userIds
NS_SWIFT_NAME(onGroupCallInviteeListUpdate(userIds:));
```

参数如下表所示：

| 参数    | 类型     | 含义           |
| ------- | -------- | -------------- |
| userIds | [String]   | 邀请 ID 列表。 |

### onUserEnter

用户进入通话回调。

```Objective-C
/// 进入通话回调 | user enter room callback
/// - Parameter uid: userid
-(void)onUserEnter:(NSString *)uid
NS_SWIFT_NAME(onUserEnter(uid:));
```

参数如下表所示：

| 参数 | 类型   | 含义              |
| ---- | ------ | ----------------- |
| uid  | String | 进入通话用户 ID。 |

### onUserLeave

用户离开通话回调。

```Objective-C
/// 离开通话回调 | user leave room callback
/// - Parameter uid: userid
-(void)onUserLeave:(NSString *)uid
NS_SWIFT_NAME(onUserLeave(uid:));
```

参数如下表所示：

| 参数 | 类型   | 含义              |
| ---- | ------ | ----------------- |
| uid  | String | 离开通话用户 ID。 |

### onUserAudioAvailable

用户是否开启音频上行回调。

```Objective-C
/// 用户是否开启音频上行回调 | is user audio available callback
/// - Parameters:
///   - uid: 用户ID | userID
///   - available: 是否有效 | available
-(void)onUserAudioAvailable:(NSString *)uid available:(BOOL)available
NS_SWIFT_NAME(onUserAudioAvailable(uid:available:));

```

参数如下表所示：

| 参数      | 类型   | 含义               |
| --------- | ------ | ------------------ |
| uid       | String | 通话用户 ID。      |
| available | Bool   | 用户音频是否可用。 |

### onUserVoiceVolume

用户通话音量回调。

```Objective-C
/// 用户音量回调
/// - Parameter uid: 用户ID | userID
/// - Parameter volume: 说话者的音量, 取值范围0 - 100
-(void)onUserVoiceVolume:(NSString *)uid volume:(UInt32)volume
NS_SWIFT_NAME(onUserVoiceVolume(uid:volume:));
```

参数如下表所示：

| 参数   | 类型   | 含义                            |
| ------ | ------ | ------------------------------- |
| uid    | String | 通话用户 ID。                   |
| volume | UInt32 | 通话者的音量, 取值范围0 - 100。 |

### onCallEnd

通话结束回调。

```Objective-C
/// 通话结束 | end callback
-(void)onCallEnd;
```
