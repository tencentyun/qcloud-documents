## Overview

Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. This document provides an overview that makes it easy for Cocos2D developers to debug and integrate the APIs for GME.


## How to Use
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)


### Key considerations for using GME

This document only provides the most important APIs to help you get started with GME. For more APIs, see [API Documentation](https://cloud.tencent.com/document/product/607/15218).


| Important API | Description |
| ------------- |-------------|
| Init | Initializes GME |
| Poll | Triggers event callback |
| EnterRoom | Enters a room |
| EnableMic | Enables the microphone |
| EnableSpeaker | Enables the speaker |

>**Notes:**
**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**

**GME APIs are called in the same thread.**

**The request for entering a room via GME API should be authenticated. For more information, see authentication section in relevant documentation.**

**The Poll API is called periodically for GME to trigger event callback.**

**See the callback message list for GME callback information.**

**The operation on devices shall be carried out after successful entry into a room.**

**This document applies to GME SDK version 2.2.**
## Procedure for Quick Integration

### 1. Get a singleton
This API is used to get the ITMGContext object when using the voice feature.

#### Sample code  

```
ITMGContext* context = ITMGContextGetInstance();
context->SetTMGDelegate(this);
```



### 2. Initialize the SDK
For more information on how to obtain parameters, see [GME Integration Guide](https://cloud.tencent.com/document/product/607/10782).
This API should contain SdkAppId and openId. The SdkAppId is obtained from the Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.
#### Function prototype

```
ITMGContext virtual void Init(const char* sdkAppId, const char* openId)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId | char* | The SdkAppId obtained from the Tencent Cloud console |
| openID | char* | The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. |

#### Sample code 
```
#define SDKAPPID3RD "1400035750"
cosnt char* openId="10001";
ITMGContext* context = ITMGContextGetInstance();
context->Init(SDKAPPID3RD, openId);
```

### 3. Trigger event callback
This API is used to trigger the event callback via periodic Poll call in update.
#### Function prototype

```
class ITMGContext {
protected:
    virtual ~ITMGContext() {}
    
public:    	
	virtual void Poll()= 0;
}
```
#### Sample code
```
ITMGContextGetInstance()->Poll();
```

### 4. Enter a room
This API is used to enter a room with the generated authentication information, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback.
- Microphone and speaker are not enabled by default after a user enters the room.
- The API Init should be called before the API EnterRoom.

#### Function prototype
```
ITMGContext virtual void EnterRoom(const char*  roomId, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen)//Common API for entering a room
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomId | char* | Room number, which is limited to 127 characters |
| roomType | ITMG_ROOM_TYPE | Audio type of the room |
| authBuffer | char* | Authentication key |
| buffLen | int | Length of the authentication key |

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY | Fluent | 1 | Speaker: chat volume; headset: media volume | 16k (if there is no special requirement for sound quality) | With high fluency and ultra-low delay, it is suitable for team speak scenarios in such games as FPS and MOBA. |							
| ITMG_ROOM_TYPE_STANDARD | Standard	|2|Speaker: chat volume; headset: media volume | 16k or 48k, depending on the requirement for sound quality	| With good sound quality and medium delay, it is suitable for voice chat scenarios in casual games such as Werewolf and board games. |												
| ITMG_ROOM_TYPE_HIGHQUALITY | HD | 3 | Speaker: media volume; headset: media volume	| 48k is recommended to ensure the best effect	| With ultra-high sound quality and high delay, it is suitable for music and voice social Apps, and scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirements for volume types or scenarios, contact the customer service.
- The sound effect in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.

#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
context->EnterRoom(roomId, ITMG_ROOM_TYPE_STANDARD, (char*)retAuthBuff,bufferLen);
```

### 5. Callback for entering a room
This API is used to send the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message after a user enters a room, which is checked in the OnEvent function.

#### Sample code 

```
//Implementation
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process
		break;
		}
	}
}
```

### 6. Enable/Disable the microphone
This API is used to enable/disable the microphone. Microphone and speaker are not enabled by default after a user enters a room.

#### Function prototype  
```
ITMGAudioCtrl virtual void EnableMic(bool bEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| bEnabled | bool | To enable the microphone, set this parameter to true, otherwise set it to false. |
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableMic(true);
```


### 7. Enable/Disable the speaker
This API is used to enable/disable the speaker.

#### Function prototype  
```
ITMGAudioCtrl virtual void EnableSpeaker(bool enabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| enable | bool | To disable the speaker, set this parameter to false, otherwise set it to true. |
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableSpeaker(true);
```


## Authentication
### Authentication information
This API is used to generate AuthBuffer for encryption and authentication of appropriate features. For more information on deployment at backend, see [GME Key](https://cloud.tencent.com/document/product/607/12218).  
When voice message is obtaining authentication, the room number parameter must be set to 0.

#### Function prototype
```
QAVSDK_AUTHBUFFER_API int QAVSDK_AUTHBUFFER_CALL QAVSDK_AuthBuffer_GenAuthBuffer(unsigned int nAppId, const char* dwRoomID, const char* strOpenID, const char* strKey, unsigned char* strAuthBuffer, unsigned int bufferLength);
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| nAppId | int | The SdkAppId obtained from the Tencent Cloud console |
| dwRoomID |char* | Room number, which is limited to 127 characters (The room number parameter for voice message must be set to 0) |
| strOpenID | char*   | User ID |
| strKey    			| char*  	| The key obtained from the Tencent Cloud [Console](https://console.cloud.tencent.com/gamegme)					|
| strAuthBuffer | char* | Returned authbuff |
| buffLenght | int | Length of returned authbuff |


#### Sample code  
```
unsigned int bufferLen = 512;
unsigned char retAuthBuff[512] = {0};
QAVSDK_AuthBuffer_GenAuthBuffer(atoi(SDKAPPID3RD), roomId, "10001", AUTHKEY,strAuthBuffer,&bufferLen);
```

