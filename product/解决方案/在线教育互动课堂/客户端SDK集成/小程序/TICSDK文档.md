## 准备工作

出于政策和合规的考虑，微信暂时没有放开所有小程序对 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签的支持：
需要在小程序管理后台的<font color='red'> “设置 - 接口设置” </font>中自助开通该组件权限，如下图所示：
![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

## 效果展示

| 涂鸦 | 课件 | 聊天互动   |
| ---- | ------ |---- |
|   <img src="https://main.qcloudimg.com/raw/08f0f143b43ce97d181fa77901f900f4.png" width="260" align="center">  | <img src="https://main.qcloudimg.com/raw/f31ec991cbad15b2804850543e264c09.png" width="260" align="center"> |   <img src="https://main.qcloudimg.com/raw/a06a7dade864eb470c33caf9802e353e.png" width="260" align="center">    | 


|        <div style="width:800px">横屏显示</div>       |
| --------------------- |
|  <div style="text-align:center;"><img src="https://main.qcloudimg.com/raw/c05ba9be8ffc1c6fe67b042c765b36d9.png" width="100%" align="center"></div> |

## 版本要求

微信 6.6.6 版本开始支持。

##  集成 TIC SDK

> 小程序端 TIC 将以组件的方式集成。
> 目前小程序端白板仅支持显示，暂不支持与其他端进行互动。

下载 [小程序 TIC 组件源码](https://gitee.com/vqcloud/MiniProgram-TIC.git)。


### 1. 源码简介

```
- constant 常量
- components
           - tic-component tic 组件
           - board-component 白板组件
           - elk-component 日志服务组件
           - libs 依赖库
           - webim-component IM 组件
           - webrtc-room webrtc 组件
```

#### 1. constant

constant 常量。

#### 2.1 tic-component

TIC 组件：统一对外提供服务和接口的组件。

#### 2.2 board-component

白板组件：主要包含白板 SDK 和白板布局文件样式。

#### 2.3 elk-component

日志服务组件：小程序 TIC 的日志服务组件。
> **注意：**
> 日志作为排查问题的主要方法，请不要随意改动此组件以及其他组件中使用该组件的代码。

#### 2.4 libs

组件中依赖的的库文件。

#### 2.5 webim-component

IM 组件：白板之间实时同步数据与课堂内互动聊天的通道。

#### 2.6 webrtc-room

webrtc-room 组件：与其他端音视频互通的组件。


### 2. 配置安全域名

在 [微信公众平台](https://mp.weixin.qq.com/) 登录您小程序的账号和密码，并在 “设置 > 开发设置”，配置服务器 request 合法域名。

> 以下域名为互动课堂 SDK 中必须的域名，另外还需要加上您业务服务器的域名。

| 域名 | 说明 |
| --- | ---  |
| `https://webim.tim.qq.com` |     IM 服务域名        |
| `https://yun.tim.qq.com` |        WebRTC 音视频鉴权服务域名 [1]     |
| `https://official.opensso.tencent-cloud.com` |     WebRTC 音视频鉴权服务域名 [2]        |
| `https://cloud.tencent.com` |     WebRTC 推拉流服务域名        |
| `https://ilivelog.qcloud.com` |   日志服务域名          |

### 3. 创建小程序应用

通过微信开发者工具创建好应用后，将下载的 TIC 源码复制到项目中。

![](https://main.qcloudimg.com/raw/62f3070c82af5ed40bf22913857ce5ea.jpg)


### 4. 组件概览

#### 4.1 tic-component 主要接口
| 方法名	| 描述 |
| ----  | --- |
| login | 登录接口 |
| logout | 注销接口 |
| joinClassRoom | 加入课堂 |
| quitClassRoom | 退出课堂 |
| initBoard | 初始化白板 |
| sendC2CTextMsg | 发送 C2C 普通文本消息 |
| sendC2CCustomMsg | 发送 C2C 自定义消息 |
| sendGroupTextMsg | 发送群组普通文本消息 |
| sendGroupCustomMsg | 发送群组自定义消息 |
| setOrientation | 设置白板展示方向 |

#### 4.2 tic-component 主要事件

> tic-component 中对外有两个事件监听接口，```IMEvent```（IM 相关事件）和 ```BoardEvent```（白板相关事件），在 tic-component 标签中通过 bindIMEvent 和 bindBoardEvent 来接收事件回调。

```
<tic-component id="tx_board" bindIMEvent="onIMEvent" bindBoardEvent="onBoardEvent"></tic-component>
```

##### 4.2.1 onIMEvent 事件
```
onIMEvent(e) {
  let code = e.detail.code;
  let tag = e.detail.tag;
  let data = e.detail.detail;
  switch (tag) {
    case CONSTANT.IM.KICKED:
      this.showErrorToast('账号在其他地方登录，被踢下线');
      break;
    case CONSTANT.IM.MSG_NOTIFY: 
      break;
  }
}
```

| 事件名 | 必要监听 | 描述 |
| ----  | --- | --- |
| CONSTANT.IM.MSG_NOTIFY | <font color="red">是</font>，课堂内 IM 聊天消息 | 接收到普通消息 |
| CONSTANT.IM.GROUP_SYSTEM_NOTIFYS | 否 | 系统消息 |
| CONSTANT.IM.GROUP_INFO_CHANGE_NOTIFY | 否 | 群资料变化 |
| CONSTANT.IM.KICKED | <font color="red">是</font> | 多终端登录，被踢下线 |

##### 4.2.2 onBoardEvent 事件

```
onBoardEvent(e) {
  const {
    tag,
    data
  } = e.detail;
  switch (tag) {
      // 白板 SDK 鉴权不通过
    case CONSTANT.BOARD.VERIFY_SDK_ERROR:
      break;
  }
}
```

| 事件名 | 必要监听 | 描述 |
| ----  | --- | --- |
| CONSTANT.BOARD.VERIFY_SDK_ERROR | 是 | 白板 SDK 鉴权不通过 |


#### 4.3 webrtc-room属性

属性	| 类型	| 值	| 说明
---| ---- | --- | -----
useCloud	| Boolean	| 	| 必要，云上环境 true    非云环境 false  推荐 true。
roomID | Number |  | 必要，房间号。
userID | String |  | 必要，用户 ID。
userSig | String |  | 必要，身份签名，相当于登录密码的作用。
sdkAppID | Number |  | 必要，开通实时音视频服务创建应用后分配的 sdkAppID。
privateMapKey | String |  | 必要，房间权限 key，相当于进入指定房间 roomID 的钥匙。
template | String | | 必要, 1v1bigsmall, 1v1horizontal。
whiteness | String | 5 | 美白指数，取值 0 - 9，数值越大效果越明显。
beauty | String | 5 | 美颜指数，取值 0 - 9，数值越大效果越明显。
aspect | String | '3:4' | 画面比例 3:4，9:16。
minBitrate | Number | 400 | 最小码率，该数值决定了画面最差的清晰度表现。
maxBitrate | Number | 800 | 最大码率，该数值决定了画面最好的清晰度表现。
muted | Boolean | false | 是否静音。
debug | Boolean | false | 是否开启调试模式。
enableIM | Boolean | true | 是否启用 IM。<br/><font color="red"> 结合 tic 使用时，请设置为 false。</font>
enableCamera | Boolean | true | 开启 / 关闭摄像头。
smallViewLeft | String | '1vw' | 小窗口距离大画面左边的距离，只在 template 设置为 1v1bigsmall 有效。
smallViewTop | String | '1vw' | 小窗口距离大画面顶部的距离，只在 template 设置为 1v1bigsmall 有效。
smallViewWidth | String | '30vw' | 小窗口宽度，只在 template 设置为 1v1bigsmall 有效。
smallViewHeight | String | '40vw' | 小窗口高度，只在 template 设置为 1v1bigsmall 有效。
waitingImg | String | | 当微信切到后台时的垫片图片。
playerBackgroundImg | String | | 拉流画面的背景图。
pusherBackgroundImg | String | | 推流画面的背景图。
loadingImg | String | | 画面 loading 图片。
pureAudioPushMod | Number | | 可选，纯音频推流模式，需要旁路直播和录制时需要带上此参数。 <br/>1 => 本次是纯音频推流,不需要录制 mp3 文件。 <br/>2 => 本次是纯音频推流，录制文件为 mp3。
recordId | Number | | 可选，自动录制时业务自定义 ID，将在录制完成后通过 [直播录制回调](https://console.cloud.tencent.com/live/livecodemanage) 接口通知业务方。 <br/>**注意：**如果小程序与小程序或者小程序与 Web 端互通，且传了 recordId，必须保证 web 端和小程序传递的值一致。

#### 4.4 webrtc-room主要接口

| 方法名	| 描述 |
| ----  | --- |
| start | 启动推流 |
| pause | 暂停推流 |
| resume | 恢复推流 |
| stop | 停止推流 |
| switchCamera | 切换摄像头 |


#### 4.7 webrtc-room 动态操作音视频

通过切换属性来完成关闭 / 打开麦克风，关闭 / 打开摄像头等。
```
// 如切换关闭/打开麦克风
this.setData({
  muted: !this.data.muted
});
```
其他属性都可以进行类似的操作。

#### 4.6 webrtc-room 主要事件

> 将 enableIM 设置为 false 后，则只会触发音视频房间事件 bindRoomEvent。

```
onRoomEvent(e) {
  const {tag, code} = e.detail;
  switch (tag) {
      case 'error':
        // 打开摄像头失败
        if(code === CONSTANT.ROOM.ERROR_OPEN_CAMERA) {

        }
      break;
  }
}
```

事件名 | 必要监听 | 说明
---| ---- | ----
CONSTANT.ROOM.ERROR_OPEN_CAMERA | <font color="red">是</font> | 打开摄像头失败
CONSTANT.ROOM.ERROR_OPEN_MIC | <font color="red">是</font> | 打开麦克风失败
CONSTANT.ROOM.ERROR_PUSH_DISCONNECT | <font color="red">是</font> | 推流连接断开
CONSTANT.ROOM.ERROR_CAMERA_MIC_PERMISSION | <font color="red">是</font> | 获取不到摄像头或者麦克风权限
CONSTANT.ROOM.ERROR_EXCEEDS_THE_MAX_MEMBER | <font color="red">是</font> |  超过最大成员数
CONSTANT.ROOM.ERROR_REQUEST_ROOM_SIG | <font color="red">是</font> |  获取推流 sig 失败
CONSTANT.ROOM.ERROR_JOIN_ROOM | <font color="red">是</font> |  进房失败
CONSTANT.ROOM.SUCC_PUSH | 否 | 推流成功
CONSTANT.ROOM.SUCC_JOIN_ROOM | 否 | 进房成功
CONSTANT.ROOM.SUCC_MEMBERS_LIST | 否 | 成员列表
CONSTANT.ROOM.NETWORK_CHANGE | 否 | 网络改变
CONSTANT.ROOM.PUSHER_LOADING | 否 | 推流端 loading
CONSTANT.ROOM.PUSHER_PLAY | 否 | 推流端 play
CONSTANT.ROOM.PLAYER_LOADING | 否 | 对端 loading
CONSTANT.ROOM.PLAYER_PLAY | 否 | 对端 play
CONSTANT.ROOM.PLAYER_DISCONNECT | 否 | 对端断开连接
CONSTANT.ROOM.EXIT_ROOM  | 否 | 正常退房

> 关于 webrtc-room 组件的属性和接口以及事件回调等更多资料，请可以参考 [webrtc-room标签](https://cloud.tencent.com/document/product/647/17018)。


### 5. 使用流程
![](https://main.qcloudimg.com/raw/d712c58d73fb66e2cc976856b6fd599d.png)

#### 5.1 以page/index页为例

页面模板 index.wxml 示例如下：
```
<view class="container">
  <view class="camera-box">
    <webrtc-room id="webrtcroom" wx:if="{{!!template}}" template="{{template}}" roomID="{{roomID}}" userID="{{userID}}" userSig="{{userSig}}" sdkAppID="{{sdkAppID}}" privateMapKey="{{privateMapKey}}" smallViewLeft="{{smallViewLeft}}" smallViewTop="{{smallViewTop}}" smallViewWidth="{{smallViewWidth}}" smallViewHeight="{{smallViewHeight}}" enableCamera="{{enableCamera}}" enableIM="{{false}}" bindRoomEvent="onRoomEvent"></webrtc-room>
  </view>
  <view class="board_container">
      <tic-component id="tx_board" bindIMEvent="onIMEvent" bindBoardEvent="onBoardEvent">
      </tic-component>
    </view>
</view>
```

页面样式文件示例如下：
```
.container {
  position: relative;
  width: 100vw;
  height: 100vh;
  background-image: url(https://mc.qcloudimg.com/static/img/7da57e0050d308e2e1b1e31afbc42929/bg.png);
  background-color: #fff;
  background-repeat: no-repeat;
  background-size: cover;
  overflow: hidden;
}

.camera-box {
  width: 100vw;
  height: calc(100vh - 100vw * 9 / 16 - 80rpx);
}

.container .board_container {
  width: 100vw;
  height: calc(100vw * 9 / 16);
}

.container .board_container.horizontal {
  position: fixed;
  left: 0;
  top: 0;
  width: calc(100vh * 9 / 16);
  height: 100vh;
}
```

页面配置 index.json 示例如下：
```
{
  "navigationBarTitleText": "互动课堂1V1Demo",
  "usingComponents": {
    "webrtc-room": "/components/webrtc-room/webrtc-room",
    "tic-component": "/components/tic-component/tic-component"
  }
}
```

> 页面模板文件中，包含两个组件 webrtc-room（音视频组件）和 tic-component（tic组件）。

> 页面样式文件，配置音视频和白板显示的大小，board_container 的大小则为白板的大小，目前白板仅支持 16:9 的比例。

> 页面配置 index.json 文件中配置了页面的标题以及要使用的组件。

#### 5.2 获取组件实例
页面 onLoad 后获取组件实例示例如下：

```
onLoad: function (options) {
  // 获取tic组件
  this.txTic = this.selectComponent('#tx_board');
  // 获取webrtc组件
  this.webrtcroomComponent = this.selectComponent('#webrtcroom');
}
```

#### 5.3 登录

> 在 4.2 中获取组件后，即可以通过 tic 组件登录接口登录。

```
this.txTic.login(loginData, succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
loginData | Object | 是 | 登录数据，如下
succ | Function | 是 | 登录成功的回调
fail | Function | 是 | 登录失败的回调

> loginDatac 参数

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
sdkAppId | String | 是 | sdkappid
identifier | String | 是 | userid
userSig | String | 是 | usersig


#### 5.4 加入课堂

##### 5.4.1 加入课堂

> 在登录成功，可加入课堂。

```
this.txTic.joinClassRoom(roomID, succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
roomID | Number | 是 | 课堂 ID
succ | Function | 是 | 加入课堂成功的回调
fail | Function | 是 | 加入课堂失败的回调

##### 5.4.2 初始化白板
> 加入课堂成功后，方可初始化白板。

```
this.txTic.initBoard(boardData);
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
boardData | Object | 否 | 白板配置

> boardData 参数

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
orientation | String | 否 | 白板展示方向，默认垂直方向<br/>垂直：'vertical'   <br/>水平：'horizontal'


##### 5.4.3 开始音视频
> 加入课堂成功后，方可进行音视频对话。

```
this.webrtcroomComponent.start();
```

```
// 通过更新 page 上的属性 5 个属性后，则可以启动推流。
this.setData({
  userID: this.data.identifier,
  userSig: this.data.userSig,
  sdkAppID: this.data.sdkAppId,
  roomID: this.data.roomID,
  privateMapKey: this.data.privateMapKey
}, () => {
  this.webrtcroomComponent.start();
});
```

> privateMapKey：进房票据：相当于是进入 roomid 的钥匙，由您的服务器签发。
> 下载 [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) 可以获得服务端签发 userSig 和 privateMapKey 的计算代码（生成 userSig 和 privateMapKey 的签名算法是 **ECDSA-SHA256**）


#### 5.5 课堂互动 - 收发消息

##### 5.5.1 发送 C2C 普通文本消息
```
this.txTic.sendC2CTextMsg(receiveUser, msg, succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
receiveUser | String | 是 | 接收方的 identifier
msg | String | 是 | 要发送的文本内容
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

##### 5.5.2 发送群组普通文本消息

```
this.txTic.sendGroupTextMsg(msg, succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msg | String | 是 | 要发送的文本内容
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

##### 5.5.3 发送 C2C 自定义消息
```
this.txTic.sendC2CCustomMsg(receiveUser, msgObj, succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
receiveUser | String | 是 | 接收方的 identifier
msgObj | Object | 是 | 自定义文本消息对象 msgObj = {data: '发送的内容', desc: '描述', ext: '扩展'}
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

##### 5.5.4 发送群组自定义消息
```
this.txTic.sendGroupCustomMsg(msgObj, succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msgObj | Object | 是 | 自定义文本消息对象 msgObj = {data: '发送的内容', desc: '描述', ext: '扩展'}
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调


#### 5.6 课堂互动 - 音视频互动
支持切换前后置摄像头，关闭/开启麦克风，关闭/开启摄像头，美颜，美白等操作，具体可以参考 [webrtc-room 组件](https://cloud.tencent.com/document/product/647/17018)。或者参考更底层的 live-pusher/live-player 来扩展更多功能。

注意：webrtc-room 中也封装了 webim，在接入互动课堂的时候，请将 webrtc-room 中的 enableIM 设置为 false，不启用 webrtc-room 中的 IM 功能。

#### 5.7 修改白板展示方向
```
this.txTic.setOrientation(orientation)
```
参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
orientation | String | 否 | 白板展示方向<br/>垂直：'vertical'   <br/>水平：'horizontal'

#### 5.8 退出课堂

```
this.txTic.quitClassRoom(succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
succ | Function | 否 | 退出课堂成功的回调
fail | Function | 否 | 退出课堂失败的回调

#### 5.9 注销

```
this.txTic.logout(succ, fail)
```

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
succ | Function | 否 | 注销成功的回调
fail | Function | 否 | 注销失败的回调
