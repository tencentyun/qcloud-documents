## 功能描述
CreateMediaTemplate 用于新增人声分离模板。

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

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>VoiceSeparate</Tag>
    <Name>TemplateName</Name>
    <AudioMode>IsAudio</AudioMode>
    <AudioConfig>
        <Codec>aac</Codec>
        <Samplerate>44100</Samplerate>
        <Bitrate>128</Bitrate>
        <Channels>4</Channels>
    </AudioConfig>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | ----------------------------------------------------- | --------- | ---- | ---- |
| Tag                | Request | 模板类型: VoiceSeparate                                | String    | 是   | 无 |
| Name               | Request | 模板名称 仅支持中文、英文、数字、\_、\-和\*                    | String    | 是   | 无 |
| AudioMode          | Request | 输出音频                                               | String    | 是   | IsAudio：输出人声<br/>IsBackground：输出背景声<br/>AudioAndBackground：输出人声和背景声 |
| AudioConfig        | Request | 音频配置                                         | Container | 是   |  无|

Container 类型 AudioConfig 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ------------- | -------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| Codec              | Request.Audio | 编解码格式     | String | 否   | aac    | 取值 aac、mp3、flac、amr                                                |
| Samplerate         | Request.Audio | 采样率         | String | 否   | 44100  | 1. 单位：Hz<br/>2. 可选 8000、11025、22050、32000、44100、48000、96000<br/>3. 当 Codec 设置为 aac/flac 时，不支持8000<br/>4. 当 Codec 设置为 mp3 时，不支持8000和96000<br/>5. 当 Codec 设置为 amr 时，只支持8000|
| Bitrate            | Request.Audio | 原始音频码率   | String | 否   | 无      | 1. 单位：Kbps<br/>2. 值范围：[8，1000]
| Channels           | Request.Audio | 声道数         | String | 否   | 无      | 1. 当 Codec 设置为 aac/flac，支持1、2、4、5、6、8<br/>2. 当 Codec 设置为 mp3，支持1、2 <br/>3. 当 Codec 设置为 amr，只支持1|


## 响应
#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>VoiceSeparate</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <VoiceSeparate>
            <AudioMode>IsAudio</AudioMode>
            <AudioConfig>
                <Codec>mp3</Codec>
                <Samplerate>44100</Samplerate>
                <Bitrate>12</Bitrate>
                <Channels>2</Channels>
            </AudioConfig>
        </VoiceSeparate>
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

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response.Template | 模板 ID                                                      | String    |
| Name               | Response.Template | 模板名称                                                     | String    |
| BucketId           | Response.Template | 模板所属存储桶                                                | String    |
| Category           | Response.Template | 模板属性，Custom 或者 Official                                | String    |
| Tag                | Response.Template | 模板类型，VoiceSeparate                                       | String    |
| UpdateTime         | Response.Template | 更新时间                                                     | String    |
| CreateTime         | Response.Template | 创建时间                                                     | String    |
| VoiceSeparate      | Response.Template | 详细的模板参数                                                | Container |


Container 节点 VoiceSeparate 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                    | 类型      |
| :----------------- | :----------------------------- | :------------------------------------ | :-------- |
| AudioMode          | Response.Template.VoiceSeparate | 同请求体中的 Request.AudioMode          | String |
| AudioConfig        | Response.Template.VoiceSeparate | 同请求体中的 Request.AudioConfig        | Container |


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Tag>VoiceSeparate</Tag>
    <Name>TemplateName</Name>
    <AudioMode>IsAudio</AudioMode>
    <AudioConfig>
        <Codec>aac</Codec>
        <Samplerate>44100</Samplerate>
        <Bitrate>128</Bitrate>
        <Channels>4</Channels>
    </AudioConfig>
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
    <Template>
        <Tag>VoiceSeparate</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <VoiceSeparate>
            <AudioMode>IsAudio</AudioMode>
            <AudioConfig>
                <Codec>mp3</Codec>
                <Samplerate>44100</Samplerate>
                <Bitrate>12</Bitrate>
                <Channels>2</Channels>
            </AudioConfig>
        </VoiceSeparate>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
