## Overview
Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides a detailed description that makes it easy for Android developers to debug and integrate the APIs for Game Multimedia Engine.


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


**Notes**
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

### Register callback
With the API class, the Delegate method is used to send callback notifications to your application. Register the callback function to the SDK to receive callback messages.

#### Sample code 
```
private ITMGContext.ITMGDelegate itmgDelegate = null;
```
Override this callback function in the constructor to process callback parameters.

| Parameter | Type | Description |
| ------------- |:-------------:| ------------- |
| type    	|ITMGContext.ITMG_MAIN_EVENT_TYPE 	| Event type in the callback response |
| data    	| Intent message type | Callback message, i.e., the event data |



#### Sample code  
```
itmgDelegate= new ITMGContext.ITMGDelegate() {
            @Override
 			public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
                }
        };
```


Register the callback function to the SDK (before a user enters the room).
#### Function prototype 
```
ITMGContext public int SetTMGDelegate(ITMGDelegate delegate)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| delegate    |ITMGDelegate | SDK callback function |
#### Sample code  
```
TMGContext.GetInstance(this).SetTMGDelegate(itmgDelegate);
```



### Initialize the SDK
For more information on how to obtain parameters, see [GME Integration Guide](/document/product/607/10782).
This API should contain SdkAppId and openId. The SdkAppId is obtained from the Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.
#### Function prototype

```
ITMGContext public int Init(String sdkAppId, String openID)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId    	|String  |The SdkAppId obtained from the Tencent Cloud console |
| openID    		|String  |The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. 	|

#### Sample code 


```
ITMGContext.GetInstance(this).Init(sdkAppId, openID);
```
### Trigger event callback
This API is used to trigger the event callback via periodic Poll call in update.
#### Function prototype

```
ITMGContext int Poll()
```
#### Sample code
```
ITMGContext.GetInstance(this).Poll();
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
ITMGContext int Resume()
```



### Deinitialize the SDK
This API is used to deinitialize an SDK to make it uninitialized.
#### Function prototype

```
ITMGContext int Uninit()
```
#### Sample code
```
ITMGContext.GetInstance(this).Uninit();
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
AuthBuffer is generated for encryption and authentication of appropriate features. For more information on how to obtain relevant parameters, see [GME Key](/document/product/607/12218).    
A value of type Byte[] is returned by this API. When voice message is obtaining authentication, the parameter of room number must be set to 0.

A value of type Byte[] is returned by this API.
#### Function prototype
```
AuthBuffer public native byte[] genAuthBuffer(int sdkAppId, String roomId, String identifier, String key)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| appId    		|int   		|The SdkAppId obtained from the Tencent Cloud console |
| roomId    		|String   		|Room number supports Int32 type (which is passed after being converted to a string)  |
| openID    	|String 	|User ID					|
| key    		|string 	|The key obtained from the Tencent Cloud console			|


#### Sample code  
```
import com.tencent.av.sig.AuthBuffer;
byte[] authBuffer=AuthBuffer.getInstance().genAuthBuffer(Integer.parseInt(sdkAppId), strRoomID,identifier, key);
```



### Enter a room
This API is used to enter a room with the generated authentication information, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback. Microphone and speaker are not enabled by default after a user enters the room.


#### Function prototype
```
ITMGContext public abstract void  EnterRoom(string roomId, int roomType, byte[] authBuffer)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomId 	|String		|Room number supports Int32 type (which is passed after being converted to a string)|
| roomType 	|int		|Audio type of the room		|
| authBuffer	|byte[]	|Authentication key				|

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume | 16k (if there is no special requirement for sound quality) | With high fluency and ultra-low delay, it is suitable for team speak scenarios in such games as FPS and MOBA. |							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| 16k or 48k, depending on the requirement for sound quality	| With good sound quality and medium delay, it is suitable for voice chat scenarios in casual games such as Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|HD	|3|Speaker: media volume; headset: media volume	| 48k is recommended to ensure the best effect	| With ultra-high sound quality and high delay, it is suitable for music and voice social Apps, and scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirements for volume types or scenarios, contact the customer service.
- The sound effect in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.
#### Sample code  
```
ITMGContext.GetInstance(this).EnterRoom(roomId,roomType, authBuffer);    
```

### Callback for entering a room
This API is used to send the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message after a user enters a room, which is checked in the OnEvent function.

#### Sample code  
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ENTER_ROOM == type)
        {
           	 // Receive the event of entering the room successfully.
        }
	}

```


### Identify whether any member has entered a room
This API is called to identify whether any member has entered a room. A bool value is returned.
#### Function prototype  
```
ITMGContext public boolean IsRoomEntered()
```
#### Sample code  
```
ITMGContext.GetInstance(this).IsRoomEntered();
```

### Exit a room
This API is called to exit the current room. It is a synchronous interface which releases occupied device resources when returned.

#### Function prototype  
```
ITMGContext public void ExitRoom()
```
#### Sample code  
```
ITMGContext.GetInstance(this).ExitRoom();
```

### Callback for exiting a room
After a user exits the room, a callback response is returned and the ITMG_MAIN_EVENT_TYPE_EXIT_ROOM message is received.
#### Sample code  
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_EXIT_ROOM == type)
        {
            // Receive the event of exiting the room successfully.
        }
}
```

### Modify the audio type of the user's room
This API is used to modify the audio type of the user's room. See the callback event for the result. The event type is ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE.
#### Function prototype  
```
IITMGContext TMGRoom public void ChangeRoomType(int nRoomType)
```


| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| nRoomType    |int    |The room type to be switched to. See the API EnterRoom for the audio type of the user's room. |

#### Sample code  
```
ITMGContext.GetInstance(this).GetRoom().ChangeRoomType(nRoomType);
```


### Obtain the audio type of the user's room
This API is used to obtain the audio type of the user's room. The returned value is the audio type of the room. Value 0 means that an error occurred while obtaining the audio type of the user's room. See the API EnterRoom for the audio type of the user's room.

#### Function prototype  
```
IITMGContext TMGRoom public  int GetRoomType()
```

#### Sample code  
```
ITMGContext.GetInstance(this).GetRoom().GetRoomType();
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
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE == type)
        {
		//Send a callback after the room type has been changed
	 }
}
```

### Member status change
Notification about this event is sent only when the status changes. To obtain member status in real time, cache the notification when receiving it at a higher layer. The event message ITMG_MAIN_EVNET_TYPE_USER_UPDATE is returned. The parameter "intent" includes event_id and user_list. Identify the event message in the OnEvent function.
Audio events are subject to a threshold above which a notification is sent. The message "A member stops sending audio packages" is sent when audio packages are not received after 2 seconds.

|event_id     | Description | What Is Maintained at the App Side |
| ------------- |:-------------:|-------------|
|ITMG_EVENT_ID_USER_ENTER    				|A member enters the room			| Member list		|
|ITMG_EVENT_ID_USER_EXIT    				|A member exits the room			| Member list		|
|ITMG_EVENT_ID_USER_HAS_AUDIO    		|A member sends audio packages		| Chat member list	|
|ITMG_EVENT_ID_USER_NO_AUDIO    			|A member stops sending audio packages		| Chat member list	|

#### Sample code  
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_USER_UPDATE == type)
        {
		//Update member status
		int nEventID = data.getIntExtra("event_id", 0);
		String[] identifierList =data.getStringArrayExtra("user_list");
		 switch (nEventID)
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
|EnableMic    						|Enables/disables the microphone |
|GetMicState    						|Obtains the microphone status |
|EnableAudioCaptureDevice    		|Enables/disables a capturing device |
|IsAudioCaptureDeviceEnabled    	|Obtains the status of a capturing device |
|EnableAudioSend    				|Enables/disables audio upstream |
|IsAudioSendEnabled    				|Obtains the status of audio upstream |
|GetMicLevel    						|Obtains real-time microphone volume |
|SetMicVolume    					|Sets microphone volume |
|GetMicVolume    					|Obtains microphone volume |
|EnableSpeaker    					|Enables/disables the speaker |
|GetSpeakerState    					|Obtains the speaker status |
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
ITMGContext ITMGAudioCtrl public int PauseAudio()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().PauseAudio();
```

### Resume the capture and playback features of the audio engine
This API is called to resume the capture and playback features of the audio engine. It is a synchronous API and only works when members have entered the room.
#### Function prototype  
```
ITMGContext ITMGAudioCtrl public int ResumeAudio()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().ResumeAudio();
```

### Enable/disable the microphone
This API is used to enable/disable the microphone. Microphone and speaker are not enabled by default after a user enters a room.

#### Function prototype  
```
ITMGContext public void EnableMic(boolean isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the microphone, set this parameter to true, otherwise, set it to false. |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableMic(true);
```

### Obtain the microphone status
This API is used to obtain the microphone status. If "0" is returned, the microphone is off. If "1" is returned, the microphone is on. If "2" is returned, the microphone is being worked on. If "3" is returned, no microphone exists. If "4" is returned, the microphone is not initialized well.
#### Function prototype  
```
ITMGContext TMGAudioCtrl public int GetMicState() 
```
#### Sample code  
```
int micState = ITMGContext.GetInstance(this).GetAudioCtrl().GetMicState();
```

### Enable/disable a capturing device
This API is used to enable/disable a capturing device. The devices is not enabled by default after a user enters the room.
- This API can only be called after a user enters the room. The device is disabled after the user exits the room.
- Operations such as permission application and volume type adjustment come with enabling the capturing device on mobile.

#### Function prototype  
```
ITMGContext public int EnableAudioCaptureDevice(boolean isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the capturing device, set this parameter to true, otherwise, set it to false. |

#### Sample code

```
Enable a capturing device
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioCaptureDevice(true);
```

### Obtain the status of a capturing device
This API is used to obtain the status of a capturing device.
#### Function prototype

```
ITMGContext public boolean IsAudioCaptureDeviceEnabled()
```
#### Sample code

```
bool IsAudioCaptureDevice =ITMGContext.GetInstance(this).GetAudioCtrl().IsAudioCaptureDeviceEnabled();
```

### Enable/disable audio upstream
This API is used to enable/disable audio upstream. If the capturing device is already enabled, captured audio data will be sent. If it is not enabled, it remains silent. To enable/disable a capturing device, see API EnableAudioCaptureDevice.

#### Function prototype

```
ITMGContext public int EnableAudioSend(boolean isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the audio upstream, set this parameter to true, otherwise, set it to false. |

#### Sample code  

```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioSend(true);
```

### Obtain the status of audio upstream
This API is used to obtain the status of audio upstream.
#### Function prototype  
```
ITMGContext TMGAudioCtrl boolean IsAudioSendEnabled()
```
#### Sample code  
```
bool IsAudioSend =  =ITMGContext.GetInstance(this).GetAudioCtrl().IsAudioSendEnabled();
```

### Obtain real-time microphone volume
This API is used to obtain real-time microphone volume. An int value is returned.
#### Function prototype  
```
ITMGContext TMGAudioCtrl int GetMicLevel() 
```
#### Sample code  
```
int micLevel = ITMGContext.GetInstance(this).GetAudioCtrl().GetMicLevel();
```

### Set software volume for the microphone
This API is used to set the software volume for the microphone. The corresponding parameter is "volume". The value "0" sets the volume to Mute, and "100" means the volume remains unchanged. Default is 100.
#### Function prototype  
```
ITMGContext TMGAudioCtrl int SetMicVolume(int volume) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| volume    |int      | Sets the volume. Value range: 0 - 200 |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().SetMicVolume(volume);
```
### Obtain the software volume for the microphone
This API is used to obtain the software volume for the microphone. An int value is returned. Value 101 represents API SetMicVolume has not been called.
#### Function prototype  
```
ITMGContext TMGAudioCtrl public int GetMicVolume()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().GetMicVolume();
```

### Enable/disable the speaker
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

### Obtain the speaker status
This API is used to obtain the speaker status. If "0" is returned, the speaker is off. If "1" is returned, the speaker is on. If "2" is returned, the speaker is being worked on. If "3" is returned, no speaker exists. If "4" is returned, the speaker is not initialized well.
#### Function prototype  
```
ITMGContext TMGAudioCtrl public int GetSpeakerState() 
```

#### Sample code  
```
int micState = ITMGContext.GetInstance(this).GetAudioCtrl().GetSpeakerState();
```

### Enable/disable a playback device
This API is used to enable/disable a playback device.

#### Function prototype  
```
ITMGContext public int EnableAudioPlayDevice(boolean isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean        | To disable the playback device, set this parameter to false, otherwise, set it to true. |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioPlayDevice(true);
```

### Obtain the status of a playback device
This API is used to obtain the status of a playback device.
#### Function prototype

```
ITMGContext public int IsAudioPlayDeviceEnabled()
```
#### Sample code  

```
bool IsAudioPlayDevice = ITMGContext.GetInstance(this).GetAudioCtrl().IsAudioPlayDeviceEnabled();
```

### Enable/disable audio downstream
This API is used to enable/disable audio downstream. If the playback device is enabled, audio data of other users in the room will be played back. If it is not enabled, it remains silent. To enable/disable a playback device, see API EnableAudioPlayDevice.

#### Function prototype  

```
ITMGContext public int EnableAudioRecv(boolean isEnabled)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |To enable the audio downstream, set this parameter to true, otherwise, set it to false. |

#### Sample code  

```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioRecv(true);
```



### Obtain the status of audio downstream
This API is used to obtain the status of audio downstream.
#### Function prototype  
```
ITMGContext TMGAudioCtrl public boolean IsAudioRecvEnabled()
```

#### Sample code  
```
bool IsAudioRecv = ITMGContext.GetInstance(this).GetAudioCtrl().IsAudioRecvEnabled();
```

### Obtain real-time speaker volume
This API is used to obtain real-time speaker volume. An int value is returned to indicate the real-time speaker volume.
#### Function prototype  
```
ITMGContext TMGAudioCtrl public int GetSpeakerLevel() 
```

#### Sample code  
```
int SpeakLevel = ITMGContext.GetInstance(this).GetAudioCtrl().GetSpeakerLevel();
```

### Set software volume for the speaker
This API is used to set the software volume for the speaker.
The corresponding parameter is "volume". The value "0" sets the volume to Mute, and "100" means the volume remains unchanged. Default is 100.

#### Function prototype  
```
ITMGContext TMGAudioCtrl public int SetSpeakerVolume(int volume) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| volume    |int        | Sets the volume. Value range: 0 - 200 |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().SetSpeakerVolume(volume);
```

### Obtain software volume for the speaker
This API is used to obtain the software volume for the speaker. An int value is returned to indicate the software volume for the speaker. Value 101 represents API SetSpeakerVolume has not been called.
"Level" indicates the real-time volume, and "Volume" the software volume for the speaker. The ultimate volume equals to Level*Volume%. For example, if the value for "Level" is 100 and the one for "Volume" is 60, the ultimate volume will be "60".

#### Function prototype  
```
ITMGContext TMGAudioCtrl public int GetSpeakerVolume()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().GetSpeakerVolume();
```


### Enable in-ear monitoring
This API is used to enable in-ear monitoring.
#### Function prototype  
```
ITMGContext TMGAudioCtrl public int EnableLoopBack(boolean enable)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| enable    |boolean         | Specifies whether to enable in-ear monitoring |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableLoopBack(true);
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
This API is used to start playing back the accompaniment. Three formats are supported: m4a,  wav, and mp3. This API is used to reset the volume.

#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int StartAccompany(String filePath, boolean loopBack, int loopCount) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    	|String    	| Accompaniment's playback path |
| loopBack  	|boolean    	|Indicates whether to send a mix. This is generally set to true, indicating that other users can also hear the accompaniment.	|
| loopCount	|int    		| The number of loops. Value -1 means an infinite loop. |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StartAccompany(filePath,true,loopCount,duckerTimeMs);
```

### Callback for accompaniment playback
After the accompaniment is over, the event message ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH is returned, which is identified in the OnEvent function.
The passed parameter "intent" includes result and file_path.
#### Sample code  
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH == type)
        {
		//Callback for accompaniment playback
	}
}
```

### Stop playing back the accompaniment
This API is used to stop playing back the accompaniment.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int StopAccompany(int duckerTimeMs)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| duckerTimeMs    |int             | Fading time |

#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StopAccompany(duckerTimeMs);
```

### Indicate whether the accompaniment is over
If it is over, "true" is returned. If it is not, "false" is returned.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public boolean IsAccompanyPlayEnd() 
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().IsAccompanyPlayEnd();
```


### Pause playing back the accompaniment
This API is used to pause playing back the accompaniment.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int PauseAccompany()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PauseAccompany();
```


### Replay the accompaniment
This API is used to replay the accompaniment.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int ResumeAccompany()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().ResumeAccompany();
```



### Set the accompaniment volume
This API is used to set the DB volume. Value range: 0 - 200. Default is 100. A value greater than 100 means volume up, otherwise volume down.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int SetAccompanyVolume(int vol)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| vol    |int             |Indicates the volume value |

#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().SetAccompanyVolume(Volume);
```

### Obtain the volume of the accompaniment
This API is used to get the DB volume.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int GetAccompanyVolume()
```
#### Sample code  
```
string currentVol = "VOL: " + ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetAccompanyVolume();
```

### Obtain the accompaniment playback progress
The following two APIs are used to obtain the accompaniment playback progress. Note: Current/Total = current loop times, Current % Total = current loop playback position.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public long GetAccompanyFileTotalTimeByMs()
ITMGContext TMGAudioEffectCtrl public long GetAccompanyFileCurrentPlayedTimeByMs()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetAccompanyFileTotalTimeByMs();
ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetAccompanyFileCurrentPlayedTimeByMs();
```


### Set the playback progress
This API is used to set the playback progress.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int SetAccompanyFileCurrentPlayedTimeByMs(long time)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| time    |long                | Indicates the playback progress in milliseconds |

#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().SetAccompanyFileCurrentPlayedTimeByMs(time);
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
This API is used to play the sound effect. The sound effect ID in the parameter needs to be managed by the App side, uniquely identifying a separate file. Three formats are supported: m4a, wav, and mp3.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int PlayEffect(int soundId, String filePath, boolean loop) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    	|int    		|Indicates the sound effect ID |
| filePath    	|String		|Indicates the sound effect path |
| loop    		|boolean	|Indicates whether to repeat playback |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PlayEffect(soundId,filePath,loop);
```


### Pause the sound effect
This API is used to pause playing back the sound effect.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int PauseEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int                    |Indicates the sound effect ID |

#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PauseEffect(soundId);
```

### Pause all sound effects
This API is used to pause all sound effects.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int PauseAllEffects()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PauseAllEffects();
```

### Replay the sound effect
This API is used to replay the sound effect.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int ResumeEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int                    |Indicates the sound effect ID |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().ResumeEffect(soundId);
```



### Replay all sound effects
This API is used to replay all sound effects.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int ResumeAllEffects()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().ResumeAllEffects();
```

### Stop the sound effect
This API is used to stop the sound effect.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int StopEffect(int soundId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| soundId    |int                    |Indicates the sound effect ID |
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StopEffect(soundId);
```

### Stop all sound effects
This API is used to stop all sound effects.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int StopAllEffects()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StopAllEffects();
```

### Voice changing effects
This API is used to set the voice changing effects.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl  public int setVoiceType(int type);
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| type    |int                    |Indicates the type of local voice changing effect |



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
ITMGContext.GetInstance(this).GetAudioEffectCtrl().setVoiceType(0);
```



### Obtain the volume of sound effects
This API is used to obtain the volume (linear volume) of sound effects. A value greater than 100 means volume up, otherwise volume down.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int GetEffectsVolume()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetEffectsVolume();
```


### Set the volume of sound effects
This API is used to set the volume of sound effects.
#### Function prototype  
```
ITMGContext TMGAudioEffectCtrl public int SetEffectsVolume(int volume)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| volume    |int                    |Indicates the volume value |

#### Sample code  
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().SetEffectsVolume(Volume);
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
ITMGContext TMGPTT public void ApplyPTTAuthbuffer(String authBuffer)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| authBuffer    |String                    | Authentication |

#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().ApplyPTTAuthbuffer(authBuffer);
```

### Specify the maximum length of a voice message
This API is used to specify the maximum length of a voice message, which is limited to 60 seconds.
#### Function prototype  
```
ITMGContext TMGPTT public void SetMaxMessageLength(int msTime)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| msTime     |  int           | Voice duration |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().SetMaxMessageLength(msTime);
```


### Start recording
This API is used to start recording.
#### Function prototype  
```
ITMGContext TMGPTT public void StartRecording(String fileDir)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileDir    |String                     | Path for storing the voice file |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().StartRecording(fileDir);
```

### Callback for starting recordings
The callback function OnEvent is called after the recording is started. The event message is ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE is returned, which is identified in the OnEvent function.
The passed parameter includes result and file_path.

#### Sample code  
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE == type)
        	{
            		//Send a callback after the recording has started
        	}
}
```

### Stop recording
This API is used to stop recording.
#### Function prototype  
```
ITMGContext TMGPTT public int StopRecording()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().StopRecording();
```



### Cancel recording
This API is used to cancel recording.
#### Function prototype  
```
ITMGContext TMGPTT public int CancelRecording()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().CancelRecording();
```

### Upload voice files
This API is used to upload voice files.
#### Function prototype  
```
ITMGContext TMGPTT public void UploadRecordedFile(String filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    |String                      |Path for uploading the voice file |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().UploadRecordedFile(filePath);
```


### Callback for uploading voice files
After the voice file is uploaded, the event message ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE is returned, which is identified in the OnEvent function.
The passed parameter includes result, file_path and file_id.
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE== type)
       	 {
           	//Send a callback after a voice file has been uploaded
       	 }
}
```


### Download voice files
This API is used to download voice files.
#### Function prototype  
```
ITMGContext TMGPTT public void DownloadRecordedFile(String fileID, String downloadFilePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileID    			|String                      |URL to a file |
| downloadFilePath 	|String                      |Local path for saving the file |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().DownloadRecordedFile(url,path);
```


### Callback for downloading voice files
After the voice file is downloaded, the event message ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE is returned, which is identified in the OnEvent function.
The passed parameter includes result, file_path and file_id.

```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE== type)
        {
            //Downloaded successfully        
	}
}
```



### Play voice files
This API is used to play voice files.
#### Function prototype  
```
ITMGContext TMGPTT public int PlayRecordedFile(String downloadFilePath) 
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| downloadFilePath    |String   |Path of the file |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().PlayRecordedFile(downloadFilePath);
```


### Callback for playing voice files
After the voice file is played back, the event message ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE is returned, which is identified in the OnEvent function.
The passed parameter includes result and file_path.
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE== type)
       	 	{
			//Callback for playing a voice file 
		}
}
```




### Stop playing voice files
This API is used to stop playing back voice files.
#### Function prototype  
```
ITMGContext TMGPTT public int StopPlayFile()
```

#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().StopPlayFile();
```



### Obtain the size of a voice file
This API is used to get the size of a voice file.
#### Function prototype  
```
ITMGContext TMGPTT public int GetFileSize(String filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    |String                     |Path of the voice file |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().GetFileSize(path);
```

### Obtain the length of a voice file
This API is used to obtain the length of a voice file (in milliseconds).
#### Function prototype  
```
ITMGContext TMGPTT public int GetVoiceFileDuration(String filePath)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| filePath    |String                     |Path of the voice file |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().GetVoiceFileDuration(path);
```


### Convert the specified voice file into text with Speech Recognition
This API is used to convert the specified voice file into text with Speech Recognition.

#### Function prototype  
```
ITMGContext TMGPTT public int SpeechToText(String fileID)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| fileID    |String                     |URL of the voice file |
#### Sample code  
```
ITMGContext.GetInstance(this).GetPTT().SpeechToText(fileID);
```

### Callback for Speech Recognition
After the specified voice file is converted into text with Speech Recognition, the event message ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE is returned, which is identified in the OnEvent function.
The passed parameter includes result, file_path and text (recognized text).
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE == type)
       	 {
            //Voice file recognized successfully       
	 }
}
```
## Advanced APIs

### Obtain the version number
This API is used to get the SDK version number for analysis.
#### Function prototype
```
ITMGContext public void GetSDKVersion()
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetSDKVersion();
```

### Set the level of logs to be printed
This API is used to set the level of logs to be printed.
#### Function prototype
```
ITMGContext int SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
```



| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| logLevel    		|int | Level of logs to be printed |
| enableWrite    	| bool | Indicates whether to write a file. The default is Yes |
| enablePrint    	|bool | Indicates whether to write a console. The default is Yes |




|ITMG_LOG_LEVEL|Description |
| -------------------------------|----------------------|
|TMG_LOG_LEVEL_NONE=0		|Do not print logs |
|TMG_LOG_LEVEL_ERROR=1		|Prints error logs (default) |
|TMG_LOG_LEVEL_INFO=2			|Prints prompt logs |
|TMG_LOG_LEVEL_DEBUG=3		|Prints development and debugging logs |
|TMG_LOG_LEVEL_VERBOSE=4		|Prints high-frequency logs |
#### Sample code  
```
ITMGContext.GetInstance(this).SetLogLevel(1,true,true);
```



### Set the path of logs to be printed
This API is used to set the path of logs to be printed. The default path is: /sdcard/Android/data/xxx.xxx.xxx/files.
#### Function prototype
```
ITMGContext int SetLogPath(String logDir)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| logDir    		|String  | Path |

#### Sample code  
```
ITMGContext.GetInstance(this).SetLogPath(path);
```


### Obtain diagnostic messages
This API is used to obtain information about the quality of real-time audio/video calls. This API is mainly used to check the quality of real-time calls and troubleshoot problems, and can be ignored at the business side.
#### Function prototype  
```
IITMGContext TMGRoom public String GetQualityTips() 
```
#### Sample code  
```
ITMGContext.GetInstance(this).GetRoom().GetQualityTips();
```

### Add an ID to the audio data blacklist
This API is used to add an ID to the audio data blacklist. A return value of 0 indicates that the call failed.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl AddAudioBlackList(String openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| openId    | String | ID that needs to be added to the blacklist |
#### Sample code  

```
ITMGContext.GetInstance(this).GetAudioCtrl().AddAudioBlackList(openId);
```

### Remove an ID from the audio data blacklist
This API is used to remove an ID from the audio data blacklist. A return value of 0 indicates that the call failed.
#### Function prototype  

```
ITMGContext ITMGAudioCtrl RemoveAudioBlackList(String openId)
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| openId    | String | ID that needs to be removed from the blacklist |
#### Sample code  

```
ITMGContext.GetInstance(this).GetAudioCtrl().RemoveAudioBlackList(openId);
```


## Callback Messages

#### Message list:

| Message | Description of Message   
| ------------- |:-------------:|
|ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		| Enters the audio room |
|ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		| Exits the audio room |
|ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT		| Room disconnection due to network or other reasons |
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE		|Room type change event |
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

