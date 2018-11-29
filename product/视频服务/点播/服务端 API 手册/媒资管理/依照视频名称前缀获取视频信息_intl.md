## API Name
DescribeVodPlayInfo

## Feature Description
1. This API is used to search for videos according to their name prefixes and return to its playback information list.

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileName | Yes | String | Video name (prefix match) |
| pageNo | No | Integer | Page number |
| pageSize | No | Integer | Page size |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeVodPlayInfo
&fileName=13425173277
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| totalCount | Integer | Total number of videos |
| fileSet | Array | Video list result set |

fileSet: Video list result set

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|---------|
| fileId | String | Video ID |
| fileName | String | Video name |
| duration | String | Video duration |
| status | String | Video status. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use; 2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcoding failed; 100: Deleted |
| imageUrl | String | Video cover image |
| playSet | Array | Video playback information |

playSet: Playback information result set of the video

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|---------|
| url | String | Playback URL |
| definition | Integer | Format. 0:  ["", "Original"], 1:  ["With watermark", "Original"], 10:  ["Mobile phone", "mp4"], 20:  ["Standard definition", "mp4"], 30:  ["High definition", "mp4"], 110:  ["Mobile phone", "flv"], 120:  ["Standard definition", "flv"], 130:  ["High definition", "flv"] |
| vbitrate | Integer | Bit rate. Unit: kbps |
| vheight | Integer | Height. Unit: px |
| vwidth | Integer | Width. Unit: px |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1 | Internal error  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 1003 | Internal error  |
| 10008 | The file does not exist  |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "totalCount": "105",
    "fileSet": [
        {
            "fileId": "11624759161874546966",
            "fileName": "13425173277_2015-09-06-18-56-11_2015-09-06-19-06-11",
            "duration": 600,
            "status": "2",
            "imageUrl": "http://p.qpic.cn/videoyun/0/1203_7626dd7d1c3e48eea1230026126caf7d_1/640",
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
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f20.mp4",
                    "definition": 20,
                    "vbitrate": 299837,
                    "vheight": 480,
                    "vwidth": 640
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
        },
        {
            "fileId": "11624759161874546967",
            "fileName": "13425173277_2015-09-06-19-06-11_2015-09-06-19-16-11",
            "duration": 599,
            "status": "2",
            "imageUrl": "http://p.qpic.cn/videoyun/0/1203_8a5015084d4f47cd9a0bc5ecfe78aecb_1/640",
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
    ]
}
```

