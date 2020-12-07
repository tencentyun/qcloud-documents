## 功能描述
UpdateTemplate 用于更新截图模板。

## 请求
### 请求实例

```shell
PUT /template/<TemplateId> HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>AI</Tag>
    <Name>TemplateName</Name>
    <Desc>TemplateDesc</Desc>
    <AI>
        <Mode>MovingObjectDetect</Mode>
        <MovingObjectDetect>
            <Type>Baby</Type>
        </MovingObjectDetect>
    </AI>
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述                                      | 类型      | 必选 |
| :----------------- | :----- | :---------------------------------------- | :-------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 模板类型：AI                                              | String    | 是   |
| Name               | Request | 模板名称仅支持中文、英文、数字、_、-和*                       | String    | 是   |
| Desc               | Request | 模板描述仅支持中文、英文、数字、_、-和*                       | String    | 否   |
| AI                 | Request | 模板详情                                                  | Container | 否   |

Container 类型 AI 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Mode                 | Request.AI | AI 类型                                            | String    | 是   |
| MovingObjectDetect   | Request.AI | 移动物体检测参数                                       | Container    | 是   |

Container 类型 MovingObjectDetect 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Type              | Request.AI.MovingObjectDetect | 检测物体 | String    | 是   | 无 | 值范围：{Baby}<br/>|

## 响应

### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>AI</Tag>
        <Name>TemplateName</Name>
        <Desc>TemplateDesc</Desc>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <AI>
            <Mode>MovingObjectDetect</Mode>
            <MovingObjectDetect>
                <Type>Baby</Type>
            </MovingObjectDetect>
        </AI>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                       | 类型      |
| :----------------- | :----- | :----------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |


Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| Tag                | Response | 模版类型，Snapshot                                           | String    |
| Name               | Response | 模版名字                                                     | String    |
| Desc               | Response | 模版描述                                                     | String    |
| TemplateId         | Response | 模版ID                                                      | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| AI                 | Response | 其详细的模版参数，同上述请求体部分AI说明 | Container |

### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

### 请求

```shell
PUT /template/<TemplateId> HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Tag>AI</Tag>
    <Name>TemplateName</Name>
    <Desc>TemplateDesc</Desc>
    <AI>
        <Mode>MovingObjectDetect</Mode>
        <MovingObjectDetect>
            <Type>Baby</Type>
        </MovingObjectDetect>
    </AI>
</Request>
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <Template>
        <Tag>AI</Tag>
        <Name>TemplateName</Name>
        <Desc>TemplateDesc</Desc>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <AI>
            <Mode>MovingObjectDetect</Mode>
            <MovingObjectDetect>
                <Type>Baby</Type>
            </MovingObjectDetect>
        </AI>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
