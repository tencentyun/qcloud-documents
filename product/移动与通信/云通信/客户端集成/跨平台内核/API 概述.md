腾讯云通信的跨平台 C 接口（API）。

**IM SDK 下载链接：**
- Windows 平台  [IM SDK](https://github.com/tencentyun/TIMSDK/tree/master/Windows)。
- Windows 快速开始  [集成SDK](https://cloud.tencent.com/document/product/269/33489)  和  [跑通demo](https://cloud.tencent.com/document/product/269/33488)。

### 注册 SDK 回调

| API | 描述 | 
|-----|-----| 
| [TIMSetRecvNewMsgCallback](https://cloud.tencent.com/document/product/269/33551#timsetrecvnewmsgcallback) | 设置接收新消息回调 | 
| [TIMSetMsgReadedReceiptCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgreadedreceiptcallback) | 设置消息已读回执回调 | 
| [TIMSetMsgRevokeCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgrevokecallback) | 设置接收的消息被撤回回调 | 
| [TIMSetMsgElemUploadProgressCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgelemuploadprogresscallback) | 设置消息内元素相关文件上传进度回调 | 
| [TIMSetGroupTipsEventCallback](https://cloud.tencent.com/document/product/269/33551#timsetgrouptipseventcallback) | 设置群组系统消息回调 | 
| [TIMSetConvEventCallback](https://cloud.tencent.com/document/product/269/33551#timsetconveventcallback) | 设置会话事件回调 | 
| [TIMSetNetworkStatusListenerCallback](https://cloud.tencent.com/document/product/269/33551#timsetnetworkstatuslistenercallback) | 设置网络连接状态监听回调 | 
| [TIMSetKickedOfflineCallback](https://cloud.tencent.com/document/product/269/33551#timsetkickedofflinecallback) | 设置被踢下线通知回调 | 
| [TIMSetUserSigExpiredCallback](https://cloud.tencent.com/document/product/269/33551#timsetusersigexpiredcallback) | 设置票据过期回调 | 
| [TIMSetLogCallback](https://cloud.tencent.com/document/product/269/33551#timsetlogcallback) | 设置日志回调 | 
| [TIMSetMsgUpdateCallback](https://cloud.tencent.com/document/product/269/33551#timsetmsgupdatecallback) | 设置消息在云端被修改后回传回来的消息更新通知回调 | 


### SDK 初始化

| API | 描述 | 
|-----|-----| 
| [TIMInit](https://cloud.tencent.com/document/product/269/33546#timinit) | IM SDK初始化 | 
| [TIMUninit](https://cloud.tencent.com/document/product/269/33546#timuninit) | IM SDK卸载 | 
| [TIMGetSDKVersion](https://cloud.tencent.com/document/product/269/33546#timgetsdkversion) | 获取IM SDK版本号 | 
| [TIMSetConfig](https://cloud.tencent.com/document/product/269/33546#timsetconfig) | 设置额外的用户配置 | 


### 登录登出

| API | 描述 | 
|-----|-----| 
| [TIMLogin](https://cloud.tencent.com/document/product/269/33547#timlogin) | 登录 | 
| [TIMLogout](https://cloud.tencent.com/document/product/269/33547#timlogout) | 登出 | 


### 会话相关接口

| API | 描述 | 
|-----|-----| 
| [TIMConvCreate](https://cloud.tencent.com/document/product/269/33548#timconvcreate) | 创建会话 | 
| [TIMConvDelete](https://cloud.tencent.com/document/product/269/33548#timconvdelete) | 删除会话 | 
| [TIMConvGetConvList](https://cloud.tencent.com/document/product/269/33548#timconvgetconvlist) | 获取本地缓存的会话列表 | 
| [TIMConvSetDraft](https://cloud.tencent.com/document/product/269/33548#timconvsetdraft) | 设置指定会话的草稿 | 
| [TIMConvCancelDraft](https://cloud.tencent.com/document/product/269/33548#timconvcanceldraft) | 取消指定会话的草稿（删除） | 


### 消息相关接口

| API | 描述 | 
|-----|-----| 
| [TIMMsgSendNewMsg](https://cloud.tencent.com/document/product/269/33549#timmsgsendnewmsg) | 发送新消息 | 
| [TIMMsgReportReaded](https://cloud.tencent.com/document/product/269/33549#timmsgreportreaded) | 消息上报已读 | 
| [TIMMsgRevoke](https://cloud.tencent.com/document/product/269/33549#timmsgrevoke) | 消息撤回 | 
| [TIMMsgFindByMsgLocatorList](https://cloud.tencent.com/document/product/269/33549#timmsgfindbymsglocatorlist) | 根据消息定位精准查找指定会话的消息 | 
| [TIMMsgImportMsgList](https://cloud.tencent.com/document/product/269/33549#timmsgimportmsglist) | 导入消息列表到指定会话 | 
| [TIMMsgSaveMsg](https://cloud.tencent.com/document/product/269/33549#timmsgsavemsg) | 保存自定义消息 | 
| [TIMMsgGetMsgList](https://cloud.tencent.com/document/product/269/33549#timmsggetmsglist) | 获取指定会话的消息列表 | 
| [TIMMsgDelete](https://cloud.tencent.com/document/product/269/33549#timmsgdelete) | 删除指定会话的消息 | 
| [TIMMsgDownloadElemToPath](https://cloud.tencent.com/document/product/269/33549#timmsgdownloadelemtopath) | 下载消息内元素到指定文件路径（图片、视频、音频、文件） | 
| [TIMMsgBatchSend](https://cloud.tencent.com/document/product/269/33549#timmsgbatchsend) | 群发消息 | 


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


