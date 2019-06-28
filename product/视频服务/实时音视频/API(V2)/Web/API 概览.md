实时音视频 Web API 中包括了主动调用类的功能接口和触发设置的事件通知类接口，其中功能接口有基础功能接口和高级功能接口，事件通知有基础事件通知和高级事件通知。初级开发人员可以通过基础功能接口和基础事件通知完成基础开发接入，即可体验实时音视频主要功能。高级开发人员可以通过高级功能接口和高级事件通知的开发，体验实时音视频更高级功能。

### 基础功能接口

| API                   |  描述            |
| -------------------- | -------- |
| [WebRTCAPI.fn.detectRTC](https://cloud.tencent.com/document/product/647/17251#webrtcapi.fn.detectrtc)     | 检测是否支持 WebRTC |
| [WebRTCAPI](https://cloud.tencent.com/document/product/647/17251#webrtcapi)     | 初始化 |
| [WebRTCAPI.getLocalStream](https://cloud.tencent.com/document/product/647/17251#webrtcapi.getlocalstream)     | 获取本地音频/视频流 |
| [WebRTCAPI.enterRoom ](https://cloud.tencent.com/document/product/647/17251#webrtcapi.enterRoom)     | 创建或进入音视频房间 |
| [WebRTCAPI.startRTC](https://cloud.tencent.com/document/product/647/17251#webrtcapi.startrtc)   | 主动推流才需要用到 |
| [WebRTCAPI.stopRtc](https://cloud.tencent.com/document/product/647/17251#webrtcapi.startrtc)   | 停止推流 |
| [WebRTCAPI.quit](https://cloud.tencent.com/document/product/647/17251#webrtcapi.quit)     | 退出音视频房间 |

### 基础事件通知
| 事件                   |  描述            |
| -------------------- | -------- |
| [onLocalStreamAdd](https://cloud.tencent.com/document/product/647/17248#onlocalstreamadd)     | 本地视频流新增/更新 |
| [onRemoteStreamUpdate](https://cloud.tencent.com/document/product/647/17248#onremotestreamupdate)     | 远端视频流新增/更新 |
| [onRemoteStreamRemove](https://cloud.tencent.com/document/product/647/17248#onremotestreamremove)     | 远端视频流断开 |
| [onWebSocketClose](https://cloud.tencent.com/document/product/647/17248#onwebsocketclose)     |  websocket 断开 |
| [onRelayTimeout](https://cloud.tencent.com/document/product/647/17248#onrelaytimeout)     | 视频流 server 超时断开 |
| [onKickout](https://cloud.tencent.com/document/product/647/17248#onkickout)     | 被踢下线（同一个用户重复登录） |
| [onMuteAudio](https://cloud.tencent.com/document/product/647/17248#onMuteAudio)     | 远端用户关闭麦克风 |
| [onUnmuteAudio](https://cloud.tencent.com/document/product/647/17248#onUnmuteAudio)     | 远端用户打开麦克风 |
| [onMuteVideo](https://cloud.tencent.com/document/product/647/17248#onMuteVideo)     | 远端用户关闭摄像头|
| [onUnmuteVideo](https://cloud.tencent.com/document/product/647/17248#onUnmuteVideo)     | 远端用户打开摄像头 |



### 高级功能接口

| API                   |  描述            |
| -------------------- | -------- |
| [WebRTCAPI.updateStream](https://cloud.tencent.com/document/product/647/17250#webrtcapi.updatestream)     | 更新视频流 |
| [WebRTCAPI.openVideo](https://cloud.tencent.com/document/product/647/17250#webrtcapi.openvideo)     | 推流期间重新打开视频采集 |
| [WebRTCAPI.closeVideo](https://cloud.tencent.com/document/product/647/17250#webrtcapi.closevideo)     | 推流期间暂时关闭视频采集 |
| [WebRTCAPI.openAudio](https://cloud.tencent.com/document/product/647/17250#webrtcapi.openaudio)     | 推流期间重新打开音频采集 |
| [WebRTCAPI.closeAudio](https://cloud.tencent.com/document/product/647/17250#webrtcapi.closeaudio)     | 推流期间暂时关闭音频采集 |
| [WebRTCAPI.changeSpearRole](https://cloud.tencent.com/document/product/647/17250#webrtcapi.changeSpearRole)     | 切换音视频参数设定 |
| [WebRTCAPI.getVideoDevices](https://cloud.tencent.com/document/product/647/17250#webrtcapi.getVideoDevices)     | 枚举视频采集设备 |
| [WebRTCAPI.getAudioDevices](https://cloud.tencent.com/document/product/647/17250#webrtcapi.getAudioDevices)     | 枚举音频采集设备 |
| [WebRTCAPI.chooseVideoDevice](https://cloud.tencent.com/document/product/647/17250#webrtcapi.chooseVideoDevice)     | 选择视频采集设备 |
| [WebRTCAPI.chooseAudioDevice](https://cloud.tencent.com/document/product/647/17250#webrtcapi.chooseaudiodevice)     | 选择音频采集设备 |
| [WebRTCAPI.SoundMeter](https://cloud.tencent.com/document/product/647/17250#webrtcapi.SoundMeter)     | 声音输入检测 |


### 高级事件通知

| 事件                   |  描述            |
| -------------------- | -------- |
| [onPeerConnectionAdd](https://cloud.tencent.com/document/product/647/17252#onpeerconnectionadd)     | PeerConnection 新增通知 ，请确保您已经了解了 peer connection 通知的作用和意义 |





### 更新日志
> 2.6.1
    ## WebRTCAPI.getSpeakerDevices
        枚举音频输出设备
    ## WebRTCAPI.chooseSpeakerDevice
        枚举音频输出设备


### 联系我们

关注公众号"腾讯云视频"，给公众号发关键字"技术支持"，会有专人联系。

![](https://main.qcloudimg.com/raw/769293c3dbc0df8fbfb7d6a7cc904692.jpg)
