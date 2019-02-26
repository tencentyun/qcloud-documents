
## 功能描述
Put Bucket Replication 请求用于向开启版本管理的存储桶添加 replication 配置。如果存储桶已经拥有 replication 配置，那么该请求会替换现有配置。

>**注意：**
>使用该接口存储桶必须已经开启版本管理，版本管理详细请参见 [Put Bucket Versioning](https://cloud.tencent.com/document/product/436/8591)。

## 请求

语法示例：
```
PUT /?replication HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
Content-MD5: MD5

Replication configuration XML in the body
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行

```
PUT /?replication HTTP/1.1
```
该 API 接口接受 PUT 请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

| 名称               | 描述      | 类型     | 必选   |
| ---------------- | ----------- | ------ | ---- |
| Content-Length       | RFC 2616 中定义的 HTTP 请求内容长度（字节） | String | 是    |
| Content-MD5 | RFC 1864 中定义的经过 Base64 编码的 128-bit 内容 MD5 校验值。此头部用来校验文件内容是否发生变化 | String | 是    |


#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该 API 接口请求的请求体具体节点内容为：
```
<ReplicationConfiguration>
    <Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
    <Rule>
        <Status></Status>
        <ID></ID>
        <Prefix></Prefix>
        <Destination>
            <Bucket>qcs::cos:[Region]::[Bucketname-Appid]</Bucket>
        </Destination>
    </Rule>
</ReplicationConfiguration>
```
具体内容描述如下：

|节点名称（关键字）|    父节点|    描述    |类型|    必选|
|---|---|---|---|---|
|ReplicationConfiguration    |无    |说明所有跨区域配置信息    |Container    |是|
|Role|ReplicationConfiguration    |发起者身份标示：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>      |String    |是|
|Rule    |ReplicationConfiguration    |具体配置信息，最多支持 1000 个，所有策略只能指向一个目标存储桶    |Container    |是|
|ID    |ReplicationConfiguration.Rule    |用来标注具体 Rule 的名称    |String    |否|
|Status    |ReplicationConfiguration.Rule    |标识 Rule 是否生效，枚举值：Enabled, Disabled    |String    |是|
|Prefix    |ReplicationConfiguration.Rule    |前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空    |String    |是|
|Destination    |ReplicationConfiguration.Rule    |目标存储桶信息    |Container    |是|
|Bucket    |ReplicationConfiguration.Rule.Destination    |资源标识符：qcs::cos:[region]::[bucketname-AppId] |String    |是|
|StorageClass    |ReplicationConfiguration.Rule.Destination    |存储级别，枚举值：STANDARD, STANDARD_IA, NEARLINE；默认值：原存储桶级别    |String    |否|

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为空。

## 实际案例

### 请求
```
PUT /?replication HTTP/1.1
Date: Mon, 28 Aug 2017 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=replication&q-signature=254bf9cd3d6615e89a36ab652437f9d45c5f63f9
Content-MD5: AAq+9nzrpsz5LJ4UEe1f6Q==
Host: sevenyounorthtest-7319456.cos.ap-guangzhou.myqcloud.com
Content-Length: 312

<ReplicationConfiguration>
    <Role>qcs::cam::uin/123456789:uin/987654543</Role>
    <Rule>
        <Status>Enabled</Status>
        <ID>RuleId_01</ID>
        <Prefix>sevenyou_10m</Prefix>
        <Destination>
            <Bucket>qcs::cos:ap-guangzhou::sevenyousouthtest-132213432</Bucket>
        </Destination>
    </Rule>
</ReplicationConfiguration>

```

### 响应
```
HTTP/1.1 200 OK

Content-Type: application/xml
Content-Length: 0
Date: Mon, 28 Aug 2017 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF84Y2M
```

