This document describes how to create a room in the client, and enable the camera and microphone to see your own video images.

## Downloading Source Code
You can download the complete demo code used in this document. 
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_create.zip)

## Concepts
 - [Room](https://cloud.tencent.com/document/product/647/16792#.E6.88.BF.E9.97.B4)
 - [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
 - [Role configuration](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
 - Video rendering
 The captured video data must be rendered. This process is called video rendering.

## Setting a callback for video data.
To obtain video data, you must set callback functions for local and remote video data before creating/entering the room.
```c++
//Callback for local video data
void OnLocalVideo(const LiveVideoFrame* video_frame, void* data)
{
}

//Callback for remote video data
void OnRemoteVideo(const LiveVideoFrame* video_frame, void* data)
{
}

GetILive()->setLocalVideoCallBack(OnLocalVideo, NULL);
GetILive()->setRemoteVideoCallBack(OnRemoteVideo, NULL);
```

## Creating a Room
To create a room, you need to enter the iLiveRoomOption structure to describe the information of the created room. The sample code is as follows:
```c++
//Notification of status changes of members in the room (such as enabling/disabling cameras)
void  OnMemStatusChange(E_EndpointEventId eventId, const Vector<String> &ids, void* data)
{
}

iLiveRoomOption roomOption;
roomOption.privateMapKey = privateMapKey;    // Configure a room ticket
roomOption.roomId = RoomId;                 //ID of the room to be created
roomOption.authBits = AUTH_BITS_DEFAULT;    //With all permissions
roomOption.controlRole = "LiveMaster";      //Use the "LiveMaster" role configured on Spear
roomOption.memberStatusListener = OnMemStatusChange;//Callback indicating status change of members in the room
roomOption.data = NULL;//void* data pointer returned intact in callback;

GetILive()->createRoom(roomOption, [](void* data) {
	//Room created successfully
}, [](const int code, const char *desc, void* data) {
	//Failed to create a room
}, NULL);
```

## Enabling Camera and Microphone
After you create a room, you don't need to call an API to enter the room. The camera and microphone can be enabled to perform audio/video data upstream.
```c++
//Enable the camera
Vector< Pair<String/*id*/, String/*name*/> > cameraList;
GetILive()->getCameraList(cameraList);//Obtain a list of available cameras
if (cameraList.size() > 0 )
{
	GetILive()->openCamera(cameraList[0].first); //Enable the first camera (default camera)
}

//Enable the microphone
Vector< Pair<String/*id*/, String/*name*/> > micList;
GetILive()->getMicList(micList);//Obtain a list of available microphones
if (micList.size() > 0)
{
	GetILive()->openMic(micList[0].first); //Enable the first microphone (default microphone)
}
```

In this case, the OnLocalVideo callback function configured previously receives every frame of video data. The data size of each video frame can be printed in the callback to verify whether the video data is received.

```c++
void OnLocalVideo(const LiveVideoFrame* video_frame, void* data)
{
	printf("frame size: %d\n", video_frame->dataSize);
}
```

## Video Rendering
To see the video image, the received video image from the local camera must be rendered. The iLiveSDK provides a rendering module (iLiveRootView) where a window handle is assigned and a View (user information of the image to be rendered) is added to the rendering module before transmitting each frame of video image to the rendering module for rendering. You can read [Rendering Module Usage Documentation](/document/product/647/16919) carefully and understand it with the demo source code in this example.

## Interface Design
In this demo, a window is created for the follow-up courses, with the upper part displaying local video images and the lower part displaying remote video images, as shown below:

![](https://main.qcloudimg.com/raw/a1fee03da78f0a145bb2fd06a62a5b27.png)

To reduce the complexity, this demo only demonstrates the audio/video communication between two people. In actual development, you can add multiple rendering views as needed.

## Execution Results

![](https://main.qcloudimg.com/raw/1f1677b779f36f761bfef6a0d5282c15.png)

## FAQ

#### Failed to enter a room, and was prompted for required permission
Make sure that the room ticket field (privateMapKey) is configured correctly.
> The privateMapKey field is required for new users, and existing users (do not need room tickets) need to configure the field at initialization
```
GetILive()->setChannelMode(E_ChannelIMSDK);
```

#### Useless information is outputted on the console:

When some APIs of the SDK are called, useless information may be outputted on the console. For example, the output results after creating a room are shown as follows:

![](https://main.qcloudimg.com/raw/b849f6239ca311d2d72a381db455d623.png)

This is because iLiveSDK uses other SDK internally. It actually shows the printing output information of other SDKs, which will not affect the actual usage and can be ignored.

## Email
If you have any questions, send us an email to trtcfb@qq.com.

