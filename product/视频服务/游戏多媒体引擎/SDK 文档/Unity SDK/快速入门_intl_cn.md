## 简介

欢迎使用腾讯云游戏多媒体引擎 SDK 。为方便 Unity 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 Unity 开发的快速接入文档。


## 使用流程图
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)


### 使用 GME 重要事项

GME 快速入门文档只提供最主要的接入接口，更多详细接口请参考 [相关接口文档](https://cloud.tencent.com/document/product/607/15228)。


|重要接口     | 接口含义|
| ------------- |:-------------:|
|Init    		|初始化 GME 	|
|Poll    		|触发事件回调	|
|EnterRoom	 	|进房  		|
|EnableAudioCaptureDevice	 	|开关采集设备 	|
|EnableAudioSend		|打开关闭音频上行 	|
|EnableAudioPlayDevice    			|开关播放设备		|
|EnableAudioRecv    					|打开关闭音频下行	|

**说明：**
** GME 的接口调用成功后返回值为 QAVError.OK，数值为 0。**
** GME 的接口调用要在同一个线程下。**
** GME 加入房间需要鉴权，请参考文档关于鉴权部分内容。**

**GME 需要调用 Poll 接口触发事件回调。**


## 快速接入步骤


### 1、初始化 SDK
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

### 2、触发事件回调
通过在 update 里面周期的调用 Poll 可以触发事件回调。
#### 函数原型

```
ITMGContext public abstract int Poll();
```

### 3、加入房间
用生成的鉴权信息进房。加入房间默认不打开麦克风及扬声器。


#### 函数原型
```
ITMGContext EnterRoom(int roomID, int roomType, byte[] authBuffer)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| roomID		|int    	|房间号，只支持32位					|
| roomType 	|ITMGRoomType		|房间音频类型		|
| authBuffer 	|Byte[] 	|鉴权码					|

|音频类型     	|含义|参数|音量类型|控制台推荐采样率设置|适用场景|
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|流畅音质	|1|扬声器：通话音量；耳机：媒体音量	|如对音质无特殊需求，16K 采样率即可；					|流畅优先、超低延迟实时语音，应用在游戏内开黑场景，适用于 FPS、MOBA 等类型的游戏；	|							
| ITMG_ROOM_TYPE_STANDARD			|标准音质	|2|扬声器：通话音量；耳机：媒体音量	|根据对音质的需求，可以选择16k/48k采样率				|音质较好，延时适中，适用于狼人杀、棋牌等休闲游戏的实时通话场景；	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|高清音质	|3|扬声器：媒体音量；耳机：媒体音量	|为了保证最佳效果，建议控制台设置 48k 采样率的高音质配置	|超高音质，延时相对大一些，适用于音乐舞蹈类游戏以及语音社交类 APP；适用于播放音乐、线上K歌等有高音质要求的场景；	|

- 如对音量类型或场景有特殊需求，请联系一线客服反馈；
- 控制台采样率设置会直接影响游戏语音效果，请在 [控制台](https://console.cloud.tencent.com/gamegme) 上再次确认采样率设置是否符合项目使用场景。
#### 示例代码  
```
IQAVContext.GetInstance().EnterRoom(roomId, ITMG_ROOM_TYPE_FLUENCY, authBuffer);
```

### 4、加入房间事件的回调
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

### 5、开启关闭采集设备
此接口用来开启/关闭采集设备。加入房间默认不打开设备。
- 只能在进房后调用此接口，退房会自动关闭设备。
- 在移动端，打开采集设备通常会伴随权限申请，音量类型调整等操作。

#### 函数原型  
```
ITMGAudioCtrl int EnableAudioPlayDevice(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |如果需要打开采集设备，则传入的参数为 true，如果关闭采集设备，则参数为 false|
#### 示例代码  
```
打开采集设备
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioCaptureDevice(true);
```


### 6、打开关闭音频上行
此接口用于打开/关闭音频上行。如果采集设备已经打开，那么会发送采集到的音频数据。如果采集设备没有打开，那么仍旧无声。采集设备的打开关闭参见接口 EnableAudioCaptureDevice。

#### 函数原型  
```
ITMGAudioCtrl int EnableAudioSend(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |如果需要打开音频上行，则传入的参数为 true，如果关闭音频上行，则参数为 false|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioSend(true);
```

### 7、开启关闭播放设备
此接口用于开启关闭播放设备。
> 函数原型  
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



### 8、打开关闭音频下行
此接口用于打开/关闭音频下行。如果播放设备已经打开，那么会播放房间里其他人的音频数据。如果播放设备没有打开，那么仍旧无声。采集设备的打开关闭参见接口 参见EnableAudioPlayDevice。

#### 函数原型  
```
ITMGAudioCtrl int EnableAudioRecv(bool isEnabled)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |如果需要打开音频下行，则传入的参数为 true，如果关闭音频下行，则参数为 false|

#### 示例代码  
```
IQAVContext.GetInstance().GetAudioCtrl().EnableAudioRecv(true);
```


## 关于鉴权
### 实时语音鉴权信息
生成 AuthBuffer，用于相关功能的加密和鉴权，相关参数获取及详情见 [GME 密钥文档](https://cloud.tencent.com/document/product/607/12218)。      
离线语音获取鉴权时，房间号参数必须填0。
该接口返回值为 Byte[] 类型。
#### 函数原型
```
QAVAuthBuffer GenAuthBuffer(int appId, int roomId, string openId, string key)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------|
| appId    		|int   		|来自腾讯云控制台的 SdkAppId 号码		|
| roomId    		|int   		|房间号，只支持32位				|
| openId    	|String 	|用户标识					|
| key    		|string 	|来自腾讯云控制台的密钥				|
#### 示例代码  

```
byte[] GetAuthBuffer(string appId, string userId, int roomId)
    {
	return QAVAuthBuffer.GenAuthBuffer(int.Parse(appId), roomId, userId, "a495dca2482589e9");
}
```
