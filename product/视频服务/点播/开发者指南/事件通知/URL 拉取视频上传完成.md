## 事件名称
PullComplete

## 事件说明
当 App 配置了事件通知后，在拉取视频上传完成后，App 后台即可通过“普通回调”或“可靠回调”的方式获取该事件通知。事件通知内容为 [PullFileTask 结构](https://cloud.tencent.com/document/api/266/31773#PullFileTask)。

## 示例
### 普通回调
如果选择普通回调模式，则回调 URL 会接收到如下形式的 HTTP 请求。
```json
{
    "version": "4.0",
    "eventType": "PullComplete",
    "data": {
        "TaskId": "Pull-f5ac8127b3b6b85cdc13f237c6005d8",
        "ErrCode": 0,
        "Message": "SUCCESS",
        "FileId": "14508071098244959037",
        "FileUrl": "http://125676836723.vod2.myqcloud.com/xxx/xxx/f0.flv",
        "ProcedureTaskId": ""
    }
}
```

### 可靠回调
如果选择可靠回调模式，调用 [拉取事件通知](/document/product/266/33433) API 会接收到如下形式的 HTTP 应答。
```json
{
	"Response": {
		"EventSet": [
			{
				"EventHandle": "EventHandleX",
				"EventType": "NewFileUpload",
				"FileUploadEvent": null,
				"ProcedureStateChangeEvent": null,
				"FileDeleteEvent": null,
				"PullCompleteEvent": {
                    "TaskId": "Pull-f5ac8127b3b6b85cdc13f237c6005d8",
                    "ErrCode": 0,
                    "Message": "SUCCESS",
                    "FileId": "14508071098244959037",
                    "FileUrl": "http://125676836723.vod2.myqcloud.com/xxx/xxx/f0.flv",
                    "ProcedureTaskId": ""
                },
				"EditMediaComplete": null,
				"WechatPublishComplete": null,
				"TranscodeCompleteEvent": null,
				"ConcatCompleteEvent": null,
				"ClipCompleteEvent": null,
				"CreateImageSpriteCompleteEvent": null,
				"SnapshotByTimeOffsetCompleteEvent": null
			}
		]
	}
}
```
