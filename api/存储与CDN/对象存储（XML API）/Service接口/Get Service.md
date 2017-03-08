## 功能描述
Get Service接口实现获取该用户下所有Bucket列表。该API接口需要使用Authorization签名认证，且只能获取签名中AccessID所属账户的Bucket列表。

## 请求

### 请求语法

```HTTP
GET / HTTP 1.1
Host:service.cos.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称                     | 描述                                       | 类型        |
| ---------------------- | ---------------------------------------- | --------- |
| ListAllMyBucketsResult | 说明本次返回的所有信息                              | Container |
| Owner                  | 说明Bucket所有者的信息<br/>父节点：ListAllMyBucketsResult | Contianer |
| UIN                    | Bucket所有者的UIN<br/>父节点：ListAllMyBucketsResult.Owner | String    |
| Buckets                | 说明本次返回的Bucket列表的所有信息<br/>父节点：ListAllMyBucketsResult | Contianer |
| Bucket                 | 单个Bucket的信息<br/>父节点：ListAllMyBucketsResult.Buckets | Contianer |
| Name                   | Bucket名称<br/>父节点：ListAllMyBucketsResult.Buckets.Bucket | String    |
|Location                | Bucket所在区域，枚举值：china-east，china-south，china-north，china-southwest | String    |
| CreateDate             | Bucket创建时间，ISO8601格式，例如 2016-11-09T08:46:32.000Z<br/>父节点：ListAllMyBucketsResult.Buckets.Bucket | Date      |

```XML
<ListAllMyBucketsResult>
  <Owner>
    <UIN></UIN>
  </Owner>
  <Buckets>
    <Bucket>
      <Name></Name>
      <Location></Location>
      <CreateDate></CreateDate>
    </Bucket>
   ...
  </Buckets>
</ListAllMyBucketsResult>
```

## 示例

### 请求

```XML

GET / HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817623;32557713623&q-key-time=1484817623;32557713623&q-header-list=host&q-url-param-list=&q-signature=9ef0c2ad86045f67d03b43cc4359ef861605390e
> 

```

### 返回

```XML

HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 428
Connection: keep-alive
Date: Thu Jan 19 17:20:30 2017
Server: tencent-cos
x-cos-request-id: NTg4MDg0ZGVfOTkxZjRlXzEwOGVfZjdh

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>arlenhuangtestsgnoversion</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>ObjectName</Key>
		<LastModified>Wed Jan 18 16:58:13 2017</LastModified>
		<ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
		<Size>10485760</Size>
	</Contents>
</ListBucketResult>

```


