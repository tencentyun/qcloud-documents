## 功能描述
CreateMediaTemplate 用于新增截图模板。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateSnapshotTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。 

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
   <Tag>Snapshot</Tag>
   <Name>TemplateName</Name>
   <Snapshot>
      <Mode>Interval</Mode>
      <Width>1280</Width>
      <Height></Height>
      <Start>0</Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
      <SnapshotOutMode>OnlySnapshot</SnapshotOutMode>
      <SpriteSnapshotConfig>
        <CellHeight></CellHeight>
        <CellWidth></CellWidth>
        <Color></Color>
        <Columns></Columns>
        <Lines></Lines>
        <Margin><Margin/>
        <Padding><Padding/>
      </SpriteSnapshotConfig>
   </Snapshot>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 模板类型：Snapshot                                    | String    | 是   |
| Name               | Request | 模板名称 仅支持中文、英文、数字、_、-和*                   | String    | 是   |
| Snapshot           | Request | 截图                                                  | Container | 是   |


Container 类型 Snapshot 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Mode                | Request.Snapshot | 截图模式 | String    | 否   | Interval | 1. 值范围：{Interval, Average, KeyFrame}<br/> 2. Interval 表示间隔模式 Average 表示平均模式 KeyFrame 表示关键帧模式<br/> 3. Interval 模式：Start，TimeInterval，Count 参数生效。当设置 Count，未设置 TimeInterval 时，表示截取所有帧，共 Count 张图片<br/> 4. Average 模式：Start，Count参数生效。表示从 Start 开始到视频结束，按平均间隔截取共 Count 张图片|
| Start                | Request.Snapshot | 开始时间 | String    | 否   | 0 | 1. [0 视频时长] <br/> 2. 单位为秒 <br/> 3. 支持 float 格式，执行精度精确到毫秒 |
| TimeInterval         | Request.Snapshot | 截图频率 | String    | 否   | 无  | 1. (0 3600] <br/> 2. 单位为秒 <br/> 3. 支持 float 格式，执行精度精确到毫秒 |
| Count                | Request.Snapshot | 截图数量 | String    | 是   | 无  | 1. (0 10000] |
| Width                | Request.Snapshot | 宽 | String    | 否   |  视频原始宽度 | 1. 值范围：[128，4096]<br/> 2. 单位：px<br/> 3. 若只设置 Width 时，按照视频原始比例计算 Height<br/> |
| Height               | Request.Snapshot | 高 | String    | 否  | 视频原始高度  | 1. 值范围：[128，4096]<br/> 2. 单位：px<br/> 3. 若只设置 Height 时，按照视频原始比例计算 Width<br/> |
| CIParam              | Request.Snapshot | 截图图片处理参数  | String    | 否   | 无  | 1. 参考 [缩放](https://cloud.tencent.com/document/product/460/36540) <br/> 2. 例如：imageMogr2/format/png |
| IsCheckCount              | Request.Snapshot | 是否强制检查截图个数 | String    | 否   | false  | 1. 使用自定义间隔模式截图时，视频时长不够截取 Count 个截图，可以转为平均截图模式截取 Count 个截图 |
| IsCheckBlack              | Request.Snapshot | 是否开启黑屏检测 | String    | 否   | false  | true/false |
| BlackLevel           | Request.Snapshot | 截图黑屏检测参数  | String    | 否   | 空  | 1.当IsCheckBlack=true时有效<br/>2. 值参考范围：[30，100]，表示黑色像素的占比值，值越小，黑色占比越小。<br/> 3. Start>0 ，参数设置无效，不做过滤黑屏；<br/> 3. Start =0 参数有效，截帧的开始时间为第一帧非黑屏开始  |
| PixelBlackThreshold  | Request.Snapshot | 截图黑屏检测参数  | String    | 否   | 空  | 1.当IsCheckBlack=true时有效<br/>2.判断像素点是否为黑色点的阈值，取值范围：[0，255]  |
| SnapshotOutMode  | Request.Snapshot | 截图输出模式参数  | String    | 否   | OnlySnapshot  | 1. 值范围：{OnlySnapshot, OnlySprite, SnapshotAndSprite}<br/> 2. OnlySnapshot 表示仅输出截图模式 OnlySprite 表示仅输出雪碧图模式 SnapshotAndSprite 表示输出截图与雪碧图模式<br/> |
| SpriteSnapshotConfig  | Request.Snapshot | 雪碧图输出配置  | Container | 否   | 无  | 无 |


Container 类型 Snapshot.SpriteSnapshotConfig 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| CellWidth                | Request.Snapshot.SpriteSnapshotConfig | 单图宽度 | String    | 否   | 截图宽度 | 1. 值范围：[8，4096]<br/> 2. 单位：px<br/> |
| CellHeight               | Request.Snapshot.SpriteSnapshotConfig | 单图高度 | String    | 否  | 截图宽度  | 1. 值范围：[8，4096]<br/> 2. 单位：px<br/> |
| Padding              | Request.Snapshot.SpriteSnapshotConfig | 雪碧图内边距大小  | String    | 否   | 0  | 1. 值范围：[0，1024]<br/> 2. 单位：px<br/> |
| Margin              | Request.Snapshot.SpriteSnapshotConfig | 雪碧图外边距大小  | String    | 否   | 0  | 1. 值范围：[0，1024]<br/> 2. 单位：px<br/> |
| Color              | Request.Snapshot.SpriteSnapshotConfig | 背景颜色  | String    | 是   | 无  |  支持颜色详见 [FFmpeg](https://www.ffmpeg.org/ffmpeg-utils.html#color-syntax) |
| Columns              | Request.Snapshot.SpriteSnapshotConfig | 雪碧图列数  | String    | 是   | 无  | 1. 值范围：[1，10000]<br/> |
| Lines              | Request.Snapshot.SpriteSnapshotConfig | 雪碧图行数  | String    | 是   | 无  | 1. 值范围：[1，10000]<br/> |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell

<Response>
    <Template>
        <Tag>Snapshot</Tag>
        <Name>TemplateName</Name>
        <TemplateId></TemplateId>
        <Snapshot>
            <Width>1280</Width>
            <Height></Height>
            <Start>0</Start>
            <TimeInterval></TimeInterval>
            <Count></Count>
            <SnapshotOutMode>OnlySnapshot</SnapshotOutMode>
            <SpriteSnapshotConfig>
              <CellHeight></CellHeight>
              <CellWidth></CellWidth>
              <Color></Color>
              <Columns></Columns>
              <Lines></Lines>
              <Margin><Margin/>
              <Padding><Padding/>
            </SpriteSnapshotConfig>
        </Snapshot>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container节点Response的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| Tag                | Response | 模版类型，Snapshot                                           | String    |
| Name               | Response | 模版名字                                                     | String    |
| TemplateId         | Response | 模版 ID                                                      | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| Snapshot           | Response | 其详细的模版参数，同上述请求体部分 Snapshot 说明 | Container |


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml



<Request>
   <Tag>Snapshot</Tag>
   <Name>TemplateName</Name>
   <Snapshot>
      <Width>1280</Width>
      <Height></Height>
      <Start>0</Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
      <SnapshotOutMode>OnlySnapshot</SnapshotOutMode>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=



<Response>
    <Template>
        <Tag>Snapshot</Tag>
        <Name>TemplateName</Name>
        <TemplateId></TemplateId>
        <Snapshot>
            <Width>1280</Width>
            <Height></Height>
            <Start>0</Start>
            <TimeInterval></TimeInterval>
            <Count></Count>
            <SnapshotOutMode>OnlySnapshot</SnapshotOutMode>
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
    </Template>
</Response>
```
