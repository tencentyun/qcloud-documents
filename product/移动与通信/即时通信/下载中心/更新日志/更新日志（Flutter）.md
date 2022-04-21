## IM Flutter SDK 3.9.3 @2022.4.20
- 修复群禁言群 tips boolValue 丢失问题
 - 目前群信息变更回调返回的数据为 key(string)-value(string) 形式，新增 key(string)-boolValue(bool) 形式
- 修复会话实例少解析了 nameCard 字段问题
- 新增群已读回执相关接口
 - [sendMessageReadReceptes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessageReadReceipts.html) 发送群消息已读回执
 - [getMessageReadReceptes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getMessageReadReceipts.html) 获取自己发送消息的已读回执
 - [getgroupMessageReadMemeberList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getGroupMessageReadMemberList.html) 获取自己发送的群消息已读（未读）群成员列表
- Flutter for Web 完善

## IM Flutter SDK 3.9.1 @2022.3.24
- 升级底层库版本到6.1.2155

## IM Flutter SDK 3.9.0 @2022.3.22
- 修改 grouplistener

## IM Flutter SDK 3.8.9 @2022.3.18
- 监听注册问题修复

## IM Flutter SDK 3.8.4 @2022.3.14
- 更新 interface

## IM Flutter SDK 3.8.3 @2022.3.1
- 根据环境切换 token 编码

## IM Flutter SDK 3.8.2 @2022.2.21
- 更新群成员参数约束

## IM Flutter SDK 3.8.0 @2022.2.17
- 升级底层 interface 依赖

## IM Flutter SDK 3.7.8 @2022.2.15
- 修复强解包带来的异常

## IM Flutter SDK 3.7.7 @2022.2.10
- 修复 Swift 代码 warning
- 重写 Swift 强解包代码
- sendMessage 接口返回的 message 实例增加 id 字段


## IM Flutter SDK 3.7.5 @2022.01.23
- 升级底层库到6.0.1975
- 离线推送配置支持 TPNS TOKEN


## IM Flutter SDK 3.7.1 @2022.01.12
- 消息发送进度事件返回创建消息的 id
- 优化回调部分，提示业务方回调的错误在 SDK 中被 catch 需业务方修改

## IM Flutter SDK 3.7.0 @2022.01.10
- 优化 cloudCustomData 解包


## IM Flutter SDK 3.6.9 @2022.01.06
- 回复消息参数优化


## IM Flutter SDK 3.6.8 @2022.01.06
- 回复消息接口优化


## IM Flutter SDK 3.6.7 @2022.01.05
- iOS 编译环境从8.0升到9.0


## IM Flutter SDK 3.6.6 @2021.12.30
- 添加消息回复接口
- 修复 Web 端 release mode 下报错问题


## IM Flutter SDK 3.6.5 @2021.12.17
- 修复 java 语法错误

## IM Flutter SDK 3.6.4  @2021.12.17
- 修复 Android 异步注册事件无返回 bug
- 修复移除基础监听事件报错
- 消息进度事件增加发送中的消息的 uuid

## IM Flutter SDK 3.6.3 @2021.12.9
- addFriend 接口优化: addType 由 int 变更为 FriendTypeEnum
- acceptFriendApplication 接口优化: acceptType 由 int 变更为 FriendResponseTypeEnum
- checkFriend 接口优化: checkType 由 int 变更为 FriendTypeEnum
- createGroup 接口优化: addOpt 由 int 变更为 GroupAddOptTypeEnum
- deleteFromFriendList 接口优化: deleteType 由 int 变更为 FriendTypeEnum
- getGroupMemberList 接口优化: filter 由 int 变更为 GroupMemberFilterTypeEnum
- getHistoryMessageList 接口优化: type 由 int 变更为 HistoryMsgGetTypeEnum
- getHistoryMessageListWithoutFormat 接口优化: type 由 int 变更为 HistoryMsgGetTypeEnum
- getGroupMemberList 接口优化: type 由 int 变更为 GroupMemberFilterTypeEnum
- getGroupMemberList 接口优化: filter 由 int 变更为 GroupMemberFilterTypeEnum
- initSDK 接口优化: loglevel 由 int 变更为 LogLevelEnum
- refuseFriendApplication 接口优化: acceptType 由 int 变更为 FriendApplicationTypeEnum
- sendCustomMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendFaceMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendFileMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendForwardMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendImageMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendLocationMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendMergerMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendSoundMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendTextAtMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- sendTextMessage 接口优化: priority 由 int 变更为 MessagePriorityEnum
- setGroupMemberRole 接口优化: role 由 int 变更为 GroupMemberRoleTypeEnum
- 事件回调注册返回修改为异步

## IM Flutter SDK 3.6.2 @2021.12.9
- 修复移除高级消息未传 uuid


## IM Flutter SDK 3.6.1 @2021.12.8
- 修复文件进度事件丢失


## IM Flutter SDK 3.6.0 @2021.12.1
- 各个模块支持 listener 多次注册，多次回调
- 新增 api markAllMessageAsRead 设置全部会话已读
- 新增组合消息解析
- 升级 native 版本至5.8.1668


## IM Flutter SDK 3.5.6 @2021.11.25
- 修复 checkFriend 失败问题
- 修复 getC2CHistoryMessageList 无法获取后续消息问题

## IM Flutter SDK 3.5.5 @2021.11.23
- 架构调整


## IM Flutter SDK 3.5.4 @2021.11.22
- 新增 downloadMergeMesasge 接口


## IM Flutter SDK 3.5.3 @2021.11.15
- 新增 onTotalUnreadMessageCountChanged 事件
- V2TimConversation 新增 orderkey 字段，用于会话排序


## IM Flutter SDK 3.5.2 @2021.11.12
add web support

## IM Flutter SDK 3.5.1 @2021.11.10
- 数组越界兼容逻辑


## IM Flutter SDK 3.5.0 @2021.10.1
- 修复若干已知问题
- 新增接口如下：
 - callExperimentalAPI
 - clearC2CHistoryMessage
 - clearGroupHistoryMessage
 - searchLocalMessages
 - findMessages
 - searchGroups
 - searchGroupMembers
 - getSignalingInfo
 - addInvitedSignaling
 - searchFriends

## IM Flutter SDK 1.0.34 @2021.03.22
- 修复 iOS 获取历史消息报错

## IM Flutter SDK 1.0.33 @2021.03.22
- 修改 sdk 的 minSdkVersion 到16

## IM Flutter SDK 1.0.32 @2021.03.22
- 修复会话信息 lastMessage 为空时 crash

## IM Flutter SDK 1.0.30-1.0.31 @2021.03.18
- 修复自定义消息 data 字段为 null 时 crash

## IM Flutter SDK 1.0.29 @2021.03.16
- 【重要】修复获取群成员列表传参报错

## IM Flutter SDK 1.0.28 @2021.03.16
- 【重要】checkFriends 接口入参改变

## IM Flutter SDK 1.0.15-1.0.27 @2021.03.15
- 新增群成员自定义字段
- 完善 iOS 信令
- iOS 信令 bug 修复
- 自定义字段解析成 String 返回
- 优化设置个人自定义字段
- 更新 Android getHistoryMessageList
- 修复 Android 端 checkFriend 传参错误

## IM Flutter SDK 1.0.5-1.0.14 @2021.02.26
- 修复 deleteFriendApplication 传参错误
- 更新 native sdk 到5.1.132
- 更新 native sdk 到5.1.137
- 修改信令邀请接口传参 bug
- 修复信令接口不返回 id
- 修改 sdk 压缩配置
- 修改信令回调 bug
- 修改自定义消息返回数据
- 【重要】信令消息返回内容格式修改，用到信令请更新到该版本或以上版本


## IM Flutter SDK 1.0.4 @2021.01.14

- 更新 Android 终端 SDK 版本到5.1.129
- 更新 iOS 终端 SDK 版本到5.1.129

## IM Flutter SDK 1.0.3 @2021.01.13
- 跨平台支持 Android/iOS
- 支持单聊、群聊（讨论组、直播群）的会话类型
- 支持文本、表情、图片、语音、自定义消息的消息类型
- 支持 APNs 离线推送（上报 token、前后台切换事件上报）
- 消息本地存储

## IM Flutter SDK 0.0.1-1.0.2 @2020.12.01
- Flutter SDK 首发
- 邀请用户参与内测
