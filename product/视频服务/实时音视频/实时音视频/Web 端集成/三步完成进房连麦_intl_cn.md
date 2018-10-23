
## 前提条件
请您务必先完成服务开通及应用创建。
## 操作步骤
### 页面准备
视频播放的媒介是 H5 提供的 Video（音视频）和 Audio（纯音频）。
```
<body >
    <!-- 音视频 -->
    <!--
        本地视频流
        muted:
            本地视频流的video必须置为静音（muted)，否则会出现啸叫/回声等问题
            Mac / iPhone / iPad 需要用js设置muted属性
        autoplay：必须为激活状态
        playsinline：保证在ios safari中不全屏播放
     -->
    <video id="localVideo" muted autoplay playsinline></video>
    <!-- 远端视频流 -->
    <video id="remoteVideo" autoplay playsinline></video>

    <!-- 纯音频 -->
    <!-- 本地音频流 / 这种场景下，localaudio 其实没有播放的必要了，可以用来调试 -->
    <!-- <audio id="localAudioMedia"  muted autoplay></audio> -->
    <!-- 远端音频流 -->
    <!-- <audio id="remoteAudioMedia" autoplay ></audio> -->
    <script src="https://sqimg.qq.com/expert_qq/webrtc/2.5/WebRTCAPI.min.js"></script>
</body>
```
### 初始化
```
var RTC = new WebRTCAPI({
    "userId": userId,
    "userSig": userSig,
    "sdkAppId":  sdkappid,
    "accountType":  accountType,
},function(){
    //初始化完成后调用进房接口
    RTC.createRoom({
        roomid : $("#roomid").val(),
        privateMapKey: privateMapKey,
        role : "user",   //画面设定的配置集名 （见控制台 - 画面设定 )
    });
},function(error){
    console.error(error)
});
```

### 事件监听


```
//本地流 新增
RTC.on("onLocalStreamAdd", function(data){
    if( data && data.stream){
        document.querySelector("#localVideo").srcObject = data.stream;
    }
});
//远端流 新增/更新
RTC.on("onRemoteStreamUpdate", function(data){
    if( data && data.stream){
        document.querySelector("#remoteVideo").srcObject = data.stream;
    }
});
```