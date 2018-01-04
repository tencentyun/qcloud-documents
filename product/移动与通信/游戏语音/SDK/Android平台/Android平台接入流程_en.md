## 1 Instructions
Client SDK of GcloudVoice runs on both iOS and Android platforms and supports mainstream game engines including Cocos, Unreal, and Unity. It provides C++ APIs on Cocos and Unreal. This document describes how to use JAVA APIs (Android can use C++ APIs as well).

Client SDK of GcloudVoice is mainly featured with voice chat (real-time) and offline voice (message). The voice chat is used for real-time communication in games, such as real-time command in MOBA games (e.g. King of Glory and We MOBA) and FPS games (CrossFire Mobile), so as to sort out the difficulty in non-real-time input on mobile phones. The offline voice is mainly used for message scenarios, such as the global chat in lobbies (Sword of Three Kingdoms) and voice message (email notification).

At the same time, the voice chat is divided into the national war voice chat (such as Legend of Yulong, the national war in MMORGP) and the team voice chat (such as a round in MOBA games and 5V5 in King of Glory). If the number of members in a room is less than 20, it is recommended to use the team voice chat, otherwise it is recommended to use the national war voice chat. With the national war voice chat, the maximum number of speakers at the same time is no more than 5.

The APIs of GcloudVoice's Client SDK are mainly composed of three parts: the basic API, voice chat API and offline voice API.

### 1.1 System Configuration and Basic Usage
[Download Android SDK](https://cloud.tencent.com/document/product/556/10041)  
[Download Android Demo](https://cloud.tencent.com/document/product/556/10042)  

After downloading Android SDK package, you need to import Jar package and SO file to Android project. The connection will be made according to the following procedure. The main work is to import the package as follows.
![](https://mc.qcloudimg.com/static/img/6f5adac586a22176e7f27155c2cb095f/1.png) 
Use the following code    
![](https://mc.qcloudimg.com/static/img/fc862a3b8de404984c173d6d644fa33a/2.png)
to initialize the Java and set the mode.  
![](https://mc.qcloudimg.com/static/img/ce293ff49f4cf57639f686fc8d6f451c/3.png)  
Implement and set the callback: Import the callback API:  
![](https://mc.qcloudimg.com/static/img/0c1626efd6ccaaf610fa75ee1cdb282c/4.png)
Implement the callback library:  
![](https://mc.qcloudimg.com/static/img/1396eee7c8ba16d27fcf55635308c317/5.png)  
Set the callback:  
![](https://mc.qcloudimg.com/static/img/727f245bc232509203aed2b6013adee2/6.png)  
Join a room:  
![](https://mc.qcloudimg.com/static/img/ce985387539c27a80716ab2303f29148/7.png)  
View the callback result of joining the room during the callback:  
![](https://mc.qcloudimg.com/static/img/785a9e54c6c0ec141a936fa5fd64deb8/8.png)  
After joining the room, you can call OpenMic and OpenSpeaker:  
![](https://mc.qcloudimg.com/static/img/d5d36d5bd99d3c09695ef09b489d0e69/9.png)  
  
The specific API calling process can be carried out according to the following detailed description.

### 1.2 Process for Calling API  
![](https://mc.qcloudimg.com/static/img/99e9bffb0f35d7d52d8775cfb47bc6ce/11.png)  
Firstly, carry out the IGCloudVoiceNotify callback and then call GetVoiceEngine to obtain the object of IGCloudVoiceNotify. After that, initialize this object and set the callback. Afterwards, call the voice chat API or the offline voice API as required. And call the callback information among the processed transactions driven by Poll where the system can be ticked (such as Update of Unity3D).

### 1.3 Process for Calling Voice Chat API  
![](https://mc.qcloudimg.com/static/img/b36200d498f8ce1c564f37c592bce125/12.png)  
When using voice chat, you first need to set the voice chat mode by calling SetMode. And judge to join a team voice chat room or a national war voice chat room according to the business logic. Call JoinTeamRoom or JoinNationalRoom according to your choice.

If Tick is required, call poll to check the callback. If you succeed or fail to join a room, the OnJoinRoom method will be called back.

After joining a room, you can call OpenMic to enable the microphone to capture data and send it to the network. After the speaker is enabled by calling OpenSpeaker, it will start to receive the audio stream from the network and play it automatically.

You can call QuitRoom to exit a room when it is required. After the calling, the OnQuitRoom method will be called back.

Note: For the national war voice chat, it is required by the system that the total number of speakers cannot exceed 5. The role information is added to each user. When joining a room, each user should specify himself/herself as a listener or a VJ host.


### 1.4 Process for Calling Offline Voice API  
![](https://mc.qcloudimg.com/static/img/5ff2e43e498ec6e8216b1a878cf501c3/13.png)  
When using voice messages, you need to set the voice message mode by calling SetMode firstly. After that, you need to apply for key information related to offline voice by calling ApplyMessageKey. After the application is successful, the callback will be carried out through OnApplyMessageKey.

When it is required to make a record, you need to call StartRecording API to record the audio into a file (the file path format is file://your path). If you want to cancel the recording, you can call StopRecording API. After the recording is completed, call UploadRecordedFile to upload the file to GcloudVoice server, during which a ShareFileID will be returned through OnUploadFile callback when the file is uploaded successfully. As the unique identifier of this file, this ID is used for file downloading when other users want to listen to it. And the server manages and forwards the ID.

When the game client needs to listen to other people's record, first of all, you need to obtain the ShareFileID forwarded by the server, and then download the record by calling DownloadRecordedFile. The download result will be notified via OnDownloadFile callback. When the download is successful, you can call PlayRecordedFile to play the downloaded voice data. Similarly, if you want to cancel the playing, you can call StopPlayFile.


## 2. API Description
### 2.1 Basic API
#### 2.1.1 Obtain the Object of IGcloudVoiceEngine  
 API: IGCloudVoiceEngine *GetVoiceEngine()   
 Parameter: None   
 Return value: IGcloudVoiceEngine object; when any error occurs, NULL will be returned.  

#### 2.1.2 Set the Applied Information

API: GCloudVoiceErrno SetAppInfo(const char appID,const char appKey, const char *openID)   
Parameter: appID: applied GameID; appKey: applied GameKey; openID: the openID obtained from QQ or WeChat by a game, or the role ID of the only player marked by the game.   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.


#### 2.1.3 Initialize the Applied Information  
API: GcloudVoiceErrno Init()   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

#### 2.1.4 Deinitialization 
API: GcloudVoiceErrno Deinit()   
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

#### 2.1.5 Deinitialization   
API: GCloudVoiceErrno SetNotify(IGCloudVoiceNotify *notify)   
Parameter: notify: the object of the implemented IGCloudVoiceNotify   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

#### 2.1.6 Set the Chat Mode 
API: GcloudVoiceErrno SetMode(GcloudVoiceMode mode)   
Parameter: mode: chat mode of enum GcloudVoiceMode  

    {
     RealTime,  // voice chat
     Messages, // offline voice
    };
     
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

#### 2.1.7 System Pause 
API: GcloudVoiceErrno Pause()  
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

#### 2.1.8 Pause Resume 
API: GcloudVoiceErrno Resume()   
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

#### 2.1.9 Callback Drive - Poll 
API: GcloudVoiceErrno Poll()   
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

### 2.2 Voice Chat API
#### 2.2.1 Join a Team Room 
API: GcloudVoiceErrno JoinTeamRoom(const char *roomName, int msTimeout)   
Parameter: roomName: The room name obtained by the server; if it is not available, the server will automatically create one with the length limit of less than 511. msTimeout: the timeout when joining a room.   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned. The successful return does not mean that you have successfully joined a room here. Whether you have successfully joined a room or not will be called back in OnJoinRoom.

#### 2.2.2 National War Room 
API: GcloudVoiceErrno JoinNationalRoom(const char *roomName, GCloudVoiceMemberRole role, int msTimeout)   
Parameter: roomName: The room name obtained by the server; if it is not available, the server will automatically create one; role: the role of a user as a listener or VJ host; msTimeout: the timeout when joining a room.   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned. The successful return does not mean that you have successfully joined a room here. Whether you have successfully joined a room or not will be called back in OnJoinRoom.

#### 2.2.3 Exit a Room 
API: GcloudVoiceErrno QuitRoom()   
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned. You will exit the room which you have joined (the team room or the national war room).

#### 2.2.4 Enable the Microphone to Start Recording 
API: GcloudVoiceErrno OpenMic()   
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

#### 2.2.5 Disable the Microphone to Stop Recording 
API: GcloudVoiceErrno CloseMic()   
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

#### 2.2.6 Enable the Speaker to Start Playing 
API: GcloudVoiceErrno OpenSpeaker()   
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

#### 2.2.7 Disable the Speaker to Stop Playing 
APIs: GcloudVoiceErrno CloseSpeaker()    
Parameter: None   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.

### 2.3 Offline Voice API  
#### 2.3.1 Apply for AuthKey    
API: GCloudVoiceErrno ApplyMessageKey(int msTimeout)   
Parameters: msTimeout   
Return values: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned. The success here does not mean your application for a Hong Kong key is successful, while it is required to make a callback in OnApplyMessageKey.  

#### 2.3.2 Start Recording 
API: GcloudVoiceErrno StartRecording (const char * filePath)   
Parameter: filePath: the location of saving a file in the format of "Save as"; "you_dir/your_filename": the file path needs to be separated by a backslash "/".   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

#### 2.3.3 Cancel the Recording 
API: GcloudVoiceErrno StopRecording ()   
Parameter: None  
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

#### 2.3.4 Send an Audio File 
API: GcloudVoiceErrno UploadRecordedFile (const char * filePath)   
Parameter: filePath: the given path when recording   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

#### 2.3.5 Download an Audio File 
API: GcloudVoiceErrno DownloadRecordedFile (const char fileID, const char downloadFilePath, int msTimeout)     
Parameter: fileID: the ID of a file to be downloaded; downloadFilePath: the location of a file to be downloaded with the format as shown above; msTimeout: the timeout.     
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

#### 2.3.6 Play a Downloaded Audio File 
API: GcloudVoiceErrno PlayRecordedFile (const char * downloadFilePath)   
Parameter: DownloadFilePath: the location of a file to be downloaded.   
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.  

#### 2.3.7 Cancel the Playing 
API: GcloudVoiceErrno StopPlayFile ()     
Parameter: None     
Return value: For a successful operation, GcloudVoiceErrno::GCLOUD_VOICE_SUCC will be returned; otherwise, other error code will be returned.    

## 2.4 Callback API  

#### 2.4.1 Results of Joining a Room 
API: void OnJoinRoom(GCloudVoiceCompleteCode code, char *roomName, int memberID)    
Parameter: code: the result of joining a room; enum GcloudVoiceCompleteCode.  
  {
      GV_ON_JOINROOM_SUCC,         // Joined a room successfully
      GV_ON_JOINROOM_TIMEOUT,    // Timeout in joining the room
      GV_ON_JOINROOM_FAIL,        // Other errors occur when joining the room
  };
roomName: the name of the room to be joined; memberID: the ID of a member.  
Return value: None  

#### 2.4.2 Results of Exiting a Room 
API: void OnQuitRoom(GCloudVoiceCompleteCode code, const char *roomName)   
Parameter: code: the result of joining a room; enum GcloudVoiceCompleteCode.

  {
      GV_ON_JOINROOM_SUCC,         // Joined a room successfully
      GV_ON_JOINROOM_TIMEOUT,    // Timeout in joining the room
      GV_ON_JOINROOM_FAIL,        // Other errors occur when joining the room
  };
roomName: the name of the room to be joined   
Return value: None

#### 2.4.3 Voice Status Changes of Other Members 
API: void OnMemberVoice (const int members, int length)   
Parameter: members: members and their statuses in the format of a pair of memberID and status; status value = 0: which means the status changes from speaking to non-speaking; status vale = 1: which means the status changes from non-speaking to speaking; status value = 2: which means the status changes from speaking to speaking again; length: the number of members with the length of the member array of 2.   
Return value: None

#### 2.4.4 Callback of the File Sending Status 
API: void OnUploadFile(GCloudVoiceCompleteCode code, const char filePath, const char fileID)   
Parameter: filePath: the location of a file to be saved, which is the same with that of sending; fileID: the only marked ID code of a file; the error code if any error occurs.   
Return value: None

#### 2.4.5 Callback of the File Downloading Status 
API: void OnDownloadFile(GCloudVoiceCompleteCode code, const char filePath, const char fileID  )   
Parameters: filePath: the location of a file to be saved, which is the same with that of down[PI1]loading; fileID: the only marked ID code of a file and the error code if any error occurs.   
Return value: None  

#### 2.4.6 Callback of Key Applying   
API: void OnApplyMessageKey(GCloudVoiceCompleteCode code)   
Parameter: code: the error code if any error occurs.   
Return value: None  

#### 2.4.7 Callback after Playing a File   
API: void OnPlayRecordedFile(GCloudVoiceCompleteCode code,const char *filePath)    
Parameter: code: the error code if any error occurs; filePath: the location of a file to be played.   
Return value: None  



