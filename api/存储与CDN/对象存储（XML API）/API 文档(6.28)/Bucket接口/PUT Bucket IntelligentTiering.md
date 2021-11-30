## 功能描述

PUT Bucket IntelligentTiering 接口用于启用存储桶的智能分层存储配置。

> ?
> - 启用智能分层配置后，将无法关闭或修改。
> - 只有主账号或者被授权 PUT Bucket IntelligentTiering 接口权限的子账号可以调用该接口。
> - 您可以通过 [查询对象元数据](https://cloud.tencent.com/document/product/436/7745) 接口返回的`x-cos-storage-tier`获取对象所处的存储层。

## 请求

#### 请求示例

```plaintext
PUT /?intelligenttiering HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Connection: keep-alive
Authorization: authorization string
Content-Type: text/plain
Content-Length: Int
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

```shell
<IntelligentTieringConfiguration xmlns="cos xmlns/"> 
  <Status>Enabled</Status>
  <Transition>
    <Days>30|60|90</Days>
    <RequestFrequent>1</RequestFrequent>
  </Transition>
</IntelligentTieringConfiguration>
```

具体的数据内容如下：

| 名称                            | 父节点                                     | 描述                                                         | 类型      | 是否必选 |
| ------------------------------- | ------------------------------------------ | ------------------------------------------------------------ | --------- | -------- |
| IntelligentTieringConfiguration | 无                                         | 智能分层存储配置的具体信息                                   | Container | 是       |
| Status                          | IntelligentTieringConfiguration            | 说明智能分层存储配置是否开启，枚举值：Suspended、Enabled     | Enum      | 是       |
| Transition                      | IntelligentTieringConfiguration            | 指定智能分层存储配置中有关数据转换的配置信息                 | Container | 是       |
| Days                            | IntelligentTieringConfiguration.Transition | 指定智能分层存储配置中标准层数据转换为低频层数据的天数限制，默认值为30天 | Int       | 是       |
|  RequestFrequent                | IntelligentTieringConfiguration.Transition | 指定配置中标准层数据转换为低频层数据的访问次数限制，默认值为1次，和天数搭配使用可以实现转换效果。例如设置该参数为1，访问天数为30，代表连续30天访问次数小于1次的对象会从标准层降到低频层  |  Int  |  是  |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
PUT /?intelligenttiering HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Content-Type: application/xml
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9Sm****&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=47ec2b80c73788ecd394d3b9ad90e120a32f****
Content-Length: 83

<IntelligentTieringConfiguration xmlns="cos xmlns/"> 
  <Status>Enabled</Status>
  <Transition>
    <Days>30</Days>
    <RequestFrequent>1</RequestFrequent>
  </Transition>
</IntelligentTieringConfiguration>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Sun, 23 Aug 2020 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0****
```
