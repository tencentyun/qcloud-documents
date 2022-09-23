直播电商解决方案组件是对直播带货场景中使用即时通信 IM 能力的二次封装，在封装基本的收发消息能力的同时，针对直播带货场景封装了点赞、送礼、商品推送、优惠券领取等相关的能力。相关 SDK 下载，请参见 [SDK 下载](https://cloud.tencent.com/document/product/269/36887#TLS)。

## 场景效果
<img src="https://main.qcloudimg.com/raw/5f9c19773bcfc22334f3d6cbf4f9e13f.png" width="450px"></img>

##  组件使用前置条件

- **创建即时通信 IM 应用**
- **创建群成员自定义字段**
  - attent：记录自己关注了哪些主播
- **创建群自定义字段**
  - add_goods ：后台上架新的直播间商品列表
  - room_status：控制直播间状态

## SDK 接入
- 引入 IM SDK
```
npm i tim-wx-sdk --save
```
- 引入直播带货 SDK
```
npm i im-live-sells --save
```

##  组件参数

| 参数     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| SDKAppID | 即时通信 IM 的应用 ID，SDKAppID 需在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 上创建，新建的应用默认为体验版，主要用于集成及测试环节。产品正式上线前，建议 [购买](https://cloud.tencent.com/document/product/269/32458) 旗舰版或专业版。 |
| userSig  | 即时通信 IM 用户签名，UserSig 为登录即时通信 IM SDK 的必要参数，可在业务后台生成后返回给前端使用，生成文档与代码请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。 |
| roomID   | 直播间群聊房间 ID，此 ID 为即时通信 IM 所创建的直播群（AVChatRoom）群组 ID，该房间无加入人数限制可通过 [即时通信 IM 控制台](https://console.cloud.tencent.com/im-detail/qun-manage) 创建，或通过 [REST API](https://cloud.tencent.com/document/product/269/1519) 创建。 |
| TIM      | 即时通信 IM SDK，如是在小程序环境，请使用 **tim-wx-sdk**，Web 环境则使用 **tim-js-sdk**。 |
| userName | 与生成 UserSig 的 userName 一致。                            |



## 初始化示例

```javascript
import TIMLiveSell from 'im-live-sells'
import TIM from 'tim-js-sdk' //Web 环境
// import TIM from 'tim-wx-sdk' 小程序环境
const tls = new TIMLiveSell({
      SDKAppID: 1400***803,
      roomID: '@TGS#E****NVLGE',
      userSig: 'eJwtzM9****-reWMQw_',
      userName: 'Ho***st',
      TIM: TIM
})
```

## 组件回调

### TLS.EVENT.SDK_READY

组件已经初始化好，对应于 IM SDK 的 `TIM.EVENT.SDK_READY`，这个时候才可以调用 SDK 的方法。

```javascript
tls.on(TLS.EVENT.SDK_READY, async() => {
  
})
```

### TLS.EVENT.ROOM_STATUS_CHANGE

房间状态改变，如主播上（下）线，暂停等。

```javascript
tls.on(TLS.EVENT.ROOM_STATUS_CHANGE, async(data) => {
  
}
```

### TLS.EVENT.JOIN_GROUP

有人加入群聊时触发。

```javascript
tls.on(TLS.EVENT.JOIN_GROUP, async(data) => {
  const {nick,avatar,userID} = data
})
```

### TLS.EVENT.EXIT_GROUP

有人退出群聊时触发。

```javascript
tls.on(TLS.EVENT.EXIT_GROUP, async(data) => {
  const {nick,avatar,userID} = data
})
```

### TLS.EVENT.NOTIFACATION

公告发生修改时触发。

```javascript
tls.on(TLS.EVENT.NOTIFACATION, async(data) => {
  const { notification } = data
})
```

### TLS.EVENT.MESSAGE

有人发送群消息时触发。

> ? 自己发送的消息不会在这个回调里，自己发送的消息上屏请使用 sendMessage 方法返回的数据，这里与 IM SDK 保持一致。

```javascript
tls.on(TLS.EVENT.MESSAGE, async(data) => {
  const { nick,avatar,message,userID } = data
})
```

### TLS.EVENT.LIKE

有人给主播点赞时触发。

```javascript
tls.on(TLS.EVENT.LIKE, async(data) => {
  const { nick,avatar,value,userID } = data
})
```

### TLS.EVENT.SEND_GIFT

有人给主播送礼时触发。

```javascript
tls.on(TLS.EVENT.SEND_GIFT, async(data) => {
  const { nick,avatar,value,userID } = data
})
```

### TLS.EVENT.ATTENT

有人关注主播时触发。

```javascript
tls.on(TLS.EVENT.ATTENT, async(data) => {
  const { nick,avatar,value,userID } = data
})
```

### TLS.EVENT.BUY_GOODS

有人购买商品时触发。

```javascript
tls.on(TLS.EVENT.BUY_GOODS, async(data) => {
  const { nick,avatar,value,userID } = data
})
```

### TLS.EVENT.USE_COUPON

有人领取优惠券时触发。

```javascript
tls.on(TLS.EVENT.USE_COUPON, async(data) => {
  const { nick,avatar,value,userID } = data
})
```

### TLS.EVENT.ADD_GOODS

该直播中所推荐的商品发生改变时触发。

```javascript
tls.on(TLS.EVENT.ADD_GOODS, async(data) => {
  const { nick,avatar,value } = data
})
```

### TLS.EVENT.KICKED

帐号其它地方登录时触发。

```javascript
tls.on(TLS.EVENT.KICKED, async() => {
  
})
```

### TLS.EVENT.NETWORK_CHANGE

网络发生改变时触发。

```javascript
tls.on(TLS.EVENT.NETWORK_CHANGE, async() => {
  
})
```

### TLS.EVENT.SDK_NOT_READY

SDK 不可用时触发。

```javascript
tls.on(TLS.EVENT.SDK_NOT_READY, async() => {
  
})
```

### TLS.EVENT.PROFILE_UPDATE

个人资料发生修改时触发。

```javascript
tls.on(TLS.EVENT.PROFILE_UPDATE, async() => {
  
})
```

### TLS.EVENT.ERROR

SDK 发生错误时触发。

```javascript
tls.on(TLS.EVENT.ERROR, async(error) => {
  
})
```

### ${type}

在调用自定义消息时触发的同名事件。

```javascript
tls.on(`${type}`, async(error) => {
  
})
```



## 组件方法

### sendMessage(message:string)

发送弹幕消息。

```javascript
/**
 * 发送弹幕消息，调用此方法时，群类所有人都可收到该文本消息
 * @method sendMessage
 * @for TLS
 * @param msg 必填 弹幕消息
 * @returns Promise
 */
const {nick,avatar,message} = await tls.sendMessage(msg);

```

### like(extension?:string)

给主播点赞。

>? extension：点赞时的附加信息，如用户等级。

```javascript
/**
 * 发送点赞消息，调用此方法时，群内所有人都可收到该点赞消息
 * @method like
 * @for TLS
 * @param extension 非必填 点赞时附加信息
 * @returns Promise
 */
const {nick,avatar} = await tls.like(extension);
```

### gift(extension?:string)

给主播送礼。

> ? extension：送礼时的附加信息，如礼物信息等。

```javascript
/**
 * 发送送礼消息，调用此方法时，群内所有人都可收到该送礼消息
 * @method gift
 * @for TLS
 * @param msg 非必填 送礼时附加信息
 * @returns Promise
 */
const {nick,avatar} = await tls.gift(extension);
```

### exitRoom()

退出直播间。

```javascript
/**
 * 退出房间，主播（群主）不可退出房间
 * @method exitRoom
 * @for TLS
 * @param 
 * @returns Promise
 */
const {status} = await tls.exitRoom();
```

### joinRoom()

加入直播间。

```javascript
/**
 * 加入房间
 * @method joinRoom
 * @for TLS
 * @param 
 * @returns Promise
 */
const {userInfo,groupInfo} = await tls.joinRoom();
const { ownerInfo } = groupInfo;//获取主播信息
const { userID,nick,avatar } = ownerInfo
```

### getRoomInfo()

获取当前房间信息。

```javascript
/**
 * 获取该聊天室的基本信息
 * @method getRoomInfo
 * @for TLS
 * @param 
 * @returns Promise
 */
const {...ownerInfo} = await tls.getRoomInfo();
//ownerInfo 为主播相关信息
const { userID,nick,avatar } = ownerInfo
```

### attention()

关注主播。

```javascript
/**
 * 关注主播
 * @method attention
 * @for TLS
 * @param 
 * @returns Promise
 */
const {nick,avatar} = await tls.attention();
```

### cancelAttention()

取消关注主播。

```javascript
/**
 * 取消关注
 * @method cancelAttention
 * @for TLS
 * @param 
 * @returns Promise
 */
const {nick,avatar} = await tls.cancelAttention();
```

### destroy()

销毁组件。

```javascript
/**
 * 销毁组件
 * @method destroy
 * @for TLS
 * @param 
 * @returns Promise
 */
tls.destroy(); 
```

### sendCustomMsgAndEmitEvent(eventName: string, extension?: string)

发送自定义消息，并触发 type 类型的回调事件。

> ?
> - eventName：事件名。
> - extension：自定义消息发送者附带信息。

```javascript
/**
 * 发送自定义消息，并触发同名事件
 * @method destroy
 * @for TLS
 * @param eventName:事件名，someExtension：附加信息
 * @returns Promise
 */
await tls.sendCustomMsgAndEmitEvent('eventName','someExtension')
```

## 内置对象

TIM  通过 `TIM.create` 创建的对象，可使用 TIM 所有的方法。

## 事件

| EVENT                                                 | 描述                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| [TLS.EVENT.SDK_READY](#tls.event.sdk_ready)           | 组件已经初始化好，对应于 IM SDK 的 `TIM.EVENT.SDK_READY`，这个时候才可以调用 SDK 的方法。 |
| [TLS.EVENT.JOIN_GROUP](#tls.event.join_group)         | 有人加入群聊时触发。                                         |
| [TLS.EVENT.EXIT_GROUP](#tls.event.join_group)         | 有人退出群聊时触发。                                         |
| [TLS.EVENT.NOTIFACATION](#tls.event.notifacation)     | 公告发生修改时触发。                                         |
| [TLS.EVENT.MESSAGE](#tls.event.message)               | 有人发送群消息时触发。                                       |
| [TLS.EVENT.PROFILE_UPDATE](#tls.event.profile_update) | 个人资料发生修改时触发。                                     |
| [TLS.EVENT.ERROR](#tls.event.error)                   | SDK 发生错误时触发。                                         |
| [TLS.EVENT.KICKED](#tls.event.kicked)                 | 帐号其它地方登录时触发。                                     |
| [TLS.EVENT.NETWORK_CHANGE](#tls.event.network_change) | 网络发生改变时触发。                                         |
| [TLS.EVENT.SDK_NOT_READY](#tls.event.sdk_not_ready)   | SDK 不可用时触发。                                           |
| [TLS.EVENT.LIKE](#tls.event.like)                     | 有人给主播点赞时触发。                                       |
| [TLS.EVENT.BUY_GOODS](#tls.event.buy_goods)           | 有人购买商品时触发。                                         |
| [TLS.EVENT.SEND_GIFT](#tls.event.send_gift)           | 有人给主播送礼时触发。                                       |
| [TLS.EVENT.ATTENT](#tls.event.attent)                 | 有人关注主播时触发。                                         |
| [TLS.EVENT.ADD_GOODS](#tls.event.add_goods)           | 该直播中所推荐的商品发生改变时触发。                         |
| [TLS.EVENT.USE_COUPON](#tls.event.use_coupon)         | 有人领取优惠券时触发。                                        |


