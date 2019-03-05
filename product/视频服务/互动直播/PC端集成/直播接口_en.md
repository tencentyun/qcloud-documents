## ILVB Procedure

The audio/video messaging capabilities of iLiveSDK are abstracted as a "room". A member can watch the videos of other members within the same room, and a maximum of 4 parallel video streams are allowed in a room. iLiveSDK (Windows) provides room management, audio/video device management and other features to allow users to set up interactive videos. The business process of ILVB is as follows:


![Basic Procedure of ILVB](http://mc.qcloudimg.com/static/img/06d2fb5027be53492249d4b81bd2f5a5/image.png)

## Set Callback Functions
iLiveSDK reports statuses and notifications to the upper layer through callback functions, which you can set based on your business needs.

```c++
void onForceOffline()
{
//The account has logged in on another terminal
}
void OnMessage( const Message& msg )
{
}
void OnLocalVideo( LiveVideoFrame* video_frame, void* custom_data )
{
	//video_frame is the data of each frame of local video view. To display a local video view, render the view using this callback function. Please see FreeShow for the rendering code;
}
void OnRemoteVideo( LiveVideoFrame* video_frame, void* custom_data )
{
	//video_frame is the data of each frame of remote video view. To display a remote video view, render the view using this callback function. Please see FreeShow for the rendering code;
}
GetILive()->setForceOfflineCallback(onForceOffline); //Set the notification function indicating a status of being forced offline;
GetILive()->setMessageCallBack(OnMessage); //Set the handling function for messages;
GetILive()->setLocalVideoCallBack(OnLocalVideo, NULL); //Set the callback function for local video;
GetILive()->setRemoteVideoCallBack(OnRemoteVideo, NULL); //Set the callback function for remote video;
```

## Initialization
iLiveSDK must be initialized before you use other features.

| API | Description |
|---|---|
| init | Internal initialization of iLiveSDK (AppId is indicated). |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| int | appId | appid of business side |
| int | accountType | accountType of business side |
| bool | IMSupport | Whether IM feature is needed |

Example:
```c++
int nRet = GetILive()->init(appid, AccountType);
if (nRet != NO_ERR)
{
	//Initialization failed
}
```

## Login
You can use messaging, interactive video and other features only after login. User ID and signature are required for login. Signature is provided by [Tencent Login Service](https://cloud.tencent.com/document/product/269/1507).

| API | Description |
|---|---|
| login | Log in to Tencent Cloud backend in standalone mode |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| const char * | userId | Account registered by user in standalone mode |
| const char * | userSig | The signature obtained by the user at the business backend |
| iLiveSuccCallback | suc | Callback indicating a successful login |
| iLiveErrCallback | err | Callback indicating a failure of login |
| void* | data | A pointer for user's custom data, which is returned intact in the callback function indicating success or failure |

* Example:
```c++
void OniLiveLoginSuccess( void* data )
{
	//Logged in successfully
}
void OniLiveLoginError( int code, const char *desc, void* data )
{
	//Login failed
}
GetILive()->login(userId, userSig, OniLiveLoginSuccess, OniLiveLoginError, NULL);
```

## Audio/Video Permission Management

At business layer, the focus is placed on the audio/video permissions of room members. Only VJs or the viewers who need to join the broadcasting are granted the permission to send upstream audio and video. Before joining or creating a room, you need to enter the correct permission (see "Join/Create a Room" below). Members are allowed to change their permissions in the room.
You can go to [Tencent Cloud Console](https://github.com/zhaoyang21cn/suixinbo_doc/blob/master/SPEARConfig.md) to configure the roles and relevant permissions to meet your business needs. Tencent CVMs assign different [access machines](https://cloud.tencent.com/document/product/268/7651) based on the permissions of room members. Incorrectly configured permissions can cause unnecessary bandwidth costs and abnormal upstream data at viewer end.

## Create a Room

| API | Description |
|---|---|
| createRoom | VJ creates a live room |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| const iLiveRoomOption & | roomOption | Options configured when VJ creates a room |
| iLiveSuccCallback | suc | Callback indicating a successful creation of room |
| iLiveErrCallback | err | Callback indicating a failure to create the room |
| void* | data | A pointer for user's custom data, which is returned intact in the callback function indicating success or failure |

* Example:

```c++
void OniLiveCreateRoomSuc( void* data )
{
	//Room created successfully
}
void OniLiveCreateRoomErr( int code, const char *desc, void* data )
{
	//Failed to create room
}

iLiveRoomOption roomOption;
roomOption.audioCategory = AUDIO_CATEGORY_MEDIA_PLAY_AND_RECORD;//ILVB scenario
roomOption.roomId = 123456;
roomOption.controlRole = "LiveMaster";
roomOption.authBits = AUTH_BITS_DEFAULT;//Pay attention to permission management
roomOption.roomDisconnectListener = OnRoomDisconnect;//Custom callback indicating room disconnection
roomOption.memberStatusListener = OnMemStatusChange;//Custom callback indicating change of member status
roomOption.data = this;
GetILive()->createRoom( roomOption, OniLiveCreateRoomSuc, OniLiveCreateRoomErr, this );
```


# 5 Join the Room (viewer)

| API | Description |
|---|---|
| joinRoom | Viewer joins the live room |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| iLiveRoomOption | roomOption | Options configured when the viewer joins a room |
| SuccessCalllback | suc | Callback indicating the success of joining the room |
| ErrorCallback | err | Callback indicating the failure to join the room |
| void* | data | A pointer for user's custom data, which is returned intact in the callback function indicating success or failure |

* Example:

```c++
void OniLiveJoinRoomSuc( void* data )
{
	//Joined the room successfully
}
void OniLiveJoinRoomErr( int code, const std::string& desc, void* data )
{
	//Failed to join the room
}

iLiveRoomOption roomOption;
roomOption.audioCategory = AUDIO_CATEGORY_MEDIA_PLAY_AND_RECORD;//ILVB scenario
roomOption.roomId = 123456;
roomOption.controlRole = "Guest";
roomOption.authBits = AUTH_BITS_JOIN_ROOM|AUTH_BITS_RECV_AUDIO|AUTH_BITS_RECV_CAMERA_VIDEO|AUTH_BITS_RECV_SCREEN_VIDEO;//Pay attention to permission management
roomOption.memberStatusListener = Live::OnMemStatusChange;//Custom callback indicating change of member status
roomOption.roomDisconnectListener = Live::OnRoomDisconnect;//Custom callback indicating room disconnection
roomOption.data = g_pMainWindow->getLiveView();
GetILive()->joinRoom( roomOption, OniLiveJoinRoomSuc, OniLiveJoinRoomErr, this );
```


