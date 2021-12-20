腾讯即时通信 IM 的跨平台 C 接口（API）。

**各个平台的下载链接：**

- Windows 平台 [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/Windows)，Windows 快速开始 [集成 IM SDK](https://cloud.tencent.com/document/product/269/33489) 和 [一分钟跑通 Demo](https://cloud.tencent.com/document/product/269/36838)。支持32位/64位系统。
- iOS 平台 [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/iOS/IMSDK)。
- Mac 平台 [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/Mac/IMSDK)。
- Android 平台 [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/Android/IMSDK)。

回调分两种，一种是指调用接口的异步返回，另外一种指后台推送的通知。回调在 IM SDK 内部的逻辑线程触发，跟调用接口的线程可能不是同一线程。
在 Windows 平台，如果调用 [TIMInit](https://cloud.tencent.com/document/product/269/33546#timinit) 接口进行初始化 IM SDK 之前，已创建了 UI 的消息循环，且调用 [TIMInit](https://cloud.tencent.com/document/product/269/33546#timinit) 接口的线程为主 UI 线程，则 IM SDK 内部会将回调抛到主 UI 线程调用。

>!如果接口的参数字符串包含非英文的字符，请使用 UTF-8 编码。



### 事件回调接口

| API | 描述 |
|-----|-----|
| [TIMAddRecvNewMsgCallback](https://cloud.tencent.com/document/product/269/33551#timaddrecvnewmsgcallback) | 增加接收新消息回调 |
| [TIMRemoveRecvNewMsgCallback](https://cloud.tencent.com/document/product/269/33551#timremoverecvnewmsgcallback) | 删除接收新消息回调 |
| [TIMSetMsgReadedReceiptCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgreadedreceiptcallback) | 设置消息已读回执回调 |
| [TIMSetMsgRevokeCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgrevokecallback) | 设置接收的消息被撤回回调 |
| [TIMSetMsgElemUploadProgressCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgelemuploadprogresscallback) | 设置消息内元素相关文件上传进度回调 |
| [TIMSetGroupTipsEventCallback](https://cloud.tencent.com/document/product/269/33551#timsetgrouptipseventcallback) | 设置群组系统消息回调 |
| [TIMSetGroupAttributeChangedCallback](https://cloud.tencent.com/document/product/269/33551#timsetgroupattributechangedcallback) | 设置群组属性变更回调 |
| [TIMSetConvEventCallback](https://cloud.tencent.com/document/product/269/33551#timsetconveventcallback) | 设置会话事件回调 |
| [TIMSetConvTotalUnreadMessageCountChangedCallback](https://cloud.tencent.com/document/product/269/33551#timsetconvtotalunreadmessagecountchangedcallback) | 设置会话未读消息总数变更的回调 |
| [TIMSetNetworkStatusListenerCallback](https://cloud.tencent.com/document/product/269/33551#timsetnetworkstatuslistenercallback) | 设置网络连接状态监听回调 |
| [TIMSetKickedOfflineCallback](https://cloud.tencent.com/document/product/269/33551#timsetkickedofflinecallback) | 设置被踢下线通知回调 |
| [TIMSetUserSigExpiredCallback](https://cloud.tencent.com/document/product/269/33551#timsetusersigexpiredcallback) | 设置票据过期回调 |
| [TIMSetOnAddFriendCallback](https://cloud.tencent.com/document/product/269/33551#timsetonaddfriendcallback) | 设置添加好友的回调 |
| [TIMSetOnDeleteFriendCallback](https://cloud.tencent.com/document/product/269/33551#timsetondeletefriendcallback) | 设置删除好友的回调 |
| [TIMSetUpdateFriendProfileCallback](https://cloud.tencent.com/document/product/269/33551#timsetupdatefriendprofilecallback) | 设置更新好友资料的回调 |
| [TIMSetFriendAddRequestCallback](https://cloud.tencent.com/document/product/269/33551#timsetfriendaddrequestcallback) | 设置好友添加请求的回调 |
| [TIMSetFriendApplicationListDeletedCallback](https://cloud.tencent.com/document/product/269/33551#timsetfriendapplicationlistdeletedcallback) | 设置好友申请被删除的回调 |
| [TIMSetFriendApplicationListReadCallback](https://cloud.tencent.com/document/product/269/33551#timsetfriendapplicationlistreadcallback) | 设置好友申请已读的回调 |
| [TIMSetFriendBlackListAddedCallback](https://cloud.tencent.com/document/product/269/33551#timsetfriendblacklistaddedcallback) | 设置黑名单新增的回调 |
| [TIMSetFriendBlackListDeletedCallback](https://cloud.tencent.com/document/product/269/33551#timsetfriendblacklistdeletedcallback) | 设置黑名单删除的回调 |
| [TIMSetLogCallback](https://cloud.tencent.com/document/product/269/33551#timsetlogcallback) | 设置日志回调 |
| [TIMSetMsgUpdateCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgupdatecallback) | 设置消息在云端被修改后回传回来的消息更新通知回调 |


### IM SDK 初始化相关接口

| API | 描述 |
|-----|-----|
| [TIMInit](https://cloud.tencent.com/document/product/269/33546#timinit) | IM SDK 初始化 |
| [TIMUninit](https://cloud.tencent.com/document/product/269/33546#timuninit) | IM SDK 卸载 |
| [TIMGetSDKVersion](https://cloud.tencent.com/document/product/269/33546#timgetsdkversion) | 获取 IM SDK 版本号 |
| [TIMSetConfig](https://cloud.tencent.com/document/product/269/33546#timsetconfig) | 设置额外的用户配置 |
| [TIMGetServerTime](https://cloud.tencent.com/document/product/269/33546#timgetservertime) | 获取服务器当前时间 |


### 登录登出相关接口

| API | 描述 |
|-----|-----|
| [TIMLogin](https://cloud.tencent.com/document/product/269/33547#timlogin) | 登录 |
| [TIMLogout](https://cloud.tencent.com/document/product/269/33547#timlogout) | 登出 |
| [TIMGetLoginStatus](https://cloud.tencent.com/document/product/269/33547#timgetloginstatus) | 获取登录状态 |
| [TIMGetLoginUserID](https://cloud.tencent.com/document/product/269/33547#timgetloginuserid) | 获取登录用户的 userID |


### 会话相关接口

| API | 描述 |
|-----|-----|
| [TIMConvDelete](https://cloud.tencent.com/document/product/269/33548#timconvdelete) | 删除会话 |
| [TIMConvGetConvList](https://cloud.tencent.com/document/product/269/33548#timconvgetconvlist) | 获取最近联系人的会话列表 |
| [TIMConvGetConvInfo](https://cloud.tencent.com/document/product/269/33548#timconvgetconvinfo) | 查询一组会话列表 |
| [TIMConvSetDraft](https://cloud.tencent.com/document/product/269/33548#timconvsetdraft) | 设置指定会话的草稿 |
| [TIMConvCancelDraft](https://cloud.tencent.com/document/product/269/33548#timconvcanceldraft) | 删除指定会话的草稿 |
| [TIMConvPinConversation](https://cloud.tencent.com/document/product/269/33548#timconvpinconversation) | 设置会话置顶 |
| [TIMConvGetTotalUnreadMessageCount](https://cloud.tencent.com/document/product/269/33548#timconvgettotalunreadmessagecount) | 获取所有会话总的未读消息数 |


### 消息相关接口

| API | 描述 |
|-----|-----|
| [TIMMsgSendMessage](https://cloud.tencent.com/document/product/269/33549#timmsgsendmessage) | 发送新消息 |
| [TIMMsgCancelSend](https://cloud.tencent.com/document/product/269/33549#timmsgcancelsend) | 根据消息 messageID 取消发送中的消息 |
| [TIMMsgFindMessages](https://cloud.tencent.com/document/product/269/33549#timmsgfindmessages) | 根据消息 messageID 查询本地的消息列表 |
| [TIMMsgReportReaded](https://cloud.tencent.com/document/product/269/33549#timmsgreportreaded) | 消息上报已读 |
| [TIMMsgMarkAllMessageAsRead](https://cloud.tencent.com/document/product/269/33549#timmsgmarkallmessageasread) | 标记所有消息为已读（5.8及其以上版本支持） |
| [TIMMsgRevoke](https://cloud.tencent.com/document/product/269/33549#timmsgrevoke) | 消息撤回 |
| [TIMMsgFindByMsgLocatorList](https://cloud.tencent.com/document/product/269/33549#timmsgfindbymsglocatorlist) | 根据消息定位精准查找指定会话的消息 |
| [TIMMsgImportMsgList](https://cloud.tencent.com/document/product/269/33549#timmsgimportmsglist) | 导入消息列表到指定会话 |
| [TIMMsgSaveMsg](https://cloud.tencent.com/document/product/269/33549#timmsgsavemsg) | 保存自定义消息 |
| [TIMMsgGetMsgList](https://cloud.tencent.com/document/product/269/33549#timmsggetmsglist) | 获取指定会话的消息列表 |
| [TIMMsgDelete](https://cloud.tencent.com/document/product/269/33549#timmsgdelete) | 删除指定会话的消息 |
| [TIMMsgListDelete](https://cloud.tencent.com/document/product/269/33549#timmsglistdelete) | 删除指定会话的本地及漫游消息列表 |
| [TIMMsgClearHistoryMessage](https://cloud.tencent.com/document/product/269/33549#timmsgclearhistorymessage) | 清空指定会话的消息 |
| [TIMMsgSetC2CReceiveMessageOpt](https://cloud.tencent.com/document/product/269/33549#timmsgsetc2creceivemessageopt) | 设置针对某个用户的 C2C 消息接收选项（支持批量设置） |
| [TIMMsgGetC2CReceiveMessageOpt](https://cloud.tencent.com/document/product/269/33549#timmsggetc2creceivemessageopt) | 查询针对某个用户的 C2C 消息接收选项 |
| [TIMMsgSetGroupReceiveMessageOpt](https://cloud.tencent.com/document/product/269/33549#timmsgsetgroupreceivemessageopt) | 设置群消息的接收选项 |
| [TIMMsgDownloadElemToPath](https://cloud.tencent.com/document/product/269/33549#timmsgdownloadelemtopath) | 下载消息内元素到指定文件路径（图片、视频、音频、文件） |
| [TIMMsgDownloadMergerMessage](https://cloud.tencent.com/document/product/269/33549#timmsgdownloadmergermessage) | 下载合并消息 |
| [TIMMsgBatchSend](https://cloud.tencent.com/document/product/269/33549#timmsgbatchsend) | 群发消息，该接口不支持向群组发送消息。 |
| [TIMMsgSearchLocalMessages](https://cloud.tencent.com/document/product/269/33549#timmsgsearchlocalmessages) | 搜索本地消息。 |
| [TIMMsgSetLocalCustomData](https://cloud.tencent.com/document/product/269/33549#timmsgsetlocalcustomdata) | 设置消息自定义数据。 |


### 群组相关接口

| API | 描述 |
|-----|-----|
| [TIMGroupCreate](https://cloud.tencent.com/document/product/269/33550#timgroupcreate) | 创建群组 |
| [TIMGroupDelete](https://cloud.tencent.com/document/product/269/33550#timgroupdelete) | 删除（解散）群组 |
| [TIMGroupJoin](https://cloud.tencent.com/document/product/269/33550#timgroupjoin) | 申请加入群组 |
| [TIMGroupQuit](https://cloud.tencent.com/document/product/269/33550#timgroupquit) | 退出群组 |
| [TIMGroupInviteMember](https://cloud.tencent.com/document/product/269/33550#timgroupinvitemember) | 邀请加入群组 |
| [TIMGroupDeleteMember](https://cloud.tencent.com/document/product/269/33550#timgroupdeletemember) | 删除群组成员 |
| [TIMGroupGetJoinedGroupList](https://cloud.tencent.com/document/product/269/33550#timgroupgetjoinedgrouplist) | 获取已加入群组列表 |
| [TIMGroupGetGroupInfoList](https://cloud.tencent.com/document/product/269/33550#timgroupgetgroupinfolist) | 获取群组信息列表 |
| [TIMGroupModifyGroupInfo](https://cloud.tencent.com/document/product/269/33550#timgroupmodifygroupinfo) | 修改群信息 |
| [TIMGroupGetMemberInfoList](https://cloud.tencent.com/document/product/269/33550#timgroupgetmemberinfolist) | 获取群成员信息列表 |
| [TIMGroupModifyMemberInfo](https://cloud.tencent.com/document/product/269/33550#timgroupmodifymemberinfo) | 修改群成员信息 |
| [TIMGroupGetPendencyList](https://cloud.tencent.com/document/product/269/33550#timgroupgetpendencylist) | 获取群未决信息列表。<br/>群未决信息是指还没有处理的操作，例如，邀请加群或者请求加群操作还没有被处理，称之为群未决信息 |
| [TIMGroupReportPendencyReaded](https://cloud.tencent.com/document/product/269/33550#timgroupreportpendencyreaded) | 上报群未决信息已读 |
| [TIMGroupHandlePendency](https://cloud.tencent.com/document/product/269/33550#timgrouphandlependency) | 处理群未决信息 |
| [TIMGroupGetOnlineMemberCount](https://cloud.tencent.com/document/product/269/33550#timgroupgetonlinemembercount) | 获取指定群在线人数 |
| [TIMGroupSearchGroups](https://cloud.tencent.com/document/product/269/33550#timgroupsearchgroups) | 搜索群列表 |
| [TIMGroupSearchGroupMembers](https://cloud.tencent.com/document/product/269/33550#timgroupsearchgroupmembers) | 搜索群成员列表 |
| [TIMGroupInitGroupAttributes](https://cloud.tencent.com/document/product/269/33550#timgroupinitgroupattributes) | 初始化群属性，会清空原有的群属性列表 |
| [TIMGroupSetGroupAttributes](https://cloud.tencent.com/document/product/269/33550#timgroupsetgroupattributes) | 设置群属性，已有该群属性则更新其 value 值，没有该群属性则添加该群属性 |
| [TIMGroupDeleteGroupAttributes](https://cloud.tencent.com/document/product/269/33550#timgroupdeletegroupattributes) | 删除群属性 |
| [TIMGroupGetGroupAttributes](https://cloud.tencent.com/document/product/269/33550#timgroupgetgroupattributes) | 获取群指定属性，keys 传 nil 则获取所有群属性。 |


### 用户资料相关接口

| API | 描述 |
|-----|-----|
| [TIMProfileGetUserProfileList](https://cloud.tencent.com/document/product/269/37661#timprofilegetuserprofilelist) | 获取指定用户列表的个人资料 |
| [TIMProfileModifySelfUserProfile](https://cloud.tencent.com/document/product/269/37661#timprofilemodifyselfuserprofile) | 修改自己的个人资料 |


### 关系链相关接口

| API | 描述 |
|-----|-----|
| [TIMFriendshipGetFriendProfileList](https://cloud.tencent.com/document/product/269/37662#timfriendshipgetfriendprofilelist) | 获取好友列表 |
| [TIMFriendshipAddFriend](https://cloud.tencent.com/document/product/269/37662#timfriendshipaddfriend) | 添加好友 |
| [TIMFriendshipHandleFriendAddRequest](https://cloud.tencent.com/document/product/269/37662#timfriendshiphandlefriendaddrequest) | 处理好友请求 |
| [TIMFriendshipModifyFriendProfile](https://cloud.tencent.com/document/product/269/37662#timfriendshipmodifyfriendprofile) | 更新好友资料（备注等） |
| [TIMFriendshipDeleteFriend](https://cloud.tencent.com/document/product/269/37662#timfriendshipdeletefriend) | 删除好友 |
| [TIMFriendshipCheckFriendType](https://cloud.tencent.com/document/product/269/37662#timfriendshipcheckfriendtype) | 检测好友类型（单向或双向） |
| [TIMFriendshipCreateFriendGroup](https://cloud.tencent.com/document/product/269/37662#timfriendshipcreatefriendgroup) | 创建好友分组 |
| [TIMFriendshipGetFriendGroupList](https://cloud.tencent.com/document/product/269/37662#timfriendshipgetfriendgrouplist) | 获取指定好友分组的分组信息 |
| [TIMFriendshipModifyFriendGroup](https://cloud.tencent.com/document/product/269/37662#timfriendshipmodifyfriendgroup) | 修改好友分组 |
| [TIMFriendshipDeleteFriendGroup](https://cloud.tencent.com/document/product/269/37662#timfriendshipdeletefriendgroup) | 删除好友分组 |
| [TIMFriendshipAddToBlackList](https://cloud.tencent.com/document/product/269/37662#timfriendshipaddtoblacklist) | 添加指定用户到黑名单 |
| [TIMFriendshipGetBlackList](https://cloud.tencent.com/document/product/269/37662#timfriendshipgetblacklist) | 获取黑名单列表 |
| [TIMFriendshipDeleteFromBlackList](https://cloud.tencent.com/document/product/269/37662#timfriendshipdeletefromblacklist) | 从黑名单中删除指定用户列表 |
| [TIMFriendshipGetPendencyList](https://cloud.tencent.com/document/product/269/37662#timfriendshipgetpendencylist) | 获取好友添加请求未决信息列表 |
| [TIMFriendshipDeletePendency](https://cloud.tencent.com/document/product/269/37662#timfriendshipdeletependency) | 删除指定好友添加请求未决信息 |
| [TIMFriendshipReportPendencyReaded](https://cloud.tencent.com/document/product/269/37662#timfriendshipreportpendencyreaded) | 上报好友添加请求未决信息已读 |
| [TIMFriendshipSearchFriends](https://cloud.tencent.com/document/product/269/37662#timfriendshipsearchfriends) | 搜索好友 |
| [TIMFriendshipGetFriendsInfo](https://cloud.tencent.com/document/product/269/37662#timfriendshipgetfriendsinfo) | 获取好友信息 |


### 废弃接口

| API | 描述 |
|-----|-----|
| [TIMConvCreate](https://cloud.tencent.com/document/product/269/37661#timconvcreate) | 创建会话 |
| [TIMMsgSendNewMsg](https://cloud.tencent.com/document/product/269/33549#timmsgsendnewmsg) | 发送新消息（推荐使用 TIMMsgSendMessage 接口） |
