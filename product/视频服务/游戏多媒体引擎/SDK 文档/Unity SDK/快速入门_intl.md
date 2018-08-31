## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides an overview that makes it easy for Unity developers to debug and integrate the APIs for Game Multimedia Engine (GME).


## How to Use
![](https://main.qcloudimg.com/raw/810d0404638c494d9d5514eb5037cd37.png)


### Key considerations for using GME

This document only provides the most important APIs to help you get started with GME. For more APIs, please see [API Documentation](https://intl.cloud.tencent.com/document/product/607/15228).


| Important API | Description |
| ------------- |-------------|
|Init    				|Initializes GME 	|
|Poll    				|Triggers event callback	|
|EnterRoom	 		|Enters a room  			|
|EnableMic	 		|Enables the microphone 		|
|EnableSpeaker		|Enables the speaker 		|

**Note:**
**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**
**GME APIs are called in the same thread.**
**The request for entering a room via GME API should be authenticated. For more information, please see authentication section in relevant documentation.**

## Procedure for Quick Integration


### 1. Initialize the SDK
For more information on how to obtain parameters, please see [GME Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782).
This API should contain SdkAppId and openId. The SdkAppId is obtained from Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.

#### Function prototype
```
IQAVContext Init(string sdkAppID, string openID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId    	|String  |The SdkAppId obtained from Tencent Cloud console |
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
This API is used to enter a room with the generated authentication information.
- Microphone and speaker are not enabled by default after a user enters the room.
- The API Init should be called before the API EnterRoom.


#### Function prototype
```
ITMGContext EnterRoom(int relationId, int roomType, byte[] authBuffer)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| relationId		|int  		| Room number. 32-bit is supported.				|
| roomType 	|ITMGRoomType		| Audio type of the room |
| authBuffer 	|Byte[] 	| Authentication code					|

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume 	| 16k sampling rate is recommended if there is no special requirement for sound quality					| With fluent sound and ultra-low latency, it allows voice chat and is suitable for team speak scenario in such games as FPS and MOBA.	|							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| Choose 16k or 48k sampling rate depending on different requirements for sound quality				| With good sound quality and medium latency, it is suitable for real time chat scenarios in casual games such as Werewolf, chess and card games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|High-quality	|3|Speaker: media volume; headset: media volume	| To ensure optimum effect, it is recommended to enable HQ configuration with 48k sampling rate	| With ultra-high sound quality and high latency, it is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirement for audio type or scenarios, contact the customer service.
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

### 5. Enable/Disable the microphone
This API is used to enable/disable the microphone. Microphone and speaker are not enabled by default after a user enters a room.

#### Function prototype  
```
ITMGAudioCtrl EnableMic(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the microphone, set this parameter to true, otherwise, set it to false. |
#### Sample code  
```
Enable the microphone
IQAVContext.GetInstance().GetAudioCtrl().EnableMic(true);
```


### 6. Enable/Disable the speaker
This API is used to enable/disable the speaker.
#### Function prototype  
```
ITMGAudioCtrl EnableSpeaker(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |bool       	| To disable the speaker, set this parameter to false, otherwise, set it to true.	|
#### Sample code  
```
Enable the speaker
IQAVContext.GetInstance().GetAudioCtrl().EnableSpeaker(true);
```

## Authentication
### Voice chat authentication
AuthBuffer is generated for encryption and authentication of appropriate features. For more information on how to obtain relevant parameters, please see [GME Key](https://intl.cloud.tencent.com/document/product/607/12218).      
A value of type Byte[] is returned by this API.
#### Function prototype
```
QAVAuthBuffer GenAuthBuffer(int appId, int roomId, string identifier, string key, int expTime, uint authBits)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| appId    		|int   		|The SdkAppId obtained from Tencent Cloud console					|
| roomId    		|int   		|Room number. 32-bit is supported.									|
| identifier    	|String 		|User ID											|
| key    			|string 		|The key obtained from Tencent Cloud console								|
| expTime    		|int   		|authBuffer timeout									|
| authBits    		|int    		|Permission (ITMG_AUTH_BITS_DEFAULT indicates full access)	|
#### Sample code  
```
byte[] GetAuthBuffer(string appId, string userId, int roomId, uint authBits)
    {
	TimeSpan t = DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, 0);
	double timeStamp = t.TotalSeconds;
	return QAVAuthBuffer.GenAuthBuffer(int.Parse(appId), roomId, userId, "a495dca2482589e9", (int)timeStamp + 1800, authBits);
}
byte[] authBuffer = this.GetAuthBuffer(str_appId,, str_userId, roomId, recvOnly ? IQAVContext.AUTH_BITS_RECV : IQAVContext.AUTH_BITS_ALL);
```

