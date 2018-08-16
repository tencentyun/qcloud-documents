## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides an overview that makes it easy for C++ developers to debug and integrate the APIs for Game Multimedia Engine (GME).


## How to Use
![](https://main.qcloudimg.com/raw/810d0404638c494d9d5514eb5037cd37.png)


### Key considerations for using GME

This document only provides the most important APIs to help you get started with GME. For more APIs, please see [API Documentation](https://intl.cloud.tencent.com/document/product/607/15232).


| Important API | Description |
| ------------- |-------------|
|Init   				|Initializes GME 	|
|Poll    				|Triggers event callback	|
|EnterRoom	 		|Enters a room  			|
|EnableMic	 		|Enables the microphone 		|
|EnableSpeaker		|Enables the speaker 		|

**Note:**
**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**
**GME APIs are called in the same thread.**
**The request for entering a room via GME API should be authenticated. For more information, please see authentication section in relevant documentation.**

## Procedure for Quick Integration

### 1. Get a singleton
This API is used to get the ITMGContext object when using the voice feature.

#### Sample code  

```
ITMGContext* context = ITMGContextGetInstance();
context->SetTMGDelegate(this);
```



### 2. Initialize the SDK
For more information on how to obtain parameters, please see [GME Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782).
This API should contain SdkAppId and openId. The SdkAppId is obtained from Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.
#### Function prototype

```
ITMGContext virtual void Init(const char* sdkAppId, const char* openId)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId    	|char*  	|The SdkAppId obtained from Tencent Cloud console					|
| openID    		|char*   	|The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. 	|

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
ITMGContext virtual void EnterRoom(int relationId, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| relationId			|int   				| Room number. 32-bit is supported. |
| roomType 			|ITMG_ROOM_TYPE	| Audio type of the room	|
| authBuffer    		|char*    				| Authentication key			|
| buffLen   			|int   				| Length of the authentication key		|

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume 	| 16k sampling rate is recommended if there is no special requirement for sound quality					| With fluent sound and ultra-low latency, it allows voice chat and is suitable for team speak scenario in such games as FPS and MOBA.	|							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| Choose 16k or 48k sampling rate depending on different requirements for sound quality				| With good sound quality and medium latency, it is suitable for real time chat scenarios in casual games such as Werewolf, chess and card games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|High-quality	|3|Speaker: media volume; headset: media volume	| To ensure optimum effect, it is recommended to enable HQ configuration with 48k sampling rate	| With ultra-high sound quality and high latency, it is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirement for audio type or scenarios, contact the customer service.
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
// ITMGDelegate is inherited from the header file and declaration is made.
class TMGTestScene : public cocos2d::Scene,public ITMGDelegate
{
public:
    void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data);
    ...	
}

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
| bEnabled    |bool     |To enable the microphone, set this parameter to true, otherwise, set it to false. |
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
| enable   		|bool       	| To disable the speaker, set this parameter to false, otherwise, set it to true.	|
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableSpeaker(true);
```


## Authentication
### Voice chat authentication
AuthBuffer is generated for encryption and authentication of appropriate features. For more information on how to obtain relevant parameters, please see [GME Key](https://intl.cloud.tencent.com/document/product/607/12218).  

#### Function prototype
```
QAVSDK_API int QAVSDK_CALL QAVSDK_AuthBuffer_GenAuthBuffer(unsigned int appId, unsigned int authId, const char* strOpenID, const char* key, unsigned int expTime, unsigned int privilegeMap, unsigned char* retAuthBuff, unsigned int* buffLenght);
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| appId    		|int   		| The SdkAppId obtained from Tencent Cloud console		|
| authId    		|int  		| Name of the room to be entered							|
| strOpenID  		|char*    		| User ID								|
| key    			|char*	    	| The key obtained from Tencent Cloud console		|
| expTime    		|int   		| authBuffer timeout						|
| privilegeMap   	|int    		| Permission (ITMG_AUTH_BITS_DEFAULT indicates full access) |
| retAuthBuff   	|char*    		| Returned authbuff							|
| buffLenght   	|int    		| Length of returned authbuff					|


#### Sample code  
```
QAVSDK_AuthBuffer_GenAuthBuffer(atoi(SDKAPPID3RD), roomId, "10001", AUTHKEY, expTime, ITMG_AUTH_BITS_DEFAULT, retAuthBuff, &bufferLen);
```

