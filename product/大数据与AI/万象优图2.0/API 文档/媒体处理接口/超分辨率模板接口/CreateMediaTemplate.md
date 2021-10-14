## 功能描述

CreateMediaTemplate 用于新增超分辨率模板。

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

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>SuperResolution</Tag>
    <Name>TemplateName</Name>
    <Resolution>sdtohd</Resolution>
    <EnableScaleUp>true</EnableScaleUp>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                        | 类型      | 是否必选 | 限制                           |
| ------------------ | ------- | ----------------------------------------------------- | --------- | ---- | ---- |
| Tag                | Request | 模板类型：SuperResolution                              | String    | 是   | 无 |
| Name               | Request | 模板名称：仅支持中文、英文、数字、\_、-和\*                 | String    | 是   | 无 |
| Resolution         | Request | 分辨率选项                                             | String    | 是   | 1. sdtohd：标清到超清<br>2. hdto4k：高清到4K |
| EnableScaleUp      | Request |   自动缩放开关，默认关闭                                    | String    | 否   | true、false | 

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据, 包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>SuperResolution</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <SuperResolution>
            <Resolution>sdtohd</Resolution>
            <EnableScaleUp>true</EnableScaleUp>
        </SuperResolution>
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
| TemplateId         | Response.Template     | 模板 ID                                                      | String    |
| Name               | Response.Template     | 模板名称                                                     | String    |
| BucketId           | Response.Template     | 模板所属存储桶                                                | String    |
| Category           | Response.Template     | 模板属性，Custom 或者 Official                                | String    |
| Tag                | Response.Template     | 模板类型，SuperResolution                                     | String    |
| UpdateTime         | Response.Template     | 更新时间                                                     | String    |
| CreateTime         | Response.Template     | 创建时间                                                     | String    |
| SuperResolution    | Response.Template     | 详细的模板参数                                                | Container |


Container 节点 SuperResolution 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                    | 类型      |
| :----------------- | :----------------------------- | :-------------------------------------- | :-------- |
| Resolution         | Response.Template.SuperResolution | 同请求体中的 Request.Resolution       | String |
| EnableScaleUp      | Response.Template.SuperResolution | 同请求体中的 Request.EnableScaleUp    | String |


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
    <Tag>SuperResolution</Tag>
    <Name>TemplateName</Name>
    <Resolution>sdtohd</Resolution>
    <EnableScaleUp>true</EnableScaleUp>
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
        <Tag>SuperResolution</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <SuperResolution>
            <Resolution>sdtohd</Resolution>
            <EnableScaleUp>true</EnableScaleUp>
        </SuperResolution>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
