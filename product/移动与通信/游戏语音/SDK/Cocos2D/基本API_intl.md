## 1 Overview
Basic APIs are required for both Voice Chat and Voice Message features.

## 2 Call Basic APIs

[1]:https://mc.qcloudimg.com/static/img/9732bfc1f2b2adb4995c59329a7ead52/1.png
**How-To**  
1. Implement `IGcloudVoiceNotify` callback class  
2. Call `GetVoiceEngine` to obtain `IGcloudVoiceEngine` object  
3. Initialize the object and set callback  
4. Call Voice Chat API or Voice Message API as required
5. Call `Poll()` function to drive the program operation in the `Tick` area (such as `Update` of `Unity3D`) of system 



## 3 Basic APIs

### 3.1 Create `IGcloudVoiceEngine` object
1. API Description

	Call this API to get `VoiceEngine` object.

2. Function Prototype

    IGCloudVoiceEngine *GetVoiceEngine()
    This function returns an `IGcloudVoiceEngine` object. Call API of this object to conduct related actions.

3. Sample Code

      private IGCloudVoiceEngine* m_voiceengine = gcloud_voice::GetVoiceEngine(); 

4. Error Codes  
   NULL object is returned when error occurs.

### 3.2 Set Business Information
1. API Description

	Before initialization, call this API to set information like game ID and key, and user's unique OpenID.

2. Function Prototype

  	` GCloudVoiceErrno SetAppInfo(const char *appID,const char *appKey, const char *openID)`

  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|appID|const char *| Game ID as on the service activation page|
  	|appKey|const char *| Game Key as on the service activation page|
  	|openID|const char *| Player unique ID, such as the OpenID obtained via Mobile QQ or WeChat|
  	|Return value|GCloudVoiceErr|Return GCLOUD_VOICE_SUCC if operation succeeds|

3. Sample Code

 	 `gcloud_voice::GetVoiceEngine()->SetAppInfo("932849489","d94749efe9fce61333121de84123ef9b","E81DCA1782C5CE8B0722A366D7ECB41F");`
### 3.3 Engine Initialization

1. API Description

	After setting your business information, call this API to initialize the engine.

2. Function Prototype  

  	`GCloudVoiceErr Init();`  

3. Sample Code

  	`gcloud_voice::GetVoiceEngine()->Init();`

4. Error Codes  
GCLOUD_VOICE_NEED_SETAPPINFO: Need to call SetAppInfo first

### 3.4 Set Engine Mode
1. API Description

	Call this API to set your engine mode: "Realtime" for Team Chatting and Commander mode; "Message" for Voice Message; "Translation" for Voice-To-Text.

2. Function Prototype

      enum GCloudVoiceMode
      {
      	RealTime = 0, // realtime mode for TeamRoom or NationalRoom
      	Messages, // voice message mode
      	Translation,  // speach to text mode
      };
      GCloudVoiceErr SetMode(GCloudVoiceMode mode)

  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|mode|GCloudVoiceMode| "Realtime" for Team Chatting and Commander mode; "Message" for Voice Message; "Translation" for Voice-To-Text
3. Sample Code

            gcloud_voice::GetVoiceEngine()>SetMode(gcloud_voice::IGCloudVoiceEngine::RealTime);
4. Error Codes

	GCLOUD_VOICE_NEED_SETAPPINFO: Need to call `SetAppInfo` first

### 3.5 Query Trigger Event Callback
1. API Description  

	Event callback may be triggered via periodic `Poll` call in `update`.

2. Function Prototype  
	`GCloudVoiceErr Poll()`

3. Sample Code  

      // Update is called timer
      void TeamRoomSection::update(float delta)
      {
      	gcloud_voice::GetVoiceEngine()->Poll();
      }
4. Error Codes  

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization

### 3.6 `Pause` of System
1. API Description

	In case of system `Pause` event, call this API to notify the engine of `Pause`.

2. Function Prototype

  	`GCloudVoiceErr Pause()`

3. Sample Code

      public void OnApplicationPause(bool pauseStatus)
      {
      	gcloud_voice::GetVoiceEngine()->Pause();
      }
4. Error Codes  

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization

### 3.7 System `Resume`
1. API Description  

	In case of system `Resume` event, call this API to notify the engine to `Resume`.

2. Function Prototype

  	`GCloudVoiceErr Resume()`  

3. Sample Code  

      public void OnApplicationPause(bool pauseStatus)
      {
      	gcloud_voice::GetVoiceEngine()->Resume();
      }
4. Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization

