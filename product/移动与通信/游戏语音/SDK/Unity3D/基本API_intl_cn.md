## 1 概述
无论使用实时语音，还是语音消息，都需要调用基本API。

## 2 基本API调用流程

![](https://mc.qcloudimg.com/static/img/d709f155acaeb336df5ee93ddc708105/2.png)

**流程说明**   
1.实现相关`Handler`的事件委托。  
2.调用`GetEngine`获取`GCloudVoice`对象。  
3.对该对象进行初始化操作并设置回调。  
4.根据需要调用实时语音接口或语音消息接口。  
5.在系统可以`Tick`的地方（如`Unity3D`的`Update`）调用`Poll()`函数驱动程序运行。 


## 3 基本API

### 3.1 获取VoiceEngine对象
1.接口说明

在使用语音功能时，需要首先获取VoiceEngine对象 。

2.函数原型

    IGCloudVoice GetEngine()   
    该函数返回一个实现了IGCloudVoice接口的对象，通过调用该对象的接口，可以执行相关动作。

3.出错处理

   `出错时，返回null对象`

4.示例代码

      //engine have init int mainscene start function
      private IGCloudVoice m_voiceengine = GCloudVoice.GetEngine(); 
### 3.2 设置业务信息
1.接口说明

在初始化之前，需要设置之前申请的游戏ID和游戏Key以及用户的唯一标示OpenID。

2.函数原型

      GCloudVoiceErr SetAppInfo(string appID, string appKey, string openID)
    
  |参数|类型|意义|
  |--|--|--|
  |appID|string| 开通业务页面中的游戏ID|
  |appKey|string| 开通业务页面中的游戏Key|
  |openID|string| 玩家唯一标示，比如从手Q或者微信获得到的OpenID|
  |返回值|GCloudVoiceErr|成功时返回GCLOUD_VOICE_SUCC|

3.示例代码

 ` m_voiceengine.SetAppInfo("932849489","d94749efe9fce61333121de84123ef9b","E81DCA1782C5CE8B0722A366D7ECB41F");`
### 3.3 初始化引擎

1.接口说明 
 
在设置好业务信息后就可以开始初始化引擎了。

2.函数原型  

  `GCloudVoiceErr Init();`  

3.示例代码

      m_voiceengine.SetAppInfo("932849489","d94749efe9fce61333121de84123ef9b","E81DCA1782C5CE8B0722A366D7ECB41F");
      m_voiceengine.Init();
4.出错处理

   `GCLOUD_VOICE_NEED_SETAPPINFO ： 需要先调用SetAppInfo`

### 3.4 设置引擎模式
1.接口说明 
   
在使用语音功能时，需要根据需要设置成离线、实时还是转文字的模式。如果是小队语音或者国战语音，设置成实时模式；如果是语音消息，设置成离线模式；如果是语音转文字，设置成翻译模式。

2.函数原型

      public enum GCloudVoiceMode
      {
      	RealTime = 0, // realtime mode for TeamRoom or NationalRoom
      	Messages, // voice message mode
      	Translation,  // speach to text mode
      };
      GCloudVoiceErr SetMode(GCloudVoiceMode mode)
    
  |参数|类型|意义|
  |--|--|--|
  |mode|GCloudVoiceMode| 如果是小队语音或者国战语音，设置成实时模式；如果是语音消息，设置成离线模式；如果是语音转文字，设置成翻译模式|

3.示例代码

      public void RealTimeBtn_Click()
      {
      	Debug.Log ("realtime button click");
      	m_voiceengine.SetMode (GCloudVoiceMode.RealTime);
      	Application.LoadLevel ("RealTimeVoice");
      }
4.出错处理

   `GCLOUD_VOICE_NEED_SETAPPINFO ：需要先调用SetAppInfo`

### 3.5 查询触发事件回调
1.接口说明  

通过在update里面周期的调用Poll可以触发事件回调

2.函数原型  

  `GCloudVoiceErr Poll()`

3.示例代码  

      // Update is called once per frame
      void Update () {
      	if (m_voiceengine != null) {
      		m_voiceengine.Poll();
      	}
    
      	m_logtext.text = s_logstr;
      }
4.出错处理

   `GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化`

### 3.6 系统发生Pause
1.接口说明
  
当系统发生Pause事件时，需要同时通知引擎进行Pause

2.函数原型

      GCloudVoiceErr Pause()

3.示例代码

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
4.出错处理
    
      GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化

### 3.7 系统发生Resume
1.接口说明  

当系统发生Resume事件时，需要同时通知引擎进行Resume

2.函数原型

  `GCloudVoiceErr Resume()`  

3.示例代码  

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
4.出错处理  

  `GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化`
