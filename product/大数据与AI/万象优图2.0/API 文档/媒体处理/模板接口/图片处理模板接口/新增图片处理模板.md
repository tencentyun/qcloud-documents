## 功能描述
CreateMediaTemplate 用于图片处理模板。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateTranscodeTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>PicProcess</Tag>
    <Name>TemplateName</Name>
    <PicProcess>
      <IsPicInfo></IsPicInfo>
      <ProcessRule></ProcessRule>
    </PicProcess>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- | ---- |
| Tag                | Request | 模板类型：PictureProcess                                    | String    | 是   | 无 |
| PicProcess         | Request | 容器格式                                               | Container | 是   | 无 |


Container 类型 PicProcess 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 是否必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| IsPicInfo                  | Request.Container | 是否返回原图信息  | String | 否   |  false | true、false |
| ProcessRule                | Request.Container.Rule | 图片处理规则      | String | 是   | 无 | 1. 基础图片处理参见 [基础图片处理](https://cloud.tencent.com/document/product/436/44879) 文档 <br/>2. 图片压缩参见 [图片压缩](https://cloud.tencent.com/document/product/436/60450) 文档 <br/>3. 盲水印参见 [盲水印](https://cloud.tencent.com/document/product/436/46782) 文档  |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>PicProcess</Tag>
        <TemplateId></TemplateId>
        <Name></Name>
        <State></State>
        <PicProcess>
          <IsPicInfo></IsPicInfo>
          <ProcessRule></ProcessRule>
        </PicProcess>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
        <BucketId></BucketId>
        <Category></Category>
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
| Tag                | Response.Template     | 模板类型，PicProcess                                          | String    |
| UpdateTime         | Response.Template     | 更新时间                                                     | String    |
| CreateTime         | Response.Template     | 创建时间                                                     | String    |
| PicProcess         | Response.Template     | 详细的模板参数                                                | Container |


Container节点 PicProcess 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                    | 类型      |
| :----------------- | :----------------------------- | :-------------------------------------- | :-------- |
| IsPicInfo          | Response.Template.PicProcess | 同请求体中的 <br/>Request.Container.IsPicInfo | String |
| ProcessRule        | Response.Template.PicProcess | 同请求体中的 <br/>Request.Container.ProcessRule | String |


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
    <Tag>PicProcess</Tag>
    <Name>TemplateName</Name>
    <PicProcess>
        <IsPicInfo>true</IsPicInfo>
        <ProcessRule>imageMogr2/rotate/90</ProcessRule>
    </PicProcess>
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
        <Tag>PicProcess</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <PicProcess>
            <IsPicInfo>true</IsPicInfo>
            <ProcessRule>imageMogr2/rotate/90</ProcessRule>
        </PicProcess>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
