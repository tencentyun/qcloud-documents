## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides an overview that makes it easy for Unity developers to debug and integrate the APIs for Game Multimedia Engine.


## How to Use
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)


### Key considerations for using GME

This document only provides the most important APIs to help you get started with GME. For more APIs, see [API Documentation](https://cloud.tencent.com/document/product/607/15228).


| Important API | Description |
| ------------- |:-------------:|
|Init    		|Initializes GME 	|
|Poll    		|Triggers event callback	|
|EnterRoom	 	|Enters a room  		|
|EnableAudioCaptureDevice	 	|Enables/disables a capturing device |
|EnableAudioSend		|Enables/disables audio upstream 	|
|EnableAudioPlayDevice    			|Enables/disables a playback device		|
|EnableAudioRecv    					|Enables/disables audio downstream 	|

**Notes:**
**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**
**GME APIs are called in the same thread.**
**The request for entering a room via GME API should be authenticated. For more information, see authentication section in relevant documentation.**

**The Poll API is called for GME to trigger event callback.**


## Procedure for Quick Integration


### 1. Initialize the SDK
For more information on how to obtain parameters, see [GME Integration Guide](https://cloud.tencent.com/document/product/607/10782).
This API should contain SdkAppId and openId. The SdkAppId is obtained from the Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.

#### Function prototype
```
IQAVContext Init(string sdkAppID, string openID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId    	|String  |The SdkAppId obtained from the Tencent Cloud console |
| openID    	|String  |The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. 	|

#### Sample code  
```
int ret = IQAVContext.GetInstance().Init(str_appId, str_userId);
	if (ret != QAVError.OK) {
		return;
	}
```

### 2. Trigger event callback
This API is used to trigger the event callback via periodic Poll call in update.
#### Function prototype

```
ITMGContext public abstract int Poll();
```

### 3. Enter a room
This API is used to enter a room with the generated authentication information. Microphone and speaker are not enabled by default after a user enters the room.


#### Function prototype
```
ITMGContext EnterRoom(int roomID, int roomType, byte[] authBuffer)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomID		|int    		| Room number. 32-bit is supported. |
| roomType 	|ITMGRoomType		|Audio type of the room		|
| authBuffer 	|Byte[] 	| Authentication key					|

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume | 16k (if there is no special requirement for sound quality) | With high fluency and ultra-low delay, it is suitable for team speak scenarios in such games as FPS and MOBA. |							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| 16k or 48k, depending on the requirement for sound quality	| With good sound quality and medium delay, it is suitable for voice chat scenarios in casual games such as Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|HD	|3|Speaker: media volume; headset: media volume	| 48k is recommended to ensure the best effect	| With ultra-high sound quality and high delay, it is suitable for music and voice social Apps, and scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirements for volume types or scenarios, contact the customer service.
- The sound effect in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.
#### Sample code  
```
IQAVContext.GetInstance().EnterRoom(roomId, ITMG_ROOM_TYPE_FLUENCY, authBuffer);
```

### 4. Callback for entering a room
The delegate function is used for callback after a user enters a room. The passed parameter includes result and error_info.
#### Function prototype
```
Delegate function:
public delegate void QAVEnterRoomComplete(int result, string error_info);
Event function:
public abstract event QAVEnterRoomComplete OnEnterRoomCompleteEvent;
```

#### Sample code

```
Listen for an event:
IQAVContext.GetInstance().OnEnterRoomCompleteEvent += new QAVEnterRoomComplete(OnEnterRoomComplete);

Process the event after listening:
void OnEnterRoomComplete(int err, string errInfo)
    {
	if (err != 0) {
	    ShowWarnning (string.Format ("join room failed, err:{0}, errInfo:{1}", err, errInfo));
	    return;
	}else{
	    ShowWarnning (string.Format ("The current audio room id:{0}. Please enter this room from another device for an audio chat.",roomId ));
    }
}
```

### 5. Enable/disable a capturing device
This API is used to enable/disable a capturing device. The devices is not enabled by default after a user enters the room.
- This API can only be called after a user enters the room. The device is disabled after the user exits the room.
- Operations such as permission application and volume type adjustment come with enabling the capturing device on mobile.

#### Function prototype  
```
ITMGAudioCtrl int EnableAudioPlayDevice(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the capturing device, set this parameter to true, otherwise, set it to false. |
#### Sample code  
```
Enable a capturing device
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioCaptureDevice(true);
```


### 6. Enable/disable audio upstream
This API is used to enable/disable audio upstream. If the capturing device is already enabled, captured audio data will be sent. If it is not enabled, it remains silent. To enable/disable a capturing device, see API EnableAudioCaptureDevice.

#### Function prototype  
```
ITMGAudioCtrl int EnableAudioSend(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the audio upstream, set this parameter to true, otherwise, set it to false. |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioSend(true);
```

### 7. Enable/disable a playback device
This API is used to enable/disable a playback device.
> Function prototype  
```
ITMGAudioCtrl EnableAudioPlayDevice(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |bool       	| To disable the playback device, set this parameter to false, otherwise, set it to true.	|
#### Sample code  
```
Enable a playback device
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioPlayDevice(true);
```



### 8. Enable/disable audio downstream
This API is used to enable/disable audio downstream. If the playback device is enabled, audio data of other users in the room will be played back. If it is not enabled, it remains silent. To enable/disable a capturing device, see API EnableAudioPlayDevice.

#### Function prototype  
```
ITMGAudioCtrl int EnableAudioRecv(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the audio downstream, set this parameter to true, otherwise, set it to false. |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioRecv(true);
```


## Authentication
### Voice chat authentication
AuthBuffer is generated for encryption and authentication of appropriate features. For more information on how to obtain relevant parameters, see [GME Key](https://cloud.tencent.com/document/product/607/12218).      
When voice message is obtaining authentication, the parameter of room number must be set to 0.
A value of type Byte[] is returned by this API.
#### Function prototype
```
QAVAuthBuffer GenAuthBuffer(int appId, int roomId, string openId, string key)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| appId    		|int   		|The SdkAppId obtained from the Tencent Cloud console |
| roomId    		|int   		|Room number. 32-bit is supported.									|
| openId    	|String 	|User ID											|
| key    		|string 	|The key obtained from the Tencent Cloud console			|
#### Sample code  

```
byte[] GetAuthBuffer(string appId, string userId, int roomId)
    {
	return QAVAuthBuffer.GenAuthBuffer(int.Parse(appId), roomId, userId, "a495dca2482589e9");
}
```

