TIM 是 IM Web SDK 的命名空间，提供了创建 SDK 实例的静态方法 create() ，以及事件常量 [EVENT](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html)，类型常量 [TYPES](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html)

## IM SDK 基本概念

| 基本概念 | 说明 |
| :--- | :---- |
| Message（消息） | IM SDK 中 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html) 表示要发送给对方的内容，消息包括若干属性，例如自己是否为发送者，发送人帐号以及消息产生时间等。 |
| Conversation（会话） | IM SDK 中 [Conversation](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Conversation.html) 分为两种：<li> C2C（Client to Client）会话，表示单聊情况，自己与对方建立的对话。</li><li> GROUP（群）会话，表示群聊情况下群内成员组成的会话。 |
| Profile（资料） | IM SDK 中 [Profile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Profile.html) 描述个人的常用基本信息，例如昵称、头像地址、个性签名以及性别等。 |
| Group（群组） | IM SDK 中 [Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html) 表示一个支持多人聊天的通信系统，支持私有群、公开群、聊天室以及音视频聊天室。 |
| GroupMember（群成员） | IM SDK 中 [GroupMember](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/GroupMember.html) 描述群内成员的常用基本信息，例如 ID、昵称、群内身份以及入群时间等。 |
| 群提示消息 | 当有用户被邀请加入群组或被移出群组等事件发生时，群内会产生提示消息，接入侧可以根据实际需求展示给群组用户或忽略。<br/>群提示消息有多种类型，详细描述请参见  [Message.GroupTipPayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupTipPayload)。|
| 群系统通知消息 | 当有用户申请加群等事件发生时，管理员会收到申请加群等系统消息。管理员同意或拒绝加群申请，IM SDK 会通过群系统通知消息将申请加群等相应消息发送给接入侧，由接入侧展示给用户。<br/>群系统通知消息有多种类型，详细描述请参见 [Message.GroupSystemNoticePayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupSystemNoticePayload)。  |
| 消息上屏 | 用户单击发送后，事先输入的文字或选择的图片等信息显示在用户电脑屏幕或手机屏幕上的过程。 |


## 支持的平台
IM SDK 支持 IE 9+、Chrome、微信、手机 QQ、QQ 浏览器、FireFox、Opera 和 Safari。

## 调用顺序介绍
IM SDK 调用 API 需要遵循如下表所示顺序。

| 操作类型 | 值 | 含义 |
| :--- | :---- | :---- |
| 创建 SDK 实例 | TIM.create(options) | 通过 TIM 工厂函数创建 SDK 实例（通常用 tim 表示）。 |
| 设置日志级别 | tim.setLogLevel(level) | 设置日志级别，低于 level 的日志将不会输出。 |
| 注册插件 | tim.registerPlugin(optoins) | 注册上传图片、文件等需要用到 [对象存储服务 COS](https://cloud.tencent.com/document/product/436/6474) 作为 IM SDK 的上传插件。 |
| 监听事件 | tim.on(event, handler) | 监听事件，在 handler 里处理 SDK 抛出来的数据。 |
| 登录 | tim.login(options) | 登录成功，SDK 状态为 ready 后，可收发消息。 |
| 创建文本消息 | tim.createTextMessage(options) | 创建文本消息。此接口返回一个消息实例，接入侧可将此消息做立即上屏处理。 |
| 发送消息 | tim.sendMessage(message) | 发送创建好的消息实例。 |
| 获取会话列表 | tim.getConversationList() | 获取会话列表，接入侧可处理会话列表数据，渲染会话列表界面。 |
| 获取群组列表 | tim.getGroupList() | 获取群组列表，接入侧可处理群组列表数据，渲染群组列表界面。 |
| 获取黑名单列表 | tim.getBlacklist() | 获取黑名单列表，接入侧可处理黑名单列表数据，渲染黑名单列表界面。 |
| 获取个人资料 | tim.getMyProfile() | 获取个人资料，接入侧可处理个人资料数据，渲染个人资料界面。|
| 登出 | tim.logout() | 退出登录。 |