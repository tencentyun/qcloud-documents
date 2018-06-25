## 事件名称
ProcedureStateChanged

## 事件说明
如果APP配置了事件通知，则在任务流状态变更之后，点播后台会将该事件通知给APP后台。

APP后台接收该事件通知的方法参见[服务端事件通知简介](/document/product/266/7829)。

> 注意：
> - 任务流状态变更通知模式由发起任务流时的参数notifyMode决定。 当notifyMode为Finish：只有当任务流全部执行完毕时，才发起一次事件通知；当notifyMode为Change：只要任务流中每个子任务的状态发生变化，都进行事件通知。 默认为Finish。

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | String | 事件通知版本号，固定为4.0 |
| eventType | String | 事件类型，固定为ProcedureStateChanged |
| data | Object | 具体回调数据 |
| data.status | String | 任务流状态，有PROCESSING和FINISH两种 |
| data.errCode | Integer | 错误码。 0: 成功, 其他值: 失败 |
| data.message | String | 错误信息  |
| data.fileId | String | 文件ID  |
| data.metaData | Object | 视频元信息，该字段一定存在，字段信息参见[metaData（视频元信息）](#metadata.EF.BC.88.E8.A7.86.E9.A2.91.E5.85.83.E4.BF.A1.E6.81.AF.EF.BC.89)  |
| data.drm | Object | 文件加密信息，用户在发起任务流时在[转码控制参数](https://cloud.tencent.com/document/product/266/9642#transcode.EF.BC.88.E8.BD.AC.E7.A0.81.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89)指定了加密，该字段才存在。 字段信息参见[drm（视频加密信息）](#drm.EF.BC.88.E8.A7.86.E9.A2.91.E5.8A.A0.E5.AF.86.E4.BF.A1.E6.81.AF.EF.BC.89)  |
| data.processTaskList | Array | 任务流包含的任务列表，字段信息参见[processTaskList（任务列表）](#processtasklist.EF.BC.88.E4.BB.BB.E5.8A.A1.E5.88.97.E8.A1.A8.EF.BC.89)  |

#### metaData（视频元信息）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| size | Integer | 视频大小。单位：字节 |
| container | String | 容器类型，例如m4a，mp4等 |
| bitrate | Integer | 视频流码率平均值与音频流码率平均值之和。 单位：kbps |
| height | Integer | 视频流高度的最大值。单位：px |
| width | Integer | 视频流宽度的最大值。单位：px |
| md5 | String | 视频的md5值 |
| duration | Integer | 视频时长。单位：秒 |
| videoStreamList | Array | 视频流信息 |
| videoStreamList.bitrate | Integer | 视频流的码率，单位：kbps |
| videoStreamList.height | Integer | 视频流的高度，单位：px |
| videoStreamList.width | Integer | 视频流的宽度，单位：px |
| videoStreamList.codec | String | 视频流的编码格式，例如h264 |
| videoStreamList.fps | Integer | 帧率，单位：hz |
| audioStreamList | Array | 音频流信息 |
| audioStreamList.bitrate | Integer | 音频流的码率。 单位：kbps |
| audioStreamList.samplingRate | Integer | 音频流的采样率。 单位：hz |
| audioStreamList.codec | String | 音频流的编码格式，例如aac |

#### drm（视频加密信息）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| definition | Integer | 加密模板ID |
| keySource | String | KMS的类型，总共三种，分别为 VodBuildInKMS：腾讯云点播内置KMS；QCloudKMS：腾讯云KMS系统（暂不支持）；PrivateKMS：用于自有KMS系统（暂不支持）。 |
| getKeyUrl | String | 获取解密秘钥的URL |
| edkList | Array | 加密后的数据秘钥列表 |

#### processTaskList（任务列表）
任务信息列表，目前有[Trancode（转码任务）](#trancode.EF.BC.88.E8.BD.AC.E7.A0.81.E4.BB.BB.E5.8A.A1.EF.BC.89)，[SampleSnapshot（采样截图任务）](#samplesnapshot.EF.BC.88.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89)，[CoverBySnapshot（截图图片作为视频封面任务）](#coverbysnapshot.EF.BC.88.E6.88.AA.E5.9B.BE.E5.9B.BE.E7.89.87.E4.BD.9C.E4.B8.BA.E8.A7.86.E9.A2.91.E5.B0.81.E9.9D.A2.E4.BB.BB.E5.8A.A1.EF.BC.89)，[SnapshotByTimeOffset（按时间点截图任务）](#snapshotbytimeoffset.EF.BC.88.E6.8C.89.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89)，[PullFile (拉取视频文件) ](https://cloud.tencent.com/document/product/266/7817)。

#### Trancode（转码任务）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| taskType | String | 任务类型，固定为Transcode |
| status | String | 任务状态，有PROCESSING，SUCCESS，FAIL三种 |
| errCode | Integer | 错误码。 0: 成功, 其他值: 失败,其中30009为原文件异常失败；30010为系统失败或未知 |
| message | String | 错误信息 |
| input | Object | 任务的输入信息 |
| input.definition | Integer | 转码模板ID |
| input.watermark | Integer | 是否设置水印，1为设置，0为没设置。 是否设置取决于用户转码配置 |
| output | Object | 任务的输出信息，任务成功时会有该字段，失败则没有 |
| output.url | String | 视频url |
| output.size | Integer | 视频大小。单位：字节 |
| output.container | String | 容器类型，例如m4a，mp4等 |
| output.bitrate | Integer | 视频流码率和音频流码率之和，单位：kbps |
| output.height | Integer | 视频流高度的最大值。单位：px |
| output.width | Integer | 视频流宽度的最大值。单位：px |
| output.md5 | String | 视频的md5值 |
| output.duration | Integer | 视频时长。单位：秒 |
| output.videoStreamList | Array | 视频流信息，元素字段和元信息中videoStreamList相同 |
| output.audioStreamList | Array | 音频流信息，元素字段和元信息中audioStreamList相同 |

#### SampleSnapshot（采样截图任务）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| taskType | String | 任务类型，固定为SampleSnapshot |
| status | String | 任务状态，有PROCESSING，SUCCESS，FAIL三种 |
| errCode | Integer | 错误码。 0: 成功, 其他值: 失败，其中30009为原文件异常失败；30010为系统失败或未知 |
| message | String | 错误信息 |
| input | Object | 任务的输入信息 |
| input.definition | Integer | 采样截图模板ID |
| output | Object | 任务的输出信息，任务成功时会有该字段，失败则没有 |
| output.imageUrls | Array | 字符串数组，生成的截图url列表 |

#### SnapshotByTimeOffset（按时间点截图任务）
	
| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| taskType | String | 任务类型，固定为SnapshotByTimeOffset |
| status | String | 任务状态，有PROCESSING，SUCCESS，FAIL三种 |
| errCode | Integer | 错误码。 0: 成功, 其他值: 失败，其中30009为原文件异常失败；30010为系统失败或未知 |
| message | String | 错误信息 |
| input | Object | 任务的输入信息 |
| input.definition | Integer | 按时间点截图模板ID |
| input.timeOffset | Array | 整形数组，截图的时间偏移，单位为毫秒 |
| output | Object | 任务的输出信息，任务成功时会有该字段，失败则没有 |
| output.imgInfo | Array | 生成的截图信息列表 |
| output.imgInfo.timeOffset | Integer | 该张截图的时间偏移，单位毫秒 |
| output.imgInfo.url | String | 截图url |



#### CoverBySnapshot（截图图片作为视频封面任务）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| taskType | String | 任务类型，固定为CoverBySnapshot |
| status | String | 任务状态，有PROCESSING，SUCCESS，FAIL三种 |
| errCode | Integer | 错误码。 0: 成功, 其他值: 失败，其中30009为原文件异常失败；30010为系统失败或未知 |
| message | String | 错误信息 |
| input | Object | 任务的输入信息 |
| input.definition | Integer | 采样截图模板ID |
| input.positionType | String | 截图方式。Time：依照时间点截图；Percent：依照百分比截图 |
| input.position | Integer | 截图位置。对于依照时间点截图，该值表示指定视频第几秒的截图作为封面；对于依照百分比截图，该值表示使用视频百分之多少的截图作为封面 |
| output | Object | 任务的输出信息，任务成功时会有该字段，失败则没有 |
| output.imageUrl | Array | 作为视频封面的截图url |

#### PullFile（拉取视频文件任务）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| taskType | String | 任务类型，固定为PullFile |
| status | String | 任务状态，有PROCESSING，SUCCESS，FAIL三种 |
| errCode | Integer | 错误码。 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| input | Object | 任务的输入信息 |
| input.url | String | 需要拉取的视频的 URL |
| input.fileName | String | 视频文件的名称 |
| input.md5 | Integer | 视频文件的MD5 |
| output | Object | 任务的输出信息，任务成功时会有该字段，失败则没有 |
| output.fileId | String | 视频文件ID |
| output.fileSize | String | 视频文件大小 |
| output.url | String | 视频文件的播放地址 |

<!--
#### ImageSprite（雪碧图截图任务）

| **参数名称** | **类型** | **描述** |
|---------|---------|---------|
| taskType | String | 任务类型，固定为ImageSprite |
| status | String | 任务状态，有PROCESSING，SUCCESS，FAIL三种 |
| errCode | Integer | 错误码。 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| input | Object | 任务的输入信息，任务成功时会有该字段，失败则没有 |
| input.definition | Integer | 雪碧图模板ID |
| input.watermark | Integer | 是否设置水印，1为设置，2为没设置。 是否设置取决于用户转码配置 |
| output | Object | 任务的输出信息 |
| output.totalCount | Integer | 雪碧图小图总数 |
| output.imageUrls | Array | 字符串数组，生成的雪碧图的url列表 |
-->

## 示例

- 对于[HTTP回调](/document/product/266/7829#http.E5.9B.9E.E8.B0.83)，以下内容为HTTP Post Body；
- 对于[基于消息队列的可靠通知](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5)，以下内容为[PullEvent接口](/document/product/266/7818)返回包体中eventList.eventContent的内容。

### 示例：

```javascript
{
    "version": "4.0",
    "eventType": "ProcedureStateChanged",
    "data": {
        "vodTaskId": "251000333-mango-c27bdf65ea06646171e714f25f5aac63",
        "status": "PROCESSING",
        "message": "",
        "errCode": 0,
        "fileId": "123123123",
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
            },
            {
                "taskType": "SnapshotByTimeOffset",
                "status": "SUCCESS",
                "message": "",
                "errCode": 0,
                "input": {
                    "definition": 10,
                    "timeOffset": [
                        300,
                        400
                    ]
                },
                "output": {
                    "imgInfo": [
                        {
                            "timeOffset": 300,
                            "url": "http://125xx.vod2.myqcloud.com/42f909a8vodtransgzp251000333/dee2963524820810452267193/snapshot/1502280085_887773835.100_300.jpg"
                        },
                        {
                            "timeOffset": 400,
                            "url": "http://125xx.vod2.myqcloud.com/42f909a8vodtransgzp251000333/dee2963524820810452267193/snapshot/1502280085_887773835.100_400.jpg"
                        }
                    ]
                }
            }
        ]
    }
}
```

### 错误码说明

事件通知包体中的errCode字段表示本次视频处理任务的执行结果。其含义参见[视频处理类操作错误码说明](/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E)。
