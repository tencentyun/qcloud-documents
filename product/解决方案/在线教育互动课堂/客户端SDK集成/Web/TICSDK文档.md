##  集成 SDK

在页面中加载以下 SDK。

```
<!-- WebRTC SDK -->
<script src="https://sqimg.qq.com/expert_qq/webrtc/2.6/WebRTCAPI.min.js"></script>
<!-- WebIM SDK -->
<script src="https://sqimg.qq.com/expert_qq/webim/1.7.1/webim.min.js"></script>
<!-- 白板SDK -->
<script src="https://sqimg.qq.com/expert_qq/edu/2.2.1/board_sdk.mini.js"></script>
<!-- COS SDK -->
<script src="https://sqimg.qq.com/expert_qq/cos/5.0.0/cos.mini.js"></script>
<!-- TIC SDK -->
<script src="https://sqimg.qq.com/expert_qq/TICSDK/1.3.0/TICSDK.mini.js"></script>
```
**建议直接使用腾讯云 CDN 加速的 SDK**。


## SDK 简介

TICSDK 是以事件驱动模式的 SDK；接入方只需要调用几个方法，注册与业务相关事件监听，即可完成简单的接入。[TICSDK事件列表](/document/product/680/17885)。

SDK | 主要功能
--------- | ---------
TICSDK | 整个 SDK 的入口类，提供了 SDK 初始化、登录/登出 SDK、创建/加入/销毁课堂、音视频操作、IM 操作以及获取 IMSDK 实例、WebRTCAPI 实例、白板实例的接口。
BoardSDK | 白板提供了画曲线、直线、矩形、圆形、激光笔、橡皮擦、上传 PPT、PDF、等功能。白板接口请参考 [白板 SDK 文档](/document/product/680/17886)。

## 使用流程

TICSDK 使用的一般流程如下：

![业务流程](https://main.qcloudimg.com/raw/30b9189f6c8fe279750cef683e44b56f.png) 


其中 **创建课堂** 为教师角色特有流程，学生角色不需调用。

下面将 SDK 按照功能划分，遵循一般的使用顺序，介绍一下 TICSDK 中各功能的使用方法和注意事项。

### 1. 初始化 SDK

要使用 TICSDK，首先得进行初始化。

```
var ticSdk = new TICSDK();
ticSdk.init();
```

### 2. 监听事件

当初始化完成后，则需要进行事件监听，TICSDK 是以事件驱动模式的 SDK，需要监听关键的事件来实现相关的业务。

```
ticsdk.on(eventName, fn);
```

如：
```
ticSdk.on(TICSDK.CONSTANT.EVENT.IM.KICKED, res => {
  // 业务侧逻辑
});
```

开发者必须监听 **TICSDK.CONSTANT.EVENT.IM.KICKED** 事件，防止被踢下线后无感知。

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
eventName | String | 是 | 监听的事件名
fn | Function | 是 | 事件的回调函数

### 3. 登录

初始化完成之后，需要进行登录，调用登录方法后，则会触发登录成功[TICSDK.CONSTANT.EVENT.IM.LOGIN_SUCC] 或者登录失败[TICSDK.CONSTANT.EVENT.IM.LOGIN_ERROR] 的事件：

```
this.ticSdk.login(loginConfig);
```

loginConfig：

参数名 | 类型 | 是否必填 | 备注 |
---------| ---- | --------- | -----
sdkAppId | Integer | 是 | 腾讯云应用的唯一标识，可以登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)查看
identifier | String | 是 | 用户名
userSig | String | 是 | 登录鉴权信息
identifierNick | String | 否 | IM昵称
userHeadImg | String | 否 | IM头像

该方法传入参数，identifier 和 userSig，identifier 为用户 ID，userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要开发者服务器遵守腾讯云生成 userSig 的规则来生成，并下发给 Web 端。

**在开发调试阶段，用户可以在自己的腾讯云应用控制台使用开发辅助工具，来生成临时的 uid 和 userSig 用于开发测试**。详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

### 4. 创建课堂

调用此方法后则会触发创建课堂成功或者创建课堂失败的事件。

```
ticSdk.createClassroom({
  roomID: 房间号,
  roomType: 'Public'
});
```
参数：

参数名 | 类型 | 是否必填 | 备注
--------- | --------- | -----| ---
roomID | Integer | 是 | 由业务方下发，并保证每次下发的 roomID 是唯一不重复的。
roomType | String | 否，默认 Public | 创建的 IM 群组类型

### 5. 加入课堂

加入课堂可以通过配置 webrtc 相关的参数，来控制是否自动/手动推流，以及是否启用摄像头和麦克风等，也可以配置白板的渲染节点，以及白板初始化颜色，以及是否可以在白板涂鸦等，而 COS 的配置决定了白板是否可以具备上传 PPT、PDF、doc 等文档能力。调用此方法后则会触发加入课堂成功或者加入课堂失败的事件。

```
ticSdk.joinClassroom(roomID, webrtc 推流配置, 白板配置);
```

参数名 | 类型 | 是否必填 | 备注
--------- | --------- | -----| ---
roomID | Integer | 是 | 由业务方下发，并保证每次下发的 roomID 是唯一不重复的。

webrtc 推流配置参数：

|参数	| 类型	| 是否必填 | 描述|
|--------- | --------- | ----- | --------- |
|closeLocalMedia | Boolean | 否，默认 false | 是否关闭自动推流（如果置为 true，则在完成加入/建房操作后，不会发起本端的推流，如需推流，需要由业务主动调推流接口 ）|
|audio | Boolean | 否，默认 true | 是否启用音频采集|
|video | Boolean | 否，默认 true | 是否启用视频采集|
|role | String | 否，默认 user | 角色名，每个角色名对应一组音视频采集的配置，可在 [控制台>画面设定](https://console.cloud.tencent.com/rav) 中配置|
|privateMapKey | String | 如果useCloud为true 则必传| 进房权限|
|useCloud | Boolean | 否，默认 true | true 表示云上环境，false 表示自研环境|
|pureAudioPushMod | Integer | 否 | 纯音频推流模式，需要旁路直播和录制时需要带上此参数 <br/>1 => 本次是纯音频推流,不需要录制 MP3 文件 <br/>2 => 本次是纯音频推流,录制文件为 MP3 |
|recordId | Integer | 否 | 自动录制时业务自定义 ID，Int32，录制回调时给到用户|
|peerAddNotify | Boolean | 否，默认 false | P2P 的建连通知，在建立 P2P 连接前由业务侧决定是否需要连接。需要结合[高级事件通知]的 [onPeerConnectionAdd] 使用 |


白板配置参数：

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
id | String | 是 | 白板渲染的在 dom 节点 ID，并保证该节点有 position: relative 样式，否则可能会引起白板定位异常的问题。
canDraw | Boolean | 否，默认 true | 白板是否可以涂鸦
color | String | 否，默认红色 |画笔颜色，只接受 Hex 色值，如 #ff00ff，大小写不敏感
globalBackgroundColor | String | 否，默认白色 | 全局的白板背景色，只接受 Hex 色值，如 #ff00ff，大小写不敏感


### 6. 使用音视频

#### 6.1 手动推流

如果在进房的时候设置了 closeLocalMedia 为 true，则需要调用 startRTC 进行手动推流。
```
ticSdk.startRTC(opts, succ, fail);
```

参数 |	类型 |	是否必须 |	描述
--------- | --------- | ----- | --------- |
opts |	Object | 	是 |	
succ |	Function | 	否 |	成功回调
fail |	Function | 	否 |	失败回调

opts的参数定义

参数 |类型 | 	是否必须 |	描述
--------- | --------- | ----- | --------- |
stream |	MediaStream | 	否 |	音视频流 MediaStream
role |	String | 	否 |	角色名 ，角色决定了服务器接收该视频流的码率控制

#### 6.2 获取摄像头设备

```
ticsdk.getCameraDevices(callback)
```
参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
callback | function | 是 | 回调函数的参数值返回了当前 PC 上可用的摄像头

#### 6.3 切换摄像头

```
ticSdk.switchCamera(device);
```
| 参数 | 类型 | 描述 |
| --- | --- | --- |
| device | Object | 摄像头设备 |

#### 6.4 获取麦克风

```
ticsdk.getMicDevices(callback)
```
参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
callback | function | 是 | 回调函数的参数值返回了当前 PC 上可用的麦克风

#### 6.5 切换麦克风

```
ticSdk.switchMic(device);
```
| 参数 | 类型 | 描述 |
| --- | --- | --- |
| device | Object | 麦克风设备 |

#### 6.6 启用/关闭摄像头

```
this.ticksdk.enableCamera();
```
| 参数 | 类型 | 描述 |
| --- | --- | --- |
| true | Boolean | 开启摄像头； false 关闭摄像头 |

#### 6.7 启用/关闭麦克风

```
this.ticksdk.enableMic();
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| true | Boolean | 开启麦克风； false 关闭麦克风 |


### 7. 使用互动白板

白板的相关操作直接通过 TICSDK 提供的获取白板实例接口获取白板实例来操作白板，TICSDK 不做任何封装。详见 [白板 SDK 文档](/document/product/680/17886)。

### 8. 使用 PPT

使用白板前，需确认已 [开通白板服务](/document/product/680/14782)。

#### 8.1 上传文件

TICSDK 支持 PPT、PDF、doc 文档上传、并且提供预览服务。

```
ticSdk.addFile(file, succ, fail)
```

参数:

| 参数 |   类型     | 是否必填 |说明 |
| --- |----------- | ---- |------------------ |
| file |  File    | 是 | 文件对象，通常这样获取 document.getElementById('file_input').files[0] |
| succ |  Function    | 否 | 上传成功的回调 |
| fail |  Function    | 否 | 上传失败的回调 |

#### 8.2 上传图片

```
ticSdk.addImgFile(imgFile, succ, fail)
```

参数:

| 参数 |   类型     | 是否必填 |说明 |
| --- |----------- | ---- |------------------ |
| file |  File    | 是 | 文件对象，通常这样获取document.getElementById('file_input').files[0] |
| succ |  Function    | 否 | 上传成功的回调 |
| fail |  Function    | 否 | 上传失败的回调 |


### 9. 收发消息

IM 相关的接口封装于腾讯云通信 IMSDK，通过监听消息事件的回调来处理消息。

#### 9.1 普通文本

```
ticSdk.sendTextMessage(msgText, receiveUserIdentifier)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msgText | String | 是 | 要发送的文本内容
receiveUserIdentifier | String | 否 | 接收方的 identifier 不填，表示给课堂群组发 IM 消息

填写`receiveUserIdentifier`，会收到`TICSDK.CONSTANT.EVENT.IM.RECEIVE_C2C_MSG`事件，不填则会收到`TICSDK.CONSTANT.EVENT.IM.RECEIVE_CHAT_ROOM_MSG`事件


#### 9.2 自定义消息

```
ticSdk.sendCustomTextMessage(msgObj, receiveUserIdentifier)
```
参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msgObj | Object | 是 | 自定义文本消息对象 msgObj = {data: '发送的内容', desc: '描述', ext: '扩展'}
receiveUserIdentifier | string | 否 | 接收方的identifier

填写`receiveUserIdentifier`，会收到`TICSDK.CONSTANT.EVENT.IM.RECEIVE_C2C_MSG`事件，不填则会收到`TICSDK.CONSTANT.EVENT.IM.RECEIVE_CHAT_ROOM_MSG`事件


### 10. 退出课堂

调用退出课堂，只是调用者自己退出课堂。调用此方法后，则会触发退出课堂成功或者退出课堂失败的事件。

```
ticSdk.quitClassroom();
```

### 11. 销毁课堂

调用销毁课堂，则会真正将课堂销毁，清除白板所有数据，解散课堂 IM 群组；本方法只能由课堂的创建者调用，非创建则调用则不能销毁课堂，并触发销毁课堂失败的事件。调用此方法后，则会触发销毁课堂成功或者销毁课堂失败的事件。

```
ticSdk.destroyClassRoom()
```

### 12. 注销事件监听

```
ticsdk.off(eventName, fn);
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
eventName | String | 是 | 监听的事件名
fn | Function | 否 | 要注销的回调函数， 不传则表示该事件的回调函数全部注销


### 13. 登出

调用登出方法后，会触发登出成功 `[TICSDK.CONSTANT.EVENT.IM.LOGOUT_SUCC]` 或者登出失败`[TICSDK.CONSTANT.EVENT.IM.LOGOUT_ERROR]`的事件：

```
ticSdk.logout();
```

### 14. 获取 TIC 内部对象实例

#### 14.1 获取白板实例

获取白板实例， 白板实例需要在监听到进房成功事件`[TICSDK.CONSTANT.EVENT.TIC.JOIN_CLASS_ROOM_SUCC]`后才返回。

```
ticsdK.getBoardInstance()
```

#### 14.2 获取 IM 实例

初始化 TICKSDK 后即可获得 IM 实例。

```
ticsdK.getImInstance()
```

#### 14.3 获取 WebRTC 实例

获取 WebRTC 实例， WebRTC 实例需要在监听到进房成功事件`[TICSDK.CONSTANT.EVENT.TIC.JOIN_CLASS_ROOM_SUCC]`后才返回。

```
ticsdK.getWebRTCInstance()
```


