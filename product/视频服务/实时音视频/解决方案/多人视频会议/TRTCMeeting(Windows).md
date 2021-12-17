TUIRoom 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建房间，参会人员输入房间号后进入房间。
- 参会人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TUIRoom 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人视频聊天室(Windows)](https://cloud.tencent.com/document/product/647/63494)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时视频会议组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 实现聊天室的功能（**IM SDK 使用 C++ 版本**）。


## TUIRoom API 概览[](id:TUIRoom)

### TUIRoomCore 基础函数

| API                                 | 描述           |
|-----|-----|
| [GetInstance](#getinstance)         | 获取单例对象。 |
| [DestroyInstance](#destroyinstance) | 销毁单例对象。 |
| [SetCallback](#setcallback)         | 设置事件回调。 |

### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [login](#login)                           | 登录。                             |
| [logout](#logout)                         | 登出。                             |
| [CreateRoom](#createroom)                 | 创建房间（主持人调用）。           |
| [DestroyRoom](#destroyroom)               | 销毁房间（主持人调用）。           |
| [EnterRoom](#enterroom)                   | 进入房间（参会成员调用）。         |
| [LeaveRoom](#leaveroom)                   | 离开房间（参会成员或主持人调用）。 |
| [GetRoomInfo](#getroominfo)               | 获取房间信息。                     |
| [GetRoomUsers](#getroomusers)             | 获取房间内所有成员信息。           |
| [GetUserInfo](#getuserinfo)               | 获取某个用户的信息。               |
| [TransferRoomMaster](#transferroommaster) | 转移主持人权限（主持人调用）。     |

### 本地音视频操作接口

| API                                                   | 描述                       |
|-----|-----|
| [StartCameraPreview](#startcamerapreview)             | 开启本地视频的预览画面。   |
| [StopCameraPreview](#stopcamerapreview)               | 停止本地视频采集及预览。   |
| [UpdateCameraPreview](#updatecamerapreview)           | 改变本地视频渲染窗口。     |
| [StartLocalAudio](#startlocalaudio)                   | 开启麦克风采集。           |
| [StopLocalAudio](#stoplocalaudio)                     | 停止麦克风采集。           |
| [StartSystemAudioLoopback](#startsystemaudioloopback) | 开启/关闭系统声音的采集。  |
| [StopSystemAudioLoopback](#stopsystemaudioloopback)   | 开启/关闭系统声音的采集。  |
| [SetVideoMirror](#setvideomirror)                     | 设置本地画面镜像预览模式。 |

### 远端用户相关接口

| API                                   | 描述                               |
|-----|-----|
| [StartRemoteView](#startremoteview)   | 订阅并播放指定成员的远端视频画面。 |
| [StopRemoteView](#stopremoteview)     | 取消订阅并停止播放远端视频画面。   |
| [UpdateRemoteView](#updateremoteview) | 改变远端用户的视频渲染窗口。       |

### 发送聊天消息接口

| API                                     | 描述             |
|-----|-----|
| [SendChatMessage](#sendchatmessage)     | 发送聊天消息。   |
| [SendCustomMessage](#sendcustommessage) | 发送自定义消息。 |

### 场控相关接口

| API                                                 | 描述                                                    |
|-----|-----|
| [MuteUserMicrophone](#muteusermicrophone)           | 禁用/恢复某用户的麦克风。                               |
| [MuteAllUsersMicrophone](#muteallusersmicrophone)   | 禁用/恢复所有用户的麦克风，并且状态会同步到房间信息中。 |
| [MuteUserCamera](#muteusercamera)                   | 禁用/恢复某用户的摄像头。                               |
| [MuteAllUsersCamera](#mutealluserscamera)           | 禁用/恢复所有用户的摄像头，并且状态会同步到房间信息中。 |
| [MuteChatRoom](#mutechatroom)                       | 开启/停止聊天室禁言（主持人调用）。                     |
| [KickOffUser](#kickoffuser)                         | 移除房间内的某人（主持人调用）。                        |
| [StartCallingRoll](#startcallingroll)               | 主持人开始点名。                                        |
| [StopCallingRoll](#stopcallingroll)                 | 主持人结束点名。                                        |
| [ReplyCallingRoll](#replycallingroll)               | 成员回复主持人点名。                                    |
| [SendSpeechInvitation](#sendspeechinvitation)       | 主持人邀请成员发言。                                    |
| [CancelSpeechInvitation](#cancelspeechinvitation)   | 主持人取消邀请成员发言。                                |
| [ReplySpeechInvitation](#replyspeechinvitation)     | 成员同意/拒绝主持人的申请发言。                         |
| [SendSpeechApplication](#sendspeechapplication)     | 成员申请发言。                                          |
| [CancelSpeechApplication](#cancelspeechapplication) | 成员取消申请发言。                                      |
| [ReplySpeechApplication](#replyspeechapplication)   | 主持人同意/拒绝成员的申请发言。                         |
| [ForbidSpeechApplication](#forbidspeechapplication) | 主持人禁止申请发言。                                    |
| [SendOffSpeaker](#sendoffspeaker)                   | 主持人令成员停止发言。                                  |
| [SendOffAllSpeakers](#sendoffallspeakers)           | 主持人令全体停止发言。                                  |
| [ExitSpeechState](#exitspeechstate)                 | 成员停止发言，转变为观众。                               |

### 基础组件接口函数

| API                                             | 描述                                       |
|-----|-----|
| [GetDeviceManager](#getdevicemanager)           | 获取本地设置管理对象 ITXDeviceManager。    |
| [GetScreenShareManager](#getscreensharemanager) | 获取屏幕分享管理对象 IScreenShareManager。 |

### 云录制接口函数

| API                                   | 描述          |
|-----|-----|
| [StartCloudRecord](#startcloudrecord) | 开始云录制 。 |
| [StopCloudRecord](#stopcloudrecord)   | 停止云录制 。 |

### 美颜相关接口函数

| API | 描述 |
|-----|-----|
| [SetBeautyStyle](#setbeautystyle) | 美颜设置 。|

### 相关设置接口

| API | 描述 |
|-----|-----|
| [SetVideoQosPreference](#setvideoqospreference) | 设置网络流控相关参数。|

### 获取 SDK 版本接口函数

| API | 描述 |
|-----|-----|
| [GetSDKVersion](#getsdkversion) | 获取 SDK 版本。|

## TUIRoomCoreCallback API 概览[](id:TUIRoomCoreCallback)

### 错误事件回调

| API | 描述 |
|-----|-----|
| [OnError](#OnError) | 错误回调。|

### 基础事件回调

| API                                         | 描述               |
|-----|-----|
| [OnLogin](#onlogin)                         | 登录回调。         |
| [OnLogout](#onlogout)                       | 登出回调。         |
| [OnCreateRoom](#oncreateroom)               | 创建房间回调。     |
| [OnDestroyRoom](#ondestroyroom)             | 房间解散回调。     |
| [OnEnterRoom](#onenterroom)                 | 进入房间回调。     |
| [OnExitRoom](#onexitroom)                   | 退出房间回调。     |
| [OnFirstVideoFrame](#onfirstvideoframe)     | 首帧画面回调。     |
| [OnUserVoiceVolume](#onuservoicevolume)     | 音量大小回调回调。 |
| [OnRoomMasterChanged](#onroommasterchanged) | 主持人更改回调。   |

### 远端用户事件回调

| API                                                          | 描述                             |
|-----|-----|
| [OnRemoteUserEnter](#onremoteuserenter)                      | 远端用户进入房间回调。           |
| [OnRemoteUserLeave](#onremoteuserleave)                      | 远端用户离开房间回调。           |
| [OnRemoteUserCameraAvailable](#onremoteusercameraavailable)  | 远端用户是否开启摄像头视频回调。 |
| [OnRemoteUserScreenVideoAvailable](#onremoteuserscreenvideoavailable) | 远端用户是否开启屏幕分享回调。   |
| [OnRemoteUserAudioAvailable](#onremoteuseraudioavailable)    | 远端用户是否开启音频上行回调。   |
| [OnRemoteUserEnterSpeechState](#onremoteuserenterspeechstate) | 远端用户开始发言回调。           |
| [OnRemoteUserExitSpeechState](#onremoteuserexitspeechstate)  | 远端用户结束发言回调。           |

### 消息事件回调

| API                                               | 描述               |
|-----|-----|
| [OnReceiveChatMessage](#onreceivechatmessage)     | 收到文本消息回调。 |
| [OnReceiveCustomMessage](#onreceivecustommessage) | 收到文本消息回调。 |

### 场控事件回调

| API                                                          | 描述                               |
|-----|-----|
| [OnReceiveSpeechInvitation](#onreceivespeechinvitation)      | 用户收到主持人发言邀请回调。       |
| [OnReceiveInvitationCancelled](#onreceiveinvitationcancelled) | 用户收到主持人取消发言邀请回调。   |
| [OnReceiveReplyToSpeechInvitation](#onreceivereplytospeechinvitation) | 主持人收到用户同意邀请发言的回调。 |
| [OnReceiveSpeechApplication](#onreceivespeechapplication)    | 主持人收到用户发言申请的回调。     |
| [OnSpeechApplicationCancelled](#onspeechapplicationcancelled) | 用户取消申请发言回调。             |
| [OnReceiveReplyToSpeechApplication](#onreceivereplytospeechapplication) | 主持人同意发言申请回调。           |
| [OnSpeechApplicationForbidden](#onspeechapplicationforbidden) | 主持人禁止申请发言回调。           |
| [OnOrderedToExitSpeechkState](#onorderedtoexitspeechkstate)  | 成员被请求停止发言的回调。         |
| [OnCallingRollStarted](#oncallingrollstarted)                | 主持人开始点名，成员收到的回调。   |
| [OnCallingRollStopped](#oncallingrollstopped)                | 主持人结束点名，成员收到的回调。   |
| [OnMemberReplyCallingRoll](#onmemberreplycallingroll)        | 成员回复点名，主持人收到的回调。   |
| [OnChatRoomMuted](#onchatroommuted)                          | 主持人更改聊天室是否禁言回调。     |
| [OnMicrophoneMuted](#onmicrophonemuted)                      | 主持人设置禁用麦克风回调。         |
| [OnCameraMuted](#oncameramuted)                              | 主持人设置禁用摄像头回调。         |

### 统计和质量回调

| API | 描述 |
|-----|-----|
| [OnStatistics](#onstatistics)         | 技术指标统计回调。 |
| [OnNetworkQuality](#onnetworkquality) | 网络质量回调。     |

### 屏幕分享相关回调

| API                                               | 描述               |
|-----|-----|
| [OnScreenCaptureStarted](#onscreencapturestarted) | 开始屏幕分享回调。 |
| [OnScreenCaptureStopped](#onscreencapturestopped) | 停止屏幕分享回调。 |

### 视频录制回调

| API                                   | 描述           |
|-----|-----|
| [OnRecordError](#onrecorderror)       | 录制错误回调。 |
| [OnRecordComplete](#onrecordcomplete) | 录制完成回调。 |
| [OnRecordProgress](#onrecordprogress) | 录制进度回调。 |


### 本地设备测试回调

| API                                                          | 描述                   |
|-----|-----|
| [OnTestSpeakerVolume](#ontestspeakervolume)                  | 扬声器大小回调。       |
| [OnTestMicrophoneVolume](#ontestmicrophonevolume)            | 麦克风大小回调。       |
| [OnAudioDeviceCaptureVolumeChanged](#onaudiodevicecapturevolumechanged) | 调节系统采集音量回调。 |
| [OnAudioDevicePlayoutVolumeChanged](#onaudiodeviceplayoutvolumechanged) | 调节系统播放音量回调。 |

## TUIRoomCore 基础函数

### GetInstance

获取 [TUIRoomCore](https://cloud.tencent.com/document/product/647/63494) 单例对象。
```C++
 static TUIRoomCore* GetInstance();
```

### DestroyInstance

```C++
static void DestroyInstance();
```

### SetCallback

[TUIRoomCore](https://cloud.tencent.com/document/product/647/63494) 事件回调，您可以通过 TUIRoomCoreCallback 获得 [TUIRoomCore](https://cloud.tencent.com/document/product/647/63494) 的各种状态通知。

```C++
virtual void SetCallback(const TUIRoomCoreCallback* callback) = 0;
```

### Login

登录。
```C++
virtual int Login(int sdk_appid, const std::string& user_id, const std::string& user_sig) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdk_appid | int |  您可以在实时音视频控制台 >**[应用管理](https://console.cloud.tencent.com/trtc/app)**> 应用信息中查看 SDKAppID。 |
| user_id | string | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| user_sig | string | 腾讯云设计的一种安全保护签名，获取方式请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |

### Logout

登出。
```C++
virtual int Logout() = 0;
```

### CreateRoom

创建房间（主持人调用）。
```C++
virtual int CreateRoom(const std::string& room_id, TUISpeechMode speech_mode) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| room_id | string | 房间标识，需要由您分配并进行统一管理。 |
| speech_mode | TUISpeechMode | 发言模式。 |

主持人正常调用流程如下：
1. **主持人**调用 `CreateRoom()` 创建房间，房间创建成功与否会通过 OnCreateRoom 通知给主持人。
2. **主持人**调用 `EnterRoom()` 进入房间。
3. **主持人**调用 `StartCameraPreview()` 打开摄像头采集和预览。
4. **主持人**调用 `StartLocalAudio()` 打开本地麦克风。

### DestroyRoom

销毁房间房间（主持人调用）。主持人在创建房间后，可以调用该函数来销毁房间。
```C++
virtual int DestroyRoom() = 0;
```

### EnterRoom

进入房间（参会成员调用）。
```C++
virtual int EnterRoom(const std::string& room_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| room_id | string | 房间标识。 |

参会成员进入房间的正常调用流程如下：
1. **参会成员**调用`EnterRoom`并传入 room_id 即可进入房间房间。
2. **参会成员**调用 `startCameraPreview()` 打开摄像头预览，调用 `StartLocalAudio()` 打开麦克风采集。
3. **参会成员**收到`OnRemoteUserCameraAvailable`的事件，调用`StartRemoteView()`开始播放视频。

### LeaveRoom

离开房间（参会成员调用）。
```C++
virtual int LeaveRoom() = 0;
```

### GetRoomInfo

获取房间信息。
```C++
virtual TUIRoomInfo GetRoomInfo() = 0;
```

### GetRoomUsers

获取房间所有成员信息。
```C++
virtual std::vector<TUIUserInfo> GetRoomUsers() = 0;
```

### GetUserInfo

获取房间成员信息。
```C++
virtual const TUIUserInfo* GetUserInfo(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户标识。 |

### SetSelfProfile

设置用户属性。
```C++
virtual int SetSelfProfile(const std::string& user_name, const std::string& avatar_url) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_name | string | 用户姓名。 |
| avatar_url | string | 用户头像 URL。 |

### TransferRoomMaster

将群转交给其他用户。
```C++
virtual int TransferRoomMaster(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户标识。 |

## 本地推流接口

### StartCameraPreview

开始本地摄像头预览。
```C++
virtual int StartCameraPreview(const liteav::TXView& view) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | liteav::TXView | 窗口句柄。 |

### StopCameraPreview

停止本地摄像头预览。
```C++
virtual int StopCameraPreview() = 0;
```

### UpdateCameraPreview

更新本地视频预览画面的窗口。
```C++
virtual int UpdateCameraPreview(const liteav::TXView& view) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | liteav::TXView | 窗口句柄。 |

### StartLocalAudio

打开本地音频设备。
```C++
virtual int StartLocalAudio(const liteav::TRTCAudioQuality& quality) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | liteav::TXView | 窗口句柄。 |

### StopLocalAudio

关闭本地音频设备。
```C++
virtual int StopLocalAudio() = 0;
```

### StartSystemAudioLoopback

开启系统声音的采集。
```C++
virtual int StartSystemAudioLoopback() = 0;
```

### StopSystemAudioLoopback

关闭系统声音的采集。
```C++
virtual int StopSystemAudioLoopback() = 0;
```

### SetVideoMirror

镜像设置。
```C++
virtual int SetVideoMirror(bool mirror) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | bool | 是否镜像。 |

## 远端用户相关接口

### StartRemoteView
订阅远端用户的视频流

```C++
virtual int StartRemoteView(const std::string& user_id, const liteav::TXView& view,
        TUIStreamType type = TUIStreamType::kStreamTypeCamera) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 需要播放的用户 ID。 |
| liteav::TXView | TXView | 承载视频画面的 view 控件。|
| type | TUIStreamType | 流类型。|

### StopRemoteView

取消订阅并停止播放远端视频画面。
```C++
virtual int StopRemoteView(const std::string& user_id,
        TUIStreamType type = TUIStreamType::kStreamTypeCamera) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 需要停止播放的用户 ID。 |
| type | TUIStreamType | 流类型。|

### UpdateRemoteView

更新远端视频渲染窗口。
```C++
virtual int UpdateRemoteView(const std::string& user_id, TUIStreamType type, liteav::TXView& view) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| type | TUIStreamType | 流类型。|
| view | liteav::TXView | 渲染窗口句柄。|

## 发送消息接口

### SendChatMessage

发送文本消息。
```C++
virtual int SendChatMessage(const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | string | 消息内容。 |

### SendCustomMessage

发送自定义消息。
```C++
virtual int SendCustomMessage(const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | string | 消息内容。 |

## 场控相关接口

### MuteUserMicrophone

禁用/恢复某用户的麦克风。
```C++
virtual int MuteUserMicrophone(const std::string& user_id, bool mute, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| mute | bool | 是否禁用。 |
| callback | Callback | 接口回调。 |

### MuteAllUsersMicrophone

禁用/恢复所有用户的麦克风。
```C++
virtual int MuteAllUsersMicrophone(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁用。 |

### MuteUserCamera

禁用/恢复某用户的摄像头。
```C++
virtual int MuteUserCamera(const std::string& user_id, bool mute, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| mute | bool | 是否禁用。 |
| callback | Callback | 接口回调。 |

### MuteAllUsersCamera

禁用/恢复所有用户的摄像头。
```C++
virtual int MuteAllUsersCamera(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁用。 |

### MuteChatRoom

开启/停止聊天室禁言。
```C++
virtual int MuteChatRoom(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁用。 |

### KickOffUser

主持人踢人。
```C++
virtual int KickOffUser(const std::string& user_id, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| callback | Callback | 接口回调。 |

### StartCallingRoll

主持人开始点名。
```C++
virtual int StartCallingRoll() = 0;
```

### StopCallingRoll

主持人结束点名。
```C++
virtual int StopCallingRoll() = 0;
```

### ReplyCallingRoll

成员回复主持人点名。
```C++
virtual int ReplyCallingRoll(Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | Callback | 接口回调。 |

### SendSpeechInvitation

主持人邀请成员发言。
```C++
virtual int SendSpeechInvitation(const std::string& user_id, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| callback | Callback | 接口回调。 |

### CancelSpeechInvitation

主持人取消邀请成员发言。
```C++
virtual int CancelSpeechInvitation(const std::string& user_id, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| callback | Callback | 接口回调。 |

### ReplySpeechInvitation

成员同意/拒绝主持人的发言邀请。
```C++
virtual int ReplySpeechInvitation(bool agree, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| agree | bool | 是否同意。 |
| callback | Callback | 接口回调。 |

### SendSpeechApplication

成员申请发言。
```C++
virtual int SendSpeechApplication(Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | Callback | 接口回调。 |

### CancelSpeechApplication

成员取消申请发言。
```C++
virtual int CancelSpeechApplication(Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | Callback | 接口回调。 |

### ReplySpeechApplication

主持人同意/拒绝成员的申请发言。
```C++
virtual int ReplySpeechApplication(const std::string& user_id, bool agree, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| callback | Callback | 接口回调。 |

### ForbidSpeechApplication

主持人禁止申请发言。
```C++
virtual int ForbidSpeechApplication(bool forbid) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| forbid | bool | 是否禁止。 |

### SendOffSpeaker

主持人令成员停止发言。
```C++
virtual int SendOffSpeaker(const std::string& user_id, Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| callback | Callback | 接口回调。 |

### SendOffAllSpeakers

主持人令所有成员停止发言。
```C++
virtual int SendOffAllSpeakers(Callback callback) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | Callback | 接口回调。 |

### ExitSpeechState

成员停止发言，转变为观众。
```C++
virtual int ExitSpeechState() = 0;
```

## 基础组件接口

### GetDeviceManager

获取设备管理的对象指针。
```C++
virtual liteav::ITXDeviceManager* GetDeviceManager() = 0;
```

### GetScreenShareManager

获取屏幕分享管理的对象指针。
```C++
virtual IScreenShareManager* GetScreenShareManager() = 0;
```

## 云录制接口

### StartCloudRecord

开始云录制。
```C++
virtual int StartCloudRecord() = 0;
```

### StopCloudRecord

停止云录制。
```C++
virtual int StopCloudRecord() = 0;
```

## 美颜相关接口函数

### SetBeautyStyle

设置美颜、美白、红润效果级别。
```C++
virtual int SetBeautyStyle(liteav::TRTCBeautyStyle style, uint32_t beauty_level,
        uint32_t whiteness_level, uint32_t ruddiness_level) = 0;
```

通过美颜管理，您可以使用以下功能：
- 设置“美颜风格”，光滑或者自然，光滑风格磨皮更加明显。
- 设置“美颜级别”，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。
- 设置“美白级别”，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| style | liteav::TRTCBeautyStyle | 美颜风格。 |
| beauty_level | uint32_t | 美颜级别。 |
| whiteness_level | uint32_t | 美白级别。 |
| ruddiness_level | uint32_t | 红润级别。 |

## 相关设置接口

### SetVideoQosPreference

设置网络流控相关参数。
```C++
virtual int SetVideoQosPreference(TUIVideoQosPreference preference) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| preference | TUIVideoQosPreference | 网络流控策略。 |

## 获取 SDK 版本接口

### GetSDKVersion

获取 SDK 版本信息。
```C++
virtual const char* GetSDKVersion() = 0;
```

## 错误事件回调
### OnError

```C++
void OnError(int code, const std::string& message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | string | 错误信息。 |

## 基础事件回调
### OnLogin

```C++
virtual void OnLogin(int code, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | string | 登录信息或登录失败的错误信息。 |

### OnLogout

```C++
virtual void OnLogout(int code, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | string | 错误信息。 |

### OnCreateRoom

创建房间回调。
```C++
virtual void OnCreateRoom(int code, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | string | 错误信息。 |

### OnDestroyRoom

房间解散回调。
```C++
virtual void OnDestroyRoom(int code, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | string | 错误信息。 |

### OnEnterRoom

进入房间回调。
```C++
virtual void OnEnterRoom(int code, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | string | 错误信息。 |

### OnExitRoom

退出房间回调。
```C++
virtual void OnExitRoom(TUIExitRoomType type, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | TUIExitRoomType | 退出房间的类型。 |
| message | string | 错误信息。 |

### OnFirstVideoFrame

开始渲染自己本地或远端用户的首帧画面。
```C++
virtual void OnFirstVideoFrame(const std::string& user_id, const TUIStreamType stream_type) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| stream_type | TUIStreamType | 流类型。 |

### OnUserVoiceVolume

用户音量大小回调。
```C++
virtual void OnUserVoiceVolume(const std::string& user_id, int volume)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| volume | int | 用户的音量大小，取值范围 0 - 100。 |

### OnRoomMasterChanged

主持人更改回调。
```C++
virtual void OnRoomMasterChanged(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

## 远端用户回调事件

### OnRemoteUserEnter

远端用户进入房间回调。
```C++
virtual void OnRemoteUserEnter(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

### OnRemoteUserLeave

远端用户离开房间回调。
```C++
virtual void OnRemoteUserLeave(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

### OnRemoteUserCameraAvailable

远端用户是否开启摄像头视频。
```C++
virtual void OnRemoteUserCameraAvailable(const std::string& user_id, bool available) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| available | bool | true：有视频流数据；false：无视频流数据。 |

### OnRemoteUserScreenVideoAvailable

远端用户是否开启摄像头视频。
```C++
virtual void OnRemoteUserScreenVideoAvailable(const std::string& user_id, bool available) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| available | bool | true：有视频流数据；false：无视频流数据。 |

### OnRemoteUserAudioAvailable

远端用户是否开启摄像头视频。
```C++
virtual void OnRemoteUserAudioAvailable(const std::string& user_id, bool available) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| available | bool | true：有视频流数据；false：无视频流数据。 |

### OnRemoteUserEnterSpeechState

远端用户开始发言。
```C++
virtual void OnRemoteUserEnterSpeechState(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

### OnRemoteUserExitSpeechState

远端用户结束发言。
```C++
virtual void OnRemoteUserExitSpeechState(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |


## 聊天室消息事件回调

### OnReceiveChatMessage

收到文本消息。
```C++
virtual void OnReceiveChatMessage(const std::string& user_id, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| message | string | 文本消息。|

### OnReceiveCustomMessage

收到自定义消息。
```C++
virtual void OnReceiveCustomMessage(const std::string& user_id, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| message | string | 自定义消息。|

## 场控消息回调

### OnReceiveSpeechInvitation

用户收到主持人发言邀请回调。
```C++
virtual void OnReceiveSpeechInvitation() = 0;
```

### OnReceiveInvitationCancelled

用户收到主持人取消发言邀请回调。
```C++
virtual void OnReceiveInvitationCancelled() = 0;
```

### OnReceiveReplyToSpeechInvitation

主持人收到用户同意邀请发言的回调。
```C++
virtual void OnReceiveReplyToSpeechInvitation(const std::string& user_id, bool agree) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| agree | bool | 是否同意。|

### OnReceiveSpeechApplication

主持人收到用户发言申请的回调。
```C++
virtual void OnReceiveSpeechApplication(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

### OnSpeechApplicationCancelled

用户取消申请发言回调。
```C++
virtual void OnSpeechApplicationCancelled(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

### OnReceiveReplyToSpeechApplication

主持人同意发言申请回调。
```C++
virtual void OnReceiveReplyToSpeechApplication(bool agree) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| agree | bool | 是否同意。 |

### OnSpeechApplicationForbidden

主持人禁止申请发言回调。
```C++
virtual void OnSpeechApplicationForbidden(bool forbidden) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| forbidden | bool | 是否禁止。 |

### OnOrderedToExitSpeechkState

成员被请求停止发言的回调。
```C++
virtual void OnOrderedToExitSpeechkState() = 0;
```

### OnCallingRollStarted

主持人开始点名，成员收到的回调。
```C++
virtual void OnCallingRollStarted() = 0;
```

### OnCallingRollStopped

主持人结束点名，成员收到的回调。
```C++
virtual void OnCallingRollStopped() = 0;
```

### OnMemberReplyCallingRoll

成员回复点名，主持人收到的回调。
```C++
virtual void OnMemberReplyCallingRoll(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

### OnChatRoomMuted

主持人更改聊天室是否禁言回调。
```C++
virtual void OnChatRoomMuted(bool muted) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| muted | bool | 是否禁用。 |

### OnMicrophoneMuted

主持人设置禁用麦克风回调。
```C++
virtual void OnMicrophoneMuted(bool muted) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| muted | bool | 是否禁用。 |

### OnCameraMuted

主持人设置禁用摄像头回调。
```C++
virtual void OnCameraMuted(bool muted) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| muted | bool | 是否禁用。 |

## 统计和质量回调

### OnStatistics

技术指标统计回调。
```C++
virtual void OnStatistics(const liteav::TRTCStatistics& statis) {}
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statis | liteav::TRTCStatistics | 统计数据。 |

### OnNetworkQuality

网络状况回调。
```C++
virtual void OnNetworkQuality(const liteav::TRTCQualityInfo& local_quality, liteav::TRTCQualityInfo* remote_quality,
        uint32_t remote_quality_count) {}
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| local_quality | liteav::TRTCQualityInfo | 本地用户质量信息。 |
| remote_quality | liteav::TRTCQualityInfo* | 远端用户质量信息指针。 |
| remote_quality_count | uint32_t | 远端用户数量。 |

## 录屏事件回调

### OnScreenCaptureStarted

开始屏幕分享回调。

```C++
virtual void OnScreenCaptureStarted() {}
```

### OnScreenCaptureStopped

停止屏幕分享回调。

```C++
void OnScreenCaptureStopped(int reason) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| reason | int  | 停止原因，0：用户主动停止；1：被其他应用抢占导致停止。 |

## 视频录制回调

### OnRecordError

录制错误回调。

```C++
virtual void OnRecordError(TXLiteAVLocalRecordError error, const std::string& messgae) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| error | TXLiteAVLocalRecordError  | 错误信息。 |
| messgae | string  | 错误描述。 |

### OnRecordComplete

录制完成回调。

```C++
virtual void OnRecordComplete(const std::string& path) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| path | string  | 错误描述。 |

### OnRecordProgress

录制进度回调。

```C++
virtual void OnRecordProgress(int duration, int file_size) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| duration | int  | 文件的时长。 |
| file_size | int  | 文件的大小。 |

## 本地设备测试回调

### OnTestSpeakerVolume

扬声器音量大小回调。

```C++
virtual void OnTestSpeakerVolume(uint32_t volume) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| volume | uint32_t  | 音量大小。 |

### OnTestMicrophoneVolume

麦克风音量大小回调。

```C++
virtual void OnTestMicrophoneVolume(uint32_t volume) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| volume | uint32_t  | 音量大小。 |

### OnAudioDeviceCaptureVolumeChanged

调节系统采集音量回调。

```C++
virtual void OnAudioDeviceCaptureVolumeChanged(uint32_t volume, bool muted) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| volume | uint32_t  | 音量大小。 |
| muted | bool  | 是否被禁用。 |

### OnAudioDevicePlayoutVolumeChanged

调节系统播放音量回调。

```C++
virtual void OnAudioDevicePlayoutVolumeChanged(uint32_t volume, bool muted) {}
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| volume | uint32_t  | 音量大小。 |
| muted | bool  | 是否被禁用。 |
