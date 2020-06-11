组件 trtc-electron-education 是针对实时互动课堂场景中使用实时音视频 TRTC 和即时通信 IM 能力的二次封装，在封装基本的音视频聊天、屏幕分享能力的同时，针对在线教育场景封装了老师开始问答、学生举手、老师邀请学生上台回答、结束回答等相关能力。
trtc-electron-education 是一个开源的 npm 组件，依赖腾讯云的两个闭源 SDK，具体实现过程请参见 [实时互动课堂(Electron)](https://cloud.tencent.com/document/product/647/45465)。
* TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
* IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。

## 组件接入
```
// yarn 方式引入
yarn add trtc-electron-education
// npm 方式引入
npm i trtc-electron-education --save
```

## 组件参数

必填的关键参数介绍如下表所示。

| 参数 |类型|说明|
| ----- | ----- | ----- |
|sdkAppId|number|必填参数，您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。|
|userID|string|必填参数，用户 ID，可以由您的帐号体系指定。|
|userSig|string|必填参数，身份签名（相当于登录密码），由 userID 计算得出，具体计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。|

## 初始化示例

```typescript
import TrtcElectronEducation from 'trtc-electron-education';
const rtcClient = new TrtcElectronEducation({
     sdkAppId: 1400***803,
     userID: '123'
     userSig: 'eJwtzM9****-reWMQw_'
 });
```

## 组件概览
### 基础函数

#### on(EventCode, handler, context)
用于监听组件派发的事件。  
参数：

|参数名|	类型	|说明|
| ----- | ----- | ----- |
|EventCode|	String|	事件码|
|handler|	Function|	监听函数|
|context|	Object|	当前执行上下文|

示例：
```typescript
const EVENT = rtcClient.EVENT
rtcClient.on(EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

#### off(EventCode, handler)
取消事件监听。  
参数：

|参数名|	类型	|说明|
| ----- | ----- | ----- |
|EventCode|	String|事件码|
|handler|	Function|需要取消的具名监听函数|

示例：
```typescript
const EVENT = rtcClient.EVENT
rtcClient.off(EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

<span id="createRoom"></span>
#### createRoom(params: CreateRoomParams)
老师创建教室。  
参数：

|参数名|	类型	|说明|
| ----- | ----- | ----- |
|classId|	number|	教室 ID|
|nickName|	string|	昵称|
|avatar|	string|	头像地址，可以不填|

示例：
```typescript
interface CreateRoomParams {
  classId: number; // 教室 ID
  nickName: string; // 昵称
  avatar?:string; // 头像地址
}
rtcClient.createRoom(params).then(() => {
})
```

#### destroyRoom(classId: number)
老师退出教室，销毁房间。
参数：

|参数名|	类型	| 说明|
| ----- | ----- | ----- |
|classId|	number|	 教室 ID|

示例：
```typescript
rtcClient.destroyRoom(classId)
```

<span id="enterRoom"></span>
#### enterRoom(params: EnterRoomParams)
老师开始上课，学生进入教室，准备听课。
参数：

|参数名|	类型	| 说明|
| ----- | ----- | ----- |
|classId|	number|	 教室 ID|
|nickName|	string| 昵称|
|role|	string|	 角色，teacher 表示老师，student 表示学生|
|avatar|	string|	 头像地址，可以不填|

示例：
```typescript
interface EnterRoomParams {
  role: string; // 角色
  classId: number; // 教室 ID
  nickName?: string; // 昵称
  avatar?:string; // 头像地址
}
rtcClient.enterRoom(params).then(() => {
})
```

#### exitRoom(role:string, classId: number)
老师下课，学生退出课堂。
参数：

|参数名|	类型	| 	说明|
| ----- | ----- | ----- |
|classId|	number|	 教室 ID|
|role|	string| 角色，teacher 表示老师，student 表示学生|

示例：
```typescript
rtcClient.exitRoom(role, classId);
```

### 举手操作环节函数
<span id="startQuestionTime"></span>
#### startQuestionTime(classId: number)
老师开始问答时间，老师端广播通知，学生收到开始问答事件， 开启举手功能。
参数：

|参数名|	类型	| 说明|
| ----- | ----- | ----- |
|classId|	number|	 教室 ID|

示例：
```typescript
rtcClient.startQuestionTime(classId)
```

<span id="raiseHand"></span>
#### raiseHand()
学生举手，学生发送举手通知，老师端收到学生举手通知。  
参数：无
示例：
```typescript
rtcClient.raiseHand()
```

<span id="inviteToPlatform"></span>
#### inviteToPlatform(userID: string)
老师邀请学生上台回答，老师端选择举手列表里的学生 userID ，发送邀请通知，学生端收到邀请上台回答事件，受邀请的学生开麦。如果没有学生举手，老师直接点名回答，学生端收到邀请上台回答事件，被点名的学生开麦。
参数：

|参数名|	类型	|说明|
| ----- | ----- |  ----- |
|userID|	string| 用户 ID|

示例：
```typescript
rtcClient.inviteToPlatform(userID).then(() => {
})
```

<span id="finishAnswering"></span>
#### finishAnswering(userID: string)
结束回答，老师端结束学生端回答，学生收到结束回答的通知，指定的学生停止连麦。
参数：

|参数名|	类型	| 说明|
| ----- | ----- |   ----- |
|userID|	string|	 用户 ID|

示例：
```typescript
rtcClient.finishAnswering(userID).then(() => {
})
```

#### stopQuestionTime(classId: number)
停止问答时间，老师端停止问答时间，学生端收到停止回答时间的通知，已连麦的学生要停止连麦，关闭举手功能。
参数：

|参数名|	类型	|说明|
| ----- | ----- | ----- |
|classId|	number|	教室 ID|

示例：
```typescript
rtcClient.stopQuestionTime(classId)
```

### 推拉流操作相关函数
<span id="getScreenShareList"></span>
#### getScreenShareList()
获取屏幕分享窗口列表。
参数：无
示例：
```typescript
rtcClient.getScreenShareList();
```


<span id="startScreenCapture"></span>
#### startScreenCapture(source: SourceParam)
选择分享屏幕，开始推流。
参数：

|参数名|	类型	|说明|
| ----- | ----- | ----- |
|type|	number|	采集源类型|
|sourceId|string|	采集源 ID，对于窗口，该字段指示窗口句柄；对于屏幕，该字段指示屏幕 ID|
|sourceName|string|采集源名称，UTF8 编码|

示例：
```typescript
interface SourceParam {
  type: number; // 采集源类型
  sourceId: string; // 采集源 ID
  sourceName: string; // 采集源名称，UTF8 编码
}
rtcClient.startScreenCapture({
   type,
   sourceId,
   sourceName
 })
```

<span id="startRemoteView"></span>
#### startRemoteView(params: RemoteParams) 
开始显示远端视频画面或屏幕分享画面。
参数：

|参数名|	类型	| 说明|
| ----- | ----- |  ---- |
|userID|	string|	 用户 ID|
|streamType|number|	 画面类型，1表示大画面，2表示小画面，3表示屏幕分享|
|view|HTMLElement|	 承载显示画面的 DOM|

示例：
```typescript
interface RemoteParams {
  userID: string; // 用户 ID
  streamType: number; // 画面类型,1-大画面，2-小画面，3-屏幕分享
  view: HTMLElement; //承载显示画面的 DOM
}
const view = document.getElementById('localVideo');
rtcClient.startRemoteView({
  userID: userID,
  streamType: 1,//1-大画面，2-小画面，3-屏幕分享
  view: view
});
```

#### stopRemoteView(params: StopRemoteParams)
停止显示远端视频画面或屏幕分享画面，同时不再拉取该远端用户的数据流。
参数：

|参数名|	类型	| 说明|
| ----- | ----- |  ----- |
|userID|	string|	 用户 ID|
|streamType|number|	 画面类型，1表示大画面，2表示小画面，3表示屏幕分享|

示例：
```typescript
interface StopRemoteParams {
  userID: string; // 用户 ID
  streamType: number; // 画面类型,1-大画面，2-小画面，3-屏幕分享
}
rtcClient.stopRemoteView({
   userID: userID,
   streamType: 1 //1-大画面，2-小画面，3-屏幕分享
 });
```

### 消息收发相关函数
#### sendTextMessage(params: MessageParams) 
发送聊天室消息。
参数：

|参数名|	类型	| 说明|
| ----- | ----- |  ----- |
|classId|number| 教室 ID|
|message|string| 消息文本|

示例：
```typescript
interface MessageParams {
  classId: number; // 教室 ID
  message: string; // 消息文本
}
rtcClient.sendTextMessage(params).then(() => {
})
```

#### sendCustomMessage(userID: string, data: string)
发送自定义 C2C 消息。 
参数：

|参数名|	类型	|	说明|
| ----- | ----- | ----- |
|userID|string| 用户 ID |
|data|string|	 自定义消息|

示例：
```typescript
rtcClient.sendCustomMessage(userID, JSON.stringify(params)
```

#### sendGroupCustomMessage(classId: number, data: string)
发送自定义群组消息。  
参数：

|参数名|	类型	| 说明|
| ----- | ----- | ----- |
|classId|number| 教室 ID|
|data|string| 自定义消息|

示例：
```typescript
rtcClient.sendGroupCustomMessage(classId, JSON.stringify(params))
```

### 设备操作相关函数
<span id="openCamera"></span>
#### openCamera(view: HTMLElement)
打开摄像头。
参数：

|参数名|	类型	| 说明|
| ----- | ----- | ----- |
|view|HTMLElement|	 承载显示画面的 DOM|

示例：
```typescript
const domEle = document.getElementById('localVideo');
rtcClient.openCamera(domEle);
```

#### closeCamera()
关闭摄像头。 
参数：无
示例：
```typescript
rtcClient.closeCamera();
```

<span id="getCameraList"></span>
#### getCameraList()
获取摄像头列表。
参数：无
示例：
```typescript
rtcClient.getCameraList()
```

<span id="setCurrentCamera"></span>
#### setCurrentCamera(deviceId:string)
设置摄像头，参数是从 getCameraDevicesList 中得到的设备 ID。
参数：

|参数名|	类型	| 说明|
| ----- | ----- |  ---- |
|deviceId|string| 设备 ID|

示例：
```typescript
rtcClient.setCurrentCamera(deviceId)
```

<span id="openMicrophone"></span>
#### openMicrophone()
打开麦克风。
参数：无
示例：
```typescript
rtcClient.openMicrophone();
```

<span id="closeMicrophone"></span>
#### closeMicrophone()
关闭麦克风。
参数：无
示例：
```typescript
rtcClient.closeMicrophone();
```


<span id="getMicrophoneList"></span>
#### getMicrophoneList()
获取麦克风设备列表。  
参数：无
示例：
```typescript
rtcClient.getMicrophoneList()
```
#### setCurrentMicDevice(micId:string)
设置麦克风，参数是从 getMicDevicesList 中得到的设备 ID。
参数：

|参数名|	类型	| 	说明|
| ----- | ----- | ----- |
|micId|string|	 设备 ID|

示例：
```typescript
rtcClient.setCurrentMicDevice(micId)
```

<span id="setBeautyStyle"></span>
#### setBeautyStyle(params: BeautyParams) 
设置美颜、美白、红润效果级别。 
参数：

|参数名|	类型	| 说明|
| ----- | ----- |  ----- |
|beautyStyle|number| 1表示光滑，适用于美女秀场，效果比较明显<br>2表示自然，磨皮算法更多地保留了面部细节，主观感受上会更加自然|
|beauty|number|	 美颜级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显|
|white|number|	 美白级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显|
|ruddiness|number|	 红润级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显，该参数 Windows 平台暂未生效|

示例：
```typescript
interface BeautyParams {
  beautyStyle: number;//光滑、自然
  beauty: number; //美颜级别
  white: number; //美白级别
  ruddiness: number; //红润级
}
rtcClient.setBeautyStyle({
	beautyStyle: 1,
	beauty: 5,
	white: 5,
	ruddiness: 5
})
```

## 组件事件
### 示例
```typescript
const EVENT = rtcClient.EVENT
rtcClient.on(EVENT.STUDENT_RAISE_HAND, () => {
   //学生举手
})
```
### 详细事件

| CODE |说明|
| ----- | ----- |
|ENTER_ROOM_SUCCESS|成功进入房间|
|LEAVE_ROOM_SUCCESS|成功离开房间|
|TEACHER_ENTER|老师进入房间|
|TEACHER_LEAVE|老师离开房间|
|STUDENT_ENTER|学生加入房间|
|STUDENT_LEAVE|学生离开房间|
|SCREEN_SHARE_ADD|老师开启屏幕分享|
|SCREEN_SHARE_REMOVE|老师关闭屏幕分享|
|REMOTE_VIDEO_ADD|远端视频流添加事件，当远端用户发布视频流后会收到该通知|
|REMOTE_VIDEO_REMOVE|远端视频流移出事件，当远端用户取消发布视频流后会收到该通知|
|REMOTE_AUDIO_ADD|远端音频流添加事件|
|REMOTE_AUDIO_REMOVE|远端音频流移除事件|
|ROOM_DESTROYED|房间被销毁|
|QUESTION_TIME_STARTED|开始问答时间|
|QUESTION_TIME_STOPPED|结束问答时间|
|STUDENT_RAISE_HAND|学生举手|
|BE_INVITED_TO_PLATFORM|被邀请回答问题、点名|
|ANSWERING_FINISHED|结束回答，禁音|
|MESSAGE_RECEIVED|收到消息|
|KICKED_OUT|同一账户在其他地方登录，被踢下线
|ERROR|异常|
|WARNING|警告|
