>!**新老版本 API 请勿混合使用**。

## 初始化登录接口
初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API | 描述 |
|---------|---------|
| [initSDK](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a8035eed3a7c9b3b1c229196ac7bc5da6) | 初始化 |
| [unInitSDK](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a286e5358ec4cd0a8f9c66f4d2d7d4544) | 反初始化 |
| [login](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a38c42943046acdaf615915c9422af07c) | 登录 |
| [logout](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a20b495d7f7a231ea33507ca4a79f811f) | 退出登录 |
| [getLoginStatus](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#acfd2f6366780badf80ebf66d95550f89) | 获取登录状态 |
| [getLoginUser](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a78ca7f39bca860e46620f8f766508fb0) | 获取当前登录用户 UserID |

## 简单消息收发接口
如果您只需要使用文本和信令（即一段自定义buffer）消息，只需要使用这套简单消息收发接口即可。

| API | 描述 |
|---------|---------|
| [addSimpleMsgListener](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a428fe7bf82be1592141d77dfa756ec68) | 设置基本消息（文本消息和自定义消息）的事件监听器，<br> 请不要同 [addAdvancedMsgListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a517a6f56909fdad2004b4679b715186a) 混用。 |
| [removeSimpleMsgListener](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a8f6f9900006bf7ad5bd9bdb8ba0914eb) | 移除基本消息（文本消息和自定义消息）的事件监听器 |
| [sendC2CTextMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a50d63810093eccc0491d058d0b883618) | 发送单聊（C2C）普通文本消息 |
| [sendC2CCustomMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a5fc3b87e9782e679c08926d07e486b90) | 发送单聊（C2C）自定义（信令）消息 |
| [sendGroupTextMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a07788874071937fac6c7093185b145f7) | 发送群聊普通文本消息 |
| [sendGroupCustomMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a537560a58d49aad36406f6d9db6ded65) | 发送群聊自定义（信令）消息 |

## 信令接口
| API | 描述 |
|---------|---------|
| [addSignalingListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#a3a7fde0d4d5a342bd93299deaf98e1d1) | 添加信令监听。 |
| [removeSignalingListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#ae730297ec335735eee3c2f3c464bde33) | 移除信令监听 |
| [invite](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#a0c7b9134995c78f3e2b855acdf65ac12) | 邀请某个人。 |
| [inviteInGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#a1ea8dcc4ee2200bf5913a40efd76bf4e) | 邀请群内的某些人 |
| [cancel](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#acaac35e5db28db783420b5eb39d53e6f) | 邀请方取消邀请。 |
| [accept](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#a1ffb6daba9deed8780f869205daf7771) | 接收方接收邀请 |
| [reject](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#a39e685924aaa4d22daa88f2ec96aa827) | 接收方拒绝邀请。 |
| [getSignalingInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#a0b149836793b8f2d54889b1c3ae40362) | 获取信令信息。 |
| [addInvitedSignaling](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Signaling_08.html#aedfb31fdd3289af36c092b55adeed231) | 添加邀请信令（可以用于群离线推送消息触发的邀请信令）。 |

## 高级消息收发接口
如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（简单消息接口和高级消息接口请不要混用）。

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a517a6f56909fdad2004b4679b715186a) | 设置高级消息的事件监听器，<br> 请不要同 [addSimpleMsgListener](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a428fe7bf82be1592141d77dfa756ec68) 混用。 |
| [removeAdvancedMsgListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a77ec89edbdf500431cbda5ee7aa50920) | 移除高级消息监听器 |
| [createTextMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a609f4d4c374d9df3abf9974ff8112fc3) | 创建文本消息 |
| [createCustomMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a7a38c42f63a4e0c9e89f6c56dd0da316) | 创建自定义消息 |
| [createImageMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a23033a764f0d95ce83c52f3cdeea4137) | 创建图片消息 |
| [createSoundMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9073007806fa186b8999ce656555032a) | 创建语音消息 |
| [createVideoMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a233a9ee5ef2ea371206005d109757f18) | 创建视频消息 |
| [createFileMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9e487ae9541111038ebed900ab639d4c) | 创建文件消息 |
| [createLocationMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a2a997472dd62d794cfd4e3a42cfab930) | 创建地理位置消息 |
| [createFaceMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#ab7a593be2cca1c8eddd7e73255f3f34a) | 创建表情消息 |
| [sendMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) | 发送消息，消息对象可以由 createXXXMessage 接口创建得来。 |
| [revokeMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9e242ba327377fe74b83e8d5572d39a0) |  撤回消息，消息对象可以由 createXXXMessage 接口创建得来。 |
| [getC2CHistoryMessageList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#abca63ad64f69aa4f424cf11849a9b89e) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9e242ba327377fe74b83e8d5572d39a0) | 获取群组历史消息 |
| [markC2CMessageAsRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a2ef856a792923811e9d16ed7a101336a) | 设置单聊（C2C）消息已读 |
| [markGroupMessageAsRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a7fc79e30877b8d77fbdfa24e057376dc) | 设置群组消息已读 |
| [deleteMessageFromLocalStorage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a2bb42528f4d166ac826914094655841c) | 删除本地消息 |
| [insertGroupMessageToLocalStorage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9b312b67e4da19978b55a7b915815dfe) | 向群组消息列表中添加一条消息 |

## 群组相关接口
腾讯云 IM SDK 支持四种预设的群组类型，每种类型都有其适用场景：
- 工作群（Work） ：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群。
- 公开群（Public）   ：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API | 描述 |
|---------|---------|
| [setGroupListener](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a74de68e55d787fd1d4ec83b99cd1fcab) | 设置群组监听器 |
| [createGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a3bbcf819c1ec70e520b7f9a42cfbb989) | 创建群组（简单版本） |
| [createGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a59824434b6096180b94d8152183dcd2c) | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员 |
| [joinGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a4762156b7a98489eb4715de53028e12a) | 加入群组 |
| [quitGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#ac2a43b3ada447131df0c5f19e8079be5) | 退出群组 |
| [dismissGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a5bd55cb04867985253949d8cc78f860e) | 解散群组（仅群主和管理员可以解散） |
| [getJoinedGroupList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a4599e99791c150cc9f3e2492e8b4ce04) | 获取已经加入的群列表（不包括已加入的直播群） |
| [getGroupsInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a9bca7e5318cfed44335566a783a6b568) | 拉取群资料 |
| [setGroupInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#aa9519a479493e56d7920e40aba796144) | 修改群资料 |
| [setReceiveMessageOpt](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a4974b44d56778b1d5a3df613bee09c87) | 设置群消息接收选项 |
| [getGroupMemberList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a148bb44bf0189a4e61a294a495a43dbe) | 获取群成员列表 |
| [getGroupMembersInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a1ab284b80811bcc697d689d7b97edf04) | 获取指定的群成员资料 |
| [setGroupMemberInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a40b97ee4b138f93e1b2073d1bdff3756) | 修改指定的群成员资料 |
| [muteGroupMember](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#aa8a0206f75d75400b517f7e0d80fe9ee) | 禁言 |
| [inviteUserToGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a942d75fdea66e22cdbd8c131cf18e1ea) | 邀请他人入群 |
| [kickGroupMember](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a0581f28fddf2ade890aa62e4318d7a97) | 踢人 |
| [setGroupMemberRole](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#af7ce533e514adfab766b1ee726d9ffce) | 切换群成员的角色 |
| [transferGroupOwner](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a58a2ffae60505a43984fe21bf0bc1101) | 转让群主 |
| [getGroupApplicationList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a29c36ad685159850a30d61a6b9c637e8) | 获取加群的申请列表 |
| [acceptGroupApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a51bb9b4f965cb3d01546fef348ac75e4) | 同意某一条加群申请 |
| [refuseGroupApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a46aa78c54986b2c0b7cc0012a3dc94ef) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#ade11e93b96206ef851641c42788132d1) | 标记申请列表为已读 |

## 会话列表相关接口
会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API | 描述 |
|---------|---------|
| [setConversationListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#a95bac7330779a8a970fc7689e436257f) | 设置会话监听器 |
| [getConversationList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#af94d9d44e90da448a395e6d92b4e512e) | 获取会话列表 |
| [deleteConversation](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#a142f5289632f29a603937f1d770748c6) | 删除会话 |
| [setConversationDraft](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#a462cd163c03cdce230ed3647b414382b) | 设置会话草稿 |


## 用户资料相关接口
包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API | 描述 |
|---------|---------|
| [getUsersInfo](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#ac638c1dd6ec1e5204637e4b87129cd38) | 获取用户资料 |
| [setSelfInfo](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a328a0d2d07e8d34e12effb73937c3437) | 修改个人资料 |
| [addToBlackList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a67d998da5085b5004bb6aa8d4322022c) | 屏蔽某人的消息（添加该用户到黑名单中） |
| [deleteFromBlackList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#aa7e69a67185eaca658ba429cf6309a5f) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a0d854d64c8ae936014a8424d55508fa3) | 获取黑名单列表 |

## 离线推送相关接口
如果想要在 App 切后台时依然能够实时收到 IM 消息，可以使用离线推送服务，详细配置请参考 [离线推送](https://cloud.tencent.com/document/product/269/9154)。

| API | 描述 |
|---------|---------|
| [setAPNSListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07APNS_08.html#a62e1694cf9e1d65b76f90064cbcbb683) | 设置 APNs 监听 |
| [setAPNS](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07APNS_08.html#a73bf19c0c019e5e27ec441bc753daa9e) | 设置离线推送配置信息 |

## 好友管理相关接口
腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [【控制台】](https://console.cloud.tencent.com/im) >【功能配置】>【登录与消息】>【好友关系检查】中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API | 描述 |
|---------|---------|
| [setFriendListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#acd403f586f3df84f56b1b757efb2d443) | 设置关系链与好友资料监听器 |
| [getFriendList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a81131d76924a03ec2b593addd6e4e101) | 获取好友列表 |
| [getFriendsInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a39f6752da11b595e4a5b6dcb0eb6a584) | 获取指定好友资料 |
| [setFriendInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ac258312c000c1af69fcf51dd6898b74b) | 设置指定好友资料 |
| [addFriend](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ac1ea1c7de2bfc2b0a25e5f6b3192e304) | 添加好友 |
| [deleteFromFriendList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#af967134fb177b32d4060fedf3663ace3) | 删除好友 |
| [checkFriend](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ad35446522c481e8fa4260452ec041e15) | 检查指定用户的好友关系 |
| [getFriendApplicationList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#acda7968f1e9adc12261a7e533d709a1c) | 获取好友申请列表 |
| [acceptFriendApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a51b913927028025e2e450e6e8ce848c0) | 同意好友申请 |
| [refuseFriendApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a406b964a6513219cfe4803f87f0f00f8) | 拒绝好友申请 |
| [deleteFriendApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a363e0622f653694999293c595d552896) | 删除好友申请 |
| [setFriendApplicationRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ad46c70c18b8f69bf272cbf3466477a85) | 设置好友申请已读 |
| [createFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a231a334fa4a064042d65a67f267ec664) | 新建好友分组 |
| [getFriendGroups](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a63f3eaae567586077d5a8d27c31e2229) | 获取分组信息 |
| [deleteFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a2dc49f2abb1238fc2d47ce6d4f14c1e7) | 删除好友分组 |
| [renameFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a93f6ba132d9706db7c74daff97a2abd0) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a0265241c39600c390406ca1f8f6ff75d) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a4a14a878816c8d6a20981d1903fcf359) | 从好友分组中删除好友 |


