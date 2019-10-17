Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes access technologies for Unity development so that Unity developers can easily debug and access APIs for Tencent Cloud GME.

## SDK Initialization
Relevant information is applied for through Tencent Cloud Console. For more information, see the [GME Access Guide](/document/product/607/10782).
The SetAppInfo function contains the **sdkAppId**, **accountType**, and **openID** parameters. The values of **sdkAppId** and **accountType** are obtained from Tencent Cloud Console. The value of **OpenID** indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers, and the ID must be unique in an application. Currently, the ID can be only of the int64 type.
#### Function Prototype
```
ITMGContext SetAppInfo(string sdkAppID, string accountType, string openID)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| sdkAppId    	|string  |The value is obtained from Tencent Cloud Console.|
| accountType    	|string  |The value is obtained from Tencent Cloud Console.|
| openID    		|string  |The value indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers. Currently, the value must be greater than **10000**.|
#### Sample Code
```
int ret = ITMGContext.GetInstance().SetAppInfo(str_appId, str_accountType, str_userId);
	if (ret != QAVError.OK) {
		return;
	}
```
## Video Access
### Set Relevant Information
The SetAppVersion function is used to set version information that is used during log query and debugging. No functions are affected if version information is not set.
#### Function Prototype
```
ITMGContext abstract void SetAppVersion(string sAppVersion)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| sAppVersion    |NSString  |Version number|
#### Sample Code
```
ITMGContext.GetInstance().SetAppVersion(sAppVersion);
```
The GetSDKVersion function is used to obtain the SDK version number.
#### Function Prototype
```
ITMGContext  abstract string GetVersion()
```
#### Sample Code
```
ITMGContext.GetInstance().GetVersion();
```
Then, the value of **AuthBuffer** is generated for encryption and authentication of relevant functions. For more information about how to obtain relevant parameters and other information, see the [GME Access Guide](/document/product/607/10782).

The return value of this function is of the NSData type.
#### Function Prototype
```
QAVAuthBuffer GenAuthBuffer(int appId, int roomId, string identifier, int accountType, string key, int expTime, uint authBits)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| appId    		|int   	|The value is the same as the value of **sdkAppId** on Tencent Cloud Console.		|
| roomId    		|int   	|Name of the room to be entered.							|
| identifier    	|string     	|User identifier.								|
| accountType    	|int   	|The value is obtained from Tencent Cloud Console.	|
| key    			|string   	|The value is the key provided by Tencent Cloud Console.					|
| expTime    		|int   	|Timeout interval for entering a room.						|
| authBits    		|uint     	|Permissions.									|

>About permissions
The value **AUTH_BITS_ALL** indicates all permissions. It is recommended that this parameter be set to **AUTH_BITS_ALL** for real-time users and VJs. The value **AUTH_BITS_RECV** indicates downstream permissions. It is recommended that this parameter be set to **AUTH_BITS_RECV** for listening- or watching-only audiences. The startAccompany function is unavailable for downstream permissions.

#### Sample Code
```
byte[] GetAuthBuffer(string appId, string accountType, string userId, int roomId, uint authBits)
    {
	TimeSpan t = DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, 0);
	double timeStamp = t.TotalSeconds;
	return QAVAuthBuffer.GenAuthBuffer(int.Parse(appId), roomId, userId, int.Parse(accountType), "a495dca2482589e9", (int)timeStamp + 1800, authBits);
}
byte[] authBuffer = this.GetAuthBuffer(str_appId, str_accountType, str_userId, roomId, recvOnly ? IQAVContext.AUTH_BITS_RECV : IQAVContext.AUTH_BITS_ALL);
```

### Enter a Room
A user enters a room with a generated **AuthBuffer** value.
>Note: The microphone and speakers are disabled by default.

It is recommended to use the following two roles:

|Role Name     | Applicable Scenario         |Key Features|
| ------------- |-------------|-------------
| LiveMaster    	|VJ.|Good sound quality and high anti packet loss rate.|
| LiveGuest    	|Audience. |Good sound quality and high anti packet loss rate.|
#### Function Prototype
```
ITMGContext EnterRoom(int relationId, string controlRole, byte[] authBuffer)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| relationId		|int   	|Room number, which is an integer of six or more digits.	|
| controlRole    	|string     	|Role name. Set the parameter based on the requirements.		|
| authBuffer 	|Byte[] 	|The value is used for authentication.						|
#### Sample Code
```
ITMGContext.GetInstance().EnterRoom(roomId, role, authBuffer);
```

### Callback for Entering a Room
The delegate function is used for callback after a user enters a room. The function contains **result** and **error_info**.
#### Function Prototype
```
Delegate function:
public delegate void QAVEnterRoomComplete(int result, string error_info);
Event function:
public abstract event QAVEnterRoomComplete OnEnterRoomCompleteEvent;
```

#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().OnEnterRoomCompleteEvent += new QAVEnterRoomComplete(OnEnterRoomComplete);

Process the event after listening:
void OnEnterRoomComplete(int err, string errInfo)
    {
	if (err != 0) {
	    ShowWarnning (string.Format ("join room failed, err:{0}, errInfo:{1}", err, errInfo));
	    return;
	}else{
	    ShowWarnning (string.Format ("Current voice room ID: {0}, please enter the room from another terminal to chat",roomId ));
    }
}
```

### Check Whether a User Has Entered a Room
The IsRoomEntered function is used to check whether a user has entered a room. The return value of this function is of the bool type.
#### Function Prototype
```
ITMGContext abstract bool IsRoomEntered()
```
#### Sample Code
```
ITMGContext.GetInstance().IsRoomEntered();
```

### Exit from a Room
The ExitRoom function is used to exit from a room.
#### Function Prototype
```
ITMGContext ExitRoom()
```
#### Sample Code
```
ITMGContext.GetInstance().ExitRoom();
```

### Callback for Exiting from a Room
Callback is executed after a user has exited from a room, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVExitRoomComplete();
Event function:
public abstract event QAVExitRoomComplete OnExitRoomCompleteEvent;
```
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().OnExitRoomCompleteEvent += new QAVExitRoomComplete(OnExitRoomComplete);
Process the event after listening:
void OnExitRoomComplete(){
    //Processing after exit from a room
}
```

### Role Setting
Change a flow control role. The resolution of a default role is 640 x 368.
#### Function Prototype
```
ITMGRoom ChangeRole(string role, byte[] authBuffer)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| role    			|string     	|Role.			|
| authBuffer    	|byte[]    	|The parameter must be reset each time.	|

>Note
Changing a flow control role means modifying audio and video encoding parameters. Therefore, the audio and video encoding API needs to be called to reset **AuthBuffer**. For more information, see how to generate **AuthBuffer**.

The following table lists the speech quality corresponding to each role.

|Role Name     | Applicable Scenario         |Key Features|
| ------------- |-------------|-------------
| LiveAnchor    	|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.|Good sound quality and high anti packet loss rate.|
| LiveGuest    	|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.|Good sound quality and high anti packet loss rate.|

#### Sample Code
```
ITMGRoom.GetInstance().GetRoom().ChangeRole(role, authBuffer);
```

### Callback for a Role Setting
Callback is executed after the role setting, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVAudioRouteChangeCallback(int code);
Event function:
public abstract event QAVCallback OnChangeRoleCallback;
```
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().GetAudioCtrl().OnAudioRouteChangeComplete += new QAVAudioRouteChangeCallback(OnAudioRouteChange);
void OnAudioRouteChange(int code){
    //Callback for a role setting
}
```

### Member State Change
The member state change event is triggered to send notifications only when the state of a member changes. To allow real-time member state query, cache the state each time the upper layer receives a notification.

Member event list:

|Event     | Parameter         |Description|
| ------------- |-------------|-------------
| EVENT_ID_ENDPOINT_ENTER				|1	|A member has entered a room.				|
| EVENT_ID_ENDPOINT_EXIT  					|2	|A member has exited from a room.				|
| EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO	|3	|A member has sent a camera video.		|
| EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO  	|4	|A member has stopped sending a camera video.	|
| EVENT_ID_ENDPOINT_HAS_AUDIO  			|5	|An audio has been received from a member.			|
| EVENT_ID_ENDPOINT_NO_AUDIO  			|6	|No audio has been received from a member for two seconds.	|

#### Sample Code
```
Delegate function:
public delegate void QAVEndpointsUpdateInfo(int eventID, int count, [MarshalAs(UnmanagedType.LPArray, SizeParamIndex = 1)]string[] identifierList);
Event function:
public abstract event QAVEndpointsUpdateInfo OnEndpointsUpdateInfoEvent;
```
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().OnEndpointsUpdateInfoEvent += new QAVEndpointsUpdateInfo(OnEndpointsUpdateInfo);
Process the event after listening:
void OnEndpointsUpdateInfo(int eventID, int count, string[] identifierList)
{
    //Maintain member information
}
```

### Turn a Camera On or Off (Push)
The EnableCamera function is used to turn a camera on or off. The function returns **OK** in case of success.
#### Function Prototype
```
ITMGVideoCtrl int EnableCamera(int cameraId, bool enable)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| cameraId	|int     	|Camera ID. Value **0** indicates a front-facing camera and value **1** indicates a rear-facing camera.	|
| enable    	|bool             	|Indicates whether to turn on a camera.							|

#### Sample Code
```
ITMGContext.GetInstance().GetVideoCtrl().EnableCamera (0, true);		//Turn on a camera
ITMGContext.GetInstance().GetVideoCtrl().EnableCamera (0, false);		//Turn off a camera
```

#### Request Picture Data (Pull)
The RequestVideoList function is used to request picture data. The function returns **OK** in case of success. If the operation fails, the function returns **ERR_FAIL**.
#### Function Prototype
```
ITMGContext int RequestVideoList (string[] identifierList)
```
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().OnEndpointsUpdateInfoEvent += new QAVEndpointsUpdateInfo(OnEndpointsUpdateInfo);
Process the event after listening:
void OnEndpointsUpdateInfo(int eventID, int count, string[] identifierList)
{
	//Maintain member information
	if (eventID == ITMGContext.EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO)//A member has sent a camera video
	{
		//Update the member list
		updateVideoIdentifierList (identifierList, true);
		//Obtain the member list and request data
		ITMGContext.GetInstance ().GetRoom ().RequestVideoList (getIdentifierList ());
	｝
}
```

### Cancel Picture Data
The CancelVideoList function is used to cancel picture data. The function returns **OK** in case of success. If the operation fails, the function returns **ERR_FAIL**.
#### Function Prototype
```
ITMGContext int CancelVideoList  (string[] identifierList)
```
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().OnEndpointsUpdateInfoEvent += new QAVEndpointsUpdateInfo(OnEndpointsUpdateInfo);
Process the event after listening:
void OnEndpointsUpdateInfo(int eventID, int count, string[] identifierList)
{
	//Maintain member information
	if (eventID == ITMGContext.EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO) //A member has stopped sending a camera video
	{
		//Update the member list
		updateVideoIdentifierList (identifierList, true);
		//Obtain the member list and stop requesting data
		ITMGContext.GetInstance ().GetRoom ().CancelVideoList (getIdentifierList ());
	｝
}
```

### Video Stream Processing
#### Player
Bind the QAV Video Player code file in the SDK to only one game object in the **Hierarchy** panel. The bound object is created and maintained by developers.
#### Function Prototype
```
public interface ITMGVideoPlayer
{
	void AddRender (QAVVideoRenderer render);
	void removeRender (QAVVideoRenderer render);
}
```
Function description:

|Function     				| Parameter Type         		|Description			|
| ---------------------	| : -------------------: 	|-----------------	|
| AddRender		|QAVVideoRenderer	|Add a renderer.	|
| removeRender  	|QAVVideoRenderer	|Remove a renderer.	|

#### Renderer
To play a user's video image, use a renderer as a parameter and call the AddRender method in ITMGVideoPlayer to add the renderer to a player.
Bind the renderer's code to the UI object in the scene. If NGUI is used, bind the QAVNguiVideoRenderer code file to the UITexture game object. If UGUI is used, bind the QAVRawImageVideoRenderer code file to the RawImage game object.

#### Function Prototype
```
public interface ITMGVideoRenderer
{
	string identifier{ get; set;}
	PlayOrientation playerOrientation{ get; set;}
	bool mirror{ get; set;}
}
```
Attribute description:

|Attribute     				| Type         		|Description			|
| ---------------------	| : ------------: 	|-----------------	|
| identifier    			|string     		|A user's video image ID.	|
| playerOrientation  	|PlayOrientation	|Types of orientation are portrait and landscape. 			|
| mirror  			|bool    			|Indicates whether to adopt mirroring.		|

#### Sample Code
```
void OnEndpointsUpdateInfo(int eventID, int count, string[] identifierList)
{
	//Maintain member information
	if (eventID == ITMGContext.EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO) //A member has stopped sending a camera video
	{
		foreach (string uin in identifierList) {
				GameObject templateRender = GameObject.Find ("render");
				GameObject renderObj = (GameObject)Instantiate (templateRender);
				QAVVideoRenderer render = renderObj.GetComponent<QAVVideoRenderer> ();
				render.identifier = uin;
				if (uin.Equals (UserConfig.GetUserID ())) {
					render.mirror = true;
				} else {
					render.mirror = false;
				}
				if (uin.Equals (UserConfig.GetUserID ())) {
					render.playerOrientation = PlayOrientation.Portrait;
					render.mirror = true;
				} else {
					render.playerOrientation = PlayOrientation.Portrait;
				}
				Debug.LogFormat ("render:{0} playerOrientation:{1}", player, render.playerOrientation);
				player.AddRender (render);
	｝
}
```

### Enable or Disable an Audio Data Blacklist
The blacklist is reset to a new member list each time the SetAudioBlackList function is called to enable the blacklist. The function is called only when audio data to be received needs to be customized. If the function is not called, all audio data in a room is received by default. If the function returns **0**, the call fails.
#### Function Prototype
```
ITMGContext GetRoom UnrequestAudioList(string[] identifierList)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| identifierList    |string[]      |Blacklist.|
#### Sample Code
```
ITMGContext.GetInstance().GetRoom ().UnrequestAudioList (identifierList);
```

### Suspend Acquisition and Playback by the Audio Engine
The PauseAudio function is used to suspend acquisition and playback by the audio engine and is effective only after a user enters a room.
After the EnterRoom function is successfully called, the microphone is occupied and other programs cannot acquire data from the microphone.
Note: Calling of EnableMic(false) cannot release the microphone.
To release a microphone, call the PauseAudio function that can suspend the audio engine. To resume audio acquisition, call the ResumeAudio function.
#### Function Prototype
```
ITMGAudioCtrl abstract int PauseAudio()
```
#### Sample Code
```
ITMGContext.GetInstance ().GetAudioCtrl ().PauseAudio();
```
### Resume Acquisition and Playback by the Audio Engine
The ResumeAudio function is used to resume acquisition and playback by the audio engine and is effective only after a user enters a room.
#### Function Prototype
```
ITMGAudioCtrl abstract int ResumeAudio()
```
#### Sample Code
```
ITMGContext.GetInstance ().GetAudioCtrl ().ResumeAudio();
```

### Enable or Disable a Microphone
The EnableMic function is used to enable or disable a microphone.
>Note: The microphone and speakers are disabled by default when a user enters a room.

#### Function Prototype
```
ITMGAudioCtrl EnableMic(bool isEnabled)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| isEnabled    |boolean     |To enable a microphone, set the input parameter to **true**. To disable a microphone, set the input parameter to **false**.|

#### Sample Code
```
Enable a microphone
ITMGContext.GetInstance().GetAudioCtrl().EnableMic(true);
Disable a microphone
ITMGContext.GetInstance().GetAudioCtrl().EnableMic(false);
```

### Obtain the Status of a Microphone
The GetMicState function is used to obtain the status of a microphone.
#### Function Prototype
```
ITMGAudioCtrl GetMicState()
```
#### Sample Code
```
micToggle.isOn = ITMGContext.GetInstance().GetAudioCtrl().GetMicState() != 0;
```

### Obtain the Real-Time Volume of a Microphone
IQAVAudioCtrl GetMicLevel()
#### Function Prototype
```
ITMGAudioCtrl -(int)GetMicLevel
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioCtrl().GetMicLevel();
```

### Set the Software Volume of a Microphone
The SetMicVolume function is used to set the software volume of a microphone. The **volume** parameter specifies the software volume of a microphone. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.
#### Function Prototype
```
ITMGAudioCtrl SetMicVolume(int volume)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| volume    |int      |Volume, ranging from **0** to **100**.|
#### Sample Code
```
int micVol = (int)(value * 100);
ITMGContext.GetInstance().GetAudioCtrl().SetMicVolume (micVol);
```

### Obtain the Software Volume of a Microphone
The GetMicVolume function is used to obtain the software volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl GetMicVolume()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioCtrl().GetMicVolume();
```

### Enable or Disable Speakers
The EnableSpeaker function is used to enable or disable speakers.
#### Function Prototype
```
ITMGAudioCtrl EnableSpeaker(bool isEnabled)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| isEnabled    |bool        |To enable speakers, set the input parameter to **true**. To disable speakers, set the input parameter to **false**.|
#### Sample Code
```
Enable speakers
ITMGContext.GetInstance().GetAudioCtrl().EnableSpeaker(true);
Disable speakers
ITMGContext.GetInstance().GetAudioCtrl().EnableSpeaker(false);
```

### Obtain the Status of Speakers
The GetSpeakerState function is used to obtain the status of speakers. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl GetSpeakerState()
```

#### Sample Code
```
speakerToggle.isOn = ITMGContext.GetInstance().GetAudioCtrl().GetSpeakerState() != 0;
```

### Obtain the Real-Time Volume of Speakers
The GetSpeakerLevel function is used to obtain the real-time volume of speakers. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl GetSpeakerLevel()
```

#### Sample Code
```
ITMGContext.GetInstance().GetAudioCtrl().GetSpeakerLevel();
```

### Set the Software Volume of Speakers
The SetSpeakerVolume function is used to set the software volume of speakers.
>Note: The **vol** parameter specifies the software volume of speakers. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.

#### Function Prototype
```
ITMGAudioCtrl SetSpeakerVolume(int volume)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| vol    |int        |Volume, ranging from **0** to **100**.|
#### Sample Code
```
int speVol = (int)(value * 100);
ITMGContext.GetInstance().GetAudioCtrl().SetSpeakerVolume(speVol );
```

### Obtain the Software Volume of Speakers
The GetSpeakerVolume function is used to obtain the software volume of speakers. The return value of this function is of the int type.
>Note: The **Level** parameter indicates the real-time volume, while the **Volume** parameter indicates the software volume of speakers. The final volume is calculated as follows: Final volume = Value of Level x Value of Volume%. For example, if the values of **Level** and **Volume** are **100** and **60** respectively, the final volume is 60.

#### Function Prototype
```
ITMGAudioCtrl GetSpeakerVolume()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioCtrl().GetSpeakerVolume();
```

### Start Playing an Accompaniment
The StartAccompany function is used to start playing an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl int StartAccompany(string filePath, bool loopBack, int loopCount, int duckerTimeMs)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    	|string 	|Path for playing an accompaniment.|
| loopBack   	|bool   	|Indicates whether to send a mix. The parameter is generally set to **true**, indicating that other users can also hear an accompaniment.|
| loopCount	|int       	|Number of loops. Value **-1** means an infinite loop.|
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().StartAccompany(filePath,true,loopCount,duckerTimeMs);
```

### Callback for Playing an Accompaniment
Callback is executed after an accompaniment has been played, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVAccompanyFileCompleteHandler(int code, string filepath);
Event function:
public abstract event QAVAccompanyFileCompleteHandler OnAccompanyFileCompleteHandler;
```
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().GetAudioEffectCtrl().OnAccompanyFileCompleteHandler += new QAVAccompanyFileCompleteHandler(OnAccomponyFileCompleteHandler);
Process the event after listening:
void OnAccomponyFileCompleteHandler(int code, string filepath){
    //Callback for playing an accompaniment
}
```

### Stop Playing an Accompaniment
The StopAccompany function is used to stop playing an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl int StopAccompany(int duckerTimeMs)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| duckerTimeMs    |int             |Fading time.|

#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().StopAccompany(duckerTimeMs);
```

### Check Whether the Playback of an Accompaniment Is Complete
The IsAccompanyPlayEnd function is used to check whether the playback of an accompaniment is complete. If yes, the function returns **true**. If no, it returns **false**.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract bool IsAccompanyPlayEnd();
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().IsAccompanyPlayEnd();
```


### Pause an Accompaniment
The PauseAccompany function is used to pause an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int PauseAccompany()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().PauseAccompany();
```

### Resume an Accompaniment
The ResumeAccompany function is used to resume an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int ResumeAccompany()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().ResumeAccompany();
```

### Configure Whether Users Can Hear Accompaniments Played by Themselves
The EnableAccompanyPlay function is used to configure whether users can hear accompaniments played by themselves.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int EnableAccompanyPlay(bool enable)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |bool             |Indicates whether users can hear accompaniments played by themselves.|
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().EnableAccompanyPlay(true);
```

### Configure Whether Other Users Can Hear an Accompaniment
The EnableAccompanyLoopBack function is used to configure whether other users can hear an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int EnableAccompanyLoopBack(bool enable)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |bool             |Indicates whether other users can hear an accompaniment.|

#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().EnableAccompanyLoopBack(true);
```

### Set the Volume of an Accompaniment
The SetAccompanyVolume function is used to set the linear volume of an accompaniment. The default value is **100**. If the return value is greater than **100**, the actual accompaniment volume is higher than the original volume. If the return value is less than **100**, the actual accompaniment volume is lower than the original volume.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int SetAccompanyVolume(int vol)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| vol    |int             |Volume.|

#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().SetAccompanyVolume(vol);
```

### Obtain the Volume of an Accompaniment
The GetAccompanyVolume function is used to obtain the volume of an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int GetAccompanyVolume()
```
#### Sample Code
```
string currentVol = "VOL: " + ITMGContext.GetInstance().GetAudioEffectCtrl().GetAccompanyVolume();
```

### Obtain the Playback Progress of an Accompaniment
The following two functions are used to obtain the playback progress of an accompaniment. Note: Current / Total = Number of current loop times; Current % Total = Playback position of the current loop.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract uint GetAccompanyFileTotalTimeByMs()
ITMGAudioEffectCtrl abstract int GetAccompanyFileCurrentPlayedTimeByMs()
```
#### Sample Code
```
Sstring current = "Current: " + ITMGContext.GetInstance().GetAudioEffectCtrl().GetAccompanyFileCurrentPlayedTimeByMs() + " ms";
string total = "Total: " + ITMGContext.GetInstance().GetAudioEffectCtrl().GetAccompanyFileTotalTimeByMs() + " ms";
```

### Set Playback Progress
The SetAccompanyFileCurrentPlayedTimeByMs function is used to set playback progress.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract uint SetAccompanyFileCurrentPlayedTimeByMs(uint time)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| time    |uint                |Playback progress, in milliseconds.|

#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().SetAccompanyFileCurrentPlayedTimeByMs(time);
```
### Obtain the dB Volume of an Accompaniment
The GetAccompanyVolumeDB function is used to obtain the dB volume of an accompaniment. The default value is **61**. If the return value is greater than **61**, the actual volume is higher than the original volume. If the return value is less than **61**, the actual volume is lower than the original volume.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int GetAccompanyVolumeDB()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().GetAccompanyVolumeDB();
```

### Set the dB Volume of an Accompaniment
The SetAccompanyVolumeDB function is used to set the dB volume of an accompaniment. The default value is **61**. If the return value is greater than **61**, the actual volume is higher than the original volume. If the return value is less than **61**, the actual volume is lower than the original volume.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int SetAccompanyVolumeDB(int dbVol)
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().SetAccompanyVolumeDB(vol);
```

### Obtain the Volume of a Sound Effect
The GetEffectsVolume function is used to obtain the linear volume of a sound effect. The default value is **100**. If the return value is greater than **100**, the actual accompaniment volume is higher than the original volume. If the return value is less than **100**, the actual accompaniment volume is lower than the original volume.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int GetEffectsVolume()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().GetEffectsVolume();
```

### Set the Volume of a Sound Effect
The SetEffectsVolume function is used to set the volume of a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int SetEffectsVolume(int volume)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| volume    |int                    |Volume.|

#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().SetEffectsVolume(volume);
```

### Play a Sound Effect
The PlayEffect function is used to play a sound effect. The **soundId** parameter, which uniquely identifies an independent file, must be managed on the application side.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int PlayEffect(int soundId, string filePath, bool loop = false, double pitch = 1.0f, double pan = 0.0f, double gain = 1.0f)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    	|int        		|Sound effect ID.|
| filePath    	|string		|Sound effect path.|
| loop    		|bool       	|Indicates whether to repeat playback.|
| pitch    	|double		|Reserved field.|
| pan    		|double 	|Reserved field.|
| gain    		|double		|Reserved field.|
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().PlayEffect(soundId,filePath,true,1.0,0,1.0);
```


### Pause a Sound Effect
The PauseEffect function is used to pause a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int PauseEffect(int soundId)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|

#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().PauseEffect(soundId);
```

### Pause All Sound Effects
The PauseAllEffects function is used to pause all sound effects.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int PauseAllEffects()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().PauseAllEffects();
```

### Resume a Sound Effect
The ResumeEffect function is used to resume a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int ResumeEffect(int soundId)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().ResumeEffect(soundId);
```

### Resume All Sound Effects
The ResumeAllEffects function is used to resume all sound effects.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int ResumeAllEffects()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().ResumeAllEffects();
```

### Stop Playing a Sound Effect
The StopEffect function is used to stop playing a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int StopEffect(int soundId)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().StopEffect(soundId);
```

### Stop Playing All Sound Effects
The StopAllEffects function is used to stop playing all sound effects.
#### Function Prototype
```
ITMGAudioEffectCtrl abstract int StopAllEffects()
```
#### Sample Code
```
ITMGContext.GetInstance().GetAudioEffectCtrl().StopAllEffects(soundId);
```

### Obtain Diagnosis Information
The GetQualityTips function is used to obtain information about the quality of real-time voice or video chats. The function is mainly used to check the quality of real-time chats and detect problems. The function can be ignored on the service side.
#### Function Prototype
```
ITMGRoom GetQualityTips()
```
#### Sample Code
```
string tips = ITMGContext.GetInstance().GetRoom().GetQualityTips();
```

## PTT Access
### Initialize PTT Access
Initializing PTT access requires passing **accessToken** to TLS-related functions. For details on the process of obtaining **accessToken** for authentication, see the [GME Access Guide](/document/product/607/10782).
The **Error** parameter is used to pass error information. For example, when **appId** is set to **0** or **privateKey** or **identifier** is left blank, error information indicating that a parameter is incorrectly set is returned.

#### Function Prototype
```
QAVSig GenSig(int appId, string identifier, string privateKey)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| appId    	|int        		|The value is the same as the value of **sdkAppId** on Tencent Cloud Console.			|
| identifier   	|string 		|Identifier that uniquely identifies a user. The setting rule is customized by application developers.	|
| privateKey	|string		|The value is the key provided by Tencent Cloud Console.						|

```
IQAVPTT ApplyAccessToken(string accessToken)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| accessToken    | string|The value is the same as the access token returned by the Gensig function.|

#### Sample Code
```
string GetAccessToken(string appId, string accountType, string userId)
	{
		string key = Key obtained from the Tencent Cloud backend;
		return QAVSig.GenSig(int.Parse(appId), userId, key);
	}

string sig = this.GetAccessToken(appId, accountType, userId);
		if (sig != null) {
			IQAVContext.GetInstance().GetPttCtrl().ApplyAccessToken(sig);
			//Success
		} else {
			//Failure
		}
```

### Specify the Maximum Length of a Voice Message
The SetMaxMessageLength function is used to specify the maximum length of a voice message. The maximum length can be 60 seconds.
#### Function Prototype
```
ITMGPTT int SetMaxMessageLength(int msTime)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| msTime    |int                    |Length of a voice message.|
#### Sample Code
```
ITMGContext.GetInstance().GetPttCtrl().SetMaxMessageLength(60000);
```

### Start Recording
The StartRecording function is used to start recording.
#### Function Prototype
```
ITMGPTT int StartRecording(string filePath)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| fileDir    |string                      |Path for playing a voice file, which can be NULL.|
#### Sample Code
```
string recordPath = Application.persistentDataPath + string.Format ("/{0}.silk", sUid++);
int ret = ITMGContext.GetInstance().GetPttCtrl().StartRecording(recordPath);
```

### Callback for Recording
Callback is executed after recording, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVRecordFileCompleteCallback(int code, string filepath);
Event function:
public abstract event QAVRecordFileCompleteCallback OnRecordFileComplete;
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| code    	|string  		|When **code** is set to **0**, the recording is complete.|
| filepath    	|string 		|Path for storing a recorded file.|

#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().GetPttCtrl().OnRecordFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath){
    //Callback for recording
}
```

### Stop Recording
The StopRecording function is used to stop recording.
#### Function Prototype
```
ITMGPTT int StopRecording()
```
#### Sample Code
```
ITMGContext.GetInstance().GetPttCtrl().StopRecording();
```

### Upload a Voice File
The UploadRecordedFile function is used to upload a voice file.
#### Function Prototype
```
ITMGPTT int UploadRecordedFile (string filePath)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |string                      |Path for uploading a voice file.|
#### Sample Code
```
ITMGContext.GetInstance().GetPttCtrl().UploadRecordedFile(filePath);
```

### Callback for Uploading a Voice File
Callback is executed after a voice file has been uploaded, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVUploadFileCompleteCallback(int code, string filepath, string fileid);
Event function:
public abstract event QAVUploadFileCompleteCallback OnUploadFileComplete;
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| code    	|int   	|When **code** is set to **0**, the recording is complete.|
| filepath    	|string	|Path for storing a recorded file.|
| fileid    	|string 	|URL of a file.|
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().GetPttCtrl().OnUploadFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath, string fileid){
    //Callback for uploading a voice file
}
```

### Download a Voice File
The QAVDownloadFileCompleteCallback function is used to download a voice file.
#### Function Prototype
```
ITMGPTT DownloadRecordedFile (string fileID, string downloadFilePath)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| fileID    			|string  	|URL of a file.|
| downloadFilePath	|string  	|Path for downloading a file.|
#### Sample Code
```
ITMGContext.GetInstance().GetPttCtrl().DownloadRecordedFile(fileId, filePath);
```

### Callback for Downloading a Voice File
Callback is executed after a voice file has been downloaded, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVDownloadFileCompleteCallback(int code, string filepath, string fileid);
Event function:
public abstract event QAVDownloadFileCompleteCallback OnDownloadFileComplete;
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| code    	|int   	|When **code** is set to **0**, the recording is complete.	|
| filepath	|string	|Path for storing a recorded file.			|
| fileid		|string	|URL of a file.			|
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().GetPttCtrl().OnDownloadFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath, string fileid){
    //Callback for downloading a voice file
}
```

### Play a Voice File
The PlayRecordedFile function is used to play a voice file.
#### Function Prototype
```
ITMGPTT PlayRecordedFile (string downloadFilePath)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| downloadFilePath    |string                       |Path for downloading a file|
#### Sample Code
```
ITMGContext.GetInstance().GetPttCtrl().PlayRecordedFile(filePath);
```

### Callback for Playing a Voice File
Callback is executed after a voice file has been played, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVPlayFileCompleteCallback(int code, string filepath);
Event function:
public abstract event QAVPlayFileCompleteCallback OnPlayFileComplete;
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| code    	|int     	|When **code** is set to **0**, the recording is complete.	|
| filepath 	|string 	|Path for storing a recorded file.			|

#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().GetPttCtrl().OnPlayFileComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string filepath){
    //Callback for playing a voice file
}
```

### Stop Playing a Voice File
The StopPlayFile function is used to stop playing a voice file.
#### Function Prototype
```
ITMGPTT int StopRecording()
```

#### Sample Code
```
ITMGContext.GetInstance().GetPttCtrl().StopRecording();
```

### Obtain the Size of a Voice File
The GetFileSize function is used to obtain the size of a voice file.
#### Function Prototype
```
ITMGPTT GetFileSize(string filePath)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |string                      |Path for storing a voice file.|
#### Sample Code
```
int fileSize = ITMGContext.GetInstance().GetPttCtrl().GetFileSize(filepath);
```

### Obtain the Duration of a Voice File
The GetVoiceFileDuration function is used to obtain the duration of a voice file.
#### Function Prototype
```
ITMGPTT int GetVoiceFileDuration(string filePath)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |string                      |Path for storing a voice file.|
#### Sample Code
```
int fileDuration = ITMGContext.GetInstance().GetPttCtrl().GetVoiceFileDuration(filepath);
```


### Convert Specified Speech into Text
The specified speech is converted into text, and the delegate function is used to transfer a message.
#### Function Prototype
```
Delegate function:
public delegate void QAVSpeechToTextCallback(int code, string fileid, string result);
Event function:
public abstract event QAVSpeechToTextCallback OnSpeechToTextComplete;
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| code    	|int 		|When **code** is set to **0**, the recording is complete.	|
| filepath    	|string 	|Path for storing a recorded file.			|
| result    	|string   	|Text generated after conversion.			|
#### Sample Code
```
Listen for an event:
ITMGContext.GetInstance().GetPttCtrl().OnSpeechToTextComplete += mInnerHandler;
Process the event after listening:
void mInnerHandler(int code, string fileid, string result){
    //Callback of a conversion event
}
```
