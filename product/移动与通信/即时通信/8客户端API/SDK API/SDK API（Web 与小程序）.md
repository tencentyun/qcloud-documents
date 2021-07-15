<td color="ff0000"> <a href="https://wj.qq.com/s2/8750536/987c"><font color="ec808d">【有奖问卷】7月31日截至！</font>即时通信 IM Web & 小程序端 TUIKit 需求调研，单击立即参与 >></a></td>

以下视频将帮助您快速了解 Web 和小程序端 SDK API：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2298-33477?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## TIM

TIM 是 IM Web SDK 的命名空间，提供了创建 SDK 实例的静态方法 [create()](https://web.sdk.qcloud.com/im/doc/zh-cn//TIM.html#.create) ，以及事件常量 [EVENT](https://web.sdk.qcloud.com/im/doc/zh-cn//module-EVENT.html)，类型常量 [TYPES](https://web.sdk.qcloud.com/im/doc/zh-cn//module-TYPES.html)。

**初始化**

| API | 描述 |
| --- | --- |
| [create](https://web.sdk.qcloud.com/im/doc/zh-cn//TIM.html#.create) | 创建 SDK 实例。 |

## SDK 实例

| 基本概念 | 说明 |
| :--- | :---- |
| Message（消息） | IM SDK 中 [Message](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html) 表示要发送给对方的内容，消息包括若干属性，例如自己是否为发送者，发送人帐号以及消息产生时间等。 |
| Conversation（会话） | IM SDK 中 [Conversation](https://web.sdk.qcloud.com/im/doc/zh-cn/Conversation.html) 分为两种：<li> C2C（Client to Client）会话，表示单聊情况，自己与对方建立的对话。</li><li> GROUP（群）会话，表示群聊情况下群内成员组成的会话。 |
| Profile（资料） | IM SDK 中 [Profile](https://web.sdk.qcloud.com/im/doc/zh-cn/Profile.html) 描述个人的常用基本信息，例如昵称、性别、个性签名以及头像地址等。 |
| Group（群组） | IM SDK 中 [Group](https://web.sdk.qcloud.com/im/doc/zh-cn/Group.html) 表示一个支持多人聊天的通信系统，支持好友工作群、陌生人社交群、临时会议群以及直播群。 |
| GroupMember（群成员） | IM SDK 中 [GroupMember](https://web.sdk.qcloud.com/im/doc/zh-cn/GroupMember.html) 描述群内成员的常用基本信息，例如 ID、昵称、群内身份以及入群时间等。 |
| 群提示消息 | 当有用户被邀请加入群组或被移出群组等事件发生时，群内会产生提示消息，接入侧可以根据实际需求展示给群组用户或忽略。<br/>群提示消息有多种类型，详细描述请参见  [Message.GroupTipPayload](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.GroupTipPayload)。|
| 群系统通知消息 | 当有用户申请加群等事件发生时，管理员会收到申请加群等系统消息。管理员同意或拒绝加群申请，IM SDK 会通过群系统通知消息将申请加群等相应消息发送给接入侧，由接入侧展示给用户。<br/>群系统通知消息有多种类型，详细描述请参见 [Message.GroupSystemNoticePayload](https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.GroupSystemNoticePayload)。  |
| 消息上屏 | 用户单击发送后，事先输入的文字或选择的图片等信息显示在用户电脑屏幕或手机屏幕上的过程。 |

### 登录相关
| API | 描述 |
| --- | --- |
| [login](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#login) | 登录。 |
| [logout](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#logout) | 登出。 |


### 消息
| API | 描述 |
| --- | --- |
| [createTextMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createTextMessage) | 创建文本消息。 |
| [createTextAtMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createTextAtMessage) |创建可以附带 @ 提醒功能的文本消息。 |
| [createImageMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createImageMessage) | 创建图片消息。 |
| [createAudioMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createAudioMessage) | 创建音频消息。 |
| [createVideoMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createVideoMessage) | 创建视频消息。 |
| [createCustomMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createCustomMessage) | 创建自定义消息。 |
| [createFaceMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createFaceMessage) | 创建表情消息。 |
| [createFileMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createFileMessage) | 创建文件消息。 |
| [createMergerMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createMergerMessage) | 创建合并消息。 |
| [downloadMergerMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#downloadMergerMessage) | 下载合并消息。 |
| [sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage) | 发送消息。 |
| [revokeMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#revokeMessage) | 撤回消息。 |
| [resendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#resendMessage) | 重发消息。 |
| [deleteMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteMessage) | 删除消息。 |

### 会话
| API | 描述 |
| --- | --- |
| [getMessageList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMessageList) | 获取消息列表。  |
| [setMessageRead](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setMessageRead) | 设置消息已读。  |
| [getConversationList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getConversationList) | 获取会话列表。 |
| [getConversationProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getConversationProfile) | 获取会话资料。 |
| [deleteConversation](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteConversation) | 删除会话。 |

### 资料
| API | 描述 |
| --- | --- |
| [getMyProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMyProfile) | 获取个人资料。 |
| [getUserProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getUserProfile) | 获取其他用户资料。 |
| [updateMyProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateMyProfile) | 更新个人资料。 |
| [getBlacklist](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getBlacklist) | 获取我的黑名单列表。 |
| [addToBlacklist](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#addToBlacklist) | 添加用户到黑名单列表。 |
| [removeFromBlacklist](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#removeFromBlacklist) | 将用户从黑名单中移除。 |

### 群组
| API | 描述 |
| --- | --- |
| [getGroupList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupList) | 获取群组列表。 |
| [getGroupProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupProfile) | 获取群详细资料。 |
| [createGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createGroup) | 创建群组。 |
| [dismissGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#dismissGroup) | 解散群组。 |
| [updateGroupProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateGroupProfile) | 修改群组资料。 |
| [joinGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#joinGroup) | 申请加群。 |
| [quitGroup](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#quitGroup) | 退出群组。 |
| [searchGroupByID](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#searchGroupByID) | 搜索群组。 |
| [getGroupOnlineMemberCount](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupOnlineMemberCount) | 获取直播群在线人数。 |
| [changeGroupOwner](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#changeGroupOwner) | 转让群组。 |
| [handleGroupApplication](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#handleGroupApplication) | 处理申请加群。 |

### 群成员
| API | 描述 |
| --- | --- |
| [getGroupMemberList](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberList) | 获取群成员列表。 |
| [getGroupMemberProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getGroupMemberProfile) | 获取群成员资料。 |
| [addGroupMember](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#addGroupMember) | 添加群成员。 |
| [deleteGroupMember](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#deleteGroupMember) | 删除群成员。 |
| [setGroupMemberMuteTime](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setGroupMemberMuteTime) |设置群成员的禁言时间。|
| [setGroupMemberRole](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setGroupMemberRole) | 修改群成员角色。 |
| [setGroupMemberNameCard](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setGroupMemberNameCard) | 设置群成员名片。 |
| [setGroupMemberCustomField](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setGroupMemberCustomField) | 设置群成员自定义字段。 |
| [setMessageRemindType](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setMessageRemindType) | 设置群消息提示类型。 |

### 其他
| API | 描述 |
| --- | --- |
| [on](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#on) | 监听事件。 |
| [off](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#off) | 取消监听事件。 |
| [registerPlugin](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#registerPlugin) | 注册插件。 |
| [setLogLevel](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setLogLevel) | 设置日志级别。 |



