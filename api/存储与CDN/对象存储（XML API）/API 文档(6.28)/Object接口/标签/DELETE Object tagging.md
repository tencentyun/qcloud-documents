## 功能描述

DELETE Object tagging 接口用于删除指定对象下已有的对象标签。

如您使用子账号调用此项接口，请确保您已经在主账号处获取了`DELETE Object tagging `这个接口的权限。

**版本控制**

如果您的存储桶开启了版本控制，并且需要删除指定版本对象的标签，可以在发起请求时携带 VersionId 参数，此时将删除指定版本 ID 对象的对象标签集。

## 请求

#### 请求示例

```plaintext
DELETE /<ObjecKey>?tagging&VersionId=VersionId HTTP 1.1
Host:<BucketName-APPID>.cos.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

| 名称      | 描述                                                         | 类型   | 是否必选 |
| :-------- | :----------------------------------------------------------- | :----- | :------- |
| versionId | 当启用版本控制时，指定要操作的对象版本 ID，如不指定则删除最新版本对象的标签 | string | 否       |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该请求无特殊响应体信息。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 案例一：删除对象标签（未开启版本控制）

#### 请求

如下请求申请删除存储桶`examplebucket-1250000000`中的对象`exampleobject.txt`下已有的标签信息。COS 解析该请求后删除该对象中的所有标签。

```plaintext
DELETE /exampleobject.txt?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Authorization: Auth String
Content-Length: 0
Content-Type: application/xml
```

#### 响应

```plaintext
HTTP/1.1 204 No Content
Content-Type: application/xml
Connection: close
Date: Fri, 19 Jan 2020 11:40:22 GMT
```

### 案例二：删除对象标签（开启版本控制）

#### 请求

如下请求申请删除存储桶`examplebucket-1250000000`中的对象`exampleobject.txt`下已有的标签信息，删除时指定对象版本号为`MTg0NDUxNTgwODg2MTEzMTQyOTI `。COS解析该请求后删除该版本的对象中的所有标签。

```plaintext
DELETE /exampleobject.txt?tagging&VersionId=MTg0NDUxNTgwODg2MTEzMTQyOTI  HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Authorization: Auth String
Content-Length: 0
Content-Type: application/xml
```

#### 响应

```plaintext
HTTP/1.1 204 No Content
Content-Type: application/xml
Connection: close
Date: Fri, 19 Jan 2020 11:45:22 GMT
```
