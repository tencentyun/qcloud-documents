
本接口是将 IoT Video P2P 的接口直接提供给用户，用户可以直接使用 IoT Video P2P 接口进行开发。

## 功能介绍

本文为您介绍 IoT Video P2P 底层接口的使用方法，IoT Video P2P 接口定义在 iv_av.h 文件中，其使用与 [音视频传输及对讲模块](https://cloud.tencent.com/document/product/1131/52955) 中的接口使用相互斥，用户只能使用一种接口进行音视频传输。使用 IoT Video P2P 接口时，IoT Video SDK 只提供基本的数据传输能力。

## 接口参考

该功能模块提供以下接口：

- iv_avt_p2p_init：P2P 初始化
- iv_avt_p2p_exit：P2P 去初始化
- iv_avt_p2p_set_buf_watermark：设置 P2P 的拥塞控制阈值
- iv_avt_p2p_get_send_buf：获取 P2P 的缓存数据大小
- iv_avt_p2p_get_send_status：获取 P2P 视频流传输通道的发包统计数据
- p2p_handle_send_init_cb：直播或者回放时启动的回调
- p2p_handle_send_get_cb：获取数据回调
- p2p_handle_send_stop_cb：直播或者回放时停止的回调
- p2p_handle_event_notify_cb：事件通知的回调
- p2p_handle_recv_init_cb：开始接收音频通知回调
- p2p_handle_recv_voice_cb：接收音频数据的回调
- p2p_handle_command_cb：命令交互的回调

#### iv_avt_p2p_init

**接口描述**

P2P 初始化，注册 P2P 的各种回调函数。

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
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315)  |

#### iv_avt_p2p_exit

**接口描述**
P2P 初始化，本模块退出时调用，用于释放资源。

```
int iv_avt_p2p_exit(void);
```

**参数说明**

| 参数名称 | 类型 | 描述 | 输入/输出 |
| -------- | ---- | ---- | --------- |
| -       | -   | -   | -        |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315)  |

#### iv_avt_p2p_set_buf_watermark

**接口描述**

设置 P2P 缓存区的拥塞控制阈值。

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
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315)  |

>? 
>- 设置 P2P 发送缓冲区的水位告警值（单位：字节），用于链路拥塞感知和码率变化控制。
  - 当发送缓冲区存在未发送的数据超过 warn_mark 时，将触发一次 `IV_AVT_EVENT_P2P_WATERMARK_WARN` 事件。
  - 当数据超过 high_mark 时，将触发一次 `IV_AVT_EVENT_P2P_WATERMARK_HIGH` 事件，并暂停通过回调取数据。
  - 当数据低于 low_mark 时，将触发一次 `IV_AVT_EVENT_P2P_WATERMARK_LOW`，并重新取数据。
- 可根据视频流码率和可用内存对参数进行动态调整。
- 目前该部分参数为全局变量，即对所有的视频流推送都使用同样的设置。
- 如果三个值都设置为0，则不进行告警，您可以通过 `iv_avt_p2p_get_send_buf` 自行做拥塞控制。


#### iv_avt_p2p_get_send_buf

**接口描述**
获取相关 P2P 数据流传输通道的缓冲区大小用于用户自定义的 P2P 链路拥塞控制。

```
size_t iv_avt_p2p_get_send_buf(void *handle);
```

**参数说明**

| 参数名称 | 类型   | 描述             | 输入/输出 |
| -------- | ------ | ---------------- | --------- |
| handle   | void * | p2p_handle_send_init_cb 回调创建的数据传输通道句柄 | 输入      |

**返回值**

| 返回值    | 描述                 |
| --------- | -------------------- | 
| 大于等于0 | 获取缓存区数据的大小 |

#### iv_avt_p2p_get_send_status

**接口描述**
获取相关 P2P 视频流传输通道的发包统计数据，例如发送速率。用于用户自定义的 P2P 链路拥塞控制，传入由 p2p_handle_send_init_cb 回调创建的视频通道句柄指针 handle。

```
iv_p2p_send_stats_s iv_avt_p2p_get_send_status(void *handle);
```

**返回值**

| 返回值              | 描述         |
| ------------------- | ------------ |
| iv_p2p_send_stats_s | 发包统计数据 |

**参数说明**

| 参数名称 | 类型   | 描述             | 输入/输出 |
| -------- | ------ | ---------------- | --------- |
| handle   | void * | 数据传输通道句柄 | 输入      |








#### p2p_handle_send_init_cb

**接口描述**
 设备端发送数据开始通知回调，传入参数为 App 端获取媒体流请求时传递的参数，可以通过 `action=live` 或 `action=playback` 来区分实时流和回放。

```
void *(*p2p_handle_send_init_cb)(const char *params, const char *peer);
```

**参数说明**

| 参数名称 | 类型         | 描述                       | 输入/输出 |
| -------- | ------------ | -------------------------- | --------- |
| params   | const char * | 直播或者回放时携带的参数   | 输入      |
| peer     | const char * | 请求端的标识，表明对端身份 | 输入      |


**返回值**

| 返回值 | 描述       |
| ------ | ---------- |
| handle | 数据传输通道的句柄 |


#### p2p_handle_send_get_cb

**接口描述**
获取设备端媒体流数据的回调，会传入 `p2p_handle_send_init_cb` 返回的句柄，该回调每10ms触发一次。

```
iv_cm_memory_s (*p2p_handle_send_get_cb)(void *handle);
```


**参数说明**

| 参数名称 | 类型   | 描述       | 输入/输出 |
| -------- | ------ | ---------- | --------- |
| handle   | void * | 数据通道的句柄 | 输入      |

**返回值**

| 返回值         | 描述                                        |
| -------------- | ------------------------------------------- |
| iv_cm_memory_s | 返回的数据结构体，包括地址、大小和地址释放回调 |

#### p2p_handle_send_stop_cb

**接口描述**
设备端发送数据停止通知回调。

```
int (*p2p_handle_send_stop_cb)(void *handle);
```


**参数说明**

| 参数名称 | 类型   | 描述       | 输入/输出 |
| -------- | ------ | ---------- | --------- |
| handle   | void * | 通道的句柄 | 输入      |


**返回值**

| 返回值   | 描述           |
| -------- | -------------- |
| 整形数值 | 返回数值不影响接口使用 |

#### p2p_handle_event_notify_cb

**接口描述**
P2P 事件通知的回调。

```
void (*p2p_handle_event_notify_cb)(iv_avt_event_e, void *handle);
```


**参数说明**

| 参数名称 | 类型           | 描述       | 输入/输出 |
| -------- | -------------- | ---------- | --------- |
| 事件     | iv_avt_event_e | 事件的类型 | 输入      |
| handle   | void *         | 通道的句柄 | 输入      |




>?当事件类型为 `*WATERMARK*` 类型时，`handle` 是 `p2p_handle_send_init_cb`时返回的句柄；否则 `handle` 为 `NULL`。

#### p2p_handle_recv_init_cb

**接口描述**
P2P 开始接收 App 音频数据通知回调。

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

#### p2p_handle_recv_voice_cb

**接口描述**
P2P 接收 App 音频的数据回调，当 App 发送结束时，会传入 `recv_buf=NULL` 且 `recv_len=0`。

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
| -     |-   |

#### p2p_handle_command_cb

**接口描述**
P2P 事件通知的回调同步接口，不能有耗时过久的操作。

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

>!iv_cm_memory_s 中的 buf 地址必须为可读写，SDK 内部将会对其进行修改，否则，SDK 运行会出现错误。如果返回 buf 为 NULL 或者 cmd_len 为0时，表示通道断开，App 则会收到通道断开通知。

## 数据结构

本模块提供以下数据结构：

- iv_p2p_parm_s：音视频对讲初始化参数结构体
- p2p_keep_alive_cfg：P2P 保活参数
- iv_avt_event_e：事件类型枚举
- iv_p2p_send_stats_s：P2P 发送状态参数

#### iv_p2p_parm_s

**接口描述**
P2P 初始化参数结构体。

```
typedef struct iv_avt_init_parm_s {
    void *(*p2p_handle_send_init_cb)(const char *params, const char *peer);
    iv_cm_memory_s (*p2p_handle_send_get_cb)(void *handle);
    int (*p2p_handle_send_stop_cb)(void *handle);
    void (*p2p_handle_event_notify_cb)(iv_avt_event_e, void *handle);
    void *(*p2p_handle_recv_init_cb)(const char *params, const char *peer);
    void (*p2p_handle_recv_voice_cb)(void *handle, uint8_t *recv_buf, size_t recv_len);
    iv_cm_memory_s (*p2p_handle_command_cb)(const char *command, size_t cmd_len, const char *peer);
    p2p_keep_alive_cfg p2p_keep_alive;
} iv_avt_init_parm_s;

```

**参数说明**

| 成员名称                   | 描述                 | 
| -------------------------- | -------------------- | 
| p2p_handle_send_init_cb    | 发送请求的开始回调   | 
| p2p_handle_send_get_cb     | 发送数据的回调       | 
| p2p_handle_send_stop_cb    | 发送请求的结束回调   |
| p2p_handle_event_notify_cb | 事件通知回调         | 
| p2p_handle_recv_init_cb    | 接收音频数据开始回调 | 
| p2p_handle_recv_voice_cb   | 发送音频数据的回调   | 
| p2p_handle_command_cb      | 信令收发的回调       | 
| p2p_keep_alive             | P2P 保活配置         | 

#### p2p_keep_alive_cfg

**类型描述**
P2P 保活参数。

```
typedef struct p2p_keep_alive_s {
    uint8_t time_inter_s;
    uint8_t max_attempt_num;
} p2p_keep_alive_cfg;
```

**参数说明**

| 成员名称        | 描述                         | 取值                         |
| --------------- | ---------------------------- | ---------------------------- |
| time_inter_s    | P2P 保活最大时间间隔，单位：s  | 0表示关闭 P2P 保活功能       |
| max_attempt_num | P2P 保活最大尝试次数，最大10 | 推荐3，0表示关闭 P2P 保活功能 |

>?
- P2P 保活通过与 P2P 服务器进行通信，判断设备端网络状态是否发生变化，特别是设备端网络出现中断后再连接时，引起设备所在网络的拓扑结构的变化。如果网络拓扑发生变化，IoT Video SDK 内部会重新进行 P2P 协商，从而保证 P2P 通信正常。
- time_inter_s 表示设备与 P2P 服务器每次通信的最大时间间隔，设置得过大，设备网络断开到恢复的时间就会太短，检测不到，可能会导致 P2P 通信失败；设置得过小，通信过于频繁，造成资源浪费。推荐设置5到10s。
- max_attempt_num 表示设备每次与服务器通信探测包数量，每次只要与 P2P 服务器至少有一个探测包通信正常，则认为网络正常。设置得过大，使得探测包过多，将会影响设备的网络资源；设置得过少，在网络差的情况下，将会判断不准确。推荐设置3。
- time_inter_s 和 max_attempt_num 其中一个为0时，表示关闭 P2P 保活机制。在此情况下，IoT Video SDK 内部会通过 system 模块中的 keep_alive_ms（MQTT 保活时间）进行网络判断，但该值较大，灵敏度不如 P2P 保活参数。

#### iv_avt_event_e

**类型描述**
事件类型。

```
typedef enum
{
    IV_AVT_EVENT_P2P_PEER_READY        = 0,  
    IV_AVT_EVENT_P2P_PEER_CONNECT_FAIL = 1,  
    IV_AVT_EVENT_P2P_PEER_ERROR        = 2,  
    IV_AVT_EVENT_P2P_PEER_ADDR_CHANGED = 3,  
    IV_AVT_EVENT_P2P_WATERMARK_LOW     = 4,  
    IV_AVT_EVENT_P2P_WATERMARK_WARN    = 5,  
    IV_AVT_EVENT_P2P_WATERMARK_HIGH    = 6, 
    IV_AVT_EVENT_P2P_BUTT
} iv_avt_event_e;
```

**参数说明**

| 成员名称                           | 描述                      | 取值 |
| ---------------------------------- | ------------------------- | ---- |
| IV_AVT_EVENT_P2P_PEER_READY        | P2P 初始化完成通知         | 0    |
| IV_AVT_EVENT_P2P_PEER_CONNECT_FAIL | P2P 连接 stun 服务器失败     | 1    |
| IV_AVT_EVENT_P2P_PEER_ERROR        | 检测网络错误              | 2    |
| IV_AVT_EVENT_P2P_PEER_ADDR_CHANGED | P2P 地址方式变化           | 3    |
| IV_AVT_EVENT_P2P_WATERMARK_LOW     | P2P 缓存数据低于最低值通知 | 4    |
| IV_AVT_EVENT_P2P_WATERMARK_WARN    | P2P 缓存数据超过报警值通知 | 5    |
| IV_AVT_EVENT_P2P_WATERMARK_HIGH    | P2P 缓存数据超过最大值通知 | 6    |
| IV_AVT_EVENT_P2P_BUTT              | 无效事件                  | 7    |

>?
- 出现 `IV_AVT_EVENT_P2P_PEER_ADDR_CHANGED` 事件，SDK 内部会进行重新协商，无需手动重启 P2P，但是如果用户主动修改设备端 IP 地址，P2P 通道可能恢复较慢。受 MQTT 保活时间影响，可以在 IP 地址修改后直接重新初始化接口，从而加快 P2P 通道恢复时间。
- 出现 `IV_AVT_EVENT_P2P_PEER_CONNECT_FAIL` 事件，表示连接 P2P 服务器失败，需要检查网络。
- 出现 `IV_AVT_EVENT_P2P_PEER_ERROR` 事件，表示网络出现错误，需要检查网络。


#### iv_p2p_send_stats_s

**类型描述**
P2P 发送状态参数

```
typedef struct {
    uint32_t inst_net_rate;
    uint32_t ave_sent_rate; 
    uint64_t sum_sent_acked;
} iv_p2p_send_stats_s;
```

**参数说明**

| 成员名称       | 描述                                                         | 取值     |
| -------------- | ------------------------------------------------------------ | -------- |
| inst_net_rate  | 瞬时发送速率，随网速变化会有较大波动，单位：字节/秒          | uint32_t |
| ave_sent_rate  | 过去一秒内累计发送并得到对端确认的数据，即平均发送速率，单位：字节/秒 | uint32_t |
| sum_sent_acked | 累计发送并得到对端确认的数据， 单位：字节                    | uint64_t |

>?
>- 若出现 IV_AVT_EVENT_P2P_PEER_ADDR_CHANGED 事件，SDK 内部会进行重新协商，无需手动重启 P2P，但是如果用户主动修改设备端 IP 地址，P2P 通道可能恢复较慢，受 MQTT 保活时间影响，可以在 IP 地址修改后直接重新初始化接口，从而加快 P2P 通道恢复时间。
>- 若出现 IV_AVT_EVENT_P2P_PEER_CONNECT_FAIL 事件，表示连接 P2P 服务器失败，需要检查网络。
>- 若出现 IV_AVT_EVENT_P2P_PEER_ERROR 事件，表示网络出现错误，需要检查网络。

## 内存消耗

设备在使用 P2P 发送数据时，其内存消耗与网络带宽（bandwidth）、传输的数据速率（rate）相关。
- 当 bandwidth > rate 时：正常连接时内存消耗 **memory <= m × 150KB**。
- 当 bandwidth <= rate 时：弱网情况下，SDK 内部缓存达到最大，其最大内存消耗
 **memory =（n × 512 KB + 732 KB）× m**。

其中，m 是设备连接的 App 数量，n 是一个 App 请求的接收数据通道数量，即设备端的数据发送通道数量。





## 示例代码

#### 1. P2P 初始化

```
	iv_p2p_parm_s cb;

	cb.p2p_handle_send_init_cb    = test_flv_send_init;
	cb.p2p_handle_send_get_cb     = test_flv_send_data;
	cb.p2p_handle_send_stop_cb    = test_flv_send_stop;
	cb.p2p_handle_event_notify_cb = test_p2p_notify;
	cb.p2p_handle_recv_init_cb    = test_recv_data_init;
	cb.p2p_handle_recv_voice_cb   = test_recv_data;
	cb.p2p_handle_command_cb      = test_command_handle;

	int ret = iv_avt_p2p_init(&cb);
	if (ret) {
			printf(" p2p init failed\n");
			return -1;
	}
```

#### 2. 配置拥塞控制参数

```
iv_avt_p2p_set_buf_watermark(200 * 1024, 400 * 1024, 500 * 1024);
```

#### 3. P2P 退出

```
void p2p_sample_exit(void)
{
    iv_avt_p2p_exit();
}
```
