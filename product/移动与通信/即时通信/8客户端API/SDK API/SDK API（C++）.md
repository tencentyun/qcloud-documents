## 初始化登录接口

初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API                                                          | 描述                      |
| ------------------------------------------------------------ | ------------------------- |
| [InitSDK](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#aecee922675b671cd979d68604a4be1bb) | 初始化 SDK                |
| [UnInitSDK](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a6c88218989a1c714b4e989d1696439a0) | 反初始化 SDK              |
| [GetVersion](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a8f5a603b985b2e305e6182db0e31c516) | 获取版本号                |
| [GetServerTime](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#af18ff99404db53f627aa619ac744a08d) | 获取服务器当前时间        |
| [Login](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a6a9c19be21327ace77ab75657d2944b3) | 登录                      |
| [Logout](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#abf4f7e18d22fe8f75b5212fcf82e7113) | 登出                      |
| [GetLoginStatus](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#ad5888b2d240c2fcb076b060d298a2c22) | 获取登录状态              |
| [GetLoginUser](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#ad19e832506181f6ec955d9e0d2035797) | 获取当前登录用户的 UserID |

## 简单消息收发接口

如果您只需要使用文本和信令（即一段自定义 buffer）消息，可通过如下消息收发接口实现。

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [AddSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#ad039bd93fe1a09cf45034697e1c1328f) | 设置基本消息（文本消息和自定义消息）的事件监听器， 请不要同 [AddAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a498688ee0f672f114e28d830761dfbf8) 混用 |
| [RemoveSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#ab4355384fafb97a099d518f40dbc7654) | 移除基本消息（文本消息和自定义消息）的事件监听器             |
| [SendC2CTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a55ff3770a4267e331cd31fcd9475a6e5) | 发送单聊（C2C）普通文本消息                                  |
| [SendC2CCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a07d2bcf26547adb609f7aef752cd8189) | 发送单聊（C2C）自定义（信令）消息                            |
| [SendGroupTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a3006778f10df146968858a53cc4854ec) | 发送群聊普通文本消息                                         |
| [SendGroupCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a9e49af2df4299a8546e19661c2792cad) | 发送群聊自定义（信令）消息                                   |

## 信令接口

| API                                                          | 描述                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [AddSignalingListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#ad05971845c3daa32b5c3ceac33cd7440) | 添加信令监听                                         |
| [RemoveSignalingListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#aee990a20a262f205cfa6d5c8117a64c2) | 移除信令监听                                           |
| [Invite](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#a85e7fab6f656ff007fa1fae5400ff547) | 邀请某个人                                           |
| [InviteInGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#a4813ae9206eb27438293054a076e2441) | 邀请群内的某些人                                       |
| [Cancel](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#a2e57c098f73789bf1a6ac0c2b916e6e0) | 邀请方取消邀请                                       |
| [Accept](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#a714672da1a57c1006368650842fc5f29) | 接收方接收邀请                                         |
| [Reject](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#abd2c124577c39c0a992a34b54665cb9b) | 接收方拒绝邀请                                       |
| [GetSignalingInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#afc6d9c1e14e05f87e7ea108711095cb8) | 获取信令信息                                         |
| [AddInvitedSignaling](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMSignalingManager.html#adefac3df746100d0afaff911066bcd7f) | 添加邀请信令（可以用于群离线推送消息触发的邀请信令） |

## 高级消息收发接口

如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（简单消息接口和高级消息接口请不要混用）。

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [AddAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a498688ee0f672f114e28d830761dfbf8) | 设置高级消息的事件监听器， 请不要同 [AddSimpleMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#ad039bd93fe1a09cf45034697e1c1328f) 混用 |
| [RemoveAdvancedMsgListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a7e27cbe3f0cc26e09de0bdee8b192bea) | 移除高级消息的事件监听器                                     |
| [CreateTextMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#ab96fac17ae7cb4d1e367dff40aa0694c) | 创建文本消息                                                 |
| [CreateTextAtMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#afa39182f419c621fc929eb3929206107) | 创建 @ 文本消息                                              |
| [CreateCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a3af1cc2c76c41f3e48080134502ac8d5) | 创建自定义消息                                               |
| [CreateImageMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a1f066186491a282c98f9cf7296720775) | 创建图片消息                                                 |
| [CreateSoundMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a017a0c2902d045a70a9d5b686154984e) | 创建语音消息                                                 |
| [CreateVideoMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#acdaefbfd8bd4826caa86c94a42d701a4) | 创建视频消息                                                 |
| [CreateFileMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a57e965e5e82477446b25253a1ae07110) | 创建文件消息                                                 |
| [CreateLocationMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a9bffc91ae3fa7ba6e330a2ffd325665a) | 创建地理位置消息                                             |
| [CreateFaceMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a72c548e00aed06ef99aca1d55d5895c2) | 创建表情消息                                                 |
| [CreateMergerMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#afc00a2a85b3d29ccfc472ea6544eccf3) | 创建合并转发消息                                             |
| [CreateForwardMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#aaff05e59893cb1cfe5a806e700e1e270) | 创建单条转发消息                                             |
| [SendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a42db237e7ae52cd2aa7edebf4f435c61) | 发送消息，消息对象可以由 CreateXXXMessage 接口创建得来     |
| [SetC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#adf166f08b68a5df8de19d152bcf868b3) | 设置单聊消息免打扰                                           |
| [GetC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a30a4979460e73c897b6130ba40356afa) | 获取单聊消息免打扰状态                                       |
| [SetGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a866d06c28faf058f253f29be6f5b3fe2) | 设置群聊消息免打扰状态                                                                    |
| [GetHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a4bbdbdd063d5dad2d164059e1f5d7851) | 获取历史消息高级接口                                         |
| [RevokeMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a3f271fcb935ada0ef05709367638a1a6) | 撤回消息，消息对象可以由 CreateXXXMessage 接口创建得来     |
| [MarkC2CMessageAsRead](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a024f95bcf2b37a354f11f5b5a4d6920f) | 设置单聊（C2C）消息已读                                      |
| [MarkGroupMessageAsRead](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#abdf09c92dccfb71b58b8a36f42494b8d) | 设置群组消息已读                                             |                                                
| [DeleteMessages](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#ac340e09d426d983fb4b6cf48d9a7ebca) | 删除本地及云端的消息                                         |
| [ClearC2CHistoryMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#aade0f8d9a53a87473990714f17a297bc) | 清空单聊本地及云端的消息                                     |
| [ClearGroupHistoryMessage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a1207155633e3deb59616d4deb779d1eb) | 清空群聊本地及云端的消息                                     |
| [InsertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a19813d01f229f5c1a413684b56c54e1b) | 向群组消息列表中添加一条消息                                 |
| [InsertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#abba2adf81fa2bb457c14fffb9ae0eda4) | 向单聊消息列表中添加一条消息                                 |
| [FindMessages](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#ac5531e73378b8b8eadd056ba99e5427e) | 根据 msgID 查找本地消息                                      |
| [SearchLocalMessages](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMMessageManager.html#a46be86c0177c868f03fc939c88e2e36d) | 搜索本地消息                                                 |

## 群组相关接口

腾讯云 IM SDK 支持四种预设的群组类型，每种类型都有其适用场景：

- 工作群（Work） ：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群。
- 公开群（Public） ：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API                                                          | 描述                                                       |
| ------------------------------------------------------------ | ---------------------------------------------------------- |
| [AddGroupListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a05af3d083cef4d667cf972e0cf340289) | 添加群组相关的事件监听器                                   |
| [RemoveGroupListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a60fe2aac014661aeaf3cbbafaea830e3) | 移除群组相关的事件监听器                                   |
| [CreateGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a0325514b94a734186be684eb9bb5cc80) | 创建群组（简单版本）                                       |
| [CreateGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#ac28eb2db747a62a12fedc604a2abfbbd) | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员 |
| [JoinGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#adf3dc4604f30fde1d34dceb1990b38fe) | 加入群组                                                   |
| [QuitGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a43ef277f0eb49d6087d140a09152eced) | 退出群组                                                   |
| [DismissGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#abfa30c09968c3b6d07c31d8d5a741502) | 解散群组（仅群主和管理员可以解散）                         |
| [GetJoinedGroupList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a3b740704edfeab9602867e284c2c7ba8) | 获取已经加入的群列表（不包括已加入的直播群）               |
| [GetGroupsInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a8c98b92b45c3a2c4e57901e6c4cd3435) | 拉取群资料                                                 |
| [SearchGroups](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a63b463ce1a5952adf8d88bc794b32f22) | 搜索群列表                                                 |
| [SetGroupInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a10785c46e166879250c2c2ba2001b354) | 修改群资料                                                 |
| [InitGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a049a490d04dde4cf925491809a6df6e2) | 初始化群属性                                               |
| [SetGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a35accef15afd5def586332c7397cee7b) | 设置群属性                                                 |
| [DeleteGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#acdbc438459cfd970bd557a3b252db768) | 删除群属性                                                 |
| [GetGroupAttributes](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a7e719bb36c782f56849a6b46bf2afab4) | 获取群属性                                                 |
| [GetGroupOnlineMemberCount](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a7633181ee22e54741600908ed45b3138) | 获取群在线人数                                             |
| [GetGroupMemberList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#ade696bf03f06de9cdfb534570de35254) | 获取群成员列表                                             |
| [GetGroupMembersInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a6db2fcfd78bbd71003ae31584c88c672) | 获取指定的群成员资料                                       |
| [SearchGroupMembers](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a705a17828623117e51da885da02d8b12) | 搜索群成员                                                 |
| [SetGroupMemberInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#acd0e222e4c3d5997666aaf4126bd974e) | 修改指定的群成员资料                                       |
| [MuteGroupMember](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#ab19d433e5552205fcba61627e54f7569) | 禁言                                                       |
| [KickGroupMember](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#ad2e4f74f4e26fb0db455d8e92f774032) | 踢人                                                       |
| [SetGroupMemberRole](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#ab429c1ded6aa3ae27bb0917be6f71dd3) | 切换群成员的角色                                           |
| [TransferGroupOwner](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a2fedff98e2e41e9d30f7a49f5c7adc8f) | 转让群主                                                   |
| [InviteUserToGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a46fecb95bf66ccc3023201fb3737c423) | 邀请他人入群                                               |
| [GetGroupApplicationList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a4609879f4c67fde60a6fa4f707987143) | 获取加群的申请列表                                         |
| [AcceptGroupApplication](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#ae829188e149f59bb5b086825f6c94ab5) | 同意某一条加群申请                                         |
| [RefuseGroupApplication](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a7cf4cdc85fab3794399137726736571b) | 拒绝某一条加群申请                                         |
| [SetGroupApplicationRead](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMGroupManager.html#a25eeb7d946d9f0eec064dc2c4c6b17a6) | 标记申请列表为已读                                         |

## 会话列表相关接口

会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [AddConversationListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#adb2c20ca824cac69d0703169f3a025a1) | 添加会话监听器   |
| [RemoveConversationListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#a0bcc8a8b6adbaaff227c970ccfad2a53) | 移除会话监听器   |
| [GetConversationList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#adf840d9f4eb800ff74a2a6852d56fc35) | 获取会话列表     |
| [GetConversation](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#a9891f4b029e7a1fd3d17398cbe1b367c) | 获取指定单个会话 |
| [GetConversationList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#a05675f2f0c00aedc2af7a2cd6cf2eb6b) | 获取指定多个会话 |
| [DeleteConversation](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#a1ada2a3c1c0ae08920bdf16ab994a1ed) | 删除会话         |
| [SetConversationDraft](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#a190fb079bf34077f71c340ec23e69ebf) | 设置会话草稿     |
| [PinConversation](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#ab5afaa92ec352f112125f5dcef288f8d) | 置顶会话         |
| [GetTotalUnreadMessageCount](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#a50e0d25b7f47c12c815e610bf5b9a048) | 获取会话总未读数 |

## 用户资料相关接口

包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API                                                          | 描述                                         |
| ------------------------------------------------------------ | -------------------------------------------- |
| [GetUsersInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#ac7aa404aec07fc0d9823d9da5fd4e443) | 获取用户资料                                 |
| [SetSelfInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#acb89663576c7f68cc4b9983733835e29) | 修改个人资料                                 |
| [AddToBlackList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a2f49378d21cb0d48b9e1e1814dc2460e) | 屏蔽某人的消息（添加该用户到黑名单中）       |
| [DeleteFromBlackList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a8bacf997892119e021a8f4aa4db48de3) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [GetBlackList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a8d402bd222d8dcb98516185bd75fc5b2) | 获取黑名单列表                               |

## 好友管理相关接口

腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [**控制台**](https://console.cloud.tencent.com/im) >**功能配置**>**登录与消息**>**好友关系检查**中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API                                                          | 描述                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [AddFriendListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#ac4c542617008471fa1fe7a64ba963fbb) | 添加关系链监听器 
| [RemoveFriendListener](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#ae21ca2737c35305ecc1f25e054265ed8) | 移除关系链监听器
| [GetFriendList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a11bcb462e073ebec63a2586bad9757cf) | 获取好友列表                                           |
| [GetFriendsInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a9b263f612a1e7e35ee2c745b5f36a1e3) | 获取指定好友资料                                       |
| [SetFriendInfo](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#abe9169909b008fd0a43044356e3206a0) | 设置指定好友资料                                       |
| [SearchFriends](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#aea84cd163665db3b0f2338d787446f53) | 搜索好友列表                                           |
| [AddFriend](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a47ae7c54faf0b4b0f1d0a14fe7ed27d3) | 添加好友                                               |
| [DeleteFromFriendList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#ae46d0b7f89dac1867de915b7fed3b479) | 删除好友                                               |
| [CheckFriend](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a90046f679ca31dedc00bbecff065538f) | 检查指定用户的好友关系                                 |
| [GetFriendApplicationList](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#aad42cc5d8f5c7abf3c2710697c29a9f9) | 获取好友申请列表                                       |
| [AcceptFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a9cfb992e1c1b958208f3c1b48a6b336d) | 同意好友申请                                           |
| [RefuseFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a333de917766b6999e819eafc0513bf6f) | 拒绝好友申请                                           |
| [DeleteFriendApplication](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a1243005c5ff2032c34dc8f3adf22f11d) | 删除好友申请                                           |
| [SetFriendApplicationRead](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a91f8045a48c78a8da493f67188078baf) | 设置好友申请已读                                       |
| [CreateFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a8f4192055ef6b4d85e01983a6369f0d4) | 新建好友分组                                           |
| [GetFriendGroups](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a3190b203cda3e1cabb947aded25c6354) | 获取分组信息                                           |
| [DeleteFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#aef0784eca4e5c17d5ef12da5788338b6) | 删除好友分组                                           |
| [RenameFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a74ada64658763bc5eb7f918993e15649) | 修改好友分组的名称                                     |
| [AddFriendsToFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a6bb688a4a82c1bc158a7873eda738c2f) | 添加好友到一个好友分组                                 |
| [DeleteFriendsFromFriendGroup](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMFriendshipManager.html#a0d9d90dc372d82b07a79fe5e843f3ab6) | 从好友分组中删除好友                                   |
