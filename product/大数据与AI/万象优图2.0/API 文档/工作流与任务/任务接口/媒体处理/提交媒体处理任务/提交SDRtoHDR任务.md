## 功能描述

提交一个 SDR to HDR 任务。

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
POST /jobs HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>SDRtoHDR</Tag>
    <Input>
        <Object>input/demo.mp4</Object>
    </Input>
    <Operation>
        <SDRtoHDR>
            <HdrMode>HLG</HdrMode>
        </SDRtoHDR>
        <TranscodeTemplateId>t160606b9752148c4absdfaf2f55163b1f</TranscodeTemplateId>
        <WatermarkTemplateId>t146d70eb241c44c63b6efc1cc93ccfc5d</WatermarkTemplateId>
        <WatermarkTemplateId>t12a74d11687d444deba8a6cc52051ac27</WatermarkTemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/out.mp4</Object>
        </Output>
        <UserData>This is my data.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
    <CallBack>http://callback.demo.com</CallBack>
    <CallBackFormat>JSON<CallBackFormat>
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | -------- |
| Request            | 无     | 保存请求的容器 | Container | 是       |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                    | 类型      | 是否必选 |
| ------------------ | ------- | ------------------------------------------------------- | --------- | -------- |
| Tag                | Request | 创建任务的 Tag：SDRtoHDR                                | String    | 是       |
| Input              | Request | 待操作的媒体信息                                        | Container | 是       |
| Operation          | Request | 操作规则                                                | Container | 是       |
| QueueId            | Request | 任务所在的队列 ID                                       | String    | 是       |
| CallBackFormat     | Request | 任务回调格式，JSON 或 XML，默认 XML，优先级高于队列的回调格式                    | String | 否 |
| CallBackType       | Request | 任务回调类型，Url 或 TDMQ，默认 Url，优先级高于队列的回调类型                    | String | 否 |
| CallBack           | Request | 任务回调地址，优先级高于队列的回调地址。设置为 no 时，表示队列的回调地址不产生回调 | String | 否 |
| CallBackMqConfig   | Request | 任务回调 TDMQ 配置，当 CallBackType 为 TDMQ 时必填。详情见 [CallBackMqConfig](https://cloud.tencent.com/document/product/460/78927#CallBackMqConfig)                | Container | 否 |


Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述       | 类型   | 是否必选 |
| ------------------ | ------------- | ---------- | ------ | -------- |
| Object             | Request.Input | 媒体文件名 | String | 是       |

<span id="operation"></span>
Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字）  | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------- | ----------------- | ------------------------------------------------------------ | --------- | -------- |
| SDRtoHDR            | Request.Operation | 指定 SDRtoHDR 参数                                           | Container | 是       |
| Transcode           | Request.Operation | 指定转码模板参数，不能与 TranscodeTemplateId 同时为空          | Container | 否       |
| TranscodeTemplateId | Request.Operation | 指定的转码模板 ID，优先使用模板 ID，不能与 Transcode 同时为空   | String    | 否       |
| Watermark           | Request.Operation | 指定水印模板参数，同创建水印模板 <a href="https://cloud.tencent.com/document/product/460/77099#Watermark" target="_blank">CreateMediaTemplate</a> 接口中的 Request.Watermark, 最多传3个 | Container 数组 | 否       |
| WatermarkTemplateId | Request.Operation | 指定的水印模板 ID，可以传多个水印模板 ID，最多传3个，优先使用模板 ID | String 数组    | 否       |
| Output              | Request.Operation | 结果输出地址                                                 | Container | 是       |
| UserData            | Request.Operation | 透传用户信息, 可打印的 ASCII 码, 长度不超过1024                                           | String | 否 |
| JobLevel             | Request.Operation | 任务优先级，级别限制：0 、1 、2。级别越大任务优先级越高，默认为0 | String | 否   |


>? 提交 SDRtoHDR 任务必须传入转码参数。对于转码参数，优先使用 TranscodeTemplateId，无 TranscodeTemplateId 时使用 Transcode；对于水印参数，可以使用 WatermarkTemplateId 或Watermark 设置，WatermarkTemplateId 优先级更高。
>

Container 类型 SDRtoHDR 的具体数据描述如下：

| 节点名称（关键字） | 父节点                     | 描述     | 类型   | 是否必选 | 限制                |
| ------------------ | :------------------------- | -------- | ------ | -------- | ------------------- |
| HdrMode            | Request.Operation.SDRtoHDR | HDR 标准 | String | 是       | 1. HLG<br/>2. HDR10 |

Container 类型 Transcode 的具体数据描述如下：

| 节点名称（关键字） | 父节点                            | 描述                                                         | 类型   | 必选 |
| ------------------ | :------------------------------ | ------------------------------------------------------------ | ------ | ---- |
| TimeInterval       | Request.Operation.Transcode     | 同创建转码模板 <a href="https://cloud.tencent.com/document/product/460/77093#TimeInterval " target="_blank">CreateMediaTemplate</a> 接口中的 Request.TimeInterval | Container | 否 | 
| Container          | Request.Operation.Transcode     | 同创建转码模板 <a href="https://cloud.tencent.com/document/product/460/77093#Container " target="_blank">CreateMediaTemplate</a> 接口中的 Request.Container    | Container | 否 | 
| Video              | Request.Operation.Transcode     | 同创建转码模板 <a href="https://cloud.tencent.com/document/product/460/77093#Video " target="_blank">CreateMediaTemplate</a> 接口中的 Request.Video        | Container | 否 |
| Audio              | Request.Operation.Transcode     | 同创建转码模板 <a href="https://cloud.tencent.com/document/product/460/77093#Audio " target="_blank">CreateMediaTemplate</a> 接口中的 Request.Audio        | Container | 否 |
| TransConfig        | Request.Operation.Transcode     | 同创建转码模板 <a href="https://cloud.tencent.com/document/product/460/77093#TransConfig " target="_blank">CreateMediaTemplate</a> 接口中的 Request.TransConfig  | Container | 否 |
| AudioMix           | Request.Operation.Transcode     | 混音参数, 详情见<a href="https://cloud.tencent.com/document/product/460/78927#AudioMix" target="_blank">AudioMix</a>  | Container 数组 | 否 |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述             | 类型   | 是否必选 |
| ------------------ | ------------------------ | ---------------- | ------ | -------- |
| Region             | Request.Operation.Output | 存储桶的地域     | String | 是       |
| Bucket             | Request.Operation.Output | 存储结果的存储桶 | String | 是       |
| Object             | Request.Operation.Output | 输出结果的文件名 | String | 是       |



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j229ed9e2f60c11ec8525e36307395bf9</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T14:44:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Tag>SDRtoHDR</Tag>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <TranscodeTemplateId>t1460606b9752148c4ab182f55163ba7cd</TranscodeTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe22</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe23</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe24</WatermarkTemplateId>
            <SDRtoHDR>
                <HdrMode>HDR10</HdrMode>
            </SDRtoHDR>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/out.mp4</Object>
            </Output>
            <UserData>This is my data.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述           | 类型      |
| :----------------- | :------- | :------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息 | Container |

<span id="jobsDetail"></span>
Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                                         | 类型      |
| :----------------- | :------------------ | :----------------------------------------------------------- | :-------- |
| Code               | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义                        | String    |
| Message            | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义                      | String    |
| JobId              | Response.JobsDetail | 新创建任务的 ID                                              | String    |
| Tag                | Response.JobsDetail | 新创建任务的 Tag：SDRtoHDR                                   | String    |
| State              | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 | String    |
| CreationTime       | Response.JobsDetail | 任务的创建时间                                               | String    |
| StartTime          | Response.JobsDetail | 任务的开始时间                                               | String    |
| EndTime            | Response.JobsDetail | 任务的结束时间                                               | String    |
| QueueId            | Response.JobsDetail | 任务所属的队列 ID                                            | String    |
| Input              | Response.JobsDetail | 该任务的输入资源地址                                         | Container |
| Operation          | Response.JobsDetail | 该任务的规则                                                 | Container |

Container 节点 Input 的内容：

| 节点名称（关键字） | 父节点                   | 描述             | 类型   |
| ------------------ | ------------------------ | ---------------- | ------ |
| Region             | Response.JobsDetail.Input | 存储桶的地域     | String |
| Bucket             | Response.JobsDetail.Input | 存储结果的存储桶 | String |
| Object             | Response.JobsDetail.Input | 输出结果的文件名 | String |

Container 节点 Operation 的内容：

| 节点名称（关键字） | 父节点                        | 描述                                  | 类型      |
| :----------------- | :---------------------------- | :------------------------------------ | :-------- |
| SDRtoHDR           | Response.JobsDetail.Operation | 同请求中的 Request.Operation.SDRtoHDR | Container |
| Output             | Response.JobsDetail.Operation | 同请求中的 Request.Operation.Output   | Container |
| MediaInfo          | Response.JobsDetail.Operation | 输出文件的媒体信息，任务未完成时不返回 | Container |
| MediaResult        | Response.JobsDetail.Operation | 输出文件的基本信息，任务未完成时不返回 | Container |
| UserData           | Response.JobsDetail.Operation | 透传用户信息                      | String |
| JobLevel           | Response.JobsDetail.Operation | 任务优先级                                                   | String |

Container 节点 MediaInfo 的内容：
同 [GenerateMediaInfo](https://cloud.tencent.com/document/product/460/38935) 接口中的 Response.MediaInfo 节点。

Container 节点 MediaResult 的内容：

| 节点名称（关键字） | 父节点                              | 描述                                                         | 类型   |
| ------------------ | :---------------------------------- | ------------------------------------------------------------ | ------ |
| OutputFile         | Response.Operation.MediaResult | 输出文件的基本信息 | Container |

Container 节点 OutputFile 的内容：

| 节点名称（关键字） | 父节点                              | 描述                                                         | 类型   |
| ------------------ | :---------------------------------- | ------------------------------------------------------------ | ------ |
| Bucket             | Response.Operation.MediaResult.OutputFile | 输出文件所在的存储桶           | String |
| Region             | Response.Operation.MediaResult.OutputFile | 输出文件所在的存储桶所在的园区  | String |
| ObjectName         | Response.Operation.MediaResult.OutputFile | 输出文件名，可能有多个         | String 数组 |
| Md5Info            | Response.Operation.MediaResult.OutputFile | 输出文件的 MD5 信息 | Container 数组 |

Container 节点 Md5Info 的内容：

| 节点名称（关键字） | 父节点                              | 描述                                                         | 类型   |
| ------------------ | :---------------------------------- | ------------------------------------------------------------ | ------ |
| ObjectName         | Response.Operation.MediaResult.OutputFile.Md5Info | 输出文件名          | String |
| Md5                | Response.Operation.MediaResult.OutputFile.Md5Info  | 输出文件的 MD5 值    | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
POST /jobs HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
    <Tag>SDRtoHDR</Tag>
    <Input>
        <Object>input/demo.mp4</Object>
    </Input>
    <Operation>
        <SDRtoHDR>
            <HdrMode>HLG</HdrMode>
        </SDRtoHDR>
        <TranscodeTemplateId>t160606b9752148c4absdfaf2f55163b1f</TranscodeTemplateId>
        <WatermarkTemplateId>t146d70eb241c44c63b6efc1cc93ccfc5d</WatermarkTemplateId>
        <WatermarkTemplateId>t12a74d11687d444deba8a6cc52051ac27</WatermarkTemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/out.mp4</Object>
        </Output>
        <UserData>This is my data.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
    <CallBack>http://callback.demo.com</CallBack>
    <CallBackFormat>JSON<CallBackFormat>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Mon, 28 Jun 2022 15:23:12 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j229ed9e2f60c11ec8525e36307395bf9</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T15:23:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Tag>SDRtoHDR</Tag>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <TranscodeTemplateId>t1460606b9752148c4ab182f55163ba7cd</TranscodeTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe22</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe23</WatermarkTemplateId>
            <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe24</WatermarkTemplateId>
            <SDRtoHDR>
                <HdrMode>HDR10</HdrMode>
            </SDRtoHDR>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/out.mp4</Object>
            </Output>
            <UserData>This is my data.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
</Response>
```
