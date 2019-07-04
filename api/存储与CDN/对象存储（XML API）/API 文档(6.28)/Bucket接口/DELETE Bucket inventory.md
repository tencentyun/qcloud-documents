## 功能描述

DELETE Bucket inventory 用于删除存储桶中指定的清单任务，用户需提供待删除的清单任务的名称。有关清单的详细特性，请参阅 [清单功能概述](https://cloud.tencent.com/document/product/436/33703)。

> !
> - 调用该请求时，请确保您有足够的权限对存储桶的清单任务进行操作。
> - 存储桶所有者默认拥有该权限，如您无该项权限，请先向存储桶所有者申请该项操作的权限。

## 请求

### 请求示例

```shell
DELETE /?inventory&id=inventory-configuration-id HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

调用 DELETE Bucket inventory 需要使用清单任务名称的参数。该参数格式如下：

| 参数 | 描述                                                         | 类型   | 必选 |
| ---- | ------------------------------------------------------------ | ------ | ---- |
| id   | 清单任务的名称。缺省值：None<br />合法字符：`a-z，A-Z，0-9，-，_，. `| String | 是   |

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

### 请求体

该请求的请求体为空。

## 响应

### 响应头

#### 公共响应头 

该响应使用公共响应头，了解公共请求头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

### 响应体

该响应体返回为空。

## 实际案例

### 请求

下述请求示例展示了从存储桶 examplebucket-1250000000 中删除清单任务 list1。

```shell
DELETE /?inventory&id=list1 HTTP/1.1
Date: Mon, 28 Aug 2018 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503901499;1503901859&q-key-time=1503901499;1503901859&q-header-list=host&q-url-param-list=inventory&q-signature=761f3f6449c6a11684464f4b09c6f292f0a4e7e0
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
```

### 响应

上述请求后，COS 返回 204 No Content 的响应表明已成功删除了该存储桶内的清单任务 list1。

```shell
HTTP/1.1 204 No Content 
Server: tencent-cos
Date: Mon, 28 Aug 2018 02:53:40 GMT
x-cos-id-2:0dfafa/DAPDIFdafdsfDdfSFFfdfKKJdafasiuKJK2
x-cos-request-id: NTlhM2I3M2JfMjQ4OGY3MGFfMWE1NF84ZTU=
```
