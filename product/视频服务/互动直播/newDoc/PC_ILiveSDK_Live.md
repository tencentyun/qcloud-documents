# iLiveSDK直播流程图：

![](http://mc.qcloudimg.com/static/img/06d2fb5027be53492249d4b81bd2f5a5/image.png)

# 1 设置基本回调函数
在初始化SDK前，需要设置几个基本的回调函数

* 示例:

```c++
void :OnLocalVideo( VideoFrame* video_frame, void* custom_data )
{
	//video_frame是本地画面每一帧的数据,用户需要显示本地画面时，在此回调函数中做渲染，渲染代码可参考随心播;
}
void OnRemoteVideo( VideoFrame* video_frame, void* custom_data )
{
	//video_frame是远程画面每一帧的数据,用户需要显示远程画面时，在此回调函数中做渲染，渲染代码可参考随心播;
}
iLiveSDK::getInstance()->SetMessageCallBack(&messageCallBack); //收到IM消息的回调;
iLiveSDK::getInstance()->setLocalVideoCallBack(OnLocalVideo, NULL); //设置本地视频的回调函数;
iLiveSDK::getInstance()->setRemoteVideoCallBack(OnRemoteVideo, NULL); //设置远程视频的回调函数;
```

# 2 初始化iLiveSDK
在应用启动时初始化iLiveSDK。

|接口名|接口描述|
|---|---|
|initSdk|iLiveSDK内部初始化，告知appId.|

|参数类型|参数名|说明|
|---|---|---|
|int|appId|传入业务方appid|
|int|accountType|传入业务方 accountType|

* 示例：

```c++
int nRet = iLiveSDK::getInstance()->initSdk(appid, AccountType);
if (nRet != ilivesdk::NO_ERR)
{
	//初始化失败
}
```

# 3 账号登录
PC版iLiveSDK目前仅支持独立模式。

|接口名|接口描述|
|---|---|
|iLiveLogin|独立模式登录到腾讯云后台|

|参数类型|参数名|说明|
|---|---|---|
|string |szUserId|用户在独立模式下注册的帐号|
|string |szUserSig|用户在业务方后台获取到的签名|
|SuccessCalllback|suc|登录成功回调|
| ErrorCallback |err|登录失败回调|
|  void * |data |用户自定义的数据的指针，在成功和失败的回调函数中原封不动地返回 |

* 示例：

```c++
void OniLiveLoginSuccess( void* data )
{
	//登录成功
}
void OniLiveLoginError( int code, const std::string& desc, void* data )
{
	//登录失败
}
iLiveSDK::getInstance()->LiveLogin(userId, userSig, OniLiveLoginSuccess, OniLiveLoginError, NULL);
```

# 4 创建房间(主播)

|接口名|接口描述|
|---|---|
|createRoom |主播创建直播间|

|参数类型|参数名|说明|
|---|---|---|
| iLiveRoomOption|roomOption|主播创建房间时的配置项|
| SuccessCalllback|suc|创建房间成功回调|
| ErrorCallback |err|创建房间失败回调|
| void * |data |用户自定义的数据的指针，在成功和失败的回调函数中原封不动地返回|

* 示例：

```c++
void OniLiveCreateRoomSuc( void* data )
{
	//创建房间成功
}
void OniLiveCreateRoomErr( int code, const std::string& desc, void* data )
{
	//创建房间失败
}

iLiveRoomOption roomOption;
roomOption.roomId = roomnum;//业务侧许保证房间id唯一性
roomOption.auth_buffer = "";
roomOption.control_role = "";//留空表示使用默认角色
roomOption.audio_category = AUDIO_CATEGORY_MEDIA_PLAY_AND_RECORD;//直播场景
roomOption.video_recv_mode = VIDEO_RECV_MODE_SEMI_AUTO_RECV_CAMERA_VIDEO; //半自动模式
roomOption.m_roomDisconnectListener = OnRoomDisconnect;
roomOption.m_memberStatusListener = OnMemStatusChange;
roomOption.m_autoRecvListener = OnSemiAutoRecvCameraVideo;
roomOption.data = NULL;
iLiveSDK::getInstance()->createRoom( roomOption, OniLiveCreateRoomSuc, OniLiveCreateRoomErr, NULL );
```

# 5 加入房间(观众)

|接口名|接口描述|
|---|---|
|joinRoom |观众进入直播间|

|参数类型|参数名|说明|
|---|---|---|
|iLiveRoomOption|roomOption|观众进入房间时的配置项|
| SuccessCalllback|suc|加入房间成功回调|
| ErrorCallback |err|加入房间失败回调|
| void * |data |用户自定义的数据的指针，在成功和失败的回调函数中原封不动地返回|

* 示例：

```c++
void OniLiveJoinRoomSuc( void* data )
{
	//加入房间成功
}
void OniLiveJoinRoomErr( int code, const std::string& desc, void* data )
{
	//加入房间失败
}

iLiveRoomOption roomOption;
roomOption.roomId = roomnum;//要加入的房间ID	
roomOption.auth_buffer = "";
roomOption.control_role = "";
roomOption.audio_category = AUDIO_CATEGORY_MEDIA_PLAY_AND_RECORD;//直播场景
roomOption.video_recv_mode = VIDEO_RECV_MODE_SEMI_AUTO_RECV_CAMERA_VIDEO; //半自动模式
roomOption.m_autoRecvListener = OnSemiAutoRecvCameraVideo;
roomOption.m_memberStatusListener = OnMemStatusChange;
roomOption.m_roomDisconnectListener = OnRoomDisconnect;
roomOption.data = NULL;
iLiveSDK::getInstance()->joinRoom( roomOption, OniLiveJoinRoomSuc, OniLiveJoinRoomErr, NULL );
```

