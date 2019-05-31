# Overview of Basic LVB APIs

## LVB Procedure Example

![](http://mc.qcloudimg.com/static/img/e6632b362fbc90745505823b1dc295bd/image.png)


### 1. Initialization

| API |  Description  |
|---------|---------|
| **initSdk** | Pre-initialization of some of the iLiveSDK classes, which is the first step of all actions. appId is required |


| Parameter | Description |
|---------|---------|
| Conext | AppcalicationContext is recommeded |
| int | appid of input business side |
| int | accounttype of input business side |

* Example
  
```java 
ILiveSDK.getInstance().initSdk(getApplicationContext(), appid, accoutype);
```  


### 2. Account Login
| API |  Description  |
|---------|---------|
| **iLiveLogin** | Use either hosting method or independent method. After acquiring user's sig, you can inform the backend of the launch of audio and video modules using login API |

| Parameter | Description |
|---------|---------|
| String | User id, which is the unique ID in LVB  |
| String |Key Sig of authentication. If independent login method is used, the sig is issued after being generated at the business backend |
| ILiveCallBack | API for account login callback. Inform whether the launch is successful |
<br/>
* Example
    
```java     
ILiveLoginManager.getInstance().iLiveLogin(ILiveSDK.getInstance().getMyUserId(), "123456", new ILiveCallBack() {
                @Override
                public void onSuccess(Object data) {
                    bLogin = true;
                    Toast.makeText(ContactActivity.this, "login success !", Toast.LENGTH_SHORT).show();
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {
                    Toast.makeText(ContactActivity.this, module + "|login fail " + errCode + " " + errMsg, Toast.LENGTH_SHORT).show();
                }
            });
```      
### 3. Create a Room

| API Name | Description |
|---------|---------|
| **createRoom** | Create an LVB. LVB can be created only after initialization and login are successful |

| Parameter | Description |
|---------|---------|
| int | Unique room ID. It is recommended to allow the business backend to assign the ID |
| ILiveRoomOption | Room configuration options. You can configure role, permission, VJ ID, camera parameters, etc. For more information, please see the class ILiveRoomOption |
| ILiveCallBack | API for room creation callback. Inform whether the creation of room is successful |

```java            
  //Configuration options of creating room
            ILiveRoomOption hostOption = new ILiveRoomOption(null).
                    controlRole("Host")//Role configuration
                    .authBits(AVRoomMulti.AUTH_BITS_DEFAULT)//Permission configuration
                    .cameraId(ILiveConstants.FRONT_CAMERA)//Front/rear-facing camera
                    .videoRecvMode(AVRoomMulti.VIDEO_RECV_MODE_SEMI_AUTO_RECV_CAMERA_VIDEO);//Whether to start semi-automatic receiving
                   //Create room
            ILVLiveManager.getInstance().createRoom(room, hostOption, new ILiveCallBack() {
                @Override
                public void onSuccess(Object data) {
                    Toast.makeText(LiveActivity.this, "create room  ok", Toast.LENGTH_SHORT).show();
                    logoutBtn.setVisibility(View.INVISIBLE);
                    backBtn.setVisibility(View.VISIBLE);
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {
                    Toast.makeText(LiveActivity.this, module + "|create fail " + errMsg + " " + errMsg, Toast.LENGTH_SHORT).show();
                }
            });
```
### 4. Join a Room
| API |  Description  |
|---------|---------|
| **joinRoom** | Call API "Join Room" for viewers |


| Parameter | Description |
|---------|---------|
| int | Unique room ID. It is recommended to allow the business backend to assign the ID |
| ILiveRoomOption | Room configuration options. You can configure role, permission, VJ ID, camera parameters, etc. For more information, please see the class ILiveRoomOption |
| ILiveCallBack | API for room joining callback. Inform whether viewer has successfully join the room |
<br/>

```java  



           //Configuration options of joining room
            ILiveRoomOption memberOption = new ILiveRoomOption(hostId)
                    .autoCamera(false) //Whether to enable camera automatically
                    .controlRole("NormalMember") //Role configuration
                    .authBits(AVRoomMulti.AUTH_BITS_JOIN_ROOM | AVRoomMulti.AUTH_BITS_RECV_AUDIO |              AVRoomMulti.AUTH_BITS_RECV_CAMERA_VIDEO | AVRoomMulti.AUTH_BITS_RECV_SCREEN_VIDEO) //Permission configuration
                    .videoRecvMode(AVRoomMulti.VIDEO_RECV_MODE_SEMI_AUTO_RECV_CAMERA_VIDEO) //Whether to start semi-automatic receiving
                    .autoMic(false);//Whether to enable mic automatically
            //Join a room
            ILVLiveManager.getInstance().joinRoom(room, memberOption, new ILiveCallBack() {
                @Override
                public void onSuccess(Object data) {
                    bEnterRoom = true;
                    Toast.makeText(LiveActivity.this, "join room  ok ", Toast.LENGTH_SHORT).show();
                    logoutBtn.setVisibility(View.INVISIBLE);
                    backBtn.setVisibility(View.VISIBLE);
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {
                    Toast.makeText(LiveActivity.this, module + "|join fail " + errMsg + " " + errMsg, Toast.LENGTH_SHORT).show();
                }
            });
```            
            
            
### Configuring Render Layers
> Illustration of render layers. Insert an AVRootView in the interface layer xml. Audio/video data is rendered through AVRootView. In a scenario of multi-screen interaction, AVRootView is not one layer of view but an overlay of multiple layers of AVVideoViews. For LVB business, the layer 0 is the maximum view by default. Other viewers who interact in LVB locate in layer 1, 2 and 3. The size of each layer can be adjusted dynamically.


![](http://mc.qcloudimg.com/static/img/d063a1980cc046cafa0444df0b609d02/image.png)
* Example

```java
    <com.tencent.ilivesdk.view.AVRootView
        android:id="@+id/av_root_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="@color/white" />
        
        
        avRootView = (AVRootView) findViewById(R.id.av_root_view);
        ILVLiveManager.getInstance().setAvVideoView(avRootView);
```  
           

