
## Prerequisites
Please make sure that you have activated the service and created an application first.
## Procedure
### Prepare pages
The media for video playback are video (audio and video) and audio (audio only) provided by H5.
```
<body >
    <!-- Video-->
    <!--
        Local video stream
        muted:
            The video of the local video stream must be muted, or issues such as howling and echo may occur
            On Mac/iPhone/iPad, you need to set the muted attribute with js
        Autoplay: must be enabled
        playsinline: guarantees that videos are not played in full screen in iOS Safari
     -->
    <video id="localVideo" muted autoplay playsinline></video>
    <!-- Remote video stream -->
    <video id="remoteVideo" autoplay playsinline></video>

    <!--Audio -->
    <!-- Local audio stream/In this scenario, localaudio is not necessary for playback and can be used for debugging -->
    <!-- <audio id="localAudioMedia"  muted autoplay></audio> -->
    <!-- Remote audio stream -->
    <!-- <audio id="remoteAudioMedia" autoplay ></audio> -->
    <script src="https://sqimg.qq.com/expert_qq/webrtc/2.5/WebRTCAPI.min.js"></script>
</body>
```
### Initialization
```
var RTC = new WebRTCAPI({
    "userId": userId,
    "userSig": userSig,
    "sdkAppId":  sdkappid,
    "accountType":  accountType,
},function(){
    //Call the API for joining a room after the initialization is completed
    RTC.createRoom({
        roomid : $("#roomid").val(),
        privateMapKey: privateMapKey,
        role : "user",   //The name of the configuration set in the **console** -> **Screen Setting**
    });
},function(error){
    console.error(error)
});
```

### Event listening


```
//Local stream adding
RTC.on("onLocalStreamAdd", function(data){
    if( data && data.stream){
        document.querySelector("#localVideo").srcObject = data.stream;
    }
});
//Remote stream adding/update
RTC.on("onRemoteStreamUpdate", function(data){
    if( data && data.stream){
        document.querySelector("#remoteVideo").srcObject = data.stream;
    }
});
```
