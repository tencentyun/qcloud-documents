## 事件回调接口

| API                                                          | 描述                                             |
| ------------------------------------------------------------ | ------------------------------------------------ |
| [TIMAddRecvNewMsgCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 增加接收新消息回调                               |
| [TIMRemoveRecvNewMsgCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除接收新消息回调                               |
| [TIMSetMsgReadedReceiptCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置消息已读回执回调                             |
| [TIMSetMsgRevokeCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置接收的消息被撤回回调                         |
| [TIMSetMsgElemUploadProgressCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置消息内元素相关文件上传进度回调               |
| [TIMSetGroupTipsEventCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置群组系统消息回调                             |
| [TIMSetConvEventCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置会话事件回调                                 |
| [TIMSetNetworkStatusListenerCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置网络连接状态监听回调                         |
| [TIMSetKickedOfflineCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置被踢下线通知回调                             |
| [TIMSetUserSigExpiredCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置票据过期回调                                 |
| [TIMSetOnAddFriendCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置添加好友的回调                               |
| [TIMSetOnDeleteFriendCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置删除好友的回调                               |
| [TIMSetUpdateFriendProfileCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置更新好友资料的回调                           |
| [TIMSetFriendAddRequestCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置好友添加请求的回调                           |
| [TIMSetLogCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置日志回调                                     |
| [TIMSetMsgUpdateCallback](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置消息在云端被修改后回传回来的消息更新通知回调 |


## IM SDK 初始化相关接口

| API                                                          | 描述               |
| ------------------------------------------------------------ | ------------------ |
| [TIMInit](https://comm.qq.com/toc-electron-sdk-doc/index.html) | IM SDK 初始化      |
| [TIMUninit](https://comm.qq.com/toc-electron-sdk-doc/index.html) | IM SDK 卸载        |
| [TIMGetSDKVersion](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取 IM SDK 版本号 |
| [TIMSetConfig](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置额外的用户配置 |


## 登录登出相关接口

| API                                                          | 描述 |
| ------------------------------------------------------------ | ---- |
| [TIMLogin](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 登录 |
| [TIMLogout](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 登出 |


## 会话相关接口

| API                                                          | 描述                     |
| ------------------------------------------------------------ | ------------------------ |
| [TIMConvCreate](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 创建会话                 |
| [TIMConvDelete](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除会话                 |
| [TIMConvGetConvList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取最近联系人的会话列表 |
| [TIMConvSetDraft](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 设置指定会话的草稿       |
| [TIMConvCancelDraft](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除指定会话的草稿       |


## 消息相关接口

| API                                                          | 描述                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [TIMMsgSendNewMsg](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 发送新消息                                             |
| [TIMMsgReportReaded](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 消息上报已读                                           |
| [TIMMsgRevoke](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 消息撤回                                               |
| [TIMMsgFindByMsgLocatorList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 根据消息定位精准查找指定会话的消息                     |
| [TIMMsgImportMsgList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 导入消息列表到指定会话                                 |
| [TIMMsgSaveMsg](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 保存自定义消息                                         |
| [TIMMsgGetMsgList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取指定会话的消息列表                                 |
| [TIMMsgDelete](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除指定会话的消息                                     |
| [TIMMsgDownloadElemToPath](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 下载消息内元素到指定文件路径（图片、视频、音频、文件） |
| [TIMMsgBatchSend](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 群发消息，该接口不支持向群组发送消息。                 |


## 群组相关接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [TIMGroupCreate](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 创建群组                                                     |
| [TIMGroupDelete](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除（解散）群组                                             |
| [TIMGroupJoin](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 申请加入群组                                                 |
| [TIMGroupQuit](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 退出群组                                                     |
| [TIMGroupInviteMember](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 邀请加入群组                                                 |
| [TIMGroupDeleteMember](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除群组成员                                                 |
| [TIMGroupGetJoinedGroupList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取已加入群组列表                                           |
| [TIMGroupGetGroupInfoList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取群组信息列表                                             |
| [TIMGroupModifyGroupInfo](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 修改群信息                                                   |
| [TIMGroupGetMemberInfoList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取群成员信息列表                                           |
| [TIMGroupModifyMemberInfo](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 修改群成员信息                                               |
| [TIMGroupGetPendencyList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取群未决信息列表。<br/>群未决信息是指还没有处理的操作，例如，邀请加群或者请求加群操作还没有被处理，称之为群未决信息 |
| [TIMGroupReportPendencyReaded](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 上报群未决信息已读                                           |
| [TIMGroupHandlePendency](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 处理群未决信息                                               |


## 用户资料相关接口

| API                                                          | 描述                       |
| ------------------------------------------------------------ | -------------------------- |
| [TIMProfileGetUserProfileList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取指定用户列表的个人资料 |
| [TIMProfileModifySelfUserProfile](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 修改自己的个人资料         |


## 关系链相关接口

| API                                                          | 描述                         |
| ------------------------------------------------------------ | ---------------------------- |
| [TIMFriendshipGetFriendProfileList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取好友列表                 |
| [TIMFriendshipAddFriend](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 添加好友                     |
| [TIMFriendshipHandleFriendAddRequest](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 处理好友请求                 |
| [TIMFriendshipModifyFriendProfile](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 更新好友资料（备注等）       |
| [TIMFriendshipDeleteFriend](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除好友                     |
| [TIMFriendshipCheckFriendType](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 检测好友类型（单向或双向）   |
| [TIMFriendshipCreateFriendGroup](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 创建好友分组                 |
| [TIMFriendshipGetFriendGroupList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取指定好友分组的分组信息   |
| [TIMFriendshipModifyFriendGroup](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 修改好友分组                 |
| [TIMFriendshipDeleteFriendGroup](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除好友分组                 |
| [TIMFriendshipAddToBlackList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 添加指定用户到黑名单         |
| [TIMFriendshipGetBlackList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取黑名单列表               |
| [TIMFriendshipDeleteFromBlackList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 从黑名单中删除指定用户列表   |
| [TIMFriendshipGetPendencyList](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 获取好友添加请求未决信息列表 |
| [TIMFriendshipDeletePendency](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 删除指定好友添加请求未决信息 |
| [TIMFriendshipReportPendencyReaded](https://comm.qq.com/toc-electron-sdk-doc/index.html) | 上报好友添加请求未决信息已读 |

