## 组件介绍
TRTCCalling 小程序组件是基于腾讯云实时音视频（TRTC）和腾讯云信令 SDK（TSignalling）组合而成，支持1V1，多人场景下的视频通话。TRTCCalling 是一个开源组件，依赖闭源的信令 SDK（TSignalling）进行状态管理，通过 C2C 通信，完成信令传递。组件可快速服务线上客服，咨询，医疗问诊，跨端实时通话等应用场景。您可前往 [【Github】](https://github.com/tencentyun/TRTCSDK/tree/master/WXMini/TRTCScenesDemo)或单击 [【ZIP】](https://web.sdk.qcloud.com/component/trtccalling/download/trtc-calling-miniapp.zip)，下载相关 SDK 及配套的 Demo 源码。
![](https://web.sdk.qcloud.com/component/trtccalling/doc/miniapp/6b1368e2186abcd5126fc1c165f2fb78.png)

## 环境要求
- 微信 App iOS 最低版本要求：7.0.9。
- 微信 App Android 最低版本要求：7.0.8。
- 小程序基础库最低版本要求：2.10.0。
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。
- 由于小程序测试号不具备 &lt;live-pusher&gt; 和 &lt;live-player&gt; 的使用权限，需要申请常规小程序账号进行开发。
- 不支持 uniapp 开发环境，请使用原生小程序开发环境。

## 前提条件
1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. **开通小程序类目与推拉流标签权限（如不开通则无法正常使用）**。
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
 - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
 - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
 - 符合类目要求的小程序，需要在【[微信公众平台](https://mp.weixin.qq.com)】>【开发】>【开发管理】>【接口设置】中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/dc6d3c9102bd81443cb27b9810c8e981.png)

## TRTCCalling API 概览

### 事件订阅/取消订阅

本组件基于事件分发进行管理，应用层可以根据组件下发的事件进行上层交互的改变。

| API | 描述 |
|---------|---------|
|[on(eventCode, handler, context)](#on)|订阅事件。|
|[off(eventCode, handler)](#off)|取消事件订阅。|

### 邀请方函数

邀请方拨打后，会收到该邀请的对端处理结果，详情可在 [事件表](#EVENT) 查询。

| API | 描述 |
|---------|---------|
|[call({userID, type})](#off)|发出 C2C 通话邀请。|
|[groupCall({userIDList, type, groupID})](#groupCall)|群组邀请通话（请先 [创建 IM 群组](https://cloud.tencent.com/document/product/269/37459)）。|

### 被邀请方函数

被邀请方如果超过30s对邀请为做出处理，将会做超时处理。

| API | 描述 |
|---------|---------|
|[accept()](#accept)|接受通话邀请。|
|[reject()](#reject)|拒绝通话邀请。|

### 通用功能函数
| API | 描述 |
|---------|---------|
|[login()](#login) | 初始化信令 SDK，执行后才能正常进行信令收发。 |
|[logout()](#logout)|登出信令 SDK，执行后不再能收发信令。|
|[hangup()](#hangup)|结束当前通话。|
|[startRemoteView(userID)](#startRemoteView)|开启远端画面渲染。|
|[stopRemoteView(userID)](#stopRemoteView)|关闭远端画面渲染。|
|[openCamera()](#openCamera)|开启摄像头。|
|[closeCamera()](#closeCamera)|关闭摄像头。|
|[setMicMute(isMute)](#setMicMute)|设置麦克风状态。<li/>当 isMute 取值为 true：关闭麦克风。<li/>当 isMute 取值为 false：打开麦克风。|
|[switchCamera(isFrontCamera)](#switchCamera)|选择摄像头。<li/>当 isFrontCamera 取值为 true：前置摄像头。<li/>当 isFrontCamera 取值为 false：后置摄像头。|
|[setHandsFree(isHandsFree)](#setHandsFree)|设置声音播放状态。<li/>当 isHandsFree 取值为 true：外放模式。<li/>当 isHandsFree 取值为 false： 听筒模式。|

## 属性表

### &lt;TRTCCalling&gt; 属性

| 属性                 | 类型    | 默认值 | 必填 | 说明                                                         |
| -------------------- | ------- | ------ | ---- | ------------------------------------------------------------ |
| id                   | String  |        | 是   | 绑定TRTCCalling的dom ID，可通过this.selectComponent(ID)获取实例 |
| config               | Object  |        | 是   | TRTCCalling初始化配置                                        |
| backgroundMute       | Boolean | false  | 否   | 进入后台时是否保持音频通话，true保持、false挂断       |


#### config 参数

| 参数     | 类型   | 必填 | 说明                                                         |
| -------- | ------ | ---- | ------------------------------------------------------------ |
| sdkAppID | Number | 是   | 开通实时音视频服务创建应用后分配的 [SDKAppID](https://console.cloud.tencent.com/trtc/app)。 |
| userID   | String | 是   | 用户 ID，可以由您的帐号体系指定。                            |
| userSig  | String | 是   | 身份签名（即相当于登录密码），由 userID 计算得出，具体计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| type     | Number | 是   | 指定通话类型。1：语音通话，2：视频通话。                     |

**示例代码：**

```html
// index.wxml
<TRTCCalling id="TRTCCalling-room" config="{{config}}"></TRTCCalling>
```

```javascript
// videocall.js
trtcConfig = {
  sdkAppID: 0, // 开通实时音视频服务创建应用后分配的 SDKAppID
  userID: 'test_user_001', // 用户 ID，可以由您的帐号系统指定
  userSig: 'xxxxxxxxxxxx', // 身份签名，相当于登录密码的作用
  type: 2, // 通话模式
}
```

### 组件方法

#### selectComponent()
您可以通过小程序提供的 `this.selectComponent()` 方法获取组件实例。
```javascript
let TRTCCallingContext = this.selectComponent('#TRTCCalling-room')
TRTCCallingContext.login()
```

[](id:login)
#### login()
登入接口，会建议在页面 onLoad 阶段调用。

```javascript
TRTCCallingContext.login()
```

[](id:logout)
#### logout()
登出信令 SDK，执行后不再能收发信令。
```javascript
TRTCCallingContext.logout()
```

[](id:on)
#### on(eventCode, handler, context)
用于监听组件派发的事件，详细事件请参见 [事件表](#EVENT)。
```javascript
TRTCCallingContext.on(EVENT.INVITED, () => {
  // todo
})
```

[](id:off)
#### off(eventCode, handler)
用于取消事件监听。
```javascript
TRTCCallingContext.off(EVENT.INVITED)
```

[](id:call)
#### call({userID, type})
进行某个 user 进行呼叫。

| 参数 | 含义 | 
|---------|---------|
| userID | 希望呼叫用户的 userID。 | 
| type | 通话类型，type = 1：语音通话，type =2：视频通话。 | 

```javascript
let userID = 'test'
let type = 2
TRTCCallingContext.call({userID, type})
```

[](id:groupCall)
#### groupCall({userIDList, type, groupID})

在调用该接口前需要使用 IM [创建群组](https://cloud.tencent.com/document/product/269/37459)，并将 groupID 作为参数传入。

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userIDList | Arrary | 拨打的用户列表 |
|type|Number|type 为通话类型，1：语音通话，2：视频通话。|
|groupID|String| IM 群组的 groupID。|

```javascript
TRTCCallingContext.groupCall({userIDList, type, groupID})
```
[](id:accept)

#### accept()

当收到邀请后，调用该接口将接受当前的邀请。

>? 当上一个 invitation 未处理完成时，组件会默认占线，之后的邀请都会回复忙线。

```javascript
TRTCCallingContext.on(EVENT.INVITED, () => {
  TRTCCallingContext.accept()
})
```

[](id:reject)
#### reject()
当收到邀请后，调用该接口将拒绝当前收到的邀请。

```javascript
TRTCCallingContext.on(EVENT.INVITED, () => {
  TRTCCallingContext.reject()
})
```

[](id:hangup)
#### hangup()  
结束当前通话。
```javascript
TRTCCallingContext.hangup()
```

[](id:startRemoteView)
#### startRemoteView(userID) 
开启指定 userID 的远端画面 （默认开启）。
```javascript
TRTCCallingContext.startRemoteView(userID)
```

[](id:stopRemoteView)
#### stopRemoteView(userID)  
关闭指定 userID 的远端画面。

```javascript
TRTCCallingContext.stopRemoteView(userID)
```

[](id:openCamera)
#### openCamera()
开启本地摄像头。
```javascript
TRTCCallingContext.openCamera()
```

[](id:closeCamera)
####  closeCamera()
关闭摄像头。
```javascript
TRTCCallingContext.closeCamera()
```

[](id:setMicMute)
####  setMicMute(isMute) 
设置麦克风状态。

| 参数 | 含义 | 
|---------|---------|
| isMute | true：关闭麦克风，false： 打开麦克风。 | 

```javascript
TRTCCallingContext.setMicMute(true) // 开启麦克风
```



[](id:switchCamera)
#### switchCamera(isFrontCamera) 
选择摄像头。

| 参数 | 含义 | 
|---------|---------|
| isFrontCamera | true：前置摄像头，false： 后置摄像头。 | 


```javascript
TRTCCallingContext.switchCamera(true) // 开启前置摄像头
```


[](id:setHandsFree)
####  setHandsFree(isHandsFree) 
设置声音播放状态。

| 参数 | 含义 | 
|---------|---------|
| isHandsFree | true：外放模式，false： 听筒模式。 | 

```javascript
TRTCCallingContext.setHandsFree(true) // 开启外放模式
```


[](id:EVENT)
## 事件表
获取 EVENT 事件。
```javascript
const TRTCCallingContext = this.selectComponent('#TRTCCalling-room')
const EVENT = trtcRoomContext.EVENT // 以下事件均在此EVENT对象下
```

### 邀请方事件
#### REJECT
邀请方发出的邀请被拒绝。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|invitee| String|被邀请人。|
|inviteID| String|邀请 ID。|
| reason | String|拒绝理由。|

#### NO_RESP 
邀请方发出的邀请无人响应（对方不在线）。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|inviteID| String|邀请 ID。|
| timeoutUserList | Array| 超时用户列表。|

#### CALLING_TIMEOUT
邀请方发出的邀请无人响应（在线未接受邀请）。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|inviteID| String|邀请 ID。|
|timeoutUserList | Array| 超时用户列表。|
| groupID | String | 群组 ID。|
| sponsor | String | 邀请者。|

#### LINE_BUSY
被邀请方正在通话中，忙线。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|invitee| String|被邀请人。|
|inviteID| String|邀请 ID。|
| reason | String|拒绝理由。|

#### CALLING_CANCEL
接受的邀请被取消。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|invitee| String|被邀请人。|
|inviteID| String|邀请 ID。|


### 被邀请方事件

#### INVITED 
收到邀请通知。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|sponsor| String|邀请人。|
| isFromGroup | Boolean | 是否是群通话。|
|inviteID| String|邀请 ID。|
|inviteData| Object | <li/>callType：通话类型。<li/>roomID：房间号。|

#### CALLING_CANCEL
接受的邀请被取消。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|invitee| String|被邀请人。|
|inviteID| String|邀请 ID。|

### 通用事件

#### USER_ENTER
用户进房。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|userID| String|加入的用户。|

#### USER_LEAVE
用户退出房间。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|userID| String|离开的用户。|

#### CALL_END
本次通话结束。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|call_end| String|通话结束事件。|

#### USER_VOICE_VOLUME
本地和远端用户的音量回调。

| 参数| 类型   |    含义   |
| --------------- | ---------- | -------------- |
|userID| String|通话人。|
|volume| Number|音量。|

#### HANG_UP
挂断电话。

## 异常捕获

通过监听 EVENT 里的 ERROR 字段，对组件抛出的错误进行处理。

```javascript
let EVENT = trtcRoomContext.EVENT
trtcRoomContext.on(EVENT.ERROR,(event)=>{
  console.log(event.data)
})
```

## 常见问题
#### 为什么拨打不通，或者被踢下线？
组件暂不支持多实例登入，不支持**离线推送信令**功能，请您确认账号登入的唯一性。

- 多实例：一个 userID 重复登入，或在不同端登入，将会引起信令的混乱。 
- 离线推送：实例在线才能接收消息，实例离线时接收到的信令不会在上线后重新推送。即，小程序在后台与离线状态下，无法收到呼入提醒或来电提醒。

