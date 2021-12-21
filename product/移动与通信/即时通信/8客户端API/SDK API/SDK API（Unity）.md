更为详细的接口，请参见  [Unity 全部接口](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.html)。

## 事件回调接口

| API                                                          | 描述                                             |
| ------------------------------------------------------------ | ------------------------------------------------ |
| [AddRecvNewMsgCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 增加接收新消息回调                               |
| [RemoveRecvNewMsgCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除接收新消息回调                               |
| [SetMsgReadedReceiptCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置消息已读回执回调                             |
| [SetMsgRevokeCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置接收的消息被撤回回调                         |
| [SetMsgElemUploadProgressCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置消息内元素相关文件上传进度回调               |
| [SetGroupTipsEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置群组系统消息回调                             |
| [SetConvEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置会话事件回调                                 |
| [SetNetworkStatusListenerCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置网络连接状态监听回调                         |
| [SetKickedOfflineCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置被踢下线通知回调                             |
| [SetUserSigExpiredCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置票据过期回调                                 |
| [SetOnAddFriendCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置添加好友的回调                               |
| [SetOnDeleteFriendCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置删除好友的回调                               |
| [SetUpdateFriendProfileCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置更新好友资料的回调                           |
| [SetFriendAddRequestCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置好友添加请求的回调                           |
| [SetLogCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置日志回调                                     |
| [SetMsgUpdateCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置消息在云端被修改后回传回来的消息更新通知回调 |


## IM SDK 初始化相关接口

| API                                                          | 描述               |
| ------------------------------------------------------------ | ------------------ |
| [Init](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | IM SDK 初始化      |
| [Uninit](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | IM SDK 卸载        |
| [GetSDKVersion](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取 IM SDK 版本号 |
| [SetConfig](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置额外的用户配置 |


## 登录登出相关接口

| API                                                          | 描述 |
| ------------------------------------------------------------ | ---- |
| [Login](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 登录 |
| [Logout](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 登出 |


## 会话相关接口

| API                                                          | 描述                     |
| ------------------------------------------------------------ | ------------------------ |
| [ConvCreate](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 创建会话                 |
| [ConvDelete](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除会话                 |
| [ConvGetConvList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取最近联系人的会话列表 |
| [ConvSetDraft](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 设置指定会话的草稿       |
| [ConvCancelDraft](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除指定会话的草稿       |


## 消息相关接口

| API                                                          | 描述                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [MsgSendNewMsg](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 发送新消息                                             |
| [MsgReportReaded](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 消息上报已读                                           |
| [MsgRevoke](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 消息撤回                                               |
| [MsgFindByMsgLocatorList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 根据消息定位精准查找指定会话的消息                     |
| [MsgImportMsgList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 导入消息列表到指定会话                                 |
| [MsgSaveMsg](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 保存自定义消息                                         |
| [MsgGetMsgList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取指定会话的消息列表                                 |
| [MsgDelete](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除指定会话的消息                                     |
| [MsgDownloadElemToPath](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 下载消息内元素到指定文件路径（图片、视频、音频、文件） |
| [MsgBatchSend](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 群发消息，该接口不支持向群组发送消息。                 |


## 群组相关接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [GroupCreate](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 创建群组                                                     |
| [GroupDelete](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除（解散）群组                                             |
| [GroupJoin](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 申请加入群组                                                 |
| [GroupQuit](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 退出群组                                                     |
| [GroupInviteMember](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 邀请加入群组                                                 |
| [GroupDeleteMember](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除群组成员                                                 |
| [GroupGetJoinedGroupList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取已加入群组列表                                           |
| [GroupGetGroupInfoList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取群组信息列表                                             |
| [GroupModifyGroupInfo](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 修改群信息                                                   |
| [GroupGetMemberInfoList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取群成员信息列表                                           |
| [GroupModifyMemberInfo](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 修改群成员信息                                               |
| [GroupGetPendencyList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取群未决信息列表。<br/>群未决信息是指还没有处理的操作，例如，邀请加群或者请求加群操作还没有被处理，称之为群未决信息 |
| [GroupReportPendencyReaded](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 上报群未决信息已读                                           |
| [GroupHandlePendency](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 处理群未决信息                                               |


## 用户资料相关接口

| API                                                          | 描述                       |
| ------------------------------------------------------------ | -------------------------- |
| [ProfileGetUserProfileList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取指定用户列表的个人资料 |
| [ProfileModifySelfUserProfile](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 修改自己的个人资料         |


## 关系链相关接口

| API                                                          | 描述                         |
| ------------------------------------------------------------ | ---------------------------- |
| [FriendshipGetFriendProfileList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取好友列表                 |
| [FriendshipAddFriend](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 添加好友                     |
| [FriendshipHandleFriendAddRequest](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 处理好友请求                 |
| [FriendshipModifyFriendProfile](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 更新好友资料（备注等）       |
| [FriendshipDeleteFriend](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除好友                     |
| [FriendshipCheckFriendType](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 检测好友类型（单向或双向）   |
| [FriendshipCreateFriendGroup](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 创建好友分组                 |
| [FriendshipGetFriendGroupList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取指定好友分组的分组信息   |
| [FriendshipModifyFriendGroup](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 修改好友分组                 |
| [FriendshipDeleteFriendGroup](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除好友分组                 |
| [FriendshipAddToBlackList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 添加指定用户到黑名单         |
| [FriendshipGetBlackList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取黑名单列表               |
| [FriendshipDeleteFromBlackList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 从黑名单中删除指定用户列表   |
| [FriendshipGetPendencyList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 获取好友添加请求未决信息列表 |
| [FriendshipDeletePendency](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 删除指定好友添加请求未决信息 |
| [FriendshipReportPendencyReaded](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html) | 上报好友添加请求未决信息已读 |

