
The basic event notifications include the addition/update of the local video stream, the addition/update of the remote video stream, the disconnection of the remote video stream, the disconnection of websocket, the disconnection of video stream server after timeout and the forced logout (the same user logged in repeatedly). The details are described as follows:

The basic syntax for event notification is as follows:
```javascript
    var RTC = new WebRTCAPI( { ... } );

    ......

    RTC.on( 'EVENT_NAME' , function(data){

    })
  ```


## onLocalStreamAdd
Notification of the addition and update of the local video stream.
#### Sample codes
```javascript
    var RTC = new WebRTCAPI( { ... } );

    RTC.on( 'onLocalStreamAdd' , function( data ){
        if( data && data.stream){
            var stream = data.stream
            document.querySelector("#localVideo").srcObject = stream
        }
    })
```
#### data
| Parameter                   | Type       | Description            |
| -------------------- | -------- | ------------- | ---- |
| stream         | Stream | Local video streamStream      |


## onRemoteStreamUpdate
Notification of the addition and update of the remote video stream.
#### Sample codes
```javascript
    var RTC = new WebRTCAPI( { ... } );

    RTC.on( 'onRemoteStreamUpdate' , function( data ){
        if( data && data.stream){
            var stream = data.stream
            console.debug( data.userId + 'enter this room with unique videoId '+ data.videoId  )
            document.querySelector("#remoteVideo").srcObject = stream
        }else{
            console.debug( 'somebody enter this room without stream' )
        }
    })
```
#### data
| Parameter                   | Type       | Description            |
| -------------------- | -------- | ------------- | ---- |
| userId     | String  | The userId of the user to which the video stream belongs |
| stream     | Stream  | The video stream, which may be null (this callback will be triggered every time a user enters the room whether or not he/she pushes)  |
| videoId    | String  | The unique ID of the video stream, consisting of tinyid + "_" + random strings       |
| videoType: | Integer | 0: NONE, 1: AUDIO, 2: MAIN 7: AUXILIARY AID |


## onRemoteStreamRemove
Notification of the disconnection of the remote video stream.
#### Sample codes
```javascript
    var RTC = new WebRTCAPI( { ... } );

    RTC.on( 'onRemoteStreamRemove' , function( data ){
        console.debug( data.userId + ' leave this room with unique videoId '+ data.videoId  )
    })
```

#### data
| Parameter                   | Type       | Description            |
| -------------------- | -------- | ------------- | ---- |
| userId         | String | The userId of the user to which the remote video stream belongs |
| videoId         | String | The unique ID of the remote video stream |


## onWebSocketClose
Notification of the disconnection of websocket.
#### Sample codes
```javascript
    var RTC = new WebRTCAPI( { ... } );

    RTC.on( 'onWebSocketClose' , function( data ){

    })
```

## onRelayTimeout
Notification of the disconnection of video stream server after timeout.
#### Sample codes
```javascript
    var RTC = new WebRTCAPI( { ... } );

    RTC.on( 'onRelayTimeout' , function( data ){
        // Video server timeout
    })
```


## onKickout
Notification of forced logout (the same user logged in repeatedly).
#### Sample codes
```javascript
    var RTC = new WebRTCAPI( { ... } );

    RTC.on( 'onKickout' , function( data ){
        //Exit the room
    })
```

