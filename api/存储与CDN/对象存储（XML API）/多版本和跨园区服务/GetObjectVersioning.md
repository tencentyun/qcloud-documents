
## 功能描述
<!-- 描述该 API 的功能、背景、条件等-->
Get Bucket Versioning 获得版本控制信息。
## 请求
<!-- 完整结构的请求语法示例，包括请求行、请求头、请求体。请求行中要有必选参数，非必选的不用写-->
语法示例：
```
GET /?versioning HTTP 1.1
Host:<Bucketname>-<APPID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```
<!-- 代码块中注意：
       1. HTTP 是全大写；
       2. 每一个冒号后面都有一个空格；
       3. Dete 格式是 GMT Date；
       4. Authorization 统一为 Auth String -->
> Authorization: Auth String (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
<!-- 将以上完整结构的请求语法示例中的请求行单独描述说明-->
```
GET /?versioning HTTP 1.1
```
该 API 接口接受 GET请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
<!-- 如果实际 API 中没有非公共头部内容，表述的语句为：该请求操作无特殊的请求头部信息。
并且以下“必选头部”、“推荐头部”和“权限相关头部”都不用说明。-->
该请求操作无特殊的请求头部信息。

### 请求体<!-- 如果实际 API 中没有请求体,表述的语句为：该请求的请求体为空。-->
该请求的请求体为空。



## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体<!-- 如果实际 API 中没有请求体,表述的语句为：该响应体返回为空。-->
```
<VersioningConfiguration>
	<Status>Enabled</Status>
</VersioningConfiguration>
```
具体的数据内容如下：

| 节点名称（关键字）                | 父节点               | 描述    | 类型   |
| --------------------------------------- | --------------------- | --------- | ------- |
| VersioningConfiguration |        无                                   |说明版本控制的具体信息    | Container    |
| Status                            |    VersioningConfiguration      | 说明版本是否开启，枚举值：Suspended\|Enabled  | Enum         |


## 实际案例
```
GET /?versioning HTTP/1.1
Host: testbucket-1352548703.cn-north.myqcloud.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9SmuG00&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=5118a936049f9d44482bbb61309235cf4abe99c2
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 120
Connection: keep-alive
Date: Wed, 23 Aug 2017 08:15:16 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5OTRfZDNhZDM1MGFfMjYyMTFfZmU3NWQ=

<?xml version='1.0' encoding='utf-8' ?>
<VersioningConfiguration>
	<Status>Enabled</Status>
</VersioningConfiguration>
```
