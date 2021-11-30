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

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。 

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
   </Snapshot>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 模板类型：Snapshot                                    | String    | 是   |
| Name               | Request | 模板名称仅支持中文、英文、数字、_、-和*                   | String    | 是   |
| Snapshot           | Request | 截图                                                  | Container | 是   |


Container 类型 Snapshot 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Mode                | Request.Snapshot | 截图模式 | String    | 否   | Interval | <li>值范围：{Interval, Average}</li><li>Interval 表示间隔模式 Average 表示平均模式</li><li> Interval 模式：Start，TimeInterval，<br/>Count 参数生效。当设置 Count，未设置 TimeInterval 时，<br/>表示截取所有帧，共 Count 张图片</li><li>Average 模式：Start，Count 参数生效。表示<br/>从 Start 开始到视频结束，按平均间隔截取共 Count 张图片</li>|
| Start                | Request.Snapshot | 开始时间 | String    | 否   | 0 | <li>[0 视频时长] </li><li>单位为秒 </li><li>支持 float 格式，执行精度精确到毫秒</li> |
| TimeInterval         | Request.Snapshot | 截图时间间隔 | String    | 否   | 无  | <li>(0 3600] </li><li>单位为秒 </li><li>支持 float 格式，执行精度精确到毫秒</li> |
| Count                | Request.Snapshot | 截图数量 | String    | 是   | 无  | (0 10000] |
| Width                | Request.Snapshot | 宽 | String    | 否   |  视频原<br/>始宽度 | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Width 时，按照视频原始比例计算 Height </li>|
| Height                | Request.Snapshot | 高 | String    | 否  | 视频原<br/>始高度  | <li>值范围：[128，4096]</li><li>单位：px</li><li>若只设置 Height 时，按照视频原始比例计算 Width</li> |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。

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

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| Tag                | Response | 模板类型，Snapshot                                           | String    |
| Name               | Response | 模板名字                                                     | String    |
| TemplateId         | Response | 模板 ID                                                      | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| Snapshot           | Response | 其详细的模板参数，同上述请求体部分 Snapshot 说明 | Container |


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
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
        </Snapshot>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
