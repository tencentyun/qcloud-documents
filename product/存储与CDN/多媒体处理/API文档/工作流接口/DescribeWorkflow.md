## 功能描述

DescribeWorkflow 接口用于搜索工作流。

## 请求

#### 请求示例

```shell
GET /workflow HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数

| 参数名称（关键字） | 描述                         | 类型   | 是否必选 |
| :----------------- | :--------------------------- | :----- | :------- |
| ids                | 工作流 ID，以`,`符号分割字符串 | string | 否       |
| name               | 工作流名称                   | string | 否       |
| pageNumber         | 第几页                       | string | 否       |
| pageSize           | 每页个数                     | string | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <MediaWorkflowList>
        <Name>demo</Name>
        <WorkflowId></WorkflowId>
        <State></State>
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
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflowList>
    <MediaWorkflowList>
        <Name>demo</Name>
        <State>Active</State>
        <WorkflowId></WorkflowId>
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
    </MediaWorkflowList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                            | 类型      |
| :----------------- | :------- | :------------------------------ | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 工作流总数                      | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| MediaWorkflowList  | Response | 工作流数组                      | Container |

Container节点 MediaWorkflowList 的内容：

| 节点名称（关键字） | 父节点                     | 描述       | 类型      | 是否必选 | 限制                                                 |
| ------------------ | -------------------------- | ---------- | --------- | -------- | ---------------------------------------------------- |
| Name               | Response.MediaWorkflowList | 工作流名称 | String    | 是       | 支持中文、英文、数字、—和\_，长度限制128字符          |
| WorkflowId         | Response.MediaWorkflowList | 工作流 ID  | String    | 是       | 工作流唯一 ID                                        |
| State              | Response.MediaWorkflowList | 工作流状态 | String    | 是       | 1. Active <br/>2. Paused<br/>                        |
| CreateTime         | Response.MediaWorkflowList | 创建时间   | String    | 是       | 无                                                   |
| UpdateTime         | Response.MediaWorkflowList | 更新时间   | String    | 是       | 无                                                   |
| Topology           | Response.MediaWorkflowList | 拓扑信息   | Container | 是       | 同 POST Workflow 中的 Request.MediaWorkflow.Topology |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求1：工作流 ID

```shell
GET /workflow?ids=demo,demo1 HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml
```

#### 响应1

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <MediaWorkflowList>
        <Name>demo</Name>
        <WorkflowId></WorkflowId>
        <State></State>
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
                            <Object>bcd/${RunId}/trans-${number}.mp4</Object>
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
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflowList>
</Response>
```

#### 请求2：工作流列表

```shell
GET /workflow?pageNumber=1&pageSize=1 HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml
```

#### 响应2

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>11</PageSize>
    <MediaWorkflowList>
        <Name>demo</Name>
        <WorkflowId></WorkflowId>
        <State></State>
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
                            <Object>bcd/${RunId}/trans-${number}.mp4</Object>
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
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflowList>
    <MediaWorkflowList>
        <Name>demo</Name>
        <State>Active</State>
        <WorkflowId></WorkflowId>
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
    </MediaWorkflowList>
</Response>
```
