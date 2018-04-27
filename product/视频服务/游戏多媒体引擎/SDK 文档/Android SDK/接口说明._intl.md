Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes access technologies for Android development so that Android developers can easily debug and access APIs for Tencent Cloud GME.
## SDK Initialization
### 1. Obtain the Communication Manager
SDK initialization starts with the TMGContext communication manager. The first step is to get a singleton.

#### Function Prototype
```
public static ITMGContext GetInstance(Context context)
```

|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------|
| context    |Context |Context object of an application.|

#### Sample Code
```
import com.tencent.TMG.ITMGContext;
TMGContext.getInstance(this);
```

### 2. Register a Callback
Register a callback function with the SDK to receive callback information.
Declare a callback function first.
#### Function Prototype
```
public abstract static class ITMGDelegate {
        public ITMGDelegate() {
        }

        public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
        }
}
```
#### Sample Code
```
private ITMGContext.ITMGDelegate itmgDelegate = null;
```
Rewrite the callback function in a constructor to process callback parameters.

|Parameter     | Type         |Description|
| ------------- |: -------------: | ------------- |
| type    	|ITMGContext.ITMG_MAIN_EVENT_TYPE 	|Type of an event for which a callback is performed.				|
| data    	|Intent message type  						|Callback-related information or event data.	|

Callback event list:

|Callback Event     | Description
| ------------- |: -------------:|
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    					|Entry into an audio/video room.
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    					|Exit from an audio/video room.
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    			|Disconnection from a room due to network issues or other reasons.
| ITMG_MAIN_EVENT_TYPE_ENABLE_MIC    					|Microphone enabled.
| ITMG_MAIN_EVENT_TYPE_DISABLE_MIC    					|Microphone disabled.
|ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER					|Speaker enabled.
|ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER					|Speaker disabled.
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE					|Role changed.
|ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH				|Accompaniment ended.
|ITMG_MAIN_EVNET_TYPE_USER_UPDATE						|Room member updated.
|ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE			|PTT recorded.
|ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE			|PTT uploaded.
|ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE		|PTT downloaded.
|ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE				|PTT played.
|ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE		|Speech converted into text.
|ITMG_MAIN_EVENT_TYPE_OPEN_CAMERA					|Camera turned on.
|ITMG_MAIN_EVENT_TYPE_CLOSE_CAMERA					|Camera turned off.

#### Sample Code
```
itmgDelegate= new ITMGContext.ITMGDelegate() {
            @Override
 			public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
                }
        };
```
**All callback functions are processed by the OnEvent function.**
Register a callback function with the SDK before users enter a room.
#### Function Prototype
```
ITMGContext public int SetTMGDelegate(ITMGDelegate delegate)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| delegate    |ITMGDelegate |SDK callback function.|
#### Sample Code
```
TMGContext.GetInstance(this).SetTMGDelegate(itmgDelegate);
```

## Real-Time Voice Access

### 1. Set Relevant Information
Relevant information is applied for through Tencent Cloud Console. For more information, see the [GME Access Guide](/document/product/607/10782).
The SetAppInfo function contains the **sdkAppId**, **accountType**, and **openID** parameters. The values of **sdkAppId** and **accountType** are obtained from Tencent Cloud Console. The value of **OpenID** indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers, and the ID must be unique in an application. Currently, the ID can be only of the int64 type.
#### Function Prototype
```
ITMGContext public int SetAppInfo(String sdkAppId, String accountType, String openID)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| sdkAppId    	|String  |The value is obtained from Tencent Cloud Console.			|
| accountType    	|String  |The value is obtained from Tencent Cloud Console.			|
| openID    		|String  |The value indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers. Currently, the value must be greater than **10000**.|
#### Sample Code
```
ITMGContext.GetInstance(this).SetAppInfo(sdkAppId, accountType, identifier);
```
The SetAppVersion function is used to set version information that is used during log query and debugging. No functions are affected if version information is not set.
#### Function Prototype
```
ITMGContext public void SetAppVersion(String sAppVersion)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| sAppVersion    |String  |Version number.|
#### Sample Code
```
ITMGContext.GetInstance(this).SetAppVersion(appVersion);
```
The GetSDKVersion function is used to obtain the SDK version number.
#### Function Prototype
```
ITMGContext public void GetSDKVersion()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetSDKVersion();
```
Then, the value of **AuthBuffer** is generated for encryption and authentication of relevant functions. For more information about how to obtain relevant parameters and other information, see the [GME Access Guide](/document/product/607/10782).

The function returns a Byte[] value.
#### Function Prototype
```
AuthBuffer public native byte[] genAuthBuffer(int sdkAppId, int roomId, String identifier, int accountType, String key, int expTime, int authBits)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| appId    		|int   	|The value is the same as the value of **sdkAppId** on Tencent Cloud Console.		|
| roomId    		|int   	|Name of the room to be entered.							|
| identifier    	|String   |User identifier.								|
| accountType    	|int   	|The value is obtained from Tencent Cloud Console.	|
| key    			|string   	|The value is the key provided by Tencent Cloud Console.					|
| expTime    		|int   	|Timeout interval for entering a room.						|
| authBits    		|int    	|Permissions.									|

>About permissions
The value **AUTH_BITS_ALL** indicates all permissions. It is recommended that this parameter be set to **AUTH_BITS_ALL** for real-time users and VJs. The value **AUTH_BITS_RECV** indicates downstream permissions. It is recommended that this parameter be set to **AUTH_BITS_RECV** for listening- or watching-only audiences. The startAccompany function is unavailable for downstream permissions.

#### Sample Code
```
import com.tencent.av.sig.AuthBuffer;//Header file
long nExpUTCTime = 1800 + System.currentTimeMillis() / 1000L;
byte[] authBuffer=AuthBuffer.getInstance().genAuthBuffer(Integer.parseInt(sdkAppId), Integer.parseInt(strRoomID),identifier, Integer.parseInt(accountType), key, (int)nExpUTCTime, (int) ITMGContext.ITMG_AUTH_BITS_DEFAULT);
```

### 2. Enter a Room
When a user enters a room with a generated **AuthBuffer** value, the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback.
>Note: The microphone and speakers are disabled by default when a user enters a room.

For more information about role settings, see the [GME Voice Role Description](/document/product/607/15172).
#### Function Prototype
```
ITMGContext public abstract void EnterRoom(int roomID, String controlRole, byte[] authBuffer)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| roomID    		|int    	|Room number, which is an integer of six or more digits.	|
| controlRole    	|String  	|Role name. Set the parameter based on the requirements.		|
| authBuffer    	|byte[]  	|The value is used for authentication.						|
#### Sample Code
```
ITMGContext.GetInstance(this).EnterRoom(Integer.parseInt(strRoomID), "user", authBuffer);
```

### 3. Callback for Entering a Room
When a user enters a room, the TMGContext communication manager checks whether a corresponding callback function is registered. If yes, TMGContext calls the callback function of the event. For example, the onEnterRoomComplete function is called when a user enters a room and the onExitRoomComplete function is called when the user exits from the room.
Code description:
```
public void onEnterRoomComplete(int nRet, String strErrMsg) {
            if(TMGContext.this.mTmgDelegate != null) {
                Intent it= TMGCallbackHelper.GetCallBackIntent(nRet, strErrMsg);
                TMGContext.this.mTmgDelegate.OnEvent(ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ENTER_ROOM, it);
            } else {
                TMGContext.this.HandleUnExceptionEnd(nRet, strErrMsg);
            }
        }
```
The value of the passed intent parameter is an Intent value returned by the TMGCallbackHelper.GetCallBackIntent function and contains **result** and **error_info**.
Code description:
```
static Intent GetCallBackIntent(int nRet, String strErrMsg) {
        Intent intent= new Intent();
        intent.putExtra("result", nRet);
        intent.putExtra("error_info", strErrMsg);
        return intent;
    }
```
#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	int nErrCode =data.getIntExtra("result" , -1);
	if (nErrCode == AVError.AV_OK)
		{
			//Room entry success
		}
	}
```
### 4. Check Whether a User Has Entered a Room
The IsRoomEntered function is used to check whether a user has entered a room. The return value of this function is of the bool type.
#### Function Prototype
```
ITMGContext public boolean IsRoomEntered()
```
#### Sample Code
```
ITMGContext.GetInstance(this).IsRoomEntered();
```

### 5. Exit from a Room
The ExitRoom function is used to exit from a room.
#### Function Prototype
```
ITMGContext public void ExitRoom()
```
#### Sample Code
```
ITMGContext.GetInstance(this).ExitRoom();
```

### 6. Callback for Exiting from a Room
After a user exits from a room, the ITMG_MAIN_EVENT_TYPE_EXIT_ROOM event message is sent, which is checked in the OnEvent function.
#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_EXIT_ROOM == type)
        {
            //Receive a room exit success message
        }
}
```
### 7. Suspend Acquisition and Playback by the Audio Engine
The PauseAudio function is used to suspend acquisition and playback by the audio engine and is effective only after a user enters a room.
After the EnterRoom function is successfully called, the microphone is occupied and other programs cannot acquire data from the microphone.
>Note: Calling of EnableMic(false) cannot release the microphone.

To release a microphone, call the PauseAudio function that can suspend the audio engine. To resume audio acquisition, call the ResumeAudio function.
#### Function Prototype
```
ITMGContext ITMGAudioCtrl public int PauseAudio()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().PauseAudio();
```
### 8. Resume Acquisition and Playback by the Audio Engine
The ResumeAudio function is used to resume acquisition and playback by the audio engine and is effective only after a user enters a room.
#### Function Prototype
```
ITMGContext ITMGAudioCtrl public int ResumeAudio()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().ResumeAudio();
```

### 9. Role Setting
Change a flow control role. The ChangeRole method is used to set a user role before a user joins a channel. The user is allowed to change the role after the user joins a channel.
The following six roles are automatically established by default: esports, Rhost, Raudience, Werewolf, host, and audience. For more information about role descriptions, see the [GME Voice Role Description](/document/product/607/15172).
#### Function Prototype
```
ITMGContext TMGRoom public void ChangeRole(String role, byte[] authBuffer)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| role    			|String     |Role			|
| authBuffer    	|byte[]     |The parameter must be reset each time.	|

>Note
Changing a flow control role means modifying audio and video encoding parameters. Therefore, the audio and video encoding API needs to be called to reset **AuthBuffer**. For more information, see how to generate **AuthBuffer**.

The following table lists the speech quality corresponding to each role.

|Role Name     | Applicable Scenario         |Key Features|
| ------------- |: -------------: |-------------
| esports    	|MOBA, competitive, and shooting games.     								|Ordinary sound quality and ultra-low latency.	|
| Rhost    	|Commander mode of MMORPGs. Only a commander can join broadcasting.     		|High fluency and low latency.		|
| Raudience	|Commander mode of MMORPGs. Only a commander can join broadcasting.     		|High fluency and low latency.		|
| Werewolf 	|Werewolf, casual games, and other games.										|Good sound quality and high anti packet loss rate.	|
| host  		|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.	|Good sound quality and high anti packet loss rate.	|
| audience  	|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.	|Good sound quality and high anti packet loss rate.	|

#### Sample Code
```
ITMGContext.GetInstance(this).GetRoom().ChangeRole("user",bytes);
```

### 10. Callback for a Role Setting
After a role setting, the ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE event message is sent as a callback. The value of the returned intent parameter contains **result** and **error_info**. The message is checked in the OnEvent function.
#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE == type)
        {
		int nErrCode =data.getIntExtra("result" , -1);
		if (nErrCode == AVError.AV_OK)
			{
				//Role changed
			}
	}
}
```

### 11. Member State Change
The member state change event is triggered to send notifications only when the state of a member changes. To allow real-time member state query, cache the state each time the upper layer receives the ITMG_MAIN_EVNET_TYPE_USER_UPDATE event message, in which the intent parameter contains  **event_id** and **user_list**. The message is checked in the OnEvent function.
#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_USER_UPDATE == type)
        {
		//Update the member state
		int nEventID = data.getIntExtra("event_id", 0);
		String[] identifierList =data.getStringArrayExtra("user_list");
	}
}
```
### 12. Enable or Disable an Audio Data Blacklist
The blacklist is reset to a new member list each time the SetAudioBlackList function is called to enable the blacklist. The function is called only when audio data to be received needs to be customized. If the function is not called, all audio data in a room is received by default. If the function returns **0**, the call fails.
#### Function Prototype
```
ITMGContext TMGRoom public int SetAudioBlackList(String[] identifierList)
```

|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| identifierList    |String[]     |Blacklist.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetRoom().SetAudioBlackList(users);
```

### 13. Enable or Disable a Microphone
The EnableMic function is used to enable or disable a microphone.
>Note: The microphone and speakers are disabled by default when a user enters a room.

#### Function Prototype
```
ITMGContext public void EnableMic(boolean isEnabled)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| isEnabled    |boolean     |To enable a microphone, set the input parameter to **true**. To disable a microphone, set the input parameter to **false**.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableMic(true);
ITMGContext.GetInstance(this).GetAudioCtrl().EnableMic(false);
```
### 14. Callback of a Microphone Event
The OnEvent function is used for callback of a microphone event. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_MIC or ITMG_MAIN_EVENT_TYPE_DISABLE_MIC, which is checked in the OnEvent function.
The value of the passed intent parameter that is passed contains **audio_state** and **audio_errcode**.
#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ENABLE_MIC == type)
        {
		nErrCode = data.getIntExtra("audio_errcode", 0);
		if (nErrCode == AVError.AV_OK)
            		{
				//Microphone enabled
			}
	}
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_DISABLE_MIC == type)
        {
		nErrCode = data.getIntExtra("audio_errcode", 0);
		if (nErrCode == AVError.AV_OK)
            		{
				//Microphone disabled
			}
	}
}
```
### 15. Obtain the Status of a Microphone
The GetMicState function is used to obtain the status of a microphone. Value **1** indicates that the microphone is turned on and value **2** indicates that the microphone is turned off.
#### Function Prototype
```
ITMGContext TMGAudioCtrl public int GetMicState()
```
#### Sample Code
```
int micState = ITMGContext.GetInstance(this).GetAudioCtrl().GetMicState();
```

### 16. Obtain the Real-Time Volume of a Microphone
The GetMicLevel function is used to obtain the real-time volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
ITMGContext TMGAudioCtrl public int GetMicLevel() 
```
#### Sample Code
```
int micLevel = ITMGContext.GetInstance(this).GetAudioCtrl().GetMicLevel();
```

### 17. Set the Software Volume of a Microphone
The SetMicVolume function is used to set the software volume of a microphone. The **volume** parameter specifies the software volume of a microphone. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.
#### Function Prototype
```
ITMGContext TMGAudioCtrl public int SetMicVolume(int volume) 
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| volume    |int      |Volume, ranging from **0** to **100**.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().SetMicVolume(volume);
```

### 18. Obtain the Software Volume of a Microphone
The GetMicVolume function is used to obtain the software volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
ITMGContext TMGAudioCtrl public int GetMicVolume()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().GetMicVolume();
```

### 19. Enable or Disable Speakers
The EnableSpeaker function is used to enable or disable speakers.
#### Function Prototype
```
ITMGContext public void EnableSpeaker(boolean isEnabled)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| isEnabled    |boolean       |To enable speakers, set the input parameter to **true**. To disable speakers, set the input parameter to **false**.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableSpeaker(true);
ITMGContext.GetInstance(this).GetAudioCtrl().EnableSpeaker(false);
```

### 20. Callback of a Speaker Event
The OnEvent function is used for callback of a speaker event. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER or ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER.
The value of the passed intent parameter that is passed contains **audio_state** and **audio_errcode**.
#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER == type)
        {
		nErrCode = data.getIntExtra("audio_errcode", 0);
		if (nErrCode == AVError.AV_OK)
            		{
				//Speakers enabled
			}
	}
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER == type)
        {
		nErrCode = data.getIntExtra("audio_errcode", 0);
		if (nErrCode == AVError.AV_OK)
            		{
				//Speakers disabled
			}
	}
}
```

### 21. Obtain the Status of Speakers
The GetSpeakerState function is used to obtain the status of speakers. The return value of this function is of the int type. Value **1** indicates that speakers are enabled and value **2** indicates that speakers are disabled.
#### Function Prototype
```
ITMGContext TMGAudioCtrl public int GetSpeakerState()
```

#### Sample Code
```
int micState = ITMGContext.GetInstance(this).GetAudioCtrl().GetSpeakerState();
```

### 22.Obtain the Real-Time Volume of Speakers
The GetSpeakerLevel function is used to obtain the real-time volume of speakers. The return value of this function is of the int type.
#### Function Prototype
```
ITMGContext TMGAudioCtrl public int GetSpeakerLevel() 
```

#### Sample Code
```
int SpeakLevel = ITMGContext.GetInstance(this).GetAudioCtrl().GetSpeakerLevel();
```

### 23. Set the Software Volume of Speakers
The SetSpeakerVolume function is used to set the software volume of speakers.
>Note: The **volume** parameter specifies the software volume of speakers. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.

#### Function Prototype
```
ITMGContext TMGAudioCtrl public int SetSpeakerVolume(int volume)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| volume    |int        |Volume, ranging from **0** to **100**.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().SetSpeakerVolume(volume);
```

### 24. Obtain the Software Volume of Speakers
The GetSpeakerVolume function is used to obtain the software volume of speakers. The return value of this function is of the int type.
>Note: The **Level** parameter indicates the real-time volume, while the **Volume** parameter indicates the software volume of speakers. The final volume is calculated as follows: Final volume = Value of Level x Value of Volume%. For example, if the values of **Level** and **Volume** are **100** and **60** respectively, the final volume is 60.

#### Function Prototype
```
ITMGContext TMGAudioCtrl public int GetSpeakerVolume()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().GetSpeakerVolume();
```
### 25. Enable In-Ear Monitoring
The EnableLoopBack function is used to enable in-ear monitoring.
#### Function Prototype
```
ITMGContext TMGAudioCtrl public int EnableLoopBack(boolean enable)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| enable    |boolean         |Indicates whether to enable in-ear monitoring.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableLoopBack(true);
```

### 26. Start Playing an Accompaniment
The StartAccompany function is used to start playing an accompaniment.
Note: 1. Calling the API will reset the volume.
2. The API is unavailable for downstream permissions.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int StartAccompany(String filePath, boolean loopBack, int loopCount)
```

|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| filePath   |String    |Path for playing an accompaniment.	|
| loopBack  |boolean    |Indicates whether to send a mix. The parameter is generally set to **true**.	|
| loopCount |int    	|Number of loops. Value **-1** means an infinite loop.	|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StartAccompany(filePath,true,loopCount,duckerTimeMs);
```

### 27. Callback for Playing an Accompaniment
After the playback of an accompaniment, the ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH event message is sent and the OnEvent function is called to check the message.
The value of the passed intent parameter contains **result** and **file_path**.
#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH == type)
        {
		//Callback for playing an accompaniment
	}
}
```

### 28. Stop Playing an Accompaniment
The StopAccompany function is used to stop playing an accompaniment.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int StopAccompany(int duckerTimeMs)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| duckerTimeMs    |int             |Fading time.|

#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StopAccompany(duckerTimeMs);
```

### 29. Check Whether the Playback of an Accompaniment Is Complete
The IsAccompanyPlayEnd function is used to check whether the playback of an accompaniment is complete. If yes, the function returns **true**. If no, it returns **false**.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public boolean IsAccompanyPlayEnd()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().IsAccompanyPlayEnd();
```


### 30. Pause an Accompaniment
The PauseAccompany function is used to pause an accompaniment.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int PauseAccompany()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PauseAccompany();
```


### 31. Resume an Accompaniment
The ResumeAccompany function is used to resume an accompaniment.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int ResumeAccompany()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().ResumeAccompany();
```

### 32. Set the Volume of an Accompaniment
The SetAccompanyVolume function is used to set the linear volume of an accompaniment. The default value is **100**. If the return value is greater than **100**, the accompaniment volume increases. If the return value is less than **100**, the accompaniment volume attenuates.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int SetAccompanyVolume(int vol)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| vol    |int             |Volume.|

#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().SetAccompanyVolume(Volume);
```

### 33. Obtain the Volume of an Accompaniment
The GetAccompanyVolume function is used to obtain the volume of an accompaniment.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int GetAccompanyVolume()
```
#### Sample Code
```
string currentVol = "VOL: " + ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetAccompanyVolume();
```

### 34. Obtain the Playback Progress of an Accompaniment
The following two functions are used to obtain the playback progress of an accompaniment. Note: Current / Total = Number of current loop times; Current % Total = Playback position of the current loop.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public long GetAccompanyFileTotalTimeByMs()
ITMGContext TMGAudioEffectCtrl public long GetAccompanyFileCurrentPlayedTimeByMs()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetAccompanyFileTotalTimeByMs();
ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetAccompanyFileCurrentPlayedTimeByMs();
```

### 35. Set Playback Progress
The SetAccompanyFileCurrentPlayedTimeByMs function is used to set playback progress.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int SetAccompanyFileCurrentPlayedTimeByMs(long time)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| time    |long                |Playback progress.|

#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().SetAccompanyFileCurrentPlayedTimeByMs(time);
```


### 36. Obtain the Volume of a Sound Effect
The GetEffectsVolume function is used to obtain the linear volume of a sound effect. The default value is **100**. If the return value is greater than **100**, the accompaniment volume increases. If the return value is less than **100**, the accompaniment volume attenuates.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int GetEffectsVolume()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().GetEffectsVolume();
```


### 37. Set the Volume of a Sound Effect
The SetEffectsVolume function is used to set the volume of a sound effect.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int SetEffectsVolume(int volume)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| volume    |int                    |Volume.|

#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().SetEffectsVolume(Volume);
```



### 38. Play a Sound Effect
The PlayEffect function is used to play a sound effect. The **soundId** parameter, which uniquely identifies an independent file, must be managed on the application side.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int PlayEffect(int soundId, String filePath, boolean loop)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| soundId    	|int    		|Sound effect ID.|
| filePath    	|String		|Sound effect path.|
| loop    		|boolean	|Indicates whether to repeat playback.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PlayEffect(soundId,filePath,loop);
```


### 39. Pause a Sound Effect
The PauseEffect function is used to pause a sound effect.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int PauseEffect(int soundId)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| soundId    |int                    |Sound effect ID.|

#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PauseEffect(soundId);
```

### 40. Pause All Sound Effects
The PauseAllEffects function is used to pause all sound effects.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int PauseAllEffects()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().PauseAllEffects();
```

### 41. Resume a Sound Effect
The ResumeEffect function is used to resume a sound effect.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int ResumeEffect(int soundId)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().ResumeEffect(soundId);
```

### 42. Resume All Sound Effects
The ResumeAllEffects function is used to resume all sound effects.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int ResumeAllEffects()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().ResumeAllEffects();
```

### 43. Stop Playing a Sound Effect
The StopEffect function is used to stop playing a sound effect.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int StopEffect(int soundId)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StopEffect(soundId);
```

### 44. Stop Playing All Sound Effects
The StopAllEffects function is used to stop playing all sound effects.
#### Function Prototype
```
ITMGContext TMGAudioEffectCtrl public int StopAllEffects()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetAudioEffectCtrl().StopAllEffects();
```

### 45. Obtain Diagnosis Information
The GetQualityTips function is used to obtain information about the quality of real-time voice or video chats. The function is mainly used to check the quality of real-time chats and detect problems. The function can be ignored on the service side.
#### Function Prototype
```
IITMGContext TMGRoom public String GetQualityTips()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetRoom().GetQualityTips();
```

## PTT Access
### 1. Initialize PTT Access
Initializing PTT access requires passing **accessToken** to TLS-related functions. For details on the process of obtaining **accessToken** for authentication, see the [GME Access Guide](/document/product/607/10782).
#### Function Prototype
```
TlsSig public String getTLSSig(int sdkAppId, String openID, String key)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| sdkAppId  	|int           	|The value is obtained from Tencent Cloud Console.|
| openID    	|String   	|Identifier that uniquely identifies a user. The setting rule is customized by application developers.|
| key    		|String      	|The value is the key provided by Tencent Cloud Console.|

```
ITMGPTT public int ApplyAccessToken(String accessToken)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| accessToken    |String                       |The value is the same as the value of **accessToken** returned by the getTLSSig function.|
#### Sample Code
```
private String GetAccessToken(String appid,String userid){
	String key ="";//Enter the private key for authentication
	return TlsSig.getInstance().getTLSSig(Integer.parseInt(appid),userid,key);
}

//Calling
String sig = GetAccessToken(sdkAppId,identifier);
	if (sig!=null){
		ITMGContext.GetInstance(this).GetPTT().ApplyAccessToken(sig);
	}else {
		Log.e("Sig","SigError");
	}
```

### 2. Specify the Maximum Length of a Voice Message
The SetMaxMessageLength function is used to specify the maximum length of a voice message. The maximum length can be 60 seconds.
#### Function Prototype
```
ITMGContext TMGPTT public void SetMaxMessageLength(int msTime)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| msTime    |int                    |Length of a voice message.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().SetMaxMessageLength(msTime);
```


### 3. Start Recording
The StartRecording function is used to start recording.
#### Function Prototype
```
ITMGContext TMGPTT public void StartRecording(String fileDir)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| fileDir    |String                     |Path for playing a voice file, which can be NULL.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().StartRecording(fileDir);
```

### 4. Callback for Starting Recording
After recording, the ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLET event message is sent and the OnEvent function is called to check the message.
The value of the passed parameter contains **result** and **file_path**.

#### Sample Code
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE == type)
        	{
            		//Callback for recording
        	}
}
```

### 5. Stop Recording
The StopRecording function is used to stop recording.
#### Function Prototype
```
ITMGContext TMGPTT public int StopRecording()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().StopRecording();
```



### 6. Cancel Recording
The CancelRecording function is used to cancel recording.
#### Function Prototype
```
ITMGContext TMGPTT public int CancelRecording()
```
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().CancelRecording();
```

### 7. Upload a Voice File
The UploadRecordedFile function is used to upload a voice file.
#### Function Prototype
```
ITMGContext TMGPTT public void UploadRecordedFile(String filePath)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| filePath    |String                      |Path for uploading a voice file.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().UploadRecordedFile(filePath);
```


### 8. Callback for Uploading a Voice File
After a voice file is uploaded, the ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE event message is sent, which is checked in the OnEvent function.
The value of the passed parameter contains **result**, **file_path**, and **file_id**.
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE== type)
       	 {
           	//Voice file uploaded
       	 }
}
```


### 9. Download a Voice File
The QAVDownloadFileCompleteCallback function is used to download a voice file.
#### Function Prototype
```
ITMGContext TMGPTT public void DownloadRecordedFile(String fileID, String downloadFilePath)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| fileID    			|String                      |URL of a file.	|
| downloadFilePath 	|String                      |Path for downloading a file.	|
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().DownloadRecordedFile(url,path);
```

### 10. Callback for Downloading a Voice File
After a voice file is downloaded, the ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE event message is sent, which is checked in the OnEvent function.
The value of the passed parameter contains **result**, **file_path**, and **file_id**.
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE== type)
        {
            //Successful download
	}
}
```



### 11. Play a Voice File
The PlayRecordedFile function is used to play a voice file.
#### Function Prototype
```
ITMGContext TMGPTT public int PlayRecordedFile(String downloadFilePath)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| downloadFilePath    |String                      |Path for downloading a file.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().PlayRecordedFile(downloadFilePath);
```


### 12. Callback for Playing a Voice File
As a callback for playing a voice file, the ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE event message is sent, which is checked in the OnEvent function.
The value of the passed parameter contains **result** and **file_path**.
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE== type)
       	 	{
			//Callback for playing a voice file
		}
}
```

### 13. Stop Playing a Voice File
The StopPlayFile function is used to stop playing a voice file.
#### Function Prototype
```
ITMGContext TMGPTT public int StopPlayFile()
```

#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().StopPlayFile();
```

### 14. Obtain the Size of a Voice File
The GetFileSize function is used to obtain the size of a voice file.
#### Function Prototype
```
ITMGContext TMGPTT public int GetFileSize(String filePath)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| filePath    |String                     |Path for storing a voice file.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().GetFileSize(path);
```

### 14. Obtain the Duration of a Voice File
The GetVoiceFileDuration function is used to obtain the duration of a voice file.
#### Function Prototype
```
ITMGContext TMGPTT public int GetVoiceFileDuration(String filePath)
```
|Parameter     | Type         |Description|
| ------------- |: -------------: |-------------
| filePath    |String                     |Path for storing a voice file.|
#### Sample Code
```
ITMGContext.GetInstance(this).GetPTT().GetVoiceFileDuration(path);
```

### 16. Convert Specified Speech into Text
As a callback for converting specified speech into text, the ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE event message is sent, which is checked in the OnEvent function.
The value of the passed intent parameter contains **result**, **file_path**, and **text** where **text** indicates text after conversion.
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if(ITMGContext.ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE == type)
       	 {
            //Speech converted
	 }
}
```
