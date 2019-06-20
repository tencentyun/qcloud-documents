
野鹤
运营一片闲云

查找系统/模块

查找系统/模块
最常使用
闲云
官网内容运营
专栏
控制台运营
社区
开发者实验室
消息中心
问答运营
官网文档中心
官网入门中心
腾讯云账号运营
社区线下活动
官网工具运营
专属实验室
腾讯云学院
国际站官网运营
移动端运营
官网 TVP 管理
日志工具
控制台监控
访问管理(CAM)
官网监控
社区沙龙
故障诊断
社区审核
实名认证工具
控制台业务自助运营
## 功能描述
GET Bucket versioning 接口实现获得存储桶的版本控制信息。
### 细节分析
1. 获取存储桶版本控制的状态，需要有该存储桶的读权限。
2. 有三种版本控制状态：未启用版本控制、启用版本控制和暂停版本控制。
  - 如果您从未在存储桶上启用（或暂停）版本控制，则响应为：
```shell
<VersioningConfiguration/>
```
  - 如果您启用了存储桶的版本控制功能，则响应为：
```shell
<VersioningConfiguration>
    <Status>Enabled</Status>
</VersioningConfiguration>
```
  - 如果您暂停了存储桶的版本控制功能，则响应为：
```shell
<VersioningConfiguration>
    <Status>Suspended</Status>
</VersioningConfiguration>
```
​
​
## 请求
### 请求示例
​
```shell
GET /?versioning HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
```
​
> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
​
### 请求头
​
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。
​
#### 非公共头部
该请求操作无特殊的请求头部信息。
​
### 请求体
该请求的请求体为空。
​
## 响应
​
### 响应头
#### 公共响应头 
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应无特殊的响应头。
​
功能描述
细节分析
请求
请求示例
请求头
请求体
响应
响应头
响应体
实际案例
响应
功能描述
GET Bucket versioning 接口实现获得存储桶的版本控制信息。

细节分析
获取存储桶版本控制的状态，需要有该存储桶的读权限。
有三种版本控制状态：未启用版本控制、启用版本控制和暂停版本控制。
如果您从未在存储桶上启用（或暂停）版本控制，则响应为：
<VersioningConfiguration/>
如果您启用了存储桶的版本控制功能，则响应为：
<VersioningConfiguration>
  <Status>Enabled</Status>
</VersioningConfiguration>
如果您暂停了存储桶的版本控制功能，则响应为：
<VersioningConfiguration>
  <Status>Suspended</Status>
</VersioningConfiguration>
请求
请求示例
GET /?versioning HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
Authorization: Auth String（详情请参阅 请求签名 文档）。

请求头
公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 公共请求头部 文档。

非公共头部
该请求操作无特殊的请求头部信息。

请求体
该请求的请求体为空。

响应
响应头
公共响应头
该响应包含公共响应头，了解公共响应头详情请参阅 公共响应头部 文档。

特有响应头
该响应无特殊的响应头。

响应体
<VersioningConfiguration>
    <Status></Status>
</VersioningConfiguration>
具体的数据内容如下：

节点名称（关键字）	父节点	描述	类型
VersioningConfiguration	无	说明版本控制的具体信息	Container
Status	VersioningConfiguration	说明版本是否开启，枚举值：Suspended\Enabled	Enum
实际案例
GET /?versioning HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9Sm****&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=5118a936049f9d44482bbb61309235cf4abe****
响应
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 120
Connection: keep-alive
Date: Wed, 23 Aug 2017 08:15:16 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5OTRfZDNhZDM1MGFfMjYyMTFfZmU3****

<?xml version='1.0' encoding='utf-8' ?>
<VersioningConfiguration>
    <Status>Enabled</Status>
</VersioningConfiguration>
