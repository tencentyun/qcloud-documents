## 功能描述
用于获取媒体文件的某个时间的截图，输出的截图统一为 jpeg 格式。

## 请求
#### 请求示例

```shell
POST /snapshot HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-type: application/xml

<body>
```

>?Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体
该 API 接口请求的请求体具体节点内容为：

```shell
<Request>
  <Input>
    <Object></Object>
  </Input>
  <Time></Time>
  <Output>
    <Region></Region>
    <Bucket></Bucket>
    <Object></Object>
  </Output>
</Request>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|是否必选|
|:---|:-- |:--|:--|:--|
| Request |无| 保存 GET Snapshot 请求的容器 | Container |是|

Container 节点 Request 的内容：

|节点名称（关键字）|父节点|描述|类型|是否必选|
|:---|:-- |:--|:--|:--|
| Input | Request | 媒体文件的位置信息 |  Container |是|
| Time | Request | 截图媒体文件哪个时间点的内容，单位为秒 | Float |是|
| Output | Request | 截图保存的位置信息 |  Container |是|

Container 节点 Input 的内容：

| 节点名称（关键字） | 父节点        | 描述        | 类型   | 是否必选 |
| :----------------- | :------------ | :---------- | :----- | :--- |
| Object             | Request.Input | 文件的名称 | String | 是   |

Container 节点 Output 的内容：

|节点名称（关键字）|父节点|描述|类型|是否必选|
|:---|:-- |:--|:--|:--|
| Region | Request.Output | 文件所在的地域 |  String |是|
| Bucket | Request.Output | 文件所属的 COS 存储桶 |  String |是|
| Object | Request.Output | 文件的名称 |  String |是|


## 响应
#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
  <Output>
    <Region></Region>
    <Bucket></Bucket>
    <Object></Object>
  </Output>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Output | Request | 截图保存的位置信息 |  Container |

Container 节点 Output 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Region | Response.Output | 文件所在的地域 |  String |
| Bucket | Response.Output | 文件所属的 COS 存储桶 |  String |
| Object | Response.Output | 文件的名字 |  String |

#### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

#### 请求
```shell
POST /snapshot HTTP/1.1
Host: bucket-1250000000.ci.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b40652
Content-Length: 552
Content-Type: application/xml

<Request>
  <Input>
    <Object>/video-for-test.mp4</Object>
  </Input>
  <Time>10</Time>
  <Output>
    <Region>ap-beijing</Region>
    <Bucket>ci-output-1250000000</Bucket>
    <Object>/snapshot/video-for-test-snapshot.jpg</Object>
  </Output>
</Request>
```

#### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 266
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-ci
x-ci-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==

<Response>
  <Output>
    <Region>ap-beijing</Region>
    <Bucket>ci-output-1250000000</Bucket>
    <Object>/snapshot/video-for-test-snapshot.jpg</Object>
  </Output>
</Response>
```

