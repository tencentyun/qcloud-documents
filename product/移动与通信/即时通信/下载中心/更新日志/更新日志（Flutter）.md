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
