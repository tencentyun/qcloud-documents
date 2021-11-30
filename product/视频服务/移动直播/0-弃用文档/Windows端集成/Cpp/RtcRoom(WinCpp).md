# 实时音视频（RTCRoom ）接口（C++）

## RTCRoom

| 名称                                       | 描述                                       |
| ---------------------------------------- | ---------------------------------------- |
| instance()                               | 获取RTCRoom单例，通过单例调用RTCRoom的接口             |
| setCallback(IRTCRoomCallback * callback) | 设置回调 RTCRoom 的回调代理，监听 RTCRoom 的内部状态和接口的执行结果 |
| login(const std::string & serverDomain, const RTCAuthData & authData, ILoginRTCCallback* callback) | 登录业务服务器RoomService，登录后才能够正常使用其他接口和使用IM功能 |
| logout()                                 | 登出业务服务器RoomService，请注意在leaveRoom调用后，再调用logout，否则leaveRoom会调用失败 |
| getRoomList(int index, int count, IGetRTCRoomListCallback* callback) | 获取房间列表，房间数量比较多时，可以分页获取                   |
| createRoom(const std::string& roomID, const std::string& roomInfo) | 创建房间，后台的房间列表中会添加一个新房间，同时会议创建者端会进入推流模式    |
| enterRoom(const std::string& roomID, HWND rendHwnd, const RECT & rect) | 进入房间                                     |
| leaveRoom()                              | 离开房间，如果是会议创建者，这个房间会被后台销毁，如果是会议参与者，不影响其他人继续通话 |
| sendRoomTextMsg(const char * msg)        | 发送普通文本消息                                 |
| sendRoomCustomMsg(const char * cmd, const char * msg) | 发送自定义消息                                  |
| startLocalPreview(HWND rendHwnd, const RECT & rect) | 启动默认的摄像头预览                               |
| updateLocalPreview(HWND rendHwnd, const RECT &rect) | 重设摄像头预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域 |
| stopLocalPreview()                       | 关闭摄像头预览                                  |
| startScreenPreview(HWND rendHwnd, HWND captureHwnd, const RECT & renderRect, const RECT & captureRect) | 启动屏幕分享                                   |
| stopScreenPreview()                      | 关闭屏幕分享                                   |
| addRemoteView(HWND rendHwnd, const RECT & rect, const char * userID) | 播放房间内其他会议参与者的视频                          |
| updateRemotePreview(HWND rendHwnd, const RECT &rect, const char * userID) | 重设指定userID的视频预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域 |
| removeRemoteView(const char * userID)    | 停止播放其他会议参与者的视频                           |
| setMute(bool mute)                       | 静音接口                                     |
| setBeautyStyle(TXEBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel) | 设置美颜和美白效果                                |

## ILoginRTCCallback

| 名称                                       | 描述           |
| ---------------------------------------- | ------------ |
| onLogin(const RTCResult& res, const RTCAuthData& authData) | login登录结果的回调 |

## IGetRTCRoomListCallback

| 名称                                       | 描述        |
| ---------------------------------------- | --------- |
| onGetRoomList(const RTCResult& res, const std::vector<RTCRoomData>& rooms) | 获取房间列表的回调 |

## IRTCRoomCallback

| 名称                                       | 描述               |
| ---------------------------------------- | ---------------- |
| onCreateRoom(const RTCResult& res, const std::string& roomID) | 创建房间的回调          |
| onEnterRoom(const RTCResult& res)        | 进入房间的回调          |
| onUpdateRoomData(const RTCResult& res, const RTCRoomData& roomData) | 房间信息变更的回调        |
| onPusherJoin(const RTCMemberData& member) | 成员进入房间的回调        |
| void onPusherQuit(const RTCMemberData& member) | 成员退出房间的回调        |
| onRoomClosed(const std::string& roomID)  | 房间解散的回调          |
| onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg) | 收到普通文本消息         |
| onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message) | 收到自定义消息          |
| onError(const RTCResult& res, const std::string& userID) | RTCRoom内部发生错误的通知 |

## RTCRoom对象接口的详情

### 1. instance

- 定义：static RTCRoom* instance()

- 说明：获取RTCRoom单例，通过单例调用RTCRoom的接口

- 示例：

  ```c++
  RTCRoom* m_RTCRoom = NULL;
  m_RTCRoom = RTCRoom::instance();
  ```

### 2. setCallback

- 定义：void setCallback(IRTCRoomCallback * callback)

- 说明：设置回调 RTCRoom 的回调代理，监听 RTCRoom 的内部状态和接口的执行结果

- 参数：

| 参数       | 类型                 | 描述                       |
| -------- | ------------------ | ------------------------ |
| callback | IRTCRoomCallback * | IRTCRoomCallback 类型的代理指针 |

- 示例：

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
      m_RTCRoom->setCallback(this);	// 设置回调
  }

  ...
  ```

  ​

### 3. login

- 定义：void login(const std::string & serverDomain, const RTCAuthData & authData, ILoginRTCCallback* callback)

- 说明：登录业务服务器RoomService，登录后才能够正常使用其他接口和使用IM功能

- 参数：

| 参数           | 类型                  | 描述                                       |
| ------------ | ------------------- | ---------------------------------------- |
| serverDomain | const std::string & | RoomService的URL地址，安全起见，建议访问https加密链接， 参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW) |
| authData     | const RTCAuthData & | RoomService提供的登录信息，包括IM相关的配置字段，在login成功后，获取到token字段，参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW) |
| callback     | ILoginRTCCallback*  | ILoginRTCCallback 类型的代理指针，回调login的结果     |

- 示例：

  ```c++
  std::string serverDomain = "https://roomtest.qcloud.com/weapp/double_room";

  m_authData.sdkAppID = sdkAppID;
  m_authData.accountType = accountType;
  m_authData.userID = userID;
  m_authData.userSig = userSig;
  m_authData.userName = userName;
  m_authData.userAvatar = userAvatar;
  m_authData.token = token;

  // 该类实现ILoginCallback接口，获取login结果
  m_RTCRoom->login(serverDomain, m_authData, this);
  ```

### 4. logout

- 定义：void logout();

- 说明：登出业务服务器RoomService，请注意在leaveRoom调用后，再调用logout，否则leaveRoom会调用失败

- 示例：

  ```c++
  m_RTCRoom->logout();
  ```

### 5. getRoomList

- 定义：void getRoomList(int index, int count, IGetRTCRoomListCallback* callback)

- 说明：获取房间列表，房间数量比较多时，可以分页获取

- 参数：

| 参数       | 类型                       | 描述                                       |
| -------- | ------------------------ | ---------------------------------------- |
| index    | int                      | 分页获取，初始默认可设置为0，后续获取为起始房间索引（如第一次设置index=0, cnt=5,获取第二页时可用index=5） |
| count    | int                      | 每次调用，最多返回房间个数；0表示所有满足条件的房间               |
| callback | IGetRTCRoomListCallback* | IGetRTCRoomListCallback 类型的代理指针，查询结果的回调  |

- 示例：

  ```c++
  // 此处从index=0开始，最多查询20个房间，该类实现IGetRoomListCallback接口，获取查询结果
  m_RTCRoom->getRoomList(0, 20, this);
  ```

### 6. createRoom

- 定义：void createRoom(const std::string& roomID, const std::string& roomInfo)

- 说明：创建房间，后台的房间列表中会添加一个新房间，同时会议创建者会进入推流模式

- 参数：

| 参数       | 类型                 | 描述                                       |
| -------- | ------------------ | ---------------------------------------- |
| roomID   | const std::string& | 房间ID，若传入空字符串，则后台会为您分配roomID，否则，传入的roomID作为这个房间的ID |
| roomInfo | const std::string& | 自定义数据，该字段包含在房间信息中，推荐您将 roomInfo 定义为 json 格式，这样可以有很强的扩展性 |

- 示例：

  ```c++
  // 后台会为您分配roomID
  m_RTCRoom->createRoom("", "{\"roomName\": \"My first room\"}");
  ```

### 7. enterRoom

- 定义：void enterRoom(const std::string& roomID)

- 说明：进入房间

- 参数：

| 参数     | 类型                 | 描述                                       |
| ------ | ------------------ | ---------------------------------------- |
| roomID | const std::string& | roomID - 要进入的房间ID，在 getRoomList 接口房间列表中查询得到 |

- 示例：

  ```c++
  m_RTCRoom->enterRoom(roomID);
  ```

### 8. leaveRoom

- 定义：void leaveRoom()

- 说明：离开房间，如果是会议创建者，这个房间会被后台销毁，如果是会议参与者，不影响其他人继续通话

- 示例：

  ```c++
  m_RTCRoom->leaveRoom();
  ```

### 9. sendRoomTextMsg

- 定义：void sendRoomTextMsg(const char * msg)

- 说明：发送普通文本消息

- 参数：

| 参数   | 类型           | 描述   |
| ---- | ------------ | ---- |
| msg  | const char * | 文本消息 |

- 示例：

  ```c++
  m_RTCRoom->sendRoomTextMsg("Hello RTCRoom");
  ```

### 10. sendRoomCustomMsg

- 定义：void sendRoomCustomMsg(const char * cmd, const char * msg)

- 说明：发送自定义消息

- 参数：

| 参数   | 类型           | 描述                 |
| ---- | ------------ | ------------------ |
| cmd  | const char * | 自定义cmd，收发双方协商好的cmd |
| msg  | const char * | 自定义消息              |

- 示例：

  ```c++
  // 假设收发双方协商好的cmd有Smile, Anger
  m_RTCRoom->sendRoomCustomMsg("Smile", "I am hungry");
  ```

### 11. startLocalPreview

- 定义：void startLocalPreview(HWND rendHwnd, const RECT & rect)

- 说明：启动默认的摄像头预览

- 参数：

| 参数       | 类型           | 描述                                       |
| -------- | ------------ | ---------------------------------------- |
| rendHwnd | HWND         | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = null时无需预览视频 |
| rect     | const RECT & | 指定视频图像在 HWND 上的渲染区域                      |

- 示例：

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// 在hwnd整个窗口中渲染
  m_RTCRoom->startLocalPreview(hwnd, rect);
  ```

### 12. updateLocalPreview

- 定义：void updateLocalPreview(HWND rendHwnd, const RECT &rect)

- 说明：重设摄像头预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域

- 参数：

| 参数       | 类型           | 描述                                       |
| -------- | ------------ | ---------------------------------------- |
| rendHwnd | HWND         | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = NULL时无需预览视频 |
| rect     | const RECT & | 指定视频图像在 HWND 上的渲染区域                      |

- 示例：

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// 在hwnd整个窗口中渲染
  m_RTCRoom->updateLocalPreview(hwnd, rect);
  ```

### 13. stopLocalPreview

- 定义：void stopLocalPreview()

- 说明：关闭摄像头预览

- 示例：

  ```c++
  m_RTCRoom->stopLocalPreview();
  ```

### 14. startScreenPreview

- 定义：bool startScreenPreview(HWND rendHwnd, HWND captureHwnd, const RECT & renderRect, const RECT & captureRect)

- 说明：启动屏幕分享

- 参数：

| 参数          | 类型           | 描述                                       |
| ----------- | ------------ | ---------------------------------------- |
| rendHwnd    | HWND         | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = NULL时无需预览视频 |
| captureHwnd | HWND         | 指定录取窗口，若为NULL，则 captureRect 不起效，并且录取整个屏幕；若不为NULL，则录取这个窗口的画面 |
| renderRect  | const RECT & | 指定视频图像在 rendHwnd 上的渲染区域                  |
| captureRect | const RECT & | 指定录取窗口客户区的区域                             |

- 返回值：成功 or 失败

- 示例：

  ```c++
  RECT renderRect = { 0 };
  ::GetClientRect(rendHwnd, &renderRect);	// 在hwnd整个窗口中渲染

  RECT captureRect = { 0 };
  ::GetClientRect(captureHwnd, &captureRect);	// 录取整个窗口的画面

  m_RTCRoom->startScreenPreview(rendHwnd, captureHwnd, renderRect, captureRect);
  ```

### 15. stopScreenPreview

- 定义：void stopScreenPreview()

- 说明：关闭屏幕分享

- 示例：

  ```c++
  m_RTCRoom->stopScreenPreview();
  ```

### 16. addRemoteView

- 定义：void addRemoteView(HWND rendHwnd, const RECT & rect, const char * userID)

- 说明：播放房间内其他会议参与者的视频

- 参数：

| 参数       | 类型           | 描述                  |
| -------- | ------------ | ------------------- |
| rendHwnd | HWND         | 承载预览画面的 HWND        |
| rect     | const RECT & | 指定视频图像在 HWND 上的渲染区域 |
| userID   | const char * | 用户ID                |

- 示例：

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// 在hwnd整个窗口中渲染

  // 打开用户的音视频播放
  m_RTCRoom->addRemoteView(hwnd， rect, userID);
  ```

### 17. updateRemotePreview

- 定义：void updateRemotePreview(HWND rendHwnd, const RECT &rect, const char * userID)
- 说明：重设指定userID的视频预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域
- 参数：

| 参数       | 类型           | 描述                  |
| -------- | ------------ | ------------------- |
| rendHwnd | HWND         | 承载预览画面的 HWND        |
| rect     | const RECT & | 指定视频图像在 HWND 上的渲染区域 |
| userID   | const char * | 用户ID                |

- 示例：

  ```c++
  RECT rect = { 0 };
  ::GetClientRect(hwnd, &rect);	// 在hwnd整个窗口中渲染

  // 更新用户的音视频播放
  m_RTCRoom->updateRemotePreview(hwnd， rect, userID);
  ```

### 18. removeRemoteView

- 定义：void removeRemoteView(const char * userID)

- 说明：停止播放其他会议参与者的视频

- 参数：

| 参数     | 类型           | 描述   |
| ------ | ------------ | ---- |
| userID | const char * | 用户ID |

- 示例：

  ```c++
  m_RTCRoom->removeRemoteView(userID);
  ```

### 19. setMute

- 定义：void setMute(bool mute)

- 说明：静音接口

- 参数：

| 参数   | 类型   | 描述   |
| ---- | ---- | ---- |
| mute | bool | 是否静音 |

- 示例：

  ```c++
  m_RTCRoom->setMute(true); // 设置为静音
  ```

### 20. setBeautyStyle

- 定义：void setBeautyStyle(TXEBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel)

- 说明：设置美颜和美白效果

- 参数：

| 参数             | 类型             | 描述                                       |
| -------------- | -------------- | ---------------------------------------- |
| beautyStyle    | TXEBeautyStyle | 参考 RTCRoomUtil.h 中定义的 RTCBeautyStyle 枚举值 |
| beautyLevel    | int            | 美颜级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |
| whitenessLevel | int            | 美白级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |

- 示例：

  ```c++
  // 自然，美颜度数5，美白度数5
  m_RTCRoom->setBeautyStyle(TXE_BEAUTY_STYLE_NATURE, 5, 5);
  ```

## ILoginRTCCallback回调接口的详情

### 1. onLogin

- 定义：virtual void onLogin(const RTCResult& res, const RTCAuthData& authData)

- 说明：login登录结果的回调

- 参数：

| 参数       | 类型                 | 描述                                       |
| -------- | ------------------ | ---------------------------------------- |
| res      | const RTCResult&   | 执行结果，参考 RTCRoomUtil.h 中定义的 RTCResult 结构体 |
| authData | const RTCAuthData& | RoomService提供的登录信息，包括IM相关的配置字段，在login成功后，获取到token字段 |

- 示例：

  ```c++
  class LoginDialog : public ILoginRTCCallback
  {
  public:
  	virtual void onLogin(const RTCResult& res, const RTCAuthData& authData)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// 登录失败
          }
          else
          {
          	// 登录成功，保存authData信息
          }
      }
  };

  // 参见RTCRoom::login接口，了解回调的使用
  ...
  ```



## IGetRTCRoomListCallback回调接口的详情

### 1. onGetRoomList

- 定义：virtual void onGetRoomList(const RTCResult& res, const std::vector<RTCRoomData>& rooms)

- 说明：获取房间列表的回调

- 参数：

| 参数    | 类型                              | 描述                                       |
| ----- | ------------------------------- | ---------------------------------------- |
| res   | const RTCResult&                | 执行结果，参考 RTCRoomUtil.h 中定义的 RTCResult 结构体 |
| rooms | const std::vector<RTCRoomData>& | 房间信息的列表                                  |

- 示例：

  ```c++
  class RoomListDialog : public IGetRTCRoomListCallback
  {
  public:
  	virtual void onGetRoomList(const RTCResult& res, const std::vector<RTCRoomData>& rooms)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// 查询失败
          }
          else
          {
          	// 查询成功，处理rooms数据
          }
      }
  };

  // 参见RTCRoom::getRoomList接口，了解回调的使用
  ...
  ```



## IRTCRoomCallback回调接口的详情

 参见RTCRoom::setCallback接口，了解如何设置IRTCRoomCallback回调。

### 1. onCreateRoom

- 定义：virtual void onCreateRoom(const RTCResult& res, const std::string& roomID)

- 说明：创建房间的回调

- 参数：

| 参数     | 类型                 | 描述                                       |
| ------ | ------------------ | ---------------------------------------- |
| res    | const RTCResult&   | 执行结果，参考 RTCRoomUtil.h 中定义的 RTCResult 结构体 |
| roomID | const std::string& | 房间ID                                     |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onCreateRoom(const RTCResult& res, const std::string& roomID)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// 创建房间失败，弹框提示
          }
          else
          {
          	// 创建房间成功，其他观众可以参与会议
          	// 紧接着处理onUpdateRoomData回调
          }
      }
      
      ...
  };
  ```

### 2. onEnterRoom

- 定义：virtual void onEnterRoom(const RTCResult& res)

- 说明：进入房间的回调

- 参数：

| 参数   | 类型               | 描述                                       |
| ---- | ---------------- | ---------------------------------------- |
| res  | const RTCResult& | 执行结果，参考 RTCRoomUtil.h 中定义的 RTCResult 结构体 |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onEnterRoom(const RTCResult& res)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// 进入房间失败，弹框提示
          }
          else
          {
          	// 进入房间成功，紧接着处理onUpdateRoomData回调
          }
      }
      
      ...
  };
  ```

### 3. onUpdateRoomData

- 定义：virtual void onUpdateRoomData(const RTCResult& res, const RTCRoomData& roomData)

- 说明：房间信息变更的回调

- 参数：

| 参数       | 类型                 | 描述                                       |
| -------- | ------------------ | ---------------------------------------- |
| res      | const RTCResult&   | 执行结果，参考 RTCRoomUtil.h 中定义的 RTCResult 结构体 |
| roomData | const RTCRoomData& | 房间信息，参考 RTCRoomUtil.h 中定义的 RTCRoomData 结构体 |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onUpdateRoomData(const RTCResult& res, const RTCRoomData& roomData)
      {
      	if (RTCROOM_SUCCESS != res.ec)
          {
          	// 更新失败，弹框提示
          }
          else
          {
          	// 更新成功，根据createRoom还是enterRoom导致这个接口的触发来做出相应的处理
          }
      }
      
      ...
  };
  ```

### 4. onPusherJoin

- 定义：virtual void onPusherJoin(const RTCMemberData& member)

- 说明：成员进入房间的回调

- 参数：

| 参数     | 类型                   | 描述                                       |
| ------ | -------------------- | ---------------------------------------- |
| member | const RTCMemberData& | 成员信息，参考 RTCRoomUtil.h 中定义的 RTCMemberData 结构体 |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onPusherJoin(const RTCMemberData& member)
      {
      	// 成员进入房间，打开成员的画面和音频
      	m_RTCRoom->addRemoteView(rendHwnd, rect, member.userID);
      	...
      }
      
      ...
  };
  ```

### 5. onPusherQuit

- 定义：virtual void onPusherQuit(const RTCMemberData& member)

- 说明：成员退出房间的回调

- 参数：

| 参数     | 类型                   | 描述                                       |
| ------ | -------------------- | ---------------------------------------- |
| member | const RTCMemberData& | 成员信息，参考 RTCRoomUtil.h 中定义的 RTCMemberData 结构体 |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onPusherQuit(const RTCMemberData& member)
      {
      	// 成员退出房间，关闭成员的画面和音频
      	m_RTCRoom->removeRemoteView(member.userID);
      	...
      }
      
      ...
  };
  ```

### 6. onRoomClosed

- 定义：virtual void onRoomClosed(const std::string& roomID)

- 说明：房间解散的回调

- 参数：

| 参数     | 类型                 | 描述   |
| ------ | ------------------ | ---- |
| roomID | const std::string& | 房间ID |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onRoomClosed(const std::string& roomID)
      {
      	// 提示房间解散，关闭已打开的音视频
      	...
      }
      
      ...
  };
  ```

### 7. onRecvRoomTextMsg

- 定义：virtual void onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg)

- 说明：收到普通文本消息

- 参数：

| 参数         | 类型           | 描述     |
| ---------- | ------------ | ------ |
| roomID     | const char * | 房间ID   |
| userID     | const char * | 发送者ID  |
| userName   | const char * | 发送者昵称  |
| userAvatar | const char * | 发送者头像  |
| message    | const char * | 文本消息内容 |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onRecvRoomTextMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * msg)
      {
      	// IM面板显示文本消息
      }
      
      ...
  };
  ```

### 8. onRecvRoomCustomMsg

- 定义：virtual void onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message)

- 说明：收到自定义消息

- 参数：

| 参数         | 类型           | 描述      |
| ---------- | ------------ | ------- |
| roomID     | const char * | 房间ID    |
| userID     | const char * | 发送者ID   |
| userName   | const char * | 发送者昵称   |
| userAvatar | const char * | 发送者头像   |
| cmd        | const char * | 自定义cmd  |
| message    | const char * | 自定义消息内容 |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onRecvRoomCustomMsg(const char * roomID, const char * userID, const char * userName, const char * userAvatar, const char * cmd, const char * message)
      {
      	// 解析和处理自定义消息，例如点赞、礼物等
      }
      
      ...
  };
  ```

### 9. onError

- 定义：virtual void onError(const RTCResult& res, const std::string& userID)

- 说明：RTCRoom内部发生错误的通知

- 参数：

| 参数     | 类型                 | 描述                                       |
| ------ | ------------------ | ---------------------------------------- |
| res    | const RTCResult&   | 执行结果，参考 RTCRoomUtil.h 中定义的 RTCResult 结构体 |
| userID | const std::string& | 用户ID                                     |

- 示例：

  ```c++
  class MainDialog : public IRTCRoomCallback
  {
  public:
  	virtual void onError(const RTCResult& res, const std::string& userID)
      {
      	// 弹框提示错误，根据错误严重程序，是否解散或者退出会议
      }
      
      ...
  };
  ```
