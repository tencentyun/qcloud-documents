WebRTC 不仅可提供以摄像头为源的视频通讯功能，也能将由canvas元素捕获的流进行推流。

### demo演示
https://sxb.qcloud.com/webrtc-samples/canvascapture/demo.html

### 示例代码
https://github.com/TencentVideoCloudMLVBDev/webrtc_web_samples

### 屏幕分享参数

> 这里隆重引入1个参数  canvas

| Key                     | 字段取值  | 含义              |
| ------------------------- | -------- | ---------------------- |
| canvas | MediaStream     | 需要推的canvas元素捕获流 |  
|  | false     | 不推canvas元素捕获流 | 


canvas参数在 **初始化** 和 **开始推流** 2个接口都可以设置

### 自动推流

> 适用于直接使用屏幕分享的场景

```javascript
    var RTC = new WebRTCAPI( {
        userId: userId,
        sdkAppId:  sdkappid,
        accountType:  accountType,
        userSig: userSig,
        canvas: canvasStream //使用该参数表示推canvas流：canvasStream
    },function(){
        ...
    },function(error){
        console.error( error )
    } );
```

### 手动推流
> 适用于手动推流的场景

```javascript
    var RTC = new WebRTCAPI( {
        userId: userId,
        sdkAppId:  sdkappid,
        accountType:  accountType,
        userSig: userSig,
        closeLocalMedia: true
    },function(){
        ...
    } ,function(error){
        console.error( error )
    } );
```

### canvas推流与摄像头切换的代码示例
```javascript
// canvas推流
function canvas(){
    RTC.stopRTC({
    },function(info){
        console.debug('摄像头断流成功');
        RTC.startRTC({
            stream: canvasStream
        },function(info){
            console.debug('画布推流成功');
        },function(error){
            console.error('画布推流失败',error)
        });
    },function(error){
        console.error('摄像头断流失败',error)
    });
}

// 摄像头推流
function video(){
    RTC.stopRTC({
        canvas: canvasStream
    },function(info){
        console.debug('画布断流成功');
        RTC.startRTC({
        },function(info){
            console.debug('摄像头推流成功');
        },function(error){
            console.error('摄像头推流失败',error)
        });
    },function(error){
        console.error('画布断流失败',error)
    });
}
```

### FAQ

- 为什么我在无法进行canvas推流？
  - 受限于浏览器支持情况，需要在Chrome浏览器52+版本下运行。 
  - 受限于浏览器权限，需要在localhost，或者通过服务器访问，不能直接访问本地html文件进行canvas推流。
- 有没有实例代码？怎么获得canvas的流?怎么在canvas推流时加入声音？
  - 请参考 https://github.com/TencentVideoCloudMLVBDev/webrtc_web_samples