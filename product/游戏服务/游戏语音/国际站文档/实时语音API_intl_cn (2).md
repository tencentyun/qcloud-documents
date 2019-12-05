## 1 概述
使用实时语音，需要先调用[基本API](https://cloud.tencent.com/document/product/556/7675)。

## 2 实时语音API调用流程 
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


## 3 实时语音API

### 3.1 加入小队语音
1.接口说明 
 
使用实时语音的小队语音功能时，需要先加入小队语音房间

2.函数原型

      GCloudVoiceErr JoinTeamRoom(string roomName, int msTimeout)   
    
  |参数|类型|意义|
  |--|--|--|
  |roomName|string| 要加入的房间名|
  |msTimeout|int| 加入房间的超时时间，单位是毫秒|
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
### 3.2 加入国战语音

1.接口说明  
  
使用国战语音功能时，需要先加入国战语音房间

2.函数原型

      public enum GCloudVoiceRole
      {
      ANCHOR = 1, // member who can open microphone and say
      AUDIENCE,   // member who can only hear anchor's voice
      }
      GCloudVoiceErr JoinNationalRoom(string roomName, GCloudVoiceRole role, int msTimeout)   
    
  |参数|类型|意义|
  |--|--|--|
  |roomName|string| 要加入的房间名|
  |role|GCloudVoiceRole| 成员加入的角色，听众只能收听语音不能发送语音，而主播既可以发送语音也可以收听语音|
 |msTimeout|int| 加入房间的超时时间，单位是毫秒|

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
### 3.3 退出实时语音
1.接口说明  

当不需要使用实时语音，可以从实时语音（包括小队语音和国战语音）房间中退出。

2.函数原型

      GCloudVoiceErr QuitRoom(string roomName, int msTimeout);  
    
  |参数|类型|意义|
  |--|--|--|
  |roomName|string| 要退出的房间名|
  |msTimeout|int| 退出房间的超时时间，单位是毫秒|
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
### 3.4 打开麦克风

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
### 3.5 关闭麦克风

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
### 3.6 打开扬声器

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
### 3.7 关闭扬声器

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
### 3.8 加入房间回调
1.接口说明 
 
当加入房间成功或者失败时会通过delegate进行通知

2.函数原型

      delegate qvoid JoinRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)
      public abstract event JoinRoomCompleteHandler OnJoinRoomComplete;
    
  |参数|类型|意义|
  |--|--|--|
  |code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义|
  |roomName| string| 加入的房间名|
  |memberID|int| 如果加入成功的话，表示加入后的成员ID|

3.示例代码

      m_voiceengine.OnJoinRoomComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string roomName, int memberID) => {
      	PrintLog ("On Join Room With " + code);
      	Debug.Log ("OnJoinRoomComplete ret=" + code + " roomName:" + roomName + " memberID:" + memberID);
      	s_logstr += "\r\n"+"OnJoinRoomComplete ret="+code+" roomName:"+roomName+" memberID:"+memberID;
      	//UIManager.m_Instance.OnJoinRoomDone(code);
      };
### 3.9 退出房间回调
1.接口说明  

当退出房间时，结果通过delegate进行通知

2.函数原型

      delegate void QuitRoomCompleteHandler(GCloudVoiceCompleteCode code, string roomName, int memberID)
      public abstract event QuitRoomCompleteHandler OnQuitRoomComplete;
    
  |参数|类型|意义|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| 参见GCloudVoiceCompleteCode定义|
  |roomName| string| 退出的房间名|
  |memberID|int| 如果加入成功的话，表示加入后的成员ID|

3.示例代码

      m_voiceengine.OnQuitRoomComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string roomName, int memberID) => {
     	 PrintLog ("On Quit Room With " + code);
      	Debug.Log ("OnQuitRoomComplete ret=" + code + " roomName:" + roomName + " memberID:" + memberID);
      	s_logstr += "\r\n"+"OnJoinRoomComplete ret="+code+" roomName:"+roomName+" memberID:"+memberID;
      	//UIManager.m_Instance.OnJoinRoomDone(code);
      };
### 3.10 成员状态改变回调

1.接口说明  

当房间中的其他成员开始说话或者停止说话的时候，通过该回调进行通知

2.函数原型

      delegate void MemberVoiceHandler(int[] members, int count) ;
      public abstract event MemberVoiceHandler  OnMemberVoice;
    
  |参数|类型|意义|
  |--|--|--|
  |members|int[]|改变状态的member成员，其值为[memberID &#124; status]这样的对，总共有count对，status有“0”：停止说话; “1”：开始说话; “2”:继续说话。|
  |count|int| 改变状态的成员的数目|
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

