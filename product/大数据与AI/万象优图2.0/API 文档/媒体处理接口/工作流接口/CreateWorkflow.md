## 功能描述

Create Workflow 接口用于新增工作流。

## 请求

#### 请求示例

```plaintext
POST /workflow HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体：

#### 请求体1：音视频转码、极速高清、截帧、转动图、人声分离、精彩集锦、音视频拼接、智能封面、视频增强、SDR to HDR、自定义函数、超分辨率和音视频分段


```plaintext
<Request>
    <MediaWorkflow>
        <Name>demo</Name>
        <State>Active</State>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Transcode_1581665960537,Animation_1581665960538,Concat_1581665960539,SmartCover_1581665960539,VoiceSeparate_1581665960551,VideoMontage_1581665960551,SDRtoHDR_1581665960553,VideoProcess_1581665960554,SCF_1581665960566,SuperResolution_1581665960583,Segment_1581665960667</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Transcode_1581665960537>End</Transcode_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Concat_1581665960539>End</Concat_1581665960539>
                <SmartCover_1581665960539>End</SmartCover_1581665960539>
                <VoiceSeparate_1581665960551>End</VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>End</VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>End</SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>End</VideoProcess_1581665960554>
                <SCF_1581665960566>End</SCF_1581665960566>
                <SuperResolution_1581665960583>End</SuperResolution_1581665960583>
                <Segment_1581665960667>End</Segment_1581665960667>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                        <NotifyConfig>
                            <Url>http://www.callback.com</Url>
                            <Event>TaskFinish,WorkflowFinish</Event>
                            <Type>Url</Type>
                        </NotifyConfig>
                        <ExtFilter>
                            <State>on</State>
                            <Audio>true</Audio>
                            <Custom>true</Custom>
                            <CustomExts>mp4/mp3</CustomExts>
                            <AllFile>true</AllFile>
                        </ExtFilter>
                    </Input>
                </Start>
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                        <SmartCover>
                            <Format>png</Format>
                            <Width>128</Width>
                            <Height>128</Height>
                            <Count>3</Count>
                            <DeleteDuplicates>false</DeleteDuplicates>
                        </SmartCover> 
                    </Operation>
                </SmartCover_1581665960539>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                            <SpriteObject>abc/${RunId}/snapshot-${number}.jpg</SpriteObject>
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Transcode_1581665960537>
                    <Type>Transcode</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/trans.mp4</Object>
                        </Output>
                    </Operation>
                </Transcode_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Concat_1581665960539>
                    <Type>Concat</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.${ext}</Object>
                        </Output>
                    </Operation>
                </Concat_1581665960539>
                <VoiceSeparate_1581665960551>
                    <Type>VoiceSeparate</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163b164</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <AuObject>bcd/${RunId}/audio.mp3</AuObject>
                            <Object>bcd/${RunId}/background.mp3</Object>
                        </Output>
                    </Operation>
                </VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>
                    <Type>VideoMontage</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba73l9</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/montage.mp4</Object>
                        </Output>
                    </Operation>
                </VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>
                    <Type>SDRtoHDR</Type>
                    <Operation>
                        <SDRtoHDR>
                            <HdrMode>HLG</HdrMode>
                        </SDRtoHDR>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/SDRtoHDR.mp4</Object>
                        </Output>
                    </Operation>
                </SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>
                    <Type>VideoProcess</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55356fshb18</TemplateId>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/videoProcess.mp4</Object>
                        </Output>
                    </Operation>
                </VideoProcess_1581665960554>
                <SCF_1581665960566>
                    <Type>SCF</Type>
                    <Operation>
                        <SCF>
                            <Region>ap-chengdu</Region>
                            <FunctionName>test</FunctionName>
                            <Namespace>testspace</Namespace>
                        </SCF>
                    </Operation>
                </SCF_1581665960566>
                <SuperResolution_1581665960583>
                    <Type>SuperResolution</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}/SuperResolution.mkv</Object>
                        </Output>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <TranscodeTemplateId>t160606b9752148c4absdfaf2f55163b1f</TranscodeTemplateId>
                    </Operation>
                </SuperResolution_1581665960583>
                <Segment_1581665960667>
                    <Type>Segment</Type>
                    <Operation>
                        <Segment>
                            <Format>mp4</Format>
                            <Duration>5</Duration>
                        </Segment>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>test-trans${Number}</Object>
                        </Output>
                    </Operation>
                </Segment_1581665960667>
            </Nodes>
        </Topology>
    </MediaWorkflow>
</Request>
```

#### 请求体2：HLS 自适应多码流

```plaintext
<Request>
    <MediaWorkflow>
        <Name>demo</Name>
        <State>Active</State>
        <Topology>
            <Dependencies>
                <Start>HlsPackConfig_1581665960532</Start>
                <HlsPackConfig_1581665960532>VideoStream_1581665960536,VideoStream_1581665960537</HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>HlsPack</VideoStream_1581665960536>
                <VideoStream_1581665960537>HlsPack</VideoStream_1581665960537>
                <HlsPack_1581665960538>End</HlsPack_1581665960538>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                        <NotifyConfig>
                            <Url>http://www.callback.com</Url>
                            <Event>TaskFinish,WorkflowFinish</Event>
                            <Type>Url</Type>
                        </NotifyConfig>
                        <ExtFilter>
                            <State>on</State>
                            <Audio>true</Audio>
                            <Custom>true</Custom>
                            <CustomExts>mp4/mp3</CustomExts>
                            <AllFile>true</AllFile>
                        </ExtFilter>
                    </Input>
                </Start>
                <HlsPackConfig_1581665960532>
                    <Type>HlsPackConfig</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${InputPath}/${InputName}._${RunId}.${ext}</Object>
                        </Output>
                    </Operation>
                </HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_1/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960536>
                <VideoStream_1581665960537>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606bgfdg2148c4ab182f55163ba7bj</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_2/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960537>
                <HlsPack_1581665960538>
                    <Type>HlsPack</Type>
                    <Operation>
                        <HlsPackInfo>
                            <VideoStreamConfig>
                                <VideoStreamName>VideoStream_1581665960536</VideoStreamName>
                                <BandWidth>0</BandWidth>
                            </VideoStreamConfig>
                            <VideoStreamConfig>
                                <VideoStreamName>VideoStream_1581665960537</VideoStreamName>
                                <BandWidth>0</BandWidth>
                            </VideoStreamConfig>
                        </HlsPackInfo>
                    </Operation>
                </HlsPack_1581665960538>
            </Nodes>
        </Topology>
    </MediaWorkflow>
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | -------- |
| Request            | 无     | 保存请求的容器 | Container | 是       |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述       | 类型      | 是否必选 |
| ------------------ | ------- | ---------- | --------- | -------- |
| MediaWorkflow      | Request | 工作流节点 | Container | 是       |


Container 类型 MediaWorkflow 的具体数据描述如下：

| 节点名称（关键字） | 父节点                | 描述       | 类型      | 是否必选 | 限制                                        |
| ------------------ | --------------------- | ---------- | --------- | -------- | ------------------------------------------- |
| Name               | Request.MediaWorkflow | 工作流名称 | String    | 是       | 支持中文、英文、数字、—和_，长度限制128字符 |
| State              | Request.MediaWorkflow | 工作流状态 | String    | 否       | Paused/Active                               |
| Topology           | Request.MediaWorkflow | 拓扑信息   | Container | 是       | 无                                          |



Container 类型 Topology 的具体数据描述如下：

| 节点名称（关键字） | 父节点                         | 描述         | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | ------| --------- | ---- | ---- |
| Dependencies      | Request.MediaWorkflow.</br>Topology | 节点依赖关系 | Container    | 是   | 无 |
| Nodes             | Request.MediaWorkflow.</br>Topology | 节点列表 | Container    | 是   | 无 |

Container 类型 Nodes 的具体数据描述如下：

| 节点名称（关键字） | 父节点                               | 描述            | 类型      | 是否<br>必选 | 限制                                                         |
| ------------------ | ------------------------------------ | --------------- | --------- | ------------ | ------------------------------------------------------------ |
| Start         | Request.MediaWorkflow.</br>Topology.Nodes | 开始节点 | Container    | 是   | 只有唯一一个开始节点 |
| Animation\_\*\*\* | Request.MediaWorkflow.</br>Topology.Nodes | 动图类型节点 | Container    | 否   | 节点名称以 Animation 为前缀，可能有多个动图节点 |
| Snapshot\_\*\*\*  | Request.MediaWorkflow.</br>Topology.Nodes | 截图类型节点 | Container    | 否   | 节点名称以 Snapshot 为前缀，可能有多个截图节点|
| SmartCover\_\*\*\* | Request.MediaWorkflow.</br>Topology.Nodes | 智能封面节点 | Container    | 否   | 节点名称以 SmartCover 为前缀，可能有多个智能封面节点|
| Transcode\_\*\*\*  | Request.MediaWorkflow.</br>Topology.Nodes | 转码节点 | Container    | 否   | 节点名称以 Transcode 为前缀，可能有多个转码节点|
| Concat\_\*\*\*  | Request.MediaWorkflow.</br>Topology.Nodes | 音视频拼接节点 | Container    | 否   | 节点名称以 Concat 为前缀，可能有多个音视频拼接节点|
| VoiceSeparate\_\*\*\*  | Request.MediaWorkflow.</br>Topology.Nodes | 人声节点 | Container    | 否   | 节点名称以 VoiceSeparate 为前缀，可能有多个人声分离节点|
| VideoMontage\_\*\*\*  | Request.MediaWorkflow.</br>Topology.Nodes | 精彩集锦节点 | Container    | 否   | 节点名称以 VideoMontage 为前缀，可能有多个精彩集锦节点|
| HlsPackConfig\_\*\*\*| Request.MediaWorkflow.</br>Topology.Nodes | Hls 打包配置节点 | Container    | 否   | 节点名称以 HlsPackConfig 为前缀，只能有一个 Hls 打包配置节点。只能在 start 节点之后，后面只能是视频子流节点，可以有多个视频子流节点|
| VideoStream\_\*\*\*| Request.MediaWorkflow.</br>Topology.Nodes | 视频子流节点 | Container    | 否   | 节点名称以 VideoStream 为前缀，可能有多个视频子流节点 ，只能在 HlsPackConfig 节点之后，后面只能是 HlsPack 节点|
| HlsPack\_\*\*\*| Request.MediaWorkflow.</br>Topology.Nodes | Hls 打包节点 | Container    | 否   | 节点名称以 HlsPack 为前缀，只能有一个 Hls 打包节点 ，只能在视频子流节点之后，后面只能是 End 节点|
| SDRtoHDR\_\*\*\*       | Request.MediaWorkflow.</br>Topology.Nodes | SDRtoHDR 节点    | Container | 否           | 节点名称以 SDRtoHDR 为前缀，可能有多个 SDRtoHDR 节点             |
| VideoProcess\_\*\*\*   | Request.MediaWorkflow.</br>Topology.Nodes | 视频处理节点    | Container | 否           | 节点名称以 VideoProcess 为前缀，可能有多个视频处理节点         |
| SCF\_\*\*\*            | Request.MediaWorkflow.</br>Topology.Nodes | SCF 函数节点     | Container | 否           | 节点名称以 SCF 为前缀，可能有多个 SCF 函数节点                   |
| SuperResolution\_\*\*\* | Request.MediaWorkflow.</br>Topology.Nodes | 超分辨率节点 | Container| 否 | 节点名称以 SuperResolution 为前缀，可能有多个超分辨率节点 |
| Segment\_\*\*\* | Request.MediaWorkflow.</br>Topology.Nodes | 音视频分段节点 | Container| 否 | 节点名称以 Segment 为前缀，可能有多个音视频分段节点 |

Container 类型 Start 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                     | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | ------| --------- | ---- | ---- |
| Type         | Request.MediaWorkflow.<br>Topology.Nodes.Start | 节点类型 | String    | 是   | Start |
| Input        | Request.MediaWorkflow.<br>Topology.Nodes.Start | 输入信息 | Container | 是   | 无 |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                           | 描述                                     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------ | ---------------------------------------- | --------- | -------- | ---- |
| ObjectPrefix       | Request.MediaWorkflow.<br>Topology.Nodes.Start.Input | Object 前缀 | String | 是       | 无   |
| QueueId            | Request.MediaWorkflow.<br>Topology.Nodes.Start.Input | 队列 ID     | String | 是       | 无   |
| NotifyConfig       | Request.MediaWorkflow.<br>Topology.Nodes.Start.Input | 回调信息，如果不设置，则使用队列的回调信息 | Container | 否       | 无   |
| ExtFilter          | Request.MediaWorkflow.<br>Topology.Nodes.Start.Input | 文件后缀过滤器                           | Container | 否       | 无   |


Container 类型 Start.Input.NotifyConfig 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型   | 是否必选 | 限制                                                         |
| ------------------ | ------------------------------------------------------------ | -------- | ------ | ---- | ------------------------------------------------------------ |
| Url                | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.NotifyConfig | 回调地址 | String | 是   | 不能为内网地址                                               |
| Type               | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.NotifyConfig | 回调类型 | String | 是   |  Url:Url回调                                         |
| Event              | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.NotifyConfig | 回调信息 | String | 是   | 1. TaskFinish：任务完成 </br> 2. WorkflowFinish：工作流完成 </br> 3. 支持多种事件，以逗号分隔 |



Container 类型 Start.Input.ExtFilter 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                     | 描述                | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ---------------------------------------------------------- | ------------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| State              | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.ExtFilter | 开关                | String | 否   | Off    | On/Off                                                       |
| Video              | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.ExtFilter | 打开视频后缀限制    | String | 否   | false  | false/true                                                   |
| Audio              | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.ExtFilter | 打开音频后缀限制    | String | 否   | false  | false/true                                                   |
| ContentType        | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.ExtFilter | 打开 ContentType 限制 | String | 否   | false  | false/true                                                   |
| Custom             | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.ExtFilter | 打开自定义后缀限制  | String | 否   | false  | false/true                                                   |
| CustomExts         | Request.MediaWorkflow.Topology.</br>Nodes.Start.Input.ExtFilter | 自定义后缀          | String | 否   | 无     | 1. 多种文件后缀以/分隔，后缀个数不超过10个</br>2. 当 Custom 为 true 时，该参数必填 |
| AllFile    | Request.MediaWorkflow.Topology.Nodes.Start.Input.ExtFilter | 所有文件          |  String  |  否   | false    |  false/true  |


Container 类型 Animation\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                     | 描述     | 类型      | 是否必选 | 限制      |
| ------------------ | ---------------------------------------------------------- | -------- | --------- | -------- | --------- |
| Type               | Request.MediaWorkflow.<br>Topology.Nodes.Animation\_\*\*\* | 节点类型 | String    | 是       | Animation |
| Operation          | Request.MediaWorkflow.<br>Topology.Nodes.Animation\_\*\*\* | 操作规则 | Container | 是       | 无        |

Container 类型 Animation\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | ---- | ---- |
| TemplateId         | Request.MediaWorkflow.Topology.<br>Nodes.Animation\_\*\*\*.Operation | 模板 ID   | String    | 是   | 无   |
| Output             | Request.MediaWorkflow.Topology.<br>Nodes.Animation\_\*\*\*.Operation | 输出地址 | Container | 是   | 无   |


Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制                                                         |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | ---- | ------------------------------------------------------------ |
| Region             | Request.MediaWorkflow.Topology.<br>Nodes.Animation\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是   | 无                                                           |
| Bucket             | Request.MediaWorkflow.Topology.<br>Nodes.Animation\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是   | 无                                                           |
| Object             | Request.MediaWorkflow.Topology.<br>Nodes.Animation\_\*\*\*.Operation.Output | 结果文件名称 | String | 是   | 1、bcd/${RunId}/bcd.gif <br/> 2、bcd/${RunId}/bcd.webp <br/> |

Container 类型 Snapshot\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制     |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | -------- |
| Type               | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*\*\*\* | 节点类型 | String    | 是       | Snapshot |
| Operation          | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*\*\*\* | 操作规则 | Container | 是       | 无       |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| TemplateId         | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*.Operation | 模板 ID  | String    | 是       | 无   |
| Output             | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否<br>必选 | 限制                                                         |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | ------------ | ------------------------------------------------------------ |
| Region             | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是           | 无                                                           |
| Bucket             | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是           | 无                                                           |
| Object             | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*.Operation.Output | 结果文件名称 | String | 否           | <li>abc/${RunId}/snapshot-${number}.${Ext}<br/><li>bcd/${RunId}/snapshot-${number}.jpg |
| SpriteObject       | Request.MediaWorkflow.Topology.<br>Nodes.Snapshot\_\*\*\*.Operation.Output | 雪碧图的名称 | String | 否           | <li>abc/${RunId}/snapshot-${number}.jpg<br/><li>bcd/${RunId}/snapshot-${number}.jpg  |

Container 类型 SmartCover_*** 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                  | 描述     | 类型      | 是否必选 | 限制       |
| ------------------ | ------------------------------------------------------- | -------- | --------- | -------- | ---------- |
| Type               | Request.MediaWorkflow.<br>Topology.Nodes.SmartCover_*** | 节点类型 | String    | 是       | SmartCover |
| Operation          | Request.MediaWorkflow.<br>Topology.Nodes.SmartCover_*** | 操作规则 | Container | 是       | 无         |

Container 类型 SmartCover_***.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| Output             | Request.MediaWorkflow.Topology.<br>Nodes.SmartCover_***.Operation | 输出地址 | Container | 是       | 无   |
| SmartCover         | Request.MediaWorkflow.Topology.<br>Nodes.SmartCover_***.Operation | 封面配置      | Container | 否   | 无   |

Container 类型 SmartCover_***.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制                            |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | -------- | ------------------------------- |
| Region             | Request.MediaWorkflow.Topology.<br>Nodes.SmartCover_***.Operation.Output | 存储桶的地域 | String | 是       | 无                              |
| Bucket             | Request.MediaWorkflow.Topology.<br>Nodes.SmartCover_***.Operation.Output | 存储桶的名称 | String | 是       | 无                              |
| Object             | Request.MediaWorkflow.Topology.<br>Nodes.SmartCover_***.Operation.Output | 结果文件名称 | String | 是       | 必须包含 ${Number} ${RunId}参数 |

Container 类型 SmartCover_***.SmartCover 的具体数据类型描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 | 默认值 | 限制 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- | ---- | ---- |
| Format             | Request.Operation.SmartCover | 封面图片类型    | String | 是  | 无 | png、jpg、webp  |
| Width              | Request.Operation.SmartCover | 封面图片宽度    | String | 是  | 无 | 1. 值范围：[128，4096]<br/> 2. 单位：px<br/> |
| Height             | Request.Operation.SmartCover | 封面图片高度    | String | 是  | 无 | 1. 值范围：[128，4096]<br/> 2. 单位：px<br/> |
| Count              | Request.Operation.SmartCover | 封面数量        | String | 否  | 3 | 值范围：[1，10] |
| DeleteDuplicates   | Request.Operation.SmartCover | 封面是否去重    | String | 否  | false | true/false |

Container 类型 Transcode_*** 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述     | 类型      | 是否必选 | 限制      |
| ------------------ | ------------------------------------------------------ | -------- | --------- | -------- | --------- |
| Type               | Request.MediaWorkflow.<br>Topology.Nodes.Transcode_*** | 节点类型 | String    | 是       | Transcode |
| Operation          | Request.MediaWorkflow.<br>Topology.Nodes.Transcode_*** | 操作规则 | Container | 是       | 无        |

Container 类型 Transcode_***.Operation 的具体数据描述如下：

| 节点名称（关键字）  | 父节点                                                       | 描述         | 类型      | 是否必选 | 限制                           |
| ------------------- | ------------------------------------------------------------ | ------------ | --------- | -------- | ------------------------------ |
| TemplateId          | Request.MediaWorkflow.Topology.</br>Nodes.Transcode_***.Operation | 转码模板ID   | String    | 是       | 无                             |
| WatermarkTemplateId | Request.MediaWorkflow.Topology.</br>Nodes.Transcode_***.Operation | 水印模板ID   | String    | 否       | 可以使用多个水印模板，不超过3个 |
| RemoveWatermark       | Request.MediaWorkflow.Topology.</br>Nodes.Transcode\_\*\*\*.Operation | 去除水印参数        | Container | 否   |无|
| Output       | Request.MediaWorkflow.Topology.</br>Nodes.Transcode\_\*\*\*.Operation | 输出地址 | Container | 是   | 无 |

Container 类型 Transcode\_\*\*\*.RemoveWatermark 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述                  | 类型   | 是否必选 | 限制                                 |
| ------------------ | :----------------------------------------------------------- | --------------------- | ------ | -------- | ------------------------------------ |
| Dx                 | Request.MediaWorkflow.Topology.Nodes.<br>Transcode\_\*\*\*.Operation.RemoveWatermark | 距离左上角原点 x 偏移 | string | 是       | 1. 值范围：[0, 4096]<br/>2. 单位：px |
| Dy                 | Request.MediaWorkflow.Topology.Nodes.<br>Transcode\_\*\*\*.Operation.RemoveWatermark | 距离左上角原点 y 偏移 | string | 是       | 1. 值范围：[0, 4096]<br/>2. 单位：px |
| Width              | Request.MediaWorkflow.Topology.Nodes.<br>Transcode\_\*\*\*.Operation.RemoveWatermark | 水印的宽度            | string | 是       | 1. 值范围：(0, 4096]<br/>2. 单位：px |
| Height             | Request.MediaWorkflow.Topology.Nodes.<br>Transcode\_\*\*\*.Operation.RemoveWatermark | 水印的高度            | string | 是       | 1. 值范围：(0, 4096]<br/>2. 单位：px |

Container 类型 Transcode\_\*\*\*.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | -------- | ---- |
| Region             | Request.MediaWorkflow.Topology.Nodes.<br>Transcode\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是       | 无   |
| Bucket             | Request.MediaWorkflow.Topology.Nodes.<br>Transcode\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是       | 无   |
| Object             | Request.MediaWorkflow.Topology.Nodes.<br>Transcode\_\*\*\*.Operation.Output | 结果文件名称 | String | 是       | 无   |

Container 类型 Concat\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                  | 描述     | 类型      | 是否必选 | 限制   |
| ------------------ | ------------------------------------------------------- | -------- | --------- | -------- | ------ |
| Type               | Request.MediaWorkflow.Topology.<br>Nodes.Concat\_\*\*\* | 节点类型 | String    | 是       | Concat |
| Operation          | Request.MediaWorkflow.Topology.<br>Nodes.Concat\_\*\*\* | 操作规则 | Container | 是       | 无     |

Container 类型 Concat\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| TemplateId         | Request.MediaWorkflow.Topology.</br>Nodes.Concat\_\*\*\*.Operation | 模板 ID  | String    | 是       | 无   |
| Output             | Request.MediaWorkflow.Topology.</br>Nodes.Concat\_\*\*\*.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 VoiceSeparate\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                     | 描述     | 类型      | 是否必选 | 限制          |
| ------------------ | ---------------------------------------------------------- | -------- | --------- | -------- | ------------- |
| Type               | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\* | 节点类型 | String    | 是       | VoiceSeparate |
| Operation          | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\* | 操作规则 | Container | 是       | 无            |

Container 类型 VoiceSeparate\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| TemplateId         | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\*.Operation | 模板 ID  | String    | 是       | 无   |
| Output             | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\*.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 VoiceSeparate\_\*\*\*.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述               | 类型   | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------------ | ------ | -------- | ---- |
| Region             | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\*.Operation.Output | 存储桶的地域       | String | 是       | 无   |
| Bucket             | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\*.Operation.Output | 存储桶的名称       | String | 是       | 无   |
| Object             | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\*.Operation.Output | 背景声结果文件名称 | String | 是       | 无   |
| AuObject           | Request.MediaWorkflow.Topology.</br>Nodes.VoiceSeparate\_\*\*\*.Operation.Output | 人声结果文件名称   | String | 是       | 无   |


Container 类型 VideoMontage\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                    | 描述     | 类型      | 是否必选 | 限制         |
| ------------------ | --------------------------------------------------------- | -------- | --------- | -------- | ------------ |
| Type               | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\* | 节点类型 | String    | 是       | VideoMontage |
| Operation          | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\* | 操作规则 | Container | 是       | 无           |

Container 类型 VideoMontage\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| TemplateId         | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation | 模板 ID  | String    | 是       | 无   |
| Output             | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 VideoMontage\_\*\*\*.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | -------- | ---- |
| Region             | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是       | 无   |
| Bucket             | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是       | 无   |
| Object             | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation.Output | 结果文件名称 | String | 是       | 无   |

Container 类型 HlsPackConfig\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                     | 描述     | 类型      | 是否必选 | 限制          |
| ------------------ | ---------------------------------------------------------- | -------- | --------- | -------- | ------------- |
| Type               | Request.MediaWorkflow.Topology.</br>Nodes.HlsPackConfig\_\*\*\* | 节点类型 | String    | 是       | HlsPackConfig |
| Operation          | Request.MediaWorkflow.Topology.</br>Nodes.HlsPackConfig\_\*\*\* | 操作规则 | Container | 是       | 无            |

Container 类型 HlsPackConfig\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| Output             | Request.MediaWorkflow.Topology.</br>Nodes.HlsPackConfig\_\*\*\*.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 HlsPackConfig\_\*\*\*.Operation.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | -------- | ---- |
| Region             | Request.MediaWorkflow.Topology.</br>Nodes.HlsPackConfig\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是       | 无   |
| Bucket             | Request.MediaWorkflow.Topology.</br>Nodes.HlsPackConfig\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是       | 无   |
| Object             | Request.MediaWorkflow.Topology.</br>Nodes.HlsPackConfig\_\*\*\*.Operation.Output | 结果文件名称 | String | 是       | 无   |


Container 类型 VideoStream\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述       | 类型      | 是否必选 | 限制|
| ------------------ | ------- | ------| --------- | ---- | ---- |
| Type       | Request.MediaWorkflow.Topology.</br>Nodes.VideoStream\_\*\*\* | 节点类型 | String    | 是   | VideoStream |
| Operation  | Request.MediaWorkflow.Topology.</br>Nodes.VideoStream\_\*\*\* | 操作规则 | Container | 是   | 无 |

Container 类型 VideoStream\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述       | 类型      | 是否必选 | 限制|
| ------------------ | ------- | ------| --------- | ---- | ---- |
| TemplateId   | Request.MediaWorkflow.Topology.</br>Nodes.VideoStream\_\*\*\*.Operation | 模板 ID  | String    | 是   | 无 |
| Output       | Request.MediaWorkflow.Topology.</br>Nodes.VideoStream\_\*\*\*.Operation | 输出地址 | Container | 是   | 无 |
| WatermarkTemplateId   | Request.MediaWorkflow.Topology.</br>Nodes.VideoStream\_\*\*\*.Operation | 水印模板 ID  | String    | 是   | 可以使用多个水印模板，不超过3个 |
| RemoveWatermark       | Request.MediaWorkflow.Topology.</br>Nodes.VideoStream\_\*\*\*.Operation | 去除水印参数        | Container | 否   |无|

Container 类型 VideoStream\_\*\*\*.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | -------- | ---- |
| Region             | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是       | 无   |
| Bucket             | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是       | 无   |
| Object             | Request.MediaWorkflow.Topology.</br>Nodes.VideoMontage\_\*\*\*.Operation.Output | 结果文件名称 | String | 是       | 无   |

Container 类型 VideoStream\_\*\*\*.RemoveWatermark 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述                  | 类型   | 是否必选 | 限制                                 |
| ------------------ | :----------------------------------------------------------- | --------------------- | ------ | -------- | ------------------------------------ |
| Dx                 | Request.MediaWorkflow.Topology.Nodes.</br>VideoStream\_\*\*\*.Operation.RemoveWatermark | 距离左上角原点 x 偏移 | string | 是       | 1. 值范围：[0, 4096]<br/>2. 单位：px |
| Dy                 | Request.MediaWorkflow.Topology.Nodes.</br>VideoStream\_\*\*\*.Operation.RemoveWatermark | 距离左上角原点 y 偏移 | string | 是       | 1. 值范围：[0, 4096]<br/>2. 单位：px |
| Width              | Request.MediaWorkflow.Topology.Nodes.</br>VideoStream\_\*\*\*.Operation.RemoveWatermark | 宽                    | string | 是       | 1. 值范围：(0, 4096]<br/>2. 单位：px |
| Height             | Request.MediaWorkflow.Topology.Nodes.</br>VideoStream\_\*\*\*.Operation.RemoveWatermark | 高                    | string | 是       | 1. 值范围：(0, 4096]<br/>2. 单位：px |


Container 类型 HlsPack\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                           | 描述     | 类型      | 是否必选 | 限制    |
| ------------------ | ------------------------------------------------ | -------- | --------- | -------- | ------- |
| Type       | Request.MediaWorkflow.Topology.</br>Nodes.HlsPack\_\*\*\* | 节点类型 | String    | 是   | HlsPack |
| Operation          | Request.MediaWorkflow.</br>Topology.Nodes.HlsPack\_\*\*\* | 操作规则 | Container | 是       | 无      |

Container 类型 HlsPack\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                     | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | --------- | ---- | ---- |
| HlsPackInfo        | Request.MediaWorkflow.Topology.</br>Nodes.HlsPack\_\*\*\*.Operation | 打包规则 | Container | 否   | 无   |

Container 类型 HlsPack\_\*\*\*.Operation.HlsPackInfo 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------ | --------- | ---- | ---- |
| VideoStreamConfig  | Request.MediaWorkflow.Topology.</br>Nodes.HlsPack\_\*\*\*.Operation.HlsPackInfo | 视频子流配置 | Container | 否   | 无   |

Container 类型 HlsPack\_\*\*\*.Operation.HlsPackInfo.VideoStreamConfig 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述                                                      | 类型      | 是否必选 | 限制                     |
| ------------------ | ------------------------------------------------------------ | --------------------------------------------------------- | --------- | ---- | ------------------------ |
| VideoStreamName    | Request.MediaWorkflow.Topology.Nodes.</br>HlsPack\_\*\*\*.Operation.HlsPackInfo.VideoStreamConfig | 视频子流名称                                              | Container | 是   | 必须和存在的视频节点对应 |
| BandWidth          | Request.MediaWorkflow.Topology.Nodes.</br>HlsPack\_\*\*\*.Operation.HlsPackInfo.VideoStreamConfig | 视频子流带宽限制，单位b/s，范围[0, 2000000000]，0表示不限制 | Container | 否   | 大于等于0，默认值是0     |


Container 类型 SDRtoHDR\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                            | 描述     | 类型      | 是否必选 | 限制     |
| ------------------ | ------------------------------------------------- | -------- | --------- | ---- | -------- |
| Type               | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\* | 节点类型 | Container | 是   | SDRtoHDR |
| Operation          | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\* | 操作规则 | Container | 是   | 无       |

Container 类型 SDRtoHDR\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字）  | 父节点                                                      | 描述         | 类型      | 是否必选 | 限制                           |
| ------------------- | ----------------------------------------------------------- | ------------ | --------- | ---- | ------------------------------ |
| SDRtoHDR            | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation | SDRtoHDR 配置 | Container | 是   | 无                             |
| TranscodeTemplateId | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation | 转码模板 ID   | String    | 是   | 无                             |
| WatermarkTemplateId | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation | 水印模板 ID   | String    | 否   | 可以使用多个水印模板,不超过3个 |
| Output              | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation | 输出地址     | Container | 是   | 无                             |

Container 类型 SDRtoHDR\_\*\*\*.SDRtoHDR 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述    | 类型   | 是否必选 | 限制                |
| ------------------ | ------------------------------------------------------------ | ------- | ------ | ---- | ------------------- |
| HdrMode            | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation.SDRtoHDR | HDR 标准 | String | 是   | 1. HLG<br/>2. HDR10 |

Container 类型 SDRtoHDR\_\*\*\*.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | ---- | ---- |
| Region             | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是   | 无   |
| Bucket             | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是   | 无   |
| Object             | Request.MediaWorkflow.Topology.</br>Nodes.SDRtoHDR\_\*\*\*.Operation.Output | 结果文件名称 | String | 是   | 无   |



Container 类型 VideoProcess\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                | 描述     | 类型      | 是否必选 | 限制         |
| ------------------ | ----------------------------------------------------- | -------- | --------- | ---- | ------------ |
| Type               | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\* | 节点类型 | String    | 是   | VideoProcess |
| Operation          | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\* | 操作规则 | Container | 是   | 无           |

Container 类型 VideoProcess\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字）  | 父节点                                                       | 描述       | 类型      | 是否必选 | 限制                           |
| ------------------- | ------------------------------------------------------------ | ---------- | --------- | ---- | ------------------------------ |
| TemplateId          | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\*.Operation | 模板 ID     | String    | 是   | 无                             |
| TranscodeTemplateId | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\*.Operation | 转码模板 ID | String    | 是   | 无                             |
| WatermarkTemplateId | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\*.Operation | 水印模板 ID | String    | 否   | 可以使用多个水印模板，不超过3个 |
| Output              | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\*.Operation | 输出地址   | Container | 是   | 无                             |

Container 类型 VideoProcess\_\*\*\*.Operation.Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | ---- | ---- |
| Region             | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是   | 无   |
| Bucket             | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是   | 无   |
| Object             | Request.MediaWorkflow.Topology.</br>Nodes.VideoProcess\_\*\*\*.Operation.Output | 结果文件名称 | String | 是   | 无   |

Container 类型 SCF\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | -------------------------------------------- | -------- | --------- | ---- | ---- |
| Type               | Request.MediaWorkflow.Topology.</br>Nodes.SCF\_\*\*\* | 节点类型 | String    | 是   | SCF  |
| Operation          | Request.MediaWorkflow.Topology.</br>Nodes.SCF\_\*\*\* | 操作规则 | Container | 是   | 无   |

Container 类型 SCF\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------ | ----------- | --------- | ---- | ---- |
| SCF                | Request.MediaWorkflow.Topology.</br>Nodes.SCF\_\*\*\*.Operation | SCF 函数信息 | Container | 是   | 无   |

Container 类型 SCF\_\*\*\*.Operation.SCF 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                     | 描述     | 类型   | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| Region             | Request.MediaWorkflow.Topology.</br>Nodes.SCF\_\*\*\*.Operation.SCF | 函数地域 | String | 是   | 无   |
| FunctionName       | Request.MediaWorkflow.Topology.</br>Nodes.SCF\_\*\*\*.Operation.SCF | 函数名称 | String | 是   | 无   |
| Namespace          | Request.MediaWorkflow.Topology.</br>Nodes.SCF\_\*\*\*.Operation.SCF | 命名空间 | String | 否   | 无   |
| Alias              | Request.MediaWorkflow.Topology.</br>Nodes.SCF\_\*\*\*.Operation.SCF | 函数别名 | String | 否   | 无   |

Container 类型 SuperResolution\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| Type               | Request.MediaWorkflow.<br>Topology.Nodes.SuperResolution\_\*\*\* | 节点类型 | String    | 是 | SuperResolution |
| Operation          | Request.MediaWorkflow.<br>Topology.Nodes.SuperResolution\_\*\*\* | 操作规则 | Container | 是     | 无       |

Container 类型 SuperResolution\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| TemplateId   | Request.MediaWorkflow.Topology.<br>Nodes.SuperResolution\_\*\*\*.Operation | 模板 ID  | String    | 是   | 无 |
| TranscodeTemplateId | Request.MediaWorkflow.Topology..<br>Nodes.SuperResolution\_\*\*\*.Operation | 转码模板 ID  | String    | 是   | 无 |
| WatermarkTemplateId | Request.MediaWorkflow.Topology..<br>Nodes.SuperResolution***.Operation | 水印模板 ID  | String    | 否   | 可以使用多个水印模板，不超过3个 |
| Output       | Request.MediaWorkflow.Topology.<br>Nodes.SuperResolution\_\*\*\*.Operation | 输出地址 | Container | 是   | 无 |


Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| Region             | Request.MediaWorkflow.Topology.<br>Nodes.SuperResolution\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是           | 无                                                     |
| Bucket             | Request.MediaWorkflow.Topology.<br>Nodes.SuperResolution\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是           | 无                                                     |
| Object   | Request.MediaWorkflow.Topology.<br>Nodes.SuperResolution\_\*\*\*.Operation.Output | 结果文件名称  | String  | 是  | 无 |


Container 类型 Segment\_\*\*\* 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| Type               | Request.MediaWorkflow.<br>Topology.Nodes.Segment\_\*\*\* | 节点类型 | String    | 是       | Segment |
| Operation          | Request.MediaWorkflow.<br>Topology.Nodes.Segment\_\*\*\* | 操作规则 | Container | 是       | 无        |

Container 类型 Segment\_\*\*\*.Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| Segment   | Request.MediaWorkflow.Topology.<br>Nodes.Segment\_\*\*\*.Operation | 音视频分段参数  | Container    | 是   | 无 |
| Output   | Request.MediaWorkflow.Topology.<br>Nodes.Segment\_\*\*\*.Operation | 输出地址 | Container | 是   | 无 |

Container 类型 Segment 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| Format            | Request.MediaWorkflow.Topology.<br>Nodes.Segment\_\*\*\*.Operation.Segment | 封装格式 | String | 是  | aac、mp3、flac、mp4、ts、mkv、avi |
| Duration          | Request.MediaWorkflow.Topology.<br>Nodes.Segment\_\*\*\*.Operation.Segment | 分段时长，单位：秒 | String | 是  | 不小于5的整数|

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                 | 描述        | 类型      | 是否必选 | 限制 |
| ------------------ | ---------------------------------------------------------- | -------- | ------ | ---- | ---- |
| Region             | Request.MediaWorkflow.Topology.<br>Nodes.Segment\_\*\*\*.Operation.Output | 存储桶的地域 | String | 是     | 无                                                     |
| Bucket             | Request.MediaWorkflow.Topology.<br>Nodes.Segment\_\*\*\*.Operation.Output | 存储桶的名称 | String | 是     | 无                                                     |
| Object   | Request.MediaWorkflow.Topology.<br>Nodes.Segment\_\*\*\*.Operation.Output | 结果文件名称  | String  | 是  | 必须包含${Number}参数，<br>作为自定义分段后每一小段音/视频流的输出序号 |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

#### 响应体1：音视频转码、极速高清、截帧、转动图、人声分离、精彩集锦、音视频拼接、智能封面、视频增强、SDR to HDR、自定义函数、超分辨率和音视频分段


```plaintext
<Response>
    <MediaWorkflow>
        <Name>demo</Name>
        <State>Active</State>
        <WorkflowId></WorkflowId>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Transcode_1581665960537,Animation_1581665960538,Concat_1581665960539,SmartCover_1581665960539,VoiceSeparate_1581665960551,VideoMontage_1581665960551,SDRtoHDR_1581665960553,VideoProcess_1581665960554,SCF_1581665960566,SuperResolution_1581665960583,Segment_1581665960667</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Transcode_1581665960537>End</Transcode_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Concat_1581665960539>End</Concat_1581665960539>
                <SmartCover_1581665960539>End</SmartCover_1581665960539>
                <VoiceSeparate_1581665960551>End</VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>End</VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>End</SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>End</VideoProcess_1581665960554>
                <SCF_1581665960566>End</SCF_1581665960566>
                <SuperResolution_1581665960583>End</SuperResolution_1581665960583>
                <Segment_1581665960667>End</Segment_1581665960667>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                        <NotifyConfig>
                            <Url>http://www.callback.com</Url>
                            <Event>TaskFinish,WorkflowFinish</Event>
                            <Type>Url</Type>
                        </NotifyConfig>
                        <ExtFilter>
                            <State>on</State>
                            <Audio>true</Audio>
                            <Custom>true</Custom>
                            <CustomExts>mp4/mp3</CustomExts>
                            <AllFile>true</AllFile>
                        </ExtFilter>
                    </Input>
                </Start>
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                        <SmartCover>
                            <Format>png</Format>
                            <Width>128</Width>
                            <Height>128</Height>
                            <Count>3</Count>
                            <DeleteDuplicates>false</DeleteDuplicates>
                        </SmartCover> 
                    </Operation>
                </SmartCover_1581665960539>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                            <SpriteObject>abc/${RunId}/snapshot-${number}.jpg</SpriteObject>                         
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Transcode_1581665960537>
                    <Type>Transcode</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/trans.mp4</Object>
                        </Output>
                    </Operation>
                </Transcode_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Concat_1581665960539>
                    <Type>Concat</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.${ext}</Object>
                        </Output>
                    </Operation>
                </Concat_1581665960539>
                <VoiceSeparate_1581665960551>
                    <Type>VoiceSeparate</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163b164</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <AuObject>bcd/${RunId}/audio.mp3</AuObject>
                            <Object>bcd/${RunId}/background.mp3</Object>
                        </Output>
                    </Operation>
                </VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>
                    <Type>VideoMontage</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba73l9</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/montage.mp4</Object>
                        </Output>
                    </Operation>
                </VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>
                    <Type>SDRtoHDR</Type>
                    <Operation>
                        <SDRtoHDR>
                            <HdrMode>HLG</HdrMode>
                        </SDRtoHDR>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/SDRtoHDR.mp4</Object>
                        </Output>
                    </Operation>
                </SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>
                    <Type>VideoProcess</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55356fshb18</TemplateId>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/videoProcess.mp4</Object>
                        </Output>
                    </Operation>
                </VideoProcess_1581665960554>
                <SCF_1581665960566>
                    <Type>SCF</Type>
                    <Operation>
                        <SCF>
                            <Region>ap-chengdu</Region>
                            <FunctionName>test</FunctionName>
                            <Namespace>testspace</Namespace>
                        </SCF>
                    </Operation>
                </SCF_1581665960566>
                <SuperResolution_1581665960583>
                    <Type>SuperResolution</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}/SuperResolution.mkv</Object>
                        </Output>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <TranscodeTemplateId>t160606b9752148c4absdfaf2f55163b1f</TranscodeTemplateId>
                    </Operation>
                </SuperResolution_1581665960583>
                <Segment_1581665960667>
                    <Type>Segment</Type>
                    <Operation>
                        <Segment>
                            <Format>mp4</Format>
                            <Duration>5</Duration>
                        </Segment>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>test-trans${Number}</Object>
                        </Output>
                    </Operation>
                </Segment_1581665960667>
            </Nodes>
        </Topology>
        <BucketId></BucketId>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflow>
</Response>
```

#### 响应体2：HLS 自适应打包

```
<Response>
    <MediaWorkflow>
        <Name>demo</Name>
        <State>Active</State>
        <WorkflowId></WorkflowId>
        <BucketId></BucketId>
        <Topology>
            <Dependencies>
                <Start>HlsPackConfig_1581665960532</Start>
                <HlsPackConfig_1581665960532>VideoStream_1581665960536,VideoStream_1581665960537</HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>HlsPack</VideoStream_1581665960536>
                <VideoStream_1581665960537>HlsPack</VideoStream_1581665960537>
                <HlsPack_1581665960538>End</HlsPack_1581665960538>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                        <NotifyConfig>
                            <Url>http://www.callback.com</Url>
                            <Event>TaskFinish,WorkflowFinish</Event>
                            <Type>Url</Type>
                        </NotifyConfig>
                        <ExtFilter>
                            <State>on</State>
                            <Audio>true</Audio>
                            <Custom>true</Custom>
                            <CustomExts>mp4/mp3</CustomExts>
                            <AllFile>true</AllFile>
                        </ExtFilter>
                    </Input>
                </Start>
                <HlsPackConfig_1581665960532>
                    <Type>HlsPackConfig</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${InputPath}/${InputName}._${RunId}.${ext}</Object>
                        </Output>
                    </Operation>
                </HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_1/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960536>
                <VideoStream_1581665960537>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606bgfdg2148c4ab182f55163ba7bj</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_2/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960537>
                <HlsPack_1581665960538>
                    <Type>HlsPack</Type>
                    <Operation>
                        <HlsPackInfo>
                            <VideoStreamConfig>
                                <VideoStreamName>VideoStream_1581665960536</VideoStreamName>
                                <BandWidth>0</BandWidth>
                            </VideoStreamConfig>
                            <VideoStreamConfig>
                                <VideoStreamName>VideoStream_1581665960537</VideoStreamName>
                                <BandWidth>0</BandWidth>
                            </VideoStreamConfig>
                        </HlsPackInfo>
                    </Operation>
                </HlsPack_1581665960538>
            </Nodes>
        </Topology>
        <BucketId></BucketId>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflow>
</Response>

```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述         | 类型      |
| :----------------- | :------- | :----------- | :-------- |
| RequestId          | Response | 请求的唯一 ID | String    |
| MediaWorkflow      | Response | 工作流数组   | Container |

Container节点 MediaWorkflow 的内容：

| 节点名称（关键字） | 父节点                 | 描述                                                        | 类型      |
| ------------------ | ---------------------- | ----------------------------------------------------------- | --------- |
| Name               | Response.MediaWorkflow | 工作流名称                                                  | String    |
| WorkflowId         | Response.MediaWorkflow | 工作流 ID                                                    | String    |
| State              | Response.MediaWorkflow | 工作流状态                                                  | String    |
| CreateTime         | Response.MediaWorkflow | 创建时间                                                    | String    |
| UpdateTime         | Response.MediaWorkflow | 更新时间                                                    | String    |
| Topology           | Response.MediaWorkflow | 拓扑信息，同 POST Workflow 中的 Request.MediaWorkflow.Topology | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求1：音视频转码、极速高清、截帧、转动图、人声分离、精彩集锦、智能封面、音视频拼接、自定义函数、超分辨率和音视频分段示例

```plaintext
POST /workflow HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
    <MediaWorkflow>
        <Name>demo</Name>
        <State>Active</State>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Transcode_1581665960537,Animation_1581665960538,Concat_1581665960539,SmartCover_1581665960539,VoiceSeparate_1581665960551,VideoMontage_1581665960551,SDRtoHDR_1581665960553,VideoProcess_1581665960554,SCF_1581665960566,SuperResolution_1581665960583,Segment_1581665960667</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Transcode_1581665960537>End</Transcode_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Concat_1581665960539>End</Concat_1581665960539>
                <SmartCover_1581665960539>End</SmartCover_1581665960539>
                <VoiceSeparate_1581665960551>End</VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>End</VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>End</SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>End</VideoProcess_1581665960554>
                <SCF_1581665960566>End</SCF_1581665960566>
                <SuperResolution_1581665960583>End</SuperResolution_1581665960583>
                <Segment_1581665960667>End</Segment_1581665960667>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                        <NotifyConfig>
                            <Url>http://www.callback.com</Url>
                            <Event>TaskFinish,WorkflowFinish</Event>
                            <Type>Url</Type>
                        </NotifyConfig>
                        <ExtFilter>
                            <State>on</State>
                            <Audio>true</Audio>
                            <Custom>true</Custom>
                            <CustomExts>mp4/mp3</CustomExts>
                            <AllFile>true</AllFile>
                        </ExtFilter>
                    </Input>
                </Start>
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                        <SmartCover>
                            <Format>png</Format>
                            <Width>128</Width>
                            <Height>128</Height>
                            <Count>3</Count>
                            <DeleteDuplicates>false</DeleteDuplicates>
                        </SmartCover> 
                    </Operation>
                </SmartCover_1581665960539>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                            <SpriteObject>abc/${RunId}/snapshot-${number}.jpg</SpriteObject>
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Transcode_1581665960537>
                    <Type>Transcode</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/trans.mp4</Object>
                        </Output>
                    </Operation>
                </Transcode_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Concat_1581665960539>
                    <Type>Concat</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.${ext}</Object>
                        </Output>
                    </Operation>
                </Concat_1581665960539>
                <VoiceSeparate_1581665960551>
                    <Type>VoiceSeparate</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163b164</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <AuObject>bcd/${RunId}/audio.mp3</AuObject>
                            <Object>bcd/${RunId}/background.mp3</Object>
                        </Output>
                    </Operation>
                </VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>
                    <Type>VideoMontage</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba73l9</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/montage.mp4</Object>
                        </Output>
                    </Operation>
                </VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>
                    <Type>SDRtoHDR</Type>
                    <Operation>
                        <SDRtoHDR>
                            <HdrMode>HLG</HdrMode>
                        </SDRtoHDR>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/SDRtoHDR.mp4</Object>
                        </Output>
                    </Operation>
                </SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>
                    <Type>VideoProcess</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55356fshb18</TemplateId>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/videoProcess.mp4</Object>
                        </Output>
                    </Operation>
                </VideoProcess_1581665960554>
                <SCF_1581665960566>
                    <Type>SCF</Type>
                    <Operation>
                        <SCF>
                            <Region>ap-chengdu</Region>
                            <FunctionName>test</FunctionName>
                            <Namespace>testspace</Namespace>
                        </SCF>
                    </Operation>
                </SCF_1581665960566>
                <SuperResolution_1581665960583>
                    <Type>SuperResolution</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}/SuperResolution.mkv</Object>
                        </Output>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <TranscodeTemplateId>t160606b9752148c4absdfaf2f55163b1f</TranscodeTemplateId>
                    </Operation>
                </SuperResolution_1581665960583>
                <Segment_1581665960667>
                    <Type>Segment</Type>
                    <Operation>
                        <Segment>
                            <Format>mp4</Format>
                            <Duration>5</Duration>
                        </Segment>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>test-trans${Number}</Object>
                        </Output>
                    </Operation>
                </Segment_1581665960667>
            </Nodes>
        </Topology>
    </MediaWorkflow>
</Request>
```

#### 响应1

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <MediaWorkflow>
        <Name>demo</Name>
        <State>Active</State>
        <WorkflowId></WorkflowId>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Transcode_1581665960537,Animation_1581665960538,Concat_1581665960539,SmartCover_1581665960539,VoiceSeparate_1581665960551,VideoMontage_1581665960551,SDRtoHDR_1581665960553,VideoProcess_1581665960554,SCF_1581665960566,SuperResolution_1581665960583,Segment_1581665960667</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Transcode_1581665960537>End</Transcode_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Concat_1581665960539>End</Concat_1581665960539>
                <SmartCover_1581665960539>End</SmartCover_1581665960539>
                <VoiceSeparate_1581665960551>End</VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>End</VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>End</SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>End</VideoProcess_1581665960554>
                <SCF_1581665960566>End</SCF_1581665960566>
                <SuperResolution_1581665960583>End</SuperResolution_1581665960583>
                <Segment_1581665960667>End</Segment_1581665960667>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                        <NotifyConfig>
                            <Url>http://www.callback.com</Url>
                            <Event>TaskFinish,WorkflowFinish</Event>
                            <Type>Url</Type>
                        </NotifyConfig>
                        <ExtFilter>
                            <State>on</State>
                            <Audio>true</Audio>
                            <Custom>true</Custom>
                            <CustomExts>mp4/mp3</CustomExts>
                            <AllFile>true</AllFile>
                        </ExtFilter>
                    </Input>
                </Start>
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                        <SmartCover>
                            <Format>png</Format>
                            <Width>128</Width>
                            <Height>128</Height>
                            <Count>3</Count>
                            <DeleteDuplicates>false</DeleteDuplicates>
                        </SmartCover> 
                    </Operation>
                </SmartCover_1581665960539>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                            <SpriteObject>abc/${RunId}/snapshot-${number}.jpg</SpriteObject>
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Transcode_1581665960537>
                    <Type>Transcode</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/trans.mp4</Object>
                        </Output>
                    </Operation>
                </Transcode_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Concat_1581665960539>
                    <Type>Concat</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.${ext}</Object>
                        </Output>
                    </Operation>
                </Concat_1581665960539>
                <VoiceSeparate_1581665960551>
                    <Type>VoiceSeparate</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163b164</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <AuObject>bcd/${RunId}/audio.mp3</AuObject>
                            <Object>bcd/${RunId}/background.mp3</Object>
                        </Output>
                    </Operation>
                </VoiceSeparate_1581665960551>
                <VideoMontage_1581665960551>
                    <Type>VideoMontage</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba73l9</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/montage.mp4</Object>
                        </Output>
                    </Operation>
                </VideoMontage_1581665960551>
                <SDRtoHDR_1581665960553>
                    <Type>SDRtoHDR</Type>
                    <Operation>
                        <SDRtoHDR>
                            <HdrMode>HLG</HdrMode>
                        </SDRtoHDR>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/SDRtoHDR.mp4</Object>
                        </Output>
                    </Operation>
                </SDRtoHDR_1581665960553>
                <VideoProcess_1581665960554>
                    <Type>VideoProcess</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55356fshb18</TemplateId>
                        <TranscodeTemplateId></TranscodeTemplateId>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/videoProcess.mp4</Object>
                        </Output>
                    </Operation>
                </VideoProcess_1581665960554>
                <SCF_1581665960566>
                    <Type>SCF</Type>
                    <Operation>
                        <SCF>
                            <Region>ap-chengdu</Region>
                            <FunctionName>test</FunctionName>
                            <Namespace>testspace</Namespace>
                        </SCF>
                    </Operation>
                </SCF_1581665960566>
                <SuperResolution_1581665960583>
                    <Type>SuperResolution</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}/SuperResolution.mkv</Object>
                        </Output>
                        <WatermarkTemplateId></WatermarkTemplateId>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <TranscodeTemplateId>t160606b9752148c4absdfaf2f55163b1f</TranscodeTemplateId>
                    </Operation>
                </SuperResolution_1581665960583>
                <Segment_1581665960667>
                    <Type>Segment</Type>
                    <Operation>
                        <Segment>
                            <Format>mp4</Format>
                            <Duration>5</Duration>
                        </Segment>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>test-trans${Number}</Object>
                        </Output>
                    </Operation>
                </Segment_1581665960667>
            </Nodes>
        </Topology>
        <BucketId></BucketId>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflow>
</Response>
```


#### 请求2：HLS 自适应打包示例


```plaintext
POST /workflow HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
    <MediaWorkflow>
        <Name>demo</Name>
        <Topology>
            <Dependencies>
                <Start>HlsPackConfig_1581665960532</Start>
                <HlsPackConfig_1581665960532>VideoStream_1581665960536,VideoStream_1581665960537</HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>HlsPack</VideoStream_1581665960536>
                <VideoStream_1581665960537>HlsPack</VideoStream_1581665960537>
                <HlsPack_1581665960538>End</HlsPack_1581665960538>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                    </Input>
                </Start>
                <HlsPackConfig_1581665960532>
                    <Type>HlsPackConfig</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${InputPath}/${InputName}._${RunId}.${ext}</Object>
                        </Output>
                    </Operation>
                </HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_1/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960536>
                <VideoStream_1581665960537>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606bgfdg2148c4ab182f55163ba7bj</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_2/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960537>
                <HlsPack_1581665960538>
                    <Type>HlsPack</Type>
                </HlsPack_1581665960538>
            </Nodes>
        </Topology>
    </MediaWorkflow>
</Request>
```


#### 响应2

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <MediaWorkflow>
        <Name>demo</Name>
        <State>Active</State>
        <WorkflowId></WorkflowId>
        <BucketId></BucketId>
        <Topology>
            <Dependencies>
                <Start>HlsPackConfig_1581665960532</Start>
                <HlsPackConfig_1581665960532>VideoStream_1581665960536,VideoStream_1581665960537</HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>HlsPack</VideoStream_1581665960536>
                <VideoStream_1581665960537>HlsPack</VideoStream_1581665960537>
                <HlsPack_1581665960538>End</HlsPack_1581665960538>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                        <NotifyConfig>
                            <Url>http://www.callback.com</Url>
                            <Event>TaskFinish,WorkflowFinish</Event>
                            <Type>Url</Type>
                        </NotifyConfig>
                        <ExtFilter>
                            <State>on</State>
                            <Audio>true</Audio>
                            <Custom>true</Custom>
                            <CustomExts>mp4/mp3</CustomExts>
                            <AllFile>true</AllFile>
                        </ExtFilter>
                    </Input>
                </Start>
                <HlsPackConfig_1581665960532>
                    <Type>HlsPackConfig</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${InputPath}/${InputName}._${RunId}.${ext}</Object>
                        </Output>
                    </Operation>
                </HlsPackConfig_1581665960532>
                <VideoStream_1581665960536>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_1/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960536>
                <VideoStream_1581665960537>
                    <Type>VideoStream</Type>
                    <Operation>
                        <TemplateId>t1460606bgfdg2148c4ab182f55163ba7bj</TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>${RunId}_Substream_2/video.m3u8</Object>
                        </Output>
                    </Operation>
                </VideoStream_1581665960537>
                <HlsPack_1581665960538>
                    <Type>HlsPack</Type>
                    <Operation>
                        <HlsPackInfo>
                            <VideoStreamConfig>
                                <VideoStreamName>VideoStream_1581665960536</VideoStreamName>
                                <BandWidth>0</BandWidth>
                            </VideoStreamConfig>
                            <VideoStreamConfig>
                                <VideoStreamName>VideoStream_1581665960537</VideoStreamName>
                                <BandWidth>0</BandWidth>
                            </VideoStreamConfig>
                        </HlsPackInfo>
                    </Operation>
                </HlsPack_1581665960538>
            </Nodes>
        </Topology>
        <BucketId></BucketId>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflow>
</Response>
```

