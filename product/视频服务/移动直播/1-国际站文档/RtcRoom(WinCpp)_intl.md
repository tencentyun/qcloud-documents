# Real-time Audio/Video (RTCRoom) APIs (C++)

## RTCRoom

| Name | Description |
| ---------------------------------------- | ---------------------------------------- |
| instance() | Gets a single instance for RTCRoom and calls RTCRoom APIs via the single instance |
| setCallback(IRTCRoomCallback * callback) | Sets the callback proxy for RTCRoom callback, and listens to the internal status of RTCRoom and the execution results of the API |
| login(const std::string & serverDomain, const RTCAuthData & authData, ILoginRTCCallback* callback) | Logs in to the business server RoomService before you can normally use other APIs and the IM feature |
| logout() | Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail. |
| getRoomList(int index, int count, IGetRTCRoomListCallback* callback) | Gets the room list. If there are many rooms, you can get the list in pages. |
| createRoom(const std::string& roomID, const std::string& roomInfo) | Creates a room, and the new room will be added to the room list in the backend, and then the meeting initiator can start pushing. |
| enterRoom(const std::string& roomID, HWND rendHwnd, const RECT & rect) | Enters a room |
| leaveRoom() | Leaves the room. If the meeting initiator leaves, the room will be terminated by the backend; if other meeting participants leave, the remaining participants can continue chatting. |
| sendRoomTextMsg(const char * msg) | Sends plain text messages |
| sendRoomCustomMsg(const char * cmd, const char * msg) | Sends custom messages |
| startLocalPreview(HWND rendHwnd, const RECT & rect) | Enables the default camera preview |
| updateLocalPreview(HWND rendHwnd, const RECT &rect) | Resets the preview area for camera. When the size of the window identified by the specified local HWND changes, you can resize the video rendering area using this function. |
| stopLocalPreview() | Disables camera preview |
| startScreenPreview(HWND rendHwnd, HWND captureHwnd, const RECT & renderRect, const RECT & captureRect) | Enables screen sharing |
| stopScreenPreview() | Disables screen sharing |
| addRemoteView(HWND rendHwnd, const RECT & rect, const char * userID) | Plays videos of other meeting participants in the room |
| updateRemotePreview(HWND rendHwnd, const RECT &rect, const char * userID) | Resets the video preview area of the specified userID. When the size of the window identified by the specified local HWND changes, you can resize the video rendering area using this function. |
| removeRemoteView(const char * userID) | Stops playing videos of other meeting participants |
| setMute(bool mute) | Enables Mute |
| setBeautyStyle(TXEBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel) | Sets beauty filter and whitening effects |

## ILoginRTCCallback

| Name | Description |
| ---------------------------------------- | ------------ |
| onLogin(const RTCResult& res, const RTCAuthData& authData) | Callback of login result |

## IGetRTCRoomListCallback

| Name | Description |
| ---------------------------------------- | --------- |
| onGetRoomList(const RTCResult& res, const std::vector<RTCRoomData>& rooms) | Callback of obtaining a room list |

## IRTCRoomCallback

| Name | Description |
| ---------------------------------------- | ---------------- |
| onCreateRoom(const RTCResult& res, const std::string& roomID) | Callback of creating a room |
| onEnterRoom(const RTCResult& res) | Callback of entering a room |
| onUpdateRoomData(const RTCResult& res, const RTCRoomData& roomData) | Callback of room information change |
| onPusherJoin(const RTCMemberData& member) | Callback of members entering a room |
| void onPusherQuit(const RTCMemberData& member) | Callback of members exiting a room |
| onRoomClosed(const std::string& roomID) | Callback of room dissolution |
| onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg) | Receives plain text messages |
| onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message) | Receives custom messages |
| onError(const RTCResult& res, const std::string& userID) | Notification of internal RTCRoom error |

## Details of RTCRoom object APIs

### 1. instance

-  Definition: static RTCRoom* instance()

-  Description: Gets a single instance for RTCRoom and calls RTCRoom APIs via the single instance

-  Example:

  ```c++
  RTCRoom* m_RTCRoom = NULL;
  m_RTCRoom = RTCRoom::instance();
  ```

### 2. setCallback

-  Definition: void setCallback(IRTCRoomCallback * callback)

-  Description: Sets the callback proxy for RTCRoom callback, and listens to the internal status of RTCRoom and the execution results of the API

-  Parameter:

| Parameter | Type | Description |
| -------- | ------------------ | ------------------------ |
| callback | IRTCRoomCallback * | Proxy pointer of IRTCRoomCallback type |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
      MainDialog();
      virtual ~MainDialog();
      
      virtual void onCreateRoom(const RTCResult& res, const std::string& roomID);
      virtual void onEnterRoom(const RTCResult& res);
      virtual void onUpdateRoomData(const RTCResult& res, const LRRoomData& roomData);
      ...
  };

  MainDialog::MainDialog()
  {
      m_RTCRoom->setCallback(this);	//Set callback
  }

  ...
  ```

  ​

### 3. login

-  Definition: void login(const std::string & serverDomain, const RTCAuthData & authData, ILoginRTCCallback* callback)

-  Description: Logs in to the business server RoomService before you can normally use other APIs and the IM feature

-  Parameters:

| Parameter | Type | Description |
| ------------ | ------------------- | ---------------------------------------- |
| serverDomain | const std::string & | URL of RoomService. In consideration of security, it is recommended to access the https encrypted link. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| authData | const RTCAuthData & | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a success login. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| callback | ILoginRTCCallback* | Proxy pointer of ILoginRTCCallback type, used to call back the login result |

-  Example:

  ```c++
  std::string serverDomain = "https://roomtest.qcloud.com/weapp/double_room";

  m_authData.sdkAppID = sdkAppID;
  m_authData.accountType = accountType;
  m_authData.userID = userID;
  m_authData.userSig = userSig;
  m_authData.userName = userName;
  m_authData.userAvatar = userAvatar;
  m_authData.token = token;

  // This class implements the ILoginCallback API to obtain login results
  m_RTCRoom->login(serverDomain, m_authData, this);
  ```

### 4. logout

-  Definition: void logout();

-  Description: Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail.

-  Example:

  ```c++
  m_RTCRoom->logout();
  ```

### 5. getRoomList

-  Definition: void getRoomList(int index, int count, IGetRTCRoomListCallback* callback)

-  Description: Gets the room list. If there are many rooms, you can get the list in pages.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------------ | ---------------------------------------- |
| index | int | Gets the list in pages. The default value can be 0, and for the subsequent retrieval, the value can be set as the starting room index (for example, set index=0 and cnt=5 for the first retrieval, and set index=5 for the second page). |
| count | int | The maximum number of rooms returned per call; 0 indicates all rooms that meet the conditions |
| callback | IGetRTCRoomListCallback* | Proxy pointer of IGetRTCRoomListCallback type, used to call back the query result |

-  Example:

  ```c++
  // Start from index=0. A maximum of 20 rooms can be queried. This class implements the IGetRoomListCallback API to obtain query results
  m_RTCRoom->getRoomList(0, 20, this);
  ```

### 6. createRoom

-  Definition: void createRoom(const std::string& roomID, const std::string& roomInfo)

-  Description: Creates a room, and the new room will be added to the room list in the backend, and then the meeting initiator can start pushing.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------ | ---------------------------------------- |
| roomID | const std::string& | Room ID. If an empty string is specified, a roomID is assigned to you. Otherwise, the specified roomID is used as the ID of this room. |
| roomInfo | const std::string& | Custom data. This field is included in the room information. It is recommended that you define roomInfo in json format, which is highly extensible. |

-  Example:

  ```c++
  // A roomID is assigned to you
  m_RTCRoom->createRoom("", "{\"roomName\": \"My first room\"}");
  ```

### 7. enterRoom

-  Definition: void enterRoom(const std::string& roomID)

-  Description: Enters a room.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | ---------------------------------------- |
| roomID | const std::string& | roomID - the ID of the room to be entered, which is obtained in the room list returned by the getRoomList API |

-  Example:

  ```c++
  m_RTCRoom->enterRoom(roomID);
  ```

### 8. leaveRoom

-  Definition: void leaveRoom()

-  Description: Leaves the room. If the meeting initiator leaves, the room will be terminated by the backend; if other meeting participants leave, the remaining participants can continue chatting.

-  Example:

  ```c++
  m_RTCRoom->leaveRoom();
  ```

### 9. sendRoomTextMsg

-  Definition: void sendRoomTextMsg(const char * msg)

-  Description: Sends plain text messages

-  Parameter:

| Parameter | Type | Description |
| ---- | ------------ | ---- |
| msg | const char * | Text message |

-  Example:

  ```c++
  m_RTCRoom->sendRoomTextMsg("Hello RTCRoom");
  ```

### 10. sendRoomCustomMsg

-  Definition: void sendRoomCustomMsg(const char * cmd, const char * msg)

-  Description: Sends custom messages

-  Parameters:

| Parameter | Type | Description |
| ---- | ------------ | ------------------ |
| cmd | const char * | Custom cmd, jointly determined by the sender and receiver |
| msg | const char * | Custom message |

-  Example:

  ```c++
  // Assume that the cmd determined by the sender and receiver includes Smile and Anger
  m_RTCRoom->sendRoomCustomMsg("Smile", "I am hungry");
  ```

### 11. startLocalPreview

-  Definition: void startLocalPreview(HWND rendHwnd, const RECT & rect)

-  Description: Enables the default camera preview

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ---------------------------------------- |
| rendHwnd | HWND | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = null, there is no need to preview the video. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window
  m_RTCRoom->startLocalPreview(hwnd, rect);
  ```

### 12. updateLocalPreview

-  Definition: void updateLocalPreview(HWND rendHwnd, const RECT &rect)

-  Description: Resets the preview area for camera. When the size of the window identified by the specified HWND changes, you can resize the video rendering area using this function.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ---------------------------------------- |
| rendHwnd | HWND | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window
  m_RTCRoom->updateLocalPreview(hwnd, rect);
  ```

### 13. stopLocalPreview

-  Definition: void stopLocalPreview()

-  Description: Disables camera preview

-  Example:

  ```c++
  m_RTCRoom->stopLocalPreview();
  ```

### 14. startScreenPreview

-  Definition: bool startScreenPreview(HWND rendHwnd, HWND captureHwnd, const RECT & renderRect, const RECT & captureRect)

-  Description: Enables screen sharing

-  Parameters:

| Parameter | Type | Description |
| ----------- | ------------ | ---------------------------------------- |
| rendHwnd | HWND | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| captureHwnd | HWND | Specifies the capture window. If it is NULL, captureRect does not work and the entire screen is captured; if it is not NULL, the current window is captured. |
| renderRect | const RECT & | Specifies the rendering area of the video screen on rendHwnd |
| captureRect | const RECT & | Specifies the customer area of the capture window |

-  Returned value: Success or Failed

-  Example:

  ```c++
  RECT renderRect = { 0 };
  ::GetClientRect(rendHwnd, &renderRect);	// Render in the entire HWND window

  RECT captureRect = { 0 };
  ::GetClientRect(captureHwnd, &captureRect);	// Capture the entire window

  m_RTCRoom->startScreenPreview(rendHwnd, captureHwnd, renderRect, captureRect);
  ```

### 15. stopScreenPreview

-  Definition: void stopScreenPreview()

-  Description: Disables screen sharing

-  Example:

  ```c++
  m_RTCRoom->stopScreenPreview();
  ```

### 16. addRemoteView

-  Definition: void addRemoteView(HWND rendHwnd, const RECT & rect, const char * userID)

-  Description: Plays videos of other meeting participants in the room

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ------------------- |
| rendHwnd | HWND | The HWND that identifies the preview window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |
| userID | const char * | User ID |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window

  // Enable playback of users' audios/videos
  m_RTCRoom->addRemoteView(hwnd, rect, userID);
  ```

### 17. updateRemotePreview

-  Definition: void updateRemotePreview(HWND rendHwnd, const RECT &rect, const char * userID)
-  Description: Resets the video preview area of the specified userID. When the size of the window identified by the specified local HWND changes, you can resize the video rendering area using this function.
-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ------------------- |
| rendHwnd | HWND | The HWND that identifies the preview window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |
| userID | const char * | User ID |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window

  // Update playback of users' audios/videos
  m_RTCRoom->updateRemotePreview(hwnd, rect, userID);
  ```

### 18. removeRemoteView

-  Definition: void removeRemoteView(const char * userID)

-  Description: Stops playing videos of other meeting participants

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------ | ---- |
| userID | const char * | User ID |

-  Example:

  ```c++
  m_RTCRoom->removeRemoteView(userID);
  ```

### 19. setMute

-  Definition: void setMute(bool mute)

-  Description: Enables Mute

-  Parameter:

| Parameter | Type | Description |
| ---- | ---- | ---- |
| mute | bool | Indicates whether to enable Mute |

-  Example:

  ```c++
  m_RTCRoom->setMute(true); // Set to mute
  ```

### 20. setBeautyStyle

-  Definition: void setBeautyStyle(TXEBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel)

-  Description: Sets beauty filter and whitening effects

-  Parameters:

| Parameter | Type | Description |
| -------------- | -------------- | ---------------------------------------- |
| beautyStyle | TXEBeautyStyle | See RTCBeautyStyle's enumerated values defined in RTCRoomUtil.h |
| beautyLevel | int | Beauty filter level: 1-9. 0 indicates disabling beauty filter. A greater value means a bigger effect. |
| whitenessLevel | int | Whiteness level: 1-9. 0 indicates disabling whitening. A greater value means a bigger effect. |

-  Example:

  ```c++
  // Natural; beauty filter level: 5; whitening level: 5
  m_RTCRoom->setBeautyStyle(TXE_BEAUTY_STYLE_NATURE, 5, 5);
  ```

## Details of ILoginRTCCallback APIs

### 1. onLogin

-  Definition: virtual void onLogin(const RTCResult& res, const RTCAuthData& authData)

-  Description: Callback of login result

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------ | ---------------------------------------- |
| res | const RTCResult& | Execution result. See RTCResult structure defined in RTCRoomUtil.h |
| authData | const RTCAuthData& | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a success login. |

-  Example:

  ```c++
  class LoginDialog : public ILoginRTCCallback
  {
  public:
  	virtual void onLogin(const RTCResult& res, const RTCAuthData& authData)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// Login failed
          }
          else
          {
          	// Login succeeded, and authData information is saved
          }
      }
  };

  // For more information on how to use callback, please see the API RTCRoom::login
  ...
  ```



## Details of IGetRTCRoomListCallback APIs

### 1. onGetRoomList

-  Definition: virtual void onGetRoomList(const RTCResult& res, const std::vector<RTCRoomData>& rooms)

-  Description: Callback of obtaining a room list

-  Parameters:

| Parameter | Type | Description |
| ----- | ------------------------------- | ---------------------------------------- |
| res | const RTCResult& | Execution result. See RTCResult structure defined in RTCRoomUtil.h |
| rooms | const std::vector<RTCRoomData>& | List of room information |

-  Example:

  ```c++
  class RoomListDialog : public IGetRTCRoomListCallback
  {
  public:
  	virtual void onGetRoomList(const RTCResult& res, const std::vector<RTCRoomData>& rooms)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// Query failed
          }
          else
          {
          	// Query succeeded, process rooms data
          }
      }
  };

  // For more information on how to use callback, please see the API RTCRoom::getRoomList
  ...
  ```



## Details of IRTCRoomCallback APIs

 For more information on how to set IRTCRoomCallback, please see the API RTCRoom::setCallback.

### 1. onCreateRoom

-  Definition: virtual void onCreateRoom(const RTCResult& res, const std::string& roomID)

-  Description: Callback of creating a room

-  Parameters:

| Parameter | Type | Description |
| ------ | ------------------ | ---------------------------------------- |
| res | const RTCResult& | Execution result. See RTCResult structure defined in RTCRoomUtil.h |
| roomID | const std::string& | Room ID |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onCreateRoom(const RTCResult& res, const std::string& roomID)
      {
      	if (RTCROOM_SUCCESS != res.ec)
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
  };
  ```

### 2. onEnterRoom

-  Definition: virtual void onEnterRoom(const RTCResult& res)

-  Description: Callback of entering a room

-  Parameter:

| Parameter | Type | Description |
| ---- | ---------------- | ---------------------------------------- |
| res | const RTCResult& | Execution result. See RTCResult structure defined in RTCRoomUtil.h |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onEnterRoom(const RTCResult& res)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// If the room fails to be entered, a prompt pops up.
          }
          else
          {
          	// If viewers enter the room successfully, process onUpdateRoomData callback immediately
          }
      }
      
      ...
  };
  ```

### 3. onUpdateRoomData

-  Definition: virtual void onUpdateRoomData(const RTCResult& res, const RTCRoomData& roomData)

-  Description: Callback of room information change

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------ | ---------------------------------------- |
| res | const RTCResult& | Execution result. See RTCResult structure defined in RTCRoomUtil.h |
| roomData | const RTCRoomData& | Room information. See RTCRoomData structure defined in RTCRoomUtil.h |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onUpdateRoomData(const RTCResult& res, const RTCRoomData& roomData)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// If the update fails, a prompt pops up.
          }
          else
          {
          	// If the update succeeds, the appropriate processing is performed based on whether the API is triggered by createRoom or enterRoom.
          }
      }
      
      ...
  };
  ```

### 4. onPusherJoin

-  Definition: virtual void onPusherJoin(const RTCMemberData& member)

-  Description: Callback of members entering a room

-  Parameter:

| Parameter | Type | Description |
| ------ | -------------------- | ---------------------------------------- |
| member | const RTCMemberData& | Member information. See the RTCMemberData structure defined in RTCRoomUtil.h. |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onPusherJoin(const RTCMemberData& member)
      {
      	// A member enters a room and enables his/her camera and microphone.
      	m_RTCRoom->addRemoteView(rendHwnd, rect, member.userID);
      	...
      }
      
      ...
  };
  ```

### 5. onPusherQuit

-  Definition: virtual void onPusherQuit(const RTCMemberData& member)

-  Description: Callback of members exiting the room

-  Parameter:

| Parameter | Type | Description |
| ------ | -------------------- | ---------------------------------------- |
| member | const RTCMemberData& | Member information. See the RTCMemberData structure defined in RTCRoomUtil.h. |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onPusherQuit(const RTCMemberData& member)
      {
      	// A member exits the room and disables his/her camera and microphone.
      	m_RTCRoom->removeRemoteView(member.userID);
      	...
      }
      
      ...
  };
  ```

### 6. onRoomClosed

-  Definition: virtual void onRoomClosed(const std::string& roomID)

-  Description: Callback of room dissolution

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | ---- |
| roomID | const std::string& | Room ID |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onRoomClosed(const std::string& roomID)
      {
      	// It prompts that the room is dismissed. The opened audio/video is closed.
      	...
      }
      
      ...
  };
  ```

### 7. onRecvRoomTextMsg

-  Definition: virtual void onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg)

-  Description: Receives plain text messages

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------------ | ------ |
| roomID | const char * | Room ID |
| userID | const char * | Sender ID |
| userName | const char * | Sender nickname |
| userAvatar | const char * | Sender profile photo |
| message | const char * | Text message content |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg)
      {
      	// Text messages are displayed on IM panel
      }
      
      ...
  };
  ```

### 8. onRecvRoomCustomMsg

-  Definition: virtual void onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message)

-  Description: Receives custom messages

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------------ | ------- |
| roomID | const char * | Room ID |
| userID | const char * | Sender ID |
| userName | const char * | Sender nickname |
| userAvatar | const char * | Sender profile photo |
| cmd | const char * | Custom CMD |
| message | const char * | Custom message content |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message)
      {
      	// Parse and process custom messages such as Likes and gifts
      }
      
      ...
  };
  ```

### 9. onError

-  Definition: virtual void onError(const RTCResult& res, const std::string& userID)

-  Description: Notification of internal RTCRoom error

-  Parameters:

| Parameter | Type | Description |
| ------ | ------------------ | ---------------------------------------- |
| res | const RTCResult& | Execution result. See RTCResult structure defined in RTCRoomUtil.h |
| userID | const std::string& | User ID |

-  Example:

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onError(const RTCResult& res, const std::string& userID)
      {
      	// An error message pops up. Decide whether to dismiss or exit the meeting based on severity of errors.
      }
      
      ...
  };
  ```

