
## 代码示例
WebRTC 不容易被理解，为此我们准备了一些以功能维度的代码示例供参考。
如遇接口问题，可以参考接口的 [API 文档](https://cloud.tencent.com/document/product/647/16865)。
### 代码示例
- [检测是否支持 WebRTC](https://cloud.tencent.com/document/product/647/16924)
- [直播连线](https://cloud.tencent.com/document/product/647/16924)
- [观众模式（不推流）](https://cloud.tencent.com/document/product/647/16924)

### 检测是否支持 WebRTC
[WebRTC 支持情况]()
```
 WebRTCAPI.fn.detectRTC( function(info ){
       if( !info.support){
           alert('不支持WebRTC')
       }
});
```	
## 直播连线
直播连线分为两种
1.进入房间后自动采集摄像头和麦克风数据连线互动。
2.进入房间后只观看不推流，在合适的时机再调用推流接口进行推流。
您可以根据业务需求进行选择，这里有 2 个接口需要配合使用。
主要差异就在初始化参数中 closeLocalMedia 的默认值设定。
### 自动推流

    var RTC = new WebRTCAPI( {
        userId: userId,
        sdkAppId:  sdkappid,
        accountType:  accountType,
        userSig: userSig
    },function(){
        //初始化化成功回调

        //进入房间
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
手动推流

    var RTC = new WebRTCAPI( {
        userId: userId,
        sdkAppId:  sdkappid,
        accountType:  accountType,
        userSig: userSig,
        closeLocalMedia: true
    },function(){
        //初始化化成功回调

        //进入房间
        RTC.createRoom({
            roomid : 12345,
            role : "user",
            privateMapKey:  privateMapKey,
        }, function(){
            //创建房间成功

            //手动推流
            RTC.startRTC();
        },function(error){
            console.error( error )
        } );
    } ,function(error){
        console.error( error )
    } );
观众模式（不推流）

    var RTC = new WebRTCAPI( {
        "userId": userId,
        "sdkAppId":  sdkappid,
        "accountType":  accountType,
        "userSig": userSig,
        "privateMapKey":  privateMapKey,
        "closeLocalMedia": true
    },function(){
        //进入房间
        RTC.createRoom({
            roomid : 12345,
            role : "user"
        });
    },function(error){
        console.error( error )
    } );
