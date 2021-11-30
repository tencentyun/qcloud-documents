<dx-alert infotype="notice" title="温馨提示">
即时通信 IM 为您准备了 Flutter 的 API 调用示例，您可以访问 [GitHub](https://github.com/tencentyun/imApiFlutterExample) 获取源码。扫描下方二维码即可体验 API 调用示例 Demo：
![](https://main.qcloudimg.com/raw/4658a0d24c33f6ec42b07bc8e36234d9.png)
</dx-alert infotype="notice" title="温馨提示">

## 初始化登录接口
初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API | 描述 |
|---------|---------|
| [initSDK](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/initSDK.html) | 初始化 SDK |
| [unInitSDK](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/unInitSDK.html) | 反初始化 SDK |
| [login](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/login.html) | 登录 |
| [logout](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/logout.html) | 登出 |
| [getLoginStatus](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/getLoginStatus.html) | 获取登录状态 |
| [getLoginUser](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/getLoginUser.html) | 获取当前登录用户的 UserID |

## 简单消息收发接口
如果您只需要使用文本和信令（即一段自定义buffer）消息，只需要使用这套简单消息收发接口即可。

| API | 描述 |
|---------|---------|
| [addSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/addSimpleMsgListener.html) | 设置基本消息（文本消息和自定义消息）的事件监听器， 请不要同  [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/addAdvancedMsgListener.html)  混用 |
| [removeSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/removeSimpleMsgListener.html) | 移除基本消息（文本消息和自定义消息）的事件监听器 |
| [sendC2CTextMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/sendC2CTextMessage.html) | 发送单聊（C2C）普通文本消息 |
| [sendC2CCustomMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/sendC2CCustomMessage.html) | 发送单聊（C2C）自定义（信令）消息 |
| [sendGroupTextMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/sendGroupTextMessage.html) | 发送群聊普通文本消息 |
| [sendGroupCustomMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/sendGroupCustomMessage.html) | 发送群聊自定义（信令）消息 |

## 信令接口
| API | 描述 |
|---------|---------|
| [addSignalingListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/addSignalingListener.html) | 添加信令监听 |
| [removeSignalingListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/removeSignalingListener.html) | 移除信令监听 |
| [invite](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/invite.html) | 邀请某个人 |
| [inviteInGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/inviteInGroup.html) | 邀请群内的某些人 |
| [cancel](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/cancel.html) | 邀请方取消邀请 |
| [accept](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/accept.html) | 接收方接受邀请 |
| [reject](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/reject.html) | 接收方拒绝邀请 |

## 高级消息收发接口
如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（简单消息接口和高级消息接口请不要混用）。

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/addAdvancedMsgListener.html) | 设置高级消息的事件监听器， 请不要同 [addSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/addSimpleMsgListener.html) 混用 |
| [removeAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/removeAdvancedMsgListener.html) | 移除高级消息的事件监听器 |
| [sendCustomMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendCustomMessage.html) | 发送自定义消息 |
| [sendImageMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendImageMessage.html) | 发送图片消息 |
| [sendSoundMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendSoundMessage.html) | 发送语音消息 |
| [sendVideoMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendVideoMessage.html) | 发送视频消息 |
| [sendFileMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendFileMessage.html) | 发送文件消息 |
| [sendLocationMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendLocationMessage.html) | 发送地理位置消息 |
| [getC2CHistoryMessageList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getC2CHistoryMessageList.html) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getGroupHistoryMessageList.html) | 获取群组历史消息 |
| [markC2CMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markC2CMessageAsRead.html) | 设置单聊（C2C）消息已读 |
| [markGroupMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markGroupMessageAsRead.html) | 设置群组消息已读 |
| [deleteMessageFromLocalStorage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/deleteMessageFromLocalStorage.html) | 删除本地消息 |
| [insertGroupMessageToLocalStorage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/insertGroupMessageToLocalStorage.html) | 向群组消息列表中添加一条消息 |


## 群组相关接口
腾讯云 IM SDK 支持四种预设的群组类型，每种类型都有其适用场景：
- 工作群（Work）	：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群，同旧版本中的 Private，同旧版本中的 Private。
- 公开群（Public）	：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息，同旧版本中的 ChatRoom，同旧版本中的 ChatRoom。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API | 描述 |
|---------|---------|
| [setGroupListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/setGroupListener.html) | 设置群组相关的事件监听器 |
| [createGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/createGroup.html) | 创建群组（简单版本） |
| [createGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/createGroup.html) | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员 |
| [joinGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/joinGroup.html) | 加入群组 |
| [quitGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/quitGroup.html) | 退出群组 |
| [dismissGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/dismissGroup.html) | 解散群组（仅群主和管理员可以解散） |
| [getJoinedGroupList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getJoinedGroupList.html) | 获取已经加入的群列表（不包括已加入的直播群） |
| [getGroupsInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupsInfo.html) | 拉取群资料 |
| [setGroupInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupInfo.html) | 修改群资料 |
| [setReceiveMessageOpt](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setReceiveMessageOpt.html) | 设置群消息的接收选项 |
| [getGroupMemberList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) | 获取群成员列表 |
| [getGroupMembersInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMembersInfo.html) | 获取指定的群成员资料 |
| [setGroupMemberInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupMemberInfo.html) | 修改指定的群成员资料 |
| [muteGroupMember](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/muteGroupMember.html) | 禁言 |
| [kickGroupMember](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/kickGroupMember.html) | 踢人 |
| [setGroupMemberRole](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupMemberRole.html) | 切换群成员的角色 |
| [transferGroupOwner](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/transferGroupOwner.html) | 转让群主 |
| [inviteUserToGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/inviteUserToGroup.html) | 邀请他人入群 |
| [getGroupApplicationList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupApplicationList.html) | 获取加群的申请列表 |
| [acceptGroupApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/acceptGroupApplication.html) | 同意某一条加群申请 |
| [refuseGroupApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/refuseGroupApplication.html) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupApplicationRead.html) | 标记申请列表为已读 |

## 会话列表相关接口
会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API | 描述 |
|---------|---------|
| [setConversationListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/setConversationListener.html) | 设置会话监听器 |
| [getConversationList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/getConversationList.html) | 获取会话列表 |
| [deleteConversation](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/deleteConversation.html) | 删除会话 |
| [setConversationDraft](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/setConversationDraft.html) | 设置会话草稿 |

## 用户资料相关接口
包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API | 描述 |
|---------|---------|
| [getUsersInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/getUsersInfo.html) | 获取用户资料 |
| [setSelfInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/setSelfInfo.html) | 修改个人资料 |
| [addToBlackList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addToBlackList.html) | 屏蔽某人的消息（添加该用户到黑名单中） |
| [deleteFromBlackList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFromBlackList.html) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getBlackList.html) | 获取黑名单列表 |

## 离线推送相关接口
如果想要在 App 切后台时依然能够实时收到 IM 消息，可以使用离线推送服务。由于大陆境内尚没有统一的推送服务，Android 的离线推送需要针对不同厂商的手机进行 [逐一适配](https://cloud.tencent.com/document/product/269/44516)。

| API | 描述 |
|---------|---------|
| [setOfflinePushConfig](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_offline_push_manager/V2TIMOfflinePushManager/setOfflinePushConfig.html) | 设置离线推送配置信息 |

## 好友管理相关接口
腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [**控制台**](https://console.cloud.tencent.com/im) >**功能配置**>**登录与消息**>**好友关系检查**中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API | 描述 |
|---------|---------|
| [setFriendListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/setFriendListener.html) | 设置关系链的监听器，用于接收好友列表和黑名单的变更事件 |
| [getFriendList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendList.html) | 获取好友列表 |
| [getFriendsInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendsInfo.html) | 获取指定好友资料 |
| [setFriendInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/setFriendInfo.html) | 设置指定好友资料 |
| [addFriend](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriend.html) | 添加好友 |
| [deleteFromFriendList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFromFriendList.html) | 删除好友 |
| [checkFriend](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/checkFriend.html) | 检查指定用户的好友关系 |
| [getFriendApplicationList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendApplicationList.html) | 获取好友申请列表 |
| [acceptFriendApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/acceptFriendApplication.html) | 同意好友申请 |
| [refuseFriendApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/refuseFriendApplication.html) | 拒绝好友申请 |
| [deleteFriendApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFriendApplication.html) | 删除好友申请 |
| [setFriendApplicationRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/setFriendApplicationRead.html) | 设置好友申请已读 |
| [createFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/createFriendGroup.html) | 新建好友分组 |
| [getFriendGroups](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendGroups.html) | 获取分组信息 |
| [deleteFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFriendGroup.html) | 删除好友分组 |
| [renameFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/renameFriendGroup.html) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriendsToFriendGroup.html) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFriendsFromFriendGroup.html) | 从好友分组中删除好友 |
