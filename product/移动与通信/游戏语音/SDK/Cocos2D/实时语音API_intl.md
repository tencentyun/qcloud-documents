## 1 Overview
To use Voice Chat, you need to call [Basic API](https://cloud.tencent.com/document/product/556/7665) at first.

## 2 Call APIs for Voice Chat 
 
![](https://mc.qcloudimg.com/static/img/d7eb0df95ebdff5e8f9d44a8a01bd74f/jj2.png)  
**How-To**   
1. Call `SetMode()` to enable Voice Chat mode.  
2. Call `JoinTeamRoom()` to enable Team Chatting mode, or `JoinNationalRoom()` to enable Commander mode.  
3. It is necessary to use the call `poll` of `Tick` to check the callback, and `OnJoinRoomComplete()` method will be called back when after successful or failed entry to room.  
4. After joining the room, call `OpenMic()` to enable microphone to collect voice and send it to the network.  
5. Call `OpenSpeaker()` to enable the speaker and begin to receive audio stream on the Internet and play automatically.  
6. Call `QuitRoom()` to quit the room, and then `OnQuitRoomComplete()` method will be called back when it succeed.  

Note:  
For commander mode, only 5 people are allowed to speak. Users will be assigned a role (listener or host) when they join the room.


### 3 Voice Chat APIs

### 3.1 Join Team Chat Room
1.API Description 

Call this API to join a team chat room.

2.Function Prototype

  `GCloudVoiceErrno JoinTeamRoom(const char *roomName, int msTimeout = 10000) `  

  |Parameter|Type|Meaning|
  ---|---|---
  |roomName| const char *| Name of room to be joined| 
  |msTimeout|int|Timeout settings for joining a room (unit: ms)
The result of joining a room is called back via `void OnJoinRoom(GCloudVoiceCompleteCode code, const char *roomName, int memberID)`.

3.Sample Code

      public void JoinRoomBtn_Click()
      {
      	gcloud_voice::GetVoiceEngine()->JoinTeamRoom("cz_test2", 5000);
      }    
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization    
GCLOUD_VOICE_MODE_STATE_ERR: Need to call `SetMode` first to set to Voice Chat mode  
GCLOUD_VOICE_PARAM_INVALID: The parameters transferred are incorrect. For example, room name is empty or too long (up to 127 bytes) and consisting of a-z, A-Z, 0-9, -,_. Timeout range: 5000ms-60000ms.  
GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error. For example, users have entered the room, but it is necessary to call `QuitRoom` first before entering again.
### 3.2 Join National Battle Room

1.API Description  
  
To enable Commander mode, you need to call this API to join a National Battle room first.

2. Function Prototype

      enum GCloudVoiceMemberRole
      {
      	Anchor = 1, // member who can open microphone and say
      	Audience,   // member who can only hear anchor's voice
      };
      GCloudVoiceErrno JoinNationalRoom(const char *roomName, GCloudVoiceMemberRole role, int msTimeout = 10000)   

  |Parameter|Type|Meaning|
  |--|--|--|
  |roomName| const char *| Name of room to be joined|
  |role|GCloudVoiceMemberRole| Role of member. Listeners can only listen but not speak. Hosts can speak and listen. |
  |msTimeout|int|Timeout setting for joining a room (unit: ms)
The result of joining a room is called back via `void OnJoinRoom(GCloudVoiceCompleteCode code, const char *roomName, int memberID)`.

3. Sample Code

      public void AudienceJoin_Click()
      {
      	gcloud_voice::GetVoiceEngine()->JoinNationalRoom("cz_test", gcloud_voice::IGCloudVoiceEngine::Audience, 5000);
      }
      public void AnchorJoin_Click()
      {
      	gcloud_voice::GetVoiceEngine()->JoinNationalRoom("cz_test", gcloud_voice::IGCloudVoiceEngine::Anchor, 5000);
      }    
4. Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
GCLOUD_VOICE_MODE_STATE_ERR: Need to call `SetMode` first to set to Voice Chat mode  
GCLOUD_VOICE_PARAM_INVALID: The parameters transferred are incorrect. For example, room name is empty or too long (127 bytes at the most) and consisting of a-z, A-Z, 0-9, -,_. Timeout range: 5000ms-60000ms.
GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error. For example, users have entered the room, but it is necessary to call `QuitRoom` first before entering again.
### 3.3 Quit Voice Chat
1. API Description  

Call this API to quit Voice Chat rooms (both Team Chatting and Commander).

2.Function Prototype

  `GCloudVoiceErrno QuitRoom(const char *roomName, int msTimeout = 10000) ` 

  |Parameter|Type|Meaning|
  |--|--|--|
  |roomName| const char *| Name of the room to be quit|
  |msTimeout|int| Timeout settings of quitting a room (unit: ms)
The result of quitting the room is called back via `void OnQuitRoom(GCloudVoiceCompleteCode code, const char *roomName)`.

3.Sample Code

      public void QuitRoomBtn_Click()
      {
      	gcloud_voice::GetVoiceEngine()->QuitRoom("cz_test", 5000);
      }   

4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode  
GCLOUD_VOICE_PARAM_INVALID: The parameters transferred are incorrect. For example, room name is empty or too long (up to 127 bytes) and consisting of a-z, A-Z, 0-9, -,_. Timeout range: 5000ms-60000ms.  
GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error. E.g. you've not joined a room.
### 3.4 Enable Microphone

1.API Description
 
For Voice Chat mode, after joining the room (both team chatting and commander mode), call this API to enable your microphone to collect voice and send it to the network.

2.Function Prototype

  `GCloudVoiceErr OpenMic();  `
  
3.Sample Code

      public void OpenMicBtn_Click()
      {
      	gcloud_voice::GetVoiceEngine()->OpenMic();
      }  
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode  
GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error. E.g. the player has not joined a room.  
GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR: Microphone cannot be opened in the big room for users as listeners.
### 3.5 Disable Microphone

1.API Description
  
For Voice Chat mode, after joining a room (both Team Chatting and Commander), call this API to disable microphone if you don't want to collect audio and send them to the network anymore.


2.Function Prototype

  `GCloudVoiceErrno CloseMic();  `

3.Sample Code

      public void CloseMicBtn_Click()
      {
      	gcloud_voice::GetVoiceEngine()->CloseMic ();
      } 
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode  
GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error. E.g. the player has not joined a room.  
GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR: Microphone cannot be opened or closed in the big room for users as listeners.  
### 3.6 Enable Speaker

1.API Description
 
For Voice Chat mode, after joining a room (both Team Chatting and Commander), call this API to enable speaker to receive and play audio.

2.Function Prototype

  `GCloudVoiceErrno OpenSpeaker();  `

3.Sample Code

      public void OpenSpeakerBtn_Click()
      {
      	gcloud_voice::GetVoiceEngine()->OpenSpeaker ();
      }
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode  
GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error. E.g. the player has not joined a room.  
### 3.7 Disable Speaker

1.API Description
  
For Voice Chat mode, after joining a room (both Team Chatting and Commander), call this API to disable speaker if you don't want to receive and play audio data from the network anymore.


2.Function Prototype

 ` GCloudVoiceErrno CloseSpeaker();  `

3.Sample Code

      public void CloseSpeakerBtn_Click()
      {
      	gcloud_voice::GetVoiceEngine()->CloseSpeaker ();
      }
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode  
GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error. E.g. the player has not joined a room.  
### 3.8 Callback of joining a room
1.API Description
 
Use this callback to return the result of joining a room

2.Function Prototype

  `virtual void OnJoinRoom(GCloudVoiceCompleteCode code, const char *roomName, int memberID) ;`

  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  |roomName| const char *| Name of room joined|
  |memberID|int| ID of member joined the room|
3.Sample Code

       void NationalRoomNotify::OnJoinRoom(gcloud_voice::GCloudVoiceCompleteCode code, const char *roomName, int memberID)
      {
      	if (code == gcloud_voice::GV_ON_JOINROOM_SUCC) {
      		_section->setText("Join Team Room Success");
      	} else {
      		_section->setText("Join Team Room Error");
      	}
      };
### 3.9 Callback of Quitting Room
1.API Description  

Return the result of quitting room via this callback.

2.Function Prototype

  `virtual void OnQuitRoom(GCloudVoiceCompleteCode code, const char *roomName) ;`

  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  |roomName| const char *| Name of room quitted|
  |memberID|int| ID of member joined the room|
3.Sample Code
    
      void NationalRoomNotify::OnQuitRoom(gcloud_voice::GCloudVoiceCompleteCode code, const char *roomName)
      {
      	if (code == gcloud_voice::GV_ON_QUITROOM_SUCC) {
      		_section->setText("Quit Team Room Success");
      	} else {
      		_section->setText("Quit Team Room Error");
      	}
      }
### 3.10 Callback of Member Status Changes

1.API Description
  
Use this callback to notify member status changes, like starting or stopping speaking

2.Function Prototype

  `virtual void OnMemberVoice    (const unsigned int *members, int count) ;`

  |Parameter|Type|Meaning|
  |--|--|--|
  |members|int[] |Members with status changes. Values show in pairs like [memberID &#124; status]. Count pairs in total. The status may be "0" (stop talking), "1" (start talking) and "2" (resume talking). |
  |count|int| Count of members with status changed
3.Sample Code

      void NationalRoomNotify::OnMemberVoice (const unsigned int *members, int count)
      {
      	for (int i=0; i<count; i++) {
      		CCLOG("member %d's status is %d", *(members+2*i), *(members+2*i+1));
      	}
      }

