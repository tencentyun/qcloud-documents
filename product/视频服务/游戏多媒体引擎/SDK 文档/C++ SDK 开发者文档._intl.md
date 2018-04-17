Welcome to the Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes access technologies for C++ development so that C++ developers can easily debug and access APIs for Tencent Cloud GME.

## SDK Initialization
### Get a Singleton
The GME SDK is provided as a singleton. All calls start with ITMGContext, and messages are transferred back to an application via ITMGDelegate callbacks. Therefore, this function must be set first.
#### Function Prototype
```
ITMGContext virtual void TMGDelegate(ITMGDelegate* delegate)
```
#### Sample Code
```
ITMGContext* m_pTmgContext;
m_pTmgContext = ITMGContextGetInstance();
```

### Message Transferring
GME messages are transferred to an application via ITMGDelegate. The message type is specified by **ITMG_MAIN_EVENT_TYPE**. Message data is in JSON string format on the Windows platform. For specific key-value pairs, see the following data list.
#### Function Prototype
```
 ITMGDelegate virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
```
#### Sample Code
```
//Function implementation:
class Callback : public ITMGDelegate
{
	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
	{
  		switch(eventType)
  		{
   			//Check the message type and process the message
  		}
 	}
}

Callback*  p = new Callback ();
m_pTmgContext->TMGDelegate(p);
```
#### Message List:

|Message     | Description
| ------------- |-------------|
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		|Entry into an audio/video room.
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		|Exit from an audio/video room.
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT	|Disconnection from a room due to network issues or other reasons.
| ITMG_MAIN_EVENT_TYPE_ENABLE_MIC    		|Microphone enabled.
| ITMG_MAIN_EVENT_TYPE_DISABLE_MIC    		|Microphone disabled.
|ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER		|Speaker enabled.
|ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER		|Speaker disabled.
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE		|Role changed.
|ITMG_MAIN_EVNET_TYPE_USER_UPDATE			|Room member updated.

##### Data List

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
### Set Relevant Information
Relevant information is applied for through Tencent Cloud Console. For more information, see the [GME Access Guide](/document/product/607/10782).
>The SetAppInfo and SetAppVersion functions need to be called to set relevant information before the EnterRoom function.

The SetAppInfo function contains the **sdkAppId**, **accountType**, and **openID** parameters. The values of **sdkAppId** and **accountType** are obtained from Tencent Cloud Console. The value of **openID** indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers, and the ID must be unique in an application. For **openID** settings, see the authentication document.
#### Function Prototype
```
ITMGContext virtual void SetAppInfo(const char* sdkAppId,const char* accountType, const char* openId)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| sdkAppId    	|char  	|The value is obtained from Tencent Cloud Console.		|
| accountType    |char  	|The value is obtained from Tencent Cloud Console.	|
| openID    		|char  	|The value of **openID** is of the Int32 type and must be greater than **10000**.	|
#### Sample Code
```
ITMGContext* m_pTmgContext;
m_pTmgContext->SetAppInfo(strAppid, strAccountType, strUserID);
```

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
ITMGContext* m_pTmgContext;
m_pTmgContext->SetAppVersion("Test_demo_1.0");
```
The GetSDKVersion function is used to obtain the SDK version number.
#### Function Prototype
```
ITMGContext virtual const char* GetSDKVersion()
```
#### Sample Code
```
ITMGContext* m_pTmgContext;
m_pTmgContext->GetSDKVersion;
```
Then, the value of **AuthBuffer** is generated for encryption and authentication of relevant functions. For more information about how to obtain relevant parameters and other information, see the authentication document.
>Note: The **AuthBuffer** parameter is required to allow a user to enter a room.

### Enter a Room
When a user enters a room with a generated **AuthBuffer** value, the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback.
>Notes: 
>- The microphone and speakers are disabled by default when a user enters a room.
>- The SetAppInfo and SetAppVersion functions need to be called to set relevant information before the EnterRoom function.
For more information about role settings, see the [GME Voice Role Description](/document/product/607/15172).

#### Function Prototype
```
ITMGContext virtual void EnterRoom(int relationId, const char* role, const char* authBuff,int buffLen)
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| relationId		|int   	|Room number, which is an integer of six or more digits.							|
| role    			|char    	|Role name, which can be set based on the requirements or obtained from an access technician.	|
| authBuffer    	|char    	|Authentication code.												|
| buffLen   		|int   	|Length of an authentication code.											|
#### Sample Code
```
m_pTmgContext->EnterRoom(nRoomID, strUserRole, strAuthBuffer, nLength);
```

### Callback for Entering a Room
After a user enters a room, the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is sent, which is checked in the OnEvent function.
Code description:
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //Enter a room
		    break;
	        }
		...
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
m_pTmgContext->IsRoomEntered();
```

### Exit from a Room
The ExitRoom function is used to exit from a room.
#### Function Prototype
```
ITMGContext virtual void ExitRoom()
```
#### Sample Code
```
m_pTmgContext->ExitRoom();
```

### Callback for Exiting from a Room
After a user exits from a room, the SDK sends the ITMG_MAIN_EVENT_TYPE_EXIT_ROOM message to notify an application of the exit via ITMGDelegate callback.
#### Sample Code
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //Enter a room
		    break;
	        }
		...
		case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM:
		{
		    //Exit from the room
		    break;
	        }
            }
        }
}
```

### Member State Change
The member state change event is triggered to send notifications only when the state of a member changes. To allow real-time member state query, cache the state each time the upper layer receives the ITMG_MAIN_EVNET_TYPE_USER_UPDATE event message, in which data contains **event_id** and **user_list**. The value of **event_id** is checked in the OnEvent function.

|event_id     | Description         |Content Maintained on the Application Side|
| ------------- |-------------|-------------|
| ITMG_EVENT_ID_USER_ENTER    			|A member has entered a room.		|Member list.		|
| ITMG_EVENT_ID_USER_EXIT    			|A member has exited from a room.		|Member list.		|
| ITMG_EVENT_ID_USER_HAS_AUDIO    	|A member has enabled a microphone.	|List of chat members.	|
| ITMG_EVENT_ID_USER_NO_AUDIO    	|A member has disabled a microphone.	|List of chat members.	|

#### Sample Code
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		...
		case ITMG_MAIN_EVNET_TYPE_USER_UPDATE:
		//Role status change
		{
		    //Parse JSON parameters to obtain values of **event_id** and **user_list**.
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
		    default:
			    break;
 		    }
		    break;
	        }
        }
    }
}
```

### Obtain the Number of Microphones
The GetMicListCount function is used to obtain the number of microphones.
>Note: The function needs to be called before microphones are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicListCount(int& nCount)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| nCount    |int     |Number of microphones. The destination address for receiving the value must be specified.|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->GetMicListCount(nCount);
```

### Enumerate Microphones
The GetMicList function is used to enumerate microphones. The number of microphones must be obtained in advance.
>Note: The function needs to be called before microphones are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicList(TMGAudioDeviceInfo* ppDeviceInfoList, int& nCount)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| ppDeviceInfoList    |TMGAudioDeviceInfo     |Device list.|
| nCount    |int     |Obtained number of microphones.|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicList(ppDeviceInfoList,nCount);
```

### Obtain the Number of Speakers
The GetSpeakerListCount function is used to obtain the number of speakers.
>Note: The function needs to be called before speakers are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerListCount(int& nCount)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| nCount    |int     |Number of speakers. The destination address for receiving the value must be specified.|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerListCount(nCount);
```

### Enumerate Speakers
The GetSpeakerList function is used to enumerate speakers. The number of speakers must be obtained in advance.
>Note: The function needs to be called before speakers are enabled.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerList(TMGAudioDeviceInfo* ppDeviceInfoList, int& nCount)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| ppDeviceInfoList    |TMGAudioDeviceInfo     |Device list.|
| nCount    |int     |Obtained number of speakers.|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerList(ppDeviceInfoList,nCount);
```

### Enable or Disable a Microphone
The EnableMic function is used to enable or disable a microphone.
>Note: The microphone and speakers are disabled by default when a user enters a room.

#### Function Prototype
```
ITMGAudioCtrl virtual int EnableMic(bool bEnabled, const char* pMicId)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |bool     |To enable a microphone, set the input parameter to **true**. To disable a microphone, set the input parameter to **false**.		|
| pMicId    |char     |Microphone ID.																	|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableMic(true,pMicId);
pTmgAudioCtrl->EnableMic(false,pMicId);
```

### Callback of a Microphone Event
The OnEvent function is used for callback of a microphone event. The SDK notifies an application of microphone invocation via the callback. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_MIC or ITMG_MAIN_EVENT_TYPE_DISABLE_MIC, which is checked in the OnEvent function.

#### Sample Code
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //Enter a room
		    break;
	        }
		...
		case ITMG_MAIN_EVENT_TYPE_ENABLE_MIC:
		{
		    //Callback for enabling a microphone
		    break;
	        }
		case ITMG_MAIN_EVENT_TYPE_DISABLE_MIC:
		{
		    //Callback for disabling a microphone
		    break;
	        }
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
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicState();
```

### Obtain the Real-Time Volume of a Microphone
The GetMicLevel function is used to obtain the real-time volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicLevel()
```
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicLevel();
```

### Set the Software Volume of a Microphone
The SetMicVolume function is used to set the software volume of a microphone. The **volume** parameter specifies the software volume of a microphone. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.
#### Function Prototype
```
ITMGAudioCtrl virtual void SetMicVolume(int volume)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| volume    |int      |Volume, ranging from **0** to **100**.|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->SetMicVolume(volume);
```

### Obtain the Software Volume of a Microphone
The GetMicVolume function is used to obtain the software volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetMicVolume()
```
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicVolume();
```

### Enable or Disable Speakers
The EnableSpeaker function is used to enable or disable speakers.
#### Function Prototype
```
ITMGAudioCtrl virtual int EnableSpeaker(bool bEnabled, const char* pSpeakerID)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable   		|bool       	|To enable speakers, set the input parameter to **true**. To disable speakers, set the input parameter to **false**.	|
| pSpeakerID    	|char      	|Speaker ID.																|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableSpeaker(true,pSpeakerID);
pTmgAudioCtrl->EnableSpeaker(false,pSpeakerID);
```

### Callback of a Speaker Event
The OnEvent function is used for callback of a speaker event. The SDK notifies an application of speaker invocation via the callback. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER or ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER.
#### Sample Code
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //Enter a room
		    break;
	        }
		...
		case ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER:
		{
		    //Callback for enabling speakers
		    break;
	        }
		case ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER:
		{
		    //Callback for disabling speakers
		    break;
	        }
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
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerState();
```

### Obtain the Real-Time Volume of Speakers
The GetSpeakerLevel function is used to obtain the real-time volume of speakers. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerLevel()
```

#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerLevel();
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
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->SetSpeakerVolume(vol);
```

### Obtain the Software Volume of Speakers
The GetSpeakerVolume function is used to obtain the software volume of speakers. The return value of this function is of the int type.
>Note: The **Level** parameter indicates the real-time volume, while the **Volume** parameter indicates the software volume of speakers. The final volume is calculated as follows: Final volume = Value of Level x Value of Volume% For example, if the values of **Level** and **Volme** are **100** and **60** respectively, the final volume is 60.

#### Function Prototype
```
ITMGAudioCtrl virtual int GetSpeakerVolume()
```
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->GetSpeakerVolume();
```

### Enable In-Ear Monitoring
The EnableLoopBack function is used to enable in-ear monitoring.
#### Function Prototype
```
ITMGAudioCtrl virtual int EnableLoopBack(bool enable)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |bool         |Indicates whether to enable in-ear monitoring.|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableLoopBack(true);
pTmgAudioCtrl->EnableLoopBack(false);
```

### Obtain Diagnosis Information
The GetQualityTips function is used to obtain information about the quality of real-time voice or video chats. The function is mainly used to check the quality of real-time chats and detect problems.
#### Function Prototype
```
ITMGRoom virtual const char* GetQualityTips()
```

#### Sample Code
```
m_pTmgContext.GetRoom().GetQualityTips();
```

## 3D Sound Effect Access
### Enable or Disable the 3D Sound Effect
The EnableSpatializer function is used to enable or disable the 3D sound effect. The return value of this function is of the int type.
#### Function Prototype
```
ITMGAudioCtrl virtual int EnableSpatializer(bool bEnabled)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| bEnabled    |bool         |Indicates whether to enable the 3D sound effect.|
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableSpatializer(true);
pTmgAudioCtrl->EnableSpatializer(false);
```

### Obtain the Current 3D Sound Effect's Status
The IsEnableSpatializer function is used to obtain the current 3D sound effect's status. The return value of this function is of the bool type.
#### Function Prototype
```
ITMGAudioCtrl virtual bool IsEnableSpatializer()
```
#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->IsEnableSpatializer();
```

### Update the Location of a Sound Source
The UpdateSpatializer function is used to update the location of a sound source.
#### Function Prototype
```
ITMGAudioCtrl virtual int UpdateSpatializer(std::string& identifier,float azimuth,float elevation,float distance_cm)
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| identifier    	|string   		|The value of **openID** is of the Int32 type and must be greater than **10000**.		|
| azimuth    		|float        	|Azimuth.								|
| elevation    	|float         	|Elevation angle.								|
| distance_cm    	|float         	|Distance in centimeters.				|

#### Function Principle
![](https://main.qcloudimg.com/raw/0f90e8e84915c3f34482b1d40b0630c0.png)

As shown in the preceding figure, assume that a recipient is located at point A, and a sender is located at point B. ![](https://main.qcloudimg.com/raw/64491afbf45c2afc68039e704b77292e.png) is the azimuth, ![](https://main.qcloudimg.com/raw/affadf85b6c842c025e2ae9f8ef114d9.png) is the elevation angle, and the length of line AB is distance_cm.
Assume that coordinates ![](https://main.qcloudimg.com/raw/8b06a9be42ac50d8653af271c057fa64.png) are converted to ![](https://main.qcloudimg.com/raw/ff91cf1896f4f15eabc677586923400f.png), where ![](https://main.qcloudimg.com/raw/1d8902af13daf380e312e36138eef7b5.png)
The formula is:
![](https://main.qcloudimg.com/raw/e1aa4d09b144af4ea920d63cf9cac6bb.png)

#### Sample Code
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->UpdateSpatializer(identifier,azimuth,elevation,distance_cm);
```

#### Function Appendix
```
/*     ^
      z|   y(azi=0)
       |  /
       | /
	   .----->x(azi=90)    ...w = 90-azi
*/
#define QDSP_PAI  3.1415926535897

void xyz2dae(float *dist,float *azi,float *elve,float x,float y,float z)
{
	float paitodu = 180/QDSP_PAI;
	float sqxy = sqrt(x*x+y*y);

	*dist = sqrt(x*x + y*y + z*z);

	if (x)
	{
		if (y)
		{
			if (x>0)
			{
				*azi = 90 - atan(y/x)*paitodu;
			}
			else
			{
				*azi = -90 - atan(y/x)*paitodu;
			}

		}
		else
		{
			if (x>0)
			{
				*azi = 90;
			}
			else
			{
				*azi = -90;
			}
		}

	}
	else
	{
		if (y>0)
		{
			*azi = 0;
		}
		else
		{
			*azi = 180;
		}
	}

	if (sqxy)
	{
		*elve = atan(z/sqxy)*paitodu;
	}
	else
	{
		if (z>0)
		{
			*elve = 90;
		}
		else
		{
			*elve = -90;
		}

	}
}


void dae2xyz(float *x,float *y,float *z,float dist,float azi,float elve)
{
	float sqxy;
	float dutopai = QDSP_PAI/180;

	*z = dist*sin(elve*dutopai);
	sqxy = dist*cos(elve*dutopai);
	*x = sqxy*cos((90-azi)*dutopai);
	*y = sqxy*sin((90-azi)*dutopai);
}
```
