TRTCMeeting 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建会议房间，参会人员输入房间号后进入会议。
- 参会人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TRTCMeeting 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人视频会议(Windows)](https://cloud.tencent.com/document/product/647/63494)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时视频会议组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 MeetingRoom 实现会议中聊天室的功能。


[](id:TRTCMeeting)
## TRTCMeeting API 概览

### ITXMediaCore 基础函数

| API | 描述 |
|-----|-----|
| [Instance](#instance) | 获取单例对象。 |
| [DestroyInstance](#destroyinstance) | 销毁单例对象。 |
| [AddCallback](#addcallback) | 设置事件回调。|
| [RemoveCallback](#removecallback) | 移除事件回调。 |
| [Login](#login) | 登录。|
| [Logout](#logout) | 登出。|

### 会议房间相关接口函数

| API | 描述 |
|-----|-----|
| [CreateRoom](#createroom) | 创建会议房间（主持人调用）。|
| [DestroyRoom](#destroyroom) | 销毁会议房间（主持人调用）。|
| [EnterRoom](#enterroom) | 进入会议房间（参会成员调用）。|
| [LeaveRoom](#leaveroom) | 离开会议房间（参会成员或主持人调用）。|
| [GetRoomInfo](#getroominfo) | 获取房间信息。|
| [TransferRoomMasterToOther](#transferroommastertoother) | 转移会议主持人权限（主持人调用）。|

### 远端用户相关接口
| API | 描述 |
|-----|-----|
| [GetRemoteUserInfoList](#getremoteuserinfolist) | 获取房间内所有的人员列表，进入房间成功后调用才有效。|
| [GetRemoteUserInfo](#getremoteuserinfo) | 获取房间内指定人员的详细信息，进入房间成功后调用才有效。|
| [SubscribeRemoteStream](#subscriberemotestream) | 订阅并播放指定成员的远端视频画面。|
| [UnSubscribeRemoteStream](#unsubscriberemotestream) | 取消订阅并停止播放远端视频画面。 |
| [MuteRemoteAudioStream](#muteremoteaudiostream) | 停止/恢复远端用户的音频流数据。 |
| [MuteRemoteVideoStream](#muteremotevideostream) | 停止/恢复远端用户的视频流数据。 |
| [UpdateRemoteView](#updateremoteview) | 改变远端用户的视频渲染窗口。 |

### 本地视频操作接口

| API | 描述 |
|-----|-----|
| [GetLocalUserInfo](#getlocaluserinfo) | 获取本地用户信息。|
| [StartCameraPreview](#startcamerapreview) | 开启本地视频的预览画面。|
| [StopCameraPreview](#stopcamerapreview) | 停止本地视频采集及预览。|
| [UpdateRenderView](#updaterenderview) | 改变本地视频渲染窗口。|
| [PublishVideoStream](#publishvideostream) | 开始推送本地视频流到远端。 |
| [UnPublishVideoStream](#unpublishvideostream) | 停止推送本地视频流到远端。|
| [SetVedioMirror](#setvediomirror) | 设置本地画面镜像预览模式。|

### 本地音频操作接口

| API | 描述 |
|-----|-----|
| [StartMicrophone](#startmicrophone) | 开启麦克风采集。|
| [StopMicrophone](#stopmicrophone) | 停止麦克风采集。|
| [PublishAudioStream](#publishaudiostream) | 推送本地音频数据到远端。|
| [UnPublishAudioStream](#unpublishaudiostream) | 停止推送本地音频数据到远端。|
| [SystemAudioLoopback](#systemaudioloopback) | 开启/关闭系统声音的采集。|

### 场控相关接口
| API | 描述 |
|-----|-----|
| [MuteUserMic](#muteusermic) | 禁用/恢复某用户的麦克风。|
| [MuteUserCamera](#muteusercamera) | 禁用/恢复某用户的摄像头。|
| [MuteAllUsersMic](#muteallusersmic) | 禁用/恢复所有用户的麦克风，并且状态会同步到房间信息中。|
| [MuteAllUsersCamera](#mutealluserscamera) | 禁用/恢复所有用户的摄像头，并且状态会同步到房间信息中。|
| [MuteUserMessage](#muteusermessage) | 禁言/恢复禁言（主持人调用）。|
| [KickOffUser](#kickoffuser) | 移除房间内的某人（主持人调用）。|

### 本地设置相关接口函数

| API | 描述 |
|-----|-----|
| [GetDeviceManager](#getdevicemanager) | 获取本地设置管理对象 ITXDeviceManager。 |
| [SetVideoQosPreference](#setvideoqospreference) | 设置网络流控相关参数。|

### 美颜相关接口函数

| API | 描述 |
|-----|-----|
| [SetBeautyStyle](#setbeautystyle) | 美颜设置 。|

### 屏幕分享相关接口

| API | 描述 |
|-----|-----|
| [GetScreenShareManager](#getscreensharemanager) | 获取屏幕分享管理对象 IScreenShareManager。 |
|[StartScreenCapture](#startscreencapture)|启动屏幕分享。|
|[StopScreenCapture](#stopscreencapture)|停止屏幕采集。|
|[PauseScreenCapture](#pausescreencapture)|暂停屏幕分享。|
|[ResumeScreenCapture](#resumescreencapture)|恢复屏幕分享。|
|[GetScreenCaptureSources](#getscreencapturesources)|获取所有窗口的小图和图标，用于屏幕分享时的选择。|
|[ReleaseScreenCaptureSources](#releasescreencapturesources)|释放窗口列表资源。|
|[SelectScreenCaptureTarget](#selectscreencapturetarget)|置屏幕分享参数，该方法在屏幕分享过程中也可以调用。|
|[AddExcludedShareWindow](#addexcludedsharewindow)|将指定窗口加入屏幕分享的排除列表中，加入排除列表中的窗口不会被分享出去。|
|[RemoveAllExcludedShareWindow](#removeallexcludedsharewindow)|将所有窗口从屏幕分享的排除列表中移除。|


### 消息发送相关接口函数

| API | 描述 |
|-----|-----|
| [SendChatMessage](#sendchatmessage) | 在房间中广播文本消息，用于聊天。|

[](id:TXMediaCoreCallback)
## TXMediaCoreCallback API 概览

### 通用事件回调

| API | 描述 |
|-----|-----|
| [onError](#onerror) | 错误回调。|
| [OnLogin](#onlogin) | 登录回调。|
| [OnLogout](#onlogout) | 登出回调。|

### 会议房间事件回调

| API | 描述 |
|-----|-----|
| [OnCreateRoom](#oncreateroom) | 创建房间回调。|
| [OnDestroyRoom](#ondestroyroom)     | 房间解散回调。   |
| [OnEnterRoom](#onenterroom) | 进入房间回调。|
| [OnExitRoom](#onexitroom) | 退出房间回调。|
| [OnRoomMasterChanged](#onroommasterchanged) | 主持人更改回调。|

### 成员进出事件回调

| API | 描述 |
|-----|-----|
| [OnRemoteUserEnterRoom](#onremoteuserenterroom) | 远端用户进入房间回调。|
| [OnRemoteUserLeaveRoom](#onremoteuserleaveroom) | 远端用户离开房间回调。|

### 成员音视频事件回调

| API | 描述 |
|-----|-----|
| [OnFirstVideoFrame](#onfirstvideoframe) | 开始渲染自己本地或远端用户的首帧画面回调。|
| [OnUserVoiceVolume](#onuservoicevolume) | 用户音量大小回调通知。|
| [OnRemoteUserVideoAvailable](#onremoteuservideoavailable) | 远端用户是否开启摄像头视频回调。|
| [OnRemoteUserAudioAvailable](#onremoteuseraudioavailable) | 远端用户是否开启音频上行回调。|
| [OnRemoteUserScreenVideoAvailable](#onremoteuserscreenvideoavailable) | 远端用户是否开启屏幕分享回调。|

### 场控事件回调

| API | 描述 |
|-----|-----|
| [OnMuteMic](#onmutemic) | 主持人设置禁用麦克风回调。|
| [OnMuteCamera](#onmutecamera) | 主持人设置禁用摄像头回调。|

### 消息事件回调

| API | 描述 |
|-----|-----|
| [OnRecevieChatMessage](#onreceviechatmessage) | 收到文本消息回调。|
| [OnMuteChatMessage](#onmutechatmessage) | 主持人更改聊天室是否禁言回调。|

### 统计和质量回调

| API | 描述 |
|-----|-----|
| [OnStatistics](#onstatistics) | 技术指标统计回调。|
| [OnNetworkQuality](#onnetworkquality) | 网络质量回调。|

### 录屏事件回调

| API | 描述 |
|-----|-----|
| [OnScreenCaptureStarted](#onscreencapturestarted) | 开始屏幕分享回调。|
| [OnScreenCaptureStopped](#onscreencapturestopped) |停止屏幕分享回调。|


### 本地设备测试回调

| API | 描述 |
|-----|-----|
| [OnTestSpeakerVolume](#ontestspeakervolume) | 扬声器大小回调。|
| [OnTestMicVolume](#ontestmicvolume) | 麦克风大小回调。|
| [OnAudioDeviceCaptureVolumeChanged](#onaudiodevicecapturevolumechanged) | 调节系统采集音量回调。|
| [OnAudioDevicePlayoutVolumeChanged](#onaudiodeviceplayoutvolumechanged) | 调节系统播放音量回调。|

## ITXMediaCore 基础函数


### Instance

获取 [TRTCMeeting](https://cloud.tencent.com/document/product/647/63494) 单例对象。
```C++
 static ITXMediaCore* Instance();
```

### DestroyInstance

```C++
static void DestroyInstance();
```

### AddCallback

[TRTCMeeting](https://cloud.tencent.com/document/product/647/63494) 事件回调，您可以通过 TXMediaCoreCallback 获得 [TRTCMeeting](https://cloud.tencent.com/document/product/647/63494) 的各种状态通知。

```C++
virtual void AddCallback(const TXMediaCoreCallback* callback) = 0;
```

### RemoveCallback

```C++
virtual void RemoveCallback(const TXMediaCoreCallback* callback) = 0;
```

### Login

登录。
```C++
virtual int Login(const int& sdk_appid, const std::string& user_id, const std::string& user_sig) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdk_appid | int | 您可以在 **实时音视频控制台>[应用管理](https://console.cloud.tencent.com/trtc/app)>应用信息** 中查看 SDKAppID。 |
| user_id | string | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| user_sig | string | 腾讯云设计的一种安全保护签名，获取方式请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |

### Logout

登出。
```C++
virtual int Logout() = 0;
```

### SetUserName

设置用户名称。
```C++
virtual void SetUserName(const std::string& user_name) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_name | string | 昵称。 |

## 会议房间相关接口函数
### CreateRoom

创建会议（主持人调用）。
```C++
virtual int CreateRoom(const std::string& room_id, TXSpeechMode speech_mode) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| room_id | int | 会议房间标识，需要由您分配并进行统一管理。 |
| speech_mode | TXSpeechMode | 发言模式。 |

主持人正常调用流程如下：
1. **主持人**调用 `CreateRoom()` 创建会议，会议房间创建成功与否会通过 OnCreateRoom 通知给主持人。
2. **主持人**调用 `EnterRoom()` 进入房间。
3. **主持人**调用 `StartCameraPreview()` 打开摄像头采集和预览。
4. **主持人**调用 `PublishVideoStream()` 推送本地流到远端。
5. **主持人**调用 `StartMicrophone()` 打开本地麦克风。
6. **主持人**调用 `PublishAudioStream()` 推送本地音频数据到远端。

### DestroyRoom

销毁会议房间（主持人调用）。主持人在创建会议后，可以调用该函数来销毁会议。
```C++
virtual int DestroyRoom(const std::string& room_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| room_id | int | 会议房间标识，需要由您分配并进行统一管理。 |

### EnterRoom

进入会议（参会成员调用）。
```C++
virtual int EnterRoom(const std::string& room_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| room_id | int | 会议房间标识。 |

参会成员进入会议的正常调用流程如下：
1. **参会成员**调用`EnterRoom` 并传入 room_id 即可进入会议房间。
2. **参会成员**调用 `startCameraPreview()` 打开摄像头预览，调用 `startMicrophone()` 打开麦克风采集。
3. **参会成员**调用 `PublishVideoStream()` 推送本地流到远端，调用 `PublishAudioStream()` 推送本地音频数据到远端。
4. **参会成员**收到 `OnRemoteUserVideoAvailable` 的事件，调用`SubscribeRemoteStream()`开始播放视频。
5. **参会成员**收到 `OnRemoteUserAudioAvailable` 的事件，调用 `MuteRemoteAudioStream()` 开始播放声音。

### LeaveRoom

离开会议（参会成员调用）。
```C++
virtual int LeaveRoom() = 0;
```

### GetRoomInfo

获取房间信息。
```C++
virtual TXRoomInfo GetRoomInfo() = 0;
```

### TransferRoomMasterToOther

将群转交给其他用户。
```C++
virtual int TransferRoomMasterToOther(const std::string& user_id) = 0;
```


## 远端用户相关接口

### GetRemoteUserInfoList

获取房间内所有的人员列表，EnterRoom() 成功后调用才有效。


```C++
virtual std::vector<TXUserInfo> GetRemoteUserInfoList() = 0;
```

### GetRemoteUserInfo

获取房间内指定人员的详细信息，EnterRoom() 成功后调用才有效。
```C++
virtual const TXUserInfo* GetRemoteUserInfo(std::string user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。|

### SubscribeRemoteStream

订阅并播放指定成员的远端视频画面。在 `OnRemoteUserVideoAvailable()` 的 available 为 true 回调时，调用该接口。
```C++
virtual int SubscribeRemoteStream(const std::string& user_id, const trtc::TXView& view,
        TXStreamType type = TXStreamType::kStreamTypeVideo) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 需要播放的用户 ID。|
| view | TXView | 承载视频画面的 view 控件。|
| type | TXStreamType | 流类型。|

### UnSubscribeRemoteStream

取消订阅并停止播放远端视频画面。
```C++
virtual int UnSubscribeRemoteStream(const std::string& user_id,
        TXStreamType type = TXStreamType::kStreamTypeVideo) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 需要停止播放的用户 ID。|
| type | TXStreamType | 流类型。|

### MuteRemoteAudioStream

订阅/取消订阅远端用户的音频流。
```C++
virtual int MuteRemoteAudioStream(const std::string& user_id, const bool& mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。|
| mute | bool  | 订阅或取消订阅 |

### MuteRemoteVideoStream

停止/恢复远端用户的视频流数据。
```C++
virtual int MuteRemoteVideoStream(const std::string& user_id, const bool& mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| mute | int  | 停止或恢复 |

### UpdateRemoteView

更新远端视频渲染窗口。
```C++
virtual int UpdateRemoteView(const std::string& user_id, TXStreamType type, trtc::TXView& view) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| type | TXStreamType | 流类型。|
| view | TXView | 渲染窗口句柄。|

## 本地视频操作接口
### GetLocalUserInfo

获取本地用户的信息。
```C++
virtual const TXUserInfo& GetLocalUserInfo() = 0;
```


### StartCameraPreview

开启本地视频的预览画面。
```C++
virtual int StartCameraPreview(const trtc::TXView& view) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TXView | 承载视频画面的控件。 |



### StopCameraPreview

停止本地视频采集及预览。
```C++
virtual int StopCameraPreview() = 0;
```



### UpdateRenderView

更新本地视频预览窗口句柄。
```C++
virtual int UpdateRenderView(const trtc::TXView& view) = 0;
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TXView | 承载视频画面的控件。 |


### PublishVideoStream

推送本地视频流到远端。

```C++
virtual int PublishVideoStream() = 0;
```
### UnPublishVideoStream

停止推送本地的视频数据到远端。
```C++
virtual int UnPublishVideoStream() = 0;
```
### SetVedioMirror

设置本地画面镜像预览模式。
```C++
virtual void SetVedioMirror(bool is_mirror)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| is_mirror | bool | 是否镜像模式。true：镜像翻转；false：不翻转。 |

## 本地音频操作接口

### StartMicrophone

开启麦克风采集。
```C++
virtual int StartMicrophone(const trtc::TRTCAudioQuality& quality) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | TRTCAudioQuality | 音频质量。|

### StopMicrophone

停止麦克风采集。
```C++
virtual int StopMicrophone() = 0;
```

### PublishAudioStream

开始推送本地的音频数据到远端。
```C++
virtual int PublishAudioStream() = 0;
```

### UnPublishAudioStream

取消推送本地音频流到远端。
```C++
virtual int UnPublishAudioStream() = 0;
```

### SystemAudioLoopback

开启/关闭系统声音的采集。
```C++
virtual int SystemAudioLoopback(bool start_up = true) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| start_up | bool | 是否上行采集的系统声音。true：开始上行采集的系统声音，默认为 true； false：停止上行采集的系统声音。 |

## 场控相关接口

禁用/恢复某用户的麦克风。
### MuteUserMic

```C++
virtual int MuteUserMic(const std::string& user_id, bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户ID。 |
| mute | bool | 是否禁用某用户麦克风：true：禁用麦克风；false：恢复使用麦克风。 |

### MuteUserCamera
禁用/恢复某用户的摄像头。

```C++
virtual int MuteUserCamera(const std::string& user_id, bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户ID。 |
| mute | bool | 是否禁用某用户摄像头：true：禁用摄像头；false：恢复使用摄像头。 |

### MuteAllUsersMic
禁用/恢复所有用户的麦克风，并且状态会同步到房间信息中。

```C++
virtual int MuteAllUsersMic(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁用所有用户的麦克风：true：禁用麦克风；false：恢复使用麦克风。 |

### MuteAllUsersCamera
禁用/恢复所有用户的摄像头，并且状态会同步到房间信息中。

```C++
virtual int MuteAllUsersCamera(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁用所有用户的摄像头：true：禁用摄像头；false：恢复使用摄像头。 |

### MuteUserMessage
禁言/恢复禁言（主持人调用）。

```C++
virtual int MuteUserMessage(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁言：true：禁言；false：不禁言。 |

### KickOffUser
移除房间内的某人（主持人调用）。

```C++
virtual int KickOffUser(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户ID。 |

## 本地设置相关接口函数
### GetDeviceManager
获取本地设置管理对象 ITXDeviceManager。

```C++
virtual trtc::ITXDeviceManager* GetDeviceManager() = 0;
```

### SetVideoQosPreference
设置网络流控相关参数。

```C++
virtual void SetVideoQosPreference(TXVideoQosPreference preference)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| preference | TXVideoQosPreference | “保清晰”还是“保流畅”，可参考 TXVideoQosPreference 接口。 |

## 美颜相关接口函数
### SetBeautyStyle

```C++
virtual void SetBeautyStyle(trtc::TRTCBeautyStyle style, uint32_t beauty_level,
        uint32_t whiteness_level, uint32_t ruddiness_level) = 0;
```

通过美颜管理，您可以使用以下功能：
- 设置“美颜风格”，光滑或者自然，光滑风格磨皮更加明显。
- 设置“美颜级别”，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。
- 设置“美白级别”，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。

## 屏幕分享相关接口
### GetScreenShareManager

获取屏幕分享管理对象 IScreenShareManager。
```C++
virtual IScreenShareManager* GetScreenShareManager() = 0;
```

### StartScreenCapture

启动屏幕分享。
```C++
virtual void StartScreenCapture(void* view) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TXView | 要分享出去的窗口句柄。 |

### StopScreenCapture

停止屏幕采集。
```C++
virtual void StopScreenCapture() = 0;
```

### PauseScreenCapture

暂停屏幕分享。
```C++
virtual void PauseScreenCapture() = 0;
```

### ResumeScreenCapture

恢复屏幕分享。
```C++
virtual void ResumeScreenCapture() = 0;
```

### GetScreenCaptureSources

获取所有窗口的小图和图标，用于屏幕分享时的选择。
```C++
virtual std::vector<ScreenCaptureSourceInfo>& GetScreenCaptureSources(const SIZE& thumb_size,
        const SIZE& icon_size) = 0;
```

返回值如下表所示：

| 返回值 | 类型 | 含义 |
|-----|-----|-----|
| thumb_size  | SIZE  | 指定要获取的窗口缩略图大小，缩略图可用于绘制在窗口选择界面上。 |
| icon_size  | SIZE  | 定要获取的窗口图标大小。 |

### ReleaseScreenCaptureSources

释放窗口列表资源。
```C++
virtual void ReleaseScreenCaptureSources() = 0;
```

### SelectScreenCaptureTarget

置屏幕分享参数，该方法在屏幕分享过程中也可以调用。
```C++
virtual void SelectScreenCaptureTarget(const ScreenCaptureSourceInfo& source, const RECT& capture_rect) = 0;
```

返回值如下表所示：

| 返回值 | 类型 | 含义 |
|-----|-----|-----|
| source  | ScreenCaptureSourceInfo  | 指定分享源。 |
| capture_rect  | RECT  | 指定捕获的区域。 |

### AddExcludedShareWindow

将指定窗口加入屏幕分享的排除列表中，加入排除列表中的窗口不会被分享出去。
```C++
virtual void AddExcludedShareWindow(void* window) = 0;
```

返回值如下表所示：

| 返回值 | 类型 | 含义 |
|-----|-----|-----|
| window  | void*  | 不希望分享出去的窗口句柄。 |

### RemoveAllExcludedShareWindow

将所有窗口从屏幕分享的排除列表中移除。
```C++
virtual void RemoveAllExcludedShareWindow() = 0;
```

## 消息发送相关接口函数
### SendChatMessage

在房间中广播文本消息。
```C++
virtual int SendChatMessage(const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | string | 文本消息。 |

[](id:TXMediaCoreCallback)

## TXMediaCoreCallback 事件回调

## 通用事件回调
### onError

```C++
void onError(int code, string message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | string | 错误信息。 |

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


## 会议房间事件回调
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
virtual void OnExitRoom(TXExitRoomType code, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | TXExitRoomType | 错误码，0：正常退出，1：踢出房间，2：房间解散，3：其他端登录挤下线，4：网络异常。 |
| message | string | 错误信息。 |

### OnRoomMasterChanged

主持人更改回调。
```C++
virtual void OnRoomMasterChanged(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | TXExitRoomType | 错误码，0：正常退出，1：踢出房间，2：房间解散，3：其他端登录挤下线，4：网络异常。 |
| message | string | 错误信息。 |

## 成员进出事件回调
### OnRemoteUserEnterRoom

远端用户进入房间回调。
```C++
virtual void OnRemoteUserEnterRoom(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |

### OnRemoteUserLeaveRoom

远端用户离开房间回调。
```C++
virtual void OnRemoteUserLeaveRoom(const std::string& user_id) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |


## 成员音视频事件回调
### OnFirstVideoFrame

开始渲染自己本地或远端用户的首帧画面。
```C++
virtual void OnFirstVideoFrame(const std::string& user_id, const TXStreamType stream_type) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| stream_type | TXStreamType | 流类型。 |


### OnUserVoiceVolume

用户音量大小回调通知。
```C++
virtual void OnUserVoiceVolume(const std::string& user_id, int volume)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| volume | int | 用户的音量大小，取值范围 0 - 100。 |

### OnRemoteUserVideoAvailable

远端用户是否开启摄像头视频。
```C++
virtual void OnRemoteUserVideoAvailable(const std::string& user_id, bool available) = 0;
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


### 场控事件回调
### OnMuteMic
主持人设置禁用麦克风回调。
```C++
virtual void OnMuteMic(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁用麦克风：true：禁用麦克风；false：恢复使用麦克风。 |

### OnMuteCamera
主持人设置禁用摄像头回调。
```C++
virtual void OnMuteCamera(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁用摄像头：true：禁用摄像头；false：恢复使用摄像头。 |


## 消息事件回调
### OnRecevieChatMessage

收到文本消息。
```C++
virtual void OnRecevieChatMessage(const std::string& user_id, const std::string& message) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | string | 用户 ID。 |
| message | string | 文本消息。|

### OnMuteChatMessage

主持人更改聊天室是否禁言回调。
```C++
virtual void OnMuteChatMessage(bool mute) = 0;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否禁言：true：禁言；false：不禁言。 |

## 统计和质量回调
### OnStatistics

技术指标统计回调。
```C++
virtual void OnStatistics(const trtc::TRTCStatistics& statis)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statis | TRTCStatistics | 网络和性能的汇总统计指标。 |

### OnNetworkQuality

网络质量回调。
```C++
virtual void OnNetworkQuality(const trtc::TRTCQualityInfo& local_quality, trtc::TRTCQualityInfo* remote_quality,
        uint32_t remote_quality_count)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| local_quality | TRTCQualityInfo | 本地上行网络质量。 |
| remote_quality | TRTCQualityInfo | 下行网络质量（即远端用户的网络质量）。 |
| remote_quality_count | int | 下行网络质量的数组大小（即远端用户个数）。 |

## 录屏事件回调

### OnScreenCaptureStarted

开始屏幕分享回调。
```C++
virtual void OnScreenCaptureStarted()
```

### OnScreenCaptureStopped

停止屏幕分享回调。
```C++
void OnScreenCaptureStopped(int reason);
```

参数如下表所示：

| 参数   | 类型 | 含义 |
| ------ | ---- | -------------------------------- |
| reason | int  | 停止原因，0：用户主动停止；1：被其他应用抢占导致停止。 |

## 本地设备测试回调
### OnTestSpeakerVolume

扬声器大小回调。
```C++
virtual void OnTestSpeakerVolume(uint32_t volume)
```

参数如下表所示：

| 参数   | 类型 | 含义 |
| ------ | ---- | -------------------------------- |
| volume | int | 用户的音量大小，取值范围 0 - 100。 |

### OnTestMicVolume

麦克风大小回调。
```C++
virtual void OnTestMicVolume(uint32_t volume)
```

参数如下表所示：

| 参数   | 类型 | 含义 |
| ------ | ---- | -------------------------------- |
| volume | int | 用户的音量大小，取值范围 0 - 100。 |

### OnAudioDeviceCaptureVolumeChanged

调节系统采集音量回调。
```C++
virtual void OnAudioDeviceCaptureVolumeChanged(uint32_t volume, bool muted)
```

参数如下表所示：

| 参数   | 类型 | 含义 |
| ------ | ---- | -------------------------------- |
| volume | int | 采集音量大小，取值范围 0 - 100。 |
| muted | bool | 是否采集。 |

### OnAudioDevicePlayoutVolumeChanged

调节系统播放音量回调。
```C++
virtual void OnAudioDevicePlayoutVolumeChanged(uint32_t volume, bool muted)
```

参数如下表所示：

| 参数   | 类型 | 含义 |
| ------ | ---- | -------------------------------- |
| volume | int | 播放音量大小，取值范围 0 - 100。 |
| muted | bool | 是否播放。 |
