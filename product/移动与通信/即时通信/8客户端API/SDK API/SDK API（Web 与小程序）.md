
以下视频将帮助您快速了解 Web 和小程序端 SDK API：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2298-33477?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## TIM

TIM 是 IM Web SDK 的命名空间，提供了创建 SDK 实例的静态方法 [create()](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/TIM.html#.create) ，以及事件常量 [EVENT](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html)，类型常量 [TYPES](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-TYPES.html)。

**初始化**

| API | 描述 |
| --- | --- |
| [create](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/TIM.html#.create) | 创建 SDK 实例。 |

## SDK 实例

| 基本概念 | 说明 |
| :--- | :---- |
| Message（消息） | IM SDK 中 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html) 表示要发送给对方的内容，消息包括若干属性，例如自己是否为发送者，发送人帐号以及消息产生时间等。 |
| Conversation（会话） | IM SDK 中 [Conversation](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Conversation.html) 分为两种：<li> C2C（Client to Client）会话，表示单聊情况，自己与对方建立的对话。</li><li> GROUP（群）会话，表示群聊情况下群内成员组成的会话。 |
| Profile（资料） | IM SDK 中 [Profile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Profile.html) 描述个人的常用基本信息，例如昵称、性别、个性签名以及头像地址等。 |
| Group（群组） | IM SDK 中 [Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html) 表示一个支持多人聊天的通信系统，支持好友工作群、陌生人社交群、临时会议群以及直播群。 |
| GroupMember（群成员） | IM SDK 中 [GroupMember](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/GroupMember.html) 描述群内成员的常用基本信息，例如 ID、昵称、群内身份以及入群时间等。 |
| 群提示消息 | 当有用户被邀请加入群组或被移出群组等事件发生时，群内会产生提示消息，接入侧可以根据实际需求展示给群组用户或忽略。<br/>群提示消息有多种类型，详细描述请参见  [Message.GroupTipPayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupTipPayload)。|
| 群系统通知消息 | 当有用户申请加群等事件发生时，管理员会收到申请加群等系统消息。管理员同意或拒绝加群申请，IM SDK 会通过群系统通知消息将申请加群等相应消息发送给接入侧，由接入侧展示给用户。<br/>群系统通知消息有多种类型，详细描述请参见 [Message.GroupSystemNoticePayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupSystemNoticePayload)。  |
| 消息上屏 | 用户单击发送后，事先输入的文字或选择的图片等信息显示在用户电脑屏幕或手机屏幕上的过程。 |

### 登录相关
| API | 描述 |
| --- | --- |
| [login](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#login) | 登录。 |
| [logout](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#logout) | 登出。 |


### 消息
| API | 描述 |
| --- | --- |
| [createTextMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createTextMessage) | 创建文本消息。 |
| [createImageMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createImageMessage) | 创建图片消息。 |
| [createAudioMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createAudioMessage) | 创建音频消息。 |
| [createVideoMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createVideoMessage) | 创建视频消息。 |
| [createCustomMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createCustomMessage) | 创建自定义消息。 |
| [createFaceMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFaceMessage) | 创建表情消息。 |
| [createFileMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFileMessage) | 创建文件消息。 |
| [sendMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) | 发送消息。 |
| [revokeMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#revokeMessage) | 撤回消息。 |
| [resendMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#resendMessage) | 重发消息。 |
| [getMessageList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMessageList) | 获取消息列表。  |
| [setMessageRead](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setMessageRead) | 设置消息已读。  |

### 会话
| API | 描述 |
| --- | --- |
| [getConversationList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getConversationList) | 获取会话列表。 |
| [getConversationProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getConversationProfile) | 获取会话资料。 |
| [deleteConversation](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#deleteConversation) | 删除会话。 |

### 资料
| API | 描述 |
| --- | --- |
| [getMyProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMyProfile) | 获取个人资料。 |
| [getUserProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getUserProfile) | 获取其他用户资料。 |
| [updateMyProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#updateMyProfile) | 更新个人资料。 |
| [getBlacklist](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getBlacklist) | 获取我的黑名单列表。 |
| [addToBlacklist](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#addToBlacklist) | 添加用户到黑名单列表。 |
| [removeFromBlacklist](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#removeFromBlacklist) | 将用户从黑名单中移除。 |

### 群组
| API | 描述 |
| --- | --- |
| [getGroupList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupList) | 获取群组列表。 |
| [getGroupProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupProfile) | 获取群详细资料。 |
| [createGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createGroup) | 创建群组。 |
| [dismissGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#dismissGroup) | 解散群组。 |
| [updateGroupProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#updateGroupProfile) | 修改群组资料。 |
| [joinGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#joinGroup) | 申请加群。 |
| [quitGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#quitGroup) | 退出群组。 |
| [searchGroupByID](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#searchGroupByID) | 搜索群组。 |
| [changeGroupOwner](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#changeGroupOwner) | 转让群组。 |
| [handleGroupApplication](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#handleGroupApplication) | 处理申请加群。 |
| [setMessageRemindType](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setMessageRemindType) | 设置群消息提示类型。 |

### 群成员
| API | 描述 |
| --- | --- |
| [getGroupMemberList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberList) | 获取群成员列表。 |
| [getGroupMemberProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberProfile) | 获取群成员资料。 |
| [addGroupMember](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#addGroupMember) | 添加群成员。 |
| [deleteGroupMember](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#deleteGroupMember) | 删除群成员。 |
| [setGroupMemberMuteTime](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setGroupMemberMuteTime) |设置群成员的禁言时间。|
| [setGroupMemberRole](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setGroupMemberRole) | 修改群成员角色。 |
| [setGroupMemberNameCard](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setGroupMemberNameCard) | 设置群成员名片。 |
| [setGroupMemberCustomField](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setGroupMemberCustomField) | 设置群成员自定义字段。 |

### 其他
| API | 描述 |
| --- | --- |
| [on](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#on) | 监听事件。 |
| [off](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#off) | 取消监听事件。 |
| [registerPlugin](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#registerPlugin) | 注册插件。 |
| [setLogLevel](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setLogLevel) | 设置日志级别。 |

