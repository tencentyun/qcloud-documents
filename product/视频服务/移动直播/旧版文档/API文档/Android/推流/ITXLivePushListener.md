

__功能__

腾讯云直播推流的回调通知。 



## onPushEvent

推流事件通知。
```
void onPushEvent(final int event, final Bundle param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| event | final int | 事件 ID。ID 类型请参考头文件 TXLiveConstants.PUSH_EVT_CONNECT_SUCC 推流事件列表。 |
| param | final Bundle | 事件相关的参数。（key，value）格式，其中 key 请查看代码中的 TXLiveConstants.EVT_TIME 事件参数。 |



## onNetStatus

网络状态通知。
```
void onNetStatus(final Bundle status)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| status | final Bundle | 通知的内容。（key，value）格式，其中 key 请查看代码中的  TXLiveConstants.NET_STATUS_VIDEO_BITRATE 网络状态通知。 |



 
