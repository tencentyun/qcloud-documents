完整的文档请参见 [tencentCloudChatAPI 模块文档](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK)。

## 初始化登录接口

初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API                                                                                                                 | 描述                            |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [initSDK](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#initSDK)                               | 初始化 SDK                      |
| [unInitSDK](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#unInitSDK)                           | 反初始化 SDK                    |
| [login](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#login)                                   | 登录                            |
| [logout](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#logout)                                 | 登出                            |
| [getLoginUser](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getLoginUser)                     | 获取当前登录用户的 UserID       |
| [getLoginStatus](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getLoginStatus)                 | 获取登录状态                    |
| [getServerTime](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getServerTime)                   | 获取服务器当前时间（Web不支持） |
| [getVersion](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getVersion)                         | 获取版本号                      |


## 信令接口

| API                                                                                                                            | 描述             |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| [addSignalingListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addSignalingListener)       | 添加信令监听     |
| [removeSignalingListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#removeSignalingListener) | 移除信令监听     |
| [invite](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#invite)                                   | 邀请某个人       |
| [inviteInGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#inviteInGroup)                     | 邀请群内的某些人 |
| [cancel](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#cancel)                                   | 邀请方取消邀请   |
| [accept](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#accept)                                   | 接收方接受邀请   |
| [reject](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#reject)                                   | 接收方拒绝邀请   |
| [getSignalingInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getSignalingInfo)               | 获取信令信息     |
| [addInvitedSignaling](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addInvitedSignaling)         | 创建一个信令请求 |

## 创建消息接口

创建的消息会返回一个id字段，将id字段等传递给统一的发送接口（sendMessage）即可发送消息。

| API                                                                                                                                | 描述               |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [createTextMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createTextMessage)                   | 创建文本消息       |
| [createCustomMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createCustomMessage)               | 创建定制化消息     |
| [createImageMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createImageMessage)                 | 创建图片消息       |
| [createSoundMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createSoundMessage)                 | 创建音频文件       |
| [createVideoMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createVideoMessage)                 | 创建视频文件       |
| [createTextAtMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createTextAtMessage)               | 创建AT消息         |
| [createFileMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createFileMessage)                   | 创建文件消息       |
| [createLocationMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createLocationMessage)           | 创建位置信息       |
| [createFaceMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createFaceMessage)                   | 创建表情消息       |
| [createMergerMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createMergerMessage)               | 创建合并消息       |
| [createForwardMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createForwardMessage)             | 创建转发消息       |
| [createTargetedGroupMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createTargetedGroupMessage) | 创建一条定向群消息 |


## 消息收发接口

如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（原3.6.0前的高级消息部分接口已弃用，请使用新版创建消息接口后调用发送消息接口）。

| API                                                                                                                                            | 描述                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [addAdvancedMsgListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addAdvancedMsgListener)                     | 设置高级消息的事件监听器                                                                                                                         |
| [removeAdvancedMsgListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#removeAdvancedMsgListener)               | 移除高级消息的事件监听器                                                                                                                         |
| [getC2CHistoryMessageList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getC2CHistoryMessageList)                 | 获取单聊（C2C）历史消息                                                                                                                          |
| [getHistoryMessageList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getHistoryMessageList)                       | 获取历史消息高级接口                                                                                                                             |
| [getGroupHistoryMessageList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupHistoryMessageList)             | 获取群组历史消息                                                                                                                                 |
| [markC2CMessageAsRead](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#markC2CMessageAsRead)                         | 设置单聊（C2C）消息已读                                                                                                                          |
| [markGroupMessageAsRead](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#markGroupMessageAsRead)                     | 设置群组消息已读                                                                                                                                 |
| [markAllMessageAsRead](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#markAllMessageAsRead)                         | 标记所有消息为已读                                                                                                                               |
| [deleteMessageFromLocalStorage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteMessageFromLocalStorage)       | 删除本地消息                                                                                                                                     |
| [deleteMessages](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#clearC2CHistoryMessage)                                     | 删除本地及漫游消息                                                                                                                               |
| [insertGroupMessageToLocalStorage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#insertGroupMessageToLocalStorage) | 向群组消息列表中添加一条消息                                                                                                                     |
| [insertC2CMessageToLocalStorage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#insertC2CMessageToLocalStorage)     | 向C2C消息列表中添加一条消息                                                                                                                      |
| [clearC2CHistoryMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#clearC2CHistoryMessage)                     | 清空单聊本地及云端的消息（不删除会话）                                                                                                           |
| [clearGroupHistoryMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#clearGroupHistoryMessage)                 | 清空群组及云端的消息（不删除会话）                                                                                                               |
| [setC2CReceiveMessageOpt](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setC2CReceiveMessageOpt)                   | 设置针对某个用户的 C2C 消息接收选项（支持批量设置）                                                                                              |
| [getC2CReceiveMessageOpt](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getC2CReceiveMessageOpt)                   | 查询针对某个用户的 C2C 消息接收选项                                                                                                              |
| [setGroupReceiveMessageOpt](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setGroupReceiveMessageOpt)               | 修改群消息接收选项                                                                                                                               |
| [revokeMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#revokeMessage)                                       | 撤回消息的时间限制默认 2 minutes，超过 2 minutes 的消息不能撤回，您也可以在 控制台（功能配置 -> 登录与消息 -> 消息撤回设置）自定义撤回时间限制。 |
| [modifyMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#modifyMessage)                                       | 消息变更                                                                                                                                         |
| [sendMessage](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#sendMessage)                                           | 发送消息                                                                                                                                         |
| [searchLocalMessages](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#searchLocalMessages)                           | 搜索本地消息                                                                                                                                     |
| [sendMessageReadReceipts](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#sendMessageReadReceipts)                   | 发送群消息已读回执                                                                                                                               |
| [getMessageReadReceipts](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getMessageReadReceipts)                     | 获取自己发送消息的已读回执                                                                                                                       |
| [getGroupMessageReadMemberList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupMessageReadMemberList)       | 获取自己发送的群消息已读（未读）群成员列表                                                                                                       |

## 群组相关接口

腾讯云 IM SDK 支持五种预设的群组类型，每种类型都有其适用场景：

- 工作群（Work） ：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群，同旧版本中的 Private，同旧版本中的 Private。
- 公开群（Public） ：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息，同旧版本中的 ChatRoom，同旧版本中的 ChatRoom。
- 社群（Community）：创建后可以随意进出，适合用于知识分享和游戏交流等超大社区群聊场景。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API                                                                                                                            | 描述                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [addGroupListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addGroupListener)                        | 添加群组监听器                                                        |
| [removeGroupListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#removeGroupListener)                  | 移除群组监听器                                                        |
| [createGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createGroup)                             | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员            |
| [joinGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#joinGroup)                                      | 加入群组                                                              |
| [quitGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#quitGroup)                                      | 退出群组                                                              |
| [dismissGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#dismissGroup)                                | 解散群组（仅群主和管理员可以解散）                                    |
| [getJoinedGroupList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getJoinedGroupList)               | 获取已经加入的群列表（不包括已加入的直播群）                          |
| [getGroupsInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupsInfo)                         | 拉取群资料                                                            |
| [setGroupInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setGroupInfo)                           | 修改群资料                                                            |
| [initGroupAttributes](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#initGroupAttributes)            | 初始化群属性，会清空原有的群属性列表                                  |
| [setGroupAttributes](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setGroupAttributes)               | 设置群属性。已有该群属性则更新其 value 值，没有该群属性则添加该属性。 |
| [deleteGroupAttributes](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteGroupAttributes)         | 删除指定群属性，keys 传 null 则清空所有群属性。                       |
| [getGroupAttributes](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupAttributes)               | 获取指定群属性，keys 传 null 则获取所有群属性。                       |
| [searchGroups](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#searchGroups)                           | 搜索群列表                                                            |
| [getGroupOnlineMemberCount](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupOnlineMemberCount) | 获取指定群在线人数(目前只支持直播群)                                  |
| [getGroupMemberList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupMemberList)               | 获取群成员列表                                                        |
| [getGroupMembersInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupMembersInfo)             | 获取指定的群成员资料                                                  |
| [setGroupMemberInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setGroupMemberInfo)               | 修改指定的群成员资料                                                  |
| [searchGroupMembers](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#searchGroupMembers)               | 搜索群成员                                                            |
| [muteGroupMember](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#muteGroupMember)                     | 禁言                                                                  |
| [kickGroupMember](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#kickGroupMember)                     | 踢人                                                                  |
| [setGroupMemberRole](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setGroupMemberRole)               | 切换群成员的角色                                                      |
| [transferGroupOwner](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#transferGroupOwner)               | 转让群主                                                              |
| [inviteUserToGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#inviteUserToGroup)                 | 邀请他人入群                                                          |
| [getGroupApplicationList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getGroupApplicationList)     | 获取加群的申请列表                                                    |
| [acceptGroupApplication](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#acceptGroupApplication)       | 同意某一条加群申请                                                    |
| [refuseGroupApplication](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#refuseGroupApplication)       | 拒绝某一条加群申请                                                    |
| [setGroupApplicationRead](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setGroupApplicationRead)     | 标记申请列表为已读                                                    |
| [getJoinedCommunityList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getJoinedCommunityList)       | 获取当前用户已经加入的支持话题的社群列表                              |
| [createTopicInCommunity](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createTopicInCommunity)       | 创建话题                                                              |
| [deleteTopicFromCommunity](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteTopicFromCommunity)   | 删除话题                                                              |
| [setTopicInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setTopicInfo)                           | 设置话题属性                                                          |
| [getTopicInfoList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getTopicInfoList)                   | 获取话题属性的列表                                                    |

## 会话列表相关接口

会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API                                                                                                                                                       | 描述                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [addConversationListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addConversationListener)                         | 添加关系链监听器           |
| [removeConversationListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#removeConversationListener)                   | 移除关系链监听器           |
| [setConversationListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setConversationListener)                         | 设置会话监听器             |
| [getConversationList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getConversationList)                                 | 获取会话列表               |
| [getConversationListByConversaionIds](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getConversationListByConversaionIds) | 通过会话ID获取指定会话列表 |
| [pinConversation](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#pinConversation)                                         | 会话置顶                   |
| [getTotalUnreadMessageCount](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getTotalUnreadMessageCount)                   | 获取会话未读总数           |
| [getConversation](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getConversation)                                         | 获取指定会话               |
| [deleteConversation](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteConversation)                                   | 删除会话                   |
| [setConversationDraft](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setConversationDraft)                               | 设置会话草稿               |

## 用户资料相关接口

包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API                                                                                                                     | 描述                                         |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [getUsersInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getUsersInfo)                         | 获取用户资料                                 |
| [getUserStatus](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getUserStatus)                       | 获取用户在线状态                             |
| [setSelfInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setSelfInfo)                           | 修改个人资料                                 |
| [setSelfStatus](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setSelfStatus)                       | 设置当前登录用户在线状态                     |
| [addToBlackList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addToBlackList)           | 屏蔽某人的消息（添加该用户到黑名单中）       |
| [deleteFromBlackList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteFromBlackList) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getBlackList)               | 获取黑名单列表                               |

## 离线推送相关接口

如果想要在 App 切后台时依然能够实时收到 IM 消息，可以使用离线推送服务。由于大陆境内尚没有统一的推送服务，Android 的离线推送需要针对不同厂商的手机进行 [逐一适配](https://cloud.tencent.com/document/product/269/75428)。

| API                                                                                                                        | 描述                           |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [doBackground](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#doBackground)                 | 设置离线推送配置信息           |
| [doForeground](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#doForeground)                 | 设置离线推送配置信息           |
| [setOfflinePushConfig](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setOfflinePushConfig) | 设置离线推送配置信息           |

## 好友管理相关接口

腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [**控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **好友关系检查**中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API                                                                                                                                       | 描述                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| [addFriendListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addFriendListener)                       | 添加关系链监听器                                       |
| [removeFriendListener](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#removeFriendListener)                 | 移除关系链监听器                                       |
| [getFriendList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getFriendList)                               | 获取好友列表                                           |
| [getFriendsInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getFriendsInfo)                             | 获取指定好友资料                                       |
| [setFriendInfo](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setFriendInfo)                               | 设置指定好友资料                                       |
| [addFriend](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addFriend)                                       | 添加好友                                               |
| [deleteFromFriendList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteFromFriendList)                 | 删除好友                                               |
| [checkFriend](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#checkFriend)                                   | 检查指定用户的好友关系                                 |
| [getFriendApplicationList](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getFriendApplicationList)         | 获取好友申请列表                                       |
| [acceptFriendApplication](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#acceptFriendApplication)           | 同意好友申请                                           |
| [refuseFriendApplication](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#refuseFriendApplication)           | 拒绝好友申请                                           |
| [deleteFriendApplication](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteFriendApplication)           | 删除好友申请                                           |
| [setFriendApplicationRead](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#setFriendApplicationRead)         | 设置好友申请已读                                       |
| [createFriendGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#createFriendGroup)                       | 新建好友分组                                           |
| [getFriendGroups](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#getFriendGroups)                           | 获取分组信息                                           |
| [deleteFriendGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteFriendGroup)                       | 删除好友分组                                           |
| [renameFriendGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#renameFriendGroup)                       | 修改好友分组的名称                                     |
| [addFriendsToFriendGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#addFriendsToFriendGroup)           | 添加好友到一个好友分组                                 |
| [deleteFriendsFromFriendGroup](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#deleteFriendsFromFriendGroup) | 从好友分组中删除好友                                   |
| [searchFriends](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK#searchFriends)                               | 搜索好友                                               |
