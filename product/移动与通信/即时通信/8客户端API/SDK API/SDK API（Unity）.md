## 初始化登录接口

初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API | 描述 |
|---------|---------|
| [initSDK](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_initSDK_System_Int32_com_tencent_imsdk_unity_LogLevel_) | 初始化 SDK |
| [unInitSDK](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_unInitSDK) | 反初始化 SDK |
| [login](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_login_System_String_System_String_) | 登录 |
| [logout](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_logout) | 登出 |
| [getLoginStatus](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_getLoginStatus) | 获取登录状态 |
| [getLoginUser](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_getLoginUser) | 获取当前登录用户的 UserID |

## 高级消息收发接口

如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（简单消息接口和高级消息接口请不要混用）。

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_addAdvancedMsgListener) | 设置高级消息的事件监听器， 请不要同 addSimpleMsgListener 混用 |
| [sendCustomMessage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_sendCustomMessage_System_String_System_String_System_Int32_System_Boolean_System_String_) | 发送自定义消息 |
| [sendImageMessage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_sendImageMessage_System_String_System_String_System_Int32_System_Boolean_System_String_) | 发送图片消息 |
| [sendSoundMessage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_sendSoundMessage_System_String_System_String_System_Int32_System_Boolean_System_String_System_Int32_) | 发送语音消息 |
| [sendVideoMessage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_sendVideoMessage_System_String_System_String_System_Int32_System_Boolean_System_String_System_String_System_String_System_Int32_) | 发送视频消息 |
| [sendFileMessage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_sendFileMessage_System_String_System_String_System_Int32_System_Boolean_System_String_System_String_) | 发送文件消息 |
| [sendLocationMessage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_sendLocationMessage_System_String_System_String_System_Int32_System_Boolean_System_Double_System_Double_) | 发送地理位置消息 |
| [getC2CHistoryMessageList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_getC2CHistoryMessageList_System_Int32_System_String_System_String_) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_getGroupHistoryMessageList_System_Int32_System_String_System_String_) | 获取群组历史消息 |
| [markC2CMessageAsRead](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_markC2CMessageAsRead_System_String_) | 设置单聊（C2C）消息已读 |
| [markGroupMessageAsRead](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_markGroupMessageAsRead_System_String_) | 设置群组消息已读 |
| [deleteMessageFromLocalStorage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_deleteMessageFromLocalStorage_System_String_) | 删除本地消息 |
| [insertGroupMessageToLocalStorage](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMMessageManager.html#com_tencent_imsdk_unity_V2TIMMessageManager_insertGroupMessageToLocalStorage_System_String_System_String_System_String_) | 向群组消息列表中添加一条消息 |

## 群组相关接口

腾讯云 IM SDK 支持四种预设的群组类型，每种类型都有其适用场景：
- 工作群（Work）	：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群，同旧版本中的 Private。
- 公开群（Public）	：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息，同旧版本中的 ChatRoom。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API | 描述 |
|---------|---------|
| [setGroupListener](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_setGroupListener) | 设置群组相关的事件监听器 |
| [createGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_createGroup_System_String_System_String_System_String_System_String_System_String_System_String_com_tencent_imsdk_unity_CreateGroupMemberInfoEntity___) | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员 |
| [joinGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_joinGroup_System_String_System_String_) | 加入群组 |
| [quitGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_quitGroup_System_String_) | 退出群组 |
| [dismissGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_dismissGroup_System_String_) | 解散群组（仅群主和管理员可以解散） |
| [getJoinedGroupList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_getJoinedGroupList) | 获取已经加入的群列表（不包括已加入的直播群） |
| [getGroupsInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_getGroupsInfo_System_String___) | 拉取群资料 |
| [setGroupInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_setGroupInfo_System_String_System_String_System_String_System_String_System_String_System_String_System_Boolean_com_tencent_imsdk_unity_GroupAddOptType_) | 修改群资料 |
| [getGroupMemberList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_getGroupMemberList_System_String_com_tencent_imsdk_unity_GroupMemberFilterType_System_Int32_) | 获取群成员列表 |
| [getGroupMembersInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_getGroupMembersInfo_System_String_System_String___) | 获取指定的群成员资料 |
| [setGroupMemberInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_setGroupMemberInfo_System_String_System_String_System_String_) | 修改指定的群成员资料 |
| [muteGroupMember](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_muteGroupMember_System_String_System_String_System_Int32_) | 禁言 |
| [kickGroupMember](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_kickGroupMember_System_String_System_String___System_String_) | 踢人 |
| [setGroupMemberRole](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_setGroupMemberRole_System_String_System_String_com_tencent_imsdk_unity_GroupMemberRoleType_) | 切换群成员的角色 |
| [transferGroupOwner](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_transferGroupOwner_System_String_System_String_) | 转让群主 |
| [inviteUserToGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_inviteUserToGroup_System_String_System_String___) | 邀请他人入群 |
| [getGroupApplicationList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_getGroupApplicationList) | 获取加群的申请列表 |
| [acceptGroupApplication](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_acceptGroupApplication_System_String_System_String_System_String_) | 同意某一条加群申请 |
| [refuseGroupApplication](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_refuseGroupApplication_System_String_System_String_System_String_) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMGroupManager.html#com_tencent_imsdk_unity_V2TIMGroupManager_setGroupApplicationRead) | 标记申请列表为已读 |

## 会话列表相关接口

会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API | 描述 |
|---------|---------|
| [setConversationListener](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_setConversationListener) | 设置会话监听器 |
| [getConversationList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMConversationManager.html#com_tencent_imsdk_unity_V2TIMConversationManager_getConversationList_System_Int32_System_Int32_) | 获取会话列表 |
| [deleteConversation](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMConversationManager.html#com_tencent_imsdk_unity_V2TIMConversationManager_deleteConversation_System_String_) | 删除会话 |
| [setConversationDraft](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMConversationManager.html#com_tencent_imsdk_unity_V2TIMConversationManager_setConversationDraft_System_String_System_String_) | 设置会话草稿 |

## 用户资料相关接口

包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API | 描述 |
|---------|---------|
| [getUsersInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_getUsersInfo_System_String___) | 获取用户资料 |
| [setSelfInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_setSelfInfo_System_String_System_String_System_String_com_tencent_imsdk_unity_Gender_com_tencent_imsdk_unity_FriendAllowType_Dictionary_System_String_System_String__) | 修改个人资料 |
| [addToBlackList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_addToBlackList_System_String___) | 屏蔽某人的消息（添加该用户到黑名单中） |
| [deleteFromBlackList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_deleteFromBlackList_System_String___) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_getBlackList) | 获取黑名单列表 |
[setOfflinePushConfig](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_offline_push_manager/V2TIMOfflinePushManager/setOfflinePushConfig.html) | 设置离线推送配置信息 |

## 好友管理相关接口

腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [**控制台**](https://console.cloud.tencent.com/im) >**功能配置**>**登录与消息**>**好友关系检查**中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API | 描述 |
|---------|---------|
| [setFriendListener](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMManager.html#com_tencent_imsdk_unity_V2TIMManager_setFriendListener) | 设置关系链的监听器，用于接收好友列表和黑名单的变更事件 |
| [getFriendsList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_getFriendList) | 获取好友列表 |
| [getFriendsInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_getFriendsInfo_System_String___) | 获取指定好友资料 |
| [setFriendInfo](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_setFriendInfo_System_String_System_String_Dictionary_System_String_System_String__) | 设置指定好友资料 |
| [addFriend](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_addFriend_System_String_com_tencent_imsdk_unity_FriendType_System_String_System_String_System_String_) | 添加好友 |
| [deleteFromFriendList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_deleteFromFriendList_System_String___com_tencent_imsdk_unity_FriendType_) | 删除好友 |
| [checkFriend](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_checkFriend_System_String_) | 检查指定用户的好友关系 |
| [getFriendApplicationList](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_getFriendApplicationList) | 获取好友申请列表 |
| [acceptFriendApplication](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_acceptFriendApplication_System_String_com_tencent_imsdk_unity_FriendAcceptType_) | 同意好友申请 |
| [refuseFriendApplication](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_refuseFriendApplication_System_String_) | 拒绝好友申请 |
| [deleteFriendApplication](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_deleteFriendApplication_System_String_) | 删除好友申请 |
| [setFriendApplicationRead](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_setFriendApplicationRead) | 设置好友申请已读 |
| [createFriendGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_createFriendGroup_System_String_System_String___) | 新建好友分组 |
| [getFriendGroups](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_getFriendGroups_System_String___) | 获取分组信息 |
| [deleteFriendGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_deleteFriendGroup_System_String___) | 删除好友分组 |
| [renameFriendGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_renameFriendGroup_System_String_System_String_) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_addFriendsToFriendGroup_System_String_System_String___) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](https://comm.qq.com/unity-im-sdk-document/v1.6.0/api/com.tencent.imsdk.unity.V2TIMFriendshipManager.html#com_tencent_imsdk_unity_V2TIMFriendshipManager_deleteFriendsFromFriendGroup_System_String_System_String___) | 从好友分组中删除好友 |
