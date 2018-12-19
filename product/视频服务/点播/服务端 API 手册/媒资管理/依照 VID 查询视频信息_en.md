## API Name
DescribeRecordPlayInfo

## Feature Description
1. The files of recorded videos from Tencent Cloud LVB and ILVB will enter the VOD system. Each record file has its own unique video_id (vid in short);
2. This API is used to acquire video information according to vid.

**Note:**

This API is only compatible with LVB/ILVB recording features of VOD 1.0 version. The VOD platform will gradually reduce the usage of video_id. It is recommended for users to avoid using this parameter that is generated during the recording of LVB or ILVB videos:

* For Tencent Cloud LVB users, it is recommended to enable record callback and acquire video URL from the callback data;
* For Tencent Cloud ILVB users, it is recommended to search for videos according to their name prefixes.

## Request Method

### Request Domain
vod.api.qcloud.com

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vid | Yes | String | video_id that is returned by the LVB/ILVB system |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example

```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeRecordPlayInfo
&vid=1200_c5997fa0f77745a49824150da4e4a6cc
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| fileSet | Array | Video list result set |

The description of each parameter element in the fileSet array is shown below:

| Name | Type | Description |
|---------|---------|---------|
| fileId | String | Video ID |
| fileName | String | Video name |
| duration | String | Video duration |
| status | String | Video status. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use; 2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcoding failed; 10: Waiting to be transcoded; 11: Transcoding partially completed (final state) 100: Deleted |
| imageUrl | String | Video cover image |
| playSet | Array | Video playback information |

The description of each parameter element in the playSet array is shown below:

| Name | Type | Description |
|---------|---------|---------|
| url | String | Playback URL |
| definition | Int | Format, 0:  ["", "Original"], 1:  ["With watermark", "Original"], 10:  ["Mobile phone", "mp4"], 20:  ["Standard definition", "mp4"], 30:  ["High definition", "mp4"], 210:  ["Mobile phone", "hls"], 220:  ["Standard Definition", "hls"], 230:  ["High definition", "hls"] |
| vbitrate | Int | Bit rate. Unit: kbps |
| vheight | String | Height. Unit: px |
| vwidth | String | Width. Unit: px |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to Common Error Codes.   |

### Response Example

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


