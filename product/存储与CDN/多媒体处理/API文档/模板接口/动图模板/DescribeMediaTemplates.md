## 功能描述
DescribeMediaTemplates 用于搜索动图模板。

## 请求

#### 请求示例

```shell
GET /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体
该请求的请求体为空。

#### 请求参数
参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| tag           | 无        | 模板 Tag：Animation       | String    |是|
| category      | 无   | Official，Custom，默认值：Custom | String  |否|
| ids           | 无        | 模板 ID，以`,`符号分割字符串  | String     |否|
| name          | 无        | 模板名称前缀              | String     |否|
| pageNumber    | 无        | 第几页                   | Integer     |否|
| pageSize      | 无        | 每页个数                 | Integer     |否|

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
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
| Category           | Response.TemplateList | 模版属性，Custom 或者 Official                                | String    |
| Tag                | Response.TemplateList | 模版 Tag：Animation                                           | String    |
| UpdateTime         | Response.TemplateList | 更新时间                                                     | String    |
| CreateTime         | Response.TemplateList | 创建时间                                                     | String    |
| TransTpl           | Response.TemplateList | 详细的模版参数                                                | Container |


TransTpl 节点 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Format                | TransTpl.Container | 容器格式：gif，hgif，webp  hgif 为高质量 gif，即清晰度比较高的 gif 格式图 | String    | 是   |

TransTpl 节点 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | TransTpl.Video | 编解码格式            | String | 是   |  无  | gif, webp                                          |
| Width                      | TransTpl.Video | 宽                    | String | 否   | 视频原<br/>始宽度 | <li>值范围：[128，4096]</li><li>单位：px<br/><li>若只设置 Width 时，按照视频原始比例计算 Height |
| Height                     | TransTpl.Video | 高                    | String | 否   | 视频原<br/>始高度 | <li>值范围：[128，4096]<br/><li>单位：px<br/><li>若只设置 Height 时，按照视频原始比例计算 Width |
| Fps                        | TransTpl.Video | 帧率                  | String | 否   | 视频原<br/>始帧率 | <li>值范围：(0，60]<br/><li>单位：fps<br/><li>帧率超过60时，设置为60<br/>用户可以设置 fps，如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率 |
| AnimateOnly<br/>KeepKeyFrame    | TransTpl.Video | 动图只保<br/>留关键帧      | String | 否   |      无        | <li>true、false<br/><li>动图保留关键帧参数                     |
| AnimateTime<br/>IntervalOfFrame | TransTpl.Video | 动图抽帧<br/>间隔时间      | String | 否   |      无        | <li>（0，视频时长]<br/><li>动图抽帧时间间隔<br/><li>若设置 TimeInterval.Duration，则小于该值 |
| AnimateFrames<br/>PerSecond     | TransTpl.Video | Animation 每秒<br/>抽帧帧数 | String | 否   |     无         | <li>（0，视频帧率)<br/><li>动图抽帧频率<br/><li>优先级：AnimateFrames<br/>PerSecond >  AnimateOnlyKeepKeyFrame  > AnimateTimeIntervalOfFrame |
| Quality                    | TransTpl.Video | 设置相对质量          | String | 否   |     无         | <li>[1, 100)<br/><li>webp 图像质量设定生效，gif 没有质量参数 </li>|


TransTpl 节点 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | TransTpl.TimeInterval | 开始时间 | String    | 否   | 0 | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒 |
| Duration             | TransTpl.TimeInterval | 持续时间 | String    | 否   | 视频时长 | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒</li> |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

**案例一：按照模板 ID 维度查询**

#### 请求

```shell
GET /template?ids=A,B,C HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
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
    <TemplateList>
        <Name>TemplateName</Name>
        <TemplateId>A</TemplateId>
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
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
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
    </TemplateList>
</Response>
```
