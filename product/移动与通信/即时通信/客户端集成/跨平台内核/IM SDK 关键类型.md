## 常用宏和基础配置选项


### TIMResult

调用接口的返回值。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| TIM_SUCC | 0 | 接口调用成功 |
| TIM_ERR_SDKUNINIT | -1 | 接口调用失败，IM SDK 未初始化 |
| TIM_ERR_NOTLOGIN | -2 | 接口调用失败，用户未登录 |
| TIM_ERR_JSON | -3 | 接口调用失败，错误的 JSON 格式或 JSON Key |
| TIM_ERR_PARAM | -4 | 接口调用成功，参数错误 |
| TIM_ERR_CONV | -5 | 接口调用成功，无效的会话 |
| TIM_ERR_GROUP | -6 | 接口调用成功，无效的群组 |

>?若接口参数中有回调，只有当接口返回 TIM_SUCC 时，回调才会被调用。


### TIMLogLevel

日志级别。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMLog_Off | 0 | 关闭日志输出 |
| kTIMLog_Verbose | 1 | 开发调试过程中一些详细信息日志 |
| kTIMLog_Debug | 2 | 调试日志 |
| kTIMLog_Info | 3 | 信息日志 |
| kTIMLog_Warn | 4 | 警告日志 |
| kTIMLog_Error | 5 | 错误日志 |
| kTIMLog_Assert | 6 | 断言日志 |

### TIMNetworkStatus

连接事件类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMConnected | 0 | 已连接 |
| kTIMDisconnected | 1 | 失去连接 |
| kTIMConnecting | 2 | 正在连接 |
| kTIMConnectFailed | 3 | 连接失败 |

### TIMConvEvent

会话事件类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMConvEvent_Add | 0 | 会话新增，例如收到一条新消息，产生一个新的会话是事件触发 |
| kTIMConvEvent_Del | 1 | 会话删除，例如自己删除某会话时会触发 |
| kTIMConvEvent_Update | 2 | 会话更新，会话内消息的未读计数变化和收到新消息时触发 |

### TIMConvType

会话类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMConv_Invalid | 0 | 无效会话 |
| kTIMConv_C2C | 1 | 个人会话 |
| kTIMConv_Group | 2 | 群组会话 |
| kTIMConv_System | 3 | 系统会话 |

### SdKConfig

初始化 IM SDK 的配置。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMSdkConfigConfigFilePath | string | 只写（选填） | 配置文件路径，默认路径为"/" |
| kTIMSdkConfigLogFilePath | string | 只写（选填） | 日志文件路径，默认路径为"/" |

### TIMGroupMemberInfoFlag

群组成员信息标识。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupMemberInfoFlag_None | 0x00 | 无 |
| kTIMGroupMemberInfoFlag_JoinTime | 0x01 | 加入时间 |
| kTIMGroupMemberInfoFlag_MsgFlag | 0x01 << 1 | 群消息接收选项 |
| kTIMGroupMemberInfoFlag_MsgSeq | 0x01 << 2 | 成员已读消息 seq |
| kTIMGroupMemberInfoFlag_MemberRole | 0x01 << 3 | 成员角色 |
| kTIMGroupMemberInfoFlag_ShutupUntill | 0x01 << 4 | 禁言时间。0：没有禁言 |
| kTIMGroupMemberInfoFlag_NameCard | 0x01 << 5 | 群名片 |

### TIMGroupMemberRoleFlag

群组成员角色标识。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupMemberRoleFlag_All | 0x00 | 获取全部角色类型 |
| kTIMGroupMemberRoleFlag_Owner | 0x01 | 获取所有者（群主） |
| kTIMGroupMemberRoleFlag_Admin | 0x01 << 1 | 获取管理员，不包括群主 |
| kTIMGroupMemberRoleFlag_Member | 0x01 << 2 | 获取普通群成员，不包括群主和管理员 |

### GroupMemberGetInfoOption

获取群组成员信息的选项。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupMemberGetInfoOptionInfoFlag |  uint64 [TIMGroupMemberInfoFlag](#timgroupmemberinfoflag)  | 读写（选填） | 根据想要获取的信息过滤，默认值为 0xffffffff（获取全部信息） |
| kTIMGroupMemberGetInfoOptionRoleFlag |  uint64 [TIMGroupMemberRoleFlag](#timgroupmemberroleflag)  | 读写（选填） | 根据成员角色过滤，默认值为 kTIMGroupMemberRoleFlag_All，获取所有角色 |
| kTIMGroupMemberGetInfoOptionCustomArray |  array string | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)  |

### TIMGroupGetInfoFlag

群组成员信息标识。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupInfoFlag_None | 0x00 | - |
| kTIMGroupInfoFlag_Name | 0x01 | 群组名称 |
| kTIMGroupInfoFlag_CreateTime | 0x01 << 1 | 群组创建时间 |
| kTIMGroupInfoFlag_OwnerUin | 0x01 << 2 | 群组创建者帐号 |
| kTIMGroupInfoFlag_Seq | 0x01 << 3 | - |
| kTIMGroupInfoFlag_LastTime | 0x01 << 4 | 群组信息最后修改时间 |
| kTIMGroupInfoFlag_NextMsgSeq | 0x01 << 5 | - |
| kTIMGroupInfoFlag_LastMsgTime | 0X01 << 6 | 最新群组消息时间 |
| kTIMGroupInfoFlag_AppId | 0x01 << 7 | - |
| kTIMGroupInfoFlag_MemberNum | 0x01 << 8 | 群组成员数量 |
| kTIMGroupInfoFlag_MaxMemberNum | 0x01 << 9 | 群组成员最大数量 |
| kTIMGroupInfoFlag_Notification | 0x01 << 10 | 群公告内容 |
| kTIMGroupInfoFlag_Introduction | 0x01 << 11 | 群简介内容 |
| kTIMGroupInfoFlag_FaceUrl | 0x01 << 12 | 群头像 URL |
| kTIMGroupInfoFlag_AddOpton | 0x01 << 13 | 加群选项 |
| kTIMGroupInfoFlag_GroupType | 0x01 << 14 | 群类型 |
| kTIMGroupInfoFlag_LastMsg | 0x01 << 15 | 群组内最新一条消息 |
| kTIMGroupInfoFlag_OnlineNum | 0x01 << 16 | 群组在线成员数 |
| kTIMGroupInfoFlag_Visible | 0x01 << 17 | 群组是否可见 |
| kTIMGroupInfoFlag_Searchable | 0x01 << 18 | 群组是否可以搜索 |
| kTIMGroupInfoFlag_ShutupAll | 0x01 << 19 | 群组是否全禁言 |

### GroupGetInfoOption

获取群组信息的选项。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetInfoOptionInfoFlag |  uint64 [TIMGroupGetInfoFlag](#timgroupgetinfoflag)  | 读写（选填） | 根据想要获取的信息过滤，默认值为 0xffffffff（获取全部信息） |
| kTIMGroupGetInfoOptionCustomArray |  array string | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)  |

### UserConfig

用于配置信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMUserConfigIsReadReceipt | bool | 只写（选填） | true 表示要收已读回执事件 |
| kTIMUserConfigIsSyncReport | bool | 只写（选填） | true 表示服务端要删掉已读状态 |
| kTIMUserConfigIsIngoreGroupTipsUnRead | bool | 只写（选填） | true 表示群 tips 不计入群消息已读计数 |
| kTIMUserConfigGroupGetInfoOption |  object [GroupGetInfoOption](#groupgetinfooption)  | 只写（选填） | 获取群组信息默认选项 |
| kTIMUserConfigGroupMemberGetInfoOption |  object [GroupMemberGetInfoOption](#groupmembergetinfooption)  | 只写（选填） | 获取群组成员信息默认选项 |

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
HTTP 代理主要用在发送图片、语音、文件、微视频等消息时，将相关文件上传到 COS，以及接收到图片、语音、文件、微视频等消息，将相关文件下载到本地时用到。设置时，设置的 IP 不能为空，端口不能为0。如果需要取消 HTTP 代理，只需将代理的 IP 设置为空字符串，端口设置为0。
- SOCKS5 代理。
SOCKS5 代理需要在初始化之前设置。设置之后 IM SDK 发送的所有协议会通过 SOCKS5 代理服务器发送的即时通信 IM 后台。


| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMSetConfigLogLevel |  uint [TIMLogLevel](#timloglevel)  | 只写（选填） | 输出到日志文件的日子级别 |
| kTIMSetConfigCackBackLogLevel |  uint [TIMLogLevel](#timloglevel)  | 只写（选填） | 日子回调的日志级别 |
| kTIMSetConfigIsLogOutputConsole | bool | 只写（选填） | 是否输出到控制台 |
| kTIMSetConfigUserConfig |  object [UserConfig](#userconfig)  | 只写（选填） | 用户配置 |
| kTIMSetConfigUserDefineData | string | 只写（选填） | 自定义数据，如果需要，初始化前设置 |
| kTIMSetConfigHttpProxyInfo |  object [HttpProxyInfo](#httpproxyinfo)  | 只写（选填） | 设置 HTTP 代理，如果需要，在发送图片、文件、语音、视频前设置 |
| kTIMSetConfigSocks5ProxyInfo |  object [Socks5ProxyInfo](#socks5proxyinfo)  | 只写（选填） | 设置 SOCKS5 代理，如果需要，初始化前设置 |

## 消息关键类型

消息相关宏定义，以及相关结构成员存取 JSON Key 定义。

### TIMMsgStatus

消息当前状态定义。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMMsg_Sending | 1 | 消息正在发送 |
| kTIMMsg_SendSucc | 2 | 消息发送成功 |
| kTIMMsg_SendFail | 3 | 消息发送失败 |
| kTIMMsg_Deleted | 4 | 消息已删除 |
| kTIMMsg_LocalImported | 5 | 消息导入状态 |
| kTIMMsg_Revoked | 6 | 消息撤回状态 |

### TIMMsgPriority

标识消息的优先级，数字越大优先级越低。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMMsgPriority_High | 0 | 优先级最高，一般为红包或者礼物消息 |
| kTIMMsgPriority_Normal | 1 | 表示优先级次之，建议为普通消息 |
| kTIMMsgPriority_Low | 2 | 建议为点赞消息等 |
| kTIMMsgPriority_Lowest | 3 | 优先级最低，一般为成员进退群通知（后台下发） |

### Message

消息 JSON Keys。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgElemArray |  array [Elem](#elem)  | 读写（必填） | 消息内元素列表 |
| kTIMMsgConvId | string | 读写（选填） | 消息所属会话 ID |
| kTIMMsgConvType |  uint [TIMConvType](#timconvtype)  | 读写（选填） | 消息所属会话类型 |
| kTIMMsgSender | string | 读写（选填） | 消息的发送者 |
| kTIMMsgPriority |  uint [TIMMsgPriority](#timmsgpriority)  | 读写（选填） | 消息优先级 |
| kTIMMsgClientTime | uint64 | 读写（选填） | 客户端时间 |
| kTIMMsgServerTime | uint64 | 读写（选填） | 服务端时间 |
| kTIMMsgIsFormSelf | bool | 读写（选填） | 消息是否来自自己 |
| kTIMMsgIsRead | bool | 读写（选填） | 消息是否已读 |
| kTIMMsgIsOnlineMsg | bool | 读写（选填） | 消息是否是在线消息，默认为 false 表示普通消息，true 表示阅后即焚消息 |
| kTIMMsgIsPeerRead | bool | 只读 | 消息是否被会话对方已读 |
| kTIMMsgStatus |  uint [TIMMsgStatus](#timmsgstatus)  | 读写（选填） | 消息当前状态 |
| kTIMMsgUniqueId | uint64 | 只读 | 消息的唯一标识 |
| kTIMMsgRand | uint64 | 只读 | 消息的随机码 |
| kTIMMsgSeq | uint64 | 只读 | 消息序列 |
| kTIMMsgCustomInt | uint32_t | 读写（选填） | 自定义整数值字段 |
| kTIMMsgCustomStr | string | 读写（选填） | 自定义数据字段 |

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
| kTIMMsgReceiptConvType |  uint [TIMConvType](#timconvtype)  | 只读 | 会话类型 |
| kTIMMsgReceiptTimeStamp | uint64 | 只读 | 时间戳 |

### TIMElemType

元素的类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMElem_Text | 0 | 文本元素 |
| kTIMElem_Image | 1 | 图片元素 |
| kTIMElem_Sound | 2 | 声音元素 |
| kTIMElem_Custom | 3 | 自定义元素 |
| kTIMElem_File | 4 | 文件元素 |
| kTIMElem_GroupTips | 5 | 群组系统消息元素 |
| kTIMElem_Face | 6 | 表情元素 |
| kTIMElem_Location | 7 | 位置元素 |
| kTIMElem_GroupReport | 8 | 群组系统通知元素 |
| kTIMElem_Video | 9 | 视频元素 |

### Elem

元素的类型。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMElemType |  uint [TIMElemType](#timelemtype)  | 读写（必填） | 元素类型 |

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

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMImageLevel_Orig | 0 | 原图发送 |
| kTIMImageLevel_Compression | 1 | 高压缩率图发送（图片较小，默认值） |
| kTIMImageLevel_HD | 2 | 高清图发送（图片较大） |

### ImageElem

图片元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMImageElemOrigPath | string | 读写（必填） | 发送图片的路径 |
| kTIMImageElemLevel | uint [TIMImageLevel](#timimagelevel)  | 读写（必填） | 发送图片的质量级别 |
| kTIMImageElemFormat | int | 读写（必填） | 发送图片格式 |
| kTIMImageElemOrigId | string | 只读 | 原图的 UUID |
| kTIMImageElemOrigPicHeight | int | 只读 | 原图的图片高度 |
| kTIMImageElemOrigPicWidth | int | 只读 | 原图的图片高度 |
| kTIMImageElemOrigPicSize | int | 只读 | 原图的图片高度 |
| kTIMImageElemThumbId | string | 只读 | 略缩图 UUID |
| kTIMImageElemThumbPicHeight | int | 只读 | 略缩图的图片高度 |
| kTIMImageElemThumbPicWidth | int | 只读 | 略缩图的图片高度 |
| kTIMImageElemThumbPicSize | int | 只读 | 略缩图的图片高度 |
| kTIMImageElemLargeId | string | 只读 | 大图片 UUID |
| kTIMImageElemLargePicHeight | int | 只读 | 大图片的图片高度 |
| kTIMImageElemLargePicWidth | int | 只读 | 大图片的图片高度 |
| kTIMImageElemLargePicSize | int | 只读 | 大图片的图片高度 |
| kTIMImageElemOrigUrl | string | 只读 | 原图 URL |
| kTIMImageElemThumbUrl | string | 只读 | 略缩图 URL |
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
| kTIMSoundElemFileId | string | 只读 | 下载声音文件时的 ID |
| kTIMSoundElemBusinessId | int | 只读 | 下载时用到的 businessID |
| kTIMSoundElemDownloadFlag | int | 只读 | 是否需要申请下载地址（0：到架平申请，1：到 cos 申请，2：不需要申请，直接拿 URL 下载） |
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
| kTIMCustomElemSound | string | 读写 | 自定义声音，这个声音是给谁听的 |

>?自定义消息是指当内置的消息类型无法满足特殊需求，开发者可以自定义消息格式，内容全部由开发者定义，IM SDK 只负责透传。


### FileElem

文件元素。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFileElemFilePath | string | 读写（必填） | 文件所在路径（包含文件名） |
| kTIMFileElemFileName | string | 读写（选填） | 文件名，显示的名称<br>不设置该参数时，kTIMFileElemFileName 默认为 kTIMFileElemFilePath 指定的文件路径中的文件名 |
| kTIMFileElemFileSize | int | 读写（必填） | 文件大小 |
| kTIMFileElemFileId | string | 只读 | 下载视频时的 UUID |
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
| kTIMVideoElemVideoId | string | 只读 | 下载视频时的 UUID |
| kTIMVideoElemBusinessId | int | 只读 | 下载时用到的 businessID |
| kTIMVideoElemVideoDownloadFlag | int | 只读 | 视频文件下载 flag |
| kTIMVideoElemVideoUrl | string | 只读 | 视频文件下载的 URL |
| kTIMVideoElemImageType | string | 读写（必填） | 截图文件类型，发送消息时进行设置 |
| kTIMVideoElemImageSize | uint | 读写（必填） | 截图文件大小 |
| kTIMVideoElemImageWidth | uint | 读写（必填） | 截图高度，发送消息时进行设置 |
| kTIMVideoElemImageHeight | uint | 读写（必填） | 截图宽度，发送消息时进行设置 |
| kTIMVideoElemImagePath | string | 读写（必填） | 保存截图的路径 |
| kTIMVideoElemImageId | string | 只读 | 下载视频截图时的 ID |
| kTIMVideoElemImageDownloadFlag | int | 只读 | 截图文件下载 flag |
| kTIMVideoElemImageUrl | string | 只读 | 截图文件下载的 URL |
| kTIMVideoElemTaskId | uint | 只读 | 任务 ID |

### TIMGroupTipGroupChangeFlag

群组信息修改的类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupTipChangeFlag_Name | 0xa | 修改群组名称 |
| kTIMGroupTipChangeFlag_Introduction | 11 | 修改群简介 |
| kTIMGroupTipChangeFlag_Notification | 12 | 修改群公告 |
| kTIMGroupTipChangeFlag_FaceUrl | 13 | 修改群头像 URL |
| kTIMGroupTipChangeFlag_Owner | 14 | 修改群所有者 |

### GroupTipGroupChangeInfo

群组系统消息-群组信息修改。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipGroupChangeInfoFlag |  uint [TIMGroupTipGroupChangeFlag](#timgrouptipgroupchangeflag)  | 只读 | 群消息修改群信息标志 |
| kTIMGroupTipGroupChangeInfoValue | string | 只读 | 修改的后值，不同的`info_flag`字段，具有不同的含义 |

### GroupTipMemberChangeInfo

群组系统消息-群组成员禁言。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipMemberChangeInfoIdentifier | string | 只读 | 群组成员 ID |
| kTIMGroupTipMemberChangeInfoShutupTime | uint | 只读 | 禁言时间 |

### UserProfile

用户个人资料。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMUserProfileIdentifier | string | 只读 | 用户 ID |
| kTIMUserProfileNickName | string | 只读 | 用户的昵称 |
| kTIMUserProfileFaceURL | string | 只读 | 用户头像 URL |
| kTIMUserProfileSelfSignature | string | 只读 | 用户个人签名 |
| kTIMUserProfileRemark | string | 只读 | 用户备注 |

### TIMGroupTipType

群组系统消息类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupTip_None | 0 | 无效的群提示 |
| kTIMGroupTip_Invite | 1 | 邀请加入提示 |
| kTIMGroupTip_Quit | 2 | 退群提示 |
| kTIMGroupTip_Kick | 3 | 踢人提示 |
| kTIMGroupTip_SetAdmin | 4 | 设置管理员提示 |
| kTIMGroupTip_CancelAdmin | 5 | 取消管理员提示 |
| kTIMGroupTip_GroupInfoChange | 6 | 群信息修改提示 |
| kTIMGroupTip_MemberInfoChange | 7 | 群成员信息修改提示 |

### GroupTipsElem

群组系统消息元素（针对所有群成员）。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipsElemTipType |  uint [TIMGroupTipType](#timgrouptiptype)  | 只读 | 群消息类型 |
| kTIMGroupTipsElemOpUser | string | 只读 | 操作者 ID |
| kTIMGroupTipsElemGroupName | string | 只读 | 群组名称 |
| kTIMGroupTipsElemGroupId | string | 只读 | 群组 ID |
| kTIMGroupTipsElemTime | uint | 只读 | 群消息时间 |
| kTIMGroupTipsElemUserArray |  array string | 只读 | 被操作的帐号列表 |
| kTIMGroupTipsElemGroupChangeInfoArray |  array [GroupTipGroupChangeInfo](#grouptipgroupchangeinfo)  | 只读 | 群资料变更信息列表，仅当`tips_type`值为`kTIMGroupTip_GroupInfoChange`时有效 |
| kTIMGroupTipsElemMemberChangeInfoArray |  array [GroupTipMemberChangeInfo](#grouptipmemberchangeinfo)  | 只读 | 群成员变更信息列表，仅当`tips_type`值为`kTIMGroupTip_MemberInfoChange`时有效 |
| kTIMGroupTipsElemOpUserInfo |  object [UserProfile](#userprofile)  | 只读 | 操作者个人资料 |
| kTIMGroupTipsElemOpGroupMemberInfo |  object [GroupMemberInfo](#groupmemberinfo)  | 只读 | 群成员信息 |
| kTIMGroupTipsElemChangedUserInfoArray |  array [UserProfile](#userprofile)  | 只读 | 被操作者列表资料 |
| kTIMGroupTipsElemChangedGroupMemberInfoArray |  array [GroupMemberInfo](#groupmemberinfo)  | 只读 | 群成员信息列表 |
| kTIMGroupTipsElemMemberNum | uint | 只读 | 当前群成员数，只有当事件消息类型为`kTIMGroupTip_Invite`、`kTIMGroupTip_Quit`、`kTIMGroupTip_Kick`时有效 |
| kTIMGroupTipsElemPlatform | string | 只读 | 操作方平台信息 |

### TIMGroupReportType

群组系统通知类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupReport_None | 0 | 未知类型 |
| kTIMGroupReport_AddRequest | 1 | 申请加群（只有管理员会接收到） |
| kTIMGroupReport_AddAccept | 2 | 申请加群被同意（只有申请人自己接收到） |
| kTIMGroupReport_AddRefuse | 3 | 申请加群被拒绝（只有申请人自己接收到） |
| kTIMGroupReport_BeKicked | 4 | 被管理员踢出群（只有被踢者接收到） |
| kTIMGroupReport_Delete | 5 | 群被解散（全员接收） |
| kTIMGroupReport_Create | 6 | 创建群（创建者接收，不展示） |
| kTIMGroupReport_Invite | 7 | 邀请加群（被邀请者接收） |
| kTIMGroupReport_Quit | 8 | 主动退群（主动退出者接收，不展示） |
| kTIMGroupReport_GrantAdmin | 9 | 设置管理员（被设置者接收） |
| kTIMGroupReport_CancelAdmin | 10 | 取消管理员（被取消者接收） |
| kTIMGroupReport_RevokeAdmin | 11 | 群已被回收（全员接收，不展示） |
| kTIMGroupReport_InviteReq | 12 | 邀请加群（只有被邀请者会接收到） |
| kTIMGroupReport_InviteAccept | 13 | 邀请加群被同意（只有发出邀请者会接收到） |
| kTIMGroupReport_InviteRefuse | 14 | 邀请加群被拒绝（只有发出邀请者会接收到） |
| kTIMGroupReport_ReadedSync | 15 | 已读上报多终端同步通知（只有上报人自己收到） |
| kTIMGroupReport_UserDefine | 16 | 用户自定义通知（默认全员接收） |

### GroupReportElem

群组系统通知元素（针对个人）。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupReportElemReportType |  uint [TIMGroupReportType](#timgroupreporttype)  | 只读 | 类型 |
| kTIMGroupReportElemGroupId | string | 只读 | 群组 ID |
| kTIMGroupReportElemGroupName | string | 只读 | 群组名称 |
| kTIMGroupReportElemOpUser | string | 只读 | 操作者 ID |
| kTIMGroupReportElemMsg | string | 只读 | 操作理由 |
| kTIMGroupReportElemUserData | string | 只读 | 操作者填的自定义数据 |
| kTIMGroupReportElemOpUserInfo |  object [UserProfile](#userprofile)  | 只读 | 操作者个人资料 |
| kTIMGroupReportElemOpGroupMemberInfo |  object [GroupMemberInfo](#groupmemberinfo)  | 只读 | 操作者群内资料 |
| kTIMGroupReportElemPlatform | string | 只读 | 操作方平台信息 |

### MsgBatchSendParam

消息群发接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgBatchSendParamIdentifierArray |  array string | 只写（必填） | 群发的 ID 列表 |
| kTIMMsgBatchSendParamMsg |  object [Message](#message)  | 只写（必填） | 群发的消息 |

### MsgBatchSendResult

消息群发接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgBatchSendResultIdentifier | string | 只读 | 群发的单个 ID |
| kTIMMsgBatchSendResultCode |  int [错误码](https://cloud.tencent.com/document/product/269/1671)  | 只读 | 消息发送结果 |
| kTIMMsgBatchSendResultDesc | string | 只读 | 消息发送的描述 |
| kTIMMsgBatchSendResultMsg |  object [Message](#message)  | 只读 | 发送的消息 |

### MsgLocator

消息定位符。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgLocatorConvId | bool | 读写 | 要查找的消息是否是被撤回。true 被撤回的，false 非撤回的。默认值为 false |
| kTIMMsgLocatorConvType | bool | 读写 | 要查找的消息是否是被撤回。true 被撤回的，false 非撤回的。默认值为 false |
| kTIMMsgLocatorIsRevoked | bool | 读写（必填） | 要查找的消息是否是被撤回。true 被撤回的，false 非撤回的。默认值为 false |
| kTIMMsgLocatorTime | uint64 | 读写（必填） | 要查找的消息的时间戳 |
| kTIMMsgLocatorSeq | uint64 | 读写（必填） | 要查找的消息的序列号 |
| kTIMMsgLocatorIsSelf | bool | 读写（必填） | 要查找的消息的发送者是否是自己。true 发送者是自己，false 发送者不是自己。默认值为 false |
| kTIMMsgLocatorRand | uint64 | 读写（必填） | 要查找的消息随机码 |

### MsgGetMsgListParam

消息获取接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgGetMsgListParamLastMsg |  object [Message](#message)  | 只写（选填） | 指定的消息，不允许为 null |
| kTIMMsgGetMsgListParamCount | uint | 只写（选填） | 从指定消息往后的消息数 |
| kTIMMsgGetMsgListParamIsRamble | bool | 只写（选填） | 是否漫游消息 |
| kTIMMsgGetMsgListParamIsForward | bool | 只写（选填） | 是否向前排序 |

### MsgDeleteParam

消息删除接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDeleteParamMsg |  object [Message](#message)  | 只写（选填） | 指定在会话中要删除的消息 |
| kTIMMsgDeleteParamIsRamble | bool | 只写（选填） | 是否删除本地/漫游所有消息。true 删除漫游消息，false 删除本地消息，默认值 false |

### TIMDownloadType

UUID 类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMDownload_VideoThumb | 0 | 视频缩略图 |
| kTIMDownload_File | 1 | 文件 |
| kTIMDownload_Video | 2 | 视频 |
| kTIMDownload_Sound | 3 | 声音 |

### DownloadElemParam

下载元素接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDownloadElemParamFlag | uint | 只写 | 从消息元素里面取出来，元素的下载类型 |
| kTIMMsgDownloadElemParamType |  uint [TIMDownloadType](#timdownloadtype)  | 只写 | 从消息元素里面取出来，元素的类型 |
| kTIMMsgDownloadElemParamId | string | 只写 | 从消息元素里面取出来，元素的 ID |
| kTIMMsgDownloadElemParamBusinessId | uint | 只写 | 从消息元素里面取出来，元素的 BusinessID |
| kTIMMsgDownloadElemParamUrl | string | 只写 | 从消息元素里面取出来，元素 URL |

### MsgDownloadElemResult

下载元素接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDownloadElemResultCurrentSize | uint | 只读 | 当前已下载的大小 |
| kTIMMsgDownloadElemResultTotalSize | uint | 只读 | 需要下载的文件总大小 |

## 会话关键类型

会话相关宏定义，以及相关结构成员存取 JSON Key 定义。

### Draft

草稿信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMDraftMsg |  object [Message](#message)  | 只读 | 草稿内的消息 |
| kTIMDraftUserDefine | string | 只读 | 用户自定义数据 |
| kTIMDraftEditTime | uint | 只读 | 草稿最新编辑时间 |

### ConvInfo

草稿信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMConvId | string | 只读 | 会话 ID |
| kTIMConvType |  uint [TIMConvType](#timconvtype)  | 只读 | 会话类型 |
| kTIMConvOwner | string | 只读 | 会话所有者 |
| kTIMConvUnReadNum | uint64 | 只读 | 会话未读计数 |
| kTIMConvActiveTime | uint64 | 只读 | 会话的激活时间 |
| kTIMConvIsHasLastMsg | bool | 只读 | 会话是否有最后一条消息 |
| kTIMConvLastMsg |  object [Message](#message)  | 只读 | 会话最后一条消息 |
| kTIMConvIsHasDraft | bool | 只读 | 会话草稿 |
| kTIMConvDraft |  object [Draft](#draft)  | 只读（选填） | 会话草稿 |

## 群组关键类型

群组相关宏定义，以及相关结构成员存取 JSON Key 定义。

### TIMGroupAddOption

群组加群选项。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupAddOpt_Forbid | 0 | 禁止加群 |
| kTIMGroupAddOpt_Auth | 1 | 需要管理员审批 |
| kTIMGroupAddOpt_Any | 2 | 任何人都可以加群 |

### TIMGroupType

群组类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroup_Public | 0 | 公开群 |
| kTIMGroup_Private | 1 | 私有群 |
| kTIMGroup_ChatRoom | 2 | 聊天室 |
| kTIMGroup_BChatRoom | 3 | 在线成员广播大群 |
| kTIMGroup_AVChatRoom | 4 | 互动直播聊天室 |

### TIMGroupMemberRole

群组成员角色类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMMemberRole_Normal | 0 | 群成员 |
| kTIMMemberRole_Admin | 1 | 管理员 |
| kTIMMemberRole_SuperAdmin | 2 | 超级管理员 |

### GroupMemberInfo

群组成员信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupMemberInfoIdentifier | string | 读写（必填） | 群组成员 ID |
| kTIMGroupMemberInfoJoinTime | uint | 只读 | 群组成员加入时间 |
| kTIMGroupMemberInfoMemberRole |  uint [TIMGroupMemberRole](#timgroupmemberrole)  | 读写（选填） | 群组成员角色 |
| kTIMGroupMemberInfoMsgFlag | uint | 只读 | 成员接收消息的选项 |
| kTIMGroupMemberInfoMsgSeq | uint | 只读 | - |
| kTIMGroupMemberInfoShutupTime | uint | 只读 | 成员禁言时间 |
| kTIMGroupMemberInfoNameCard | string | 只读 | 成员群名片 |
| kTIMGroupMemberInfoCustomInfo |  object key string value string | 只读 | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)  |

### CreateGroupParam

创建群组接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMCreateGroupParamGroupName | string | 只写（必填） | 群组名称 |
| kTIMCreateGroupParamGroupId | string | 只写（选填） | 群组 ID，不填时创建成功回调会返回一个后台分配的群 ID |
| kTIMCreateGroupParamGroupType | uint [TIMGroupType](#timgrouptype)  | 只写（选填） | 群组类型，默认为 Public |
| kTIMCreateGroupParamGroupMemberArray |  array [GroupMemberInfo](#groupmemberinfo)  | 只写（选填） | 群组初始成员数组 |
| kTIMCreateGroupParamNotification | string | 只写（选填） | 群组公告， |
| kTIMCreateGroupParamIntroduction | string | 只写（选填） | 群组简介， |
| kTIMCreateGroupParamFaceUrl | string | 只写（选填） | 群组头像 URL |
| kTIMCreateGroupParamAddOption |  uint [TIMGroupAddOption](#timgroupaddoption)  | 只写（选填） | 加群选项，默认为 Any |
| kTIMCreateGroupParamMaxMemberCount | uint | 只写（选填） | 群组最大成员数 |
| kTIMCreateGroupParamCustomInfo |  object key string value string | 只读（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)  |

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
| kTIMGroupInviteMemberParamIdentifierArray |  array string | 只写（必填） | 被邀请加入群组用户 ID 数组 |
| kTIMGroupInviteMemberParamUserData | string | 只写（选填） | 用于自定义数据 |

### HandleGroupMemberResult

群组基础信息。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupMember_HandledErr | 0 | 失败 |
| kTIMGroupMember_HandledSuc | 1 | 成功 |
| kTIMGroupMember_Included | 2 | 已是群成员 |
| kTIMGroupMember_Invited | 3 | 已发送邀请 |

### GroupInviteMemberResult

邀请成员接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupInviteMemberResultIdentifier | string | 只读 | 被邀请加入群组的用户 ID |
| kTIMGroupInviteMemberResultResult |  uint [HandleGroupMemberResult](#handlegroupmemberresult)  | 只读 | 邀请结果 |

### GroupDeleteMemberParam

删除成员接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDeleteMemberParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupDeleteMemberParamIdentifierArray |  array string | 只写（必填） | 被删除群组成员数组 |
| kTIMGroupDeleteMemberParamUserData | string | 只写（选填） | 用于自定义数据 |

### GroupDeleteMemberResult

删除成员接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDeleteMemberResultIdentifier | string | 只读 | 删除的成员 ID |
| kTIMGroupDeleteMemberResultResult |  uint [HandleGroupMemberResult](#handlegroupmemberresult)  | 只读 | 删除结果 |

### TIMGroupReceiveMessageOpt

群组消息接收选项。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMRecvGroupMsgOpt_ReceiveAndNotify | 0 | 接收群消息并提示 |
| kTIMRecvGroupMsgOpt_NotReceive | 1 | 不接收群消息，服务器不会进行转发 |
| kTIMRecvGroupMsgOpt_ReceiveNotNotify | 2 | 接收群消息，不提示 |

### GroupSelfInfo

群组内本人的信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupSelfInfoJoinTime | uint | 只读 | 加入群组时间 |
| kTIMGroupSelfInfoRole | uint | 只读 | 用户在群组中的角色 |
| kTIMGroupSelfInfoUnReadNum | uint | 只读 | 消息未读计数 |
| kTIMGroupSelfInfoMsgFlag |  uint [TIMGroupReceiveMessageOpt](#timgroupreceivemessageopt)  | 只读 | 群消息接收选项 |

### GroupBaseInfo

获取已加入群组列表接口的返回（群组基础信息）。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupBaseInfoGroupId | string | 只读 | 群组 ID |
| kTIMGroupBaseInfoGroupName | string | 只读 | 群组名称 |
| kTIMGroupBaseInfoGroupType |  string [TIMGroupType](#timgrouptype)  | 只读 | 群组类型 |
| kTIMGroupBaseInfoFaceUrl | string | 只读 | 群组头像 URL |
| kTIMGroupBaseInfoInfoSeq | uint | 只读 | - |
| kTIMGroupBaseInfoLastestSeq | uint | 只读 | - |
| kTIMGroupBaseInfoReadedSeq | uint | 只读 | - |
| kTIMGroupBaseInfoMsgFlag | uint | 只读 | - |
| kTIMGroupBaseInfoIsShutupAll | bool | 只读 | 当前群组是否设置了全员禁言 |
| kTIMGroupBaseInfoSelfInfo |  object [GroupSelfInfo](#groupselfinfo)  | 只读 | 用户所在群的个人信息 |

### GroupDetailInfo

群组详细信息。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDetialInfoGroupId | string | 只读 | 群组 ID |
| kTIMGroupDetialInfoGroupType |  uint [TIMGroupType](#timgrouptype)  | 只读 | 群组类型 |
| kTIMGroupDetialInfoGroupName | string | 只读 | 群组名称 |
| kTIMGroupDetialInfoNotification | string | 只读 | 群组公告 |
| kTIMGroupDetialInfoIntroduction | string | 只读 | 群组简介 |
| kTIMGroupDetialInfoFaceUrl | string | 只读 | 群组头像 URL |
| kTIMGroupDetialInfoCreateTime | uint | 只读 | 群组创建时间 |
| kTIMGroupDetialInfoInfoSeq | uint | 只读 | - |
| kTIMGroupDetialInfoLastInfoTime | uint | 只读 | 群组信息最后修改时间 |
| kTIMGroupDetialInfoNextMsgSeq | uint | 只读 | - |
| kTIMGroupDetialInfoLastMsgTime | uint | 只读 | 最新群组消息时间 |
| kTIMGroupDetialInfoMemberNum | uint | 只读 | 群组当前成员数量 |
| kTIMGroupDetialInfoMaxMemberNum | uint | 只读 | 群组最大成员数量 |
| kTIMGroupDetialInfoAddOption |  uint [TIMGroupAddOption](#timgroupaddoption)  | 只读 | 群组加群选项 |
| kTIMGroupDetialInfoOnlineMemberNum | uint | 只读 | 群组在线成员数量 |
| kTIMGroupDetialInfoVisible | uint | 只读 | 群组成员是否对外可见 |
| kTIMGroupDetialInfoSearchable | uint | 只读 | 群组是否能被搜索 |
| kTIMGroupDetialInfoIsShutupAll | bool | 只读 | 群组是否被设置了全员禁言 |
| kTIMGroupDetialInfoOwnerIdentifier | string | 只读 | 群组所有者 ID |
| kTIMGroupDetialInfoCustomInfo |  object key string value string | 只读 | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)  |

### GetGroupInfoResult

获取群组信息列表接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGetGroupInfoResultCode |  int [错误码](https://cloud.tencent.com/document/product/269/1671)  | 只读 | 获取群组详细信息的结果 |
| kTIMGetGroupInfoResultDesc | string | 只读 | 获取群组详细失败的描述信息 |
| kTIMGetGroupInfoResultInfo |  json object [GroupDetailInfo](#groupdetailinfo)  | 只读 | 群组详细信息 |

### TIMGroupModifyInfoFlag

设置（修改）群组信息的类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupModifyInfoFlag_None | 0x00 | - |
| kTIMGroupModifyInfoFlag_Name | 0x01 | 修改群组名称， |
| kTIMGroupModifyInfoFlag_Notification | 0x01 << 1 | 修改群公告， |
| kTIMGroupModifyInfoFlag_Introduction | 0x01 << 2 | 修改群简介 |
| kTIMGroupModifyInfoFlag_FaceUrl | 0x01 << 3 | 修改群头像 URL |
| kTIMGroupModifyInfoFlag_AddOption | 0x01 << 4 | 修改群组添加选项， |
| kTIMGroupModifyInfoFlag_MaxMmeberNum | 0x01 << 5 | 修改群最大成员数， |
| kTIMGroupModifyInfoFlag_Visible | 0x01 << 6 | 修改群是否可见， |
| kTIMGroupModifyInfoFlag_Searchable | 0x01 << 7 | 修改群是否被搜索， |
| kTIMGroupModifyInfoFlag_ShutupAll | 0x01 << 8 | 修改群是否全体禁言， |
| kTIMGroupModifyInfoFlag_Owner | 0x01 << 31 | 修改群主 |

### GroupModifyInfoParam

设置群信息接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupModifyInfoParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupModifyInfoParamModifyFlag |  uint [TIMGroupModifyInfoFlag](#timgroupmodifyinfoflag)  | 只写（必填） | 修改标识，可设置多个值按位或 |
| kTIMGroupModifyInfoParamGroupName | string | 只写（选填） | 修改群组名称，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Name`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamNotification | string | 只写（选填） | 修改群公告，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Notification`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamIntroduction | string | 只写（选填） | 修改群简介，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Introduction`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamFaceUrl | string | 只写（选填） | 修改群头像 URL，当`modify_flag`包含`kTIMGroupModifyInfoFlag_FaceUrl`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamAddOption | uint | 只写（选填） | 修改群组添加选项，当`modify_flag`包含`kTIMGroupModifyInfoFlag_AddOption`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamMaxMemberNum | uint | 只写（选填） | 修改群最大成员数，当`modify_flag`包含`kTIMGroupModifyInfoFlag_MaxMmeberNum`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamVisible | uint | 只写（选填） | 修改群是否可见，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Visible`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamSearchAble | uint | 只写（选填） | 修改群是否被搜索，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Searchable`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamIsShutupAll | bool | 只写（选填） | 修改群是否全体禁言，当`modify_flag`包含`kTIMGroupModifyInfoFlag_ShutupAll`时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamOwner | string | 只写（选填） | 修改群主所有者，当`modify_flag`包含`kTIMGroupModifyInfoFlag_Owner`时必填，其他情况不用填。此时`modify_flag`不能包含其他值，当修改群主时，同时修改其他信息已无意义 |
| kTIMGroupModifyInfoParamCustomInfo |  object key string value string | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)  |

### GroupGetMemberInfoListParam

获取群成员列表接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetMemberInfoListParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupGetMemberInfoListParamIdentifierArray |  array string | 只写（选填） | 群成员 ID 列表 |
| kTIMGroupGetMemberInfoListParamOption |  object [GroupMemberGetInfoOption](#groupmembergetinfooption)  | 只写（选填） | 获取群成员信息的选项 |
| kTIMGroupGetMemberInfoListParamNextSeq | uint64 | 只写（选填） | 分页拉取标志，第一次拉取填0，回调成功如果不为零，需要分页，传入再次拉取，直至为0 |

### GroupGetMemberInfoListResult

获取群成员列表接口的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetMemberInfoListResultNexSeq | uint64 | 只读 | 下一次拉取的标志，server 返回0表示没有更多的数据，否则在下次获取数据时填入这个标志 |
| kTIMGroupGetMemberInfoListResultInfoArray |  array [GroupMemberInfo](#groupmemberinfo)  | 只读 | 成员信息列表 |

### TIMGroupMemberModifyInfoFlag

设置（修改）群成员信息的类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupMemberModifyFlag_None | 0x00 | - |
| kTIMGroupMemberModifyFlag_MsgFlag | 0x01 | 修改消息接收选项 |
| kTIMGroupMemberModifyFlag_MemberRole | 0x01 << 1 | 修改成员角色 |
| kTIMGroupMemberModifyFlag_ShutupTime | 0x01 << 2 | 修改禁言时间 |
| kTIMGroupMemberModifyFlag_NameCard | 0x01 << 3 | 修改群名片 |

### GroupModifyMemberInfoParam

设置群成员信息接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupModifyMemberInfoParamGroupId | string | 只写（必填） | 群组 ID |
| kTIMGroupModifyMemberInfoParamIdentifier | string | 只写（必填） | 被设置信息的成员 ID |
| kTIMGroupModifyMemberInfoParamModifyFlag |  uint [TIMGroupMemberModifyInfoFlag](#timgroupmembermodifyinfoflag)  | 只写（必填） | 修改类型，可设置多个值按位或 |
| kTIMGroupModifyMemberInfoParamMsgFlag | uint | 只写（选填） | 修改消息接收选项，当`modify_flag`包含`kTIMGroupMemberModifyFlag_MsgFlag`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamMemberRole |  uint [TIMGroupMemberRole](#timgroupmemberrole)  | 只写（选填） | 修改成员角色，当`modify_flag`包含`kTIMGroupMemberModifyFlag_MemberRole`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamShutupTime | uint | 只写（选填） | 修改禁言时间，当`modify_flag`包含`kTIMGroupMemberModifyFlag_ShutupTime`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamNameCard | string | 只写（选填） | 修改群名片，当`modify_flag`包含`kTIMGroupMemberModifyFlag_NameCard`时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamCustomInfo |  object key string value string | 只写（选填） | 请参考 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)  |

### GroupPendencyOption

获取群未决信息列表的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyOptionStartTime | uint64 | 只写（必填） | 设置拉取时间戳，第一次请求填0，后边根据 server 返回的 [GroupPendencyResult](#grouppendencyresult) 键 kTIMGroupPendencyResultNextStartTime 指定的时间戳进行填写 |
| kTIMGroupPendencyOptionMaxLimited | uint | 只写（选填） | 拉取的建议数量，server 可根据需要返回或多或少，不能作为完成与否的标志 |

### TIMGroupPendencyType

未决请求类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupPendency_RequestJoin | 0 | 请求加群 |
| kTIMGroupPendency_InviteJoin | 1 | 邀请加群 |
| kTIMGroupPendency_ReqAndInvite | 2 | 邀请和请求的 |

### TIMGroupPendencyHandle

群未决处理状态。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupPendency_NotHandle | 0 | 未处理 |
| kTIMGroupPendency_OtherHandle | 1 | 他人处理 |
| kTIMGroupPendency_OperatorHandle | 2 | 操作方处理 |

### TIMGroupPendencyHandleResult

群未决处理操作类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupPendency_Refuse | 0 | 拒绝 |
| kTIMGroupPendency_Accept | 1 | 同意 |

### GroupPendency

群未决信息定义。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyGroupId | string | 读写 | 群组 ID |
| kTIMGroupPendencyFromIdentifier | string | 读写 | 请求者的 ID。例如，请求加群：请求者，邀请加群：邀请人。 |
| kTIMGroupPendencyToIdentifier | string | 读写 | 判决者的 ID，请求加群：""，邀请加群：被邀请人。 |
| kTIMGroupPendencyAddTime | uint64 | 只读 | 未决信息添加时间 |
| kTIMGroupPendencyPendencyType |  uint [TIMGroupPendencyType](#timgrouppendencytype)  | 只读 | 未决请求类型 |
| kTIMGroupPendencyHandled |  uint [TIMGroupPendencyHandle](#timgrouppendencyhandle)  | 只读 | 群未决处理状态 |
| kTIMGroupPendencyHandleResult |  uint [TIMGroupPendencyHandleResult](#timgrouppendencyhandleresult)  | 只读 | 群未决处理操作类型 |
| kTIMGroupPendencyApplyInviteMsg | string | 只读 | 申请或邀请附加信息 |
| kTIMGroupPendencyFromUserDefinedData | string | 只读 | 申请或邀请者自定义字段 |
| kTIMGroupPendencyApprovalMsg | string | 只读 | 审批信息：同意或拒绝信息 |
| kTIMGroupPendencyToUserDefinedData | string | 只读 | 审批者自定义字段 |

### GroupPendencyResult

获取群未决信息列表的返回。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyResultNextStartTime | uint64 | 只读 | 下一次拉取的起始时戳，server 返回0表示没有更多的数据，否则在下次获取数据时以这个时间戳作为开始时间戳 |
| kTIMGroupPendencyResultReadTimeSeq | uint64 | 只读 | 已读上报的时间戳 |
| kTIMGroupPendencyResultUnReadNum | uint | 只读 | 未决请求的未读数？ |
| kTIMGroupPendencyResultPendencyArray |  array [GroupPendency](#grouppendency)  | 只读 | 群未决信息列表 |

### GroupHandlePendencyParam

处理群未决消息接口的参数。

| JSON 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupHandlePendencyParamIsAccept | bool | 只写（选填） | true 表示接受，false 表示拒绝。默认为 false |
| kTIMGroupHandlePendencyParamHandleMsg | string | 只写（选填） | 同意或拒绝信息，默认为空字符串 |
| kTIMGroupHandlePendencyParamPendency |  object [GroupPendency](#grouppendency)  | 只写（必填） | 未决信息详情 |

