## 功能概述

PUT Bucket Origin 接口用于设置 Bucket 的回源。

## 请求

### 请求示例

```http
PUT /?origin HTTP 1.1
Host:<BucketName-APPID>.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```

> - Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 该请求需结合请求体一起使用。

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

无特殊请求头部。

### 请求体

请求的请求体为回源规则。

```http
<?xml version="1.0" encoding="UTF-8"?>
<OriginConfiguration>
  <OriginRule>
    <OriginType>Redirect</OriginType>
    <OriginInfo>
      <Protocol>HTTP</Protocol>
      <HostName>examplebucket.test.xyz</HostName>
    </OriginInfo>
    <HttpRedirectCode>302</HttpRedirectCode>
  </OriginRule>
</OriginConfiguration>
```

具体的数据内容如下：

| 节点名称（关键字）  | 父节点 | 描述            | 类型      | 必选 |
| :------------------ | :----- | :-------------- | :-------- | :--- |
| OriginConfiguration | 无     | Origin 回源配置 | Container | 是   |

Container 节点 OriginConfiguration 的内容：

| 节点名称（关键字） | 父节点              | 描述                | 类型      | 必选 |
| :----------------- | :------------------ | :------------------ | :-------- | :--- |
| OriginRule         | OriginConfiguration | 支持一条 OriginRule | Container | 是   |

Container 节点 OriginRule 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| OriginType         | OriginConfiguration.OriginRule | 回源类型 枚举值：Redirect                        | Container | 是   |
| Prefix             | OriginConfiguration.OriginRule | 回源作用的目录，默认为根目录，如果设置，不能为空 | String    | 否   |
| OriginInfo         | OriginConfiguration.OriginRule | 回源地址相关信息                                 | Container | 是   |
| HttpRedirectCode   | OriginConfiguration.OriginRule | 重定向后的请求返回码，目前只支持302              | String    | 否   |

Container 节点 OriginInfo 的内容：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>必选</th>
   </tr>
   <tr>
      <td>Protocol</td>
      <td>OriginConfiguration.OriginRule.OriginInfo</td>
      <td>回源使用的协议，目前只支持 HTTP</td>
      <td>String</td>
      <td>是</td>
   </tr>
   <tr>
      <td>HostName</td>
      <td>OriginConfiguration.OriginRule.OriginInfo</td>
			<td>回源地址，填入地址时只需填入域名或 IP 地址，无需带前缀<code>http://</code>，亦支持以<code>:[port]</code>方式填写对应的端口号，<code>:</code>使用英文字符，注意内网 IP 无效</td>
      <td>String</td>
      <td>是</td>
   </tr>
</table>

## 响应

### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

### 响应体

该响应体为空。

### 错误码

| 错误码/返回码         | 描述                                   | HTTP 状态码     |
| --------------------- | -------------------------------------- | --------------- |
| InvalidArgument       | 提供的参数错误                         | 400 Bad Request |
| SignatureDoesNotMatch | 提供的签名不符合规则，返回该错误码     | 403 Forbidden   |
| NoSuchKey             | 如果设置的 Bucket 不存在，返回该错误码 | 404 Not Found   |

## 实际案例

### 请求

```http
PUT /?origin= HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d00dc
Content-Length: 347

<?xml version="1.0" encoding="UTF-8"?>
<OriginConfiguration>
  <OriginRule>
    <OriginType>Redirect</OriginType>
    <OriginInfo>
      <Protocol>HTTP</Protocol>
      <HostName>examplebucket.test.xyz</HostName>
    </OriginInfo>
    <HttpRedirectCode>302</HttpRedirectCode>
  </OriginRule>
</OriginConfiguration>
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Sun, 28 Apr 2019 12:02:25 GMT
Server: tencent-cos
x-cos-request-id: NWNjNTk2NTFfMmM4OGY3MGFfNTI1X2Y2NmU=
```
