## 文件上传接口说明

### 上传小文件（小于5MB）使用的 API
1. [简单上传文件](/document/api/436/7749)

### 上传大文件（大于5MB）使用的 API
1. [初始化分片上传](/document/api/436/7746)
2. [逐个上传分片](/document/api/436/7750)
3. [结束上传分片](/document/api/436/7742)

## 功能说明
1. 上传媒体（和封面）文件。
2. API 在服务端上传位于哪个步骤请参考[服务端上传综述](/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B)。

## SDK
建议使用[封装的 SDK](/document/product/436/6474) 进行 API 的调用。

## 使用方式

使用方式可以参考以上各 API 链接中的文档，各 API 的语法为：
```
PUT <ObjectName> HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

语法中的以下变量取值 [ VOD 申请上传的返回结果](/document/product/266/31767)：  

`<ObjectName>`为 **MediaStoragePath** （对于封面文件为 **CoverStoragePath** ） 

`<BucketName>-<APPID>`为 **StorageBucket** 

`<Region>`为 **StorageRegion**

对于 API 请求需要注意下面两点：

1. Authorization 签名使用[ VOD 申请上传返回结果](/document/product/266/31767)中 **TempCertificate**的 SecretId 和 SecretKey 按照[签名文档](/document/api/436/7778)指引进行计算
2. 在 HTTP 头部或 POST 请求包的 form-data 中传入 **x-cos-security-token** 字段标识该请求使用的安全令牌，并赋值等于 **TempCertificate** 的 Token 字段
