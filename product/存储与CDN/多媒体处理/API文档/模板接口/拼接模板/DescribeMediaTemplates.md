## 功能描述
DescribeMediaTemplates 用于搜索拼接模板。

## 请求

#### 请求实例

```shell
GET /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。


#### 请求体
该请求的请求体为空。

#### 请求参数
参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| tag           | 无        | 模板 Tag：Concat     | String    |是|
| ids           | 无        | 模板 ID，以`,`符号分割字符串  | String     |否|
| name          | 无        | 模板名称前缀              | String     |否|
| pageNumber    | 无        | 第几页                   | Integer     |否|
| pageSize      | 无        | 每页个数                 | Integer     |否|


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。


#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
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
    </TemplateList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                           | 类型      |
| :----------------- | :------- | :----------------------------- | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 模版总数                       | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| TemplateList       | Response | 模版数组                       | Container |

Container节点TemplateList的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response.TemplateList | 模版 ID                                                      | String    |
| Name               | Response.TemplateList | 模版名字                                                     | String    |
| BucketId           | Response.TemplateList | 模版所属存储桶                                                | String    |
| Category           | Response.TemplateList | 模版属性，Custom                                             | String    |
| Tag                | Response.TemplateList | 模版类型，Concat                                          | String    |
| UpdateTime         | Response.TemplateList | 更新时间                                                     | String    |
| CreateTime         | Response.TemplateList | 创建时间                                                     | String    |
| ConcatTemplate     | Response.TemplateList | 水印信息                 | Container |


Container 类型 ConcatTemplate 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| ConcatFragment      | Response.TemplateList.<br/>ConcatTemplate | 拼接节点    | Container    | 是   | 无  | 无 |
| Audio               | Response.TemplateList.<br/>ConcatTemplate | 基准位置    | String    | 是   | 无  | 无 |
| Video               | Response.TemplateList.<br/>ConcatTemplate | 视频参数    | Container    | 是   | 无  | 无 |
| Container           | Response.TemplateList.<br/>ConcatTemplate | 封装格式    | Container    | 是   | 无  | 无 |

Container 类型 ConcatFragment 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Url                 | Response.TemplateList.<br/>ConcatTemplate.ConcatFragment | 拼接对象地址   | String    | 是   | 无   | 同 bucket 对象文件 |
| Mode                | Response.TemplateList.<br/>ConcatTemplate.ConcatFragment | 节点类型      | String    | 是   | 无   |<li>Start：开头 </br><li>End：结尾 |


Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Codec              | Response.TemplateList.<br/>ConcatTemplate.Audio | 编解码格式     | String | 否   | aac    | 取值 aac、mp3                                                |
| Samplerate         | Response.TemplateList.<br/>ConcatTemplate.Audio | 采样率         | String | 否   | 44100  |<li>单位：Hz<br/><li>可选 11025、22050、32000、44100、48000、96000<br/><li>不同的封装，mp3 支持不同的采样率，如下表所示|
| Bitrate            | Response.TemplateList.<br/>ConcatTemplate.Audio | 原始音频码率   | String | 否   | 无    | <li>单位：Kbps<br/><li>值范围：[8，1000]                       |
| Channels           | Response.TemplateList.<br/>ConcatTemplate.Audio | 声道数         | String | 否   | 无      | <li>当 Codec 设置为 aac，支持1、2、4、5、6、8<br/><li>当 Codec 设置为mp3，支持1、2 |

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
| Codec                      | Response.TemplateList.<br/>ConcatTemplate.Video | 编解码格式             | String | 否   |   H.264 | H.264                                          |
| Width                      | Response.TemplateList.<br/>ConcatTemplate.Video | 宽                    | String | 否   | 视频原始宽度 | <li>值范围：[128，4096]<br/><li>单位：px<br/><li>若只设置 Width 时，按照视频原始比例计算 Height |
| Height                     | Response.TemplateList.<br/>ConcatTemplate.Video | 高                    | String | 否   | 视频原始高度 | <li>值范围：[128，4096]<br/><li>单位：px<br/><li>若只设置 Height 时，按照视频原始比例计算 Width |
| Fps                        | Response.TemplateList.<br/>ConcatTemplate.Video | 帧率                  | String | 否   | 视频原始帧率 | <li>值范围：(0，60]<br><li>单位：fps |
| Bitrate                    | Response.TemplateList.<br/>ConcatTemplate.Video | 视频输出文件的码率      | String | 否   |  视频原始码率           | <li>值范围：[10，50000]<br/><li>单位：Kbps   </li>                  |
| Remove                     | Response.TemplateList.<br/>ConcatTemplate.Video | 是否删除视频流         | String | 否   | false        | 取值 true、false


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

**案例一：按照模板 ID 维度查询**
#### 请求

```shell
GET /template?ids=A,B,C HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98****-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=



<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzh****=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
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
    </TemplateList>
    <NonExistTIDs>
        <TemplateId>B</TemplateId>
        <TemplateId>C</TemplateId>
    </NonExistTIDs>
</Response>
```

**案例二：按照分页列表维度查询**
#### 请求

```shell
GET /template?pageSize=10&pageNumber=1 HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98****-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=



<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzh****=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
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
    </TemplateList>
</Response>
```