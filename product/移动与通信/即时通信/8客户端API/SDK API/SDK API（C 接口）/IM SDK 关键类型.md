## 常用宏和基础配置选项


### TIMResult

调用接口的返回值。

| 名称 | 含义 |
|-----|-----|
| TIM_SUCC | 接口调用成功 |
| TIM_ERR_SDKUNINIT | 接口调用失败，IM SDK 未初始化 |
| TIM_ERR_NOTLOGIN | 接口调用失败，用户未登录 |
| TIM_ERR_JSON | 接口调用失败，错误的 JSON 格式或 JSON Key |
| TIM_ERR_PARAM | 接口调用失败，参数错误 |
| TIM_ERR_CONV | 接口调用失败，无效的会话 |
| TIM_ERR_GROUP | 接口调用失败，无效的群组 |

>?若接口参数中有回调，只有当接口返回 TIM_SUCC 时，回调才会被调用。


### TIMLogLevel

日志级别。

| 名称 | 含义 |
|-----|-----|
| kTIMLog_Off | 关闭日志输出 |
| kTIMLog_Test | 全量日志 |
| kTIMLog_Verbose | 开发调试过程中一些详细信息日志 |
| kTIMLog_Debug | 调试日志 |
| kTIMLog_Info | 信息日志 |
| kTIMLog_Warn | 警告日志 |
| kTIMLog_Error | 错误日志 |
| kTIMLog_Assert | 断言日志 |

### TIMLoginStatus

登录状态。

| 名称 | 含义 |
|-----|-----|
| kTIMLoginStatus_Logined | 已登录 |
| kTIMLoginStatus_Logining | 登录中 |
| kTIMLoginStatus_UnLogined | 未登录 |
| kTIMLoginStatus_Logouting | 登出中 |

### TIMNetworkStatus

连接事件类型。

| 名称 | 含义 |
|-----|-----|
| kTIMConnected | 已连接 |
| kTIMDisconnected | 失去连接 |
| kTIMConnecting | 正在连接 |
| kTIMConnectFailed | 连接失败 |

### TIMConvEvent

会话事件类型。

| 名称 | 含义 |
|-----|-----|
| kTIMConvEvent_Add | 会话新增，例如收到一条新消息，产生一个新的会话是事件触发 |
| kTIMConvEvent_Del | 会话删除，例如自己删除某会话时会触发 |
| kTIMConvEvent_Update | 会话更新，会话内消息的未读计数变化和收到新消息时触发 |
| kTIMConvEvent_Start | 会话开始 |
| kTIMConvEvent_Finish | 会话结束 |

### TIMConvType

会话类型。

| 名称 | 含义 |
|-----|-----|
| kTIMConv_Invalid | 无效会话 |
| kTIMConv_C2C | 个人会话 |
| kTIMConv_Group | 群组会话 |
| kTIMConv_System | 系统会话 |

### TIMPlatform

平台信息。

| 名称 | 含义 |
|-----|-----|
| kTIMPlatform_Other | 未知平台 |
| kTIMPlatform_Windows | Windows 平台 |
| kTIMPlatform_Android | Android 平台 |
| kTIMPlatform_IOS | iOS 平台 |
| kTIMPlatform_Mac | MacOS 平台 |
| kTIMPlatform_Simulator | iOS 模拟器平台 |

### SdKConfig

初始化 IM SDK 的配置。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMSdkConfigConfigFilePath | string | 只写（必填） | 配置文件路径 |
| kTIMSdkConfigLogFilePath | string | 只写（必填） | 日志文件路径 |
| kTIMSdkConfigJavaVM | uint64 | 只写（选填） | 配置 Android 平台的 Java 虚拟机指针 |

### TIMGroupMemberInfoFlag

群组成员信息标识。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupMemberInfoFlag_None | 无 |
| kTIMGroupMemberInfoFlag_JoinTime | 加入时间 |
| kTIMGroupMemberInfoFlag_MsgFlag | 群消息接收选项 |
| kTIMGroupMemberInfoFlag_MsgSeq | 成员已读消息 seq |
| kTIMGroupMemberInfoFlag_MemberRole | 成员角色 |
| kTIMGroupMemberInfoFlag_ShutupUntill | 禁言时间。当该值为0时表示没有被禁言 |
| kTIMGroupMemberInfoFlag_NameCard | 群名片 |

### TIMGroupMemberRoleFlag

群组成员角色标识。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupMemberRoleFlag_All | 获取全部角色类型 |
| kTIMGroupMemberRoleFlag_Owner | 获取所有者（群主） |
| kTIMGroupMemberRoleFlag_Admin | 获取管理员，不包括群主 |
| kTIMGroupMemberRoleFlag_Member | 获取普通群成员，不包括群主和管理员 |

### GroupMemberGetInfoOption

获取群组成员信息的选项。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupMemberGetInfoOptionInfoFlag | uint64 [TIMGroupMemberInfoFlag](#timgroupmemberinfoflag) | 读写（选填） | 根据想要获取的信息过滤，默认值为 0xffffffff（获取全部信息） |
| kTIMGroupMemberGetInfoOptionRoleFlag | uint64 [TIMGroupMemberRoleFlag](#timgroupmemberroleflag) | 读写（选填） | 根据成员角色过滤，默认值为 kTIMGroupMemberRoleFlag_All，获取所有角色 |
| kTIMGroupMemberGetInfoOptionCustomArray | array string | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

### TIMGroupGetInfoFlag

群组成员信息标识。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupInfoFlag_None | - |
| kTIMGroupInfoFlag_Name | 群组名称 |
| kTIMGroupInfoFlag_CreateTime | 群组创建时间 |
| kTIMGroupInfoFlag_OwnerUin | 群组创建者帐号 |
| kTIMGroupInfoFlag_Seq | - |
| kTIMGroupInfoFlag_LastTime | 群组信息最后修改时间 |
| kTIMGroupInfoFlag_NextMsgSeq | - |
| kTIMGroupInfoFlag_LastMsgTime | 最新群组消息时间 |
| kTIMGroupInfoFlag_AppId | - |
| kTIMGroupInfoFlag_MemberNum | 群组成员数量 |
| kTIMGroupInfoFlag_MaxMemberNum | 群组成员最大数量 |
| kTIMGroupInfoFlag_Notification | 群公告内容 |
| kTIMGroupInfoFlag_Introduction | 群简介内容 |
| kTIMGroupInfoFlag_FaceUrl | 群头像 URL |
| kTIMGroupInfoFlag_AddOpton | 加群选项 |
| kTIMGroupInfoFlag_GroupType | 群类型 |
| kTIMGroupInfoFlag_LastMsg | 群组内最新一条消息 |
| kTIMGroupInfoFlag_OnlineNum | 群组在线成员数 |
| kTIMGroupInfoFlag_Visible | 群组是否可见 |
| kTIMGroupInfoFlag_Searchable | 群组是否可以搜索 |
| kTIMGroupInfoFlag_ShutupAll | 群组是否全禁言 |

### GroupGetInfoOption

获取群组信息的选项。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetInfoOptionInfoFlag | uint64 [TIMGroupGetInfoFlag](#timgroupgetinfoflag) | 读写（选填） | 根据想要获取的信息过滤，默认值为 0xffffffff（获取全部信息） |
| kTIMGroupGetInfoOptionCustomArray | array string | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

### UserConfig

用于配置信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMUserConfigIsReadReceipt | bool | 只写（选填） | true 表示要收已读回执事件 |
| kTIMUserConfigIsSyncReport | bool | 只写（选填） | true 表示服务端要删掉已读状态 |
| kTIMUserConfigIsIngoreGroupTipsUnRead | bool | 只写（选填） | true 表示群 tips 不计入群消息已读计数 |
| kTIMUserConfigIsDisableStorage | bool | 只写（选填） | 是否禁用本地数据库，true 表示禁用，false 表示不禁用。默认是 false |
| kTIMUserConfigGroupGetInfoOption | object [GroupGetInfoOption](#groupgetinfooption) | 只写（选填） | 获取群组信息默认选项 |
| kTIMUserConfigGroupMemberGetInfoOption | object [GroupMemberGetInfoOption](#groupmembergetinfooption) | 只写（选填） | 获取群组成员信息默认选项 |

### HttpProxyInfo

HTTP 代理信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMHttpProxyInfoIp | string | 只写（必填） | 代理的 IP |
| kTIMHttpProxyInfoPort | int | 只写（必填） | 代理的端口 |

### Socks5ProxyInfo

SOCKS5 代理信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMSocks5ProxyInfoIp | string | 只写（必填） | SOCKS5 代理的 IP |
| kTIMSocks5ProxyInfoPort | int | 只写（必填） | SOCKS5 代理的端口 |
| kTIMSocks5ProxyInfoUserName | string | 只写（选填） | 认证的用户名 |
| kTIMSocks5ProxyInfoPassword | string | 只写（选填） | 认证的密码 |

### SetConfig

**更新配置**

- 自定义数据。
开发者可以自定义的数据（长度限制为64个字节），IM SDK 只负责透传给即时通信 IM 后台后，可以通过第三方回调 [状态变更回调](https://cloud.tencent.com/document/product/269/2570) 告知开发者业务后台。
- HTTP 代理。
HTTP 代理主要用在发送图片、语音、文件、微视频等消息时，将相关文件上传到 COS，以及接收到图片、语音、文件、微视频等消息，将相关文件下载到本地时用到。设置时，设置的 IP 不能为空，端口不能为0（0端口不可用）。如果需要取消 HTTP 代理，只需将代理的 IP 设置为空字符串，端口设置为0。
- SOCKS5 代理。
SOCKS5 代理需要在初始化之前设置。设置之后 IM SDK 发送的所有协议会通过 SOCKS5 代理服务器发送的即时通信 IM 后台。


| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMSetConfigLogLevel | uint [TIMLogLevel](#timloglevel) | 只写（选填） | 输出到日志文件的日志级别 |
| kTIMSetConfigCackBackLogLevel | uint [TIMLogLevel](#timloglevel) | 只写（选填） | 日志回调的日志级别 |
| kTIMSetConfigIsLogOutputConsole | bool | 只写（选填） | 是否输出到控制台 |
| kTIMSetConfigUserConfig | object [UserConfig](#userconfig) | 只写（选填） | 用户配置 |
| kTIMSetConfigUserDefineData | string | 只写（选填） | 自定义数据，如果需要，初始化前设置 |
| kTIMSetConfigHttpProxyInfo | object [HttpProxyInfo](#httpproxyinfo) | 只写（选填） | 设置 HTTP 代理，如果需要，在发送图片、文件、语音、视频前设置 |
| kTIMSetConfigSocks5ProxyInfo | object [Socks5ProxyInfo](#socks5proxyinfo) | 只写（选填） | 设置 SOCKS5 代理，如果需要，初始化前设置 |
| kTIMSetConfigIsOnlyLocalDNSSource | bool | 只写（选填） | 如果为 true，SDK 内部会在选择最优 IP 时只使用 LocalDNS |

## 消息关键类型

消息相关宏定义，以及相关结构成员存取 JSON Key 定义。

### IOSOfflinePushConfig

消息在 iOS 系统上的离线推送配置。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMIOSOfflinePushConfigTitle | string | 读写 | 通知标题 |
| kTIMIOSOfflinePushConfigSound | string | 读写 | 当前消息在 iOS 设备上的离线推送提示声音 URL。当设置为 push。no_sound 时表示无提示音无振动 |
| kTIMIOSOfflinePushConfigIgnoreBadge | bool | 读写 | 是否忽略 badge 计数。若为 true，在 iOS 接收端，这条消息不会使 App 的应用图标未读计数增加 |

### TIMAndroidOfflinePushNotifyMode

Android 离线推送模式。

| 名称 | 含义 |
|-----|-----|
| kTIMAndroidOfflinePushNotifyMode_Normal | 普通通知栏消息模式，离线消息下发后，点击通知栏消息直接启动应用，不会给应用进行回调 |
| kTIMAndroidOfflinePushNotifyMode_Custom | 自定义消息模式，离线消息下发后，点击通知栏消息会给应用进行回调 |

### AndroidOfflinePushConfig

消息在 Android 系统上的离线推送配置。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMAndroidOfflinePushConfigTitle | string | 读写 | 通知标题 |
| kTIMAndroidOfflinePushConfigSound | string | 读写 | 当前消息在 Android 设备上的离线推送提示声音 URL |
| kTIMAndroidOfflinePushConfigNotifyMode | uint [TIMAndroidOfflinePushNotifyMode](#timandroidofflinepushnotifymode) | 读写 | 当前消息的通知模式 |
| kTIMAndroidOfflinePushConfigOPPOChannelID | string | 读写 | OPPO 的 ChannelID |

>?ChannelID 的说明
Android8。0系统以上通知栏消息增加了 channelid 的设置，目前 oppo 要求必须填写，否则在8。0及以上的 OPPO 手机上会收不到离线推送消息。后续可能会增加 xiaomi_channel_id_，huawei_channel_id 等。


### TIMOfflinePushFlag

推送规则。

| 名称 | 含义 |
|-----|-----|
| kTIMOfflinePushFlag_Default | 按照默认规则进行推送 |
| kTIMOfflinePushFlag_NoPush | 不进行推送 |

### OfflinePushConfig

消息离线推送配置。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMOfflinePushConfigDesc | string | 读写 | 当前消息在对方收到离线推送时候展示内容 |
| kTIMOfflinePushConfigExt | string | 读写 | 当前消息离线推送时的扩展字段 |
| kTIMOfflinePushConfigFlag | uint [TIMOfflinePushFlag](#timofflinepushflag) | 读写 | 当前消息是否允许推送，默认允许推送 kTIMOfflinePushFlag_Default |
| kTIMOfflinePushConfigIOSConfig | object [IOSOfflinePushConfig](#iosofflinepushconfig) | 读写 | iOS 离线推送配置 |
| kTIMOfflinePushConfigAndroidConfig | object [AndroidOfflinePushConfig](#androidofflinepushconfig) | 读写 | Android 离线推送配置 |

### TIMMsgStatus

消息当前状态定义。

| 名称 | 含义 |
|-----|-----|
| kTIMMsg_Sending | 消息正在发送 |
| kTIMMsg_SendSucc | 消息发送成功 |
| kTIMMsg_SendFail | 消息发送失败 |
| kTIMMsg_Deleted | 消息已删除 |
| kTIMMsg_LocalImported | 消息导入状态 |
| kTIMMsg_Revoked | 消息撤回状态 |

### TIMMsgPriority

标识消息的优先级，数字越大优先级越低。

| 名称 | 含义 |
|-----|-----|
| kTIMMsgPriority_High | 优先级最高，一般为红包或者礼物消息 |
| kTIMMsgPriority_Normal | 表示优先级次之，建议为普通消息 |
| kTIMMsgPriority_Low | 建议为点赞消息等 |
| kTIMMsgPriority_Lowest | 优先级最低，一般为成员进退群通知（后台下发） |

### Message

消息 JSON Keys。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgElemArray | array [Elem](#elem) | 读写（必填） | 消息内元素列表 |
| kTIMMsgConvId | string | 读写（选填） | 消息所属会话 ID |
| kTIMMsgConvType | uint [TIMConvType](#timconvtype) | 读写（选填） | 消息所属会话类型 |
| kTIMMsgSender | string | 读写（选填） | 消息的发送者 |
| kTIMMsgPriority | uint [TIMMsgPriority](#timmsgpriority) | 读写（选填） | 消息优先级 |
| kTIMMsgClientTime | uint64 | 读写（选填） | 客户端时间 |
| kTIMMsgServerTime | uint64 | 读写（选填） | 服务端时间 |
| kTIMMsgIsFormSelf | bool | 读写（选填） | 消息是否来自自己 |
| kTIMMsgPlatform | bool | 读写（选填） | 发送消息的平台 |
| kTIMMsgIsRead | bool | 读写（选填） | 消息是否已读 |
| kTIMMsgIsOnlineMsg | bool | 读写（选填） | 消息是否是在线消息，false 表示普通消息，true 表示阅后即焚消息，默认为 false |
| kTIMMsgIsPeerRead | bool | 只读 | 消息是否被会话对方已读 |
| kTIMMsgStatus | uint [TIMMsgStatus](#timmsgstatus) | 读写（选填） | 消息当前状态 |
| kTIMMsgUniqueId | uint64 | 只读 | 消息的唯一标识，推荐使用 kTIMMsgMsgId |
| kTIMMsgMsgId | string | 只读 | 消息的唯一标识 |
| kTIMMsgRand | uint64 | 只读 | 消息的随机码 |
| kTIMMsgSeq | uint64 | 只读 | 消息序列 |
| kTIMMsgCustomInt | uint32_t | 读写（选填） | 自定义整数值字段（本地保存，不会发送到对端，程序卸载重装后失效） |
| kTIMMsgCloudCustomStr | string | 读写（选填） | 消息自定义数据（云端保存，会发送到对端，程序卸载重装后还能拉取到） |
| kTIMMsgIsExcludedFromUnreadCount | bool | 读写（选填） | 消息是否不计入未读计数：默认为 NO，表明需要计入未读计数，设置为 YES，表明不需要计入未读计数 |
| kTIMMsgGroupAtUserArray | string | 读写（选填） |  群消息中被 @ 的用户 UserID 列表（即该消息都 @ 了哪些人），如果需要 @ALL ，请传入 kImSDK_MesssageAtALL 字段 |
| kTIMMsgIsForwardMessage | bool | 读写（选填） | 如果需要转发一条消息，不能直接调用 sendMessage 接口发送原消息，原消息 kTIMMsgIsForwardMessage 设置为 true 再发送 |
| kTIMMsgSenderProfile | object [UserProfile](#userprofile) | 读写（选填） | 消息的发送者的用户资料 |
| kTIMMsgSenderGroupMemberInfo | object [GroupMemberInfo](#groupmemberinfo) | 读写（选填） | 消息发送者在群里面的信息，只有在群会话有效。目前仅能获取字段kTIMGroupMemberInfoIdentifier、kTIMGroupMemberInfoNameCard 其他的字段建议通过`TIMGroupGetMemberInfoList`接口获取 |
| kTIMMsgOfflinePushConfig | object [OfflinePushConfig](#offlinepushconfig) | 读写（选填） | 消息的离线推送设置 |
| kTIMMsgExcludedFromLastMessage | string | 读写（选填） | 是否作为会话的 lasgMessage，true - 不作为，false - 作为 |

>?
- 对应 Elem 的顺序。
目前文件和语音 Elem 不一定会按照添加顺序传输，其他 Elem 按照顺序，不过建议不要过于依赖 Elem 顺序进行处理，应该逐个按照 Elem 类型处理，防止异常情况下进程 Crash。
- 针对群组的红包和点赞消息。
对于直播场景，会有点赞和发红包功能，点赞相对优先级较低，红包消息优先级较高，具体消息内容可以使用自定义消息 [CustomElem](#customelem) 进行定义，发送消息时，可通过`kTIMMsgPriority`定义消息优先级。
- 阅后即焚消息。
开发者通过设置`kTIMMsgIsOnlineMsg`字段为 true 时，表示发送阅后即焚消息，该消息有如下特性。
 - C2C 会话，当此消息发送时，只有对方在线，对方才会收到。如果当时离线，后续再登录也收不到此消息。
 - 群会话，当此消息发送时，只有群里在线的成员才会收到。如果当时离线，后续再登录也收不到此消息。
 - 此消息服务器不会保存。
 - 此消息不计入未读计数。
 - 此消息在本地不会存储。
- 消息自定义字段。
开发者可以对消息增加自定义字段，如自定义整数（通过`kTIMMsgCustomInt`指定）、自定义二进制数据（通过`kTIMMsgCustomStr`指定，必须转换成 String，JSON 不支持二进制传输），可以根据这两个字段做出各种不同效果，例如语音消息是否已经播放等等。另外需要注意，此自定义字段仅存储于本地，不会同步到 Server，更换终端获取不到。


### MessageReceipt

消息已读回执。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgReceiptConvId | string | 只读 | 会话 ID |
| kTIMMsgReceiptConvType | uint [TIMConvType](#timconvtype) | 只读 | 会话类型 |
| kTIMMsgReceiptTimeStamp | uint64 | 只读 | 时间戳 |

### TIMElemType

元素的类型。

| 名称 | 含义 |
|-----|-----|
| kTIMElem_Text | 文本元素 |
| kTIMElem_Image | 图片元素 |
| kTIMElem_Sound | 声音元素 |
| kTIMElem_Custom | 自定义元素 |
| kTIMElem_File | 文件元素 |
| kTIMElem_GroupTips | 群组系统消息元素 |
| kTIMElem_Face | 表情元素 |
| kTIMElem_Location | 位置元素 |
| kTIMElem_GroupReport | 群组系统通知元素 |
| kTIMElem_Video | 视频元素 |
| kTIMElem_FriendChange | 关系链变更消息元素 |
| kTIMElem_ProfileChange | 资料变更消息元素 |
| kTIMElem_Merge | 合并消息元素 |
| kTIMElem_Invalid | 未知元素类型 |

### Elem

元素的类型。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMElemType | uint [TIMElemType](#timelemtype) | 读写（必填） | 元素类型 |

### TextElem

文本元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMTextElemContent | string | 读写（必填） | 文本内容 |

### FaceElem

表情元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFaceElemIndex | int | 读写（必填） | 表情索引 |
| kTIMFaceElemBuf | string | 读写（选填） | 其他额外数据，可由用户自定义填写。若要传输二进制，麻烦先转码成字符串。JSON 只支持字符串 |

>?IM SDK 并不提供表情包，如果开发者有表情包，可使用`kTIMFaceElemIndex`存储表情在表情包中的索引，由用户自定义。或者直接使用`kTIMFaceElemBuf`存储表情二进制信息（必须转换成 String，JSON 不支持二进制传输），由用户自定义，IM SDK 内部只做透传。


### LocationElem

位置元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMLocationElemDesc | string | 读写（选填） | 位置描述 |
| kTIMLocationElemLongitude | double | 读写（必填） | 经度 |
| kTIMLocationElemlatitude | double | 读写（必填） | 纬度 |

### TIMImageLevel

图片质量级别。

| 名称 | 含义 |
|-----|-----|
| kTIMImageLevel_Orig | 原图发送 |
| kTIMImageLevel_Compression | 高压缩率图发送（图片较小，默认值） |
| kTIMImageLevel_HD | 高清图发送（图片较大） |

### ImageElem

图片元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMImageElemOrigPath | string | 读写（必填） | 发送图片的路径 |
| kTIMImageElemLevel | uint [TIMImageLevel](#timimagelevel) | 读写（必填） | 发送图片的质量级别 |
| kTIMImageElemFormat | int | 读写 | 发送图片格式 |
| kTIMImageElemOrigId | string | 只读 | 原图 ID |
| kTIMImageElemOrigPicHeight | int | 只读 | 原图的图片高度 |
| kTIMImageElemOrigPicWidth | int | 只读 | 原图的图片宽度 |
| kTIMImageElemOrigPicSize | int | 只读 | 原图的图片大小 |
| kTIMImageElemThumbId | string | 只读 | 缩略图 ID |
| kTIMImageElemThumbPicHeight | int | 只读 | 缩略图的图片高度 |
| kTIMImageElemThumbPicWidth | int | 只读 | 缩略图的图片宽度 |
| kTIMImageElemThumbPicSize | int | 只读 | 缩略图的图片大小 |
| kTIMImageElemLargeId | string | 只读 | 大图片 ID |
| kTIMImageElemLargePicHeight | int | 只读 | 大图片的图片高度 |
| kTIMImageElemLargePicWidth | int | 只读 | 大图片的图片宽度 |
| kTIMImageElemLargePicSize | int | 只读 | 大图片的图片大小 |
| kTIMImageElemOrigUrl | string | 只读 | 原图 URL |
| kTIMImageElemThumbUrl | string | 只读 | 缩略图 URL |
| kTIMImageElemLargeUrl | string | 只读 | 大图片 URL |
| kTIMImageElemTaskId | int | 只读 | 任务 ID |

>?
- 图片规格说明：每幅图片有三种规格，分别是 Original（原图）、Large（大图）、Thumb（缩略图）。
 - 原图：指用户发送的原始图片，尺寸和大小都保持不变。
 - 大图：是将原图等比压缩，压缩后宽、高中较小的一个等于720像素。
 - 缩略图：是将原图等比压缩，压缩后宽、高中较小的一个等于198像素。
- 如果原图尺寸就小于198像素，则三种规格都保持原始尺寸，不需压缩。
- 如果原图尺寸在198 - 720之间，则大图和原图一样，不需压缩。
- 在手机上展示图片时，建议优先展示缩略图，用户单击缩略图时再下载大图，单击大图时再下载原图。当然开发者也可以选择跳过大图，单击缩略图时直接下载原图。
- 在 Pad 或 PC 上展示图片时，由于分辨率较大，且基本都是 Wi-Fi 或有线网络，建议直接显示大图，用户单击大图时再下载原图。


### SoundElem

声音元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMSoundElemFilePath | string | 读写（必填） | 语音文件路径，需要开发者自己先保存语言然后指定路径 |
| kTIMSoundElemFileSize | int | 读写（必填） | 语言数据文件大小，以秒为单位 |
| kTIMSoundElemFileTime | int | 读写（必填） | 语音时长 |
| kTIMSoundElemFileId | string | 只读 | 语音 ID |
| kTIMSoundElemBusinessId | int | 只读 | 下载时用到的 businessID |
| kTIMSoundElemDownloadFlag | int | 只读 | 是否需要申请下载地址（0：需要申请，1：到 cos 申请，2：不需要申请，直接拿 URL 下载） |
| kTIMSoundElemUrl | string | 只读 | 下载的 URL |
| kTIMSoundElemTaskId | int | 只读 | 任务 ID |

>?
- 语音是否已经播放，可使用消息自定义字段实现，如定义一个字段值0表示未播放，1表示播放，当用户单击播放后可设置改字段的值为1。
- 一条消息只能添加一个声音元素，添加多个声音元素时，发送消息可能失败。


### CustomElem

自定义元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMCustomElemData | string | 读写 | 数据，支持二进制数据 |
| kTIMCustomElemDesc | string | 读写 | 自定义描述 |
| kTIMCustomElemExt | string | 读写 | 后台推送对应的 ext 字段 |
| kTIMCustomElemSound | string | 读写 | 自定义声音 |

>?自定义消息是指当内置的消息类型无法满足特殊需求，开发者可以自定义消息格式，`kTIMCustomElemData` 可以存储二进制信息（必须转换成 String，JSON 不支持二进制传输） 内容全部由开发者定义，IM SDK 只负责透传。



使用  kTIMCustomElemData  发送二进制数据

```c++
// 假设 pBuffer 是指向二进制数据的指针，nLength 表示二进制数据的长度
char * pBuffer;
int length = xxx;

// 对二进制数据做 base16 编码，转换为字符串
char * pBase16Buf = (char *)malloc(2 * length + 1);
memset(pBase16Buf, 0, 2 * length + 1);
for (int i = 0; i < length; ++i) {
    snprintf(pBase16Buf + 2 * i, 3, "%02X", pBuffer[i]); 
}
std::string strBase16 = std::string(pBase16Buf, strlen(pBase16Buf));
free(pBase16Buf);

// 创建 kTIMCustomElemData 类型的 element
json::Object json_element;
json_element[kTIMElemType] = kTIMElem_Custom;
json_element[kTIMCustomElemData] = strBase16.c_str();
json_element[kTIMCustomElemDesc] = "description";
json_element_array.push_back(json_element);
```

 使用 kTIMCustomElemData  接收二进制数据

```c++
// 假设 json_element 是 kTIMCustomElemData 类型的 element，从中解析出 kTIMCustomElemData 字段
std::string strCustomData = json_element[kTIMCustomElemData];

// 对 strCustomData 做 base16 解码，得到原始二进制数据
char * pCustomData = (char*)(strCustomData.c_str());
int customDataLength = (int)(strCustomData.length());

int length = customDataLength / 2;
char * pBuffer = (char *)malloc(length + 1);
memset(pBuffer, 0, length + 1);
for (int i = 0; i < length; ++i) {
    sscanf(pCustomData + 2 * i, "%02X", (char*)(pBuffer + i));
}

// 在这里使用二进制数据: pBuffer 是指向二进制数据的指针，length 表示二进制数据的长度
...
// 释放 pBuffer
free(pBuffer);
```


### FileElem

文件元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFileElemFilePath | string | 读写（必填） | 文件所在路径（包含文件名） |
| kTIMFileElemFileName | string | 读写（必填） | 文件名，显示的名称。不设置该参数时，kTIMFileElemFileName 默认为 kTIMFileElemFilePath 指定的文件路径中的文件名 |
| kTIMFileElemFileSize | int | 读写（必填） | 文件大小 |
| kTIMFileElemFileId | string | 只读 | 文件 ID |
| kTIMFileElemBusinessId | int | 只读 | 下载时用到的 businessID |
| kTIMFileElemDownloadFlag | int | 只读 | 文件下载 flag |
| kTIMFileElemUrl | string | 只读 | 文件下载的 URL |
| kTIMFileElemTaskId | int | 只读 | 任务 ID |

>?一条消息只能添加一个文件元素，添加多个文件时，发送消息可能失败。


### VideoElem

视频元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMVideoElemVideoType | string | 读写（必填） | 视频文件类型，发送消息时进行设置 |
| kTIMVideoElemVideoSize | uint | 读写（必填） | 视频文件大小 |
| kTIMVideoElemVideoDuration | uint | 读写（必填） | 视频时长，发送消息时进行设置 |
| kTIMVideoElemVideoPath | string | 读写（必填） | 适配文件路径 |
| kTIMVideoElemVideoId | string | 只读 | 视频 ID |
| kTIMVideoElemBusinessId | int | 只读 | 下载时用到的 businessID |
| kTIMVideoElemVideoDownloadFlag | int | 只读 | 视频文件下载 flag |
| kTIMVideoElemVideoUrl | string | 只读 | 视频文件下载的 URL |
| kTIMVideoElemImageType | string | 读写（必填） | 截图文件类型，发送消息时进行设置 |
| kTIMVideoElemImageSize | uint | 读写（必填） | 截图文件大小 |
| kTIMVideoElemImageWidth | uint | 读写（必填） | 截图高度，发送消息时进行设置 |
| kTIMVideoElemImageHeight | uint | 读写（必填） | 截图宽度，发送消息时进行设置 |
| kTIMVideoElemImagePath | string | 读写（必填） | 保存截图的路径 |
| kTIMVideoElemImageId | string | 只读 | 截图 ID |
| kTIMVideoElemImageDownloadFlag | int | 只读 | 截图文件下载 flag |
| kTIMVideoElemImageUrl | string | 只读 | 截图文件下载的 URL |
| kTIMVideoElemTaskId | uint | 只读 | 任务 ID |


### MergerElem

合并消息元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMergerElemTitle | string | 读写（必填） | 合并消息 title |
| kTIMMergerElemAbstractArray | uint | 读写（必填） | 合并消息摘要列表 |
| kTIMMergerElemCompatibleText | uint | 读写（必填） | 合并消息兼容文本，低版本 SDK 如果不支持合并消息，默认会收到一条文本消息，文本消息的内容为 compatibleText，该参数不能为空 |
| kTIMMergerElemMsgArray | string | 读写（必填） | 消息列表（最大支持 300 条，消息对象必须是 kTIMMsg_SendSucc 状态，消息类型不能为 GroupTipsElem 或 GroupReportElem） |
| kTIMMergerElemLayersOverLimit | string | 只读 | 合并消息里面又包含合并消息我们称之为合并嵌套，合并嵌套层数不能超过 100 层，如果超过限制，layersOverLimit 会返回 YES，kTIMMergerElemTitle 和 kTIMMergerElemAbstractArray 为空，DownloadMergerMessage 会返回 ERR_MERGER_MSG_LAYERS_OVER_LIMIT 错误码 |
| kTIMMergerElemRelayPbKey | int | 只读 | native 端消息列表下载 key |
| kTIMMergerElemRelayJsonKey | int | 只读 | web 端消息列表下载 key |
| kTIMMergerElemRelayBuffer | string | 只读 | 转发消息的 buffer |

### TIMGroupTipGroupChangeFlag

群组信息修改的类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupTipChangeFlag_Unknown | 未知的修改 |
| kTIMGroupTipChangeFlag_Name | 修改群组名称 |
| kTIMGroupTipChangeFlag_Introduction | 修改群简介 |
| kTIMGroupTipChangeFlag_Notification | 修改群公告 |
| kTIMGroupTipChangeFlag_FaceUrl | 修改群头像 URL |
| kTIMGroupTipChangeFlag_Owner | 修改群所有者 |
| kTIMGroupTipChangeFlag_Custom | 修改群自定义信息 |
| kTIMGroupTipChangeFlag_Attribute | 群属性变更 (新增) |

### GroupTipGroupChangeInfo

群组系统消息-群组信息修改。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipGroupChangeInfoFlag | uint [TIMGroupTipGroupChangeFlag](#timgrouptipgroupchangeflag) | 只读 | 群消息修改群信息标志 |
| kTIMGroupTipGroupChangeInfoValue | string | 只读 | 修改的后值，不同的`info_flag`字段，具有不同的含义 |
| kTIMGroupTipGroupChangeInfoKey | string | 只读 | 自定义信息对应的`key`值，只有`info_flag`为`kTIMGroupTipChangeFlag_Custom`时有效 |

### GroupTipMemberChangeInfo

群组系统消息-群组成员禁言。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipMemberChangeInfoIdentifier | string | 只读 | 群组成员 ID |
| kTIMGroupTipMemberChangeInfoShutupTime | uint | 只读 | 禁言时间 |

### TIMGroupTipType

群组系统消息类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupTip_None | 无效的群提示 |
| kTIMGroupTip_Invite | 邀请加入提示 |
| kTIMGroupTip_Quit | 退群提示 |
| kTIMGroupTip_Kick | 踢人提示 |
| kTIMGroupTip_SetAdmin | 设置管理员提示 |
| kTIMGroupTip_CancelAdmin | 取消管理员提示 |
| kTIMGroupTip_GroupInfoChange | 群信息修改提示 |
| kTIMGroupTip_MemberInfoChange | 群成员信息修改提示 |

### GroupTipsElem

群组系统消息元素（针对所有群成员）。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipsElemTipType | uint [TIMGroupTipType](#timgrouptiptype) | 只读 | 群消息类型 |
| kTIMGroupTipsElemOpUser | string | 只读 | 操作者 ID |
| kTIMGroupTipsElemGroupName | string | 只读 | 群组名称 |
| kTIMGroupTipsElemGroupId | string | 只读 | 群组 ID |
| kTIMGroupTipsElemTime | uint | 只读 | 群消息时间，废弃 |
| kTIMGroupTipsElemUserArray | array string | 只读 | 被操作的帐号列表 |
| kTIMGroupTipsElemGroupChangeInfoArray | array [GroupTipGroupChangeInfo](#grouptipgroupchangeinfo) | 只读 | 群资料变更信息列表，仅当`tips_type`值为`kTIMGroupTip_GroupInfoChange`时有效 |
| kTIMGroupTipsElemMemberChangeInfoArray | array [GroupTipMemberChangeInfo](#grouptipmemberchangeinfo) | 只读 | 群成员变更信息列表，仅当`tips_type`值为`kTIMGroupTip_MemberInfoChange`时有效 |
| kTIMGroupTipsElemOpUserInfo | object [UserProfile](#userprofile) | 只读 | 操作者个人资料 |
| kTIMGroupTipsElemOpGroupMemberInfo | object [GroupMemberInfo](#groupmemberinfo) | 只读 | 群成员信息 |
| kTIMGroupTipsElemChangedUserInfoArray | array [UserProfile](#userprofile) | 只读 | 被操作者列表资料 |
| kTIMGroupTipsElemChangedGroupMemberInfoArray | array [GroupMemberInfo](#groupmemberinfo) | 只读 | 群成员信息列表 |
| kTIMGroupTipsElemMemberNum | uint | 只读 | 当前群成员数，只有当事件消息类型为`kTIMGroupTip_Invite`、`kTIMGroupTip_Quit`、`kTIMGroupTip_Kick`时有效 |
| kTIMGroupTipsElemPlatform | string | 只读 | 操作方平台信息 |

### TIMGroupReportType

群组系统通知类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupReport_None | 未知类型 |
| kTIMGroupReport_AddRequest | 申请加群（只有管理员会接收到） |
| kTIMGroupReport_AddAccept | 申请加群被同意（只有申请人自己接收到） |
| kTIMGroupReport_AddRefuse | 申请加群被拒绝（只有申请人自己接收到） |
| kTIMGroupReport_BeKicked | 被管理员踢出群（只有被踢者接收到） |
| kTIMGroupReport_Delete | 群被解散（全员接收） |
| kTIMGroupReport_Create | 创建群（创建者接收，不展示） |
| kTIMGroupReport_Invite | 无需被邀请者同意，拉入群中（例如工作群） |
| kTIMGroupReport_Quit | 主动退群（主动退出者接收，不展示） |
| kTIMGroupReport_GrantAdmin | 设置管理员（被设置者接收） |
| kTIMGroupReport_CancelAdmin | 取消管理员（被取消者接收） |
| kTIMGroupReport_GroupRecycle | 群已被回收（全员接收，不展示） |
| kTIMGroupReport_InviteReq | 被邀请者收到邀请，由被邀请者同意是否接受  |
| kTIMGroupReport_InviteAccept | 邀请加群被同意（只有发出邀请者会接收到） |
| kTIMGroupReport_InviteRefuse | 邀请加群被拒绝（只有发出邀请者会接收到） |
| kTIMGroupReport_ReadReport | 已读上报多终端同步通知（只有上报人自己收到） |
| kTIMGroupReport_UserDefine | 用户自定义通知（默认全员接收） |

### GroupReportElem

群组系统通知元素（针对个人）。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupReportElemReportType | uint [TIMGroupReportType](#timgroupreporttype) | 只读 | 类型 |
| kTIMGroupReportElemGroupId | string | 只读 | 群组 ID |
| kTIMGroupReportElemGroupName | string | 只读 | 群组名称 |
| kTIMGroupReportElemOpUser | string | 只读 | 操作者 ID |
| kTIMGroupReportElemMsg | string | 只读 | 操作理由 |
| kTIMGroupReportElemUserData | string | 只读 | 操作者填的自定义数据 |
| kTIMGroupReportElemOpUserInfo | object [UserProfile](#userprofile) | 只读 | 操作者个人资料 |
| kTIMGroupReportElemOpGroupMemberInfo | object [GroupMemberInfo](#groupmemberinfo) | 只读 | 操作者群内资料 |
| kTIMGroupReportElemPlatform | string | 只读 | 操作方平台信息 |

### TIMProfileChangeType

| 名称 | 含义 |
|-----|-----|
| kTIMProfileChange_None | 未知类型 |
| kTIMProfileChange_Profile | 资料修改 |

### ProfileChangeElem

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMProfileChangeElemChangeType | uint [TIMProfileChangeType](#timprofilechangetype) | 只读 | 资料变更类型 |
| kTIMProfileChangeElemFromIndentifier | string | 只读 | 资料变更用户的 UserID |
| kTIMProfileChangeElemUserProfileItem | object [UserProfileItem](#userprofileitem) | 只读 | 具体的变更信息，只有当`change_type`为`kTIMProfileChange_Profile`时有效 |

### TIMFriendChangeType

| 名称 | 含义 |
|-----|-----|
| kTIMFriendChange_None | 未知类型 |
| kTIMFriendChange_FriendAdd | 新增好友 |
| kTIMFriendChange_FriendDel | 删除好友 |
| kTIMFriendChange_PendencyAdd | 新增好友申请的未决 |
| kTIMFriendChange_PendencyDel | 删除好友申请的未决 |
| kTIMFriendChange_BlackListAdd | 加入黑名单 |
| kTIMFriendChange_BlackListDel | 从黑名单移除 |
| kTIMFriendChange_PendencyReadedReport | 未决已读上报 |
| kTIMFriendChange_FriendProfileUpdate | 好友数据更新 |
| kTIMFriendChange_FriendGroupAdd | 分组增加 |
| kTIMFriendChange_FriendGroupDel | 分组删除 |
| kTIMFriendChange_FriendGroupModify | 分组修改 |

### FriendProfileUpdate

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendProfileUpdateIdentifier | string | 只写 | 资料更新的好友的 UserID |
| kTIMFriendProfileUpdateItem | object [FriendProfileItem](#friendprofileitem) | 只写 | 资料更新的 Item |

### FriendChangeElem

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendChangeElemChangeType | uint [TIMFriendChangeType](#timfriendchangetype) | 只读 | 资料变更类型 |
| kTIMFriendChangeElemFriendAddIdentifierArray | array string | 只读 | 新增的好友 UserID 列表，只有当`change_type`为`kTIMFriendChange_FriendAdd`时有效 |
| kTIMFriendChangeElemFriendDelIdentifierArray | array string | 只读 | 删除的好友 UserID 列表，只有当`change_type`为`kTIMFriendChange_FriendDel`时有效 |
| kTIMFriendChangeElemFriendAddPendencyItemArray | array [FriendAddPendency](#friendaddpendency) | 只读 | 好友申请的未决列表，只有当`change_type`为`kTIMFriendChange_PendencyAdd`时有效 |
| kTIMFriendChangeElemPendencyDelIdentifierArray | array string | 只读 | 被删除的好友申请的未决列表，只有当`change_type`为`kTIMFriendChange_PendencyDel`时有效 |
| kTIMFriendChangeElemPendencyReadedReportTimestamp | uint64 | 只读 | 未决已读上报时间戳，只有当`change_type`为`kTIMFriendChange_PendencyReadedReport`时有效 |
| kTIMFriendChangeElemBlackListAddIdentifierArray | array string | 只读 | 新增的黑名单 UserID 列表，只有当`change_type`为`kTIMFriendChange_BlackListAdd`时有效 |
| kTIMFriendChangeElemBlackListDelIdentifierArray | array string | 只读 | 删除的黑名单 UserID 列表，只有当`change_type`为`kTIMFriendChange_BlackListDel`时有效 |
| kTIMFriendChangeElemFreindProfileUpdateItemArray | array [FriendProfileUpdate](#friendprofileupdate) | 只读 | 好友资料更新列表，只有当`change_type`为`kTIMFriendChange_FriendProfileUpdate`时有效 |
| kTIMFriendChangeElemFriendGroupAddIdentifierArray | array string | 只读 | 新增的好友分组名称列表，只有当`change_type`为`kTIMFriendChange_FriendGroupAdd`时有效 |
| kTIMFriendChangeElemFriendGroupDelIdentifierArray | array string | 只读 | 删除的好友分组名称列表，只有当`change_type`为`kTIMFriendChange_FriendGroupDel`时有效 |
| kTIMFriendChangeElemFriendGroupModifyIdentifierArray | array string | 只读 | 修改的好友分组名称列表，只有当`change_type`为`kTIMFriendChange_FriendGroupModify`时有效 |

### MsgBatchSendParam

消息群发接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgBatchSendParamIdentifierArray | array string | 只写（必填） | 接收群发消息的用户 ID 列表 |
| kTIMMsgBatchSendParamMsg | object [Message](#message) | 只写（必填） | 群发的消息 |

### MsgBatchSendResult

消息群发接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgBatchSendResultIdentifier | string | 只读 | 接收群发消息的用户 ID |
| kTIMMsgBatchSendResultCode | int [错误码](https://cloud.tencent.com/document/product/269/1671) | 只读 | 消息发送结果 |
| kTIMMsgBatchSendResultDesc | string | 只读 | 消息发送的描述 |
| kTIMMsgBatchSendResultMsg | object [Message](#message) | 只读 | 发送的消息 |

### MsgLocator

消息定位符。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgLocatorConvId | bool | 读写 | 要查找的消息所属的会话 ID |
| kTIMMsgLocatorConvType | bool | 读写 | 要查找的消息所属的会话类型 |
| kTIMMsgLocatorIsRevoked | bool | 读写（必填） | 要查找的消息是否是被撤回。true 表示被撤回的，false 表示未撤回的。默认为 false |
| kTIMMsgLocatorTime | uint64 | 读写（必填） | 要查找的消息的时间戳 |
| kTIMMsgLocatorSeq | uint64 | 读写（必填） | 要查找的消息的序列号 |
| kTIMMsgLocatorIsSelf | bool | 读写（必填） | 要查找的消息的发送者是否是自己。true 表示发送者是自己，false 表示发送者不是自己。默认为 false |
| kTIMMsgLocatorRand | uint64 | 读写（必填） | 要查找的消息随机码 |
| kTIMMsgLocatorUniqueId | uint64 | 读写（必填） | 要查找的消息的唯一标识 |

### MsgGetMsgListParam

消息获取接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgGetMsgListParamLastMsg | object [Message](#message) | 只写（选填） | 指定的消息，不允许为 null |
| kTIMMsgGetMsgListParamCount | uint | 只写（选填） | 从指定消息往后的消息数 |
| kTIMMsgGetMsgListParamIsRamble | bool | 只写（选填） | 是否漫游消息 |
| kTIMMsgGetMsgListParamIsForward | bool | 只写（选填） | 是否向前排序 |
| kTIMMsgGetMsgListParamLastMsgSeq | bool | 只写（选填） | 指定的消息的 seq |
| kTIMMsgGetMsgListParamTimeBegin | bool | 只写（选填） | 开始时间；UTC 时间戳， 单位：秒 |
| kTIMMsgGetMsgListParamTimePeriod | bool | 只写（选填） | 持续时间；单位：秒 |

### MsgDeleteParam

消息删除接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDeleteParamMsg | object [Message](#message) | 只写（选填） | 要删除的消息 |
| kTIMMsgDeleteParamIsRamble | bool | 只写（选填） | 是否删除本地/漫游所有消息。true 删除漫游消息，false 删除本地消息，默认值 false |

### TIMReceiveMessageOpt

消息接收选项。

| 名称 | 含义 |
|-----|-----|
| kTIMRecvMsgOpt_Receive | 在线正常接收消息，离线时会进行 APNs 推送 |
| kTIMRecvMsgOpt_Not_Receive | 不会接收到消息，离线不会有推送通知 |
| kTIMRecvMsgOpt_Not_Notify | 在线正常接收消息，离线不会有推送通知 |

### GetC2CRecvMsgOptResult

查询 C2C 消息接收选项的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgGetC2CRecvMsgOptResultIdentifier | string | 只写 | 用户ID |
| kTIMMsgDeleteParamIsRamble | TIMReceiveMessageOpt | 只写 | 消息接收选项 |


### TIMDownloadType

UUID 类型。

| 名称 | 含义 |
|-----|-----|
| kTIMDownload_VideoThumb | 视频缩略图 |
| kTIMDownload_File | 文件 |
| kTIMDownload_Video | 视频 |
| kTIMDownload_Sound | 声音 |

### DownloadElemParam

下载元素接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDownloadElemParamFlag | uint | 只写 | 从消息元素里面取出来，元素的下载类型 |
| kTIMMsgDownloadElemParamType | uint [TIMDownloadType](#timdownloadtype) | 只写 | 从消息元素里面取出来，元素的类型 |
| kTIMMsgDownloadElemParamId | string | 只写 | 从消息元素里面取出来，元素的 ID |
| kTIMMsgDownloadElemParamBusinessId | uint | 只写 | 从消息元素里面取出来，元素的 BusinessID |
| kTIMMsgDownloadElemParamUrl | string | 只写 | 从消息元素里面取出来，元素 URL |

### MsgDownloadElemResult

下载元素接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDownloadElemResultCurrentSize | uint | 只读 | 当前已下载的大小 |
| kTIMMsgDownloadElemResultTotalSize | uint | 只读 | 需要下载的文件总大小 |

### KeywordListMatchType

消息搜索关键字的组合类型。

| 名称 | 含义 |
|-----|-----|
| TIMKeywordListMatchType_Or |  |
| TIMKeywordListMatchType_And |  |

### MessageSearchParam

消息搜索参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgSearchParamKeywordArray | array string | 只写(必填) | 搜索关键字列表，最多支持5个。 |
| kTIMMsgSearchParamMessageTypeArray | array [TIMElemType]() | 只读 | 指定搜索的消息类型集合，传入空数组，表示搜索支持的全部类型消息（FaceElem 和 GroupTipsElem 暂不支持）取值详见 TIMElemType。 |
| kTIMMsgSearchParamConvId | string | 只写(必填) | 会话 ID |
| kTIMMsgSearchParamConvType | uint | 只写(必填) | 会话类型，如果设置 kTIMConv_Invalid，代表搜索全部会话。否则，代表搜索指定会话。 |
| kTIMMsgSearchParamSearchTimePosition | uint | 只写(必填) | 搜索的起始时间点。默认为0即代表从现在开始搜索。UTC 时间戳，单位：秒 |
| kTIMMsgSearchParamSearchTimePeriod | uint | 只写(必填) | 从起始时间点开始的过去时间范围，单位秒。默认为0即代表不限制时间范围，传24x60x60代表过去一天。 |
| kTIMMsgSearchParamPageIndex | uint | 只写(必填) | 分页的页号：用于分页展示查找结果，从零开始起步。首次调用：通过参数 pageSize = 10, pageIndex = 0 调用 searchLocalMessage，从结果回调中的 totalCount 可以获知总共有多少条结果。计算页数：可以获知总页数：totalPage = (totalCount % loadCount == 0) ? (totalCount / pageIndex) : (totalCount / pageIndex + 1) 。再次调用：可以通过指定参数 pageIndex （pageIndex < totalPage）返回后续页号的结果。 |
| kTIMMsgSearchParamPageSize | uint | 只写(必填) | 每页结果数量：用于分页展示查找结果，如不希望分页可将其设置成 0，但如果结果太多，可能会带来性能问题。 |
| kTIMMsgSearchParamKeywordListMatchType | uint | 只写(必填) | 关键字进行 Or 或者 And 进行搜索 |
| kTIMMsgSearchParamSenderIdentifierArray | uint | 只写(必填) | 按照发送者的 userid 进行搜索 |

### MessageSearchResultItem

消息搜索结果项。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgSearchResultItemConvId | string | 只读 | 会话 ID |
| kTIMMsgSearchResultItemConvType | uint | 只读 | 会话类型，如果设置 kTIMConv_Invalid，代表搜索全部会话。否则，代表搜索指定会话。 |
| kTIMMsgSearchResultItemTotalMessageCount | uint | 只读 | 当前会话一共搜索到了多少条符合要求的消息。 |
| kTIMMsgSearchResultItemMessageArray | array [Message]() | 只读 | 满足搜索条件的消息列表。 |

### MessageSearchResult

消息搜索结果返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgSearchResultTotalCount | uint | 只读 | 如果您本次搜索【指定会话】，那么返回满足搜索条件的消息总数量；如果您本次搜索【全部会话】，那么返回满足搜索条件的消息所在的所有会话总数量。 |
| kTIMMsgSearchResultItemConvType | uint | 只读 | 会话类型，如果设置 kTIMConv_Invalid，代表搜索全部会话。否则，代表搜索指定会话。 |
| kTIMMsgSearchResultItemArray | array [TIMMessageSearchResultItem]() | 只读 | 如果您本次搜索【指定会话】，那么返回结果列表只包含该会话结果；如果您本次搜索【全部会话】，那么对满足搜索条件的消息根据会话 ID 分组，分页返回分组结果；。 |

## 会话关键类型

会话相关宏定义，以及相关结构成员存取 JSON Key 定义。

### Draft

草稿信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMDraftMsg | object [Message](#message) | 只读 | 草稿内的消息 |
| kTIMDraftUserDefine | string | 只读 | 用户自定义数据 |
| kTIMDraftEditTime | uint | 只读 | 草稿最新编辑时间 |

### TIMGroupAtType

@ 类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroup_At_Me | @ 我 |
| kTIMGroup_At_All | @ 群里所有人 |
| kTIMGroup_At_All_At_ME | @ 群里所有人并且单独 @ 我 |

### GroupAtInfo

群 @ 信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupAtInfoSeq | uint64 | 只读 | @ 消息序列号，即带有 “@我” 或者 “@所有人” 标记的消息的序列号 |
| kTIMGroupAtInfoAtType | uint [TIMGroupAtType]() | 只读 | @ 提醒类型，分成 “@我” 、“@所有人” 以及 “@我并@所有人” 三类 |

### ConvInfo

会话信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMConvId | string | 只读 | 会话 ID |
| kTIMConvType | uint [TIMConvType](#timconvtype) | 只读 | 会话类型 |
| kTIMConvOwner | string | 只读 | 会话所有者 |
| kTIMConvUnReadNum | uint64 | 只读 | 会话未读计数 |
| kTIMConvActiveTime | uint64 | 只读 | 会话的激活时间 |
| kTIMConvIsHasLastMsg | bool | 只读 | 会话是否有最后一条消息 |
| kTIMConvLastMsg | object [Message](#message) | 只读 | 会话最后一条消息 |
| kTIMConvIsHasDraft | bool | 只读 | 会话是否有草稿 |
| kTIMConvDraft | object [Draft](#draft) | 只读（选填） | 会话草稿 |
| kTIMConvRecvOpt | uint [TIMReceiveMessageOpt]() | 只读（选填） | 消息接收选项 |
| kTIMConvGroupAtInfoArray | array [GroupAtInfo]() | 只读（选填） | 群会话 @ 信息列表，用于展示 “有人@我” 或 “@所有人” 这两种提醒状态 |
| kTIMConvIsPinned | object [Draft](#draft) | 只读（选填） | 是否置顶 |
| kTIMConvShowName | object [Draft](#draft) | 只读（选填） | 获取会话展示名称，其展示优先级如下：1、群组，群名称 C2C; 2、对方好友备注->对方昵称->对方的 userID |

### GetConversationListParam

获取指定的会话列表。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGetConversationListParamConvId | string | 只写 | 会话 ID |
| kTIMConvType | uint [TIMConvType](#timconvtype) | 只写 | 会话类型 |

### GetTotalUnreadNumberResult

获取会话未读消息个数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMConvGetTotalUnreadMessageCountResultUnreadCount | int | 只读 | 会话未读数 |

## 群组关键类型

群组相关宏定义，以及相关结构成员存取 JSON Key 定义。

### TIMGroupAddOption

群组加群选项。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupAddOpt_Forbid | 禁止加群 |
| kTIMGroupAddOpt_Auth | 需要管理员审批 |
| kTIMGroupAddOpt_Any | 任何人都可以加群 |

### TIMGroupType

群组类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroup_Public | 公开群（Public），成员上限 2000 人，任何人都可以申请加群，但加群需群主或管理员审批，适合用于类似 QQ 中由群主管理的兴趣群。 |
| kTIMGroup_Private | 工作群（Work），成员上限 200  人，不支持由用户主动加入，需要他人邀请入群，适合用于类似微信中随意组建的工作群（对应老版本的 Private 群）。 |
| kTIMGroup_ChatRoom | 会议群（Meeting），成员上限 6000 人，任何人都可以自由进出，且加群无需被审批，适合用于视频会议和在线培训等场景（对应老版本的 ChatRoom 群）。 |
| kTIMGroup_BChatRoom | 在线成员广播大群，推荐使用 直播群（AVChatRoom） |
| kTIMGroup_AVChatRoom | 直播群（AVChatRoom），人数无上限，任何人都可以自由进出，消息吞吐量大，适合用作直播场景中的高并发弹幕聊天室。 |
| kTIMGroup_Community | 社群（Community），成员上限 100000 人，任何人都可以自由进出，且加群无需被审批，适合用于知识分享和游戏交流等超大社区群聊场景。5.8 版本开始支持，需要您购买旗舰版套餐。 |

### TIMGroupMemberRole

群组成员角色类型。

| 名称 | 含义 |
|-----|-----|
| kTIMMemberRole_None | 未定义 |
| kTIMMemberRole_Normal | 群成员 |
| kTIMMemberRole_Admin | 管理员 |
| kTIMMemberRole_Owner | 超级管理员（群主） |

### GroupMemberInfoCustemString

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupMemberInfoCustemStringInfoKey | string | 只写 | 自定义字段的 key |
| kTIMGroupMemberInfoCustemStringInfoValue | string | 只写 | 自定义字段的 value |

### GroupMemberInfo

群组成员信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupMemberInfoIdentifier | string | 读写（必填） | 群组成员 ID |
| kTIMGroupMemberInfoGroupId | string | 只读 | 群组 ID |
| kTIMGroupMemberInfoJoinTime | uint | 只读 | 群组成员加入时间 |
| kTIMGroupMemberInfoMemberRole | uint [TIMGroupMemberRole](#timgroupmemberrole) | 读写（选填） | 群组成员角色 |
| kTIMGroupMemberInfoMsgFlag | uint | 只读 | 成员接收消息的选项 |
| kTIMGroupMemberInfoMsgSeq | uint | 只读 | - |
| kTIMGroupMemberInfoShutupTime | uint | 只读 | 成员禁言时间 |
| kTIMGroupMemberInfoNameCard | string | 只读 | 成员群名片 |
| kTIMGroupMemberInfoNickName | string | 只读 | 好友昵称 |
| kTIMGroupMemberInfoRemark | string | 只读 | 好友备注 |
| kTIMGroupMemberInfoFaceUrl | string | 只读 | 好友头像 |
| kTIMGroupMemberInfoCustomInfo | array [GroupMemberInfoCustemString](#groupmemberinfocustemstring) | 只读 | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

### GroupInfoCustemString

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupInfoCustemStringInfoKey | string | 只写 | 自定义字段的 key |
| kTIMGroupInfoCustemStringInfoValue | string | 只写 | 自定义字段的 value |

### CreateGroupParam

创建群组接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMCreateGroupParamGroupName | string | 只写（必填） | 群组名称 |
| kTIMCreateGroupParamGroupId | string | 只写（选填） | 群组ID,不填时创建成功回调会返回一个后台分配的群ID。如果创建社群（Community）需要自定义群组 ID ，那必须以 "@TGS#_" 作为前缀。 |
| kTIMCreateGroupParamGroupType | uint [TIMGroupType](#timgrouptype) | 只写（选填） | 群组类型，默认为 Public |
| kTIMCreateGroupParamGroupMemberArray | array [GroupMemberInfo](#groupmemberinfo) | 只写（选填） | 群组初始成员数组 |
| kTIMCreateGroupParamNotification | string | 只写（选填） | 群组公告 |
| kTIMCreateGroupParamIntroduction | string | 只写（选填） | 群组简介 |
| kTIMCreateGroupParamFaceUrl | string | 只写（选填） | 群组头像 URL |
| kTIMCreateGroupParamAddOption | uint [TIMGroupAddOption](#timgroupaddoption) | 只写（选填） | 加群选项，默认为 Any |
| kTIMCreateGroupParamMaxMemberCount | uint | 只写（选填） | 群组最大成员数 |
| kTIMCreateGroupParamCustomInfo | array [GroupInfoCustemString](#groupinfocustemstring) | 只读（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

### CreateGroupResult

创建群组接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMCreateGroupResultGroupId | string | 只读 | 创建的群 ID |

### GroupInviteMemberParam

邀请成员接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupInviteMemberParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupInviteMemberParamIdentifierArray | array string | 只写（必填） | 被邀请加入群组用户 ID 数组 |
| kTIMGroupInviteMemberParamUserData | string | 只写（选填） | 用于自定义数据 |

### HandleGroupMemberResult

群组基础信息。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupMember_HandledErr | 失败 |
| kTIMGroupMember_HandledSuc | 成功 |
| kTIMGroupMember_Included | 已是群成员 |
| kTIMGroupMember_Invited | 已发送邀请 |

### GroupInviteMemberResult

邀请成员接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupInviteMemberResultIdentifier | string | 只读 | 被邀请加入群组的用户 ID |
| kTIMGroupInviteMemberResultResult | uint [HandleGroupMemberResult](#handlegroupmemberresult) | 只读 | 邀请结果 |

### GroupDeleteMemberParam

删除成员接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDeleteMemberParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupDeleteMemberParamIdentifierArray | array string | 只写（必填） | 被删除群组成员数组 |
| kTIMGroupDeleteMemberParamUserData | string | 只写（选填） | 用于自定义数据 |

### GroupDeleteMemberResult

删除成员接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDeleteMemberResultIdentifier | string | 只读 | 删除的成员 ID |
| kTIMGroupDeleteMemberResultResult | uint [HandleGroupMemberResult](#handlegroupmemberresult) | 只读 | 删除结果 |

### TIMGroupReceiveMessageOpt

群组消息接收选项。

| 名称 | 含义 |
|-----|-----|
| kTIMRecvGroupMsgOpt_ReceiveAndNotify | 接收群消息并提示 |
| kTIMRecvGroupMsgOpt_NotReceive | 不接收群消息，服务器不会进行转发 |
| kTIMRecvGroupMsgOpt_ReceiveNotNotify | 接收群消息，不提示 |

### GroupSelfInfo

群组内本人的信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupSelfInfoJoinTime | uint | 只读 | 加入群组时间 |
| kTIMGroupSelfInfoRole | uint | 只读 | 用户在群组中的角色 |
| kTIMGroupSelfInfoUnReadNum | uint | 只读 | 消息未读计数 |
| kTIMGroupSelfInfoMsgFlag | uint [TIMGroupReceiveMessageOpt](#timgroupreceivemessageopt) | 只读 | 群消息接收选项 |

### GroupBaseInfo

获取已加入群组列表接口的返回（群组基础信息）。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupBaseInfoGroupId | string | 只读 | 群组 ID |
| kTIMGroupBaseInfoGroupName | string | 只读 | 群组名称 |
| kTIMGroupBaseInfoGroupType | uint [TIMGroupType](#timgrouptype) | 只读 | 群组类型 |
| kTIMGroupBaseInfoFaceUrl | string | 只读 | 群组头像 URL |
| kTIMGroupBaseInfoInfoSeq | uint | 只读 | 群资料的 Seq，群资料的每次变更都会增加这个字段的值 |
| kTIMGroupBaseInfoLastestSeq | uint | 只读 | 群最新消息的 Seq。群组内每一条消息都有一条唯一的消息 Seq，且该 Seq 是按照发消息顺序而连续的。从1开始，群内每增加一条消息，LastestSeq 就会增加1 |
| kTIMGroupBaseInfoReadedSeq | uint | 只读 | 用户所在群已读的消息 Seq |
| kTIMGroupBaseInfoMsgFlag | uint | 只读 | 消息接收选项 |
| kTIMGroupBaseInfoIsShutupAll | bool | 只读 | 当前群组是否设置了全员禁言 |
| kTIMGroupBaseInfoSelfInfo | object [GroupSelfInfo](#groupselfinfo) | 只读 | 用户所在群的个人信息 |

### GroupDetailInfo

群组详细信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDetialInfoGroupId | string | 只读 | 群组 ID |
| kTIMGroupDetialInfoGroupType | uint [TIMGroupType](#timgrouptype) | 只读 | 群组类型 |
| kTIMGroupDetialInfoGroupName | string | 只读 | 群组名称 |
| kTIMGroupDetialInfoNotification | string | 只读 | 群组公告 |
| kTIMGroupDetialInfoIntroduction | string | 只读 | 群组简介 |
| kTIMGroupDetialInfoFaceUrl | string | 只读 | 群组头像 URL |
| kTIMGroupDetialInfoCreateTime | uint | 只读 | 群组创建时间 |
| kTIMGroupDetialInfoInfoSeq | uint | 只读 | 群资料的 Seq，群资料的每次变更都会增加这个字段的值 |
| kTIMGroupDetialInfoLastInfoTime | uint | 只读 | 群组信息最后修改时间 |
| kTIMGroupDetialInfoNextMsgSeq | uint | 只读 | 群最新消息的 Seq |
| kTIMGroupDetialInfoLastMsgTime | uint | 只读 | 最新群组消息时间 |
| kTIMGroupDetialInfoMemberNum | uint | 只读 | 群组当前成员数量 |
| kTIMGroupDetialInfoMaxMemberNum | uint | 只读 | 群组最大成员数量 |
| kTIMGroupDetialInfoAddOption | uint [TIMGroupAddOption](#timgroupaddoption) | 只读 | 群组加群选项 |
| kTIMGroupDetialInfoOnlineMemberNum | uint | 只读 | 群组在线成员数量 |
| kTIMGroupDetialInfoVisible | uint | 只读 | 群组成员是否对外可见 |
| kTIMGroupDetialInfoSearchable | uint | 只读 | 群组是否能被搜索 |
| kTIMGroupDetialInfoIsShutupAll | bool | 只读 | 群组是否被设置了全员禁言 |
| kTIMGroupDetialInfoOwnerIdentifier | string | 只读 | 群组所有者 ID |
| kTIMGroupDetialInfoCustomInfo | array [GroupInfoCustemString](#groupinfocustemstring) | 只读 | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

### GetGroupInfoResult

获取群组信息列表接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGetGroupInfoResultCode | int [错误码](https://cloud.tencent.com/document/product/269/1671) | 只读 | 获取群组详细信息的结果 |
| kTIMGetGroupInfoResultDesc | string | 只读 | 获取群组详细失败的描述信息 |
| kTIMGetGroupInfoResultInfo | object [GroupDetailInfo](#groupdetailinfo) | 只读 | 群组详细信息 |

### TIMGroupModifyInfoFlag

设置（修改）群组信息的类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupModifyInfoFlag_None | - |
| kTIMGroupModifyInfoFlag_Name | 修改群组名称 |
| kTIMGroupModifyInfoFlag_Notification | 修改群公告 |
| kTIMGroupModifyInfoFlag_Introduction | 修改群简介 |
| kTIMGroupModifyInfoFlag_FaceUrl | 修改群头像 URL |
| kTIMGroupModifyInfoFlag_AddOption | 修改群组添加选项 |
| kTIMGroupModifyInfoFlag_MaxMmeberNum | 修改群最大成员数 |
| kTIMGroupModifyInfoFlag_Visible | 修改群是否可见 |
| kTIMGroupModifyInfoFlag_Searchable | 修改群是否允许被搜索到 |
| kTIMGroupModifyInfoFlag_ShutupAll | 修改群是否全体禁言 |
| kTIMGroupModifyInfoFlag_Custom | 修改群自定义信息 |
| kTIMGroupModifyInfoFlag_Owner | 修改群主 |

### GroupModifyInfoParam

设置群信息接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupModifyInfoParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupModifyInfoParamModifyFlag | uint [TIMGroupModifyInfoFlag](#timgroupmodifyinfoflag) | 只写（必填） | 修改标识，可设置多个值按位或 |
| kTIMGroupModifyInfoParamGroupName | string | 只写（选填） | 修改群组名称，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Name`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamNotification | string | 只写（选填） | 修改群公告，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Notification`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamIntroduction | string | 只写（选填） | 修改群简介，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Introduction`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamFaceUrl | string | 只写（选填） | 修改群头像 URL，当`modify_flag`包含`kTIMGroupModifyInfoFlag_FaceUrl`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamAddOption | uint | 只写（选填） | 修改加群方式，当`modify_flag`包含`kTIMGroupModifyInfoFlag_AddOption`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamMaxMemberNum | uint | 只写（选填） | 修改群最大成员数，当`modify_flag`包含`kTIMGroupModifyInfoFlag_MaxMmeberNum`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamVisible | uint | 只写（选填） | 修改群是否可见，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Visible`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamSearchAble | uint | 只写（选填） | 修改群是否被搜索，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Searchable`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamIsShutupAll | bool | 只写（选填） | 修改群是否全体禁言，当`modify_flag`包含`kTIMGroupModifyInfoFlag_ShutupAll`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamOwner | string | 只写（选填） | 修改群主所有者，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Owner`时必填，其他情况不用填。此时`modify_flag`不能包含其他值，当修改群主时，同时修改其他信息已无意义 |
| kTIMGroupModifyInfoParamCustomInfo | array [GroupInfoCustemString](#groupinfocustemstring) | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

### GroupGetMemberInfoListParam

获取群成员列表接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetMemberInfoListParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupGetMemberInfoListParamIdentifierArray | array string | 只写（选填） | 群成员 ID 列表 |
| kTIMGroupGetMemberInfoListParamOption | object [GroupMemberGetInfoOption](#groupmembergetinfooption) | 只写（选填） | 获取群成员信息的选项 |
| kTIMGroupGetMemberInfoListParamNextSeq | uint64 | 只写（选填） | 分页拉取标志，第一次拉取填0，回调成功如果不为零，需要分页，调用接口传入再次拉取，直至为0 |

### GroupGetMemberInfoListResult

获取群成员列表接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetMemberInfoListResultNexSeq | uint64 | 只读 | 下一次拉取的标志，server 返回0表示没有更多的数据，否则在下次获取数据时填入这个标志 |
| kTIMGroupGetMemberInfoListResultInfoArray | array [GroupMemberInfo](#groupmemberinfo) | 只读 | 成员信息列表 |

### TIMGroupMemberModifyInfoFlag

设置（修改）群成员信息的类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupMemberModifyFlag_None | - |
| kTIMGroupMemberModifyFlag_MsgFlag | 修改消息接收选项 |
| kTIMGroupMemberModifyFlag_MemberRole | 修改成员角色 |
| kTIMGroupMemberModifyFlag_ShutupTime | 修改禁言时间 |
| kTIMGroupMemberModifyFlag_NameCard | 修改群名片 |
| kTIMGroupMemberModifyFlag_Custom | 修改群成员自定义信息 |

### GroupModifyMemberInfoParam

设置群成员信息接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupModifyMemberInfoParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupModifyMemberInfoParamIdentifier | string | 只写（必填） | 被设置信息的成员 ID |
| kTIMGroupModifyMemberInfoParamModifyFlag | uint [TIMGroupMemberModifyInfoFlag](#timgroupmembermodifyinfoflag) | 只写（必填） | 修改类型，可设置多个值按位或 |
| kTIMGroupModifyMemberInfoParamMsgFlag | uint | 只写（选填） | 修改消息接收选项，当`modify_flag`包含`kTIMGroupMemberModifyFlag_MsgFlag`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamMemberRole | uint [TIMGroupMemberRole](#timgroupmemberrole) | 只写（选填） | 修改成员角色，当`modify_flag`包含`kTIMGroupMemberModifyFlag_MemberRole`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamShutupTime | uint | 只写（选填） | 修改禁言时间，当`modify_flag`包含`kTIMGroupMemberModifyFlag_ShutupTime`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamNameCard | string | 只写（选填） | 修改群名片，当`modify_flag`包含`kTIMGroupMemberModifyFlag_NameCard`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamCustomInfo | array [GroupMemberInfoCustemString](#groupmemberinfocustemstring) | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

### GroupPendencyOption

获取群未决信息列表的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyOptionStartTime | uint64 | 只写（必填） | 设置拉取时间戳，第一次请求填0，后边根据 server 返回的 [GroupPendencyResult](#grouppendencyresult) 键 kTIMGroupPendencyResultNextStartTime 指定的时间戳进行填写 |
| kTIMGroupPendencyOptionMaxLimited | uint | 只写（选填） | 拉取的建议数量，server 可根据需要返回或多或少，不能作为完成与否的标志 |

### TIMGroupPendencyType

未决请求类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupPendency_RequestJoin | 请求加群 |
| kTIMGroupPendency_InviteJoin | 邀请加群 |
| kTIMGroupPendency_ReqAndInvite | 邀请和请求的 |

### TIMGroupPendencyHandle

群未决处理状态。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupPendency_NotHandle | 未处理 |
| kTIMGroupPendency_OtherHandle | 他人处理 |
| kTIMGroupPendency_OperatorHandle | 操作方处理 |

### TIMGroupPendencyHandleResult

群未决处理操作类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupPendency_Refuse | 拒绝 |
| kTIMGroupPendency_Accept | 同意 |

### GroupPendency

群未决信息定义。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyGroupId | string | 读写 | 群组 ID |
| kTIMGroupPendencyFromIdentifier | string | 读写 | 请求者的 ID，例如：请求加群：请求者，邀请加群：邀请人 |
| kTIMGroupPendencyToIdentifier | string | 读写 | 判决者的 ID，处理此条“加群的未决请求”的管理员ID |
| kTIMGroupPendencyAddTime | uint64 | 只读 | 未决信息添加时间 |
| kTIMGroupPendencyPendencyType | uint [TIMGroupPendencyType](#timgrouppendencytype) | 只读 | 未决请求类型 |
| kTIMGroupPendencyHandled | uint [TIMGroupPendencyHandle](#timgrouppendencyhandle) | 只读 | 群未决处理状态 |
| kTIMGroupPendencyHandleResult | uint [TIMGroupPendencyHandleResult](#timgrouppendencyhandleresult) | 只读 | 群未决处理操作类型 |
| kTIMGroupPendencyApplyInviteMsg | string | 只读 | 申请或邀请附加信息 |
| kTIMGroupPendencyFromUserDefinedData | string | 只读 | 申请或邀请者自定义字段 |
| kTIMGroupPendencyApprovalMsg | string | 只读 | 审批信息：同意或拒绝信息 |
| kTIMGroupPendencyToUserDefinedData | string | 只读 | 审批者自定义字段 |
| kTIMGroupPendencyKey | string | 只读 | 签名信息，客户不用关心 |
| kTIMGroupPendencyAuthentication | string | 只读 | 签名信息，客户不用关心 |
| kTIMGroupPendencySelfIdentifier | string | 只读 | 自己的 ID |

### GroupPendencyResult

获取群未决信息列表的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyResultNextStartTime | uint64 | 只读 | 下一次拉取的起始时戳，server 返回0表示没有更多的数据，否则在下次获取数据时以这个时间戳作为开始时间戳 |
| kTIMGroupPendencyResultReadTimeSeq | uint64 | 只读 | 已读上报的时间戳 |
| kTIMGroupPendencyResultUnReadNum | uint | 只读 | 未决请求的未读数 |
| kTIMGroupPendencyResultPendencyArray | array [GroupPendency](#grouppendency) | 只读 | 群未决信息列表 |

### GroupHandlePendencyParam

处理群未决消息接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupHandlePendencyParamIsAccept | bool | 只写（选填） | true 表示接受，false 表示拒绝。默认为 false |
| kTIMGroupHandlePendencyParamHandleMsg | string | 只写（选填） | 同意或拒绝信息，默认为空字符串 |
| kTIMGroupHandlePendencyParamPendency | object [GroupPendency](#grouppendency) | 只写（必填） | 未决信息详情 |

### GroupGetOnlineMemberCountResult

获取指定群在线人数结果。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| TIMGroupGetOnlineMemberCountResulCount | int | 只读 | 指定群的在线人数 |

### TIMGroupSearchFieldKey

群搜索 Field 的枚举。

| 名称 | 含义 |
|-----|-----|
| kTIMGroupSearchFieldKey_GroupId | 群 ID |
| kTIMGroupSearchFieldKey_GroupName | 群名称 |

### GroupSearchParam

群搜索参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| TIMGroupMemberSearchParamGroupidList | array string | 只写（选填） | 指定群 ID 列表，若为不填则搜索全部群中的群成员 |
| TIMGroupMemberSearchParamKeywordList | array string | 只写（选填） | 搜索关键字列表，最多支持5个 |
| TIMGroupMemberSearchParamFieldList | array [TIMGroupMemberSearchFieldKey] | 只写（选填） | 搜索域列表 |

### GroupAttributes

设置群属性的 map 对象。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| TIMGroupAttributeKey | string | 只写（选填） | 群属性 map 的 key |
| TIMGroupAttributeValue | array string | 只写（选填） | 群属性 map 的 value|

### GroupMemberSearchParam

群成员搜索参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| TIMGroupSearchParamKeywordList | array string | 只写（选填） | 搜索关键字列表，最多支持5个 |
| TIMGroupSearchParamFieldList | array [TIMGroupSearchFieldKey] | 只写（选填） | 搜索域列表 |

## 关系链和资料关键类型

关系链和资料相关宏定义，以及相关结构成员存取 JSON Key 定义。

### FriendShipGetProfileListParam

处理群未决消息接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendShipGetProfileListParamIdentifierArray | array string | 只写 | 想要获取目标用户资料的 UserID 列表 |
| kTIMFriendShipGetProfileListParamForceUpdate | bool | 只写 | 是否强制更新。false 表示优先从本地缓存获取，获取不到则去网络上拉取。true 表示直接去网络上拉取资料。默认为 false |

### TIMGenderType

用户性别类型。

| 名称 | 含义 |
|-----|-----|
| kTIMGenderType_Unkown | 未知性别 |
| kTIMGenderType_Male | 性别男 |
| kTIMGenderType_Female | 性别女 |

### TIMProfileAddPermission

用户加好友的选项。

| 名称 | 含义 |
|-----|-----|
| kTIMProfileAddPermission_Unknown | 未知 |
| kTIMProfileAddPermission_AllowAny | 允许任何人添加好友 |
| kTIMProfileAddPermission_NeedConfirm | 添加好友需要验证 |
| kTIMProfileAddPermission_DenyAny | 拒绝任何人添加好友 |

### UserProfileCustemStringInfo

用户自定义资料字段，字符串。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMUserProfileCustemStringInfoKey | string | 只写 | 用户自定义资料字段的 key 值（包含前缀 Tag_Profile_Custom_） |
| kTIMUserProfileCustemStringInfoValue | string | 只写 | 该字段对应的字符串值 |

>?字符串长度不得超过500字节。


### UserProfile

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMUserProfileIdentifier | string | 只读 | 用户 ID |
| kTIMUserProfileNickName | string | 只读 | 用户的昵称 |
| kTIMUserProfileGender | uint [TIMGenderType](#timgendertype) | 只读 | 性别 |
| kTIMUserProfileFaceUrl | string | 只读 | 用户头像 URL |
| kTIMUserProfileSelfSignature | string | 只读 | 用户个人签名 |
| kTIMUserProfileAddPermission | uint [TIMProfileAddPermission](#timprofileaddpermission) | 只读 | 用户加好友的选项 |
| kTIMUserProfileLocation | string | 只读 | 用户位置信息 |
| kTIMUserProfileLanguage | uint | 只读 | 语言 |
| kTIMUserProfileBirthDay | uint | 只读 | 生日 |
| kTIMUserProfileLevel | uint | 只读 | 等级 |
| kTIMUserProfileRole | uint | 只读 | 角色 |
| kTIMUserProfileCustomStringArray | array [UserProfileCustemStringInfo](#userprofilecustemstringinfo) | 只读 | 请参考 [自定义资料字段](https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5) |

### UserProfileItem

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMUserProfileItemNickName | string | 只写 | 修改用户昵称 |
| kTIMUserProfileItemGender | uint [TIMGenderType](#timgendertype) | 只写 | 修改用户性别 |
| kTIMUserProfileItemFaceUrl | string | 只写 | 修改用户头像 |
| kTIMUserProfileItemSelfSignature | string | 只写 | 修改用户签名 |
| kTIMUserProfileItemAddPermission | uint [TIMProfileAddPermission](#timprofileaddpermission) | 只写 | 修改用户加好友的选项 |
| kTIMUserProfileItemLoaction | uint | 只写 | 修改位置 |
| kTIMUserProfileItemLanguage | uint | 只写 | 修改语言 |
| kTIMUserProfileItemBirthDay | uint | 只写 | 修改生日 |
| kTIMUserProfileItemLevel | uint | 只写 | 修改等级 |
| kTIMUserProfileItemRole | uint | 只写 | 修改角色 |
| kTIMUserProfileItemCustomStringArray | array [UserProfileCustemStringInfo](#userprofilecustemstringinfo) | 只写 | 修改 [自定义资料字段](https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5) |

### FriendProfileCustemStringInfo

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendProfileCustemStringInfoKey | string | 只写 | 好友自定义资料字段 key |
| kTIMFriendProfileCustemStringInfoValue | string | 只写 | 好友自定义资料字段 value |

### FriendProfile

好友资料。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendProfileIdentifier | string | 只读 | 好友 UserID |
| kTIMFriendProfileGroupNameArray | array string | 只读 | 好友分组名称列表 |
| kTIMFriendProfileRemark | string | 只读 | 好友备注，最大96字节，获取自己资料时，该字段为空 |
| kTIMFriendProfileAddWording | string | 只读 | 好友申请时的添加理由 |
| kTIMFriendProfileAddSource | string | 只读 | 好友申请时的添加来源 |
| kTIMFriendProfileAddTime | uint64 | 只读 | 好友添加时间 |
| kTIMFriendProfileUserProfile | object [UserProfile](#userprofile) | 只读 | 好友的个人资料 |
| kTIMFriendProfileCustomStringArray | array [FriendProfileCustemStringInfo](#friendprofilecustemstringinfo) | 只读 | [自定义好友字段](https://cloud.tencent.com/document/product/269/1501#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.A5.BD.E5.8F.8B.E5.AD.97.E6.AE.B5) |

### FriendProfileItem

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendProfileItemRemark | string | 只写 | 修改好友备注 |
| kTIMFriendProfileItemGroupNameArray | array string | 只写 | 修改好友分组名称列表 |
| kTIMFriendProfileItemCustomStringArray | array [FriendProfileCustemStringInfo](#friendprofilecustemstringinfo) | 只写 | 修改 [自定义好友字段](https://cloud.tencent.com/document/product/269/1501#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.A5.BD.E5.8F.8B.E5.AD.97.E6.AE.B5) |

### TIMFriendType

| 名称 | 含义 |
|-----|-----|
| FriendTypeSignle | 单向好友：用户 A 的好友表中有用户 B，但 B 的好友表中却没有 A |
| FriendTypeBoth | 双向好友：用户 A 的好友表中有用户 B，B 的好友表中也有 A |

### FriendshipAddFriendParam

添加好友接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipAddFriendParamIdentifier | string | 只写 | 请求加好友对应的 UserID |
| kTIMFriendshipAddFriendParamFriendType | uint [TIMFriendType](#timfriendtype) | 只写 | 请求添加好友的好友类型 |
| kTIMFriendshipAddFriendParamRemark | string | 只写 | 预备注 |
| kTIMFriendshipAddFriendParamGroupName | string | 只写 | 预分组名 |
| kTIMFriendshipAddFriendParamAddSource | string | 只写 | 加好友来源描述 |
| kTIMFriendshipAddFriendParamAddWording | string | 只写 | 加好友附言 |

### FriendResult

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendResultIdentifier | string | 只读 | 关系链操作的用户 ID |
| kTIMFriendResultCode | int [错误码](https://cloud.tencent.com/document/product/269/1671) | 只读 | 关系链操作的结果 |
| kTIMFriendResultDesc | string | 只读 | 关系链操作失败的详细描述 |

### FriendshipModifyFriendProfileParam

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipModifyFriendProfileParamIdentifier | string | 只写 | 被修改的好友的 UserID |
| kTIMFriendshipModifyFriendProfileParamItem | object [FriendProfileItem](#friendprofileitem) | 只写 | 修改的好友资料各个选项 |

### FriendAddPendency

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendAddPendencyIdentifier | string | 只读 | 添加好友请求方的 UserID |
| kTIMFriendAddPendencyNickName | string | 只读 | 添加好友请求方的昵称 |
| kTIMFriendAddPendencyAddSource | string | 只读 | 添加好友请求方的来源 |
| kTIMFriendAddPendencyAddWording | string | 只读 | 添加好友请求方的附言 |

### TIMFriendPendencyType

| 名称 | 含义 |
|-----|-----|
| FriendPendencyTypeComeIn | 别人发给我的 |
| FriendPendencyTypeSendOut | 我发给别人的 |
| FriendPendencyTypeBoth | 双向的 |

### FriendshipGetPendencyListParam

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipGetPendencyListParamType | uint [TIMFriendPendencyType](#timfriendpendencytype) | 只写 | 添加好友的未决请求类型 |
| kTIMFriendshipGetPendencyListParamStartSeq | uint64 | 只写 | 分页获取未决请求的起始 seq，返回的结果包含最大 seq，作为获取下一页的起始 seq |
| kTIMFriendshipGetPendencyListParamStartTime | uint64 | 只写 | 获取未决信息的开始时间戳 |
| kTIMFriendshipGetPendencyListParamLimitedSize | int | 只写 | 获取未决信息列表，每页的数量 |

### PendencyPage

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMPendencyPageStartTime | uint64 | 只读 | 未决请求信息页的起始时间 |
| kTIMPendencyPageUnReadNum | uint64 | 只读 | 未决请求信息页的未读数量 |
| kTIMPendencyPageCurrentSeq | uint64 | 只读 | 未决请求信息页的当前 Seq |
| kTIMPendencyPagePendencyInfoArray | array [FriendAddPendencyInfo](#friendaddpendencyinfo) | 只读 | 未决请求信息页的未决信息列表 |

### FriendAddPendencyInfo

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendAddPendencyInfoType | uint [TIMFriendPendencyType](#timfriendpendencytype) | 只读 | 好友添加请求未决类型 |
| kTIMFriendAddPendencyInfoIdentifier | string | 只读 | 好友添加请求未决的 UserID |
| kTIMFriendAddPendencyInfoNickName | string | 只读 | 好友添加请求未决的昵称 |
| kTIMFriendAddPendencyInfoAddTime | uint64 | 只读 | 发起好友申请的时间 |
| kTIMFriendAddPendencyInfoAddSource | string | 只读 | 好友添加请求未决的添加来源 |
| kTIMFriendAddPendencyInfoAddWording | string | 只读 | 好友添加请求未决的添加附言 |

### FriendshipDeletePendencyParam

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipDeletePendencyParamType | uint [TIMFriendPendencyType](#timfriendpendencytype) | 只读 | 添加好友的未决请求类型 |
| kTIMFriendshipDeletePendencyParamIdentifierArray | array string | 只读 | 删除好友未决请求的 UserID 列表 |

### TIMFriendResponseAction

| 名称 | 含义 |
|-----|-----|
| ResponseActionAgree | 同意 |
| ResponseActionAgreeAndAdd | 同意并添加 |
| ResponseActionReject | 拒绝 |

### FriendRespone

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendResponeIdentifier | string | 只写（必填） | 响应好友添加的 UserID |
| kTIMFriendResponeAction | uint [TIMFriendResponseAction](#timfriendresponseaction) | 只写（必填） | 响应好友添加的动作 |
| kTIMFriendResponeRemark | string | 只写（选填） | 好友备注 |
| kTIMFriendResponeGroupName | string | 只写（选填） | 好友分组列表 |

### FriendshipDeleteFriendParam

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipDeleteFriendParamFriendType | uint [TIMFriendType](#timfriendtype) | 只写 | 删除好友，指定删除的好友类型 |
| kTIMFriendshipDeleteFriendParamIdentifierArray | array string | 只写（选填） | 删除好友 UserID 列表 |

### FriendGroupInfo

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipCreateFriendGroupParamNameArray | array string | 只写 | 创建分组的名称列表 |
| kTIMFriendshipCreateFriendGroupParamIdentifierArray | array string | 只写 | 要放到创建的分组的好友 UserID 列表 |

### FriendGroupInfo

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendGroupInfoName | string | 只读 | 分组名称 |
| kTIMFriendGroupInfoCount | uint64 | 只读 | 当前分组的好友个数 |
| kTIMFriendGroupInfoIdentifierArray | array string | 只读 | 当前分组内好友 UserID 列表 |

### FriendshipModifyFriendGroupParam

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipModifyFriendGroupParamName | string | 只写 | 要修改的分组名称 |
| kTIMFriendshipModifyFriendGroupParamNewName | string | 只写（选填） | 修改后的分组名称 |
| kTIMFriendshipModifyFriendGroupParamDeleteIdentifierArray | array string | 只写（选填） | 要从当前分组删除的好友 UserID 列表 |
| kTIMFriendshipModifyFriendGroupParamAddIdentifierArray | array string | 只写（选填） | 当前分组要新增的好友 UserID 列表 |

### FriendshipCheckFriendTypeParam

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipCheckFriendTypeParamCheckType | uint [TIMFriendType](#timfriendtype) | 只写 | 要检测的好友类型 |
| kTIMFriendshipCheckFriendTypeParamIdentifierArray | array string | 只写 | 要检测的好友 UserID 列表 |

### TIMFriendCheckRelation

| 名称 | 含义 |
|-----|-----|
| FriendCheckNoRelation | 无关系 |
| FriendCheckAWithB | 仅 A 中有 B |
| FriendCheckBWithA | 仅 B 中有 A |
| FriendCheckBothWay | 双向 |

### FriendshipCheckFriendTypeResult

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipCheckFriendTypeResultIdentifier | string | 只读 | 被检测的好友 UserID |
| kTIMFriendshipCheckFriendTypeResultRelation | uint [TIMFriendCheckRelation](#timfriendcheckrelation) | 只读 | 检测成功时返回的二者之间的关系 |
| kTIMFriendshipCheckFriendTypeResultCode | int [错误码](https://cloud.tencent.com/document/product/269/1671) | 只读 | 检测的结果 |
| kTIMFriendshipCheckFriendTypeResultDesc | string | 只读 | 检测好友失败的描述信息 |

### TIMFriendshipSearchFieldKey

好友搜索的枚举。

| 名称 | 含义 |
|-----|-----|
| kTIMFriendshipSearchFieldKey_Identifier | 用户 ID |
| kTIMFriendshipSearchFieldKey_NikeName | 昵称 |
| kTIMFriendshipSearchFieldKey_Remark | 备注 |

### FriendSearchParam

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipSearchParamKeywordList | array string | 只写 | 搜索的关键字列表，关键字列表最多支持 5 个 |
| kTIMFriendshipSearchParamSearchFieldList | array int | 只写 | 好友搜索类型 |

### TIMFriendshipRelationType

二者之间的关系。

| 名称 | 含义 |
|-----|-----|
| kTIMFriendshipRelationType_None | 未知关系 |
| kTIMFriendshipRelationType_InMyFriendList | 单向好友：对方是我的好友，我不是对方的好友 |
| kTIMFriendshipRelationType_InOtherFriendList | 单向好友：对方不是我的好友，我是对方的好友 |
| kTIMFriendshipRelationType_BothFriend | 双向好友 |

### FriendInfoGetResult

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFriendshipFriendInfoGetResultIdentifier | string | 只读 | 好友 user_id |
| kTIMFriendshipFriendInfoGetResultRelationType | uint [TIMFriendshipRelationType] | 只读 | 好友关系 |

| kTIMFriendshipFriendInfoGetResultErrorCode | uint | 只读 | 错误码 |
| kTIMFriendshipFriendInfoGetResultErrorMessage | string | 只读 | 错误描述 |
| kTIMFriendshipFriendInfoGetResultFriendInfo | array [FriendProfile] | 只读 | 好友资料 |
