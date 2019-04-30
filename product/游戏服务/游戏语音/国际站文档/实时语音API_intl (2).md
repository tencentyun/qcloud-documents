## 1 Overview
To use Voice Chat, you need to call [Basic APIs](https://cloud.tencent.com/document/product/556/7675).

## 2 Call APIs for Voice Chat 
![](https://mc.qcloudimg.com/static/img/69e8fafb64190a5ddc1f18a954d977ce/j2.png)

**How-To**   
1. Call `SetMode()` to enable Voice Chat mode.  
2. Call `JoinTeamRoom()` to enable Team Chatting mode, or `JoinNationalRoom()` to enable Commander mode.  
3. It is necessary to use the call `poll` of `Tick` to check the callback, and `OnJoinRoomComplete()` method will be called back when after successful or failed entry to room.  
4. After joining the room, call `OpenMic()` to enable microphone to collect voice and send it to the network.  
5. Call `OpenSpeaker()` to enable the speaker and begin to receive audio stream on the Internet and play automatically.  
6. Call `QuitRoom()` to quit the room, and then `OnQuitRoomComplete()` method will be called back when it succeed.  

**Note**  
For commander mode, only 5 people are allowed to speak. Users will be assigned a role (listener or host) when they join the room.

### 3 Voice Chat APIs

### 3.1 Join Team Chat Room
1.API Description 
 
To enable the Team Chatting feature of Voice Chat mode, you need to call this API to join a team chatroom first.

2.Function Prototype

      GCloudVoiceErr JoinTeamRoom(string roomName, int msTimeout)   
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |roomName|string| Name of room to be joined|
  |msTimeout|int|Timeout setting for joining a room (unit: ms)
   The result of joining the room is be called back via delegate void JoinRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID).

3.Sample Code

      public void JoinRoomBtn_Click()
      {
      	Debug.Log ("JoinRoom Btn Click");
    
      	int ret = m_voiceengine.JoinTeamRoom(m_roomName, 15000);
      	PrintLog ("joinroom ret=" + ret);
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Need to call SetMode to set to Voice Chat mode
    GCLOUD_VOICE_PARAM_INVALID: The parameters transferred are incorrect.For example, room name is empty or too long (127 bytes at the most) and consisting of a-z, A-Z, 0-9, -,_.Timeout range: 5000ms-60000ms.
    GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error (e.g.the user has already joined the room.Need to call QuitRoom first and join again).
### 3.2 Join National Battle Room

1.API Description  
  
To enable Commander mode, you need to call this API to join a National Battle room first.

2.Function Prototype

      public enum GCloudVoiceRole
      {
      ANCHOR = 1, // member who can open microphone and say
      AUDIENCE,   // member who can only hear anchor's voice
      }
      GCloudVoiceErr JoinNationalRoom(string roomName, GCloudVoiceRole role, int msTimeout)   
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |roomName|string| Name of room to be joined|
  |role|GCloudVoiceRole| Role of members.Listener can only receive voice, and cannot send voice; while anchor can both send and receive voice.|
 |msTimeout|int| Timeout settings for joining a room (unit: ms)

The result of joining the room is called back via `delegate void JoinRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)`.

3.Sample Code

      public void AudienceJoin_Click()
      {
      Debug.Log ("AudienceJoin Btn Click");
      int ret = m_voiceengine.JoinNationalRoom(m_roomName, GCloudVoiceRole.AUDIENCE, 15000);
      PrintLog ("AudienceJoin ret=" + ret);
      }
      public void AnchorJoin_Click()
      {
      Debug.Log ("AnchorJoin Btn Click");
      int ret = m_voiceengine.JoinNationalRoom(m_roomName, GCloudVoiceRole.ANCHOR, 15000);
      PrintLog ("AnchorJoin ret=" + ret);
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Need to call SetMode to set to Voice Chat mode
    GCLOUD_VOICE_PARAM_INVALID: The parameters transferred are incorrect.For example, room name is empty or too long (127 bytes at the most) and consisting of a-z, A-Z, 0-9, -,_.Timeout range: 5000ms-60000ms.
    GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error (e.g.the user has already joined the room.Need to call QuitRoom first and join again).
### 3.3 Quit Voice Chat
1.API Description  

Call this API to quit Voice Chat rooms (both Team Chatting and Commander).

2.Function Prototype

      GCloudVoiceErr QuitRoom(string roomName, int msTimeout);  
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |roomName|string| Name of room to be quit|
  |msTimeout|int| Timeout settings of quitting a room (unit: ms)
The result of quitting the room should be called back via `delegate void QuitRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)`.

3.Sample Code  

      public void QuitRoomBtn_Click()
      {
      Debug.Log ("quit room btn click");
      m_voiceengine.QuitRoom(m_roomName, 15000);
      }   
4.Error Codes  

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode
    GCLOUD_VOICE_PARAM_INVALID: The parameters transferred are incorrect.For example, room name is empty or too long (127 bytes at the most) and consisting of a-z, A-Z, 0-9, -,_.Timeout range: 5000ms-60000ms.
    GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error.(e.g.the user has not joined the room)
### 3.4 Enable Microphone

1.API Description 
 
For Voice Chat mode, after joining the room (both team chatting and commander mode), call this API to enable your microphone to collect voice and send it to the network.

2.Function Prototype

  `GCloudVoiceErr OpenMic();  `
  
3.Sample Code

      public void OpenMicBtn_Click()
      {
      	Debug.Log ("Open Mic btn clieck");
      	int ret = m_voiceengine.OpenMic ();
      	PrintLog ("openmic ret=" + ret);
      }  
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode
    GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error.(e.g.the user has not joined the room)
    GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR: Microphone cannot be opened in the big room for users as listeners.
### 3.5 Disable Microphone

1.API Description  

For Voice Chat mode, after joining a room (both Team Chatting and Commander), call this API to disable microphone if you don't want to collect audio and send them to the network anymore.


2.Function Prototype

 ` GCloudVoiceErr CloseMic();  `  

3.Sample Code

      public void CloseMicBtn_Click()
      {
      	Debug.Log ("CoseMic btn click");
      	m_voiceengine.CloseMic ();
      } 
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode
    GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error.(e.g.the user has not joined the room)
    GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR: Microphone cannot be opened or closed in the big room for users as listeners.
### 3.6 Enable Speaker

1.API Description 
 
For Voice Chat mode, after joining a room (both Team Chatting and Commander), call this API to enable speaker to receive and play audio.

2.Function Prototype

 ` GCloudVoiceErr OpenSpeaker();  `  

3.Sample Code

      public void OpenSpeakerBtn_Click()
      {
      	Debug.Log ("OpenSpeaker btn click");
      	int ret = m_voiceengine.OpenSpeaker ();
      	PrintLog ("OpenSpeaker ret=" + ret);
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode
    GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error.(e.g.the user has not joined the room)
### 3.7 Disable Speaker

1.API Description  

For Voice Chat mode, after joining a room (both Team Chatting and Commander), call this API to disable speaker if you don't want to receive and play audio data from the network anymore.


2.Function Prototype

  `GCloudVoiceErr CloseSpeaker();  `  

3.Sample Code

      public void CloseSpeakerBtn_Click()
      {
      	Debug.Log ("Close speaker btn click");
      	m_voiceengine.CloseSpeaker ();
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Chat mode
    GCLOUD_VOICE_REALTIME_STATE_ERR: Voice Chat status error.(e.g.the user has not joined the room)
### 3.8 Callback of joining a room
1.API Description 
 
Notification of successful or failed entry to room will be sent via delegate

2.Function Prototype

      delegate qvoid JoinRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)
      public abstract event JoinRoomCompleteHandler OnJoinRoomComplete;
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  |roomName| string| Name of room to be joined|
  |memberID|int| ID of member joined the room|

3.Sample Code

      m_voiceengine.OnJoinRoomComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string roomName, int memberID) => {
      	PrintLog ("On Join Room With " + code);
      	Debug.Log ("OnJoinRoomComplete ret=" + code + " roomName:" + roomName + " memberID:" + memberID);
      	s_logstr += "\r\n"+"OnJoinRoomComplete ret="+code+" roomName:"+roomName+" memberID:"+memberID;
      	//UIManager.m_Instance.OnJoinRoomDone(code);
      };
### 3.9 Callback of Quitting Room
1.API Description  

Notification of the result of quitting room will be sent via `delegate`.

2.Function Prototype

      delegate void QuitRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)
      public abstract event QuitRoomCompleteHandler OnQuitRoomComplete;
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  |roomName| string| Name of room quitted|
  |memberID|int| ID of member joined the room|

3.Sample Code

      m_voiceengine.OnQuitRoomComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string roomName, int memberID) => {
     	 PrintLog ("On Quit Room With " + code);
      	Debug.Log ("OnQuitRoomComplete ret=" + code + " roomName:" + roomName + " memberID:" + memberID);
      	s_logstr += "\r\n"+"OnJoinRoomComplete ret="+code+" roomName:"+roomName+" memberID:"+memberID;
      	//UIManager.m_Instance.OnJoinRoomDone(code);
      };
### 3.10 Callback of Member Status Changes

1.API Description  

Use this callback to notify member status changes, like starting or stopping speaking

2.Function Prototype

      delegate void MemberVoiceHandler(int[] members, int count) ;
      public abstract event MemberVoiceHandler  OnMemberVoice;
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |members|int[]| Members with status changes.Values show in pairs like [memberID &#124; status].Count pairs in total.The status may be "0" (stop talking), "1" (start talking) and "2" (resume talking).|
  |count|int| Count of members with status changed
3.Sample Code

      m_voiceengine.OnMemberVoice += (int[] members, int count) =>
      {
      	//PrintLog ("OnMemberVoice");
      	//s_logstr +="\r\ncount:"+count;
      	for(int i=0; i < count && (i+1) < members.Length; ++i)
      	{
      		//s_logstr +="\r\nmemberid:"+members[i]+"  state:"+members[i+1];
      		++i;
      	}
      	//UIManager.m_Instance.UpdateMemberState(members, length, usingCount);
      };


