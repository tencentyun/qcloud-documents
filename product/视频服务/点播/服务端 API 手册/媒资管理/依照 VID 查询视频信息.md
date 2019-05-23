## 接口名称
DescribeRecordPlayInfo

## 功能说明
1. 腾讯云直播、互动直播录制文件会进入点播系统，每个录制文件会有唯一的 video_id（简称 vid）。
2. 该接口用于依照 vid 获取视频信息。

>! 该接口仅为兼容点播1.0时代的直播/互动直播录制而存在。点播平台将逐步弱化 video_id 的使用，建议用户不要直接使用直播和互动直播录制生成的该参数：

* 对于腾讯云直播用户，建议开通录制回调，并直接从回调数据中获取视频 URL。
* 对于腾讯云互动直播用户，建议用户依照视频名称前缀来搜索视频。

## 请求方式

### 请求域名
`vod.api.qcloud.com`

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| vid | 是 | String | 直播/互动直播系统返回的 video_id。 |
| COMMON_PARAMS | 是 |  | 参见 [公共参数](/document/api/213/6976)。 |

### 请求示例

```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeRecordPlayInfo
&vid=1200_c5997fa0f77745a49824150da4e4a6cc
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | int | 错误码, 0：成功，其他值：失败。 |
| message | String | 错误信息。 |
| fileSet | Array | 视频列表结果集。 |

fileSet 数组中，各元素的参数说明如下：

| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| fileId | String | 视频 ID。 |
| fileName | String | 视频名称。 |
| duration | String | 视频持续时间。 |
| status | String | 视频状态：-1：未上传完成，不存在；0：初始化，暂未使用；1：审核不通过，暂未使用； 2：正常；3：暂停；4：转码中；5：发布中；6：删除中；7：转码失败；10：等待转码；11：转码部分完成（终态）100：已删除。 |
| imageUrl | String | 视频封面图片。 |
| playSet | Array | 视频播放信息。 |

playSet 数组中，各元素的参数说明如下：

| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| url | String | 播放地址。 |
| definition | Int | 格式， 0: ["", "原始"], 1: ["带水印", "原始"], 10: ["手机", "mp4"], 20: ["标清", "mp4"],  30: ["高清", "mp4"], 210: ["手机", "hls"], 220: ["标清", "hls"], 230: ["高清", "hls"]。 |
| vbitrate | Int | 码率，单位：kbps。|
| vheight | String | 高度，单位：px。 |
| vwidth | String | 宽度，单位：px。 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000 - 7000 | 参见 [公共错误码](https://cloud.tencent.com/document/api/213/10146)。  |

### 应答示例

```javascript
{
    "code": 0,
    "message": "",
    "fileSet": [
        {
            "fileId": "11624759161874546966",
            "fileName": "13425173277_2015-09-06-18-56-11_2015-09-06-19-06-11",
            "duration": 600,
            "status": "2",
            "image_url": "http://p.qpic.cn/videoyun/0/1203_7626dd7d1c3e48eea1230026126caf7d_1/640",
            "playSet": [
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f0.mp4",
                    "definition": 0,
                    "vbitrate": 250000,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f10.mp4",
                    "definition": 10,
                    "vbitrate": 149128,
                    "vheight": 240,
                    "vwidth": 320
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f220.av.m3u8",
                    "definition": 220,
                    "vbitrate": 524288,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f30.mp4",
                    "definition": 30,
                    "vbitrate": 865828,
                    "vheight": 960,
                    "vwidth": 1280
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f40.mp4",
                    "definition": 40,
                    "vbitrate": 1709293,
                    "vheight": 1440,
                    "vwidth": 1920
                }
            ]
        }
    ]
}

```

