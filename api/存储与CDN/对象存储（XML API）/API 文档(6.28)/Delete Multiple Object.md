## 功能描述
Delete Multiple Object 接口请求实现在指定 Bucket 中批量删除 Object，单次请求最大支持批量删除 1000 个 Object。对于响应结果，COS 提供 Verbose 和 Quiet 两种模式：Verbose 模式将返回每个 Object 的删除结果；Quiet 模式只返回报错的 Object 信息。
>** 注：此请求必须携带 Content-MD5 用来校验 Body 的完整性。**

## 请求

语法示例：
```
POST /?delete HTTP/1.1
Host: <Bucketname>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: authorization string

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

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
POST /?delete HTTP/1.1
```
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 `delete`。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**
该请求操作需要请求头帯必选头部参数，具体内容如下：

|名称|描述|类型|必选|
|:---|:---|:---|:---|
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）| String | 是 |
| Content-MD5 | RFC 1864 中定义的 128位 内容 MD5 算法校验值| String | 是 |

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
| Quiet | Delete|布尔值，这个值决定了是否启动 Quiet 模式。<br> 值为 True 启动 Quiet 模式，值为 False 则启动 Verbose 模式，默认值为 False | Boolean | 否 |
| Object |Delete |RFC 1864 中定义的 128位 内容 MD5 算法校验值| Container | 是 |
| Key | Delete.Object |文件名称| String | 是 |


## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该请求操作无特殊的响应头。


#### 响应体
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
POST /coss3/?delete HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Content-MD5: 35385efb5ba5134bffb192bfa17c3d5e
Authorization: q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487065662;32466649662&q-key-time=1487065662;32559961662&q-header-list=host&q-url-param-list=delete&q-signature=286ef48c81f1652c37c635f0fb7db7a2150aa5ba
Content-Length: 75
Content-Type: application/x-www-form-urlencoded

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 79
Connection: keep-alive
Date: Wed, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NThhMmQyOTdfMmM4OGY3XzZjZGFfY2Mx

<DeleteResult>
    <Deleted>
        <Key>ObjectName</Key>
    </Deleted>
</DeleteResult>

```
