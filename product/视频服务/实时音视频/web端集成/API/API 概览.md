实时音视频 Web API 中包括了主动调用类的功能接口和触发设置的事件通知类接口，其中功能接口有基础功能接口和高级功能接口，事件通知有基础事件通知和高级事件通知。初级开发人员可以通过基础功能接口和基础事件通知完成基础开发接入，即可体验实时音视频主要功能。高级开发人员可以通过高级功能接口和高级事件通知的开发，体验实时音视频更高级功能。

### 基础功能接口

| API                   |  描述            |
| -------------------- | -------- |
| [WebRTCAPI.fn.detectRTC](#webrtcapi.fn.detectrtc)     | 检测是否支持 WebRTC |
| [WebRTCAPI](#webrtcapi)     | 初始化 |
| [WebRTCAPI.createRoom](#webrtcapi.createroom)     | 创建或进入音视频房间 |
| [WebRTCAPI.quit](#webrtcapi.quit)     | 退出音视频房间 |

### 基础事件通知
| 事件                   |  描述            |
| -------------------- | -------- |
| [onLocalStreamAdd](#onlocalstreamadd)     | 本地视频流新增/更新 |
| [onRemoteStreamUpdate](#onremotestreamupdate)     | 远端视频流新增/更新 |
| [onRemoteStreamRemove](#onremotestreamremove)     | 远端视频流断开 |
| [onWebSocketClose](#onwebsocketclose)     |  websocket 断开 |
| [onRelayTimeout](#onrelaytimeout)     | 视频流 server 超时断开 |
| [onKickout](#onkickout)     | 被踢下线（同一个用户重复登录） |



### 高级功能接口

| API                   |  描述            |
| -------------------- | -------- |
| [WebRTCAPI.startRTC](#webRTCAPI.startRTC)   | 主动推流才需要用到 |
| [WebRTCAPI.getLocalStream](#webrtcapi.getlocalstream)     | 获取本地音频/音频流 |
| [WebRTCAPI.openVideo](#webrtcapi.openVideo)     | 推流期间重新打开视频采集 |
| [WebRTCAPI.closeVideo](#webrtcapi.closeVideo)     | 推流期间暂时关闭视频采集 |
| [WebRTCAPI.openAudio](#webrtcapi.openAudio)     | 推流期间重新打开音频采集 |
| [WebRTCAPI.closeAudio](#webrtcapi.closeAudio)     | 推流期间暂时关闭音频采集 |
| [WebRTCAPI.changeSpearRole](#webrtcapi.changeSpearRole)     | 切换音视频参数设定 |
| [WebRTCAPI.getVideoDevices](#webrtcapi.getVideoDevices)     | 枚举视频采集设备 |
| [WebRTCAPI.getAudioDevices](#webrtcapi.getAudioDevices)     | 枚举音频采集设备 |
| [WebRTCAPI.chooseVideoDevice](#webrtcapi.chooseVideoDevice)     | 选择视频采集设备 |
| [WebRTCAPI.chooseAudioDevice](#webrtcapi.chooseAudioDevice)     | 选择音频采集设备 |


### 高级事件通知

| 事件                   |  描述            |
| -------------------- | -------- |
| [onPeerConnectionAdd](#onpeerconnectionadd)     | PeerConnection 新增通知 ，请确保您已经了解了 peer connection 通知的作用和意义 |
