
## TIMCloud

腾讯云通信的跨平台C接口(API)

**IM SDK 下载链接**

>windows平台  [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/Windows)。
>windows快速开始  [集成SDK](https://cloud.tencent.com/document/product/269/33489)  和  [跑通demo](https://cloud.tencent.com/document/product/269/33488)。

### 注册SDK回调

| API | 描述 | 
|-----|-----| 
| [TIMSetRecvNewMsgCallback](url_for_cb_api#TIMSetRecvNewMsgCallback) | 设置接收新消息回调。 | 
| [TIMSetMsgReadedReceiptCallback](url_for_cb_api#TIMSetMsgReadedReceiptCallback) | 设置消息已读回执回调。 | 
| [TIMSetMsgRevokeCallback](url_for_cb_api#TIMSetMsgRevokeCallback) | 设置接收的消息被撤回回调。 | 
| [TIMSetMsgElemUploadProgressCallback](url_for_cb_api#TIMSetMsgElemUploadProgressCallback) | 设置消息内元素相关文件上传进度回调。 | 
| [TIMSetGroupTipsEventCallback](url_for_cb_api#TIMSetGroupTipsEventCallback) | 设置群组系统消息回调。 | 
| [TIMSetConvEventCallback](url_for_cb_api#TIMSetConvEventCallback) | 设置会话事件回调。 | 
| [TIMSetNetworkStatusListenerCallback](url_for_cb_api#TIMSetNetworkStatusListenerCallback) | 设置网络连接状态监听回调。 | 
| [TIMSetKickedOfflineCallback](url_for_cb_api#TIMSetKickedOfflineCallback) | 设置被踢下线通知回调。 | 
| [TIMSetUserSigExpiredCallback](url_for_cb_api#TIMSetUserSigExpiredCallback) | 设置票据过期回调。 | 
| [TIMSetLogCallback](url_for_cb_api#TIMSetLogCallback) | 设置日志回调。 | 
| [TIMSetMsgUpdateCallback](url_for_cb_api#TIMSetMsgUpdateCallback) | 设置消息在云端被修改后回传回来的消息更新通知回调。 | 


### SDK初始化

| API | 描述 | 
|-----|-----| 
| [TIMInit](url_for_init_api#TIMInit) | IM SDK 初始化。 | 
| [TIMUninit](url_for_init_api#TIMUninit) | IM SDK 卸载。 | 
| [TIMGetSDKVersion](url_for_init_api#TIMGetSDKVersion) | 获取 IM SDK 版本号。 | 
| [TIMSetConfig](url_for_init_api#TIMSetConfig) | 设置额外的用户配置。 | 


### 登录登出

| API | 描述 | 
|-----|-----| 
| [TIMLogin](url_for_login_api#TIMLogin) | 登录。 | 
| [TIMLogout](url_for_login_api#TIMLogout) | 登出。 | 


### 会话相关接口

| API | 描述 | 
|-----|-----| 
| [TIMConvCreate](url_for_conv_api#TIMConvCreate) | 创建会话。 | 
| [TIMConvDelete](url_for_conv_api#TIMConvDelete) | 删除会话。 | 
| [TIMConvGetConvList](url_for_conv_api#TIMConvGetConvList) | 获取本地缓存的会话列表。 | 
| [TIMConvSetDraft](url_for_conv_api#TIMConvSetDraft) | 设置指定会话的草稿。 | 
| [TIMConvCancelDraft](url_for_conv_api#TIMConvCancelDraft) | 取消指定会话的草稿(删除)。 | 


### 消息相关接口

| API | 描述 | 
|-----|-----| 
| [TIMMsgSendNewMsg](url_for_msg_api#TIMMsgSendNewMsg) | 发送新消息。 | 
| [TIMMsgReportReaded](url_for_msg_api#TIMMsgReportReaded) | 消息上报已读。 | 
| [TIMMsgRevoke](url_for_msg_api#TIMMsgRevoke) | 消息撤回。 | 
| [TIMMsgFindByMsgLocatorList](url_for_msg_api#TIMMsgFindByMsgLocatorList) | 根据消息定位精准查找指定会话的消息。 | 
| [TIMMsgImportMsgList](url_for_msg_api#TIMMsgImportMsgList) | 导入消息列表到指定会话。 | 
| [TIMMsgSaveMsg](url_for_msg_api#TIMMsgSaveMsg) | 保存自定义消息。 | 
| [TIMMsgGetMsgList](url_for_msg_api#TIMMsgGetMsgList) | 获取指定会话的消息列表。 | 
| [TIMMsgDelete](url_for_msg_api#TIMMsgDelete) | 删除指定会话的消息。 | 
| [TIMMsgDownloadElemToPath](url_for_msg_api#TIMMsgDownloadElemToPath) | 下载消息内元素到指定文件路径(图片、视频、音频、文件)。 | 
| [TIMMsgBatchSend](url_for_msg_api#TIMMsgBatchSend) | 群发消息。 | 


### 群组相关接口

| API | 描述 | 
|-----|-----| 
| [TIMGroupCreate](url_for_group_api#TIMGroupCreate) | 创建群组。 | 
| [TIMGroupDelete](url_for_group_api#TIMGroupDelete) | 删除(解散)群组。 | 
| [TIMGroupJoin](url_for_group_api#TIMGroupJoin) | 申请加入群组。 | 
| [TIMGroupQuit](url_for_group_api#TIMGroupQuit) | 退出群组。 | 
| [TIMGroupInviteMember](url_for_group_api#TIMGroupInviteMember) | 邀请加入群组。 | 
| [TIMGroupDeleteMember](url_for_group_api#TIMGroupDeleteMember) | 删除群组成员。 | 
| [TIMGroupGetJoinedGroupList](url_for_group_api#TIMGroupGetJoinedGroupList) | 获取已加入群组列表。 | 
| [TIMGroupGetGroupInfoList](url_for_group_api#TIMGroupGetGroupInfoList) | 获取群组信息列表。 | 
| [TIMGroupModifyGroupInfo](url_for_group_api#TIMGroupModifyGroupInfo) | 修改群信息。 | 
| [TIMGroupGetMemberInfoList](url_for_group_api#TIMGroupGetMemberInfoList) | 获取群成员信息列表。 | 
| [TIMGroupModifyMemberInfo](url_for_group_api#TIMGroupModifyMemberInfo) | 修改群成员信息。 | 
| [TIMGroupGetPendencyList](url_for_group_api#TIMGroupGetPendencyList) | 获取群未决信息列表。群未决信息是指还没有处理的操作，比如邀请加群或者请求加群，这个操作还没有被处理，称之为群未决信息。 | 
| [TIMGroupReportPendencyReaded](url_for_group_api#TIMGroupReportPendencyReaded) | 上报群未决信息已读。 | 
| [TIMGroupHandlePendency](url_for_group_api#TIMGroupHandlePendency) | 处理群未决信息。 | 


