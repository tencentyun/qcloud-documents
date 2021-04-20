>!**新老版本 API 请勿混合使用**。

## 初始化登录接口
初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API | 描述 |
|---------|---------|
| [initSDK](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a534a3f98ea1447984b5f0932fecfe194) | 初始化 |
| [unInitSDK](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a286e5358ec4cd0a8f9c66f4d2d7d4544) | 反初始化 |
| [login](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a3237ea515b8a78e94a6579447ba282ee) | 登录 |
| [logout](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#ab4233cb134d5c6125d0a2d2d83ec1afa) | 退出登录 |
| [getLoginStatus](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#acfd2f6366780badf80ebf66d95550f89) | 获取登录状态 |
| [getLoginUser](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a78ca7f39bca860e46620f8f766508fb0) | 获取当前登录用户 UserID |

## 简单消息收发接口
如果您只需要使用文本和信令（即一段自定义buffer）消息，只需要使用这套简单消息收发接口即可。

| API | 描述 |
|---------|---------|
| [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a149cdf7924aa13746692d18d605def88) | 设置基本消息（文本消息和自定义消息）的事件监听器，<br> 请不要同 [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#acf794752cc6bfa786aea5cd7fabadfab) 混用。 |
| [removeSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#afa3040f676105f3fb78d4835ee3c898b) | 移除基本消息（文本消息和自定义消息）的事件监听器 |
| [sendC2CTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a8f4eb13fbf039c0216f14f178d9f9f36) | 发送单聊（C2C）普通文本消息 |
| [sendC2CCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a20c6ea174904a99fafebb5c1b3475b39) | 发送单聊（C2C）自定义（信令）消息 |
| [sendGroupTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a74fc1a30a7c1a292e625c5b2cf1e91f0) | 发送群聊普通文本消息 |
| [sendGroupCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#af8b149e054d532a8fb5ca12a7160c90f) | 发送群聊自定义（信令）消息 |

## 信令接口
| API | 描述 |
|---------|---------|
| [addSignalingListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#a3a7fde0d4d5a342bd93299deaf98e1d1) | 添加信令监听。 |
| [removeSignalingListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#ae730297ec335735eee3c2f3c464bde33) | 移除信令监听 |
| [invite](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#a0d75713295f5f19c7d303a0eaeeaaacb) | 邀请某个人。 |
| [inviteInGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#ae7efa9137309a48c93fcd84a6d997506) | 邀请群内的某些人 |
| [cancel](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#a09bc478d84e053d94004c7ec1bbddf58) | 邀请方取消邀请。 |
| [accept](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#a0f486191d6b1755a12de6e2fc42afc14) | 接收方接收邀请 |
| [reject](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#aa945a73b34c98e5512ecdd77f2628b53) | 接收方拒绝邀请。 |
| [getSignalingInfo](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#a0b149836793b8f2d54889b1c3ae40362) | 获取信令信息。 |
| [addInvitedSignaling](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Signaling_08.html#a4332550c567f9f7e6bed5716fd9a1133) | 添加邀请信令（可以用于群离线推送消息触发的邀请信令）。 |

## 高级消息收发接口
如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（简单消息接口和高级消息接口请不要混用）。

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#acf794752cc6bfa786aea5cd7fabadfab) | 设置高级消息的事件监听器，<br> 请不要同 [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a149cdf7924aa13746692d18d605def88) 混用。 |
| [removeAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a28aeebff4a791c9bb8f91a4f61e020e6) | 移除高级消息监听器 |
| [createTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a609f4d4c374d9df3abf9974ff8112fc3) | 创建文本消息 |
| [createTextAtMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#ad33b6f7cb849054333b18eeb1e9c187d) | 创建 @ 文本消息 |
| [createCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a7a38c42f63a4e0c9e89f6c56dd0da316) | 创建自定义消息 |
| [createImageMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a23033a764f0d95ce83c52f3cdeea4137) | 创建图片消息 |
| [createSoundMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a254e943133e35b15088769c2159b0d4b) | 创建语音消息 |
| [createVideoMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a959a66944acc6f712710990880259a0b) | 创建视频消息 |
| [createFileMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#afbc32249f988afdac127227d9ae000a1) | 创建文件消息 |
| [createLocationMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a93b0a2918926e59f56f8fc65dabb8bfd) | 创建地理位置消息 |
| [createFaceMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a5c1199090729348379354eb3402c6d9c) | 创建表情消息 |
| [createMergerMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a0f56dde34bd350dd6e829e5bff067722) | 创建合并转发消息 |
| [createForwardMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a05d088b7d9883e18af41355cdd3f4562) | 创建单条转发消息 |
| [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) | 发送消息，消息对象可以由 createXXXMessage 接口创建得来。 |
| [setC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#ace29641a1c691bc44705b9bc8b08be37) | 设置单聊消息免打扰 |
| [getC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a63d51af9d34e0cd8011da374b7e7a786) | 获取单聊消息免打扰状态 |
| [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a40f3e2ada605b73a39b05a3d3144636b) | 设置群聊消息免打扰状态 |
| [getC2CHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a63b5809dea41a83cfff3c63ede7a152b) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#acc79b07f0ac1b4b29b72878850ce4ad1) | 获取群组历史消息 |
| [getHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#ac1623571db7e6f52484532e2f1630132) | 获取历史消息高级接口 |
| [revokeMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a972ac3fb7744458eb0d6abd96ce35126) |  撤回消息，消息对象可以由 createXXXMessage 接口创建得来。 |
| [markC2CMessageAsRead](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#ad7d239caa69ec7da45f52d6bb02ee19c) | 设置单聊（C2C）消息已读 |
| [markGroupMessageAsRead](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a40afaf1f06edd10c90d8d67fa98c2b14) | 设置群组消息已读 |
| [deleteMessageFromLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a989a11c62ba2001a6a8360d6421d9dd3) | 删除本地消息 |
| [insertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a941598ae3367267ce6bf8ec3d8dcb2eb) | 向群组消息列表中添加一条消息 |
| [insertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a220423e265e3916e530814372799cf4f) | 向单聊消息列表中添加一条消息 |
| [findMessages](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#abacfae1406f7d82241ec4e4a8072fa3e) | 根据 msgID 查找本地消息 |

## 群组相关接口
腾讯云 IM SDK 支持四种预设的群组类型，每种类型都有其适用场景：
- 工作群（Work） ：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群。
- 公开群（Public）   ：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API | 描述 |
|---------|---------|
| [setGroupListener](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a74de68e55d787fd1d4ec83b99cd1fcab) | 设置群组监听器 |
| [createGroup](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a4bada5d6a06fac04a1424ae2c597e389) | 创建群组（简单版本） |
| [createGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a10dc812487a4e9071d65a49df277f183) | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员 |
| [joinGroup](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a9979ed856657724d317791c723bacef5) | 加入群组 |
| [quitGroup](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#abada02babd5dc4c59f485c6aa1678dcb) | 退出群组 |
| [dismissGroup](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#af6605dd9624849843938573ef05b5463) | 解散群组（仅群主和管理员可以解散） |
| [getJoinedGroupList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#ae12e170ad585eaa8fb9f080bdc3bf8b8) | 获取已经加入的群列表（不包括已加入的直播群） |
| [getGroupsInfo](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#aeeffef844fd0948dda227620f0fac895) | 拉取群资料 |
| [setGroupInfo](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a13b25d1f491e18ab0ba953ffc2ca9e82) | 修改群资料 |
| [ initGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a6d34074aa8ce1e8a6dc41ee53ff5963a) | 初始化群属性 |
| [ setGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a60bbd75b35c42e823c9538b4be44e3ea) | 设置群属性 |
| [ deleteGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a60bbd75b35c42e823c9538b4be44e3ea) | 删除群属性 |
| [ getGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#af3e1eb1c23996f2beab55670be96fb2d) | 获取群属性 |
| [getGroupOnlineMemberCount](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#ac6236048b0184ee5d35c6071a92b6d1c) | 获取群在线人数 |
| [getGroupMemberList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a1ba27ad3077804addcfd92c3a45dd092) | 获取群成员列表 |
| [getGroupMembersInfo](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#ab74754f326c661e94b4511a3b6d91f32) | 获取指定的群成员资料 |
| [setGroupMemberInfo](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a32caf9bf614778c291194fb5cf3ca3b0) | 修改指定的群成员资料 |
| [muteGroupMember](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a0ee1017ecded651208261ac7d1013ad0) | 禁言 |
| [inviteUserToGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#af9d9a04bf3fe5a38346af842f7335f39) | 邀请他人入群 |
| [kickGroupMember](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a21d4d4d5b5291d8eda74b3359d857714) | 踢人 |
| [setGroupMemberRole](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a548aef46b1ef435864678d56f0c0ce54) | 切换群成员的角色 |
| [transferGroupOwner](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a99e8c3488c6bbb553fc662804f7e2f02) | 转让群主 |
| [getGroupApplicationList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#ae761e7a0c5fd2ad55219bb732edae9cb) | 获取加群的申请列表 |
| [acceptGroupApplication](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a72a9fc4dbb99d354121b944e98382e68) | 同意某一条加群申请 |
| [refuseGroupApplication](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#ad632874883b7b73e3fba773044bd8c1a) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Group_08.html#a141b2b0b02f32039fc3e777599ba2360) | 标记申请列表为已读 |

## 会话列表相关接口
会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API | 描述 |
|---------|---------|
| [setConversationListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#a95bac7330779a8a970fc7689e436257f) | 设置会话监听器 |
| [getConversationList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#afbf2764146025df3c2202058026fda77) | 获取会话列表 |
| [getConversation](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#ac279fbef674e0de22c038951a9efc779) | 获取指定单个会话 |
| [getConversationList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#ac279fbef674e0de22c038951a9efc779) | 获取指定多个会话 |
| [deleteConversation](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#a42238db95428faae2da25a093569fda0) | 删除会话 |
| [setConversationDraft](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#ade2830b5c35df27a4b8fea44408a07a0) | 设置会话草稿 |
| [pinConversation](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#adc50026943585a0aa37ac8856b6b43bb) | 置顶会话 |
| [getTotalUnreadMessageCount](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#adc50026943585a0aa37ac8856b6b43bb) | 获取会话总未读数 |

## 用户资料相关接口
包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API | 描述 |
|---------|---------|
| [getUsersInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a0071a5be9f333698f05fd80aff203560) | 获取用户资料 |
| [setSelfInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMManager.html#a2ff0139742c4a0bf6dce1ef7423f3bee) | 修改个人资料 |
| [addToBlackList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#ad1de7b4712309ce4164e4db6574486f0) | 屏蔽某人的消息（添加该用户到黑名单中） |
| [deleteFromBlackList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#afe61664e0afee949f99ec63a288316e2) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#aa0e6338aefd556a23507c2798af6e717) | 获取黑名单列表 |

## 离线推送相关接口
如果想要在 App 切后台时依然能够实时收到 IM 消息，可以使用离线推送服务，详细配置请参考 [离线推送](https://cloud.tencent.com/document/product/269/9154)。

| API | 描述 |
|---------|---------|
| [setAPNSListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a62e1694cf9e1d65b76f90064cbcbb683) | 设置 APNs 监听 |
| [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a6aecbdc0edaa311c3e4e0ed3e71495b1) | 设置离线推送配置信息 |

## 好友管理相关接口
腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [【控制台】](https://console.cloud.tencent.com/im) >【功能配置】>【登录与消息】>【好友关系检查】中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API | 描述 |
|---------|---------|
| [setFriendListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#acd403f586f3df84f56b1b757efb2d443) | 设置关系链与好友资料监听器 |
| [getFriendList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a8d03aec2e3efd16b7942944c6cb30d0e) | 获取好友列表 |
| [getFriendsInfo](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a930bb2a8cd664a4037797970ce9fc0d8) | 获取指定好友资料 |
| [setFriendInfo](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a97409aaccf135d60344f002aca06e63e) | 设置指定好友资料 |
| [addFriend](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#ae46b728a77d71e302e10b71ee6b0241e) | 添加好友 |
| [deleteFromFriendList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a2786c60824ea6ec117429ef2b59630a1) | 删除好友 |
| [checkFriend](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a2add6bf5b1e2bc8c20bbc2a3f7e0b2f2) | 检查指定用户的好友关系 |
| [getFriendApplicationList](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a46147f28e4c974aa29c0e48a1bdc483f) | 获取好友申请列表 |
| [acceptFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a2546222b4994a5be9f67dfa8eb504e6b) | 同意好友申请 |
| [refuseFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#acb564676b24c76609acf645c4ad999ad) | 拒绝好友申请 |
| [deleteFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a37d87181021d023774a40a79e89e010b) | 删除好友申请 |
| [setFriendApplicationRead](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#abcdd9faaff90b13d077d10a50373d9df) | 设置好友申请已读 |
| [createFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#acd85704b4a6ad4293d8bbcdb73385f4c) | 新建好友分组 |
| [getFriendGroups](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a44c12380968b1d51c5ea5f90fa627a56) | 获取分组信息 |
| [deleteFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a73a1219065649398d4ba1001f9bd1c9b) | 删除好友分组 |
| [renameFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a2677f9d9febe8f28f16f3972f7c45638) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a24b2297a1d9c2c3fa816839b3108ef72) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Friendship_08.html#a65380db025573ac7c6d20f66a8b40ee2) | 从好友分组中删除好友 |


