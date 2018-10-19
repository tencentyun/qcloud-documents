
## Sample Codes
We provide some sample codes for different features to help you understand WebRTC.
For more information on APIs, see [API Documentation](https://cloud.tencent.com/document/product/647/16865).
### Sample codes
- [Detect whether WebRTC is supported](https://cloud.tencent.com/document/product/647/16924)
- [LVB and Joint Broadcasting](https://cloud.tencent.com/document/product/647/16924)
- [Viewer mode (non-push)](https://cloud.tencent.com/document/product/647/16924)

### Detect whether WebRTC is supported
[Whether WebRTC is supported]()
```
 WebRTCAPI.fn.detectRTC( function(info ){
       if( !info.support){
           alert('Not SupportedWebRTC')
       }
});
```	
## LVB and Joint Broadcasting
There are two ways of "LVB + Joint Broadcasting"
1. After a user joins a room, the camera and microphone data is collected automatically for joint broadcasting.
2. After a user joins a room, LVB video is played without push, and the push API is called at the right time for push.
Choose either way based on your business needs, and two APIs are needed.
The main difference is the default setting of closeLocalMedia in the initialization parameters.
### Automatic push

    var RTC = new WebRTCAPI( {
        userId: userId,
        sdkAppId:  sdkappid,
        accountType:  accountType,
        userSig: userSig
    },function(){
        //Callback of successful initialization

        //Join a room
        RTC.createRoom({
            roomid : 12345,
            role : "user",
            privateMapKey:  privateMapKey,
        },function(error){
            console.error( error )
        } );
    },function(error){
        console.error( error )
    } );
Manual push

    var RTC = new WebRTCAPI( {
        userId: userId,
        sdkAppId:  sdkappid,
        accountType:  accountType,
        userSig: userSig,
        closeLocalMedia: true
    },function(){
        //Callback of successful initialization

        //Join a room
        RTC.createRoom({
            roomid : 12345,
            role : "user",
            privateMapKey:  privateMapKey,
        }, function(){
            //Room created successfully

            //Manual push
            RTC.startRTC();
        },function(error){
            console.error( error )
        } );
    } ,function(error){
        console.error( error )
    } );
Viewer mode (non-push)

    var RTC = new WebRTCAPI( {
        "userId": userId,
        "sdkAppId":  sdkappid,
        "accountType":  accountType,
        "userSig": userSig,
        "privateMapKey":  privateMapKey,
        "closeLocalMedia": true
    },function(){
        //Join a room
        RTC.createRoom({
            roomid : 12345,
            role : "user"
        });
    },function(error){
        console.error( error )
    } );

