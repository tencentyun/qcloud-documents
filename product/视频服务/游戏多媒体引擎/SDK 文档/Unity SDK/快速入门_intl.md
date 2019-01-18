## Overview
 Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides an overview that makes it easy for Unity developers to debug and integrate the APIs for Game Multimedia Engine.
 ## How to Use
![](https://main.qcloudimg.com/raw/810d0404638c494d9d5514eb5037cd37.png)
 ### Key considerations for using GME
 This document only provides the most important APIs to help you get started with GME. For more APIs, see [API Documentation](/document/product/607/15228).

| Important API | Description |
| ------------- |-------------|
|Init    				|Initializes GME 	|
|Poll    				|Triggers event callback	|
|EnterRoom	 		|Enters a room  			|
|EnableMic	 		|Enables the microphone 		|
|EnableSpeaker		|Enables the speaker 		|

 **Notes:**
**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**

**GME APIs should be called in the same thread.**

**Authentication is needed before entering a room. Refer to the authentication section in relevant documentation for more information.**

**The Poll API should be called for GME to trigger event callback.**

**Refer to the callback message list for callback related information.**

**Device related operations can only be done after entering a room.**

**This document is applicable to GME sdk version：2.2.**

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
| sdkAppId    	|String  | The SdkAppId obtained from Tencent Cloud console				|
| openID |String | The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. |

#### Sample code  
```
int?ret?=?IQAVContext.GetInstance().Init(str_appId,?str_userId);
	if?(ret?!=?QAVError.OK)?{
		return;
	}
```
 ### 2. Trigger event callback
This API is used to trigger the event callback via periodic Poll call in update.
#### Function prototype

```
ITMGContext public abstract int Poll();
```
 ### 3.  Join a room
This API is used to enter a room with the generated authentication data, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback. Microphone and speaker are not enabled by default after a user enters the room.
For entering a common voice chat room that does not involve team voice chat, use the common API for entering a room. For more information, please see the [GME team voice chat documentation](../GME%20TeamAudio%20Manual_intl.md).

#### Function prototype

```
ITMGContext EnterRoom(string?roomId,?int?roomType,?byte[]?authBuffer)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomId | string |  Room ID. maximum to 127 characters. |
| roomType | ITMGRoomType | Audio type of the room |
| authBuffer | Byte[] | Authentication key |

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume 	| 16k sampling rate is recommended if there is no special requirement for sound quality					| Fluent sound quality and ultra-low delay which is suitable for team speak scenarios in games like FPS and MOBA.	|							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| Choose 16k or 48k sampling rate depending on different requirements for sound quality				| Good sound quality and medium delay which is suitable for voice chat scenarios in casual games like Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|High-quality	|3|Speaker: media volume; headset: media volume	| To ensure optimum effect, it is recommended to enable HQ configuration with 48k sampling rate	| Super-high sound quality and relative high delay which is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirements on the sound quality for certain scenario, contact the customer service.
- The sound quality in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.


#### Sample code  

```
IQAVContext.GetInstance().EnterRoom(roomId,?ITMG_ROOM_TYPE_FLUENCY,?authBuffer);
```
 ### 4. Callback for entering a room
The delegate function is used for callback after a user enters a room. The passed parameter includes result and error_info.
#### Function prototype
```
Delegate function:
public?delegate?void?QAVEnterRoomComplete(int?result,?string?error_info);
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
EnableMic = EnableAudioCaptureDevice + EnableAudioSend.
#### Function prototype  
```
ITMGAudioCtrl EnableMic(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     | To enable the microphone, set this parameter to true, otherwise, set it to false. |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioCtrl().EnableMic(true);
```
 ### 6. Enable/Disable the speaker
This API is used to enable/disable the speaker.
EnableSpeaker = EnableAudioPlayDevice + EnableAudioRecv.
#### Function prototype  
```
ITMGAudioCtrl EnableSpeaker(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled | bool | To disable the speaker, set this parameter to false, otherwise set it to true. |

#### Sample code  
```
Enable the speaker
IQAVContext.GetInstance().GetAudioCtrl().EnableSpeaker(true);
```
 ## Authentication
### Voice chat authentication
AuthBuffer is generated for the purpose of encryption and authentication. For more information about the authentication data, refer to  [GME Key](https://intl.cloud.tencent.com/document/product/607/12218).    

#### Function prototype
```
QAVAuthBuffer GenAuthBuffer(int appId, string roomId, string openId, string key)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| appId    		|int   		| The SdkAppId obtained from the Tencent Cloud console |
| roomId | string | Room ID, maximum to 127 characters (The room ID parameter for voice message must be set to "null")|
| openId | String | User ID |
| key    		|string 	| The key obtained from the Tencent Cloud [Console](https://console.cloud.tencent.com/gamegme) 				|



#### Sample code  
```
byte[] GetAuthBuffer(string appId, string userId, string roomId)
    {
	return QAVAuthBuffer.GenAuthBuffer(int.Parse(appId), roomId, userId, "a495dca2482589e9");
}
```