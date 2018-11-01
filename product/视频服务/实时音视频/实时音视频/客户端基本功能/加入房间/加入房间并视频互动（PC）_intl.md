This document describes how a viewer enters a created room and interacts with other users.

## Downloading Source Code
You can download the complete demo code used in this document.
[Click to download](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_join.zip)

## Entering a Room
Just like creating a room, you need to complete initialization and login before you can enter a room. You also need to enter the iLiveRoomOption structure to describe the information of the room you want to enter, and then call the API joinRoom() to enter the room.
```c++
//Notification of status changes of members in the room (such as enabling/disabling cameras)
void  OnMemStatusChange(E_EndpointEventId eventId, const Vector<String> &ids, void* data)
{
}

iLiveRoomOption roomOption;
roomOption.privateMapKey = privateMapKey;    // Configure a room ticket
roomOption.roomId = RoomId;                 //ID of the room to be entered
roomOption.authBits = AUTH_BITS_DEFAULT;    //With all permissions
roomOption.controlRole = "user";      //Use the "user" role configured on Spear
roomOption.memberStatusListener = OnMemStatusChange;//Callback indicating change of member status
roomOption.data = NULL;//void* data pointer returned intact in callback.

GetILive()->joinRoom(roomOption, [](void* data) {
	//Entered the room successfully
}, [](const int code, const char *desc, void* data) {
	//Failed to enter the room
}, NULL);
```

## Enabling Camera and Microphone

After entering a room, a user can enable the camera and the microphone to interact with other users in exactly the same way as that in Creating a Room.
For more information, see [Creating a Room - Enabling Camera and Microphone](/document/product/647/16819#.E6.89.93.E5.BC.80.E6.91.84.E5.83.8F.E5.A4.B4.E5.92.8C.E9.BA.A6.E5.85.8B.E9.A3.8E).

## Remote Video Rendering
After a user enter a room, the SDK will automatically request the video images of other members in the room, which means the remote video data can be obtained in this callback at this time. You need to render the remote screen in the same way as that in Creating a Room. For more information, see [Creating a Room - Video Rendering](/document/product/647/16819#.E8.A7.86.E9.A2.91.E6.B8.B2.E6.9F.93).

In this way, members in the room can have audio/video interactions.

## Source Code Description
- Test description
The interoperability test between the Demo provided in this document and the complete Demo in [Creating a Room](/document/product/647/16819) should be conducted separately on two computers, because it is hard coded to enable the first camera and the first microphone. If you want to do the test on one computer, the computer must have at least two cameras and microphones, and two users cannot use the same device.

## Execution Results

![](https://main.qcloudimg.com/raw/7f16017270f4be5d36d8954b85dd57d6.png)

## FAQ

#### Failed to enter a room, and was prompted for required permission
Make sure that the room ticket field (privateMapKey) is configured correctly.
> The privateMapKey field is required for new users, and existing users (do not need room tickets) need to configure [[ILiveSDK getInstance] setChannelMode:E_ChannelIMRestAPI withHost:@""]; at initialization
```
GetILive()->setChannelMode(E_ChannelIMSDK);
```

## Email
If you have any questions, send us an email to trtcfb@qq.com.

