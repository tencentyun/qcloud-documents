>?更为详细的接口，请参见  [Unity 全部接口](https://comm.qq.com/im/doc/unity/zh/)。

## 会话相关接口

<style>
table th:first-of-type {
    width: 50%;
}
table th:nth-of-type(2) {
    width: 50%;
}
</style>

| API                                                                                                                   | 描述               |
| --------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [ConvCancelDraft](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvCancelDraft.html)                               | 取消会话草稿       |
| [ConvDelete](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvDelete.html)                                         | 删除会话           |
| [ConvGetConvInfo](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvGetConvInfo.html)                               | 获取会话信息       |
| [ConvGetConvList](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvGetConvList.html)                               | 获取会话列表       |
| [ConvGetTotalUnreadMessageCount](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvGetTotalUnreadMessageCount.html) | 获取全部会话未读数 |
| [ConvPinConversation](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvPinConversation.html)                       | 会话置顶           |
| [ConvSetDraft](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvSetDraft.html)                                     | 设置会话草稿       |

## 关系链相关接口

| API                                                                                                                             | 描述                 |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [FriendshipAddFriend](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipAddFriend.html)                           | 添加好友             |
| [FriendshipAddToBlackList](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipAddToBlackList.html)                 | 添加黑名单           |
| [FriendshipCheckFriendType](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipCheckFriendType.html)               | 检测好友关系         |
| [FriendshipCreateFriendGroup](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipCreateFriendGroup.html)           | 创建好友分组         |
| [FriendshipDeleteFriend](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipDeleteFriend.html)                     | 删除好友             |
| [FriendshipDeleteFriendGroup](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipDeleteFriendGroup.html)           | 删除好友分组列表     |
| [FriendshipDeleteFromBlackList](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipDeleteFromBlackList.html)       | 从黑名单删除         |
| [FriendshipDeletePendency](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipDeletePendency.html)                 | 删除好友申请未决     |
| [FriendshipGetBlackList](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipGetBlackList.html)                     | 获取黑名单列表       |
| [FriendshipGetFriendGroupList](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipGetFriendGroupList.html)         | 获取好友分组列表     |
| [FriendshipGetFriendProfileList](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipGetFriendProfileList.html)     | 获取好友列表信息     |
| [FriendshipGetFriendsInfo](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipGetFriendsInfo.html)                 | 获取好友信息         |
| [FriendshipGetPendencyList](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipGetPendencyList.html)               | 获取好友申请未决     |
| [FriendshipHandleFriendAddRequest](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipHandleFriendAddRequest.html) | 处理好友申请         |
| [FriendshipModifyFriendGroup](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipModifyFriendGroup.html)           | 修改好友分组列表     |
| [FriendshipModifyFriendProfile](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipModifyFriendProfile.html)       | 修改好友信息         |
| [FriendshipReportPendencyReaded](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipReportPendencyReaded.html)     | 上报好友申请未决已读 |
| [FriendshipSearchFriends](https://comm.qq.com/im/doc/unity/zh/api/FriendshipApi/FriendshipSearchFriends.html)                   | 搜索好友             |

## 群组相关接口

| API                                                                                                                  | 描述                                     |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [GroupCreate](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupCreate.html)                                     | 创建群                                   |
| [GroupCreateTopicInCommunity](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupCreateTopicInCommunity.html)     | 创建话题                                 |
| [GroupDelete](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupDelete.html)                                     | 删除群                                   |
| [GroupDeleteGroupAttributes](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupDeleteGroupAttributes.html)       | 删除群自定义属性                         |
| [GroupDeleteMember](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupDeleteMember.html)                         | 踢出群成员                               |
| [GroupDeleteTopicFromCommunity](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupDeleteTopicFromCommunity.html) | 删除话题                                 |
| [GroupGetGroupAttributes](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetGroupAttributes.html)             | 获取群指定属性                           |
| [GroupGetGroupInfoList](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetGroupInfoList.html)                 | 获取群信息                               |
| [GroupGetJoinedCommunityList](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetJoinedCommunityList.html)     | 获取当前用户已经加入的支持话题的社群列表 |
| [GroupGetJoinedGroupList](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetJoinedGroupList.html)             | 获取已加入的群组列表                     |
| [GroupGetMemberInfoList](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetMemberInfoList.html)               | 获取群成员信息                           |
| [GroupGetOnlineMemberCount](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetOnlineMemberCount.html)         | 获取群在线用户数                         |
| [GroupGetPendencyList](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetPendencyList.html)                   | 获取群未决信息列表                       |
| [GroupGetTopicInfoList](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupGetTopicInfoList.html)                 | 获取话题列表                             |
| [GroupHandlePendency](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupHandlePendency.html)                     | 处理群未决信息                           |
| [GroupInitGroupAttributes](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupInitGroupAttributes.html)           | 初始化群自定义属性                       |
| [GroupInviteMember](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupInviteMember.html)                         | 邀请用户进群                             |
| [GroupJoin](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupJoin.html)                                         | 加入群                                   |
| [GroupModifyGroupInfo](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupModifyGroupInfo.html)                   | 修改群信息                               |
| [GroupModifyMemberInfo](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupModifyMemberInfo.html)                 | 修改群成员信息                           |
| [GroupQuit](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupQuit.html)                                         | 退出群                                   |
| [GroupReportPendencyReaded](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupReportPendencyReaded.html)         | 上报群未决信息已读                       |
| [GroupSearchGroupMembers](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupSearchGroupMembers.html)             | 搜索群成员                               |
| [GroupSearchGroups](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupSearchGroups.html)                         | 搜索群资料                               |
| [GroupSetGroupAttributes](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupSetGroupAttributes.html)             | 设置群属性                               |
| [GroupSetTopicInfo](https://comm.qq.com/im/doc/unity/zh/api/GroupApi/GroupSetTopicInfo.html)                         | 修改话题信息                             |

## IM SDK 初始化相关接口

| API                                                                                   | 描述                 |
| ------------------------------------------------------------------------------------- | -------------------- |
| [GetSDKVersion](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/GetSDKVersion.html) | 获取SDK底层库版本    |
| [GetServerTime](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/GetServerTime.html) | 获取服务端时间（秒） |
| [Init](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/Init.html)                   | 初始化IM SDK         |
| [SetConfig](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/SetConfig.html)         | 设置全局配置         |
| [Uninit](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/Uninit.html)               | 反初始化IM SDK       |


## 登录相关接口

| API                                                                                         | 描述               |
| ------------------------------------------------------------------------------------------- | ------------------ |
| [GetLoginStatus](https://comm.qq.com/im/doc/unity/zh/api/loginOrlogout/GetLoginStatus.html) | 获取当前登录状态   |
| [GetLoginUserID](https://comm.qq.com/im/doc/unity/zh/api/loginOrlogout/GetLoginUserID.html) | 获取当前登录用户ID |
| [Login](https://comm.qq.com/im/doc/unity/zh/api/loginOrlogout/Login.html)                   | 登录               |
| [Logout](https://comm.qq.com/im/doc/unity/zh/api/loginOrlogout/Logout.html)                 | 登出               |

## 消息相关接口

| API                                                                                                                          | 描述                                   |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [GetMsgGroupMessageReadMemberList](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/GetMsgGroupMessageReadMemberList.html) | 获取群消息已读群成员列表               |
| [MsgBatchSend](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgBatchSend.html)                                         | 批量发送消息                           |
| [MsgCancelSend](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgCancelSend.html)                                       | 取消消息发送                           |
| [MsgClearHistoryMessage](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgClearHistoryMessage.html)                     | 清除历史消息                           |
| [MsgDelete](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgDelete.html)                                               | 消息删除                               |
| [MsgDoBackground](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgDoBackground.html)                                   | APP 检测到应用退后台时可以调用此接口。 |
| [MsgDoForeground](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgDoForeground.html)                                   | APP 检测到应用进前台时可以调用此接口   |
| [MsgDownloadElemToPath](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgDownloadElemToPath.html)                       | 下载多媒体消息                         |
| [MsgDownloadMergerMessage](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgDownloadMergerMessage.html)                 | 下载合并消息                           |
| [MsgFindByMsgLocatorList](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgFindByMsgLocatorList.html)                   | 通过消息定位符查找消息                 |
| [MsgFindMessages](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgFindMessages.html)                                   | 从本地查找消息                         |
| [MsgGetC2CReceiveMessageOpt](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgGetC2CReceiveMessageOpt.html)             | 获取C2C收消息选项                      |
| [MsgGetMessageReadReceipts](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgGetMessageReadReceipts.html)               | 获取消息已读回执                       |
| [MsgGetMsgList](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgGetMsgList.html)                                       | 获取历史消息列表                       |
| [MsgImportMsgList](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgImportMsgList.html)                                 | 导入消息                               |
| [MsgListDelete](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgListDelete.html)                                       | 消息删除                               |
| [MsgMarkAllMessageAsRead](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgMarkAllMessageAsRead.html)                   | 标记所有消息为已读                     |
| [MsgModifyMessage](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgModifyMessage.html)                                 | 消息变更                               |
| [MsgReportReaded](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgReportReaded.html)                                   | 消息已读上报 C2C                       |
| [MsgRevoke](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgRevoke.html)                                               | 消息撤回                               |
| [MsgSaveMsg](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSaveMsg.html)                                             | 保存消息                               |
| [MsgSearchLocalMessages](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSearchLocalMessages.html)                     | 搜索本地消息                           |
| [MsgSendMessage](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSendMessage.html)                                     | 发送消息                               |
| [MsgSendMessageReadReceipts](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSendMessageReadReceipts.html)             | 发送消息已读回执                       |
| [MsgSetC2CReceiveMessageOpt](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSetC2CReceiveMessageOpt.html)             | 设置收消息选项                         |
| [MsgSetGroupReceiveMessageOpt](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSetGroupReceiveMessageOpt.html)         | 设置群收消息选项                       |
| [MsgSetLocalCustomData](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSetLocalCustomData.html)                       | 设置消息本地数据                       |
| [MsgSetOfflinePushToken](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSetOfflinePushToken.html)                     | 设置离线推送配置信息                   |

## 用户资料相关接口

| API                                                                                                               | 描述             |
| ----------------------------------------------------------------------------------------------------------------- | ---------------- |
| [GetUserStatus](https://comm.qq.com/im/doc/unity/zh/api/UserApi/GetUserStatus.html)                               | 查询用户状态     |
| [ProfileGetUserProfileList](https://comm.qq.com/im/doc/unity/zh/api/UserApi/ProfileGetUserProfileList.html)       | 获取用户信息列表 |
| [ProfileModifySelfUserProfile](https://comm.qq.com/im/doc/unity/zh/api/UserApi/ProfileModifySelfUserProfile.html) | 修改自己的信息   |
| [SetSelfStatus](https://comm.qq.com/im/doc/unity/zh/api/UserApi/SetSelfStatus.html)                               | 设置自己的状态   |
| [SubscribeUserStatus](https://comm.qq.com/im/doc/unity/zh/api/UserApi/SubscribeUserStatus.html)                   | 订阅用户状态     |
| [UnsubscribeUserStatus](https://comm.qq.com/im/doc/unity/zh/api/UserApi/UnsubscribeUserStatus.html)               | 取消订阅用户状态 |

## 注册SDK回调

| API                                                                                                                                                                | 描述                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| [AddRecvNewMsgCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/AddRecvNewMsgCallback.html)                                                 | 注册收到新消息回调                           |
| [RemoveRecvNewMsgCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/RemoveRecvNewMsgCallback.html)                                           | 移除收到新消息回调                           |
| [SetConvEventCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetConvEventCallback.html)                                                   | 设置会话事件回调                             |
| [SetConvTotalUnreadMessageCountChangedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetConvTotalUnreadMessageCountChangedCallback.html) | 设置会话未读消息总数变更的回调               |
| [SetFriendAddRequestCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetFriendAddRequestCallback.html)                                     | 设置好友添加请求的回调                       |
| [SetFriendApplicationListDeletedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetFriendApplicationListDeletedCallback.html)             | 设置好友申请被删除的回调                     |
| [SetFriendApplicationListReadCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetFriendApplicationListReadCallback.html)                   | 设置好友申请已读的回调                       |
| [SetFriendBlackListAddedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetFriendBlackListAddedCallback.html)                             | 设置黑名单新增的回调                         |
| [SetFriendBlackListDeletedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetFriendBlackListDeletedCallback.html)                         | 设置黑名单删除的回调                         |
| [SetGroupAttributeChangedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetGroupAttributeChangedCallback.html)                           | 设置群组属性变更回调                         |
| [SetGroupTipsEventCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetGroupTipsEventCallback.html)                                         | 设置群组系统消息回调                         |
| [SetGroupTopicChangedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetGroupTopicChangedCallback.html)                                   | 设置话题更新回调                             |
| [SetGroupTopicCreatedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetGroupTopicCreatedCallback.html)                                   | 设置话题创建回调                             |
| [SetGroupTopicDeletedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetGroupTopicDeletedCallback.html)                                   | 设置话题被删除回调                           |
| [SetKickedOfflineCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetKickedOfflineCallback.html)                                           | 设置被踢下线通知回调                         |
| [SetLogCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetLogCallback.html)                                                               | 设置日志回调                                 |
| [SetMsgElemUploadProgressCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetMsgElemUploadProgressCallback.html)                           | 设置消息内元素相关文件上传进度回调           |
| [SetMsgReadedReceiptCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetMsgReadedReceiptCallback.html)                                     | 设置消息已读回执回调                         |
| [SetMsgRevokeCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetMsgRevokeCallback.html)                                                   | 设置接收的消息被撤回回调                     |
| [SetMsgUpdateCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetMsgUpdateCallback.html)                                                   | 设置消息在云端被修改后回传回来的更新通知回调 |
| [SetNetworkStatusListenerCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetNetworkStatusListenerCallback.html)                           | 设置网络连接状态监听回调                     |
| [SetOnAddFriendCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetOnAddFriendCallback.html)                                               | 设置添加好友的回调                           |
| [SetOnDeleteFriendCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetOnDeleteFriendCallback.html)                                         | 设置删除好友的回调                           |
| [SetOnDeleteFriendCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetOnDeleteFriendCallback.html)                                         | 设置删除好友的回调                           |
| [SetSelfInfoUpdatedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetSelfInfoUpdatedCallback.html)                                       | 设置当前用户的资料发生更新时的回调           |
| [SetUpdateFriendProfileCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetUpdateFriendProfileCallback.html)                               | 设置更新好友资料的回调                       |
| [SetUserSigExpiredCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetUserSigExpiredCallback.html)                                         | 设置票据过期回调                             |
| [SetUserStatusChangedCallback](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetUserStatusChangedCallback.html)                                   | 设置用户状态变更通知回调                     |





