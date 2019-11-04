## 功能描述
搜索指定状态的自定义模板。

## 请求
#### 请求示例

```shell
GET /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml
<body>
```

>?Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体
该请求的请求体为空。

#### 请求参数

<table>
   <tr>
      <th nowrap="nowrap">名称	</th>
      <th>类型</th>
      <th>描述</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>ids</td>
      <td>string</td>
      <td>模板 ID，以“,”符号分割字符串</td>
      <td>否</td>
   </tr>
   <tr>
      <td>name</td>
      <td>string</td>
      <td>模板名称前缀</td>
      <td>否</td>
   </tr>
   <tr>
      <td>tag</td>
      <td>string</td>
      <td>模板 Tag。如 Snapshot，Animation</td>
      <td>是</td>
   </tr>
   <tr>
      <td>category</td>
      <td>string</td>
      <td>Official 或者 Custom，默认值：Custom</td>
      <td>否</td>
   </tr>
   <tr>
      <td>pageNumber</td>
      <td>string</td>
      <td>第几页</td>
      <td>否</td>
   </tr>
   <tr>
      <td>pageSize</td>
      <td>string</td>
      <td>每页个数</td>
      <td>否</td>
   </tr>
</table>


## 响应
#### 响应头
此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。 

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>017F1B2D-2B5B-4441-ABBA-E0DC08F5AFEC</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <Template>
            <TemplateID>A</TemplateID>
            <Name>Template Name</Name>
            <Tag>Animation</Tag>
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
                <Audio>
                    <Codec>AAC</Codec>
                    <Profile>aac_he</Profile>
                    <Samplerate>44100</Samplerate>
                    <Bitrate>8</Bitrate>
                    <Channels>2</Channels>
                    <Remove>false</Remove>
                </Audio>
                <TransConfig>
                    <TransMode>onepass</TransMode>
                    <IsCheckReso>true</IsCheckReso>
                    <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
                    <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
                </TransConfig>
                <TimeInterval>
                    <Start></Start>
                    <Duration></Duration>
                </TimeInterval>
            </TransTpl>
            <CreateTime></CreateTime>
            <UpdateTime></UpdateTime>
        </Template>
    </TemplateList>
</Response>
```

#### 错误码
该请求操作可能会出现如下错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

错误码|描述|HTTP 状态码
---|---|---
InternalErrror|服务端内部错误|500 Internal Server
AccessDenied|签名或者权限不正确，拒绝访问|403 Forbidden

## 实际案例

### 获取模板列表
#### 请求

```shell
GET /template?templateIds=A,B,C HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <RequestId>017F1B2D-2B5B-4441-ABBA-E0DC08F5AFEC</RequestId>
    <TemplateList>
        <TemplateID>A</TemplateID>
        <Name>Template Name</Name>
        <Tag>Animation</Tag>
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
            <Audio>
                <Codec>AAC</Codec>
                <Profile>aac_he</Profile>
                <Samplerate>44100</Samplerate>
                <Bitrate>8</Bitrate>
                <Channels>2</Channels>
                <Remove>false</Remove>
            </Audio>
            <TransConfig>
                <TransMode>onepass</TransMode>
                <IsCheckReso>true</IsCheckReso>
                <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
                <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
            </TransConfig>
            <TimeInterval>
                <Start></Start>
                <Duration></Duration>
            </TimeInterval>
        </TransTpl>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </TemplateList>
    <NonExistTIDs>
        <TemplateID>B</TemplateID>
        <TemplateID>C</TemplateID>
    </NonExistTIDs>
</Response>
```

### 获取特定模板信息

#### 请求

```shell
GET /template?page_size=10&page_number=1 HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <RequestId>017F1B2D-2B5B-4441-ABBA-E0DC08F5AFEC</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <TemplateID>A</TemplateID>
        <Name>Template Name</Name>
        <Tag>Animation</Tag>
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
            <Audio>
                <Codec>AAC</Codec>
                <Profile>aac_he</Profile>
                <Samplerate>44100</Samplerate>
                <Bitrate>8</Bitrate>
                <Channels>2</Channels>
                <Remove>false</Remove>
            </Audio>
            <TransConfig>
                <TransMode>onepass</TransMode>
                <IsCheckReso>true</IsCheckReso>
                <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
                <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
            </TransConfig>
            <TimeInterval>
                <Start></Start>
                <Duration></Duration>
            </TimeInterval>
        </TransTpl>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </TemplateList>
    <TemplateList>
        <TemplateID>A</TemplateID>
        <Name>Template Name</Name>
        <Tag>Animation</Tag>
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
            <Audio>
                <Codec>AAC</Codec>
                <Profile>aac_he</Profile>
                <Samplerate>44100</Samplerate>
                <Bitrate>8</Bitrate>
                <Channels>2</Channels>
                <Remove>false</Remove>
            </Audio>
            <TransConfig>
                <TransMode>onepass</TransMode>
                <IsCheckReso>true</IsCheckReso>
                <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
                <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
            </TransConfig>
            <TimeInterval>
                <Start></Start>
                <Duration></Duration>
            </TimeInterval>
        </TransTpl>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </TemplateList>
</Response>
```
