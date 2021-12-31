## 功能描述
DescribeMediaTemplates 用于搜索截图模板。

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
| tag           | 无        | 模板 Tag：Snapshot       | String    |是|
| category      | 无        | Official，Custom，默认值：Custom | String  |否|
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
        <TemplateId>A</TemplateId>
        <Name>TemplateName</Name>
        <Tag>Snapshot</Tag>
        <Snapshot>
            <Width>1280</Width>
            <Height></Height>
            <Start>0</Start>
            <TimeInterval></TimeInterval>
            <Count></Count>
        </Snapshot>
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

Container 节点 TemplateList 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response.TemplateList | 模版 ID                                                      | String    |
| Name               | Response.TemplateList | 模版名字                                                     | String    |
| BucketId           | Response.TemplateList | 模版所属存储桶                                                | String    |
| Category           | Response.TemplateList | 模版属性，Custom 或者 Official                                | String    |
| Tag                | Response.TemplateList | 模版类型，Snapshot                                           | String    |
| UpdateTime         | Response.TemplateList | 更新时间                                                     | String    |
| CreateTime         | Response.TemplateList | 创建时间                                                     | String    |
| Snapshot           | Response.TemplateList | 其详细的模版参数 | Container |

Container 类型 Snapshot 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Mode                | TemplateList.Snapshot | 截图模式 | String    | 是   | Interval | <li>值范围：{Interval, Average}</li><li>Interval 表示间隔模式 Average 表示平均模式</li><li> Interval模式：Start，TimeInterval，<br/>Count 参数生效。当设置 Count，<br/>未设置 TimeInterval 时，表示截取所有帧，共 Count 张图片</li><li>Average 模式：Start，Count 参数生效。表示从 <br/>Start 开始到视频结束，按平均间隔截取共 Count 张图片</li>|
| Start                | TemplateList.Snapshot | 开始时间 | String    | 是   | 0 | <li>[0 视频时长] </li><li>单位为秒 </li><li>支持 float 格式，执行精度精确到毫秒</li> |
| TimeInterval         | TemplateList.Snapshot | 截图时间间隔 | String    | 否   | 无  | <li>(0 3600] </li><li>单位为秒 </li><li>支持 float 格式，执行精度精确到毫秒</li> |
| Count                | TemplateList.Snapshot | 截图数量 | String    | 是   | 无  | (0 10000] |
| Width                | TemplateList.Snapshot | 宽 | String    | 否   |  视频原<br/>始宽度 | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Width 时，按照视频原始比例计算 Height</li> |
| Height                | TemplateList.Snapshot | 高 | String    | 否  | 视频原<br/>始高度  | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Height 时，按照视频原始比例计算 Width</li> |
| CIParam              | TemplateList.Snapshot | 截图图片处理参数  | String    | 否   | 无  | 1. 参考 [缩放](https://cloud.tencent.com/document/product/460/36540) 文档 <br/> 2. 例如：imageMogr2/format/png |
| IsCheckCount              | TemplateList.Snapshot | 是否强制检查截图个数 | String    | 否   | false  | 1. 使用自定义间隔模式截图时，视频时长不够截取 Count 个截图，可以转为平均截图模式截取 Count 个截图 |
| IsCheckBlack              | TemplateList.Snapshot | 是否开启黑屏检测 | String    | 否   | false  | true/false |
| BlackLevel           | TemplateList.Snapshot | 截图黑屏检测参数  | String    | 否   | 空  | 1.当 IsCheckBlack=true 时有效<br/>2. 值参考范围[30，100]，表示黑色像素的占比值，值越小，黑色占比越小 <br/> 3. Start>0 ，参数设置无效，不做过滤黑屏 <br/> 3. Start =0 参数有效，截帧的开始时间为第一帧非黑屏开始  |
| PixelBlackThreshold  | TemplateList.Snapshot | 截图黑屏检测参数  | String    | 否   | 空  | 1. 当 IsCheckBlack=true 时有效<br/>2. 判断像素点是否为黑色点的阈值，取值范围：[0，255]  |
| SnapshotOutMode  | TemplateList.Snapshot | 截图输出模式参数  | String    | 否   | OnlySnapshot  | 1. 值范围：{OnlySnapshot, OnlySprite, SnapshotAndSprite}<br/> 2. OnlySnapshot 表示仅输出截图模式 OnlySprite 表示仅输出雪碧图模式 SnapshotAndSprite 表示输出截图与雪碧图模式<br/> |
| SpriteSnapshotConfig  | TemplateList.Snapshot | 雪碧图输出配置  | Container | 否   | 无  | 无 |


Container 类型 Snapshot.SpriteSnapshotConfig 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| CellWidth                | TemplateList.Snapshot.SpriteSnapshotConfig | 单图宽度 | String    | 否   | 截图宽度 | 1. 值范围：[8，4096]<br/> 2. 单位：px<br/> |
| CellHeight               | TemplateList.Snapshot.SpriteSnapshotConfig | 单图高度 | String    | 否  | 截图宽度  | 1. 值范围：[8，4096]<br/> 2. 单位：px<br/> |
| Padding              | TemplateList.Snapshot.SpriteSnapshotConfig | 雪碧图内边距大小  | String    | 否   | 0  | 1. 值范围：[0，1024]<br/> 2. 单位：px<br/> |
| Margin              | TemplateList.Snapshot.SpriteSnapshotConfig | 雪碧图外边距大小  | String    | 否   | 0  | 1. 值范围：[0，1024]<br/> 2. 单位：px<br/> |
| Color              | TemplateList.Snapshot.SpriteSnapshotConfig | 背景颜色  | String    | 是   | 无  | 支持颜色详见 [FFmpeg](https://www.ffmpeg.org/ffmpeg-utils.html#color-syntax) |
| Columns              | TemplateList.Snapshot.SpriteSnapshotConfig | 雪碧图列数  | String    | 是   | 0  | 1. 值范围：[1，10000]<br/> |
| Lines              | TemplateList.Snapshot.SpriteSnapshotConfig | 雪碧图行数  | String    | 是   | 0  | 1. 值范围：[1，10000]<br/> |


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
        <TemplateId>A</TemplateId>
        <Name>TemplateName</Name>
        <Tag>Snapshot</Tag>
        <Snapshot>
            <Width>1280</Width>
            <Height></Height>
            <Start>0</Start>
            <TimeInterval></TimeInterval>
            <Count></Count>
            <SpriteSnapshotConfig>
                <CellHeight>128</CellHeight>
                <CellWidth>128</CellWidth>
                <Color>White</Color>
                <Columns>10</Columns>
                <Lines>10</Lines>
                <Margin>0<Margin/>
                <Padding>0<Padding/>
            </SpriteSnapshotConfig>
        </Snapshot>
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
        <TemplateId>A</TemplateId>
        <Name>TemplateName</Name>
        <Tag>Snapshot</Tag>
        <Snapshot>
            <Width>1280</Width>
            <Height></Height>
            <Start>0</Start>
            <TimeInterval></TimeInterval>
            <Count></Count>
        </Snapshot>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
</Response>
```
