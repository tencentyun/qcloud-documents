
## 未读消息

**未读消息**是指用户没有读过的消息（而非对方是否已经阅读，这种情况需要回执才能实现，目前 ImSDK 没有此功能。），`TIMMessage` 方法 `isRead` 标识消息是否已读，要想显示正确的未读计数，需要开发者显式调用已读上报，告诉 App 某条消息是否已读，例如，当用户进入聊天界面，可以设置整个会话的消息已读。对于聊天室，Server 不保存未读计数，每次登录后跟 Server 同步未读计数后将会清零。

```
public boolean isRead()
```

## 获取当前未读消息数量

可通过 `TIMConversation` 的 `getUnReadMessageNum` 方法获取当前会话中未读消息的数量，对于聊天室，Server 不保存未读计数，每次登录后跟 Server 同步未读计数后将会清零。

**原型：**

```
//获取未读消息数
public long getUnreadMessageNum()
```

**示例：**

```
//获取未读消息数
long num = conversation.getUnreadMessageNum();
Log.d(tag, "unread msg num: " + num);
```

## 已读上报

当用户阅读某个会话的数据后，需要进行会话消息的已读上报，SDK 根据会话中最后一条阅读的消息，设置会话中之前所有消息为已读。

> **注意：**
>- 无参数的版本设置一个会话中所有消息为已读状态，对于单聊会话，无参数版本性能要高很多，大多数情况下使用无参数版本即可。
>- 单聊和群聊设置已读用法相同，区别在于会话类型。

**原型：**

```
//将此消息之前的所有消息标记为已读
public void setReadMessage(TIMMessage msg)
//将所有消息标记为已读
public void setReadMessage()
```

**参数说明：**

参数|说明
---|---
msg | 为当前会话中最后一条读过的消息，ImSDK 会把比此消息的时间更早的消息标记为已读消息。

**示例：**

```
//对单聊会话已读上报
String peer = "sample_user_1";  //获取与用户 "sample_user_1" 的会话
conversation = TIMManager.getInstance().getConversation(
        TIMConversationType.C2C,    //会话类型：单聊
        peer);                      //会话对方用户帐号
conversation.setReadMessage(lastMsg); //lastMsg 为最后一条读过的消息
 
//对群聊会话已读上报
String groupId = "TGID1EDABEAEO";  //获取与群组 "TGID1LTTZEAEO" 的会话
conversation = TIMManager.getInstance().getConversation(
        TIMConversationType.Group,      //会话类型：群组
        groupId);                       //群组 ID
conversation.setReadMessage(lastMsg); //lastMsg 为最后一条读过的消息
```

**多终端已读上报同步：**在 2.0 以上版本中引入了**多终端已读上报同步**的功能，在多终端情况下，未读消息计数由 Server 下发同步通知，SDK 在本地更新未读计数后，通知用户更新会话。通知会通过 `TIMRefreshListener` 中的 `onRefreshConversation` 接口来进行回调，对于关注多终端同步的用户，可以在这个接口中进行相关的同步处理。

**原型：**

```
//部分会话刷新（包括多终端已读上报同步）
public void onRefreshConversation(List<TIMConversation> conversations)
```

**参数：**

参数|说明
---|---
conversations|需要刷新的会话列表

## 禁用自动上报

在 1.9 以上版本引入的方法，在单终端情况下，默认设置可以满足需求，出于性能考虑，未读消息由 SDK 拉回到本地，Server 默认会删除未读消息，切换终端以后无法看到之前终端已经拉回的未读消息，如果仅在一个终端，未读计数没有问题。如果需要多终端情况下仍然会有未读，可以通过 `TIMManager` 中的 `disableAutoReport` 方法禁用自动上报，IM 通讯云不会代替用户已读上报，**一旦禁用自动上报，需要开发者显式调用 `setReadMessage`**。

> **注意：**
> 禁用自动已读上报，需登录前设置。

```
public void disableAutoReport()
```

