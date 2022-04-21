### 用 Taro 开发项目，集成 WebIM v2.x，为什么一直收不到 TIM.EVENT.SDK_READY 事件？

WebIM v2.x 不需要被 Taro 编译。如果您通过 `npm i` 的方式集成了 WebIM，请手动将文件 `node_modules/tim-js-sdk/tim-js.js` 或 `node_modules/tim-wx-sdk/tim-wx.js` 拷贝到您项目的 src 目录下，并在配置文件中配置（更详细的请参见 [编译配置详情](https://nervjs.github.io/taro/docs/config-detail.html#weappcompileexclude)）。
示例：
<dx-codeblock>
:::  js
weapp: {
  compile: {
    exclude: ['src/tencent-webim/tim-wx.js']
  }
}
:::
</dx-codeblock>

### 为什么调用 off 接口取消监听事件后，仍然能监听到 SDK 派发的事件？

对于同一个事件，如 [TIM.EVENT.MESSAGE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_RECEIVED)，调用 [on](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#on) 接口监听事件和调用 [off](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#off) 接口取消监听事件，handler 参数应当指向同一个 function，避免以下写法：

<dx-codeblock>
:::  js
// 注意！以下代码有 bug，无法取消监听 TIM.EVENT.MESSAGE_RECEIVED，因为 bind() 方法每次会返回一个新的函数
tim.on(TIM.EVENT.MESSAGE_RECEIVED, this.onMessageReceived.bind(this));
tim.off(TIM.EVENT.MESSAGE_RECEIVED, this.onMessageReceived.bind(this));

// 建议写法
tim.on(TIM.EVENT.MESSAGE_RECEIVED, onMessageReceived, this);
tim.off(TIM.EVENT.MESSAGE_RECEIVED, onMessageReceived);
:::
</dx-codeblock>

>?bind() 方法的详细说明请参见 [Function.prototype.bind()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

### 调用 logout 接口，SDK 会自动取消监听接入侧通过调用 on 接口已监听的事件吗？

不会。取消监听事件，需接入侧主动调用 [off](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#off) 接口。


### 登录时遇到 Err_TLS_Third_Sig_Check_Session_Key_Too_Long 的提示？

密钥问题导致生成的 UserSig 鉴权失败。请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。

### 登录时遇到 TypeError: wx.$app.ready is not a function？

请通过监听事件 [TIM.EVENT.SDK_READY](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.SDK_READY) 代替直接使用 ready 函数，后者已经废弃。

### 登录成功后不能发送消息，提示接口调用时机不合理？

请监听事件 [TIM.EVENT.SDK_READY](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.SDK_READY)，待 SDK ready 后再调用发送消息等需要鉴权的接口。

### WebIM v2.x 怎样拉取历史消息？没有 getC2CHistoryMsgs 接口了吗？

WebIM v2.x 没有 getC2CHistoryMsgs 接口，[getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 接口可用于"拉取历史消息"。

### 我想在音视频聊天室实现点赞，送鲜花的功能，请问该怎么办？

可以通过 [createCustomMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createCustomMessage) 和 [sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage) 接口实现。

### WebIM v2.x 和 WebIM v1.7.x 消息是互通的吗？

互通。如果条件允许，建议接入使用最新的 WebIM，获得更好的体验和维护。

### WebIM v2.x 如何兼容 REST API 或 旧版 IM 发送的组合消息？

请升级 SDK 版本至 2.1.3 或更高版本。组合消息的内容存储在 Message 实例的 _elements 属性，接入侧需自主解析，解析请参见 [消息格式](https://cloud.tencent.com/document/product/269/2720)。
非组合消息，请使用推荐做法：使用 [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 实例的 type 和 payload 属性。

### 为什么 WebIM v2.x 调用 sendMessage发消息成功后，未收到 TIM.EVENT.MESSAGE_RECEIVED 事件？

[sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage) 接口返回 `Promise`，接入侧请通过 `Promise.then` 或 `Promise.catch` 处理发送消息成功或失败后的业务逻辑。
此时 SDK 不会派发 [TIM.EVENT.MESSAGE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_RECEIVED) 事件，避免消息重复。

### 通过 getMessageList 拉取到的消息列表和通过监听 TIM.EVENT.MESSAGE_RECEIVED 事件收到的消息合并后，发现有时会消息乱序，为什么？

接入侧维护会话的消息列表时，请注意保证消息入列的顺序正确，若消息列表从旧到新排列，则通过 [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 拉取到的历史消息应该从头部入列，通过监听 [TIM.EVENT.MESSAGE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_RECEIVED) 事件收到的实时消息应该从尾部入列。

### 调用 createGroup 接口创建音视频聊天室后，收不到消息？

调用 [createGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createGroup) 接口创建音视频聊天室后，需调用 [joinGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#joinGroup) 接口加入群组（必须带上类型 TIM.TYPES.GRP_AVCHATROOM），才能进行消息收发流程。

<dx-codeblock>
:::  js
let promise = tim.joinGroup({ groupID: 'group1', type: TIM.TYPES.GRP_AVCHATROOM });
promise.then(function(imResponse) {
  switch (imResponse.data.status) {
    case TIM.TYPES.JOIN_STATUS_WAIT_APPROVAL: // 等待管理员同意
      break;
    case TIM.TYPES.JOIN_STATUS_SUCCESS: // 加群成功
      console.log(imResponse.data.group); // 加入的群组资料
      break;
    case TIM.TYPES.JOIN_STATUS_ALREADY_IN_GROUP: // 已经在群中
      break;
    default:
      break;
    }
  }).catch(function(imError){
    console.warn('joinGroup error:', imError); // 申请加群失败的相关信息
});
:::
</dx-codeblock>

### 音视频聊天室怎么没有未读消息计数？为什么拉取不到历史消息？

已定的产品策略：音视频聊天室不支持未读消息计数，也不支持查看入群前历史消息，详细请参见 [群组系统](https://cloud.tencent.com/document/product/269/1502)。
**旗舰版**支持直播群新成员查看入群前历史消息（SDK 请升级到v2.16.0或更高版本）。

### 可以同时加入两个或多个音视频聊天室吗？
目前不可以。同一用户同时只能加入一个音视频聊天室。
**示例**：用户已在音视频聊天室 A 中，再加入音视频聊天室 B，SDK 会先退出音视频聊天室 A，然后加入音视频聊天室 B。
详细请参见 [joinGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#joinGroup)。

