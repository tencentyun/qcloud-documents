Welcome to the Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes access technologies for iOS development so that iOS developers can easily debug and access APIs for Tencent Cloud GME.

## SDK Initialization

### Get a Singleton
The GME SDK is provided as a singleton. All calls start with ITMGContext. Asynchronous operation results or any internal status changes are passed to an application via ITMGDelegate.
#### Function Prototype
```
ITMGContext @protocol ITMGDelegate <NSObject>
```
#### Sample Code
```
ITMGContext* _context = [ITMGContext GetInstance];
_context.TMGDelegate =self;
```

### Message Transferring
GME messages are transferred to an application via ITMGDelegate. The message type is specified by **ITMG_MAIN_EVENT_TYPE**. The message content is a dictionary. Message content varies with the event type.
#### Function Prototype
```
- (void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary*)data
```
#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    	NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
		switch (eventType) {
			//Check eventType
			}
	}
```
#### Message List:

|Message     | Description
| ------------- |-------------|
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    				|Entry into an audio/video room.
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    				|Exit from an audio/video room.
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    		|Disconnection from a room due to network issues or other reasons.
| ITMG_MAIN_EVENT_TYPE_ENABLE_MIC    				|Microphone enabled.
| ITMG_MAIN_EVENT_TYPE_DISABLE_MIC    				|Microphone disabled.
|ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER				|Speaker enabled.
|ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER				|Speaker disabled.
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE				|Role changed.
|ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH			|Accompaniment ended.
|ITMG_MAIN_EVNET_TYPE_USER_UPDATE					|Room member updated.
|ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE		|PTT recorded.
|ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE		|PTT uploaded.
|ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE	|PTT downloaded.
|ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE			|PTT played.
|ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE	|Speech converted into text.
|ITMG_MAIN_EVENT_TYPE_OPEN_CAMERA				|Camera turned on.
|ITMG_MAIN_EVENT_TYPE_CLOSE_CAMERA				|Camera turned off.


## Real-Time Voice Access

### Set Relevant Information
Relevant information is applied for through Tencent Cloud Console. For more information, see the [GME Access Guide](/document/product/607/10782).
The SetAppInfo function contains the **sdkAppId**, **accountType**, and **openID** parameters. The values of **sdkAppId** and **accountType** are obtained from Tencent Cloud Console. The value of **OpenID** indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers, and the ID must be unique in an application. Currently, the ID can be only of the int64 type.
#### Function Prototype
```
ITMGContext -(void)SetAppInfo:(NSString*)sdkAppID accountType:(NSString*)accountType openID:(NSString*)openID
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| sdkAppId    	|NSString  |The value is obtained from Tencent Cloud Console.				|
| accountType    	|NSString  |The value is obtained from Tencent Cloud Console.			|
| openID    		|NSString  |The value indicates an ID that uniquely identifies a user. The ID setting rule can be customized by application developers. Currently, the value must be greater than **10000**.|

#### Sample Code
```
[[ITMGContext GetInstance] SetAppInfo:SDKAPPID3RD accountType:ACCOUNTTYPE openID:_openId];
```
The SetAppVersion function is used to set version information that is used during log query and debugging. No functions are affected if version information is not set.
#### Function Prototype
```
ITMGContext  -(void)SetAppVersion:(NSString*)appVersion
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| sAppVersion    |NSString  |Version number.|

#### Sample Code
```
[[ITMGContext GetInstance]SetAppVersion:appversion];
```
The GetSDKVersion function is used to obtain the SDK version number.

#### Function Prototype
```
ITMGContext  -(NSString*)GetSDKVersion
```
#### Sample Code
```
[[ITMGContext GetInstance] GetSDKVersion];
```
Then, the value of **AuthBuffer** is generated for encryption and authentication of relevant functions. For more information about how to obtain relevant parameters and other information, see the [GME Access Guide](/document/product/607/10782).
The return value of this function is of the NSData type.
#### Function Prototype
```
@interface QAVAuthBuffer : NSObject
+ (NSData*) GenAuthBuffer:(unsigned int)appId roomId:(unsigned int)roomId identifier:(NSString*)identifier accountType:(unsigned int)accountType key:(NSString*)key expTime:(unsigned int)expTime authBits:(unsigned int) authBits;
@end
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| appId    		|int   		|The value is the same as the value of **sdkAppId** on Tencent Cloud Console.		|
| roomId    		|int  		|Name of the room to be entered.						|
| identifier  		|NSString    	|User identifier.								|
| accountType    	|int   		|The value is obtained from Tencent Cloud Console.	|
| key    			|NSString    	|The value is the key provided by Tencent Cloud Console.					|
| expTime    		|int   		|Timeout interval for entering a room.						|
| authBits   	 	|uint64    	|Permissions.									|

>About permissions
The value **ITMG_AUTH_BITS_ALL** indicates all permissions. It is recommended that this parameter be set to **ITMG_AUTH_BITS_ALL** for real-time users and VJs. The value **ITMG_AUTH_BITS_RECV** indicates downstream permissions. It is recommended that this parameter be set to ITMG_AUTH_BITS_RECV for listening- or watching-only audiences. The startAccompany function is unavailable for downstream permissions.

#### Sample Code
```
NSData* authBuffer =   [QAVAuthBuffer GenAuthBuffer:SDKAPPID3RD.intValue roomId:_roomId identifier:_openId accountType:ACCOUNTTYPE.intValue key:AUTHKEY expTime:[[NSDate date] timeIntervalSince1970] + 3600 authBits:ITMG_AUTH_BITS_ALL];
```

### Enter a Room
When a user enters a room with a generated **AuthBuffer** value, the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback.
>Note: The microphone and speakers are disabled by default when a user enters a room.
For more information about role settings, see the [GME Voice Role Description](/document/product/607/15172).

#### Function Prototype
```
ITMGContext   -(void)EnterRoom:(int) relationId controlRole:(NSString*)role authBuffer:(NSData*)authBuffer
```

|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| roomID		|int    		|Room number, which is an integer of six or more digits.	|
| controlRole    	|NSString    	|Role name. Set the parameter based on the requirements.		|
| authBuffer    	|NSData    	|The value is used for authentication.						|

#### Sample Code
```
[[ITMGContext GetInstance] EnterRoom:_roomId controlRole:@"user" authBuffer:authBuffer];
```

### Callback for Entering a Room
After a user enters a room, the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is sent, which is checked in the OnEvent function.
#### Function Prototype
```
- (void)OnEnterRoomComplete:(int)result WithErrinfo:(NSString *)error_info
```

#### Code Description
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
        {
            int result = ((NSNumber*)[data objectForKey:@"result"]).intValue;
            NSString* error_info = [data objectForKey:@"error_info"];
            //Enter a room
        }
            break;
     }
}
```

### Check Whether a User Has Entered a Room
The IsRoomEntered function is used to check whether a user has entered a room. The return value of this function is of the bool type.
#### Function Prototype
```
ITMGContext -(BOOL)IsRoomEntered
```
#### Sample Code
```
[[ITMGContext GetInstance] IsRoomEntered];
```

### Exit from a Room
The ExitRoom function is used to exit from a room.
#### Function Prototype
```
ITMGContext -(void)ExitRoom
```
#### Sample Code
```
[[ITMGContext GetInstance] ExitRoom];
```

### Callback for Exiting from a Room
After a user exits from a room, the SDK sends the ITMG_MAIN_EVENT_TYPE_EXIT_ROOM message to notify an application of the exit via ITMGDelegate callback.
#### Function Prototype
```
 -(void)OnExitRoomComplete
```
#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM：
        {
	    //Exit from a room
        }
            break;
    }
}
```

### Suspend Acquisition and Playback by the Audio Engine
The PauseAudio function is used to suspend acquisition and playback by the audio engine and is effective only after a user enters a room.
After the EnterRoom function is successfully called, the microphone is occupied and other programs cannot acquire data from the microphone.
Note: Calling of EnableMic(false) cannot release the microphone.
To release a microphone, call the PauseAudio function that can suspend the audio engine. To resume audio acquisition, call the ResumeAudio function.
#### Function Prototype
```
GetAudioCtrl -(QAVResult)PauseAudio
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] PauseAudio];
```

### Resume Acquisition and Playback by the Audio Engine
The ResumeAudio function is used to resume acquisition and playback by the audio engine and is effective only after a user enters a room.
#### Function Prototype
```
GetAudioCtrl -(QAVResult)ResumeAudio
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] ResumeAudio];
```

### Role Setting
Change a flow control role. The ChangeRole method is used to set a user role before a user joins a channel. The user is allowed to change the role after the user joins a channel.
The following six roles are automatically established by default: esports, Rhost, Raudience, Werewolf, host, and audience. For more information about role descriptions, see the [GME Voice Role Description](/document/product/607/15172).
#### Function Prototype
```
GetRoom -(void)ChangeRole:(NSString*)role authBuffer:(NSData*)authBuffer
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| role    			|NSString     	|Role.			|
| authBuffer    	|NSData    	|The parameter must be reset each time.	|

>Note
Changing a flow control role means modifying audio and video encoding parameters. Therefore, the audio and video encoding API needs to be called to reset **AuthBuffer**. For more information, see how to generate **AuthBuffer**.

The following table lists the speech quality corresponding to each role.

|Role Name     | Applicable Scenario         |Key Features|
| ------------- |-------------|-------------
| esports    	|MOBA, competitive, and shooting games.     								|Ordinary sound quality and ultra-low latency.	|
| Rhost    	|Commander mode of MMORPGs. Only a commander can join broadcasting.     		|High fluency and low latency.		|
| Raudience	|Commander mode of MMORPGs. Only a commander can join broadcasting.     		|High fluency and low latency.		|
| Werewolf 	|Werewolf, casual games, and other games.										|Good sound quality and high anti packet loss rate.	|
| host  		|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.	|Good sound quality and high anti packet loss rate.	|
| audience  	|VJ mode of MMORPGs. A VJ can interact with players in voice and video mode.	|Good sound quality and high anti packet loss rate.	|

#### Sample Code
```
[[[ITMGContext GetInstance]GetRoom ]ChangeRole:@"Playre"authBuffer:authBuffer];
```

### Callback for a Role Setting
After a role setting, the ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE event message is sent as a callback and is checked in the OnEvent function.
#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE：
        {
	    //Role set
        }
            break;
    }
}
```

### Member State Change
The member state change event is triggered to send notifications only when the state of a member changes. To allow real-time member state query, cache the state each time the upper layer receives the ITMG_MAIN_EVNET_TYPE_USER_UPDATE event message, which contains **event_id** and **endpoints**. The message is checked in the OnEvent function.
#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVNET_TYPE_USER_UPDATE：
        {
	    //Member state change
        }
            break;
    }
}
```
### Enable or Disable an Audio Data Blacklist
The blacklist is reset to a new member list each time the SetAudioBlackList function is called to enable the blacklist. The function is called only when audio data to be received needs to be customized. If the function is not called, all audio data in a room is received by default. If the function returns **0**, the call fails.
#### Function Prototype
```
GetRoom -(QAVResult)SetAudioBlackList:(NSArray*)identifierList
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| identifierList    |NSArray      |Blacklist.|
#### Sample Code
```
[[[ITMGContext GetInstance]GetRoom ] GetQualityTips];
```

### Enable or Disable a Microphone
The EnableMic function is used to enable or disable a microphone.
>Note: The microphone and speakers are disabled by default when a user enters a room.

#### Function Prototype
```
GetAudioCtrl -(void)EnableMic:(BOOL)enable
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| isEnabled    |boolean     |To enable a microphone, set the input parameter to **true**. To disable a microphone, set the input parameter to **false**.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] EnableMic:YES];
```
### Callback of a Microphone Event
The OnEvent function is used for callback of a microphone event. The SDK notifies an application of microphone invocation via the callback. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_MIC or ITMG_MAIN_EVENT_TYPE_DISABLE_MIC, which is checked in the OnEvent function.

#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_ENABLE_MIC：
        {
	    //Enable a microphone
        }
            break;
	case ITMG_MAIN_EVENT_TYPE_DISABLE_MIC：
        {
	    //Disable a microphone
        }
            break;
    }
}
```
### Obtain the Status of a Microphone
The GetMicState function is used to obtain the status of a microphone.
#### Function Prototype
```
GetAudioCtrl -(int)GetMicState
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] GetMicState];
```

### Obtain the Real-Time Volume of a Microphone
The GetMicLevel function is used to obtain the real-time volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
GetAudioCtrl -(int)GetMicLevel
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] GetMicLevel];
```

### Set the Software Volume of a Microphone
The SetMicVolume function is used to set the software volume of a microphone. The **volume** parameter specifies the software volume of a microphone. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.
#### Function Prototype
```
GetAudioCtrl -(void)SetMicVolume:(int) volume
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| volume    |int      |Volume, ranging from **0** to **100**.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] SetMicVolume:100];
```

### Obtain the Software Volume of a Microphone
The GetMicVolume function is used to obtain the software volume of a microphone. The return value of this function is of the int type.
#### Function Prototype
```
GetAudioCtrl -(int) GetMicVolume
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] GetMicVolume];
```

### Enable or Disable Speakers
The EnableSpeaker function is used to enable or disable speakers.
#### Function Prototype
```
GetAudioCtrl -(void)EnableSpeaker:(BOOL)enable
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| isEnabled    |boolean       |To enable speakers, set the input parameter to **true**. To disable speakers, set the input parameter to **false**.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] EnableSpeaker:YES];
```

### Callback of a Speaker Event
The OnEvent function is used for callback of a speaker event. The SDK notifies an application of speaker invocation via the callback. The event message involved is ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER or ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER.
#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER：
        {
	    //Enable speakers
        }
            break;
	case ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER：
        {
	    //Disable speakers
        }
            break;
    }
}
```

### Obtain the Status of Speakers
The GetSpeakerState function is used to obtain the status of speakers. The return value of this function is of the int type.
#### Function Prototype
```
GetAudioCtrl -(int)GetSpeakerState
```

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] GetSpeakerState];
```

### Obtain the Real-Time Volume of Speakers
The GetSpeakerLevel function is used to obtain the real-time volume of speakers. The return value of this function is of the int type.
#### Function Prototype
```
GetAudioCtrl -(int)GetSpeakerLevel
```

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] GetSpeakerLevel];
```

### Set the Software Volume of Speakers
The SetSpeakerVolume function is used to set the software volume of speakers.
>Note: The **vol** parameter specifies the software volume of speakers. Value **0** indicates mute and value **100** indicates that the actual volume will be the same as the original volume. The default value is **100**.

#### Function Prototype
```
GetAudioCtrl -(void)SetSpeakerVolume:(int)vol
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| vol    |int        |Volume, ranging from **0** to **100**.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] SetSpeakerVolume:100];
```

### Obtain the Software Volume of Speakers
The GetSpeakerVolume function is used to obtain the software volume of speakers and returns  an INT value.
>Note: The **Level** parameter indicates the real-time volume, while the **Volume** parameter indicates the software volume of speakers. The final volume is calculated as follows: Final volume = Value of Level x Value of Volume%. For example, if the values of **Level** and **Volume** are **100** and **60** respectively, the final volume is 60.

#### Function Prototype
```
GetAudioCtrl -(int)GetSpeakerVolume
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] GetSpeakerVolume];
```
### Enable In-Ear Monitoring
The EnableLoopBack function is used to enable in-ear monitoring.
#### Function Prototype
```
GetAudioCtrl -(QAVResult)EnableLoopBack:(BOOL)enable
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |boolean         |Indicates whether to enable in-ear monitoring.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioCtrl] EnableLoopBack:YES];
```

### Start Playing an Accompaniment
The StartAccompany function is used to start playing an accompaniment.
>Note:
1. Calling the API will reset the volume.
2. The API is unavailable for downstream permissions.

#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)StartAccompany:(NSString*)filePath loopBack:(BOOL)loopBack loopCount:(int)loopCount
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    	|NSString    		|Path for playing an accompaniment.											|
| loopBack  	|boolean         	|Indicates whether to send a mix. The parameter is generally set to **true**, indicating that other users can also hear an accompaniment.	|
| loopCount	|int          		|Number of loops. Value **-1** means an infinite loop.							|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] StartAccompany:path loopBack:isLoopBack loopCount:loopCount];
```

### Callback for Playing an Accompaniment
After the playback of an accompaniment, the ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH event message is sent and the OnEvent function is called to check the message.
#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH：
        {
	    //Accompaniment played
        }
            break;
    }
}
```

### Stop Playing an Accompaniment
The StopAccompany function is used to stop playing an accompaniment.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)StopAccompany:(int)duckerTime
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| duckerTimeMs    |int             |Fading time.|

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] StopAccompany:duckerTime];
```

### Check Whether the Playback of an Accompaniment Is Complete
The IsAccompanyPlayEnd function is used to check whether the playback of an accompaniment is complete. If yes, the function returns **true**. If no, it returns **false**.
#### Function Prototype
```
GetAudioEffectCtrl -(bool)IsAccompanyPlayEnd
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] IsAccompanyPlayEnd];
```

### Pause an Accompaniment
The PauseAccompany function is used to pause an accompaniment.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)PauseAccompany
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] IsAccompanyPlayEnd];
```

### Resume an Accompaniment
The ResumeAccompany function is used to resume an accompaniment.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)ResumeAccompany
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] ResumeAccompany];
```

### Configure Whether Users Can Hear Accompaniments Played by Themselves
The EnableAccompanyPlay function is used to configure whether users can hear accompaniments played by themselves.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)EnableAccompanyPlay:(BOOL)enable
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |BOOL             |Indicates whether users can hear accompaniments played by themselves.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] GetAudioEffectCtrl :YES];
```

### Configure Whether Other Users Can Hear an Accompaniment
The EnableAccompanyLoopBack function is used to configure whether other users can hear an accompaniment.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)EnableAccompanyLoopBack:(BOOL)enable
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| enable    |BOOL             |Indicates whether other users can hear an accompaniment.|

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] EnableAccompanyLoopBack:YES];
```

### Set the Volume of an Accompaniment
The SetAccompanyVolume function is used to set the linear volume of an accompaniment. The default value is **100**. If the return value is greater than **100**, the accompaniment volume increases. If the return value is less than **100**, the accompaniment volume attenuates.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)SetAccompanyVolume:(int)vol
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| vol    |int             |Volume.|

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] SetAccompanyVolume:volume];
```

### Obtain the Volume of an Accompaniment
The GetAccompanyVolume function is used to obtain the volume of an accompaniment.
#### Function Prototype
```
GetAudioEffectCtrl -(int)GetAccompanyVolume
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] GetAccompanyVolume];
```

### Obtain the Playback Progress of an Accompaniment
The following two functions are used to obtain the playback progress of an accompaniment. Note: Current / Total = Number of current loop times; Current % Total = Playback position of the current loop.
#### Function Prototype
```
GetAudioEffectCtrl -(int)GetAccompanyFileTotalTimeByMs
GetAudioEffectCtrl -(int)GetAccompanyFileCurrentPlayedTimeByMs
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] GetAccompanyFileTotalTimeByMs];
[[[ITMGContext GetInstance] GetAudioEffectCtrl] GetAccompanyFileCurrentPlayedTimeByMs];
```

### Set Playback Progress
The SetAccompanyFileCurrentPlayedTimeByMs function is used to set playback progress.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVAccResult)SetAccompanyFileCurrentPlayedTimeByMs:(uint) time
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| time    |uint                |Playback progress, in milliseconds.|

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] SetAccompanyFileCurrentPlayedTimeByMs:time];
```

### Obtain the Volume of a Sound Effect
The GetEffectsVolume function is used to obtain the linear volume of a sound effect. The default value is **100**. If the return value is greater than **100**, the accompaniment volume increases. If the return value is less than **100**, the accompaniment volume attenuates.
#### Function Prototype
```
GetAudioEffectCtrl -(int)GetEffectsVolume
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] GetEffectsVolume];
```

### Set the Volume of a Sound Effect
The SetEffectsVolume function is used to set the volume of a sound effect.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)SetEffectsVolume:(int)volume
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| volume    |int                    |Volume.|

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] SetEffectsVolume:(int)Volume];
```

### Play a Sound Effect
The PlayEffect function is used to play a sound effect. The **soundId** parameter, which uniquely identifies an independent file, must be managed on the application side.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)PlayEffect:(int)soundId filePath:(NSString*)filePath loop:(BOOL)loop
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId  	|int           	|Sound effect ID.			|
| filePath    	|NSString    	|Sound effect path.		|
| loop    		|boolean  	|Indicates whether to repeat playback.	|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] PlayEffect:soundId filePath:path loop:isLoop];
```

### Pause a Sound Effect
The PauseEffect function is used to pause a sound effect.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)PauseEffect:(int)soundId
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|

#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] PauseEffect:soundId];
```

### Pause All Sound Effects
The PauseAllEffects function is used to pause all sound effects.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)PauseAllEffects
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] PauseAllEffects];
```

### Resume a Sound Effect
The ResumeEffect function is used to resume a sound effect.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)ResumeEffect:(int)soundId
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] ResumeEffect:soundId];
```

### Resume All Sound Effects
The ResumeAllEffects function is used to resume all sound effects.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)ResumeAllEffects
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] ResumeAllEffects];
```

### Stop Playing a Sound Effect
The StopEffect function is used to stop playing a sound effect.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)StopEffect:(int)soundId
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| soundId    |int                    |Sound effect ID.|
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] StopEffect:soundId];
```

### Stop Playing All Sound Effects
The StopAllEffects function is used to stop playing all sound effects.
#### Function Prototype
```
GetAudioEffectCtrl -(QAVResult)StopAllEffects
```
#### Sample Code
```
[[[ITMGContext GetInstance] GetAudioEffectCtrl] StopAllEffects];
```

### Obtain Diagnosis Information
The GetQualityTips function is used to obtain information about the quality of real-time voice or video chats. The function is mainly used to check the quality of real-time chats and detect problems. The function can be ignored on the service side.
#### Function Prototype
```
GetRoom -(NSString*)GetQualityTips
```
#### Sample Code
```
[[[ITMGContext GetInstance]GetRoom ] GetQualityTips];
```

## PTT Access
### Initialize PTT Access
Initializing PTT access requires passing **accessToken** to TLS-related functions. For details on the process of obtaining **accessToken** for authentication, see the [GME Access Guide](/document/product/607/10782).
The **Error** parameter is used to pass error information. For example, when **appId** is set to **0** or **privateKey** or **identifier** is left blank, error information indicating that a parameter is incorrectly set is returned.
#### Function Prototype
```
+(NSString*)genSig:(NSString*)appId identifier:(NSString*)identifier privateKey:(NSString*)privateKey error:(NSError**)error
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| sdkAppId  	|int   		|The value is obtained from Tencent Cloud Console.													|
| openID    	|NSString	|Identifier that uniquely identifies a user. The setting rule is customized by application developers.											|
| key    		|NSString 	|The value is the key provided by Tencent Cloud Console.																|
| error    	|Error   		|The destination address for receiving an error value must be specified. If an error occurs during the **sig** generation, the return value is left blank and the value of the **error** parameter includes error information.	|
```
 -(QAVResult)ApplyAccessToken:(NSString*)accessToken
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| accessToken    |NSString                       |The value is the same as the value of **accessToken** returned by the getTLSSig function.|
#### Sample Code
```
NSString* privateKey = @"Private key on the official website";
NSString* accessToken = [QAVSDKSigManager genSig:SDKAPPID3RD identifier:_openId privateKey:privateKey error:&error];
[[[ITMGContext GetInstance]GetPTT]ApplyAccessToken:accessToken];
```

### Specify the Maximum Length of a Voice Message
The SetMaxMessageLength function is used to specify the maximum length of a voice message. The maximum length can be 60 seconds.
#### Function Prototype
```
GetPTT -(void)SetMaxMessageLength:(int)msTime
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| msTime    |int                    |Length of a voice message.|
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]SetMaxMessageLength:(int)msTime];
```

### Start Recording
The StartRecording function is used to start recording.
#### Function Prototype
```
GetPTT -(void)StartRecording:(NSString*)fileDir
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| fileDir    |NSString                     |Path for playing a voice file, which can be NULL.|
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]StartRecording:path];
```

### Callback for Starting Recording
After recording, the ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLET event message is sent and the OnEvent function is called to check the message.

#### Sample Code
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE：
        {
	    //PTT recorded
        }
            break;
    }
}
```

### Stop Recording
The StopRecording function is used to stop recording.
#### Function Prototype
```
GetPTT -(QAVResult)StopRecording
```
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]StopRecording];
```

### Cancel Recording
The CancelRecording function is used to cancel recording.
#### Function Prototype
```
GetPTT -(QAVResult)CancelRecording
```
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]CancelRecording];
```

### Upload a Voice File
The UploadRecordedFile function is used to upload a voice file.
#### Function Prototype
```
GetPTT -(void)UploadRecordedFile:(NSString*)filePath
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |NSString                      |Path for uploading a voice file.|
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]UploadRecordedFile:path];
```

### Callback for Uploading a Voice File
After a voice file is uploaded, the ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE event message is sent, which is checked in the OnEvent function.
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE：
        {
	    //Voice file uploaded
        }
            break;
    }
}
```

### Download a Voice File
The QAVDownloadFileCompleteCallback function is used to download a voice file.
#### Function Prototype
```
GetPTT -(void)DownloadRecordedFile:(NSString*)fileId downloadFilePath:(NSString*)downloadFilePath
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| fileID    			|NSString                      |URL of a file.		|
| downloadFilePath 	|NSString                      |Path for downloading a file.	|
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]DownloadRecordedFile:fileIdpath downloadFilePath:path];
```

### Callback for Downloading a Voice File
After a voice file is downloaded, the ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE event message is sent, which is checked in the OnEvent function.
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE：
        {
	    //Voice file downloaded
        }
            break;
    }
}
```

### Play a Voice File
The PlayRecordedFile function is used to play a voice file.
#### Function Prototype
```
GetPTT -(void)PlayRecordedFile:(NSString*)downloadFilePath
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| downloadFilePath    |NSString                      |Path for downloading a file.|
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]downloadFilePath:path];
```

### Callback for Playing a Voice File
As a callback for playing a voice file, the ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE event message is sent, which is checked in the OnEvent function.
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE：
        {
	    //Playback completed
        }
            break;
    }
}
```

### Stop Playing a Voice File
The StopPlayFile function is used to stop playing a voice file.
#### Function Prototype
```
GetPTT -(int)StopPlayFile
```
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]StopPlayFile];
```
### Obtain the Size of a Voice File
The GetFileSize function is used to obtain the size of a voice file.
#### Function Prototype
```
GetPTT -(int)GetFileSize:(NSString*)filePath
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |NSString                     |Path for storing a voice file.|
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]GetFileSize:path];
```

### Obtain the Duration of a Voice File
The GetVoiceFileDuration function is used to obtain the duration of a voice file.
#### Function Prototype
```
GetPTT -(int)GetVoiceFileDuration:(NSString*)filePath
```
|Parameter     | Type         |Description|
| ------------- |-------------|-------------
| filePath    |NSString                     |Path for storing a voice file.|
#### Sample Code
```
[[[ITMGContext GetInstance]GetPTT]GetVoiceFileDuration:path];
```

### Convert Specified Speech into Text
As a callback for converting specified speech into text, the ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE event message is sent, which is checked in the OnEvent function.
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE：
        {
	    //Conversion completed
        }
            break;
    }
}
```
