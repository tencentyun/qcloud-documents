# 直播+连麦（LiveRoom ）

**直播+连麦** 是在 **秀场直播** 和 **在线教育** 场景中经常使用的直播模式，它既能支持高并发和低成本的在线直播，又能通过连麦实现主播和观众之间的视频通话互动，具有极强的场景适用性。

![img](https://main.qcloudimg.com/raw/4032376146a41d3597d9a28350b542b5.jpg)

腾讯云基于 [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606) 组件实现“直播 + 连麦”功能，它分成 Client 和 Server 两个部分（都是开源的），对接攻略请参考 [DOC](https://cloud.tencent.com/document/product/454/14606)，本文档主要是详细列出了 Client 端的 API 列表：

> 在腾讯云官网 [下载](https://cloud.tencent.com/document/product/454/7873#Windows) SDK 开发包，在SDK\Rooms\LiveRoom中，包括LiveRoom相关的头文件和源码文件。

## LiveRoom

| 名称                                       | 描述                                       |
| ---------------------------------------- | ---------------------------------------- |
| instance()                               | 获取LiveRoom单例，通过单例调用LiveRoom的接口           |
| setCallback(ILiveRoomCallback callback)  | 设置回调 LiveRoom 的回调代理，监听 LiveRoom 的内部状态和接口的执行结果 |
| login(string serverDomain, LiveAuthData authData, ILoginLiveCallback callback) | 登录业务服务器RoomService，登录后才能够正常使用其他接口和使用IM功能 |
| logout()                                 | 登出业务服务器RoomService，请注意在leaveRoom调用后，再调用logout，否则leaveRoom会调用失败 |
| getRoomList(int index, int cnt, IGetLiveRoomListCallback callback) | 获取房间列表，房间数量比较多时，可以分页获取                   |
| getAudienceList(string roomID)           | 获取观众列表，只返回最近进入房间的 30 位观众                 |
| createRoom(string roomID, string roomInfo) | 创建房间，后台的房间列表中会添加一个新房间，同时主播端会进入推流模式       |
| enterRoom(string roomID, IntPtr rendHwnd, Rectangle rect) | 进入房间                                     |
| leaveRoom()                              | 离开房间，如果是大主播，这个房间会被后台销毁，如果是小主播或者观众，不影响其他人继续观看 |
| sendRoomTextMsg(string msg)              | 发送普通文本消息，比如直播场景中，发送弹幕                    |
| sendRoomCustomMsg(string cmd, string msg) | 发送自定义消息，比如直播场景中，发送点赞、送花等消息               |
| startLocalPreview(IntPtr rendHwnd, Rectangle rect) | 启动默认的摄像头预览                               |
| updateLocalPreview(IntPtr rendHwnd, Rectangle rect) | 重设摄像头预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域 |
| stopLocalPreview()                       | 关闭摄像头预览                                  |
| startScreenPreview(IntPtr rendHwnd, IntPtr captureHwnd, Rectangle renderRect, Rectangle captureRect) | 启动屏幕分享                                   |
| stopScreenPreview()                      | 关闭屏幕分享                                   |
| addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID) | 播放房间内其他主播的视频                             |
| updateRemotePreview(IntPtr rendHwnd, Rectangle rect, string userID) | 重设指定userID的视频预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域 |
| removeRemoteView(string userID)          | 停止播放其他主播的视频                              |
| setMute(bool mute)                       | 静音接口                                     |
| setVideoQuality(LiveVideoQuality quality, LiveAspectRatio ratio) | 设置画面质量预设选项                               |
| setBeautyStyle(LiveBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel) | 设置美颜和美白效果                                |
| requestJoinPusher()                      | 观众端发起请求连麦                                |
| acceptJoinPusher(string userID)          | 大主播接受连麦请求，并通知给连麦发起方                      |
| rejectJoinPusher(string userID, string reason) | 大主播拒绝连麦请求，并通知给连麦发起方                      |
| kickoutSubPusher(string userID)          | 大主播踢掉某一个小主播                              |

## ILoginLiveCallback

| 名称                                       | 描述           |
| ---------------------------------------- | ------------ |
| onLogin(LiveResult res, LiveAuthData authData) | login登录结果的回调 |

## IGetLiveRoomListCallback

| 名称                                       | 描述        |
| ---------------------------------------- | --------- |
| onGetRoomList(LiveResult res, List<LiveRoomData> rooms) | 获取房间列表的回调 |

## ILiveRoomCallback

| 名称                                       | 描述                |
| ---------------------------------------- | ----------------- |
| onCreateRoom(LiveResult res, string roomID) | 创建房间的回调           |
| onEnterRoom(LiveResult res)              | 进入房间的回调           |
| onUpdateRoomData(LiveResult res, LiveRoomData roomData) | 房间信息变更的回调         |
| void onGetAudienceList(LiveResult res, List<LiveAudienceData> audiences) | 查询观众列表的回调         |
| onPusherJoin(LiveMemberData member)      | 连麦观众进入房间的回调       |
| void onPusherQuit(LiveMemberData member) | 连麦观众退出房间的回调       |
| onRoomClosed(string roomID)              | 房间解散的回调           |
| onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg) | 收到普通文本消息          |
| onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message) | 收到自定义消息           |
| onError(LiveResult res, string userID)   | LiveRoom内部发生错误的通知 |
| onRecvJoinPusherRequest(string roomID, string userID, string userName, string userAvatar) | 接收到连麦请求           |
| onRecvAcceptJoinPusher(string roomID, string msg) | 接收到接受连麦请求的回复      |
| onRecvRejectJoinPusher(string roomID, string msg) | 接收到拒绝连麦请求的回复      |
| onRecvKickoutSubPusher(string roomID)    | 接收大主播踢小主播的通知      |

## LiveRoom对象接口的详情

### 1. instance

- 定义：static LiveRoom instance()

- 说明：获取LiveRoom单例，通过单例调用LiveRoom的接口

- 示例：

  ```c#
  LiveRoom m_liveRoom = null;
  m_liveRoom = LiveRoom.instance();
  ```

### 2. setCallback

- 定义：void setCallback(ILiveRoomCallback callback)

- 说明：设置回调 LiveRoom 的回调代理，监听 LiveRoom 的内部状态和接口的执行结果

- 参数：

| 参数       | 类型                | 描述                        |
| -------- | ----------------- | ------------------------- |
| callback | ILiveRoomCallback | ILiveRoomCallback 类型的代理接口 |

- 示例：

  ```c#
  public class MainDialog : ILiveRoomCallback
  {
      MainDialog()
      {
          m_liveRoom.setCallback(this);	// 设置回调
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

- 定义：void login(string serverDomain, LiveAuthData authData, ILoginLiveCallback callback)

- 说明：登录业务服务器RoomService，登录后才能够正常使用其他接口和使用IM功能

- 参数：

| 参数           | 类型                 | 描述                                       |
| ------------ | ------------------ | ---------------------------------------- |
| serverDomain | string             | RoomService的URL地址，安全起见，建议访问https加密链接， 参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW) |
| authData     | LiveAuthData       | RoomService提供的登录信息，包括IM相关的配置字段，在login成功后，获取到token字段，参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW) |
| callback     | ILoginLiveCallback | ILoginLiveCallback 类型的代理接口，回调login的结果    |

- 示例：

  ```c#
  string serverDomain = "https://roomtest.qcloud.com/weapp/live_room";

  m_authData.sdkAppID = sdkAppID;
  m_authData.accountType = accountType;
  m_authData.userID = userID;
  m_authData.userSig = userSig;
  m_authData.userName = userName;
  m_authData.userAvatar = userAvatar;
  m_authData.token = token;

  // 该类实现ILoginCallback接口，获取login结果
  m_liveRoom.login(serverDomain, m_authData, this);
  ```

### 4. logout

- 定义：void logout();

- 说明：登出业务服务器RoomService，请注意在leaveRoom调用后，再调用logout，否则leaveRoom会调用失败

- 示例：

  ```c#
  m_liveRoom.logout();
  ```

### 5. getRoomList

- 定义：void getRoomList(int index, int cnt, IGetLiveRoomListCallback callback)

- 说明：获取房间列表，房间数量比较多时，可以分页获取

- 参数：

| 参数       | 类型                       | 描述                                       |
| -------- | ------------------------ | ---------------------------------------- |
| index    | int                      | 分页获取，初始默认可设置为0，后续获取为起始房间索引（如第一次设置index=0, cnt=5,获取第二页时可用index=5） |
| count    | int                      | 每次调用，最多返回房间个数；0表示所有满足条件的房间               |
| callback | IGetLiveRoomListCallback | IGetLiveRoomListCallback 类型的代理接口，查询结果的回调 |

- 示例：

  ```c#
  // 此处从index=0开始，最多查询20个房间，该类实现IGetRoomListCallback接口，获取查询结果
  m_liveRoom.getRoomList(0, 20, this);
  ```

### 6. getAudienceList

- 定义：void getAudienceList(string roomID)
- 说明：获取观众列表，只返回最近进入房间的 30 位观众
- 参数：

| 参数     | 类型     | 描述                             |
| ------ | ------ | ------------------------------ |
| roomID | string | 房间ID，在 getRoomList 接口房间列表中查询得到 |

- 示例：

```c#
m_liveRoom.getRoomList(roomID);
```

### 7. createRoom

- 定义：void createRoom(string roomID, string roomInfo)

- 说明：创建房间，后台的房间列表中会添加一个新房间，同时主播端会进入推流模式

- 参数：

| 参数       | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| roomID   | string | 房间ID，若传入空字符串，则后台会为您分配roomID，否则，传入的roomID作为这个房间的ID |
| roomInfo | string | 自定义数据，该字段包含在房间信息中，推荐您将 roomInfo 定义为 json 格式，这样可以有很强的扩展性 |

- 示例：

  ```c#
  // 后台会为您分配roomID
  m_liveRoom.createRoom("", "{\"roomName\": \"My first room\"}");
  ```

### 8. enterRoom

- 定义：void enterRoom(string roomID, IntPtr rendHwnd, Rectangle rect)

- 说明：进入房间

- 参数：

| 参数       | 类型        | 描述                                       |
| -------- | --------- | ---------------------------------------- |
| roomID   | string    | roomID - 要进入的房间ID，在 getRoomList 接口房间列表中查询得到 |
| rendHwnd | IntPtr    | 承载预览画面的 HWND                             |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域                      |

- 示例：

  ```c#
  // 在form整个窗口中渲染
  Rectangle rect = new Rectangle(0, 0, form.Width, form.Height);
  m_liveRoom.enterRoom(roomID, form.Handle, rect);
  ```

### 9. leaveRoom

- 定义：void leaveRoom()

- 说明：离开房间，如果是大主播，这个房间会被后台销毁，如果是小主播或者观众，不影响其他人继续观看

- 示例：

  ```c#
  m_liveRoom.leaveRoom();
  ```

### 10. sendRoomTextMsg

- 定义：void sendRoomTextMsg(string msg)

- 说明：发送普通文本消息，比如直播场景中，发送弹幕

- 参数：

| 参数   | 类型     | 描述   |
| ---- | ------ | ---- |
| msg  | string | 文本消息 |

- 示例：

  ```c#
  m_liveRoom.sendRoomTextMsg("Hello LiveRoom");
  ```

### 11. sendRoomCustomMsg

- 定义：void sendRoomCustomMsg(string cmd, string msg)

- 说明：发送自定义消息，比如直播场景中，发送点赞、送花等消息

- 参数：

| 参数   | 类型     | 描述                 |
| ---- | ------ | ------------------ |
| cmd  | string | 自定义cmd，收发双方协商好的cmd |
| msg  | string | 自定义消息              |

- 示例：

  ```c#
  // 假设收发双方协商好的cmd有Smile, Anger
  m_liveRoom.sendRoomCustomMsg("Smile", "I am hungry");
  ```

### 12. startLocalPreview

- 定义：void startLocalPreview(IntPtr rendHwnd, Rectangle rect)

- 说明：启动默认的摄像头预览

- 参数：

| 参数       | 类型        | 描述                                       |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr    | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = null时无需预览视频 |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域                      |

- 示例：

  ```c#
  // 在form整个窗口中渲染
  Rectangle rect = new Rectangle(0, 0, form.Width, form.Height);
  m_liveRoom.startLocalPreview(form.Handle, rect);
  ```

### 13. updateLocalPreview

- 定义：void updateLocalPreview(IntPtr rendHwnd, Rectangle rect)

- 说明：重设摄像头预览区域，当您指定的本地 HWND 的窗口尺寸发生变化时，可以通过这个函数重新调整视频渲染区域

- 参数：

| 参数       | 类型        | 描述                                       |
| -------- | --------- | ---------------------------------------- |
| rendHwnd | IntPtr    | 承载预览画面的 HWND，目前 SDK 是采用 OpenGL 向 HWND 上绘制图像的,rendHwnd = null时无需预览视频 |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域                      |

- 示例：

  ```c#
  // 在form整个窗口中渲染
  Rectangle rect = new Rectangle(0, 0, form.Width, form.Height);
  m_liveRoom.updateLocalPreview(form.Handle, rect);
  ```

### 14. stopLocalPreview

- 定义：void stopLocalPreview()

- 说明：关闭摄像头预览

- 示例：

  ```c#
  m_liveRoom.stopLocalPreview();
  ```

### 15. startScreenPreview

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
  // 在form整个窗口中渲染
  Rectangle renderRect = new Rectangle(0, 0, rendForm.Width, rendForm.Height);

  // 录取整个窗口的画面
  Rectangle captureRect = new Rectangle(0, 0, captureForm.Width, captureForm.Height);

  m_liveRoom.startScreenPreview(rendForm.Handle, captureForm.Handle, renderRect, captureRect);
  ```

### 16. stopScreenPreview

- 定义：void stopScreenPreview()

- 说明：关闭屏幕分享

- 示例：

  ```c#
  m_liveRoom.stopScreenPreview();
  ```

### 17. addRemoteView

- 定义：void addRemoteView(IntPtr rendHwnd, Rectangle rect, string userID)

- 说明：播放房间内其他主播的视频

- 参数：

| 参数       | 类型        | 描述                  |
| -------- | --------- | ------------------- |
| rendHwnd | IntPtr    | 承载预览画面的 HWND        |
| rect     | Rectangle | 指定视频图像在 HWND 上的渲染区域 |
| userID   | string    | 用户ID                |

- 示例：

  ```c#
  // 在form整个窗口中渲染
  Rectangle renderRect = new Rectangle(0, 0, form.Width, form.Height);

  // 打开用户的音视频播放
  m_liveRoom.addRemoteView(form.Handle，rect, userID);
  ```

### 18. updateRemotePreview

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
  // 在form整个窗口中渲染
  Rectangle renderRect = new Rectangle(0, 0, form.Width, form.Height);

  // 重设指定userID的视频预览区域
  m_liveRoom.updateRemotePreview(form.Handle, rect, userID);
```

### 18. removeRemoteView

- 定义：void removeRemoteView(string userID)

- 说明：停止播放其他主播的视频

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| userID | string | 用户ID |

- 示例：

  ```c#
  m_liveRoom.removeRemoteView(userID);
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
  m_liveRoom.setMute(true); // 设置为静音
  ```

### 20. setVideoQuality

- 定义：void setVideoQuality(LiveVideoQuality quality, LiveAspectRatio ratio)

- 说明：设置推流的画面质量选项

- 参数：

| 参数      | 类型               | 描述                                       |
| ------- | ---------------- | ---------------------------------------- |
| quality | LiveVideoQuality | 画质，参考 LiveRoomUtil.h 中定义的 LiveVideoQuality 枚举值 |
| ratio   | LiveAspectRatio  | 宽高比，参考 LiveRoomUtil.h 中定义的 LiveAspectRatio 枚举值 |

- 示例：

  ```c#
  // 设置画质为高清，宽高比为4:3
  m_liveRoom.setVideoQuality(LIVEROOM_VIDEO_QUALITY_HIGH_DEFINITION, LIVEROOM_ASPECT_RATIO_4_3);
  ```

### 21. setBeautyStyle

- 定义：void setBeautyStyle(LiveBeautyStyle beautyStyle, int beautyLevel, int whitenessLevel)

- 说明：设置美颜和美白效果

- 参数：

| 参数             | 类型             | 描述                                       |
| -------------- | -------------- | ---------------------------------------- |
| beautyStyle    | TXEBeautyStyle | 参考 LiveRoomUtil.h 中定义的 LiveBeautyStyle 枚举值 |
| beautyLevel    | int            | 美颜级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |
| whitenessLevel | int            | 美白级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |

- 示例：

  ```c#
  // 自然，美颜度数5，美白度数5
  m_liveRoom.setBeautyStyle(TXE_BEAUTY_STYLE_NATURE, 5, 5);
  ```

### 22. requestJoinPusher

- 定义：void requestJoinPusher()

- 说明：观众端发起请求连麦

- 示例：

  ```c#
  m_liveRoom.requestJoinPusher();
  ```

### 23. acceptJoinPusher

- 定义：void acceptJoinPusher(string userID)

- 说明：大主播接受连麦请求，并通知给连麦发起方

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| userID | string | 用户ID |

- 示例：

  ```c#
  m_liveRoom.acceptJoinPusher(userID);
  ```

### 24. rejectJoinPusher

- 定义：void rejectJoinPusher(string userID, string reason)

- 说明：大主播拒绝连麦请求，并通知给连麦发起方

- 参数：

| 参数     | 类型     | 描述    |
| ------ | ------ | ----- |
| userID | string | 用户ID  |
| reason | string | 拒绝的原因 |

- 示例：

  ```c#
  m_liveRoom.acceptJoinPusher(userID, reason);
  ```

### 25. kickoutSubPusher

- 定义：void kickoutSubPusher(string userID)

- 说明：大主播踢掉某一个小主播

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| userID | string | 用户ID |

- 示例：

  ```c#
  m_liveRoom.kickoutSubPusher(userID);
  ```



## ILoginLiveCallback回调接口的详情

### 1. onLogin

- 定义：void onLogin(LiveResult res, LiveAuthData authData)

- 说明：login登录结果的回调

- 参数：

| 参数       | 类型           | 描述                                       |
| -------- | ------------ | ---------------------------------------- |
| res      | LiveResult   | 执行结果，参考 LiveRoomUtil.h 中定义的 LiveResult 类 |
| authData | LiveAuthData | RoomService提供的登录信息，包括IM相关的配置字段，在login成功后，获取到token字段 |

- 示例：

  ```c#
  class LoginDialog : ILoginLiveCallback
  {
  	void ILoginLiveCallback.onLogin(LiveResult res, LiveAuthData authData)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// 登录失败
          }
          else
          {
          	// 登录成功，保存authData信息
          }
      }
  }

  // 参见LiveRoom::login接口，了解回调的使用
  ...
  ```



## IGetLiveRoomListCallback回调接口的详情

### 1. onGetRoomList

- 定义：void onGetRoomList(LiveResult res, List<LiveRoomData> rooms)

- 说明：获取房间列表的回调

- 参数：

| 参数    | 类型                 | 描述                                       |
| ----- | ------------------ | ---------------------------------------- |
| res   | LiveResult         | 执行结果，参考 LiveRoomUtil.h 中定义的 LiveResult 类 |
| rooms | List<LiveRoomData> | 房间信息的列表                                  |

- 示例：

  ```c#
  class RoomListDialog : IGetLiveRoomListCallback
  {
  	void IGetRoomListCallback.onGetRoomList(LiveResult res, List<LiveRoomData> rooms)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// 查询失败
          }
          else
          {
          	// 查询成功，处理rooms数据
          }
      }
  }

  // 参见LiveRoom::getRoomList接口，了解回调的使用
  ...
  ```



## ILiveRoomCallback回调接口的详情

 参见LiveRoom::setCallback接口，了解如何设置ILiveRoomCallback回调。

### 1. onCreateRoom

- 定义：void onCreateRoom(LiveResult res, string roomID)

- 说明：创建房间的回调

- 参数：

| 参数     | 类型         | 描述                                       |
| ------ | ---------- | ---------------------------------------- |
| res    | LiveResult | 执行结果，参考 LiveRoomUtil.h 中定义的 LiveResult 类 |
| roomID | string     | 房间ID                                     |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onCreateRoom(LiveResult res, string roomID)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
          {
          	// 创建房间失败，弹框提示
          }
          else
          {
          	// 创建房间成功，其他观众可以观看直播
          	// 紧接着处理onUpdateRoomData回调
          }
      }
      
      ...
  }
  ```

### 2. onEnterRoom

- 定义：void onEnterRoom(LiveResult res)

- 说明：进入房间的回调

- 参数：

| 参数   | 类型         | 描述                                       |
| ---- | ---------- | ---------------------------------------- |
| res  | LiveResult | 执行结果，参考 LiveRoomUtil.h 中定义的 LiveResult 类 |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onEnterRoom(LiveResult res)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
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

- 定义：void onUpdateRoomData(LiveResult res, LiveRoomData roomData)

- 说明：房间信息变更的回调

- 参数：

| 参数       | 类型           | 描述                                       |
| -------- | ------------ | ---------------------------------------- |
| res      | LiveResult   | 执行结果，参考 LiveRoomUtil.h 中定义的 LiveResult 类 |
| roomData | LiveRoomData | 房间信息，参考 LiveRoomUtil.h 中定义的 LiveRoomData 类 |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onUpdateRoomData(LiveResult res, LiveRoomData roomData)
      {
      	if (LIVEROOM_SUCCESS != res.ec)
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

### 4. onGetAudienceList

- 定义：void onGetAudienceList(LiveResult res, List<LiveAudienceData> audiences)
- 说明：查询观众列表的回调
- 参数：

| 参数        | 类型                     | 描述                                       |
| --------- | ---------------------- | ---------------------------------------- |
| res       | LiveResult             | 执行结果，参考 LiveRoomUtil.h 中定义的 LiveResult 类 |
| audiences | List<LiveAudienceData> | 观众信息的列表                                  |

- 示例：

```c#
class MainDialog : ILiveRoomCallback
{
	void ILiveRoomCallback.onGetAudienceList(LiveResult res, List<LiveAudienceData> audiences)
    {
    	if (LIVEROOM_SUCCESS != res.ec)
        {
        	// 查询失败，弹框提示
        }
        else
        {
        	// 查询成功，列表更新到UI
        }
    }
    
    ...
}
```

### 5. onPusherJoin

- 定义：void onPusherJoin(LiveMemberData member)

- 说明：连麦观众进入房间的回调

- 参数：

| 参数     | 类型             | 描述                                       |
| ------ | -------------- | ---------------------------------------- |
| member | LiveMemberData | 成员信息，参考 LiveRoomUtil.h 中定义的 LiveMemberData 类 |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onPusherJoin(LiveMemberData member)
      {
      	// 通常连麦观众请求连麦，打开连麦观众的画面和音频
      	m_liveRoom.addRemoteView(rendHwnd, rect, member.userID);
      	...
      }
      
      ...
  }
  ```

### 6. onPusherQuit

- 定义：void onPusherQuit(LiveMemberData member)

- 说明：连麦观众退出房间的回调

- 参数：

| 参数     | 类型             | 描述                                       |
| ------ | -------------- | ---------------------------------------- |
| member | LiveMemberData | 成员信息，参考 LiveRoomUtil.h 中定义的 LiveMemberData 类 |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onPusherQuit(LiveMemberData member)
      {
      	// 通常连麦观众关闭连麦，关闭连麦观众的画面和音频
      	m_liveRoom.removeRemoteView(member.userID);
      	...
      }
      
      ...
  }
  ```

### 7. onRoomClosed

- 定义：void onRoomClosed(string roomID)

- 说明：房间解散的回调

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| roomID | string | 房间ID |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRoomClosed(string roomID)
      {
      	// 提示房间解散，关闭已打开的音视频
      	...
      }
      
      ...
  }
  ```

### 8. onRecvRoomTextMsg

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
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRoomTextMsg(string roomID, string userID, string userName, string userAvatar, string msg)
      {
      	// IM面板显示文本消息
      }
      
      ...
  }
  ```

### 9. onRecvRoomCustomMsg

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
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRoomCustomMsg(string roomID, string userID, string userName, string userAvatar, string cmd, string message)
      {
      	// 解析和处理自定义消息，例如点赞、礼物等
      }
      
      ...
  }
  ```

### 10. onError

- 定义：void onError(LiveResult res, string userID)

- 说明：LiveRoom内部发生错误的通知

- 参数：

| 参数     | 类型         | 描述                                       |
| ------ | ---------- | ---------------------------------------- |
| res    | LiveResult | 执行结果，参考 LiveRoomUtil.h 中定义的 LiveResult 类 |
| userID | string     | 用户ID                                     |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onError(LiveResult res, string userID)
      {
      	// 弹框提示错误，根据错误严重程度，是否关闭直播
      }
      
      ...
  }
  ```

### 11. onRecvJoinPusherRequest

- 定义：void onRecvJoinPusherRequest(string roomID, string userID, string userName, string userAvatar)

- 说明：接收到连麦请求

- 参数：

| 参数         | 类型     | 描述    |
| ---------- | ------ | ----- |
| roomID     | string | 房间ID  |
| userID     | string | 发送者ID |
| userName   | string | 发送者昵称 |
| userAvatar | string | 发送者头像 |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvJoinPusherRequest(string roomID, string userID, string userName, string userAvatar)
      {
      	// 大主播接收到观众的连麦请求
      	// 先判断roomID是否合法
      	// UI显示谁发起请求的提示
      	// 大主播可以通过acceptJoinPusher接受连麦，或者rejectJoinPusher拒绝连麦
      }
      
      ...
  }
  ```

### 12. onRecvAcceptJoinPusher

- 定义：void onRecvAcceptJoinPusher(string roomID, string msg)

- 说明：接收到接受连麦请求的回复

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| roomID | string | 房间ID |
| msg    | string | 消息   |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvAcceptJoinPusher(string roomID, string msg)
      {
      	// 连麦观众接收到大主播的接收连麦的回复
      	// 先判断roomID是否合法
      	// 处理msg
      }
      
      ...
  }
  ```

  ​

### 13. onRecvRejectJoinPusher

- 定义：void onRecvRejectJoinPusher(string roomID, string msg)

- 说明：接收到拒绝连麦请求的回复

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| roomID | string | 房间ID |
| msg    | string | 消息   |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRejectJoinPusher(string roomID, string msg)
      {
      	// 连麦观众接收到大主播的拒绝连麦的回复
      	// 先判断roomID是否合法
      	// 处理msg
      }
      
      ...
  }
  ```

  ​

### 14. onRecvKickoutSubPusher

- 定义：void onRecvKickoutSubPusher(string roomID)

- 说明：接收大主播踢小主播的通知

- 参数：

| 参数     | 类型     | 描述   |
| ------ | ------ | ---- |
| roomID | string | 房间ID |

- 示例：

  ```c#
  class MainDialog : ILiveRoomCallback
  {
  	void ILiveRoomCallback.onRecvRejectJoinPusher(string roomID, string msg)
      {
      	// 大主播踢掉某个正在连麦的观众
      	// 先判断roomID是否合法
      	// 处理msg
      }
      
      ...
  }
  ```

  ​