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

