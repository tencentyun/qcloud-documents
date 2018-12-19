## 事件名称
TranscodeComplete

## 事件说明
如果APP配置了事件通知，则在视频转码任务完成之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见[服务端事件通知简介](/document/product/266/7829)。

> 注意：
> - 整个转码过程可能会输出多个规格的视频，例如标清、高清等；只有当所有规格的视频均生成成功之后，才会触发该回调。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | String | 事件通知版本号，固定为4.0 |
| eventType | String | 事件类型，固定为TranscodeComplete |
| data | Object | 具体回调数据 |
| data.status | Integer | 错误码, 0: 成功, 其他值: 失败 |
| data.message | String | 错误信息  |
| data.fileId | String | 被转码的文件ID  |
| data.vodTaskId | String | 转码任务ID  |

## 示例

- 对于[HTTP回调](/document/product/266/7829#http.E5.9B.9E.E8.B0.83)，以下内容为HTTP Post Body；
- 对于[基于消息队列的可靠通知](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5)，以下内容为[PullEvent接口](/document/product/266/7818)返回包体中eventList.eventContent的内容。

### 示例：转码成功

```javascript
{
    "version": "4.0",
    "eventType": "TranscodeComplete",
    "data": {
        "status": 0,
        "message": "",
        "vodTaskId": "Transcode-1edb7eb88a599d05abe451cfc541cfbd",
        "fileId": "14508071098244931831",
        "fileName": "13425173277_2015-09-06-19-06-11_2015-09-06-19-16-11",
        "duration": 599,
        "coverUrl": "http://p.qpic.cn/videoyun/0/1203_8a5015084d4f47cd9a0bc5ecfe78aecb_1/640",
        "playSet": [
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f0.mp4",
                "definition": 0,
                "vbitrate": 246000,
                "vheight": 480,
                "vwidth": 640
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f10.mp4",
                "definition": 10,
                "vbitrate": 149193,
                "vheight": 240,
                "vwidth": 320
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f20.mp4",
                "definition": 20,
                "vbitrate": 297656,
                "vheight": 480,
                "vwidth": 640
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f220.av.m3u8",
                "definition": 220,
                "vbitrate": 524288,
                "vheight": 480,
                "vwidth": 640
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f30.mp4",
                "definition": 30,
                "vbitrate": 899976,
                "vheight": 960,
                "vwidth": 1280
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f40.mp4",
                "definition": 40,
                "vbitrate": 1746652,
                "vheight": 1440,
                "vwidth": 1920
            }
        ]
    }
}
```

### 示例：转码失败

```javascript
{
    "version": "4.0",
    "eventType": "TranscodeComplete",
    "data": {
        "status": -43001,
        "message": "",
        "fileId": "14508071098244931831",
        "vodTaskId": "Transcode-1edb7eb88a599d05abe451cfc541cfbd"
    }
}
```

### 错误码说明

事件通知包体中的status字段表示本次视频处理任务的执行结果。其含义参见[视频处理类操作错误码说明](/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E)。