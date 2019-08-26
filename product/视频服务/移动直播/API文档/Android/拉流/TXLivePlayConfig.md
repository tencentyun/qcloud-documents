
__功能__

腾讯云直播播放器的参数配置模块。

__介绍__

主要负责 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34775#txliveplayer) 对应的参数设置，**其中绝大多数设置项在播放开始之后再设置是无效的**。



## 常用设置项
### setAutoAdjustCacheTime

设置是否自动调整缓存时间。
```
void setAutoAdjustCacheTime(boolean bAuto)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bAuto | boolean | true：启用； false：关闭。 |

__介绍__

接口说明：
- 默认值：true。
- true：启用自动调整， SDK 将根据网络状况在一个范围内调整缓存时间；通过 [setMaxAutoAdjustCacheTime](https://cloud.tencent.com/document/product/454/34774#setmaxautoadjustcachetime) 和 [setMinAutoAdjustCacheTime](https://cloud.tencent.com/document/product/454/34774#setminautoadjustcachetime) 两个接口来进行设置。
- false：关闭自动调整， SDK 将使用固定缓存时长；通过 [setCacheTime(float)](https://cloud.tencent.com/document/product/454/34774#setcachetime) 来进行设置。

***

### setCacheTime

设置播放器缓存时间。
```
void setCacheTime(float time)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| time | float | 播放器缓存时长。 |

__介绍__

接口说明：
- 设置播放器缓存时间，单位为秒，默认值为5秒。
- 不建议设置过大，会影响秒开以及直播流播放的实时性。

***

### setMaxAutoAdjustCacheTime

设置最大的缓存时间。
```
void setMaxAutoAdjustCacheTime(float time)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| time | float | 播放器最大缓存时间。 |

__介绍__

接口说明：
- 默认值：5，单位为秒。
- 仅在启用自动调用缓存时间接口时，有效。

***

### setMinAutoAdjustCacheTime

设置最小的缓存时间。
```
void setMinAutoAdjustCacheTime(float time)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| time | float | 播放器最小缓存时间。 |

__介绍__

接口说明：
- 默认值：1，单位为秒。
- 仅在启用自动调用缓存时间接口时，有效。

***

### setVideoBlockThreshold

设置播放器视频卡顿报警阈值。
```
void setVideoBlockThreshold(int threshold)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| threshold | int | 播放器视频卡顿报警阈值。 |

__介绍__

接口说明：
- 默认值：800，单位为毫秒。
- 当渲染间隔超过此阈值时候，表明产生了卡顿；播放器会通过 [ITXLivePlayListener#onPlayEvent(int， Bundle)](https://cloud.tencent.com/document/product/454/34773#onplayevent) 回调 PLAY_WARNING_VIDEO_PLAY_LAG 事件通知。

***

### setConnectRetryCount

设置播放器重连次数。
```
void setConnectRetryCount(int count)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| count | int | SDK 重连次数。 |

__介绍__

接口说明：
- 默认值：3；取值范围：1 - 10。
- 当 SDK 与服务器异常断开连接时，SDK 会尝试与服务器重连；您可通过此接口设置重连次数。

***

### setConnectRetryInterval

设置播放器重连间隔。
```
void setConnectRetryInterval(int interval)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| interval | int | SDK 重连间隔。 |

__介绍__

接口说明：
- 默认值：3，单位为秒；取值范围：3 - 30。
- 当 SDK 与服务器异常断开连接时， SDK 会尝试与服务器重连；您可通过此接口设置连续两次重连的时间间隔。

***


## 专业设置项
### setEnableMessage

开启消息通道。
```
void setEnableMessage(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启；false：关闭。 |

__介绍__

此接口在视频帧与消息需要高同步的情况使用，如：直播答题场景。
接口说明：
- 默认值：false。
- 此接口需要搭配 TXLivePusher#sendMessageEx(byte[]) 使用。
- 此接口存在一定的性能开销以及兼容性风险。

***

### enableAEC

设置回声消除。
```
void enableAEC(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启； false：关闭。 |

__介绍__

接口说明：
- 默认值为：false。
- 连麦时必须开启，非连麦时不要开启。

***


## 待废弃设置项
### setEnableNearestIP

设置就近选路。
```
void setEnableNearestIP(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启；false：关闭。 |

__介绍__

待废弃，默认值：true。
只对加速拉流生效，用于指定加速拉流是否开启就近选路。

***

### setRtmpChannelType

设置 RTMP 传输通道的类型。
```
void setRtmpChannelType(int type)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | int | 通道类型。 |

__介绍__

待废弃，默认值：TXLiveConstants#RTMP_CHANNEL_TYPE_AUTO。
通道类型说明：
- TXLiveConstants#RTMP_CHANNEL_TYPE_AUTO ：自动。
- TXLiveConstants#RTMP_CHANNEL_TYPE_STANDARD：标准的 RTMP 协议，网络层采用 TCP 协议。
- TXLiveConstants#RTMP_CHANNEL_TYPE_PRIVATE：标准的 RTMP 协议，网络层采用私有通道传输（在 UDP 上封装的一套可靠快速的传输通道），能够更好地抵抗网络抖动；对于播放来说，私有传输通道只有在拉取低时延加速流时才可以生效。

***

### setCacheFolderPath

设置点播缓存目录。
```
void setCacheFolderPath(String folderPath)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| folderPath | String | 缓存目录。 |

__介绍__

待废弃，如果您需要使用点播播放器，推荐您使用：TXVodPlayer。

***

### setMaxCacheItems

设置点播缓存文件个数。
```
void setMaxCacheItems(int maxCacheItems)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| maxCacheItems | int | 缓存个数。 |

__介绍__

待废弃，如果您需要使用点播播放器，推荐您使用：TXVodPlayer。

***

### setHeaders

设置自定义 HTTP Headers。
```
void setHeaders(Map< String, String > headers)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| headers | Map< String, String > | HTTP 头。 |

__介绍__

待废弃，用于点播视频下载；如果您需要使用点播播放器，推荐您使用：TXVodPlayer。

***


