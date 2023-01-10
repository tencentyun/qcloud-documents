

本接口是将 `IoT Video P2P`的接口暴露给用户，用户可以直接使用 `IoT Video P2P`接口进行开发。

## 功能介绍

本文档介绍 `IoT Video P2P` 底层接口的使用方法， `IoT Video P2P`接口定义在 `iv_av.h` 文件中，其使用与文档《音视频传输及对讲模块说明》中的接口使用是互斥，用户只能使用一种接口进行音视频传输。使用 `IoT Video P2P`接口时，`IoT Video SDK` 只提供基本的数据传输能力。

## 接口参考

**该功能模块提供以下接口**  

- iv_avt_p2p_init P2P初始化
- iv_avt_p2p_exit P2P去初始化
- iv_avt_p2p_set_buf_watermark 设置 P2P 的拥塞控制阈值
- iv_avt_p2p_get_send_buf 获取 P2P 的缓存数据大小
- iv_avt_p2p_get_send_status 获取发送流的实时状态
- iv_avt_p2p_send_command 主动发送到对端

**用户需注册以下回调函数**  

- p2p_handle_send_init_cb 直播或者回放时启动的回调
- p2p_handle_send_get_cb 获取数据回调
- p2p_handle_send_stop_cb 直播或者回放时停止的回调
- p2p_handle_event_notify_cb 事件通知的回调
- p2p_handle_recv_init_cb 开始接收音频通知回调
- p2p_handle_recv_voice_cb 接收音频数据的回调
- p2p_handle_command_cb 命令交互的回调


## 接口描述

### iv_avt_p2p_init

**功能描述**  
P2P初始化，注册P2P的各种回调函数。

**函数原型**  

```
int iv_avt_p2p_init(const iv_p2p_parm_s *pstInitParm);
```

**参数说明**  

| 参数名称    | 类型          | 描述       | 输入/输出 |
| ----------- | ------------- | ---------- | --------- |
| pstInitParm | iv_p2p_parm_s | 初始化参数 | 输入      |

**返回值**  

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_xx   | 失败，对应相应错误码 |


### iv_avt_p2p_exit

**功能描述**  
P2P初始化。本模块退出时调用，用于释放资源。

**函数原型**  

```
int iv_avt_p2p_exit(void);
```

**参数说明**  

| 参数名称 | 类型 | 描述 | 输入/输出 |
| -------- | ---- | ---- | --------- |
| 无       | 无   | 无   | 无        |

**返回值**  

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_xx   | 失败，对应相应错误码 |


### iv_avt_p2p_set_buf_watermark

**功能描述**  
设置 P2P 缓存区的拥塞控制阈值。

**函数原型**  

```
int iv_avt_p2p_set_buf_watermark(size_t low_mark, size_t warn_mark, size_t high_mark);
```

**参数说明**  

| 参数名称  | 类型   | 描述             | 输入/输出 |
| --------- | ------ | ---------------- | --------- |
| low_mark  | size_t | 缓存数据低阈值   | 输入      |
| warn_mark | size_t | 缓存数据报警阈值 | 输入      |
| high_mark | size_t | 缓存数据高阈值   | 输入      |

**返回值**  

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_xx   | 失败，对应相应错误码 |

>?
>设置 P2P 发送缓冲区的水位告警值(单位：字节)，用于链路拥塞感知和码率变化控制
>- 当发送缓冲区存在未发送的数据超过warn_mark时，会触发一次`IV_AVT_EVENT_P2P_WATERMARK_WARN`事件
>- 当数据超过 high_mark 时，会触发一次`IV_AVT_EVENT_P2P_WATERMARK_HIGH`事件，并暂停通过回调取数据
>- 直到数据低于 low_mark 时，会触发一次`IV_AVT_EVENT_P2P_WATERMARK_LOW`，并重新取数据
  可根据视频流码率和可用内存做动态调整，目前该设置是全局的，即对所有的视频流推送都使用同样的设置，如果三个值都设置为0，则不进行告警，用户可以通过`iv_avt_p2p_get_send_buf`自行做拥塞控制


### iv_avt_p2p_get_send_buf

**功能描述**  
获取相关`P2P`数据流传输通道的缓冲区大小。

**函数原型**  

```
size_t iv_avt_p2p_get_send_buf(void *handle);
```

**参数说明**  

| 参数名称 | 类型   | 描述             | 输入/输出 |
| -------- | ------ | ---------------- | --------- |
| handle   | void * | 数据传输通道句柄 | 输入      |

**返回值**  

| 返回值 | 描述       |
| ------ | ---------- |
| size_t | 缓冲区大小 |

>?获取相关 P2P 视频流传输通道的发送缓冲区大小，用于用户自定义的 P2P 链路拥塞控制，传入由`p2p_handle_send_init_cb`回调创建的视频通道句柄指针handle


### iv_avt_p2p_get_send_status

**功能描述**  
获取相关`P2P`视频流传输通道的发包统计数据如发送速率。

**函数原型**  

```
iv_p2p_send_stats_s iv_avt_p2p_get_send_status(void *handle);
```

**参数说明**  

| 参数名称 | 类型   | 描述             | 输入/输出 |
| -------- | ------ | ---------------- | --------- |
| handle   | void * | 数据传输通道句柄 | 输入      |

**返回值**  

| 返回值              | 描述         |
| ------------------- | ------------ |
| iv_p2p_send_stats_s | 发包统计数据 |

>? 获取相关 P2P 视频流传输通道的发包统计数据如发送速率等，用于用户自定义的`P2P`链路拥塞控制, 传入由`p2p_handle_send_init_cb`回调创建的视频通道句柄指针`handle`


### iv_avt_p2p_send_command

**功能描述**  
在看直播期间，设备端可以通过该接口主动发送反馈消息给对端，并可以接收对端回复

**函数原型**  

```
int iv_avt_p2p_send_command(const char *peer, const char *msg, size_t msg_len,
                            unsigned char *recv_buf, size_t *recv_len, uint32_t timeout_ms);
```

**参数说明**  

| 参数名称   | 类型           | 描述            | 输入/输出 |
| ---------- | -------------- | --------------- | --------- |
| peer       | const char *   | 对端的peername  | 输入      |
| msg        | char*          | 发送的消息内容  | 输入      |
| msg_len    | size_t         | 发送的消息长度  | 输入      |
| recv_buf   | unsigned char* | 接收消息的缓存  | 输出      |
| recv_len   | size_t*        | 接收消息的长度  | 输入输出  |
| timeout_ms | uint32_t       | 超时时间,单位ms | 输入      |

**返回值**  

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应错误码 |

>?
>* 该调用为同步阻塞方式，如果设置了较短的超时时间，则在网络繁忙或不稳定时候，该消息可能会因为超时而被丢弃
>* msg传入的内存类型不做要求, 可以是只读的，也可以是可读写的;msg可以为任意格式字符或二进制数据，长度由msg_len提供，建议在16KB以内，否则会影响实时性
>* recv_buf必须是事先分配的足够大的内存用于存放对端回复的数据, recv_len首先传入recv_buf的最大大小，接收到数据后会写入实际接收的数据大小;
>* recv_buf必须是事先分配的足够大的内存用于存放回复的数据，实际数据长度根据recv_len获取
>* timeout_us: 命令超时时间，单位为毫秒，值为0时采用默认超时(7500ms左右)


### p2p_handle_send_init_cb

**功能描述**  
设备端发送数据开始通知回调，入口参数为app端获取媒体流请求时传递的参数，可以通过“action=live”或“action=playback”来区分实时流和回放。

**函数原型**  

```
void *(*p2p_handle_send_init_cb)(const char *params, const char *peer);
```

**参数说明**  

| 参数名称 | 类型         | 描述                       | 输入/输出 |
| -------- | ------------ | -------------------------- | --------- |
| params   | const char * | 直播或者回放时携带的参数   | 输入      |
| peer     | const char * | 请求端的标识，表面对端身份 | 输入      |

**返回值**  

| 返回值 | 描述       |
| ------ | ---------- |
| handle | 通道的句柄 |


### p2p_handle_send_get_cb

**功能描述**  
获取设备端媒体流数据的回调，会传入 `p2p_handle_send_init_cb` 返回的句柄,该回调每10ms触发一次。

**函数原型**  

```
iv_cm_memory_s (*p2p_handle_send_get_cb)(void *handle);
```

**参数说明**  

| 参数名称 | 类型   | 描述       | 输入/输出 |
| -------- | ------ | ---------- | --------- |
| handle   | void * | 通道的句柄 | 输入      |

**返回值**  

| 返回值         | 描述                                        |
| -------------- | ------------------------------------------- |
| iv_cm_memory_s | 返回的数据结构体,包括地址,大小,地址释放回调 |


### p2p_handle_send_stop_cb

**功能描述**  
设备端发送数据停止通知回调。

**函数原型**  

```
int (*p2p_handle_send_stop_cb)(void *handle);
```

**参数说明**  

| 参数名称 | 类型   | 描述       | 输入/输出 |
| -------- | ------ | ---------- | --------- |
| handle   | void * | 通道的句柄 | 输入      |

**返回值**  

| 返回值 | 描述           |
| ------ | -------------- |
| int    | 返回数值不影响 |


### p2p_handle_event_notify_cb

**功能描述**  
P2P 事件通知的回调。

**函数原型**  

```
void (*p2p_handle_event_notify_cb)(iv_avt_event_e, void *handle);
```

**参数说明**  

| 参数名称 | 类型           | 描述       | 输入/输出 |
| -------- | -------------- | ---------- | --------- |
| 事件     | iv_avt_event_e | 事件的类型 | 输入      |
| handle   | void *         | 通道的句柄 | 输入      |

**返回值**  

| 返回值 | 描述 |
| ------ | ---- |
| 无     | 无   |

**使用说明**  
当事件类型是 `*WATERMARK*` 类型时, `handle` 是 `p2p_handle_send_init_cb`时返回的句柄;否则，`handle` 为 `NULL`;


### p2p_handle_recv_init_cb

**功能描述**  
P2P 开始接收app音频数据通知回调

**函数原型**  

```
void *(*p2p_handle_recv_init_cb)(const char *params, const char *peer);
```

**参数说明**  

| 参数名称 | 类型        | 描述                 | 输入/输出 |
| -------- | ----------- | -------------------- | --------- |
| params   | const char* | 接收音频时携带的参数 | 输入      |
| peer     | const char* | 对端音频标识         | 输入      |

**返回值**  

| 返回值 | 描述       |
| ------ | ---------- |
| void*  | 自定义句柄 |


### p2p_handle_recv_voice_cb

**功能描述**  
P2P 接收app音频的数据回调，当app的发送结束时，会传入recv_buf=NULL且recv_len=0。

**函数原型**  

```
void (*p2p_handle_recv_voice_cb)(void *handle, uint8_t *recv_buf, size_t recv_len);
```

**参数说明**  

| 参数名称 | 类型     | 描述                               | 输入/输出 |
| -------- | -------- | ---------------------------------- | --------- |
| handle   | void*    | p2p_handle_recv_init_cb 返回的句柄 | 输入      |
| recv_buf | uint8_t* | 接收的音频数据首地址               | 输入      |
| recv_len | size_t   | 接收的音频数据大小                 | 输入      |

**返回值**  

| 返回值 | 描述 |
| ------ | ---- |
| 无     | 无   |


### p2p_handle_command_cb

**功能描述**  
P2P 事件通知的回调，是一个同步接口，不能有耗时太久的操作。

**函数原型**  

```
iv_cm_memory_s (*p2p_handle_command_cb)(const char *command, size_t cmd_len, const char *peer);
```

**参数说明**  

| 参数名称 | 类型         | 描述             | 输入/输出 |
| -------- | ------------ | ---------------- | --------- |
| command  | const char * | 收到的命令       | 输入      |
| cmd_len  | size_t       | 命令的长度       | 输入      |
| peer     | const char * | 发送命令端的标识 | 输入      |

**返回值**  

| 返回值         | 描述       |
| -------------- | ---------- |
| iv_cm_memory_s | 返回的数据 |

**注意事项**  
`iv_cm_memory_s` 中的 `buf` 地址必须是可读写的, SDK 内部会对其进行修改;否则，SDK 运行会出现错误;如果返回 `buf` 为 `NULL`或者 `cmd_len` 为0时,表示通道断开, `APP`侧会收到通道断开通知;


## 数据结构

**本模块提供以下数据结构**  

- iv_p2p_parm_s 音视频对讲初始化参数结构体

其余数据结构请参考《音视频传输及对讲模块说明》

### iv_p2p_parm_s

**功能描述**  
P2P 初始化参数结构体。

**结构原型**  

```
typedef struct iv_avt_init_parm_s {
    void *(*p2p_handle_send_init_cb)(const char *params, const char *peer);
    iv_cm_memory_s (*p2p_handle_send_get_cb)(void *handle);
    int (*p2p_handle_send_stop_cb)(void *handle);
    void (*p2p_handle_event_notify_cb)(iv_avt_event_e, void *handle);
    void *(*p2p_handle_recv_init_cb)(const char *params, const char *peer);
    void (*p2p_handle_recv_voice_cb)(void *handle, uint8_t *recv_buf, size_t recv_len);
    iv_cm_memory_s (*p2p_handle_command_cb)(const char *command, size_t cmd_len, const char *peer);
    avt_xp2p_ops_s p2p_keep_alive;
    p2p_init_params_s p2p_init_params;
    local_net_info_s net_info;
} iv_avt_init_parm_s;
```

**参数说明**  

| 成员名称                   | 描述                 | 取值 |
| -------------------------- | -------------------- | ---- |
| p2p_handle_send_init_cb    | 发送请求的开始回调   | -    |
| p2p_handle_send_get_cb     | 发送数据的回调       | -    |
| p2p_handle_send_stop_cb    | 发送请求的结束回调   | -    |
| p2p_handle_event_notify_cb | 事件通知回调         | -    |
| p2p_handle_recv_init_cb    | 接收音频数据开始回调 | -    |
| p2p_handle_recv_voice_cb   | 发送音频数据的回调   | -    |
| p2p_handle_command_cb      | 信令收发的回调       | -    |
| p2p_keep_alive             | P2P 保活配置         | -    |
| p2p_init_params            | P2P 初始化参数       | -    |
| net_info                   | 局域网配置（可选）   | -    |


## 内存消耗统计

设备在使用 P2P 发送数据时,其内存消耗与网络带宽bandwidth，传输的数据速率rate相关;

* 当 bandwidth > rate 时; 正常连接时内存消耗 memory <= m * 150KB;
* 当 bandwidth <= rate时; 弱网情况下，SDK 内部缓存达到最大, 其最大内存消耗memory = (n * 512 KB+ 732 KB) * m;
  其中, m 是设备连接的APP数量，n 是一个APP请求的接收数据通道数量, 即设备端的数据发送通道数量;


## 示例代码

### 1. P2P 初始化
```
    iv_p2p_parm_s p2p_param = {0};

    p2p_param.p2p_handle_send_init_cb        = test_flv_send_init;
    p2p_param.p2p_handle_send_get_cb         = test_flv_send_data;
    p2p_param.p2p_handle_send_stop_cb        = test_flv_send_stop;
    p2p_param.p2p_handle_event_notify_cb     = test_p2p_notify;
    p2p_param.p2p_handle_recv_init_cb        = test_recv_data_init;
    p2p_param.p2p_handle_recv_voice_cb       = test_recv_data;
    p2p_param.p2p_handle_command_cb          = test_command_handle;
    p2p_param.p2p_keep_alive.time_inter_s    = 10;
    p2p_param.p2p_keep_alive.max_attempt_num = 3;
    p2p_param.p2p_init_params.log_level      = IV_AVT_P2P_LOG_DEBUG;
    p2p_param.p2p_init_params.log_file_path  = "/tmp";
    p2p_param.p2p_init_params.log_file_size  = 1 * 1024 * 1024;

    memset(sg_p2p_chn_hanlde, 0, MAX_CHANNEL_NUM * sizeof(p2p_chn_handle));

    int ret = iv_avt_p2p_init(&p2p_param);
    if (ret) {
        printf(" p2p init failed\n");
        return -1;
    }

#ifdef USER_CONGESTION_CTRL
    // do network congestion control by yourself
    iv_avt_p2p_set_buf_watermark(0, 0, 0);
#else
    iv_avt_p2p_set_buf_watermark(200 * 1024, 400 * 1024, 500 * 1024);
#endif
```

### 2. 配置拥塞控制参数
```
iv_avt_p2p_set_buf_watermark(200 * 1024, 400 * 1024, 500 * 1024);
```

### 3. p2p 退出

```
void p2p_sample_exit(void)
{
    iv_avt_p2p_exit();
}
```
