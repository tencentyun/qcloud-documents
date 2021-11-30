

__功能__

腾讯云直播推流的回调通知。
 


## onPushEvent

事件通知。
```
- (void)onPushEvent:(int)EvtID withParam:(NSDictionary *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| EvtID | int | 参见头文件 TXLiveSDKEventDef.h |
| param | NSDictionary * | 参见头文件 TXLiveSDKTypeDef.h |



## onNetStatus

状态通知。
```
- (void)onNetStatus:(NSDictionary *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | NSDictionary * | 参见头文件 TXLiveSDKTypeDef.h |


 

