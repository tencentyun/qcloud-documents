## 功能描述
CancelMediaJob 用于取消一个任务。

## 请求

#### 请求示例

```shell
PUT /jobs/<jobId>?cancel HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求体
该请求无请求体。


## 响应

#### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 特有响应头
该响应无特殊的响应头。

#### 响应体
该请求无响应体。

#### 错误码
该请求操作可能会出现如下错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
PUT /jobs/j-xxx-xxx-xxx-xxxx?cancel HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98****-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=

```

