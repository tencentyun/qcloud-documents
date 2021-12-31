>!**新老版本 API 请勿混合使用**。

## 初始化登录接口
初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API | 描述 |
|---------|---------|
| [initSDK](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ac905c315726b517ba62421471bbecf56) | 初始化 SDK |
| [unInitSDK](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a8ac73b4f71f9d9a1ca01551c919d3cdd) | 反初始化 SDK |
| [getVersion](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a8142d4e71e0ee1b8d2ec99740e2cb1ca) |获取版本号 |
| [getServerTime](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0f95b1e166f22d261e73fbf01987fb0f) |获取服务器当前时间 |
| [login](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a73fc0e14c5f2f5fc06a80081479fb416) | 登录 |
| [logout](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0398924fa1b62a8f5cc9b51673273b48) | 登出 |
| [getLoginStatus](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a1836146275265b2a120412f18961db95) | 获取登录状态 |
| [getLoginUser](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ad4b2e5a7df5e786ba369054ac582007f) | 获取当前登录用户的 UserID |

## 简单消息收发接口
如果您只需要使用文本和信令（即一段自定义buffer）消息，只需要使用这套简单消息收发接口即可。

| API | 描述 |
|---------|---------|
| [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd96fd1591e41f031421c0655d8e5d6b) | 设置基本消息（文本消息和自定义消息）的事件监听器，<br> 请不要同  [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aaccdec10b9fbee5e43eaf908e359c823)  混用。 |
| [removeSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a86ac462d87f652960d2600a52009849a) | 移除基本消息（文本消息和自定义消息）的事件监听器 |
| [sendC2CTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a59a8ba6e4a973b4c40a09ae7dfdc6981) | 发送单聊（C2C）普通文本消息 |
| [sendC2CCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af3e08b936df77210c6cdd0ce5c7fa87f) | 发送单聊（C2C）自定义（信令）消息 |
| [sendGroupTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a56359fd1ce0a96f289dcd4bef522fb52) | 发送群聊普通文本消息 |
| [sendGroupCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afbce8ff97be0a3a42c7dc826d316f2c2) | 发送群聊自定义（信令）消息 |

## 信令接口
| API | 描述 |
|---------|---------|
| [addSignalingListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a862073ac16de7f02e5f97b8cbe7eb028) | 添加信令监听。 |
| [removeSignalingListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a72f6c032de1b0dbaabb227be54d0bcfc) | 移除信令监听 |
| [invite](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a61e283c64f1a303b0a9f0e13a48de0a9) | 邀请某个人。 |
| [inviteInGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#ad51059e9f430650da09bcae01f0bb3b8) | 邀请群内的某些人 |
| [cancel](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a9d69707620f038d6e47356cdaa3ab9bd) | 邀请方取消邀请。 |
| [accept](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a4cd3629a0952db7c59186e0c222e17a0) | 接收方接收邀请 |
| [reject](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#ad9510bf8a333189fd1a0c1eafbde2266) | 接收方拒绝邀请。 |
| [getSignalingInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#ab303f20f53de134e6f6ebe5f9f9bcad0) | 获取信令信息。 |
| [addInvitedSignaling](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#ac50301e05e1672b771dc2c92fadff8de) | 添加邀请信令（可以用于群离线推送消息触发的邀请信令）。 |

## 高级消息收发接口
如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（简单消息接口和高级消息接口请不要混用）。

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aaccdec10b9fbee5e43eaf908e359c823) | 设置高级消息的事件监听器，<br> 请不要同 [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd96fd1591e41f031421c0655d8e5d6b) 混用。 |
| [removeAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a44e1e9126bf5b30234330fe19259cd93) | 移除高级消息的事件监听器 |
| [createTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a3ea254cd12aa0bcfd004f26f759b76a0) | 创建文本消息 |
| [createTextAtMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a09a259ceb314754dd267533597138391) | 创建 @ 文本消息 |
| [createCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5c2495d4b7ecd66e5636aeb865c17efd) | 创建自定义消息 |
| [createImageMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#adef5bc7a67b9a69f70f6417fd810d4b1) | 创建图片消息 |
| [createSoundMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7e661ce2b4eba1535bd04f3b6539b9dc) | 创建语音消息 |
| [createVideoMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ada17dbc78e9876a8f3a9fd24a73752b5) | 创建视频消息 |
| [createFileMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a39e4b6609321fd188a2e156a00bb3135) | 创建文件消息 |
| [createLocationMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a67cebe27192392080fc80a86c80a4321) | 创建地理位置消息 |
| [createFaceMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7ad0f3b7eff3978c12d8c912ca164a5d) | 创建表情消息 |
| [createMergerMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#acebe275789ab49cc8abe6af5e07aa3b0) | 创建合并转发消息 |
| [createForwardMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#af8f609bfbfe99a0c65611b14159b6b4d) | 创建单条转发消息 |
| [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) | 发送消息，消息对象可以由 createXXXMessage 接口创建得来。 |
| [setC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a6524143895cdee25fabd9aeeae73a3c5) | 设置单聊消息免打扰 |
| [getC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a9693dd66432f931ac0a1f2168d899501) | 获取单聊消息免打扰状态 |
| [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a2735427ac22485626aea278a9d465b3e) | 设置群聊消息免打扰状态 |
| [getC2CHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#afedccbe0e5229ae15e0e07b722ea39df) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a671e8737fcea0c05dc661c753e5b3597) | 获取群组历史消息 |
| [getHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a97fe2d6a7bab8f45b758f84df48c0b12) | 获取历史消息高级接口 |
| [revokeMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ad0dfce6be749165cd90a9ff67a1308b1) | 撤回消息，消息对象可以由 createXXXMessage 接口创建得来。 |
| [markC2CMessageAsRead](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7c09d0ba4a8018f5f9eec4760c4c7b9b) | 设置单聊（C2C）消息已读 |
| [markGroupMessageAsRead](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ac0a65f18d361abde8a0ac16132027e69) | 设置群组消息已读 |
| [deleteMessageFromLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa31e3b48fb666b970120fc0bc6343534) | 删除本地消息 |
| [deleteMessages](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#adb346fede13d493e415f6574df911e9a) | 删除本地及云端的消息 |
| [clearC2CHistoryMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a29aa6e75c2238c35cc609bef0e5a46ce) | 清空单聊本地及云端的消息 |
| [clearGroupHistoryMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a6e1a1dce441243d0bd5ac2f8bcecb3d9) | 清空群聊本地及云端的消息 |
| [insertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a04a3f6c250f9d6c0053fd71be74f047f) | 向群组消息列表中添加一条消息 |
| [insertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5afe4461b4a47205d2865ea94317d4aa) | 向单聊消息列表中添加一条消息 |
| [findMessages](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ad0dbaec04bc389d01f815f46c550e2fd) | 根据 msgID 查找本地消息 |
| [searchLocalMessages](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a9364c8a0c6a0899b17c0a479b8ca848a) | 搜索本地消息 |

## 群组相关接口
腾讯云 IM SDK 支持五种预设的群组类型，每种类型都有其适用场景：
- 工作群（Work）	：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群，同旧版本中的 Private。
- 公开群（Public）	：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息，同旧版本中的 ChatRoom。
- 社群（Community）：创建后可以随意进出，适合用于知识分享和游戏交流等超大社区群聊场景。该功能仅SDK5.8.1668增强版及以上版本支持，需购买旗舰版套餐包并 [申请开通](https://cloud.tencent.com/document/product/269/3916) 后方可使用。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API | 描述 |
|---------|---------|
| [setGroupListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a092fc428f35eb18c41a80b3655948d40) | 设置群组相关的事件监听器 |
| [createGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af836e4912f668dddf6cc679233cfb0bb) | 创建群组（简单版本） |
| [createGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a121d53137a38d0fc0bc8a8e0a9c55647) | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员 |
| [joinGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ad64a09bea508672d6d5a402b3455b564) | 加入群组 |
| [quitGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a6d140dbeb44906de9cb69f69c2ce5919) | 退出群组 |
| [dismissGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd0221c0c842a6dcfa0acc657e50caeb) | 解散群组（仅群主和管理员可以解散） |
| [getJoinedGroupList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a05bfd8f7df6bfba718abc96fdad49791) | 获取已经加入的群列表（不包括已加入的直播群） |
| [getGroupsInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ada614335043d548c11f121500e279154) | 拉取群资料 |
| [searchGroups](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a94a72082b7e2682942f35196a7e28023) | 搜索群列表 |
| [setGroupInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad87ce42b4dc4d97334fe857e4caa36c4) | 修改群资料 |
| [ initGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a17569b57abc77adb6be9356b9eb70182) | 初始化群属性 |
| [ setGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a3ec31101e4763dab7a1c99a71bc3da08) | 设置群属性 |
| [ deleteGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a45f211bafddc58bf5e199e18a6814578) | 删除群属性 |
| [ getGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ade2155fb24ed1c0b8eb976e146c14e3d) | 获取群属性 |
| [getGroupOnlineMemberCount](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a56840105a4b3371eeab2046d8c300bce) | 获取群在线人数 |
| [getGroupMemberList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a69fc0831aacaa0585c1855f4c91320be) | 获取群成员列表 |
| [getGroupMembersInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#adb08e1c4fa9aff407c7b2678757f66d5) | 获取指定的群成员资料 |
|  [searchGroupMembers](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a493fb73258019961f3ca8934ff625b0a) | 搜索群成员 |
| [setGroupMemberInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a6f1cf8ede41348b4cd7b63b8e4caa77b) | 修改指定的群成员资料 |
| [muteGroupMember](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a450230c4d129611e1b0519827ec0f8b5) | 禁言 |
| [kickGroupMember](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a6da6755c6e0c46e96cb02575074a5333) | 踢人 |
| [setGroupMemberRole](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a34ebf60528d02626834f022b4ebabfa8) | 切换群成员的角色 |
| [transferGroupOwner](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ac16d66c8e293c2ee95c7b673e5ad80c4) | 转让群主 |
| [inviteUserToGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#afd219107653b877e446c149531d65e92) | 邀请他人入群 |
| [getGroupApplicationList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a240db7bdc023ad6fc63e9ee9b72714c4) | 获取加群的申请列表 |
| [acceptGroupApplication](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad743008d30c909ef0be0f8aa91102e07) | 同意某一条加群申请 |
| [refuseGroupApplication](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#aa518c54e77f7c0f6e7dd129d6c433acd) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a498d9d76217cbae0aa235ac928ad02d8) | 标记申请列表为已读 |

## 会话列表相关接口
会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API | 描述 |
|---------|---------|
| [setConversationListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a39228ebb1c5d6855643aa8c1efcc429c) | 设置会话监听器 |
| [getConversationList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a1bb5ba2beecb4f68146e7f664124fd8b) | 获取会话列表 |
| [getConversation](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a619aaff2bb5664e094d2341819b95096) | 获取指定单个会话 |
| [getConversationList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a1bb5ba2beecb4f68146e7f664124fd8b) | 获取指定多个会话 |
| [deleteConversation](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a7a6e38c5a7431646bd4c0c4c66279077) | 删除会话 |
| [setConversationDraft](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#ae7f2f52bf375dae69368eae42edb28ab) | 设置会话草稿 |
| [pinConversation](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a4da7467f54c891c4929152260e42f4b6) | 置顶会话 |
| [getTotalUnreadMessageCount](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a08bdd15d7ee2737335a01285d7f9c44a) | 获取会话总未读数 |

## 用户资料相关接口
包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API | 描述 |
|---------|---------|
| [getUsersInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a7ca8c0f71a9875021fc35dfcaff68d1e) | 获取用户资料 |
| [setSelfInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af004ab2f1d1458de354883f1995b678a) | 修改个人资料 |
| [addToBlackList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a8804c7f47000bf1c26aa6ab744a53456) | 屏蔽某人的消息（添加该用户到黑名单中） |
| [deleteFromBlackList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a3dcd8f1c70dceafa94ab48796c2f26aa) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a6269df2d96c910648ab2f0c43e1931c6) | 获取黑名单列表 |

## 离线推送相关接口
如果想要在 App 切后台时依然能够实时收到 IM 消息，可以使用离线推送服务。由于大陆境内尚没有统一的推送服务，Android 的离线推送需要针对不同厂商的手机进行 [逐一适配](https://cloud.tencent.com/document/product/269/44516)。

| API | 描述 |
|---------|---------|
| [setOfflinePushConfig](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) | 设置离线推送配置信息 |

## 好友管理相关接口
腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [**控制台**](https://console.cloud.tencent.com/im) >**功能配置**>**登录与消息**>**好友关系检查**中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API | 描述 |
|---------|---------|
| [setFriendListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a17e92c5ca9abad7afe25b654f1fcd75c) | 设置关系链的监听器，用于接收好友列表和黑名单的变更事件 |
| [getFriendList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ae478de55db21d42b72a6c5a6a5d16624) | 获取好友列表 |
| [getFriendsInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a88732b0f7a5e77a9dd34403fe7bbdd21) | 获取指定好友资料 |
| [setFriendInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a151b7de6219d966b4194ad7fcc8450fe) | 设置指定好友资料 |
| [searchFriends](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a815b7c4ff79f1441ee1416ff679eda6a) | 搜索好友列表 |
| [addFriend](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a19d0f22aaea285e8cee85a5dd6ed9208) | 添加好友 |
| [deleteFromFriendList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#af7ecf8641b58462d038a9c97bfbd4d61) | 删除好友 |
| [checkFriend](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#accac9a69c8e4332b0b83755ec54ecfed) | 检查指定用户的好友关系 |
| [getFriendApplicationList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a2dbf4da19f3b9b170089b8e8cb210166) | 获取好友申请列表 |
| [acceptFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ab69ed69330428caff6f468b7df5259fa) | 同意好友申请 |
| [refuseFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#af1bcbc196015de8e7a94b1575c466f89) | 拒绝好友申请 |
| [deleteFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a5c869e3358ca74f9cd2eaebfc7298490) | 删除好友申请 |
| [setFriendApplicationRead](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a022b4817a31dd25707f14b8184c42675) | 设置好友申请已读 |
| [createFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#afe729e7a74d1e7fd06a5f23c155a08ae) | 新建好友分组 |
| [getFriendGroups](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a0043ca81fdeec5d3e842e85278003d1e) | 获取分组信息 |
| [deleteFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ac9f06f447ee4452aa12e078b48023cee) | 删除好友分组 |
| [renameFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a5345957f4d75d8e57ea3b4cff9adee13) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a6de9168d476ac14e21025ec5c26251df) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ae367dfec88522e96d96c5ab942e50653) | 从好友分组中删除好友 |
