## 功能描述

在删除好友或退出群组后，如果不需要查看好友或群会话的历史消息，可以选择删除会话。会话删除默认关闭多端同步，可在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im-detail/login-message) 开启多端同步。

## 删除会话

>!
>- v2.16.1起删除会话会同时删除历史消息。
>- v2.16.1之前的版本，只删除会话，不删除历史消息。例如：删除与用户 A 的会话，下次再与用户 A 发起会话时，之前的聊天信息仍在。
>- 删除会话默认不会多端同步，如果需要多端同步，请在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im-detail/login-message)>**应用配置**>**功能配置**>**登录与消息**>**多端同步设置**开启**删除会话后多端同步**。

**接口**

<dx-codeblock>
:::  js

tim.deleteConversation(conversationID);

:::
</dx-codeblock>

**参数**

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| conversationID     | String | 会话 ID。会话 ID 组成方式：<br/><li>C2C${userID}（单聊）</li><li>GROUP{groupID}（群聊）</li><li>@TIM#SYSTEM（系统通知会话）</li> |


**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.deleteConversation('C2CExample');
promise.then(function(imResponse) {
  // 删除会话成功
  const { conversationID } = imResponse.data; // 被删除的会话 ID
}).catch(function(imError) {
  console.warn('deleteConversation error:', imError); // 删除会话失败的相关信息
});

:::
</dx-codeblock>
