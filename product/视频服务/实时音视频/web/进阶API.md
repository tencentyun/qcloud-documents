## 第二课 进阶API

### 导语
欢迎来到第二课!

在本节课程中，是进阶API的说明和使用API。

### 预备知识
本课程要求用户已完成完成前面课程的学习。

### API

## [基础] 接口 & 事件通知
> 了解一下接口的使用，就已经可以实现主要功能

### 接口
| API                   |  描述            |
| -------------------- | -------- |
| [WebRTCAPI.fn.detectRTC](#WebRTCAPI.fn.detectRTC)     | 检测是否支持WebRTC |
| [WebRTCAPI](#WebRTCAPI)     | 初始化 |
| [WebRTCAPI.createRoom](#WebRTCAPI.createRoom)     | 创建或进入音视频房间 |
| [WebRTCAPI.quit](#WebRTCAPI.quit)     | 退出音视频房间 |


### 事件通知
| 事件                   |  描述            |
| -------------------- | -------- |
| [onLocalStreamAdd](#onLocalStreamAdd)     | 本地视频流新增/更新 |
| [onRemoteStreamUpdate](#onRemoteStreamUpdate)     | 远端视频流新增/更新 |
| [onRemoteStreamRemove](#onRemoteStreamRemove)     | 远端视频流断开 |
| [onWebSocketClose](#onWebSocketClose)     |  websocket断开 |
| [onRelayTimeout](#onRelayTimeout)     | 视频流server超时断开 |
| [onKickout](#onKickout)     | 被踢下线(同一个用户重复登录) |

> 如需一些满足一些特定场景的需求，可以了解以下接口

<br>
## [进阶]接口 & 事件监听

### 接口

| API                   |  描述            |
| -------------------- | -------- |
| [WebRTCAPI.startRTC](#WebRTCAPI.startRTC)     | 主动推流才需要用到 |
| [WebRTCAPI.getLocalStream](#WebRTCAPI.getLocalStream)     | 获取本地音频/音频流 |


### 事件通知
> 以下事件通知

| 事件                   |  描述            |
| -------------------- | -------- |
| [onPeerConnectionAdd](#onPeerConnectionAdd)     | PeerConnection 新增通知 ，请确保您已经了解了peer connection通知的作用和意义 |



#### WebRTCAPI.fn.detectRTC

> 检测是否支持 WebRTC

```javascript
var info = WebRTCAPI.fn.detectRTC();
```

> info 字段

| 字段  | 含义    |  备注|
| ------------------------- | -------- | ---------------------- |
| isTBS      | 是否是TBS |                 |
| TBSversion      | TBS版本号 |                 |
| isTBSValid      | TBS版本号是否支持WebRTC |                 |
| support      | 是否支持WebRTC |                 |


<br >


#### WebRTCAPI
> 初始化 WebRTC


```javascript
var RTC = new WebRTCAPI( options , succ , error)
```
> 参数

| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- | ---- |
| options         | object | 参数      |
| succ         | function | 成功回调      |
| error         | function | 失败回调      |

> options

| 参数               | 类型      | 描述                                       | 备注           |
| ---------------- | ------- | ---------------------------------------- | ------------ |
| **sdkAppId**         | integer | 应用的sdkappid( 如有疑义请看[集成SDK](集成SDK.md)              | 必填           |
| **accountType**      | integer | 账户类型( 如有疑义请看[集成SDK](集成SDK.md) )                     | 必填           |
| **openid**           | string  | 用户的唯一标识，也就是我们常说的用户名( 如有疑义请看[集成SDK](集成SDK.md) ) | 必填           |
| **userSig**          | string  | 鉴权签名( 如有疑义请看[集成SDK](集成SDK.md) )                     | 必填           |
| closeLocalMedia | boolean | 是否关闭自动推流(如果置为true，则在完成加入/建房操作后，不会发起本端的推流，如需推流，需要由业务主动调推流接口) | 非必填，默认 false |
| audio            | boolean | 是否启用音频采集                                 | 非必填，默认 true  |
| video            | boolean | 是否启用视频采集                                 | 非必填，默认 true  |

> code

```javascript
    var RTC = new WebRTCAPI( {
        "openid": openid,
        "sdkAppId":  sdkappid,
        "accountType":  accountType,
        "userSig": userSig,
        "closeLocalMedia": false //默认是false
    } );
```

#### WebRTCAPI.createRoom
> 创建或进入音视频房间
```javascript
    var RTC = new WebRTCAPI( ... )
    ...
    //注意：这里必须在 WebRTCAPI 的初始化成功的回调中调用
    RTC.createRoom( options, succ , error );
```

> 参数

| 参数                   | 类型       | 描述            | 备注           |
| -------------------- | -------- | ------------- | ---- |
| options         | object | 参数      |         |
| succ         | function | 成功回调      |      |
| error         | function | 失败回调      |      |

> options

| 参数               | 类型      | 描述                                       | 备注           |
| ---------------- | ------- | ---------------------------------------- | ------------ |
| **roomid**         | integer | 房间id          | 必填           |
| **role**      | string | 切换画面设定的用户角色[ 控制台 - 画面设定([spear](https://cloud.tencent.com/document/product/268/10620)配置)]                    | 必填           |


> code
```javascript
var RTC = new WebRTCAPI({
    "openid": "username",
    "sdkAppId":  1400012345,
    "accountType":  12345,
    "userSig": "xxxxxxxxxxxxxxxxxxxxxxxxx",
}, function(data){
    console.debug( ' 初始化成功 ')
}, function(data){
    console.debug( ' 初始化失败 ' , data)
});
```

#### WebRTCAPI.quit
> 退出音视频房间
```javascript
    var RTC = new WebRTCAPI( ... )
    ...
    //注意：这里必须在 WebRTCAPI 的初始化成功的回调中调用
    RTC.quit(  succ , error );
```

> 参数

| 参数               | 类型      | 描述                                       | 备注           |
| -------------------- | -------- | ------------- | ---- |
| succ         | function | 成功回调      |    非必填 |
| error         | function | 失败回调      |非必填 |

> code 
```javascript
    var RTC = new WebRTCAPI( ... )
    ...
    //注意：这里必须在 WebRTCAPI 的初始化成功的回调中调用
    RTC.quit(  function(){
        //退出成功
    } , function(){
        //退出失败
    } );
```
---
### 事件通知的基本写法如下
```javascript
    var RTC = new WebRTCAPI( { ... } );

    ......

    RTC.on( 'EVENT_NAME' , function(data){

    })
```


#### onLocalStreamAdd
> 本地视频流新增/更新

```javascript
    var RTC = new WebRTCAPI( { ... } );
    
    RTC.on( 'onLocalStreamAdd' , function( data ){
        if( data && data.stream){
            var stream = data.stream
            document.querySelector("#localVideo").srcObject = stream
        }
    })
```
> data 

| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- | ---- |
| stream         | Stream | 本地视频流Stream      |





#### onRemoteStreamUpdate
> 远端视频流新增/更新

```javascript
    var RTC = new WebRTCAPI( { ... } );
    
    RTC.on( 'onRemoteStreamUpdate' , function( data ){
        if( data && data.stream){
            var stream = data.stream
            console.debug( data.openId + 'enter this room with unique videoId '+ data.videoId  )
            document.querySelector("#remoteVideo").srcObject = stream
        }else{
            console.debug( 'somebody enter this room without stream' )
        }
    })
```

> data 

| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- | ---- |
| openId     | Stream  | 视频流所属用户的openId（identifier）    |
| stream     | Stream  | 视频流Stream，可能为null( 每一个用户进来 不管是否推流，都会触发这个回调)  |
| videoId    | string  | 视频流Stream的唯一id ,由 tinyid + "_" + 由随机字符串 组成      |
| videoType: | Integer | 0 : NONE , 1:AUDIO 音频,   2：主路 MAIN   7：辅路 AID |



#### onRemoteStreamRemove
> 远端视频流断开

```javascript
    var RTC = new WebRTCAPI( { ... } );
    
    RTC.on( 'onRemoteStreamRemove' , function( data ){
        console.debug( data.openId + ' leave this room with unique videoId '+ data.videoId  )
    })
```

> data 

| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- | ---- |
| openId         | Stream | 远端视频流所属用户的openId（identifier）    |
| videoId         | Stream | 远端视频流Stream 的唯一ID    |


#### onWebSocketClose
> websocket断开

```javascript
    var RTC = new WebRTCAPI( { ... } );
    
    RTC.on( 'onWebSocketClose' , function( data ){
        
    })
```

#### onRelayTimeout
> 视频流server超时断开

```javascript
    var RTC = new WebRTCAPI( { ... } );
    
    RTC.on( 'onRelayTimeout' , function( data ){
        //视频服务器超时
    })
```

#### onKickout
> 被踢下线(同一个用户重复登录)

```javascript
    var RTC = new WebRTCAPI( { ... } );
    
    RTC.on( 'onKickout' , function( data ){
        //退出房间
    })
```

---

### [进阶]接口

### WebRTCAPI.getLocalStream
> 获取本地音频/音频流
> 这里的获取，是指拿到 [Stream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream),而不是调起音视频设备采集，所以需要在成功推流后调用才有意义。
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 

    var stream = RTC.getLocalStream();
    document.getElementById("#localVideo").srcObject = stream
```

### WebRTCAPI.closeAudio
> 不采集音频（静音）
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 

    RTC.closeAudio();
```
### WebRTCAPI.openAudio
> 采集音频标识（取消静音）
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 

    RTC.openAudio();
```

### WebRTCAPI.closeVideo
> 不采集视频
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 

    RTC.closeVideo();
```

### WebRTCAPI.openVideo
> 采集视频
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 

    RTC.openVideo();
```

### WebRTCAPI.getLocalMediaStatus
> 获取当前视频采集配置
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 
    var status = RTC.getLocalMediaStatus();
    //status.video  true | false (表示当前是否采集视频)
    //status.audio true | false (表示当前是否采集音频)
```

### WebRTCAPI.changeSpearRole
> 切换画面设定的用户角色[ 控制台 - 画面设定(spear配置)]
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 
    RTC.changeSpearRole( "role_name" );
    //status.video  true | false (表示当前是否采集视频)
    //status.audio true | false (表示当前是否采集音频)
```



#### WebRTCAPI.getVideoDevices
> 枚举摄像头
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 
    RTC.getVideoDevices( function(devices){
        //devices 是枚举当前设备的视频输入设备的数组(DeviceObject)
        // 例如 ：[device,device,device]
        // 这些device将在选择摄像头的时候使用
    })
```



#### WebRTCAPI.chooseVideoDevice
> 选择摄像头

```javascript
/*
 * params:
 *   DeviceObject device
 * return:
 *   null
 */
    var RTC = new WebRTCAPI({ ... });
    ... 
    RTC.chooseVideoDevice( device );

```


#### WebRTCAPI.getAudioDevices
> 枚举麦克风
```javascript
    var RTC = new WebRTCAPI({ ... });
    ... 
    RTC.getAudioDevices( function(devices){
        //devices 是枚举当前设备的音频输入设备的数组(DeviceObject)
        // 例如 ：[device,device,device]
        // 这些device将在选择麦克风的时候使用
    })
```


### WebRTCAPI.chooseAudioDevice
> 切换画面设定的用户角色[ 控制台 - 画面设定(spear配置)]

```javascript
/*
 * params:
 *   DeviceObject device
 * return:
 *   null
 */
    var RTC = new WebRTCAPI({ ... });
    ... 
    RTC.chooseAudioDevice( device );

```

---
### 事件通知


#### onPeerConnectionAdd

> PeerConnection连接通知

```javascript
    RTC.on( 'onPeerConnectionAdd' , function( info ){ })
```

> info 

| 参数        | 类型     | 描述           |
| --------- | ------ | ------------ |
| srcopenid | String | 连接所属用户openid |
| srctinyid | string | 连接所属用户tinyid |

> code
```javascript
    RTC.on( 'onPeerConnectionAdd' , function( info ){
        //由业务决定，是否要建立peerconnection
        if( info.srcopenid === '指定用户名'){
            WebRTCAPI.startRTC(info.srctinyid);
        }else{
            console.debug('不建立连接')
        }
    })
```


[上一课 三步完成进房连麦](三步完成进房连麦.md)