## SDK1.8.1
**1、添加**
- 视频采集支持16:9宽高比
- iOS8.0以上支持硬件编解码
- xPlatform更新到支持IPv6-Only的版本
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
- 修复主播场景下，部分观众方听不到声音的问题；
- 修复音频伴奏内存未释放问题；
- 修复若干Crash问题。

**4、接口变化**
1.QAVAudioCtrl
- 增加pauseAudio方法:停止音频引擎
- 增加resumeAudio方法:重启音频引擎

2.QAVRoom
- 修改getStatParam方法:接口名变为getQualityParam
- 增加getStatisticsParam方法:获取音视频无参考评分的分布和平均值

3.QAVVideoCtrl
- 删除setExternalCamAbility方法:该接口用来修改PC视频流控，现在不需要
- 删除enableBeauty方法:调用isEnableBeauty判断能否支持美颜之后，可以直接调用inputBeautyparam接口传入参数并开启美颜

4.QAVEndpoint 
- 增加lastVideoStampRecv属性:获取视频帧接收时间戳
- 增加lastVideoStampSend属性:获取视频帧发送时间戳
- 删除requestView方法:改用requestViewList方法
- 删除cancelView方法:改用cancelAllView方法

## SDK1.8.0和1.7接口变化
1. QAVAudioCtrl
	- 增加audioDataDispose方法，用于音频数据预处理回调；
	- 增加enableHighQuality方法，用于加强主播场景下开播模式的通话音质。
2. QAVContext
 - 增加getVersion方法，获取SDK版本信息。
3. QAVRoomDelegate
 - 增加OnPrivilegeDiffNotify方法，房间成员无某个通话能力权限却去使用相关通话能力而导致的异常通知的函数；
 - 增加OnSemiAutoRecvCameraVideo方法，自动接收摄像头视频的事件通知。
4. QAVRoomParam
 - 增加videoRecvMode参数，控制视频接收模式。
5. QAVMultiRoom
 - 增加ChangeAVControlRole方法，不重新进入房间的情况下进行用户角色的切换。
6. QAVVideoCtrl
 - 增加isEnableBeauty方法，外部查询机型是否支持美颜；
 - 增加OnLocalVideoPreProcess方法，本地画面预处理视频回调。
7. QAVEndpoint 
 - 增加lastAudioStampSend属性，获取当前音频的上行时间戳；
 - 增加lastAudioStampRecv属性，获取当前音频的下行时间戳。                       