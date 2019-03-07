## 错误码

### TIMErrCode

错误码。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| ERR_SUCC | 0 | 成功                |
| ERR_PARSE_RESPONSE_FAILED | 6001 | 回包解析失败,内部错误 |
| ERR_SERIALIZE_REQ_FAILED | 6002 | 文档未定义 |
| ERR_NO_SUCC_RESULT | 6003 | 批量操作无成功结果,请检查输入列表是否合法（如用户是否存在,传入列表类型是否与 API 匹配） |
| ERR_INVALID_CONVERSATION | 6004 | 会话无效,getConversation 时检查是否已经登录,如未登录获取会话,会有此错误码返回 |
| ERR_LOADMSG_FAILED | 6005 | 加载本地消息存储失败,可能存储文件有损坏 |
| ERR_FILE_TRANS_AUTH_FAILED | 6006 | 文件传输-鉴权失败 |
| ERR_FILE_TRANS_NO_SERVER | 6007 | 文件传输-获取 Server 列表失败 |
| ERR_FILE_TRANS_UPLOAD_FAILED | 6008 | 文件传输-上传失败,请检查网络是否连接 |
| ERR_FILE_TRANS_DOWNLOAD_FAILED | 6009 | 文件传输-下载失败,请检查网络,或者文件、语音是否已经过期,目前资源文件存储 7 天 |
| ERR_HTTP_REQ_FAILED | 6010 | HTTP 请求失败 |
| ERR_TO_USER_INVALID | 6011 | 消息接收方无效,对方用户不存在（接收方需登录过 IMSDK 或用帐号导入接口导入） |
| ERR_REQUEST_TIMEOUT | 6012 | 请求超时,请等网络恢复后重试。（Android SDK 1.8.0 以上需要参考 Android 服务进程配置方式进行配置,否则会出现此错误） |
| ERR_SDK_NOT_INITIALIZED | 6013 | SDK 未初始化或者用户未登录成功,请先登录,成功回调之后重试 |
| ERR_SDK_NOT_LOGGED_IN | 6014 | SDK 未登录,请先登录,成功回调之后重试,或者被踢下线,可使用 TIMManager getLoginUser 检查当前是否在线 |
| ERR_IN_PROGESS | 6015 | 请做好接口调用控制,第一次 login 操作回调前,后续的 login 操作会返回该错误码 |
| ERR_INVALID_MSG_ELEM | 6016 | 注册超时,需要重试 |
| ERR_INVALID_PARAMETERS | 6017 | API 参数无效,请检查参数是否符合要求,具体可查看错误信息进一步定义哪个字段 |
| ERR_INIT_CORE_FAIL | 6018 | SDK 初始化失败,可能是部分目录无权限 |
| ERR_DATABASE_OPERATE_FAILED | 6019 | 本地数据库操作失败,可能是部分目录无权限或者数据库文件已损坏 |
| ERR_EXPIRED_SESSION_NODE | 6020 | Session Node 过期 |
| ERR_INVALID_SDK_OBJECT | 6021 | 下载资源文件参数错误,如还未上传成功调用接口下载资源,或者用户自己生成 TIMImage 等对象 |
| ERR_IO_OPERATION_FAILED | 6022 | 操作本地 IO 错误,检查是否有读写权限,磁盘是否已满 |
| ERR_LOGGED_OUT_BEFORE_LOGIN_FINISHED | 6023 | 在登录操作没有完成前进行了登出操作（或者被踢下线） |
| ERR_TLSSDK_NOT_INITIALIZED | 6024 | TLSSDK未初始化 |
| ERR_TLSSDK_FIND_NO_USER | 6025 | TLSSDK没有找到相应的用户信息 |
| ERR_REQUEST_NO_NET_ONREQ | 6200 | 请求时没有网络,请等网络恢复后重试 |
| ERR_REQUEST_NO_NET_ONRSP | 6201 | 响应时没有网络,请等网络恢复后重试 |
| ERR_SERIVCE_NOT_READY | 6205 | QAL服务未启动 |
| ERR_USER_SIG_EXPIRED | 6206 | 票据过期(imcore) |
| ERR_LOGIN_KICKED_OFF_BY_OTHER | 6208 | 其他终端登录帐号被踢,需重新登录 |
| ERR_NEVER_CONNECT_AFTER_LAUNCH | 6209 | 程序启动后没有尝试联网 |
| ERR_REQUEST_FAILED | 6210 | QAL执行失败 |
| ERR_REQUEST_INVALID_REQ | 6211 | 请求非法,toMsgService非法 |
| ERR_REQUEST_OVERLOADED | 6212 | 请求队列満 |
| ERR_REQUEST_KICK_OFF | 6213 | 已经被其他终端踢了 |
| ERR_REQUEST_SERVICE_SUSPEND | 6214 | 服务被暂停 |
| ERR_REQUEST_INVALID_SIGN | 6215 | SSO签名错误 |
| ERR_REQUEST_INVALID_COOKIE | 6216 | SSO cookie无效 |
| ERR_LOGIN_TLS_RSP_PARSE_FAILED | 6217 | 登录时TLS回包校验,包体长度错误 |
| ERR_LOGIN_OPENMSG_TIMEOUT | 6218 | 登录时OPENSTATSVC向OPENMSG上报状态时超时 |
| ERR_LOGIN_OPENMSG_RSP_PARSE_FAILED | 6219 | 登录时OPENSTATSVC向OPENMSG上报状态时解析回包失败 |
| ERR_LOGIN_TLS_DECRYPT_FAILED | 6220 | 登录时TLS解密失败 |
| ERR_WIFI_NEED_AUTH | 6221 | 连接上的wifi需要认证（不认证的情况下,无法连接网络） |
| ERR_USER_CANCELED | 6222 | 用户已取消 |
| ERR_REVOKE_TIME_LIMIT_EXCEED | 6223 | 消息撤回超过了时间限制（默认2分钟） |
| ERR_QAL_NO_SHORT_CONN_AVAILABLE | 6300 | 没有可用的短连接sso |

### TIMResult

调用接口的返回值。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| TIM_SUCC | 0 | 接口调用成功 |
| TIM_ERR_SDKUNINIT | -1 | 接口调用失败,SDK未初始化 |
| TIM_ERR_NOTLOGIN | -2 | 接口调用失败,用户未登入 |
| TIM_ERR_JSON | -3 | 接口调用失败,错误的Json格式或Json Key |
| TIM_ERR_PARAM | -4 | 接口调用成功,参数错误 |
| TIM_ERR_CONV | -5 | 接口调用成功,无效的会话 |
| TIM_ERR_GROUP | -6 | 接口调用成功,无效的群组 |



## 相关配置选项

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
| kTIMConvEvent_Add | 0 | 会话新增,比如收到一条新消息,产生一个新的会话是事件触发 |
| kTIMConvEvent_Del | 1 | 会话删除,比如自己删除某会话时会触发 |
| kTIMConvEvent_Update | 2 | 会话更新,会话内消息的未读计数变化和收到新消息时触发 |

### TIMPlatform

平台类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMPlatform_Android | 0 | Android平台 |
| kTIMPlatform_IOS | 1 | IOS平台 |
| kTIMPlatform_Mac | 2 | Mac平台 |
| kTIMPlatform_Simulator | 3 | 模拟器 |
| kTIMPlatform_Windows | 4 | Windows平台 |
| kTIMPlatform_Other | 5 | 其他 |



## 消息相关结构 

### TIMConvType

会话类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMConv_Invalid | 0 | 无效会话 |
| kTIMConv_C2C | 1 | 个人会话 |
| kTIMConv_Group | 2 | 群组会话 |
| kTIMConv_System | 3 | 系统会话 |

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
| kTIMMsgPriority_Lowest | 3 | 优先级最低，一般为成员进退群通知(后台下发) |

### Message

消息Json Keys。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgElemArray | array  [Elem](https://cloud.tencent.com/document/product/269/33487#Elem)  | 读写(必填) | 消息内元素列表 |
| kTIMMsgConvId | string | 读写(选填) | 消息所属会话ID |
| kTIMMsgConvType | uint  [TIMConvType](https://cloud.tencent.com/document/product/269/33487#TIMConvType)  | 读写(选填) | 消息所属会话类型 |
| kTIMMsgSender | string | 读写(选填) | 消息的发送者 |
| kTIMMsgClientTime | uint64 | 读写(选填) | 客户端时间 |
| kTIMMsgServerTime | uint64 | 读写(选填) | 服务端时间 |
| kTIMMsgIsFormSelf | bool | 读写(选填) | 消息是否来自自己 |
| kTIMMsgIsRead | bool | 读写(选填) | 消息是否已读 |
| kTIMMsgStatus | uint  [TIMMsgStatus](https://cloud.tencent.com/document/product/269/33487#TIMMsgStatus)  | 读写(选填) | 消息当前状态 |
| kTIMMsgRand | uint64 | 读写(选填) | 唯一标识 |
| kTIMMsgSeq | uint64 | 读写(选填) | 消息序列 |
| kTIMMsgPriority | uint  [TIMMsgPriority](https://cloud.tencent.com/document/product/269/33487#TIMMsgPriority)  | 读写(选填) | 消息优先级 |
| kTIMMsgCustom | string | 读写(选填) | 用于自定义字段(与后台协商) |

**注释： 1. 对应Elem的顺序**

>目前文件和语音 Elem 不一定会按照添加顺序传输，其他 Elem 按照顺序，不过建议不要过于依赖 Elem 顺序进行处理，应该逐个按照 Elem 类型处理，防止异常情况下进程 Crash。

**注释： 2. 针对群组的红包和点赞消息**

>对于直播场景，会有点赞和发红包功能，点赞相对优先级较低，红包消息优先级较高，具体消息内容可以使用 TIMCustomElem 进行定义，发送消息时，可使用不同接口定义消息优先级。具体消息优先级的策略，可参阅 [互动直播集成多人聊天方案](https://cloud.tencent.com/document/product/269/3885#互动直播集成多人聊天方案) 。

**注释： 3. 消息自定义字段**

>开发者可以对消息增加自定义字段，如自定义整数、自定义二进制数据(必须转换成String，Json不支持二进制传输)，可以根据这两个字段做出各种不通效果，比如语音消息是否已经播放等等。另外需要注意，此自定义字段仅存储于本地，不会同步到 Server，更换终端获取不到。


### MessageReceipt

消息已读回执。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgReceiptConvId | string | 只读 | 会话ID |
| kTIMMsgReceiptConvType | uint  [TIMConvType](https://cloud.tencent.com/document/product/269/33487#TIMConvType)  | 只读 | 会话类型 |
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

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMElemType | uint  [TIMElemType](https://cloud.tencent.com/document/product/269/33487#TIMElemType)  | 读写(必填) | 元素类型 |

### TextElem

文本元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMTextElemContent | string | 读写(必填) | 文本内容 |

### FaceElem

表情元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFaceElemIndex | int | 读写(必填) | 表情索引 |
| kTIMFaceElemBuf | string | 读写(选填) | 其他额外数据，可由用户自定义填写。若要传输二进制，麻烦先转码成字符串。Json只支持字符串 |

**注释：**

>SDK 并不提供表情包，如果开发者有表情包，可使用 `kTIMFaceElemIndex` 存储表情在表情包中的索引，由用户自定义。 或者直接使用 `kTIMFaceElemBuf` 存储表情二进制信息(必须转换成String，Json不支持二进制传输)，由用户自定义，SDK 内部只做透传。


### LocationElem

位置元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMLocationElemDesc | string | 读写(选填) | 位置描述 |
| kTIMLocationElemLongitude | double | 读写(必填) | 经度 |
| kTIMLocationElemlatitude | double | 读写(必填) | 纬度 |

### TIMImageLevel

图片质量级别。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMImageLevel_Orig | 0 | 原图发送 |
| kTIMImageLevel_Compression | 1 | 高压缩率图发送(图片较小,默认值) |
| kTIMImageLevel_HD | 2 | 高清图发送(图片较大) |

### ImageElem

图片元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMImageElemOrigPath | string | 读写(必填) | 发送图片的路径 |
| kTIMImageElemLevel | uint [TIMImageLevel](https://cloud.tencent.com/document/product/269/33487#TIMImageLevel)  | 读写(必填) | 发送图片的质量级别 |
| kTIMImageElemFormat | int | 读写(必填) | 发送图片格式 |
| kTIMImageElemOrigId | string | 只读 | 原图的uuid |
| kTIMImageElemOrigPicHeight | int | 只读 | 原图的图片高度 |
| kTIMImageElemOrigPicWidth | int | 只读 | 原图的图片高度 |
| kTIMImageElemOrigPicSize | int | 只读 | 原图的图片高度 |
| kTIMImageElemThumbId | string | 只读 | 略缩图uuid |
| kTIMImageElemThumbPicHeight | int | 只读 | 略缩图的图片高度 |
| kTIMImageElemThumbPicWidth | int | 只读 | 略缩图的图片高度 |
| kTIMImageElemThumbPicSize | int | 只读 | 略缩图的图片高度 |
| kTIMImageElemLargeId | string | 只读 | 大图片uuid |
| kTIMImageElemLargePicHeight | int | 只读 | 大图片的图片高度 |
| kTIMImageElemLargePicWidth | int | 只读 | 大图片的图片高度 |
| kTIMImageElemLargePicSize | int | 只读 | 大图片的图片高度 |
| kTIMImageElemOrigUrl | string | 只读 | 原图URL |
| kTIMImageElemThumbUrl | string | 只读 | 略缩图URL |
| kTIMImageElemLargeUrl | string | 只读 | 大图片URL |
| kTIMImageElemTaskId | int | 只读 | 任务ID |

**注释：**

>1. 图片规格说明：每幅图片有三种规格，分别是 Original（原图）、Large（大图）、Thumb（缩略图）。 。
>   原图：指用户发送的原始图片，尺寸和大小都保持不变。 。
>   大图：是将原图等比压缩，压缩后宽、高中较小的一个等于 720 像素。 。
>   缩略图：是将原图等比压缩，压缩后宽、高中较小的一个等于 198 像素 。
>2. 如果原图尺寸就小于 198 像素，则三种规格都保持原始尺寸，不需压缩。 。
>3. 如果原图尺寸在 198~720 之间，则大图和原图一样，不需压缩。 。
>4. 在手机上展示图片时，建议优先展示缩略图，用户单击缩略图时再下载大图，单击大图时再下载原图。当然开发者也可以选择跳过大图，单击缩略图时直接下载原图。 。
>5. 在 Pad 或 PC 上展示图片时，由于分辨率较大，且基本都是 Wi-Fi 或有线网络，建议直接显示大图，用户单击大图时再下载原图。


### SoundElem

声音元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMSoundElemFilePath | string | 读写(必填) | 语音文件路径，需要客户自己先保存语言然后指定路径 |
| kTIMSoundElemFileSize | int | 读写(必填) | 语言数据文件大小，以秒为单位 |
| kTIMSoundElemFileTime | int | 读写(必填) | 语音时长 |
| kTIMSoundElemFileId | string | 只读 | 下载声音文件时的id |
| kTIMSoundElemBusinessId | int | 只读 | 下载时用到的businessID |
| kTIMSoundElemDownloadFlag | int | 只读 | 是否需要申请下载地址(0:到架平申请  1:到cos申请  2:不需要申请，直接拿url下载) |
| kTIMSoundElemUrl | string | 只读 | 下载的URL |
| kTIMSoundElemTaskId | int | 只读 | 任务ID |

**注释：**

>1. 语音是否已经播放，可使用 消息自定义字段 实现，如定义一个字段值 0 表示未播放，1表示播放，当用户单击播放后可设置改字段的值为1 。
>2. 一条消息只能添加一个声音元素，添加多个声音元素时，发送消息可能失败。


### CustomElem

自定义元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMCustomElemData | string | 读写() | 数据，支持二进制数据 |
| kTIMCustomElemDesc | string | 读写() | 自定义描述 |
| kTIMCustomElemExt | string | 读写() | 后台推送对应的ext字段 |
| kTIMCustomElemSound | string | 读写() | 自定义声音，这个声音是给谁听的 |

**注释：**

>自定义消息是指当内置的消息类型无法满足特殊需求，开发者可以自定义消息格式，内容全部由开发者定义，ImSDK 只负责透传。


### FileElem

文件元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMFileElemFilePath | string | 读写(必填) | 文件所在路径（包含文件名） |
| kTIMFileElemFileName | string | 读写(选填) | 文件名，显示的名称 |
| kTIMFileElemFileSize | int | 读写(必填) | 文件大小 |
| kTIMFileElemFileId | string | 只读 | 下载视频时的uuid |
| kTIMFileElemBusinessId | int | 只读 | 下载时用到的businessID |
| kTIMFileElemDownloadFlag | int | 只读 | 文件下载flag |
| kTIMFileElemUrl | string | 只读 | 文件下载的URL |
| kTIMFileElemTaskId | int | 只读 | 任务ID |

**注释：**

>一条消息只能添加一个文件元素，添加多个文件时，发送消息可能失败。


### VideoElem

视频元素。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMVideoElemVideoType | string | 读写(必填) | 视频文件类型，发送消息时进行设置 |
| kTIMVideoElemVideoSize | uint | 读写(必填) | 视频文件大小 |
| kTIMVideoElemVideoDuration | uint | 读写(必填) | 视频时长，发送消息时进行设置 |
| kTIMVideoElemVideoPath | string | 读写(必填) | 适配文件路径 |
| kTIMVideoElemVideoId | string | 只读 | 下载视频时的uuid |
| kTIMVideoElemBusinessId | int | 只读 | 下载时用到的businessID |
| kTIMVideoElemVideoDownloadFlag | int | 只读 | 视频文件下载flag |
| kTIMVideoElemVideoUrl | string | 只读 | 视频文件下载的URL |
| kTIMVideoElemImageType | string | 读写(必填) | 截图文件类型，发送消息时进行设置 |
| kTIMVideoElemImageSize | uint | 读写(必填) | 截图文件大小 |
| kTIMVideoElemImageWidth | uint | 读写(必填) | 截图高度，发送消息时进行设置 |
| kTIMVideoElemImageHeight | uint | 读写(必填) | 截图宽度，发送消息时进行设置 |
| kTIMVideoElemImagePath | string | 读写(必填) | 保存截图的路径 |
| kTIMVideoElemImageId | string | 只读 | 下载视频截图时的id |
| kTIMVideoElemImageDownloadFlag | int | 只读 | 截图文件下载flag |
| kTIMVideoElemImageUrl | string | 只读 | 截图文件下载的URL |
| kTIMVideoElemTaskId | uint | 只读 | 任务ID |

### TIMGroupTipGroupChangeFlag

群组信息修改的类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupTipChangeFlag_Name | 0xa | 修改群组名称 |
| kTIMGroupTipChangeFlag_Introduction | 11 | 修改群简介 |
| kTIMGroupTipChangeFlag_Notification | 12 | 修改群公告 |
| kTIMGroupTipChangeFlag_FaceUrl | 13 | 修改群头像URL |
| kTIMGroupTipChangeFlag_Owner | 14 | 修改群所有者 |

### GroupTipGroupChangeInfo

群组系统消息-群组信息修改。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipGroupChangeInfoFlag | uint  [TIMGroupTipGroupChangeFlag](https://cloud.tencent.com/document/product/269/33487#TIMGroupTipGroupChangeFlag)  | 只读 | 群消息修改群信息标志 |
| kTIMGroupTipGroupChangeInfoValue | string | 只读 | 修改的后值，不同的info_flag字段，具有不同的含义 |

### GroupTipMemberChangeInfo

群组系统消息-群组成员禁言。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipMemberChangeInfoIdentifier | string | 只读 | 群组成员ID |
| kTIMGroupTipMemberChangeInfoShutupTime | uint | 只读 | 禁言时间 |

### UserProfile

用户个人资料。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMUserProfileIdentifier | string | 只读 | 用户ID |
| kTIMUserProfileNickName | string | 只读 | 用户的昵称 |
| kTIMUserProfileFaceURL | string | 只读 | 用户头像URL |
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

群组系统消息元素(针对所有群成员)。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupTipsElemTipType | uint  [TIMGroupTipType](https://cloud.tencent.com/document/product/269/33487#TIMGroupTipType)  | 只读 | 群消息类型 |
| kTIMGroupTipsElemOpUser | string | 只读 | 操作者ID |
| kTIMGroupTipsElemGroupName | string | 只读 | 群组名称 |
| kTIMGroupTipsElemGroupId | string | 只读 | 群组ID |
| kTIMGroupTipsElemTime | uint | 只读 | 群消息时间 |
| kTIMGroupTipsElemUserArray | array string | 只读 | 被操作的帐号列表 |
| kTIMGroupTipsElemGroupChangeInfoArray | array  [GroupTipGroupChangeInfo](https://cloud.tencent.com/document/product/269/33487#GroupTipGroupChangeInfo)  | 只读 | 群资料变更信息列表，仅当tips_type值为kTIMGroupTip_GroupInfoChange时有效 |
| kTIMGroupTipsElemMemberChangeInfoArray | array  [GroupTipMemberChangeInfo](https://cloud.tencent.com/document/product/269/33487#GroupTipMemberChangeInfo)  | 只读 | 群成员变更信息列表，仅当tips_type值为kTIMGroupTip_MemberInfoChange时有效 |
| kTIMGroupTipsElemOpUserInfo | object  [UserProfile](https://cloud.tencent.com/document/product/269/33487#UserProfile)  | 只读 | 操作者个人资料 |
| kTIMGroupTipsElemOpGroupMemberInfo | object  [GroupMemberInfo](https://cloud.tencent.com/document/product/269/33487#GroupMemberInfo)  | 只读 | 群成员信息 |
| kTIMGroupTipsElemChangedUserInfoArray | array  [UserProfile](https://cloud.tencent.com/document/product/269/33487#UserProfile)  | 只读 | 被操作者列表资料 |
| kTIMGroupTipsElemChangedGroupMemberInfoArray | array  [GroupMemberInfo](https://cloud.tencent.com/document/product/269/33487#GroupMemberInfo)  | 只读 | 群成员信息列表 |
| kTIMGroupTipsElemMemberNum | uint | 只读 | 当前群成员数，只有当事件消息类型为kTIMGroupTip_Invite、kTIMGroupTip_Quit、kTIMGroupTip_Kick的时候有效 |
| kTIMGroupTipsElemPlatform | string | 只读 | 操作方平台信息 |

### TIMGroupReportType

群组系统通知类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupReport_None | 0 | 未知类型 |
| kTIMGroupReport_AddRequest | 1 | 申请加群(只有管理员会接收到) |
| kTIMGroupReport_AddAccept | 2 | 申请加群被同意(只有申请人自己接收到) |
| kTIMGroupReport_AddRefuse | 3 | 申请加群被拒绝(只有申请人自己接收到) |
| kTIMGroupReport_BeKicked | 4 | 被管理员踢出群(只有被踢者接收到) |
| kTIMGroupReport_Delete | 5 | 群被解散(全员接收) |
| kTIMGroupReport_Create | 6 | 创建群(创建者接收, 不展示) |
| kTIMGroupReport_Invite | 7 | 邀请加群(被邀请者接收) |
| kTIMGroupReport_Quit | 8 | 主动退群(主动退出者接收, 不展示) |
| kTIMGroupReport_GrantAdmin | 9 | 设置管理员(被设置者接收) |
| kTIMGroupReport_CancelAdmin | 10 | 取消管理员(被取消者接收) |
| kTIMGroupReport_RevokeAdmin | 11 | 群已被回收(全员接收, 不展示) |
| kTIMGroupReport_InviteReq | 12 | 邀请加群(只有被邀请者会接收到) |
| kTIMGroupReport_InviteAccept | 13 | 邀请加群被同意(只有发出邀请者会接收到) |
| kTIMGroupReport_InviteRefuse | 14 | 邀请加群被拒绝(只有发出邀请者会接收到) |
| kTIMGroupReport_ReadedSync | 15 | 已读上报多终端同步通知(只有上报人自己收到) |
| kTIMGroupReport_UserDefine | 16 | 用户自定义通知(默认全员接收) |

### GroupReportElem

群组系统通知元素(针对个人)。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupReportElemReportType | uint  [TIMGroupReportType](https://cloud.tencent.com/document/product/269/33487#TIMGroupReportType)  | 只读 | 类型 |
| kTIMGroupReportElemGroupId | string | 只读 | 群组ID |
| kTIMGroupReportElemGroupName | string | 只读 | 群组名称 |
| kTIMGroupReportElemOpUser | string | 只读 | 操作者ID |
| kTIMGroupReportElemMsg | string | 只读 | 操作理由 |
| kTIMGroupReportElemUserData | string | 只读 | 操作者填的自定义数据 |
| kTIMGroupReportElemOpUserInfo | object  [UserProfile](https://cloud.tencent.com/document/product/269/33487#UserProfile)  | 只读 | 操作者个人资料 |
| kTIMGroupReportElemOpGroupMemberInfo | object  [GroupMemberInfo](https://cloud.tencent.com/document/product/269/33487#GroupMemberInfo)  | 只读 | 操作者群内资料 |
| kTIMGroupReportElemPlatform | string | 只读 | 操作方平台信息 |

### MsgBatchSendParam

消息群发接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgBatchSendParamIdentifierArray | array string | 只写(必填) | 群发的ID列表 |
| kTIMMsgBatchSendParamMsg | object  [Message](https://cloud.tencent.com/document/product/269/33487#Message)  | 只写(必须) | 群发的消息 |

### MsgBatchSendResult

消息群发接口的返回。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgBatchSendResultIdentifier | string | 只读 | 群发的单个ID |
| kTIMMsgBatchSendResultCode | int [TIMErrCode](https://cloud.tencent.com/document/product/269/33487#TIMErrCode)  | 只读 | 消息发送结果 |
| kTIMMsgBatchSendResultDesc | string | 只读 | 消息发送的描述 |

### MsgLocator

消息定位符。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgLocatorConvId | bool | 读写 | 要查找的消息是否是被撤回。true被撤回的，false非撤回的。默认值为false |
| kTIMMsgLocatorConvType | bool | 读写 | 要查找的消息是否是被撤回。true被撤回的，false非撤回的。默认值为false |
| kTIMMsgLocatorIsRevoked | bool | 读写(必填) | 要查找的消息是否是被撤回。true被撤回的，false非撤回的。默认值为false |
| kTIMMsgLocatorTime | uint | 读写(必填) | 要查找的消息的时间戳 |
| kTIMMsgLocatorSeq | uint64 | 读写(必填) | 要查找的消息的序列号 |
| kTIMMsgLocatorIsSelf | bool | 读写(必填) | 要查找的消息的发送者是否是自己。true发送者是自己，false发送者不是自己。默认值为false |
| kTIMMsgLocatorRand | uint64 | 读写(必填) | 要查找的消息随机码 |

### MsgGetMsgListParam

消息获取接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgGetMsgListParamLastMsg | object  [Message](https://cloud.tencent.com/document/product/269/33487#Message)  | 只写(选填) | 指定的消息，不允许为null |
| kTIMMsgGetMsgListParamCount | uint | 只写(选填) | 从指定消息往后的消息数 |
| kTIMMsgGetMsgListParamIsRamble | bool | 只写(选填) | 是否漫游消息 |
| kTIMMsgGetMsgListParamIsForward | bool | 只写(选填) | 是否向前排序 |

### MsgDeleteParam

消息删除接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDeleteParamMsg | object  [Message](https://cloud.tencent.com/document/product/269/33487#Message)  | 只写(选填) | 指定在会话中要删除的消息 |
| kTIMMsgDeleteParamIsRamble | bool | 只写(选填) | 是否删除本地/漫游所有消息。true删除漫游消息，false删除本地消息，默认值false |

### TIMDownloadType

UUID类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMDownload_VideoThumb | 0 | 视频缩略图 |
| kTIMDownload_File | 1 | 文件 |
| kTIMDownload_Video | 2 | 视频 |
| kTIMDownload_Sound | 3 | 声音 |

### DownloadElemParam

下载元素接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDownloadElemParamFlag | uint | 只写 | 从消息元素里面取出来，元素的下载类型 |
| kTIMMsgDownloadElemParamType | uint  [TIMDownladType](https://cloud.tencent.com/document/product/269/33487#TIMDownladType)  | 只写 | 从消息元素里面取出来，元素的类型 |
| kTIMMsgDownloadElemParamId | string | 只写 | 从消息元素里面取出来，元素的ID |
| kTIMMsgDownloadElemParamBusinessId | uint | 只写 | 从消息元素里面取出来，元素的BusinessID |
| kTIMMsgDownloadElemParamUrl | string | 只写 | 从消息元素里面取出来，元素URL |

### MsgDownloadElemResult

下载元素接口的返回。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMMsgDownloadElemResultCurrentSize | uint | 只读 | 当前已下载的大小 |
| kTIMMsgDownloadElemResultTotalSize | uint | 只读 | 需要下载的文件总大小 |



## 会话相关结构

### Draft

草稿信息。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMDraftMsg | object  [Message](https://cloud.tencent.com/document/product/269/33487#Message)  | 只读 | 草稿内的消息 |
| kTIMDraftUserDefine | string |  |  |
| kTIMDraftEditTime | uint |  |  |

### ConvInfo

草稿信息。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMConvId | string | 只读 | 会话ID |
| kTIMConvType | uint  [TIMConvType](https://cloud.tencent.com/document/product/269/33487#TIMConvType)  | 只读 | 会话类型 |
| kTIMConvOwner | string | 只读 | 会话所有者 |
| kTIMConvUnReadNum | uint64 | 只读 | 会话未读计数 |
| kTIMConvActiveTime | uint64 | 只读 | 会话的激活时间 |
| kTIMConvIsHasLastMsg | bool | 只读 | 会话是否有最后一条消息 |
| kTIMConvLastMsg | object  [Message](https://cloud.tencent.com/document/product/269/33487#Message)  | 只读 | 会话最后一条消息 |
| kTIMConvIsHasDraft | bool | 只读 | 会话草稿 |
| kTIMConvDraft | object  [Draft](https://cloud.tencent.com/document/product/269/33487#Draft)  | 只读(可选) | 会话草稿 |



## 群组相关结构

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

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupMemberInfoIdentifier | string | 读写(必填) | 群组成员ID |
| kTIMGroupMemberInfoJoinTime | uint | 只读 | 群组成员加入时间 |
| kTIMGroupMemberInfoMemberRole | uint  [TIMGroupMemberRole](https://cloud.tencent.com/document/product/269/33487#TIMGroupMemberRole)  | 读写(选填) | 群组成员角色 |
| kTIMGroupMemberInfoMsgFlag | uint | 只读 | 成员接收消息的选项 |
| kTIMGroupMemberInfoMsgSeq | uint | 只读 |  |
| kTIMGroupMemberInfoShutupTime | uint | 只读 | 成员禁言时间 |
| kTIMGroupMemberInfoNameCard | string | 只读 | 成员群名片 |
| kTIMGroupMemberInfoCustomInfo | object <string | string> | 只读，详见 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5#自定义字段)  |

### CreateGroupParam

创建群组接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMCreateGroupParamGroupName | string | 只写(必填) | 群组名称 |
| kTIMCreateGroupParamGroupId | string | 只写(选填) | 群组ID，不填时创建成功回调会返回一个后台分配的群ID |
| kTIMCreateGroupParamGroupType | uint。 [TIMGroupType](https://cloud.tencent.com/document/product/269/33487#TIMGroupType)  | 只写(选填) | 群组类型，默认为Public |
| kTIMCreateGroupParamGroupMemberArray | array  [GroupMemberInfo](https://cloud.tencent.com/document/product/269/33487#GroupMemberInfo)  | 只写(选填) | 群组初始成员数组 |
| kTIMCreateGroupParamNotification | string | 只写(选填) | 群组公告， |
| kTIMCreateGroupParamIntroduction | string | 只写(选填) | 群组简介， |
| kTIMCreateGroupParamFaceUrl | string | 只写(选填) | 群组头像URL |
| kTIMCreateGroupParamAddOption | uint  [TIMGroupAddOption](https://cloud.tencent.com/document/product/269/33487#TIMGroupAddOption)  | 只写(选填) | 加群选项，默认为Any |
| kTIMCreateGroupParamMaxMemberCount | uint | 只写(选填) | 群组最大成员数 |
| kTIMCreateGroupParamCustomInfo | object <string | string> | 只读(选填)，详见 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5#自定义字段)  |

### CreateGroupResult

创建群组接口的返回。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMCreateGroupResultGroupId | string | 只读 | 创建的群ID |

### GroupInviteMemberParam

邀请成员接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupInviteMemberParamGroupId | string | 只写(必填) | 群组ID |
| kTIMGroupInviteMemberParamIdentifierArray | array string | 只写(必填) | 被邀请加入群组用户ID数组 |
| kTIMGroupInviteMemberParamUserData | string | 只写(选填) | 用于自定义数据 |

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

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupInviteMemberResultIdentifier | string | 只读 | 被邀请加入群组的用户ID |
| kTIMGroupInviteMemberResultResult | uint  [HandleGroupMemberResult](https://cloud.tencent.com/document/product/269/33487#HandleGroupMemberResult)  | 只读 | 邀请结果 |

### GroupDeleteMemberParam

删除成员接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDeleteMemberParamGroupId | string | 只写(必填) | 群组ID |
| kTIMGroupDeleteMemberParamIdentifierArray | array string | 只写(必填) | 被删除群组成员数组 |
| kTIMGroupDeleteMemberParamUserData | string | 只写(选填) | 用于自定义数据 |

### GroupDeleteMemberResult

删除成员接口的返回。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDeleteMemberResultIdentifier | string | 只读 | 删除的成员ID |
| kTIMGroupDeleteMemberResultResult | uint  [HandleGroupMemberResult](https://cloud.tencent.com/document/product/269/33487#HandleGroupMemberResult)  | 只读 | 删除结果 |

### TIMGroupReceiveMessageOpt

群组消息接收选项。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMRecvGroupMsgOpt_ReceiveAndNotify | 0 | 接收群消息 并提示 |
| kTIMRecvGroupMsgOpt_NotReceive | 1 | 不接收群消息, 服务器不会进行转发 |
| kTIMRecvGroupMsgOpt_ReceiveNotNotify | 2 | 接收群消息,不提示 |

### GroupSelfInfo

群组内本人的信息。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupSelfInfoJoinTime | uint | 只读 | 加入群组时间 |
| kTIMGroupSelfInfoRole | uint | 只读 | 用户在群组中的角色 |
| kTIMGroupSelfInfoUnReadNum | uint | 只读 | 消息未读计数 |
| kTIMGroupSelfInfoMsgFlag | uint  [TIMGroupReceiveMessageOpt](https://cloud.tencent.com/document/product/269/33487#TIMGroupReceiveMessageOpt)  | 只读 | 群消息接收选项 |

### GroupBaseInfo

获取已加入群组列表接口的返回(群组基础信息)。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupBaseInfoGroupId | string | 只读 | 群组ID |
| kTIMGroupBaseInfoGroupName | string | 只读 | 群组名称 |
| kTIMGroupBaseInfoGroupType | string  [TIMGroupType](https://cloud.tencent.com/document/product/269/33487#TIMGroupType)  | 只读 | 群组类型 |
| kTIMGroupBaseInfoFaceUrl | string | 只读 | 群组头像URL |
| kTIMGroupBaseInfoInfoSeq | uint | 只读 |  |
| kTIMGroupBaseInfoLastestSeq | uint | 只读 |  |
| kTIMGroupBaseInfoReadedSeq | uint | 只读 |  |
| kTIMGroupBaseInfoMsgFlag | uint | 只读 |  |
| kTIMGroupBaseInfoIsShutupAll | bool | 只读 | 当前群组是否设置了全员禁言 |
| kTIMGroupBaseInfoSelfInfo | object  [GroupSelfInfo](https://cloud.tencent.com/document/product/269/33487#GroupSelfInfo)  | 只读 | 用户所在群的个人信息 |

### GroupDetailInfo

群组详细信息。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupDetialInfoGroupId | string | 只读 | 群组ID |
| kTIMGroupDetialInfoGroupType | uint  [TIMGroupType](https://cloud.tencent.com/document/product/269/33487#TIMGroupType)  | 只读 | 群组类型 |
| kTIMGroupDetialInfoGroupName | string | 只读 | 群组名称 |
| kTIMGroupDetialInfoNotification | string | 只读 | 群组公告 |
| kTIMGroupDetialInfoIntroduction | string | 只读 | 群组简介 |
| kTIMGroupDetialInfoFaceUrl | string | 只读 | 群组头像URL |
| kTIMGroupDetialInfoCreateTime | uint | 只读 | 群组创建时间 |
| kTIMGroupDetialInfoInfoSeq | uint | 只读 |  |
| kTIMGroupDetialInfoLastInfoTime | uint | 只读 | 群组信息最后修改时间 |
| kTIMGroupDetialInfoNextMsgSeq | uint | 只读 |  |
| kTIMGroupDetialInfoLastMsgTime | uint | 只读 | 最新群组消息时间 |
| kTIMGroupDetialInfoMemberNum | uint | 只读 | 群组当前成员数量 |
| kTIMGroupDetialInfoMaxMemberNum | uint | 只读 | 群组最大成员数量 |
| kTIMGroupDetialInfoAddOption | uint  [TIMGroupAddOption](https://cloud.tencent.com/document/product/269/33487#TIMGroupAddOption)  | 只读 | 群组加群选项 |
| kTIMGroupDetialInfoOnlineMemberNum | uint | 只读 | 群组在线成员数量 |
| kTIMGroupDetialInfoVisible | uint | 只读 | 群组成员是否对外可见 |
| kTIMGroupDetialInfoSearchable | uint | 只读 | 群组是否能被搜索 |
| kTIMGroupDetialInfoIsShutupAll | bool | 只读 | 群组是否被设置了全员禁言 |
| kTIMGroupDetialInfoOwnerIdentifier | string | 只读 | 群组所有者ID |
| kTIMGroupDetialInfoCustomInfo | object <string | string> | 只读，详见 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5#自定义字段)  |

### GetGroupInfoResult

获取群组信息列表接口的返回。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGetGroupInfoResultCode | uint | 只读 | 获取群组详细信息的结果 |
| kTIMGetGroupInfoResultDesc | string | 只读 | 获取群组详细失败的描述信息 |
| kTIMGetGroupInfoResultInfo | json object  [GroupDetailInfo](https://cloud.tencent.com/document/product/269/33487#GroupDetailInfo)  | 只读 | 群组详细信息 |

### TIMGroupModifyInfoFlag

设置(修改)群组信息的类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupModifyInfoFlag_None | 0x00 |  |
| kTIMGroupModifyInfoFlag_Name | 0x01 | 修改群组名称,       |
| kTIMGroupModifyInfoFlag_Notification | 0x01 << 1 | 修改群公告,         |
| kTIMGroupModifyInfoFlag_Introduction | 0x01 << 2 | 修改群简介          |
| kTIMGroupModifyInfoFlag_FaceUrl | 0x01 << 3 | 修改群头像URL       |
| kTIMGroupModifyInfoFlag_AddOption | 0x01 << 4 | 修改群组添加选项,   |
| kTIMGroupModifyInfoFlag_MaxMmeberNum | 0x01 << 5 | 修改群最大成员数,   |
| kTIMGroupModifyInfoFlag_Visible | 0x01 << 6 | 修改群是否可见,     |
| kTIMGroupModifyInfoFlag_Searchable | 0x01 << 7 | 修改群是否被搜索,   |
| kTIMGroupModifyInfoFlag_ShutupAll | 0x01 << 8 | 修改群是否全体禁言, |
| kTIMGroupModifyInfoFlag_Owner | 0x01 << 31 | 修改群主 |

### GroupModifyInfoParam

设置群信息接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupModifyInfoParamGroupId | string | 只写(必填) | 群组ID |
| kTIMGroupModifyInfoParamModifyFlag | uint  [TIMGroupSetInfoFlag](https://cloud.tencent.com/document/product/269/33487#TIMGroupSetInfoFlag)  | 只写(必填) | 修改标识，可设置多个值按位或 |
| kTIMGroupModifyInfoParamGroupName | string | 只写(选填) | 修改群组名称，当modify_flag包含GroupSet_Name时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamNotification | string | 只写(选填) | 修改群公告，当modify_flag包含GroupSet_Notification时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamIntroduction | string | 只写(选填) | 修改群简介，当modify_flag包含GroupSet_Introduction时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamFaceUrl | string | 只写(选填) | 修改群头像URL，当modify_flag包含GroupSet_FaceUrl时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamAddOption | uint | 只写(选填) | 修改群组添加选项，当modify_flag包含GroupSet_AddOption时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamMaxMemberNum | uint | 只写(选填) | 修改群最大成员数，当modify_flag包含GroupSet_MaxMmeberNum时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamVisible | uint | 只写(选填) | 修改群是否可见，当modify_flag包含GroupSet_Visible时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamSearchAble | uint | 只写(选填) | 修改群是否被搜索，当modify_flag包含GroupSet_Searchable时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamIsShutupAll | bool | 只写(选填) | 修改群是否全体禁言，当modify_flag包含GroupSet_ShutupAll时必填，其他情况不用填 |
| kTIMGroupModifyInfoParamOwner | string | 只写(选填) | 修改群主所有者，当modify_flag包含GroupSet_Owner时必填，其他情况不用填。此时modify_flag不能包含其他值，当修改群主时，同时修改其他信息已无意义 |
| kTIMGroupModifyInfoParamCustomInfo | object <string | string> | 只写(选填)，详见 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5#自定义字段)  |

### GroupGetMemberInfoListParam

获取群成员列表接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetMemberInfoListParamGroupId | string | 只写(必填) | 群组ID |
| kTIMGroupGetMemberInfoListParamIdentifierArray | array string | 只写(选填) | 群成员ID列表 |
| kTIMGroupGetMemberInfoListParamOption | object  [GroupMemberGetInfoOption](https://cloud.tencent.com/document/product/269/33487#GroupMemberGetInfoOption)  | 只写(选填) | 获取群成员信息的选项 |
| kTIMGroupGetMemberInfoListParamNextSeq | uint64 | 只写(选填) | 分页拉取标志，第一次拉取填0，回调成功如果不为零，需要分页，传入再次拉取，直至为0 |

### GroupGetMemberInfoListResult

获取群成员列表接口的返回。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupGetMemberInfoListResultNexSeq | uint64 | 只读 | 下一次拉取的标志，server返回0表示没有更多的数据，否则在下次获取数据的时候填入这个标志 |
| kTIMGroupGetMemberInfoListResultInfoArray | array  [GroupMemberInfo](https://cloud.tencent.com/document/product/269/33487#GroupMemberInfo)  | 只读 | 成员信息列表 |

### TIMGroupMemberModifyInfoFlag

设置(修改)群成员信息的类型。

| 名称 | 值 | 含义 |
|-----|-----|-----|
| kTIMGroupMemberModifyFlag_None | 0x00 |  |
| kTIMGroupMemberModifyFlag_MsgFlag | 0x01 | 修改消息接收选项 |
| kTIMGroupMemberModifyFlag_MemberRole | 0x01 << 1 | 修改成员角色 |
| kTIMGroupMemberModifyFlag_ShutupTime | 0x01 << 2 | 修改禁言时间 |
| kTIMGroupMemberModifyFlag_NameCard | 0x01 << 3 | 修改群名片 |

### GroupModifyMemberInfoParam

设置群成员信息接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupModifyMemberInfoParamGroupId | string | 只写(必填) | 群组ID |
| kTIMGroupModifyMemberInfoParamIdentifier | string | 只写(必填) | 被设置信息的成员ID |
| kTIMGroupModifyMemberInfoParamModifyFlag | uint  [TIMGroupMemberModifyInfoFlag](https://cloud.tencent.com/document/product/269/33487#TIMGroupMemberModifyInfoFlag)  | 只写(必填) | 修改类型，可设置多个值按位或 |
| kTIMGroupModifyMemberInfoParamMsgFlag | uint | 只写(选填) | 修改消息接收选项，当modify_flag包含GroupSetMember_MsgFlag时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamMemberRole | uint  [TIMGroupMemberRole](https://cloud.tencent.com/document/product/269/33487#TIMGroupMemberRole)  | 只写(选填) | 修改成员角色，当modify_flag包含GroupSetMember_MemberRole时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamShutupTime | uint | 只写(选填) | 修改禁言时间，当modify_flag包含GroupSetMember_ShutupTime时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamNameCard | string | 只写(选填) | 修改群名片，当modify_flag包含GroupSetMember_NameCard时必填，其他情况不用填 |
| kTIMGroupModifyMemberInfoParamCustomInfo | object <string | string> | 只写(选填)，详见 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5#自定义字段)  |

### GroupPendencyOption

获取群未决信息列表的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyOptionStartTime | uint64 | 只写(必填) | 设置拉取时间戳，第一次请求填0，后边根据server返回的 [GroupPendencyResult](https://cloud.tencent.com/document/product/269/33487#GroupPendencyResult) 键kTIMGroupPendencyResultNextStartTime指定的时间戳进行填写 |
| kTIMGroupPendencyOptionMaxLimited | uint | 只写(选填) | 拉取的建议数量，server可根据需要返回或多或少，不能作为完成与否的标志 |

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

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyGroupId | string | 读写() | 群组id |
| kTIMGroupPendencyFromIdentifier | string | 读写() | 请求者的id，比如：请求加群:请求者，邀请加群:邀请人。 |
| kTIMGroupPendencyToIdentifier | string | 读写() | 判决者的id，请求加群:""，邀请加群:被邀请人。 |
| kTIMGroupPendencyAddTime | uint64 | 只读() | 未决信息添加时间 |
| kTIMGroupPendencyPendencyType | uint  [TIMGroupPendencyType](https://cloud.tencent.com/document/product/269/33487#TIMGroupPendencyType)  | 只读() | 未决请求类型 |
| kTIMGroupPendencyHandled | uint  [TIMGroupPendencyHandle](https://cloud.tencent.com/document/product/269/33487#TIMGroupPendencyHandle)  | 只读() | 群未决处理状态 |
| kTIMGroupPendencyHandleResult | uint  [TIMGroupPendencyHandleResult](https://cloud.tencent.com/document/product/269/33487#TIMGroupPendencyHandleResult)  | 只读() | 群未决处理操作类型 |
| kTIMGroupPendencyApplyInviteMsg | string | 只读() | 申请或邀请附加信息 |
| kTIMGroupPendencyFromUserDefinedData | string | 只读() | 申请或邀请者自定义字段 |
| kTIMGroupPendencyApprovalMsg | string | 只读() | 审批信息：同意或拒绝信息 |
| kTIMGroupPendencyToUserDefinedData | string | 只读() | 审批者自定义字段 |

### GroupPendencyResult

获取群未决信息列表的返回。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupPendencyResultNextStartTime | uint64 | 只读 | 下一次拉取的起始时戳，server返回0表示没有更多的数据，否则在下次获取数据的时候以这个时间戳作为开始时间戳 |
| kTIMGroupPendencyResultReadTimeSeq | uint64 | 只读 | 已读上报的时间戳 |
| kTIMGroupPendencyResultUnReadNum | uint | 只读 | 未决请求的未读数 ? |
| kTIMGroupPendencyResultPendencyArray | array  [GroupPendency](https://cloud.tencent.com/document/product/269/33487#GroupPendency)  | 只读 | 群未决信息列表 |

### GroupHandlePendencyParam

处理群未决消息接口的参数。

| Json 键 | 值类型 | 属性 | 含义 |
|-----|-----|-----|-----|
| kTIMGroupHandlePendencyParamIsAccept | bool | 只写(选填) | true accept false refuse。默认为false |
| kTIMGroupHandlePendencyParamHandleMsg | string | 只写(选填) | 同意或拒绝信息，默认为空字符串 |
| kTIMGroupHandlePendencyParamPendency | object  [GroupPendency](https://cloud.tencent.com/document/product/269/33487#GroupPendency)  | 只写(必填) | 未决信息详情 |



