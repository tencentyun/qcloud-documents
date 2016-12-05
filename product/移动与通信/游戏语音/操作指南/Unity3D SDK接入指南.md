本文档介绍了GVoice游戏语音C#接口SDK的接入方法，适用于Unity3D引擎开发的游戏。
## 1 下载SDK
[下载Unity3D SDK包](https://mc.qcloudimg.com/static/archive/c185768d0f00929468930d89846e9573/gcloud_voice_1_1_2_133767_20161117_Unity3D.zip)  
下载SDK包解压后，目录结构如下： 
![](https://mc.qcloudimg.com/static/img/ef63d54941048e51fdaf9c023fa8be2f/image.jpg)
## 2 系统配置
### 2.1 iOS系统配置
1.将压缩包中的 `dist\Unity3D\Plugins\iOS\ GCloudVoice.bundle` 整个文件夹拷贝到自己的工程 `MyProj\Assets\Plugins\iOS` 目录下。  
2.链接发布包中静态库`dist\Unity3D\Plugins\iOS\libGCloudVoice.a`，在`Unity3d`导出的`Xcode`工程中，同时需要链接如下6个系统库：

![](https://mc.qcloudimg.com/static/img/a6b6942b66e94582145b89b224ce6f5f/ios.jpg)

### 2.2 Android系统

1.将压缩包中的 `dist\Unity3D\Plugins\Android` 目录下的 `GCloudVoice`、`assets`两个文件夹拷贝到自己的工程`MyProj\Assets\Plugins\Android`目录下。  
2.将压缩包中的 `dist\Unity3D\Scripts\GCloudVoice` 目录下的`cs`脚本文件，拷贝到工程`Scripts`文件夹中，使用即可。注意，使用时命名空间为`gcloud_voice`。  
3.在游戏主`Activiy`的`OnCreate`函数处，添加`Java`层的`Init`代码。 导入类：`import com.tencent.gcloud.voice.GCloudVoiceEngine;` 调用`Init`代码：     

![](https://mc.qcloudimg.com/static/img/bdea05411bb37424592d69a76dc595e7/image.jpg)

## 3流程概述
### 3.1 接口调用流程

![](https://mc.qcloudimg.com/static/img/e92b02b285664c7d54170b901cea51f1/j1.png)

**流程说明**   
1.实现相关`Handler`的事件委托。  
2.调用`GetEngine`获取`GCloudVoice`对象。  
3.对该对象进行初始化操作并设置回调。  
4.根据需要调用实时语音接口或语音消息接口。  
5.在系统可以`Tick`的地方（如`Unity3D`的`Update`）调用`Poll()`函数驱动程序运行。 

### 3.2 实时语音接口调用流程 
![](https://mc.qcloudimg.com/static/img/69e8fafb64190a5ddc1f18a954d977ce/j2.png)

**流程说明**   
1.调用`SetMode()`方法设置使用实时语音模式。  
2.根据业务需求使用小队语音或国战语音，分别调用`JoinTeamRoom()`或`JoinNationalRoom()`。  
3.需要`Tick`的调用`poll`来检查回调，当加入房间成功或者失败时，会回调`OnJoinRoomComplete()`方法。  
4.加入房间成功后，就可以调用`OpenMic()`打开麦克风进行采集并发送到网络。  
5.调用`OpenSpeaker()`打开扬声器，开始接受网络上的音频流并自动进行播放。  
6.当需要退出房间时，调用`QuitRoom()`即可，成功后会回调`OnQuitRoomComplete()`方法。  

**注意**  
对于国战语音，系统要求说话人数不能超过5个人，每个用户多了一个角色信息，在加入房间的时候需要指定是以听众的身份加入还是以主播的身份加入。

### 3.3 离线语音接口调用流程
 
![](https://mc.qcloudimg.com/static/img/f3de36c0e998cb98d4085ede1879e65d/j3.jpg)

**流程说明  **
1.调用`SetMode`方法设置使用语音消息模式。  
2.调用`ApplyMessageKey()`获取语音消息安全密钥key信息，当申请成功后会通过`OnApplyMessageKeyComplete`进行回调。    
3.当需要录音时，调用`StartRecording()`录制音频到文件中（文件的路径格式是`/your path`）。  
4.如果想取消录制可以调用`StopRecording`接口进行取消。  
5.当录制完成后，调用`UploadRecordedFile()`将文件上传到`GcloudVoice`的服务器上，该过程会通过`OnUploadReccordFileComplete()`回调在上传成功的时候返还一个`ShareFileID`.该ID是这个文件的唯一标识符，用于其他用户收听时候的下载。服务器需要对其进行管理和转发。  
6.当游戏客户端需要收听其他人的录音时，首先从服务器获取转发的`ShareFileID`，然后调用`DownloadRecordedFile`下载该语言文件，下载结果通过`OnDownloadRecordFileComplete`回调来通知。当下载成功时，就可以调用`PlayRecordedFile`播放下载完成的语音数据了。同样的，如果想取消播放，可以调用`StopPlayFile`进行取消。
## 4 接口说明
GVoice客户端SDK接口主要分成三个部分：基本API、实时语音API、语音消息API。
### 4.1 基本API

#### 4.1.1 获取VoiceEngine对象
1.接口说明

在使用语音功能时，需要首先获取VoiceEngine对象 。

2.函数原型

    IGCloudVoice GetEngine()   
    该函数返回一个实现了IGCloudVoice接口的对象，通过调用该对象的接口，可以执行相关动作。

3.出错处理

    出错时，返回null对象

4.示例代码

      //engine have init int mainscene start function
      private IGCloudVoice m_voiceengine = GCloudVoice.GetEngine(); 
#### 4.1.2 设置业务信息
1.接口说明

在初始化之前，需要设置之前申请的游戏ID和游戏Key以及用户的唯一标示OpenID。

2.函数原型

      GCloudVoiceErr SetAppInfo(string appID, string appKey, string openID)
    
  参数|类型|意义  
  ---|---|---
  appID|string| 开通业务页面中的游戏ID  
  appKey|string| 开通业务页面中的游戏Key  
  openID|string| 玩家唯一标示，比如从手Q或者微信获得到的OpenID  
  返回值|GCloudVoiceErr|成功时返回GCLOUD_VOICE_SUCC    

3.示例代码

 ` m_voiceengine.SetAppInfo("932849489","d94749efe9fce61333121de84123ef9b","E81DCA1782C5CE8B0722A366D7ECB41F");`
#### 4.1.3 初始化引擎

1.接口说明 
 
在设置好业务信息后就可以开始初始化引擎了。

2.函数原型  

  `GCloudVoiceErr Init();`  

3.示例代码

      m_voiceengine.SetAppInfo("932849489","d94749efe9fce61333121de84123ef9b","E81DCA1782C5CE8B0722A366D7ECB41F");
      m_voiceengine.Init();
4.出错处理


    GCLOUD_VOICE_NEED_SETAPPINFO ： 需要先调用SetAppInfo
#### 4.1.4 设置引擎模式
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
    
  参数|类型|意义
  ---|---|---
  mode|GCloudVoiceMode| 如果是小队语音或者国战语音，设置成实时模式；如果是语音消息，设置成离线模式；如果是语音转文字，设置成翻译模式

3.示例代码

      public void RealTimeBtn_Click()
      {
      	Debug.Log ("realtime button click");
      	m_voiceengine.SetMode (GCloudVoiceMode.RealTime);
      	Application.LoadLevel ("RealTimeVoice");
      }
4.出错处理

    GCLOUD_VOICE_NEED_SETAPPINFO ：需要先调用SetAppInfo
#### 4.1.5 查询触发事件回调
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

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
#### 4.1.6 系统发生Pause
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
#### 4.1.7 系统发生Resume
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

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
### 4.2 实时语音API

### 4.2.1 加入小队语音
1.接口说明 
 
使用实时语音的小队语音功能时，需要先加入小队语音房间

2.函数原型

      GCloudVoiceErr JoinTeamRoom(string roomName, int msTimeout)   
    
  参数|类型| 意义
  ---|---|---
  roomName|string| 要加入的房间名 
  msTimeout|int| 加入房间的超时时间，单位是毫秒
   加入房间的结果，需要通过delegate void JoinRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)进行回调

3.示例代码

      public void JoinRoomBtn_Click()
      {
      	Debug.Log ("JoinRoom Btn Click");
    
      	int ret = m_voiceengine.JoinTeamRoom(m_roomName, 15000);
      	PrintLog ("joinroom ret=" + ret);
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 需要先调用SetMode设置成实时模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，比如房间名为空或者超长（最大长度127字节）且由a-z,A-Z,0-9,-,_组成。超时范围5000ms-60000ms。
    GCLOUD_VOICE_REALTIME_STATE_ERR ： 实时语音状态不对，比如已经加入房间了，需要先调用QuitRoom才能再次加入
### 4.2.2 加入国战语音

1.接口说明  
  
使用国战语音功能时，需要先加入国战语音房间

2.函数原型

      public enum GCloudVoiceRole
      {
      ANCHOR = 1, // member who can open microphone and say
      AUDIENCE,   // member who can only hear anchor's voice
      }
      GCloudVoiceErr JoinNationalRoom(string roomName, GCloudVoiceRole role, int msTimeout)   
    
  参数|类型| 意义
  ---|---|---
  roomName|string| 要加入的房间名 
  role|GCloudVoiceRole| 成员加入的角色，听众只能收听语音不能发送语音，而主播既可以发送语音也可以收听语音
  msTimeout|int| 加入房间的超时时间，单位是毫秒

加入房间的结果，需要通过delegate void JoinRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)进行回调

3.示例代码

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
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 需要先调用SetMode设置成实时模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，比如房间名为空或者超长（最大长度127字节）且由a-z,A-Z,0-9,-,_组成。超时范围5000ms-60000ms。
    GCLOUD_VOICE_REALTIME_STATE_ERR ： 实时语音状态不对，比如已经加入房间了，需要先调用QuitRoom才能再次加入
### 4.2.3 退出实时语音
1.接口说明  

当不需要使用实时语音，可以从实时语音（包括小队语音和国战语音）房间中退出。

2.函数原型

      GCloudVoiceErr QuitRoom(string roomName, int msTimeout);  
    
  参数|类型| 意义
  ---|---|---
  roomName|string| 要退出的房间名   
  msTimeout|int| 退出房间的超时时间，单位是毫秒
退出房间的结果，需要通过delegate void QuitRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)进行回调

3.示例代码  

      public void QuitRoomBtn_Click()
      {
      Debug.Log ("quit room btn click");
      m_voiceengine.QuitRoom(m_roomName, 15000);
      }   
4.出错处理  

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是实时语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，比如房间名为空或者超长（最大长度127字节）且由a-z,A-Z,0-9,-,_组成。超时范围5000ms-60000ms。
    GCLOUD_VOICE_REALTIME_STATE_ERR ： 实时语音状态不对，比如还没有加入房间
### 4.2.4 打开麦克风

1.接口说明 
 
在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），需要打开麦克风才能采集音频并发送到网络

2.函数原型

  `GCloudVoiceErr OpenMic();  `
  
3.示例代码

      public void OpenMicBtn_Click()
      {
      	Debug.Log ("Open Mic btn clieck");
      	int ret = m_voiceengine.OpenMic ();
      	PrintLog ("openmic ret=" + ret);
      }  
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是实时语音模式
    GCLOUD_VOICE_REALTIME_STATE_ERR ： 实时语音状态不对，比如还没有加入房间
    GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR ： 当前以听众身份加入的大房间，不能开麦
### 4.2.5 关闭麦克风

1.接口说明  

在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），当不需要采集音频并发送到网络，可以调用关闭麦克风接口

2.函数原型

 ` GCloudVoiceErr CloseMic();  `  

3.示例代码

      public void CloseMicBtn_Click()
      {
      	Debug.Log ("CoseMic btn click");
      	m_voiceengine.CloseMic ();
      } 
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是实时语音模式
    GCLOUD_VOICE_REALTIME_STATE_ERR ： 实时语音状态不对，比如还没有加入房间
    GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR ： 当前以听众身份加入的大房间，不能开麦关麦
### 4.2.6 打开扬声器

1.接口说明 
 
在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），需要打开扬声器才能从网络接收数据并播放

2.函数原型

 ` GCloudVoiceErr OpenSpeaker();  `  

3.示例代码

      public void OpenSpeakerBtn_Click()
      {
      	Debug.Log ("OpenSpeaker btn click");
      	int ret = m_voiceengine.OpenSpeaker ();
      	PrintLog ("OpenSpeaker ret=" + ret);
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是实时语音模式
    GCLOUD_VOICE_REALTIME_STATE_ERR ： 实时语音状态不对，比如还没有加入房间
### 4.2.7 关闭扬声器

1.接口说明  

在实时语音的模式下，加入房间成功后（包括小队语音和国战语音），当不需要从网络接收数据并播放时，可以调用关闭麦克风接口

2.函数原型

  `GCloudVoiceErr CloseSpeaker();  `  

3.示例代码

      public void CloseSpeakerBtn_Click()
      {
      	Debug.Log ("Close speaker btn click");
      	m_voiceengine.CloseSpeaker ();
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是实时语音模式
    GCLOUD_VOICE_REALTIME_STATE_ERR ： 实时语音状态不对，比如还没有加入房间
### 4.2.8 加入房间回调
1.接口说明 
 
当加入房间成功或者失败时会通过delegate进行通知

2.函数原型

      delegate qvoid JoinRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)
      public abstract event JoinRoomCompleteHandler OnJoinRoomComplete;
    
  参数|类型|意义
  ---|---|---
  code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义  
  roomName| string| 加入的房间名  
  memberID|int| 如果加入成功的话，表示加入后的成员ID  

3.示例代码

      m_voiceengine.OnJoinRoomComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string roomName, int memberID) => {
      	PrintLog ("On Join Room With " + code);
      	Debug.Log ("OnJoinRoomComplete ret=" + code + " roomName:" + roomName + " memberID:" + memberID);
      	s_logstr += "\r\n"+"OnJoinRoomComplete ret="+code+" roomName:"+roomName+" memberID:"+memberID;
      	//UIManager.m_Instance.OnJoinRoomDone(code);
      };
### 4.2.9 退出房间回调
1.接口说明  

当退出房间时，结果通过delegate进行通知

2.函数原型

      delegate void QuitRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)
      public abstract event QuitRoomCompleteHandler OnQuitRoomComplete;
    
  参数|类型| 意义
  ---|---|---
  code|GCloudVoiceCompleteCode| 参见GCloudVoiceCompleteCode定义
  roomName| string| 退出的房间名
  memberID|int| 如果加入成功的话，表示加入后的成员ID

3.示例代码

      m_voiceengine.OnQuitRoomComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string roomName, int memberID) => {
     	 PrintLog ("On Quit Room With " + code);
      	Debug.Log ("OnQuitRoomComplete ret=" + code + " roomName:" + roomName + " memberID:" + memberID);
      	s_logstr += "\r\n"+"OnJoinRoomComplete ret="+code+" roomName:"+roomName+" memberID:"+memberID;
      	//UIManager.m_Instance.OnJoinRoomDone(code);
      };
### 4.2.10 成员状态改变回调

1.接口说明  

当房间中的其他成员开始说话或者停止说话的时候，通过该回调进行通知

2.函数原型

      delegate void MemberVoiceHandler(int[] members, int count) ;
      public abstract event MemberVoiceHandler  OnMemberVoice;
    
  参数| 类型| 意义
  ---|---|---
  members|int[]|改变状态的member成员，其值为[memberID &#124; status]这样的对，总共有count对，status有“0”：停止说话; “1”：开始说话; “2”:继续说话。
  count|int| 改变状态的成员的数目
3.示例代码

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
###4.3 离线语音API

### 4.3.1 申请语音消息key
1.接口说明  

在语音消息的模式下，需要先申请许可才可以正常使用

2.函数原型

      GCloudVoiceErr ApplyMessageKey(int msTimeout)
    
  参数|类型|意义
  ---|---|---
  msTimeout|itn|超时时间，单位毫秒  
    
申请的结果通过delegate void ApplyMessageKeyCompleteHandler(GCloudVoiceCompleteCode code);进行回调  

3.示例代码

      m_voiceengine.OnApplyMessageKeyComplete += (IGCloudVoice.GCloudVoiceCompleteCode code) => {
      	Debug.Log ("OnApplyMessageKeyComplete c# callback");
      	s_strLog += "\r\n"+"OnApplyMessageKeyComplete ret="+code;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_MESSAGE_KEY_APPLIED_SUCC) {
      		Debug.Log ("OnApplyMessageKeyComplete succ11");
      	} else {
      		Debug.Log ("OnApplyMessageKeyComplete error");
      	}
      };
4.出错处理

    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，比如超时范围5000ms-60000ms。
    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_AUTHKEY_ERR ： 请求Key的内部错误，此时需要联系GCloud团队，并提供日志进行定位
### 4.3.2 限制最大语音消息的长度
1.接口说明 
 
在语音消息的模式下，可以限制最大语音消息的长度，目前默认是2min，最大不超过2min。

2.函数原型

      GCloudVoiceErr SetMaxMessageLength(int msTime)
    
  参数|类型|意义
  ---|---|---
  msTimeout|itn|最大语音消息长度，单位毫秒  
3.示例代码

      int ret1 = m_voiceengine.SetMaxMessageLength (60000);
      Debug.Log ("SetMaxMessageLength ret==" + ret1);
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，时间范围1000ms-1000260ms。
### 4.3.3 开始录音
1.接口说明  

在语音消息的模式下，开始录音时，需要提供一个录音文件存储的地址路径

2.函数原型

      GCloudVoiceErr StartRecording(string filePath)
    
  参数|类型|意义
  ---|---|---
  filePath|string|录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\"  
3.示例代码

      public void Click_btnStartRecord()
      {
      	Debug.Log("startrecord btn click, recordpath="+m_recordpath);
      	m_voiceengine.StartRecording (m_recordpath);
    
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写
### 4.3.4 停止录音
1.接口说明  

在语音消息的模式下，调用停止录音接口会

2.函数原型

      GCloudVoiceErr StopRecording()
3.示例代码

      public void Click_btnStopRecord()
      {
      	Debug.Log("stoprecord btn click");
      	m_voiceengine.StopRecording ();
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
### 4.3.5 上传录音的文件
1.接口说明  

录音完成后，通过提供一个录音文件存储的地址路径，将已经录音完的文件进行上传

2.函数原型

      GCloudVoiceErr UploadRecordedFile(string filePath, int msTimeout)
    
  参数|类型|意义
  ---|---|---
  filePath|string|录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\" 
  msTimeout|int|上传文件超时时间 
  上传的结果通过delegate void UploadReccordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)进行回调  

3.示例代码
    
      public void Click_btnUploadFile()
      {
      	int ret1 = m_voiceengine.UploadRecordedFile (m_recordpath, 60000);
      	Debug.Log ("Click_btnUploadFile file with ret==" + ret1);
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可读
    GCLOUD_VOICE_HTTP_BUSY ： 还在上一次上传或者下载中，需要等待后再尝试
### 4.3.6 下载录音的文件
1.接口说明  

录音完成后，通过提供一个录音文件存储的地址路径，将已经录音完的文件进行上传

2.函数原型
    
      GCloudVoiceErr DownloadRecordedFile(string fileID, string downloadFilePath, int msTimeout);
    
  参数|类型|意义
  ---|---|---
  fileID| string| 要下载文件的文件ID
  downloadFilePath|string|下载录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\" 
  msTimeout|int|下载文件超时时间 
 下载的结果通过delegate void DownloadRecordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)进行回调   

3.示例代码
    
      public void Click_btnDownloadFile()
      {
      	int ret = m_voiceengine.DownloadRecordedFile (m_fileid, m_downloadpath, 60000);
      	s_strLog += "\r\n download file with ret=="+ret+" fileid="+m_fileid+" downpath"+m_downloadpath;
      }
4.出错处理
    
    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写或者不可读
    GCLOUD_VOICE_HTTP_BUSY ： 还在上一次上传或者下载中，需要等待后再尝试
### 4.3.7 开始播放下载的音频
1.接口说明    

下载下来的音频文件，需要调用相关接口进行播放

2.函数原型

      GCloudVoiceErr PlayRecordedFile (string downloadFilePath)
  参数|类型|意义
  ---|---|---
  filePath|string|下载文件存储的地址路径，路径中需要"/"作分隔，不能用"\"  
  
 如果正常播放完，会回调delegate void PlayRecordFilCompletehandler(GCloudVoiceCompleteCode code, string filepath)   

3.示例代码

      public void Click_btnPlayReocrdFile()
      {
    
      	int err;
      	if (m_ShareFileID == null) {
      		err = m_voiceengine.PlayRecordedFile(m_recordpath);
      		PrintLog ("downloadpath is nill, play local record file with ret=" + err);
      		return;
      	}
      	err = m_voiceengine.PlayRecordedFile(m_downloadpath);
      	PrintLog ("playrecord file with ret=" + err);
    
      	//m_voiceengine.PlayRecordedFile (m_downloadpath);
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写
    GCLOUD_VOICE_SPEAKER_ERR : 打开麦克风失败
### 4.3.8 停止播放下载的音频
1.接口说明  

中断播放动作

2.函数原型

 ` GCloudVoiceErr StopPlayFile() `  

3.示例代码

      public void Click_btnStopPlayRecordFile()
      {
      	m_voiceengine.StopPlayFile ();
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
### 4.3.9 请求语音消息Key回调
1.接口说明  

请求语音消息许可的时候会回调

2.函数原型

      delegate void ApplyMessageKeyCompleteHandler(GCloudVoiceCompleteCode code)
      public abstract event ApplyMessageKeyCompleteHandler OnApplyMessageKeyComplete
    
  参数| 类型| 意义
  ---|---|---
  code|GCloudVoiceCompleteCode| 参见GCloudVoiceCompleteCode定义
3.示例代码
    
      m_voiceengine.OnApplyMessageKeyComplete += (IGCloudVoice.GCloudVoiceCompleteCode code) => {
      	Debug.Log ("OnApplyMessageKeyComplete c# callback");
      	s_strLog += "\r\n"+"OnApplyMessageKeyComplete ret="+code;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_MESSAGE_KEY_APPLIED_SUCC) {
      		Debug.Log ("OnApplyMessageKeyComplete succ11");
      	} else {
      		Debug.Log ("OnApplyMessageKeyComplete error");
      	}
      };
### 4.3.10 上传完成回调
1.接口说明  

上传语音文件后的结果通过这个进行回调

2.函数原型

      delegate void UploadReccordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)
      public abstract event UploadReccordFileCompletehandler OnUploadReccordFileComplete
    
  参数|类型|意义
  ---|---|---
  code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义
  filepath|string| 上传的文件路径
  fileid|string|文件的id
3.示例代码

      m_voiceengine.OnUploadReccordFileComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath, string fileid) => {
      	Debug.Log ("OnUploadReccordFileComplete c# callback");
      	s_strLog += "\r\n"+" fileid len="+fileid.Length+"OnUploadReccordFileComplete ret="+code+" filepath:"+filepath+" fielid:"+fileid;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_UPLOAD_RECORD_DONE) {
      		m_fileid = fileid;
      		s_strLog+="OnUploadReccordFileComplete succ, filepath:" +" fileid len="+fileid.Length+ filepath + " fileid:" + fileid+" fileid len="+fileid.Length;
      		Debug.Log ("OnUploadReccordFileComplete succ, filepath:" + filepath +" fileid len="+fileid.Length+ " fileid:" + fileid+" fileid len="+fileid.Length);
      	} else {
      		s_strLog+="OnUploadReccordFileComplete err, filepath:" + filepath + " fileid:" + fileid;
      		Debug.Log ("OnUploadReccordFileComplete error");
      	}
      };    
### 4.3.11 下载完成回调
1.接口说明  

下载语音文件后的结果通过这个进行回调

2.函数原型

      delegate void DownloadRecordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)
      public abstract event DownloadRecordFileCompletehandler OnDownloadRecordFileComplete
    
  参数|类型|意义
  ---|---|---
  code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义
  filepath|string| 下载的路径
  fileid|string|文件的id
3.示例代码

      m_voiceengine.OnDownloadRecordFileComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath, string fileid) => {
      	Debug.Log ("OnDownloadRecordFileComplete c# callback");
      	s_strLog += "\r\n"+"OnDownloadRecordFileComplete ret="+code+" filepath:"+filepath+" fielid:"+fileid;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_DOWNLOAD_RECORD_DONE) {
      		Debug.Log ("OnDownloadRecordFileComplete succ, filepath:" + filepath + " fileid:" + fileid);
      	} else {
      		Debug.Log ("OnDownloadRecordFileComplete error");
      	}
      };
### 4.3.12 正常播放完成后回调
1.接口说明  

如果用户没有暂停播放，而语音文件已经播放完了，通过这个进行回调

2.函数原型

      delegate void PlayRecordFilCompletehandler(GCloudVoiceCompleteCode code, string filepath)
      public abstract event PlayRecordFilCompletehandler OnPlayRecordFilComplete;
    
  参数|类型|意义
  ---|---|---
  code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义
  filepath|string| 播放的文件路径
3.示例代码

      m_voiceengine.OnPlayRecordFilComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath) => {
      	Debug.Log ("OnPlayRecordFilComplete c# callback");
      	s_strLog += "\r\n"+"OnPlayRecordFilComplete ret="+code+" filepath:"+filepath;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_PLAYFILE_DONE) {
      		Debug.Log ("OnPlayRecordFilComplete succ, filepath:" + filepath);
      	} else {
      		Debug.Log ("OnPlayRecordFilComplete error");
      	}
      };   
###4.4 错误码表
	

    错误	|十六进制值|	十进制值	|意义
 	---|---|---|---
    GCLOUD_VOICE_SUCC|	0x0|	0	|Success
    GCLOUD_VOICE_PARAM_NULL|	0x1001|	4097	|some param is null
    GCLOUD_VOICE_NEED_SETAPPINFO|	0x1002	|4098|	you should call SetAppInfo first before call other api
    GCLOUD_VOICE_INIT_ERR|	0x1003|	4099|	Init Erro
    GCLOUD_VOICE_RECORDING_ERR|	0x1004	|4100|	now is recording, can't do other operator
    GCLOUD_VOICE_POLL_BUFF_ERR|	0x1005|	4101|	poll buffer is not enough or null
    GCLOUD_VOICE_MODE_STATE_ERR|	0x1006|	4102|	call some api, but the mode is not correct, maybe you shoud call SetMode first and correct
    GCLOUD_VOICE_PARAM_INVALID|	0x1007|	4103	|some param is null or value is invalid for our request, used right param and make sure is value range is correct by our comment
    GCLOUD_VOICE_OPENFILE_ERR|	0x1008	|4104|	open a file err
    GCLOUD_VOICE_NEED_INIT|	0x1009|	4105|	you should call Init before do this operator
    GCLOUD_VOICE_ENGINE_ERR|	0x100A|	4106	|you have not get engine instance, this common in use c# api. but not get gcloudvoice instance first
    GCLOUD_VOICE_POLL_MSG_PARSE_ERR|	0x100B|	4107|	this common in c# api, parse poll msg err
    GCLOUD_VOICE_POLL_MSG_NO|	0x100C	|4108|	poll no msg to update
    GCLOUD_VOICE_REALTIME_STATE_ERR|	0x2001|	8193	|call some realtime api, but state err. such as OpenMic but you have not Join Room first
    GCLOUD_VOICE_JOIN_ERR|	0x2002	|8194	|join room failed
    GCLOUD_VOICE_QUIT_ROOMNAME_ERR|	0x2003|	8195|	quit room err, the quit roomname not equal join roomname
    GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR|	0x2004|	8196|	open mic in bigroom,but not anchor role
    GCLOUD_VOICE_AUTHKEY_ERR|	0x3001|	12289|	apply authkey api error
    GCLOUD_VOICE_PATH_ACCESS_ERR|	0x3002	|12290|	the path can not access ,may be path file not exists or deny to access
    GCLOUD_VOICE_PERMISSION_MIC_ERR|	0x3003|	12291|	you have not right to access micphone in android
    GCLOUD_VOICE_NEED_AUTHKEY|	0x3004|	12292|	you have not get authkey, call ApplyMessageKey first
    GCLOUD_VOICE_UPLOAD_ERR	|0x3005	|12293|	upload file err
    GCLOUD_VOICE_HTTP_BUSY|	0x3006|	12294|	http is busy,maybe the last upload/download not finish.
    GCLOUD_VOICE_DOWNLOAD_ERR|	0x3007|	12295|	download file err
    GCLOUD_VOICE_SPEAKER_ERR|	0x3008|	12296|	open or close speaker tve error
    GCLOUD_VOICE_TVE_PLAYSOUND_ERR|	0x3009|	12297|	tve play file error
    GCLOUD_VOICE_INTERNAL_TVE_ERR|	0x5001|	20481|	internal TVE err, our used
    GCLOUD_VOICE_INTERNAL_VISIT_ERR	|0x5002	|20482	|internal Not TVE err, out used
    GCLOUD_VOICE_INTERNAL_USED|	0x5003|	20483|	internal used, you should not get this err num

## 5 调用demo
参见DEMO