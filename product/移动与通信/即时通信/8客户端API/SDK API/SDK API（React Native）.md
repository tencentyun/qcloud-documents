## 初始化登录接口
<style>
table th:first-of-type {
    width: 50%;
}
table th:nth-of-type(2) {
    width: 50%;
}
</style>

初始化并成功登录，是正常使用腾讯云 IM 服务的前提。


| API                                                                                     | 描述                      |
| --------------------------------------------------------------------------------------- | ------------------------- |
| [initSDK](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/initSDK.html)               | 初始化 SDK                |
| [unInitSDK](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/unInitSDK.html)           | 反初始化 SDK              |
| [login](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/login.html)                   | 登录                      |
| [logout](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/logout.html)                 | 登出                      |
| [getLoginUser](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/getLoginUser.html)     | 获取当前登录用户的 UserID |
| [getLoginStatus](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/getLoginStatus.html) | 获取登录状态              |
| [getServerTime](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/getServerTime.html)   | 获取服务器当前时间        |
| [getVersion](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/getVersion.html)         | 获取版本号                |

## 信令接口

| API                                                                                                                | 描述             |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |
| [accept](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/accept.html)                                   | 接收方接受邀请   |
| [addInvitedSignaling](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/addInvitedSignaling.html)         | 创建一个信令请求 |
| [addSignalingListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/addSignalingListener.html)       | 添加信令监听     |
| [cancel](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/cancel.html)                                   | 邀请方取消邀请   |
| [getSignalingInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/getSignalingInfo.html)               | 获取信令信息     |
| [invite](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/invite.html)                                   | 邀请某个人       |
| [inviteInGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/inviteInGroup.html)                     | 邀请群内的某些人 |
| [reject](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/reject.html)                                   | 接收方拒绝邀请   |
| [removeSignalingListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMSignalingManager/removeSignalingListener.html) | 移除信令监听器   |

## 消息相关接口

| API                                                                                                                                | 描述                                                |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [addAdvancedMsgListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/addAdvancedMsgListener.html)                     | 添加高级消息的事件监听器                            |
| [appendMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/appendMessage.html)                                       | 为一条消息，附着另一条消息，添加至链表。            |
| [clearC2CHistoryMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/clearC2CHistoryMessage.html)                     | 清空单聊本地及云端的消息（不删除会话）              |
| [clearGroupHistoryMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/clearGroupHistoryMessage.html)                 | 清空群聊本地及云端的消息（不删除会话）              |
| [createCustomMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createCustomMessage.html)                           | 创建定制化消息                                      |
| [createFaceMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createFaceMessage.html)                               | 创建表情消息                                        |
| [createFileMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createFileMessage.html)                               | 创建文件消息                                        |
| [createForwardMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createForwardMessage.html)                         | 创建转发消息                                        |
| [createImageMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createImageMessage.html)                             | 创建图片消息                                        |
| [createLocationMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createLocationMessage.html)                       | 创建位置信息                                        |
| [createMergerMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createMergerMessage.html)                           | 创建合并消息                                        |
| [createSoundMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createSoundMessage.html)                             | 创建音频消息                                        |
| [createTargetedGroupMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createTargetedGroupMessage.html)             | 创建一条定向群消息                                  |
| [createTextAtMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createTextAtMessage.html)                           | 创建文本消息，并且可以附带 @ 提醒功能(直播群不支持) |
| [createTextMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createTextMessage.html)                               | 创建文本消息                                        |
| [createVideoMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/createVideoMessage.html)                             | 创建视频文件                                        |
| [deleteMessageExtensions](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/deleteMessageExtensions.html)                   | 删除消息扩展                                        |
| [deleteMessageFromLocalStorage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/deleteMessageFromLocalStorage.html)       | 删除本地消息                                        |
| [deleteMessages](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/deleteMessages.html)                                     | 删除本地及漫游消息                                  |
| [downloadMergerMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/downloadMergerMessage.html)                       | 获取合并消息的子消息列表                            |
| [downloadMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/downloadMessage.html)                                   | 下载多媒体消息                                      |
| [getC2CHistoryMessageList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getC2CHistoryMessageList.html)                 | 获取单聊历史消息                                    |
| [getC2CReceiveMessageOpt](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getC2CReceiveMessageOpt.html)                   | 查询某个用户的 C2C 消息接收选项                     |
| [getGroupHistoryMessageList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getGroupHistoryMessageList.html)             | 获取群组历史消息                                    |
| [getGroupMessageReadMemberList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getGroupMessageReadMemberList.html)       | 获取群消息已读或未读群成员列表                      |
| [getHistoryMessageList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getHistoryMessageList.html)                       | 获取历史消息高级接口                                |
| [getMessageExtensions](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getMessageExtensions.html)                         | 获取消息扩展                                        |
| [getMessageOnlineUrl](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getMessageOnlineUrl.html)                           | 获取多媒体消息URL                                   |
| [getMessageReadReceipts](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/getMessageReadReceipts.html)                     | 获取消息已读回执。                                  |
| [insertC2CMessageToLocalStorage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/insertC2CMessageToLocalStorage.html)     | 向C2C消息列表中添加一条消息                         |
| [insertGroupMessageToLocalStorage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/insertGroupMessageToLocalStorage.html) | 向群组消息列表中添加一条消息                        |
| [markAllMessageAsRead](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/markAllMessageAsRead.html)                         | 标记所有消息为已读                                  |
| [markC2CMessageAsRead](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/markC2CMessageAsRead.html)                         | 设置单聊消息已读                                    |
| [markGroupMessageAsRead](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/markGroupMessageAsRead.html)                     | 设置群组消息已读                                    |
| [modifyMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/modifyMessage.html)                                       | 消息编辑                                            |
| [removeAdvancedMsgListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/removeAdvancedMsgListener.html)               | 移除高级消息监听器                                  |
| [reSendMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/reSendMessage.html)                                       | 消息重发                                            |
| [revokeMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/revokeMessage.html)                                       | 撤回消息                                            |
| [searchLocalMessages](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/searchLocalMessages.html)                           | 搜索本地消息                                        |
| [sendMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/sendMessage.html)                                           | 发送消息                                            |
| [sendMessageReadReceipts](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/sendMessageReadReceipts.html)                   | 发送消息已读回执                                    |
| [sendReplyMessage](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/sendReplyMessage.html)                                 | 发送回复消息                                        |
| [setC2CReceiveMessageOpt](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/setC2CReceiveMessageOpt.html)                   | 设置用户消息接收选项                                |
| [setGroupReceiveMessageOpt](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/setGroupReceiveMessageOpt.html)               | 设置群组消息接收选项                                |
| [setLocalCustomData](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/setLocalCustomData.html)                             | 设置消息自定义数据                                  |
| [setLocalCustomInt](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/setLocalCustomInt.html)                               | 设置消息自定义数据                                  |
| [setMessageExtensions](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/setMessageExtensions.html)                         | 设置消息扩展                                        |




## 会话相关接口

| API                                                                                                                                           | 描述                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [addConversationListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/addConversationListener.html)                         | 设置会话监听器             |
| [deleteConversation](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/deleteConversation.html)                                   | 删除会话                   |
| [getConversation](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/getConversation.html)                                         | 获取会话信息               |
| [getConversationList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/getConversationList.html)                                 | 获取会话列表               |
| [getConversationListByConversaionIds](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/getConversationListByConversaionIds.html) | 通过会话ID获取指定会话列表 |
| [getTotalUnreadMessageCount](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/getTotalUnreadMessageCount.html)                   | 获取会话未读总数           |
| [pinConversation](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/pinConversation.html)                                         | 会话置顶                   |
| [removeConversationListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/removeConversationListener.html)                   | 移除会话监听器             |
| [setConversationDraft](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMConversationManager/setConversationDraft.html)                               | 设置会话草稿               |


## 关系链相关接口

| API       | 描述                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [acceptFriendApplication](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/acceptFriendApplication.html)           | 同意好友申请           |
| [addFriend](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/addFriend.html)                                       | 添加好友               |
| [addFriendListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/addFriendListener.html)                       | 添加关系链监听器       |
| [addFriendsToFriendGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/addFriendsToFriendGroup.html)           | 添加好友到一个好友分组 |
| [addToBlackList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/addToBlackList.html)                             | 添加用户到黑名单       |
| [checkFriend](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/checkFriend.html)                                   | 检查指定用户的好友关系 |
| [createFriendGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/createFriendGroup.html)                       | 新建好友分组           |
| [deleteFriendApplication](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/deleteFriendApplication.html)           | 删除好友申请           |
| [deleteFriendGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/deleteFriendGroup.html)                       | 删除好友分组           |
| [deleteFriendsFromFriendGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/deleteFriendsFromFriendGroup.html) | 同意好友申请           |
| [deleteFromBlackList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/deleteFromBlackList.html)                   | 把用户从黑名单中删除   |
| [deleteFromFriendList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/deleteFromFriendList.html)                 | 删除好友               |
| [getBlackList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/getBlackList.html)                                 | 获取黑名单列表         |
| [getFriendApplicationList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/getFriendApplicationList.html)         | 获取好友申请列表       |
| [getFriendGroups](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/getFriendGroups.html)                           | 获取好友分组列表       |
| [getFriendList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/getFriendList.html)                               | 获取好友列表           |
| [getFriendsInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/getFriendsInfo.html)                             | 获取指定好友资料       |
| [refuseFriendApplication](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/refuseFriendApplication.html)           | 拒绝好友申请           |
| [removeFriendListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/removeFriendListener.html)                 | 移除关系链监听器       |
| [renameFriendGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/renameFriendGroup.html)                       | 修改好友分组的名称     |
| [searchFriends](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/searchFriends.html)                               | 搜索好友               |
| [setFriendApplicationRead](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/setFriendApplicationRead.html)         | 设置好友申请已读       |
| [setFriendInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMFriendshipManager/setFriendInfo.html)                               | 设置指定好友资料       |

## 群组相关接口

| API        | 描述                                     |
| ----------------------------------- | ---------------------------------------- |
| [addGroupListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/addGroupListener.html)                       | 添加群组监听器                           |
| [dismissGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/dismissGroup.html)                               | 解散群组                                 |
| [joinGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/joinGroup.html)                                     | 加入群组                                 |
| [quitGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/quitGroup.html)                                     | 退出群组                                 |
| [removeGroupListener](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMManager/removeGroupListener.html)                 | 移除群组监听器                           |
| [acceptGroupApplication](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/acceptGroupApplication.html)       | 同意某一条加群申请                       |
| [createGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/createGroup.html)                             | 创建自定义群组                           |
| [createTopicInCommunity](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/createTopicInCommunity.html)       | 创建话题                                 |
| [deleteGroupAttributes](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/deleteGroupAttributes.html)         | 删除指定群属性                           |
| [deleteTopicFromCommunity](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/deleteTopicFromCommunity.html)   | 删除话题                                 |
| [getGroupApplicationList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getGroupApplicationList.html)     | 获取加群的申请列表                       |
| [getGroupAttributes](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getGroupAttributes.html)               | 获取指定群属性                           |
| [getGroupMemberList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getGroupMemberList.html)               | 获取群成员列表                           |
| [getGroupMembersInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getGroupMembersInfo.html)             | 获取指定的群成员资料                     |
| [getGroupOnlineMemberCount](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getGroupOnlineMemberCount.html) | 获取指定群在线人数                       |
| [getGroupsInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getGroupsInfo.html)                         | 获取群资料                               |
| [getJoinedCommunityList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getJoinedCommunityList.html)       | 获取当前用户已经加入的支持话题的社群列表 |
| [getJoinedGroupList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getJoinedGroupList.html)               | 获取当前用户已经加入的群组               |
| [getTopicInfoList](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/getTopicInfoList.html)                   | 获取话题属性的列表                       |
| [initGroupAttributes](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/initGroupAttributes.html)             | 初始化群属性                             |
| [inviteUserToGroup](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/inviteUserToGroup.html)                 | 邀请他人入群                             |
| [kickGroupMember](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/kickGroupMember.html)                     | 踢人                                     |
| [muteGroupMember](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/muteGroupMember.html)                     | 禁言                                     |
| [refuseGroupApplication](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/refuseGroupApplication.html)       | 拒绝某一条加群申请                       |
| [searchGroupMembers](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/searchGroupMembers.html)               | 搜索群成员                               |
| [searchGroups](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/searchGroups.html)                           | 搜索群资料                               |
| [setGroupApplicationRead](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/setGroupApplicationRead.html)     | 标记所有群组申请列表为已读               |
| [setGroupAttributes](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/setGroupAttributes.html)               | 设置群属性                               |
| [setGroupInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/setGroupInfo.html)                           | 修改群资料                               |
| [setGroupMemberInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/setGroupMemberInfo.html)               | 修改指定的群成员资料                     |
| [setGroupMemberRole](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/setGroupMemberRole.html)               | 设置群成员的角色                         |
| [setTopicInfo](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/setTopicInfo.html)                           | 设置话题属性                             |
| [transferGroupOwner](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMGroupManager/transferGroupOwner.html)               | 转让群主                                 |

## 离线推送相关接口

| API                                                                                                            | 描述                                     |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [doBackground](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMOfflinePushManager/doBackground.html)                 | APP 检测到应用退后台时可以调用此接口     |
| [doForeground](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMOfflinePushManager/doForeground.html)                 | APP 检测到应用返回到前台时可以调用此接口 |
| [setOfflinePushConfig](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMOfflinePushManager/setOfflinePushConfig.html) | 设置离线推送配置信息                     |
