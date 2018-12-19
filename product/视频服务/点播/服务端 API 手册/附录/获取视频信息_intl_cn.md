## 接口名称
DescribeVodPlayUrls

**注意**

该接口仅限点播1.0使用。如果是点播4.0，请使用[获取视频信息V2](/document/product/266/8586)。

## 功能说明
1. 获取当前视频的播放信息，包括播放地址、格式、码率、高度、宽度信息。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 希望获取的视频的ID |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeVodPlayUrls
&fileId=2721945854681023354
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| playSet | Array | 该视频的播放信息结果集 |

playSet 该视频的播放信息结果集

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| url | String | 播放地址 |
| definition | Integer | 格式， 0: ["", "原始"], 1: ["带水印", "原始"], 10: ["手机", "mp4"], 20: ["标清", "mp4"], 30: ["高清", "mp4"], 110: ["手机", "flv"], 120: ["标清", "flv"], 130: ["高清", "flv"],210: ["手机", "hls"], 220: ["标清", "hls"], 230: ["高清", "hls"],240: ["超高清", "hls"] |
| vbitrate | Integer | 码率，单位：kbps |
| vheight | Integer | 高度，单位：px |
| vwidth | Integer | 宽度，单位：px |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1 | 内部错误  |
| 1000 | 无效参数  |
| 1001 | 内部错误  |
| 1003 | 内部错误  |
| 2000 | 内部错误  |
| 10008 | 文件不存在  |
| 10022 | 内部错误 |

### 应答示例
```javascript
{
    "code": 0,
    "message": "",
    "playSet": [
        {
            "url": "http://vcloud1200.tc.qq.com/1200_5b9688d481d8b811095d30a78cf44c4285026a4c.f0.mp4",
            "definition": 0,
            "vbitrate": 2332000,
            "vheight": 576,
            "vwidth": 1024
        }
    ]
}
```
