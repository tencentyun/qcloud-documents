## 功能描述
Delete Multiple Object请求实现批量删除文件，最大支持单次删除1000个文件。对于返回结果，COS提供Verbose和Quiet两种结果模式。Verbose模式将返回每个Object的删除结果；Quiet模式只返回报错的Object信息。

此请求必须携带x-cos-sha1用来校验Body的完整性。

## 请求

### 请求语法

```Http
POST /?delete HTTP/1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date: date
Content-Length:length
Content-Type:application/xml
Content-MD5:MD5
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

### 请求参数

无特殊请求参数

### 请求头部

#### 必选头部

| 名称             | 描述                               | 类型     | 必须   |
| -------------- | -------------------------------- | ------ | ---- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）。   | String | 是    |
| Content-MD5    | RFC 1864 中定义的 128位 内容 MD5 算法校验值。 | String | 是    |

### 请求内容

| 名称     | 描述                                       | 类型        | 必须   |
| ------ | ---------------------------------------- | --------- | ---- |
| Delete | 说明本次删除的返回结果方式和目标Object                   | Container | 是    |
| Quiet  | 布尔值，这个值决定了是否启动Quiet模式，True启动Quiet模式，False启动Verbose模式，默认False<Br/>父节点：Delete | Boolean   | 否    |
| Object | 说明每个将要删除的目标文件信息                          | Container | 是    |
| Key    | 目标文件名                                    | String    | 是    |

```xml
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


## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称           | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |
| DeleteResult | 说明本次删除的返回结果                           | Container |
| Deleted      | 说明本次删除的成功Object信息<Br/>父节点：DeleteResult | Container |
| Key          | Object的名称<Br/>父节点：Deleted，Error       | String    |
| Error        | 说明本次删除的失败Object信息<Br/>父节点：DeleteResult | Container |
| Code         | 删除失败的错误码                              | String    |
| Message      | 删除错误信息                                | String    |

```xml
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
## 示例
### 请求
```http
POST /coss3/?delete HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Content-MD5:35385efb5ba5134bffb192bfa17c3d5e
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487065662;32466649662&q-key-time=1487065662;32559961662&q-header-list=host&q-url-param-list=delete&q-signature=286ef48c81f1652c37c635f0fb7db7a2150aa5ba
Content-Length: 75
Content-Type: application/x-www-form-urlencoded
```
### 返回
```http
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 79
Connection: keep-alive
Date: Tue Feb 14 17:49:12 2017
Server: tencent-cos
x-cos-request-id: NThhMmQyOTdfMmM4OGY3XzZjZGFfY2Mx

<DeleteResult>
	<Deleted>
		<Key>ObjectName</Key>
	</Deleted>
</DeleteResult>

```

