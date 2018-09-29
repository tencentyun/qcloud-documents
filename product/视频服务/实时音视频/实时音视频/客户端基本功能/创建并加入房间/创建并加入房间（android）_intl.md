This document describes how to create a room in the client and publish a live video.
## Downloading Source Code
You can download the complete demo code used in this document.
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/demo_create.zip)

## Concepts
 - [Room](https://cloud.tencent.com/document/product/647/16792#.E6.88.BF.E9.97.B4)
 - [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
 - [Role configuration](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
 - Rendering control
 You need a platform to display the obtained video data. That is the rendering control, which can correspond to an Android control.

## Adding Rendering Control
You must first add a control to the previous demo layout to render the video:
```
<com.tencent.ilivesdk.view.AVRootView
        android:id="@+id/av_root_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
```

## Creating a Room Module
Define an API for the communication between the room module and Activity:
```Java
public interface IRoomView {
    // Entered the room successfully
    void onEnterRoom();
    // Failed to enter the room
    void onEnterRoomFailed(String module, int errCode, String errMsg);

    // Exited room successfully
    void onQuitRoomSuccess();
    // Failed to exit the room
    void onQuitRoomFailed(String module, int errCode, String errMsg);

    // Room disconnected
    void onRoomDisconnect(String module, int errCode, String errMsg);
}
```

Create a room module:
```Java
public class RoomHelper implements ILiveRoomOption.onExceptionListener, ILiveRoomOption.onRoomDisconnectListener {
    private IRoomView roomView;

    public RoomHelper(IRoomView view){
        roomView = view;
    }
    // Set the rendering control
    public void setRootView(AVRootView avRootView){
        ILiveRoomManager.getInstance().initAvRootView(avRootView);
    }
    // Create a room
    public int createRoom(int roomId){
        ILiveRoomOption option = new ILiveRoomOption()
                .privateMapKey(privateMapKey)   //Room ticket
                .imsupport(false)       // Do not need the IM feature              
                .exceptionListener(this)  //Listen on exceptional events
                .roomDisconnectListener(this)   //Listen on room disconnection events
                .controlRole("user")    // Use the user role
                .autoCamera(true)       // Enable the camera automatically and perform the upstream
                .autoMic(true);         // Enable the microphone automatically and perform the upstream

        return ILiveRoomManager.getInstance().createRoom(roomId, option, new ILiveCallBack() {
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
    // Exit the room
    public int quitRoom(){
        return ILiveRoomManager.getInstance().quitRoom(new ILiveCallBack() {
            @Override
            public void onSuccess(Object data) {
                roomView.onQuitRoomSuccess();
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                roomView.onQuitRoomFailed(module, errCode, errMsg);
            }
        });
    }

    // Handle the Activity event
    public void onPause(){
        ILiveRoomManager.getInstance().onPause();
    }
    public void onResume(){
        ILiveRoomManager.getInstance().onResume();
    }

    @Override
    public void onException(int exceptionId, int errCode, String errMsg) {
        //Handle the exceptional event
    }

    @Override
    public void onRoomDisconnect(int errCode, String errMsg) {
        //Handle room disconnection (generally, the room is reclaimed in Tencent QCloud server due to network outage or no upstream for a long time)
    }
}
```

## UI Development
In the onCreate event of the Activity of a room, you can create a room module and configure a rendering control.
```Java
roomHelper = new RoomHelper(this);
// Obtain the rendering control
AVRootView avRootView = findViewById(R.id.av_root_view);
// Set the background color to blue when there is no rendering (Note: you cannot set it directly in the layout)
avRootView.getVideoGroup().setBackgroundColor(Color.BLUE);
// Set the rendering control
roomHelper.setRootView(avRootView);
```
You can enter the room number and create a room according to the entered room number in the interface, or the room number can be hard-coded (for testing).
```Java
roomHelper.createRoom(1234);
```
If the onEnterRoom event is thrown and you can see your video images, the room is created successfully.

## FAQ

#### Error code 10004 Failed to enter a room and prompts "request room server address failed"
Make sure that the room ticket field (privateMapKey) is configured correctly.
> The privateMapKey field is required for new users, and existing users (do not need room tickets) need to configure the field at initialization
```
ILiveSDK.getInstance().setChannelMode(CommonConstants.E_ChannelMode.E_ChannelIMSDK);
```

#### Error code 71 Failed to enter a room and prompts "decodeSsoCmd_pbvideoapp_pbvideoinfoErr:user id error longConnHead.account=0"
This is caused by login of multiple accounts. Confirm whether the previous account is logged out before you log in to the new account.

#### Receive EXCEPTION_ENABLE_CAMERA_FAILED in onException and errCode is 1. Failed to enable the camera.
1. Confirm whether Android devices have a camera and the camera is working properly.
2. Confirm whether no other app occupies the camera in the background.
3. For devices with Android 6.0 or above, confirm whether the dynamic permission `Manifest.permission.CAMERA` of the camera is enabled.

#### Callback for failed operations. Error code 1003 or 8011
1. Operations of entering/exiting rooms are linearly exclusive. If your request is too frequent, SDK may throw 8011, which means the last operation must be completed (callback and return) before continuing (to enter/exit the room);
2. You can only enter one room at a time. If you do not exit the last room before creating (or entering) a new room, 1003 is thrown. In this case, you must exit the last room first.

## Email
If you have any questions, send us an email to trtcfb@qq.com.

