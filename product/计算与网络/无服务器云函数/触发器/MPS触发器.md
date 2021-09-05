[视频处理](https://cloud.tencent.com/document/product/862)（Media Processing Service，MPS）是针对海量多媒体数据，提供的云端转码和音视频处理服务。您可以编写云函数来处理 MPS 中的回调信息，通过接收相关回调帮助转储、投递和处理视频任务中的相关事件与后续内容。

MPS 触发器具有以下特点：
- **Push 模型**：MPS 触发器会监听视频处理的回调信息，并通过单次触发的方式将事件数据推送至 SCF 函数。
- **异步调用**：MSP 触发器始终使用异步调用类型来调用函数，结果不会返回给调用方。有关调用类型的更多信息，请参见 [调用类型](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B)。

## MPS 触发器属性

- **事件类型**：MPS 触发器以账号维度的事件类型推送 Event 事件，目前支持工作流任务（WorkflowTask）和视频编辑任务（EditMediaTask）两种事件类型触发。
- **事件处理**：MPS 触发器以服务维度产生的事件作为事件源，不区分地域、资源等属性。每个账号全地域只能创建一个 MPS 触发器。如需多个函数并行处理任务，请参见 [函数间调用 SDK](https://cloud.tencent.com/document/product/583/37316)。

## MPS 触发器的事件消息结构

在指定的 MPS 触发器接收到消息时，事件结构与字段以 WorkflowTask 为例，示例如下：

```
{
    "EventType":"WorkflowTask",
    "WorkflowTaskEvent":{
        "TaskId":"245****654-WorkflowTask-f46dac7fe2436c47******d71946986t0",
        "Status":"FINISH",
        "ErrCode":0,
        "Message":"",
        "InputInfo":{
            "Type":"COS",
            "CosInputInfo":{
                "Bucket":"macgzptest-125****654",
                "Region":"ap-guangzhou",
                "Object":"/dianping2.mp4"
            }
        },
        "MetaData":{
            "AudioDuration":11.261677742004395,
            "AudioStreamSet":[
                {
                    "Bitrate":127771,
                    "Codec":"aac",
                    "SamplingRate":44100
                }
            ],
            "Bitrate":2681468,
            "Container":"mov,mp4,m4a,3gp,3g2,mj2",
            "Duration":11.261677742004395,
            "Height":720,
            "Rotate":90,
            "Size":3539987,
            "VideoDuration":10.510889053344727,
            "VideoStreamSet":[
                {
                    "Bitrate":2553697,
                    "Codec":"h264",
                    "Fps":29,
                    "Height":720,
                    "Width":1280
                }
            ],
            "Width":1280
        },
        "MediaProcessResultSet":[
            {
                "Type":"Transcode",
                "TranscodeTask":{
                    "Status":"SUCCESS",
                    "ErrCode":0,
                    "Message":"SUCCESS",
                    "Input":{
                        "Definition":10,
                        "WatermarkSet":[
                            {
                                "Definition":515247,
                                "TextContent":"",
                                "SvgContent":""
                            }
                        ],
                        "OutputStorage":{
                            "Type":"COS",
                            "CosOutputStorage":{
                                "Bucket":"gztest-125****654",
                                "Region":"ap-guangzhou"
                            }
                        },
                        "OutputObjectPath":"/dasda/dianping2_transcode_10",
                        "SegmentObjectName":"/dasda/dianping2_transcode_10_{number}",
                        "ObjectNumberFormat":{
                            "InitialValue":0,
                            "Increment":1,
                            "MinLength":1,
                            "PlaceHolder":"0"
                        }
                    },
                    "Output":{
                        "OutputStorage":{
                            "Type":"COS",
                            "CosOutputStorage":{
                                "Bucket":"gztest-125****654",
                                "Region":"ap-guangzhou"
                            }
                        },
                        "Path":"/dasda/dianping2_transcode_10.mp4",
                        "Definition":10,
                        "Bitrate":293022,
                        "Height":320,
                        "Width":180,
                        "Size":401637,
                        "Duration":11.26200008392334,
                        "Container":"mov,mp4,m4a,3gp,3g2,mj2",
                        "Md5":"31dcf904c03d0cd78346a12c25c0acc9",
                        "VideoStreamSet":[
                            {
                                "Bitrate":244608,
                                "Codec":"h264",
                                "Fps":24,
                                "Height":320,
                                "Width":180
                            }
                        ],
                        "AudioStreamSet":[
                            {
                                "Bitrate":48414,
                                "Codec":"aac",
                                "SamplingRate":44100
                            }
                        ]
                    }
                },
                "AnimatedGraphicTask":null,
                "SnapshotByTimeOffsetTask":null,
                "SampleSnapshotTask":null,
                "ImageSpriteTask":null
            },
            {
                "Type":"AnimatedGraphics",
                "TranscodeTask":null,
                "AnimatedGraphicTask":{
                    "Status":"FAIL",
                    "ErrCode":30010,
                    "Message":"TencentVodPlatErr Or Unkown",
                    "Input":{
                        "Definition":20000,
                        "StartTimeOffset":0,
                        "EndTimeOffset":600,
                        "OutputStorage":{
                            "Type":"COS",
                            "CosOutputStorage":{
                                "Bucket":"gztest-125****654",
                                "Region":"ap-guangzhou"
                            }
                        },
                        "OutputObjectPath":"/dasda/dianping2_animatedGraphic_20000"
                    },
                    "Output":null
                },
                "SnapshotByTimeOffsetTask":null,
                "SampleSnapshotTask":null,
                "ImageSpriteTask":null
            },
            {
                "Type":"SnapshotByTimeOffset",
                "TranscodeTask":null,
                "AnimatedGraphicTask":null,
                "SnapshotByTimeOffsetTask":{
                    "Status":"SUCCESS",
                    "ErrCode":0,
                    "Message":"SUCCESS",
                    "Input":{
                        "Definition":10,
                        "TimeOffsetSet":[

                        ],
                        "WatermarkSet":[
                            {
                                "Definition":515247,
                                "TextContent":"",
                                "SvgContent":""
                            }
                        ],
                        "OutputStorage":{
                            "Type":"COS",
                            "CosOutputStorage":{
                                "Bucket":"gztest-125****654",
                                "Region":"ap-guangzhou"
                            }
                        },
                        "OutputObjectPath":"/dasda/dianping2_snapshotByOffset_10_{number}",
                        "ObjectNumberFormat":{
                            "InitialValue":0,
                            "Increment":1,
                            "MinLength":1,
                            "PlaceHolder":"0"
                        }
                    },
                    "Output":{
                        "Storage":{
                            "Type":"COS",
                            "CosOutputStorage":{
                                "Bucket":"gztest-125****654",
                                "Region":"ap-guangzhou"
                            }
                        },
                        "Definition":0,
                        "PicInfoSet":[
                            {
                                "TimeOffset":0,
                                "Path":"/dasda/dianping2_snapshotByOffset_10_0.jpg",
                                "WaterMarkDefinition":[
                                    515247
                                ]
                            }
                        ]
                    }
                },
                "SampleSnapshotTask":null,
                "ImageSpriteTask":null
            },
            {
                "Type":"ImageSprites",
                "TranscodeTask":null,
                "AnimatedGraphicTask":null,
                "SnapshotByTimeOffsetTask":null,
                "SampleSnapshotTask":null,
                "ImageSpriteTask":{
                    "Status":"SUCCESS",
                    "ErrCode":0,
                    "Message":"SUCCESS",
                    "Input":{
                        "Definition":10,
                        "OutputStorage":{
                            "Type":"COS",
                            "CosOutputStorage":{
                                "Bucket":"gztest-125****654",
                                "Region":"ap-guangzhou"
                            }
                        },
                        "OutputObjectPath":"/dasda/dianping2_imageSprite_10_{number}",
                        "WebVttObjectName":"/dasda/dianping2_imageSprite_10",
                        "ObjectNumberFormat":{
                            "InitialValue":0,
                            "Increment":1,
                            "MinLength":1,
                            "PlaceHolder":"0"
                        }
                    },
                    "Output":{
                        "Storage":{
                            "Type":"COS",
                            "CosOutputStorage":{
                                "Bucket":"gztest-125****654",
                                "Region":"ap-guangzhou"
                            }
                        },
                        "Definition":10,
                        "Height":80,
                        "Width":142,
                        "TotalCount":2,
                        "ImagePathSet":[
                            "/dasda/imageSprite/dianping2_imageSprite_10_0.jpg"
                        ],
                        "WebVttPath":"/dasda/imageSprite/dianping2_imageSprite_10.vtt"
                    }
                }
            }
        ]
    }
}
```

### WorkflowTask 事件

WorkflowTask 事件消息体详细字段如下：
```
{
    "EventType":"WorkflowTask",
    "WorkflowTaskEvent":{
        // WorkflowTaskEvent 字段
     }
}
```

WorkflowTask 数据结构及字段内容详细说明：

| 名称 | 类型 | 描述 |
|:----|:----|:----|
| TaskId | String | 视频处理任务 ID。 |
| Status | String | 任务流状态，取值如下：<br><li>PROCESSING：处理中。<br><li>FINISH：已完成。 |
| ErrCode | Integer | 已弃用，请使用各个具体任务的 ErrCode。 |
| Message | String | 已弃用，请使用各个具体任务的 Message。 |
| InputInfo | [MediaInputInfo](https://cloud.tencent.com/document/api/862/37615#MediaInputInfo) | 视频处理的目标文件信息。注意：此字段可能返回 null，表示取不到有效值。 |
| MetaData | [MediaMetaData](https://cloud.tencent.com/document/api/862/37615#MediaMetaData) | 原始视频的元信息。注意：此字段可能返回 null，表示取不到有效值。 |
| MediaProcessResultSet | Array of [MediaProcessTaskResult](https://cloud.tencent.com/document/api/862/37615#MediaProcessTaskResult) | 视频处理任务的执行状态与结果。 |
| AiContentReviewResultSet | Array of [AiContentReviewResult](https://cloud.tencent.com/document/api/862/37615#AiContentReviewResult) | 视频内容审核任务的执行状态与结果。 |
| AiAnalysisResultSet | Array of [AiAnalysisResult](https://cloud.tencent.com/document/api/862/37615#AiAnalysisResult) | 视频内容分析任务的执行状态与结果。 |
| AiRecognitionResultSet | Array of [AiRecognitionResult](https://cloud.tencent.com/document/api/862/37615#AiRecognitionResult) | 视频内容识别任务的执行状态与结果。 |


### EditMediaTask 事件

EditMediaTask 事件消息体详细字段如下：
```
{
    "EventType":"EditMediaTask",
    "EditMediaTaskEvent":{
        // EditMediaTask 字段
     }
}
```

EditMediaTask 数据结构及字段内容详细说明：

<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>TaskId</td>
<td>String</td>
<td>任务 ID。</td>
</tr>
<tr>
<td>Status</td>
<td>String</td>
<td>任务状态，取值如下：<br><li>PROCESSING：处理中。<br></li><li>FINISH：已完成。</li></td>
</tr>
<tr>
<td>ErrCode</td>
<td>Integer</td>
<td>错误码0：成功；其他值：失败。</td>
</tr>
<tr>
<td>Message</td>
<td>String</td>
<td>错误信息。</td>
</tr>
<tr>
<td>Input</td>
<td><a href="https://cloud.tencent.com/document/api/862/37615#EditMediaTaskInput">EditMediaTaskInput</a></td>
<td>视频编辑任务的输入。</td>
</tr>
<tr>
<td>Output</td>
<td><a href="https://cloud.tencent.com/document/api/862/37615#EditMediaTaskOutput">EditMediaTaskOutput</a></td>
<td>视频编辑任务的输出。注意：此字段可能返回 null，表示取不到有效值。</td>
</tr>
</tbody></table>
