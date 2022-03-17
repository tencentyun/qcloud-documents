## 功能描述
GetSnapshot 接口用于获取媒体文件某个时间的截图。

## 请求

#### 请求示例

```shell
GET /for-test.mp4?ci-process=snapshot&time=1&format=jpg HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>

```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求参数

参数说明如下：

|参数名称|描述|类型|必选|
|:---|:--|:--|:--|
| ci-process | 操作类型，固定使用 snapshot | String |是|
| time | 截图的时间点，单位为秒 | float |是|
| width | 截图的宽。默认为0 | Int |否|
| height | 截图的高。默认为0<br/>width 和 height 都为0时表示使用视频的宽高，如果单个为0，则以另外一个值按视频宽高比例自动适应 | Int |否|
| format | 截图的格式，支持 jpg 和 png，默认 jpg | String |否|
| rotate | 图片旋转方式<br/><li>auto：按视频旋转信息进行自动旋转<br/><li>off：不旋转<br/>默认值为 auto | String |否|
| mode | 截帧方式<br/><li>keyframe：截取指定时间点之前的最近的一个关键帧<br><li>exactframe：截取指定时间点的帧<br/>默认值为 exactframe | String |否|


#### 请求体
该请求无请求体。


## 响应

#### 响应头

该响应包含公共响应头，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体为截图文件内容。

#### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
GET /for-test.mp4?ci-process=snapshot&time=1.5 HTTP/1.1
Host: bucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfG****-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b40652
Content-Length: 0
```
#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 266005
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==

<图片内容>
```
