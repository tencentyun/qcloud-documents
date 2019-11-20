
__功能__

腾讯云直播播放的回调通知。



## onPlayEvent

播放事件通知。
```
void onPlayEvent(final int event, final Bundle param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| event | final int | 事件 ID，ID 类型请查看代码中的 com.tencent.rtmp.TXLiveConstants.[PUSH_EVT_CONNECT_SUCC](https://cloud.tencent.com/document/product/454/7885#.E4.BA.8B.E4.BB.B6.E5.A4.84.E7.90.86) 播放事件列表。 |
| param | final Bundle | 事件相关的参数（key，value）格式，其中 key 请查看代码中的 com.tencent.rtmp.TXLiveConstants.EVT_TIME 事件参数。 |

***

## onNetStatus

网络状态通知。
```
void onNetStatus(final Bundle status)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| status | final Bundle | 通知的内容（key，value）格式，其中 key 请查看代码中的 com.tencent.rtmp.TXLiveConstants.NET_STATUS_VIDEO_BITRATE 网络状态通知。 |

***

