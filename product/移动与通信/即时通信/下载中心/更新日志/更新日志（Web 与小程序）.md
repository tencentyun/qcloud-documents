
### 2.26.6 @2023.3.17

**新增**

- [sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage) 发送消息支持不过安全审核。
- uni-app 离线推送支持荣耀手机。

**变更**

- 体积优化，减少45KB。
- 提升 SDK 稳定性。

**修复**

- 偶现的 [joinGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#joinGroup) 后查询群资料失败导致加群失败。
- 最近联系人中有带未读数的空会话，未读数无法清零。

### 2.26.2 @2023.2.24

**新增**

支持单聊消息撤回通知存未读，保障弱网下消息状态的准确性。

**变更**

删除视频消息默认封面图。

**修复**

空会话导致的会话列表排序问题。

### 2.26.1 @2023.2.10

**修复**

- 群历史消息最近一条是群提示消息的场景下，群会话的 lastMessage.lastTime 不准确。
- 调用 [markConversation](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#markConversation) 接口设置了会话标记，重新登录后标记内容缺失。
- 调用 [createGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createGroup) 接口创建群组偶现查群资料失败。
- 调用 [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 接口拉群历史消息，部分场景下历史消息缺失。

### 2.26.0 @2023.1.13

**新增**

- [translateText](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#translateText) 接口，支持翻译文本。
- [setGroupCounters](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setGroupCounters) 接口，支持设置群计数器。接入侧可通过此接口实现一些常见的计数功能，如点赞计数、直播群礼物计数、观看人数计数等。
- [increaseGroupCounter](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#increaseGroupCounter) 接口，递增群计数器。
- [decreaseGroupCounter](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#decreaseGroupCounter) 接口，递减群计数器。
- [getGroupCounters](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupCounters) 接口，获取群计数器。
- 支持拉取群消息撤回信令，提升弱网下群消息被撤回状态的准确性。
- [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 新增字段 `revoker`，标识消息撤回者的 `userID`。

**修复**

- 跨站购买的号段未被识别为国际站。
- 重复登录日志提示的 userID 错误。


### 2.25.0 @2022.12.8

**新增**

- [clearHistoryMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#clearHistoryMessage) 接口，支持清空本地及云端消息。
- 支持消息扩展（旗舰版功能）。
- 支持普通群和社群群属性。
- 兼容 [wx.chooseMedia](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.chooseMedia.html)。
- [Message.readReceiptInfo](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 支持 C2C 已读回执（数据结构跟 NativeIM 对齐）。
- 错误码2101：未加入直播群不能向直播群发送消息。

**变更**

- 日志上报备份通道使用独立集群域名 `https://events.im.qcloud.com`（小程序平台需新增一个受信域名配置）。

**修复**

- cookies blocked 导致的运行时错误（Failed to read the 'localStorage' property from 'Window': Access is denied for this document）。


### 2.24.1 @2022.11.11

**新增**

- 英文版 ts 声明文件。
- restapi 修改好友自定义资料字段支持推送给 SDK。

**修复**

- [getMessageListHopping](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageListHopping) 部分场景下返回结果异常的问题。

### 2.24.0 @2022.11.3

**新增**

- 支持微信小游戏环境集成。
- 本地审核插件 [tim-profanity-filter-plugin](https://www.npmjs.com/package/tim-profanity-filter-plugin) ，支持本地审核功能。
- [getFriendProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getFriendProfile) 默认支持拉取好友自定义字段和资料自定义字段，提升产品体验。
- [getGroupApplicationList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupApplicationList) 支持拉取全量的加群申请列表。
- RESTAPI 修改好友自定义字段支持推送给 SDK。
- 支持发送话题消息不计入未读。
- 支持发送普通社群消息不计入未读。
- 发送消息支持 voip push。

**修复**

- 好友资料相关的问题。


### 2.23.1 @2022.9.29

**新增**

- [createTextMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createTextMessage) 等接口支持创建群定向消息（即在群组内发送消息给部分群成员，其他群成员不会收到这些消息）。
- 支持发送 mov 格式的视频。
- REST API [更新好友](https://cloud.tencent.com/document/product/269/12525) 支持推送给 SDK。
- [getFriendProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getFriendProfile) 支持拉取自定义好友字段和自定义资料字段。
- [getConversationList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getConversationList) 接口的返回数据新增字段 isSyncCompleted，用于标识从云端同步会话列表是否完成。
- 话题所属的社群消息，支持通过 [MESSAGE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_RECEIVED) 事件通知给接入侧。
- 完善对 uni-app [离线推送](https://cloud.tencent.com/document/product/269/79587) 的支持。

**修复**

- 群列表超过上限5000后，部分群会话拉不到漫游消息的问题。
- 调用 setConversationCustomData 设置会话自定义字段后重新登录，对应会话的 customData 为 '' 的问题。

### 2.23.0 @2022.9.16

**新增**

- SDK 支持境外环境。
- [getTotalUnreadMessageCount](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getTotalUnreadMessageCount)，支持获取会话未读总数。
- [TOTAL_UNREAD_MESSAGE_COUNT_UPDATED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.TOTAL_UNREAD_MESSAGE_COUNT_UPDATED)，接入侧监听此事件，可获取会话未读总数变更的通知。
- [markGroupMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#markGroupMemberList)，支持标记直播群群成员（需开通旗舰版）。
- 群成员被踢出群，或者群被解散，SDK 同步更新此群会话所在的会话分组。
- 支持小程序独立分包。
- Web 多实例登录场景下，断网重连后 SDK 主动恢复最近联系人的消息记录，保障消息可靠性。

**修复**

- Web 多实例登录场景下可能出现的会话 lastMessage 撤回状态不同步问题。
- 同步最近联系人时会话置顶问题。

### 2.22.0 @2022.8.18

**新增**

- 支持 uni-app 打包到 native app 使用离线推送，请参见 [registerPlugin](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#registerPlugin)。
- 支持获取直播群在线成员列表，请参见 [getGroupMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberList) （需开通旗舰版）。
- 支持直播群封禁成员，请参见 [deleteGroupMember](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteGroupMember)（需开通旗舰版）。
- [setConversationCustomData](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setConversationCustomData) 设置会话自定义数据。
- [markConversation](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#markConversation) 标记会话（需开通旗舰版）。
- [getConversationGroupList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getConversationGroupList) 获取会话分组列表（需开通旗舰版）。
- [createConversationGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createConversationGroup) 创建会话分组（需开通旗舰版）。
- [deleteConversationGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteConversationGroup) 删除会话分组（需开通旗舰版）。
- [renameConversationGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#renameConversationGroup) 重命名会话分组（需开通旗舰版）。
- [addConversationsToGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#addConversationsToGroup) 添加会话到一个会话分组（需开通旗舰版）。
- [deleteConversationsFromGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteConversationsFromGroup) 从一个会话分组中删除会话（需开通旗舰版）。

**修复**

- 收到话题消息被撤回的通知后，话题未读数未更新的问题。

### 2.21.2 @2022.8.8

**新增**

- 支持 Web 端创建和发送语音消息。
- [createMergerMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createMergerMessage) 创建合并消息，被合并的消息新增 ID 字段。

### 2.21.1 @2022.8.3

**修复**

[resendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#resendMessage) 可能导致的消息重复问题。

### 2.21.0 @2022.7.28

**新增**

- [setSelfStatus](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setSelfStatus)，设置自己的自定义状态。
- [getUserStatus](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getUserStatus)，查询用户状态。
- [subscribeUserStatus](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#subscribeUserStatus)，订阅用户状态。
- [unsubscribeUserStatus](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#unsubscribeUserStatus)，取消订阅用户状态。
- [setMessageRemindType](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setMessageRemindType) 支持群消息和话题消息的免打扰设置多端、多实例同步。
- [createFileMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createFileMessage) 支持手机端微信小程序 和 QQ 小程序发文件消息。
- [modifyMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#modifyMessage) 支持变更所有类型消息的 cloudCustomData。
- [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 新增字段 isBroadcastMessage，支持直播群广播消息。
- 支持加群选项多终端、多实例同步。
- 支持普通社群和话题@全员以及话题 lastMessage。

**变更**

- 浏览器支持 webworker 时国际站和私有化环境默认开启 webworker。

**修复**

- 收到不更新会话 lastMessage 的消息后，lastMessage.payload 被置为 undefined 的问题。
- 在线消息引起的群组消息补偿未启动问题。
- 频繁退群、加群后拉群漫游消息异常。
- 分页拉取群组列表滞后导致拉取群会话漫游消息为空数组的问题。
- 话题已知问题。

### 2.20.1 @2022.6.27

**变更**

- 退出/被踢出非直播群，或非直播群被解散，只删除群组记录，不删除对应的群会话，体验对齐 native。
- [deleteMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteMessage) 不支持删除群系统通知，并给出具体错误信息。
- 私有化部署的富媒体消息支持 HTTP 协议。

**修复**

- 小程序前后台切换等场景下偶现群会话丢失问题。
- C2C 会话 lastMessage 被异常更新问题。

### 2.20.0 @2022.6.9

**新增**

- [modifyMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#modifyMessage)，支持消息变更。
- [getMessageListHopping](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageListHopping)，支持根据指定的消息 sequence 或消息时间拉取会话的消息列表。
- 支持针对单条或多条 C2C 消息发送已读回执（需开通旗舰版）。
- C2C 会话 lastMessage 新增字段 isPeerRead，用于标识对端是否已读。
- 支持群提示消息不计入会话未读。
- 新增类型 [TIM.TYPES.KICKED_OUT_REST_API](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.KICKED_OUT_REST_API)，支持 REST API [kick](https://cloud.tencent.com/document/product/269/3853)。

**变更**

完善并优化 [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 拉漫游消息的体验。

**修复**

- 传参问题导致的 [deleteMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteMessage) 成功后会话列表未更新。
- 部分机型真机调试小程序时遇到的 `Cannot add property markTimeline, Object is not extensible` 问题。

### 2.19.1 @2022.5.7

**新增**

- 支持 [社群（Community）](https://cloud.tencent.com/document/product/269/1502#.E7.BE.A4.E7.BB.84.E7.B1.BB.E5.9E.8B.E4.BB.8B.E7.BB.8D)下创建话题（Topic），支持互动性更强的场景。
- [getJoinedCommunityList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getJoinedCommunityList) 获取支持话题的社群列表。
- [createTopicInCommunity](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createTopicInCommunity) 创建话题。
- [deleteTopicFromCommunity](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteTopicFromCommunity) 删除话题。
- [updateTopicProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateTopicProfile) 设置话题资料。
- [getTopicList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getTopicList) 获取话题列表。
- [Topic](https://web.sdk.qcloud.com/im/doc/zh-cn/Topic.html) 社群话题对象，用于描述话题具有的属性，如名称、公告、简介、未读数等信息。
- 事件 [TIM.EVENT.TOPIC_CREATED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.TOPIC_CREATED) 创建话题时触发。
- 事件 [TIM.EVENT.TOPIC_DELETED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.TOPIC_DELETED) 删除话题时触发。
- 事件 [TIM.EVENT.TOPIC_UPDATED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.TOPIC_UPDATED) 话题资料更新时触发。

### 2.18.2 @2022.4.22

**变更**

优化直播群使用体验。

**修复**

- 部分场景下统计不准确的问题。
- 调用接口 [getGroupMessageReadMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMessageReadMemberList) 返回结果不准确的问题。

### 2.18.0 @2022.4.8

**新增**

- [sendMessageReadReceipt](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessageReadReceipt) 发送群消息已读回执。
- [getMessageReadReceiptList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageReadReceiptList) 拉取群消息已读回执列表。
- [getGroupMessageReadMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMessageReadMemberList) 拉取群消息已读（或未读）群成员列表。
- [findMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#findMessage) 根据 messageID 查询会话的本地消息。
- 消息被撤回后，会话未读数的变更体验对齐 NativeIM。

**变更**

- [Message.ID](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 拼接规则为 `${senderTinyID}-${clientTime}-${random}`，与 NativeIM 消息的 ID 拼接规则一致。
- SDK not ready 时提示具体原因，方便接入侧使用。

**修复**

踢出群成员后，其它群成员从 [CONVERSATION_LIST_UPDATED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.CONVERSATION_LIST_UPDATED) 事件回调里面获取的 `Conversation.groupProfile.memberCount` 值未更新。

### 2.17.0 @2022.3.2

**新增**

- 支持 [社群](https://cloud.tencent.com/document/product/269/1502#.E7.BE.A4.E7.BB.84.E7.B3.BB.E7.BB.9F.E7.AE.80.E4.BB.8B)。
- 最近联系人 `Conversation.lastMessage` 支持群提示消息。
- `Message.payload.memberList` 支持获取加入群或者退出群的群成员的昵称、头像等信息。
- 发送图片消息支持 webp 格式的图片。
- 发视频消息支持视频封面 [snapshotUrl](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.VideoPayload)。
- 优化消息传输效率，节流 [CONVERSATION_LIST_UPDATED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.CONVERSATION_LIST_UPDATED) 等事件。

**修复**

- 发送了带自定义数据（cloudCustomData）的消息后，重新登录后 cloudCustomData 为空的问题。
- [login](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#login) 失败后再次登录提示“请勿重复登录”的问题。
- [getGroupProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupProfile) 后 `Conversation.groupProfile` 与最新群资料不一致的问题。

### 2.16.3 @2022.2.11

**修复**

Windows 微信访问小程序和 uni-app 打包 Android app（部分设备）后遇到的无法登录的问题。

### 2.16.2 @2022.2.10

**新增**

- 支持 uni-app 打包 native app 后发送文件消息。
- 支持印度国际站。

**修复**

- 部分 emoji 表情渲染问题。

### 2.16.1 @2022.1.14

**新增**

- 支持支付宝小程序发送 .image 后缀的图片。
- 删除会话 [deleteConversation](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteConversation) 同时删除历史消息。

**修复**

- 下行文件消息 `fileName` 为空字符串导致的错误。
- 群属性接口调用时序引起的问题。
- uni-app 打包到百度小程序等平台，遇到的 `__wxConfig is not defined` 问题。

### 2.16.0 @2022.1.5

**新增**

- [setMessageRemindType](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setMessageRemindType)，支持设置 C2C 会话消息免打扰。
- [setAllMessageRead](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setAllMessageRead)，支持一键清空所有会话未读。
- [sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage)，支持发送不计入会话未读和不更新会话 `lastMessage` 的消息。
- 支持直播群新成员查看入群前历史消息（需开通旗舰版）。

**变更**

- SDK 使用 [严格模式](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode)。
- 会话列表过滤掉与被删除的帐号的会话。
- 优化漫游消息的 `nick` 和 `avatar` 的更新时机。
- 收到对端（好友）资料更新后，对应更新 `conversation.userProfile`。

**修复**

- 非 UTF-8 字符导致 WebSocket 长连接异常断开问题。
- [deleteMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteMessage) 时传入复制的消息导致的运行时错误： `e.getOnlineOnlyFlag is not a function`。
- [deleteMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteMessage) 后会话 `lastMessage` 未正确更新。
- C2C 会话未读数计算问题。
- C2C 会话的实时消息未带 `nick` 和 `avatar` 导致的消息渲染异常。
- 偶现的会话 `lastMessage.payload` 为 `null`。
- 预签名上传图片缩略图 URL 不生效。
- @ 群成员，重新登录后拉漫游消息，对应的 message.atUserList 为空数组。
- 处理群提示消息（转让群主）时的错误。
- 一些统计错误。

### 2.15.0 @2021.10.29

**新增**

- 支持国际站。
- [createLocationMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createLocationMessage)，支持发送地理位置消息。
- 上传图片、视频、文件等带文件类型，方便下载和预览，兼容 uniapp。
- [Conversation](https://web.sdk.qcloud.com/im/doc/zh-cn/Conversation.html) `lastMessage` 数据结构新增 `nick` `nameCard` 字段，便于展示群聊会话 `lastMessage` 的发送者的信息。

**变更**

- [getConversationList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getConversationList) 支持批量获取指定会话。
- 提高了长连接的稳定性。

**修复**

- 无会话列表缓存，最近联系人没有分页的情况下，登录后未派发事件 [CONVERSATION_LIST_UPDATED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.CONVERSATION_LIST_UPDATED)。
- 部分场景 [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 回包 `isCompleted` 始终为 `false`。
- [createFaceMessage](createFaceMessage)设置 `index` 为0接收方丢失 `index` 字段。

### 2.14.0 @2021.9.24

**新增**

- [pinConversation](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#pinConversation)，支持会话置顶。
- [initGroupAttributes](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#initGroupAttributes) 等群属性相关接口，支持 TRTC 语聊房的麦位管理。

**变更**

- 发送群聊消息自动补齐消息体 `nameCard` 属性，便于接入侧展示。
- 因多端登录或多实例登录被踢下线时，不再触发服务端的 logout 回调。

**修复**

- C2C 会话拉漫游消息偶现丢消息。
- 加群附言（applyMessage）缺失。

### 2.13.1 @2021.8.27

**变更**

- 未登录时，连续调用 [login](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#login)，返回错误码 `2025`，表示【重复登录】。
- WebSocket 重连后，SDK 重新登录并同步未读消息，保障消息的可靠性。

**修复**

- 未登录时，连续调用 [login](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#login) 后会话的未读数错误。
- 调用 [setGroupMemberNameCard](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setGroupMemberNameCard) 接口，`nameCard` 传入空字符串后报错。
- 调用 [getGroupMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberList) 接口，回包数据 `muteUntil` 的值错误。

### 2.13.0 @2021.8.23

**新增**

支持好友关系链，请参见 [使用指引](https://web.sdk.qcloud.com/im/doc/zh-cn/tutorial-03-sns.html)。

**修复**

WebSocket 长连接断开时偶现的报错。

### 2.12.2 @2021.8.6

**新增**

小程序视频上传支持进度回调。

**变更**

修改群自定义字段等不存漫游的群提示消息，SDK 不再计入会话未读数。

**修复**

- 加入直播群偶现收不到自己进群的提示消息。
- 使用 restapi 发送 c2c 消息 random 设置为0时，接收端触发2次 [MESSAGE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_RECEIVED) 事件。

### 2.12.1 @2021.7.20

**新增**

- 支持 Meeting 群未读计数。
- [TIM.EVENT.MESSAGE_MODIFIED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_MODIFIED) 事件，第三方回调修改了的消息，SDK 通过此事件通知给消息发送方。

**修复**

- 拉群漫游消息偶发丢消息问题。
- uni-app 集成时可能遇到的`xx.toFixed is not a function`。

### 2.12.0 @2021.7.5

**新增**

- [deleteMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteMessage)，支持删除消息。
- 同步会话列表时支持 `lastMessage` 为被撤回消息的情况。
- [getGroupMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberList) 支持拉取 `joinTime`（入群时间）。

**修复**
被设置 admin 和取消 admin 后群提示消息的 `nick` 错误。

### 2.11.2 @2021.6.16

**新增**

- 支持 WebSocket，[升级指引](https://web.sdk.qcloud.com/im/doc/zh-cn/tutorial-02-upgradeguideline.html)。
- 支持 uni-app 发送图片、视频等文件类消息。

### 2.10.2 @2021.4.27

**新增**

- 创建消息支持设置 `cloudCustomData`（自定义字段），满足更多样的业务需求。
- [createGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createGroup) 或 [addGroupMember](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#addGroupMember) 时，如果有用户超过了“单个用户可加入群的上限”，则通过 `overLimitUserIDList` 通知给接入侧。

**修复**

- 在 [控制台](https://console.cloud.tencent.com/im) 创建音视频聊天室（AVChatRoom）并指定群主，群主加入此群后，调用 [发送系统通知](https://cloud.tencent.com/document/product/269/1630) 的 REST API， 群主侧收到重复的群系统通知。
- [createForwardMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createForwardMessage) 昵称丢失。
- [downloadMergerMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#downloadMergerMessage) 偶现出错。

### 2.10.1 @2021.3.19

**新增**

- [createMergerMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createMergerMessage) 接口，创建合并消息。
- [createForwardMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createForwardMessage) 接口，创建转发消息。
- 多实例或多终端登录，一端上报已读后，Web 端同一个会话未读数同步清零。

**变更**

废弃 MTA 统计。

**修复**

- Web 多实例登录，C2C 会话对端头像和昵称出错。
- 注册发消息后回调并调用 REST API 频繁撤回消息的场景，部分消息未正确撤回。

### 2.9.3 @2021.2.3

**变更**

用户未加入群组（非直播群），[quitGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#quitGroup) 时返回错误码 2623 - 用户不在该群组内。

**修复**

C2C 会话消息列表 `avatar`（头像）或 `nick`（昵称）不一致。

### 2.9.2 @2021.1.26

**新增**

- 收发 C2C 消息带 `avatar`（头像） 和 `nick`（昵称）。
- 支持腾讯云即时通信 IM 上传插件 [tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin)，上传文件更快更安全，支持 Web 和微信、QQ、百度、头条、支付宝小程序平台，体积仅26KB，详细使用请参考 [registerPlugin](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#registerPlugin)。

**修复**

- 登出后匿名加入直播群，长轮询回包错误码70402。
- Taro 3.0+ 集成时浏览器环境判断错误。
- 图片类型和尺寸校验失败时，返回的数据结构异常。

### 2.9.1 @2020.12.23

**修复**

微信开发者工具基础版本库2.14.1引入 [tim-wx-sdk.js](https://www.npmjs.com/package/tim-wx-sdk) 编译报错。

### 2.9.0 @2020.12.15

**新增**

- [createTextAtMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createTextMessage) 接口，支持群聊时 @ 某人或者 @ 所有人。
- [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 增加 `namecard` 属性，用于展示群成员的群名片（简称群昵称）。

### 2.8.5 @2020.11.23

**变更**

[logout](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#logout) 接口在 SDK 未 ready 时可以调用。

**修复**

- 已读回执和已读通知同时存在时 SDK 运行时错误。
- 登出后再次匿名加入直播群失败。
- 群组列表被异常清空。

### 2.8.4 @2020.11.4

**新增**

- 支持微信、QQ、百度、头条、支付宝小程序平台（在百度、头条、支付宝小程序平台上，暂时不支持发送图片、视频、文件等需要上传到 COS 的消息）。
- 支持 MPX、uni-app 第三方框架。

### 2.8.1 @2020.10.29

**新增**

支持发送 bmp 格式的图片。

**变更**

发送方发送在线消息和接收方接收在线消息,都不更新 [会话对象](https://web.sdk.qcloud.com/im/doc/zh-cn/Conversation.html) 的 `unreadCount` 和 `lastMessage`。

**修复**

同步最近联系人列表异常导致 SDK 无法 ready 的问题。

### 2.8.0 @2020.10.20

**新增**

- [getGroupOnlineMemberCount](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupOnlineMemberCount)，支持查询直播群在线人数。
- 发送图片消息接入图片压缩，接入侧根据可根据业务需要展示原图或者缩略图，请查看 [ImagePayload](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.ImagePayload)。

**修复**

Taro 3.x 集成 WebIM 时的兼容性问题。

**变更**

缩减 SDK 体积。[tim-js-sdk](https://www.npmjs.com/package/tim-js-sdk) 体积减小8.5%，[tim-wx-sdk](https://www.npmjs.com/package/tim-wx-sdk) 体积减小15%。

### 2.7.8 @2020.9.24

**新增**

[TIM.create](https://web.sdk.qcloud.com/im/doc/zh-cn/TIM.html#.create) 接口新增 `oversea` 参数，设置为 `true` 时 SDK 使用境外域名，避免被干扰。

**修复**

- SDK 处于 not ready 状态时，调用相关 API 返回值为 `undefined` 的问题。
- 统计相关问题。

### 2.7.7 @2020.8.12

**新增**

[TIM.EVENT.SDK_RELOAD](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.SDK_RELOAD) 事件。

**修复**

- 长时间断网后重新接入网络或者小程序长时间切后台又切回前台，偶现直播群拉不到消息。
- 图片消息 imageFormat 的类型和值，跟实际图片格式不一致。
- Work Public 群昵称错乱问题。

### 2.7.6 @2020.7.9

**修复**

长时间使用直播群（AVChatRoom）偶现拉不到消息。

### 2.7.5 @2020.7.2

**修复**

使用 REST API [创建好友工作群](https://cloud.tencent.com/document/product/269/1615) 并指定群成员，创建成功后群成员发消息失败。

### 2.7.2 @2020.6.30

**修复**

- 偶现 [joinGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#joinGroup) 时 SDK 提示“已在群内”，实际未在群内，导致无法正常收发消息的问题。
- 临时会议群发消息数量统计错误。

### 2.7.0 @2020.6.8

**新增**

支持 C2C 消息已读回执（即对端是否阅读了您发的消息），详细请参考事件 [TIM.EVENT.MESSAGE_READ_BY_PEER](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_READ_BY_PEER)，对端已读的 [消息](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html)，`isPeerRead` 属性值为 `true`。

**修复**

- 加入聊天室(ChatRoom)后新创建的会话没有展示最近一条消息。
- 登录后未加入音视频聊天室（AVChatRoom）却可以向音视频聊天室（AVChatRoom） 发送消息。

### 2.6.6 @2020.5.27

**修复**

- 音视频聊天室（AVChatRoom）偶发消息重复上屏。
- [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 遇到空消息时报错。
- [logout](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#logout) 后再次 [login](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#login)，偶发 [joinGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#joinGroup) 时遇到70001错误。

### 2.6.4 @2020.5.8

**新增**

[sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage) 接口增加发送选项，支持发送在线消息（即不存离线和漫游，AVChatRoom 和 BChatRoom 不允许使用）和配置 [离线推送](https://cloud.tencent.com/document/product/269/3604)。

### 2.6.3 @2020.4.26

**修复**

- [createCustomMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createCustomMessage) 的 payload.data payload.extension 类型传入不正确导致的消息内容丢失问题。
- 单次请求回包多条消息时可能存在的乱序问题。
- 偶发 C2C 会话未读数溢出导致的上报已读后未读计数无法清零。
- 偶发 [TIM.EVENT.ERROR](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.ERROR) event.data.code 和 event.data.undefined 为 undefined。

### 2.6.2 @2020.4.16

**新增**

- [updateGroupProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateGroupProfile) 支持全体禁言和取消全体禁言。
- [getGroupMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberList) 支持拉取群成员禁言截止时间戳（[muteUntil](https://web.sdk.qcloud.com/im/doc/zh-cn/GroupMember.html)）。

**修复**

群最新的消息是群提示消息时导致的未读计数无法清零。

### 2.6.1 @2020.4.8

**修复**

偶发 COS 上传签名失效后未及时更新导致无法上传文件。

### 2.6.0 @2020.3.30

**新增**

- Web 端支持创建发送视频消息 [createVideoMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createVideoMessage)，最大支持发送100MB的视频文件。
- [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 增加 `nick` 和 `avatar` 属性，用于展示音视频聊天室（AVChatRoom）内消息发送者的昵称和头像地址（需提前调用 [updateMyProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateMyProfile) 设置）。
- Web 端多实例登录时，C2C 消息的撤回通知可在各实例同步。
- 调用 [updateGroupProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateGroupProfile) 修改群自定义字段成功后，群成员能收到群提示消息，且能获取到相关内容：[Message.payload.newGroupProfile.groupCustomField](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.GroupTipPayload)。

**变更**

[TIM.EVENT.GROUP_SYSTEM_NOTICE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.GROUP_SYSTEM_NOTICE_RECEIVED) 已废弃，请使用 [MESSAGE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_RECEIVED) 代替。

**修复**

调用 [getGroupList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupList) 接口偶发报错问题。

### 2.5.2 @2020.3.13

**变更**

[searchGroupByID](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#searchGroupByID) 失败时日志级别降为 Warning，并修改提示文案。

**修复**

- 匿名用户（或游客）加入 [TIM.TYPES.GRP_AVCHATROOM](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组失败及统计问题。
- 其它已知问题。

### 2.5.1 @2020.3.5

**变更**

[login](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#login) 成功时的回调对象 `imResponse.data` 新增 `repeatLogin: true` 键值对，用于标识某帐号已登录后重复登录的情况。

**修复**

音视频聊天室（AVChatRoom）接收侧收到的消息优先级与发送侧设置的消息优先级不一致。

### 2.5.0 @2020.2.28

**新增**

- 网络状态变更事件 [TIM.EVENT.NET_STATE_CHANGE](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.NET_STATE_CHANGE)，接入侧可根据此事件做相关的提示和引导。
- 支持在微信小程序插件环境运行。

**变更**
减少优化 [错误码](https://web.sdk.qcloud.com/im/doc/zh-cn/global.html)。

**修复**

- 在 [控制台](https://console.cloud.tencent.com/im) 创建音视频聊天室（AVChatRoom）并指定群主，群主加入此群后，群内其他人发的信息在群主侧重复。
- 在 [控制台](https://console.cloud.tencent.com/im) 或者用 REST API 频繁创建销毁群组，SDK 没有派发 [TIM.EVENT.GROUP_SYSTEM_NOTICE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.GROUP_SYSTEM_NOTICE_RECEIVED) 事件。
- [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 偶发拉不到群消息列表。

### 2.4.2 @2020.2.7

**新增**
群组消息支持设置 [消息优先级](https://cloud.tencent.com/document/product/269/3663#.E7.BE.A4.E6.B6.88.E6.81.AF.E4.BC.98.E5.85.88.E7.BA.A7)，[枚举值](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.MSG_PRIORITY_HIGH)，[使用示例](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createTextMessage)。

### 2.4.1 @2020.1.14

**变更**
匿名用户（或游客）只允许加入 [TIM.TYPES.GRP_AVCHATROOM](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组。

**修复**

- 偶发拉取在线消息缺失。
- 收到 AVChatRoom 的群系统通知未派发 [TIM.EVENT.MESSAGE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_RECEIVED) 事件。
- 部分场景下撤回群聊消息结果不准确。
- 其它已知问题。

### 2.4.0 @2020.1.3

**新增**

- 撤回消息 [revokeMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#revokeMessage)。
- [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 增加 `isRevoked` 属性，值为 `true` 时标识被撤回的消息。
- 消息被撤回的事件通知 [TIM.EVENT.MESSAGE_REVOKED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.MESSAGE_REVOKED)。
- 被踢下线的事件通知 [TIM.EVENT.KICKED_OUT](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.KICKED_OUT) 增加被踢下线类型：[多终端登录被踢](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.KICKED_OUT_MULT_ACCOUNT) 和 [UserSig 失效被踢](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.KICKED_OUT_USERSIG_EXPIRED)。

**变更**

- [createFileMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createFileMessage) 上传文件大小由20M调整为100M。
- [群提示消息](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.GroupTipPayload) 的 `msgMemberInfo` 和 `shutupTime` 即将废弃，请使用 `memberList` 和 `muteTime` 代替。
- 控制台新增 [IM 智能客服入口](https://cloud.tencent.com/act/event/smarty-service?from=im-doc)。

**修复**

- 调用 [off](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#off) 接口无法取消监听事件。
- [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 的 `isRead` 属性值和类型不准确。
- 发送视频消息，视频文件超过最大限制后的错误码和错误信息有误。
- 偶现更新自定义字段后字段内容不准确。
- 登录后加入音视频聊天室类型的群组偶现 [JOIN_STATUS_ALREADY_IN_GROUP](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.JOIN_STATUS_ALREADY_IN_GROUP)。
- core-js 导致的潜在性能问题。

### 2.3.2 @2019.12.18

**变更**
[getUserProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getUserProfile) 和 [updateMyProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateMyProfile) 支持 [自定义资料字段](https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。

**修复**
[getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 获取的组合消息丢失消息。

### 2.3.1 @2019.12.13

**新增**

- [createImageMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createImageMessage) 和 [createFileMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createFileMessage) 接口支持传入 [File](https://developer.mozilla.org/zh-CN/docs/Web/API/File) 对象。
- 创建表情消息接口 [createFaceMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createFaceMessage)。
- 优化 [TIM.TYPES.GRP_AVCHATROOM](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组的消息通知效率，大幅提升使用体验。

**变更**

- 发消息失败时，SDK 返回实际的错误码和错误信息。
- 调用 [logout](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#logout) 时只登出当前实例的消息通道。
- 对接入侧传入的回调函数做安全性封装，如果回调函数逻辑有误，可捕获异常快速定位问题。
- 遇到 [IM 服务端的错误码](https://cloud.tencent.com/document/product/269/1671#.EF.BC.88.E4.BA.8C.EF.BC.89.E6.9C.8D.E5.8A.A1.E7.AB.AF.E7.9A.84.E9.94.99.E8.AF.AF.E7.A0.81) 时 SDK 输出中文错误信息。

**修复**

- 微信小程序环境长时间切后台再切回前台偶现消息丢失。
- 发一次消息触发多次 [TIM.EVENT.CONVERSATION_LIST_UPDATED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.CONVERSATION_LIST_UPDATED)。
- 未调用 [registerPlugin](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#registerPlugin) 或者接口传参有误，上传图片等文件时 SDK 报错。
- 解散 [TIM.TYPES.GRP_AVCHATROOM](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组后长轮询未停止。
- 开启了“多实例”或“多终端”登录，一个 Web 实例登出后其它实例或者其它端收不到消息。
- 偶现的由于拉取的会话列表结构问题导致 SDK 报错。

### 2.2.1 @2019.11.28

**变更**
完善拉群漫游消息的逻辑。

**修复**

- 群主修改音视频聊天室的群资料后 SDK 提示 [2901错误码](https://web.sdk.qcloud.com/im/doc/zh-cn/global.html)。
- 群管理员处理完加群申请，刷新后仍能收到已处理过的申请。

### 2.2.0 @2019.11.21

**新增**

- 小程序支持创建发送视频消息 [createVideoMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createVideoMessage)，视频消息全平台互通（需升级使用最新版本的 [TUIKit 以及 SDK](https://cloud.tencent.com/document/product/269/36887)）。
- 查询群成员资料接口 [getGroupMemberProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberProfile)。
- 兼容 Native IM v3.x 发送的语音、文件消息。
- 支持接收位置消息 [GeoPayload](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.GeoPayload)。

**变更**
最多向本地存储写入100个群组。长度超过100的群组列表不再全量写入。

**修复**

- 登出后 [TIM.TYPES.GRP_AVCHATROOM](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组的长轮询仍在运行。
- [TIM.TYPES.GRP_AVCHATROOM](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组的消息实例中群名片没有值。
- IE10 浏览器下报错。
- 无法匿名加群。

### 2.1.4 @2019.11.7

**变更**

- SDK API 返回的`Promise`状态是`rejected`时，SDK 不再派发 [TIM.EVENT.ERROR](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.ERROR) 事件。
- 自己的 Profile（资料）有更新时，立即写入本地缓存。

**修复**

- Angular 框架的 zone.js 修改原型链导致集成 SDK 出错。
- 群主创建 [TIM.TYPES.GRP_AVCHATROOM](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组并加入，无法收到消息。
- 群组列表过大导致的初始化出错。

### 2.1.3 @2019.10.31

**变更**
兼容 REST API 或 旧版 IM 发送的组合消息（即单条消息中包括多个消息元素），更多详情请参见 [兼容指引](https://web.sdk.qcloud.com/im/doc/zh-cn/tutorial-01-faq.html)。

**修复**

- 未读计数不准。
- 未上报消息已读可能导致的消息乱序。
- 发送空图片消息成功但无法渲染。SDK 不支持发送空图片消息。
- 发送空文件消息，消息状态不对。SDK 不支持发送空文件消息。
- 偶发调用 [getGroupMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberList) 接口 SDK 代码报错。

### 2.1.2 @2019.10.25

**新增**
 [getGroupList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupList) 接口支持拉取群主 ID、群成员数量等群相关的资料。

**修复**

- 使用 REST API 发音视频聊天室的群自定义通知，SDK 代码报错。
- 退群后再进群，调用 getMessageList 接口 SDK 没有发起拉历史消息的请求。
- 上传失败时，SDK 代码报错。

### 2.1.1 @2019.10.18

**新增**
小程序支持 [发送音频消息](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createAudioMessage)，音频消息全平台互通（需升级使用最新版本的 [TUIKit 以及 SDK](https://cloud.tencent.com/document/product/269/36887)）。

**修复**
退出群组后再进群，[getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 仍能拉到退群前的历史消息。

### 2.1.0 @2019.10.16

**新增**

- Web & 小程序支持接收 [音频消息](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.AudioPayload)。
- Web & 小程序支持接收 [视频消息](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.VideoPayload)。

**变更**

- [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 接口单次调用至多拉取15条消息。
- 废弃 [TIM.TYPES.MSG_SOUND](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.MSG_SOUND)，用 [TIM.TYPES.MSG_AUDIO](https://web.sdk.qcloud.com/im/doc/zh-cn/module-TYPES.html#.MSG_AUDIO) 代替。

**修复**

- [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) 接口无法拉取已删除的群聊会话的消息。
- 群系统通知没有群名称。
- 收到消息新建的会话没有资料。

### 2.0.11 @2019.10.12

**修复**
React 框架下发送图片消息失败。

### 2.0.9 @2019.9.19

**新增**
发送图片消息前，探测图片真实宽高。

**变更**

- 默认使用 HTTPS 协议。
- 收到新的群系统通知事件，类型为 [TIM.EVENT.GROUP_SYSTEM_NOTICE_RECEIVED](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.GROUP_SYSTEM_NOTICE_RECEIVED)。

**修复**

- 小程序发图片消息闪屏。
- 发送后缀为 JPG 等类型的图片失败。
