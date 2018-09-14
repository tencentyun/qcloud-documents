WebRTC 不仅可提供以摄像头为源的视频通讯功能，也能将由canvas元素捕获的流进行推流。

### demo演示
https://www.qcloudtrtc.com/webrtc-samples/canvascapture/demo.html

### 示例代码
https://gitee.com/vqcloud/webrtc-samples



### step 1.先以观众角色进入房间

> closeLocalMedia => true
```javascript
    var RTC = new WebRTCAPI( {
        userId: userId,
        sdkAppId:  sdkappid,
        accountType:  accountType,
        userSig: userSig
    },function(){
        ...
    } ,function(error){
        console.error( error )
    } );
```

### step 2.获取canvas视频流
参考demo，通过 canvas.captureStream 获取到MediaStream


### step 3.进房并推流
> role 必须带上，这将决定了canvas流的码率，请到控制台配置一个合适的码率。
> role 可以在进房的时候带，也可以在推流的时候带，建议在进房的时候带，会更快哦

```javascript
    RTC.enterRoom({
        role: 'canvas_stream_role_name',
        roomid : $("#roomid").val()
    },function(){
        //进房成功，音视频推流
        RTC.startRTC({
        role: 'canvas_stream_role_name',
        stream: canvasStream
        });
    },function(){

    });

```


### FAQ

- 为什么我在无法进行canvas推流？
  - 受限于浏览器支持情况，需要在Chrome浏览器52+版本下运行。
  - 受限于浏览器权限，需要在localhost，或者通过服务器访问，不能直接访问本地html文件进行canvas推流。
- 有没有实例代码？怎么获得canvas的流?怎么在canvas推流时加入声音？
  - 请参考 https://gitee.com/vqcloud/webrtc-samples