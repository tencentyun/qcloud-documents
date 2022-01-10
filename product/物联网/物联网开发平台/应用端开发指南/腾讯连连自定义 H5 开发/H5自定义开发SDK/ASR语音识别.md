## 语音识别

目前支持两种场景，分别为“录音文件”与“一句话识别”，两种场景下入参会有所不同。
由于识别过程是异步，因此接口“voiceRecognition”并不会立即返回识别结果，可以理解为该接口是创建了一个“异步任务”，当这个成功被创建的“异步任务”执行完后，会通过 websocket 将结果推送到所有订阅该 deviceId 的终端上，下文为您详细介绍 ASR 语音识别。

**接口定义**

```typescript
sdk.voiceRecognition({...}) => Promise<{...}>
```

**参数说明**

- 关于“录音文件”场景支持的音频类型、大小限制以及相关字段的详细介绍，详情请参见 [ 录音文件识别](https://cloud.tencent.com/document/api/1093/37823)。
- 关于“一句话识别”场景支持的音频类型、大小限制以及相关字段的详细介绍，详情请参见 [一句话识别](https://cloud.tencent.com/document/api/1093/35646)。

**公共参数**

| 参数名         | 参数描述                                                     | 类型         | 必填 |
| -------------- | ------------------------------------------------------------ | ------------ | ---- |
| DeviceId       | 默认使用当前设备的设备 ID                                    | string       | 否   |
| AudioType      | 识别场景。<br><li>“录音文件”取值“file”</li><br><li>“一句话识别”取值“sentence”</li> | string       | 是   |
| Data           | 音频文件                                                     | Blob \| File | 是   |
| ResourceName   | 文件名称，如果 Data 类型是 File，则取其“name”作为默认值      | string       | 否   |
| EngineType     | 引擎模型类型，默认值为“16k_zh”                               | string       | 否   |
| FilterDirty    | 是否过滤脏词                                                 | number       | 否   |
| FilterModal    | 是否过滤语气词                                               | number       | 否   |
| FilterPunc     | 是否过滤标点符号                                             | number       | 否   |
| ConvertNumMode | 是否进行阿拉伯数字智能转换                                   | number       | 否   |

**录音文件额外参数**

| 参数名             | 参数描述            | 类型   | 必填 |
| ------------------ | ------------------- | ------ | ---- |
| ChannelNum         | 语音声道数，默认为1 | number | 否   |
| SpeakerDiarization | 是否开启话者分离    | number | 否   |
| SpeakerNumber      | 话者分离人数        | number | 否   |

**返回值**

| 参数名        | 参数描述                       | 类型   |
| ------------- | ------------------------------ | ------ |
| ResourceToken | 某个设备下，音频文件的唯一标示 | string |



## 监听识别结果

对于“录音文件”场景，如果音频文件过大，后台可能会对音频文件进行分片识别，每个分片识别完成后，都将推送一条 websocket 消息，但推送的消息不保证顺序（例如有可能分片2的结果先到达）。

对于“asrResponse”事件，实际是基于“wsControl”事件进行二次封装；当然，您也可以通过监听“wsControl”事件获取识别结果。

**接口定义**

```
sdk.on('asrResponse', ({ deviceId, data }) => void)
```

**返回值说明**

| 参数名              | 参数描述                                                     | 类型   |
| :------------------ | :----------------------------------------------------------- | :----- |
| deviceId            | 设备 ID                                                      | string |
| data                | 识别结果数据                                                 | object |
| data.resource_token | 某个设备下，音频文件的唯一标示                               | string |
| data.result_code    | 状态码，0代表成功                                            | number |
| data.total_num      | 分片总数                                                     | number |
| data.seq            | 当前分片序号                                                 | number |
| data.res_text       | 当前分片识别结果，对于“录音文件”场景，识别结果会包含分段时间戳 | string |



## 获取语音文件下载链接（仅限“录音文件”场景）

**接口定义**

```typescript
sdk.getAsrDownloadUrl({...}) => Promise<{...}>
```

**参数说明**

| 参数名        | 参数描述                                   | 类型   | 必填 |
| :------------ | :----------------------------------------- | :----- | :--- |
| DeviceId      | 设备 ID                                    | string | 是   |
| ResourceToken | 调用 voiceRecognition 返回的 ResourceToken | string | 是   |

**返回值说明**

| 参数名      | 参数描述     | 类型   |
| :---------- | :----------- | :----- |
| ResourceURL | cos 访问链接 | string |

