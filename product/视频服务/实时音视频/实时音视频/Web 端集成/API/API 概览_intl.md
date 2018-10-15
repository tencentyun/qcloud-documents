TRTC Web APIs include the feature APIs for active calling and the event notification APIs with trigger setting, wherein the feature APIs include basic feature APIs and advanced feature APIs, and the event notifications include basic event notifications and advanced event notifications. Junior developers can complete basic development access through basic feature APIs and basic event notifications, and can experience the main features of TRTC. Senior developers can complete the development through advanced feature APIs and advanced event notifications, and can experience the advanced features of TRTC.

### Basic feature APIs

| API                   | Description            |
| -------------------- | -------- |
| [WebRTCAPI.fn.detectRTC](https://cloud.tencent.com/document/product/647/17251#webrtcapi.fn.detectrtc)     | Detects whether it supports WebRTC |
| [WebRTCAPI](https://cloud.tencent.com/document/product/647/17251#webrtcapi)     | Initialization |
| [WebRTCAPI.enterRoom( WebRTCAPI.createRoom )](https://cloud.tencent.com/document/product/647/17251#webrtcapi.createroom)     | Creates or enters an audio/video room |
| [WebRTCAPI.quit](https://cloud.tencent.com/document/product/647/17251#webrtcapi.quit)     | Exits an audio/video room |

### Basic event notifications
| Event                   |  Description            |
| -------------------- | -------- |
| [onLocalStreamAdd](https://cloud.tencent.com/document/product/647/17248#onlocalstreamadd)     | Addition/update of local video stream |
| [onRemoteStreamUpdate](https://cloud.tencent.com/document/product/647/17248#onremotestreamupdate)     | Addition/update of remote video stream |
| [onRemoteStreamRemove](https://cloud.tencent.com/document/product/647/17248#onremotestreamremove)     | Disconnection of remote video stream |
| [onWebSocketClose](https://cloud.tencent.com/document/product/647/17248#onwebsocketclose)     | Disconnection of websocket |
| [onRelayTimeout](https://cloud.tencent.com/document/product/647/17248#onrelaytimeout)     | Disconnection of video stream server after timeout |
| [onKickout](https://cloud.tencent.com/document/product/647/17248#onkickout)  | Forced logout (The same user logged in repeatedly)  |



### Advanced feature APIs

| API                   | Description            |
| -------------------- | -------- |
| [WebRTCAPI.startRTC](https://cloud.tencent.com/document/product/647/17250#webrtcapi.startrtc)  | Only used for active push  |
| [WebRTCAPI.stopRtc](https://cloud.tencent.com/document/product/647/17250#webrtcapi.startrtc)  | Stops the push  |
| [WebRTCAPI.getLocalStream](https://cloud.tencent.com/document/product/647/17250#webrtcapi.getlocalstream)     | Gets local audio/video stream |
| [WebRTCAPI.updateStream](https://cloud.tencent.com/document/product/647/17250#webrtcapi.updatestream)     | Updates video stream |
| [WebRTCAPI.openVideo](https://cloud.tencent.com/document/product/647/17250#webrtcapi.openvideo)     | Turns on video collection again during the push process |
| [WebRTCAPI.closeVideo](https://cloud.tencent.com/document/product/647/17250#webrtcapi.closevideo)     | Temporarily turns off video collection during the push process |
| [WebRTCAPI.openAudio](https://cloud.tencent.com/document/product/647/17250#webrtcapi.openaudio)     | Turns on audio collection again during the push process |
| [WebRTCAPI.closeAudio](https://cloud.tencent.com/document/product/647/17250#webrtcapi.closeaudio)     | Temporarily turns off audio collection during the push process |
| [WebRTCAPI.changeSpearRole](https://cloud.tencent.com/document/product/647/17250#webrtcapi.changeSpearRole)     | Switches audio and video parameter settings |
| [WebRTCAPI.getVideoDevices](https://cloud.tencent.com/document/product/647/17250#webrtcapi.getVideoDevices)     | Enumerates video collection devices |
| [WebRTCAPI.getAudioDevices](https://cloud.tencent.com/document/product/647/17250#webrtcapi.getAudioDevices)     | Enumerates audio collection devices |
| [WebRTCAPI.chooseVideoDevice](https://cloud.tencent.com/document/product/647/17250#webrtcapi.chooseVideoDevice)     | Chooses the video collection device |
| [WebRTCAPI.chooseAudioDevice](https://cloud.tencent.com/document/product/647/17250#webrtcapi.chooseaudiodevice)     | Chooses the audio collection device |
| [WebRTCAPI.SoundMeter](https://cloud.tencent.com/document/product/647/17250#webrtcapi.SoundMeter)     | Sound input detection |


### Advanced event notifications

| Event                   |  Description            |
| -------------------- | -------- |
| [onPeerConnectionAdd](https://cloud.tencent.com/document/product/647/17252#onpeerconnectionadd)  | Notification of PeerConnection addition. Please make sure you understand the role and significance of peer connection notification |





### Update log
> 2.6.1
    ## WebRTCAPI.getSpeakerDevices
        This API is used to enumerate audio output devices
    ## WebRTCAPI.chooseSpeakerDevice
        This API is used to enumerate audio output devices
