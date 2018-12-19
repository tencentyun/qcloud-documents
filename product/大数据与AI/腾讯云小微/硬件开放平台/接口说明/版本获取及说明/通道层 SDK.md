
## 接口介绍

为了提高接入层的自由度和施展空间，我们提供了这么一套接口：

> *   提供尽可能精简的 API，只提供问答结果，包括结果文本、可播放资源、操作指令以及上下文信息。
> *   信息的处理和交互过程需要接入层自行实现。

我们称之为 ** 通道层 SDK**。

[![img_channel](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Channel_interface.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Channel_interface.png)

## SDK 下载
目前小微处于内测阶段，SDK 下载请在审核通过后，联系小微工作人员获取。

## API 说明

这套 SDK 的基础对接部分 (除语音以外的功能)，是和 ** 全功能 SDK** 完全一致的，不多做介绍。

下边针对通道层特有的 API 进行说明：

通道层接口由 7 个功能接口，1 个回调接口，和 6 个数据类型组成，本说明只做简单展示，更多信息，请参考 Demo 或查看 SDK 包中的 API 文档。

### Android API

#### 功能接口

| Class | Methods | 说明 |
| :-- | :-- | :-- |
| TXAudioManager | init | 初始化语音服务 |
| TXAudioManager | unInit | 反初始化语音服务 |
| TXAudioManager | request | 语音请求 |
| TXAudioManager | requestCancel | 取消语音请求 |
| TXAudioManager | reportState | 上报播放状态 |
| TXAudioManager | getPlaylist | 拉取更多列表请求, 在 Response.hasMorePlaylist，且有必要拉取时调用 |
| TXAudioManager | getPlayDetailInfo | 拉取播放资源详情, 用于拉取歌词、是否收藏等信息时调用 |

#### 回调接口

| Class | Methods | 说明 |
| :-- | :-- | :-- |
| TXAudioManager.RequestListener | onRequest | 请求结果回调接口 |

#### 数据结构

| Class | Field | 数据类型 | 说明 |
| :-- | :-- | :-- | :-- |
| AppInfo | ID | 场景信息 | App ID，当前 App(Skill) 的唯一 ID |
| AppInfo | name | 场景信息 | App 名称，用于表示场景名称 |
| AppInfo | type | 场景信息 | App 类型，App(Skill) 类型，用于进行场景分类 |
| ContextInfo | ID | 上下文 | 上下文 ID，非空时需要自动开启下一轮请求 |
| ContextInfo | silentTimeout | 上下文信息 | 用户开始说话后的断句时间 (单位: ms) |
| ContextInfo | speakTimeout | 上下文信息 | 等待用户说话的超时时间 (单位: s) |
| ContextInfo | voiceRequestBegin | 上下文信息 | 声音请求的首包标志，首包时必须为 true |
| ContextInfo | voiceRequestEnd | 上下文信息 | 当使用外部 VAD 时，声音尾包置成 true |
| DeviceInfo | properties | 设备信息 | 设备支持能力 (位域) |
| DeviceInfo | extendBuffer | 设备信息 | 扩展参数 |
| State | appInfo | 状态信息 | 场景信息 |
| State | state | 状态信息 | 播放状态 |
| State | playID | 状态信息 | playID，如果不是在播放 url 资源，则无需上报 |
| State | playContent | 状态信息 | 播放内容 |
| State | playOffset | 状态信息 | 播放偏移量，预留，目前无场景支持 |
| State | playMode | 状态信息 | 播放模式 |
| Response | appInfo | 响应信息 | 场景信息 |
| Response | resultCode | 响应信息 | 请求结果 |
| Response | voiceID | 响应信息 | VoiceID |
| Response | context | 响应信息 | 上下文信息 |
| Response | requestText | 响应信息 | 请求文本 |
| Response | resources | 响应信息 | 资源 list |
| Response | hasMorePlaylist | 响应信息 | 是否有更多资源 |
| Response | isRecovery | 响应信息 | 资源是否可以暂停恢复 |
| Response | playBehavior | 响应信息 | 资源列表拼接类型 |
| Response | responseType | 响应信息 | 响应扩展数据类型 |
| Response | responseData | 响应信息 | 响应扩展数据，json 格式 |
| Resource | format | 响应资源 | 资源类型 |
| Resource | ID | 响应资源 | 资源 ID |
| Resource | content | 响应资源 | 资源内容 |
| Resource | extendInfo | 响应资源 | 扩展信息，json 格式 |

### linux API

#### 功能接口

| Methods | 说明 |
| :-- | :-- |
| txca_service_start | 初始化语音服务 |
| txca_service_stop | 反初始化语音服务 |
| txca_request | 语音请求 |
| txca_request_cancel | 取消语音请求 |
| txca_report_state | 上报播放状态 |
| txca_get_play_list | 拉取更多列表请求, 在 TXCA_PARAM_RESPONSE.has_more_playlist，且有必要拉取时调用 |
| txca_get_play_detail_info | 拉取播放资源详情, 用于拉取歌词、是否收藏等信息时调用 |

#### 回调接口

| Methods | 说明 |
| :-- | :-- |
| TXCA_CALLBACK.on_request_callback | 请求结果回调接口 |

#### 数据结构

| Struct | param | 数据类型 | 说明 |
| :-- | :-- | :-- | :-- |
| TXCA_PARAM_APP | app_id | 场景信息 | App ID，当前 App(Skill) 的唯一 ID |
| TXCA_PARAM_APP | app_name | 场景信息 | App 名称，用于表示场景名称 |
| TXCA_PARAM_APP | app_type | 场景信息 | App 类型，App(Skill) 类型，用于进行场景分类 |
| TXCA_PARAM_CONTEXT | id | 上下文 | 上下文 ID，非空时需要自动开启下一轮请求 |
| TXCA_PARAM_CONTEXT | silent_timeout | 上下文信息 | 用户开始说话后的断句时间 (单位: ms) |
| TXCA_PARAM_CONTEXT | speak_timeout | 上下文信息 | 等待用户说话的超时时间 (单位: s) |
| TXCA_PARAM_CONTEXT | voice_request_begin | 上下文信息 | 声音请求的首包标志，首包时必须为 true |
| TXCA_PARAM_CONTEXT | voice_request_end | 上下文信息 | 当使用外部 VAD 时，声音尾包置成 true |
| TXCA_PARAM_DEVICE | properties | 设备信息 | 设备支持能力 (位域) |
| TXCA_PARAM_DEVICE | extend_buffer | 设备信息 | 扩展参数 |
| TXCA_PARAM_DEVICE | extend_buffer_len | 设备信息 | 扩展参数长度 |
| TXCA_PARAM_STATE | app_info | 状态信息 | 场景信息 |
| TXCA_PARAM_STATE | play_state | 状态信息 | 播放状态 |
| TXCA_PARAM_STATE | play_id | 状态信息 | playID，如果不是在播放 url 资源，则无需上报 |
| TXCA_PARAM_STATE | play_content | 状态信息 | 播放内容 |
| TXCA_PARAM_STATE | play_offset | 状态信息 | 播放偏移量，预留，目前无场景支持 |
| TXCA_PARAM_STATE | play_mode | 状态信息 | 播放模式 |
| TXCA_PARAM_RESPONSE | app_info | 响应信息 | 场景信息 |
| TXCA_PARAM_RESPONSE | error_code | 响应信息 | 请求结果 |
| TXCA_PARAM_RESPONSE | voice_id | 响应信息 | VoiceID |
| TXCA_PARAM_RESPONSE | context | 响应信息 | 上下文信息 |
| TXCA_PARAM_RESPONSE | request_text | 响应信息 | 请求文本 |
| TXCA_PARAM_RESPONSE | resources | 响应信息 | 资源 list |
| TXCA_PARAM_RESPONSE | resources_size | 响应信息 | 资源 list 长度 |
| TXCA_PARAM_RESPONSE | has_more_playlist | 响应信息 | 是否有更多资源 |
| TXCA_PARAM_RESPONSE | is_recovery | 响应信息 | 资源是否可以暂停恢复 |
| TXCA_PARAM_RESPONSE | play_behavior | 响应信息 | 资源列表拼接类型 |
| TXCA_PARAM_RESPONSE | response_type | 响应信息 | 响应扩展数据类型 |
| TXCA_PARAM_RESPONSE | response_data | 响应信息 | 响应扩展数据，json 格式 |
| TXCA_PARAM_RESOURCE | format | 响应资源 | 资源类型 |
| TXCA_PARAM_RESOURCE | id | 响应资源 | 资源 ID |
| TXCA_PARAM_RESOURCE | content | 响应资源 | 资源内容 |
| TXCA_PARAM_RESOURCE | extend_buffer | 响应资源 | 扩展信息，json 格式 |

## 使用说明

上文简单列举了API具备的接口和数据类型，使用时可以参考[通道层SDK接入指引](/wiki/#APIDesc_tunnel_sdk_access)来完成。
