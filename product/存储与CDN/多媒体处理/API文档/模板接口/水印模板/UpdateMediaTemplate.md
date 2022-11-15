## 功能描述

UpdateMediaTemplate 用于更新水印模板。

## 请求

#### 请求示例

```shell
PUT /template/<TemplateId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
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
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述                                      | 类型      | 必选 |
| :----------------- | :----- | :---------------------------------------- | :-------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 模板类型：Watermark                                   | String    | 是   |
| Name               | Request | 模板名称仅支持中文、英文、数字、\_、-和\*                                             | String    | 是   |
| Watermark           | Request| 水印信息                                              | Container | 是   |


Container 类型 Watermark 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Type                | Request.Watermark | 水印<br/>类型    | String    | 是   | 无  | <li>Text：文字水印<li>Image：图片水印 |
| Pos                 | Request.Watermark | 基准<br/>位置    | String    | 是   | 无  | <li>TopRight：右上<li>TopLeft：左上<li>BottomRight：右下<li>BottomLeft：左下 |
| LocMode             | Request.Watermark | 偏移<br/>方式    | String    | 是   | 无  | <li>Relativity：按比例<li>Absolute：固定位置 |
| Dx                  | Request.Watermark | 水平偏移    | String    | 是   | 无  | 1. 在图片水印中，如果 Background 为 true，当 locMode 为 Relativity 时，单位为%，值范围：[-300 0]；当 locMode 为 Absolute 时，单位为 px，值范围：[-4096 0] <br/> 2. 在图片水印中，如果 Background 为 false，当 locMode 为 Relativity 时，单位为%，值范围：[0 100]；当 locMode 为 Absolute 时，单位为 px，值范围：[0 4096]<br/>3. 在文字水印中，当 locMode 为 Relativity 时，单位为%，值范围：[0 100]；当 locMode 为 Absolute 时，单位为 px，值范围：[0 4096] |
| Dy                  | Request.Watermark | 垂直偏移    | String    | 是   | 无  | 1. 在图片水印中，如果 Background 为 true，当 locMode 为 Relativity 时，单位为%，值范围：[-300 0]；当 locMode 为 Absolute 时，单位为 px，值范围：[-4096 0] <br/> 2. 在图片水印中，如果 Background 为 false，当 locMode 为 Relativity 时，单位为%，值范围：[0 100]；当 locMode 为 Absolute 时，单位为 px，值范围：[0 4096]<br/>3. 在文字水印中，当 locMode 为 Relativity 时，单位为%，值范围：[0 100]；当 locMode 为 Absolute 时，单位为 px，值范围：[0 4096] |
| StartTime           | Request.Watermark | 水印<br/>开始<br/>时间 | String    | 否   | 0   | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒 |
| EndTime             | Request.Watermark | 水印<br/>结束<br/>时间 | String    | 否   | 视频结束时间  | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒 |
| Image               | Request.Watermark | 图片<br/>水印<br/>节点 | Container    | 否   | 无  | 无 |
| Text                | Request.Watermark | 文本<br/>水印<br/>节点 | Container    | 否   | 无  | 无 |


Container 类型 Image 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Url                 | Request.Watermark.<br/>Image | 水印图地址   | String    | 是   | 无  | <li>水印图片地址 <br/><li>如果水印图片为私有对象时，请携带签名信息 |
| Mode                 | Request.Watermark.<br/>Image | 尺寸模式    | String    | 是   | 无   | <li>Original：原有尺寸 <br/><li>Proportion：按比例 <br/><li>Fixed：固定大小 |
| Width                | Request.Watermark.<br/>Image | 宽         | String    | 否   | 无   | <li>当 Mode 为 Original 时，不支持设置水印图宽度 <br/><li>当 Mode 为 Proportion，单位为%，背景图值范围：[100 300]；前景图值范围：[1 100]<br/><li>当 Mode 为 Fixed，单位为 px，值范围：[8，4096]，若只设置 Width 时，按照视频原始比例计算 Height<br/> |
| Height               | Request.Watermark.<br/>Image | 高         | String    | 否   | 无   | <li>当 Mode 为 Original 时，不支持设置水印图高度 <br/><li>当 Mode 为 Proportion，单位为%，背景图值范围：[100 300]；前景图值范围：[1 100]<br/><li>当 Mode 为 Fixed，单位为px，值范围：[128，4096]，若只设置 Height 时，按照视频原始比例计算 Width<br/>|
| Transparency         | Request.Watermark.<br/>Image | 透明度      | String    | 是   | 无   | 值范围：[0 100]，单位为% |
| Background           | Request.Watermark.<br/>Image | 是否背景图   | String    | 否   | false   |  true、false |


Container 类型 Text 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| FontSize            | Request.Watermark.<br/>Text | 字体大小    | String    | 是   | 无  | 值范围：[0 100]，单位为 px |
| FontType            | Request.Watermark.<br/>Text | 字体类型    | String    | 是   | 无  | 参考下表 |
| FontColor           | Request.Watermark.<br/>Text | 字体颜色    | String    | 是   | 无  | 格式：0xRRGGBB |
| Transparency        | Request.Watermark.<br/>Text | 透明度      | String    | 是   | 无  | 值范围：[0 100]，单位为%|
| Text                | Request.Watermark.<br/>Text | 水印内容    | String    | 是   | 无  | 长度不超过64个字符，仅支持中文、英文、数字、_、-和*|


Text 的 FontType 具体数据描述如下：

| 字体名称               | 支持的语言             | 描述
| ------------------     | -------                | ------
| simfang.ttf            |  中/英                 | 仿宋
| simhei.ttf             |  中/英                 | 黑体
| simkai.ttf             |  中/英                 | 楷体
| simsun.ttc             |  中/英                 | 宋体
| STHeiti-Light.ttc      |  中/英                 | 华文黑体
| STHeiti-Medium.ttc     |  中/英                 | 华文黑体中
| youyuan.TTF            |  中/英                 | 幼圆
| ariblk.ttf             |  英                    | 无
| arial.ttf              |  英                    | 无
| ahronbd.ttf            |  英                    | 无
| Helvetica.dfont        |  英                    | 无
| HelveticaNeue.dfont    |  英                    | 无

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
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
    </Template>
</Response>

```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                       | 类型      |
| :----------------- | :----- | :----------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器      |   Container   |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                           | 类型      |
| :----------------- | :------- | :----------------------------- | :-------- |
| TemplateId          | Response | 模板 ID                   | String    |
| Watermark           | Response| 水印信息，详情请见同页面请求体 Watermark 的具体数据描述                                          | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
PUT /template/<TemplateId> HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
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
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
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
    </Template>
</Response>
```
