### 2.4.1 @2020.1.14

**变更**
匿名用户（或游客）只允许加入 [TIM.TYPES.GRP_AVCHATROOM](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组。

**修复**
- 偶发拉取在线消息缺失。
- 收到 AVChatRoom 的群系统通知未派发 [TIM.EVENT.MESSAGE_RECEIVED](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED) 事件。
- 部分场景下撤回群聊消息结果不准确。
- 其它已知问题。

### 2.4.0 @2020.1.3
**新增**
- 撤回消息 [revokeMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#revokeMessage)。
- [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html) 增加 `isRevoked` 属性，值为 `true` 时标识被撤回的消息。
- 消息被撤回的事件通知 [TIM.EVENT.MESSAGE_REVOKED](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_REVOKED)。
- 被踢下线的事件通知 [TIM.EVENT.KICKED_OUT](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.KICKED_OUT) 增加被踢下线类型：[多终端登录被踢](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.KICKED_OUT_MULT_ACCOUNT) 和 [UserSig 失效被踢](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.KICKED_OUT_USERSIG_EXPIRED)。

**变更**
- [createFileMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFileMessage) 上传文件大小由20M调整为100M。
- [群提示消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupTipPayload) 的 `msgMemberInfo` 和 `shutupTime` 即将废弃，请使用 `memberList` 和 `muteTime` 代替。
- 控制台新增 [IM 智能客服入口](https://cloud.tencent.com/act/event/smarty-service?from=im-doc)。

**修复**
- 调用 [off](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#off) 接口无法取消监听事件。
- [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html) 的 `isRead` 属性值和类型不准确。
- 发送视频消息，视频文件超过最大限制后的错误码和错误信息有误。
- 偶现更新自定义字段后字段内容不准确。
- 登录后加入音视频聊天室类型的群组偶现 [JOIN_STATUS_ALREADY_IN_GROUP](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.JOIN_STATUS_ALREADY_IN_GROUP)。
- core-js 导致的潜在性能问题。


### 2.3.2 @2019.12.18
**变更**
[getUserProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getUserProfile) 和 [updateMyProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#updateMyProfile) 支持 [自定义资料字段](https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。

**修复**
[getMessageList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMessageList) 获取的组合消息丢失消息。

### 2.3.1 @2019.12.13
**新增**
- [createImageMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createImageMessage) 和 [createFileMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFileMessage) 接口支持传入 [File](https://developer.mozilla.org/zh-CN/docs/Web/API/File) 对象。
- 创建表情消息接口 [createFaceMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFaceMessage)。
- 优化 [TIM.TYPES.GRP_AVCHATROOM](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组的消息通知效率，大幅提升使用体验。

**变更**
- 发消息失败时，SDK 返回实际的错误码和错误信息。
- 调用 [logout](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#logout) 时只登出当前实例的消息通道。
- 对接入侧传入的回调函数做安全性封装，如果回调函数逻辑有误，可捕获异常快速定位问题。
- 遇到 [IM 服务端的错误码](https://cloud.tencent.com/document/product/269/1671#.EF.BC.88.E4.BA.8C.EF.BC.89.E6.9C.8D.E5.8A.A1.E7.AB.AF.E7.9A.84.E9.94.99.E8.AF.AF.E7.A0.81) 时 SDK 输出中文错误信息。

**修复**
- 微信小程序环境长时间切后台再切回前台偶现消息丢失。
- 发一次消息触发多次 [TIM.EVENT.CONVERSATION_LIST_UPDATED](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.CONVERSATION_LIST_UPDATED)。
- 未调用 [registerPlugin](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#registerPlugin) 或者接口传参有误，上传图片等文件时 SDK 报错。
- 解散 [TIM.TYPES.GRP_AVCHATROOM](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组后长轮询未停止。
- 开启了“多实例”或“多终端”登录，一个 Web 实例登出后其它实例或者其它端收不到消息。
- 偶现的由于拉取的会话列表结构问题导致 SDK 报错。

### 2.2.1 @2019.11.28
**变更**
完善拉群漫游消息的逻辑。

**修复**
- 群主修改音视频聊天室的群资料后 SDK 提示 [2901错误码](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html)。
- 群管理员处理完加群申请，刷新后仍能收到已处理过的申请。

### 2.2.0 @2019.11.21
**新增**
- 小程序支持创建发送视频消息 [createVideoMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createVideoMessage)，视频消息全平台互通（需升级使用最新版本的 [TUIKit 以及 SDK](https://cloud.tencent.com/document/product/269/36887)）。
- 查询群成员资料接口 [getGroupMemberProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberProfile)。
- 兼容 Native IM v3.x 发送的语音、文件消息。
- 支持接收位置消息 [GeoPayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GeoPayload)。

**变更**
最多向本地存储写入100个群组。长度超过100的群组列表不再全量写入。
  
**修复**
- 登出后 [TIM.TYPES.GRP_AVCHATROOM](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组的长轮询仍在运行。
- [TIM.TYPES.GRP_AVCHATROOM](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组的消息实例中群名片没有值。
- IE10 浏览器下报错。
- 无法匿名加群。

### 2.1.4 @2019.11.7
**变更**
- SDK API 返回的`Promise`状态是`rejected`时，SDK 不再派发 [TIM.EVENT.ERROR](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.ERROR) 事件。
- 自己的 Profile（资料）有更新时，立即写入本地缓存。

**修复**
- Angular 框架的 zone.js 修改原型链导致集成 SDK 出错。
- 群主创建 [TIM.TYPES.GRP_AVCHATROOM](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.GRP_AVCHATROOM) 类型的群组并加入，无法收到消息。
- 群组列表过大导致的初始化出错。

### 2.1.3 @2019.10.31

**变更**
兼容 REST API 或 旧版 IM 发送的组合消息（即单条消息中包括多个消息元素），更多详情请参见 [兼容指引](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/tutorial-01-faq.html)。

**修复**
- 未读计数不准。
- 未上报消息已读可能导致的消息乱序。
- 发送空图片消息成功但无法渲染。SDK 不支持发送空图片消息。
- 发送空文件消息，消息状态不对。SDK 不支持发送空文件消息。
- 偶发调用 [getGroupMemberList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberList) 接口 SDK 代码报错。

### 2.1.2 @2019.10.25
**新增**
 [getGroupList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupList) 接口支持拉取群主 ID、群成员数量等群相关的资料。

**修复**
- 使用 REST API 发音视频聊天室的群自定义通知，SDK 代码报错。
- 退群后再进群，调用 getMessageList 接口 SDK 没有发起拉历史消息的请求。
- 上传失败时，SDK 代码报错。

### 2.1.1 @2019.10.18
**新增**
小程序支持 [发送音频消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createAudioMessage)，音频消息全平台互通（需升级使用最新版本的 [TUIKit 以及 SDK](https://cloud.tencent.com/document/product/269/36887)）。

**修复**
退出群组后再进群，[getMessageList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMessageList) 仍能拉到退群前的历史消息。

### 2.1.0 @2019.10.16

**新增**
- Web & 小程序支持接收 [音频消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.AudioPayload)。
- Web & 小程序支持接收 [视频消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.VideoPayload)。

**变更**
- [getMessageList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMessageList) 接口单次调用至多拉取15条消息。
- 废弃 [TIM.TYPES.MSG_SOUND](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.MSG_SOUND)，用 [TIM.TYPES.MSG_AUDIO](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html#.MSG_AUDIO) 代替。

**修复**
- [getMessageList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMessageList) 接口无法拉取已删除的群聊会话的消息。
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
- 收到新的群系统通知事件，类型为 [TIM.EVENT.GROUP_SYSTEM_NOTICE_RECEIVED](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.GROUP_SYSTEM_NOTICE_RECEIVED)。

**修复**
- 小程序发图片消息闪屏。
- 发送后缀为 JPG 等类型的图片失败。
