# Real-time Audio/Video (RTCRoom) APIs (CSharp)

## RTCRoom

| Name | Description |
| ---------------------------------------- | ---------------------------------------- |
| instance() | Gets a single instance for RTCRoom and calls RTCRoom APIs via the single instance |
| setCallback(IRTCRoomCallback callback) | Sets the callback proxy for RTCRoom callback, and listens to the internal status of RTCRoom and the execution results of the API |
| login(string serverDomain, RTCAuthData authData, ILoginRTCCallback callback) | Logs in to the business server RoomService before you can normally use other APIs and the IM feature. |
| logout() | Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail. |
| getRoomList(int index, int cnt, IGetRTCRoomListCallback callback) | Gets the room list. If there are many rooms, you can get the list in pages. |
| createRoom(string roomID, string roomInfo) | Creates a room, and the new room will be added to the room list in the backend, and then the meeting initiator can start pushing. |
| enterRoom(string roomID) | Enters a room |
| leaveRoom() | Leaves the room. If the meeting initiator leaves, the room will be terminated by the backend; if other meeting participants leave, the remaining participants can continue chatting. |
| sendRoomTextMsg(string msg) | Sends plain text messages, such as sending on-screen comments in the room. |
| sendRoomCustomMsg(string cmd, string msg) | Sends custom messages, such as giving a "Like", or flower in the room. |
| startLocalPreview(IntPtr rendHwnd, Rectangle rect) | Enables the default camera preview |
| updateLocalPreview(IntPtr rendHwnd, Rectangle rect) | Resets the camera preview area. When the size of the specified local HWND window changes, the video rendering area can be rescaled via this function. |
| stopLocalPreview() | Disables camera preview |
| startScreenPreview(IntPtr rendHwnd, IntPtr captureHwnd, Rectangle renderRect, Rectangle captureRect) | Enables screen sharing |
| stopScreenPreview() | Disables screen sharing |
| addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID) | Plays videos of other meeting participants in the room |
| updateRemotePreview(IntPtr rendHwnd, Rectangle rect, string userID) | Resets the video preview area of the specified userID. When the size of the specified local HWND window changes, the video rendering area can be rescaled via this function. |
| removeRemoteView(string userID) | Stops playing videos of other meeting participants |
| setMute(bool mute) | Enables Mute |
| setBeautyStyle(RTCBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel) | Sets beauty filter and whitening effects |

## ILoginRTCCallback

| Name | Description |
| ---------------------------------------- | ------------ |
| onLogin(RTCResult res, RTCAuthData authData) | Callback of the login result |

## IGetRTCRoomListCallback

| Name | Description |
| ---------------------------------------- | --------- |
| onGetRoomList(RTCResult res, List<RTCRoomData> rooms) | Callback of obtaining a room list |

## IRTCRoomCallback

| Name | Description |
| ---------------------------------------- | ---------------- |
| onCreateRoom(RTCResult res, string roomID) | Callback of creating a room |
| onEnterRoom(RTCResult res) | Callback of entering a room |
| onUpdateRoomData(RTCResult res, RTCRoomData roomData) | Callback of room information change |
| onPusherJoin(RTCMemberData member) | Callback of members entering a room |
| onPusherQuit(RTCMemberData member) | Callback of members exiting a room |
| onRoomClosed(string roomID) | Callback of room dissolution |
| onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg) | Receives plain text messages |
| onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message) | Receives custom messages |
| onError(RTCResult res, string userID | Notification of internal RTCRoom error |

## Details of RTCRoom object APIs

### 1. instance

-  Definition: static RTCRoom instance()

-  Description: Gets a single instance for RTCRoom and calls RTCRoom APIs via the single instance

-  Example:

  ```c#
  RTCRoom mRTCRoom = RTCRoom.instance();
  ```

### 2. setCallback

-  Definition: void setCallback(IRTCRoomCallback callback)

-  Description: Sets the callback proxy for RTCRoom callback, and listens to the internal status of RTCRoom and the execution results of the API

- Parameter:

| Parameter | Type | Description |
| -------- | ---------------- | ---------------------- |
| callback | IRTCRoomCallback | API of IRTCRoomCallback type |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
      void IRTCRoomCallback.onCreateRoom(RTCResult res, string roomID){}
      void IRTCRoomCallback.onEnterRoom(RTCResult res){}
      void IRTCRoomCallback.onUpdateRoomData(RTCResult res, RTCRoomData roomData){}
      ...
  };

  MainDialog::MainDialog()
  {
      mRTCRoom.setCallback(this);	//Set callback
  }

  ...
  ```

  ​

### 3. login

-  Definition: void login(string serverDomain, RTCAuthData authData, ILoginRTCCallback callback)

-  Description: Logs in to the business server RoomService before you can normally use other APIs and the IM feature

-  Parameters:

| Parameter | Type | Description |
| ------------ | ----------------- | ---------------------------------------- |
| serverDomain | string | URL of RoomService. In consideration of security, it is recommended to access the https encrypted link. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| authData | RTCAuthData | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a success login. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| callback | ILoginRTCCallback | API of ILoginRTCCallback type, used to call back the login result |

-  Example:

  ```c#
  string serverDomain = "https://roomtest.qcloud.com/weapp/double_room";

  m_authData.sdkAppID = sdkAppID;
  m_authData.accountType = accountType;
  m_authData.userID = userID;
  m_authData.userSig = userSig;
  m_authData.userName = userName;
  m_authData.userAvatar = userAvatar;
  m_authData.token = token;

  // This class implements the ILoginCallback API to obtain login results
  mRTCRoom.login(serverDomain, m_authData, this);
  ```

### 4. logout

-  Definition: void logout()

-  Description: Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail.

-  Example:

  ```c#
  mRTCRoom.logout();
  ```

### 5. getRoomList

-  Definition: void getRoomList(int index, int count, IGetRTCRoomListCallback callback)

-  Description: Gets the room list. If there are many rooms, you can get the list in pages.

-  Parameters:

| Parameter | Type | Description |
| -------- | ----------------------- | ---------------------------------------- |
| index | int | Gets the list in pages. The default value can be 0, and for the subsequent retrieval, the value can be set as the starting room index (for example, set index=0 and cnt=5 for the first retrieval, and set index=5 for the second page). |
| count | int | The maximum number of rooms returned per call; 0 indicates all rooms that meet the conditions |
| callback | IGetRTCRoomListCallback | API of IGetRTCRoomListCallback type, used to call back the query result |

-  Example:

  ```c#
  // Start from index=0. A maximum of 20 rooms can be queried. This class implements the IGetRoomListCallback API to obtain query results
  mRTCRoom.getRoomList(0, 20, this);
  ```

### 6. createRoom

-  Definition: void createRoom(string roomID, string roomInfo)

-  Description: Creates a room, and the new room will be added to the room list in the backend, and then the meeting initiator can start pushing.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------ | ---------------------------------------- |
| roomID | string | Room ID. If an empty string is specified, a roomID is assigned to you. Otherwise, the specified roomID is used as the ID of this room. |
| roomInfo | string | Custom data. This field is included in the room information. It is recommended that you define roomInfo in json format, which is highly extensible. |

-  Example:

  ```c#
  // A roomID is assigned to you
  mRTCRoom.createRoom("", "{\"roomName\": \"My first room\"}");
  ```

### 7. enterRoom

-  Definition: void enterRoom(string roomID)

-  Description: Enters a room.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ---------------------------------------- |
| roomID | string | roomID - the ID of the room to be entered, which is obtained in the room list returned by the getRoomList API |

-  Example:

  ```c#
  mRTCRoom.enterRoom(roomID);
  ```

### 8. leaveRoom

-  Definition: void leaveRoom()

-  Description: Leaves the room. If the meeting initiator leaves, the room will be terminated by the backend; if other meeting participants leave, the remaining participants can continue chatting.

-  Example:

  ```c#
  mRTCRoom.leaveRoom();
  ```

### 9. sendRoomTextMsg

-  Definition: void sendRoomTextMsg(string msg)

-  Description: Sends plain text messages

-  Parameters:

| Parameter | Type | Description |
| ---- | ------ | ---- |
| msg | string | Text messages |

-  Example:

  ```c#
  mRTCRoom.sendRoomTextMsg("Hello RTCRoom");
  ```

### 10. sendRoomCustomMsg

-  Definition: void sendRoomCustomMsg(string cmd, string msg)

-  Description: Sends custom messages

-  Parameters:

| Parameter | Type | Description |
| ---- | ------ | ------------------ |
| cmd | string | Custom CMD, jointly determined by the sender and receiver |
| msg | string | Custom messages |

-  Example:

  ```c#
  // Assume that the CMD determined by the sender and receiver includes Smile and Anger
  mRTCRoom.sendRoomCustomMsg("Anger", "I am hungry");
  ```

### 11. startLocalPreview

-  Definition: void startLocalPreview(IntPtr rendHwnd, Rectangle rect)

-  Description: Enables the default camera preview
-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c#
  mRTCRoom.startLocalPreview(panel_main.Handle, new Rectangle(0, 0, panel_main.Width, panel_main.Height));
  ```

### 12. updateLocalPreview

-  Definition: void updateLocalPreview(IntPtr rendHwnd, Rectangle rect)

-  Description: Resets the preview area for camera. When the size of the window identified by the specified HWND changes, you can resize the video rendering area using this function.

-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c#
  mRTCRoom.updateLocalPreview(panel_main.Handle, new Rectangle(0, 0, panel_main.Width, panel_main.Height));
  ```

### 13. stopLocalPreview

-  Definition: void stopLocalPreview()

-  Description: Disables camera preview

-  Example:

  ```c#
  mRTCRoom.stopLocalPreview();
  ```

### 14. startScreenPreview

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
  mRTCRoom.startScreenPreview(panel_main.Handle, null, new Rectangle(0, 0, panel_main.Width, panel_main.Height), null);
  ```

### 15. stopScreenPreview

-  Definition: void stopScreenPreview()

-  Description: Disables screen sharing

-  Example:

  ```c#
  mRTCRoom.stopScreenPreview();
  ```

### 16. addRemoteView

-  Definition: void addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID)

-  Description: Plays videos of other meeting participants in the room

-  Parameters:

| Parameter | Type | Description |
| -------- | --------- | ------------------- |
| rendHwnd | IntPtr | HWND that identifies the preview window. |
| rect | Rectangle | Specifies the rendering area of the video image on the window identified by HWND. |
| userID | string | User ID |

-  Example:

  ```c#
  // Enable playback of users' audios/videos
  mRTCRoom.addRemoteView(panel_display.Handle, new Rectangle(0, 0, panel_display.Width, panel_display.Height), userID);
  ```

### 17. updateRemotePreview

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
  // Update playback of users' audios/videos
  mRTCRoom.updateRemotePreview(panel_display.Handle, new Rectangle(0, 0, panel_display.Width, panel_display.Height), userID);
  ```

### 18. removeRemoteView

-  Definition: void removeRemoteView(string userID)

-  Description: Stops playing videos of other meeting participants

-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| userID | string | User ID |

-  Example:

  ```c#
  mRTCRoom.removeRemoteView(userID);
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
  mRTCRoom.setMute(true); // Set to mute
  ```

### 20. setBeautyStyle

-  Definition: void setBeautyStyle(RTCBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel)

-  Description: Sets beauty filter and whitening effects

-  Parameters:

| Parameter | Type | Description |
| -------------- | -------------- | ---------------------------------------- |
| beautyStyle | RTCBeautyStyle | See RTCBeautyStyle's enumerated values defined in RTCRoomUtil.cs |
| beautyLevel | int | Beauty filter level: 1-9. 0 indicates disabling beauty filter. A greater value means a bigger effect. |
| whitenessLevel | int | Whiteness level: 1-9. 0 indicates disabling whitening. A greater value means a bigger effect. |

-  Example:

  ```c#
  // Natural; beauty filter level: 5; whitening level: 5
  mRTCRoom.setBeautyStyle(RTCBeautyStyle.RTCROOM_BEAUTY_STYLE_NATURE, 5, 5);
  ```

## Details of ILoginRTCCallback APIs

### 1. onLogin

-  Definition: void onLogin(RTCResult res, RTCAuthData authData)

-  Description: Callback of login result
-  Parameters:

| Parameter | Type | Description |
| -------- | ----------- | ---------------------------------------- |
| res | RTCResult | Execution result. See RTCResult class defined in RTCRoomUtil.cs |
| authData | RTCAuthData | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a success login. |

-  Example:

  ```c#
  class LoginDialog : ILoginRTCCallback
  {
  	void onLogin(RTCResult res, RTCAuthData authData)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
          {
          	// Login failed
          }
          else
          {
          	// Login succeeded, and authData information is saved
          }
      }
  }

  // For more information on how to use callback, please see the API RTCRoom.login.
  ...
  ```



## Details of IGetRTCRoomListCallback APIs

### 1. onGetRoomList

-  Definition: void onGetRoomList(RTCResult res, List<RTCRoomData> rooms)

-  Description: Callback of obtaining a room list

-  Parameters:

| Parameter | Type | Description |
| ----- | ----------------- | --------------------------------------- |
| res | RTCResult | Execution result. See RTCResult class defined in RTCRoomUtil.cs |
| rooms | List<RTCRoomData> | List of room information |

-  Example:

  ```c#
  class RoomListDialog : IGetRTCRoomListCallback
  {
  	void onGetRoomList(RTCResult res, List<RTCRoomData> rooms)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
          {
          	// Query failed
          }
          else
          {
          	// Query succeeded, process rooms data
          }
      }
  }

  // For more information on how to use callback, please see the API RTCRoom.getRoomList.
  ...
  ```



## Details of IRTCRoomCallback APIs

 For more information on how to set IRTCRoomCallback, please see the API RTCRoom.setCallback.

### 1. onCreateRoom

-  Definition: void onCreateRoom(RTCResult res, string roomID)

-  Description: Callback of creating a room

-  Parameters:

| Parameter | Type | Description |
| ------ | --------- | --------------------------------------- |
| res | RTCResult | Execution result. See RTCResult class defined in RTCRoomUtil.cs |
| roomID | string | Room ID |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onCreateRoom(RTCResult res, string roomID)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
          {
          	// If the room fails to be created, a prompt pops up.
          }
          else
          {
          	// If the room is created successfully, other audiences can participate in the meeting.
          	// Process onUpdateRoomData callback immediately
          }
      }
      
      ...
  }
  ```

### 2. onEnterRoom

-  Definition: void onEnterRoom(RTCResult res)

-  Description: Callback of entering a room

-  Parameter:

| Parameter | Type | Description |
| ---- | --------- | --------------------------------------- |
| res | RTCResult | Execution result. See RTCResult class defined in RTCRoomUtil.cs |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onEnterRoom(RTCResult res)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
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

-  Definition: void onUpdateRoomData(RTCResult res, RTCRoomData roomData)

-  Description: Callback of room information change

-  Parameters:

| Parameter | Type | Description |
| -------- | ----------- | ---------------------------------------- |
| res | RTCResult | Execution result. See RTCResult class defined in RTCRoomUtil.cs |
| roomData | RTCRoomData | Room information. See RTCRoomData class defined in RTCRoomUtil.cs |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onUpdateRoomData(RTCResult res, RTCRoomData roomData)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
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

### 4. onPusherJoin

-  Definition: void onPusherJoin(RTCMemberData member)

-  Description: Callback of members entering a room

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------- | ---------------------------------------- |
| member | RTCMemberData | Member information. See the RTCMemberData class defined in RTCRoomUtil.cs. |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onPusherJoin(RTCMemberData member)
      {
      	// A member enters a room and enables his/her camera and microphone.
      	this.BeginInvoke(new Action(() =>
          {
      		mRTCRoom.addRemoteView(panel_display.Handle, new Rectangle(0, 0, panel_display.Width, panel_display.Height), userID);
      	...
      	}));
      }
      
      ...
  }
  ```

### 5. onPusherQuit

-  Definition: void onPusherQuit(RTCMemberData member)

-  Description: Callback of members exiting the room

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------- | ---------------------------------------- |
| member | RTCMemberData | Member information. See the RTCMemberData class defined in RTCRoomUtil.cs. |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onPusherQuit(RTCMemberData member)
      {
      	// A member exits the room and disables his/her camera and microphone.
      	this.BeginInvoke(new Action(() =>
          {
      		mRTCRoom.removeRemoteView(member.userID);
      	...
      	}));
      	...
      }
      
      ...
  }
  ```

### 6. onRoomClosed

-  Definition: void onRoomClosed(string roomID)

-  Description: Callback of room dissolution

-  Parameter:

| Parameter | Type | Description |
| ------ | ------ | ---- |
| roomID | string | Room ID |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onRoomClosed(string roomID)
      {
      	// It prompts that the room is dismissed. The opened audio/video is closed.
      	...
      }
      
      ...
  }
  ```

### 7. onRecvRoomTextMsg

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
  class MainDialog : IRTCRoomCallback
  {
  	void onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg)
      {
      	// Text messages are displayed on IM panel
      }
      
      ...
  }
  ```

### 8. onRecvRoomCustomMsg

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
  class MainDialog : IRTCRoomCallback
  {
  	void onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message)
      {
      	// Parse and process custom messages such as Likes and gifts
      }
      
      ...
  }
  ```

### 9. onError

-  Definition: void onError(RTCResult res, string userID)

-  Description: Notification of internal RTCRoom error

-  Parameters:

| Parameter | Type | Description |
| ------ | --------- | --------------------------------------- |
| res | RTCResult | Execution result. See RTCResult class defined in RTCRoomUtil.cs |
| userID | string | User ID |

-  Example:

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onError(RTCResult res, string userID)
      {
      	// An error message pops up. Decide whether to dismiss or exit the meeting based on severity of errors.
      }
      
      ...
  }
  ```

