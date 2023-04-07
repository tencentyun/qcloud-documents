<dx-alert infotype="notice" title="温馨提示">
即时通信 IM 为您准备了 Flutter 的 API 调用示例，您可以访问 [GitHub](https://github.com/TencentCloud/chat-sdk-flutter/tree/main/example) 获取源码。
</dx-alert infotype="notice" title="温馨提示">

## 初始化登录接口

初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API                                                                                                                 | 描述                            |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [initSDK](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/initSDK.html)                               | 初始化 SDK                      |
| [unInitSDK](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/unInitSDK.html)                           | 反初始化 SDK                    |
| [login](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/login.html)                                   | 登录                            |
| [logout](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/logout.html)                                 | 登出                            |
| [getLoginUser](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getLoginUser.html)                     | 获取当前登录用户的 UserID       |
| [getLoginStatus](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getLoginStatus.html)                 | 获取登录状态                    |
| [getServerTime](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getServerTime.html)                   | 获取服务器当前时间（Web不支持） |
| [getVersion](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getVersion.html)                         | 获取版本号                      |
| [getConversationManager](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getConversationManager.html) | 会话功能入口                    |
| [getFriendshipManager](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getFriendshipManager.html)     | 关系链功能入口                  |
| [getGroupManager](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getGroupManager.html)               | 高级群组功能入口                |
| [getMessageManager](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getMessageManager.html)           | 高级消息功能入口                |
| [getOfflinePushManager](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getOfflinePushManager.html)   | 获取版本号                      |
| [getSignalingManager](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getSignalingManager.html)       | 信令入口                        |

## 信令接口

| API                                                                                                                            | 描述             |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| [addSignalingListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/addSignalingListener.html)       | 添加信令监听     |
| [removeSignalingListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/removeSignalingListener.html) | 移除信令监听     |
| [invite](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/invite.html)                                   | 邀请某个人       |
| [inviteInGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/inviteInGroup.html)                     | 邀请群内的某些人 |
| [cancel](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/cancel.html)                                   | 邀请方取消邀请   |
| [accept](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/accept.html)                                   | 接收方接受邀请   |
| [reject](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/reject.html)                                   | 接收方拒绝邀请   |
| [getSignalingInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/getSignalingInfo.html)               | 获取信令信息     |
| [addInvitedSignaling](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMSignalingManager/addInvitedSignaling.html)         | 创建一个信令请求 |

## 创建消息接口

创建的消息会返回一个id字段，将id字段等传递给统一的发送接口（sendMessage）即可发送消息。

| API                                                                                                                                | 描述               |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [createTextMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createTextMessage.html)                   | 创建文本消息       |
| [createCustomMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createCustomMessage.html)               | 创建定制化消息     |
| [createImageMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createImageMessage.html)                 | 创建图片消息       |
| [createSoundMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createSoundMessage.html)                 | 创建音频文件       |
| [createVideoMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createVideoMessage.html)                 | 创建视频文件       |
| [createTextAtMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createTextAtMessage.html)               | 创建AT消息         |
| [createFileMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createFileMessage.html)                   | 创建文件消息       |
| [createLocationMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createLocationMessage.html)           | 创建位置信息       |
| [createFaceMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createFaceMessage.html)                   | 创建表情消息       |
| [createMergerMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createMergerMessage.html)               | 创建合并消息       |
| [createForwardMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createForwardMessage.html)             | 创建转发消息       |
| [createTargetedGroupMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/createTargetedGroupMessage.html) | 创建一条定向群消息 |
| [appendMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/appendMessage.html)                           | 添加多Element消息  |

## 消息收发接口

如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（原3.6.0前的高级消息部分接口已弃用，请使用新版创建消息接口后调用发送消息接口）。

| API                                                                                                                                            | 描述                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [addAdvancedMsgListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/addAdvancedMsgListener.html)                     | 设置高级消息的事件监听器                                                                                                                         |
| [removeAdvancedMsgListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/removeAdvancedMsgListener.html)               | 移除高级消息的事件监听器                                                                                                                         |
| [getC2CHistoryMessageList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/getC2CHistoryMessageList.html)                 | 获取单聊（C2C）历史消息                                                                                                                          |
| [getHistoryMessageList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/getHistoryMessageList.html)                       | 获取历史消息高级接口                                                                                                                             |
| [getGroupHistoryMessageList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/getGroupHistoryMessageList.html)             | 获取群组历史消息                                                                                                                                 |
| [markC2CMessageAsRead](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/markC2CMessageAsRead.html)                         | 设置单聊（C2C）消息已读                                                                                                                          |
| [markGroupMessageAsRead](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/markGroupMessageAsRead.html)                     | 设置群组消息已读                                                                                                                                 |
| [markAllMessageAsRead](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/markAllMessageAsRead.html)                         | 标记所有消息为已读                                                                                                                               |
| [deleteMessageFromLocalStorage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/deleteMessageFromLocalStorage.html)       | 删除本地消息                                                                                                                                     |
| [deleteMessages](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/deleteMessages.html)                                     | 删除本地及漫游消息                                                                                                                               |
| [insertGroupMessageToLocalStorage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/insertGroupMessageToLocalStorage.html) | 向群组消息列表中添加一条消息                                                                                                                     |
| [insertC2CMessageToLocalStorage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/insertC2CMessageToLocalStorage.html)     | 向C2C消息列表中添加一条消息                                                                                                                      |
| [clearC2CHistoryMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/clearC2CHistoryMessage.html)                     | 清空单聊本地及云端的消息（不删除会话）                                                                                                           |
| [clearGroupHistoryMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/clearGroupHistoryMessage.html)                 | 清空群组及云端的消息（不删除会话）                                                                                                               |
| [downloadMergerMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/downloadMergerMessage.html)                       | 获取合并消息的子消息                                                                                                                             |
| [reSendMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/reSendMessage.html)                                       | 消息重发                                                                                                                                         |
| [setC2CReceiveMessageOpt](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/setC2CReceiveMessageOpt.html)                   | 设置针对某个用户的 C2C 消息接收选项（支持批量设置）                                                                                              |
| [getC2CReceiveMessageOpt](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/getC2CReceiveMessageOpt.html)                   | 查询针对某个用户的 C2C 消息接收选项                                                                                                              |
| [setGroupReceiveMessageOpt](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/setGroupReceiveMessageOpt.html)               | 修改群消息接收选项                                                                                                                               |
| [setLocalCustomData](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/setLocalCustomData.html)                             | 设置消息自定义数据（本地保存，不会发送到对端，程序卸载重装后失效）                                                                               |
| [setLocalCustomInt](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/setLocalCustomInt.html)                               | 设置消息自定义数据，可以用来标记语音、视频消息是否已经播放（本地保存，不会发送到对端，程序卸载重装后失效）                                       |
| [revokeMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/revokeMessage.html)                                       | 撤回消息的时间限制默认 2 minutes，超过 2 minutes 的消息不能撤回，您也可以在 控制台（功能配置 -> 登录与消息 -> 消息撤回设置）自定义撤回时间限制。 |
| [modifyMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/modifyMessage.html)                                       | 消息变更                                                                                                                                         |
| [sendMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/sendMessage.html)                                           | 发送消息                                                                                                                                         |
| [sendReplyMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/sendReplyMessage.html)                                 | 发送回复消息                                                                                                                                     |
| [searchLocalMessages](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/searchLocalMessages.html)                           | 搜索本地消息                                                                                                                                     |
| [sendMessageReadReceipts](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/sendMessageReadReceipts.html)                   | 发送群消息已读回执                                                                                                                               |
| [getMessageReadReceipts](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/getMessageReadReceipts.html)                     | 获取自己发送消息的已读回执                                                                                                                       |
| [getGroupMessageReadMemberList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/getGroupMessageReadMemberList.html)       | 获取自己发送的群消息已读（未读）群成员列表                                                                                                       |

## 群组相关接口

腾讯云 IM SDK 支持五种预设的群组类型，每种类型都有其适用场景：

- 工作群（Work） ：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群，同旧版本中的 Private，同旧版本中的 Private。
- 公开群（Public） ：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息，同旧版本中的 ChatRoom，同旧版本中的 ChatRoom。
- 社群（Community）：创建后可以随意进出，适合用于知识分享和游戏交流等超大社区群聊场景。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API                                                                                                                            | 描述                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [addGroupListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/addGroupListener.html)                        | 添加群组监听器                                                        |
| [setGroupListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/setGroupListener.html)                        | 设置群组相关的事件监听器                                              |
| [removeGroupListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/removeGroupListener.html)                  | 移除群组监听器                                                        |
| [createGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/createGroup.html)                             | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员            |
| [joinGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/joinGroup.html)                                      | 加入群组                                                              |
| [quitGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/quitGroup.html)                                      | 退出群组                                                              |
| [dismissGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/dismissGroup.html)                                | 解散群组（仅群主和管理员可以解散）                                    |
| [getJoinedGroupList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getJoinedGroupList.html)               | 获取已经加入的群列表（不包括已加入的直播群）                          |
| [getGroupsInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getGroupsInfo.html)                         | 拉取群资料                                                            |
| [setGroupInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/setGroupInfo.html)                           | 修改群资料                                                            |
| [initGroupAttributes](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/initGroupAttributes.html )            | 初始化群属性，会清空原有的群属性列表                                  |
| [setGroupAttributes](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/setGroupAttributes.html)               | 设置群属性。已有该群属性则更新其 value 值，没有该群属性则添加该属性。 |
| [deleteGroupAttributes](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/deleteGroupAttributes.html)         | 删除指定群属性，keys 传 null 则清空所有群属性。                       |
| [getGroupAttributes](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getGroupAttributes.html)               | 获取指定群属性，keys 传 null 则获取所有群属性。                       |
| [searchGroups](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/searchGroups.html)                           | 搜索群列表                                                            |
| [getGroupOnlineMemberCount](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getGroupOnlineMemberCount.html) | 获取指定群在线人数(目前只支持直播群)                                  |
| [getGroupMemberList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getGroupMemberList.html)               | 获取群成员列表                                                        |
| [getGroupMembersInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getGroupMembersInfo.html)             | 获取指定的群成员资料                                                  |
| [setGroupMemberInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/setGroupMemberInfo.html)               | 修改指定的群成员资料                                                  |
| [searchGroupMembers](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/searchGroupMembers.html)               | 搜索群成员                                                            |
| [muteGroupMember](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/muteGroupMember.html)                     | 禁言                                                                  |
| [kickGroupMember](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/kickGroupMember.html)                     | 踢人                                                                  |
| [setGroupMemberRole](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/setGroupMemberRole.html)               | 切换群成员的角色                                                      |
| [transferGroupOwner](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/transferGroupOwner.html)               | 转让群主                                                              |
| [inviteUserToGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/inviteUserToGroup.html)                 | 邀请他人入群                                                          |
| [getGroupApplicationList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getGroupApplicationList.html)     | 获取加群的申请列表                                                    |
| [acceptGroupApplication](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/acceptGroupApplication.html)       | 同意某一条加群申请                                                    |
| [refuseGroupApplication](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/refuseGroupApplication.html)       | 拒绝某一条加群申请                                                    |
| [setGroupApplicationRead](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/setGroupApplicationRead.html)     | 标记申请列表为已读                                                    |
| [getJoinedCommunityList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getJoinedCommunityList.html)       | 获取当前用户已经加入的支持话题的社群列表                              |
| [createTopicInCommunity](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/createTopicInCommunity.html)       | 创建话题                                                              |
| [deleteTopicFromCommunity](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/deleteTopicFromCommunity.html)   | 删除话题                                                              |
| [setTopicInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/setTopicInfo.html)                           | 设置话题属性                                                          |
| [getTopicInfoList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMGroupManager/getTopicInfoList.html)                   | 获取话题属性的列表                                                    |

## 会话列表相关接口

会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API                                                                                                                                                       | 描述                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [addConversationListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/addConversationListener.html)                         | 添加关系链监听器           |
| [removeConversationListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/removeConversationListener.html)                   | 移除关系链监听器           |
| [setConversationListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/setConversationListener.html)                         | 设置会话监听器             |
| [getConversationList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/getConversationList.html)                                 | 获取会话列表               |
| [getConversationListByConversaionIds](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/getConversationListByConversaionIds.html) | 通过会话ID获取指定会话列表 |
| [pinConversation](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/pinConversation.html)                                         | 会话置顶                   |
| [getTotalUnreadMessageCount](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/getTotalUnreadMessageCount.html)                   | 获取会话未读总数           |
| [getConversation](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/getConversation.html)                                         | 获取指定会话               |
| [deleteConversation](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/deleteConversation.html)                                   | 删除会话                   |
| [setConversationDraft](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMConversationManager/setConversationDraft.html)                               | 设置会话草稿               |

## 用户资料相关接口

包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API                                                                                                                     | 描述                                         |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [getUsersInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getUsersInfo.html)                         | 获取用户资料                                 |
| [getUserStatus](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/getUserStatus.html)                       | 获取用户在线状态                             |
| [setSelfInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/setSelfInfo.html)                           | 修改个人资料                                 |
| [setSelfStatus](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/setSelfStatus.html)                       | 设置当前登录用户在线状态                     |
| [addToBlackList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/addToBlackList.html)           | 屏蔽某人的消息（添加该用户到黑名单中）       |
| [deleteFromBlackList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/deleteFromBlackList.html) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/getBlackList.html)               | 获取黑名单列表                               |

## 离线推送相关接口

如果想要在 App 切后台时依然能够实时收到 IM 消息，可以使用离线推送服务。由于大陆境内尚没有统一的推送服务，Android 的离线推送需要针对不同厂商的手机进行 [逐一适配](https://cloud.tencent.com/document/product/269/75428)。

| API                                                                                                                        | 描述                           |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [setAPNSListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMManager/setAPNSListener.html)                      | 设置苹果系统离线推送专用监听器 |
| [doBackground](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMOfflinePushManager/doBackground.html)                 | 设置离线推送配置信息           |
| [doForeground](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMOfflinePushManager/doForeground.html)                 | 设置离线推送配置信息           |
| [setOfflinePushConfig](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMOfflinePushManager/setOfflinePushConfig.html) | 设置离线推送配置信息           |

## 好友管理相关接口

腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [**控制台**](https://console.cloud.tencent.com/im) >**功能配置**>**登录与消息**>**好友关系检查**中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API                                                                                                                                       | 描述                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| [setFriendListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/setFriendListener.html)                       | 设置关系链的监听器，用于接收好友列表和黑名单的变更事件 |
| [addFriendListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/addFriendListener.html)                       | 添加关系链监听器                                       |
| [removeFriendListener](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/removeFriendListener.html)                 | 移除关系链监听器                                       |
| [getFriendList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/getFriendList.html)                               | 获取好友列表                                           |
| [getFriendsInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/getFriendsInfo.html)                             | 获取指定好友资料                                       |
| [setFriendInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/setFriendInfo.html)                               | 设置指定好友资料                                       |
| [addFriend](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/addFriend.html)                                       | 添加好友                                               |
| [deleteFromFriendList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/deleteFromFriendList.html)                 | 删除好友                                               |
| [checkFriend](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/checkFriend.html)                                   | 检查指定用户的好友关系                                 |
| [getFriendApplicationList](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/getFriendApplicationList.html)         | 获取好友申请列表                                       |
| [acceptFriendApplication](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/acceptFriendApplication.html)           | 同意好友申请                                           |
| [refuseFriendApplication](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/refuseFriendApplication.html)           | 拒绝好友申请                                           |
| [deleteFriendApplication](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/deleteFriendApplication.html)           | 删除好友申请                                           |
| [setFriendApplicationRead](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/setFriendApplicationRead.html)         | 设置好友申请已读                                       |
| [createFriendGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/createFriendGroup.html)                       | 新建好友分组                                           |
| [getFriendGroups](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/getFriendGroups.html)                           | 获取分组信息                                           |
| [deleteFriendGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/deleteFriendGroup.html)                       | 删除好友分组                                           |
| [renameFriendGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/renameFriendGroup.html)                       | 修改好友分组的名称                                     |
| [addFriendsToFriendGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/addFriendsToFriendGroup.html)           | 添加好友到一个好友分组                                 |
| [deleteFriendsFromFriendGroup](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/deleteFriendsFromFriendGroup.html) | 从好友分组中删除好友                                   |
| [searchFriends](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMFriendshipManager/searchFriends.html)                               | 搜索好友                                               |
