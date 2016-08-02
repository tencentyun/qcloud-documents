## SDK1.8.1
**1、添加**

- 视频采集支持16:9宽高比
- 音频的2s上报增加上行码率


**2、修改**
- 采集宽高比对齐云配置下发宽高比，支持4:3和16:9之间的互相转换；
- 主播模式下视频软件编码效果优化。

**3、修复**
- 修复视频画面花屏、绿屏、倒播的问题；
- 修复视频观看方偶现唇音不同步的问题；
- 修复个别机型视频画面被压缩/拉伸的问题；
- 修复关闭视频时，音频也会被短暂关闭的问题；
- 修复视频高码率场景，实际码率达不到云配置码率的问题；
- 修复若干Crash问题。

**4、接口变化**
1.AVRoom
- 修改getQualityParas方法：接口名改为getQualityParam
- 增加getStatisticsParam方法:获取音视频无参考评分的分布和平均值

2.AVEndpoint
- 增加getLastVideoStampRecv方法:获取视频帧接收时间戳
- 增加getLastVideoStampSend方法:获取视频帧发送时间戳

3.AVVideoCtrl
- 删除enableBeauty方法:调用isEnableBeauty判断能否支持美颜之后，可以直接调用inputBeautyparam接口传入参数并开启美颜

## SDK1.8.0和1.7接口变化
1. AVAudioCtrl
	- AudioDataSourceType增加一个新的枚举值AUDIO_DATA_SOURCE_VOICEDISPOSE，麦克风音频数据预处理选项，自定义音效预处理。
2. AVContext
 - createContext方法重命名为createInstance；
 - destroyContext静态方法调整为destroy实例方法；
 - startContext方法重命名为start；
 - stopContext方法重命名为stop；
 - StartContextCallback接口重命名为StartCallback；
 - StopContextCallback接口重命名为StopCallback；
 - GetSDKVersion方法重命名为GetVersion；
 - 删除onPause方法；
 - 删除onResume方法。
3. AVEndpoint
 - 增加getLastAudioStampSend方法，获取当前音频的上行时间戳；
 - 增加getLastAudioStampRecv方法，获取当前音频的下行时间戳。
4. AVRoomMulti
 - 增加ChangeAVControlRole方法，房间通话中动态修改流控角色； 
5. AVRoomMulti.EnterRoomParam
 - 增加videoRecvMode参数，控制视频接收模式。
6. AVRoom.Delegate
 - 增加OnSemiAutoRecvCameraVideo方法，半自动模式接收摄像头视频的事件通知。
7. AVVideoCtrl
 - 增加isEnableBeauty方法，外部查询机型是否支持美颜。