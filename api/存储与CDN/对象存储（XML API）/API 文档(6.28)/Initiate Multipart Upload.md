## 功能描述
Initiate Multipart Upload 接口请求实现初始化分片上传，成功执行此请求以后会返回 UploadId 用于后续的 Upload Part 请求。

## 请求

语法示例：
```
POST /Object?uploads HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth
```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
POST /Object?uploads HTTP/1.1
```
该 API 接口接受 POST 请求。

#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 Object?uploads。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**推荐头部**
该请求操作推荐请求头使用推荐头部参数，具体内容如下：

|名称|描述|类型|必选|
|:---|:---|:---|:---|
| Cache-Control | RFC 2616 中定义的缓存策略，将作为 Object 元数据保存。| String | 否 |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为 Object 元数据保存。| String | 否 |
| Content-Encoding | RFC 2616 中定义的编码格式，将作为 Object 元数据保存。| String | 否 |
| Content-Type| RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存。| String | 否 |
| Expires | RFC 2616 中定义的文件名称，将作为 Object 元数据保存。| String | 否 |
| x-cos-meta-`*` | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K。 | String | 否 |
| x-cos-storage-class | 设置Object的存储级别，枚举值：Standard, Standard_IA, Nearline，默认值：Standard（目前只支持华南园区）| String | 否 |

**权限相关头部**
该请求操作的实现可以用 PUT 请求中的 `x-cos-acl` 头来设置 Object 访问权限。目前 Object 有三种访问权限：public-read-write，public-read 和 private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| x-cos-acl | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | String|  否 |
| x-cos-grant-read | 赋予被授权者读的权限。格式：x-cos-grant-read: uin=" ",uin=" "；</br> 当需要给子账户授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"`，当需要给根账户授权时，uin="RootAccountID" | String |  否 |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: uin=" ",uin=" "；</br>当需要给子账户授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"`，当需要给根账户授权时，uin="RootAccountID" |String |  否 |
| x-cos-grant-full-control | 赋予被授权者读写权限。格式：x-cos-grant-full-control: uin=" ",uin=" "；</br>当需要给子账户授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"`，当需要给根账户授权时，uin="RootAccountID" | String|  否 |

### 请求体
该请求的操作请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<InitiateMultipartUploadResult>
  <Bucket></Bucket>
  <Key></Key>
  <UploadId></UploadId>
</InitiateMultipartUploadResult>
```
具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| InitiateMultipartUploadResult |无| 说明所有返回信息 | Container |

Container 节点 InitiateMultipartUploadResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Bucket | InitiateMultipartUploadResult | 分片上传的目标 Bucket |  Container |
| Key | InitiateMultipartUploadResult | Object 的名称 |  Container |
| UploadId | InitiateMultipartUploadResult | 在后续上传中使用的 ID |  Container |

## 实际案例

### 请求
```
POST /ObjectName?uploads HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727259;32557623259&q-key-time=1484727259;32557623259&q-header-list=host&q-url-param-list=uploads&q-signature=b5f46c47379aeaee74be7578380b193c01b28045

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjIzZTZfOWIxZjRlXzZmMzhfMWRj

<InitiateMultipartUploadResult>
    <Bucket>arlenhuangtestsgnoversion</Bucket>
    <Key>ObjectName</Key>
    <UploadId>1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e</UploadId>
</InitiateMultipartUploadResult>
```
