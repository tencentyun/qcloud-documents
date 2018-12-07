## 简介

欢迎使用腾讯云游戏多媒体引擎 SDK 。为方便 Unity 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 Unity 开发的接入技术文档。

## 使用流程图
### 实时语音流程图
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)
### 离线语音语音转文字流程图
![](https://main.qcloudimg.com/raw/4c875d05cd2b4eaefba676d2e4fc031d.png)


### 使用 GME 重要事项

|重要接口     | 接口含义|
| ------------- |:-------------:|
|Init    		|初始化 GME 	|
|Poll    		|触发事件回调	|
|EnterRoom	 	|进房  		|
|EnableMic	 	|开麦克风 	|
|EnableSpeaker		|开扬声器 	|

>**说明：**
- GME 的接口调用成功后返回值为 QAVError.OK，数值为 0。
- GME 的接口调用要在同一个线程下。
- GME 加入房间需要鉴权，请参考文档关于鉴权部分内容。
- GME 需要周期性的调用 Poll 接口触发事件回调。
- GME 回调信息参考回调消息列表。
- 设备的操作要在进房成功之后。
- 此文档对应GME sdk version：2.2。


## 初始化相关接口
未初始化前，SDK 处于未初始化阶段，需要初始化鉴权后，通过初始化 SDK，才可以进房。

|接口     | 接口含义   |
| ------------- |:-------------:|
|Init    	|初始化 GME	|
|Poll    	|触发事件回调	|
|Pause   	|系统暂停	|
|Resume 	|系统恢复	|
|Uninit    	|反初始化 GME 	|

### 获取实例
请使用 ITMGContext 的方法获取 Context 实例，不要直接使用 QAVContext.GetInstance() 去获取实例。

### 初始化 SDK
参数获取见文档：[游戏多媒体引擎接入指引](https://cloud.tencent.com/document/product/607/10782)。
此接口需要来自腾讯云控制台的 SdkAppId 号码作为参数，再加上 openId，这个 openId 是唯一标识一个用户，规则由 App 开发者自行制定，App 内不重复即可（目前只支持 INT64）。
初始化 SDK 之后才可以进房。

#### 函数原型
```
IQAVContext Init(string sdkAppID, string openID)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| sdkAppId    	|String  |来自腾讯云控制台的 SdkAppId 号码						|
| openID    	|String  |OpenID 只支持 Int64 类型（转为string传入），必须大于 10000，用于标识用户 	|

#### 示例代码  
```
int ret = IQAVContext.GetInstance().Init(str_appId, str_userId);
	if (ret != QAVError.OK) {
		return;
	}
```

### 触发事件回调
通过在 update 里面周期的调用 Poll 可以触发事件回调。
#### 函数原型

```
ITMGContext public abstract int Poll();
```
### 系统暂停
当系统发生 Pause 事件时，需要同时通知引擎进行 Pause。
#### 函数原型

```
ITMGContext public abstract int Pause()
```

### 系统恢复
当系统发生 Resume 事件时，需要同时通知引擎进行 Resume。
#### 函数原型

```
ITMGContext  public abstract int Resume()
```






### 反初始化 SDK
反初始化 SDK，进入未初始化状态。
#### 函数原型

```
ITMGContext public abstract int Uninit()
```





## 实时语音房间相关接口
初始化之后，SDK 调用进房后进去了房间，才可以进行实时语音通话。

|接口     | 接口含义   |
| ------------- |:-------------:|
|GenAuthBuffer    	|初始化鉴权|
|EnterRoom   		|加入房间|
|EnterTeamRoom   	|加入小队语音房间|
|IsRoomEntered   	|是否已经进入房间|
|ExitRoom 		|退出房间|
|ChangeRoomType 	|修改用户房间音频类型|
|GetRoomType 		|获取用户房间音频类型|



### 鉴权信息
生成 AuthBuffer，用于相关功能的加密和鉴权，相关后台部署见 [GME 密钥文档](https://cloud.tencent.com/document/product/607/12218)。    
离线语音获取鉴权时，房间号参数必须填null。
该接口返回值为 Byte[] 类型。
#### 函数原型
```
QAVAuthBuffer GenAuthBuffer(int appId, string roomId, string openId, string key)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| appId    		|int   		|来自腾讯云控制台的 SdkAppId 号码		|
| roomId    		|string   		|房间号，最大支持127字符	（离线语音房间号参数必须填null）|
| openId    	|String 	|用户标识					|
| key    		|string 	|来自腾讯云[控制台](https://console.cloud.tencent.com/gamegme)的密钥				|



#### 示例代码  
```
byte[] GetAuthBuffer(string appId, string userId, string roomId)
    {
	return QAVAuthBuffer.GenAuthBuffer(int.Parse(appId), roomId, userId, "a495dca2482589e9");
}
```

### 加入房间
用生成的鉴权信息进房。加入房间默认不打开麦克风及扬声器。进房超时是 30 秒会有回调。

小队语音详细接入细节请查阅 [GME 小队语音](https://cloud.tencent.com/document/product/607/17972)。


#### 函数原型
```
ITMGContext EnterRoom(string roomId, int roomType, byte[] authBuffer)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| roomId		|string    	|房间号，支持 Int32 类型，转为字符串传入					|
| roomType 	|ITMGRoomType		|房间音频类型		|
| authBuffer 	|Byte[] 	|鉴权码					|

|音频类型     	|含义|参数|音量类型|控制台推荐采样率设置|适用场景|
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|流畅音质	|1|扬声器：通话音量；耳机：媒体音量	|如对音质无特殊需求，16K 采样率即可；					|流畅优先、超低延迟实时语音，应用在游戏内开黑场景，适用于 FPS、MOBA 等类型的游戏；	|							
| ITMG_ROOM_TYPE_STANDARD			|标准音质	|2|扬声器：通话音量；耳机：媒体音量	|根据对音质的需求，可以选择 16k/48k 采样率				|音质较好，延时适中，适用于狼人杀、棋牌等休闲游戏的实时通话场景；	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|高清音质	|3|扬声器：媒体音量；耳机：媒体音量	|为了保证最佳效果，建议控制台设置 48k 采样率的高音质配置	|超高音质，延时相对大一些，适用于音乐舞蹈类游戏以及语音社交类 APP；适用于播放音乐、线上K歌等有高音质要求的场景；	|

- 如对音量类型或场景有特殊需求，请联系一线客服反馈；
- 控制台采样率设置会直接影响游戏语音效果，请在 [控制台](https://console.cloud.tencent.com/gamegme) 上再次确认采样率设置是否符合项目使用场景。
#### 示例代码  
```
IQAVContext.GetInstance().EnterRoom(roomId, ITMG_ROOM_TYPE_FLUENCY, authBuffer);
```

### 加入房间事件的回调
加入房间后，需要通过委托函数进行回调。其中包含两个信息：result 及 error_info。
#### 函数原型
```
委托函数：
public delegate void QAVEnterRoomComplete(int result, string error_info);
事件函数：
public abstract event QAVEnterRoomComplete OnEnterRoomCompleteEvent;
```

#### 示例代码
```
对事件进行监听：
IQAVContext.GetInstance().OnEnterRoomCompleteEvent += new QAVEnterRoomComplete(OnEnterRoomComplete);

监听处理：
void OnEnterRoomComplete(int err, string errInfo)
    {
	if (err != 0) {
	    ShowWarnning (string.Format ("join room failed, err:{0}, errInfo:{1}", err, errInfo));
	    return;
	}else{
	    ShowWarnning (string.Format ("当前语音房间id:{0},请在别的终端加入这个房间进行通话",roomId ));
    }
}
```

### 判断是否已经进入房间
通过调用此接口可以判断是否已经进入房间，返回值为 BOOL 类型。
#### 函数原型  
```
ITMGContext abstract bool IsRoomEntered()
```
#### 示例代码  
```
IQAVContext.GetInstance().IsRoomEntered();
```

### 退出房间
通过调用此接口可以退出所在房间。这是一个异步接口，返回值为 AV_OK 的时候代表异步投递成功。

#### 函数原型  
```
ITMGContext ExitRoom()
```
#### 示例代码  
```
IQAVContext.GetInstance().ExitRoom();
```

### 退出房间回调
退出房间完成回调，通过委托传递消息。
#### 函数原型  
```
委托函数：
public delegate void QAVExitRoomComplete();
事件函数：
public abstract event QAVExitRoomComplete OnExitRoomCompleteEvent; 
```
#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().OnExitRoomCompleteEvent += new QAVExitRoomComplete(OnExitRoomComplete);
监听处理：
void OnExitRoomComplete(){
    //退出房间后的处理
}
```

### 获取用户房间音频类型
此接口用于获取用户房间音频类型，返回值为房间音频类型，返回值为0时代表获取用户房间音频类型发生错误，房间音频类型参考 EnterRoom 接口。

#### 函数原型  
```
ITMGContext ITMGRoom public  int GetRoomType()
```

#### 示例代码  
```
IQAVContext.GetInstance().GetRoom().GetRoomType();
```

### 修改用户房间音频类型
此接口用于修改用户房间音频类型。
#### 函数原型  
```
ITMGContext ITMGRoom public void ChangeRoomType(ITMGRoomType roomtype)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| roomtype    |ITMGRoomType    |希望房间切换成的类型，房间音频类型参考 EnterRoom 接口|

#### 示例代码  
```
IQAVContext.GetInstance().GetRoom().ChangeRoomType(ITMG_ROOM_TYPE_FLUENCY);
```



### 修改房间音频类型回调
主动设置房间类型，房间类型设置后，通过委托传递修改完成的相关消息。

|返回的参数     | 意义  |
| ------------- |:-------------:|
| result    |0 是代表成功|
| error_info    |如果失败，会传递相关错误信息|

```
委托函数：
public delegate void QAVOnChangeRoomtypeCallback(int result, string error_info);

事件函数：
public abstract event QAVCallback OnChangeRoomtypeCallback; 
```
#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().OnChangeRoomtypeCallback += new QAVOnChangeRoomtypeCallback(OnChangeRoomtypeCallback);
监听处理：
void OnChangeRoomtypeCallback(){
    //房间类型设置完成后的处理
}
```

### 房间类型变化通知
用户主动修改房间类型，或者房间内其它用户修改房间类型，只要房间类型发生变化，该回调函数就会被调用，通过次回调函数通知业务层房间类型发生变化，返回的是房间类型，参考 EnterRoom 接口。
```
委托函数：
public delegate void QAVOnRoomTypeChangedEvent(int roomtype);

事件函数：
public abstract event QAVOnRoomTypeChangedEvent OnRoomTypeChangedEvent;	
```
#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().OnRoomTypeChangedEvent += new QAVOnRoomTypeChangedEvent(OnRoomTypeChangedEvent);
监听处理：
void OnRoomTypeChangedEvent(){
    //房间类型改变后的处理
}
```


	
### 成员状态变化
该事件在状态变化才通知，状态不变化的情况下不通知。如需实时获取成员状态，请在上层收到通知时缓存，事件消息为 ITMG_MAIN_EVNET_TYPE_USER_UPDATE，参数 intent 包含两个信息，event_id 及 user_list，在 OnEvent 函数中对事件消息进行判断。
音频事件的通知有一个阈值，超过这个阈值才会发送通知。超过两秒没有收到音频包才通知“有成员停止发送音频包”消息。

|event_id     | 含义         |应用侧维护内容|
| ------------- |:-------------:|-------------|
|ITMG_EVENT_ID_USER_ENTER    				|有成员进入房间			|应用侧维护成员列表		|
|ITMG_EVENT_ID_USER_EXIT    				|有成员退出房间			|应用侧维护成员列表		|
|ITMG_EVENT_ID_USER_HAS_AUDIO    		|有成员发送音频包		|应用侧维护通话成员列表	|
|ITMG_EVENT_ID_USER_NO_AUDIO    			|有成员停止发送音频包	|应用侧维护通话成员列表	|

#### 示例代码  
```
委托函数：
public delegate void QAVEndpointsUpdateInfo(int eventID, int count, [MarshalAs(UnmanagedType.LPArray, SizeParamIndex = 1)]string[] openIdList);
事件函数：
public abstract event QAVEndpointsUpdateInfo OnEndpointsUpdateInfoEvent;

对事件进行监听：
IQAVContext.GetInstance().OnEndpointsUpdateInfoEvent += new QAVEndpointsUpdateInfo(OnEndpointsUpdateInfo);
监听处理：
void OnEndpointsUpdateInfo(int eventID, int count, string[] openIdList)
{
    //进行处理
		//开发者对参数进行解析，得到信息 event_id及 user_list
		    switch (eventID)
 		    {
 		    case ITMG_EVENT_ID_USER_ENTER:
  			    //有成员进入房间
  			    break;
 		    case ITMG_EVENT_ID_USER_EXIT:
  			    //有成员退出房间
			    break;
		    case ITMG_EVENT_ID_USER_HAS_AUDIO:
			    //有成员发送音频包
			    break;
		    case ITMG_EVENT_ID_USER_NO_AUDIO:
			    //有成员停止发送音频包
			    break;
		  
		    default:
			    break;
 		    }
		break;
}

```


### 质量监控事件
质量监控事件，事件消息为 ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_QUALITY，返回的参数为 weight、floss  及 delay，代表的信息如下，在 OnEvent 函数中对事件消息进行判断。

|参数     | 含义         |
| ------------- |-------------|
|weight    				|范围是 1 到 50，数值为 50 是音质评分极好，数值为 1 是音质评分很差，几乎不能使用，数值为 0 代表初始值，无意义|
|floss    				|丢包率|
|delay    		|音频触达延迟时间（ms）|


## 实时语音音频接口
初始化 SDK 之后进房，在房间中，才可以调用实时音频语音相关接口。
调用场景举例：

当用户界面点击打开/关闭麦克风/扬声器按钮时，建议如下方式：
- 对于大部分的游戏类 App，推荐调用 EnableMic 及 EnbaleSpeaker 接口，相当于总是应该同时调用 EnableAudioCaptureDevice/EnableAudioSend 和 EnableAudioPlayDevice/EnableAudioRecv 接口；

- 其他类型的移动端 App 例如社交类型 App，打开或者关闭采集设备，会伴随整个设备（采集及播放）重启，如果此时 App 正在播放背景音乐，那么背景音乐的播放也会被中断。利用控制上下行的方式来实现开关麦克风效果，不会中断播放设备。具体调用方式为：在进房的时候调用 EnableAudioCaptureDevice(true) && EnabledAudioPlayDevice(true) 一次，点击开关麦克风时只调用 EnableAudioSend/Recv 来控制音频流是否发送/接收。

如目的是互斥（释放录音权限给其他模块使用），建议使用 PauseAudio/ResumeAudio。


|接口     | 接口含义   |
| ------------- |:-------------:|
|PauseAudio    				       	   |暂停音频引擎		|
|ResumeAudio    				      	 |恢复音频引擎		|
|EnableMic    						|开关麦克风|
|GetMicState    						|获取麦克风状态|
|EnableAudioCaptureDevice    		|开关采集设备		|
|IsAudioCaptureDeviceEnabled    	|获取采集设备状态	|
|EnableAudioSend    				|打开关闭音频上行	|
|IsAudioSendEnabled    				|获取音频上行状态	|
|GetMicLevel    						|获取实时麦克风音量	|
|SetMicVolume    					|设置麦克风音量		|
|GetMicVolume    					|获取麦克风音量		|
|EnableSpeaker    					|开关扬声器|
|GetSpeakerState    					|获取扬声器状态|
|EnableAudioPlayDevice    			|开关播放设备		|
|IsAudioPlayDeviceEnabled    		|获取播放设备状态	|
|EnableAudioRecv    					|打开关闭音频下行	|
|IsAudioRecvEnabled    				|获取音频下行状态	|
|GetSpeakerLevel    					|获取实时扬声器音量	|
|SetSpeakerVolume    				|设置扬声器音量		|
|GetSpeakerVolume    				|获取扬声器音量		|
|EnableLoopBack    					|开关耳返			|


### 暂停音频引擎的采集和播放
调用此接口暂停音频引擎的采集和播放，此接口为同步接口，且只在进房后有效。
如果想单独释放采集或者播放设备，请参考接口 EnableAudioCaptureDevice 及 EnableAudioPlayDevice。
#### 函数原型  

```
ITMGAudioCtrl abstract int PauseAudio()
```
#### 示例代码  
```
IQAVContext.GetInstance ().GetAudioCtrl ().PauseAudio();
```

### 恢复音频引擎的采集和播放
调用此接口恢复音频引擎的采集和播放，此接口为同步接口，且只在进房后有效。

#### 函数原型  
```
ITMGAudioCtrl abstract int ResumeAudio()
```
#### 示例代码  
```
IQAVContext.GetInstance ().GetAudioCtrl ().ResumeAudio();
```

### 开启关闭麦克风
此接口用来开启关闭麦克风。加入房间默认不打开麦克风及扬声器。

#### 函数原型  
```
ITMGAudioCtrl EnableMic(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |如果需要打开麦克风，则传入的参数为 true，如果关闭麦克风，则参数为 false|

#### 示例代码  
```
打开麦克风
IQAVContext.GetInstance().GetAudioCtrl().EnableMic(true);
```

### 麦克风状态获取
此接口用于获取麦克风状态，返回值 0 为关闭麦克风状态，返回值 1 为打开麦克风状态，返回值 2 为麦克风设备正在操作中，返回值 3 为麦克风设备不存在，返回值 4 为设备没初始化好。
#### 函数原型  
```
ITMGAudioCtrl GetMicState()
```
#### 示例代码  
```
micToggle.isOn = IQAVContext.GetInstance().GetAudioCtrl().GetMicState();
```

### 开启关闭采集设备
此接口用来开启/关闭采集设备。加入房间默认不打开设备。
- 只能在进房后调用此接口，退房会自动关闭设备。
- 在移动端，打开采集设备通常会伴随权限申请，音量类型调整等操作。

#### 函数原型  
```
ITMGAudioCtrl int EnableAudioPlayDevice(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |bool     |如果需要打开采集设备，则传入的参数为 true，如果关闭采集设备，则参数为 false|

#### 示例代码  
```
打开采集设备
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioCaptureDevice(true);
```

### 采集设备状态获取
此接口用于采集设备状态获取。

#### 函数原型  
```
ITMGAudioCtrl bool IsAudioCaptureDeviceEnabled()
```
#### 示例代码

```
bool IsAudioCaptureDevice = IQAVContext.GetInstance().GetAudioCtrl().IsAudioCaptureDeviceEnabled();
```

### 打开关闭音频上行
此接口用于打开/关闭音频上行。如果采集设备已经打开，那么会发送采集到的音频数据。如果采集设备没有打开，那么仍旧无声。采集设备的打开关闭参见接口 EnableAudioCaptureDevice。

#### 函数原型

```
ITMGAudioCtrl int EnableAudioSend(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |bool     |如果需要打开音频上行，则传入的参数为 true，如果关闭音频上行，则参数为 false|

#### 示例代码  

```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioSend(true);
```

### 音频上行状态获取
此接口用于音频上行状态获取。
#### 函数原型  

```
ITMGAudioCtrl bool IsAudioSendEnabled()
```
#### 示例代码  
```
bool IsAudioSend = IQAVContext.GetInstance().GetAudioCtrl().IsAudioSendEnabled();
```

### 获取麦克风实时音量
此接口用于获取麦克风实时音量，返回值为 int 类型。
#### 函数原型  
```
ITMGAudioCtrl -(int)GetMicLevel
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioCtrl().GetMicLevel();
```

### 设置麦克风的音量
此接口用于设置麦克风的音量。参数 volume 用于设置麦克风的音量，当数值为 0 的时候表示静音，当数值为 100 的时候表示音量不增不减，默认数值为 100。

#### 函数原型  
```
ITMGAudioCtrl SetMicVolume(int volume)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| volume    |int      |设置音量，范围 0 到 200|

#### 示例代码  

```
int micVol = (int)(value * 100);
IQAVContext.GetInstance().GetAudioCtrl().SetMicVolume (micVol);
```

### 获取麦克风的音量
此接口用于获取麦克风的音量。返回值为一个int类型数值，返回值为101代表没调用过接口 SetMicVolume。

#### 函数原型  
```
ITMGAudioCtrl GetMicVolume()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioCtrl().GetMicVolume();
```

### 开启关闭扬声器
此接口用于开启关闭扬声器。
#### 函数原型  
```
ITMGAudioCtrl EnableSpeaker(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |bool        |如果需要关闭扬声器，则传入的参数为 false，如果打开扬声器，则参数为 true|

#### 示例代码  
```
打开扬声器
IQAVContext.GetInstance().GetAudioCtrl().EnableSpeaker(true);
```


### 扬声器状态获取
此接口用于扬声器状态获取。返回值 0 为关闭扬声器状态，返回值 1 为打开扬声器状态，返回值 2 为扬声器设备正在操作中，返回值 3 为扬声器设备不存在，返回值 4 为设备没初始化好。
#### 函数原型  
```
ITMGAudioCtrl GetSpeakerState()
```

#### 示例代码  
```
speakerToggle.isOn = IQAVContext.GetInstance().GetAudioCtrl().GetSpeakerState();
```


### 开启关闭播放设备
此接口用于开启关闭播放设备。
#### 函数原型  

```
ITMGAudioCtrl EnableAudioPlayDevice(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |bool        |如果需要关闭播放设备，则传入的参数为 false，如果打开播放设备，则参数为 true|

#### 示例代码

```
打开播放设备
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioPlayDevice(true);
```


### 播放设备状态获取
此接口用于播放设备状态获取。
#### 函数原型

```
ITMGAudioCtrl bool IsAudioPlayDeviceEnabled()
```
#### 示例代码

```
bool IsAudioPlayDevice = IQAVContext.GetInstance().GetAudioCtrl().IsAudioPlayDeviceEnabled();
```

### 打开关闭音频下行
此接口用于打开/关闭音频下行。如果播放设备已经打开，那么会播放房间里其他人的音频数据。如果播放设备没有打开，那么仍旧无声。播放设备的打开关闭参见接口 参见EnableAudioPlayDevice。

#### 函数原型  

```
ITMGAudioCtrl int EnableAudioRecv(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |bool     |如果需要打开音频下行，则传入的参数为 true，如果关闭音频下行，则参数为 false|

#### 示例代码  

```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioRecv(true);
```

### 音频下行状态获取
此接口用于音频下行状态获取。
#### 函数原型  

```
ITMGAudioCtrl bool IsAudioRecvEnabled()
```
#### 示例代码  

```
bool IsAudioRecv = IQAVContext.GetInstance().GetAudioCtrl().IsAudioRecvEnabled();
```


### 获取扬声器实时音量
此接口用于获取扬声器实时音量。返回值为 int 类型数值，表示扬声器实时音量。
#### 函数原型  
```
ITMGAudioCtrl GetSpeakerLevel()
```

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioCtrl().GetSpeakerLevel();
```

### 设置扬声器的音量
此接口用于设置扬声器的音量。
参数 volume 用于设置扬声器的音量，当数值为 0 的时候表示静音，当数值为 100 的时候表示音量不增不减，默认数值为 100。

#### 函数原型  
```
ITMGAudioCtrl SetSpeakerVolume(int volume)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| volume    |int        |设置音量，范围 0 到 200|

#### 示例代码

```
int speVol = (int)(value * 100);
IQAVContext.GetInstance().GetAudioCtrl().SetSpeakerVolume(speVol);
```

### 获取扬声器的音量
此接口用于获取扬声器的音量。返回值为 int 类型数值，代表扬声器的音量，返回值为101代表没调用过接口 SetSpeakerVolume。
Level 是实时音量，Volume 是扬声器的音量，最终声音音量相当于 Level*Volume%。举个例子：实时音量是数值是 100 的话，此时Volume的数值是 60，那么最终发出来的声音数值也是 60。

#### 函数原型  
```
ITMGAudioCtrl GetSpeakerVolume()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioCtrl().GetSpeakerVolume();
```


### 启动耳返
此接口用于启动耳返。
#### 函数原型  

```
ITMGContext GetAudioCtrl EnableLoopBack(bool enable)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| enable    |bool         |设置是否启动|

#### 示例代码  

```
IQAVContext.GetInstance().GetAudioCtrl().EnableLoopBack(true);
```

### 设备占用和释放事件回调
在房间内，占用设备和释放设备时会回调，通过委托传递事件的相关消息。

```
委托函数：
public delegate void QAVOnDeviceStateChangedEvent(int deviceType, string deviceId, bool openOrClose);
事件函数：
public abstract event QAVOnDeviceStateChangedEvent OnDeviceStateChangedEvent;
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| deviceType    	|int       	|1 代表采集设备，2 代表播放设备							|
| deviceId   	 	|string 	|设备GUID，用于标记设备，仅在 Windows 端和 Mac 端有效	|
| openOrClose    |bool  	|采集设备/播放设备占用或者释放							|


|参数     | 数值         |意义|
| ------------- |:-------------:|-------------|
| AUDIODEVICE_CAPTURE    	|1       	|代表采集设备|
| AUDIODEVICE_PLAYER   	 	|2 			|代表播放设备|

#### 示例代码  

```
对事件进行监听：
ITMGContext.GetInstance().GetAudioCtrl().OnDeviceStateChangedEvent += new QAVAudioDeviceStateCallback(OnAudioDeviceStateChange);
监听处理：
void QAVAudioDeviceStateCallback(){
    //设备占用和释放事件相关回调处理
}
```


## 实时语音伴奏相关接口
|接口     | 接口含义   |
| ------------- |:-------------:|
|StartAccompany    				       |开始播放伴奏|
|StopAccompany    				   	|停止播放伴奏|
|IsAccompanyPlayEnd				|伴奏是否播放完毕|
|PauseAccompany    					|暂停播放伴奏|
|ResumeAccompany					|重新播放伴奏|
|SetAccompanyVolume 				|设置伴奏音量|
|GetAccompanyVolume				|获取播放伴奏的音量|
|SetAccompanyFileCurrentPlayedTimeByMs 				|设置播放进度|

### 开始播放伴奏
调用此接口开始播放伴奏。支持 m4a、wav、mp3 一共三种格式。调用此 API，音量会重置。
#### 函数原型  
```
IQAVAudioEffectCtrl int StartAccompany(string filePath, bool loopBack, int loopCount, int duckerTimeMs)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| filePath    |string            |播放伴奏的路径|
| loopBack    |bool          |是否混音发送，一般都设置为 true ，即其他人也能听到伴奏|
| loopCount    |int          |循环次数，数值为 -1 表示无限循环|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StartAccompany(filePath,true,loopCount,duckerTimeMs);
```

### 播放伴奏的回调
伴奏播放结束时的回调，通过委托传递消息。
#### 函数原型  
```
委托函数：
public delegate void QAVAccompanyFileCompleteHandler(int code, string filepath);
事件函数：
public abstract event QAVAccompanyFileCompleteHandler OnAccompanyFileCompleteHandler;
```
#### 示例代码
```
对事件进行监听：
IQAVContext.GetInstance().GetAudioEffectCtrl().OnAccompanyFileCompleteHandler += new QAVAccompanyFileCompleteHandler(OnAccomponyFileCompleteHandler);
监听处理：
void OnAccomponyFileCompleteHandler(int code, string filepath){
    //播放伴奏的事件回调
}
```

### 停止播放伴奏
调用此接口停止播放伴奏。
#### 函数原型  
```
IQAVAudioEffectCtrl int StopAccompany(int duckerTimeMs)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| duckerTimeMs    |int             |淡出时间|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StopAccompany(duckerTimeMs);
```

### 伴奏是否播放完毕
如果播放完毕，返回值为 true，如果没播放完，返回值为 false。
#### 函数原型  
```
IQAAudioEffectCtrl bool IsAccompanyPlayEnd();
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().IsAccompanyPlayEnd();
```


### 暂停播放伴奏
调用此接口暂停播放伴奏。
#### 函数原型  
```
IQAAudioEffectCtrl int PauseAccompany()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PauseAccompany();
```



### 重新播放伴奏
此接口用于重新播放伴奏。
#### 函数原型  
```
IQAAudioEffectCtrl int ResumeAccompany()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().ResumeAccompany();
```

### 设置自己是否可以听到伴奏
此接口用于设置自己是否可以听到伴奏。
#### 函数原型  
```
IQAAudioEffectCtrl int EnableAccompanyPlay(bool enable)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| enable    |bool             |是否能听到|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().EnableAccompanyPlay(true);
```

### 设置他人是否也可以听到伴奏
设置他人是否也可以听到伴奏。
#### 函数原型  
```
IQAAudioEffectCtrl int EnableAccompanyLoopBack(bool enable)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| enable    |bool             |是否能听到|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().EnableAccompanyLoopBack(true);
```


### 设置伴奏音量
设置 DB 音量，默认值为 100，数值大于 100 音量增益，数值小于 100 音量减益，值域为 0 - 200。
#### 函数原型  
```
IQAAudioEffectCtrl int SetAccompanyVolume(int vol)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| vol    |int             |音量数值|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().SetAccompanyVolume(vol);
```

### 获取播放伴奏的音量
此接口用于获取 DB 音量。
#### 函数原型  
```
IQAAudioEffectCtrl abstract int GetAccompanyVolume()
```
#### 示例代码  
```
string currentVol = "VOL: " + IQAVContext.GetInstance().GetAudioEffectCtrl().GetAccompanyVolume();
```

### 获得伴奏播放进度
以下两个接口用于获得伴奏播放进度。需要注意：Current / Total = 当前循环次数，Current % Total = 当前循环播放位置。
#### 函数原型  
```
IQAAudioEffectCtrl abstract uint GetAccompanyFileTotalTimeByMs()
IQAAudioEffectCtrl abstract int GetAccompanyFileCurrentPlayedTimeByMs()
```
#### 示例代码  
```
Sstring current = "Current: " + IQAVContext.GetInstance().GetAudioEffectCtrl().GetAccompanyFileCurrentPlayedTimeByMs() + " ms";
string total = "Total: " + IQAVContext.GetInstance().GetAudioEffectCtrl().GetAccompanyFileTotalTimeByMs() + " ms";
```


### 设置播放进度
此接口用于设置播放进度。
#### 函数原型  
```
IQAAudioEffectCtrl abstract uint SetAccompanyFileCurrentPlayedTimeByMs(uint time)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| time    |uint                |播放进度，以毫秒为单位|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().SetAccompanyFileCurrentPlayedTimeByMs(time);
```


## 实时语音音效相关接口
|接口     | 接口含义   |
| ------------- |:-------------:|
|PlayEffect    		|播放音效|
|PauseEffect    	|暂停播放音效|
|PauseAllEffects	|暂停所有音效|
|ResumeEffect    	|重新播放音效|
|ResumeAllEffects	|重新播放所有音效|
|StopEffect 		|停止播放音效|
|StopAllEffects		|停止播放所有音效|
|SetVoiceType 		|变声特效|
|SetKaraokeType 		|K歌音效特效|
|GetEffectsVolume	|获取播放音效的音量|
|SetEffectsVolume 	|设置播放音效的音量|

### 播放音效
此接口用于播放音效。参数中音效 id 需要 App 侧进行管理，唯一标识一个独立文件。文件支持 m4a、wav、mp3 一共三种格式。
#### 函数原型  

```
IQAAudioEffectCtrl int PlayEffect(int soundId, string filePath, bool loop = false, double pitch = 1.0f, double pan = 0.0f, double gain = 1.0f)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| soundId    	|int      	|音效 id|
| filePath    	|string 	|音效路径|
| loop    		|bool   	|是否重复播放|
| pitch    	|double	|保留字段|
| pan    		|double	|保留字段|
| gain    		|double	|保留字段|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PlayEffect(soundId,filePath,true,1.0,0,1.0);
```

### 暂停播放音效
此接口用于暂停播放音效。
#### 函数原型  
```
IQAAudioEffectCtrl int PauseEffect(int soundId)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| soundId    |int                    |音效 id|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PauseEffect(soundId);
```

### 暂停所有音效
调用此接口暂停所有音效。
#### 函数原型  
```
IQAAudioEffectCtrl int PauseAllEffects()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().PauseAllEffects();
```

### 重新播放音效
此接口用于重新播放音效。
#### 函数原型  
```
IQAAudioEffectCtrl int ResumeEffect(int soundId)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| soundId    |int                    |音效 id|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().ResumeEffect(soundId);
```



### 重新播放所有音效
调用此接口重新播放所有音效。
#### 函数原型  
```
IQAAudioEffectCtrl int ResumeAllEffects()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().ResumeAllEffects();
```

### 停止播放音效
此接口用于停止播放音效。
#### 函数原型  
```
IQAAudioEffectCtrl int StopEffect(int soundId)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| soundId    |int                    |音效 id|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StopEffect(soundId);
```

### 停止播放所有音效
调用此接口停止播放所有音效。
#### 函数原型  
```
IQAAudioEffectCtrl int StopAllEffects()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().StopAllEffects(); 
```

### 变声特效
调用此接口设置变声特效。
#### 函数原型  
```
IQAAudioEffectCtrl int setVoiceType(int type)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| type    |int                    |表示本端音频变声类型|



|类型参数     |参数代表|意义|
| ------------- |-------------|------------- |
| ITMG_VOICE_TYPE_ORIGINAL_SOUND  		|0	|原声			|
| ITMG_VOICE_TYPE_LOLITA    				|1	|萝莉			|
| ITMG_VOICE_TYPE_UNCLE  				|2	|大叔			|
| ITMG_VOICE_TYPE_INTANGIBLE    			|3	|空灵			|
| ITMG_VOICE_TYPE_DEAD_FATBOY  			|4	|死肥仔			|
| ITMG_VOICE_TYPE_HEAVY_MENTA			|5	|重金属			|
| ITMG_VOICE_TYPE_DIALECT 				|6	|歪果仁			|
| ITMG_VOICE_TYPE_INFLUENZA 				|7	|感冒			|
| ITMG_VOICE_TYPE_CAGED_ANIMAL 			|8	|困兽			|
| ITMG_VOICE_TYPE_HEAVY_MACHINE		|9	|重机器			|
| ITMG_VOICE_TYPE_STRONG_CURRENT		|10	|强电流			|
| ITMG_VOICE_TYPE_KINDER_GARTEN			|11	|幼稚园			|
| ITMG_VOICE_TYPE_HUANG 					|12	|小黄人			|


#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().setVoiceType(0);
```

### K歌音效特效
调用此接口设置K歌音效特效。
####  函数原型  
```
IQAAudioEffectCtrl int SetKaraokeType(int type)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| type    |int                    |表示本端音频变声类型|


|类型参数     |参数代表|意义|
| ------------- |-------------|------------- |
|ITMG_KARAOKE_TYPE_ORIGINAL 		|0	|原声			|
|ITMG_KARAOKE_TYPE_POP 				|1	|流行			|
|ITMG_KARAOKE_TYPE_ROCK 			|2	|摇滚			|
|ITMG_KARAOKE_TYPE_RB 				|3	|嘻哈			|
|ITMG_KARAOKE_TYPE_DANCE 			|4	|舞曲			|
|ITMG_KARAOKE_TYPE_HEAVEN 			|5	|空灵			|
|ITMG_KARAOKE_TYPE_TTS 				|6	|语音合成		|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().SetKaraokeType(0);
```




### 获取播放音效的音量
获取播放音效的音量，为线性音量，默认值为 100，数值大于 100 为增益效果，数值小于 100 为减益效果。
#### 函数原型  
```
IQAAudioEffectCtrl  int GetEffectsVolume()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().GetEffectsVolume();
```


### 设置播放音效的音量
调用此接口设置播放音效的音量。
#### 函数原型  
```
IQAAudioEffectCtrl  int SetEffectsVolume(int volume)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| volume    |int                    |音量数值|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioEffectCtrl().SetEffectsVolume(volume);
```







## 离线语音
使用离线语音及转文字功能需要先初始化 SDK。

|接口     | 接口含义   |
| ------------- |:-------------:|
|ApplyPTTAuthbuffer    |鉴权初始化	|
|SetMaxMessageLength    |限制最大语音信息时长	|
|StartRecording		|启动录音		|
|StartRecordingWithStreamingRecognition		|启动流式录音		|
|StopRecording    	|停止录音		|
|CancelRecording	|取消录音		|
|UploadRecordedFile 	|上传语音文件		|
|DownloadRecordedFile	|下载语音文件		|
|PlayRecordedFile 	|播放语音		|
|StopPlayFile		|停止播放语音		|
|GetFileSize 		|语音文件的大小		|
|GetVoiceFileDuration	|语音文件的时长		|
|SpeechToText 		|语音识别成文字			|

### 鉴权初始化
在初始化 SDK 之后调用鉴权初始化，authBuffer 的获取参见上文实时语音鉴权信息接口。
#### 函数原型  
```
ITMGPTT int ApplyPTTAuthbuffer (byte[] authBuffer)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| authBuffer    |byte[]                   |鉴权|

#### 示例代码  
```
IQAVContext.GetInstance().GetPttCtrl().ApplyPTTAuthbuffer(authBuffer);
```

### 限制最大语音信息时长
限制最大语音消息的长度，最大支持 60 秒。
#### 函数原型  
```
ITMGPTT int SetMaxMessageLength(int msTime)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| msTime    |int                    |语音时长，单位ms|

#### 示例代码  

```
IQAVContext.GetInstance().GetPttCtrl().SetMaxMessageLength(60000); 
```


### 启动录音
此接口用于启动录音。
#### 函数原型  
```
ITMGPTT int StartRecording(string fileDir)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| fileDir    |string                      |存放的语音路径|

#### 示例代码  
```
string recordPath = Application.persistentDataPath + string.Format ("/{0}.silk", sUid++);
int ret = IQAVContext.GetInstance().GetPttCtrl().StartRecording(recordPath);
```

### 启动录音的回调
录音完成的回调，通过委托传递消息。
#### 函数原型  
```
委托函数：
public delegate void QAVRecordFileCompleteCallback(int code, string filepath); 
事件函数：
public abstract event QAVRecordFileCompleteCallback OnRecordFileComplete;
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| code    |string                      |当 code 为 0 时，录制完成|
| filepath    |string                      |录制的存放地址|

#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().GetPttCtrl().OnRecordFileComplete += mInnerHandler;
监听处理：
void mInnerHandler(int code, string filepath){
    //启动录音的回调
}
```

### 启动流式录音
此接口用于启动流式录音，同时在回调中会有实时的语音转文字返回。

#### 函数原型  

```
ITMGPTT int StartRecordingWithStreamingRecognition(string filePath, string language)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| filePath    	|String	|存放的语音路径	|
| language 	|String	|需要转换的语言代码，参考[语音转文字的语言参数参考列表](/GME%20Developer%20Manual/GME%20SpeechToText.md)|

#### 示例代码  
```
string recordPath = Application.persistentDataPath + string.Format("/{0}.silk", sUid++);
int ret = ITMGContext.GetInstance().GetPttCtrl().StartRecordingWithStreamingRecognition(recordPath, "cmn-Hans-CN");
```

### 启动流式录音的回调
启动录音完成后的回调通过委托传递消息。
```
委托函数：
public delegate void QAVStreamingRecognitionCallback(int code, string fileid, string filepath, string result);
事件函数：
public abstract event QAVStreamingRecognitionCallback OnStreamingSpeechComplete;
```

|消息名称     | 意义         |
| ------------- |:-------------:|
| code    	|用于判断流式录音是否成功的返回码		|
| result    		|语音转文字识别的文本	|
| filepath 	|录音存放的本地地址		|
| fileid 		|录音在后台的 url 地址	|

|错误码     | 意义         |处理方式|
| ------------- |:-------------:|:-------------:|
|32775	|流式语音转文本失败，但是录音成功	|调用 UploadRecordedFile 接口上传录音，再调用 SpeechToText 接口进行语音转文字操作
|32777	|流式语音转文本失败，但是录音成功，上传成功	|返回的信息中有上传成功的后台 url 地址，调用 SpeechToText 接口进行语音转文字操作

#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().GetPttCtrl().OnStreamingSpeechComplete += mInnerHandler;
监听处理：
void mInnerHandler(int code, string fileid, string filepath, string result){
    //启动流式录音的回调
}

```
### 停止录音
此接口用于停止录音。
#### 函数原型  
```
ITMGPTT int StopRecording()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetPttCtrl().StopRecording();
```

### 取消录音
调用此接口取消录音。
#### 函数原型  

```
IQAVPTT int CancelRecording()
```
#### 示例代码  

```
IQAVContext.GetInstance().GetPttCtrl().CancelRecording();
```

### 上传语音文件
此接口用于上传语音文件。
#### 函数原型  

```
IQAVPTT int UploadRecordedFile (string filePath)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| filePath    |string                      |上传的语音路径|

#### 示例代码

```
IQAVContext.GetInstance().GetPttCtrl().UploadRecordedFile(filePath);
```


### 上传语音完成的回调
上传语音完成的回调，通过委托传递消息。
#### 函数原型  
```
委托函数：
public delegate void QAVUploadFileCompleteCallback(int code, string filepath, string fileid);
事件函数：
public abstract event QAVUploadFileCompleteCallback OnUploadFileComplete; 
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| code    |int                       |当code为0时，录制完成|
| filepath    |string                      |录制的存放地址|
| fileid    |string                      |文件的url路径|

#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().GetPttCtrl().OnUploadFileComplete += mInnerHandler;
监听处理：
void mInnerHandler(int code, string filepath, string fileid){
    //上传语音完成的回调
}
```


### 下载语音文件
此接口用于下载语音文件。
#### 函数原型  

```
IQAVPTT DownloadRecordedFile (string fileID, string downloadFilePath)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| fileID    |string                       |文件的url路径|
| downloadFilePath    |string                       |文件的本地保存路径|

#### 示例代码

```
IQAVContext.GetInstance().GetPttCtrl().DownloadRecordedFile(fileId, filePath);
```


### 下载语音文件完成回调
下载语音文件完成回调，通过委托传递消息。
#### 函数原型  
```
委托函数：
public delegate void QAVDownloadFileCompleteCallback(int code, string filepath, string fileid);
事件函数：
public abstract event QAVDownloadFileCompleteCallback OnDownloadFileComplete;
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| code    |int                       |当code为0时，录制完成|
| filepath    |string                      |录制的存放地址|
| fileid    |string                      |文件的url路径|

#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().GetPttCtrl().OnDownloadFileComplete += mInnerHandler;
监听处理：
void mInnerHandler(int code, string filepath, string fileid){
    //下载语音文件完成回调
}
```



### 播放语音
此接口用于播放语音。
#### 函数原型  
```
IQAVPTT PlayRecordedFile (string downloadFilePath)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| downloadFilePath    |string                       |文件的路径|

#### 示例代码  
```
IQAVContext.GetInstance().GetPttCtrl().PlayRecordedFile(filePath); 
```


### 播放语音的回调
播放语音的回调，通过委托传递消息。
#### 函数原型  
```
委托函数：
public delegate void QAVPlayFileCompleteCallback(int code, string filepath);
事件函数：
public abstract event QAVPlayFileCompleteCallback OnPlayFileComplete;
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| code    |int                       |当code为0时，录制完成|
| filepath    |string                      |录制的存放地址|

#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().GetPttCtrl().OnPlayFileComplete += mInnerHandler;
监听处理：
void mInnerHandler(int code, string filepath){
    //播放语音的回调
}
```




### 停止播放语音
此接口用于停止播放语音。
#### 函数原型  
```
IQAVPTT int StopPlayFile()
```

#### 示例代码  
```
IQAVContext.GetInstance().GetPttCtrl().StopPlayFile();
```



### 获取语音文件的大小
通过此接口，获取语音文件的大小。
#### 函数原型  
```
IQAVPTT GetFileSize(string filePath) 
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| filePath    |string                      |语音文件的路径|

#### 示例代码  
```
int fileSize = IQAVContext.GetInstance().GetPttCtrl().GetFileSize(filepath);
```

### 获取语音文件的时长
此接口用于获取语音文件的时长，单位毫秒。
#### 函数原型  
```
IQAVPTT int GetVoiceFileDuration(string filePath)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| filePath    |string                      |语音文件的路径|

#### 示例代码  
```
int fileDuration = IQAVContext.GetInstance().GetPttCtrl().GetVoiceFileDuration(filepath);
```


### 将指定的语音文件识别成文字
此接口用于将指定的语音文件识别成文字。

#### 函数原型  

```
IQAVPTT int SpeechToText(String fileID)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| fileID    |string                      |语音文件 url|

#### 示例代码  
```
IQAVContext.GetInstance().GetPttCtrl().SpeechToText(fileID);
```

### 将指定的语音文件识别成文字（指定语言）
此接口用于将指定的语音文件识别成指定语言的文字。

####  函数原型  
```
IQAVPTT int SpeechToText(String fileID,String language)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| fileID    |String                     |语音文件 url|
| language    |String                     |参数参考[语音转文字的语言参数参考列表](https://github.com/TencentMediaLab/GME/blob/master/GME%20Developer%20Manual/GME%20SpeechToText.md)|

####  示例代码  
```
IQAVContext.GetInstance().GetPttCtrl().SpeechToText(fileID,"cmn-Hans-CN");
```


### 识别回调
将指定的语音文件识别成文字，通过委托传递消息。
#### 函数原型  
```
委托函数：
public delegate void QAVSpeechToTextCallback(int code, string fileid, string result);
事件函数：
public abstract event QAVSpeechToTextCallback OnSpeechToTextComplete;
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| code    |int                       |当code为0时，录制完成|
| fileid    |string                      |语音文件 url	|
| result    |string                      |转换的文本结果|

#### 示例代码  
```
对事件进行监听：
IQAVContext.GetInstance().GetPttCtrl().OnSpeechToTextComplete += mInnerHandler;
监听处理：
void mInnerHandler(int code, string fileid, string result){
    //识别回调
}
```
## 高级 API
### 获取版本号
获取 SDK 版本号，用于分析。
#### 函数原型
```
ITMGContext  abstract string GetSDKVersion()
```
#### 示例代码  
```
IQAVContext.GetInstance().GetSDKVersion();
```





### 设置打印日志等级
用于设置打印日志等级。
#### 函数原型
```
ITMGContext  SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
```


|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| logLevel    		|int   		|打印日志级别			|
| enableWrite    	|bool   		|是否写文件，默认为是	|
| enablePrint    	|bool   		|是否写控制台，默认为是	|



|ITMG_LOG_LEVEL|意义|
| -------------------------------|:-------------:|
|TMG_LOG_LEVEL_NONE=0		|不打印日志			|
|TMG_LOG_LEVEL_ERROR=1		|打印错误日志（默认）	|
|TMG_LOG_LEVEL_INFO=2			|打印提示日志		|
|TMG_LOG_LEVEL_DEBUG=3		|打印开发调试日志	|
|TMG_LOG_LEVEL_VERBOSE=4		|打印高频日志		|

#### 示例代码  
```
IQAVContext.GetInstance().SetLogLevel(TMG_LOG_LEVEL_NONE,true,true);
```

### 设置打印日志路径
用于设置打印日志路径。
默认路径为：

|平台     |路径        |
| ------------- |-------------|
|Windows 	|%appdata%\Tencent\GME\ProcessName|
|iOS    		|Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents|
|Android	|/sdcard/Android/data/xxx.xxx.xxx/files|
|Mac    		|/Users/username/Library/Containers/xxx.xxx.xxx/Data/Documents|

#### 函数原型
```
ITMGContext  SetLogPath(string logDir)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| logDir    		|NSString   		|路径|

#### 示例代码  
```
IQAVContext.GetInstance().SetLogPath(path);
```
### 获取诊断信息
获取音视频通话的实时通话质量的相关信息。该接口主要用来查看实时通话质量、排查问题等，业务侧可以忽略。
#### 函数原型  
```
IQAVRoom GetQualityTips()
```
#### 示例代码  
```
string tips = IQAVContext.GetInstance().GetRoom().GetQualityTips();
```

### 加入音频数据黑名单
将某个 id 加入音频数据黑名单。返回值为 0 表示调用失败。
#### 函数原型  

```
ITMGContext ITMGAudioCtrl AddAudioBlackList(string openId)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| openId    |NSString      |需添加黑名单的id|

#### 示例代码  

```
IQAVContext.GetInstance().GetAudioCtrl ().AddAudioBlackList (id);
```

### 移除音频数据黑名单
将某个 id 移除音频数据黑名单。返回值为 0 表示调用失败。
#### 函数原型  

```
ITMGContext ITMGAudioCtrl RemoveAudioBlackList(string openId)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| openId    |NSString      |需移除黑名单的 id|

#### 示例代码  

```
IQAVContext.GetInstance().GetAudioCtrl ().RemoveAudioBlackList (id);
```

