## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides an overview that makes it easy for Android developers to debug and integrate the APIs for Game Multimedia Engine.


## How to Use
![](https://main.qcloudimg.com/raw/810d0404638c494d9d5514eb5037cd37.png)


### Key considerations for using GME

This document only provides the most important APIs to help you get started with GME. For more APIs, please see [API Documentation](https://intl.cloud.tencent.com/document/product/607/15210).


| Important API | Description |
| ------------- |-------------|
|Init    				|Initializes GME 	|
|Poll    				|Triggers event callback	|
|EnterRoom	 		|Enters a room  			|
|EnableMic	 		|Enables the microphone 		|
|EnableSpeaker		|Enables the speaker 		|

**Note**
**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**
**GME APIs are called in the same thread.**
**The request for entering a room via GME API should be authenticated. For more information, please see authentication section in relevant documentation.**

## Procedure for Quick Integration

### 1. Get a singleton
This API is used to get the ITMGContext object when using the voice feature.

#### Function prototype 

```
public static ITMGContext GetInstance(Context context)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| context    |Context |Application's context object |


#### Sample code  

```
import com.tencent.TMG.ITMGContext; 
TMGContext.getInstance(this);
```

### 2. Initialize the SDK
For more information on how to obtain parameters, please see [GME Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782).
This API should contain SdkAppId and openId. The SdkAppId is obtained from Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.
#### Function prototype

```
ITMGContext public int Init(String sdkAppId, String openID)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId    	|String  |The SdkAppId obtained from Tencent Cloud console |
| openID    		|String  |The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. 	|

#### Sample code 
```
ITMGContext.GetInstance(this).Init(sdkAppId, openId);
```

### 3. Trigger event callback
This API is used to trigger the event callback via periodic Poll call in update.
#### Function prototype

```
ITMGContext int Poll()
```
#### Sample code
```
ITMGContext.GetInstance(this).Poll();
```

### 4. Enter a room
This API is used to enter a room with the generated authentication information, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback.
- Microphone and speaker are not enabled by default after a user enters the room.
- The API Init should be called before the API EnterRoom.

#### Function prototype
```
ITMGContext public abstract void  EnterRoom(int relationId, int roomType, byte[] authBuffer)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| relationId 	|int		| Room number. 32-bit is supported. |
| roomType 	|int		|Audio type of the room		|
| authBuffer	|byte[]	|Authentication key				|

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume 	| 16k sampling rate is recommended if there is no special requirement for sound quality					| With fluent sound and ultra-low latency, it allows voice chat and is suitable for team speak scenario in such games as FPS and MOBA.	|							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| Choose 16k or 48k sampling rate depending on different requirements for sound quality				| With good sound quality and medium latency, it is suitable for real time chat scenarios in casual games such as Werewolf, chess and card games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|High-quality	|3|Speaker: media volume; headset: media volume	| To ensure optimum effect, it is recommended to enable HQ configuration with 48k sampling rate	| With ultra-high sound quality and high latency, it is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirement for audio type or scenarios, contact the customer service.
- The sound effect in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.
#### Sample code  
```
ITMGContext.GetInstance(this).EnterRoom(Integer.parseInt(relationId),roomType, authBuffer);    
```

### 5. Callback for entering a room
A callback response is returned after entering the room, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received.
Reference code for the callback setting:
```
private ITMGContext.ITMGDelegate itmgDelegate = null;
itmgDelegate= new ITMGContext.ITMGDelegate() {
            @Override
 			public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
                }
        };
```
Reference code for the callback processing:
#### Sample code  
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ENTER_ROOM == type)
        {
           	 // Receive the event of entering the room successfully.
        }
	}
```

### 6. Enable/Disable the microphone
This API is used to enable/disable the microphone. Microphone and speaker are not enabled by default after a user enters a room.

#### Function prototype  
```
ITMGContext public void EnableMic(boolean isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To disable the microphone, set this parameter to false, otherwise, set it to true. |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableMic(true);
```


### 7. Enable/Disable the speaker
This API is used to enable/disable the speaker.

#### Function prototype  
```
ITMGContext public void EnableSpeaker(boolean isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean       |To disable the speaker, set this parameter to false, otherwise, set it to true.	|
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableSpeaker(true);
```


## Authentication
### Voice chat authentication
AuthBuffer is generated for encryption and authentication of appropriate features. For more information on how to obtain relevant parameters, please see [GME Key](https://intl.cloud.tencent.com/document/product/607/12218).    
A value of type Byte[] is returned by this API.

#### Function prototype
```
AuthBuffer public native byte[] genAuthBuffer(int sdkAppId, int roomId, String identifier, String key, int expTime, int authBits)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| appId    		|int   	|The SdkAppId obtained from Tencent Cloud console |
| roomId    		|int   	|Room number. 32-bit is supported.									|
| identifier    	|String | User ID |
| key    		|string |The key obtained from Tencent Cloud console			|
| expTime    		|int   	| authBuffer timeout |
| authBits    		|int    |Permission (ITMG_AUTH_BITS_DEFAULT indicates full access)	|


#### Sample code  
```
long nExpUTCTime = 1800 + System.currentTimeMillis() / 1000L;
byte[] authBuffer=AuthBuffer.getInstance().genAuthBuffer(Integer.parseInt(sdkAppId), Integer.parseInt(strRoomID),identifier, key, (int)nExpUTCTime, (int) ITMGContext.ITMG_AUTH_BITS_DEFAULT);
```

