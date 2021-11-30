## 事件名称
ConcatComplete

## 事件说明
如果APP配置了事件通知，则在视频拼接任务完成之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见[服务端事件通知简介](/document/product/266/7829)。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | String | 回调版本号，固定为4.0 |
| eventType | String | 回调类型，固定为ConcatComplete |
| data | Object | 具体回调数据 |
| data.vodTaskId | String | 拼接任务ID  |
| data.fileInfo | Array | 拼接输出的视频文件信息 |

data.fileInfo数组中每个元素均为Object，每个参数含义如下：

| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| fileType | String | 拼接出的文件类型 |
| status | Integer | 任务执行结果，0为成功，-1或者4为失败 |
| message | String | 错误信息 |
| fileId | String | 拼接出的文件的fileId |
| fileUrl | String | 拼接出的文件url  |

## 示例

- 对于[HTTP回调](/document/product/266/7829#http.E5.9B.9E.E8.B0.83)，以下内容为HTTP Post Body；
- 对于[基于消息队列的可靠通知](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5)，以下内容为[PullEvent接口](/document/product/266/7818)返回包体中eventList.eventContent的内容。

### 示例：视频拼接成功

```javascript
{
    "version": "4.0",
    "eventType": "ConcatComplete",
    "data": {
        "vodTaskId": "Concat-1edb7eb88a599d05abe451cfc541cfbd",
        "fileInfo": [
            {
                "fileType": "m3u8",
                "status": 0,
                "message": "",
                "fileId": "14508071098244931831",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244931831/playlist.f6.m3u8"
            },
            {
                "fileType": "mp4",
                "status": 0,
                "message": "",
                "fileId": "14508071098244929440",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4"
            }
        ]
    }
}
```

### 示例：视频拼接失败

```javascript
{
    "version": "4.0",
    "eventType": "ConcatComplete",
    "data": {
        "message": "",
        "vodTaskId": "Concat-1edb7eb88a599d05abe451cfc541cfbd",
        "fileInfo": [
            {
                "fileType": "m3u8",
                "status": 4,
                "message": ""
            },
            {
                "fileType": "mp4",
                "status": 4,
                "message": ""
            }
        ]
    }
}
```

### 错误码说明

事件通知包体中的status字段表示本次视频处理任务的执行结果，0为成功，-1或者4为失败。
