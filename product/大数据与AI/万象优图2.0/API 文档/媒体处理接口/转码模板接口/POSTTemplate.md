## 功能描述

CreateMediaTemplate 接口用于新增转码模板。

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

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```shell
<Request>
   <Tag>Animation</Tag>
   <Name>Template Name</Name>
   <Container>
      <Format>gif</Format>
   </Container>
   <Video>
      <Codec>GIF</Codec>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Fps>1-60</Fps>
      <Remove>false</Remove>
   </Video>
   <TimeInterval>
      <Start></Start>
      <Duration></Duration>
   </TimeInterval>
</Request>

<Request>
   <Tag>Snapshot</Tag>
   <Name>Template Name</Name>
   <Snapshot>
      <Mode>Interval</Mode>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Start></Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
   </Snapshot>
</Request>
```

具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>Request</td>
      <td>无</td>
      <td>保存请求的容器</td>
      <td>Container</td>
      <td>是</td>
   </tr>
</table>

Container 类型 Request 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Tag</td>
      <td>Request</td>
      <td>模板类型 Animation，Snapshot</td>
      <td>String</td>
      <td>是</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>Name</td>
      <td>Request</td>
      <td>模板名称</td>
      <td>String</td>
      <td>是</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>Container</td>
      <td>Request</td>
      <td>容器格式</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
   <tr>
      <td>Video</td>
      <td>Request</td>
      <td>视频信息</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
   <tr>
      <td>TimeInterval</td>
      <td>Request</td>
      <td>转码时间区间</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
   <tr>
      <td>Snapshot</td>
      <td>Request</td>
      <td>截图</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
</table>

Container 类型 Container 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>默认值</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Format</td>
      <td>Request.Container</td>
      <td>容器格式</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
       gif，hgif，webp。其中 hgif 为高质量 gif，即清晰度比较高的 gif 格式图<br>
      </td>
   </tr>
</table>

Container 类型 Video 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>默认值</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Codec</td>
      <td>Request.Video</td>
      <td>编解码格式</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        GIF、WEBP
      </td>
   </tr>
   <tr>
      <td>Width</td>
      <td>Request.Video</td>
      <td>宽</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始宽度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px<br>
        3. 若只设置 Width 时，按照视频原始比例计算 Height
      </td>
   </tr>
   <tr>
      <td>Height</td>
      <td>Request.Video</td>
      <td>高</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始高度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px<br>
        3. 若只设置 Height 时，按照视频原始比例计算 Width
      </td>
   </tr>
   <tr>
      <td>Fps</td>
      <td>Request.Video</td>
      <td>帧率</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始帧率</td>
      <td>
        1. 值范围：(0，60]<br>
        2. 单位：fps<br>
        3. 帧率超过60时，设置为60<br>
        4. 用户可以设置 fps，如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率
      </td>
   </tr>
   <tr>
      <td>Remove</td>
      <td>Request.Video</td>
      <td>是否删除视频流</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td>
       true、false
      </td>
   </tr>
   <tr>
      <td>AnimateOnlyKeepKeyFrame</td>
      <td>Request.Video</td>
      <td>动图只保留关键帧</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1. true、false<br>
        2. 动图保留关键帧参数
      </td>
   </tr>
   <tr>
      <td>AnimateTimeIntervalOfFrame</td>
      <td>Request.Video</td>
      <td>动图抽帧间隔时间</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1. （0，视频时长]<br>
        2. 动图抽帧时间间隔<br>
        3. 若设置 TimeInterval.Duration，则小于该值<br>
      </td>
   </tr>
   <tr>
      <td>AnimateFramesPerSecond</td>
      <td>Request.Video</td>
      <td>Animation 每秒抽帧帧数</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1.（0，视频帧率)<br>
        2. 动图抽帧频率<br>
        3. 优先级：AnimateFramesPerSecond >  AnimateOnlyKeepKeyFrame  > AnimateTimeIntervalOfFrame<br>
      </td>
   </tr>
   <tr>
      <td>Quality</td>
      <td>Request.Video</td>
      <td>设置相对质量</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
       1. [1, 100)<br>
       2. webp 图像质量设定生效，gif 没有质量参数
      </td>
   </tr>
</table>

Container 类型 TimeInterval 的具体数据描述如下：

<table width="100%">
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>默认值</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Start</td>
      <td>Request.TimeInterval</td>
      <td>开始时间</td>
      <td>String</td>
      <td>否</td>
      <td>0</td>
      <td>
        1. [0 视频时长] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
   <tr>
      <td>Duration</td>
      <td>Request.TimeInterval</td>
      <td>持续时间</td>
      <td>String</td>
      <td>否</td>
      <td>视频时长</td>
      <td>
        1. (0 视频时长] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
</table>

Container 类型 Snapshot 的具体数据描述如下：

<table width="100%">
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>默认值</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Start</td>
      <td>Request.Snapshot</td>
      <td>开始时间</td>
      <td>String</td>
      <td>是</td>
      <td>无</td>
      <td>
        1. [0 视频时长] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
   <tr>
      <td>TimeInterval</td>
      <td>Request.Snapshot</td>
      <td>截图频率</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1. (0 3600] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
   <tr>
      <td>Count</td>
      <td>Request.Snapshot</td>
      <td>截图数量</td>
      <td>String</td>
      <td>是</td>
      <td>无</td>
      <td>
        (0 10000] <br>
      </td>
   </tr>
   <tr>
      <td>Width</td>
      <td>Request.Snapshot</td>
      <td>宽</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始宽度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px<br>
        3. 若只设置 Width 时，按照视频原始比例计算 Height<br>
      </td>
   </tr>
   <tr>
      <td>Height</td>
      <td>Request.Snapshot</td>
      <td>高</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始高度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px<br>
        3. 若只设置 Height 时，按照视频原始比例计算 Width<br>
      </td>
   </tr>
   <tr>
      <td>Mode</td>
      <td>Request.Snapshot</td>
      <td>截屏模式</td>
      <td>String</td>
      <td>否</td>
      <td>Interval</td>
      <td>
        1. 值范围：{Interval, Average}<br>
        2. Interval 表示间隔模式 Average 表示平均模式<br>
        3. Interval 模式：Start，TimeInterval，Count 参数生效。当设置 Count，未设置 TimeInterval 时，表示截取所有帧，共 Count 张图片<br>
        4. Average 模式：Start，Count 参数生效。表示从 Start 开始到视频结束，按平均间隔截取共 Count 张图片
      </td>
   </tr>
</table>



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Name>Template Name</Name>
    <TemplateID></TemplateID>
    <Tag>Animation</Tag>
    <TransTpl>
      <Container>
         <Format>mp4</Format>
      </Container>
      <Video>
         <Codec>GIF</Codec>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Remove>false</Remove>
      </Video>
      <TimeInterval>
         <Start></Start>
         <Duration></Duration>
      </TimeInterval>
   </TransTpl>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型      |
| :----------------- | :----- | :----------------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器，同 DescribeMediaTemplates 中的 Response.TemplateList | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

### 截帧示例

#### 请求

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Name>Template Name</Name>
    <Tag>Animation</Tag>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>GIF</Codec>
        <Width>128-4096</Width>
        <Height>128-4096</Height>
        <Fps>1-60</Fps>
        <Remove>false</Remove>
    </Video>
    <TimeInterval>
        <Start></Start>
        <Duration></Duration>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <Tag>Animation</Tag>
    <Name>Template Name</Name>
    <TemplateID></TemplateID>
    <TransTpl>
      <Container>
         <Format>mp4</Format>
      </Container>
      <Video>
         <Codec>GIF</Codec>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Remove>false</Remove>
      </Video>
      <TimeInterval>
         <Start></Start>
         <Duration></Duration>
      </TimeInterval>
   </TransTpl>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>
```

### 视频转动图示例

#### 请求

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
   <Tag>Snapshot</Tag>
   <Name>Template Name</Name>
   <Snapshot>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Start></Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
   </Snapshot>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
   <Tag>Snapshot</Tag>
   <Name>Template Name</Name>
   <TemplateID></TemplateID>
   <Snapshot>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Start></Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
   </Snapshot>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>
```
