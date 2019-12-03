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
