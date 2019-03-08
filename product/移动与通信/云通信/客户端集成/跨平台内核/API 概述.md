腾讯云通信的跨平台 C 接口（API）。

**IM SDK 下载链接：**
- Windows 平台  [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/Windows)。
- Windows 快速开始  [集成SDK](https://cloud.tencent.com/document/product/269/33489)  和  [跑通demo](https://cloud.tencent.com/document/product/269/33488)。

### 注册 SDK 回调

| API | 描述 | 
|-----|-----| 
| [TIMSetRecvNewMsgCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetRecvNewMsgCallback) | 设置接收新消息回调 | 
| [TIMSetMsgReadedReceiptCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetMsgReadedReceiptCallback) | 设置消息已读回执回调 | 
| [TIMSetMsgRevokeCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetMsgRevokeCallback) | 设置接收的消息被撤回回调 | 
| [TIMSetMsgElemUploadProgressCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetMsgElemUploadProgressCallback) | 设置消息内元素相关文件上传进度回调 | 
| [TIMSetGroupTipsEventCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetGroupTipsEventCallback) | 设置群组系统消息回调 | 
| [TIMSetConvEventCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetConvEventCallback) | 设置会话事件回调 | 
| [TIMSetNetworkStatusListenerCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetNetworkStatusListenerCallback) | 设置网络连接状态监听回调 | 
| [TIMSetKickedOfflineCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetKickedOfflineCallback) | 设置被踢下线通知回调 | 
| [TIMSetUserSigExpiredCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetUserSigExpiredCallback) | 设置票据过期回调 | 
| [TIMSetLogCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetLogCallback) | 设置日志回调 | 
| [TIMSetMsgUpdateCallback](https://cloud.tencent.com/document/product/269/33551#TIMSetMsgUpdateCallback) | 设置消息在云端被修改后回传回来的消息更新通知回调 | 


### SDK 初始化

| API | 描述 | 
|-----|-----| 
| [TIMInit](https://cloud.tencent.com/document/product/269/33546#TIMInit) | IM SDK 初始化 | 
| [TIMUninit](https://cloud.tencent.com/document/product/269/33546#TIMUninit) | IM SDK 卸载 | 
| [TIMGetSDKVersion](https://cloud.tencent.com/document/product/269/33546#TIMGetSDKVersion) | 获取 IM SDK 版本号 | 
| [TIMSetConfig](https://cloud.tencent.com/document/product/269/33546#TIMSetConfig) | 设置额外的用户配置 | 


### 登录登出

| API | 描述 | 
|-----|-----| 
| [TIMLogin](https://cloud.tencent.com/document/product/269/33547#TIMLogin) | 登录 | 
| [TIMLogout](https://cloud.tencent.com/document/product/269/33547#TIMLogout) | 登出 | 


### 会话相关接口

| API | 描述 | 
|-----|-----| 
| [TIMConvCreate](https://cloud.tencent.com/document/product/269/33548#TIMConvCreate) | 创建会话 | 
| [TIMConvDelete](https://cloud.tencent.com/document/product/269/33548#TIMConvDelete) | 删除会话 | 
| [TIMConvGetConvList](https://cloud.tencent.com/document/product/269/33548#TIMConvGetConvList) | 获取本地缓存的会话列表 | 
| [TIMConvSetDraft](https://cloud.tencent.com/document/product/269/33548#TIMConvSetDraft) | 设置指定会话的草稿 | 
| [TIMConvCancelDraft](https://cloud.tencent.com/document/product/269/33548#TIMConvCancelDraft) | 取消指定会话的草稿（删除）| 


### 消息相关接口

| API | 描述 | 
|-----|-----| 
| [TIMMsgSendNewMsg](https://cloud.tencent.com/document/product/269/33549#TIMMsgSendNewMsg) | 发送新消息 | 
| [TIMMsgReportReaded](https://cloud.tencent.com/document/product/269/33549#TIMMsgReportReaded) | 消息上报已读 | 
| [TIMMsgRevoke](https://cloud.tencent.com/document/product/269/33549#TIMMsgRevoke) | 消息撤回 | 
| [TIMMsgFindByMsgLocatorList](https://cloud.tencent.com/document/product/269/33549#TIMMsgFindByMsgLocatorList) | 根据消息定位精准查找指定会话的消息| 
| [TIMMsgImportMsgList](https://cloud.tencent.com/document/product/269/33549#TIMMsgImportMsgList) | 导入消息列表到指定会话 | 
| [TIMMsgSaveMsg](https://cloud.tencent.com/document/product/269/33549#TIMMsgSaveMsg) | 保存自定义消息 | 
| [TIMMsgGetMsgList](https://cloud.tencent.com/document/product/269/33549#TIMMsgGetMsgList) | 获取指定会话的消息列表 | 
| [TIMMsgDelete](https://cloud.tencent.com/document/product/269/33549#TIMMsgDelete) | 删除指定会话的消息 | 
| [TIMMsgDownloadElemToPath](https://cloud.tencent.com/document/product/269/33549#TIMMsgDownloadElemToPath) | 下载消息内元素到指定文件路径（图片、视频、音频、文件） | 
| [TIMMsgBatchSend](https://cloud.tencent.com/document/product/269/33549#TIMMsgBatchSend) | 群发消息 | 


### 群组相关接口

| API | 描述 | 
|-----|-----| 
| [TIMGroupCreate](https://cloud.tencent.com/document/product/269/33550#TIMGroupCreate) | 创建群组 | 
| [TIMGroupDelete](https://cloud.tencent.com/document/product/269/33550#TIMGroupDelete) | 删除(解散)群组 | 
| [TIMGroupJoin](https://cloud.tencent.com/document/product/269/33550#TIMGroupJoin) | 申请加入群组 | 
| [TIMGroupQuit](https://cloud.tencent.com/document/product/269/33550#TIMGroupQuit) | 退出群组 | 
| [TIMGroupInviteMember](https://cloud.tencent.com/document/product/269/33550#TIMGroupInviteMember) | 邀请加入群组 | 
| [TIMGroupDeleteMember](https://cloud.tencent.com/document/product/269/33550#TIMGroupDeleteMember) | 删除群组成员 | 
| [TIMGroupGetJoinedGroupList](https://cloud.tencent.com/document/product/269/33550#TIMGroupGetJoinedGroupList) | 获取已加入群组列表 | 
| [TIMGroupGetGroupInfoList](https://cloud.tencent.com/document/product/269/33550#TIMGroupGetGroupInfoList) | 获取群组信息列表 | 
| [TIMGroupModifyGroupInfo](https://cloud.tencent.com/document/product/269/33550#TIMGroupModifyGroupInfo) | 修改群信息 | 
| [TIMGroupGetMemberInfoList](https://cloud.tencent.com/document/product/269/33550#TIMGroupGetMemberInfoList) | 获取群成员信息列表 | 
| [TIMGroupModifyMemberInfo](https://cloud.tencent.com/document/product/269/33550#TIMGroupModifyMemberInfo) | 修改群成员信息 | 
| [TIMGroupGetPendencyList](https://cloud.tencent.com/document/product/269/33550#TIMGroupGetPendencyList) | 获取群未决信息列表。<br/>群未决信息是指还没有处理的操作，例如，邀请加群或者请求加群操作还没有被处理，称之为群未决信息 | 
| [TIMGroupReportPendencyReaded](https://cloud.tencent.com/document/product/269/33550#TIMGroupReportPendencyReaded) | 上报群未决信息已读 | 
| [TIMGroupHandlePendency](https://cloud.tencent.com/document/product/269/33550#TIMGroupHandlePendency) | 处理群未决信息 | 


