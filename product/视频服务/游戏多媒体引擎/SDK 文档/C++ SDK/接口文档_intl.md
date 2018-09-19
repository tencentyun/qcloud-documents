## Overview
Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides a detailed description that makes it easy for C++ developers to debug and integrate the APIs for Game Multimedia Engine.


## How to Use
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)

### Key considerations for using GME

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

## Initialization-Related APIs
For an uninitialized SDK, you must initialize it via initialization authentication to enter a room.

| API | Description |
| ------------- |:-------------:|
|Init    	|Initializes GME 	| 
|Poll    	|Triggers event callback	|
|Pause   	|Pauses the system	|
|Resume 	|Resumes the system	|
|Uninit    	|Deinitializes GME 	|


### Get a singleton
GMESDK is provided as a singleton. ITMGContext must be configured first, because all calls begin from ITMGContext and are called and passed back to your application via ITMGDelegate.    
#### Function prototype 

```
ITMGContext virtual void TMGDelegate(ITMGDelegate* delegate)
```
#### Sample code  

```
ITMGContext* m_pTmgContext;
m_pTmgContext = ITMGContextGetInstance();
```


### Message passing
With the API class, the Delegate method is used to send callback notifications to your application. ITMG_MAIN_EVENT_TYPE indicates the message type. The data under Windows is in json string format. See the relevant documentation for the key-value pairs.

#### Sample code 

```
//Function implementation:
class Callback : public SetTMGDelegate 
{
	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
	{
  		switch(eventType)
  		{
   			//Determine the message type and process the message
  		}
 	}
}

Callback*  p = new Callback ();
m_pTmgContext->TMGDelegate(p);

```

### Initialize the SDK

For more information on how to obtain parameters, see [GME Integration Guide](https://cloud.tencent.com/document/product/607/10782).
This API should contain SdkAppId and openId. The SdkAppId is obtained from the Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.
#### Function prototype 

```
ITMGContext virtual void Init(const char* sdkAppId, const char* openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId    	|char*   	|The SdkAppId obtained from the Tencent Cloud console					|
| openID    	|char*   	|The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. 	|

#### Sample code  

```
#define SDKAPPID3RD "1400035750"
cosnt char* openId="10001";
ITMGContext* context = ITMGContextGetInstance();
context->Init(SDKAPPID3RD, openId);
```


### Trigger event callback

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
//Code implementation
void TMGTestScene::update(float delta)
{
    ITMGContextGetInstance()->Poll();
}
```


### Pause the system

This API is used to notify the engine for Pause at the same time the system Pause occurs.
#### Function prototype

```
ITMGContext int Pause()
```

### Resume the system
This API is used to notify the engine for Resume at the same time the system Resume occurs.
#### Function prototype

```
ITMGContext  int Resume()
```



### Deinitialize the SDK
This API is used to deinitialize an SDK to make it uninitialized.

#### Function prototype 
```
ITMGContext int Uninit()

```
#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
context->Uninit();
```


## Voice Chat Room-Related APIs
You must initialize and call the SDK to enter a room before Voice Chat can start.

| API | Description |
| ------------- |:-------------:|
|GenAuthBuffer    	|Initialization authentication |
|EnterRoom   		|Enters a room |
|IsRoomEntered   	|Indicates whether any member has entered a room |
|ExitRoom 		|Exits a room |
|ChangeRoomType 	|Modifies the audio type of the user's room |
|GetRoomType 		|Obtains the audio type of the user's room |


### Voice chat authentication
AuthBuffer is generated for encryption and authentication of appropriate features. For more information on how to obtain relevant parameters, see [GME Key](https://cloud.tencent.com/document/product/607/12218).    
When voice message is obtaining authentication, the parameter of room number must be set to 0.

#### Function prototype
```
QAVSDK_AUTHBUFFER_API int QAVSDK_AUTHBUFFER_CALL QAVSDK_AuthBuffer_GenAuthBuffer(unsigned int nAppId, unsigned int dwRoomID, const char* strOpenID, const char* strKey, unsigned char* strAuthBuffer, unsigned int bufferLength);
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| nAppId    			|int   		| The SdkAppId obtained from the Tencent Cloud console		|
| dwRoomID    		|int   		| Room number. 32-bit is supported.	|
| strOpenID  		|char*    		| User ID								|
| strKey    			|char*	    	| The key obtained from the Tencent Cloud console		|
|strAuthBuffer		|char*    	| Returned authbuff				|
| buffLenght   		|int    		| Length of returned authbuff					|



#### Sample code  
```
unsigned int bufferLen = 512;
unsigned char retAuthBuff[512] = {0};
QAVSDK_AuthBuffer_GenAuthBuffer(atoi(SDKAPPID3RD), roomId, "10001", AUTHKEY,strAuthBuffer,&bufferLen);
```

### Enter a room
This API is used to enter a room with the generated authentication information, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback. Microphone and speaker are not enabled by default after a user enters the room.
For entering a common voice chat room that does not involve team chatting, use the common API for entering a room. For more information, see the [GME team chatting documentation](https://cloud.tencent.com/document/product/607/17972).

#### Function prototype

```
ITMGContext virtual void EnterRoom(int roomId, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen)//Common API for entering a room
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomId			|int   		| Room number. 32-bit is supported.	|
| roomType 			|ITMG_ROOM_TYPE	|Audio type of the room		|
| authBuffer    		|char*     	| Authentication key			|
| buffLen   			|int   		| Length of the authentication key		|

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume | 16k (if there is no special requirement for sound quality) | With high fluency and ultra-low delay, it is suitable for team speak scenarios in such games as FPS and MOBA. |							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| 16k or 48k, depending on the requirement for sound quality	| With good sound quality and medium delay, it is suitable for voice chat scenarios in casual games such as Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|HD	|3|Speaker: media volume; headset: media volume	| 48k is recommended to ensure the best effect	| With ultra-high sound quality and high delay, it is suitable for music and voice social Apps, and scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirements for volume types or scenarios, contact the customer service.
- The sound effect in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.


#### Sample code  

```
ITMGContext* context = ITMGContextGetInstance();
context->EnterRoom(roomId, ITMG_ROOM_TYPE_STANDARD, (char*)retAuthBuff,bufferLen);//Sample code for entering a common voice chat room
```


### Team chatting room
For more information on how to integrate team chatting, see [GME team chatting documentation](https://cloud.tencent.com/document/product/607/17972).

#### Function prototype
```
ITMGContext virtual void EnterTeamRoom(int roomId, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen, int teamId, int gameAudioMode)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomId		|int   		| Room number. 32-bit is supported.			|
| roomType 		|ITMG_ROOM_TYPE	|Audio type of the room |
| authBuffer    	|char*    	| Authentication key					|
| buffLen   		|int   		| Length of the authentication key				|
| teamId    		|int    	| The ID of the team that enters the room (0 is not allowed)	|
| audioMode    		|int    	| 0 is for global chatting, and 1 for team chatting		|


| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume | 16k (if there is no special requirement for sound quality) | With high fluency and ultra-low delay, it is suitable for team speak scenarios in such games as FPS and MOBA. |							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| 16k or 48k, depending on the requirement for sound quality	| With good sound quality and medium delay, it is suitable for voice chat scenarios in casual games such as Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|HD	|3|Speaker: media volume; headset: media volume	| 48k is recommended to ensure the best effect	| With ultra-high sound quality and high delay, it is suitable for music and voice social Apps, and scenarios demanding high sound quality, such as music playback and online karaoke.	|

#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
context->EnterRoom(roomId, ITMG_ROOM_TYPE_STANDARD, (char*)retAuthBuff,bufferLen,1000,0);
```


### Callback for entering a room
This API is used to send the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message after a user enters a room, which is checked in the OnEvent function.
#### Code description
```

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

### Identify whether any member has entered a room
This API is called to identify whether any member has entered a room. A bool value is returned.
#### Function prototype  
```
ITMGContext virtual bool IsRoomEntered()
```
#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
context->IsRoomEntered();
```

### Exit a room
This API is called to exit the current room. It is a synchronous interface which releases occupied device resources when returned.
#### Function prototype  

```
ITMGContext virtual void ExitRoom()
```
#### Sample code  

```
ITMGContext* context = ITMGContextGetInstance();
context->ExitRoom();
```

### Callback for exiting a room
After a user exits the room, a callback response is returned and the ITMG_MAIN_EVENT_TYPE_EXIT_ROOM message is received.
#### Sample code  

```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM:
		{
		//Process
		break;
		}
	}
}
```

### Modify the audio type of the user's room
This API is used to modify the audio type of the user's room. See the callback event for the result. The event type is ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE.
#### Function prototype  
```
IITMGContext TMGRoom public void ChangeRoomType((ITMG_ROOM_TYPE roomType)
```


| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomType    |ITMG_ROOM_TYPE    |The room type to be switched to. See the API EnterRoom for the audio type of the user's room. |

#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
ITMGContextGetInstance()->GetRoom()->ChangeRoomType(ITMG_ROOM_TYPE_FLUENCY);
```


### Obtain the audio type of the user's room
This API is used to obtain the audio type of the user's room. The returned value is the audio type of the room. Value 0 means that an error occurred while obtaining the audio type of the user's room. See the API EnterRoom for the audio type of the user's room.

#### Function prototype  
```
IITMGContext TMGRoom public  int GetRoomType()
```

#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
ITMGContextGetInstance()->GetRoom()->GetRoomType();
```


### Callback after the room type is set
After the room type is set, the event message ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE is returned in the callback response. The returned parameters include result, error_info, and new_room_type. new_room_type represents the following information and is identified in the OnEvent function.

| Event Sub-type | Parameters | Description |
| ------------- |:-------------:|-------------|
| ITMG_ROOM_CHANGE_EVENT_ENTERROOM		|1 	|Indicates that the existing audio type is inconsistent with and changed to that of the room to enter.	|
| ITMG_ROOM_CHANGE_EVENT_START			|2	|Indicates that there are members in the room and the audio type starts changing (e.g., the audio type is changed after the ChangeRoomType API is called.) |
| ITMG_ROOM_CHANGE_EVENT_COMPLETE		|3	|Indicates that there are members in the room and the audio type has changed |
| ITMG_ROOM_CHANGE_EVENT_REQUEST			|4	|Indicates that a room member calls the ChangeRoomType API to request a change in the audio type |	


#### Sample code  
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE == type)
        {
		//Work with room type events
	 }
}
```

### Member status change
Notification about this event is sent only when the status changes. To obtain the member status in real time, cache the notification when receiving it at a higher layer. The event message ITMG_MAIN_EVNET_TYPE_USER_UPDATE is returned. The "data" includes event_id and user_list, and event_id is identified in the OnEvent function.
Audio events are subject to a threshold above which a notification is sent. The message "A member stops sending audio packages" is sent when audio packages are not received after 2 seconds.

|event_id     | Description | What Is Maintained at the App Side |
| ------------- |:-------------:|-------------|
|ITMG_EVENT_ID_USER_ENTER    				|A member enters the room			| Member list		|
|ITMG_EVENT_ID_USER_EXIT    				|A member exits the room			| Member list		|
|ITMG_EVENT_ID_USER_HAS_AUDIO    		|A member sends audio packages		| Chat member list	|
|ITMG_EVENT_ID_USER_NO_AUDIO    			|A member stops sending audio packages		| Chat member list	|

#### Sample code  

```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVNET_TYPE_USER_UPDATE:
		{
		//Process
		//The developer parses the parameter to obtain event_id and user_list.
		    switch (eventID)
 		    {
 		    case ITMG_EVENT_ID_USER_ENTER:
  			    //A member enters the room
  			    break;
 		    case ITMG_EVENT_ID_USER_EXIT:
  			    //A member exits the room
			    break;
		    case ITMG_EVENT_ID_USER_HAS_AUDIO:
			    //A member sends audio packages
			    break;
		    case ITMG_EVENT_ID_USER_NO_AUDIO:
			    //A member stops sending audio packages
			    break;
 		    default:
			    break;
		    }
		break;
		}
	}
}
```

### Message details

| Message | Description of Message   
| ------------- |:-------------:|
|ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    				       |Enters the audio/video room |
|ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    				         	|Exits the audio/video room |
|ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    		       |Room disconnection due to network or other reasons |
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE				|Room type change event |

### Details of Data corresponding to the message
| Message | Data         | Example |
| ------------- |:-------------:|------------- |
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    				|result; error_info					|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    				|result; error_info  					|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    		|result; error_info  					|{"error_info":"waiting timeout, please check your network","result":0}|
| ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE    		|result; error_info; new_room_type	|{"error_info":"","new_room_type":0,"result":0}|


## Audio APIs for Voice Chat
The audio APIs for Voice Chat can only be called after the SDK is initialized and there are members in the room.
Calling scenario example:

When you click the On/Off button of the microphone or speaker on the page, it is recommended as follows:
- For most gaming Apps, call EnableAudioCaptureDevice/EnableAudioSend and EnableAudioPlayDevice/EnableAudioRecv at the same time;
- For other mobile Apps (such as social networking Apps), enabling/disabling a capturing device will restart both the capturing and playback devices. If the App is playing a background music, it will also be interrupted. Playback won't be interrupted if the microphone is enabled/disabled through control of upstream/downstream. Calling method: Call EnableAudioCaptureDevice(true) and EnabledAudioPlayDevice(true) once after entering the room. Enable the microphone only by calling EnableAudioSend/Recv to send/receive audio stream.

It is recommended to call PauseAudio/ResumeAudio for mutually exclusive (releasing the recording permission to other modules).

| API | Description |
| ------------- |:-------------:|
|PauseAudio    				       	   |Pauses audio engine |
|ResumeAudio    				      	 |Resumes audio engine |
|EnableAudioCaptureDevice    		|Enables/disables a capturing device |
|IsAudioCaptureDeviceEnabled    	|Obtains the status of a capturing device |
|EnableAudioSend    				|Enables/disables audio upstream |
|IsAudioSendEnabled    				|Obtains the status of audio upstream |
|GetMicLevel    						|Obtains real-time microphone volume |
|SetMicVolume    					|Sets microphone volume |
|GetMicVolume    					|Obtains microphone volume |
|EnableAudioPlayDevice    			|Enables/disables a playback device		|
|IsAudioPlayDeviceEnabled    		|Obtains the status of a playback device |
|EnableAudioRecv    					|Enables/disables audio downstream 	|
|IsAudioRecvEnabled    				|Obtains the status of audio downstream |
|GetSpeakerLevel    					|Obtains real-time speaker volume |
|SetSpeakerVolume    				|Sets speaker volume |
|GetSpeakerVolume    				|Obtains speaker volume |
|EnableLoopBack    					|Enables/disables in-ear monitoring |

### Pause the capture and playback features of the audio engine
This API is called to pause the capture and playback features of the audio engine. It is a synchronous API and only works when members have entered the room.
For releasing only the capturing or playback device, see API EnableAudioCaptureDevice and EnableAudioPlayDevice.

#### Function prototype  

```
ITMGContext ITMGAudioCtrl int PauseAudio()
```
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->PauseAudio();
```

### Resume the capture and playback features of the audio engine
This API is called to resume the capture and playback features of the audio engine. It is a synchronous API and only works when members have entered the room.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl int ResumeAudio()
```
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->ResumeAudio();
```



### Obtain the number of microphones
This API is used to obtain the number of microphones.

#### Function prototype  
```
ITMGAudioCtrl virtual int GetMicListCount()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicListCount();
```

### Enumerate microphones
This API is used to enumerate microphones. It is used with API GetMicListCount.

#### Function prototype 
```
ITMGAudioCtrl virtual int GetMicList(TMGAudioDeviceInfo* ppDeviceInfoList, int nCount)

class TMGAudioDeviceInfo
{
public:
	const char* pDeviceID;
	const char* pDeviceName;
};
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| ppDeviceInfoList    	|TMGAudioDeviceInfo   	| Device list		|
| nCount    		|int     		| Obtains the number of microphones	|
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicList(ppDeviceInfoList,nCount);
```



### Select the microphone
This API is used to select the microphone. If this API is not called or an empty string is passed in, the default microphone is selected.
#### Function prototype  
```
ITMGAudioCtrl virtual int SelectMic(const char* pMicID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| pMicID    |char*      |Microphone ID |
#### Sample code  
```
const char* pMicID ="1";
ITMGContextGetInstance()->GetAudioCtrl()->SelectMic(pMicID);
```

### Enable/disable a capturing device
This API is used to enable/disable a capturing device. The devices is not enabled by default after a user enters the room.
- This API can only be called after a user enters the room. The device is disabled after the user exits the room.
- Operations such as permission application and volume type adjustment come with enabling the capturing device on mobile.

#### Function prototype  
```
ITMGContext virtual int EnableAudioCaptureDevice(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| enable    |bool     |To enable the capturing device, set this parameter to true, otherwise, set it to false. |

> Sample code

```
Enable a capturing device
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioCaptureDevice(true);
```

### Obtain the status of a capturing device
This API is used to obtain the status of a capturing device.
#### Function prototype

```
ITMGContext virtual bool IsAudioCaptureDeviceEnabled()
```
#### Sample code

```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioCaptureDeviceEnabled();
```

### Enable/disable audio upstream
This API is used to enable/disable audio upstream. If the capturing device is already enabled, captured audio data will be sent. If it is not enabled, it remains silent. To enable/disable a capturing device, see API EnableAudioCaptureDevice.

#### Function prototype

```
ITMGContext  virtual int EnableAudioSend(bool bEnable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| bEnable    |bool     |To enable the audio upstream, set this parameter to true, otherwise, set it to false. |

> Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioSend(true);
```

### Obtain the status of audio upstream
This API is used to obtain the status of audio upstream.
#### Function prototype  
```
ITMGContext virtual bool IsAudioSendEnabled()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioSendEnabled();
```

### Obtain real-time microphone volume
This API is used to obtain real-time microphone volume. An int value is returned.
#### Function prototype  
```
ITMGAudioCtrl virtual int GetMicLevel()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicLevel();
```

### Set software volume for the microphone
This API is used to set the software volume for the microphone. The corresponding parameter is "volume". The value "0" sets the volume to Mute, and "100" means the volume remains unchanged. Default is 100.
#### Function prototype  
```
ITMGAudioCtrl virtual int SetMicVolume(int vol)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| vol    |int      | Sets the volume, value range: 0 to 200 |
#### Sample code  
```
int vol = 100;
ITMGContextGetInstance()->GetAudioCtrl()->SetMicVolume(vol);
```

### Obtain software volume for the microphone
This API is used to obtain the software volume for the microphone. An int value is returned. Value 101 represents API SetMicVolume has not been called.
#### Function prototype  
```
ITMGAudioCtrl virtual int GetMicVolume()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicVolume();
```

### Obtain the number of speakers
This API is used to obtain the number of speakers.

#### Function prototype  

```
ITMGAudioCtrl virtual int GetSpeakerListCount()
```
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerListCount();
```

### Enumerate speakers
This API is used to enumerate speakers. It is used with API GetSpeakerListCount.

#### Function prototype  
```
ITMGAudioCtrl virtual int GetSpeakerList(TMGAudioDeviceInfo* ppDeviceInfoList, int nCount)

class TMGAudioDeviceInfo
{
public:
	const char* pDeviceID;
	const char* pDeviceName;
};
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| ppDeviceInfoList    	|TMGAudioDeviceInfo    	| Device list		|
| nCount   		|int     		| Obtains the number of speakers	|
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerList(ppDeviceInfoList,nCount);
```

### Select speakers
This API is used to select the playback device. If this API is not called or an empty string is passed in, the default device is selected.
#### Function prototype  
```
ITMGAudioCtrl virtual int SelectSpeaker(const char* pSpeakerID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| pSpeakerID    |char*      |Speaker ID |
#### Sample code  
```
const char* pSpeakerID ="1";
ITMGContextGetInstance()->GetAudioCtrl()->SelectSpeaker(pSpeakerID);
```

### Enable/disable a playback device
This API is used to enable/disable a playback device.

#### Function prototype  
```
ITMGContext virtual int EnableAudioPlayDevice(bool enable) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| enable    |bool       	| To disable the playback device, set this parameter to false, otherwise, set it to true.	|
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioPlayDevice(true);
```

### Obtain the status of a playback device
This API is used to obtain the status of a playback device.
#### Function prototype

```
ITMGContext virtual bool IsAudioPlayDeviceEnabled()
```
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioPlayDeviceEnabled();
```

### Enable/disable audio downstream
This API is used to enable/disable audio downstream. If the playback device is enabled, audio data of other users in the room will be played back. If it is not enabled, it remains silent. To enable/disable a playback device, see API EnableAudioPlayDevice.

#### Function prototype  

```
ITMGContext virtual int EnableAudioRecv(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| enable    |bool     |To enable the audio downstream, set this parameter to true, otherwise, set it to false. |

#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioRecv(true);
```



### Obtain the status of audio downstream
This API is used to obtain the status of audio downstream.
#### Function prototype  
```
ITMGContext virtual bool IsAudioRecvEnabled() 
```

#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioRecvEnabled();
```

### Obtain real-time speaker volume
This API is used to obtain real-time speaker volume. An int value is returned to indicate the real-time speaker volume.
#### Function prototype  
```
ITMGAudioCtrl virtual int GetSpeakerLevel()
```

#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerLevel();
```

### Set software volume for the speaker
This API is used to set the software volume for the speaker.
The corresponding parameter is "volume". The value "0" sets the volume to Mute, and "100" means the volume remains unchanged. Default is 100.

#### Function prototype  
```
ITMGAudioCtrl virtual int SetSpeakerVolume(int vol)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| vol    |int        | Sets the volume, value range: 0 to 200 |
#### Sample code  
```
int vol = 100;
ITMGContextGetInstance()->GetAudioCtrl()->SetSpeakerVolume(vol);
```

### Obtain software volume for the speaker
This API is used to obtain the software volume for the speaker. An int value is returned to indicate the software volume for the speaker. Value 101 represents API SetSpeakerVolume has not been called.
"Level" indicates the real-time volume, and "Volume" the software volume for the speaker. The ultimate volume equals to Level*Volume%. For example, if the value for "Level" is 100 and the one for "Volume" is 60, the ultimate volume will be "60".

#### Function prototype  
```
ITMGAudioCtrl virtual int GetSpeakerVolume()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerVolume();
```


### Enable in-ear monitoring
This API is used to enable in-ear monitoring.
#### Function prototype  
``` 
ITMGAudioCtrl virtual int EnableLoopBack(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| enable    |bool         | Specifies whether to enable in-ear monitoring |
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableLoopBack(true);
```


## APIs Related to the Accompaniment in Voice Chat
| API | Description |
| ------------- |:-------------:|
|StartAccompany    				       |Starts playing back the accompaniment |
|StopAccompany    				   	|Stops playing back the accompaniment |
|IsAccompanyPlayEnd				|Indicates whether the accompaniment is over |
|PauseAccompany    					|Pauses playing back the accompaniment |
|ResumeAccompany					|Replays the accompaniment |
|SetAccompanyVolume 				|Sets the accompaniment volume |
|GetAccompanyVolume				|Obtains the volume of the accompaniment |
|SetAccompanyFileCurrentPlayedTimeByMs 				|Sets the playback progress |

### Start playing back the accompaniment
This API is used to start playing back the accompaniment. Four formats are supported: m4a, AAC, wav, and mp3. This API is used to reset the volume.

#### Function prototype  
```
ITMGAudioEffectCtrl virtual int StartAccompany(const char* filePath, bool loopBack, int loopCount, int msTime) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| filePath    	|char* 	|Accompaniment's playback path						|
| loopBack  	|bool	|Indicates whether to send a mix. This is generally set to true, indicating that other users can also hear the accompaniment.	|
| loopCount	|int 	|Number of loops. Value -1 means an infinite loop.				|
| msTime	|int   	| Delay time						|
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StartAccompany(filePath,true,-1,0);
```

### Callback for accompaniment playback
After the accompaniment is over, the event message ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH is returned, which is identified in the OnEvent function.
#### Sample code  
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process
		break;
	   	}
		...
        case ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH:
		{
		//Process
		break;
		}
	}
}
```

### Stop playing back the accompaniment
This API is used to stop playing back the accompaniment.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int StopAccompany(int duckerTime)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| duckerTime	|int             | Fading time |

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopAccompany(0);
```

### Indicate whether the accompaniment is over
If it is over, "true" is returned. If it is not, "false" is returned.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual bool IsAccompanyPlayEnd()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->IsAccompanyPlayEnd();
```

### Pause playing back the accompaniment
This API is used to pause playing back the accompaniment.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int PauseAccompany()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseAccompany();
```

### Replay the accompaniment
This API is used to replay the accompaniment.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int ResumeAccompany()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAccompany();
```

### Specify whether you can hear the accompaniment
This API is used to specify whether you can hear the accompaniment.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int EnableAccompanyPlay(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|--------------|
| enable    |bool | Indicates whether you can hear the accompaniment |
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyPlay(false);
```

### Specify whether others can also hear the accompaniment
This API is used to specify whether others can also hear the accompaniment.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int EnableAccompanyLoopBack(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|--------------|
| enable    |bool | Indicates whether you can hear the accompaniment |

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyLoopBack(false);
```

### Set the accompaniment volume
This API is used to set the DB volume. Value range: 0-200. Default is 100. A value greater than 100 means volume up, otherwise volume down.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int SetAccompanyVolume(int vol)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| vol    |int | Indicates the volume value |

#### Sample code  
```
int vol=100;
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetAccompanyVolume(vol);
```

### Obtain the volume of the accompaniment
This API is used to get the DB volume.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int GetAccompanyVolume()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyVolume();
```

### Obtain the accompaniment playback progress
The following two APIs are used to obtain the accompaniment playback progress. Note: Current/Total = current loop times, Current % Total = current loop playback position.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int GetAccompanyFileTotalTimeByMs()
ITMGAudioEffectCtrl virtual int GetAccompanyFileCurrentPlayedTimeByMs()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyFileTotalTimeByMs();
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyFileCurrentPlayedTimeByMs();
```

### Set the playback progress
This API is used to set the playback progress.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int SetAccompanyFileCurrentPlayedTimeByMs(unsigned int time)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| time    |int | Indicates the playback progress in milliseconds |

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetAccompanyFileCurrentPlayedTimeByMs(time);
```



## APIs Related to Sound Effect in Voice Chat

| API | Description |
| ------------- |:-------------:|
|PlayEffect    		|Plays the sound effect |
|PauseEffect    	|Pauses the sound effect |
|PauseAllEffects	|Pauses all sound effects |
|ResumeEffect    	|Replays the sound effect |
|ResumeAllEffects	|Replays all sound effects |
|StopEffect 		|Stops the sound effect |
|StopAllEffects		|Stops all sound effects |
|SetVoiceType 		|Voice changing effects |
|GetEffectsVolume	|Obtains the volume of sound effects |
|SetEffectsVolume 	|Sets the volume of sound effects |


### Play the sound effect
This API is used to play the sound effect. The sound effect ID in the parameter needs to be managed by the App side, uniquely identifying a separate file. Four formats are supported: m4a, AAC, wav, and mp3.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int PlayEffect(int soundId,  const char* filePath, bool loop, double pitch, double pan, double gain)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId  	|int        	|Indicates the sound effect ID |
| filePath    	|char*     	|Indicates the sound effect path |
| loop    		|bool  	|Indicates whether to repeat playback |
| pitch    	|double	|Indicates the playback frequency, and the default is 1.0. The smaller the value, the slower the playback speed and the longer the time.|
| pan    		|double	|Indicates the channel, value range: -1.0 to 1.0. -1.0 means only the left channel is turned on. |
| gain    		|double	|Indicates the gain volume, ranging from 0.0 to 1.0. The default is 1.0 |

#### Sample code  
```
double pitch = 1.0;
double pan = 0.0;
double gain = 0.0;
ITMGContextGetInstance()->GetAudioEffectCtrl()->PlayEffect(soundId,filepath,true,pitch,pan,gain);
```

### Pause the sound effect
This API is used to pause playing back the sound effect.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int PauseEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int | Indicates the sound effect ID |

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseEffect(soundId);
```

### Pause all sound effects
This API is used to pause all sound effects.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int PauseAllEffects()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseAllEffects();
```

### Replay the sound effect
This API is used to replay the sound effect.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int ResumeEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int | Indicates the sound effect ID |
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeEffect(soundId);
```

### Replay all sound effects
This API is used to replay all sound effects.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int ResumeAllEffects()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAllEffects();
```

### Stop the sound effect
This API is used to stop the sound effect.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int StopEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int | Indicates the sound effect ID |
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopEffect(soundId);
```

### Stop all sound effects
This API is used to stop all sound effects.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int StopAllEffects()
```


#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopAllEffects();
```



### Voice changing effects
This API is used to set the voice changing effects.
#### Function prototype  
```
TMGAudioEffectCtrl int setVoiceType(int type)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| type    |int | Indicates the type of local voice changing effect |



| Type | Parameter | Description |
| ------------- |-------------|------------- |
|ITMG_VOICE_TYPE_ORIGINAL_SOUND  		|0	|Original sound |
|ITMG_VOICE_TYPE_LOLITA    				|1	|Lolita |
|ITMG_VOICE_TYPE_UNCLE  				|2	|Uncle |
|ITMG_VOICE_TYPE_INTANGIBLE    			|3	|Ethereal |
|ITMG_VOICE_TYPE_DEAD_FATBOY  			|4	|Fat boy |
|ITMG_VOICE_TYPE_HEAVY_MENTA			|5	|Heavy metal |
|ITMG_VOICE_TYPE_DIALECT 				|6	|Dialect |
|ITMG_VOICE_TYPE_INFLUENZA 				|7	|Catching cold |
|ITMG_VOICE_TYPE_CAGED_ANIMAL 			|8	|Trapped beast |
|ITMG_VOICE_TYPE_HEAVY_MACHINE			|9	|Mechanic sound |
|ITMG_VOICE_TYPE_STRONG_CURRENT			|10	|Strong current |
|ITMG_VOICE_TYPE_KINDER_GARTEN			|11	|Kindergarten |
|ITMG_VOICE_TYPE_HUANG 					|12	|Minions |

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->setVoiceType(0);
```

### Obtain the volume of sound effects
This API is used to obtain the volume (linear volume) of sound effects. A value greater than 100 means volume up, otherwise volume down.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int GetEffectsVolume()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetEffectsVolume();
```

### Set the volume of sound effects
This API is used to set the volume of sound effects.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int SetEffectsVolume(int volume)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| volume    |int | Indicates the volume value |

#### Sample code  
```
int volume=1;
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetEffectsVolume(volume);
```
## Voice Message
Initialize the SDK before using voice message and voice-to-text converting features.

| API | Description |
| ------------- |:-------------:|
|ApplyPTTAuthbuffer    |Authentication initialization	|
|SetMaxMessageLength    |Specifies the maximum length of a voice message |
|StartRecording		|Starts recording |
|StopRecording    	|Stops recording |
|CancelRecording	|Cancels recording |
|UploadRecordedFile 	|Uploads voice files |
|DownloadRecordedFile	|Downloads voice files |
|PlayRecordedFile 	|Plays voice files |
|StopPlayFile		|Stops playing voice files |
|GetFileSize 		|Indicates the size of a voice file |
|GetVoiceFileDuration	|Indicates the length of a voice file |
|SpeechToText 		|Converts the voice file into text with Speech Recognition |


### Authentication initialization
Call authentication initialization after initializing the SDK. To obtain authBuffer, see the API of voice chat authentication.
#### Function prototype  
```
ITMGPTT virtual void ApplyPTTAuthbuffer(const char* authBuffer, int authBufferLen)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| authBuffer    |char* | Authentication |
| authBufferLen    |int   		| Length of the authentication |

#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->ApplyPTTAuthbuffer(authBuffer,authBufferLen);
```

### Specify the maximum length of a voice message
This API is used to specify the maximum length of a voice message, which is limited to 60 seconds.
#### Function prototype  
```
ITMGPTT virtual void SetMaxMessageLength(int msTime)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| msTime    |int | Indicates the length of a voice message |
#### Sample code  
```
int msTime = 10;
ITMGContextGetInstance()->GetPTT()->SetMaxMessageLength(msTime);
```

### Start recording
This API is used to start recording.
#### Function prototype  
```
ITMGPTT virtual void StartRecording(const char* fileDir)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileDir    |char* | Indicates the path for storing the voice file
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->SetMaxMessageLength(fileDir);
```

### Callback for starting recordings
The callback function OnEvent is called after the recording is started. The event message is ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE is returned, which is identified in the OnEvent function.

#### Sample code  
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE:
		{
		//Process
		break;
		}
	}
}

```

### Stop recording
This API is used to stop recording.
#### Function prototype  
```
ITMGPTT virtual int StopRecording()
```
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->StopRecording();
```

### Cancel recording
This API is used to cancel recording.
#### Function prototype  
```
ITMGPTT virtual int CancelRecording()
```
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->CancelRecording();
```

### Upload voice files
This API is used to upload voice files.
#### Function prototype  
```
ITMGPTT virtual void UploadRecordedFile(const char* filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    |char* | Indicates the path for uploading voice files |
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->UploadRecordedFile(filePath);
```

### Callback for uploading voice files
After the voice file is uploaded, the event message ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE is returned, which is identified in the OnEvent function.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE:
		{
		//Process
		break;
		}
	}
}
```

### Download voice files
This API is used to download voice files.
#### Function prototype  
```
ITMGPTT virtual void DownloadRecordedFile(const char* fileId, const char* filePath, const char* authBuffer, int authBufferLen) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileId  		|char*   	|URL to a file |
| filePath 	|char*  	|Local path for saving the file |
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->DownloadRecordedFile(fileID,filePath);
```

### Callback for downloading voice files
After the voice file is downloaded, the event message ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE is returned, which is identified in the OnEvent function.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE:
		{
		//Process
		break;
		}
	}
}
```

### Play voice files
This API is used to play voice files.
#### Function prototype  
```
ITMGPTT virtual void PlayRecordedFile(const char* filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    |char* | Indicates the path to a file |
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->PlayRecordedFile(filePath);
```

### Callback for playing voice files
After the voice file is played back, the event message ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE is returned, which is identified in the OnEvent function.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE:
		{
		//Process
		break;
		}
	}
}
```

### Stop playing voice files
This API is used to stop playing back voice files.
#### Function prototype  
```
ITMGPTT virtual int StopPlayFile()
```
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->StopPlayFile();
```
### Obtain the size of a voice file
This API is used to get the size of a voice file.
#### Function prototype  
```
ITMGPTT virtual int GetFileSize(const char* filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    |char* | Indicates the path to a voice file |
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->GetFileSize(filePath);
```

### Obtain the length of a voice file
This API is used to obtain the length of a voice file (in milliseconds).
#### Function prototype  
```
ITMGPTT virtual int GetVoiceFileDuration(const char* filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    |char* | Indicates the path to a voice file |
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->GetVoiceFileDuration(filePath);
```



### Convert the specified voice file into text with Speech Recognition
This API is used to convert the specified voice file into text with Speech Recognition.
#### Function prototype  
```
ITMGPTT virtual void SpeechToText(const char* fileID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileID    |char* | Indicates the URL to a voice file |
#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->SpeechToText(fileID);
```

### Callback for Speech Recognition
After the specified voice file is converted into text with Speech Recognition, the event message ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE is returned, which is identified in the OnEvent function.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE:
		{
		//Process
		break;
		}
	}
}
```


## Advanced APIs

### Obtain diagnostic messages
This API is used to obtain information about the quality of real-time audio/video calls. This API is mainly used to check the quality of real-time calls and troubleshoot problems, and can be ignored at the business side.
#### Function prototype  

```
ITMGRoom virtual const char* GetQualityTips()
```
#### Sample code  

```
ITMGContextGetInstance()->GetRoom()->GetQualityTips();
```


### Obtain the version number
This API is used to get the SDK version number for analysis.
#### Function prototype
```
ITMGContext virtual const char* GetSDKVersion()
```
#### Sample code  
```
ITMGContextGetInstance()->GetSDKVersion();
```

### Set the level of logs to be printed
This API is used to set the level of logs to be printed.
#### Function prototype
```
ITMGContext virtual void SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| logLevel    		|int | Level of logs to be printed |
| enableWrite    	| bool | Indicates whether to write a file. The default is Yes |
| enablePrint    	|bool | Indicates whether to write a console. The default is Yes |


|ITMG_LOG_LEVEL|Description |
| -------------------------------|:-------------:|
|TMG_LOG_LEVEL_NONE=0		|Do not print logs |
|TMG_LOG_LEVEL_ERROR=1		|Prints error logs (default) |
|TMG_LOG_LEVEL_INFO=2			|Prints prompt logs |
|TMG_LOG_LEVEL_DEBUG=3		|Prints development and debugging logs |
|TMG_LOG_LEVEL_VERBOSE=4		|Prints high-frequency logs |

#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
context->SetLogLevel(0,true,true);
```

### Set the path of logs to be printed
This API is used to set the path of logs to be printed.
The default path is:

| Platform | Path |
| ------------- |:-------------:|
|Windows 	|%appdata%\Tencent\GME\ProcessName|
|iOS    		|Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents|
|Android	|/sdcard/Android/data/xxx.xxx.xxx/files|
|Mac    		|/Users/username/Library/Containers/xxx.xxx.xxx/Data/Documents|

#### Function prototype
```
ITMGContext virtual void SetLogPath(const char* logDir) 
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| logDir    		|char* | Path |
#### Sample code  
```
cosnt char* logDir = ""// You can set your own path
ITMGContext* context = ITMGContextGetInstance();
context->SetLogPath(logDir);
```

### Add an ID to the audio data blacklist
This API is used to add an ID to the audio data blacklist. A return value of 0 indicates that the call failed.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl int AddAudioBlackList(const char* openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| openId    |char* | ID that needs to be added to the blacklist |
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->AddAudioBlackList(openId);
```

### Remove an ID from the audio data blacklist
This API is used to remove an ID from the audio data blacklist. A return value of 0 indicates that the call failed.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl int RemoveAudioBlackList(const char* openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| openId    |char*       | ID that needs to be removed from the blacklist |
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->RemoveAudioBlackList(openId);
```


## Callback Messages

#### Message list:

| Message | Description of Message   
| ------------- |:-------------:|
|ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		| Enters the audio room |
|ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		| Exits the audio room |
|ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT		| Room disconnection due to network or other reasons |
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE		|Room type change event |
|ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    	|Adds a microphone |
|ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    	|Loses a microphone |
|ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE	|Adds a speaker |
|ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE	|Loses a speaker |
|ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH		|The accompaniment is over |
|ITMG_MAIN_EVNET_TYPE_USER_UPDATE		|The room members are updated |
|ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE	|PTT recording is completed |
|ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE	|PTT is successfully uploaded |
|ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE	|PTT is successfully downloaded |
|ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE		|The playback of PTT is completed |
|ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE	|The voice-to-text conversion is completed |

#### Data list:

| Message | Data         | Example |
| ------------- |:-------------:|------------- |
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		|result; error_info			|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		|result; error_info  			|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    	|result; error_info  			|{"error_info":"waiting timeout, please check your network","result":0}|
| ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE    	|result; error_info; new_room_type	|{"error_info":"","new_room_type":0,"result":0}|
| ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE	|result; error_info  			|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"Speaker  (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":false,"result":0}|
| ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE    	|result; error_info  			|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"Speaker  (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":false,"result":0}|
| ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    	|result; error_info  			|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"Microphone  (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":true,"result":0}|
| ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    	|result; error_info 			|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"Microphone  (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":true,"result":0}|
| ITMG_MAIN_EVNET_TYPE_USER_UPDATE    		|user_list;  event_id			|{"event_id":1,"user_list":["0"]}|
| ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE 	|result; file_path  			|{"filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE 	|result; file_path;file_id  		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE	|result; file_path;file_id  		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE 	|result; file_path  			|{"filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE	|result; file_path;file_id		|{"file_id":"","filepath":"","result":0}|


