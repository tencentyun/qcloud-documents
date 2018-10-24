 The details are described as follows:

### onStreamNotify
Video stream event notification.

#### Syntax example
```javascript
    RTC.on( 'onStreamNotify' , function( info ){ })
```

#### info

| Parameter | Type | Description |
| --------- | ------ | ------------ |
| event | String | onadd: addition of an audio/video stream   onactive: disconnection of an audio/video stream |
| isLocal | Bool | Whether it is a local stream |
| stream | Stream | Whether it is a local stream |
| type | Type | stream/audio/video (stream is the carrier of audio and video track. If the type is stream, it indicates that the stream is disconnected) |

#### Sample codes
```javascript
    RTC.on( 'onStreamNotify' , function( info ){
        
    })
```



### onErrorNotify
Error event notification.

#### Syntax example
```javascript
    RTC.on( 'onErrorNotify' , function( info ){ })
```

#### info

| Parameter | Type | Description |
| --------- | ------ | ------------ |
| errorCode | Integer | Error code |
| errorMsg | String | Error message |

#### Sample codes
```javascript
    RTC.on( 'onErrorNotify' , function( info ){
        
    })
```




### onWebSocketNotify
websocket event notification.

#### Syntax example
```javascript
    RTC.on( 'onWebSocketNotify' , function( info ){ })
```

#### info

| Parameter | Type | Description |
| --------- | ------ | ------------ |
| errorCode | Integer | Error code |
| errorMsg | String | Error message |
| extInfo | Object | Specific information of websocket |


#### Sample codes
```javascript
    var error_code_map = WebRTCAPI.fn.getErrorCode();
    
    RTC.on( 'onWebsocketNotify' , function( info ){
        switch( info.errorCode ){
            case 0:
                // conn succ
                break;
            case error_code_map.WS_CLOSE:
                // close
                console.warn( info );
                break;
            case error_code_map.WS_ERROR:
                // error
                console.error( info );
                break;
            default:
                break;
        }
    })
```


### onPeerConnectionAdd
PeerConnection connection notification. With this notification, the business side can determine whether a connection is required before establishing a p2p connection. It needs to be used in conjunction with the instantiated parameter peerAddNotify

There are also examples of peerconnection in our demo code that can be referenced

#### Syntax example
```javascript
    RTC.on( 'onPeerConnectionAdd' , function( info ){ })
```



#### info

| Parameter | Type | Description |
| --------- | ------ | ------------ |
| userId | String | User name of the user to which the connection belongs |
| tinyId | String | The unique 64-bit ID in Tencent Cloud corresponding to the user name of the user to which the connection belongs. You don't need to understand the role of this parameter here, and only need to pass it through when startRTC is used. |

#### Sample codes
```javascript
    RTC.on( 'onPeerConnectionAdd' , function( info ){
        // The business decides whether to establish peerconnection
        if( info.userId === 'Specified user name'){
            WebRTCAPI.startRTC( info );
        }else{
            console.debug('No connection is established')
        }
    })
```
