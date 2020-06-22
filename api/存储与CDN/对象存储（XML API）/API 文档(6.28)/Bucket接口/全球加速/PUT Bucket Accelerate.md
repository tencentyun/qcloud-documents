## 功能描述

PUT Bucket Accelerate 接口实现启用或者暂停存储桶的全球加速功能。

**细节分析**

1. 如果您从未在存储桶上启用过全球加速功能，则 GET Bucket Accelerate 请求不返回全球加速功能配置状态。
2. 开启全球加速功能功能后，只能暂停，不能关闭。
3. 设置全球加速功能状态值为 Enabled 或 Suspended，表示开启或暂停全球加速功能。
4. 如果您是子账号，需要设置存储桶的全球加速功能功能，您需要有该配置的写入权限。

## 请求

#### 请求示例

```shell
PUT /?accelerate HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

```shell
<AccelerateConfiguration xmlns="cos xmlns/"> 
  <Status>Enabled</Status> 
</AccelerateConfiguration>
```

具体的节点描述如下：

| 节点名称（关键字）      | 父节点                  | 描述                                                 | 类型      |
| ----------------------- | ----------------------- | ---------------------------------------------------- | --------- |
| AccelerateConfiguration | 无                      | 全球加速的具体信息                                   | Container |
| Status                  | AccelerateConfiguration | 说明全球加速功能是否开启，枚举值：Suspended、Enabled | Enum      |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。 

#### 响应体

该响应体返回为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

#### 请求

```shell
PUT /?accelerate HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Connection: keep-alive
Authorization: authorization string
Content-Type: text/plain
Content-Length: 83

<AccelerateConfiguration>
    <Status>Enabled</Status>
</AccelerateConfiguration>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Aug 2019 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0****
```
