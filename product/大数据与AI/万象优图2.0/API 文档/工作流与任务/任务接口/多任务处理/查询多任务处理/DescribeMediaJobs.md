## 功能描述

DescribeMediaJobs 用于拉取符合条件的任务。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateAnimationTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>



## 请求

#### 请求示例

```shell
GET /jobs?size=&states=&queueId=&startCreationTime=&endCreationTime= HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型    | 是否必选 |
| :----------------- | :----- | :----------------------------------------------------------- | :------ | :------- |
| queueId            | 无     | 拉取该队列 ID 下的任务                                       | String  | 是       |
| tag                | 无     | 任务的 Tag                                                  | String  | 是       |
| orderByTime        | 无     | Desc 或者 Asc。默认为 Desc                                   | String  | 否       |
| nextToken          | 无     | 请求的上下文，用于翻页。上次返回的值                         | String  | 否       |
| size               | 无     | 拉取的最大任务数。默认为10。最大为100                        | Integer | 否       |
| states             | 无     | 拉取该状态的任务，以`,`分割，支持多状态：All、Submitted、Running、Success、Failed、Pause、Cancel。默认为 All | String  | 否       |
| startCreationTime  | 无     | 拉取创建时间大于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`，示例：2001-01-01T00:00:00+0800 | String  | 否 |
| endCreationTime    | 无     | 拉取创建时间小于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`，示例：2001-01-01T23:59:59+0800 | String  | 否 |

tag 支持以下几种类型:

| 任务类型 | tag |
| :----------------- | :----- |
| 音视频转码          | Transcode |
| 视频转动图          | Animation |
| 视频截图            | Snapshot |
| 智能封面            | SmartCover |
| 音视频拼接          | Concat |
| 人声分离            | VoiceSeparate |
| 精彩集锦            | VideoMontage |
| SDR to HDR         | SDRtoHDR |
| 视频增强            | VideoProcess |
| 超级分辨率          | SuperResolution |
| 音视频转封装        | Segment |
| 数字水印            | DigitalWatermark |
| 提取数字水印        | ExtractDigitalWatermark |
| 视频标签            | VideoTag |
| 获取媒体信息         | MediaInfo |
| 音视频流分离         | StreamExtract |
| 视频质量分析         | QualityEstimate |
| 语音合成            | Tts |
| 音频降噪            | NoiseReduction |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <JobsDetail>
        ...
    </JobsDetail>
    <NextToken></NextToken>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                                                         | 类型      |
| :----------------- | :------- | :----------------------------------------------------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息                                               | Container 数组 |
| NextToken          | Response | 翻页的上下文 Token                                            | String    |

对于不同的任务类型，JobsDetail 的内容不同，请参照以下链接：
- <a href="https://cloud.tencent.com/document/product/460/76913#jobsDetail" target="_blank">音视频转码</a>
- <a href="https://cloud.tencent.com/document/product/460/76900#jobsDetail" target="_blank">视频转动图</a>
- <a href="https://cloud.tencent.com/document/product/460/76910#jobsDetail" target="_blank">视频截帧</a>
- <a href="https://cloud.tencent.com/document/product/460/76909#jobsDetail" target="_blank">智能封面</a>
- <a href="https://cloud.tencent.com/document/product/460/76901#jobsDetail" target="_blank">音视频拼接</a>
- <a href="https://cloud.tencent.com/document/product/460/76918#jobsDetail" target="_blank">人声分离</a>
- <a href="https://cloud.tencent.com/document/product/460/76915#jobsDetail" target="_blank">精彩集锦</a>
- <a href="https://cloud.tencent.com/document/product/460/76907#jobsDetail" target="_blank">SDR to HDR</a>
- <a href="https://cloud.tencent.com/document/product/460/76916#jobsDetail" target="_blank">视频增强</a>
- <a href="https://cloud.tencent.com/document/product/460/76912#jobsDetail" target="_blank">超分辨率</a>
- <a href="https://cloud.tencent.com/document/product/460/76908#jobsDetail" target="_blank">音视频转封装</a>
- <a href="https://cloud.tencent.com/document/product/460/76902#jobsDetail" target="_blank">数字水印</a>
- <a href="https://cloud.tencent.com/document/product/460/76903#jobsDetail" target="_blank">提取数字水印</a>
- <a href="https://cloud.tencent.com/document/product/460/76917#jobsDetail" target="_blank">视频标签</a>
- <a href="https://cloud.tencent.com/document/product/460/76904#jobsDetail" target="_blank">获取媒体信息</a>
- <a href="https://cloud.tencent.com/document/product/460/76911#jobsDetail" target="_blank">音视频流分离</a>
- <a href="https://cloud.tencent.com/document/product/460/76906#jobsDetail" target="_blank">视频质量分析</a>
- <a href="https://cloud.tencent.com/document/product/460/76914#jobsDetail" target="_blank">语音合成</a>
- <a href="https://cloud.tencent.com/document/product/460/76905#jobsDetail" target="_blank">音频降噪</a>


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
GET /jobs?queueId=p2242ab62c7c94486915508540933a2c6&tag=Transcode HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Mon, 28 Jun 2022 15:23:12 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=

<Response>
    <JobsDetail>
        <Code>Success</Code>
        </Message>
        <JobId>j8d121820f5e411ec926ef19d53ba9c6f</JobId>
        <State>Running</State>
        <Progress>30</Progress>
        <CreationTime>2022-06-27T15:23:12+0800</CreationTime>
        <StartTime>2022-06-27T15:23:13+0800</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Tag>Transcode</Tag>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe22</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe23</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe24</WatermarkTemplateId>
            <RemoveWatermark>
                <Dx>150</Dx>
                <Dy>150</Dy>
                <Width>75</Width>
                <Height>75</Height>
            </RemoveWatermark>
            <DigitalWatermark>
                <Type>Text</Type>
                <Message>123456789ab</Message>
                <Version>V1</Version>
                <IgnoreError>false</IgnoreError>
                <State>Running</State>
            </DigitalWatermark>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/out.mp4</Object>
            </Output>
            <UserData>This is my data.</UserData>
        </Operation>
    </JobsDetail>
    <JobsDetail>
        <Code>Success</Code>
        </Message>
        <JobId>j9c0a4726f6ac11ec96aaa9b64ab18d00</JobId>
        <State>Success</State>
        <Progress>100</Progress>
        <CreationTime>2022-06-27T15:23:12+0800</CreationTime>
        <StartTime>2022-06-27T15:23:13+0800</StartTime>
        <EndTime>2022-06-27T15:24:33+0800</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Tag>Transcode</Tag>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe22</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe23</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe24</WatermarkTemplateId>
            <RemoveWatermark>
                <Dx>150</Dx>
                <Dy>150</Dy>
                <Width>75</Width>
                <Height>75</Height>
            </RemoveWatermark>
            <DigitalWatermark>
                <Type>Text</Type>
                <Message>123456789ab</Message>
                <Version>V1</Version>
                <IgnoreError>false</IgnoreError>
                <State>Running</State>
            </DigitalWatermark>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/out.mp4</Object>
            </Output>
            <UserData>This is my data.</UserData>
            <MediaInfo>
                <Format>
                    <Bitrate>834.736000</Bitrate>
                    <Duration>13.654000</Duration>
                    <FormatLongName>QuickTime / MOV</FormatLongName>
                    <FormatName>mov,mp4,m4a,3gp,3g2,mj2</FormatName>
                    <NumProgram>0</NumProgram>
                    <NumStream>2</NumStream>
                    <Size>1424687</Size>
                    <StartTime>0.000000</StartTime>
                </Format>
                <Stream>
                    <Audio>
                        <Bitrate>104.047000</Bitrate>
                        <Channel>2</Channel>
                        <ChannelLayout>stereo</ChannelLayout>
                        <CodecLongName>AAC (Advanced Audio Coding)</CodecLongName>
                        <CodecName>aac</CodecName>
                        <CodecTag>0x6134706d</CodecTag>
                        <CodecTagString>mp4a</CodecTagString>
                        <CodecTimeBase>1/44100</CodecTimeBase>
                        <Duration>13.653311</Duration>
                        <Index>1</Index>
                        <Language>und</Language>
                        <SampleFmt>fltp</SampleFmt>
                        <SampleRate>44100</SampleRate>
                        <StartTime>0.000000</StartTime>
                        <Timebase>1/44100</Timebase>
                    </Audio>
                    <Subtitle/>
                    <Video>
                        <AvgFps>25.000000</AvgFps>
                        <Bitrate>763.774000</Bitrate>
                        <CodecLongName>H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10</CodecLongName>
                        <CodecName>h264</CodecName>
                        <CodecTag>0x31637661</CodecTag>
                        <CodecTagString>avc1</CodecTagString>
                        <CodecTimeBase>1/12800</CodecTimeBase>
                        <ColorPrimaries>bt470bg</ColorPrimaries>
                        <ColorRange>tv</ColorRange>
                        <ColorTransfer>smpte170m</ColorTransfer>
                        <Duration>12.960000</Duration>
                        <Fps>25.000000</Fps>
                        <HasBFrame>0</HasBFrame>
                        <Height>960</Height>
                        <Index>0</Index>
                        <Language>und</Language>
                        <Level>10</Level>
                        <NumFrames>324</NumFrames>
                        <PixFormat>yuv420p</PixFormat>
                        <Profile>High</Profile>
                        <RefFrames>1</RefFrames>
                        <Rotation>0.000000</Rotation>
                        <StartTime>0.000000</StartTime>
                        <Timebase>1/12800</Timebase>
                        <Width>544</Width>
                    </Video>
                </Stream>
            </MediaInfo>
            <MediaResult>
                <OutputFile>
                    <Bucket>test-123456789</Bucket>
                    <Region>ap-chongqing</Region>
                    <ObjectName>output/out.mp4</ObjectName>
                    <Md5Info>
                            <Md5>3df1f845d2ffd20a525a93ec40014d90</Md5>
                            <ObjectName>output/out.mp4</ObjectName>
                    </Md5Info>
                </OutputFile>
            </MediaResult>
        </Operation>
    </JobsDetail>
    <NextToken>225508</NextToken>
</Response>
```

