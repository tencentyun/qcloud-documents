## Creating a Channel

### 1. API description

Domain name: live.api.qcloud.com
 

### 2. Input parameters

| **Parameter Name** | **Required** | **Type** | **Description** |
| --- | --- | --- | --- |
| channelName | Yes | String | Channel name |
| channelDescribe | No | string | LVB channel description |
| outputSourceType | Yes | int | Select an output source. 1: RTMP output only; 2: HLS output only; 3: Both RTMP and HLS output. |
| playerPassword | No | string | Password for the receiver's player. |
| sourceList | Yes | array | An LVB source list. Each LVB source may contain the type, name, and address (limited to stream pulling). Note: Only one LVB source is supported. |
| watermarkId | No | int | Watermark ID |
| outputRate | No | array | Output bitrate. Note: For the parameter array, 0 indicates the original bitrate, 10 indicates a bitrate of 550 (standard definition), and 20 indicates a bitrate of 900 (high definition). The value 0 is required if you need to set the bitrate. |

The sourceList structure is as follows:

| **Parameter Name** | **Required** | **Type** | **Description** |
| --- | --- | --- | --- |
| name | Yes | string | LVB source name |
| type | Yes | int | 1: RTMP push |

### 3. Output parameters

| **Parameter Name** | **Type** | **Description** |
| --- | --- | --- |
| code | Int | Error code. 0: Successful; other values: Failed |
| message | String | Error message |
| channel\_id | String | Channel ID |

### 4. Examples

Input (RTMP push)

<pre>
https://domain/v2/index.php?Action=CreateLVBChannel&channelName=%E5%9B%BD%E9%99%85%E4%B9%92%E4%B9%93%E7%90%83%E9%94%A6%E6%A0%87%E8%B5%9B3&outputSourceType=2&sourceList.1.name=video-1999&sourceList.1.type=1&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>


Output

```
{
    "code": 0,
  "message": "",
"codeDesc":"Success",
"channel_id": "XXX",
     "channelInfo":
      {
       "upstream_address":"rtmp://2000.livepush.myqcloud.com/live/YYYYYYYYYYYYYYYYYY?bizid2000",
	   "downstream_address":[{
	   "rate_type":0,
            "hls_downstream_address": "http://2000.liveplay.myqcloud.com/live/XXX.m3u8",
            "rtmp_downstream_address": "rtmp://2000.liveplay.myqcloud.com/live/XXX",
            "flv_downstream_address": "http://2000.liveplay.myqcloud.com/live/XXX.flv"
        }]
      }
}
```

### 5. Standard parameter definitions

Channel status definitions:

| Value | Status |
| --- | --- |
| 0 | No input stream |
| 1 | LVB in progress |
| 2 | Exception |
| 3 | Disable |

Receiver type definitions:

| Type | Description |
| --- | --- |
| 1 | RTMP output |
| 2 | HLS output |
| 3 | RTMP and HLS output |

LVB stream protocol definitions:

| Type | Description |
| --- | --- |
| 1 | RTMP push |
| 2 | RTMP pull |
| 3 | HLS pull |

