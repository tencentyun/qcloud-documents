## 功能描述
DescribeMediaTemplates 搜索水印模板。

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

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体
该请求的请求体为空。

#### 请求参数
参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| tag           | 无        | 模板 Tag：Watermark       | String    |是|
| ids           | 无        | 模板 ID，以,符号分割字符串  | String     |否|
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
        <TemplateId>A</TemplateId>
        <Tag>Watermark</Tag>
        <Name>TemplateName</Name>
        <Watermark>
            <Type>Text</Type>
            <LocMode>Absolute</LocMode>
            <Dx>128</Dx>
            <Dy>128</Dy>
            <Pos>TopRight</Pos>
            <StartTime>0</StartTime>
            <EndTime>100.5</EndTime>
            <Text>
                <Text>水印内容</Text>
                <FontSize>30</FontSize>
                <FontType></FontType>
                <FontColor>0xRRGGBB</FontColor>
                <Transparency>30</Transparency>
            </Text>
        </Watermark>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
</Response>

```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                       | 类型      |
| :----------------- | :----- | :----------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器      |   Container   |

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
| Tag                | Response.TemplateList | 模版类型，Watermark                                          | String    |
| UpdateTime         | Response.TemplateList | 更新时间                                                     | String    |
| CreateTime         | Response.TemplateList | 创建时间                                                     | String    |
| Watermark           | Response.TemplateList | 水印信息                 | Container |


Container 类型 Watermark 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Type                | Response.TemplateList.Watermark | 水印类型    | String    | 是   | 无  |  Text：文字水印、 Image：图片水印 |
| Pos                 | Response.TemplateList.Watermark | 基准位置    | String    | 是   | 无  | TopRight、TopLeft、BottomRight、 BottomLeft |
| LocMode             | Response.TemplateList.Watermark | 偏移方式    | String    | 是   | 无  |  Relativity：按比例、 Absolute：固定位置 |
| Dx                  | Response.TemplateList.Watermark | 水平偏移    | String    | 是   | 无  |1. 在图片水印中，如果 Background 为 true，当 locMode为Relativity时，为% 取值范围[-300 0]；当locMode为Absolute时，为px 值范围：[-4096 0] <br/> 2. 在图片水印中，如果Background为false，当locMode 为 Relativity 时，为%取值范围[0 100]；当 locMode 为 Absolute 时，为 px 值范围：[0 4096]<br/>3. 在文字水印中，当 locMode 为 Relativity 时，为%取值范围[0 100]；当 locMode 为 Absolute 时，为 px 值范围：[0 4096] |
| Dy                  | Response.TemplateList.Watermark | 垂直偏移    | String    | 是   | 无  |1. 在图片水印中，如果 Background 为 true，当 locMode 为 Relativity 时，为%取值范围[-300 0]；当 locMode 为 Absolute 时，为 px 值范围：[-4096 0] <br/> 2. 在图片水印中，如果 Background 为 false，当 locMode 为 Relativity 时，为%取值范围[0 100]；当 locMode 为 Absolute 时，为 px 值范围：[0 4096]<br/>3. 在文字水印中，当 locMode 为 Relativity 时，为%取值范围[0 100]；当 locMode 为 Absolute 时，为 px 值范围：[0 4096] |
| StartTime           | Response.TemplateList.Watermark | 水印开始时间 | String    | 否   | 0   | 1. [0 视频时长] <br/> 2. 单位为秒 <br/> 3. 支持 float 格式，执行精度精确到毫秒 |
| EndTime             | Response.TemplateList.Watermark | 水印结束时间 | String    | 否   | 视频结束时间  | 1. [0 视频时长] <br/> 2. 单位为秒 <br/> 3. 支持 float 格式，执行精度精确到毫秒 |
| Image               | Response.TemplateList.Watermark | 图片水印节点 | Container    | 否   | 无  | 无 |
| Text                | Response.TemplateList.Watermark | 文本水印节点 | Container    | 否   | 无  | 无 |


Container 类型 Image 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Url                 | Response.TemplateList.Watermark.Image | 水印图地址   | String    | 是   | 无  | 1. 水印图片地址 <br/> 2. 如果水印图片为私有对象时，请携带签名信息 |
| Mode                 | Response.TemplateList.Watermark.Image | 尺寸模式    | String    | 是   | 无   | 1. Original：原有尺寸 <br/>  2. Proportion：按比例 <br/> 3. Fixed：固定大小 |
| Width                | Response.TemplateList.Watermark.Image | 宽         | String    | 否   | 无   | 1. 当 Mode 为 Original，水印图宽 <br/> 2. 当 Mode 为 Proportion，单位为%，背景图：[100 300]；前景图：[1 100]<br/> 3. 当 Mode 为 Fixed，单位为 px，值范围：[8，4096]，若只设置 Width 时，按照视频原始比例计算 Height<br/> |
| Height               | Response.TemplateList.Watermark.Image | 高         | String    | 否   | 无   | 1. 当 Mode 为 Original，水印图高 <br/> 2. 当 Mode 为 Proportion，单位为%，背景图：[100 300]；前景图：[1 100]<br/> 3.当 Mode 为 Fixed，单位为 px，值范围：[8，4096]，若只设置 Height 时，按照视频原始比例计算 Width<br/>|
| Transparency         | Response.TemplateList.Watermark.Image | 透明度      | String    | 是   | 无   | 值范围：[0 100]，单位% |
| Background           | Request.Watermark.Image | 是否背景图   | String    | 否   | false   | true、false |


Container 类型 Text 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| FontSize            | Response.TemplateList.Watermark.Text | 字体大小    | String    | 是   | 无  | 值范围：[0 100]，单位px |
| FontType            | Response.TemplateList.Watermark.Text | 字体类型    | String    | 是   | 无  | -  |
| FontColor           | Response.TemplateList.Watermark.Text | 字体颜色    | String    | 是   | 无  | 格式：0xRRGGBB |
| Transparency        | Response.TemplateList.Watermark.Text | 透明度      | String    | 是   | 无  |值范围：[0 100]，单位%|
| Text                | Response.TemplateList.Watermark.Text | 水印内容    | String    | 是   | 无  | 长度不超过64个字符，仅支持中文、英文、数字、_、-和*|

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
GET /template?ids=A,B,C HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <TemplateId>A</TemplateId>
        <Tag>Watermark</Tag>
        <Name>TemplateName</Name>
        <Watermark>
            <Type>Text</Type>
            <LocMode>Absolute</LocMode>
            <Dx>128</Dx>
            <Dy>128</Dy>
            <Pos>TopRight</Pos>
            <StartTime>0</StartTime>
            <EndTime>100.5</EndTime>
            <Text>
                <Text>水印内容</Text>
                <FontSize>30</FontSize>
                <FontType></FontType>
                <FontColor>0xRRGGBB</FontColor>
                <Transparency>30</Transparency>
            </Text>
        </Watermark>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
    <NonExistTIDs>
        <TemplateId>B</TemplateId>
        <TemplateId>C</TemplateId>
    </NonExistTIDs>
</Response>
```

#### 请求

```shell
GET /template?pageSize=10&pageNumber=1 HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <TemplateId>A</TemplateId>
        <Tag>Watermark</Tag>
        <Name>TemplateName</Name>
        <Watermark>
            <Type>Text</Type>
            <LocMode>Absolute</LocMode>
            <Dx>128</Dx>
            <Dy>128</Dy>
            <Pos>TopRight</Pos>
            <StartTime>0</StartTime>
            <EndTime>100.5</EndTime>
            <Text>
                <Text>水印内容</Text>
                <FontSize>30</FontSize>
                <FontType></FontType>
                <FontColor>0xRRGGBB</FontColor>
                <Transparency>30</Transparency>
            </Text>
        </Watermark>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
</Response>
```
