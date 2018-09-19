# LVB+Joint Broadcasting (LiveRoom)

**LVB+Joint Broadcasting** is an LVB mode commonly used in the **Live Show** and **Online Education** scenarios. With a good applicability to many scenarios, it supports online live broadcasting featuring both high concurrency and low cost, but also enables video chats between VJs and viewers via joint broadcasting.

![img](https://main.qcloudimg.com/raw/4032376146a41d3597d9a28350b542b5.jpg)

Tencent Cloud provides "LVB+Joint Broadcasting" by using [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606), a component consisting of Client and Server (both open source). For more information on how to interface with it, please see [DOC](https://cloud.tencent.com/document/product/454/14606). This document displays the API list for Client:

> [Download](https://cloud.tencent.com/document/product/454/7873#Windows) the SDK package on Tencent Cloud's official website. LiveRoom related header files and source code files are included in SDK\Rooms\LiveRoom.

## LiveRoom

| Name | Description |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| instance() | Gets a single instance of LiveRoom and calls the API of LiveRoom through the single instance. |
| setCallback(ILiveRoomCallback * callback) | Sets the callback proxy for LiveRoom callback, and listens to the internal status of LiveRoom and the execution results of the API. |
| login(const std::string & serverDomain, const LRAuthData & authData, ILoginLiveCallback* callback) | Logs in to the business server RoomService before you can normally use other APIs and the IM feature. |
| logout() | Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail. |
| getRoomList(int index, int count, IGetLiveRoomListCallback* callback) | Gets the room list. If there are many rooms, you can get the list in pages. |
| void getAudienceList(const std::string& roomID) | Gets the list of viewers and returns only the last 30 viewers who entered the room. |
| createRoom(const std::string& roomID, const std::string& roomInfo) | Creates a room, and the new room will be added to the room list in the backend, and then VJs can start pushing. |
| enterRoom(const std::string& roomID, HWND rendHwnd, const RECT & rect) | Enters a room |
| leaveRoom() | Leaves the room. If the primary VJ leaves, the room will be terminated by the backend; if secondary VJs or viewers leave, the remaining participants can continue watching. |
| sendRoomTextMsg(const char * msg) | Sends plain text messages, such as sending on-screen comments under LVB scenarios |
| sendRoomCustomMsg(const char * cmd, const char * msg) | Sends custom messages, such as giving a "Like" or flower under LVB scenarios. |
| startLocalPreview(HWND rendHwnd, const RECT & rect) | Enables the default camera preview |
| updateLocalPreview(HWND rendHwnd, const RECT &rect) | Resets the preview area for camera. When the size of the window identified by the specified local HWND changes, you can resize the video rendering area using this function. |
| stopLocalPreview() | Disables camera preview |
| startScreenPreview(HWND rendHwnd, HWND captureHwnd, const RECT & renderRect, const RECT & captureRect) | Enables screen sharing |
| stopScreenPreview() | Disables screen sharing |
| addRemoteView(HWND rendHwnd, const RECT & rect, const char * userID) | Plays videos of other VJs in the room |
| removeRemoteView(const char * userID) | Stops playing videos of other VJs |
| setMute(bool mute) | Enables Mute |
| setVideoQuality(LRVideoQuality quality, LRAspectRatio ratio) | Sets the preset options for image quality |
| setBeautyStyle(TXEBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel) | Sets beauty filter and whitening effects |
| requestJoinPusher() | Joint broadcasting request from viewer |
| acceptJoinPusher(const std::string& userID) | The primary VJ accepts the joint broadcasting request and informs the request initiator |
| rejectJoinPusher(const std::string& userID, const std::string& reason) | The primary VJ rejects the joint broadcasting request and informs the request initiator |
| kickoutSubPusher(const std::string& userID) | The primary VJ kicks out a secondary VJ |

## ILoginLiveCallback

| Name | Description |
| -------------------------------------------------------- | ------------------- |
| onLogin(const LRResult& res, const LRAuthData& authData) | Callback of login result |

## IGetLiveRoomListCallback

| Name | Description |
| ------------------------------------------------------------ | ------------------ |
| onGetRoomList(const LRResult& res, const std::vector<LRRoomData>& rooms) | Callback of obtaining a room list |

## ILiveRoomCallback

| Name | Description |
| ------------------------------------------------------------ | -------------------------- |
| onCreateRoom(const LRResult& res, const std::string& roomID) | Callback of creating a room |
| onEnterRoom(const LRResult& res) | Callback of entering a room |
| onUpdateRoomData(const LRResult& res, const LRRoomData& roomData) | Callback of room information change |
| void onGetAudienceList(const LRResult& res, const std::vector<LRAudienceData>& audiences) | Callback of viewer list query |
| onPusherJoin(const LRMemberData& member) | Callback of joint broadcasting viewer entering the room |
| void onPusherQuit(const LRMemberData& member) | Callback of joint broadcasting viewer exiting the room |
| onRoomClosed(const std::string& roomID) | Callback of room dissolution |
| onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg) | Receives plain text messages |
| onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message) | Receives custom messages |
| onError(const LRResult& res, const std::string& userID) | Notification of internal LiveRoom error |
| onRecvJoinPusherRequest(const std::string& roomID, const std::string& userID, const std::string& userName, const std::string& userAvatar) | Receives a joint broadcasting request |
| onRecvAcceptJoinPusher(const std::string& roomID, const std::string& msg) | Receives the notification of accepting a joint broadcasting request |
| onRecvRejectJoinPusher(const std::string& roomID, const std::string& msg) | Receives the notification of rejecting a joint broadcasting request |
| onRecvKickoutSubPusher(const std::string& roomID) | Receives the notification of the primary VJ kicking out a secondary VJ |

## Details of LiveRoom Object APIs

### 1. instance

-  Definition: static LiveRoom* instance()

-  Description: Gets a single instance of LiveRoom and calls the API of LiveRoom through the single instance

-  Example:

  ```c++
  LiveRoom* m_liveRoom = NULL;
  m_liveRoom = LiveRoom::instance();
  ```

### 2. setCallback

-  Definition: void setCallback(ILiveRoomCallback * callback)

-  Description: Sets the callback proxy for LiveRoom callback, and listens to the internal status of LiveRoom and the execution results of the API

-  Parameter:

| Parameter | Type | Description |
| -------- | ------------------- | -------------------------------- |
| callback | ILiveRoomCallback * | Proxy pointer of ILiveRoomCallback type |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
      MainDialog();
      virtual ~MainDialog();
      
      virtual void onCreateRoom(const LRResult& res, const std::string& roomID);
      virtual void onEnterRoom(const LRResult& res);
      virtual void onUpdateRoomData(const LRResult& res, const LRRoomData& roomData);
      ...
  };

  MainDialog::MainDialog()
  {
      m_liveRoom->setCallback(this);	//Set callback
  }

  ...
  ```

  ​

### 3. login

-  Definition: void login(const std::string & serverDomain, const LRAuthData & authData, ILoginLiveCallback* callback)

-  Description: Logs in to the business server RoomService before you can normally use other APIs and the IM feature

-  Parameters:

| Parameter | Type | Description |
| ------------ | ------------------- | ------------------------------------------------------------ |
| serverDomain | const std::string & | URL of RoomService. In consideration of security, it is recommended to access the https encrypted link. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| authData | const LRAuthData & | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a success login. For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW). |
| callback | ILoginLiveCallback* | Proxy pointer of ILoginLiveCallback type, used to call back the login result |

-  Example:

  ```c++
  std::string serverDomain = "https://roomtest.qcloud.com/weapp/live_room";

  m_authData.sdkAppID = sdkAppID;
  m_authData.accountType = accountType;
  m_authData.userID = userID;
  m_authData.userSig = userSig;
  m_authData.userName = userName;
  m_authData.userAvatar = userAvatar;
  m_authData.token = token;

  // This class implements the ILoginCallback API to obtain login results
  m_liveRoom->login(serverDomain, m_authData, this);
  ```

### 4. logout

-  Definition: void logout();

-  Description: Logs out of the business server RoomService. Make sure to call "logout" after "leaveRoom" is called, otherwise the call of leaveRoom will fail.

-  Example:

  ```c++
  m_liveRoom->logout();
  ```

### 5. getRoomList

-  Definition: void getRoomList(int index, int count, IGetLiveRoomListCallback* callback)

-  Description: Gets the room list. If there are many rooms, you can get the list in pages.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------------- | ------------------------------------------------------------ |
| index | int | Retrieval by page. The initial default can be set to 0, and the subsequent retrieval is the initial room index (for example, set index=0 and cnt=5 for the first retrieval, and set index=5 for the second page). |
| count | int | The maximum number of rooms returned per call; 0 indicates all rooms that meet the conditions |
| callback | IGetLiveRoomListCallback* | Proxy pointer of IGetLiveRoomListCallback type, used to call back the query result |

-  Example:

  ```c++
  // Start from index=0. A maximum of 20 rooms can be queried. This class implements the IGetRoomListCallback API to obtain query results
  m_liveRoom->getRoomList(0, 20, this);
  ```

### 6. getAudienceList

-  Definition: void getAudienceList(const std::string& roomID)
-  Description: Gets the list of viewers and returns only the last 30 viewers who entered the room
-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | --------------------------------------------- |
| roomID | const std::string& | roomID, which is obtained in the room list returned by the getRoomList API |

-  Example:

```c++
m_liveRoom->getRoomList(roomID);
```

### 7. createRoom

-  Definition: void createRoom(const std::string& roomID, const std::string& roomInfo)

-  Description: Creates a room, and the new room will be added to the room list in the backend, and then VJs can start pushing.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------ | ------------------------------------------------------------ |
| roomID | const std::string& | Room ID. If an empty string is specified, a roomID is assigned to you. Otherwise, the specified roomID is used as the ID of this room. |
| roomInfo | const std::string& | Custom data. This field is included in the room information. It is recommended that you define roomInfo in json format, which is highly extensible. |

-  Example:

  ```c++
  // A roomID is assigned to you
  m_liveRoom->createRoom("", "{\"roomName\": \"My first room\"}");
  ```

### 8. enterRoom

-  Definition: void enterRoom(const std::string& roomID, HWND rendHwnd, const RECT & rect)

-  Description: Enters a room.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------------ | ------------------------------------------------------------ |
| roomID | const std::string& | roomID - the ID of the room to be entered, which is obtained in the room list returned by the getRoomList API |
| rendHwnd | HWND | The HWND that identifies the preview window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window
  m_liveRoom->enterRoom(roomID, hwnd, rect);
  ```

### 9. leaveRoom

-  Definition: void leaveRoom()

-  Description: Leaves the room. If the primary VJ leaves, the room will be terminated by the backend; if secondary VJs or viewers leave, the remaining participants can continue watching.

-  Example:

  ```c++
  m_liveRoom->leaveRoom();
  ```

### 10. sendRoomTextMsg

-  Definition: void sendRoomTextMsg(const char * msg)

-  Description: Sends plain text messages, such as sending on-screen comments under LVB scenarios.

-  Parameter:

| Parameter | Type | Description |
| ---- | ------------ | -------- |
| msg | const char * | Text message |

-  Example:

  ```c++
  m_liveRoom->sendRoomTextMsg("Hello LiveRoom");
  ```

### 11. sendRoomCustomMsg

-  Definition: void sendRoomCustomMsg(const char * cmd, const char * msg)

-  Description: Sends custom messages, such as giving a "Like" or flower under LVB scenarios

-  Parameter:

| Parameter | Type | Description |
| ---- | ------------ | ------------------------------ |
| cmd | const char * | Custom cmd, jointly determined by the sender and receiver |
| msg | const char * | Custom message |

-  Example:

  ```c++
  // Assume that the cmd determined by the sender and receiver includes Smile and Anger
  m_liveRoom->sendRoomCustomMsg("Smile", "I am hungry");
  ```

### 12. startLocalPreview

-  Definition: void startLocalPreview(HWND rendHwnd, const RECT & rect)

-  Description: Enables the default camera preview

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ------------------------------------------------------------ |
| rendHwnd | HWND | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = null, there is no need to preview the video. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window
  m_liveRoom->startLocalPreview(hwnd, rect);
  ```

### 13. updateLocalPreview

-  Definition: void updateLocalPreview(HWND rendHwnd, const RECT &rect)

-  Description: Resets the preview area for camera. When the size of the window identified by the specified HWND changes, you can resize the video rendering area using this function.

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | ------------------------------------------------------------ |
| rendHwnd | HWND | HWND that identifies the preview screen. OpenGL is used to draw images on HWND. If rendHwnd = NULL, there is no need to preview the video. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window
  m_liveRoom->updateLocalPreview(hwnd, rect);
  ```

### 14. stopLocalPreview

-  Definition: void stopLocalPreview()

-  Description: Disables camera preview

-  Example:

  ```c++
  m_liveRoom->stopLocalPreview();
  ```

### 15. startScreenPreview

-  Definition: bool startScreenPreview(HWND rendHwnd, HWND captureHwnd, const RECT & renderRect, const RECT & captureRect)

-  Description: Enables screen sharing

-  Parameters:

| Parameter | Type | Description |
| ----------- | ------------ | ------------------------------------------------------------ |
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

  m_liveRoom->startScreenPreview(rendHwnd, captureHwnd, renderRect, captureRect);
  ```

### 16. stopScreenPreview

-  Definition: void stopScreenPreview()

-  Description: Disables screen sharing

-  Example:

  ```c++
  m_liveRoom->stopScreenPreview();
  ```

### 17. addRemoteView

-  Definition: void addRemoteView(HWND rendHwnd, const RECT & rect, const char * userID)

-  Description: Plays videos of other VJs in the room

-  Parameters:

| Parameter | Type | Description |
| -------- | ------------ | -------------------------------- |
| rendHwnd | HWND | The HWND that identifies the preview window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |
| userID | const char * | User ID |

-  Example:

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// Render in the entire HWND window

  // Enable playback of users' audios/videos
  m_liveRoom->addRemoteView(hwnd, rect, userID);
  ```

### 18. removeRemoteView

-  Definition: void removeRemoteView(const char * userID)

-  Description: Stops playing videos of other VJs

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------ | ------ |
| userID | const char * | User ID |

-  Example:

  ```c++
  m_liveRoom->removeRemoteView(userID);
  ```

### 19. setMute

-  Definition: void setMute(bool mute)

-  Description: Enables Mute

-  Parameter:

| Parameter | Type | Description |
| ---- | ---- | -------- |
| mute | bool | Indicates whether to enable Mute |

-  Example:

  ```c++
  m_liveRoom->setMute(true); // Set to mute
  ```

### 20. setVideoQuality

-  Definition: void setVideoQuality(LRVideoQuality quality, LRAspectRatio ratio)

- Description: Sets the pushed video quality

-  Parameter:

| Parameter | Type | Description |
| ------- | -------------- | --------------------------------------------------------- |
| quality | LRVideoQuality | Image quality, see LRVideoQuality's enumerated values defined in LiveRoomUtil.h |
| ratio | LRAspectRatio | Aspect ratio, see LRAspectRatio's enumerated values defined in LiveRoomUtil.h |

-  Example:

  ```c++
  // Set the image quality to HD and the aspect ratio to 4:3
  m_liveRoom->setVideoQuality(LIVEROOM_VIDEO_QUALITY_HIGH_DEFINITION, LIVEROOM_ASPECT_RATIO_4_3);
  ```

### 21. setBeautyStyle

-  Definition: void setBeautyStyle(TXEBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel)

-  Description: Sets beauty filter and whitening effects

-  Parameter:

| Parameter | Type | Description |
| -------------- | -------------- | ------------------------------------------------------------ |
| beautyStyle | TXEBeautyStyle | See LRBeautyStyle's enumerated values defined in LiveRoomUtil.h |
| beautyLevel | int | Beauty filter level: 1-9. 0 indicates disabling beauty filter. A greater value means a bigger effect. |
| whitenessLevel | int | Whiteness level: 1-9. 0 indicates disabling whitening. A greater value means a bigger effect. |

-  Example:

  ```c++
  // Natural; beauty filter level: 5; whitening level: 5
  m_liveRoom->setBeautyStyle(TXE_BEAUTY_STYLE_NATURE, 5, 5);
  ```

### 22. requestJoinPusher

-  Definition: void requestJoinPusher()

-  Description: Joint broadcasting request from viewer

-  Example:

  ```c++
  m_liveRoom->requestJoinPusher();
  ```

### 23. acceptJoinPusher

-  Definition: void acceptJoinPusher(const std::string& userID)

-  Description: The primary VJ accepts the joint broadcasting request and informs the request initiator.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | ------ |
| userID | const std::string& | User ID |

-  Example:

  ```c++
  m_liveRoom->acceptJoinPusher(userID);
  ```

### 24. rejectJoinPusher

- Definition: void rejectJoinPusher(const std::string& userID, const std::string& reason)

- Description: The primary VJ rejects the joint broadcasting request and informs the request initiator.

-  Parameters:

| Parameter | Type | Description |
| ------ | ------------------ | ---------- |
| userID | const std::string& | User ID |
| reason | const std::string& | Reason for rejection |

-  Example:

  ```c++
  m_liveRoom->acceptJoinPusher(userID, reason);
  ```

### 25. kickoutSubPusher

-  Definition: void kickoutSubPusher(const std::string& userID)

-  Description: The primary VJ kicks out a secondary VJ.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | ------ |
| userID | const std::string& | User ID |

-  Example:

  ```c++
  m_liveRoom->kickoutSubPusher(userID);
  ```



## Details of ILoginLiveCallback APIs

### 1. onLogin

-  Definition: virtual void onLogin(const LRResult& res, const LRAuthData& authData)

-  Description: Callback of login result

-  Parameters:

| Parameter | Type | Description |
| -------- | ----------------- | ------------------------------------------------------------ |
| res | const LRResult& | Execution result. See LRResult structure defined in LiveRoomUtil.h |
| authData | const LRAuthData& | Login information provided by RoomService, including IM related configuration fields. The token field can be obtained after a successful login. |

-  Example:

  ```c++
  class LoginDialog : public ILoginLiveCallback
  {
  public:
  	virtual void onLogin(const LRResult& res, const LRAuthData& authData)
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
  };

  // For more information on how to use callback, please see LiveRoom::login API
  ...
  ```



## Details of IGetLiveRoomListCallback APIs

### 1. onGetRoomList

-  Definition: virtual void onGetRoomList(const LRResult& res, const std::vector<LRRoomData>& rooms)

-  Description: Callback of obtaining a room list

-  Parameters:

| Parameter | Type | Description |
| ----- | ------------------------------ | ------------------------------------------------------ |
| res | const LRResult& | Execution result. See LRResult structure defined in LiveRoomUtil.h |
| rooms | const std::vector<LRRoomData>& | List of room information |

-  Example:

  ```c++
  class RoomListDialog : public IGetRoomListCallback
  {
  public:
  	virtual void onGetRoomList(const LRResult& res, const std::vector<LRRoomData>& rooms)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// Query Failed
          }
          else
          {
          	// Query succeeded, process rooms data
          }
      }
  };

  // For more information on how to use callback, please see LiveRoom::getRoomList API
  ...
  ```



## Details of ILiveRoomCallback APIs

 For more information on how to set ILiveRoomCallback, please see the API LiveRoom::setCallback.

### 1. onCreateRoom

-  Definition: virtual void onCreateRoom(const LRResult& res, const std::string& roomID)

-  Description: Callback of creating a room

-  Parameters:

| Parameter | Type | Description |
| ------ | ------------------ | ------------------------------------------------------ |
| res | const LRResult& | Execution result. See LRResult structure defined in LiveRoomUtil.h |
| roomID | const std::string& | Room ID |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onCreateRoom(const LRResult& res, const std::string& roomID)
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
  };
  ```

### 2. onEnterRoom

-  Definition: virtual void onEnterRoom(const LRResult& res)

-  Description: Callback of entering a room

-  Parameter:

| Parameter | Type | Description |
| ---- | --------------- | ------------------------------------------------------ |
| res | const LRResult& | Execution result. See LRResult structure defined in LiveRoomUtil.h |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onEnterRoom(const LRResult& res)
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
  };
  ```

### 3. onUpdateRoomData

-  Definition: virtual void onUpdateRoomData(const LRResult& res, const LRRoomData& roomData)

-  Description: Callback of room information change

-  Parameters:

| Parameter | Type | Description |
| -------- | ----------------- | -------------------------------------------------------- |
| res | const LRResult& | Execution result. See LRResult structure defined in LiveRoomUtil.h |
| roomData | const LRRoomData& | Room information. See LRRoomData structure defined in LiveRoomUtil.h. |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onUpdateRoomData(const LRResult& res, const LRRoomData& roomData)
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
  };
  ```

### 4. onGetAudienceList

-  Definition: virtual void onGetAudienceList(const LRResult& res, const std::vector<LRAudienceData>& audiences)
-  Description: Callback of viewer list query
-  Parameters:

| Parameter | Type | Description |
| --------- | ---------------------------------- | ------------------------------------------------------ |
| res | const LRResult& | Execution result. See LRResult structure defined in LiveRoomUtil.h |
| audiences | const std::vector<LRAudienceData>& | Viewer information list |

-  Example:

```c++
class MainDialog : public ILiveRoomCallback
{
public:
	virtual void onGetAudienceList(const LRResult& res, const std::vector<LRAudienceData>& audiences)
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
};
```

### 5. onPusherJoin

-  Definition: virtual void onPusherJoin(const LRMemberData& member)

-  Description: Callback of joint broadcasting viewer entering the room

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------- | ---------------------------------------------------------- |
| member | const LRMemberData& | Member information. See LRMemberData structure defined in LiveRoomUtil.h. |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onPusherJoin(const LRMemberData& member)
      {
      	// Usually, the video and audio of the joint broadcasting viewer are turned on after he or she requests joint broadcasting.
      	m_liveRoom->addRemoteView(rendHwnd, rect, member.userID);
      	...
      }
      
      ...
  };
  ```

### 6. onPusherQuit

-  Definition: virtual void onPusherQuit(const LRMemberData& member)

-  Description: Callback of the joint broadcasting viewer exiting the room

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------- | ---------------------------------------------------------- |
| member | const LRMemberData& | Member information. See LRMemberData structure defined in LiveRoomUtil.h. |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onPusherQuit(const LRMemberData& member)
      {
      	// Usually, the video and audio of the joint broadcasting viewer are turned off after he or she stops joint broadcasting.
      	m_liveRoom->removeRemoteView(member.userID);
      	...
      }
      
      ...
  };
  ```

### 7. onRoomClosed

-  Definition: virtual void onRoomClosed(const std::string& roomID)

-  Description: Callback of room dissolution

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | ------ |
| roomID | const std::string& | Room ID |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
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

### 8. onRecvRoomTextMsg

-  Definition: virtual void onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg)

-  Description: Receives plain text messages

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------------ | ------------ |
| roomID | const char * | Room ID |
| userID | const char * | Sender ID |
| userName | const char * | Sender nickname |
| userAvatar | const char * | Sender profile photo |
| message | const char * | Text message content |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg)
      {
      	// Text messages are displayed on IM panel
      }
      
      ...
  };
  ```

### 9. onRecvRoomCustomMsg

-  Definition: virtual void onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message)

-  Description: Receives custom messages

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------------ | -------------- |
| roomID | const char * | Room ID |
| userID | const char * | Sender ID |
| userName | const char * | Sender nickname |
| userAvatar | const char * | Sender profile photo |
| cmd | const char * | Custom CMD |
| message | const char * | Custom message content |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message)
      {
      	// Parse and process custom messages such as Likes and gifts
      }
      
      ...
  };
  ```

### 10. onError

-  Definition: virtual void onError(const LRResult& res, const std::string& userID)

-  Description: Notification of internal LiveRoom error

-  Parameters:

| Parameter | Type | Description |
| ------ | ------------------ | ------------------------------------------------------ |
| res | const LRResult& | Execution result. See LRResult structure defined in LiveRoomUtil.h |
| userID | const std::string& | User ID |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onError(const LRResult& res, const std::string& userID)
      {
      	// An error message pops up. Decide whether to close LVB based on severity of errors
      }
      
      ...
  };
  ```

### 11. onRecvJoinPusherRequest

- Definition: virtual void onRecvJoinPusherRequest(const std::string& roomID, const std::string& userID, const std::string& userName, const std::string& userAvatar)

-  Description: Receives a joint broadcasting request

-  Parameters:

| Parameter | Type | Description |
| ---------- | ------------------ | ---------- |
| roomID | const std::string& | Room ID |
| userID | const std::string& | Sender ID |
| userName   | const std::string& | Sender nickname |
| userAvatar | const std::string& | Sender profile photo |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onRecvJoinPusherRequest(const std::string& roomID, const std::string& userID, const std::string& userName, const std::string& userAvatar)
      {
      	// The primary VJ receives a joint broadcasting request from a viewer.
      	// Verify the validity of roomID
      	// UI shows who initiates the request.
      	// The primary VJ selects "acceptJoinPusher" to accept or "rejectJoinPusher" to reject the request.
      }
      
      ...
  };
  ```

### 12. onRecvAcceptJoinPusher

-  Definition: virtual void onRecvAcceptJoinPusher(const std::string& roomID, const std::string& msg)

-  Description: Receives the notification of accepting a joint broadcasting request.

-  Parameters:

| Parameter | Type | Description |
| ------ | ------------------ | ------ |
| roomID | const std::string& | Room ID |
| msg | const std::string& | Message |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onRecvAcceptJoinPusher(const std::string& roomID, const std::string& msg)
      {
      	// The viewer receives the notification of the primary VJ accepting the joint broadcasting request.
      	// Verify the validity of roomID
      	// Process msg
      }
      
      ...
  };
  ```

  ​

### 13. onRecvRejectJoinPusher

-  Definition: virtual void onRecvRejectJoinPusher(const std::string& roomID, const std::string& msg)

-  Description: Receives the notification of rejecting a joint broadcasting request

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | ------ |
| roomID | const std::string& | Room ID |
| msg | const std::string& | Message |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onRecvRejectJoinPusher(const std::string& roomID, const std::string& msg)
      {
      	// The viewer receives the notification of the primary VJ rejecting the joint broadcasting request.
      	// Verify the validity of roomID
      	// Process msg
      }
      
      ...
  };
  ```

  ​

### 14. onRecvKickoutSubPusher

-  Definition: virtual void onRecvKickoutSubPusher(const std::string& roomID)

-  Description: Receives the notification of the primary VJ kicking out a secondary VJ.

-  Parameter:

| Parameter | Type | Description |
| ------ | ------------------ | ------ |
| roomID | const std::string& | Room ID |

-  Example:

  ```c++
  class MainDialog : public ILiveRoomCallback
  {
  public:
  	virtual void onRecvRejectJoinPusher(const std::string& roomID, const std::string& msg)
      {
      	// The primary VJ kicks out a viewer invited for joint broadcasting
      	// Verify the validity of roomID
      	// Process msg
      }
      
      ...
  };
  ```

  ​
