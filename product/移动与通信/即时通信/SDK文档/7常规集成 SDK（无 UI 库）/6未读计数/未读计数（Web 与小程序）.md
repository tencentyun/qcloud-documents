
本文的未读消息是指用户没有进行已读上报的消息，而非对方是否已经阅读。如需显示正确的未读计数，需要开发者显式调用已读上报，告诉 IM SDK 某个会话的消息是否已读，例如，当用户进入聊天界面，可以设置整个会话的消息已读。

## 获取当前未读消息数量

每次使用 [ getConversationList() ](https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#getConversationList) 时，会获得[[Conversation](https://web.sdk.qcloud.com/im/doc/zh-cn//Conversation.html)，[Conversation](https://web.sdk.qcloud.com/im/doc/zh-cn//Conversation.html)，......]数组，每个`Conversation`都有当前会话的未读数目，用`unreadCount`表示。
所有会话的未读计数，由所有会话的`unreadCount`相加所得。


## 已读上报

当用户阅读某个会话的消息后，需要进行会话消息的已读上报，IM SDK 根据会话中最后一条阅读的消息，设置会话中之前所有消息为已读。建议在单击进行切换会话时进行消息的已读上报。

>?已读上报会改变会话的未读计数。v2.7.0 起，设置`C2C`会话消息已读，会向对端推送已读回执，请参考事件 [TIM.EVENT.MESSAGE_READ_BY_PEER](https://web.sdk.qcloud.com/im/doc/zh-cn//module-EVENT.html#.MESSAGE_READ_BY_PEER)。

**接口**

```javascript
tim.setMessageRead(options);
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name             | Type     | Description |
| ---------------- | -------- | ----------- |
| `conversationID` | `String` | 会话 ID     |

**示例**

```javascript
// 将某会话下所有未读消息已读上报
let promise = tim.setMessageRead({conversationID: 'C2Cexample'});
promise.then(function(imResponse) {
  // 已读上报成功，指定 ID 的会话的 unreadCount 属性值被置为0
}).catch(function(imError) {
  // 已读上报失败
  console.warn('setMessageRead error:', imError);
});
```


