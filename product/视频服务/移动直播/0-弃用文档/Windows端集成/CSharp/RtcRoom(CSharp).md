# 实时音视频（RTCRoom ）接口（CSharp）

## RTCRoom

| 名称                                       | 描述                                       |
| ---------------------------------------- | ---------------------------------------- |
| instance()                               | 获取RTCRoom单例，通过单例调用RTCRoom的接口             |
| setCallback(IRTCRoomCallback callback)   | 设置回调 RTCRoom 的回调代理，监听 RTCRoom 的内部状态和接口的执行结果 |
| login(string serverDomain, RTCAuthData authData, ILoginRTCCallback callback) | 登录业务服务器RoomService，登录后才能够正常使用其他接口和使用IM功能 |
| logout()                                 | 登出业务服务器RoomService，请注意在leaveRoom调用后，再调用logout，否则leaveRoom会调用失败 |
| getRoomList(int index, int cnt, IGetRTCRoomListCallback callback) | 获取房间列表，房间数量比较多时，可以分页获取                   |
| createRoom(string roomID, string roomInfo) | 创建房间，后台的房间列表中会添加一个新房间，同时会议创建者端会进入推流模式    |
| enterRoom(string roomID)                 | 进入房间                                     |
| leaveRoom()                              | 离开房间，如果是会议创建者，这个房间会被后台销毁，如果是会议参与者，不影响其他人继续通话 |
| sendRoomTextMsg(string msg)              | 在房间内，发送普通文本消息，比如发送弹幕                     |
| sendRoomCustomMsg(string cmd, string msg) | 在房间内，发送普通自定义消息，比如发送点赞、送花等消息              |
| startLocalPreview(IntPtr rendHwnd, Rectangle rect) | 启动默认的摄像头预览                               |
| updateLocalPreview(IntPtr rendHwnd, Rectangle rect) | 重设摄像头预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域 |
| stopLocalPreview()                       | 关闭摄像头预览                                  |
| startScreenPreview(IntPtr rendHwnd, IntPtr captureHwnd, Rectangle renderRect, Rectangle captureRect) | 启动屏幕分享                                   |
| stopScreenPreview()                      | 关闭屏幕分享                                   |
| addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID) | 播放房间内其他会议参与者的视频                          |
| updateRemotePreview(IntPtr rendHwnd, Rectangle rect, string userID) | 重设指定userID的视频预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域 |
| removeRemoteView(string userID)          | 停止播放其他会议参与者的视频                           |
| setMute(bool mute)                       | 静音接口                                     |
| setBeautyStyle(RTCBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel) | 设置美颜和美白效果                                |

## ILoginRTCCallback

| 名称                                       | 描述           |
| ---------------------------------------- | ------------ |
| onLogin(RTCResult res, RTCAuthData authData) | login登录结果的回调 |

## IGetRTCRoomListCallback

| 名称                                       | 描述        |
| ---------------------------------------- | --------- |
| onGetRoomList(RTCResult res, List<RTCRoomData> rooms) | 获取房间列表的回调 |

## IRTCRoomCallback

| 名称                                       | 描述               |
| ---------------------------------------- | ---------------- |
| onCreateRoom(RTCResult res, string roomID) | 创建房间的回调          |
| onEnterRoom(RTCResult res)               | 进入房间的回调          |
| onUpdateRoomData(RTCResult res, RTCRoomData roomData) | 房间信息变更的回调        |
| onPusherJoin(RTCMemberData member)       | 成员进入房间的回调        |
| onPusherQuit(RTCMemberData member)       | 成员退出房间的回调        |
| onRoomClosed(string roomID)              | 房间解散的回调          |
| onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg) | 收到普通文本消息         |
| onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message) | 收到自定义消息          |
| onError(RTCResult res, string userID)    | RTCRoom内部发生错误的通知 |

## RTCRoom对象接口的详情

### 1. instance

- 定义：static RTCRoom instance()

- 说明：获取RTCRoom单例，通过单例调用RTCRoom的接口

- 示例：

  ```c#
  RTCRoom mRTCRoom = RTCRoom.instance();
  ```

### 2. setCallback

- 定义：void setCallback(IRTCRoomCallback callback)

- 说明：设置回调 RTCRoom 的回调代理，监听 RTCRoom 的内部状态和接口的执行结果

- 参数：

| 参数       | 类型               | 描述                     |
| -------- | ---------------- | ---------------------- |
| callback | IRTCRoomCallback | IRTCRoomCallback 类型的接口 |

- 示例：

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
      mRTCRoom.setCallback(this);	// 设置回调
  }

  ...
  ```

  ​

### 3. login

- 定义：void login(string serverDomain, RTCAuthData authData, ILoginRTCCallback callback)

- 说明：登录业务服务器RoomService，登录后才能够正常使用其他接口和使用IM功能

- 参数：

| 参数           | 类型                | 描述                                       |
| ------------ | ----------------- | ---------------------------------------- |
| serverDomain | string            | RoomService的URL地址，安全起见，建议访问https加密链接， 参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW) |
| authData     | RTCAuthData       | RoomService提供的登录信息，包括IM相关的配置字段，在login成功后，获取到token字段，参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW) |
| callback     | ILoginRTCCallback | ILoginRTCCallback 类型的接口，回调login的结果       |

- 示例：

  ```c#
  string serverDomain = "https://roomtest.qcloud.com/weapp/double_room";

  m_authData.sdkAppID = sdkAppID;
  m_authData.accountType = accountType;
  m_authData.userID = userID;
  m_authData.userSig = userSig;
  m_authData.userName = userName;
  m_authData.userAvatar = userAvatar;
  m_authData.token = token;

  // 该类实现ILoginCallback接口，获取login结果
  mRTCRoom.login(serverDomain, m_authData, this);
  ```

### 4. logout

- 定义：void logout()

- 说明：登出业务服务器RoomService，请注意在leaveRoom调用后，再调用logout，否则leaveRoom会调用失败

- 示例：

  ```c#
  mRTCRoom.logout();
  ```

### 5. getRoomList

- 定义：void getRoomList(int index, int count, IGetRTCRoomListCallback callback)

- 说明：获取房间列表，房间数量比较多时，可以分页获取

- 参数：

| 参数       | 类型                      | 描述                                       |
| -------- | ----------------------- | ---------------------------------------- |
| index    | int                     | 分页获取，初始默认可设置为0，后续获取为起始房间索引（如第一次设置index=0, cnt=5,获取第二页时可用index=5） |
| count    | int                     | 每次调用，最多返回房间个数；0表示所有满足条件的房间               |
| callback | IGetRTCRoomListCallback | IGetRTCRoomListCallback 类型的接口，查询结果的回调    |

- 示例：

  ```c#
  // 此处从index=0开始，最多查询20个房间，该类实现IGetRoomListCallback接口，获取查询结果
  mRTCRoom.getRoomList(0, 20, this);
  ```

### 6. createRoom

- 定义：void createRoom(string roomID, string roomInfo)

- 说明：创建房间，后台的房间列表中会添加一个新房间，同时会议创建者会进入推流模式

- 参数：

| 参数       | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| roomID   | string | 房间ID，若传入空字符串，则后台会为您分配roomID，否则，传入的roomID作为这个房间的ID |
| roomInfo | string | 自定义数据，该字段包含在房间信息中，推荐您将 roomInfo 定义为 json 格式，这样可以有很强的扩展性 |

- 示例：

  ```c#
  // 后台会为您分配roomID
  mRTCRoom.createRoom("", "{\"roomName\": \"My first room\"}");
  ```

### 7. enterRoom

- 定义：void enterRoom(string roomID)

- 说明：进入房间

- 参数：

| 参数     | 类型     | 描述                                       |
| ------ | ------ | ---------------------------------------- |
| roomID | string | roomID - 要进入的房间ID，在 getRoomList 接口房间列表中查询得到 |

- 示例：

  ```c#
  mRTCRoom.enterRoom(roomID);
  ```

### 8. leaveRoom

- 定义：void leaveRoom()

- 说明：离开房间，如果是会议创建者，这个房间会被后台销毁，如果是会议参与者，不影响其他人继续通话

- 示例：

  ```c#
  mRTCRoom.leaveRoom();
  ```

### 9. sendRoomTextMsg

- 定义：void sendRoomTextMsg(string msg)

- 说明：发送普通文本消息

- 参数：

| 参数   | 类型     | 描述   |
| ---- | ------ | ---- |
| msg  | string | 文本消息 |

- 示例：

  ```c#
  mRTCRoom.sendRoomTextMsg("Hello RTCRoom");
  ```

### 10. sendRoomCustomMsg

- 定义：void sendRoomCustomMsg(string cmd, string msg)

- 说明：发送自定义消息

- 参数：

| 参数   | 类型     | 描述                 |
| ---- | ------ | ------------------ |
| cmd  | string | 自定义cmd，收发双方协商好的cmd |
| msg  | string | 自定义消息              |

- 示例：

  ```c#
  // 假设收发双方协商好的cmd有Smile, Anger
  mRTCRoom.sendRoomCustomMsg("Anger", "I am hungry");
  ```

### 11. startLocalPreview

- 定义：void startLocalPreview(IntPtr rendHwnd, Rectangle rect)

- 说明：启动默认的摄像头预览
- 参数：

| 参数       | 类型        | 描述                                       |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr    | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = null时无需预览视频 |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域                      |

- 示例：

  ```c#
  mRTCRoom.startLocalPreview(panel_main.Handle, new Rectangle(0, 0, panel_main.Width, panel_main.Height));
  ```

### 12. updateLocalPreview

- 定义：void updateLocalPreview(IntPtr rendHwnd, Rectangle rect)

- 说明：重设摄像头预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域

- 参数：

| 参数       | 类型        | 描述                                       |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr    | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = null时无需预览视频 |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域                      |

- 示例：

  ```c#
  mRTCRoom.updateLocalPreview(panel_main.Handle, new Rectangle(0, 0, panel_main.Width, panel_main.Height));
  ```

### 13. stopLocalPreview

- 定义：void stopLocalPreview()

- 说明：关闭摄像头预览

- 示例：

  ```c#
  mRTCRoom.stopLocalPreview();
  ```

### 14. startScreenPreview

- 定义：bool startScreenPreview(IntPtr rendHwnd, IntPtr captureHwnd, Rectangle renderRect, Rectangle captureRect)

- 说明：启动屏幕分享

- 参数：

| 参数          | 类型        | 描述                                       |
| ----------- | --------- | ---------------------------------------- |
| rendHwnd    | IntPtr    | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = null时无需预览视频 |
| captureHwnd | IntPtr    | 指定录取窗口，若为null，则 captureRect 不起效，并且录取整个屏幕；若不为null，则录取这个窗口的画面 |
| renderRect  | Rectangle | 指定视频图像在 rendHwnd 上的渲染区域                  |
| captureRect | Rectangle | 指定录取窗口客户区的区域                             |

- 返回值：成功 or 失败

- 示例：

  ```c#
  mRTCRoom.startScreenPreview(panel_main.Handle, null, new Rectangle(0, 0, panel_main.Width, panel_main.Height), null);
  ```

### 15. stopScreenPreview

- 定义：void stopScreenPreview()

- 说明：关闭屏幕分享

- 示例：

  ```c#
  mRTCRoom.stopScreenPreview();
  ```

### 16. addRemoteView

- 定义：void addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID)

- 说明：播放房间内其他会议参与者的视频

- 参数：

| 参数       | 类型        | 描述                  |
| -------- | --------- | ------------------- |
| rendHwnd | IntPtr    | 承载预览画面的 HWND        |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域 |
| userID   | string    | 用户ID                |

- 示例：

  ```c#
  // 打开用户的音视频播放
  mRTCRoom.addRemoteView(panel_display.Handle, new Rectangle(0, 0, panel_display.Width, panel_display.Height), userID);
  ```

### 17. updateRemotePreview

- 定义：void updateRemotePreview(IntPtr rendHwnd, Rectangle rect, string userID)
- 说明：重设指定userID的视频预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域
- 参数：

| 参数       | 类型        | 描述                  |
| -------- | --------- | ------------------- |
| rendHwnd | IntPtr    | 承载预览画面的 HWND        |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域 |
| userID   | string    | 用户ID                |

- 示例：

  ```c#
  // 更新用户的音视频播放
  mRTCRoom.updateRemotePreview(panel_display.Handle, new Rectangle(0, 0, panel_display.Width, panel_display.Height), userID);
  ```

### 18. removeRemoteView

- 定义：void removeRemoteView(string userID)

- 说明：停止播放其他会议参与者的视频

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| userID | string | 用户ID |

- 示例：

  ```c#
  mRTCRoom.removeRemoteView(userID);
  ```

### 19. setMute

- 定义：void setMute(bool mute)

- 说明：静音接口

- 参数：

| 参数   | 类型   | 描述   |
| ---- | ---- | ---- |
| mute | bool | 是否静音 |

- 示例：

  ```c#
  mRTCRoom.setMute(true); // 设置为静音
  ```

### 20. setBeautyStyle

- 定义：void setBeautyStyle(RTCBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel)

- 说明：设置美颜和美白效果

- 参数：

| 参数             | 类型             | 描述                                       |
| -------------- | -------------- | ---------------------------------------- |
| beautyStyle    | RTCBeautyStyle | 参考 RTCRoomUtil.cs 中定义的 RTCBeautyStyle 枚举值 |
| beautyLevel    | int            | 美颜级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |
| whitenessLevel | int            | 美白级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |

- 示例：

  ```c#
  // 自然，美颜度数5，美白度数5
  mRTCRoom.setBeautyStyle(RTCBeautyStyle.RTCROOM_BEAUTY_STYLE_NATURE, 5, 5);
  ```

## ILoginRTCCallback回调接口的详情

### 1. onLogin

- 定义：void onLogin(RTCResult res, RTCAuthData authData)

- 说明：login登录结果的回调
- 参数：

| 参数       | 类型          | 描述                                       |
| -------- | ----------- | ---------------------------------------- |
| res      | RTCResult   | 执行结果，参考 RTCRoomUtil.cs中定义的 RTCResult 类   |
| authData | RTCAuthData | RoomService提供的登录信息，包括IM相关的配置字段，在login成功后，获取到token字段 |

- 示例：

  ```c#
  class LoginDialog : ILoginRTCCallback
  {
  	void onLogin(RTCResult res, RTCAuthData authData)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
          {
          	// 登录失败
          }
          else
          {
          	// 登录成功，保存authData信息
          }
      }
  }

  // 参见RTCRoom.login接口，了解回调的使用
  ...
  ```



## IGetRTCRoomListCallback回调接口的详情

### 1. onGetRoomList

- 定义：void onGetRoomList(RTCResult res, List<RTCRoomData> rooms)

- 说明：获取房间列表的回调

- 参数：

| 参数    | 类型                | 描述                                      |
| ----- | ----------------- | --------------------------------------- |
| res   | RTCResult         | 执行结果，参考 RTCRoomUtil.cs 中定义的 RTCResult 类 |
| rooms | List<RTCRoomData> | 房间信息的列表                                 |

- 示例：

  ```c#
  class RoomListDialog : IGetRTCRoomListCallback
  {
  	void onGetRoomList(RTCResult res, List<RTCRoomData> rooms)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
          {
          	// 查询失败
          }
          else
          {
          	// 查询成功，处理rooms数据
          }
      }
  }

  // 参见RTCRoom.getRoomList接口，了解回调的使用
  ...
  ```



## IRTCRoomCallback回调接口的详情

 参见RTCRoom.setCallback接口，了解如何设置IRTCRoomCallback回调。

### 1. onCreateRoom

- 定义：void onCreateRoom(RTCResult res, string roomID)

- 说明：创建房间的回调

- 参数：

| 参数     | 类型        | 描述                                      |
| ------ | --------- | --------------------------------------- |
| res    | RTCResult | 执行结果，参考 RTCRoomUtil.cs 中定义的 RTCResult 类 |
| roomID | string    | 房间ID                                    |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onCreateRoom(RTCResult res, string roomID)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
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
  }
  ```

### 2. onEnterRoom

- 定义：void onEnterRoom(RTCResult res)

- 说明：进入房间的回调

- 参数：

| 参数   | 类型        | 描述                                      |
| ---- | --------- | --------------------------------------- |
| res  | RTCResult | 执行结果，参考 RTCRoomUtil.cs 中定义的 RTCResult 类 |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onEnterRoom(RTCResult res)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
          {
          	// 进入房间失败，弹框提示
          }
          else
          {
          	// 进入房间成功，紧接着处理onUpdateRoomData回调
          }
      }
      
      ...
  }
  ```

### 3. onUpdateRoomData

- 定义：void onUpdateRoomData(RTCResult res, RTCRoomData roomData)

- 说明：房间信息变更的回调

- 参数：

| 参数       | 类型          | 描述                                       |
| -------- | ----------- | ---------------------------------------- |
| res      | RTCResult   | 执行结果，参考 RTCRoomUtil.cs 中定义的 RTCResult 类  |
| roomData | RTCRoomData | 房间信息，参考 RTCRoomUtil.cs 中定义的 RTCRoomData 类 |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onUpdateRoomData(RTCResult res, RTCRoomData roomData)
      {
      	if (RTCErrorCode.RTCROOM_SUCCESS != res.ec)
          {
          	// 更新失败，弹框提示
          }
          else
          {
          	// 更新成功，根据createRoom还是enterRoom导致这个接口的触发来做出相应的处理
          }
      }
      
      ...
  }
  ```

### 4. onPusherJoin

- 定义：void onPusherJoin(RTCMemberData member)

- 说明：成员进入房间的回调

- 参数：

| 参数     | 类型            | 描述                                       |
| ------ | ------------- | ---------------------------------------- |
| member | RTCMemberData | 成员信息，参考 RTCRoomUtil.cs 中定义的 RTCMemberData 类 |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onPusherJoin(RTCMemberData member)
      {
      	// 成员进入房间，打开成员的画面和音频
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

- 定义：void onPusherQuit(RTCMemberData member)

- 说明：成员退出房间的回调

- 参数：

| 参数     | 类型            | 描述                                       |
| ------ | ------------- | ---------------------------------------- |
| member | RTCMemberData | 成员信息，参考 RTCRoomUtil.cs 中定义的 RTCMemberData 类 |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onPusherQuit(RTCMemberData member)
      {
      	// 成员退出房间，关闭成员的画面和音频
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

- 定义：void onRoomClosed(string roomID)

- 说明：房间解散的回调

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| roomID | string | 房间ID |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onRoomClosed(string roomID)
      {
      	// 提示房间解散，关闭已打开的音视频
      	...
      }
      
      ...
  }
  ```

### 7. onRecvRoomTextMsg

- 定义：void onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg)

- 说明：收到普通文本消息

- 参数：

| 参数         | 类型     | 描述     |
| ---------- | ------ | ------ |
| roomID     | string | 房间ID   |
| userID     | string | 发送者ID  |
| userName   | string | 发送者昵称  |
| userAvatar | string | 发送者头像  |
| message    | string | 文本消息内容 |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg)
      {
      	// IM面板显示文本消息
      }
      
      ...
  }
  ```

### 8. onRecvRoomCustomMsg

- 定义：void onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message)

- 说明：收到自定义消息

- 参数：

| 参数         | 类型     | 描述      |
| ---------- | ------ | ------- |
| roomID     | string | 房间ID    |
| userID     | string | 发送者ID   |
| userName   | string | 发送者昵称   |
| userAvatar | string | 发送者头像   |
| cmd        | string | 自定义cmd  |
| message    | string | 自定义消息内容 |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message)
      {
      	// 解析和处理自定义消息，例如点赞、礼物等
      }
      
      ...
  }
  ```

### 9. onError

- 定义：void onError(RTCResult res, string userID)

- 说明：RTCRoom内部发生错误的通知

- 参数：

| 参数     | 类型        | 描述                                      |
| ------ | --------- | --------------------------------------- |
| res    | RTCResult | 执行结果，参考 RTCRoomUtil.cs 中定义的 RTCResult 类 |
| userID | string    | 用户ID                                    |

- 示例：

  ```c#
  class MainDialog : IRTCRoomCallback
  {
  	void onError(RTCResult res, string userID)
      {
      	// 弹框提示错误，根据错误严重程序，是否解散或者退出会议
      }
      
      ...
  }
  ```
