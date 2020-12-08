## 功能描述
CreateProject 用于新增项目。

## 请求
### 请求实例

```shell
POST /project HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <Mode>HTTP</Mode>
    <Bucket>
        <Region></Region>
        <BucketId></BucketId>
        <Prefix></Prefix>
    </Bucket>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                     | 类型      | 必选 |
| ------------------ | ------- | ---------------------------------------- | --------- | ---- |
| Mode               | Request | 接入类型: HTTP                           | String    | 是   |
| Name               | Request | 项目名称 仅支持中文、英文、数字、_、-和* | String    | 是   |
| Bucket             | Request | Bucket 信息                               | Container | 否   |


Container 类型 Bucket 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Region                | Request.Bucket | Bucket 地区 | String    | 是   | 无 | 无|
| BucketId            | Request.Bucket | Bucket 的 ID | String      | 是   | 无  | 无 |
| Prefix            | Request.Bucket     | 对象 key 前缀 | String    | 否   | 无  | 无 |



## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/1344/50452) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell

<Response>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container节点Response的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| Name               | Response | 项目名字                                                     | String    |
| Desc               | Response | 项目描述                                                     | String    |
| ProjectId          | Response | 项目 ID                                                      | String    |
| Mode               | Response | 接入类型                                                     | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| Bucket             | Response | 其详细的参数，同上述请求体部分 Bucket 说明                          | Container |


### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

### 请求示例

```shell
POST /project HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <Mode>HTTP</Mode>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
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
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```
