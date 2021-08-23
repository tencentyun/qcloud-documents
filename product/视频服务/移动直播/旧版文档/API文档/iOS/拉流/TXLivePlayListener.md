

__功能__

腾讯云直播播放的回调通知。


 
## onPlayEvent

直播事件通知。
```
- (void)onPlayEvent:(int)EvtID withParam:(NSDictionary *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| EvtID | int | 参见头文件 TXLiveSDKEventDef.h |
| param | NSDictionary * | 参见头文件 TXLiveSDKTypeDef.h |



## onNetStatus

网络状态通知。
```
- (void)onNetStatus:(NSDictionary *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | NSDictionary * | 参见头文件 TXLiveSDKTypeDef.h |


  

