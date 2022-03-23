**新接入的开发者推荐使用 [新版本 API](https://cloud.tencent.com/document/product/269/44498)。**

以下视频将帮助您快速了解即时通信 IM 的旧版 Android SDK API：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2624-51217?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## TIMManager

IM SDK 主核心模块，负责 IM SDK 的初始化、登录、创建会话以及管理推送等功能。
- 初始化：初始化是使用 IM SDK 的前提，调用 init 接口后，才能调用其它 API。
- 登录：需要设置 SDKAppID，UserID 和 UserSig 才能使用即时通信 IM 服务。
- 会话：一个会话对应一个聊天窗口，例如，与单个好友的 C2C 聊天或者一个聊天群都是一个会话。
- 推送：管理和设置离线推送的相关功能，包括 token 和开关等。

### 初始化相关接口
| API | 描述 |
| --- | --- |
| [getInstance](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getinstance) | 获取管理器实例 [TIMManager](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#timmanager)。 |
| [init](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#init) | 初始化 SDK，设置全局配置信息。 |
| [unInit](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#uninit) | 反初始化。 |
| [getSdkConfig](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getsdkconfig) | 获取全局配置信息。 |
| [setUserConfig](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#setuserconfig) | 设置用户配置信息。 |
| [getUserConfig](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getuserconfig) | 获取用户配置信息。 |
| [addMessageListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#addmessagelistener) | 新增新消息接收监听。 |
| [removeMessageListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#removemessagelistener) | 移除消息监听。 |
| [isInited](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#isinited) | 确认是否已经初始化。 |


### 登录相关接口
| API | 描述 |
| --- | --- |
| [login](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#login) | 登录。 |
| [autoLogin](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#autologin) | 自动登录。 |
| [logout](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#logout) | 登出。 |
| [getLoginUser](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getloginuser) | 获取当前登录的用户。 |
| [getLoginStatus](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getLoginStatus) | 获取当前登录状态。 |


### 会话管理器
| API | 描述 |
| --- | --- |
| [getConversationList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getconversationlist) | 获取会话列表。 |
| [getConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getconversation) | 获取单个会话。 |
| [deleteConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#deleteconversation) | 删除单个会话。 |
| [deleteConversationAndLocalMsgs](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#deleteconversationandlocalmsgs) | 删除单个会话和对应的会话消息。 |


### 设置离线推送
| API | 描述 |
| --- | --- |
| [setOfflinePushToken](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#setofflinepushtoken) | 设置客户端 token 和证书 busiID。 |
| [setOfflinePushSettings](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#setofflinepushsettings) | 初始化离线推送配置，需登录后设置才生效。 |
| [getOfflinePushSettings](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getofflinepushsettings) | 获取离线推送配置，需登录后才能获取。 |
| [setOfflinePushListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#setofflinepushlistener) | 设置 App 在后台时的消息通知监听器（已废弃）。 |
| [doBackground](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#dobackground) | 上报 App 应用退至后台。 |
| [doForeground](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#doforeground) | 上报 App 应用切换回前台。 |


### 未登录查看本地会话和消息
| API | 描述 |
| --- | --- |
| [initStorage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#initstorage) | 在未登录的情况下加载本地存储。 |


### 调试相关接口
| API | 描述 |
| --- | --- |
| [getVersion](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getversion) | 获取版本号。 |
| [addMessageUpdateListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#addmessageupdatelistener) | 添加一个消息更新监听器，以便监听消息变更。 |
| [removeMessageUpdateListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#removemessageupdatelistener) | 删除一个消息更新监听器。 |
| [getNetworkStatus](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getnetworkstatus) | 获取网络连接状态。 |
| [getServerTimeDiff](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMManager.html#getservertimediff) | 获取服务器与本地的时间差，单位为秒，`时间差值 = svrTime - localTime`。 |


## TIMConversation

一个会话对应一个聊天窗口，例如，与单个好友的 C2C 聊天或者一个聊天群都是一个会话。
[TIMConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#timconversation) 提供的接口函数都是围绕消息的相关操作，包括发送消息、获取历史消息、设置消息已读、撤回消息和删除消息等。

### 发消息相关接口
| API | 描述 |
| --- | --- |
| [sendMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#sendmessage) | 发送消息。 |
| [sendOnlineMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#sendonlinemessage) | 发送在线消息（无痕消息）。 |


### 获取消息相关接口
| API | 描述 |
| --- | --- |
| [getMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#getmessage) | 从云端拉取历史消息。 |
| [getLocalMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#getlocalmessage) | 从本地数据库中获取历史消息。 |
| [getLastMsg](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#getlastmsg) | 获取当前会话的最后一条消息。 |


### 设置消息已读
| API | 描述 |
| --- | --- |
| [setReadMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#setreadmessage) | 标记消息为已读状态。 |
| [getUnreadMessageNum](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#getunreadmessagenum) | 获取会话的未读消息计数。 |


### 撤回/删除消息相关接口
| API | 描述 |
| --- | --- |
| [revokeMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#revokemessage) | 撤回一条已发送的消息（消息发送成功后）。 |
| [deleteLocalMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#deletelocalmessage) | 删除当前会话的本地历史消息。 |


### 获取会话信息相关接口
| API | 描述 |
| --- | --- |
| [getType](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#gettype) | 获取会话类型。 |
| [getPeer](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#getpeer) | 获取会话 ID。 |
| [getGroupName](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#getgroupname) | 获取群名称。 |


### 草稿箱
| API | 描述 |
| --- | --- |
| [setDraft](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#setdraft) | 添加未编辑完的草稿消息。 |
| [getDraft](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#getdraft) | 获取未编辑完的草稿消息。 |
| [hasDraft](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#hasdraft) | 确认当前会话是否存在草稿。 |


### 导入消息到会话相关接口
| API | 描述 |
| --- | --- |
| [saveMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#savemessage) | 向本地消息列表中添加一条消息，但并不将其发送出去。 |
| [importMsg](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#importmsg) | 将消息导入本地数据库。 |
| [findMessages](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMConversation.html#findmessages) | 根据提供的消息定位符查找相应消息。 |


## TIMGroupManager

群组管理模块负责群组的创建群组、删除群组、邀请群成员、删除群成员、修改群信息和修改群成员信息等功能。

### 获取群组实例
| API | 描述 |
| --- | --- |
| [getInstance](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getinstance) | 获取群管理器实例。 |


### 创建/删除/加入/退出群组
| API | 描述 |
| --- | --- |
| [createGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#creategroup) | 创建群组。 |
| [deleteGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#deletegroup) | 解散群组。 |
| [applyJoinGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#applyjoingroup) | 申请加群。 |
| [quitGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#quitgroup) | 主动退出群组。 |


### 邀请/删除群成员
| API | 描述 |
| --- | --- |
| [inviteGroupMember](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#invitegroupmember) | 邀请好友入群。 |
| [deleteGroupMember](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#deletegroupmember) | 删除群成员。 |


### 获取群信息
| API | 描述 |
| --- | --- |
| [getGroupList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getgrouplist) | 获取群列表。 |
| [getGroupInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getgroupinfo) | 获取服务器存储的群组信息。 |
| [queryGroupInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#querygroupinfo) | 获取本地存储的群组信息。 |
| [getGroupMembers](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getgroupmembers) | 获取群成员列表。 |
| [getSelfInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getselfinfo) | 获取本人在群组内的成员信息。 |
| [getGroupMembersInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getgroupmembersinfo) | 获取群组指定成员的信息。 |
| [getGroupMembersByFilter](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getgroupmembersbyfilter) | 获取指定类型的成员列表（支持按字段拉取，分页）。 |


### 修改群信息
| API | 描述 |
| --- | --- |
| [modifyGroupInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#modifygroupinfo) | 修改群组基本信息。 |
| [modifyGroupOwner](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#modifygroupowner) | 转让群给新群主。 |


### 修改群成员信息
| API | 描述 |
| --- | --- |
| [modifyMemberInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#modifymemberinfo) | 修改群成员资料。 |


### 群未处理请求逻辑
| API | 描述 |
| --- | --- |
| [getGroupPendencyList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#getgrouppendencylist) | 获取群组未处理请求列表。 |
| [reportGroupPendency](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMGroupManager.html#reportgrouppendency) | 上报群未处理列表已读。 |


## TIMFriendshipManager

资料关系链管理模块负责添加好友、删除好友、获取好友相关信息以及修改资料等功能。

| API | 描述 |
| --- | --- |
| [getInstance](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getinstance) | 获取好友管理器实例。 |
| [init](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#init) | 初始化 TIMFriendshipManager。 |
| [getUsersProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getusersprofile) | 获取指定用户资料。 |
| [getSelfProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getselfprofile) | 获取自己资料。 |
| [querySelfProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#queryselfprofile) | 获取本地自己的资料，没有则返回 null。 |
| [queryUserProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#queryuserprofile) | 获取本地用户资料，没有则返回 null。 |
| [modifySelfProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#modifyselfprofile) | 修改自己的资料。 |
| [getFriendList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getfriendlist) | 获取好友列表。 |
| [queryFriendList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#queryfriendlist) | 获取缓存中的关系链列表，缓存数据来自前一次调用  [getFriendList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getfriendlist) 的返回结果，请确保已调用过 getFriendList。 |
| [queryFriend](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#queryfriend) | 在缓存中查询用户的关系链数据，缓存数据来自前一次调用  [getFriendList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getfriendlist) 的返回结果，请确保已调用过 getFriendList。 |
| [addFriend](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#addfriend) | 添加好友。 |
| [deleteFriends](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#deletefriends) | 删除好友。 |
| [modifyFriend](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#modifyfriend) | 修改好友资料。 |
| [doResponse](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#doresponse) | 处理好友请求。 |
| [createFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#createfriendgroup) | 新建好友分组。 |
| [getFriendGroups](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getfriendgroups) | 获取指定的好友分组，传入 null 时表示获得所有分组信息。 |
| [deleteFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#deletefriendgroup) | 删除好友分组。 |
| [renameFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#renamefriendgroup) | 重命名好友分组。 |
| [addFriendsToFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#addfriendstofriendgroup) | 添加好友至指定分组。 |
| [deleteFriendsFromFriendGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#deletefriendsfromfriendgroup) | 从指定分组中删除指定好友。 |
| [getPendencyList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getpendencylist) | 获取未决列表。 |
| [deletePendency](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#deletependency) | 删除未决消息。 |
| [pendencyReport](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#pendencyreport) | 上报未决消息已读。 |
| [getBlackList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#getblacklist) | 获取黑名单列表。 |
| [addBlackList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#addblacklist) | 添加用户到黑名单。 |
| [deleteBlackList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#deleteblacklist) |从黑名单中删除指定用户。 |
| [checkFriends](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMFriendshipManager.html#checkfriends) | 检查指定用户的好友关系。 |


## TIMMessage

[TIMMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#timmessage) 由多个消息元素（TIMElem）组成，每个 TIMElem 都可以是文本或图片，即每条消息可包含多个文本或图片。详情请参见 [消息收发](https://cloud.tencent.com/document/product/269/9232)。

| API | 描述 |
| --- | --- |
| [addElement](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#addelement) | 增加消息元素。 |
| [getElement](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getelement) | 获取对应索引的 Elem。 |
| [getElementCount](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getelementcount) | 获取 Elem 数量。 |
| [status](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#status) | 查询消息状态。 |
| [isSelf](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#isself) | 确认自己是否为发送方。 |
| [getSender](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getsender) | 获取消息的发送方。 |
| [getSenderNickname](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getsender) | 获取消息的发送方昵称。 |
| [getSenderFaceUrl](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getsender) | 获取消息的发送方头像 URL。 |
| [getMsgId](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getmsgid) | 获取消息 ID。 |
| [getMsgUniqueId](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getmsguniqueid) | 获取消息 uniqueId。 |
| [timestamp](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#timestamp) | 获取当前消息的时间戳。 |
| [isRead](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#isread) | 确认自己是否已读。 |
| [isPeerReaded](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#ispeerreaded) | 确认对方是否已读（仅 C2C 消息有效）。 |
| [getMessageLocator](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getmessagelocator) | 获取消息定位符。 |
| [checkEquals](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#checkequals) | 确认是否为 locator 对应的消息。 |
| [remove](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#remove) | 删除消息。 |
| [getConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getconversation) | 获取会话。 |
| [getSenderProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getsenderprofile) | 获取发送者资料。 |
| [getSenderGroupMemberProfile](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getsendergroupmemberprofile) | 获取发送者群内资料。 |
| [setPriority](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#setpriority) | 设置消息的优先级（仅对群组消息有效）。 |
| [getPriority](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getpriority) | 获取消息的优先级（仅对群组消息有效）。 |
| [setOfflinePushSettings](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#setofflinepushsettings) | 配置消息离线推送相关参数。 |
| [getOfflinePushSettings](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getofflinepushsettings) | 获取消息离线推送配置。 |
| [setCustomInt](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#setcustomint) | 设置自定义整数， 默认为0（此属性仅本地使用）。 |
| [getCustomInt](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getcustomint) | 获取自定义整数。 |
| [setCustomStr](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#setcustomstr) | 设置自定义数据内容，默认为空串`""`（此属性仅本地使用）。 |
| [getCustomStr](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getcustomstr) | 获取自定义数据内容的值。 |
| [copyFrom](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#copyfrom) | 复制消息内容到当前消息（复制对象包括 Elem、priority、online 以及 offlinePushInfo 等）。 |
| [convertToImportedMsg](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#converttoimportedmsg) | 将消息导入到本地。 |
| [setTimestamp](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#settimestamp) | 设置消息时间。 |
| [setSender](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#setsender) | 设置消息发送方 ID。 |
| [getRecvFlag](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getrecvflag) | 获取消息通知类型。 |
| [getRand](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getrand) | 获取当前消息的随机码。 |
| [getSeq](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/ImSDK/com/tencent/imsdk/TIMMessage.html#getseq) | 获取当前消息的序列号。 |





