本章节将指导您如何在客户端对ILiveSDK采集的声音进行混音、变声等特效操作

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[点击下载]()

## 相关概念
混音一般是指把多种来源的声音，整合至一个立体音轨或单音音轨中，如在原声中添加背景音乐

变声一般是通过改变输入音频的音色、音调，使输出声音在感官上与原声音不同

ILiveSDK中主播端的音频采集、处理流程可参考下图
![](https://main.qcloudimg.com/raw/2ae58918ee38c5fba7575ba357a4a46e.jpg)

ILiveSDK中观众端的音频采集、处理流程如下
![](https://main.qcloudimg.com/raw/2fcfe50f8e40fc9bc0e61a67754c99b0.jpg)

混音操作需要对Androi的音频处理有一定的了解，本章节对于的demo中有简单的音频操作库，这里就不做过多说明。

## 具体实现


### 开启直播
创建房间，开启直播可参考（[创建房间](创建房间.md)。


### 注册音频数据处理器
用户在创建房间成功后，先向SDK注册音频采集的处理回调
```Java
ILiveSDK.getInstance().getAvAudioCtrl().registAudioDataCallback(int src_type,AVAudioCtrl.RegistAudioDataCompleteCallback callback(){
		@Override
		public int onComplete(AVAudioCtrl.AudioFrame audioFrame, int src_type) {

		}
})
```
该注册的机制是sdk每20ms执行一次音频数据处理对象RegistAudioDataCompleteCallbackWithByteBuffer的回调函数onComplete，回调函数onComplete中AudioFrame携带了20ms的原始麦克风数据及相关采样信息。
开发者可通过该回调函数对原始音频数据做混音处理。
```Java
public static class AudioFrame {
	public byte[] data;
	...
}
```
AudioFrame中data即为20ms的原始麦克风数据，混音处理完后需间音频数据重新赋值给data。

### 注销音频数据处理器
如不再需要对音频数据做处理，可调用注销接口
```Java
ILiveSDK.getInstance().getAvAudioCtrl().unregistAudioDataCallback(int src_type)
```

注：上面提到的注册与注销接口都需在主线程中调用


## API说明

### registAudioDataCallback
AVAudioCtrl类的方法，用于向SDK注册音频数据处理的回调
参数说明

|名称|类型|描述|
|--|--|--|
|src_type|int|需要处理音频源类型，参考AVAudioCtrl.AudioDataSourceType(注：只有某些类型的音频源可以做特效梳理，参考文章开头流程图的说明)|
|callback|RegistAudioDataCompleteCallback|音频处理回调|


### onComplete
AVAudioCtrl.RegistAudioDataCompleteCallback类的方法，SDK的音频引擎每隔20ms调用一次该方法
参数说明

|名称|类型|描述|
|--|--|--|
|src_type|int|音频源类型，参考AVAudioCtrl.AudioDataSourceType|
|audioFrame|AudioFrame|音频数据信息|

### AudioFrame
SDK的音频数据对象
参数说明：

|名称|类型|描述|
|--|--|--|
|data|byte[]|音频数据|
|bits|int|音频数据位宽，目前固定为16|
|channelNum|int|通道数|
|dataLen|int|音频帧的数据缓冲区大小，单位：字节。|
|identifier|int|音频帧所属的房间成员id(即userId)|
|sampleRate|int|采样率|
|srcTye|int|音频源类型|
|timeStamp|long|音频帧的时间戳，SDK内部会自动填写好，utc时间，0为无效值。|


### unregistAudioDataCallback
AVAudioCtrl类的方法，用于向SDK注销音频数据处理的回调
参数说明：

|名称|类型|描述|
|--|--|--|
|src_type|int|需要注销回调处理的音频源类型(与注册时对应)，参考AVAudioCtrl.AudioDataSourceType|



## 常见问题

- 混音后音频卡顿？
> sdk每20ms调用一次RegistAudioDataCompleteCallbackWithByteBuffer的函数onComplete，故在onComplete里处理的混音操作不能超过20ms，否则会有卡顿现象。另应避免在onComplete加锁。

- 混音后声音异常？
> 混音操作需要有一定的音频知识。混音要求各个输入音频的采样信息要一致，如不一致需要重采样。
这里需要简单说明的sdk默认抛出的人声数据为48K双声道。在做混音时如要混入的音频采样率不一致则可对SDK音频源做采样率设置。这样可不必再做重采样
对AUDIO_DATA_SOURCE_VOICEDISPOSE做采样率设置
```Java
AudioFrameDesc audio_desc = avAudioCtrl.getAudioDataFormat(AudioDataSourceType.AUDIO_DATA_SOURCE_VOICEDISPOSE);
audio_desc.sampleRate = 44100;//这里只是举例采样频率为44100，实际应用中应与要混音的音频采样率一直
avAudioCtrl.setAudioDataFormat(AudioDataSourceType.AUDIO_DATA_SOURCE_VOICEDISPOSE, audio_desc);

## 联系邮箱
如果对上述文档有不明白的地方，请反馈到trtcfb@qq.com
```
