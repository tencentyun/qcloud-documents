## 功能描述

UpdateMediaTemplate 接口用于更新转码模板。

## 请求

#### 请求示例

```shell
PUT /template/<TemplateID> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

> ?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>Animation</Tag>
    <Name>Template Name</Name>
    <TemplateID></TemplateID>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>GIF</Codec>
        <Profile>high</Profile>
        <Bitrate>10-50000</Bitrate>
        <Crf>0-51</Crf>
        <Width>128-4096</Width>
        <Height>128-4096</Height>
        <Fps>1-60</Fps>
        <Gop>1-100000</Gop>
        <Preset>fast</Preset>
        <ScanMode>interlaced</ScanMode>
        <Bufsize>1000-128000</Bufsize>
        <Maxrate>10-50000</Maxrate>
        <PixFmt>yuv420p</PixFmt>
        <Remove>false</Remove>
        <Crop>border</Crop>
        <Pad></Pad>
        <LongShortMode>false</LongShortMode>
    </Video>
    <TimeInterval>
        <Start></Start>
        <Duration></Duration>
    </TimeInterval>
</Request>

<Request>
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
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述                                                | 类型      | 必选 |
| :----------------- | :----- | :-------------------------------------------------- | :-------- | ---- |
| Request            | 无     | 保存请求的容器，同 CreateMediaTemplate 中的 Request | Container | 是   |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
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
         <Profile>high</Profile>
         <Bitrate>10-50000</Bitrate>
         <Crf>0-51</Crf>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Gop>1-100000</Gop>
         <Preset>fast</Preset>
         <ScanMode>interlaced</ScanMode>
         <Bufsize>1000-128000</Bufsize>
         <Maxrate>10-50000</Maxrate>
         <PixFmt>yuv420p</PixFmt>
         <Remove>false</Remove>
         <Crop>border</Crop>
         <Pad></Pad>
         <LongShortMode>false</LongShortMode>
      </Video>
      <TimeInterval>
         <Start></Start>
         <Duration></Duration>
      </TimeInterval>
   </TransTpl>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>

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

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                 | 类型      |
| :----------------- | :----- | :--------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器，同 CreateMediaTemplate 中的 Response | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
PUT /template/<TemplateID> HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Tag>Animation</Tag>
    <Name>Template Name</Name>
    <TemplateID></TemplateID>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>GIF</Codec>
        <Profile>high</Profile>
        <Bitrate>10-50000</Bitrate>
        <Crf>0-51</Crf>
        <Width>128-4096</Width>
        <Height>128-4096</Height>
        <Fps>1-60</Fps>
        <Gop>1-100000</Gop>
        <Preset>fast</Preset>
        <ScanMode>interlaced</ScanMode>
        <Bufsize>1000-128000</Bufsize>
        <Maxrate>10-50000</Maxrate>
        <PixFmt>yuv420p</PixFmt>
        <Remove>false</Remove>
        <Crop>border</Crop>
        <Pad></Pad>
        <LongShortMode>false</LongShortMode>
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
         <Profile>high</Profile>
         <Bitrate>10-50000</Bitrate>
         <Crf>0-51</Crf>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Gop>1-100000</Gop>
         <Preset>fast</Preset>
         <ScanMode>interlaced</ScanMode>
         <Bufsize>1000-128000</Bufsize>
         <Maxrate>10-50000</Maxrate>
         <PixFmt>yuv420p</PixFmt>
         <Remove>false</Remove>
         <Crop>border</Crop>
         <Pad></Pad>
         <LongShortMode>false</LongShortMode>
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
