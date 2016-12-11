## 事件说明
如果APP配置了事件通知，则在URL转拉任务完成之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见服务端事件通知简介。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | Integer | 回调版本号，固定为4 |
| event_type | String | 回调类型，固定为"pull-complete" |
| data | Object | 具体回调数据 |
| data.status | Integer | 错误码，0: 成功；其他值: 失败 |
| data.message | String | 错误信息  |
| data.file_url | String | 视频上传完成之后的URL  |
| data.file_id | String | 发起拼接请求后获取到的唯一id |
| data.transcode_task_id | String | 如果该视频上传之后发起了转码，则该参数为转码任务id |
| data.porncheck_task_id | String | 如果该视频上传之后发起了鉴黄，则该参数为鉴黄任务id |


## 示例
对于HTTP回调，以下内容为HTTP Post Body；对于基于消息队列的可靠通知，以下内容为PullVodEvent接口返回包体中eventList数组的元素。

### 示例：URL转拉成功

```javascript
{
    "version" : 4,
    "event_type": "pull-complete",
    "data" : {
        "status" : 0,
        "message" : "",
        "vod_task_id" : "pull-f5ac8127b3b6b85cdc13f237c6005d8",
        "file_url": "http://251000330.vod2.myqcloud.com/vod251000330/14508071098244959037/f0.flv",
        "file_id": "14508071098244959037",
        "transcode_task_id" : "transcode-0bee89b07a248e27c83fc3d5951213c1",
        "porncheck_task_id" : "porncheck-f5ac8127b3b6b85cdc13f237c6005d80"
    }
}
```

### 示例：URL转拉失败

TODO：完善真正的错误码和错误信息 by fishlyliu

```javascript
{
    "version" : 4,
    "event": "pull-complete",
    "data" : {
        "status" : 1,
        "message" : "???",
        "vod_task_id" : "pull-f5ac8127b3b6b85cdc13f237c6005d8"
    }
}
```

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| TODO | TODO  |