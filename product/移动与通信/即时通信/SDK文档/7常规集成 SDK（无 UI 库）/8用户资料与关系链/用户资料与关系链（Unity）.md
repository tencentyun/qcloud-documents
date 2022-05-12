## 用户资料管理

### 查询和修改自己的资料

-  **查询自己的资料**接口为 [ProfileGetUserProfileList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ProfileGetUserProfileList_com_tencent_imsdk_unity_types_FriendShipGetProfileListParam_com_tencent_imsdk_unity_callback_ValueCallback_)，其中参数 `userIDList` 需填入自己的 UserID。
- **修改自己的资料**接口为 [ProfileModifySelfUserProfile](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ProfileModifySelfUserProfile_com_tencent_imsdk_unity_types_UserProfileItem_com_tencent_imsdk_unity_callback_ValueCallback_)。修改自己的资料成功后，会收到 [UpdateFriendProfileCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.callback.UpdateFriendProfileCallback.html) 回调。

## 屏蔽某人消息

- **拉黑某人**
  如需屏蔽某人的消息，请调用 [FriendshipAddToBlackList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_FriendshipAddToBlackList_System_Collections_Generic_List_System_String__com_tencent_imsdk_unity_callback_ValueCallback_) 接口把该用户加入黑名单，即拉黑该用户。
  被拉黑的用户默认不会感知到“被拉黑”的状态，消息发送后不会返回已被对方拉黑的错误码。如果希望被拉黑的用户在发消息时返回已被对方拉黑的错误提醒，可以参见 [被拉黑的用户发消息怎么给错误提示](#block)。
- **解除拉黑**
  从黑名单中移除对方后可再次接收对方的消息，可调用 [FriendshipDeleteFromBlackList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_FriendshipDeleteFromBlackList_System_Collections_Generic_List_System_String__com_tencent_imsdk_unity_callback_ValueCallback_)。
- **获取黑名单列表**
  您可以通过 [FriendshipGetBlackList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_FriendshipGetBlackList_com_tencent_imsdk_unity_callback_ValueCallback_)  查看已拉黑多少用户，并对黑名单人员进行管理。

## 好友管理

### 是否需要加好友

IM SDK 在发送单聊消息的时候，默认不检查好友关系。在客服场景中，如果用户需要先加客服为好友才能进行沟通非常不方便，因此该默认设置常用于在线客服等场景。
如需实现类似“微信”或者“QQ”中“先加好友，再发消息”的交互体验，您可以在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **好友关系检查** 中开启"发送单聊消息检查关系链"。开启后，用户只能给好友发送消息，当用户给非好友发消息时，SDK 会报20009错误码。
![](https://qcloudimg.tencent-cloud.cn/raw/b116ad37b4f1292a5a0c80122624b9f3.png)

### 好友列表管理

IM SDK 支持好友关系链逻辑，您可以调用 [FriendshipGetFriendProfileList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_FriendshipGetFriendProfileList_com_tencent_imsdk_unity_callback_ValueCallback_) 接口获取好友列表，调用 [FriendshipAddFriend](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_FriendshipAddFriend_com_tencent_imsdk_unity_types_FriendshipAddFriendParam_com_tencent_imsdk_unity_callback_ValueCallback_) 接口添加好友。

## 常见使用问题

### 1. 非好友之间怎么禁止收发消息？

SDK 默认不限制非好友之间收发消息。如果您希望只允许好友之间收发消息，请在 [**即时通信 IM 控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **好友关系检查** 中开启"发送单聊消息检查关系链"。开启之后，给陌生人发消息时，SDK 会报20009错误码。

### 2. 被拉黑的用户发消息怎么给错误提示？[](id:block)

当消息发送者被拉黑后，发送者默认不会感知到“被拉黑”的状态，即发送消息后仍展示发送成功（实际上此时接收方不会收到消息）。如果需要被拉黑的发送者收到消息发送失败的提示，请在 [**即时通信 IM 控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **黑名单检查** 中关闭"发送消息后展示发送成功"，关闭后，被拉黑的发送者在发送消息时，SDK 会报20007错误码。

### 3. 增强版获取用户资料为什么不是最新的？

增强版 SDK 中用户资料的更新分好友和陌生人两种情况：

- 好友资料：由于好友资料更新时，后台会主动向 SDK 发送系统通知，因此好友资料可以实时更新。
- 陌生人资料：陌生人资料更新时，由于没有好友关系，后台无法向 SDK 发送系统通知，因此无法实时更新；为了避免每次获取用户资料都向后台发起网络请求，SDK 增加了缓存逻辑，对同一个用户主动向后台拉取资料的时间间隔为10分钟。
