## 事件名称
PullComplete

## 事件说明
如果APP配置了事件通知，则在URL转拉任务完成之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见[服务端事件通知简介](/document/product/266/7829)。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | String | 回调版本号，固定为4.0 |
| eventType | String | 回调类型，固定为PullComplete |
| data | Object | 具体回调数据 |
| data.vodTaskId | String | 拉取上传任务 ID |
| data.status | Integer | 错误码，0: 成功；其他值: 失败 |
| data.message | String | 错误信息  |
| data.fileId | String | 发起拼接请求后获取到的唯一id |
| data.fileUrl | String | 视频上传完成之后的URL |
| data.transcodeTaskId | String | 如果该视频上传之后发起了转码，则该参数为转码任务id |


## 示例

- 对于[HTTP回调](/document/product/266/7829#http.E5.9B.9E.E8.B0.83)，以下内容为HTTP Post Body；
- 对于[基于消息队列的可靠通知](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5)，以下内容为[PullEvent接口](/document/product/266/7818)返回包体中eventList.eventContent的内容。

```javascript
{
    "version": "4.0",
    "eventType": "PullComplete",
    "data": {
        "status": 0,
        "message": "",
        "vodTaskId": "Pull-f5ac8127b3b6b85cdc13f237c6005d8",
        "fileId": "14508071098244959037",
        "fileUrl": "http://251000330.vod2.myqcloud.com/vod251000330/14508071098244959037/f0.flv",
        "transcodeTaskId": "transcode-0bee89b07a248e27c83fc3d5951213c1"
    }
}
```
