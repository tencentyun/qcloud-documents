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

[TIM.create](https://web.sdk.qcloud.com/im/doc/zh-cn/TIM.html#.create) 接口新增 `oversea` 参数，设置为 `true` 时 SDK 使用海外域名，避免被干扰。

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
