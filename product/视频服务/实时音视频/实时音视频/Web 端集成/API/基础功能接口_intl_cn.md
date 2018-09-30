
## WebRTCAPI.fn.detectRTC
检测是否支持 WebRTC。
语法示例：
`WebRTCAPI.fn.detectRTC(options, callback);`

参数描述：

|参数	|类型	|描述|
|---|---|---|
|options	|object	|参数|

options：

|参数	|类型|	描述|
|---|---|---|
|screenshare	|boolean	|是否进行屏幕分享检测，默认true|

回调callback的 info 字段：

|字段	|含义	|备注|
|---|---|---|
|support	|是否支持WebRTC	| |
|h264Support	|是否支持H.264	|必须支持 H.264|
|screenshare	|是否支持屏幕分享	|必须安装插件|

实际示例：
```
WebRTCAPI.fn.detectRTC({
        screenshare : false
    }, function(info){
    if( !info.support ) {
        alert('不支持WebRTC')
    }
});
```

## WebRTCAPI
初始化 WebRTC。
语法示例:

`var RTC = new WebRTCAPI( options , succ , error)`

参数描述:

|参数	|类型	|描述|
|---|---|---|
|options	|object	|参数|
|succ	|function	|成功回调|
|error|	function	|失败回调|

Options 描述：

|参数	|类型	|描述	|备注|
|---|---|---|---|
|sdkAppId	|integer|	应用的 sdkappid（如有疑义请看  [集成SDK](https://cloud.tencent.com/document/product/647/16863) ）	|必填|
|accountType	|integer|	账户类型（ 如有疑义请看 [集成SDK](https://cloud.tencent.com/document/product/647/16863) )	|必填|
|userId	|string	|用户的唯一标识，也就是我们常说的用户名（如有疑义请看  [集成SDK](https://cloud.tencent.com/document/product/647/16863)）|	必填|
|userSig|	string	|必要，身份签名，相当于登录密码的作用 （如有疑义请看  [集成SDK](https://cloud.tencent.com/document/product/647/16863) ）	|必填|
|closeLocalMedia	|boolean	|是否关闭自动推流（如果置为 true，则在完成加入/建房操作后，不会发起本端的推流，如需推流，需要由业务主动调推流接口 ）	|非必填，默认 false|
|audio|	boolean	|是否启用音频采集|	非必填，默认 true|
|video	|boolean|	是否启用视频采集	|非必填，默认 true|
|debug	|object	|调试模式（控制台打印日志）{ log:true, uploadLog:true, vconsole:true}	|非必填|
|peerAddNotify	|boolean	|p2p的建连通知，在建立p2p连接前由业务侧决定是否需要连接。需要结合[高级事件通知]的[onPeerConnectionAdd]使用	|非必填，默认false|

实际示例：

    var RTC = new WebRTCAPI( {
        "userId": userId,
        "sdkAppId":  sdkappid,
        "accountType":  accountType,
        "userSig": userSig
    } );

    //调试模式
    var RTC = new WebRTCAPI( {
        "userId": userId,
        "sdkAppId":  sdkappid,
        "accountType":  accountType,
        "userSig": userSig,
        "debug":{
            "log": true, //是否在控制台打印调试日志 ,默认为false
            "vconsole": true //是否展示 vconsole （方便在移动端查看日志）
            "uploadLog": true //是否上报日志
        }
    } );
		
## WebRTCAPI.enterRoom ( WebRTCAPI.createRoom )
创建或进入音视频房间。
语法示例

    var RTC = new WebRTCAPI( ... )
    ...
    //注意：这里必须在 WebRTCAPI 的初始化成功的回调中调用
    RTC.enterRoom( options, succ , error );
参数描述：

|参数	|类型	|是否必须	|描述|
|--|--|--|--|
|options|	object	|是	|参数|
|succ	|function|	否	|成功回调|
|error|	function	|否	|失败回调|

Options 描述：

|参数	|类型	|是否必须|	描述|
|--|--|--|--|
|roomid|	integer	|是	|房间 id|
|privateMapKey	|string	|否	|如果业务认为无需限制用户的权限，可以不带，相当于进入指定房间roomID的钥匙 （如有疑义请看 [集成SDK ](https://cloud.tencent.com/document/product/647/16863)）|
|role	|string	|是	|切换画面设定的用户角色 [控制台 - SPEAR引擎配置](https://cloud.tencent.com/document/product/647/16792)|
pureAudioPushMod	integer	否	纯音频推流模式，需要旁路直播和录制时需要带上此参数<br>1 => 本次是纯音频推流,不需要录制mp3文件 <br>2 => 本次是纯音频推流,录制文件为mp3|
|recordId	|integer|	否|	自动录制时业务自定义id，int32，录制回调时给到用户|

实际示例:
```
var RTC = new WebRTCAPI({
    "userId": "username",
    "sdkAppId":  1400012345,
    "accountType":  12345,
    "userSig": "xxxxxxxxxxxxxxxxxxxxxxxxx",
}, function(data){
    //初始化成功
    RTC.createRoom( {
        roomid : 123456,
        role : "user",
    }, function(){
        //进房房间成功
    } ,  function(data){
        //进入房间失败
    } );
}, function(data){
    //初始化失败
});
```

## WebRTCAPI.quit
退出音视频房间。
语法示例
```
 var RTC = new WebRTCAPI( ... )
 ...
 //注意：这里必须在 WebRTCAPI 的初始化成功的回调中调用
 RTC.quit(  succ , error );
```
		
参数描述：

|参数|	类型|	描述	|备注|
|--|--|--|--|
|succ	|function	|成功回调	|非必填|
|error	|function	|失败回调	|非必填|

实际示例

    var RTC = new WebRTCAPI( ... )
    ...
    //注意：这里必须在 WebRTCAPI 的初始化成功的回调中调用
    RTC.quit(  function(){
        //退出成功
    } , function(){
        //退出失败
    } );
