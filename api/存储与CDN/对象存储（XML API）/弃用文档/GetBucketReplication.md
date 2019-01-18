## 功能描述

Get Bucket Replication 接口请求实现读取存储桶中用户跨区域复制配置信息。

## 请求
语法示例：
```
GET /?replication HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行

```
GET /?replication HTTP/1.1
```
该 API 接口接受 GET 请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<ReplicationConfiguration>
    <Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
    <Rule>
        <Status></Status>
        <ID></ID>
        <Prefix></Prefix>
        <Destination>
            <Bucket>qcs::cos:[Region]::[Bucketname-Appid]</Bucket>
            <StorageClass></StorageClass>
        </Destination>
    </Rule>
    <Rule>
        ...
    </Rule>
</ReplicationConfiguration>
```
具体内容描述如下：

|节点名称（关键字）|    父节点|    描述    |类型|    必选|
|---|---|---|---|---|
|ReplicationConfiguration    |无    |说明所有跨区域配置信息    |Container    |是|
|Role|ReplicationConfiguration    |发起者身份标示：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>  |String    |是|
|Rule    |ReplicationConfiguration    |具体配置信息，最多支持 1000 个，所有策略只能指向一个目标存储桶    |Container    |是|
|ID    |ReplicationConfiguration.Rule    |用来标注具体 Rule 的名称    |String    |否|
|Status    |ReplicationConfiguration.Rule    |标识 Rule 是否生效，枚举值：Enabled, Disabled    |String    |是|
|Prefix    |ReplicationConfiguration.Rule    |前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空    |String    |是|
|Destination    |ReplicationConfiguration.Rule    |目标存储桶信息    |Container    |是|
|Bucket    |ReplicationConfiguration.Rule.Destination    |资源标识符：qcs::cos:[region]::[bucketname-Appid]    |String    |是|
|StorageClass    |ReplicationConfiguration.Rule.Destination    |存储级别，枚举值：Standard, Standard_IA, Nearline；默认值：原存储桶级别    |String    |否|


## 实际案例

### 请求
```
GET /?replication HTTP/1.1
Date: Mon, 28 Aug 2017 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503895278;1503895638&q-key-time=1503895278;1503895638&q-header-list=host&q-url-param-list=replication&q-signature=f77900be432072b16afd8222b4b349aabd837cb9
Host: sevenyounorthtest-7319456.cos.cn-north.myqcloud.com
Content-Length: 0
```

### 响应
```
HTTP/1.1 200 OK

Content-Type: application/xml
Content-Length: 331
Date: Mon, 28 Aug 2017 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF84Y2M

<ReplicationConfiguration>
    <Role>qcs::cam::uin/491107630:uin/491107630</Role>
    <Rule>
        <ID>RuleId_01</ID>
        <Status>Enabled</Status>
        <Prefix>sevenyou_10m</Prefix>
        <Destination>
            <Bucket>qcs::cos:cn-south::sevenyousouthtest-7319456</Bucket>
            <StorageClass></StorageClass>
        </Destination>
    </Rule>
</ReplicationConfiguration>
```

