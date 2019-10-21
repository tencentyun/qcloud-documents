## 更新日志（Web & 小程序）

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
