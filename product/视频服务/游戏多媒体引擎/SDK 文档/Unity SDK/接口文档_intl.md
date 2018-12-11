## Overview

Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. This document provides a detailed description that makes it easy for Unity developers to debug and integrate the APIs of GME.

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
|Uninit    	|Initializes GME 	|

### Obtain the instance
Obtain the Context instance using ITMGContext instead of QAVContext.GetInstance().

### Initialize the SDK

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
int ret = IQAVContext.GetInstance().Init(str_appId, str_userId);
	if (ret != QAVError.OK) {
		return;
	}
```

### Trigger event callback
This API is used to trigger the event callback via periodic Poll call in update.
#### Function prototype

```
ITMGContext public abstract int Poll();
```
### Pause the system

This API is used to notify the engine for Pause when the system Pause occurs.
#### Function prototype

```
ITMGContext public abstract int Pause()
```

### Resume the system
This API is used to notify the engine for Resume when the system Resume occurs.
#### Function prototype

```
ITMGContext  public abstract int Resume()
```






### Deinitialize the SDK
This API is used to deinitialize SDK to make it uninitialized.

#### Function prototype 
```
ITMGContext public abstract int Uninit()
```





## Voice Chat Room-Related APIs
After the initialization, API for entering a room should be called before Voice Chat can start.

| API | Description |
| ------------- |:-------------:|
|GenAuthBuffer    	|Generates authentication data |
|EnterRoom   		| Enters a room |
|IsRoomEntered   	|Indicates whether the room is entered successfully |
|ExitRoom 		|Exits the room |
|ChangeRoomType 	| Modifies the audio type of the user's room |
|GetRoomType 		| Obtains the audio type of the user's room |


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

### Join a room
This API is used to enter a room with the generated authentication data, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback. Microphone and speaker are not enabled by default after a user enters the room.
For entering a common voice chat room that does not involve team voice chat, use the common API for entering a room. For more information, please see the [GME team voice chat documentation](https://intl.cloud.tencent.com/document/product/607/17972).

#### Function prototype

```
ITMGContext EnterRoom(string roomId, int roomType, byte[] authBuffer)
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
IQAVContext.GetInstance().EnterRoom(roomId, ITMG_ROOM_TYPE_FLUENCY, authBuffer);
```

### Callback for entering a room
The delegate function is used for callback after a user enters a room. The passed parameter includes result and error_info.
#### Function prototype
```
Delegate function:
public delegate void QAVEnterRoomComplete(int result, string error_info);
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

### Identify whether the room is entered successfully
This API is called to identify whether the room is entered successfully. A bool value is returned.
#### Function prototype  
```
ITMGContext abstract bool IsRoomEntered()
```
#### Sample code  
```
IQAVContext.GetInstance().IsRoomEntered();
```

### Exit a room
This API is called to exit the current room.
#### Function prototype  
```
ITMGContext ExitRoom()
```
#### Sample code  
```
IQAVContext.GetInstance().ExitRoom();
```

### Callback for exiting a room
Callback is executed after a user exits the room, and the delegate function is used to pass the message.
#### Function prototype  
```
Delegate function:
public delegate void QAVExitRoomComplete();
Event function:
public abstract event QAVExitRoomComplete OnExitRoomCompleteEvent; 
```
#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().OnExitRoomCompleteEvent += new QAVExitRoomComplete(OnExitRoomComplete);
Process the event after listening:
void OnExitRoomComplete(){
    //Send a callback after a user exits the room
}
```

### Obtain the audio type of the user's room
This API is used to obtain the audio type of the user's room. The returned value is the audio type of the room. Returned value of 0 means error happens. The audio type definition can be found in the API EnterRoom.

#### Function prototype  
```
ITMGContext ITMGRoom public  int GetRoomType()
```

#### Sample code  
```
IQAVContext.GetInstance().GetRoom().GetRoomType();
```

### Modify the audio type of the user's room
This API is used to modify the audio type of the user's room.
#### Function prototype  
```
ITMGContext ITMGRoom public void ChangeRoomType(ITMGRoomType roomtype)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomtype | ITMGRoomType | The room type to be switched to. See the API EnterRoom for the audio type definition. |

#### Sample code  
```
IQAVContext.GetInstance().GetRoom().ChangeRoomType(ITMG_ROOM_TYPE_FLUENCY);
```


### Callback for changing the audio type of the user's room
Callback is executed after a user changes the audio type, and the delegate function is used to pass the message.

| Returned Parameter | Description |
| ------------- |:-------------:|
| result | Value 0 represents success |
| error_info | In case of failure, an error message will be passed |

```
Delegate function:
public delegate void QAVOnChangeRoomtypeCallback(int result, string error_info);

Event function:
public abstract event QAVCallback OnChangeRoomtypeCallback; 
```
#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().OnChangeRoomtypeCallback += new QAVOnChangeRoomtypeCallback(OnChangeRoomtypeCallback);
Process the event after listening:
void OnChangeRoomtypeCallback(){
    //Send a callback after the room type has been set
}
```

### Notification of room type change
This API is used to allow you or other users in a room to modify the room type. This callback function is called whenever the room type changes, which is used to notify the App layer of such change. The room type definition can be found in the API EnterRoom.
```
Delegate function:
public delegate void QAVOnRoomTypeChangedEvent(int roomtype);

Event function:
public abstract event QAVOnRoomTypeChangedEvent OnRoomTypeChangedEvent;	
```
#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().OnRoomTypeChangedEvent += new QAVOnRoomTypeChangedEvent(OnRoomTypeChangedEvent);
Process the event after listening:
void OnRoomTypeChangedEvent(){
    //Send a callback after the room type has been changed
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
Delegate function:
public delegate void QAVEndpointsUpdateInfo(int eventID, int count, [MarshalAs(UnmanagedType.LPArray, SizeParamIndex = 1)]string[] openIdList);
Event function:
public abstract event QAVEndpointsUpdateInfo OnEndpointsUpdateInfoEvent;

Listen for an event:
IQAVContext.GetInstance().OnEndpointsUpdateInfoEvent += new QAVEndpointsUpdateInfo(OnEndpointsUpdateInfo);
Process the event after listening:
void OnEndpointsUpdateInfo(int eventID, int count, string[] openIdList)
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
			    //A member sends audio packets
			    break;
		    case ITMG_EVENT_ID_USER_NO_AUDIO:
			    //A member stops sending audio packets
			    break;
		  
		    default:
			    break;
 		    }
		break;
}

```


### Quality monitoring events
The message for quality monitoring event is ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_QUALITY. The returned parameters include weight, floss, and delay, which represent the following information and the action of this event should be implemented in the OnEvent function.

| Parameter | Description |
| ------------- |-------------|
|weight    				| Its value ranges from 1 to 50. The value of 50 indicates excellent quality of audio packets, and the value of 1 indicates poor quality of audio packets, which can barely be used; and "0" represents an initial value and is meaningless. |
|floss    				| Packet loss |
|delay    		| Voice chat delay (ms) |


## Audio APIs for Voice Chat
The audio APIs for Voice Chat can only be called after the SDK is initialized and the room is entered successfully.
Call scenario examples:

When a user click the UI button to enable or disable the microphone or speaker:
- For most game Apps, it's recommended to call EnableMic and EnableSpeaker APIs. Because calling EnableMic is equivalent to calling EnableAudioCaptureDevice and EnableAudioSend at the same time, and calling EnableSpeaker is equivalent to calling EnableAudioPlayDevice and EnableAudioRecv at the same time.

- For other mobile Apps (such as social networking Apps), enabling/disabling a capturing device will restart both the capturing and the playback devices. If the App is playing background music, it will also be interrupted. But if the microphone is enabled/disabled through control of upstream/downstream, playback will not be interrupted . So the calling method is: Call EnableAudioCaptureDevice(true) and EnableAudioPlayDevice(true) once after entering the room, and call EnableAudioSend/Recv to send/receive audio streams when the microphone button is clicked to enable or disable.

If you do not need to enable both the microphone and the speaker (releasing the recording permission to other modules), it is recommended to call PauseAudio/ResumeAudio.

| API | Description |
| ------------- |:-------------:|
|PauseAudio    				       	   |Pauses audio engine		 |
|ResumeAudio    				      	 | Resumes audio engine		 |
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
ITMGAudioCtrl abstract int PauseAudio()
```
#### Sample code  
```
IQAVContext.GetInstance ().GetAudioCtrl ().PauseAudio();
```

### Resume the capture and playback features of the audio engine
This API is called to resume the capture and playback features of the audio engine, and only works when room is entered successfully.

#### Function prototype  
```
ITMGAudioCtrl abstract int ResumeAudio()
```
#### Sample code  
```
IQAVContext.GetInstance ().GetAudioCtrl ().ResumeAudio();
```

### Enable/disable the microphone
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

### Obtain the microphone status
This API is used to obtain the microphone status. "0" means microphone is enabled, "1" means microphone is disabled, "2" means microphone is under working.
#### Function prototype  
```
ITMGAudioCtrl GetMicState()
```
#### Sample code  
```
micToggle.isOn = IQAVContext.GetInstance().GetAudioCtrl().GetMicState();
```

### Enable/disable audio capture device
This API is used to enable/disable the audio capture device. The audio capture device is not enabled by default. 
- API can only be called after the room is entered.The device will disabled automatically after exiting the room.
- For mobile use case, permission is normally asked when enabling the capture device.

#### Function prototype  
```
ITMGAudioCtrl int EnableAudioPlayDevice(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled | bool | true means enable，false means disable |

#### Sample code 

```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioCaptureDevice(true);
```

### Obtain the audio capture device status
This API is used to obtain the audio capture device status.
#### Function prototype

```
ITMGAudioCtrl bool IsAudioCaptureDeviceEnabled()
```
#### Sample code 

```
bool IsAudioCaptureDevice = IQAVContext.GetInstance().GetAudioCtrl().IsAudioCaptureDeviceEnabled();
```

### Enable/disable the audio sending

This API is used to enable/disable the audio sending. Enable means sending the captured voice. 

#### Function prototype

```
ITMGAudioCtrl int EnableAudioSend(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled | bool |true means enable audio sending，false means not|

#### Sample code  

```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioSend(true);
```

### Obtain status on if captured audio is being sent 
This API is called to obtain the status if captured audio is being sent.
#### Function prototype
```
ITMGAudioCtrl bool IsAudioSendEnabled()
```
#### Sample code  
```
bool IsAudioSend = IQAVContext.GetInstance().GetAudioCtrl().IsAudioSendEnabled();
```

### Obtain real-time microphone volume
This API is used to obtain real time microphone volume. An int value is returned.
#### Function prototype  
```
ITMGAudioCtrl -(int)GetMicLevel
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioCtrl().GetMicLevel();
```

### Set software volume for the microphone
This API is used to set software volume for the microphone. The value "0" means Mute, and "100" means the volume remains unchanged. Default value is 100.
#### Function prototype  
```
ITMGAudioCtrl SetMicVolume(int volume)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| volume | int | Sets the volume, value range: 0 to 200 |

#### Sample code  

```
int micVol = (int)(value * 100);
IQAVContext.GetInstance().GetAudioCtrl().SetMicVolume (micVol);
```

### Obtain software volume for the microphone
This API is used to obtain the software volume for the microphone. An int value is returned to indicate the software volume for the microphone. Returned value of 101 means SetMicVolume() has not been called.
#### Function prototype  
```
ITMGAudioCtrl GetMicVolume()
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioCtrl().GetMicVolume();
```

### Enable/disable the speaker
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


### Obtain the speaker status
This API is used to obtain the speaker status. "0" means speaker is enabled, "1" means speaker is disabled, "2" means speaker is under working.
#### Function prototype  
```
ITMGAudioCtrl GetSpeakerState()
```

#### Sample code  
```
speakerToggle.isOn = IQAVContext.GetInstance().GetAudioCtrl().GetSpeakerState();
```

### Enable/disable audio playback device
This API is used to enable/disable audio playback device.

#### Function prototype
```
ITMGAudioCtrl EnableAudioPlayDevice(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled | bool | true means enable, false means disable |

#### Sample code

```
Enable a playback device
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioPlayDevice(true);
```

### Obtain audio playback device status
This API is used to obtain the status of audio playback device.
#### Function prototype

```
ITMGAudioCtrl bool IsAudioPlayDeviceEnabled()
```
#### Sample code

```
bool IsAudioPlayDevice = IQAVContext.GetInstance().GetAudioCtrl().IsAudioPlayDeviceEnabled();
```

### Enable/disable the audio receiving
This API is used to enable/disable the audio receving. Enable means playing the received voice. 

#### Function prototype

```
ITMGAudioCtrl int EnableAudioRecv(bool isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled | bool | true means enabling the audio receing. false means not |

#### Sample code  

```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioRecv(true);
```


### Obtain status on if received audio is being played 
This API is called to obtain the status if received audio is being played.
#### Function prototype
```
ITMGAudioCtrl bool IsAudioRecvEnabled()
```
#### Sample code  
```
bool IsAudioRecv = IQAVContext.GetInstance().GetAudioCtrl().IsAudioRecvEnabled();
```

### Obtain real-time speaker volume
This API is used to obtain real time speaker volume. An int value is returned to indicate the real-time speaker volume.
#### Function prototype  
```
ITMGAudioCtrl GetSpeakerLevel()
```

#### Sample code  
```
IQAVContext.GetInstance().GetAudioCtrl().GetSpeakerLevel();
```

### Set software volume for the speaker
This API is used to set the software volume for the speaker.
The value "0" means Mute, and "100" means the volume remains unchanged. Default value is 100.


#### Function prototype  
```
ITMGAudioCtrl SetSpeakerVolume(int volume)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| volume | int | Sets the volume. Value range: 0 to 200. |

#### Sample code

```
int speVol = (int)(value * 100);
IQAVContext.GetInstance().GetAudioCtrl().SetSpeakerVolume(speVol);
```

### Obtain software volume for the speaker
This API is used to obtain the software volume for the speaker. An int value is returned to indicate the software volume for the speaker. Returned value of 101 means SetSpeakerVolume() has not been called.
"Level" indicates the real-time volume, and "Volume" the is software volume for the speaker. The ultimate volume equals to Level*Volume%. For example, if the value for "Level" is 100 and the one for "Volume" is 60, the ultimate volume will be "60".

#### Function prototype  
```
ITMGAudioCtrl GetSpeakerVolume()
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioCtrl().GetSpeakerVolume();
```


### Enable in-ear monitoring
This API is used to enable in-ear monitoring.
#### Function prototype  

```
ITMGContext GetAudioCtrl EnableLoopBack(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| enable    |bool         | Specifies whether to enable in-ear monitoring |

#### Sample code  

```
IQAVContext.GetInstance().GetAudioCtrl().EnableLoopBack(true);
```

### Callback for device occupation and release
Callback is executed after a device is occupied or released, and the delegate function is used to pass the message.

```
Delegate function:
public delegate void QAVOnDeviceStateChangedEvent(int deviceType, string deviceId, bool openOrClose);
Event function:
public abstract event QAVOnDeviceStateChangedEvent OnDeviceStateChangedEvent;
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| deviceType | int |1 indicates a capturing device. 2 indicates a playback device |
| deviceId | string | Device GUID, which is used to mark a device and only valid on Windows and Mac. |
| openOrClose | bool | Occupies or releases a capturing/playback device |


| Parameter | Value | Description |
| ------------- |:-------------:|-------------|
| AUDIODEVICE_CAPTURE | 1 | Indicates a capturing device |
| AUDIODEVICE_PLAYER | 2 | Indicates a playback device |

#### Sample code  

```
Listen for an event:
ITMGContext.GetInstance().GetAudioCtrl().OnDeviceStateChangedEvent += new QAVAudioDeviceStateCallback(OnAudioDeviceStateChange);
Process the event after listening:
void QAVAudioDeviceStateCallback(){
    //Callback for device occupation and release
}
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
IQAVAudioEffectCtrl int StartAccompany(string filePath, bool loopBack, int loopCount, int duckerTimeMs)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath | string  |Path of the accompaniment file	|
| loopBack | bool | Indicates whether to send a mix. This is generally set to true, so that other users can also hear the accompaniment. |
| loopCount | int | Number of loops to be played. Value -1 means an infinite loop.	 |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StartAccompany(filePath,true,loopCount,duckerTimeMs);
```

### Callback for accompaniment playback
Callback is executed after an accompaniment has been played, and the delegate function is used to pass the message.
#### Function prototype  
```
Delegate function:
public delegate void QAVAccompanyFileCompleteHandler(int code, string filepath);
Event function:
public abstract event QAVAccompanyFileCompleteHandler OnAccompanyFileCompleteHandler;
```
#### Sample code
```
Listen for an event:
IQAVContext.GetInstance().GetAudioEffectCtrl().OnAccompanyFileCompleteHandler += new QAVAccompanyFileCompleteHandler(OnAccomponyFileCompleteHandler);
Process the event after listening:
void OnAccomponyFileCompleteHandler(int code, string filepath){
    //Callback for accompaniment playback
}
```

### Stop playing back the accompaniment
This API is used to stop playing back the accompaniment.
#### Function prototype  
```
IQAVAudioEffectCtrl int StopAccompany(int duckerTimeMs)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| duckerTimeMs | int | Fading out time |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StopAccompany(duckerTimeMs);
```

### Indicate whether the accompaniment is over
If it is over, "true" is returned. If it is not, "false" is returned.
#### Function prototype  
```
IQAAudioEffectCtrl bool IsAccompanyPlayEnd();
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().IsAccompanyPlayEnd();
```

### Pause playing back the accompaniment
This API is used to pause playing back the accompaniment.
#### Function prototype  
```
IQAAudioEffectCtrl int PauseAccompany()
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PauseAccompany();
```

### Resume playing back the accompaniment
This API is used to resume playing back the accompaniment.
#### Function prototype  
```
IQAAudioEffectCtrl int ResumeAccompany()
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().ResumeAccompany();
```

### Set whether you can hear the accompaniment
This API is used to set whether you can hear the accompaniment.
#### Function prototype  
```
IQAAudioEffectCtrl int EnableAccompanyPlay(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|--------------|
| enable    |bool | Indicates whether you can hear the accompaniment |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().EnableAccompanyPlay(true);
```

### Set whether others can also hear the accompaniment
This API is used to set whether others can also hear the accompaniment.
#### Function prototype  
```
IQAAudioEffectCtrl int EnableAccompanyLoopBack(bool enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|--------------|
| enable    |bool | Indicates whether others can also hear the accompaniment |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().EnableAccompanyLoopBack(true);
```

### Set the accompaniment volume
This API is used to set the accompaniment volume. Value range: 0-200. Default is 100. A value greater than 100 means volume up, otherwise volume down.
#### Function prototype  
```
IQAAudioEffectCtrl int SetAccompanyVolume(int vol)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| vol    |int | Indicates the volume value |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().SetAccompanyVolume(vol);
```

### Obtain the volume of the accompaniment
This API is used to get the accompaniment volume.
#### Function prototype  
```
IQAAudioEffectCtrl abstract int GetAccompanyVolume()
```
#### Sample code  
```
string currentVol = "VOL: " + IQAVContext.GetInstance().GetAudioEffectCtrl().GetAccompanyVolume();
```

### Obtain the accompaniment playback progress
The following two APIs are used to obtain the accompaniment playback progress. Note: Current/Total = current loop times, Current % Total = current loop playback position.
#### Function prototype  
```
IQAAudioEffectCtrl abstract uint GetAccompanyFileTotalTimeByMs()
IQAAudioEffectCtrl abstract int GetAccompanyFileCurrentPlayedTimeByMs()
```
#### Sample code  
```
Sstring current = "Current: " + IQAVContext.GetInstance().GetAudioEffectCtrl().GetAccompanyFileCurrentPlayedTimeByMs() + " ms";
string total = "Total: " + IQAVContext.GetInstance().GetAudioEffectCtrl().GetAccompanyFileTotalTimeByMs() + " ms";
```


### Set the playback progress
This API is used to set the playback progress.
#### Function prototype  
```
IQAAudioEffectCtrl abstract uint SetAccompanyFileCurrentPlayedTimeByMs(uint time)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| time | uint | Indicates the playback progress in milliseconds |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().SetAccompanyFileCurrentPlayedTimeByMs(time);
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
IQAAudioEffectCtrl int PlayEffect(int soundId, string filePath, bool loop = false, double pitch = 1.0f, double pan = 0.0f, double gain = 1.0f)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId  	|int        	|Indicates the sound effect ID |
| filePath    	|string     	|Indicates the sound effect file path |
| loop    		|bool  	|Indicates whether to repeat playback |
| pitch    	|double	|Indicates the playback frequency, and the default is 1.0. The smaller the value is, the slower the playback speed and the longer the time will be.|
| pan    		|double	|Indicates the channel, value range: -1.0 to 1.0. -1.0 means only the left channel is turned on. |
| gain    		|double	|Indicates the gain volume, ranging from 0.0 to 1.0. The default is 1.0 |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PlayEffect(soundId,filePath,true,1.0,0,1.0);
```

### Pause the sound effect
This API is used to pause playing back the sound effect.
#### Function prototype  
```
IQAAudioEffectCtrl int PauseEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId | int | Indicates the sound effect ID |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PauseEffect(soundId);
```

### Pause all the sound effects
This API is used to pause all the sound effects.
#### Function prototype  
```
IQAAudioEffectCtrl int PauseAllEffects()
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PauseAllEffects();
```

### Resume the sound effect
This API is used to resume playing back the sound effect.
#### Function prototype  
```
IQAAudioEffectCtrl int ResumeEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int | Indicates the sound effect ID |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().ResumeEffect(soundId);
```

### Resume all the sound effects
This API is used to sesume all sound effects.
#### Function prototype  
```
IQAAudioEffectCtrl int ResumeAllEffects()
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().ResumeAllEffects();
```

### Stop the sound effect
This API is used to stop the sound effect.
#### Function prototype  
```
IQAAudioEffectCtrl int StopEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int | Indicates the sound effect ID |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StopEffect(soundId);
```

### Stop all the sound effects
This API is used to stop all the sound effects.
#### Function prototype  
```
IQAAudioEffectCtrl int StopAllEffects()
```


#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StopAllEffects(); 
```



### Voice changing effects
This API is used to set the voice changing effects.
#### Function prototype  
```
IQAAudioEffectCtrl int setVoiceType(int type)
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
IQAVContext.GetInstance().GetAudioEffectCtrl().setVoiceType(0);
```

### Set Kalaok effect
This API is called to set the Kalaok effect
#### Function prototype   
```
IQAAudioEffectCtrl int SetKaraokeType(int type)
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
IQAVContext.GetInstance().GetAudioEffectCtrl().SetKaraokeType(0);
```


### Obtain the volume of sound effects
This API is used to obtain the volume (linear volume) of the sound effects. A value greater than 100 means volume up, otherwise volume down.
#### Function prototype  
```
IQAAudioEffectCtrl  int GetEffectsVolume()
```
#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().GetEffectsVolume();
```


### Set the volume of sound effects
This API is used to set the volume of sound effects.
#### Function prototype  
```
IQAAudioEffectCtrl  int SetEffectsVolume(int volume)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| volume    |int | Indicates the volume value |

#### Sample code  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().SetEffectsVolume(volume);
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
ITMGPTT int ApplyPTTAuthbuffer (byte[] authBuffer)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| authBuffer	|byte[]	| Authentication data|

#### Sample code  
```
IQAVContext.GetInstance().GetPttCtrl().ApplyPTTAuthbuffer(authBuffer);
```

### Specify the maximum length of a voice message
This API is used to specify the maximum length of a voice message,  the maximum duration of which is limited to 60 seconds.
#### Function prototype  
```
ITMGPTT int SetMaxMessageLength(int msTime)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| msTime    |int | Indicates the length of a voice message in millisecond|

#### Sample code  
```
IQAVContext.GetInstance().GetPttCtrl().SetMaxMessageLength(60000); 
```


### Start recording
This API is used to start recording.
#### Function prototype  
```
ITMGPTT int StartRecording(string fileDir)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileDir | string | Indicates the path for storing the voice file |

#### Sample code  
```
string recordPath = Application.persistentDataPath + string.Format ("/{0}.silk", sUid++);
int ret = IQAVContext.GetInstance().GetPttCtrl().StartRecording(recordPath);
```

### Callback for starting recordings
Callback is executed after recording, and the delegate function is used to pass the message.
#### Function prototype  
```
Delegate function:
public delegate void QAVRecordFileCompleteCallback(int code, string filepath); 
Event function:
public abstract event QAVRecordFileCompleteCallback OnRecordFileComplete;
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| code | string | When code is 0, recording is completed |
| filepath | string | Path for storing the recorded file |

#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().GetPttCtrl().OnRecordFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath){
    //Callback for starting recordings
}
```

### Enable streaming speech recognition
This API is used to start streaming speech recognition. Texts obtained from voice-to-text conversion will be returned in real time in its callback. The recognition only supports Chinese and English.

#### Function prototype 
```
ITMGPTT int StartRecordingWithStreamingRecognition(string filePath, string language)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath | String | Indicates the path for storing the voice file |
| language | String | Language code, refer to [language reference list](https://github.com/TencentMediaLab/GME/blob/master/GME%20Developer%20Manual/GME%20SpeechToText.md) |

#### Sample code  
```
string recordPath = Application.persistentDataPath + string.Format("/{0}.silk", sUid++);
int ret = ITMGContext.GetInstance().GetPttCtrl().StartRecordingWithStreamingRecognition(recordPath, "cmn-Hans-CN");
```

### Callback for streaming speech recognition
Callback is executed after recognition is finished, and the delegate function is used to pass the message.
```
Delegate function:
public delegate void QAVStreamingRecognitionCallback(int code, string fileid, string filepath, string result);
Event function:
public abstract event QAVStreamingRecognitionCallback OnStreamingSpeechComplete;
```

|Message Name     | Description         |
| ------------- |:-------------:|
| result    	|Error code indicating whether streaming speech recoginition is successful			|
| text    		|text obtained from voice-to-text conversion	|
| file_path 	|local path for the recorded voice file		|
| file_id 		|URL for the recorded voice file uploaded to server	|

|Error Code     | Description         |Recommended Action|
| ------------- |:-------------:|:-------------:|
|32775	|Recording is successful but streaming voice to text is failed	|Call the API UploadRecordedFile to upload the recording, and then call the API SpeechToText to perform voice-to-text conversion.
|32777	|Recording and uploading is successful, but streaming voice to text is failed.	|The message returned includes a URL for successful upload. Call the SpeechToText API to perform voice-to-text conversion.

#### Sample code
```
Listen for an event:
IQAVContext.GetInstance().GetPttCtrl().OnStreamingSpeechComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string fileid, string filepath, string result){
    //Callback for starting streaming recordings
}

```
### Stop recording
This API is used to stop recording. There will be a callback after the recording is stopped.
#### Function prototype  
```
ITMGPTT int StopRecording()
```
#### Sample code  
```
IQAVContext.GetInstance().GetPttCtrl().StopRecording();
```

### Cancel recording
This API is used to cancel recording.
#### Function prototype  

```
IQAVPTT int CancelRecording()
```
#### Sample code  

```
IQAVContext.GetInstance().GetPttCtrl().CancelRecording();
```

### Upload voice files
This API is used to upload voice files.
#### Function prototype  

```
IQAVPTT int UploadRecordedFile (string filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath | string | Indicates the path of the voice files to be uploaded |

#### Sample code

```
IQAVContext.GetInstance().GetPttCtrl().UploadRecordedFile(filePath);
```


### Callback for uploading voice files
Callback is executed after a voice file has been uploaded, and the delegate function is used to pass the message.
#### Function prototype  
```
Delegate function:
public delegate void QAVUploadFileCompleteCallback(int code, string filepath, string fileid);
Event function:
public abstract event QAVUploadFileCompleteCallback OnUploadFileComplete; 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| code | int | When code is 0, recording is completed |
| filepath | string | Path for storing the recorded file |
| fileid | string | URL to the file |

#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().GetPttCtrl().OnUploadFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath, string fileid){
    //Callback for uploading voice files
}
```


### Download voice files
This API is used to download voice files.
#### Function prototype  

```
IQAVPTT DownloadRecordedFile (string fileID, string downloadFilePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileID | string | URL to a file |
| downloadFilePath | string | Local path for saving the file |

#### Sample code

```
IQAVContext.GetInstance().GetPttCtrl().DownloadRecordedFile(fileId, filePath);
```


### Callback for downloading voice files
Callback is executed after a voice file has been downloaded, and the delegate function is used to pass the message.
#### Function prototype  
```
Delegate function:
public delegate void QAVDownloadFileCompleteCallback(int code, string filepath, string fileid);
Event function:
public abstract event QAVDownloadFileCompleteCallback OnDownloadFileComplete;
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| code | int | When code is 0, recording is completed |
| filepath | string | Path for storing the recorded file |
| fileid | string | URL to the file |

#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().GetPttCtrl().OnDownloadFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath, string fileid){
    //Send a callback after a voice file has been downloaded
}
```



### Play voice files
This API is used to play voice files.
#### Function prototype  
```
IQAVPTT PlayRecordedFile (string downloadFilePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| downloadFilePath | string |Indicates the path of the file to be played|

#### Sample code  
```
IQAVContext.GetInstance().GetPttCtrl().PlayRecordedFile(filePath); 
```


### Callback for playing voice files
Callback is executed after a voice file has been played, and the delegate function is used to pass the message.
#### Function prototype  
```
Delegate function:
public delegate void QAVPlayFileCompleteCallback(int code, string filepath);
Event function:
public abstract event QAVPlayFileCompleteCallback OnPlayFileComplete;
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| code | int | When code is 0, recording is completed |
| filepath | string | Path for storing the recorded file |

#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().GetPttCtrl().OnPlayFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath){
    //Callback for playing a voice file
}
```




### Stop playing voice files
This API is used to stop playing back voice files.
#### Function prototype  
```
IQAVPTT int StopPlayFile()
```

#### Sample code  
```
IQAVContext.GetInstance().GetPttCtrl().StopPlayFile();
```



### Obtain the size of a voice file
This API is used to get the size of a voice file.
#### Function prototype  
```
IQAVPTT GetFileSize(string filePath) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath | string | Indicates the path to a voice file |

#### Sample code  
```
int fileSize = IQAVContext.GetInstance().GetPttCtrl().GetFileSize(filepath);
```

### Obtain the length of a voice file
This API is used to obtain the duration of a voice file (in milliseconds).
#### Function prototype  
```
IQAVPTT int GetVoiceFileDuration(string filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath | string |  Indicates the path to a voice file |

#### Sample code  
```
int fileDuration = IQAVContext.GetInstance().GetPttCtrl().GetVoiceFileDuration(filepath);
```



### Convert the specified voice file into text with Speech Recognition
This API is used to convert the specified voice file into text with Speech Recognition.
#### Function prototype  
```
IQAVPTT int SpeechToText(String fileID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileID | string | URL to the voice file |

#### Sample code  
```
IQAVContext.GetInstance().GetPttCtrl().SpeechToText(fileID);
```

### Convert the specified voice file into text with Speech Recognition(specify language
This API is used to convert the specified voice file into text with Speech Recognition.
#### Function prototype  
```
IQAVPTT int SpeechToText(String fileID,String language)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileID    |char* | Indicates the URL to a voice file |
| language    |char*                     |Language code, refer to [language reference list](https://github.com/TencentMediaLab/GME/blob/master/GME%20Developer%20Manual/GME%20SpeechToText.md)|

#### Sample code  
```
IQAVContext.GetInstance().GetPttCtrl().SpeechToText(fileID,"cmn-Hans-CN");
```

### Callback for Speech Recognition
This API is used to convert the specified voice file into text with Speech Recognition, and the delegate function is used to pass the message.
#### Function prototype  
```
Delegate function:
public delegate void QAVSpeechToTextCallback(int code, string fileid, string result);
Event function:
public abstract event QAVSpeechToTextCallback OnSpeechToTextComplete;
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| code | int | When code is 0, recording is completed |
| fileid | string | URL to the voice file |
| result | string | Result of text conversion |

#### Sample code  
```
Listen for an event:
IQAVContext.GetInstance().GetPttCtrl().OnSpeechToTextComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string fileid, string result){
    //Callback for Speech Recognition
}
```
## Advanced APIs
### Obtain the version number
This API is used to get the SDK version number for analysis.
#### Function prototype
```
ITMGContext  abstract string GetSDKVersion()
```
#### Sample code  
```
IQAVContext.GetInstance().GetSDKVersion();
```





### Set the print log level
This API is used to set the print log level.
#### Function prototype
```
ITMGContext  SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
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
IQAVContext.GetInstance().SetLogLevel(TMG_LOG_LEVEL_NONE,true,true);
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
ITMGContext  SetLogPath(string logDir)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| logDir | NSString | Path |

#### Sample code  
```
IQAVContext.GetInstance().SetLogPath(path);
```
### Obtain diagnostic messages
This API is used to obtain information about the quality of real-time audio/video calls. This API is mainly used to check the quality of real-time calls and troubleshoot problems, and can be ignored for this service.
#### Function prototype  
```
IQAVRoom GetQualityTips()
```
#### Sample code  
```
string tips = IQAVContext.GetInstance().GetRoom().GetQualityTips();
```

### Add an ID to the audio data blacklist
This API is used to add an ID to the audio data blacklist. A return value of 0 indicates that the call is failed.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl AddAudioBlackList(string openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| openId | NSString | ID that needs to be added to the blacklist |

#### Sample code  

```
IQAVContext.GetInstance().GetAudioCtrl ().AddAudioBlackList (id);
```

### Remove an ID from the audio data blacklist
This API is used to remove an ID from the audio data blacklist. A return value of 0 indicates that the call failed.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl RemoveAudioBlackList(string openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| openId | NSString | ID that needs to be removed from the blacklist |

#### Sample code  

```
IQAVContext.GetInstance().GetAudioCtrl ().RemoveAudioBlackList (id);
```


