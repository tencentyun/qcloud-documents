## 功能描述
DELETE Bucket replication 用来删除存储桶中的跨区域复制配置。用户发起该请求时需获得请求签名，表明该请求已获得许可。

## 请求
### 请求示例

```
DELETE /?replication HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。
### 请求体
该请求的请求体为空。

## 响应
### 响应头
#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体为空。

## 实际案例

### 请求
```
DELETE /?replication HTTP/1.1
Date: Mon, 28 Aug 2017 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503901499;1503901859&q-key-time=1503901499;1503901859&q-header-list=host&q-url-param-list=replication&q-signature=761f3f6449c6a11684464f4b09c6f292f0a4e7e0
Host: sevenyounorthtest-7319456.cos.ap-guangzhou.myqcloud.com
```

### 响应
```
HTTP/1.1 204 No Content 
Content-Type: application/xml
Content-Length: 0
Date: Mon, 28 Aug 2017 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhM2I3M2JfMjQ4OGY3MGFfMWE1NF84ZTU=
```
