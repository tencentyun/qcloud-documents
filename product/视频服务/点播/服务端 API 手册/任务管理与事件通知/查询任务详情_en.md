## API Name
GetTaskInfo

## Feature Description
1. The API is used to obtain task execution status;
2. Only tasks within the last three days (72 hours) can be queried.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| vodTaskId | Yes | String | Task ID |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

### Request Example

```
https://vod.api.qcloud.com/v2/index.php?Action=GetTaskInfo
&vodTaskId=1251989944-Procedure-d7c9631c15ecf653b1ff67e34cb04692
&COMMON_PARAMS
```

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message. |
| type | String | Task type: Procedure/transcode/clipVideo. |
| status | String | Task status: WAITING/PROCESSING/FINISH. |
| createTime | Integer | Task creation time (Unix timestamp). |
| beginProcessTime | Integer | The time when the task is executed (Unix timestamp). The value is 0 if the task is still in queue. |
| finishTime | Integer | The latest update time of the task information (Unix timestamp). The value is 0 if the task is still in process. |
| data | Object | Task details. The value changes based on different types. If the status is WAITING, this field is unavailable. |


### data Description
When "type" is Procedure, the "data" content is the same as the data field of the callback packet in [Task Flow Status Change](https://cloud.tencent.com/document/product/266/9636).

When "type" is transcode, the "data" content is the same as the data field of the callback packet in [Video Transcoding Completion](https://cloud.tencent.com/document/product/266/7832).

When "type" is clipVideo, the "data" content is the same as the data field of the callback packet in [Video Clipping Completion](https://cloud.tencent.com/document/product/266/10157).

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter. |
| 70014 | The task does not exist. |
| 10027 | System internal error. |

### Response Example (for "procedure")
```
{
    "code": 0,
    "message": "",
    "type": "procedure",
    "status":"PROCESSING",
    "createTime": 1485156352,
    "beginProcessTime": 1485156354,
    "finishTime": 1485156352,
    "data": {
        "errCode": 0,
        "fileId": "24961954183381008",
        "metaData": {
            "size": 10556,
            "container": "m4a",
            "bitrate": 246035,
            "height": 480,
            "width": 640,
            "md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
            "duration": 3601,
            "videoStreamList": [
                {
                    "bitrate": 246000,
                    "height": 480,
                    "width": 640,
                    "codec": "h264",
                    "fps": 22
                }
            ],
            "audioStreamList": [
                {
                    "codec": "aac",
                    "samplingRate": 44100,
                    "bitrate": 35
                }
            ]
        },
        "drm": {
            "definition": 10,
            "getKeyUrl": "https://123.xxx.com/getkey",
            "keySource": "VodBuildInKMS",
            "edkList": [
                "232abc30"
            ]
        },
        "processTaskList": [
            {
                "taskType": "Transcode",
                "status": "PROCESSING",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 10,
                    "watermark": 1
                }
            },
            {
                "taskType": "Transcode",
                "status": "SUCCESS",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 20,
                    "watermark": 1
                },
                "output": {
                    "url": "http://125xx.vod2.myqcloud.com/9fcd41e6vodgzp1251953760/7585975f9031868222912340/f20.mp4",
                    "size": 10556,
                    "container": "m4a",
                    "md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                    "bitrate": 246035,
                    "height": 480,
                    "width": 640,
                    "duration": 3601,
                    "videoStreamList": [
                        {
                            "bitrate": 246000,
                            "height": 480,
                            "width": 640,
                            "codec": "h264",
                            "fps": 222
                        }
                    ],
                    "audioStreamList": [
                        {
                            "codec": "aac",
                            "samplingRate": 44100,
                            "bitrate": 35
                        }
                    ]
                }
            },
            {
                "taskType": "SampleSnapshot",
                "status": "SUCCESS",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 10
                },
                "output": {
                    "imageUrls": [
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx1.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx2.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx3.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx4.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx5.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx6.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx7.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx8.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx9.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx10.png"
                    ]
                }
            },
            {
                "taskType": "CoverBySnapshot",
                "status": "SUCCESS",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 10,
                    "position": 10,
                    "positionType": "Percent"
                },
                "output": {
                    "imageUrl": "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx1.png"
                }
            }
        ]
    }
}
```

### Response Example (for "transcode")
```
{
    "code": 0,
    "message": "",
    "type": "transcode",
    "status":"PROCESSING",
    "createTime": 1485156352,
    "beginProcessTime": 1485156354,
    "finishTime": 1485156352,
    "data": {
        "errCode": 0,
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


