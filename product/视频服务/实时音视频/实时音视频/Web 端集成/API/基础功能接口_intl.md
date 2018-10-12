
## WebRTCAPI.fn.detectRTC
This API is used to detect whether WebRTC is supported.
Syntax example:
`WebRTCAPI.fn.detectRTC(options, callback);`

Parameter description:

| Parameter	|Type	|Description |
|---|---|---|
|options	|object | Parameter |

options:

| Parameter | Type | Description |
|---|---|---|
|screenshare	| boolean | Whether to perform screen sharing detection. Defaults to true. |

Callback's info field:

| Field | Description | Note |
|---|---|---|
|support	|Whether WebRTC is supported | |
|h264Support	|Whether H.264 is supported | H.264 must be supported |
|screenshare	|Whether screen sharing is supported | Plug-ins must be installed |

Actual example:
```
WebRTCAPI.fn.detectRTC({
        screenshare : false
    }, function(info){
    if( !info.support ) {
        alert('WebRTC is not supported')
    }
});
```

## WebRTCAPI
This API is used to initialize WebRTC.
Syntax example:

`var RTC = new WebRTCAPI( options , succ , error)`

Parameter description:

| Parameter | Type | Description |
|---|---|---|
|options	|object | Parameter |
|succ	|function | Callback successful |
|error|function | Callback failed |

Options description:

| Parameter | Type | Description | Note |
|---|---|---|---|
|sdkAppId	|integer | sdkappid of application (if there is any doubt, see [Integrating the SDK](https://cloud.tencent.com/document/product/647/16863) ) | Required |
|accountType	|integer | Account type (if there is any doubt, see [Integrating the SDK](https://cloud.tencent.com/document/product/647/16863) ) | Required |
|userId	|string | The unique ID of the user, which is the user name we often say (if there is any doubt, see [Integrating the SDK](https://cloud.tencent.com/document/product/647/16863)) | Required |
|userSig| string | Required. Identity signature, equivalent to the role of login password (if there is any doubt, see [Integrating the SDK](https://cloud.tencent.com/document/product/647/16863) ) | Required |
|closeLocalMedia	|boolean | Whether to disable the automatic push (if set to true, the push at the local end will not be initiated after the entering/creating operation is completed; if the push is required, the push API needs to be actively called by the business) | Optional. Defaults to false. |
|audio| boolean | Whether to enable audio collection | Optional. Defaults to true. |
|video	| boolean | Whether to enable video collection | Optional. Defaults to true. |
|debug	| object | Debug mode (Prints the log on the console) {log:true, uploadLog:true, vconsole:true} | Optional |
|peerAddNotify	|boolean | p2p connection notification. The business side determines whether a connection is required before establishing a p2p connection. Need to be used with [onPeerConnectionAdd] of [Advanced Event Notifications] | Optional. Defaults to false. |

Actual example:

    var RTC = new WebRTCAPI( {
        "userId": userId,
        "sdkAppId":  sdkappid,
        "accountType":  accountType,
        "userSig": userSig
    } );

    // Debug mode
    var RTC = new WebRTCAPI( {
        "userId": userId,
        "sdkAppId":  sdkappid,
        "accountType":  accountType,
        "userSig": userSig,
        "debug":{
            "log": true, //Whether to print the debug log on the console. It is false by default
            "vconsole": true //Whether the vconsole is shown (to facilitate viewing logs on the mobile end)
            "uploadLog": true //Whether to report the log
        }
    } );
		
## WebRTCAPI.enterRoom ( WebRTCAPI.createRoom )
This API is used to create or enter an audio/video room.
Syntax example

    var RTC = new WebRTCAPI( ... )
    ...
    //Note: This must be called in the successful initialized callback of WebRTCAPI
    RTC.enterRoom( options, succ , error );
Parameter description:

| Parameter | Type | Required | Description |
|--|--|--|--|
|options|object | Yes | Parameter |
|succ	|function | No | Callback successful |
|error|function | No | Callback failed |

Options description:

| Parameter | Type | Required | Description |
|--|--|--|--|
|roomid|integer | Yes | Room ID |
|privateMapKey	|string | No | It refers to the key to enter the room with the specified roomID. If the business believes that there is no need to restrict the permission of users, you can leave it unset (if there is any doubt, see [Integrating the SDK](https://cloud.tencent.com/document/product/647/16863)) |
|role	|string | Yes | Switches the user role in the Screen Setting [Console - SPEAR engine configuration](https://cloud.tencent.com/document/product/647/16792) |
| pureAudioPushMod | integer | No | Audio-only push mode. You need to use this parameter when you need to perform non-interactive broadcasting and recording<br>1 => This is an audio-only push, so there is no need to record mp3 files<br>2 => This is an audio-only push, and the recording file is mp3 |
|recordId	| integer | No | Custom business ID at automatic recording, int32, which is assigned to users at recording callback |

Actual example:
```
var RTC = new WebRTCAPI({
    "userId": "username",
    "sdkAppId":  1400012345,
    "accountType":  12345,
    "userSig": "xxxxxxxxxxxxxxxxxxxxxxxxx",
}, function(data){
    //Initialized successfully
    RTC.createRoom( {
        roomid : 123456,
        role : "user",
    }, function(){
        //Entered the room successfully
    } ,  function(data){
        //Failed to enter the room
    } );
}, function(data){
    //Initialization failed
});
```

## WebRTCAPI.quit
This API is used to exit the audio/video room.
Syntax example
```
 var RTC = new WebRTCAPI( ... )
 ...
 //Note: This must be called in the successful initialized callback of WebRTCAPI
 RTC.quit(  succ , error );
```
		
Parameter description:

| Parameter | Type | Description | Note |
|--|--|--|--|
|succ	|function | Callback successful | Optional |
|error	|function | Callback failed | Optional |

Actual example:

    var RTC = new WebRTCAPI( ... )
    ...
    //Note: This must be called in the successful initialized callback of WebRTCAPI
    RTC.quit(  function(){
        //Exited successfully
    } , function(){
        //Failed to exit
    } );

