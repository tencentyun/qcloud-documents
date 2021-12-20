## 功能描述
CreateMediaTemplate 用于新增动图模板。

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
POST /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
   <Tag>Animation</Tag>
   <Name>TemplateName</Name>
   <Container>
      <Format>gif</Format>
   </Container>
   <Video>
      <Codec>gif</Codec>
      <Width>1280</Width>
      <Height></Height>
      <Fps>15</Fps>
      <AnimateOnlyKeepKeyFrame>true</AnimateOnlyKeepKeyFrame>
   </Video>
   <TimeInterval>
      <Start>0</Start>
      <Duration>60</Duration>
   </TimeInterval>
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 模板类型：Animation                                    | String    | 是   |
| Name               | Request | 模板名称仅支持中文、英文、数字、\_、\-和\*                    | String    | 是   |
| Container          | Request | 容器格式                                               | Container | 是   |
| Video              | Request | 视频信息                                               | Container | 否   |
| TimeInterval       | Request | 时间区间                                               | Container | 否   |


Request 节点 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Format                | Request.Container | 容器格式：gif，hgif，webp  hgif 为高质量 gif，即清晰度比较高的 gif 格式图 | String    | 是   |

Request 节点 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 是否必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Request.Video | 编解码格式            | String | 是   |  无  | gif, webp                                          |
| Width                      | Request.Video | 宽                    | String | 否   | 视频原<br/>始宽度 | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Width 时，按照视频原始比例计算 Height</li> |
| Height                     | Request.Video | 高                    | String | 否   | 视频原<br/>始高度 | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Height 时，按照视频原始比例计算 Width</li> |
| Fps                        | Request.Video | 帧率                  | String | 否   | 视频原<br/>始帧率 | <li>值范围：(0，60]</li><li>单位：fps</li><li>如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率</li> |
| AnimateOnly<br/>KeepKeyFrame    | Request.Video | 动图只保留<br/>关键帧 。若 AnimateOnlyKeepKeyFrame 设置为 true 时，则不考虑 AnimateTimeIntervalOfFrame、AnimateFramesPerSecond；若 AnimateOnlyKeepKeyFrame 设置为 false 时，则必须填写AnimateTimeIntervalOfFrame 或 AnimateFramesPerSecond     | String | 否   |      false        | <li>true、false</li><li>动图保留关键帧参数 </li> <li>优先级：AnimateFramesPerSecond > AnimateOnlyKeepKeyFrame > AnimateTimeIntervalOfFrame</li>               |
| AnimateTime<br/>IntervalOfFrame | Request.Video | 动图抽帧间<br/>隔时间      | String | 否   |      无        | <li>（0，视频时长]</li><li>动图抽帧时间间隔</li><li>若设置 TimeInterval.Duration，则小于该值</li> |
| AnimateFrames<br/>PerSecond     | Request.Video | Animation 每秒<br/>抽帧帧数 | String | 否   |     无         | <li>（0，视频帧率)</li><li>动图抽帧频率</li><li>优先级：AnimateFramesPerSecond >  AnimateOnlyKeepKeyFrame  > AnimateTimeIntervalOfFrame</li> |
| Quality                    | Request.Video | 设置相对质量          | String | 否   |     无         | <li>[1, 100)</li><li>webp 图像质量设定生效，gif 没有质量参数</li> |


Request 节点 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | Request.TimeInterval | 开始时间 | String    | 否   | 0 |<li> [0 视频时长] </li> <li>单位为秒 </li> <li>支持 float 格式，执行精度精确到毫秒</li> |
| Duration             | Request.TimeInterval | 持续时间 | String    | 否   | 视频时长 | <li> [0 视频时长] </li><li>单位为秒 </li> <li>支持 float 格式，执行精度精确到毫秒</li> |


## 响应

#### 响应头

该响应包含公共响应头，详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Name>TemplateName</Name>
        <TemplateId></TemplateId>
        <Tag>Animation</Tag>
        <TransTpl>
            <Container>
                <Format>gif</Format>
            </Container>
            <Video>
                <Codec>gif</Codec>
                <Width>1280</Width>
                <Height></Height>
                <Fps>15</Fps>
                <AnimateOnlyKeepKeyFrame>true</AnimateOnlyKeepKeyFrame>
            </Video>
            <TimeInterval>
                <Start>0</Start>
                <Duration>60</Duration>
            </TimeInterval>
        </TransTpl>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Response的具体描述：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response | 模板 ID                                                      | String    |
| Name               | Response | 模板名字                                                     | String    |
| BucketId           | Response | 模板所属存储桶                                                | String    |
| Category           | Response | 模板属性，Custom 或者 Official                                | String    |
| Tag                | Response | 模板 Tag Animation                                           | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| TransTpl           | Response | 详细的模板参数                                                | Container |


TransTpl 节点 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Format                | Response.TransTpl.Container | 容器格式： gif，hgif，webp  hgif 为高质量 gif，即清晰度比较高的 gif 格式图 | String    | 是   |

TransTpl 节点 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 是否必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Response.<br/>TransTpl.Video | 编解码格式            | String | 是   |  无  |  gif, webp                                          |
| Width                      | Response.<br/>TransTpl.Video | 宽                    | String | 否   | 视频原始宽度 | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Width 时，按照视频原始比例计算 Height</li> |
| Height                     | Response.<br/>TransTpl.Video | 高                    | String | 否   | 视频原始高度 | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Height 时，按照视频原始比例计算Width </li>|
| Fps                        | Response.<br/>TransTpl.Video | 帧率                  | String | 否   | 视频原始帧率 | <li>值范围：(0，60]</li><li>单位：fps</li><li>帧率超过60时，设置为60<br/>用户可以设置 fps，如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率</li> |
| AnimateOnly<br/>KeepKeyFrame    | Response.<br/>TransTpl.Video | 动图只保留关键帧      | String | 否   |      false        | <li>true、false<br/><li>动图保留关键帧参数                     |
| AnimateTime<br/>IntervalOfFrame | Response.<br/>TransTpl.Video | 动图抽帧间隔时间      | String | 否   |      无        | <li>（0，视频时长]</li><li>动图抽帧时间间隔</li><li> 若设置 TimeInterval.Duration，则小于该值 </li>|
| AnimateFrames<br/>PerSecond     | Response.<br/>TransTpl.Video | Animation 每秒抽帧帧数 | String | 否   |     无         | <li>（0，视频帧率)</li><li>动图抽帧频率</li><li> 优先级：AnimateFramesPerSecond >  AnimateOnlyKeepKeyFrame  > AnimateTimeIntervalOfFrame </li>|
| Quality                    | Response.<br/>TransTpl.Video | 设置相对质量          | String | 否   |     无         | <li>[1, 100)</li><li>webp 图像质量设定生效，gif 没有质量参数</li> |


TransTpl 节点 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | Response.TransTpl.TimeInterval | 开始时间 | String    | 否   | 0 | <li> [0 视频时长]</li> <li>单位为秒</li><li>支持 float 格式，执行精度精确到毫秒</li> |
| Duration             | Response.TransTpl.TimeInterval | 持续时间 | String    | 否   | 视频时长 | <li>[0 视频时长] </li><li>单位为秒 </li><li>支持 float 格式，执行精度精确到毫秒</li> |


#### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml



<Request>
   <Tag>Animation</Tag>
   <Name>TemplateName</Name>
   <Container>
      <Format>gif</Format>
   </Container>
   <Video>
      <Codec>gif</Codec>
      <Width>1280</Width>
      <Height></Height>
      <Fps>15</Fps>
      <AnimateOnlyKeepKeyFrame>true</AnimateOnlyKeepKeyFrame>
   </Video>
   <TimeInterval>
      <Start>0</Start>
      <Duration>60</Duration>
   </TimeInterval>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYz****=



<Response>
    <Template>
        <Name>TemplateName</Name>
        <TemplateId></TemplateId>
        <Tag>Animation</Tag>
        <TransTpl>
            <Container>
                <Format>gif</Format>
            </Container>
            <Video>
                <Codec>gif</Codec>
                <Width>1280</Width>
                <Height></Height>
                <Fps>15</Fps>
                <AnimateOnlyKeepKeyFrame>true</AnimateOnlyKeepKeyFrame>
            </Video>
            <TimeInterval>
                <Start>0</Start>
                <Duration>60</Duration>
            </TimeInterval>
        </TransTpl>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
