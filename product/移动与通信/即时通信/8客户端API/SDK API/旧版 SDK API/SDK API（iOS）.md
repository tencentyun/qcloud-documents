，同旧版本中的 Private


，同旧版本中的 ChatRoom**新接入的开发者推荐使用 [新版本 API](https://cloud.tencent.com/document/product/269/44499)。**

## TIMManager

IM SDK 主核心模块，负责 IM SDK 的初始化、登录、创建会话以及管理推送等功能。
- 初始化：初始化是使用 IM SDK 的前提，调用 init 接口后，才能调用其它 API。
- 登录：需要设置 SDKAppID，UserID 和 UserSig 才能使用即时通信 IM 服务。
- 会话：一个会话对应一个聊天窗口，例如，与单个好友的 C2C 聊天或者一个聊天群都是一个会话。
- 推送：管理和设置离线推送的相关功能，包括 token 和开关等。

### 初始化相关接口
| API | 描述 |
| --- | --- |
| [sharedInstance](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#sharedinstance) | 获取管理器实例 [TIMManager](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#timmanager)。 |
| [initSdk](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#initsdk) | 初始化 SDK，设置全局配置信息。 |
| [unInit](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#uninit) | 反初始化。 |
| [getGlobalConfig](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getglobalconfig) | 获取全局配置信息。 |
| [setUserConfig](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#setuserconfig) | 设置用户配置信息。 |
| [getUserConfig](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getuserconfig) | 获取用户配置信息。 |
| [addMessageListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#addmessagelistener) | 新增新消息接收监听。 |
| [removeMessageListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#removemessagelistener) | 移除消息监听。 |


### 登录相关接口
| API | 描述 |
| --- | --- |
| [login](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#login) | 登录。 |
| [autoLogin](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#autologin) | 自动登录。 |
| [logout](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#logout) | 登出。 |
| [getLoginUser](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getloginuser) | 获取当前登录的用户。 |
| [getLoginStatus](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getloginstatus) | 获取当前登录状态。 |


### 会话管理器
| API | 描述 |
| --- | --- |
| [getConversationList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getconversationlist) | 获取会话列表。 |
| [getConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getconversation) | 获取单个会话。 |
| [deleteConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#deleteconversation) | 删除单个会话。 |
| [deleteConversationAndMessages](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#deleteconversationandmessages) | 删除单个会话和对应的会话消息。 |


### 设置 APNs 推送
| API | 描述 |
| --- | --- |
| [setToken](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#settoken) | 设置客户端 Token 和证书 busiID。 |
| [setAPNS](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#setapns) | 配置 APNS。 |
| [getAPNSConfig](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getapnsconfig) | 获取 APNS 配置。 |
| [doBackground](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#dobackground) | 上报 App 应用退至后台。 |
| [doForeground](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#doforeground) | 上报 App 应用切换回前台。 |


### 未登录查看本地会话和消息
| API | 描述 |
| --- | --- |
| [initStorage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#initstorage) | 在未登录的情况下加载本地存储。 |


### 调试相关接口
| API | 描述 |
| --- | --- |
| [GetVersion](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getversion) | 获取版本号。 |
| [log](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#log) | 打印日志。 |
| [getLogPath](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getlogpath) | 获取日志文件路径。 |
| [getIsLogPrintEnabled](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getislogprintenabled) | 获取日志打印开启状态。 |
| [getLogLevel](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMManager.html#getloglevel) | 获取日志级别。 |


## TIMConversation

一个会话对应一个聊天窗口，例如，与单个好友的 C2C 聊天或者一个聊天群都是一个会话。
TIMConversation 提供的接口函数都是围绕消息的相关操作，包括发送消息、获取历史消息、设置消息已读设置、撤回和删除等。

### 发消息相关接口
| API | 描述 |
| --- | --- |
| [sendMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#sendmessage) | 发送消息。 |
| [sendOnlineMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#sendonlinemessage) | 发送在线消息（无痕消息）。 |


### 获取消息相关接口
| API | 描述 |
| --- | --- |
| [getMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#getmessage) | 从云端拉取历史消息。 |
| [getLocalMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#getlocalmessage) | 从本地数据库中获取历史消息。 |
| [getLastMsg](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#getlastmsg) | 获取当前会话的最后一条消息。 |


### 设置消息已读
| API | 描述 |
| --- | --- |
| [setReadMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#setreadmessage) | 标记消息为已读状态。 |
| [getUnReadMessageNum](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#getunreadmessagenum) | 获取会话的未读消息计数。 |


### 撤回/删除消息相关接口
| API | 描述 |
| --- | --- |
| [revokeMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#revokemessage) | 撤回一条已发送的消息（消息发送成功后 ）。 |
| [deleteLocalMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#deletelocalmessage) | 删除当前会话的本地历史消息。 |


### 获取会话信息相关接口
| API | 描述 |
| --- | --- |
| [getType](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#gettype) | 获取会话类型。 |
| [getReceiver](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#getreceiver) | 获取会话 ID。 |
| [getGroupName](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#getgroupname) | 获取群名称。 |


### 草稿箱
| API | 描述 |
| --- | --- |
| [setDraft](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#setdraft) | 添加未编辑完的草稿消息。 |
| [getDraft](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#getdraft) | 获取未编辑完的草稿消息。 |


### 导入消息到会话相关接口
| API | 描述 |
| --- | --- |
| [saveMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#savemessage) | 向本地消息列表中添加一条消息，但并不将其发送出去。 |
| [importMessages](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMConversation.html#importmessages) | 将消息导入本地数据库。 |


## TIMGroupManager

群组管理模块负责群组的创建群组、删除群组、邀请群成员、删除群成员、修改群信息和修改群成员信息等功能。

### 获取群组实例
| API | 描述 |
| --- | --- |
| [sharedInstance](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#sharedinstance) | 获取群管理器实例。 |


### 创建/删除/加入/退出群组
| API | 描述 |
| --- | --- |
| [createPrivateGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#createprivategroup) | 创建私有群，同新版本中的 Work。 |
| [createPublicGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#createpublicgroup) | 创建公开群。 |
| [createChatRoomGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#createchatroomgroup) | 创建聊天室，同新版本中的 Meeting。 |
| [createAVChatRoomGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#createavchatroomgroup) | 创建音视频聊天室。 |
| [createGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#creategroup) | 创建指定类型和 ID 的群组。 |
| [createGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#creategroup2) | 创建自定义群组。 |
| [deleteGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#deletegroup) | 解散群组。 |
| [joinGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#joingroup) | 申请加群。 |
| [quitGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#quitgroup) | 主动退出群组。 |


### 邀请/删除群成员
| API | 描述 |
| --- | --- |
| [inviteGroupMember](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#invitegroupmember) | 邀请好友入群。 |
| [deleteGroupMemberWithReason](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#deletegroupmemberwithreason) | 删除群成员。 |


### 获取群信息
| API | 描述 |
| --- | --- |
| [getGroupList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getgrouplist) | 获取群列表。 |
| [getGroupInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getgroupinfo) | 获取服务器存储的群组信息。 |
| [queryGroupInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#querygroupinfo) | 获取本地存储的群组信息。 |
| [getGroupMembers](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getgroupmembers) | 获取群成员列表。 |
| [getGroupSelfInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getgroupselfinfo) | 获取本人在群组内的成员信息。 |
| [getGroupMembersInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getgroupmembersinfo) | 获取群组指定成员的信息。 |
| [getGroupMembers](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getgroupmembers2) | 获取指定类型的成员列表（支持按字段拉取，分页）。 |
| [getReciveMessageOpt](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getrecivemessageopt) | 获取接受消息选项。 |


### 修改群信息
| API | 描述 |
| --- | --- |
| [modifyGroupName](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupname) | 修改群名。 |
| [modifyGroupIntroduction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupintroduction) | 修改群简介。 |
| [modifyGroupNotification](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupnotification) | 修改群公告。 |
| [modifyGroupFaceUrl](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupfaceurl) | 修改群头像。 |
| [modifyGroupAddOpt](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupaddopt) | 修改加群选项。 |
| [modifyGroupSearchable](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupsearchable) | 修改群组是否可被搜索属性。 |
| [modifyReceiveMessageOpt](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifyreceivemessageopt) | 修改接受消息选项。 |
| [modifyGroupAllShutup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupallshutup) | 修改群组全员禁言属性。 |
| [modifyGroupCustomInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupcustominfo) | 修改群自定义字段集合。 |
| [modifyGroupOwner](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupowner) | 转让群给新群主。 |


### 修改群成员信息
| API | 描述 |
| --- | --- |
| [modifyGroupMemberInfoSetNameCard](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupmemberinfosetnamecard) | 修改群成员名片。 |
| [modifyGroupMemberInfoSetRole](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupmemberinfosetrole) | 修改群成员角色。 |
| [modifyGroupMemberVisible](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupmembervisible) | 修改群组成员是否可见属性。 |
| [modifyGroupMemberInfoSetSilence](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupmemberinfosetsilence) | 禁言用户。 |
| [modifyGroupMemberInfoSetCustomInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#modifygroupmemberinfosetcustominfo) | 修改群成员自定义字段集合。 |


### 群未处理请求逻辑
| API | 描述 |
| --- | --- |
| [getPendencyFromServer](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#getpendencyfromserver) | 获取群组未处理请求列表。 |
| [pendencyReport](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMGroupManager.html#pendencyreport) | 上报群未处理列表已读。 |


## TIMFriendshipManager

资料关系链管理模块负责添加好友、删除好友、获取好友相关信息以及修改资料等功能。

| API | 描述 |
| --- | --- |
| [sharedInstance](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#sharedinstance) | 获取好友管理器实例。 |
| [modifySelfProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#modifyselfprofile) | 设置自己的资料。 |
| [getSelfProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#getselfprofile) | 获取自己的资料。 |
| [querySelfProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#queryselfprofile) | 在缓存中查询自己的资料。 |
| [getUsersProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#getusersprofile) | 获取指定用户资料。 |
| [queryUserProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#queryuserprofile) | 在缓存中查询用户的资料。 |
| [getFriendList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#getfriendlist) | 获取好友列表。 |
| [queryFriend](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#queryfriend) | 在缓存中查询用户的关系链数据。 |
| [queryFriendList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#queryfriendlist) | 获取缓存中的关系链列表。 |
| [checkFriends](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#checkfriends) | 检查指定用户的好友关系。 |
| [addFriend](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#addfriend) | 添加好友。 |
| [doResponse](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#doresponse) | 响应对方好友邀请。 |
| [deleteFriends](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#deletefriends) | 删除好友。 |
| [modifyFriend](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#modifyfriend) | 修改好友。 |
| [getPendencyList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#getpendencylist) | 获取未决列表。 |
| [deletePendency](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#deletependency) | 删除未决消息。 |
| [pendencyReport](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#pendencyreport) | 上报未决消息已读。 |
| [getBlackList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#getblacklist) | 获取黑名单列表。 |
| [addBlackList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#addblacklist) | 添加用户到黑名单。 |
| [deleteBlackList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#deleteblacklist) | 从黑名单中删除指定用户。 |
| [createFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#createfriendgroup) | 新建好友分组。 |
| [getFriendGroups](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#getfriendgroups) | 获取指定的好友分组信息。 |
| [deleteFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#deletefriendgroup) | 删除好友分组。 |
| [renameFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#renamefriendgroup) | 修改好友分组的名称。 |
| [addFriendsToFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#addfriendstofriendgroup) | 添加好友至指定好友分组。 |
| [deleteFriendsFromFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMFriendshipManager.html#deletefriendsfromfriendgroup) | 从指定分组中删除指定好友。 |


## TIMMessage

[TIMMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#timmessage) 由多个 [TIMElem](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#timelem) 组成，每个 TIMElem 可以是文本或图片，即每条消息可包含多个文本或图片，详情请参见 [消息收发](https://cloud.tencent.com/document/product/269/9150)。

| API | 描述 |
| --- | --- |
| [addElem](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#addelem) | 增加 Elem。 |
| [getElem](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#getelem) | 获取对应索引的 Elem。 |
| [elemCount](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#elemcount) | 获取 Elem 数量。 |
| [setBusinessCmd](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#setbusinesscmd) | 设置业务命令字。 |
| [status](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#status) | 查询消息状态。 |
| [isSelf](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#isself) | 确认自己是否为发送方。 |
| [sender](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#sender) | 获取消息的发送方。 |
| [msgId](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#msgid) | 获取消息 ID。 |
| [uniqueId](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#uniqueid) | 获取消息 uniqueId。 |
| [timestamp](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#timestamp) | 获取当前消息的时间戳。 |
| [isReaded](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#isreaded) | 确认自己是否已读。 |
| [isPeerReaded](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#ispeerreaded) | 确认对方是否已读（仅 C2C 消息有效）。 |
| [locator](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#locator) | 获取消息定位符。 |
| [respondsToLocator](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#respondstolocator) | 确认是否为 locator 对应的消息。 |
| [remove](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#remove) | 删除消息。 |
| [getConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#getconversation) | 获取会话。 |
| [getSenderProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#getsenderprofile) | 获取发送者资料。 |
| [getSenderGroupMemberProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#getsendergroupmemberprofile) | 获取发送者群内资料。 |
| [setPriority](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#setpriority) | 设置消息的优先级（仅对群组消息有效）。 |
| [getPriority](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#getpriority) | 获取消息的优先级（仅对群组消息有效）。 |
| [setOfflinePushInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#setofflinepushinfo) | 配置消息离线推送相关参数。 |
| [getOfflinePushInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#getofflinepushinfo) | 获取消息离线推送配置。 |
| [setCustomInt](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#setcustomint) | 设置自定义整数，默认为0。 |
| [customInt](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#customint) | 获取 CustomInt。 |
| [setCustomData](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#setcustomdata) | 设置自定义数据，默认为空串`""`。 |
| [customData](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#customdata) | 获取 CustomData。 |
| [copyFrom](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#copyfrom) | 复制消息中的属性（复制对象包括 ELem、priority、online 以及 offlinePushInfo）。 |
| [convertToImportedMsg](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#converttoimportedmsg) | 将消息导入到本地。 |
| [setTime](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#settime) | 设置消息时间戳。 |
| [setSender](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMMessage.html#setsender) | 设置消息发送方。 |




