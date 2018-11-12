## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides an overview that makes it easy for iOS developers to debug and integrate the APIs of Game Multimedia Engine.


## How to Use
![](https://main.qcloudimg.com/raw/810d0404638c494d9d5514eb5037cd37.png)


### Key considerations for using GME

This document only provides the most important APIs to help you get started with GME. For more APIs, see [API Documentation](https://intl.cloud.tencent.com/document/product/607/15221).


| Important API | Description |
| ------------- |:-------------:|
| InitEngine | Initializes GME |
|Poll    		| Triggers event callback	|
| SetDefaultAudienceAudioCategory | Sets background playback |
|EnterRoom	 	| Enters a room  		|
|EnableMic	 	| Enables the microphone 	|
|EnableSpeaker		| Enables the speaker 	|

**Notes:**

**When a GME API is called successfully, QAVError.OK is returned, and the value is 0.**

**GME APIs should be called in the same thread.**

**Authentication is needed before entering a room. Refer to the authentication section in relevant documentation for more information.**

**The Poll API should be called for GME to trigger event callback.**

**Refer to the callback message list for callback related information.**

**Device related operations can only be done after entering a room.**

**This document is applicable to GME sdk version：2.2.**

## Procedure for Quick Integration

### 1. Get a singleton
This API is used to get the ITMGContext instance when using the voice feature.
#### Function prototype

```
ITMGContext ITMGDelegate <NSObject>
```
#### Sample code  

```
ITMGContext* _context = [ITMGContext GetInstance];
_context.TMGDelegate =self;
```



### 2. Initialize the SDK
For more information on how to obtain parameters, please see [GME Integration Guide](https://intl.cloud.tencent.com/document/product/607/10782).
This API call needs SdkAppId and openId. The SdkAppId is obtained from Tencent Cloud console, and the openId is used to uniquely identify a user. The setting rule for openId can be customized by App developers, and this ID must be unique in an App (only INT64 is supported).
SDK must be initialized before a user can enter a room.
#### Function prototype 

```
ITMGContext -(void)InitEngine:(NSString*)sdkAppID openID:(NSString*)openID
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| sdkAppId | NSString | The SdkAppId obtained from Tencent Cloud console |
| openID | NSString | The OpenID supports Int64 type (which is passed after being converted to a string) only. It is used to identify users and must be greater than 10000. |
#### Sample code  

```
[[ITMGContext GetInstance] InitEngine:SDKAPPID3RD openID:_openId];
```


### Trigger event callback

This API is used to trigger the event callback via periodic Poll call in update.
#### Function prototype

```
ITMGContext -(void)Poll
```
#### Sample code
```
[[ITMGContext GetInstance] Poll];
```

### 4. Enter a room
This API is used to enter a room with the generated authentication information, and the ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received as a callback.
- Microphone and speaker are not enabled by default after a user enters the room.
- The API InitEngine should be called before the API EnterRoom.

#### Function prototype
```
ITMGContext   -(void)EnterRoom:(NSString*) roomId roomType:(int*)roomType authBuffer:(NSData*)authBuffer
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| roomId | NSString | Room ID. maximum to 127 characters.|
| roomType | int | Audio type of the room |
| authBuffer | NSData | Authentication key |

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume 	| 16k sampling rate is recommended if there is no special requirement for sound quality					| Fluent sound quality and ultra-low delay which is suitable for team speak scenarios in games like FPS and MOBA.	|							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| Choose 16k or 48k sampling rate depending on different requirements for sound quality				| Good sound quality and medium delay which is suitable for voice chat scenarios in casual games like Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|High-quality	|3|Speaker: media volume; headset: media volume	| To ensure optimum effect, it is recommended to enable HQ configuration with 48k sampling rate	| Super-high sound quality and relative high delay which is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

- If you have special requirements on the sound quality for certain scenario, contact the customer service.
- The sound quality in a game depends directly on the sampling rate set on the console. Please confirm whether the sampling rate you set on the [console](https://console.cloud.tencent.com/gamegme) is suitable for the project's application scenario.

#### Sample code  

```
[[ITMGContext GetInstance] EnterRoom:_roomId roomType:_roomType authBuffer:authBuffer];
```

### Callback for entering a room
ITMG_MAIN_EVENT_TYPE_ENTER_ROOM message is received after a user enters a room, the action of this event should be implemented in the OnEvent function.
#### Code Description
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
        {
            int result = ((NSNumber*)[data objectForKey:@"result"]).intValue;
            NSString* error_info = [data objectForKey:@"error_info"];
            // Receive the event of entering the room successfully.
        }
            break;
     }
}
```

### 6. Enable/Disable the microphone
This API is used to enable/disable the microphone. Microphone and speaker are not enabled by default after a user enters a room.
EnableMic = EnableAudioCaptureDevice + EnableAudioSend.
#### Function prototype  

```
ITMGContext GetAudioCtrl -(void)EnableMic:(BOOL)enable
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled | boolean | To enable the microphone, set this parameter to true, otherwise, set it to false. |

#### Sample code  

```
[[[ITMGContext GetInstance] GetAudioCtrl] EnableMic:YES];
```


### 7. Enable/Disable the speaker
This API is used to enable/disable the speaker.
EnableSpeaker = EnableAudioPlayDevice + EnableAudioRecv.
#### Function prototype  

```
ITMGContext GetAudioCtrl -(void)EnableSpeaker:(BOOL)enable
```
| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| isEnabled | boolean | To disable the speaker, set this parameter to NO, otherwise set it to YES. |

#### Sample code  

```
[[[ITMGContext GetInstance] GetAudioCtrl] EnableSpeaker:YES];
```


## Authentication
### Authentication information
AuthBuffer is generated for the purpose of encryption and authentication. For more information about the authentication data, refer to [GME Key](https://intl.cloud.tencent.com/document/product/607/12218). 

#### Function prototype

```
@interface QAVAuthBuffer : NSObject
+ (NSData*) GenAuthBuffer:(unsigned int)appId roomId:(NSString*)roomId identifier:(NSString*)identifier key:(NSString*)key;
+ @end
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------|
| appId | int | The SdkAppId obtained from the Tencent Cloud console |
| roomId | NSString |Room ID, maximum to 127 characters (The room ID parameter for voice message must be set to "null") |
| identifier | NSString | User ID |
| key | NSString | The key obtained from the Tencent Cloud [Console](https://console.cloud.tencent.com/gamegme)



#### Sample code  

```
NSData* authBuffer =   [QAVAuthBuffer GenAuthBuffer:SDKAPPID3RD.intValue roomId:_roomId openID:_openId key:AUTHKEY];
```

