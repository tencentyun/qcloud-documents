## 功能描述
删除自定义模板接口。如果有已创建的任务使用该自定义模板，则相应的转码模板不能被删除。

## 请求
#### 请求示例

```shell
DELETE /template/<TemplateID> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml
<body>
```

>?Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体
该请求的请求体为空。

## 响应
#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。 

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>017F1B2D-2B5B-4441-ABBA-E0DC08F5AFEC</RequestId>
    <TemplateID>A</TemplateID>
<Response>
```

#### 错误码
该请求操作可能会出现如下错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

错误码|描述|HTTP 状态码
---|---|---
InternalErrror|服务端内部错误|500 Internal Server
AccessDenied|签名或者权限不正确，拒绝访问|403 Forbidden

## 实际案例

#### 请求

```shell
DELETE /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <TemplateID>A</TemplateID>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=


<Response>
    <RequestId>017F1B2D-2B5B-4441-ABBA-E0DC08F5AFEC</RequestId>
    <TemplateID>A</TemplateID>
</Response>
```
