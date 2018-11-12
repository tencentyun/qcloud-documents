This document describes how to create a room, obtain LVB video images and exit the room when appropriate.
## Downloading Source Code
You can download the complete demo code used in this document. 
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/MAC_TRTC.zip)

## Concepts
 - [Room](https://cloud.tencent.com/document/product/647/16792#.E6.88.BF.E9.97.B4)
 - [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
 - [Role configuration](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
 - Rendering control
 You need a platform to display the obtained video data. That is the rendering control.
 - Video data types
 Tencent Cloud supports performing the upstream of one mainstream and one substream simultaneously in one account. Videos from different sources of video streams are classified into the following types: camera, screen sharing, and video playing (generated from PC).

| Video Type | Stream Type | Description |
|--|--|--|
| Camera | Mainstream | Data collected from the camera |
| Screen sharing | Substream | Generated from screen sharing |
| Video playing | Substream | Generated from video file playing |

## Procedure
### Creating a room
A room can be created by `ILiveRoomManager.h`, which requires two key parameters, room ID (roomId) and room configuration object (option):
* The roomId can be entered by users in an interface (see the demo), or hard-coded in codes for testing. The roomId must conform to the rules described in Preliminary Information.
    
* The room configuration object must be created by users. The ILiveRoomOption is a class used to configure the instant messaging and other features of the audios and videos in the room to be created. You can use defaultHostLiveOption by default.

The result of creating a room is returned by calling back Block. You can process it in successful/failed callback based on your business logic.

```objc
> TCLiveRoomWC.m
// Import the header file
#import <ILiveSDK/ILiveCoreHeader.h>

// Create a room
- (void)enterRoom{
    //Step 3: Configure a room
    ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption];
    option.imOption.imSupport = YES;
    // Set audio/video listening in the room
    option.memberStatusListener = self;
    // Set room disconnection event listening
    option.roomDisconnectListener = self;
    option.firstFrameListener = self;
    // This parameter indicates the audio/video specification used after a user enters a room. The value of the parameter is the role name configured by the customer in **Screen Setting** on the Tencent Cloud TRTC console (for example, the default role name is User, and you can set controlRole = @"user")
    option.controlRole = self.role;
    // Configure a room ticket
    option.privateMapKey = privateMapKey;

    //Step 4: Call the API to create a room and pass the room ID and room configuration object
    [[ILiveRoomManager getInstance] createRoom:[self.roomID intValue] option:option succ:^{
        NSLog(@"-----> create room succ");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"-----> create room fail,%@ %d %@",module, errId, errMsg);
    }];

}
```

After you enter the room, the camera and microphone are automatically enabled and the stream is automatically pushed, which can be set in the `ILiveRoomOption` configuration object passed when you create the room). In the live room, all audio/video events are notified to the listener through audio/video event callback. First, you must set a listener option.memberStatusListener = self;.


### Listening events in the room
When creating a room, you can set room audio/video event listening and room disconnection event listening in the configuration object to listen for events in the room.
The listener of audio/video events complies with the `ILiveMemStatusListener` protocol and implements the following methods:

```objc
@protocol ILiveMemStatusListener <NSObject>
/**
 The function of the notification of status changes of members in the room, through which the business side will be notified when the status members in the room change (such as publishing audios or videos).

 @param event     Status change ID. For more information, see the definition of QAVUpdateEvent
 @param endpoints List of member IDs whose statuses change.

 @return YES Operation succeeded
 */
- (BOOL)onEndpointsUpdateInfo:(QAVUpdateEvent)event updateList:(NSArray *)endpoints;
@end
```

>**Notes:**
> This method is a callback method for audio/video events in the room. If someone in the room enables the camera and microphone, the underlying SDK will call back this method to notify the listener. This method has two parameters, event and endpoints.
>  - The event is an enumerated value for events, which defines the types of events that could occur to members in the room, including entering and exiting the room, and enabling/disabling cameras and microphones.
> 
>  - The endpoints is an array of QAVEndpoint objects, which specifies each user sending an event. This method is used to send notifications of specific types of changes in audios and videos and the users who make those changes. When an event change is listened for, some adjustments must be made on the interface. For example, when it finds that a user camera is enabled, a rendering image should be added to the interface to render the user's image.


The event has the following values:

```objc
typedef NS_ENUM(NSInteger, QAVUpdateEvent) {
    QAV_EVENT_ID_NONE                      = 0, ///< Default value. Ignored..
    QAV_EVENT_ID_ENDPOINT_ENTER            = 1, ///< Event of entering a room..
    QAV_EVENT_ID_ENDPOINT_EXIT             = 2, ///< Event of exiting a room..
    QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO = 3, ///< Has a camera video event.
    QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO  = 4, ///< No camera video event.
    QAV_EVENT_ID_ENDPOINT_HAS_AUDIO        = 5, ///< Has an audio event.
    QAV_EVENT_ID_ENDPOINT_NO_AUDIO         = 6, ///< No audio event.
    QAV_EVENT_ID_ENDPOINT_HAS_SCREEN_VIDEO = 7, ///< Has a screen video event.
    QAV_EVENT_ID_ENDPOINT_NO_SCREEN_VIDEO  = 8, ///< No screen video event.
    QAV_EVENT_ID_ENDPOINT_HAS_MEDIA_FILE_VIDEO = 9, ///< Has a file video event.
    QAV_EVENT_ID_ENDPOINT_NO_MEDIA_FILE_VIDEO  = 10, ///< No file video event.
};
```
The "video data types" mentioned earlier can be defined in the event.
You only need to configure the listener, listen for the event QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO which indicates that the camera is enabled in the proxy method, and add the user's rendering image to the interface.

```objc
// Import the header file
#import <ILiveSDK/ILiveCoreHeader.h>

// Audio/video event callback
- (BOOL)onEndpointsUpdateInfo:(QAVUpdateEvent)event updateList:(NSArray *)endpoints {
    switch (event) {
        case QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO:
            {
                /*
                 Create and add rendering views, pass userID and rendering image type. QAVVIDEO_SRC_TYPE_CAMERA (camera image) is entered here.
                 */
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderViewForMac  *renderView = [frameDispatcher addRenderAt:CGRectMake(0,  0, self.videoLayoutView.frame.size.width, self.videoLayoutView.frame.size.height - 20) forIdentifier:endoption.identifier srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                renderView.identifier = endoption.identifier;
                [self.window.contentView addSubview:renderView];
            }
            break;
    }
    return YES;
}
```

If everything goes well, you can see the live image when you successfully create the room and are redirected to the LVB page.

> Since this document is intended to create a live room and obtain images, the processing of audio and video event callback is relatively simple, but this is also fundamental. More information on this method will be described in subsequent documents. You can listen for different events as needed. For example, you can listen for the events of members entering and exiting the room and display the notification of members entering and exiting the room on the interface.

The listening of the room disconnection event complies with the `ILiveRoomDisconnectListener` protocol and implements the following methods:

```objc

/**
 Prompt when SDK actively exits the room. This callback method indicates that the SDK has actively exited the room. The SDK will actively exit the room due to the 30s timeout of heartbeat packet. The App listens for this event of exiting a room and processes it accordingly.

 @param reason Reasons for exiting the room. See the error code for specific values

 @return YES Operation succeeded
 */
- (BOOL)onRoomDisconnect:(int)reason;
```

This method is a callback after the SDK actively exits the room, and developers can process it in methods based on the business needs.

### Exit a room
Call the API of exiting a room of ILiveSDk.
Call the API when the window is closed.


```objc
//Close the window and exit the room
-(void)windowWillClose:(NSNotification *)notification{
    [[ILiveRoomManager getInstance] quitRoom:^{
        NSLog(@"-----> quit room succ");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"-----> quit room fail,%@ %d %@",module, errId, errMsg);
    }];
}
```
After a user exits the room, the resources in the room will be reclaimed, including roomID. You can create a new room with the same roomID.

## FAQ
#### Failed to enter a room, and was prompted for required permission
Make sure that the room ticket field (privateMapKey) is configured correctly.
> The privateMapKey field is required for new users, and existing users (do not need room tickets) need to configure the field at initialization
```
[[ILiveSDK getInstance] setChannelMode:E_ChannelIMSDK withHost:@""];
```

#### Callback for failed operations. Error code 1003 or 8011
1. Operations of entering/exiting rooms are linearly exclusive. If your request is too frequent, SDK may throw 8011, which means the last operation must be completed (callback and return) before continuing (to enter/exit the room).
2. You can only enter one room at a time. If you do not exit the last room before creating (or entering) a new room, 1003 is thrown. In this case, you must exit the last room first.

## Email
If you have any questions, send us an email to trtcfb@qq.com.

