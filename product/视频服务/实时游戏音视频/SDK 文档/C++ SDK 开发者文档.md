欢迎使用腾讯云游戏多媒体引擎 SDK。为方便 C++ 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 C++ 开发的接入技术文档。

## SDK初始化
### 获取单例
TMGSDK 以单例的形式提供，所有调用都从 ITMGContext 开始，通过 ITMGDelegate 回调回传给应用，必须首先设置。
#### 函数原型
```
ITMGContext virtual void TMGDelegate(ITMGDelegate* delegate)
```
#### 示例代码
```
ITMGContext* m_pTmgContext;
m_pTmgContext = ITMGContextGetInstance();
```

### 消息传递
TMG 的消息通过 ITMGDelegate 传给应用，消息类型参考 ITMG_MAIN_EVENT_TYPE，data 在 Windows 平台下是 json 字符串格式， 具体 key-value 参见说明文档。
#### 函数原型
```
 ITMGDelegate virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
```
#### 示例代码
```
//函数实现：
class Callback : public ITMGDelegate
{
	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
	{
  		switch(eventType)
  		{
   			//判断消息类型并处理
  		}
 	}
}

Callback*  p = new Callback ();
m_pTmgContext->TMGDelegate(p);
```
#### 消息列表：

|消息     | 消息代表的描述
| ------------- |-------------|
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		|进入音视频房间消息
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		|退出音视频房间消息
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT	|房间因为网络等原因断开消息
| ITMG_MAIN_EVENT_TYPE_ENABLE_MIC    		|打开麦克风消息
| ITMG_MAIN_EVENT_TYPE_DISABLE_MIC    		|关闭麦克风消息
|ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER		|打开扬声器消息
|ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER		|关闭扬声器消息
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROLE		|切换角色消息
|ITMG_MAIN_EVNET_TYPE_USER_UPDATE			|房间成员更新消息

##### Data 列表

|消息     | Data         |例子|
| ------------- |-------------|------------- |
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    			|result; error_info	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    			|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    	|result; error_info  	|{"error_info":"waiting timeout, please check your network","result":0}
| ITMG_MAIN_EVENT_TYPE_ENABLE_MIC    			|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_DISABLE_MIC    			|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER    		|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER    		|result; error_info  	|{"error_info":"","result":0}
| ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE	|result; error_info  	|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"扬声器 (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":false,"result":0}
| ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE    	|result; error_info  	|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"扬声器 (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":false,"result":0}
| ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    		|result; error_info  	|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"麦克风 (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":true,"result":0}
| ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    		|result; error_info 	|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"麦克风 (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":true,"result":0}
| ITMG_MAIN_EVNET_TYPE_USER_UPDATE    			|user_list;  event_id	|{"event_id":1,"user_list":["0"]}


## 实时语音接入
### 设置相关信息
获取相关信息，由腾讯云控制台申请，详情见 [游戏音视频接入指引](/document/product/607/10782)。
>在 EnterRoom 函数调用之前要先调用 SetAppInfo 函数及 SetAppVersion 函数进行相关信息的设置

此函数需要来自腾讯云控制台的 SdkAppId 号码及 accountType 号码作为参数，再加上 Id，这个 Id 是唯一标识一个用户，规则由 App 开发者自行制定，App 内不重复即可（Id 需参考鉴权使用文档）。
#### 函数原型
```
ITMGContext virtual void SetAppInfo(const char* sdkAppId,const char* accountType, const char* openId)
```
|参数     | 类型         |描述|
| ------------- |-------------|-------------
| sdkAppId    	|char  	|来自腾讯云控制台的 SdkAppId 号码		|
| accountType    |char  	|来自腾讯云控制台的 accountType 号码	|
| openID    		|char  	|OpenID 为 Int32 类型，必须大于 10000 	|
#### 示例代码
```
ITMGContext* m_pTmgContext;
m_pTmgContext->SetAppInfo(strAppid, strAccountType, strUserID);
```

设置版本信息，用于查 Log 信息及 Bug 时使用，方便后台统计, 策略调整等（不设置不影响功能）。
#### 函数原型
```
ITMGContext virtual void SetAppVersion(const char* appVersion)
```
|参数     | 类型         |描述|
| ------------- |-------------|-------------
| appVersion    |char  |版本号|
#### 示例代码
```
ITMGContext* m_pTmgContext;
m_pTmgContext->SetAppVersion("Test_demo_1.0");
```
获取 SDK 版本号。
#### 函数原型
```
ITMGContext virtual const char* GetSDKVersion()
```
#### 示例代码
```
ITMGContext* m_pTmgContext;
m_pTmgContext->GetSDKVersion;
```
接下来是生成 AuthBuffer，用于相关功能的加密和鉴权，相关参数获取及详情参考鉴权使用文档。
>注意：在加入房间之前需要 AuthBuffer 作为参数。

### 加入房间
用生成的权鉴进房，会收到消息为 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM 的回调。
>注意:1、加入房间默认不打开麦克风及扬声器。
>2、在 EnterRoom 函数调用之前要先调用 SetAppInfo 函数及 SetAppVersion 函数进行相关信息的设置
关于角色的设置，在[游戏实时语音角色说明](/document/product/607/15172)中有介绍。
#### 函数原型
```
ITMGContext virtual void EnterRoom(int relationId, const char* role, const char* authBuff,int buffLen)
```
|参数     | 类型         |描述|
| ------------- |-------------|-------------
| relationId		|int   	|房间号，大于等于六位的整数							|
| role    			|char    	|角色名称，按照需求设置，也可以询问接入技术人员获取	|
| authBuffer    	|char    	|鉴权码												|
| buffLen   		|int   	|鉴权码长度											|
#### 示例代码
```
m_pTmgContext->EnterRoom(nRoomID, strUserRole, strAuthBuffer, nLength);
```

### 加入房间事件的回调
加入房间完成后会发送信息 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM，在 OnEvent 函数中进行判断。
代码说明：
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //加入房间
		    break;
	        }
		...
            }
        }
}
```

### 判断是否已经进入房间
通过调用此函数可以判断是否已经进入房间，返回值为 BOOL 类型。
#### 函数原型
```
ITMGContext virtual bool IsRoomEntered()
```
#### 示例代码
```
m_pTmgContext->IsRoomEntered();
```

### 退出房间
通过调用此函数可以退出所在房间。
#### 函数原型
```
ITMGContext virtual void ExitRoom()
```
#### 示例代码
```
m_pTmgContext->ExitRoom();
```

### 退出房间回调
退出房间完成回调，SDK 通过此回调通知 APP 成功退出了房间，事件为 ITMG_MAIN_EVENT_TYPE_EXIT_ROOM。
#### 示例代码
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //加入房间
		    break;
	        }
		...
		case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM:
		{
		    //退出房间
		    break;
	        }
            }
        }
}
```

### 成员状态变化
该事件在状态变化才通知，状态不变化的情况下不通知。如需实时获取成员状态，请在上层收到通知时缓存，事件消息为 ITMG_MAIN_EVNET_TYPE_USER_UPDATE，其中 data 包含两个信息，event_id 及 user_list，在 OnEvent 函数中需要对信息 event_id 进行判断。

|event_id     | 含义         |应用侧维护内容|
| ------------- |-------------|-------------|
| ITMG_EVENT_ID_USER_ENTER    			|有成员进入房间		|应用侧维护成员列表		|
| ITMG_EVENT_ID_USER_EXIT    			|有成员退出房间		|应用侧维护成员列表		|
| ITMG_EVENT_ID_USER_HAS_AUDIO    	|有成员开启麦克风	|应用侧维护通话成员列表	|
| ITMG_EVENT_ID_USER_NO_AUDIO    	|有成员关闭麦克风	|应用侧维护通话成员列表	|

#### 示例代码
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		...
		case ITMG_MAIN_EVNET_TYPE_USER_UPDATE:
		//角色状态变化
		{
		    //开发者对 Json 类型参数进行解析，得到信息 event_id及 user_list
		    switch (eventID)
 		    {
 		    case ITMG_EVENT_ID_USER_ENTER:
  			    //有成员进入房间
  			    break;
 		    case ITMG_EVENT_ID_USER_EXIT:
  			    //有成员退出房间
			    break;
		    case ITMG_EVENT_ID_USER_HAS_AUDIO:
			    //有成员开启麦克风
			    break;
		    case ITMG_EVENT_ID_USER_NO_AUDIO:
			    //有成员关闭麦克风
			    break;
		    default:
			    break;
 		    }
		    break;
	        }
        }
    }
}
```

### 获取麦克风设备数量
此函数用来获取麦克风设备数量。
>注意：需要在开启麦克风之前调用。

#### 函数原型
```
ITMGAudioCtrl virtual int GetMicListCount(int& nCount)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| nCount    |int     |指定一个传值的对象的地址，传递设备数量|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->GetMicListCount(nCount);
```

### 枚举麦克风设备
此函数用来枚举麦克风设备。需要先获取麦克风设备数量。
>注意：需要在开启麦克风之前调用。

#### 函数原型
```
ITMGAudioCtrl virtual int GetMicList(TMGAudioDeviceInfo* ppDeviceInfoList, int& nCount)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| ppDeviceInfoList    |TMGAudioDeviceInfo     |设备列表|
| nCount    |int     |获取的麦克风设备数量|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicList(ppDeviceInfoList,nCount);
```

### 获取扬声器设备数量
此函数用来获取扬声器设备数量。
>注意：需要在开启扬声器之前调用。

#### 函数原型
```
ITMGAudioCtrl virtual int GetSpeakerListCount(int& nCount)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| nCount    |int     |指定一个传值的对象的地址，传递设备数量|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerListCount(nCount);
```

### 枚举扬声器设备
此函数用来枚举扬声器设备。需要先获取扬声器设备数量。
>注意：需要在开启扬声器之前调用。

#### 函数原型
```
ITMGAudioCtrl virtual int GetSpeakerList(TMGAudioDeviceInfo* ppDeviceInfoList, int& nCount)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| ppDeviceInfoList    |TMGAudioDeviceInfo     |设备列表|
| nCount    |int     |获取的扬声器设备数量|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerList(ppDeviceInfoList,nCount);
```

### 麦克风开启关闭事件
此函数用来开启及关闭麦克风。
>注意:加入房间默认不打开麦克风及扬声器。

#### 函数原型
```
ITMGAudioCtrl virtual int EnableMic(bool bEnabled, const char* pMicId)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| enable    |bool     |如果需要关闭麦克风，则传入的参数为 true，如果打开麦克风，则参数为 false		|
| pMicId    |char     |麦克风ID																	|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableMic(true,pMicId);
pTmgAudioCtrl->EnableMic(false,pMicId);
```

### 麦克风事件的回调
麦克风事件的回调调用函数 OnEvent，SDK 通过此回调通知成功调用了麦克风，事件消息为 ITMG_MAIN_EVENT_TYPE_ENABLE_MIC， ITMG_MAIN_EVENT_TYPE_DISABLE_MIC，在 OnEvent 函数中对事件消息进行判断。

#### 示例代码
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //加入房间
		    break;
	        }
		...
		case ITMG_MAIN_EVENT_TYPE_ENABLE_MIC:
		{
		    //开麦克风回调
		    break;
	        }
		case ITMG_MAIN_EVENT_TYPE_DISABLE_MIC:
		{
		    //关麦克风回调
		    break;
	        }
            }
        }
}
```

### 麦克风状态获取
此函数获取麦克风状态。
#### 函数原型
```
ITMGAudioCtrl virtual int GetMicState()
```
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicState();
```

### 获取麦克风实时音量
此函数用于获取麦克风实时音量，返回值为 int 类型。
#### 函数原型
```
ITMGAudioCtrl virtual int GetMicLevel()
```
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicLevel();
```

### 设置麦克风的软件音量
此函数用于设置麦克风的软件音量。参数 volume 用于设置麦克风的软件音量，当数值为 0 的时候表示静音，当数值为 100 的时候表示音量不增不减，默认数值为 100。
#### 函数原型
```
ITMGAudioCtrl virtual void SetMicVolume(int volume)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| volume    |int      |设置音量，范围 0 到 100|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->SetMicVolume(volume);
```

### 获取麦克风的软件音量
此函数用于获取麦克风的软件音量。返回值为一个int类型数值。
#### 函数原型
```
ITMGAudioCtrl virtual int GetMicVolume()
```
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetMicVolume();
```

### 扬声器开启关闭事件
此函数用于设置扬声器开启关闭。
#### 函数原型
```
ITMGAudioCtrl virtual int EnableSpeaker(bool bEnabled, const char* pSpeakerID)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| enable   		|bool       	|如果需要关闭扬声器，则传入的参数为 false，如果打开扬声器，则参数为 true	|
| pSpeakerID    	|char      	|扬声器ID																|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableSpeaker(true,pSpeakerID);
pTmgAudioCtrl->EnableSpeaker(false,pSpeakerID);
```

### 扬声器事件的回调
扬声器事件回调，SDK 通过此回调通知成功调用了扬声器，事件消息为 ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER， ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER。
#### 示例代码
```
class Callback : public ITMGDelegate
{
 	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
 	{
 	    switch(eventType)
	    {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		    //加入房间
		    break;
	        }
		...
		case ITMG_MAIN_EVENT_TYPE_ENABLE_SPEAKER:
		{
		    //开启扬声器回调
		    break;
	        }
		case ITMG_MAIN_EVENT_TYPE_DISABLE_SPEAKER:
		{
		    //关闭扬声器回调
		    break;
	        }
            }
        }
}
```

### 扬声器状态获取
此函数用于扬声器状态获取。返回值为 int 类型数值。
#### 函数原型
```
ITMGAudioCtrl virtual int GetSpeakerState()
```

#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerState();
```

### 获取扬声器实时音量
此函数用于获取扬声器实时音量。返回值为 int 类型数值，表示扬声器实时音量。
#### 函数原型
```
ITMGAudioCtrl virtual int GetSpeakerLevel()
```

#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->GetSpeakerLevel();
```

### 设置扬声器的软件音量
此函数用于设置扬声器的软件音量。
>注意：参数 volume 用于设置扬声器的软件音量，当数值为 0 的时候表示静音，当数值为 100 的时候表示音量不增不减，默认数值为 100。

#### 函数原型
```
ITMGAudioCtrl virtual void SetSpeakerVolume(int vol)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| vol    |int        |设置音量，范围 0 到 100|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->SetSpeakerVolume(vol);
```

### 获取扬声器的软件音量
此函数用于获取扬声器的软件音量。返回值为 int 类型数值，代表扬声器的软件音量。
>注意：Level 是实时音量，Volume 是扬声器的软件音量，最终声音音量相当于 Level*Volume%。举个例子：实时音量是数值是 100 的话，此时Volume的数值是 60，那么最终发出来的声音数值也是 60。

#### 函数原型
```
ITMGAudioCtrl virtual int GetSpeakerVolume()
```
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->GetSpeakerVolume();
```

### 启动耳返
此函数用于启动耳返。
#### 函数原型
```
ITMGAudioCtrl virtual int EnableLoopBack(bool enable)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| enable    |bool         |设置是否启动|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableLoopBack(true);
pTmgAudioCtrl->EnableLoopBack(false);
```

### 获取诊断信息
获取音视频通话的实时通话质量的相关信息。该函数主要用来查看实时通话质量、排查问题等。
#### 函数原型
```
ITMGRoom virtual const char* GetQualityTips()
```

#### 示例代码
```
m_pTmgContext.GetRoom().GetQualityTips();
```

## 3D音效接入
### 开关3D音效
此函数用于开关 3D音效，返回值为 int 类型数值。
#### 函数原型
```
ITMGAudioCtrl virtual int EnableSpatializer(bool bEnabled)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| bEnabled    |bool         |设置是否开启|
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->EnableSpatializer(true);
pTmgAudioCtrl->EnableSpatializer(false);
```

### 获取当前 3D 音效状态
此函数获取当前 3D 音效状态，返回值为 bool 类型数值。
#### 函数原型
```
ITMGAudioCtrl virtual bool IsEnableSpatializer()
```
#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();

pTmgAudioCtrl->IsEnableSpatializer();
```

### 更新声源方位
此函数用于更新声源方位。
#### 函数原型
```
ITMGAudioCtrl virtual int UpdateSpatializer(std::string& identifier,float azimuth,float elevation,float distance_cm)
```

|参数     | 类型         |描述|
| ------------- |-------------|-------------
| identifier    	|string   		|OpenID 为Int32类型，必须大于 10000		|
| azimuth    		|float        	|方位参数								|
| elevation    	|float         	|角度参数								|
| distance_cm    	|float         	|距离参数，以厘米为距离单位				|

#### 函数原理
![](https://main.qcloudimg.com/raw/0f90e8e84915c3f34482b1d40b0630c0.png)

从图看参数，假设接收端用户为 A 点位置，发送端用户为 B点位置 ,<a href="https://www.codecogs.com/eqnedit.php?latex=\angle&space;CAB'" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\angle&space;CAB'" title="\angle CAB'" /></a> 为 azimuth 方位，<a href="https://www.codecogs.com/eqnedit.php?latex=\angle&space;B'AB" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\angle&space;B'AB" title="\angle B'AB" /></a> 为 elevation 角度，AB 即为 distance_cm 距离。
假设坐标 <a href="https://www.codecogs.com/eqnedit.php?latex=A\left&space;(&space;x_{1},&space;y_{1},&space;z_{1}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A\left&space;(&space;x_{1},&space;y_{1},&space;z_{1}&space;\right&space;)" title="A\left ( x_{1}, y_{1}, z_{1} \right )" /></a> ，<a href="https://www.codecogs.com/eqnedit.php?latex=B\left&space;(&space;x_{2},&space;y_{2},&space;z_{2}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B\left&space;(&space;x_{2},&space;y_{2},&space;z_{2}&space;\right&space;)" title="B\left ( x_{2}, y_{2}, z_{2} \right )" /></a>，转换为<a href="https://www.codecogs.com/eqnedit.php?latex=A\left&space;(&space;0,&space;0,0&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A\left&space;(&space;0,&space;0,0&space;\right&space;)" title="A\left ( 0, 0,0 \right )" /></a>，<a href="https://www.codecogs.com/eqnedit.php?latex=B\left&space;(&space;x,&space;y,z\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B\left&space;(&space;x,&space;y,z\right&space;)" title="B\left ( x, y,z\right )" /></a>，其中 <a href="https://www.codecogs.com/eqnedit.php?latex=x=x_{2}-x_{1},y=y_{2}-y_{1},z=z_{2}-z_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x=x_{2}-x_{1},y=y_{2}-y_{1},z=z_{2}-z_{1}" title="x=x_{2}-x_{1},y=y_{2}-y_{1},z=z_{2}-z_{1}" /></a>
则计算公式为：

![](https://main.qcloudimg.com/raw/e1aa4d09b144af4ea920d63cf9cac6bb.png)

#### 示例代码
```
ITMGAudioCtrl* pTmgAudioCtrl = m_pTmgContext->GetAudioCtrl();
pTmgAudioCtrl->UpdateSpatializer(identifier,azimuth,elevation,distance_cm);
```

#### 函数附录
```
/*     ^
      z|   y(azi=0)
       |  /
       | /
	   .----->x(azi=90)    ...w = 90-azi
*/
#define QDSP_PAI  3.1415926535897

void xyz2dae(float *dist,float *azi,float *elve,float x,float y,float z)
{
	float paitodu = 180/QDSP_PAI;
	float sqxy = sqrt(x*x+y*y);

	*dist = sqrt(x*x + y*y + z*z);

	if (x)
	{
		if (y)
		{
			if (x>0)
			{
				*azi = 90 - atan(y/x)*paitodu;
			}
			else
			{
				*azi = -90 - atan(y/x)*paitodu;
			}

		}
		else
		{
			if (x>0)
			{
				*azi = 90;
			}
			else
			{
				*azi = -90;
			}
		}

	}
	else
	{
		if (y>0)
		{
			*azi = 0;
		}
		else
		{
			*azi = 180;
		}
	}

	if (sqxy)
	{
		*elve = atan(z/sqxy)*paitodu;
	}
	else
	{
		if (z>0)
		{
			*elve = 90;
		}
		else
		{
			*elve = -90;
		}

	}
}


void dae2xyz(float *x,float *y,float *z,float dist,float azi,float elve)
{
	float sqxy;
	float dutopai = QDSP_PAI/180;

	*z = dist*sin(elve*dutopai);
	sqxy = dist*cos(elve*dutopai);
	*x = sqxy*cos((90-azi)*dutopai);
	*y = sqxy*sin((90-azi)*dutopai);
}
```
