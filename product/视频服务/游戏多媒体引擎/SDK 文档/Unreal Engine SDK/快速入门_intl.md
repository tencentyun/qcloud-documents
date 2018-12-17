## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides an overview that makes it easy for Unreal developers to debug and integrate the APIs for Game Multimedia Engine (GME).


## How to Use
![](https://main.qcloudimg.com/raw/810d0404638c494d9d5514eb5037cd37.png)


### Key considerations for using GME

This document only provides the most important APIs to help you get started with GME. For more APIs, see [API Documentation](https://intl.cloud.tencent.com/document/product/607/15231).


| Important API | Description |
| ------------- |:-------------:|
|Init    		|Initializes GME 	|
|Poll    		|Triggers event callback	|
|EnterRoom	 	|Enters a room  		|
|EnableMic	 	|Enables the microphone 	|
|EnableSpeaker		|Enables the speaker 	|

**Notes:**

**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**

**GME APIs should be called in the same thread.**

**Authentication is needed before entering a room. Refer to the authentication section in relevant documentation for more information.**

**The Poll API should be called for GME to trigger event callback.**

**Refer to the callback message list for callback related information.**

**Device related operations can only be done after entering a room.**

**This document is applicable to GME sdk version：2.2.**

### 1. Get a singleton
This API is used to get the ITMGContext object when using the voice feature.

#### Sample code  

```
ITMGContext* context = ITMGContextGetInstance();
context->SetTMGDelegate(this);
```



### 2. Initialize the SDK
For more information on how to obtain parameters, please see [GME Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782).
This API call needs SdkAppId and openId. The SdkAppId is obtained from Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.
#### Function prototype 

```
ITMGContext virtual void Init(const char* sdkAppId, const char* openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId    	|char*   	|The SdkAppId obtained from Tencent Cloud console					|
| openID    	|char*   	|The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. 	|

#### Sample code  

```
std::string appid = TCHAR_TO_UTF8(CurrentWidget->editAppID->GetText().ToString().operator*());
std::string userId = TCHAR_TO_UTF8(CurrentWidget->editUserID->GetText().ToString().operator*());
ITMGContextGetInstance()->Init(appid.c_str(), userId.c_str());
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
//Declaration in the header file
virtual void Tick(float DeltaSeconds);

//Code implementation
void AUEDemoLevelScriptActor::Tick(float DeltaSeconds) 
{
    ITMGContextGetInstance()->Poll();
}
```

### 4. Join a room
This API is used to enter a room with the generated authentication data, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback. Microphone and speaker are not enabled by default after a user enters the room.
For entering a common voice chat room that does not involve team voice chat, use the common API for entering a room. For more information, please see the [GME team voice chat documentation](https://intl.cloud.tencent.com/document/product/607/17972).

#### Function prototype

```
ITMGContext virtual void EnterRoom(const char*  roomId, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen)//Common API for entering a room
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomId			|char*   		| Room ID. maximum to 127 characters.	|
| roomType 			|ITMG_ROOM_TYPE	|Audio type of the room		|
| authBuffer    		|char*     	| Authentication key			|
| buffLen   			|int   		| Length of the authentication key		|

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume 	| 16k sampling rate is recommended if there is no special requirement for sound quality					| Fluent sound quality and ultra-low delay which is suitable for team speak scenarios in games like FPS and MOBA.	|							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| Choose 16k or 48k sampling rate depending on different requirements for sound quality				| Good sound quality and medium delay which is suitable for voice chat scenarios in casual games like Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|High-quality	|3|Speaker: media volume; headset: media volume	| To ensure optimum effect, it is recommended to enable HQ configuration with 48k sampling rate	| Super-high sound quality and relative high delay which is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirements on the sound quality for certain scenario, contact the customer service.
- The sound quality in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.


#### Sample code  

```
ITMGContext* context = ITMGContextGetInstance();
context->EnterRoom(roomId, ITMG_ROOM_TYPE_STANDARD, (char*)retAuthBuff,bufferLen);//Sample code for entering a common voice chat room
```



### 5. Callback for entering a room
ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received after a user enters a room, the action of this event should be implemented in the OnEvent function.
#### Code Description

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
EnableMic = EnableAudioCaptureDevice + EnableAudioSend.
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
EnableSpeaker = EnableAudioPlayDevice + EnableAudioRecv.
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
### Authentication information
AuthBuffer is generated for the purpose of encryption and authentication. For more information about the authentication data, refer to  [GME Key](https://intl.cloud.tencent.com/document/product/607/12218).    
The room ID parameter for voice message must be set to "null".

#### Function prototype
```
QAVSDK_AUTHBUFFER_API int QAVSDK_AUTHBUFFER_CALL QAVSDK_AuthBuffer_GenAuthBuffer(unsigned int nAppId, const char* dwRoomID, const char* strOpenID, const char* strKey, unsigned char* strAuthBuffer, unsigned int bufferLength);
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| nAppId | int | The SdkAppId obtained from the Tencent Cloud console |
| dwRoomID |char* | Room ID, maximum to 127 characters (The room room ID for voice message must be set to "null") |
| strOpenID | char*   | User ID |
| strKey | char* | The key obtained from the Tencent Cloud [Console](https://console.cloud.tencent.com/gamegme) |
| strAuthBuffer | char* | Returned authbuff |
| buffLenght | int | Length of returned authbuff |



#### Sample code  
```
unsigned int bufferLen = 512;
unsigned char retAuthBuff[512] = {0};
QAVSDK_AuthBuffer_GenAuthBuffer(atoi(SDKAPPID3RD), roomId, "10001", AUTHKEY,strAuthBuffer,&bufferLen);
```
