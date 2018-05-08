Welcome to the Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes access technologies for Unreal Engine development so that Unreal Engine developers can easily debug and access APIs for Tencent Cloud GME.

## SDK Initialization

### Preparation
The **tmg_sdk.h** file is required for access to the GME SDK. The header file is inherited from ITMGDelegate for message transferring and a callback.
#### Sample Code
```
#include "tmg_sdk.h"

class UEDEMO1_API AUEDemoLevelScriptActor : public ALevelScriptActor, public ITMGDelegate
{
public:
...
private:
...
｝
```

### Message Transferring
GME messages are transferred to an application via ITMGDelegate. The message type is specified by **ITMG_MAIN_EVENT_TYPE**. Message data is in JSON string format on the Windows platform. For specific key-value pairs, see the following data list.

#### Sample Code
```
//Function implementation:
//UEDemoLevelScriptActor.h:
class UEDEMO1_API AUEDemoLevelScriptActor : public ALevelScriptActor, public ITMGDelegate
{
public:
	void OnEvent(ITMG_MAIN_EVENT_TYPE eventType, const char* data);
...
｝

//UEDemoLevelScriptActor.cpp:
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType, const char* data){
	//Check **eventType** and process the event message
}
```
#### Message List:

|Message     | Description
| ------------- |-------------|
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    				|Entry into an audio/video room.
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    				|Exit from an audio/video room.
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT			|Disconnection from a room due to network issues or other reasons.
| ITMG_MAIN_EVENT_TYPE_ENABLE_MIC    				|Microphone enabled.
| ITMG_MAIN_EVENT_TYPE_DISABLE_MIC    				|Microphone disabled.
| ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    			|Microphone added.
| ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    			|Microphone lost.
|ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER				|Speaker enabled.
|ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER				|Speaker disabled.
|ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE			|Speaker added.
|ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE		|Speaker lost.
|ITMG_MAIN_EVENT_TYPE_OPEN_CAMERA				|Camera turned on.
|ITMG_MAIN_EVENT_TYPE_CLOSE_CAMERA				|Camera turned off.
|ITMG_MAIN_EVENT_TYPE_REQUEST_VIDEO_LIST			|Whitelist for opening a video.
|ITMG_MAIN_EVENT_TYPE_CANCEL_VIDEO_LIST			|Whitelist for closing a video.
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE				|Role changed.
|ITMG_MAIN_EVNET_TYPE_USER_UPDATE					|Room member updated.
|ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH			|Accompaniment ended.
|ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE		|PTT recorded.
|ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE		|PTT uploaded.
|ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE	|PTT downloaded.
|ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE			|PTT played.
|ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE	|Speech converted into text.

#### Data List

|Message     | Data         | Example|
| ------------- |-------------|------------- |
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    			|result; error_info	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    			|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    	|result; error_info  	|{"error_info":"waiting timeout, please check your network","result":0}
| ITMG_MAIN_EVENT_TYPE_ENABLE_MIC    			|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_DISABLE_MIC    			|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER    		|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER    		|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE	|result; error_info  	|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"Speaker (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":false,"result":0}
| ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE    	|result; error_info  	|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"Speaker (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":false,"result":0}
| ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    		|result; error_info  	|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"Microphone (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":true,"result":0}
| ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    		|result; error_info 	|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"Microphone (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":true,"result":0}
| ITMG_MAIN_EVNET_TYPE_USER_UPDATE    			|user_list;  event_id	|{"event_id":1,"user_list":["0"]}

## Real-Time Voice Access
### Initialization
Relevant information is applied for through Tencent Cloud Console. For more information, see the [GME Access Guide](/document/product/607/10782).
ITMGContext should be obtained before the EnterRoom function is called. The GME SDK is provided as a singleton. All calls start with ITMGContext, and messages are transferred back to an application via ITMGDelegate callbacks. Therefore, this function must be set first.
#### Sample Code
```
 ITMGContextGetInstance()->TMGDelegate(this);
```

The SetAppInfo and SetAppVersion functions are called to set relevant information. The SetAppInfo function contains the **sdkAppId**, **accountType**, and **openID** parameters. The values of **sdkAppId** and **accountType** are obtained from Tencent Cloud Console. The value of **openID** indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers, and the ID must be unique in an application.
#### Function Prototype**
```
ITMGContext virtual void SetAppInfo(const char* sdkAppId,const char* accountType, const char* openId)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| sdkAppId    	|char  	|The value is obtained from Tencent Cloud Console.					|
| accountType    	|char  	|The value is obtained from Tencent Cloud Console.				|
| openID    		|char  	|The parameter is used to identify a user. The value of **openID** is of the Int32 type and must be greater than **10000**.	|
#### Sample Code
```
std::string appid = TCHAR_TO_UTF8(CurrentWidget->editAppID->GetText().ToString().operator*());
std::string accountType = TCHAR_TO_UTF8(CurrentWidget->editAccountType->GetText().ToString().operator*());
std::string userId = TCHAR_TO_UTF8(CurrentWidget->editUserID->GetText().ToString().operator*());
ITMGContextGetInstance()->SetAppInfo(appid.c_str(), accountType.c_str(), userId.c_str());
```

 Unreal Engine's update function Tick must be configured.
>Poll is a function that triggers an SDK callback via the *ITMGDelegate::OnEvent* event. The callback thread is Poll's calling thread.

#### Function Prototype
```
class ITMGContext {
protected:
    virtual ~ITMGContext() {}

public:
	//Destroy TMGSDK, make sure to release SDK after use.
    	virtual void Destroy() = 0;
	//Poll
    	virtual void Poll()= 0;
	//Pause
	virtual int Pause() = 0;
	//Resume
    	virtual int Resume() = 0;
}
```
#### Sample Code
```
//Declaration in the header file
virtual void Tick(float DeltaSeconds);

//Code implementation
void AUEDemoLevelScriptActor::Tick(float DeltaSeconds)
{
ITMGContextGetInstance()->Poll();
}
```

### Set Relevant Information
The SetAppVersion function is used to set version information that is used during log query and debugging, helping with background statistics collection and policy adjustment. No functions are affected if version information is not set.
#### Function Prototype
```
ITMGContext virtual void SetAppVersion(const char* appVersion)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| appVersion    |char  |Version number.|
#### Sample Code
```
ITMGContextGetInstance()->SetAppVersion("1.0");
```
The GetSDKVersion function is used to obtain the SDK version number.
#### Function Prototype
```
ITMGContext virtual const char* GetSDKVersion()
```
#### Sample Code
```
ITMGContextGetInstance()->GetSDKVersion;
```

Set a log level.
#### Function Prototype
```
ITMGContext virtual void SetLogLevel(ITMG_LOG_LEVEL logLevel)
```
ITMG_LOG_LEVEL comparison table

|ITMG_LOG_LEVEL|Description|
| -------------------------------	|----------------------	|
|TMG_LOG_LEVEL_NONE		|Not print logs.			|
|TMG_LOG_LEVEL_ERROR		|Print error logs.		|
|TMG_LOG_LEVEL_INFO		|Print information logs.		|
|TMG_LOG_LEVEL_DEBUG	|Print debug logs.	|
|TMG_LOG_LEVEL_VERBOSE	|Print high frequency logs.		|
#### Sample Code
```
ITMGContextGetInstance()->SetLogLevel(TMG_LOG_LEVEL_NONE);
```

Set a path for printing logs.
#### Function Prototype
```
ITMGContext virtual void SetLogPath(const char* logDir)
```

#### Sample Code
```
cosnt char* logDir = ""//Set a path based on the requirements
ITMGContext* context = ITMGContextGetInstance();
context->SetLogPath(logDir);
```

### Generate Authentication
The value of the **AuthBuffer** parameter is generated for encryption and authentication of relevant functions. For more information about how to obtain values of related parameters and other information, see the [GME AuthBuffer Use Manual](/document/product/607/12218).
>Note: The **AuthBuffer** parameter is required to allow a user to enter a room.

#### Function Prototype
```
QAVSDK_API int QAVSDK_CALL QAVSDK_AuthBuffer_GenAuthBuffer(unsigned int appId, unsigned int authId, const char* account, unsigned int accountType, const char* key, unsigned int expTime, unsigned int privilegeMap, unsigned char* retAuthBuff, unsigned int* buffLenght);
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| appId    		|int   		|The value is the same as the value of **sdkAppId** on Tencent Cloud Console.		|
| authId    		|int  		|Name of the room to be entered.							|
| account  		|char    		|User identifier.								|
| accountType    	|int   		|The value is obtained from Tencent Cloud Console.	|
| key    			|char	    	|The value is the key provided by Tencent Cloud Console.					|
| expTime    		|int   		|Timeout interval for entering a room.						|
| privilegeMap   	|int    		|Permissions.									|
| retAuthBuff   	|char    		|Returned **AuthBuff** value.							|
| buffLenght   	|int    		|Length of the returned **AuthBuff** value.					|

>About permissions
The value **ITMG_AUTH_BITS_ALL** indicates all permissions. It is recommended that this parameter be set to **ITMG_AUTH_BITS_ALL** for real-time users and VJs. The value **ITMG_AUTH_BITS_RECV** indicates downstream permissions. It is recommended that this parameter be set to **ITMG_AUTH_BITS_RECV** for listening- or watching-only audiences. The startAccompany function is unavailable for downstream permissions.

#### Sample Code
```
unsigned int bufferLen = 512;
unsigned char retAuthBuff[512] = {0};
unsigned int expTime =0;

QAVSDK_AuthBuffer_GenAuthBuffer(appId, roomId, "", account, accountType, expTime, ITMG_AUTH_BITS_DEFAULT, retAuthBuff, &bufferLen);
```

### Enter a Room
When a user enters a room with a generated **AuthBuffer** value, the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback.
>Notes:
>1. The microphone and speakers are disabled by default when a user enters a room.
>2. The SetAppInfo function needs to be called to set relevant information before the EnterRoom function.
>For more information about role settings, see the [GME Voice Role Description](/document/product/607/15172).

#### Function Prototype
```
ITMGContext virtual void EnterRoom(int relationId, const char* role, const char* authBuff, int buffLen, int teamId, int gameAudioMode)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| relationId			|int   	|Room number, which is an integer of six or more digits.							|
| role    				|char    	|Role name, which can be set based on the requirements or obtained from an access technician.	|
| authBuffer    		|char    	|Authentication code.												|
| buffLen   			|int   	|Length of an authentication code.											|
| teamId    			|int    	|The default value is **0**.											|
| gameAudioMode   	|int   	|The default value is **0**.											|
#### Sample Code
```
ITMGContextGetInstance()->EnterRoom(roomId, role, (char*)retAuthBuff,bufferLen,atoi(_teamId->getText()),atoi(_audioModeId->getText()));
```

### Callback for Entering a Room
After a user enters a room, the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is sent, which is checked in the OnEvent function.
Code description:
```
//Implementation code
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Process parameters
		TSharedPtr<FJsonObject> JsonObject;
        	TSharedRef<TJsonReader<> > Reader = TJsonReaderFactory<>::Create(FString(UTF8_TO_TCHAR(data)));
        	FJsonSerializer::Deserialize(Reader, JsonObject);
        	int32 result = JsonObject->GetIntegerField(L"result");
        	FString error_info = JsonObject->GetStringField(L"error_info");

        	if (result == 0)
        		{
				//Check the result
			}
			break;
		}
	}
}
```

### Check Whether a User Has Entered a Room
The IsRoomEntered function is used to check whether a user has entered a room. The return value of this function is of the bool type.
#### Function Prototype
```
ITMGContext virtual bool IsRoomEntered()
```
#### Sample Code
```
ITMGContextGetInstance()->IsRoomEntered();
```

### Exit from a Room
The ExitRoom function is used to exit from a room.
#### Function Prototype
```
ITMGContext virtual void ExitRoom()
```
#### Sample Code
```
ITMGContextGetInstance()->ExitRoom();
```

### Callback for Exiting from a Room
After a user exits from a room, the SDK sends the ITMG_MAIN_EVENT_TYPE_EXIT_ROOM message to notify an application of the exit via ITMGDelegate callback.
#### Sample Code
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM:
		{
		//Processing
		break;
		}
	}
}
```

### Member State Change
The member state change event is triggered to send notifications only when the state of a member changes. To allow real-time member state query, cache the state each time the upper layer receives the ITMG_MAIN_EVNET_TYPE_USER_UPDATE event message, in which data contains **event_id** and **user_list**. The value of **event_id** is checked in the OnEvent function.

|event_id     | Description         |Content Maintained on the Application Side|
| ------------- |-------------|-------------|
| ITMG_EVENT_ID_USER_ENTER    				|A member has entered a room.		|Member list.		|
| ITMG_EVENT_ID_USER_EXIT    				|A member has exited from a room.		|Member list.		|
| ITMG_EVENT_ID_USER_HAS_AUDIO    		|A member has enabled a microphone.	|List of chat members.	|
| ITMG_EVENT_ID_USER_NO_AUDIO    		|A member has disabled a microphone.	|List of chat members.	|
|ITMG_EVENT_ID_USER_HAS_CAMERA_VIDEO	|A member has turned on a camera.	|List of chat members.	|
|ITMG_EVENT_ID_USER_NO_CAMERA_VIDEO	|A member has turned off a camera.	|List of chat members.	|

#### Sample Code
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVNET_TYPE_USER_UPDATE:
		{
		//Processing
		//Parse parameters to obtain values of **event_id** and **user_list**.
		    switch (eventID)
 		    {
 		    case ITMG_EVENT_ID_USER_ENTER:
  			    //A member has entered a room
  			    break;
 		    case ITMG_EVENT_ID_USER_EXIT:
  			    //A member has exited from a room
			    break;
		    case ITMG_EVENT_ID_USER_HAS_AUDIO:
			    //A member has enabled a microphone
			    break;
		    case ITMG_EVENT_ID_USER_NO_AUDIO:
			    //A member has disabled a microphone
			    break;
		    case ITMG_EVENT_ID_USER_HAS_CAMERA_VIDEO:
			    //A member has turned on a camera
			    break;
		    case ITMG_EVENT_ID_USER_NO_CAMERA_VIDEO:
			    //A member has turned off a camera
			    break;
		    default:
			    break;
 		    }
		break;
		}
	}
}
```

### Role Setting
Change a flow control role. The ChangeRole method is used to set a user role before a user joins a channel. The user is allowed to change the role after the user joins a channel.
The following six roles are automatically established by default: esports, Rhost, Raudience, Werewolf, host, and audience. For more information about role descriptions, see the [GME Voice Role Description](/document/product/607/15172).
#### Function Prototype
```
ITMGRoom virtual void ChangeRole(const char* role, const unsigned char* authBuff, int authBuffLenght)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| role    				|char     	|Role.			|
| authBuffer    		|char    	|The parameter must be reset each time.	|
| authBuffLenght	|int    	|Length of an authentication code.			|
>Note
Changing a flow control role means modifying audio and video encoding parameters. Therefore, the audio and video encoding API needs to be called to reset **AuthBuffer**. For more information, see how to generate **AuthBuffer**.


The following table lists the speech quality corresponding to each role.

|Role Name     | Applicable Scenario         |Key Features|
| ------------- |-------------|-------------
| esports    		|MOBA, competitive, and shooting games.     								|Ordinary sound quality and ultra-low latency.	|
| Rhost    			|Commander mode of MMORPGs. Only a commander can join broadcasting.     			|High fluency and low latency.		|
| Raudience	|Commander mode of MMORPGs. Only a commander can join broadcasting.     			|High fluency and low latency.		|
| Werewolf 	|Werewolf, casual games, and other games.										|Good sound quality and high anti packet loss rate.	|
| host    			|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.	|Good sound quality and high anti packet loss rate.	|
| audience  	|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.	|Good sound quality and high anti packet loss rate.	|

#### Sample Code
```
ITMGContextGetInstance()->GetRoom()->ChangeRole(role,authBuff,authBuffLenght);
```

### Callback for a Role Setting
After a role setting, the ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE event message is sent as a callback, which is checked in the OnEvent function.
#### Sample Code
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	    	}
		...
            case ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE:
		{
		//Processing
		break;
		}
	}
}
```

### Obtain Diagnosis Information
The GetQualityTips function is used to obtain information about the quality of real-time voice or video chats. The function is mainly used to check the quality of real-time chats and detect problems. The function can be ignored on the service side.
#### Function Prototype
```
ITMGRoom virtual const char* GetQualityTips()
```
#### Sample Code
```
ITMGContextGetInstance()->GetRoom()->GetQualityTips();
```

### Obtain the Number of Microphones
The GetMicListCount function is used to obtain the number of microphones.
>Note: The function needs to be called before microphones are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicListCount()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicListCount();
```

### Enumerate Microphones
The GetMicList function is used to enumerate microphones. The number of microphones must be obtained in advance.
>Note: The function needs to be called before microphones are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicList(TMGAudioDeviceInfo* ppDeviceInfoList, int nCount)

class TMGAudioDeviceInfo
{
public:
	const char* pDeviceID;
	const char* pDeviceName;
};
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| ppDeviceInfoList    	|TMGAudioDeviceInfo   	|Device list.				|
| nCount    			|int     					|Obtained number of microphones.	|
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicList(ppDeviceInfoList,nCount);
```

### Obtain the Number of Speakers
The GetSpeakerListCount function is used to obtain the number of speakers.
>Note: The function needs to be called before speakers are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerListCount()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerListCount();
```

### Enumerate Speakers
The GetSpeakerList function is used to enumerate speakers. The number of speakers must be obtained in advance.
>Note: The function needs to be called before speakers are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerList(TMGAudioDeviceInfo* ppDeviceInfoList, int nCount)

class TMGAudioDeviceInfo
{
public:
	const char* pDeviceID;
	const char* pDeviceName;
};
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| ppDeviceInfoList    	|TMGAudioDeviceInfo    	|Device list.				|
| nCount   			|int     					|Obtained number of speakers.	|

#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerList(ppDeviceInfoList,nCount);
```

### Search for Microphones
The SelectMic function is used to search for microphones.
#### Function Prototype
```
ITMGAudioCtrl virtual int SelectMic(const char* pMicID)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| pMicID    |char     |Microphone ID.|
#### Sample Code
```
const char* pMicID ="1";
ITMGContextGetInstance()->GetAudioCtrl()->SelectMic(pMicID);
```

### Enable or Disable a Microphone
The EnableMic function is used to enable or disable a microphone.
>Note: The microphone and speakers are disabled by default when a user enters a room.

#### Function Prototype
```
ITMGAudioCtrl virtual void EnableMic(bool bEnabled)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| bEnabled    |bool     |To enable a microphone, set the input parameter to **true**. To disable a microphone, set the input parameter to **false**.		|
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableMic(true);
ITMGContextGetInstance()->GetAudioCtrl()->EnableMic(false);
```

### Callback of a Microphone Event
The OnEvent function is used for callback of a microphone event. The SDK notifies an application of microphone invocation via the callback. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_MIC or ITMG_MAIN_EVENT_TYPE_DISABLE_MIC, which is checked in the OnEvent function.

#### Sample Code
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	        }
		...
            	case ITMG_MAIN_EVENT_TYPE_ENABLE_MIC:
		{
		//Processing
		break;
		}
		case ITMG_MAIN_EVENT_TYPE_DISABLE_MIC:
		{
		//Processing
		break;
		}
	}
}
```

### Obtain the Status of a Microphone
The GetMicState function is used to obtain the status of a microphone.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicState()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicState();
```

### Obtain the Real-Time Volume of a Microphone
The GetMicLevel function is used to obtain the real-time volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicLevel()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicLevel();
```

### Set the Software Volume of a Microphone
The SetMicVolume function is used to set the software volume of a microphone. The **vol** parameter specifies the software volume of a microphone. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.
#### Function Prototype
```
ITMGAudioCtrl virtual void SetMicVolume(int vol)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| vol    |int      |Volume, ranging from **0** to **100**.|
#### Sample Code
```
int vol = 100;
ITMGContextGetInstance()->GetAudioCtrl()->SetMicVolume(vol);
```

### Obtain the Software Volume of a Microphone
The GetMicVolume function is used to obtain the software volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicVolume()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicVolume();
```
### Search for Speakers
The SelectSpeaker function is used to search for speakers.
#### Function Prototype
```
ITMGAudioCtrl virtual int SelectSpeaker(const char* pSpeakerID)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| pSpeakerID    |char     |Speaker ID.|
#### Sample Code
```
const char* pSpeakerID ="1";
ITMGContextGetInstance()->GetAudioCtrl()->SelectSpeaker(pSpeakerID);
```
### Enable or Disable Speakers
The EnableSpeaker function is used to enable or disable speakers.
#### Function Prototype
```
ITMGAudioCtrl virtual void EnableSpeaker(bool enabled)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable   		|bool       	|To enable speakers, set the input parameter to **true**. To disable speakers, set the input parameter to **false**.	|
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableSpeaker(true);
ITMGContextGetInstance()->GetAudioCtrl()->EnableSpeaker(false);
```

### Callback of a Speaker Event
The OnEvent function is used for callback of a speaker event. The SDK notifies an application of speaker invocation via the callback. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER or ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER.
#### Sample Code
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	    	}
		...
        	case ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER:
		{
		//Processing
		break;
		}
 		case ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER:
		{
		//Processing
		break;
		}
	}
}
```

### Obtain the Status of Speakers
The GetSpeakerState function is used to obtain the status of speakers. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerState()
```

#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerState();
```

### Obtain the Real-Time Volume of Speakers
The GetSpeakerLevel function is used to obtain the real-time volume of speakers. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerLevel()
```

#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerLevel();
```

### Set the Software Volume of Speakers
The SetSpeakerVolume function is used to set the software volume of speakers.
>Note: The **vol** parameter specifies the software volume of speakers. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.

#### Function Prototype
```
ITMGAudioCtrl virtual void SetSpeakerVolume(int vol)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| vol    |int        |Volume, ranging from **0** to **100**.|
#### Sample Code
```
int vol = 100;
ITMGContextGetInstance()->GetAudioCtrl()->SetSpeakerVolume(vol);
```

### Obtain the Software Volume of Speakers
The GetSpeakerVolume function is used to obtain the software volume of speakers. The return value of this function is of the int type.
>Note: The **Level** parameter indicates the real-time volume, while the **Volume** parameter indicates the software volume of speakers. The final volume is calculated as follows: Final volume = Value of Level x Value of Volume%. For example, if the values of **Level** and **Volume** are **100** and **60** respectively, the final volume is 60.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerVolume()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerVolume();
```

### Enable In-Ear Monitoring
The EnableLoopBack function is used to enable in-ear monitoring.
#### Function Prototype
```
ITMGAudioCtrl virtual int EnableLoopBack(bool enable)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------|
| enable    |bool         |Indicates whether to enable in-ear monitoring.|

#### Sample Code
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableLoopBack(true);
ITMGContextGetInstance()->GetAudioCtrl()->EnableLoopBack(false);
```

## Sound Effect Access
### Start Playing an Accompaniment
The StartAccompany function is used to start playing an accompaniment.
>Notes:
1. Calling the API will reset the volume.
2. The API is unavailable for downstream please enter the room from another terminal to chat.

#### Function Prototype
```
ITMGAudioEffectCtrl virtual void StartAccompany(const char* filePath, bool loopBack, int loopCount, int msTime)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    	|char	|Path for playing an accompaniment.											|
| loopBack    	|bool          	|Indicates whether to send a mix. The parameter is generally set to **true**, indicating that other users can also hear an accompaniment.	|
| loopCount	|int 		|Number of loops. Value **-1** means an infinite loop.							|
| msTime	|int   	|Delay time.												|
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StartAccompany(filePath,true,-1,0);
```

### Callback for Playing an Accompaniment
After the playback of an accompaniment, the ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH event message is sent and the OnEvent function is called to check the message.
#### Sample Code
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	   	}
		...
        case ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH:
		{
		//Processing
		break;
		}
	}
}
```

### Stop Playing an Accompaniment
The StopAccompany function is used to stop playing an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int StopAccompany(int duckerTime)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| duckerTime	|int             |Fading time.|

#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopAccompany(0);
```

### Check Whether the Playback of an Accompaniment Is Complete
The IsAccompanyPlayEnd function is used to check whether the playback of an accompaniment is complete. If yes, the function returns **true**. If no, it returns **false**.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual bool IsAccompanyPlayEnd()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->IsAccompanyPlayEnd();
```

### Pause an Accompaniment
The PauseAccompany function is used to pause an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int PauseAccompany()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseAccompany();
```

### Resume an Accompaniment
The ResumeAccompany function is used to resume an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int ResumeAccompany()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAccompany();
```

### Configure Whether Users Can Hear Accompaniments Played by Themselves
The EnableAccompanyPlay function is used to configure whether users can hear accompaniments played by themselves.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int EnableAccompanyPlay(bool enable)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |bool             |Indicates whether users can hear accompaniments played by themselves.|
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyPlay(false);
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyPlay(true);
```

### Configure Whether Other Users Can Hear an Accompaniment
The EnableAccompanyLoopBack function is used to configure whether other users can hear an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int EnableAccompanyLoopBack(bool enable)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |bool             |Indicates whether other users can hear an accompaniment.|

#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyLoopBack(false);
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyLoopBack(true);
```

### Set the Volume of an Accompaniment
The SetAccompanyVolume function is used to set the linear volume of an accompaniment. The default value is **100**. If the return value is greater than **100**, the accompaniment volume increases. If the return value is less than **100**, the accompaniment volume attenuates.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int SetAccompanyVolume(int vol)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| vol    |int             |Volume.|

#### Sample Code
```
int vol=100;
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetAccompanyVolume(vol);
```

### Obtain the Volume of an Accompaniment
The GetAccompanyVolume function is used to obtain the volume of an accompaniment.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int GetAccompanyVolume()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyVolume();
```

### Obtain the Playback Progress of an Accompaniment
The following two functions are used to obtain the playback progress of an accompaniment. Note: Current / Total = Number of current loop times; Current % Total = Playback position of the current loop.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int GetAccompanyFileTotalTimeByMs()
ITMGAudioEffectCtrl virtual int GetAccompanyFileCurrentPlayedTimeByMs()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyFileTotalTimeByMs();
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyFileCurrentPlayedTimeByMs();
```

### Set Playback Progress
The SetAccompanyFileCurrentPlayedTimeByMs function is used to set playback progress.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int SetAccompanyFileCurrentPlayedTimeByMs(unsigned int time)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| time    |int                |Playback progress, in milliseconds.|

#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetAccompanyFileCurrentPlayedTimeByMs(time);
```

### Obtain the Volume of a Sound Effect
The GetEffectsVolume function is used to obtain the linear volume of a sound effect. The default value is **100**. If the return value is greater than **100**, the accompaniment volume increases. If the return value is less than **100**, the accompaniment volume attenuates.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int GetEffectsVolume()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetEffectsVolume();
```

### Set the Volume of a Sound Effect
The SetEffectsVolume function is used to set the volume of a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int SetEffectsVolume(int volume)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| volume    |int                    |Volume.|

#### Sample Code
```
int volume=1;
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetEffectsVolume(volume);
```

### Play a Sound Effect
The PlayEffect function is used to play a sound effect. The **soundId** parameter, which uniquely identifies an independent file, must be managed on the application side.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int PlayEffect(int soundId,  const char* filePath, bool loop, double pitch, double pan, double gain)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId  	|int        	|Sound effect ID.													|
| filePath    	|char    	|Sound effect path.												|
| loop    		|bool  	|Indicates whether to repeat playback.											|
| pitch    	|double	|Playback frequency. The default value is **1.0**. A smaller value means a slower, longer playback.		|
| pan    		|double	|Sound channel. The value ranges from **-1.0** to **1.0**. Value **-1.0** indicates that only the left sound channel is enabled.	|
| gain    		|double	|Acoustic gain, ranging from **0.0** to **1.0**. The default value is **1.0**.			|
#### Sample Code
```
double pitch = 1.0;
double pan = 0.0;
double gain = 0.0;
ITMGContextGetInstance()->GetAudioEffectCtrl()->PlayEffect(soundId,filepath,true,pitch,pan,gain);
```

### Pause a Sound Effect
The PauseEffect function is used to pause a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int PauseEffect(int soundId)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|

#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseEffect(soundId);
```

### Pause All Sound Effects
The PauseAllEffects function is used to pause all sound effects.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int PauseAllEffects()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseAllEffects();
```

### Resume a Sound Effect
The ResumeEffect function is used to resume a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int ResumeEffect(int soundId)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeEffect(soundId);
```

### Resume All Sound Effects
The ResumeAllEffects function is used to resume all sound effects.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int ResumeAllEffects()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAllEffects();
```

### Stop Playing a Sound Effect
The StopEffect function is used to stop playing a sound effect.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int StopEffect(int soundId)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopEffect(soundId);
```

### Stop Playing All Sound Effects
The StopAllEffects function is used to stop playing all sound effects.
#### Function Prototype
```
ITMGAudioEffectCtrl virtual int StopAllEffects()
```
#### Sample Code
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopAllEffects();
```

## PTT Access
### Initialize PTT Access
Initializing PTT access requires passing **accessToken** to TLS-related functions. For details on the process of obtaining **accessToken** for authentication, see the [GME Access Guide](/document/product/607/10782).
#### Function Prototype
```
QAVSDK_API int QAVSDK_CALL QAVSDK_SIG_GenSig(unsigned int appId,const char* uin,const char* privateKey,char* retSigBuff,unsigned int buffLenght);
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| appId  		|int   		|The value is the same as the value of **sdkAppId** on Tencent Cloud Console.				|
| uin    		|char		|Identifier that uniquely identifies a user. The setting rule is customized by application developers.		|
| privateKey	|char 		|The value is the key provided by Tencent Cloud Console.							|
| retSigBuff 	|char   		|Returned **sig** value.										|
| buffLenght	|int   		|Length of the returned **sig** value.									|

```
ITMGPTT virtual int ApplyAccessToken(const char* accessToken)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| accessToken    |char                       |The value is the same as the access token returned by the QAVSDK_CALL QAVSDK_SIG_GenSig function.|
#### Sample Code
```
char openID = 10000;
int buffLength = 1024;
char* sigBuff = new char[buffLength];
const char* privateKey  = @"Private key on the official website";

int retCode = QAVSDK_SIG_GenSig(atoi(SDKAPPID3RD),openID,privateKey,sigBuff,buffLength);
ITMGContextGetInstance()->GetPTT()->ApplyAccessToken(sigBuff);
```

### Specify the Maximum Length of a Voice Message
The SetMaxMessageLength function is used to specify the maximum length of a voice message. The maximum length can be 60 seconds.
#### Function Prototype
```
ITMGPTT virtual void SetMaxMessageLength(int msTime)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| msTime    |int                    |Length of a voice message.|
#### Sample Code
```
int msTime = 10;
ITMGContextGetInstance()->GetPTT()->SetMaxMessageLength(msTime);
```

### Start Recording
The StartRecording function is used to start recording.
#### Function Prototype
```
ITMGPTT virtual void StartRecording(const char* fileDir)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| fileDir    |char                     |Path for playing a voice file, which can be NULL.|
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->SetMaxMessageLength(fileDir);
```

### Callback for Starting Recording
After recording, the ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLET event message is sent and the OnEvent function is called to check the message.

#### Sample Code
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE:
		{
		//Processing
		break;
		}
	}
}

```

### Stop Recording
The StopRecording function is used to stop recording.
#### Function Prototype
```
ITMGPTT virtual int StopRecording()
```
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->StopRecording();
```

### Cancel Recording
The CancelRecording function is used to cancel recording.
#### Function Prototype
```
ITMGPTT virtual int CancelRecording()
```
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->CancelRecording();
```

### Upload a Voice File
The UploadRecordedFile function is used to upload a voice file.
#### Function Prototype
```
ITMGPTT virtual void UploadRecordedFile(const char* filePath)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |char                      |Path for uploading a voice file.|
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->UploadRecordedFile(filePath);
```

### Callback for Uploading a Voice File
After a voice file is uploaded, the ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE event message is sent, which is checked in the OnEvent function.
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE:
		{
		//Processing
		break;
		}
	}
}
```

### Download a Voice File
The QAVDownloadFileCompleteCallback function is used to download a voice file.
#### Function Prototype
```
ITMGPTT virtual void DownloadRecordedFile(const char* fileId,const char* filePath)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| fileId  		|char  	|URL of a file.	|
| filePath 	|char 	|Path for downloading a file.	|
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->DownloadRecordedFile(fileID,filePath);
```

### Callback for Downloading a Voice File
After a voice file is downloaded, the ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE event message is sent, which is checked in the OnEvent function.
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE:
		{
		//Processing
		break;
		}
	}
}
```

### Play a Voice File
The PlayRecordedFile function is used to play a voice file.
#### Function Prototype
```
ITMGPTT virtual void PlayRecordedFile(const char* filePath)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |char                      |Path for storing a file.|
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->PlayRecordedFile(filePath);
```

### Callback for Playing a Voice File
As a callback for playing a voice file, the ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE event message is sent, which is checked in the OnEvent function.
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE:
		{
		//Processing
		break;
		}
	}
}
```

### Stop Playing a Voice File
The StopPlayFile function is used to stop playing a voice file.
#### Function Prototype
```
ITMGPTT virtual int StopPlayFile()
```
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->StopPlayFile();
```
### Obtain the Size of a Voice File
The GetFileSize function is used to obtain the size of a voice file.
#### Function Prototype
```
ITMGPTT virtual int GetFileSize(const char* filePath)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |char                     |Path for storing a voice file.|
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->GetFileSize(filePath);
```

### Obtain the Duration of a Voice File
The GetVoiceFileDuration function is used to obtain the duration of a voice file.
#### Function Prototype
```
ITMGPTT virtual void SpeechToText(const char* fileID)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| fileID    |char                     |Path for storing a voice file.|
#### Sample Code
```
ITMGContextGetInstance()->GetPTT()->SpeechToText(fileID);
```

### Convert Specified Speech into Text
As a callback for converting specified speech into text, the ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE event message is sent, which is checked in the OnEvent function.
```
void AUEDemoLevelScriptActor::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//Processing
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE:
		{
		//Processing
		break;
		}
	}
}
```
