## Overview
Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides a detailed description that makes it easy for Windows developers to debug and integrate the APIs of Game Multimedia Engine.


## How to Use
![](https://main.qcloudimg.com/raw/810d0404638c494d9d5514eb5037cd37.png)


### Key considerations for using GME

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

## Initialization-related APIs
GME should be initialized with the authentication data before entering a room.

| API | Description |
| ------------- |:-------------:|
|Init    	|Initializes GME 	| 
|Poll    	|Triggers event callback	|
|Pause   	|Pauses the system	|
|Resume 	|Resumes the system	|
|Uninit    	|Deinitializes GME 	|


### Get a singleton

Get ITMGContext single instance first and all calls should be done accroding to this instance. ITMGDelegate is defined in the Application which is used to receive and process the callback from this instance.    
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
void TMGTestScene::update(float delta)
{
    ITMGContextGetInstance()->Poll();
}
```


### Pause the system

This API is used to notify the engine for Pause when the system Pause occurs.
#### Function prototype

```
ITMGContext int Pause()
```

### Resume the system
This API is used to notify the engine for Resume when the system Resume occurs.
#### Function prototype

```
ITMGContext  int Resume()
```



### Deinitialize the SDK
This API is used to deinitialize SDK to make it uninitialized.

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
After the initialization, API for entering a room should be called before Voice Chat can start.

| API | Description |
| ------------- |:-------------:|
|GenAuthBuffer    	|Generates authentication data |
|EnterRoom   		|Enters a room |
|IsRoomEntered   	|Indicates whether the room is entered successfully |
|ExitRoom 		|Exits the room |
|ChangeRoomType 	|Modifies the audio type of the user's room |
|GetRoomType 		|Obtains the audio type of the user's room |


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
| dwRoomID |char* | Room ID, maximum to 127 characters (The room ID parameter for voice message must be set to "null") |
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

### Join a room
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


### Callback for entering a room
ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received after a user enters a room, the action of this event should be implemented in the OnEvent function.
#### Code Description
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

### Identify whether the room is entered successfully
This API is called to identify whether the room is entered successfully. A bool value is returned.
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
This API is called to exit the current room.
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
ITMG_MAIN_EVENT_TYPE_EXIT_ROOM message is received after a user exits a room, the action of this event should be implemented in the OnEvent function.
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
This API is used to modify the audio type of the user's room. A ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE callback event will be sent.
#### Function prototype  
```
IITMGContext TMGRoom public void ChangeRoomType((ITMG_ROOM_TYPE roomType)
```


| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomType    |ITMG_ROOM_TYPE    |The room type to be switched to. See the API EnterRoom for the audio type definition. |

#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
ITMGContextGetInstance()->GetRoom()->ChangeRoomType(ITMG_ROOM_TYPE_FLUENCY);
```


### Obtain the audio type of the user's room
This API is used to obtain the audio type of the user's room. The returned value is the audio type of the room. Returned value of 0 means error happens. The audio type definition can be found in the API EnterRoom.

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
ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE message is received after a user change the room type. The returned parameters include result, error_info, and new_room_type. new_room_type represents the following information and the action of each event should be implemented in the OnEvent function.

| Event Sub-type | Parameters | Description |
| ------------- |:-------------:|-------------|
| ITMG_ROOM_CHANGE_EVENT_ENTERROOM		|1 	|Indicates that the audio type is inconsistent with that of the room to be entered and it is changed to that of the room.	|
| ITMG_ROOM_CHANGE_EVENT_START			|2	|Indicates that the room is entered and the audio type starts changing (e.g., the audio type is changed after the ChangeRoomType API is called.) |
| ITMG_ROOM_CHANGE_EVENT_COMPLETE		|3	|Indicates that the room is entered and the audio type has changed |
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
Notification about this event is sent only when the member status changes. To obtain the member status in real time, cache the notification when receiving it at a higher layer. The event message ITMG_MAIN_EVNET_TYPE_USER_UPDATE is returned. The "data" includes event_id and user_list, and the action of event_id should be implemented in the OnEvent function.
These events will only be sent when exceeding a certain threshold. For example, when audio data of a user is not received for more than two seconds, the ITMG_EVENT_ID_USER_NO_AUDIO will be sent.

|event_id     | Description | What is maintained at the App side |
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
		//The developer parses the parameter to obtain vent_id and user_list.
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

### Quality monitoring events
The message for quality monitoring event is ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_QUALITY. The returned parameters include weight, floss, and delay, which represent the following information and the action of this event should be implemented in the OnEvent function.

| Parameter | Description |
| ------------- |-------------|
|weight    				| Its value ranges from 1 to 50. The value of 50 indicates excellent quality of audio packets, and the value of 1 indicates poor quality of audio packets, which can barely be used; and "0" represents an initial value and is meaningless. |
|floss    				| Packet loss |
|delay    		| Voice chat delay (ms) |

### Message details

| Message | Description of message |   
| ------------- |:-------------:|
|ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    				       |Enters the room |
|ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    				         	|Exits the room |
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
The audio APIs for Voice Chat can only be called after the SDK is initialized and the room is entered successfully.
Call scenario examples:

When a user click the UI button to enable or disable the microphone or speaker:
- For most game Apps, it's recommended to call EnableMic and EnableSpeaker APIs. Because calling EnableMic is equivalent to calling EnableAudioCaptureDevice and EnableAudioSend at the same time, and calling EnableSpeaker is equivalent to calling EnableAudioPlayDevice and EnableAudioRecv at the same time.

- For other mobile Apps (such as social networking Apps), enabling/disabling a capturing device will restart both the capturing and the playback devices. If the App is playing background music, it will also be interrupted. But if the microphone is enabled/disabled through control of upstream/downstream, playback will not be interrupted . So the calling method is: Call EnableAudioCaptureDevice(true) and EnableAudioPlayDevice(true) once after entering the room, and call EnableAudioSend/Recv to send/receive audio streams when the microphone button is clicked to enable or disable.

If you do not need to enable both the microphone and the speaker (releasing the recording permission to other modules), it is recommended to call PauseAudio/ResumeAudio.


| API | Description |
| ------------- |:-------------:|
|PauseAudio    				       	|Pauses audio engine |
|ResumeAudio    				      	|Resumes audio engine |
|GetMicListCount    				       	|Obtains the number of microphones |
|GetMicList    				      	|Enumerates microphones |
|GetSpeakerListCount    				      	|Obtains the number of speakers |
|GetSpeakerList    				      	|Enumerates speakers |
|SelectMic    				      	|Selectes microphones |
|SelectSpeaker    				|Selectes speakers |
|EnableMic    						|Enables/disables the microphone |
|GetMicState    						|Obtains the microphone status |
|EnableAudioCaptureDevice    		|Enables audio capture device		|
|IsAudioCaptureDeviceEnabled    	|Indicates if audio capture device is enabled or not	|
|EnableAudioSend    				|Enables the audio sending 	|
|IsAudioSendEnabled    				|Indicates if audio is being sent or not	|
|GetMicLevel    						|Obtains real-time microphone volume |
|SetMicVolume    					|Sets microphone volume |
|GetMicVolume    					|Obtains microphone volume |
|EnableSpeaker    					|Enables/disables the speaker |
|GetSpeakerState    					|Obtains the speaker status |
|EnableAudioPlayDevice    			|Enables audio playback device		|
|IsAudioPlayDeviceEnabled    		|Indicates if audio playback devices is enabled or not	|
|EnableAudioRecv    					|Enables the audio receving	|
|IsAudioRecvEnabled    				|Indicates if audio is being received or not	|
|GetSpeakerLevel    					|Obtains real-time speaker volume |
|SetSpeakerVolume    				|Sets speaker volume |
|GetSpeakerVolume    				|Obtains speaker volume |
|EnableLoopBack    					|Enables/disables in-ear monitoring |

### Pause the capture and playback features of the audio engine
This API is called to pause the capture and playback features of the audio engine, and only works when room is entered successfully.
You can get the microphone permission after calling the EnterRoom API successfully, and other programs cannot capture audio data from the microphone during your use of microphone. Calling EnableMic(false) does not release the microphone.
If you really need to release the microphone, call PauseAudio, which can cause the engine to be paused entirely. To resume audio capturing, call ResumeAudio.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl int PauseAudio()
```
#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->PauseAudio();
```

### Resume the capture and playback features of the audio engine
This API is called to resume the capture and playback features of the audio engine, and only works when room is entered successfully.
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
This API is used together with the GetMicListCount API to enumerate microphones.

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
| nCount    		|int     		|The number of microphones obtained	|

#### Sample code  

```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicList(ppDeviceInfoList,nCount);
```



### Select the microphone
This API is used to select the microphone. If this API is not called or an "DEVICEID_DEFAULT" is passed in, the default microphone is selected.The device ID comes from the GetMicList API return list.
#### Function prototype  
```
ITMGAudioCtrl virtual int SelectMic(const char* pMicID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| pMicID    |char*      |Microphone ID |

#### Sample code  
```
const char* pMicID ="{0.0.1.00000000}.{7b0b712d-3b46-4f7a-bb83-bf9be4047f0d}";
ITMGContextGetInstance()->GetAudioCtrl()->SelectMic(pMicID);
```

### Enable/disable the microphone
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

### Obtain the microphone status
This API is used to obtain the microphone status. "0" means microphone is enabled, "1" means microphone is disabled, "2" means microphone is under working.
#### Function prototype  
```
ITMGAudioCtrl virtual int GetMicState()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicState();
```

### Enable/disable audio capture device
This API is used to enable/disable the audio capture device. The audio capture device is not enabled by default. 
- API can only be called after the room is entered.The device will disabled automatically after exiting the room.
- For mobile use case, permission is normally asked when enabling the capture device.

#### Function prototype   

```
ITMGContext virtual int EnableAudioCaptureDevice(bool enable)
```
|Parameter     | Type         |Description|
| ------------- |:-------------:|-------------|
| enable    |bool     | true means enable，false means disable|

#### Sample code 

```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioCaptureDevice(true);
```

### Obtain the audio capture device status
This API is used to obtain the audio capture device status.
#### Function prototype

```
ITMGContext virtual bool IsAudioCaptureDeviceEnabled()
```
#### Sample code 

```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioCaptureDeviceEnabled();
```

### Enable/disable the audio sending

This API is used to enable/disable the audio sending. Enable means sending the captured voice. 

#### Function prototype

```
ITMGContext  virtual int EnableAudioSend(bool bEnable)
```
|Parameter     | Type         |Description|
| ------------- |:-------------:|-------------|
| bEnable    |bool     |true means enable audio sending，false means not|

#### Sample code

```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioSend(true);
```

### Obtain status on if captured audio is being sent 
This API is called to obtain the status if captured audio is being sent.
#### Function prototype
```
ITMGContext virtual bool IsAudioSendEnabled()
```
#### Sample code
```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioSendEnabled();
```

### Obtain real-time microphone volume
This API is used to obtain real time microphone volume. An int value is returned.
#### Function prototype  
```
ITMGAudioCtrl virtual int GetMicLevel()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicLevel();
```

### Set software volume for the microphone
This API is used to set software volume for the microphone. The value "0" means Mute, and "100" means the volume remains unchanged. Default value is 100.
#### Function prototype  
```
ITMGAudioCtrl virtual void SetMicVolume(int vol)
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
This API is used to obtain the software volume for the microphone. An int value is returned to indicate the software volume for the microphone. Returned value of 101 means SetMicVolume() has not been called.
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
This API is used together with the GetSpeakerListCount API to enumerate speakers.

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
| nCount   		|int     		| The number of speakers obtained	|

#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerList(ppDeviceInfoList,nCount);
```

### Select speakers
This API is used to select the playback device.If this API is not called or an "DEVICEID_DEFAULT" is passed in, the default device is selected.The device ID comes from the GetSpeakerList API return list.
#### Function prototype  
```
ITMGAudioCtrl virtual int SelectSpeaker(const char* pSpeakerID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| pSpeakerID    |char*      |Speaker ID |

#### Sample code  
```
const char* pSpeakerID ="{0.0.1.00000000}.{7b0b712d-3b46-4f7a-bb83-bf9be4047f0d}";
ITMGContextGetInstance()->GetAudioCtrl()->SelectSpeaker(pSpeakerID);
```

### Enable/disable the speaker
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

### Obtain the speaker status
This API is used to obtain the speaker status. "0" means speaker is enabled, "1" means speaker is disabled, "2" means speaker is under working.
#### Function prototype  
```
ITMGAudioCtrl virtual int GetSpeakerState()
```

#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerState();
```

### Enable/disable audio playback device
This API is used to enable/disable audio playback device.

#### Function prototype
```
ITMGContext virtual int EnableAudioPlayDevice(bool enable) 
```
|Parameter     | Type         |Description|
| ------------- |:-------------:|-------------|
| enable    |bool        |true means enable, false means disable|

#### Sample code 
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioPlayDevice(true);
```

### Obtain audio playback device status
This API is used to obtain the status of audio playback device.
#### Function prototype

```
ITMGContext virtual bool IsAudioPlayDeviceEnabled()
```
#### Sample code 

```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioPlayDeviceEnabled();
```

### Enable/disable the audio receiving
This API is used to enable/disable the audio receving. Enable means playing the received voice. 

#### Function prototype

```
ITMGContext virtual int EnableAudioRecv(bool enable)
```
|Parameter     | Type         |Description|
| ------------- |:-------------:|-------------|
| enable    |bool     |true means enabling the audio receing. false means not|


#### Sample code

```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioRecv(true);
```


### Obtain status on if received audio is being played 
This API is called to obtain the status if received audio is being played.
#### Function prototype
```
ITMGContext virtual bool IsAudioRecvEnabled() 
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioRecvEnabled();
```

### Obtain real-time speaker volume
This API is used to obtain real time speaker volume. An int value is returned to indicate the real-time speaker volume.
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
The value "0" means Mute, and "100" means the volume remains unchanged. Default value is 100.


#### Function prototype  
```
ITMGAudioCtrl virtual void SetSpeakerVolume(int vol)
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
This API is used to obtain the software volume for the speaker. An int value is returned to indicate the software volume for the speaker. Returned value of 101 means SetSpeakerVolume() has not been called.
"Level" indicates the real-time volume, and "Volume" is the software volume for the speaker. The ultimate volume equals to Level*Volume%. For example, if the value for "Level" is 100 and the one for "Volume" is 60, the ultimate volume will be "60".

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

## Accompaniment APIs for Voice Chat
| API | Description |
| ------------- |:-------------:|
|StartAccompany    				       |Starts playing back the accompaniment |
|StopAccompany    				   	|Stops playing back the accompaniment |
|IsAccompanyPlayEnd				|Indicates whether the accompaniment is over |
|PauseAccompany    					|Pauses playing back the accompaniment |
|ResumeAccompany					|Resumes playing back the accompaniment |
|SetAccompanyVolume 				|Sets the accompaniment volume |
|GetAccompanyVolume				|Obtains the accompaniment volume |
|SetAccompanyFileCurrentPlayedTimeByMs 				|Sets the playback progress |

### Start playing back the accompaniment
This API is called to play back the accompaniment. Supported formats are M4A, WAV, and MP3. Volume will be reset after being called.

#### Function prototype  
```
ITMGAudioEffectCtrl virtual void StartAccompany(const char* filePath, bool loopBack, int loopCount, int msTime) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| filePath    	|char* 	|Path of the accompaniment file						|
| loopBack  	|bool	|Indicates whether to send a mix. This is generally set to true, so that other users can also hear the accompaniment.	|
| loopCount	|int 	|Number of loops to be played. Value -1 means an infinite loop.				|
| msTime	|int   	| Delay time						|

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StartAccompany(filePath,true,-1,0);
```

### Callback for accompaniment playback
After the accompaniment is over, the event message ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH is returned, the action of this event should be implemented in OnEvent function.
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
| duckerTime	|int             | Fading out time |

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

### Resume playing back the accompaniment
This API is used to resume playing back the accompaniment.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int ResumeAccompany()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAccompany();
```

### Set whether you can hear the accompaniment
This API is used to set whether you can hear the accompaniment.
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

### Set whether others can also hear the accompaniment
This API is used to set whether others can also hear the accompaniment.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int EnableAccompanyLoopBack(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|--------------|
| enable    |bool | Indicates whether others can also hear the accompaniment |

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyLoopBack(false);
```

### Set the accompaniment volume
This API is used to set the accompaniment volume. Value range: 0-200. Default is 100. A value greater than 100 means volume up, otherwise volume down.
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
This API is used to get the accompaniment volume.
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



## Voice Effect APIs for Voice Chat

| API | Description |
| ------------- |:-------------:|
|PlayEffect    		|Plays the sound effect |
|PauseEffect    	|Pauses the sound effect |
|PauseAllEffects	|Pauses all the sound effects |
|ResumeEffect    	|Rsumes the sound effect |
|ResumeAllEffects	|Rsumes all the sound effects |
|StopEffect 		|Stops the sound effect |
|StopAllEffects		|Stops all the sound effects |
|SetVoiceType 		|Voice changing effects |
|SetKaraokeType     |Sets kalaok effects|
|GetEffectsVolume	|Obtains the volume of sound effects |
|SetEffectsVolume 	|Sets the volume of sound effects |


### Play the sound effect
This API is used to play sound effects. The sound effect ID in the parameter needs to be managed by the App side, uniquely identifying a separate file.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int PlayEffect(int soundId,  const char* filePath, bool loop, double pitch, double pan, double gain)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId  	|int        	|Indicates the sound effect ID |
| filePath    	|char*     	|Indicates the sound effect file path |
| loop    		|bool  	|Indicates whether to repeat playback |
| pitch    	|double	|Indicates the playback frequency, and the default is 1.0. The smaller the value is, the slower the playback speed and the longer the time will be.|
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

### Pause all the sound effects
This API is used to pause all the sound effects.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int PauseAllEffects()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseAllEffects();
```

### Resume the sound effect
This API is used to resume playing back the sound effect.
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

### Resume all the sound effects
This API is used to resume all the sound effects.
#### Function prototype  
```
ITMGAudioEffectCtrl virtual int ResumeAllEffects()
```
#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAllEffects();
```

### Stop the sound effect
This API is used to stop playing back the sound effect.
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

### Stop all the sound effects
This API is used to stop all the sound effects.
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
| type    |int | Indicates the voice font |


| Type | Parameter | Description |
| ------------- |-------------|------------- |
|ITMG_VOICE_TYPE_ORIGINAL_SOUND  		|0	|original sound			|
|ITMG_VOICE_TYPE_LOLITA    				|1	|lolita			|
|ITMG_VOICE_TYPE_UNCLE  				|2	|uncle			|
|ITMG_VOICE_TYPE_INTANGIBLE    			|3	|intangible			|
| ITMG_VOICE_TYPE_DEAD_FATBOY  			|4	|dead fatboy			|
| ITMG_VOICE_TYPE_HEAVY_MENTA			|5	|heavy mental			|
| ITMG_VOICE_TYPE_DIALECT 				|6	|dialect			|
| ITMG_VOICE_TYPE_INFLUENZA 				|7	|influenza			|
| ITMG_VOICE_TYPE_CAGED_ANIMAL 			|8	|caged animal			|
| ITMG_VOICE_TYPE_HEAVY_MACHINE		|9	|heavy machine			|
| ITMG_VOICE_TYPE_STRONG_CURRENT		|10	|strong current			|
| ITMG_VOICE_TYPE_KINDER_GARTEN			|11	|kinder garten			|
| ITMG_VOICE_TYPE_HUANG 					|12	|huang			|

#### Sample code  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->setVoiceType(0);
```

### Set Kalaok effect
This API is called to set the Kalaok effect
#### Function prototype   
```
TMGAudioEffectCtrl int SetKaraokeType(int type)
```
|Parameter     | Type         |Description|
| ------------- |:-------------:|-------------|
| type    |int                    |the Kalaok effect type|


|Type     | Parameter | Description |
| ------------- |-------------|------------- |
|ITMG_KARAOKE_TYPE_ORIGINAL 		|0	|Original			|
|ITMG_KARAOKE_TYPE_POP 				|1	|Pop			|
|ITMG_KARAOKE_TYPE_ROCK 			|2	|Rock			|
|ITMG_KARAOKE_TYPE_RB 				|3	|Hip-pop			|
|ITMG_KARAOKE_TYPE_DANCE 			|4	|Dance			|
|ITMG_KARAOKE_TYPE_HEAVEN 			|5	|Heaven			|
|ITMG_KARAOKE_TYPE_TTS 				|6	|TTS		|

#### Sample code   
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetKaraokeType(0);
```

### Obtain the volume of sound effects
This API is used to obtain the volume (linear volume) of the sound effects. A value greater than 100 means volume up, otherwise volume down.
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
## Offline Voice
| API | Description |
| ------------- |:-------------:|
|ApplyPTTAuthbuffer    		| authentication |
|SetMaxMessageLength    |Specifies the maximum length of a voice message |
|StartRecording		|Starts recording |
|StartRecordingWithStreamingRecognition		| Starts streaming speech recognition		|
|StopRecording    	|Stops recording |
|CancelRecording	|Cancels recording |
|UploadRecordedFile 	|Uploads voice files |
|DownloadRecordedFile	|Downloads voice files |
|PlayRecordedFile 	|Plays recorded voice files |
|StopPlayFile		|Stops playing voice files |
|GetFileSize 		|Obtains the size of a voice file |
|GetVoiceFileDuration	|Obtains the duration of a voice file |
|SpeechToText 		|Converts the voice file into text with Speech Recognition |

### Authentication
Do the authentication after the SDK is initialized. Please refer to the previous section on how to generate authBuffer. 
#### Function prototype    
```
ITMGPTT virtual void ApplyPTTAuthbuffer(const char* authBuffer, int authBufferLen)
```
|Parameter     | Type         |Description|
| ------------- |:-------------:|-------------|
| authBuffer    |char*                    |Authentication data|
| authBufferLen    |int                |Length of Authentication data|

#### Sample code   
```
ITMGContextGetInstance()->GetPTT()->ApplyPTTAuthbuffer(authBuffer,authBufferLen);
```

### Specify the maximum length of a voice message
This API is used to specify the maximum length of a voice message,  the maximum duration of which is limited to 60 seconds.
#### Function prototype  
```
ITMGPTT virtual void SetMaxMessageLength(int msTime)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| msTime    |int | Indicates the length of a voice message in millisecond|

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
ITMGContextGetInstance()->GetPTT()->StartRecording(fileDir);
```

### Callback for starting recordings
The callback function OnEvent is called after the recording is started. The event message ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE is returned, the action of this event should be implemeted in OnEvent function.

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

### Enable streaming speech recognition
This API is used to start streaming speech recognition. Texts obtained from voice-to-text conversion will be returned in real time in its callback. The recognition only supports Chinese and English.

#### Function prototype 
```
ITMGPTT virtual int StartRecordingWithStreamingRecognition(const char* filePath,const char* language) 
```
|Parameter     | Type         |Description|
| ------------- |:-------------:|-------------|
| filePath    	|char*	|Indicates the path for storing the voice file	|
| language 	|char*	|Language code, refer to [language reference list](https://github.com/TencentMediaLab/GME/blob/master/GME%20Developer%20Manual/GME%20SpeechToText.md)|

#### Sample code 
```
ITMGContextGetInstance()->GetPTT()->StartRecordingWithStreamingRecognition(filePath,"cmn-Hans-CN");
```

### Callback for streaming speech recognition
The callback function OnEvent is called after the recognition is finished. The event message ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE is returned, the action of this event should be implemented in the OnEvent function.

|Message Name     | Description         |
| ------------- |:-------------:|
| result    	|Error code indicating whether streaming speech recognition is successful			|
| text    		|text obtained from voice-to-text conversion	|
| file_path 	|local path for the recorded voice file		|
| file_id 		|URL for the recorded voice file uploaded to server	|

|Error Code     | Description         |Recommended Action|
| ------------- |:-------------:|:-------------:|
|32775	|Recording is successful but streaming voice to text is failed	|Call the API UploadRecordedFile to upload the recording, and then call the API SpeechToText to perform voice-to-text conversion.
|32777	|Recording and uploading is successful, but streaming voice to text is failed.	|The message returned includes a URL for successful upload. Call the SpeechToText API to perform voice-to-text conversion.

#### Sample code
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE:
		{
		break;
		}
	}
}

```

### Stop recording
This API is used to stop recording. There will be a callback after the recording is stopped.
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
| filePath    |char* | Indicates the path of the voice files to be uploaded |

#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->UploadRecordedFile(filePath);
```

### Callback for uploading voice files
After the voice file is uploaded, the event message ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE is returned, the action of this event should be implemented in the OnEvent function.
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
ITMGPTT virtual void DownloadRecordedFile(const char* fileId,const char* filePath)
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
After the voice file is downloaded, the event message ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE is returned, the action of this event should be implemented in the OnEvent function.
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
| filePath    |char* | Indicates the path of the file to be played|

#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->PlayRecordedFile(filePath);
```

### Callback for playing voice files
After the voice file is played back, the event message ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE is returned, the action of this event should be implemented in the OnEvent function.
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
This API is used to obtain the duration of a voice file (in milliseconds).
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
ITMGPTT virtual void SpeechToText(const char* fileID, const char* language)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileID    |char* | Indicates the URL to a voice file |
| language    |char*                     |Language code, refer to [language reference list](https://github.com/TencentMediaLab/GME/blob/master/GME%20Developer%20Manual/GME%20SpeechToText.md)|

#### Sample code  
```
ITMGContextGetInstance()->GetPTT()->SpeechToText((filePath,"cmn-Hans-CN");
```

### Callback for Speech Recognition
After the specified voice file is converted into text with Speech Recognition, the event message ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE is returned, the action of this event should be implemented in the OnEvent function.
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

### Set the print log level
This API is used to set the print log level.
#### Function prototype
```
ITMGContext virtual void SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| logLevel    		|int | Indicates the print log level |
| enableWrite    	| bool | Indicates whether to write a file. The default is Yes |
| enablePrint    	|bool | Indicates whether to write a console. The default is Yes |


|ITMG_LOG_LEVEL|Description |
| -------------------------------|:-------------:|
|TMG_LOG_LEVEL_NONE=0		|Do not print logs |
|TMG_LOG_LEVEL_ERROR=1		|Prints error logs (default) |
|TMG_LOG_LEVEL_INFO=2			|Prints prompt logs |
|TMG_LOG_LEVEL_DEBUG=3		|Prints development and debugging logs |
|TMG_LOG_LEVEL_VERBOSE=4		| Prints verbose logs |

#### Sample code  
```
ITMGContext* context = ITMGContextGetInstance();
context->SetLogLevel(0,true,true);
```

### Set the print log path
This API is used to set the print log path.
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
This API is used to add an ID to the audio data blacklist. A return value of 0 indicates that the call is failed.
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

| Message | Description of message |   
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

#### Data list

| Message | Data         | Example |
| ------------- |:-------------:|------------- |
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		|result; error_info			|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		|result; error_info  			|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    	|result; error_info  			|{"error_info":"waiting timeout, please check your network","result":0}|
| ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE    	|result; error_info; new_room_type	|{"error_info":"","new_room_type":0,"result":0}|
| ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE	|result; error_info  			|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"speaker (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":false,"result":0}|
| ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE    	|result; error_info  			|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"speaker (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":false,"result":0}|
| ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    	|result; error_info  			|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"microphone (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":true,"result":0}|
| ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    	|result; error_info 			|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"microphone (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":true,"result":0}|
| ITMG_MAIN_EVNET_TYPE_USER_UPDATE    		|user_list;  event_id			|{"event_id":1,"user_list":["0"]}|
| ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE 	|result; file_path  			|{"filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE 	|result; file_path;file_id  		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE	|result; file_path;file_id  		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE 	|result; file_path  			|{"filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE	|result; file_path;file_id		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE	|result; text; file_path;file_id		|{"file_id":"","filepath":","text":"","result":0}|

