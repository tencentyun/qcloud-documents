## 接口名称
GetVideoInfo

## 功能说明
1. 该接口可以获取单个视频的多种信息，包括：
    1. 基础信息（basicInfo）：包括视频名称、大小、时长、封面图片等；
    2. 元信息（metaData）：包括视频流信息、音频流信息等；
    3. 加密信息（drm）：对视频加密之后，相关的加密信息；
    4. 转码结果信息（transcodeInfo）：包括该视频转码生成的各种码率的视频的地址、规格、码率、分辨率等；
    5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后，相关截图信息；
    6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图之后，雪碧的相关信息；
    7. 指定时间点截图信息（snapshotByTimeOffsetInfo）对视频依照指定时间点截图后，各个截图的信息。
2. 可以指定回包只返回部分信息。  
*本接口只支持点播4.0*

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 希望获取的视频的ID |
| infoFilter.n | 否 | String | 指定需要返回的信息，可同时指定多个信息，n 从0开始递增。如果未填写该字段，默认返回所有信息。备选项：basicInfo（基础信息）、元信息（metaData）、加密信息（drm）、transcodeInfo（转码结果信息）、imageSpriteInfo（雪碧图信息）、snapshotByTimeOffsetInfo（指定时间点截图信息）、sampleSnapshotInfo（采样截图信息）。 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例

#### 获取视频所有信息

```
https://vod.api.qcloud.com/v2/index.php?Action=GetVideoInfo
&fileId=12345
&COMMON_PARAMS
```

#### 获取视频部分信息（基础信息和转码结果信息）
```
https://vod.api.qcloud.com/v2/index.php?Action=GetVideoInfo
&fileId=12345
&infoFilter.0=basicInfo
&infoFilter.1=transcodeInfo
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| basicInfo | Object | 视频基础信息，字段信息参见[basicInfo（视频基础信息））](#) |
| metaData | Object | 视频元信息，字段信息参见[metaData（视频元信）](#) |
| drm | Object | 文件加密信息，用户在发起任务流时在[转码控制参数](https://cloud.tencent.com/document/product/266/9642#transcode.EF.BC.88.E8.BD.AC.E7.A0.81.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89)指定了加密，该字段才存在。 字段信息参见[drm（视频加密信息）](#drm.EF.BC.88.E8.A7.86.E9.A2.91.E5.8A.A0.E5.AF.86.E4.BF.A1.E6.81.AF.EF.BC.89) |
| transcodeInfo | Object | 视频转码结果信息 |
| sampleSnapshotInfo | Object | 采样截图信息 |
| imageSpriteInfo | Object | 视频雪碧图信息 |
| snapshotByTimeOffsetInfo | Object | 指定时间点截图信息 |
<!--
| keyFrameDescInfo | Object | 视频关键帧描述（打点）信息 |
-->

#### basicInfo（视频基础信息）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| name | String | 视频名称 |
| size | Integer | 视频大小。单位：字节 |
| duration | Integer | 视频时长。单位：秒 |
| description | String | 视频描述 |
| status | String | 视频状态， normal：正常 |
| createTime | Integer | 视频创建时间（Unix时间戳） |
| updateTime | Integer | 视频信息最近更新时间（Unix时间戳） |
| expireTime | Integer | 视频过期时间（Unix时间戳），视频过期之后，该视频及其所有附属对象（转码结果、雪碧图等）将都被删除 |
| classificationId | Integer | 视频分类Id |
| classificationName | String | 视频分类名称 |
| playerId | Integer | 播放器Id |
| coverUrl | String | 视频封面图片地址 |
| type | String | 视频封装格式，例如mp4, flv等 |
| sourceVideoUrl | String | 视频源文件地址 |

#### metaData（视频元信息）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| size | Integer | 视频大小。单位：字节 |
| container | String | 容器类型，例如m4a，mp4等 |
| bitrate | Integer | 视频流码率平均值与音频流码率平均值之和。 单位：bps |
| height | Integer | 视频流高度的最大值。单位：px |
| width | Integer | 视频流宽度的最大值。单位：px |
| md5 | String | 视频的md5值，目前暂不支持 |
| duration | Integer | 视频时长。单位：秒 |
| videoStreamList | Array | 视频流信息 |
| videoStreamList.bitrate | Integer | 视频流的码率，单位：bps |
| videoStreamList.height | Integer | 视频流的高度，单位：px |
| videoStreamList.width | Integer | 视频流的宽度，单位：px |
| videoStreamList.codec | String | 视频流的编码格式，例如h264 |
| videoStreamList.fps | Integer | 帧率，单位：hz |
| audioStreamList | Array | 音频流信息 |
| audioStreamList.bitrate | Integer | 音频流的码率。 单位：bps |
| audioStreamList.samplingRate | Integer | 音频流的采样率。 单位：hz |
| audioStreamList.codec | String | 音频流的编码格式，例如aac |

#### drm（视频加密信息）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| definition | Integer | 加密模板ID |
| encryptType | String | 加密类型，目前只有SingleKey一种 |
| keySource | String | KMS（秘钥管理服务）的类型，总共三种，分别为 VodBuildInKMS：腾讯云点播内置KMS；QCloudKMS：腾讯云KMS系统（暂不支持）；PrivateKMS：用于自有KMS系统（暂不支持）|
| getKeyUrl | String | 获取解密秘钥的URL |
| edkList | Array | 加密后的数据秘钥列表 |

#### transcodeInfo（视频转码结果信息）

> 如果视频已经成功进行转码，则可以获取视频的转码结果信息；如果视频并未进行过转码，或者转码失败，则该视频不存在转码结果信息。

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| transcodeList | Array | 各规格的转码信息集合，每个元素代表一个规格的转码结果 |
| transcodeList.url | String | 转码后的视频文件地址 |
| transcodeList.definition | Integer | 参见[转码参数模板](/document/product/266/8098) |
| transcodeList.bitrate | Integer | 视频流码率平均值与音频流码率平均值之和。 单位：bps |
| transcodeList.height | Integer | 视频流高度的最大值。单位：px |
| transcodeList.width | Integer | 视频流宽度的最大值。单位：px |
| transcodeList.size | Integer | 视频大小。单位：字节 |
| transcodeList.duration | Integer | 视频时长。单位：秒 |
| transcodeList.container | String | 容器类型，例如m4a，mp4等 |
| transcodeList.md5 | String | 视频的md5值 |
| transcodeList.audioStreamList | Array | 音频流信息，字段信息与元信息中audioStreamList相同 |
| transcodeList.videoStreamList | Array | 视频流信息，字段信息与元信息中videoStreamList相同 |

#### sampleSnapshotInfo（采样截图信息）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| sampleSnapshotInfo.definition | Integer | 参见[采样截图参数模板](/document/product/266/9050) |
| sampleSnapshotInfo.sampleType | Integer | 采样方式，Percent为根据百分比间隔采样，Time为根据时间间隔采样，默认为0   |
| sampleSnapshotInfo.Interval | String | 若type为Percent，表示多少百分比一张图； 若type为Time，表示多少时间间隔一张图，单位秒。 第一张图均为视频首帧 |
| sampleSnapshotInfo.imageUrls | Array | 字符串数组，生成的截图url列表 

#### imageSpriteInfo（视频雪碧图信息）

> 如果视频已经成功截取雪碧图，则可以获取视频的雪碧图信息；如果视频并未截取过雪碧图，或者截取雪碧图失败，则该视频不存在雪碧图信息。

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| imageSpriteList | Array | 特定规格的雪碧图信息集合，每个元素代表一套相同规格的雪碧图 |
| imageSpriteList.definition | Integer | 参见[雪碧图参数模板](/document/product/266/8099) |
| imageSpriteList.height | Integer | 雪碧图小图的高度 |
| imageSpriteList.width | Integer | 雪碧图小图的宽度 |
| imageSpriteList.totalCount | Integer | 每一张雪碧图中小图的数量 |
| imageSpriteList.imageUrls | Array | 每一张雪碧图的地址 |

#### snapshotByTimeOffsetInfo（视频指定时间点截图信息）

> 如果视频曾经指定时间点截图成功过，则可以获取视频的指定时间点截图信息；如果视频并未进行过指定时间点截图，则该视频不存在指定时间点截图信息。

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| snapshotByTimeOffsetList | Array | 特定规格的指定时间点截图信息集合。目前每种规格只能有一套截图。 |
| snapshotByTimeOffsetList.definition | Integer | 参见[截图参数模板](/document/product/266/8097) |
| snapshotByTimeOffsetList.picInfoList | Array | 同一规格的截图信息集合，每个元素代表一张截图 |
| snapshotByTimeOffsetList.picInfoList.timeOffset | Integer | 该张截图对应视频文件中的时间偏移。单位：毫秒 |
| snapshotByTimeOffsetList.picInfoList.url | String | 该张截图的地址，如果status非0，则url不存在 ||

<!---
keyFrameDescInfo 视频关键帧描述（打点）信息

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| keyFrame | Array | 视频打点信息集合，每个元素代表一个打点 |

keyFrame 视频打点信息集合

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| timeOffset | Integer | 打点时间偏移，唯一标识一个打点。单位：秒 |
| type | String | 打点类型 |
| comment | String | 打点文本描述信息 |
| screenshotUrl | String | 打点对应的视频截图地址 |
| custom | String | 用户自定义信息，最大512字节 |
-->

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
    "basicInfo": {
        "name": "test file",
        "size": 1000,
        "duration": 10,
        "description": "",
        "status": "",
        "createTime": 1485156352,
        "updateTime": 1485156352,
        "expireTime": 1485256352,
        "classificationId": 1,
        "classificationName": "",
        "playerId": 0,
        "coverUrl": "http://xxxx.vod2.myqcloud.com/xxxx/xxxx/shotup/f0.100_0.jpg",
        "type": "mp4",
        "sourceVideoUrl": "http://xxxx.vod2.myqcloud.com/xxxx/xxxx/f0.mp4"
    },
    "metaData": {
        "size": 10556,
        "container": "m4a",
        "md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
        "duration": 3601,
        "bitrate": 246035,
        "height": 480,
        "width": 640,
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
    },
    "drm": {
        "definition": 10,
        "getKeyUrl": "https://123.xxx.com/getkey",
        "encryptType": "SingleKey",
        "keySource": "VodBuildInKMS",
        "edkList": [
            "232abc30"
        ]
    },
    "transcodeInfo": {
        "transcodeList": [
            {
                "url": "http://xxxx.vod2.myqcloud.com/xxxx/xxxx/f0.mp4",
                "definition": 0,
                "bitrate": 563477,
                "height": 378,
                "width": 672,
                "container": "m4a",
                "duration": 3601,
                "size": 10502,
                "md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
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
            },
            {
                "url": "http://xxxx.vod2.myqcloud.com/xxxx/xxxx/f0.f210.m3u8",
                "definition": 211,
                "bitrate": 563477,
                "height": 378,
                "width": 672,
                "container": "mov",
                "duration": 3601,
                "size": 10502,
                "md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
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
            },
            {
                "url": "http://xxxx.vod2.myqcloud.com/4126dd3evodtransgzp1251132611/61f61b839031868223117809145/master_playlist.m3u8",
                "definition": 10000,
                "duration": 145,
                "size": 265,
                "bitrate": 2840055,
                "height": 1080,
                "width": 1920,
                "container": "hls,applehttp",
                "md5": "bfcf7c6f154b18890661f9e80b0731d0",
                "videoStreamList": [
                    {
                        "bitrate": 2794233,
                        "height": 1080,
                        "width": 1920,
                        "codec": "h264",
                        "fps": 24
                    }
                ],
                "audioStreamList": [
                    {
                        "samplingRate": 44100,
                        "bitrate": 45822,
                        "codec": "aac"
                    }
                ]
            }
        ]
    },
    "sampleSnapshotInfo": [
        {
            "definition": 10,
            "sampleType": "percent",
            "Interval": 10,
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
    ],
    "imageSpriteInfo": {
        "imageSpriteList": [
            {
                "definition": 10,
                "height": 576,
                "width": 1024,
                "totalCount": 100,
                "imageUrls": [
                    "http://xxxx.vod2.myqcloud.com/xxxx/xxxx/imageSprite/1490065623_3650079727.100_0.jpg"
                ]
            }
        ]
    },
    "snapshotByTimeOffsetInfo": {
        "snapshotByTimeOffsetList": [
            {
                "definition": 10,
                "picInfoList": [
                    {
                        "timeOffset": 0,
                        "url": "http://xxxx.vod2.myqcloud.com/xxxx/xxxx/snapshotByTime/1490004036_648247659.100_1000.jpg"
                    },
                    {
                        "timeOffset": 1000,
                        "url": "http://xxxx.vod2.myqcloud.com/xxxx/xxxx/snapshotByTime/1490004081_878165936.100_1000.jpg"
                    }
                ]
            }
        ]
    }
}
```
