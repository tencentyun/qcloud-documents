## 1 Overview
Basic APIs are required for both Voice Chat and Voice Message features.

## 2 Call Basic APIs

[1]:https://mc.qcloudimg.com/static/img/d709f155acaeb336df5ee93ddc708105/2.png

**How-To**   
1.Implement `Handler` event entrustment.   
2.Call `GetEngine` to obtain `GCloudVoice` object.   
3.Initialize the object and set callback.     
4.Call Voice Chat API or Voice Message API as required.   
5.Call `Poll()` function to drive the program operation in the `Tick` area (such as `Update` of `Unity3D`) of system.


## 3 Basic API

### 3.1 Obtain `VoiceEngine` Object
1.API Description

Call this API to obtain `VoiceEngine` object

2.Function Prototype

    IGCloudVoice GetEngine()   
    An object of realizing `IGCloudVoice` API  is returned.Relevant actions may be conducted via calling API of this object.

3.Error Codes

   `null` object is returned when error occurs.

4.Sample Code

      //engine have init int mainscene start function
      private IGCloudVoice m_voiceengine = GCloudVoice.GetEngine(); 
### 3.2 Set Business Information
1.API Description

Before initialization, call this API to set information like game ID and key, and user's unique OpenID.

2.Function Prototype

      GCloudVoiceErr SetAppInfo(string appID, string appKey, string openID)
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |appID|string| Game ID as on the service activation page|
  |appKey|string| Game Key as on the service activation page|
  |openID|string| Player unique ID, such as the OpenID obtained via Mobile QQ or WeChat|
  |Return value|GCloudVoiceErr|Return GCLOUD_VOICE_SUCC if operation succeeds|

3.Sample Code

 ` m_voiceengine.SetAppInfo("932849489","d94749efe9fce61333121de84123ef9b","E81DCA1782C5CE8B0722A366D7ECB41F");`
### 3.3 Engine Initialization

1.API Description 
 
Call this API to initialize the engine

2.Function Prototype  

  `GCloudVoiceErr Init();`  

3.Sample Code

      m_voiceengine.SetAppInfo("932849489","d94749efe9fce61333121de84123ef9b","E81DCA1782C5CE8B0722A366D7ECB41F");
      m_voiceengine.Init();
4.Error Codes

   GCLOUD_VOICE_NEED_SETAPPINFO: Need to call `SetAppInfo` first

### 3.4 Set Engine Mode
1.API Description 
   
Call this API to set your engine mode: "Realtime" for Team Chatting and Commander mode; "Message" for Voice Message; "Translation" for Voice-To-Text.

2.Function Prototype

      public enum GCloudVoiceMode
      {
      	RealTime = 0, // realtime mode for TeamRoom or NationalRoom
      	Messages, // voice message mode
      	Translation,  // speach to text mode
      };
      GCloudVoiceErr SetMode(GCloudVoiceMode mode)
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |mode|GCloudVoiceMode| "Realtime" for Team Chatting and Commander mode; "Message" for Voice Message; "Translation" for Voice-To-Text

3.Sample Code

      public void RealTimeBtn_Click()
      {
      	Debug.Log ("realtime button click");
      	m_voiceengine.SetMode (GCloudVoiceMode.RealTime);
      	Application.LoadLevel ("RealTimeVoice");
      }
4.Error Codes

   GCLOUD_VOICE_NEED_SETAPPINFO: Need to call `SetAppInfo` first

### 3.5 Query Trigger Event Callback
1.API Description  

Event callback may be triggered via periodic `Poll` call in `update`.

2.Function Prototype  

  `GCloudVoiceErr Poll()`

3.Sample Code  

      // Update is called once per frame
      void Update () {
      	if (m_voiceengine != null) {
      		m_voiceengine.Poll();
      	}
    
      	m_logtext.text = s_logstr;
      }
4.Error Codes

   GCLOUD_VOICE_NEED_INIT: Call `Init` first for initialization

### 3.6 System `Pause`
1.API Description
  
In case of system `Pause` event, it is necessary to notify the engine of `Pause`.

2.Function Prototype

      GCloudVoiceErr Pause()

3.Sample Code

      public void OnApplicationPause(bool pauseStatus)
      {
      	Debug.Log("Voice OnApplicationPause: " + pauseStatus);
      	if (pauseStatus)
      	{
      		if (m_voiceengine == null)
      		{
     	 		return;
      		}
      		m_voiceengine.Pause();
      	}
      	...
      }
4.Error Codes
    
      GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization

### 3.7 System `Resume`
1.API Description  

In case of system `Resume` event, call this API to notify the engine to `Resume`.

2.Function Prototype

  `GCloudVoiceErr Resume()`  

3.Sample Code  

      public void OnApplicationPause(bool pauseStatus)
      {
      	Debug.Log("Voice OnApplicationPause: " + pauseStatus);
      	if (pauseStatus)
      	{
      	...
     	}
      	else
      	{
      		if (m_voiceengine == null)
      		{
      		return;
      		}
      		m_voiceengine.Resume();
      	}
      }
4.Error Codes  

  GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
