# LVB+Joint Broadcasting (LiveRoom)

**LVB+Joint Broadcasting** is an LVB mode commonly used in the **Live Show** and **Online Education** scenarios. With a good applicability to many scenarios, it supports online live broadcasting featuring both high concurrency and low cost, but also enables video chats between VJs and viewers via joint broadcasting.

![img](https://main.qcloudimg.com/raw/4032376146a41d3597d9a28350b542b5.jpg)

Tencent Cloud provides "LVB+Joint Broadcasting" by using [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606), a component consisting of Client and Server (both open source). For more information on how to interface with it, please see [DOC](https://cloud.tencent.com/document/product/454/14606). This document displays the API list for Client:

> [Download](https://cloud.tencent.com/document/product/454/7873#Windows) the SDK package on Tencent Cloud's official website. LiveRoom related header files and source code files are included in SDK\Rooms\LiveRoom.

## LiveRoom

| Name | Description |
| ---------------------------------------- | ---------------------------------------- |
| instance() | Gets a single instance of LiveRoom and calls the API of LiveRoom through the single instance. |
| setCallback(ILiveRoomCallback callback) | Sets the callback proxy for LiveRoom callback, and listens to the internal status of LiveRoom and the execution results of the API. |
| login(string serverDomain, LiveAuthData authData, ILoginLiveCallback callback) | Logs in to the business server RoomService before you can normally use other APIs and the IM feature. |
| logout() | Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail. |
| getRoomList(int index, int cnt, IGetLiveRoomListCallback callback) | Gets the room list. If there are many rooms, you can get the list in pages. |
| getAudienceList(string roomID) | Gets the list of viewers and returns only the last 30 viewers who entered the room. |
| createRoom(string roomID, string roomInfo) | Creates a room. The new room will be added to the room list in the backend, and then VJs can start pushing. |
| enterRoom(string roomID, IntPtr rendHwnd, Rectangle rect) | Enters a room. |
| leaveRoom() | Leaves the room. If the primary VJ leaves, the room will be terminated by the backend; if secondary VJs or viewers leave, the remaining participants can continue watching. |
| sendRoomTextMsg(string msg) | Sends plain text messages, such as sending on-screen comments under LVB scenarios. |
| sendRoomCustomMsg(string cmd, string msg) | Sends custom messages, such as giving a "Like" or flower under LVB scenarios. |
| startLocalPreview(IntPtr rendHwnd, Rectangle rect) | Enables the default camera preview |
| updateLocalPreview(IntPtr rendHwnd, Rectangle rect) | Resets the camera preview area. When the size of the specified local HWND window changes, the video rendering area can be rescaled via this function. |
| stopLocalPreview() | Disables camera preview |
| startScreenPreview(IntPtr rendHwnd, IntPtr captureHwnd, Rectangle renderRect, Rectangle captureRect) | Enables screen sharing |
| stopScreenPreview() | Disables screen sharing |
| addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID) | Plays videos of other VJs in the room. |
| updateRemotePreview(IntPtr rendHwnd, Rectangle rect, string userID) | Resets the video preview area of the specified userID. When the size of the specified local HWND window changes, the video rendering area can be rescaled via this function. |
| removeRemoteView(string userID) | Stops playing videos of other VJs. |
| setMute(bool mute) | Enables Mute |
| setVideoQuality(LiveVideoQuality quality, LiveAspectRatio ratio) | Sets the preset options for image quality |
| setBeautyStyle(LiveBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel) | Sets beauty filter and whitening effects |
| requestJoinPusher() | Joint broadcasting request from viewer |
| acceptJoinPusher(string userID) | The primary VJ accepts the joint broadcasting request and informs the request initiator |
| rejectJoinPusher(string userID, string reason) | The primary VJ rejects the joint broadcasting request and informs the request initiator |
| kickoutSubPusher(string userID) | The primary VJ kicks out a secondary VJ |

## ILoginLiveCallback

| Name | Description |
| ---------------------------------------- | ------------ |
| onLogin(LiveResult res, LiveAuthData authData) | Callback of the login result |

## IGetLiveRoomListCallback

| Name | Description |
| ---------------------------------------- | --------- |
| onGetRoomList(LiveResult res, List<LiveRoomData> rooms) | Callback of obtaining a room list |

## ILiveRoomCallback

| Name | Description |
| ---------------------------------------- | ----------------- |
| onCreateRoom(LiveResult res, string roomID) | Callback of creating a room |
| onEnterRoom(LiveResult res) | Callback of entering a room |
| onUpdateRoomData(LiveResult res, LiveRoomData roomData) | Callback of room information change |
| void onGetAudienceList(LiveResult res, List<LiveAudienceData> audiences) | Callback of viewer list query |
| onPusherJoin(LiveMemberData member) | Callback of joint broadcasting viewer entering the room |
| void onPusherQuit(LiveMemberData member) | Callback of joint broadcasting viewers exiting the room |
| onRoomClosed(string roomID) | Callback of room dissolution |
| onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg) | Receives plain text messages |
| onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message) | Receives custom messages |
| onError(LiveResult res, string userID) | Notification of internal LiveRoom error |
| onRecvJoinPusherRequest(string roomID, string userID, string userName, string userAvatar) | Receives a joint broadcasting request |
| onRecvAcceptJoinPusher(string roomID, string msg) | Receives the notification of accepting a joint broadcasting request |
| onRecvRejectJoinPusher(string roomID, string msg) | Receives the notification of rejecting a joint broadcasting request |
| onRecvKickoutSubPusher(string roomID) | Receives the notification of the primary VJ kicking out a secondary VJ |

## Details of LiveRoom Object APIs

### 1. instance

-  Definition: static LiveRoom instance()

-  Description: Gets a single instance of LiveRoom and calls the API of LiveRoom through the single instance

-  Example:

  ```c#
  LiveRoom m_liveRoom = null;
  m_liveRoom = LiveRoom.instance();
  ```

### 2. setCallback

-  Definition: void setCallback(ILiveRoomCallback callback)

-  Description: Sets the callback proxy for LiveRoom callback, and listens to the internal status of LiveRoom and the execution results of the API

-  Parameter:

| Parameter | Type | Description |
| -------- | ----------------- | ------------------------- |
| callback | ILiveRoomCallback | Proxy API of ILiveRoomCallback type |

-  Example:

  ```c#
  public class MainDialog : ILiveRoomCallback
  {
      MainDialog()
      {
          m_liveRoom.setCallback(this);	//Set callback
      }
      
      void ILiveRoomCallback.onCreateRoom(LiveResult res, string roomID)
      {
      
      }
    
      void ILiveRoomCallback.onEnterRoom(LiveResult res)
      {
    
      }
    
      void ILiveRoomCallback.onUpdateRoomData(LiveResult res, LiveRoomData roomData)
      {
    
      }
    
      ...
  }
  ```

  ​

### 3. login

-  Definition: void login(string serverDomain, LiveAuthData authData, ILoginLiveCallback callback)

-  Description: Logs in to the business server RoomService before you can normally use other APIs and the IM feature

-  Parameters:

| Parameter | Type | Description |
| ------------ | ------------------ | ---------------------------------------- |
| serverDomain | string | URL of RoomService. In consideration of security, it is recommended to access the https encrypted link. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| authData | LiveAuthData | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a success login. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| callback | ILoginLiveCallback | Proxy API of ILoginLiveCallback type, used to call back the login result |

-  Example:

  ```c#
  string serverDomain = "https://roomtest.qcloud.com/weapp/live_room";

  m_authData.sdkAppID = sdkAppID;
  m_authData.accountType = accountType;
  m_authData.userID = userID;
  m_authData.userSig = userSig;
  m_authData.userName = userName;
  m_authData.userAvatar = userAvatar;
  m_authData.token = token;

  // This class implements the ILoginCallback API to obtain login results
  m_liveRoom.login(serverDomain, m_authData, this);
  ```

### 4. logout

-  Definition: void logout();

-  Description: Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail.

-  Example:

  ```c#
  m_liveRoom.logout();
  ```

### 5. getRoomList

-  Definition: void getRoomList(int index, int cnt, IGetLiveRoomListCallback* callback)

-  Description: Gets the room list. If there are many rooms, you can get the list in pages.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------------ | ---------------------------------------- |
| index | int | Gets the list in pages. The default value can be 0, and for the subsequent retrieval, the value can be set as the starting room index (for example, set index=0 and cnt=5 for the first retrieval, and set index=5 for the second page). |
| count | int | The maximum number of rooms returned per call; 0 indicates all rooms that meet the conditions |
| callback | IGetLiveRoomListCallback | Proxy API of IGetLiveRoomListCallback type, used to call back the query result |

-  Example:

  ```c#
  // Start from index=0. A maximum of 20 rooms can be queried. This class implements the IGetRoomListCallback API to obtain query results
  m_liveRoom.getRoomList(0, 20, this);
  ```

### 6. getAudienceList

-  Definition: void getAudienceList(string roomID)
-  Description: Gets the list of viewers and returns only the last 30 viewers who entered the room
-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ------------------------------ |
| roomID | string | roomID, which is obtained in the room list returned by the getRoomList API |

-  Example:

```c#
m_liveRoom.getRoomList(roomID);
```

### 7. createRoom

-  Definition: void createRoom(string roomID, string roomInfo)

-  Description: Creates a room, and the new room will be added to the room list in the backend, and then VJs can start pushing.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------ | ---------------------------------------- |
| roomID | string | Room ID. If an empty string is specified, a roomID is assigned to you. Otherwise, the specified roomID is used as the ID of this room. |
| roomInfo | string | Custom data. This field is included in the room information. It is recommended that you define roomInfo in json format, which is highly extensible. |

-  Example:

  ```c#
  // A roomID is assigned to you
  m_liveRoom.createRoom("", "{\"roomName\": \"My first room\"}");
  ```

### 8. enterRoom

-  Definition: void enterRoom(string roomID, IntPtr rendHwnd, Rectangle rect)

-  Description: Enters a room.

-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ---------------------------------------- |
| roomID | string | roomID - the ID of the room to be entered, which is obtained in the room list returned by the getRoomList API |
| rendHwnd | IntPtr | HWND that identifies the preview window. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c#
  // Render in the entire form window
  Rectangle rect = new Rectangle(0, 0, form.Width, form.Height);
  m_liveRoom.enterRoom(roomID, form.Handle, rect);
  ```

### 9. leaveRoom

-  Definition: void leaveRoom()

-  Description: Leaves the room. If the primary VJ leaves, the room will be terminated by the backend; if secondary VJs or viewers leave, the remaining participants can continue watching.

-  Example:

  ```c#
  m_liveRoom.leaveRoom();
  ```

### 10. sendRoomTextMsg

-  Definition: void sendRoomTextMsg(string msg)

-  Description: Sends plain text messages, such as sending on-screen comments under LVB scenarios.

-  Parameter:

| Parameter | Type | Description |
| ---- | ------ | ---- |
| msg | string | Text messages |

-  Example:

  ```c#
  m_liveRoom.sendRoomTextMsg("Hello LiveRoom");
  ```

### 11. sendRoomCustomMsg

-  Definition: void sendRoomCustomMsg(string cmd, string msg)

-  Description: Sends custom messages, such as giving a "Like" or flower under LVB scenarios

-  Parameters:

| Parameter | Type | Description |
| ---- | ------ | ------------------ |
| cmd | string | Custom CMD, jointly determined by the sender and receiver |
| msg | string | Custom messages |

-  Example:

  ```c#
  // Assume that the CMD determined by the sender and receiver includes Smile and Anger
  m_liveRoom.sendRoomCustomMsg("Smile", "I am hungry");
  ```

### 12. startLocalPreview

-  Definition: void startLocalPreview(IntPtr rendHwnd, Rectangle rect)

-  Description: Enables the default camera preview

-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c#
  // Render in the entire form window
  Rectangle rect = new Rectangle(0, 0, form.Width, form.Height);
  m_liveRoom.startLocalPreview(form.Handle, rect);
  ```

### 13. updateLocalPreview

-  Definition: void updateLocalPreview(IntPtr rendHwnd, Rectangle rect)

-  Description: Resets the preview area for camera. When the size of the window identified by the specified HWND changes, you can resize the video rendering area using this function.

-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c#
  // Render in the entire form window
  Rectangle rect = new Rectangle(0, 0, form.Width, form.Height);
  m_liveRoom.updateLocalPreview(form.Handle, rect);
  ```

### 14. stopLocalPreview

-  Definition: void stopLocalPreview()

-  Description: Disables camera preview

-  Example:

  ```c#
  m_liveRoom.stopLocalPreview();
  ```

### 15. startScreenPreview

-  Definition: bool startScreenPreview(IntPtr rendHwnd, IntPtr captureHwnd, Rectangle renderRect, Rectangle captureRect)

-  Description: Enables screen sharing

-  Parameters:

| Parameter | Type | Description |
| ----------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| captureHwnd | IntPtr | Specifies the capture window. If it is NULL, captureRect does not work and the entire screen is captured; if it is not NULL, the current window is captured. |
| renderRect | Rectangle | Specifies the rendering area of the video screen on rendHwnd |
| captureRect | Rectangle | Specifies the customer area of the capture window |

-  Returned value: Success or Failed

-  Example:

  ```c#
  // Render in the entire form window
  Rectangle renderRect = new Rectangle(0, 0, rendForm.Width, rendForm.Height);

  // Capture the entire window
  Rectangle captureRect = new Rectangle(0, 0, captureForm.Width, captureForm.Height);

  m_liveRoom.startScreenPreview(rendForm.Handle, captureForm.Handle, renderRect, captureRect);
  ```

### 16. stopScreenPreview

-  Definition: void stopScreenPreview()

-  Description: Disables screen sharing

-  Example:

  ```c#
  m_liveRoom.stopScreenPreview();
  ```

### 17. addRemoteView

-  Definition: void addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID)

-  Description: Plays videos of other VJs in the room

-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview window. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |
| userID | string | User ID |

-  Example:

  ```c#
  // Render in the entire form window
  Rectangle renderRect = new Rectangle(0, 0, form.Width, form.Height);

  // Enable playback of users' audios/videos
  m_liveRoom.addRemoteView(form.Handle,rect, userID);
  ```

### 18. updateRemotePreview

-  Definition: void updateRemotePreview(IntPtr rendHwnd, Rectangle rect, string userID)
-  Description: Resets the video preview area of the specified userID. When the size of the window identified by the specified local HWND changes, you can resize the video rendering area using this function.
-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview window. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |
| userID | string | User ID |

-  Example:

```c#
  // Render in the entire form window
  Rectangle renderRect = new Rectangle(0, 0, form.Width, form.Height);

  // Reset the video preview area of the specified userID
  m_liveRoom.updateRemotePreview(form.Handle, rect, userID);
```

### 18. removeRemoteView

-  Definition: void removeRemoteView(string userID)

-  Description: Stops playing videos of other VJs

-  Parameters:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| userID | string | User ID |

-  Example:

  ```c#
  m_liveRoom.removeRemoteView(userID);
  ```

### 19. setMute

-  Definition: void setMute(bool mute)

-  Description: Enables Mute

-  Parameter:

| Parameter | Type | Description |
| ---- | ---- | ---- |
| mute | bool | Indicates whether to enable Mute |

-  Example:

  ```c#
  m_liveRoom.setMute(true); // Set to mute
  ```

### 20. setVideoQuality

-  Definition: void setVideoQuality(LiveVideoQuality quality, LiveAspectRatio ratio)

- Description: Sets the pushed video quality

-  Parameters:

| Parameter | Type | Description |
| ------- | ---------------- | ---------------------------------------- |
| quality | LiveVideoQuality | Image quality. See LiveVideoQuality's enumerated values defined in LiveRoomUtil.h |
| ratio | LiveAspectRatio | Aspect ratio. See LiveAspectRatio's enumerated values defined in LiveRoomUtil.h |

-  Example:

  ```c#
  // Set the image quality to HD and the aspect ratio to 4:3
  m_liveRoom.setVideoQuality(LIVEROOM_VIDEO_QUALITY_HIGH_DEFINITION, LIVEROOM_ASPECT_RATIO_4_3);
  ```

### 21. setBeautyStyle

-  Definition: void setBeautyStyle(LiveBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel)

-  Description: Sets beauty filter and whitening effects

-  Parameters:

| Parameter | Type | Description |
| -------------- | -------------- | ---------------------------------------- |
| beautyStyle | TXEBeautyStyle | See LiveBeautyStyle's enumerated values defined in LiveRoomUtil.h |
| beautyLevel | int | Beauty filter level: 1-9. 0 indicates disabling beauty filter. A greater value means a bigger effect. |
| whitenessLevel | int | Whiteness level: 1-9. 0 indicates disabling whitening. A greater value means a bigger effect. |

-  Example:

  ```c#
  // Natural; beauty filter level: 5; whitening level: 5
  m_liveRoom.setBeautyStyle(TXE_BEAUTY_STYLE_NATURE, 5, 5);
  ```

### 22. requestJoinPusher

-  Definition: void requestJoinPusher()

-  Description: Joint broadcasting request from viewer

-  Example:

  ```c#
  m_liveRoom.requestJoinPusher();
  ```

### 23. acceptJoinPusher

-  Definition: void acceptJoinPusher(string userID)

-  Description: The primary VJ accepts the joint broadcasting request and informs the request initiator.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| userID | string | User ID |

-  Example:

  ```c#
  m_liveRoom.acceptJoinPusher(userID);
  ```

### 24. rejectJoinPusher

-  Definition: void rejectJoinPusher(string userID, string reason)

- Description: The primary VJ rejects the joint broadcasting request and informs the request initiator.

-  Parameters:

| Parameter | Type | Description |
| ------ | ------ | ----- |
| userID | string | User ID |
| reason | string | Reason for rejection |

-  Example:

  ```c#
  m_liveRoom.acceptJoinPusher(userID, reason);
  ```

### 25. kickoutSubPusher

-  Definition: void kickoutSubPusher(string userID)

-  Description: The primary VJ kicks out a secondary VJ.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| userID | string | User ID |

-  Example:

  ```c#
  m_liveRoom.kickoutSubPusher(userID);
  ```



## Details of ILoginLiveCallback APIs

### 1. onLogin

-  Definition: void onLogin(LiveResult res, LiveAuthData authData)

-  Description: Callback of login result

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ---------------------------------------- |
| res | LiveResult | Execution result. See LiveResult class defined in LiveRoomUtil.h |
| authData | LiveAuthData | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a success login. |

-  Example:

  ```c#
  class LoginDialog : ILoginLiveCallback
  {
  	void ILoginLiveCallback.onLogin(LiveResult res, LiveAuthData authData)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// Login failed
          }
          else
          {
          	// Login succeeded, and authData information is saved
          }
      }
  }

  // For more information on how to use callback, please see LiveRoom::login API
  ...
  ```



## Details of IGetLiveRoomListCallback APIs

### 1. onGetRoomList

-  Definition: void onGetRoomList(LiveResult res, List<LiveRoomData> rooms)

-  Description: Callback of obtaining a room list

-  Parameters:

| Parameter | Type | Description |
| ----- | ------------------ | ---------------------------------------- |
| res | LiveResult | Execution result. See LiveResult class defined in LiveRoomUtil.h |
| rooms | List<LiveRoomData> | List of room information |

-  Example:

  ```c#
  class RoomListDialog : IGetLiveRoomListCallback
  {
  	void IGetRoomListCallback.onGetRoomList(LiveResult res, List<LiveRoomData> rooms)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// Query failed
          }
          else
          {
          	// Query succeeded, process rooms data
          }
      }
  }

  // For more information on how to use callback, please see LiveRoom::getRoomList API
  ...
  ```



## Details of ILiveRoomCallback APIs

 For more information on how to set ILiveRoomCallback, please see the API LiveRoom::setCallback.

### 1. onCreateRoom

-  Definition: void onCreateRoom(LiveResult res, string roomID)

-  Description: Callback of creating a room

-  Parameters:

| Parameter | Type | Description |
| ------ | ---------- | ---------------------------------------- |
| res | LiveResult | Execution result. See LiveResult class defined in LiveRoomUtil.h |
| roomID | string | Room ID |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onCreateRoom(LiveResult res, string roomID)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// If the room fails to be created, a prompt pops up.
          }
          else
          {
          	// If the room is created successfully, the viewers can watch the LVB.
          	// Process onUpdateRoomData callback immediately
          }
      }
      
      ...
  }
  ```

### 2. onEnterRoom

-  Definition: void onEnterRoom(LiveResult res)

-  Description: Callback of entering a room

-  Parameter:

| Parameter | Type | Description |
| ---- | ---------- | ---------------------------------------- |
| res | LiveResult | Execution result. See LiveResult class defined in LiveRoomUtil.h |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onEnterRoom(LiveResult res)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// If the room fails to be entered, a prompt pops up.
          }
          else
          {
          	// If viewers enter the room successfully, process onUpdateRoomData callback immediately
          }
      }
      
      ...
  }
  ```

### 3. onUpdateRoomData

-  Definition: void onUpdateRoomData(LiveResult res, LiveRoomData roomData)

-  Description: Callback of room information change

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ---------------------------------------- |
| res | LiveResult | Execution result. See LiveResult class defined in LiveRoomUtil.h |
| roomData | LiveRoomData | Room information. See LiveRoomData class defined in LiveRoomUtil.h. |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onUpdateRoomData(LiveResult res, LiveRoomData roomData)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// If the update fails, a prompt pops up.
          }
          else
          {
          	// If the update succeeds, the appropriate processing is performed based on whether the API is triggered by createRoom or enterRoom.
          }
      }
      
      ...
  }
  ```

### 4. onGetAudienceList

-  Definition: void onGetAudienceList(LiveResult res, List<LiveAudienceData> audiences)
-  Description: Callback of viewer list query
-  Parameters:

| Parameter | Type | Description |
| --------- | ---------------------- | ---------------------------------------- |
| res | LiveResult | Execution result. See LiveResult class defined in LiveRoomUtil.h |
| audiences | List<LiveAudienceData> | Viewer information list |

-  Example:

```c#
class MainDialog : ILiveRoomCallback
{
	void ILiveRoomCallback.onGetAudienceList(LiveResult res, List<LiveAudienceData> audiences)
    {
    	if (LIVEROOM_SUCCESS != res.ec)
        {
        	// If the query fails, a prompt pops up.
        }
        else
        {
        	// If the query succeeds, the list is updated to UI.
        }
    }
    
    ...
}
```

### 5. onPusherJoin

-  Definition: void onPusherJoin(LiveMemberData member)

-  Description: Callback of joint broadcasting viewer entering the room

-  Parameter:

| Parameter | Type | Description |
| ------ | -------------- | ---------------------------------------- |
| member | LiveMemberData | Member information. See LiveMemberData class defined in LiveRoomUtil.h. |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onPusherJoin(LiveMemberData member)
      {
      	// Usually, the video and audio of the joint broadcasting viewer are turned on after he or she requests joint broadcasting.
      	m_liveRoom.addRemoteView(rendHwnd, rect, member.userID);
      	...
      }
      
      ...
  }
  ```

### 6. onPusherQuit

-  Definition: void onPusherQuit(LiveMemberData member)

-  Description: Callback of the joint broadcasting viewer exiting the room

-  Parameter:

| Parameter | Type | Description |
| ------ | -------------- | ---------------------------------------- |
| member | LiveMemberData | Member information. See LiveMemberData class defined in LiveRoomUtil.h. |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onPusherQuit(LiveMemberData member)
      {
      	// Usually, the video and audio of the joint broadcasting viewer are turned off after he or she stops joint broadcasting.
      	m_liveRoom.removeRemoteView(member.userID);
      	...
      }
      
      ...
  }
  ```

### 7. onRoomClosed

-  Definition: void onRoomClosed(string roomID)

-  Description: Callback of room dissolution

-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| roomID | string | Room ID |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRoomClosed(string roomID)
      {
      	// It prompts that the room is dismissed. The opened audio/video is closed.
      	...
      }
      
      ...
  }
  ```

### 8. onRecvRoomTextMsg

-  Definition: void onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg)

-  Description: Receives plain text messages

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------ | ------ |
| roomID | string | Room ID |
| userID | string | Sender ID |
| userName | string | Sender nickname |
| userAvatar | string | Sender profile photo |
| message | string | Text message |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg)
      {
      	// Text messages are displayed on IM panel
      }
      
      ...
  }
  ```

### 9. onRecvRoomCustomMsg

-  Definition: void onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message)

-  Description: Receives custom messages

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------ | ------- |
| roomID | string | Room ID |
| userID | string | Sender ID |
| userName | string | Sender nickname |
| userAvatar | string | Sender profile photo |
| cmd | string | Custom CMD |
| message | string | Custom message |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message)
      {
      	// Parse and process custom messages such as Likes and gifts
      }
      
      ...
  }
  ```

### 10. onError

-  Definition: void onError(LiveResult res, string userID)

-  Description: Notification of internal LiveRoom error

-  Parameters:

| Parameter | Type | Description |
| ------ | ---------- | ---------------------------------------- |
| res | LiveResult | Execution result. See LiveResult class defined in LiveRoomUtil.h |
| userID | string | User ID |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onError(LiveResult res, string userID)
      {
      	// An error message pops up. Decide whether to close LVB based on severity of errors
      }
      
      ...
  }
  ```

### 11. onRecvJoinPusherRequest

-  Definition: void onRecvJoinPusherRequest(string roomID, string userID, string userName, string userAvatar)

-  Description: Receives a joint broadcasting request

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------ | ----- |
| roomID | string | Room ID |
| userID | string | Sender ID |
| userName | string | Sender nickname |
| userAvatar | string | Sender profile photo |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvJoinPusherRequest(string roomID, string userID, string userName, string userAvatar)
      {
      	// The primary VJ receives a joint broadcasting request from a viewer.
      	// Verify the validity of roomID
      	// UI shows who initiates the request.
      	// The primary VJ selects "acceptJoinPusher" to accept or "rejectJoinPusher" to reject the request.
      }
      
      ...
  }
  ```

### 12. onRecvAcceptJoinPusher

-  Definition: void onRecvAcceptJoinPusher(string roomID, string msg)

-  Description: Receives the notification of accepting a joint broadcasting request.

-  Parameters:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| roomID | string | Room ID |
| msg | string | Message |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvAcceptJoinPusher(string roomID, string msg)
      {
      	// The viewer receives the notification of the primary VJ accepting the joint broadcasting request.
      	// Verify the validity of roomID
      	// Process msg
      }
      
      ...
  }
  ```

  ​

### 13. onRecvRejectJoinPusher

-  Definition: void onRecvRejectJoinPusher(string roomID, string msg)

-  Description: Receives the notification of rejecting a joint broadcasting request

-  Parameters:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| roomID | string | Room ID |
| msg | string | Message |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRejectJoinPusher(string roomID, string msg)
      {
      	// The viewer receives the notification of the primary VJ rejecting the joint broadcasting request.
      	// Verify the validity of roomID
      	// Process msg
      }
      
      ...
  }
  ```

  ​

### 14. onRecvKickoutSubPusher

-  Definition: void onRecvKickoutSubPusher(string roomID)

-  Description: Receives the notification of the primary VJ kicking out a secondary VJ.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| roomID | string | Room ID |

-  Example:

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRejectJoinPusher(string roomID, string msg)
      {
      	// The primary VJ kicks out a viewer invited for joint broadcasting
      	// Verify the validity of roomID
      	// Process msg
      }
      
      ...
  }
  ```

  ​
