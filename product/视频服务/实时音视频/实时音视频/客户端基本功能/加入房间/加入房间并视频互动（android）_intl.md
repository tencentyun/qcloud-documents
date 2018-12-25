This document describes how a viewer enters a room and enables the camera and the microphone to interact with other users.

## Downloading Source Code
You can download the complete demo code used in this document. 
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/demo_join.zip)

## Concepts
* [TRTC application](https://cloud.tencent.com/document/product/647/16792#.E5.AE.9E.E6.97.B6.E9.9F.B3.E8.A7.86.E9.A2.91.E5.BA.94.E7.94.A8)
* [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
* [Role configuration](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
* Camera ID (cameraId) 
  Android phones usually have two cameras: a front camera and a rear camera. The SDK can distinguish between them by cameraId.
	
| Constant | Description |
|--|--|
|ILiveConstants.NONE_CAMERA|Invalid camera ID (Generally indicating that the camera is not enabled) |
|ILiveConstants.FRONT_CAMERA|Front camera ID |
|ILiveConstants.BACK_CAMERA|Rear camera ID |

## Entering a Room
The room module in entering a room is basically the same as that in [Creating a room](/document/product/647/16806), except that the method used here is joinRoom.
```Java
    // Enter a room
    public int joinRoom(int roomId){
        ILiveRoomOption option = new ILiveRoomOption()
                .privateMapKey(privateMapKey)   // Room ticket
                .imsupport(false)       // Do not need the IM feature
                .exceptionListener(this)  // Listen on exceptional events
                .roomDisconnectListener(this)   // Listen on room disconnection events
                .controlRole("user")  // Use the user role
                .autoCamera(false)       // Do not enable the camera when the user enters a room
                .autoMic(false);         // Do not enable the microphone when the user enters a room

        return ILiveRoomManager.getInstance().joinRoom(roomId, option, new ILiveCallBack() {
            @Override
            public void onSuccess(Object data) {
                roomView.onEnterRoom();
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                roomView.onEnterRoomFailed(module, errCode, errMsg);
            }
        });
    }
```
 
## Enabling Capturing Devices (Camera and Microphone)
If interaction with other users via upstream audio/video is required, you need to add two APIs to the room module to control the camera and the microphone respectively.
```
    // Camera
    public int enableCamera(int cameraId, boolean enable){
        return ILiveRoomManager.getInstance().enableCamera(cameraId, enable);
    }
    // Microphone
    public int enableMic(boolean enable){
        return ILiveRoomManager.getInstance().enableMic(enable);
    }
```

## UI Development
We can enrich the interface by placing a set of buttons on the top of the rendering control for switching roles, and enabling or disabling the camera and the microphone.
We won't go into details here.

## FAQ
#### Failed to enter a room, and was prompted for required permission
Make sure that the room ticket field (privateMapKey) is configured correctly.
> The privateMapKey field is required for new users, and existing users (do not need room tickets) need to configure the field at initialization
```
ILiveSDK.getInstance().setChannelMode(CommonConstants.E_ChannelMode.E_ChannelIMSDK);
```

## Email
If you have any questions, send us an email to trtcfb@qq.com.

