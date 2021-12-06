## 功能描述
CreateMediaTemplate 用于新增拼接模板。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateConcatTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


## 请求

#### 请求实例

```shell
POST /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。


#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
   <Tag>Concat</Tag>
   <Name>TemplateName</Name>
   <ConcatTemplate>
        <ConcatFragment>
            <Mode>Start</Mode>
            <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
        </ConcatFragment>
        <ConcatFragment>
            <Mode>End</Mode>
            <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
        </ConcatFragment>
        <Audio>
            <Codec>mp3</Codec>
            <Samplerate></Samplerate>
            <Bitrate></Bitrate>
            <Channels></Channels>
        </Audio>
        <Video>
            <Codec>H.264</Codec>
            <Bitrate>1000</Bitrate>
            <Width>1280</Width>
            <Height></Height>
            <Fps>30</Fps>
        </Video>
        <Container>
            <Format>mp4</Format>
        </Container>
   </ConcatTemplate>
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 模板类型：Concat                                   | String    | 是   |
| Name               | Request | 模板名称仅支持中文、英文、数字、\_、-和\*                     | String    | 是   |
| ConcatTemplate     | Request | 拼接模板                                                | Container | 是   |


Container 类型 ConcatTemplate 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| ConcatFragment      | Request.ConcatTemplate | 拼接节点    | Container    | 是   | 无  | 无 |
| Audio               | Request.ConcatTemplate | 音频参数    | Container    | 否   | 媒体原始值  | 目标文件不需要 Audio 信息，</br>需要设置 Audio.Remove 为 true |
| Video               | Request.ConcatTemplate | 视频参数    | Container    | 否   | 媒体原始值  | 目标文件不需要 Video 信息，</br>需要设置 Video.Remove 为 true |
| Container           | Request.ConcatTemplate | 封装格式    | Container    | 是   | 无  | 无 |


Container 类型 ConcatFragment 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Url                 | Request.ConcatTemplate.ConcatFragment | 拼接对象地址（需要 Urlencode 后传入）  | String    | 是   | 无   | 同 bucket 对象文件 |
| Mode                | Request.ConcatTemplate.<br/>ConcatFragment | 节点类型      | String    | 是   | 无   | <li>Start：开头 </br><li>End：结尾 |


Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Codec              | Request.ConcatTemplate.<br/>Audio | 编解码格式     | String | 是   | 文件原编码    | 取值 aac、mp3                                                |
| Samplerate         | Request.ConcatTemplate.<br/>Audio | 采样率         | String | 否   | 文件原采样率  | <li>单位：Hz<br/><li>可选 11025、22050、32000、44100、48000、96000<br/><li>不同的封装，mp3 支持不同的采样率，如下表所示|
| Bitrate            | Request.ConcatTemplate.<br/>Audio | 音频码率   | String | 否   | 文件原音频码率   | <li>单位：Kbps<br/><li>值范围：[8，1000]                       |
| Channels           | Request.ConcatTemplate.<br/>Audio | 声道数         | String | 否   | 文件原声道数      | <li>当 Codec 设置为 aac，支持1、2、4、5、6、8<br/><li>当 Codec 设置为 mp3，支持1、2 |

Y 表示支持这种采样率，N 表示不支持

| 封装格式/音频采样率| 	11025  | 	22050| 	 32000 | 	44100|  	48000|   	96000 |
| ------------------ | ------- | ------- | ------- | ------- |------------| ------------- |
| mp3     | Y       | 	Y| 	Y| 	Y| 	Y| 	N|

Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | ---------------------------------------------------- | --------- | ---- |
| Format                | Request.ConcatTemplate.<br/>Container | 容器格式：mp4，flv，hls，ts, mp3, aac   | String    | 是   |

Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Request.ConcatTemplate.<br/>Video | 编解码格式             | String | 是   |   H.264 | H.264                                          |
| Width                      | Request.ConcatTemplate.<br/>Video | 宽                    | String | 否   | 视频原始宽度 | <li>值范围：[128，4096]<br/><li>单位：px<br/><li>若只设置 Width 时，按照视频原始比例计算 Height |
| Height                     | Request.ConcatTemplate.<br/>Video | 高                    | String | 否   | 视频原始高度 | <li>值范围：[128，4096]<br/><li>单位：px<br/><li>若只设置 Height 时，按照视频原始比例计算 Width |
| Fps                        | Request.ConcatTemplate.<br/>Video | 帧率                  | String | 否   | 视频原始帧率 | <li>值范围：(0，60]<br><li>单位：fps |
| Bitrate                    | Request.ConcatTemplate.<br/>Video | 视频输出文件的码率      | String | 否   |  视频原始码率           | <li>值范围：[10，50000]<br/><li>单位：Kbps    </li>                 |
| Crf                        | Request.ConcatTemplate.Video | 码率-质量控制因子     | String | 否   | 无           | 1. 值范围：(0, 51]<br/>2. 如果设置了 Crf，则 Bitrate 的设置失效<br/>3. 当 Bitrate 为空时，默认为25 |
| Remove                     | Request.ConcatTemplate.<br/>Video | 是否删除视频流         | String | 否   | false        | 取值 true、false

## 响应


#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Tag>Concat</Tag>
        <Name>TemplateName</Name>
        <ConcatTemplate>
            <ConcatFragment>
                <Mode>Start</Mode>
                <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
            </ConcatFragment>
            <ConcatFragment>
                <Mode>End</Mode>
                <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
            </ConcatFragment>
            <Audio>
                <Codec>mp3</Codec>
                <Samplerate></Samplerate>
                <Bitrate></Bitrate>
                <Channels></Channels>
            </Audio>
            <Video>
                <Codec>H.264</Codec>
                <Bitrate>1000</Bitrate>
                <Width>1280</Width>
                <Height></Height>
                <Fps>30</Fps>
            </Video>
            <Container>
                <Format>mp4</Format>
            </Container>
        </ConcatTemplate>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |


Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                           | 类型      |
| :----------------- | :------- | :----------------------------- | :-------- |
| TemplateId         | Response | 模板 ID                                                | String    |
| TotalCount         | Response | 模版总数                                               | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber                           | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize                             | Int       |
| ConcatTemplate     | Response | 拼接信息，详情请见同页面请求体 ConcatTemplate 的具体数据描述  | Container |



#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98****-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml



<Request>
   <Tag>Concat</Tag>
   <Name>TemplateName</Name>
   <ConcatTemplate>
        <ConcatFragment>
            <Mode>Start</Mode>
            <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
        </ConcatFragment>
        <ConcatFragment>
            <Mode>End</Mode>
            <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
        </ConcatFragment>
        <Audio>
            <Codec>mp3</Codec>
            <Samplerate></Samplerate>
            <Bitrate></Bitrate>
            <Channels></Channels>
        </Audio>
        <Video>
            <Codec>H.264</Codec>
            <Bitrate>1000</Bitrate>
            <Width>1280</Width>
            <Height></Height>
            <Fps>30</Fps>
        </Video>
        <Container>
            <Format>mp4</Format>
        </Container>
   </ConcatTemplate>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=



<Response>
    <Template>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Tag>Concat</Tag>
        <Name>TemplateName</Name>
        <ConcatTemplate>
            <ConcatFragment>
                <Mode>Start</Mode>
                <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
            </ConcatFragment>
            <ConcatFragment>
                <Mode>End</Mode>
                <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
            </ConcatFragment>
            <Audio>
                <Codec>mp3</Codec>
                <Samplerate></Samplerate>
                <Bitrate></Bitrate>
                <Channels></Channels>
            </Audio>
            <Video>
                <Codec>H.264</Codec>
                <Bitrate>1000</Bitrate>
                <Width>1280</Width>
                <Height></Height>
                <Fps>30</Fps>
            </Video>
            <Container>
                <Format>mp4</Format>
            </Container>
        </ConcatTemplate>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```