## 功能描述
Delete Multiple Object 接口请求实现在指定 Bucket 中批量删除 Object，单次请求最大支持批量删除 1000 个 Object。对于响应结果，COS 提供 Verbose 和 Quiet 两种模式：Verbose 模式将返回每个 Object 的删除结果；Quiet 模式只返回报错的 Object 信息。
><font color="#0000cc">**注意：** </font>
>此请求必须携带 Content-MD5 用来校验 Body 的完整性。

## 请求

语法示例：
```
POST /?delete HTTP/1.1
Host: <Bucketname>-<AppID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String

<Delete>
  <Quiet></Quiet>
  <Object>
    <Key></Key>
  </Object>
  <Object>
    <Key></Key>
  </Object>
  ...
</Delete>

```

> Authorization: Auth String (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
POST /?delete HTTP/1.1
```
该 API 接口接受 POST 请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**
该请求操作的实现使用如下必选头部：
<style rel="stylesheet"> table th:nth-of-type(1) { width: 200px;	} </style>

|名称|描述|类型|必选|
|:---|:---|:---|:---|
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）| String | 是 |
| Content-MD5 | RFC 1864 中定义的经过 Base64 编码的 128-bit 内容 MD5 校验值。此头部用来校验文件内容是否发生变化| String | 是 |

### 请求体
该请求的请求体具体节点内容为：
```
<Delete>
  <Quiet></Quiet>
  <Object>
    <Key></Key>
  </Object>
  <Object>
    <Key></Key>
  </Object>
  ...
</Delete>

```
具体内容描述如下：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:---|:---|:---|:---|
| Delete |无| 说明本次删除的返回结果方式和目标 Object | Container | 是 |
| Quiet | Delete|布尔值，这个值决定了是否启动 Quiet 模式。<br> 值为 true 启动 Quiet 模式，值为 false 则启动 Verbose 模式，默认值为 False | Boolean | 否 |
| Object |Delete |说明每个将要删除的目标 Object 信息| Container | 是 |
| Key | Delete.Object |目标 Object 文件名称| String | 是 |


## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
#### 特有响应头
该请求操作无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<DeleteResult>
  <Deleted>
    <Key></Key>
  </Deleted>
  <Error>
    <Key></Key>
    <Code></Code>
    <Message></Message>
  </Error>
</DeleteResult>
```
具体内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:---|:---|:---|
| DeleteResult |无| 说明本次删除返回结果的方式和目标 Object | Container | 

Container 节点 DeleteResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:---|:---|:---|
| Deleted | DeleteResult |说明本次删除的成功 Object 信息 | Boolean | 
| Error| DeleteResult | 说明本次删除的失败 Object 信息 | Container | 

Container 节点 Deleted 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:---|:---|:---|
| Key | DeleteResult.Deleted | Object 的名称 | String |

Container 节点 Error 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:---|:---|:---|
| Key | DeleteResult.Error | 删除失败的 Object 的名称 | String |
| Code  | DeleteResult.Error | 删除失败的错误代码 | String |
| Message | DeleteResult.Error | 删除失败的错误信息 | String |

## 实际案例

### 请求
```
POST /?delete HTTP/1.1
Host: lelu06-1252400000.cn-north.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9SmuG00&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=delete&q-header-list=host&q-signature=c54f22fd92232a76972ba599cba25a8a733d2fef
Content-MD5: yoLiNjQuvB7lu8cEmPafrQ==
Content-Length: 125

<Delete>
  <Quiet>true</Quiet>
  <Object>
    <Key>aa</Key>
  </Object>
  <Object>
    <Key>aaa</Key>
  </Object>
</Delete>

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 17
Connection: keep-alive
Date: Tue, 22 Aug 2017 12:00:48 GMT
Server: tencent-cos
x-cos-request-id: NTk5YzFjZjBfZWFhZDM1MGFfMjkwZV9lZGM3ZQ==

<DeleteResult/>
```

### 请求
```
POST /?delete HTTP/1.1
Host: lelu06-1252440000.cn-north.myqcloud.com
Date: Tue, 22 Aug 2017 12:16:35 GMT
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9SmuG00&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=delete&q-header-list=host&q-signature=c54f22fd92232a76972ba599cba25a8a733d2fef
Content-MD5: V0XuU8V7aqMYeWyD3BC2nQ==
Content-Length: 126

<Delete>
  <Quiet>false</Quiet>
  <Object>
    <Key>aa</Key>
  </Object>
  <Object>
    <Key>aaa</Key>
  </Object>
</Delete>

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 111
Connection: keep-alive
Date: Tue, 22 Aug 2017 12:16:35 GMT
Server: tencent-cos
x-cos-request-id: NTk5YzIwYTNfMzFhYzM1MGFfMmNmOWZfZWVhNjQ=

<DeleteResult>
 <Deleted>
  <Key>aa</Key>
 </Deleted>
 <Deleted>
  <Key>aaa</Key>
 </Deleted>
</DeleteResult>

```

