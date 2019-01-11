## 功能描述

GET Bucket Referer 接口用于读取存储桶 Referer 白名单或者黑名单。

## 请求

### 请求示例

```HTTP
GET /?referer HTTP 1.1
Host:<BucketName-APPID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization：Auth String （详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

### 请求体

该请求的请求体为空。

## 响应

### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

### 响应体

该响应体返回为 application/xml 数据，包含完整节点数据的内容展示如下：

```XML
<RefererConfiguration>
  <Status></Status>
  <RefererType></RefererType>
  <DomainList>
    <Domain></Domain>
    <Domain></Domain>
  </DomainList>
  <EmptyReferConfiguration></EmptyReferConfiguration>
</RefererConfiguration>
```

具体的数据内容如下：

| 名称                    | 父节点               | 描述                                                         | 类型      | 必选 |
| ----------------------- | -------------------- | ------------------------------------------------------------ | --------- | ---- |
| RefererConfiguration    | 无                   | 防盗链配置信息                                               | Container | 是   |
| Status                  | RefererConfiguration | 是否开启防盗链，枚举值：Eabled，Disabled                 | String    | 是   |
| RefererType             | RefererConfiguration | 防盗链类型，枚举值：Black-List，White-List               | String    | 是   |
| DomainList              | RefererConfiguration | 生效域名列表。 支持多个域名且为前缀匹配， 支持带端口的域名和 IP， 支持通配符`* `，做二级域名或多级域名的通配 | Container | 是   |
| Domain                  | DomainList           | 单条生效域名，例如 `www.qq.com/example`，`192.168.1.2:8080`， `*.qq.com` | String    | 是   |
| EmptyReferConfiguration | RefererConfiguration | 是否允许空 Refer 访问，枚举值：Allow，Deny，默认值为 Deny | String    | 否   |

### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求

```HTTP
GET /?referer HTTP 1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2017 04:10:22 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1547105134;32526689134&q-key-time=1547105134;32620001134&q-header-list=content-md5;content-type;host&q-url-param-list=referer&q-signature=0f7fef5b1d2180deaf6f92fa2ee0cf87ae83f0cd
```

### 响应

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 260
Connection: keep-alive
Date: Fri, 25 Feb 2017 04:10:22 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw

<RefererConfiguration>
	<Status>Enabled</Status>
	<RefererType>White-List</RefererType>
	<DomainList>
		<Domain>*.qq.com</Domain>
		<Domain>*.qcloud.com</Domain>
	</DomainList>
	<EmptyReferConfiguration>Allow</EmptyReferConfiguration>
</RefererConfiguration>
```
