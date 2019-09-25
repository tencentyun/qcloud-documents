视频内容审核是借助于 AI 对视频内容进行智能审核，是一种离线任务。任务的执行结果中，包括审核评分、审核建议和嫌疑视频片段。根据“审核建议”，视频管理者可以决定视频是否允许公开，有效规避违规视频带来的法律风险和品牌伤害。

云点播可以对视频画面、ASR 文字和 OCR 文字三种对象进行智能审核，审核操作包括鉴黄、鉴暴和鉴政。

<table>
    <tr>
        <th style="width:20%">
            对象
        </th>
        <th style="width:10%">
            操作
        </th>
        <th>
            说明
        </th>
    </tr>
    <tr>
        <td rowspan=4>
            视频画面（人和物体）
        </td>
    </tr>
    <tr>
        <td>
            鉴黄
        </td>
        <td>
				    对视频画面做涉黄检查，检查内容包括：
				    <li>porn：色情</li>
				    <li>vulgar：低俗</li>
				    <li>intimacy：亲密行为</li>
				    <li>sexy：性感</li>
        </td>
    </tr>
    <tr>
        <td>
            鉴暴
        </td>
        <td>
				    对视频画面做涉暴检查，检查内容包括：
				    <li>militant：武装分子</li>
				    <li>guns：武器枪支</li>
				    <li>bloody：血腥画面</li>
				    <li>explosion：爆炸火灾</li>
				    <li>banners：暴恐旗帜</li>
				    <li>terrorists：暴恐人物</li>
				    <li>police：警察部队</li>
				    <li>crowd：人群聚集</li>
        </td>
    </tr>
    <tr>
        <td>
            鉴政
        </td>
        <td>
            对视频画面做涉政检查，检查内容包括：
				    <li>violation_photo：违规图标</li>
				    <li>politician：政治人物</li>
        </td>
    </tr>
    <tr>
        <td rowspan=2>
            ASR 文字（音频中的文字）
        </td>
        <td>
				    鉴黄
        <td>
            对音频中的文字做涉黄检查，识别出嫌疑关键词
        </td>
    </tr>
    <tr>
        <td>
            鉴政
        </td>
        <td>
            对音频中的文字做涉政检查，识别出嫌疑关键词
        </td>
    </tr>
    <tr>
        <td rowspan=2>
            OCR 文字（画面中的文字）
        </td>
        <td>
				    鉴黄
        </td>
        <td>
            对画面中的文字做涉黄检查，识别出嫌疑关键词
        </td>
    </tr>
    <tr>
        <td>
            鉴政
        </td>
        <td>
            对画面中的文字做涉政检查，识别出嫌疑关键词
        </td>
    </tr>
</table>


| 字段名     | 类型   | 含义                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| confidence | Float  | 审核评分（0 - 100），评分越高，嫌疑越大                |
| suggestion | String | 审核建议，有 pass，review，block 三种：<ul><li>pass：嫌疑度不高，建议直接通过</li><li>review：嫌疑度较高，建议人工复核</li><li>block：嫌疑度很高，建议直接屏蔽</li></ul> |
| segments   | Array  | 有嫌疑的视频片段，帮助定位视频中具体哪一段涉嫌违规         |

## <span id = "sh"></span>视频内容审核模板

通过视频内容审核参数，可以控制审核任务具体执行哪几项审核操作。云点播使用视频内容审核模板来表示智能审核参数集合，通过视频内容审核模板，可以指定审核任务中执行以下哪一项或几项操作：
- 对视频画面做鉴黄
- 对视频画面做鉴暴
- 对视频画面做鉴政
- 对 ASR 文字做鉴黄
- 对 ASR 文字做鉴政
- 对 OCR 文字做鉴黄
- 对 OCR 文字做鉴政

针对常见的操作组合，云点播提供了 [预置视频内容审核模板](https://cloud.tencent.com/document/product/266/33476#verify)。另外，您还可以调用 [服务端 API](https://cloud.tencent.com/document/product/266/34790) 创建和管理自定义视频内容审核模板。

## 任务发起

发起视频内容审核任务，有“通过服务端 API 直接发起”、“通过控制台直接发起”和“上传时指定要执行的任务”三种方式。具体请参照视频处理的 [任务发起](https://cloud.tencent.com/document/product/266/33475#OriginatingTask)。

以下是各种方式发起视频内容审核任务的说明：

* 调用服务端 API [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 发起任务：在请求中的`AiContentReviewTask`参数指定 [视频内容审核模板](#sh) 的模板 ID。
* 调用服务端 API [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426) 发起任务：在请求中的`AiContentReviewTask`参数指定 [视频内容审核模板](#sh) 的模板 ID。
* 通过控制台对视频发起任务：在控制台 [添加任务流](https://cloud.tencent.com/document/product/266/33819)，任务流中开启视频内容审核；在控制台使用该任务流 [发起视频处理](https://cloud.tencent.com/document/product/266/2841#.E5.A4.84.E7.90.86.E8.A7.86.E9.A2.91)。
* 服务端上传时指定任务：在控制台 [添加任务流](https://cloud.tencent.com/document/product/266/33819)，任务流中开启视频内容审核； [申请上传](https://cloud.tencent.com/document/api/266/31767#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0) 中的`procedure`参数指定为该任务流。
* 客户端上传时指定任务：在控制台 [添加任务流](https://cloud.tencent.com/document/product/266/33819)，任务流中开启视频内容审核；在 [客户端上传签名](https://cloud.tencent.com/document/product/266/9221#.E7.AD.BE.E5.90.8D.E5.8F.82.E6.95.B0) 中的`procedure`指定该任务流。
* 控制台上传：在控制台 [添加任务流](https://cloud.tencent.com/document/product/266/33819)，任务流中开启视频内容审核；通过控制台上传视频，选择 [上传的同时对视频进行处理操作](https://cloud.tencent.com/document/product/266/2841#.E4.B8.8A.E4.BC.A0.E8.A7.86.E9.A2.91) 并指定视频上传后执行该任务流。

## 结果获取

发起视频内容审核任务后，您可以通过异步等待 [结果通知](https://cloud.tencent.com/document/product/266/33475#ResultNotification) 和同步进行 [任务查询](https://cloud.tencent.com/document/product/266/33475#TaskQuery) 两种方式获取视频内容审核任务的执行结果。下面是发起内容审核任务后，普通回调方式下结果通知的示例（省略了值为 null 的字段）：
```json
{
    "EventType":"ProcedureStateChanged",
    "ProcedureStateChangeEvent":{
        "TaskId":"1256768367-Procedure-2e1af2456351812be963e309cc133403t0",
        "Status":"FINISH",
        "FileId":"5285890784246869930",
        "FileName":"动物世界",
        "FileUrl":"http://1256768367.vod2.myqcloud.com/xxx/xxx/AtUCmy6gmIYA.mp4",
        "MetaData":{
            "AudioDuration":60,
            "AudioStreamSet":[
                {
                    "Bitrate":383854,
                    "Codec":"aac",
                    "SamplingRate":48000
                }
            ],
            "Bitrate":1021028,
            "Container":"mov,mp4,m4a,3gp,3g2,mj2",
            "Duration":60,
            "Height":480,
            "Rotate":0,
            "Size":7700180,
            "VideoDuration":60,
            "VideoStreamSet":[
                {
                    "Bitrate":637174,
                    "Codec":"h264",
                    "Fps":23,
                    "Height":480,
                    "Width":640
                }
            ],
            "Width":640
        },
        "AiContentReviewResultSet":[
            {
                "Type":"Porn",
                "PornTask":{
                    "Status":"SUCCESS",
                    "ErrCode":0,
                    "Message":"",
                    "Input":{
                        "Definition":10
                    },
                    "Output":{
                        "Confidence":98,
                        "Suggestion":"block",
                        "Label":"sexy",
                        "SegmentSet":[
                            {
                                "StartTimeOffset":9.5,
                                "EndTimeOffset":14,
                                "Confidence":98,
                                "Suggestion":"block",
                                "Label":"sexy",
                                "Url":"http://xxx.vod2.myqcluod.com/xxx/xxx/xx1.jpg",
                                "PicUrlExpireTimeStamp":1530005146
                            },
                            {
                                "StartTimeOffset":16.5,
                                "EndTimeOffset":18,
                                "Confidence":80,
                                "Suggestion":"review",
                                "Label":"sexy",
                                "Url":"http://xxx.vod2.myqcluod.com/xxx/xxx/xx2.jpg",
                                "PicUrlExpireTimeStamp":1530005146
                            },
                            {
                                "StartTimeOffset":41,
                                "EndTimeOffset":49,
                                "Confidence":97,
                                "Suggestion":"block",
                                "Label":"sexy",
                                "Url":"http://xxx.vod2.myqcluod.com/xxx/xxx/xx3.jpg",
                                "PicUrlExpireTimeStamp":1530005146
                            }
                        ]
                    }
                }
            },
            {
                "Type":"Terrorism",
                "TerrorismTask":{
                    "Status":"SUCCESS",
                    "ErrCode":0,
                    "Message":"",
                    "Input":{
                        "Definition":10
                    },
                    "Output":{
                        "Confidence":0,
                        "Suggestion":"pass",
                        "SegmentSet":[

                        ]
                    }
                }
            },
            {
                "Type":"Political",
                "PoliticalTask":{
                    "Status":"SUCCESS",
                    "ErrCode":0,
                    "Message":"",
                    "Input":{
                        "Definition":10
                    },
                    "Output":{
                        "Confidence":0,
                        "Suggestion":"pass",
                        "SegmentSet":[

                        ]
                    }
                }
            }
        ],
        "TasksPriority":0,
        "TasksNotifyMode":""
    }
}
```

回调结果中，`ProcedureStateChangeEvent.AiContentReviewResultSet`有`Type`为`Porn`、`Terrorism`和`Political`三种类型的审核结果，分别代表视频画面鉴黄、视频画面鉴暴和视频画面鉴政。

* `Type`为`Porn`的结果显示，`Output.Suggestion`为`block`，即涉黄可能性高，建议拦截，涉黄的置信度为98分，涉黄的原因是`sexy`（性感）。
* `Type`为`Porn`的结果`Output.SegmentSet`，给出了三段有涉黄嫌疑的视频片段，每个片段的`StartTimeOffset`和`EndTimeOffset`标明了片段起止时间。
* `Type`为`Terrorism`和`Political`的结果显示，视频没有涉暴和涉政的嫌疑。
