## 1.Instructions
This document describes how to connect Objective-C API SDK for GVoice, which is applicable to games or APPs directly developed on iOS platform.

GVoice provides two major functions, namely, the voice chat (Real-Time) and voice message (Message). The voice chat function enables multiple players to have a voice chat in real time, while the voice message function enables users to make recording rapidly and send a voice message to other players.

Voice chat is divided into two modes, namely the team voice chat and the national war voice chat. If the number of players chatting at the same time in a room is less than 20, it is recommended to use the team voice chat (usually used for communication among team members) for free chatting. If the number above is more than 20, it is recommended to use the national war voice chat (usually used for team battle commands and hosting), which allows developers to control the speaking permission and no more than 5 players to speak at the same time.

Client SDK APIs of GVoice are mainly divided into three parts: the basic API, voice chat API and voice message API.

### 1.1 System Configuration and Basic Usage
[Download IOS SDK](https://cloud.tencent.com/document/product/556/10041)  
[Download IOS Demo](https://cloud.tencent.com/document/product/556/10042)


(1) After downloading and extracting the iOS SDK package, you can obtain a .a file, a .h file and a bundle file. And you can access the APIs by following the procedure below. 1、 Import the following library files and bundle files into Xcode project:
![](https://mc.qcloudimg.com/static/img/b980d0e2ba93fd8ce0884170c6cab596/1.png)

Import the following library files:
![](https://mc.qcloudimg.com/static/img/00705b94a989e2d452846136c971095f/2.png)


The microphone permission needs to be configured in Info for iOS10 and above.

![](https://mc.qcloudimg.com/static/img/4f821f50b9c45118cba2cd17c34f5a94/3.png)


(2) Put the header file "GVoice.h" in a proper place, and initialize the engine.

GVoice uses the singleton method [GVGVGCloudVoice sharedInstance] to obtain sample objects and perform relevant operations. First of all, set the applied information, and then initialize the engine:

    [[GVGCloudVoice sharedInstance] setAppInfo:"your_appid" withKey:"your_appkey" andOpenID:"your_open_id"];
	[[GVGCloudVoice sharedInstance] initEngine];

(3) Before using voice, you need to set the voice mode and carry out callback of delegate.

    [[GVGCloudVoice sharedInstance] setMode:RealTime];

    @interface TeamRoomViewController : UIViewController <GVGCloudVoiceDelegate>
    @end

    #pragma mark delegate

        - (void) onJoinRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID {
        }

        - (void) onStatusUpdate:(enum GCloudVoiceCompleteCode) status withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID {

        }

        - (void) onQuitRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName {
        }

        - (void) onMemberVoice:    (const unsigned int * _Nullable)members withCount: (int) count {
        }

        - (void) onUploadFile: (enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID  {

        }

        - (void) onDownloadFile: (enum GCloudVoiceCompleteCode) code  withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID {

        }

        - (void) onPlayRecordedFile:(enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath {

        }

        - (void) onApplyMessageKey:(enum GCloudVoiceCompleteCode) code {

        }

        - (void) onSpeechToText:(enum GCloudVoiceCompleteCode) code withFileID:(const char * _Nullable)fileID andResult:( const char * _Nullable)result {

        }

        - (void) onRecording:(const unsigned char* _Nullable) pAudioData withLength: (unsigned int) nDataLength {

        }
  
(4) To drive the callback, you need to call Poll function regularly so as to trigger the callback.

For example, you can call Poll function through a timer in the UI thread:

    _pollTimer = [NSTimer scheduledTimerWithTimeInterval:1.000/15 repeats:YES block:^(NSTimer * _Nonnull timer) {
    [[GVGCloudVoice sharedInstance] poll];
    }];
  
(5) Join a room: (you can know whether you have joined a room successful or not in the callback of joining a room).

   `[[GVGCloudVoice sharedInstance] joinTeamRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] timeout:18000];`
  
(6) If the callback indicates that you have joined a room successfully, you can enalbe the microphone and speaker to start a voice chat.

      [[GVGCloudVoice sharedInstance] openSpeaker];

### 1.2 API Calling Process
![](https://mc.qcloudimg.com/static/img/db4301975a4007a65e2b71152e103fd4/4.png)



- Implement callback library GVGCloudVoiceDelegate.  


- Obtain GVGCloudVoice object by calling [GVGCloudVoice sharedInstance] method of GVGCloudVoice.  


- Initialize the object and set the callback.  


- Call the voice chat API or voice message API as required.  


- Call the poll() function where the system tick happens (such as Update of Unity3D ) to run the program.  
### 1.3 Voice Chat API Calling Procedure
![](https://mc.qcloudimg.com/static/img/d7eb0df95ebdff5e8f9d44a8a01bd74f/5.png)



- Set the voice chat mode by calling setMode().


- Use the team voice chat or the national war voice chat based on business needs by calling joinTeamRoom() or joinNationalRoom() respectively.


- If Tick is required, call poll to check the callback. If you succeed or fail to join a room, onJoinRoomComplete() will be called back.


- After joining a room successfully, you can enable the microphone by calling openMic() to capture data and send it to the network.


- Enable the speaker by calling openSpeaker() to receive the audio stream on the network and play it automatically.


- Exit a room by calling QuitRoom() as required. And then onQuitRoomComplete() will be called back.  

Notes:  
In the national war voice chat mode, no more than 5 players can speak at the same time. And additional role information is attached to each user. When joining a room, each user needs to specify himself/herself as a listener or a host.

### 1.4 Offline Voice Chat API Calling Procedure
![](https://mc.qcloudimg.com/static/img/28ec9bf0eab80c06c7883219fbd7604a/6.png)



- Set the voice message mode by calling setMode method.


- Obtain the voice message security key information by calling applyMessageKey(). After the application succeeds, the callback will be carried out via onApplyMessageKeyComplete.


- When recording is required, call startRecording() to record the voice as a file (the file path format is /your path).


- If you want to cancel the recording, call stopRecording API to cancel it.


- After the recording is completed, call uploadRecordedFile to upload the file to GcloudVoice server, during which a ShareFileID will be returned through onUploadReccordFileComplete callback when the file is uploaded successfully. As the unique identifier of this file, this ID is used for file downloading when other users want to listen to it. And the server manages and forwards the ID.


- When the game client needs to listen to other people's audio recording, first of all, it needs to obtain the ShareFileID forwarded by the server, and then download the concerning language file by calling DownloadRecordedFile. The download result will be notified via OnDownloadFile callback. When the downloading is successful, you can call PlayRecordedFile to play the downloaded audio data. Similarly, if you want to cancel the playing, you can call StopPlayFile to cancel it.
### 1.5 Voice-to-text Calling Procedure
![](https://mc.qcloudimg.com/static/img/c0789172ff0ffb679cc9beeb3ba4d18b/7.png)



- Set the translation mode by calling setMode method.


- Obtain the voice message security key information by calling applyMessageKey(). After the application succeeds, the callback will be carried out via onApplyMessageKeyComplete.


- If you want to make recording, call startRecording() to record a voice as a file (the format of file path is /your path).


- If you want to cancel the recording, call stopRecording API to cancel it.


- After the recording is completed, call uploadRecordedFile to upload the file to GcloudVoice server, during which a ShareFileID will be returned through onUploadReccordFileComplete callback when the file is uploaded successfully. As the unique identifier of this file, this ID is used for file downloading when other users want to listen to it. And the server manages and forwards the ID.
To use the translation feature, you need to call speechToText with one important parameter, namely fileid in the last step. After this function is called, the translation result will be notified in the onSpeechToText callback.

Note: The translated fileidIt is generated in the tranlation mode rather than the message mode.

## 2. API Description
### 2.1 Basic APIs
#### 2.1.1 Creating IGcloudVoiceEngine object
(1) API description

This API is used to obtain IGcloudVoiceEngine object when using the voice feature.

(2) Function prototypes

    + (GVGCloudVoice* _Nullable) sharedInstance;
    This function returns a GVGCloudVoice object. And relevant actions can be carried out by calling the API of this object.

(3) Error handling

A NULL object is returned in case of error.

(4) Sample code  
    
    [[GVGCloudVoice sharedInstance] closeMic];

#### 2.1.2 Set business information
(1) API description

This API is used to set the game ID and game key applied previously as well as the unique user identifier OpenID before initialization.

(2) Function prototypes

    - (enum GCloudVoiceErrno) setAppInfo:(const char *_Nullable) appID withKey: (const char *_Nullable)appKey andOpenID:(const char *_Nullable)openID;
    Parameter	Type	Description
    appID	const char *	Game ID on the enabled business page
    appKey	const char *	Game Key on the enabled business page
    openID	const char *	The unique player identifier, such as OpenID obtained from Mobile QQ or WeChat.
    
(3) Return values

	GCloudVoiceErr	If successful, GCLOUD_VOICE_SUCC is returned.
  
(4) Sample code  

    [[GVGCloudVoice sharedInstance] setAppInfo:"93223849489" withKey:"d94749efe9dddfce61333121de84123ef9b" andOpenID:[_openID cStringUsingEncoding:NSUTF8StringEncoding]];

#### 2.1.3 Initializing Engines
(1) API description

This API is used to initialize engines after the business information is configured.

(2) Function prototypes

    - (enum GCloudVoiceErrno) initEngine;

(3) Sample code

    [[GVGCloudVoice sharedInstance] initEngine];

(4) Error handling

GCLOUD_VOICE_NEED_SETAPPINFO: SetAppInfo needs to be called first.    


#### 2.1.4 Setting an engine mode
(1) API description

This API is used to set the mode (offline voice, voice chat or voice-to-text) as the actual voice feature requires. In case of team voice chat or national war voice chat, choose the voice chat mode; in case of voice message, choose the offline voice mode; in case of voice-to-text, choose the translation mode.

(2) Function prototypes

    enum GCloudVoiceMode
    {
    RealTime = 0, // realtime mode for TeamRoom or NationalRoom
    Messages, // voice message mode
    Translation,  // speach to text mode
    };
    (enum GCloudVoiceErrno) setMode:(enum GCloudVoiceMode) mode;
    
    Parameter	Type	Description
    mode	GCloudVoiceMode	In case of team voice chat or national war voice chat, choose the voice chat mode; in case of voice message, choose the offline voice mode; in case of voice-to-text, choose the translation mode.
  
(3) Sample code

    [[GVGCloudVoice sharedInstance] setMode:RealTime];
                                
(4) Error handling

GCLOUD_VOICE_NEED_SETAPPINFO: SetAppInfo needs to be called first.  
  
#### 2.1.5 Querying the trigger event callback
(1) API description

This API is used to trigger event callback by calling Poll periodically in update.

(2) Function prototypes

   ` - (enum GCloudVoiceErrno) poll;`
  
(3) Sample code

_pollTimer = [NSTimer scheduledTimerWithTimeInterval:1.000/15 repeats:YES block:^(NSTimer * _Nonnull timer) {
    [[GVGCloudVoice sharedInstance] poll];
}];
  
(4) Error handling

    GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization. 

#### 2.1.6 The system Pause
(1) API description

This API is used to notify the engine for Pause at the same time the system Pause occurs.

(2) Function prototypes

    - (enum GCloudVoiceErrno) pause;

(3) Error handling

    GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization. 


#### 2.1.7 The system Resume
(1) API description

This API is used to notify the engine for Resume at the same time the system Resume occurs.

(2) Function prototypes

    - (enum GCloudVoiceErrno) resume;

(3) Error handling

    GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.

### 2.2 Voice Chat APIs
#### 2.2.1 Joining the team voice chat
(1) API description

This API is used to join the team voice chat room in order to use the team voice chat feature of the voice chat.

(2) Function prototypes

       - (enum GCloudVoiceErrno) joinTeamRoom:(const char * _Nullable)roomName timeout: (int) msTimeout;
    Parameter	Type	Description
    roomName	const char *	Name of the room to be joined
    msTimeout	int	Timeout when joining the room (in milliseconds)
    The result of joining the room needs to be called back through void OnJoinRoom(GCloudVoiceCompleteCode code, const char *roomName, int memberID).
  
(3) Sample code

     [[GVGCloudVoice sharedInstance] joinTeamRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] timeout:18000];
 
(4) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: It is required to set the voice chat mode by calling SetMode method first.    
GCLOUD_VOICE_PARAM_INVALID: The parameters are invalid. For example, the room name is empty or too long (its maximum length is 127 bytes and it can consist of a-z, A-Z, 0-9, - and _). The timeout range is between 5,000ms and 60,000ms.
GCLOUD_VOICE_REALTIME_STATE_ERR: **The status of Voice Chat is incorrect. For example, though a member has joined a room, he/she has to rejoin this room by calling QuitRoom first.

#### 2.2.2 Joining the national war voice chat
(1) API description

This API is used to join the national war voice chat room in order to use the national voice chat feature.

(2) Function prototypes

        enum GCloudVoiceMemberRole
    {
    Anchor = 1, // member who can open microphone and say
    Audience,   // member who can only hear anchor's voice
    };
    - (enum GCloudVoiceErrno) joinNationalRoom:(const char *_Nullable)roomName role: (enum GCloudVoiceMemberRole) role timeout: (int) msTimeout;   
    Parameter	Type	Description
    roomName	const char *	Name of the room to be joined
    role	GCloudVoiceMemberRole	The member role. Listeners can only listen to voices, but not to send any voice, while hosts can send/listen to voices.
    msTimeout	int	Timeout when joining the room (in milliseconds)
    It is required to call back the result of joining a room through void OnJoinRoom(GCloudVoiceCompleteCode code, const char *roomName, int memberID).

(3) Sample code

    [[GVGCloudVoice sharedInstance] joinNationalRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] role:role timeout:18000]; 

(4) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: It is required to set the voice chat mode by calling SetMode method first.    
GCLOUD_VOICE_PARAM_INVALID: The introduced parameters are incorrect, for example, the room name is empty or too long (its maximum length is 127 bytes and it consists of a-z, A-Z, 0-9, - and _). The time range is between 5,000ms and 60,000ms.
GCLOUD_VOICE_REALTIME_STATE_ERR: The status of the Voice Chat is incorrect. For example, though a member has joined a room, he/she has to rejoin this room by calling QuitRoom first.

#### 2.2.3 Quiting the voice chat
(1) API description

This API is used to quit the voice chat room (including team voice chat room and national war voice chat room) when you do not need it.

(2) Function prototypes

        - (enum GCloudVoiceErrno) quitRoom:(const char * _Nullable)roomName timeout:(int) msTimeout ;  
    Parameter	Type	Description
    roomName	const char *	Name of the room to quit
    msTimeout	int	Timeout when quiting the room (in milliseconds)
    The result of quiting the room needs to be called back through void OnQuitRoom(GCloudVoiceCompleteCode code, const char *roomName).

(3) Sample code

    [[GVGCloudVoice sharedInstance] quitRoom:[_roomID cStringUsingEncoding:NSUTF8StringEncoding] timeout:18000]; 

(4) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the voice chat.   
GCLOUD_VOICE_PARAM_INVALID: The parameters are invalid. For example, the room name is empty or too long (its maximum length is 127 bytes and it can consist of a-z, A-Z, 0-9, - and _). The time range is between 5,000ms and 60,000ms.
GCLOUD_VOICE_REALTIME_STATE_ERR: The status of the voice chat is incorrect, for example, a member has not joined a room.

#### 2.2.4 Enabling the microphone

(1) API description

This API is used to enable the microphone for voice capturing and sending to network after a member joined a room successfully in the voice chat mode (including team voice chat and national war voice chat).

(2) Function prototypes

    - (enum GCloudVoiceErrno) openMic; 
 
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the voice chat.   
GCLOUD_VOICE_REALTIME_STATE_ERR: The status of the voice chat is incorrect, for example, a member has not joined a room.
GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR: The microphone cannot be enabled because the member joined a big room as a listener.

#### 2.2.5 Disabling the microphone
(1) API description

This API is used to disable the microphone when voices do not need to be captured and sent to network after a member joined a room successfully in the voice chat mode (including team voice chat and national war voice chat).

(2) Function prototypes
    
  ` - (enum GCloudVoiceErrno) closeMic;`
   
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the voice chat.   
GCLOUD_VOICE_REALTIME_STATE_ERR: The status of the voice chat is incorrect, for example, a member has not joined a room.
GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR: The microphone cannot be enabled/disabled because the member joined a big room as a listener.


#### 2.2.6 Enabling the speaker

(1) API description: This API is used to enable the speaker for data receiving (from network) and playing after a member joined a room successfully in the voice chat mode (including team voice chat and national war voice chat).

(2) Function prototypes

   `- (enum GCloudVoiceErrno) openSpeaker;`
   
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the voice chat.   
GCLOUD_VOICE_REALTIME_STATE_ERR: The status of the voice chat is incorrect, for example, a member has not joined a room.

#### 2.2.7 Diabling the speaker

(1) API description
This API is used to disable the speaker when voices do not need to be received from network and played after a member joined a room successfully in the voice chat mode (including team voice chat and national war voice chat).

(2) Function prototypes

 `   - (enum GCloudVoiceErrno) closeSpeaker;  `
    
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the voice chat.   
GCLOUD_VOICE_REALTIME_STATE_ERR: The status of the voice chat is incorrect, for example, a member has not joined a room.

#### 2.2.8 Callback of joining a room

(1) API description

This API is used to call back the result of joining a room (successful or failed).

(2) Function prototypes

        - (void) onJoinRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID;
    Parameter	Type	Description
    code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode
    roomName	const char *	Name of the room to be joined
    memberID	int	ID of the member who has joined the room successfully


(3) Sample code

    #pragma mark delegate

    - (void) onJoinRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName andMemberID:(int) memberID {
        NSString *msg;
        if (GV_ON_JOINROOM_SUCC == code) {
            msg = [NSString stringWithFormat:@"Join Room Success"];
        } else {
            msg = [NSString stringWithFormat:@"Join Room Failed with code: %d", code];
        }
        [self warnning:msg];
    }

#### 2.2.9 Callback of quiting a room

(1) API description

This API is used to call back the result of quiting a room.

(2) Function prototypes

        - (void) onQuitRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName
    Parameter	Type	Description
    code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode
    roomName	const char *	Name of the room to quit
    memberID	int	ID of the member who joined the room successfully

(3) Sample code

             - (void) onQuitRoom:(enum GCloudVoiceCompleteCode) code withRoomName: (const char * _Nullable)roomName {
    [_pollTimer invalidate];
    }

#### 2.2.10 Callback of the member status change

(1) API description

This API is used to call back the status change when other members in the room begin to speak or stop speaking.

(2) Function prototypes

    - (void) onMemberVoice:(const unsigned int * _Nullable)members withCount: (int) count
    Parameter	Type	Description
    members	int[]	The member whose status changed. The format of this parameter is a [memberID	status] pair, and there are count pairs in total. The status is individed into 3 types, that is, 0: stop speaking; 1: start to speak; 2: continue to speak.
    count	int	The number of members with changed statuses

(3) Sample code

    - (void) onMemberVoice:    (const unsigned int * _Nullable)members withCount: (int) count {
        for (int i=0; i<count; i++) {
            NSLog(@"Member %d status %d", *((int*)members+2*i), *((int *)members+2*i+1));
        }
    }
### 2.3 Offline Voice Chat API
#### 2.3.1 Applying for the voice message key
(1) API description

This API is used to apply for permission before using the voice message service.

(2) Function prototypes

        - (enum GCloudVoiceErrno) applyMessageKey:(int) msTimeout;
    Parameter	Type	Description
    msTimeout	int	Timeout in milliseconds
    The application result is called back through void OnApplyMessageKey(GCloudVoiceCompleteCode code).

(3) Error handling

GCLOUD_VOICE_PARAM_INVALID: The parameters are incorrect, for example, the timeout range is between 5,000ms and 60,000ms.
GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_AUTHKEY_ERR: Internal error of the voice message key. In such case, you need to contact GCloud team and provide logs for error positioning.
#### 2.3.2 Limiting the voice message length

(1) API description

This API is used to set the maximum length of a voice message in the voice message mode. Default is 2min, that is, a voice message cannot exceed 2 minutes.

(2) Function prototypes

    - (enum GCloudVoiceErrno) setMaxMessageLength:(int) msTime;
    Parameter	Type	Description
    msTimeout	int	The maximum length of a voice message (in milliseconds)

(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_PARAM_INVALID: The parameters are incorrect. And the time range is 1,000ms-1,000*2*60ms.

### 2.3.3 Starting Recording
(1) API description

This API is used to specify a path to save the recording file before recording in the voice message mode.

(2) Function prototypes

    - (enum GCloudVoiceErrno) startRecording:(const char *_Nullable) filePath;
Parameter	Type	Description
filePath	const char *	The path to save the recording file, which is separated by "/" instead of "\".
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the offline voice chat.
GCLOUD_VOICE_PARAM_INVALID: The parameters are incorrect. The path cannot be empty.
GCLOUD_VOICE_NEED_AUTHKEY: GetAuthKey needs to be called first to apply for the permission.
GCLOUD_VOICE_PATH_ACCESS_ERR: The provided path is invalid or non-writable.


#### 2.3.4 Stopping recording
(1) API description

This API is used to stop recording in the voice message mode.

(2) Function prototypes

    - (enum GCloudVoiceErrno) stopRecording;
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the offline voice chat.
GCLOUD_VOICE_NEED_AUTHKEY: GetAuthKey needs to be called first to apply for the permission.  

#### 2.3.5 Uploading a recording file

(1) API description

This API is used to upload a recording file by providing the path of this file after the recording is completed.

(2) Function prototypes
    
       - (enum GCloudVoiceErrno) uploadRecordedFile:(const char *_Nullable) filePath timeout: (int) msTimeout ;
    Parameter	Type	Description
    filePath	const char *	The path to save the recording file, which is separated by "/" instead of "\".
    msTimeout	int	Timeout when uploading a file.
    The uploading result will be called back through void OnUploadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID).
    
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the offline voice chat.
GCLOUD_VOICE_PARAM_INVALID: The parameters are incorrect. The path cannot be empty.
GCLOUD_VOICE_NEED_AUTHKEY: GetAuthKey needs to be called first to apply for the permission.
GCLOUD_VOICE_PATH_ACCESS_ERR: The provided path is invalid or non-readable.
GCLOUD_VOICE_HTTP_BUSY: The last uploading/downloading has not completed. Please try again later.

#### 2.3.6 Downloading a recording file

(1) API description

This API is used to download a recording file by providing the path of this file after the recording is completed.

(2) Function prototypes

        - (enum GCloudVoiceErrno) downloadRecordedFile:(const char *_Nullable)fileID filePath:(const char *_Nullable) downloadFilePath timeout: (int) msTimeout ;
    Parameter	Type	Description
    fileID	const char *	The ID of the file to be downloaded
    downloadFilePath	const char *	The path to save the downloaded recording file, which is separated by "/" instead of "\".
    msTimeout	int	The timeout when downloading a file.
    The downloading result is called back through void OnDownloadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID).

(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the offline voice chat.
GCLOUD_VOICE_PARAM_INVALID: The parameters are incorrect. The path cannot be empty.
GCLOUD_VOICE_NEED_AUTHKEY: GetAuthKey needs to be called first to apply for the permission.
GCLOUD_VOICE_PATH_ACCESS_ERR: The provided path is invalid, non-writable or non-readable.
GCLOUD_VOICE_HTTP_BUSY: The last uploading/downloading has not completed. Please try again later.

#### 2.3.7 Starting to play a downloaded audio file

(1) API description

This API is used to play a downloaded audio file.

(2) Function prototypes

       - (enum GCloudVoiceErrno) playRecordedFile:(const char *_Nullable) downloadFilePath;
    Parameter	Type	Description
    filePath	const char*	The path to save the downloaded recording file, which is separated by "/" instead of "\".
    If the file has been played completely, void OnPlayRecordedFile(GCloudVoiceCompleteCode code,const char *filePath) will be called back.

(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the offline voice chat.
GCLOUD_VOICE_PARAM_INVALID: The parameters are incorrect. The path cannot be empty.
GCLOUD_VOICE_PATH_ACCESS_ERR: The provided path is invalid or non-writable.
GCLOUD_VOICE_SPEAKER_ERR: Failed to enable the microphone.

#### 2.3.8 Stoping playing a downloaded audio file

(1) API description

This API is used to stop playing a downloaded audio file.

(2) Function prototypes

  ` - (enum GCloudVoiceErrno) stopPlayFile;`
   
(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_MODE_STATE_ERR: The current mode is not the offline voice chat.

#### 2.3.9 Callback of applying for the voice message key

(1) API description

This API is used to perform the callback when applying for the voice message permission.

(2) Function prototypes

    - (void) onApplyMessageKey:(enum GCloudVoiceCompleteCode) code
Parameter	Type	Description
code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode

(3) Sample code

   - (void) onApplyMessageKey:(enum GCloudVoiceCompleteCode) code {
NSString *msg;
msg = @"Apply AuthKey Success";
[self warnning:msg];
}
#### 2.3.10 Callback on upload completion
(1) API description

This API is used to call back the result of uploading a voice file.

(2) Function prototypes

        - (void) onUploadFile: (enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID
    Parameter	Type	Description
    code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode
    filepath	const char *	The path of the file to be uploaded
    fileid	const char *	The ID of the file

(3) Sample code

        - (void) onUploadFile: (enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID  {
    _fileID = [NSString stringWithFormat:@"%s", fileID];
    [self warnning:@"Upload Success"];
    }

#### 2.3.11 Callback on download completion

(1) API description

This API is used to call back the result of downloading a voice file.

(2) Function prototypes

      - (void) onDownloadFile: (enum GCloudVoiceCompleteCode) code  withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID 
    Parameter	Type	Description
    code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode
    filepath	const char *	The path of the file to be downloaded
    fileid	const char *	The ID of a file

(3) Sample code

     - (void) onDownloadFile: (enum GCloudVoiceCompleteCode) code  withFilePath: (const char * _Nullable)filePath andFileID:(const char * _Nullable)fileID {
    NSString *msg;
    msg = @"Download File Success";
    [self warnning:msg];
    }

#### 2.3.12 Callback after playing is normally completed

(1) API description

This API is used to perform callback when a voice file has been completely played without any pause.

(2) Function prototypes

       - (void) onPlayRecordedFile:(enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath
    Parameter	Type	Description
    code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode
    filepath	const char *	The path of the file to be played

(3) Sample code

       - (void) onPlayRecordedFile:(enum GCloudVoiceCompleteCode) code withFilePath: (const char * _Nullable)filePath {
    
    NSString *msg;
    msg = @"Finish Play File";
    [self warnning:msg];
    } 

### 2.4 Voice-to-text
#### 2.4.1 Converting voice into text
(1) API description

This API is used to convert voice into text.

(2) Function prototypes

     - (enum GCloudVoiceErrno) speechToText:(const char *_Nullable)fileID timeout:(int) msTimeout language:(enum GCloudLanguage) language ;
    Parameter	Type	Description
    code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode
    fileID	string	The ID of the file to be converted
    result	string	The converted text

(3) Error handling

GCLOUD_VOICE_NEED_INIT: Init needs to be called first for itialization.
GCLOUD_VOICE_STTING: In the process of voice-to-text conversion

(4) Sample code

[[GVGCloudVoice sharedInstance] speechToText:[_fileID cStringUsingEncoding:NSUTF8StringEncoding]  timeout:18000 language:China];

#### 2.4.2 Callback after voice-to-text is completed
(1) API description

This API is used to call back the converted result from voice to text.

(2) Function prototypes

        - (void) onSpeechToText:(enum GCloudVoiceCompleteCode) code withFileID:(const char * _Nullable)fileID andResult:( const char * _Nullable)result
    Parameter	Type	Description
    code	GCloudVoiceCompleteCode	See the definition of GCloudVoiceCompleteCode
    fileID	const char *	The fileid of the converted file
    result	const char *	The converted text
  
(3) Sample code

        - (void) onSpeechToText:(enum GCloudVoiceCompleteCode) code withFileID:(const char * _Nullable)fileID andResult:( const char * _Nullable)result {
    _resultTV.text = [NSString stringWithUTF8String: result];
    }
    
