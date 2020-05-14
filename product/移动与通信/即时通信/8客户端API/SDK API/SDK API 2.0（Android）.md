## V2TIMManager
### 初始化接口函数

| API | 描述 |
|---------|---------|
| [initSDK](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ac905c315726b517ba62421471bbecf56) | 初始化 |
| [unInitSDK](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a05db3ac73a3ad4bbb7e25a89d27ea8f0) | 反初始化 |

### 登录登出接口函数

| API | 描述 |
|---------|---------|
| [login](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a73fc0e14c5f2f5fc06a80081479fb416) | 登录 |
| [logout](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0398924fa1b62a8f5cc9b51673273b48) | 退出登录 |
| [getLoginStatus](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a1836146275265b2a120412f18961db95) | 获取登录状态 |
| [getLoginUser](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ad4b2e5a7df5e786ba369054ac582007f) | 获取当前登录用户 UserID |

### 消息收发接口函数

| API | 描述 |
|---------|---------|
| [addSimpleMsgListener](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd96fd1591e41f031421c0655d8e5d6b) | 设置基本消息（文本消息和自定义消息）的事件监听器 |
| [removeSimpleMsgListener](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a86ac462d87f652960d2600a52009849a) | 移除基本消息的事件监听器 |
| [sendC2CTextMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a59a8ba6e4a973b4c40a09ae7dfdc6981) | 发送单聊普通文本消息 |
| [sendC2CCustomMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af3e08b936df77210c6cdd0ce5c7fa87f) | 发送单聊自定义（信令）消息 |
| [sendGroupTextMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a56359fd1ce0a96f289dcd4bef522fb52) | 发送群聊普通文本消息 |
| [sendGroupCustomMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afbce8ff97be0a3a42c7dc826d316f2c2) | 发送群聊自定义（信令）消息 |

### 群接口函数

| API | 描述 |
|---------|---------|
| [setGroupListener](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a092fc428f35eb18c41a80b3655948d40) | 设置群组监听器 |
| [createGroup](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af836e4912f668dddf6cc679233cfb0bb) | 创建群组 |
| [joinGroup](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ad64a09bea508672d6d5a402b3455b564) | 加入群组 |
| [quitGroup](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a6d140dbeb44906de9cb69f69c2ce5919) | 退出群组 |
| [dismissGroup](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd0221c0c842a6dcfa0acc657e50caeb) | 解散群组 |

### 资料接口函数

| API | 描述 |
|---------|---------|
| [getUsersInfo](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a7ca8c0f71a9875021fc35dfcaff68d1e) | 获取用户资料 |
| [setSelfInfo](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af004ab2f1d1458de354883f1995b678a) | 修改个人资料 |

### 高级功能入口

| API | 描述 |
|---------|---------|
| [getMessageManager](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ac6f2ad3f6a199e29639225f1eee6125d) | 高级消息功能入口 |
| [getGroupManager](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a5b3d1cb8869c299a59f72d1a40be0bfc) | 高级群组功能入口 |
| [getConversationManager](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ae42ba51aca2b207a8c6ef854f037a295) | 会话功能入口 |
| [getFriendshipManager](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0f9aaa1471f544b86506644ddd6613a1) | 关系链与好友资料功能入口 |
| [getOfflinePushManager](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ac4cf560770a6db7dfc1836fa48f76cc9) | 离线推送功能入口 |

## V2TIMMessageManager

### 监听 - 高级（图片、语音、视频等）消息

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aaccdec10b9fbee5e43eaf908e359c823) | 设置高级消息的事件监听器 |
| [removeAdvancedMsgListener](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a44e1e9126bf5b30234330fe19259cd93) | 移除高级消息监听器 |

### 创建 - 高级（图片、语音、视频等）消息

| API | 描述 |
|---------|---------|
| [createTextMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a3ea254cd12aa0bcfd004f26f759b76a0) | 创建文本消息 |
| [createCustomMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5c2495d4b7ecd66e5636aeb865c17efd) | 创建自定义消息 |
| [createImageMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#adef5bc7a67b9a69f70f6417fd810d4b1) | 创建图片消息 |
| [createSoundMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7e661ce2b4eba1535bd04f3b6539b9dc) | 创建语音消息 |
| [createVideoMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a26e375dbdd8c4e068ad5c147396f74bf) | 创建视频消息 |
| [createFileMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a39e4b6609321fd188a2e156a00bb3135) | 创建文件消息 |
| [createLocationMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a67cebe27192392080fc80a86c80a4321) | 创建地理位置消息 |
| [createFaceMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7ad0f3b7eff3978c12d8c912ca164a5d) | 创建表情消息 |

### 发送 - 高级（图片、语音、视频等）消息

| API | 描述 |
|---------|---------|
| [sendMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a86bb09717a09feeae10dea18e3a138d8) | 发送消息 |

### 获取历史消息、撤回、删除、标记已读等高级接口

| API | 描述 |
|---------|---------|
| [getC2CHistoryMessageList](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#afedccbe0e5229ae15e0e07b722ea39df) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a671e8737fcea0c05dc661c753e5b3597) | 获取群组历史消息 |
| [revokeMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ad0dfce6be749165cd90a9ff67a1308b1) | 撤回消息 |
| [markC2CMessageAsRead](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7c09d0ba4a8018f5f9eec4760c4c7b9b) | 设置单聊（C2C）消息已读 |
| [markGroupMessageAsRead](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ac0a65f18d361abde8a0ac16132027e69) | 设置群组消息已读 |
| [deleteMessageFromLocalStorage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa31e3b48fb666b970120fc0bc6343534) | 删除本地消息 |
| [insertGroupMessageToLocalStorage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a04a3f6c250f9d6c0053fd71be74f047f) | 向群组消息列表中添加一条消息 |

## `V2TIMGroupManager`

### 群相关的高级接口

| API | 描述 |
|---------|---------|
| [createGroup](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a121d53137a38d0fc0bc8a8e0a9c55647) | 创建自定义群组 |
| [getJoinedGroupList](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a05bfd8f7df6bfba718abc96fdad49791) | 获取当前用户已经加入的群列表 |

### 群资料和高级设置项

| API | 描述 |
|---------|---------|
| [getGroupsInfo](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ada614335043d548c11f121500e279154) | 拉取群资料 |
| [setGroupInfo](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad87ce42b4dc4d97334fe857e4caa36c4) | 修改群资料 |
| [setReceiveMessageOpt](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a6bf8f3eafb5ffcb1d13bd69231de8bd4) | 设置群消息接收选项 |

### 群成员管理

| API | 描述 |
|---------|---------|
| [getGroupMemberList](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#aaec81358caf818ba6d5424687016d0fe) | 获取群成员列表 |
| [getGroupMembersInfo](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#adb08e1c4fa9aff407c7b2678757f66d5) | 获取指定的群成员资料 |
| [setGroupMemberInfo](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a6f1cf8ede41348b4cd7b63b8e4caa77b) | 修改指定的群成员资料 |
| [muteGroupMember](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a450230c4d129611e1b0519827ec0f8b5) | 禁言 |
| [inviteUserToGroup](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a20f3a8726aff3969607b2ea6d1d913e2) | 邀请他人入群 |
| [kickGroupMember](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a44b5ebe7ad55b9c14a45339920afe25f) | 踢人 |
| [setGroupMemberRole](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a34ebf60528d02626834f022b4ebabfa8) | 切换群成员的角色 |
| [transferGroupOwner](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ac16d66c8e293c2ee95c7b673e5ad80c4) | 转让群主 |

### 加群申请

| API | 描述 |
|---------|---------|
| [getGroupApplicationList](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#acba91018aa4c73d2ca1388749282b6fe) | 获取加群的申请列表 |
| [acceptGroupApplication](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad743008d30c909ef0be0f8aa91102e07) | 同意某一条加群申请 |
| [refuseGroupApplication](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#aa518c54e77f7c0f6e7dd129d6c433acd) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a498d9d76217cbae0aa235ac928ad02d8) | 标记申请列表为已读 |

## V2TIMConversationManager
### 会话的获取，删除和更新接口函数

| API | 描述 |
|---------|---------|
| [setConversationListener](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a39228ebb1c5d6855643aa8c1efcc429c) | 设置会话监听器 |
| [getConversationList](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a9626b74409a3f7e2899217c18202bcec) | 获取会话列表 |
| [deleteConversation](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#ae5850472b32de16f3d38ab232d621b66) | 删除会话 |
| [setConversationDraft](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#ae7f2f52bf375dae69368eae42edb28ab) | 设置会话草稿 |

## `V2TIMFriendshipManager`

###  关系链与好友资料监听器

| API | 描述 |
|---------|---------|
| [setFriendListener](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a17e92c5ca9abad7afe25b654f1fcd75c) | 设置关系链与好友资料监听器 |

### 好友添加、删除、列表获取、资料设置接口函数

| API | 描述 |
|---------|---------|
| [getFriendList](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ae478de55db21d42b72a6c5a6a5d16624) | 获取好友列表 |
| [getFriendsInfo](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a400a4bc1cc300cae5ad7fa6b17f029fc) | 获取指定好友资料 |
| [setFriendInfo](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a151b7de6219d966b4194ad7fcc8450fe) | 设置指定好友资料 |
| [addFriend](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ac335328107b329c5e4a75fd35f3061cb) | 添加好友 |
| [deleteFromFriendList](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a8cba474bb57980b183909e9a8d09e380) | 删除好友 |
| [checkFriend](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#abc51b726bb74d7a4268cb3b1bb242f7f) | 检查指定用户的好友关系 |

### 好友申请、删除接口函数

| API | 描述 |
|---------|---------|
| [getFriendApplicationList](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a482a642d6f785abb461f2a490376e7a3) | 获取好友申请列表 |
| [acceptFriendApplication](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a0d5cb04207d381ae976201cd285464c2) | 同意好友申请 |
| [refuseFriendApplication](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a7ac84e0c32d08660aefeb256ac6517fa) | 拒绝好友申请 |
| [deleteFriendApplication](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a5c869e3358ca74f9cd2eaebfc7298490) | 删除好友申请 |
| [setFriendApplicationRead](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a022b4817a31dd25707f14b8184c42675) | 设置好友申请已读 |

### 黑名单接口函数

| API | 描述 |
|---------|---------|
| [addToBlackList](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a7a1bef210f5bb18c223ecf3f0746cde0) | 添加用户到黑名单 |
| [deleteFromBlackList](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a34ed4efa939a4b86b3f4f42f0e9805e4) | 把用户从黑名单中删除 |
| [getBlackList](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a6269df2d96c910648ab2f0c43e1931c6) | 获取黑名单列表 |

### 好友分组接口函数

| API | 描述 |
|---------|---------|
| [createFriendGroup](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#abfbec300cca0464fa8297c674ff66ec9) | 新建好友分组 |
| [getFriendGroups](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a0043ca81fdeec5d3e842e85278003d1e) | 获取分组信息 |
| [deleteFriendGroup](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ac9f06f447ee4452aa12e078b48023cee) | 删除好友分组 |
| [renameFriendGroup](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a5345957f4d75d8e57ea3b4cff9adee13) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a978c80bed19697a92d1cd3892c068865) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a761d91e687619dd0e1d8a6dbc2533134) | 从好友分组中删除好友 |

## V2TIMOfflinePushManager

### 设置离线推送配置接口函数

| API | 描述 |
|---------|---------|
| [setOfflinePushConfig](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) | 设置离线推送配置信息 |
