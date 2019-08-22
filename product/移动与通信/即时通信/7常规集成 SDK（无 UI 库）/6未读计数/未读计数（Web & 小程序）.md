## 未读消息计数

这里的未读消息是指用户没有进行已读上报的消息，而非对方是否已经阅读。 要想显示正确的未读计数，需要开发者显式调用已读上报，告诉 IM SDK 某个会话的消息是否已读，例如，当用户进入聊天界面，可以设置整个会话的消息已读。

## 获取当前未读消息数量

每次使用[ getConversationList() ](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getConversationList)时，会获得[ [Conversation](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Conversation.html)，[Conversation](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Conversation.html)，......]数组，每个`Conversation`都有当前会话的未读数目，用`unreadCount`表示。
如果要获得所有会话的未读计数，即将所有会话的`unreadCount`相加得到


## 已读上报

当用户阅读某个会话的数据后，需要进行会话消息的已读上报，IM SDK 根据会话中最后一条阅读的消息，设置会话中之前所有消息为已读。建议在点击进行切换回话的时候进行消息的已读上报。

**接口**

```javascript
tim.setMessageRead(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下：

| Name             | Type     | Description |
| ---------------- | -------- | ----------- |
| `conversationID` | `String` | 会话 ID     |

**示例**

```javascript
// 将某会话下所有未读消息已读上报
tim.setMessageRead({conversationID: 'C2Cexample'});
```

