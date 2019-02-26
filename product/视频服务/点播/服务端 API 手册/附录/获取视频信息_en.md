## API Name
DescribeVodPlayUrls

**Note**

The API has been deprecated. [Acquire Video Information V2](/document/product/266/8586) is recommended.

## Feature Description
1. This API is used to acquire the playback information of current video, including playback URLs, format, bit rate, height, and width.

## Request Method

### Domain for API Request
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | ID of the video whose information is to be acquired |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeVodPlayUrls
&fileId=2721945854681023354
&COMMON_PARAMS
```
## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| playSet | Array | Playback information result set of this video |

playSet: Playback information result set of this video

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| url | String | Playback URL |
| definition | Integer | Format. 0:  ["", "Original"], 1:  ["With watermark", "Original"], 10:  ["Mobile phone", "mp4"], 20:  ["Standard definition", "mp4"], 30:  ["High definition", "mp4"], 110:  ["Mobile phone", "flv"], 120:  ["Standard definition", "flv"], 130:  ["High definition", "flv"],210:  ["Mobile phone", "hls"], 220:  ["Standard Definition", "hls"], 230:  ["High definition", "hls"],240:  ["Ultra high definition", "hls"] |
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
| 2000 | Internal error  |
| 10008 | The file does not exist  |
| 10022 | Internal error |

### Response Example
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

