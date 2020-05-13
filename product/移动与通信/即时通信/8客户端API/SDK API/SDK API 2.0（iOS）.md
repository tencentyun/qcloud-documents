## V2TIMManager
### 初始化接口函数

| API | 描述 |
|---------|---------|
| [initSDK](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a7430e88cf0b7173f3803d54802cb13ac) | 初始化 |
| [unInitSDK](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a286e5358ec4cd0a8f9c66f4d2d7d4544) | 反初始化 |

### 登录登出接口函数

| API | 描述 |
|---------|---------|
| [login](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a38c42943046acdaf615915c9422af07c) | 登录 |
| [logout](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a20b495d7f7a231ea33507ca4a79f811f) | 退出登录 |
| [getLoginStatus](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#acfd2f6366780badf80ebf66d95550f89) | 获取登录状态 |
| [getLoginUser](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a78ca7f39bca860e46620f8f766508fb0) | 获取当前登录用户 UserID |

### 消息收发接口函数

| API | 描述 |
|---------|---------|
| [addSimpleMsgListener](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a428fe7bf82be1592141d77dfa756ec68) | 设置基本消息（文本消息和自定义消息）的事件监听器 |
| [removeSimpleMsgListener](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a8f6f9900006bf7ad5bd9bdb8ba0914eb) | 移除基本消息的事件监听器 |
| [sendC2CTextMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a50d63810093eccc0491d058d0b883618) | 发送单聊普通文本消息 |
| [sendC2CCustomMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a5fc3b87e9782e679c08926d07e486b90) | 发送单聊自定义（信令）消息 |
| [sendGroupTextMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a07788874071937fac6c7093185b145f7) | 发送群聊普通文本消息 |
| [sendGroupCustomMessage](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a537560a58d49aad36406f6d9db6ded65) | 发送群聊自定义（信令）消息 |

### 群接口函数

| API | 描述 |
|---------|---------|
| [setGroupListener](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a74de68e55d787fd1d4ec83b99cd1fcab) | 设置群组监听器 |
| [createGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a3bbcf819c1ec70e520b7f9a42cfbb989) | 创建群组 |
| [joinGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a4762156b7a98489eb4715de53028e12a) | 加入群组 |
| [quitGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#ac2a43b3ada447131df0c5f19e8079be5) | 退出群组 |
| [dismissGroup](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a5bd55cb04867985253949d8cc78f860e) | 解散群组 |

### 资料接口函数

| API | 描述 |
|---------|---------|
| [getUsersInfo](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#ac638c1dd6ec1e5204637e4b87129cd38) | 获取用户资料 |
| [setSelfInfo](http://doc.qcloudtrtc.com/im/interfaceV2TIMManager.html#a328a0d2d07e8d34e12effb73937c3437) | 修改个人资料 |


## V2TIMManager+Message.h

### 监听 - 高级（图片、语音、视频等）消息

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a517a6f56909fdad2004b4679b715186a) | 设置高级消息的事件监听器 |
| [removeAdvancedMsgListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a77ec89edbdf500431cbda5ee7aa50920) | 移除高级消息监听器 |

### 创建 - 高级（图片、语音、视频等）消息

| API | 描述 |
|---------|---------|
| [createTextMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a609f4d4c374d9df3abf9974ff8112fc3) | 创建文本消息 |
| [createCustomMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a7a38c42f63a4e0c9e89f6c56dd0da316) | 创建自定义消息 |
| [createImageMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a23033a764f0d95ce83c52f3cdeea4137) | 创建图片消息 |
| [createSoundMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9073007806fa186b8999ce656555032a) | 创建语音消息 |
| [createVideoMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a233a9ee5ef2ea371206005d109757f18) | 创建视频消息 |
| [createFileMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9e487ae9541111038ebed900ab639d4c) | 创建文件消息 |
| [createLocationMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a2a997472dd62d794cfd4e3a42cfab930) | 创建地理位置消息 |
| [createFaceMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#ab7a593be2cca1c8eddd7e73255f3f34a) | 创建表情消息 |

### 发送 - 高级（图片、语音、视频等）消息

| API | 描述 |
|---------|---------|
| [sendMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) | 发送消息 |

### 获取历史消息、撤回、删除、标记已读等高级接口

| API | 描述 |
|---------|---------|
| [getC2CHistoryMessageList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#ad7dfd40e7b765a43c8580c3ed295a7b7) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#addaf00771fe89bf38800ea344dfe0e25) | 获取群组历史消息 |
| [revokeMessage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a2ef856a792923811e9d16ed7a101336a) | 撤回消息 |
| [markC2CMessageAsRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#acb3a67bd2fa131b50c611a48fa78f34d) | 设置单聊（C2C）消息已读 |
| [markGroupMessageAsRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a7fc79e30877b8d77fbdfa24e057376dc) | 设置群组消息已读 |
| [deleteMessageFromLocalStorage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a2bb42528f4d166ac826914094655841c) | 删除本地消息 |
| [insertGroupMessageToLocalStorage](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Message_08.html#a9b312b67e4da19978b55a7b915815dfe) | 向群组消息列表中添加一条消息 |

## `V2TIMManager+Group.h`

### 群相关的高级接口

| API | 描述 |
|---------|---------|
| [createGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a59824434b6096180b94d8152183dcd2c) | 创建自定义群组 |
| [getJoinedGroupList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a11e7d6d778817b85d1d1b897b9d3975c) | 获取当前用户已经加入的群列表 |

### 群资料和高级设置项

| API | 描述 |
|---------|---------|
| [getGroupsInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a9b6733af999cb7dbffd4ad56b5b1c879) | 拉取群资料 |
| [setGroupInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#aa9519a479493e56d7920e40aba796144) | 修改群资料 |
| [setReceiveMessageOpt](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a4974b44d56778b1d5a3df613bee09c87) | 设置群消息接收选项 |

### 群成员管理

| API | 描述 |
|---------|---------|
| [getGroupMemberList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a6961b1c4883fdd2859d71bf4a9ae67d4) | 获取群成员列表 |
| [getGroupMembersInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a1ab284b80811bcc697d689d7b97edf04) | 获取指定的群成员资料 |
| [setGroupMemberInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a40b97ee4b138f93e1b2073d1bdff3756) | 修改指定的群成员资料 |
| [muteGroupMember](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#aa8a0206f75d75400b517f7e0d80fe9ee) | 禁言 |
| [inviteUserToGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a4b76317a9f21069b2d9a754b6239898b) | 邀请他人入群 |
| [kickGroupMember](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a06cd0f8440c164f9157a26d56b0af85b) | 踢人 |
| [setGroupMemberRole](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#af7ce533e514adfab766b1ee726d9ffce) | 切换群成员的角色 |
| [transferGroupOwner](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a58a2ffae60505a43984fe21bf0bc1101) | 转让群主 |

### 加群申请

| API | 描述 |
|---------|---------|
| [getGroupApplicationList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#ae154de92f3c394b09f770e5ebc914c0c) | 获取加群的申请列表 |
| [acceptGroupApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a51bb9b4f965cb3d01546fef348ac75e4) | 同意某一条加群申请 |
| [refuseGroupApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#a46aa78c54986b2c0b7cc0012a3dc94ef) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Group_08.html#ade11e93b96206ef851641c42788132d1) | 标记申请列表为已读 |

## V2TIMConversationManager
### 会话的获取，删除和更新接口函数

| API | 描述 |
|---------|---------|
| [setConversationListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#a95bac7330779a8a970fc7689e436257f) | 设置会话监听器 |
| [getConversationList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#a63ae21facd6d4aa1a41d886a4d9ab5e8) | 获取会话列表 |
| [deleteConversation](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#a8b00b2cfd85e87e24f6f1b25716a7710) | 删除会话 |
| [setConversationDraft](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Conversation_08.html#a462cd163c03cdce230ed3647b414382b) | 设置会话草稿 |

## V2TIMManager+Friendship.h

###  关系链与好友资料监听器

| API | 描述 |
|---------|---------|
| [setFriendListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#acd403f586f3df84f56b1b757efb2d443) | 设置关系链与好友资料监听器 |

### 好友添加、删除、列表获取、资料设置接口函数

| API | 描述 |
|---------|---------|
| [getFriendList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a383261ef075f5ad9c3ea856e0a92599d) | 获取好友列表 |
| [getFriendsInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a0f25ace3c3cd5a07de41179c1373f692) | 获取指定好友资料 |
| [setFriendInfo](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ac258312c000c1af69fcf51dd6898b74b) | 设置指定好友资料 |
| [addFriend](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ac1ea1c7de2bfc2b0a25e5f6b3192e304) | 添加好友 |
| [deleteFromFriendList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#af967134fb177b32d4060fedf3663ace3) | 删除好友 |
| [checkFriend](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ad35446522c481e8fa4260452ec041e15) | 检查指定用户的好友关系 |

### 好友申请、删除接口函数

| API | 描述 |
|---------|---------|
| [getFriendApplicationList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a7a0932dcd91967caa8bb7550880fac1e) | 获取好友申请列表 |
| [acceptFriendApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a51b913927028025e2e450e6e8ce848c0) | 同意好友申请 |
| [refuseFriendApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a406b964a6513219cfe4803f87f0f00f8) | 拒绝好友申请 |
| [deleteFriendApplication](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a363e0622f653694999293c595d552896) | 删除好友申请 |
| [setFriendApplicationRead](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#ad46c70c18b8f69bf272cbf3466477a85) | 设置好友申请已读 |

### 黑名单接口函数

| API | 描述 |
|---------|---------|
| [addToBlackList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a67d998da5085b5004bb6aa8d4322022c) | 添加用户到黑名单 |
| [deleteFromBlackList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#aa7e69a67185eaca658ba429cf6309a5f) | 把用户从黑名单中删除 |
| [getBlackList](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a60735e0967153750823a33c94f1a2c51) | 获取黑名单列表 |

### 好友分组接口函数

| API | 描述 |
|---------|---------|
| [createFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a231a334fa4a064042d65a67f267ec664) | 新建好友分组 |
| [getFriendGroups](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#abd8a88d065615ff73f70768eed7e41dc) | 获取分组信息 |
| [deleteFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a2dc49f2abb1238fc2d47ce6d4f14c1e7) | 删除好友分组 |
| [renameFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a93f6ba132d9706db7c74daff97a2abd0) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a0265241c39600c390406ca1f8f6ff75d) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07Friendship_08.html#a4a14a878816c8d6a20981d1903fcf359) | 从好友分组中删除好友 |

## V2TIMManager+APNS.h

### 设置离线推送配置接口函数

| API | 描述 |
|---------|---------|
| [setAPNSListener](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07APNS_08.html#a62e1694cf9e1d65b76f90064cbcbb683) | 设置 APNs 监听 |
| [setAPNS](http://doc.qcloudtrtc.com/im/categoryV2TIMManager_07APNS_08.html#a73bf19c0c019e5e27ec441bc753daa9e) | 设置 APNs 推送 |

