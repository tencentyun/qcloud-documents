## 事件名称
PullComplete

## 事件说明
当 App 配置了事件通知，并且在拉取视频上传完成后，App 后台即可通过“普通回调”或“可靠回调”的方式获取该事件通知。事件通知内容为 [PullComplete 结构](https://cloud.tencent.com/document/api/266/31773#EventContent)。


## 示例
### 普通回调
如果选择普通回调模式，则回调 URL 会接收到来自云点播的 HTTP 请求。请求采用 POST 方法，请求内容在 BODY 中，如下所示（省略了值为 null 的字段）。

```json
{
    "version": "4.0", 
    "eventType": "PullComplete", 
    "data": {
        "TaskId": "Pull-f5ac8127b3b6b85cdc13f237c6005d8", 
        "ErrCode": 0, 
        "Message": "SUCCESS", 
        "FileId": "14508071098244959037", 
        "MediaBasicInfo": {
            "FileId": "14508071098244959037", 
            "MediaBasicInfo": {
                "Name": "动物世界", 
                "Description": "", 
                "CreateTime": "2019-01-09T16:36:22Z", 
                "UpdateTime": "2019-01-09T16:36:24Z", 
                "ExpireTime": "9999-12-31T23:59:59Z", 
                "ClassId": 0, 
                "ClassName": "其他", 
                "ClassPath": "其他", 
                "CoverUrl": "", 
                "Type": "mp4", 
                "MediaUrl": "http://125676836723.vod2.myqcloud.com/xxx/xxx/xxx.mp4", 
                "TagSet": [ ], 
                "StorageRegion": "ap-guangzhou-2", 
                "SourceInfo": {
                    "SourceType": "Upload", 
                    "SourceContext": ""
                }, 
                "Vid": ""
            }
        }, 
        "FileUrl": "http://125676836723.vod2.myqcloud.com/xxx/xxx/xxx.mp4", 
        "ProcedureTaskId": ""
    }
}
```

### 可靠回调
如果选择可靠回调模式，调用 [拉取事件通知](/document/product/266/33433) API 会接收到如下形式的 HTTP 应答（省略了值为 null 的字段）。

```json
{
    "Response": {
        "EventSet": [
            {
                "EventHandle": "EventHandleX", 
                "EventType": "PullComplete", 
                "PullCompleteEvent": {
                    "TaskId": "Pull-f5ac8127b3b6b85cdc13f237c6005d8", 
                    "ErrCode": 0, 
                    "Message": "SUCCESS", 
                    "FileId": "14508071098244959037", 
                    "MediaBasicInfo": {
                        "FileId": "14508071098244959037", 
                        "MediaBasicInfo": {
                            "Name": "动物世界", 
                            "Description": "", 
                            "CreateTime": "2019-01-09T16:36:22Z", 
                            "UpdateTime": "2019-01-09T16:36:24Z", 
                            "ExpireTime": "9999-12-31T23:59:59Z", 
                            "ClassId": 0, 
                            "ClassName": "其他", 
                            "ClassPath": "其他", 
                            "CoverUrl": "", 
                            "Type": "mp4", 
                            "MediaUrl": "http://125676836723.vod2.myqcloud.com/xxx/xxx/xxx.mp4", 
                            "TagSet": [ ], 
                            "StorageRegion": "ap-guangzhou-2", 
                            "SourceInfo": {
                                "SourceType": "Upload", 
                                "SourceContext": ""
                            }, 
                            "Vid": ""
                        }
                    }, 
                    "FileUrl": "http://125676836723.vod2.myqcloud.com/xxx/xxx/xxx.mp4", 
                    "ProcedureTaskId": ""
                }
            }
        ]
    }
}
```
