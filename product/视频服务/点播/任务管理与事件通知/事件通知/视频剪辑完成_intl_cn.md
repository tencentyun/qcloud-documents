## 事件名称
ClipComplete

## 事件说明
如果APP配置了事件通知，则在视频剪辑任务完成之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见[服务端事件通知简介](/document/product/266/7829)。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | String | 回调版本号，固定为4.0 |
| eventType | String | 回调类型，固定为ClipComplete |
| data | Object | 具体回调数据 |
| data.vodTaskId | String | 剪辑任务ID  |
| data.srcFileId | String | 剪辑任务源文件fileId  |
| data.fileInfo | Object | 剪辑输出的视频文件信息 |

data.fileInfo每个参数含义如下：

| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| fileType | String | 剪辑的文件类型 |
| status | Integer | 该类型文件的错误信息，0为成功，其他为失败，详见错误码说明 |
| message | String | 错误信息 |
| fileId | String | 剪辑的文件的fileId |
| fileUrl | String | 剪辑的文件url  |

## 示例

- 对于[HTTP回调](/document/product/266/7829#http.E5.9B.9E.E8.B0.83)，以下内容为HTTP Post Body；
- 对于[基于消息队列的可靠通知](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5)，以下内容为[PullEvent接口](/document/product/266/7818)返回包体中eventList.eventContent的内容。

### 示例：视频剪辑成功

```javascript
{
    "version": "4.0",
    "eventType": "ClipComplete",
    "data": {
        "vodTaskId": "clipVideo-0a78cf44c4285026a4c",
        "srcFileId": "16092504232103571364",
        "fileInfo": {
            "fileType": "mp4",
            "status": 0,
            "message": "",
            "fileId": "14508071098244929440",
            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4"
        }
    }
}
```

### 示例：视频剪辑失败

```javascript
{
    "version": "4.0",
    "eventType": "ClipComplete",
    "data": {
        "vodTaskId": "clipVideo-0a78cf44c4285026a4c",
        "srcFileId": "16092504232103571364",
        "fileInfo": {
            "status": -43001,
            "message": ""
        }
    }
}
```

### 错误码说明

事件通知包体中的status字段表示本次视频处理任务的执行结果。其含义参见[视频处理类操作错误码说明](/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E)。