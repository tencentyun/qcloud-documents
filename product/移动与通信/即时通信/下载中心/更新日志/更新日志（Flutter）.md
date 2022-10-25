## 平台支持版本

我们致力于打造一套支持 Flutter 全平台的即时通信 IM SDK 及 TUIKit，帮助您一套代码，全平台运行。

| 平台 | 无 UI SDK (tencent_im_sdk_plugin) | 含 UI 及基础业务逻辑 TUIKit (tim_ui_kit) |
|---------|---------|---------|
| iOS | 所有版本支持 | 所有版本支持 |
| Android | 所有版本支持 | 所有版本支持 |
| [Web](https://cloud.tencent.com/document/product/269/68823#web) | 4.1.1+2版本起支持 | 0.1.5版本起支持 |
| [macOS](https://cloud.tencent.com/document/product/269/68823#pc) | 4.1.8版本起支持 | 即将上线 |
| [Windows](https://cloud.tencent.com/document/product/269/68823#pc) | 4.1.8版本起支持 | 即将上线 |

>? Web/macOS/Windows 平台需要简单的几步额外引入，详情请查看 [Web 兼容](https://cloud.tencent.com/document/product/269/68823#web) 和 [Desktop 兼容](https://cloud.tencent.com/document/product/269/68823#pc) 指引。

## 更新日志
>?
>
>- IM Flutter SDK（无 UI）指代 [tencent_im_sdk_plugin](https://pub.dev/packages/tencent_im_sdk_plugin) 包，仅包括所有 IM 客户端 API 及监听回调。
>- IM Flutter TUIKit（含 UI）指代 [tim_ui_kit](https://pub.dev/packages/tim_ui_kit) 包，在无 UI SDK 基础上，还包括完整 UI 组件库及业务逻辑。

### IM Flutter TUIKit（含 UI） 0.1.8 @2022.10.21
* 优化：文件批量下载队列，允许一次点击多个文件消息。
* 优化：群组列表小部件可以自动更新。
* 优化：相机拍摄支持性能相对较低的设备，自动调整分辨率。
* 优化：支持自定义应用栏的颜色和文字样式，特别是在 `TIMUIKitChat` 组件上。
* 修复：好友备注或昵称无法在群提示中显示。
* 修正：视频播放错误。
* 修正：几个错误。

### IM Flutter SDK（无 UI） 4.1.8 @2022.10.18
- 新增：支持 PC 平台，包含 macOS 与 Windows
- 新增：消息扩展
- 新增：信令编辑
- 优化：升级底层 SDK
- 修复：高版本 JDK 转换问题
- 修复：若干问题

### IM Flutter TUIKit（含 UI） 0.1.7 @2022.10.18
* 新增：支持大图片和 RAW 图片，特别是那些从最新版本的 iOS 和 iPhone 14 Pro 系列捕获的图片，在自动发送前压缩和格式化
* 优化：性能和稳定性，特别是历史消息列表和启动
* 优化：使初始化' TIMUIKitChat '为幂等操作
* 优化：当滚动回底部时加载最新的消息
* 优化：优化支持 Flutter 2.x和 3.x 系列
* 修复：iOS 相册，仅允许部分图片，权限支持
* 修复：几个 bug

### IM Flutter TUIKit（含 UI） 0.1.5 @2022.09.22
* 新增：Web支持。现在，您可以在 iOS/Android/Web 平台上实现 TUIKit
* 新增：登录后检查磁盘存储，控制在`init`的`config`中
* 新增：在`TIMUIKitChatConfig`中添加：`timeDividerConfig`、`notificationAndroidSound` 华为Google推送声音配置、`isSupportMarkdown` 文本消息是否支持Markdown解析 、`onTapLink`
* 移除：默认Emoji列表，由于版权问题。您可以通过[tim_ui_kit_sticker_plugin](https://pub.dev/packages/tim_ui_kit_sticker_plugin)向TUIKit提供您自己的表情列表
* 优化：您现在可以选择禁用对话列表中 @消息 的显示
* 优化：您现在可以在`TIMUIKitChatConfig`和`MessageItemBuilder`中返回`notificationExt`/`notificationBody`为`null`，在特定的情况下可以根据需要使用默认值，这意味着您可以根据提供的情况控制是否使用自定义设置，而不需要重新定义代码中与TUIKit相同的逻辑
* 优化：支持文本消息多行
* 优化：对`TIMUIKitChat`的体验进行改造和提升。另外，如需使用`TIMUIKitChatController`，需要传入`controler`，就像我们在[教程](https://cloud.tencent.com/document/product/269/70746#.E6.AD.A5.E9.AA.A46.EF.BC.9A.5B.E9.80.89.E8.A3.85.5D-.E4.BD.BF.E7.94.A8-controller-.E6.8E.A7.E5.88.B6-tuikit.3Ca-id.3D.22controller.22.3E.3C.2Fa.3E)中显示的那样

### IM Flutter SDK（无 UI） 4.1.3 @2022.09.21
- 解决一些 Web 端的问题

### IM Flutter SDK（无 UI） 4.1.1+2 @2022.08.25
- 升级底层库版本到6.6.x
- 全面支持 Flutter Web

### IM Flutter SDK（无 UI） 4.1.0 @2022.08.09
- 升级底层库版本

### IM Flutter TUIKit（含 UI） 0.1.3 @2022.08.03
- 新增用户输入中状态
- 新增消息表情回应能力
- 新增用户在线状态展示

### IM Flutter SDK（无 UI） 4.0.8 @2022.07.25
- 新增获取会话列表高级接口，支持按照会话 类型/标签 分组拉取会话列表
- 新增自定义标记会话接口
- 新增会话分组能力
- Dart 版本依赖降低至2.0.0
- 支持 Flutter 多引擎
- 支持 Android 端离线推送音效配置
- 支持自定义用户在线状态
- 升级底层库版本至6.5.x

### IM Flutter TUIKit（含 UI） 0.1.2 @2022.07.08
- 修复原引用的第三方底层录音库 `flutter_record_plugin_plus` 无法使用问题

### IM Flutter TUIKit（含 UI） 0.1.1 @2022.07.07
- 优化图片预览逻辑
- 为各个组件新增生命周期钩子函数 LifeCycle hooks
- 新增群聊天页新增禁言状态
- 文本消息中的 URL 可点击跳转及新增网站信息预览卡片
- 新增 TUIKit 层全局事件回调，包括需要提示的信息语/ Flutter 层报错/ IM API层报错返回，TUIKit 不再进行信息弹窗，可根据回调及提示语自定弹窗
- 重构 `TUIKitGroupProfile`群资料 组件及 `TUIKitProfile`用户资料 组件，简化用法，超快速接入

### IM Flutter SDK（无 UI） 4.0.7 @2022.07.07
- iOS 支持自定义角标数字
- 优化入群申请逻辑

### IM Flutter SDK（无 UI） 4.0.6 @2022.07.04
- 升级底层库版本到6.2.x
- 修复离线推送信息字段

### IM Flutter SDK（无 UI） 4.0.5 @2022.07.01
- 新增用户在线状态查询
- 支持通过消息类型请求历史消息列表
- 支持富文本消息发送

### IM Flutter TUIKit（含 UI） 0.1.0 @2022.06.10
- 新增 `TIMUIKitChat` 组件原子化开发能力，通过各种子组件可自行拼装聊天页面。
- 支持消息编辑更新UI能力
- 新增入群申请审批页面组件
- 国际化语言新增繁体中文
- 开放更多自定义组件参数

### IM Flutter TUIKit（含 UI） 0.0.9 @2022.05.30
- 支持离线推送，配合新发布的 [tim_ui_kit_push_plugin](https://pub.dev/packages/tim_ui_kit_push_plugin) 推送插件
- 支持 Flutter 3.0
- 优化媒体消息本地预览

### IM Flutter SDK（无 UI） 4.0.2 @2022.05.27
- 修复本地视频路径

### IM Flutter SDK（无 UI） 4.0.1 @2022.05.23
- 新增话题能力
- 新增消息编辑能力

### IM Flutter SDK（无 UI） 4.0.0 @2022.04.26
- 升级底层库版本到6.2.x
- 修复离线推送信息字段

### IM Flutter TUIKit（含 UI） 0.0.8 @2022.04.24
- 新增群消息已读回执能力
- 新增聊天区域右下角小舌头，支持返回底部/展示新消息数量/@消息提醒。

### IM Flutter SDK（无 UI） 3.9.3 @2022.04.20
- 修复群禁言群 tips boolValue 丢失问题
 - 目前群信息变更回调返回的数据为 key(string)-value(string) 形式，新增 key(string)-boolValue(bool) 形式
- 修复会话实例少解析了 nameCard 字段问题
- 新增群已读回执相关接口
 - [sendMessageReadReceptes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessageReadReceipts.html) 发送群消息已读回执
 - [getMessageReadReceptes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getMessageReadReceipts.html) 获取自己发送消息的已读回执
 - [getgroupMessageReadMemeberList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getGroupMessageReadMemberList.html) 获取自己发送的群消息已读（未读）群成员列表
- Flutter for Web 完善

### IM Flutter TUIKit（含 UI） 0.0.7 @2022.04.13
- 体验优化

### IM Flutter TUIKit（含 UI） 0.0.6 @2022.04.08
- 开放发送消息自动上屏接口，及更多定制化能力参数
- 用户登录鉴权优化
- 个保法隐私政策对齐优化

### IM Flutter TUIKit（含 UI） 0.0.5 @2022.03.24
- 聊天区域组件 `TIMUIKitChat` 开放更多定制化能力

### IM Flutter SDK（无 UI） 3.9.1 @2022.03.24
- 升级底层库版本到6.1.2155

### IM Flutter SDK（无 UI） 3.9.0 @2022.03.22
- 修改 grouplistener

### IM Flutter SDK（无 UI） 3.8.9 @2022.03.18
- 监听注册问题修复

### IM Flutter TUIKit（含 UI） 0.0.4 @2022.03.17
- 新增支持发送图片及视频
- 优化主题样式
- 优化搜索组件

### IM Flutter TUIKit（含 UI） 0.0.3 @2022.03.14
- 组件细节优化
- 自动国际化能力完善
- 新增全局搜索 `TIMUIKitSearch` 组件
- 新增会话内搜索 `TIMUIKitSearchMsgDetail` 组件
- 新增添加好友 `TIMUIKitAddFriend` 组件
- 新增申请入群 `TIMUIKitAddGroup` 组件
- 新增主题样式

### IM Flutter SDK（无 UI） 3.8.4 @2022.03.14
- 更新 interface

### IM Flutter TUIKit（含 UI） 0.0.2 @2022.03.02
- 优化 `TIMUIKitChat` 组件
- 支持国际化语言自动及手动切换，简体中文/英文

### IM Flutter TUIKit（含 UI） 0.0.1 @2022.03.01
- 腾讯云 IM for Flutter 含 UI 及业务逻辑组件库首发
- 首批上线七个主组件，涵盖聊天区域/会话列表/联系人及群组资料/联系人列表/黑名单/好友申请列表等

### IM Flutter SDK（无 UI） 3.8.3 @2022.03.01
- 根据环境切换 token 编码

### IM Flutter SDK（无 UI） 3.8.2 @2022.02.21
- 更新群成员参数约束

### IM Flutter SDK（无 UI） 3.8.0 @2022.02.17
- 升级底层 interface 依赖

### IM Flutter SDK（无 UI） 3.7.8 @2022.02.15
- 修复强解包带来的异常

### IM Flutter SDK（无 UI） 3.7.7 @2022.02.10
- 修复 Swift 代码 warning
- 重写 Swift 强解包代码
- sendMessage 接口返回的 message 实例增加 id 字段


### IM Flutter SDK（无 UI） 3.7.5 @2022.01.23
- 升级底层库到6.0.1975
- 离线推送配置支持 TPNS TOKEN


### IM Flutter SDK（无 UI） 3.7.1 @2022.01.12
- 消息发送进度事件返回创建消息的 id
- 优化回调部分，提示业务方回调的错误在 SDK 中被 catch 需业务方修改

### IM Flutter SDK（无 UI） 3.7.0 @2022.01.10
- 优化 cloudCustomData 解包


### IM Flutter SDK（无 UI） 3.6.9 @2022.01.06
- 回复消息参数优化


### IM Flutter SDK（无 UI） 3.6.8 @2022.01.06
- 回复消息接口优化


### IM Flutter SDK（无 UI） 3.6.7 @2022.01.05
- iOS 编译环境从8.0升到9.0


### IM Flutter SDK（无 UI） 3.6.6 @2021.12.30
- 添加消息回复接口
- 修复 Web 端 release mode 下报错问题


### IM Flutter SDK（无 UI） 3.6.5 @2021.12.17
- 修复 java 语法错误

### IM Flutter SDK（无 UI） 3.6.4  @2021.12.17
- 修复 Android 异步注册事件无返回 bug
- 修复移除基础监听事件报错
- 消息进度事件增加发送中的消息的 uuid

### IM Flutter SDK（无 UI） 3.6.3 @2021.12.9
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

### IM Flutter SDK（无 UI） 3.6.2 @2021.12.9
- 修复移除高级消息未传 uuid


### IM Flutter SDK（无 UI） 3.6.1 @2021.12.8
- 修复文件进度事件丢失


### IM Flutter SDK（无 UI） 3.6.0 @2021.12.1
- 各个模块支持 listener 多次注册，多次回调
- 新增 api markAllMessageAsRead 设置全部会话已读
- 新增组合消息解析
- 升级 native 版本至5.8.1668


### IM Flutter SDK（无 UI） 3.5.6 @2021.11.25
- 修复 checkFriend 失败问题
- 修复 getC2CHistoryMessageList 无法获取后续消息问题

### IM Flutter SDK（无 UI） 3.5.5 @2021.11.23
- 架构调整


### IM Flutter SDK（无 UI） 3.5.4 @2021.11.22
- 新增 downloadMergeMesasge 接口


### IM Flutter SDK（无 UI） 3.5.3 @2021.11.15
- 新增 onTotalUnreadMessageCountChanged 事件
- V2TimConversation 新增 orderkey 字段，用于会话排序


### IM Flutter SDK（无 UI） 3.5.2 @2021.11.12
add web support

### IM Flutter SDK（无 UI） 3.5.1 @2021.11.10
- 数组越界兼容逻辑


### IM Flutter SDK（无 UI） 3.5.0 @2021.10.1
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

### IM Flutter SDK（无 UI） 1.0.34 @2021.03.22
- 修复 iOS 获取历史消息报错

### IM Flutter SDK（无 UI） 1.0.33 @2021.03.22
- 修改 sdk 的 minSdkVersion 到16

### IM Flutter SDK（无 UI） 1.0.32 @2021.03.22
- 修复会话信息 lastMessage 为空时 crash

### IM Flutter SDK（无 UI） 1.0.30-1.0.31 @2021.03.18
- 修复自定义消息 data 字段为 null 时 crash

### IM Flutter SDK（无 UI） 1.0.29 @2021.03.16
- 【重要】修复获取群成员列表传参报错

### IM Flutter SDK（无 UI） 1.0.28 @2021.03.16
- 【重要】checkFriends 接口入参改变

### IM Flutter SDK（无 UI） 1.0.15-1.0.27 @2021.03.15
- 新增群成员自定义字段
- 完善 iOS 信令
- iOS 信令 bug 修复
- 自定义字段解析成 String 返回
- 优化设置个人自定义字段
- 更新 Android getHistoryMessageList
- 修复 Android 端 checkFriend 传参错误

### IM Flutter SDK（无 UI） 1.0.5-1.0.14 @2021.02.26
- 修复 deleteFriendApplication 传参错误
- 更新 native sdk 到5.1.132
- 更新 native sdk 到5.1.137
- 修改信令邀请接口传参 bug
- 修复信令接口不返回 id
- 修改 sdk 压缩配置
- 修改信令回调 bug
- 修改自定义消息返回数据
- 【重要】信令消息返回内容格式修改，用到信令请更新到该版本或以上版本


### IM Flutter SDK（无 UI） 1.0.4 @2021.01.14

- 更新 Android 终端 SDK 版本到5.1.129
- 更新 iOS 终端 SDK 版本到5.1.129

### IM Flutter SDK（无 UI） 1.0.3 @2021.01.13
- 跨平台支持 Android/iOS
- 支持单聊、群聊（讨论组、直播群）的会话类型
- 支持文本、表情、图片、语音、自定义消息的消息类型
- 支持 APNs 离线推送（上报 token、前后台切换事件上报）
- 消息本地存储

### IM Flutter SDK（无 UI） 0.0.1-1.0.2 @2020.12.01
- Flutter SDK 首发
- 邀请用户参与内测

## 联系我们[](id:contact)
如果您在接入使用过程中有任何疑问，请加入 QQ 群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/eacb194c77a76b5361b2ae983ae63260.png)
