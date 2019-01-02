本章节将指导您如何在客户端采集自定义的音频，并且上行播放给观众

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[点击下载]()

## 相关说明
自行音频采集是指用户不用ILiveSDK默认的音频采集（目前ILiveSDK）是通过手机的麦克风录入采集音频的。

某些场景下，用户需自己控制麦克风录入声音，或如添加背景音乐，或者需要对SDK采集的音频加工后（如美声，变音等）再上行。对此ILiveSDK提供了一套较简洁的方案。

PS:对于添加背景音乐和对SDK采集音频加工SDK有更加单的方案，可参考其它教程或API。
## 具体实现

### 实现自定义音频采集
这里以自行打开麦克风来举例说明。
由于是自行打开麦克风来采集视频，所以此处我们要对麦克风采集做一些操作。
这里直接上代码示范Android通过麦克风采集音频的操作，这是Android的原生知识，就不做过多说明。

开启麦克风采集
```Java
private boolean startMic;
static final int frequency = 44100; //音频采样频率
static final int channelConfiguration = AudioFormat.CHANNEL_IN_STEREO; //音频的录制的声道
static final int audioEncoding = AudioFormat.ENCODING_PCM_16BIT; //音频编码率
private class RecordThread extends Thread {
	@Override
	public void run() {
		//根据采样参数获取每一次音频采样大小
		int recBufSize = AudioRecord.getMinBufferSize(frequency, channelConfiguration, audioEncoding) * 2;
		AudioRecord audioRecord = new AudioRecord(MediaRecorder.AudioSource.MIC, frequency, channelConfiguration, audioEncoding, recBufSize);
		byte[] recBuf = new byte[recBufSize];
		audioRecord.startRecording();
		while (startMic) {
			int readLen = audioRecord.read(recBuf, 0, recBufSize);
		}
		audioRecord.stop();
	}
}
```

### 开启直播
创建房间，开启直播可参考（[创建房间](创建房间.md))。
此处有几点需要主要：
1、后台spear角色配置里音频场景要设置为“开播”（开播场景会占用本地录音权限），也可以设置为“观看”这样就不会占用本地音频设备了；
2、进房间时mic和speaker都要打开；
3、进房间成功后调用接口AVAudioCtrl.changeAudioCategory切换至观看场景（第一步如果设置为“观看”场景此步省略）；
```Java
ILiveRoomOption option = new ILiveRoomOption(ILiveLoginManager.getInstance().getMyUserId())
	.autoMic(true) //开启mic
	.autoSpeaker(true) //开启speaker
	.videoMode(ILiveConstants.VIDEOMODE_NORMAL)
	.controlRole(Constants.ROLE_MASTER);


ILiveRoomManager.getInstance().createRoom(iRoomNum, option, new ILiveCallBack() {
		@Override
		public void onSuccess(Object data) {
		    //创建房间成功后切换至观看场景
			ILiveSDK.getInstance().getAvAudioCtrl().changeAudioCategory(AVRoomMulti.AUDIO_CATEGORY_MEDIA_PLAYBACK);
		}

		@Override
		public void onError(String module, int errCode, String errMsg) {
		}
	});		
```

### 开启自定义音频采集，填充音频数据
用户在创建房间成功后，先调用接口开启SDK的允许外部音频采集功能
```Java
ILiveSDK.getInstance().getAvAudioCtrl().enableExternalAudioDataInput(true);
```

开启允许外部音频采集后，用户需将自行采集的数据给到SDK进行上传。
参考最开始的麦克风采集音频代码，我们可将麦克风采集到的音频数据通过填充接口给到SDK
```Java
ILiveSDK.getInstance().getAvAudioCtrl().fillExternalAudioFrame(byte[] datas, int dataLen, int sampleRate, int channels, int bits)
```

注：此处的两个接口都需在主线程中调用


## API说明

### changeAudioCategory
AVAudioCtrl类的方法，用于切换用户的实时场景
参数说明

|名称|类型|描述|
|--|--|--|
|int|category|AVRoomMulti.AUDIO_CATEGORY_VOICECHAT 实时场景 AVRoomMulti.AUDIO_CATEGORY_MEDIA_PLAY_AND_RECORD 主播模式 AVRoomMulti.AUDIO_CATEGORY_MEDIA_PLAYBACK 观看者模式 AVRoomMulti.AUDIO_CATEGORY_MEDIA_PLAY_AND_RECORD_HIGH_QUALITY 高音质模式|


### fillExternalAudioFrame
AVAudioCtrl类的方法，用于开启SDK允许外部采集音频功能
参数说明：

|名称|类型|描述|
|--|--|--|
|enable|boolean|是否允许开启|

### fillExternalAudioFrame
AVAudioCtrl类的方法，用于向SDK填充自行采集的音频数据
参数说明：

|名称|类型|描述|
|--|--|--|
|datas|byte[]|音频数据|
|dataLen|int|数据长度，即datas的长度|
|sampleRate|int|音频采样率 可取值：8000,16000,32000,44100,48000|
|channels|int|音频数据 1：单声道 2：双声道|
|bits|int|音频采样精度 可取值：8,16|



## 常见问题

- 音频fillExternalAudioFrame的参数该如何设置？
> 自定义采集需开发者对音频相关知识有一定的了解。参数的设置需参考API说明
