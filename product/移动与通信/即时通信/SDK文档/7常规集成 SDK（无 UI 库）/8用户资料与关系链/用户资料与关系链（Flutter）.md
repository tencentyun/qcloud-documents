## 用户资料管理
### 查询和修改自己的资料
**查询自己的资料**接口为 [getUsersInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/getUsersInfo.html)，其中参数 `userIDList` 需填入自己的 UserID。
**修改自己的资料**接口为 [setSelfInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/setSelfInfo.html)。修改自己的资料成功后，会收到 [onSelfInfoUpdated](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimSDKListener/V2TimSDKListener/onSelfInfoUpdated.html) 回调。

### 查询非好友用户资料
查询非好友资料接口同查询自己的资料 [getUsersInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/getUsersInfo.html)，参数 `userIDList` 填入非好友的 UserID 即可。

### 查询和修改好友的资料
**查询指定的好友资料**接口为 [getFriendsInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendsInfo.html)，从回调信息中通过 `V2TIMFriendInfoResult` 的 `relation` 字段可以得到该用户与自己的关系：
- `FriendTypeWeb.V2TIM_FRIEND_RELATION_TYPE_NONE` 表示不是好友。
- `FriendTypeWeb.V2TIM_FRIEND_RELATION_TYPE_BOTH_WAY` 表示互为好友。
- `FriendTypeWeb.V2TIM_FRIEND_RELATION_TYPE_IN_MY_FRIEND_LIST` 表示对方在我的好友列表中。
- `FriendTypeWeb.V2TIM_FRIEND_RELATION_TYPE_IN_OTHER_FRIEND_LIST` 表示我在对方的好友列表中。

**修改指定的好友信息**接口为 [setFriendInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/setFriendInfo.html) ，可修改好友备注等资料。

## 屏蔽某人消息
- **拉黑某人**
如需屏蔽某人的消息，请调用 [addToBlackList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addToBlackList.html) 接口把该用户加入黑名单，即拉黑该用户。
被拉黑的用户默认不会感知到“被拉黑”的状态，消息发送后不会返回已被对方拉黑的错误码。如果希望被拉黑的用户在发消息时返回已被对方拉黑的错误提醒，可以参考最下方的常见问题 [被拉黑的用户发消息怎么给错误提示](#msgSendTips)。

- **解除拉黑**
从黑名单中移除对方后可再次接收对方的消息，可调用 [deleteFromBlackList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFromBlackList.html)。

- **获取黑名单列表**
您可以通过 [getBlackList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getBlackList.html) 查看已拉黑多少用户，并对黑名单人员进行管理。

## 好友管理
### 是否需要加好友
IM SDK 在发送单聊消息的时候，默认不检查好友关系。在客服场景中，如果用户需要先加客服为好友才能进行沟通非常不方便，因此该默认设置常用于在线客服等场景。
如需实现类似“微信”或者“QQ”中“先加好友，再发消息”的交互体验，您可以在 [**即时通信 IM 控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **好友关系检查** 中开启"发送单聊消息检查关系链"。开启后，用户只能给好友发送消息，当用户给非好友发消息时，SDK 会报20009错误码。
![](https://qcloudimg.tencent-cloud.cn/raw/56eebda5e424acc4f2a426bba5fe7c22.png)

### 好友列表管理

IM SDK 支持好友关系链逻辑，您可以调用 [getFriendList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendList.html) 接口获取好友列表，调用 [deleteFromFriendList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFromFriendList.html) 接口删除好友关系，也可以调用 [addFriend](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriend.html) 接口添加好友。

根据对方用户资料中的加好友需要验证与否，可以分为两种处理流程：

#### 第一种 加好友不需要验证
1. 用户 A 和 B 调用 [setFriendListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/setFriendListener.html) 设置关系链监听。
2. 用户 B 调用 [setSelfInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/setSelfInfo.html) 接口通过字段 `userFullInfo` 传入 V2TimUserFullInfo.fromJson({...})，将V2TimUserFullInfo中的 [allowType](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_user_full_info/V2TimUserFullInfo/allowType.html) 设置为加好友不需要验证 `AllowType.V2TIM_FRIEND_ALLOW_ANY`。
3. 用户 A 调用  [addFriend](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriend.html) 申请添加 B 为好友即可添加成功。如果申请参数中的 addType 设置为双向好友即 `FriendTypeEnum.V2TIM_FRIEND_TYPE_BOTH`，则用户 A 和 B 都会收到 [onFriendListAdded](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendListAdded.html) 回调；
	如果设置为单向好友即 `FriendTypeEnum.V2TIM_FRIEND_TYPE_SINGLE`，则只有用户 A 收到 [onFriendListAdded](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendListAdded.html) 回调。

#### 第二种 加好友需要验证
1. 用户 A 和 B 调用 [setFriendListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/setFriendListener.html) 设置关系链监听。
2. 用户 B 调用 [setSelfInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/setSelfInfo.html) 接口通过字段 `userFullInfo` 传入 V2TimUserFullInfo.fromJson({...})，将V2TimUserFullInfo中的 [allowType](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_user_full_info/V2TimUserFullInfo/allowType.html)  设置为加好友需要验证 `AllowType.V2TIM_FRIEND_NEED_CONFIRM`。
3. 用户 A 调用  [addFriend](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriend.html) 申请添加 B 为好友，接口的成功回调参数中 `V2TIMFriendOperationResult` 中的 [code](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_value_callback/V2TimValueCallback/code.html) 返回30539，表示需要等待用户 B 的验证，同时 A 和 B 都会收到 [onFriendApplicationListAdded](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendApplicationListAdded.html) 的回调。
4. 用户 B 会收到 [onFriendApplicationListAdded](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendApplicationListAdded.html) 的回调，当参数 `V2TIMFriendApplication` 中的 [tyoe](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_friend_application/V2TimFriendApplication/type.html) 为 `V2TIMFriendApplication.V2TIM_FRIEND_APPLICATION_COME_IN` 时，可以选择接受或者拒绝。
	- 调用 [acceptFriendApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/acceptFriendApplication.html) 接受好友请求，如果参数接受类型为 `FriendApplicationTypeEnum.V2TIM_FRIEND_ACCEPT_AGREE` 仅同意加单向好友时，A 会收到 [onFriendListAdded](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendListAdded.html) 回调，说明单向加好友成功，B 会收到 [onFriendApplicationListDeleted](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendApplicationListDeleted.html) 回调，此时 B 成为 A 的好友，但 A 仍不是 B 的好友。
	- 如果参数接受类型为 `FriendApplicationTypeEnum.V2TIM_FRIEND_ACCEPT_AGREE_AND_ADD` 同意加双向好友时，双方都会收到  [onFriendListAdded](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendListAdded.html) 回调，说明互相加好友成功。
	- 调用 [refuseFriendApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/refuseFriendApplication.html) 拒绝好友请求，双方都会收到 [onFriendApplicationListDeleted](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendApplicationListDeleted.html) 回调。

### 好友分组管理
在某些场景下，您可能需要对好友进行分组，例如分为 "大学同学"、"公司同事" 等，您可以调用以下接口实现。

| 功能描述 | 接口指引 |
|---------|---------|
| 新建好友分组 | [createFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/createFriendGroup.html) |
| 删除好友分组 | [deleteFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFriendGroup.html) |
| 修改好友分组 | [renameFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/renameFriendGroup.html) |
| 获取好友分组 |  [getFriendGroups](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendGroups.html) |
| 添加好友到一个分组 |  [addFriendsToFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriendsToFriendGroup.html) |
| 从分组中删除某好友 |  [deleteFriendsFromFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFriendsFromFriendGroup.html) |

## 常见使用问题

### 1. 非好友之间怎么禁止收发消息？
SDK 默认不限制非好友之间收发消息。如果您希望只允许好友之间收发消息，请在 [**即时通信 IM 控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **好友关系检查** 中开启"发送单聊消息检查关系链"。开启之后，给陌生人发消息时，SDK 会报20009错误码。

[](id:msgSendTips)
### 2. 被拉黑的用户发消息怎么给错误提示？
当消息发送者被拉黑后，发送者默认不会感知到“被拉黑”的状态，即发送消息后仍展示发送成功（实际上此时接收方不会收到消息）。如果需要被拉黑的发送者收到消息发送失败的提示，请在 [**即时通信 IM 控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **黑名单检查** 中关闭"发送消息后展示发送成功"，关闭后，被拉黑的发送者在发送消息时，SDK 会报20007错误码。

### 3. 增强版获取用户资料为什么不是最新的？
增强版 SDK 中用户资料的更新分好友和陌生人两种情况：
 - 好友资料：由于好友资料更新时，后台会主动向 SDK 发送系统通知，因此好友资料可以实时更新。
 - 陌生人资料：陌生人资料更新时，由于没有好友关系，后台无法向 SDK 发送系统通知，因此无法实时更新；为了避免每次获取用户资料都向后台发起网络请求，SDK 增加了缓存逻辑，对同一个用户主动向后台拉取资料的时间间隔为10分钟。
