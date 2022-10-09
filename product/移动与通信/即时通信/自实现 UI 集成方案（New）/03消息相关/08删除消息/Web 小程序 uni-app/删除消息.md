## 功能描述

删除成功后，被删除消息的 isDeleted 属性值为 true。C2C 会话，消息被删除后，下次登录拉取历史消息将拉取不到，对端不受影响。群会话，消息被删除后，下次登录拉取历史消息将拉取不到，群内其他成员不受影响。

>!
>- v2.12.0起支持。
>- 一次最多只能删除30条消息，超过30条则只删除前30条。
>- 要删除的消息必须属于同一会话，以消息列表的第1个消息的所属会话为准。
>- 一秒钟最多只能调用一次该接口。
>- 删除消息不支持多端同步。
>- AVChatRoom（直播群）不支持删除消息，调用此接口将返回10035错误码。

**接口**

<dx-codeblock>
:::  js

tim.deleteMessage(messageList);

:::
</dx-codeblock>

**参数**

| Name               | Type     | Description                                                  |
| ------------------ | -------- |------------------------------------------------------------ |
| messageList          | Array |  同一会话的消息列表，最大长度为30 |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

// 删除消息，v2.12.0起支持
let promise = tim.deleteMessage([message1, message2, message3, ...]);
promise.then(function(imResponse) {
  // 删除消息成功
}).catch(function(imError) {
  // 删除消息失败
  console.warn('deleteMessage error:', imError);
});

:::
</dx-codeblock>