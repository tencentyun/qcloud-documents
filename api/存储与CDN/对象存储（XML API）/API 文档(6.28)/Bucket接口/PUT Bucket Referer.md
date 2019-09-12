## 功能描述

PUT Bucket referer 接口用于为存储桶设置 Referer 白名单或者黑名单。

## 请求

#### 请求示例

```shell
PUT /?referer HTTP 1.1
Host:<BucketName-APPID>.<Region>.myqcloud.com
Date:GMT Date
Authorization: Auth String
Content-Length:length
Content-MD5:MD5
```

>?Authorization：Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。 

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

**必选头部**

<table>
   <tr>
      <th>名称</th>
      <th>描述</th>
      <th>类型</th>
      <th>必选</th>
   </tr>
   <tr>
      <td nowrap="nowrap">Content-Length</td>
      <td>RFC 2616中定义的 HTTP 请求内容长度（字节）</td>
      <td>String</td>
      <td>是</td>
   </tr>
   <tr>
      <td>Content-MD5</td>
      <td>RFC 1864中定义的经过 Base64 编码的 128-bit 内容 MD5 校验值，此头部用来校验文件内容是否发生变化</td>
      <td>String</td>
      <td>是</td>
   </tr>
</table>

该请求操作无特殊的请求头部信息。

#### 请求体

该请求的请求体具体节点内容为：

```shell
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

具体内容描述如下：

| 名称                    | 父节点               | 描述                                                         | 类型      | 必选 |
| ----------------------- | -------------------- | ------------------------------------------------------------ | --------- | ---- |
| RefererConfiguration    | 无                   | 防盗链配置信息                                               | Container | 是   |
| Status                  | RefererConfiguration | 是否开启防盗链，枚举值：Enabled、Disabled                | String    | 是   |
| RefererType             | RefererConfiguration | 防盗链类型，枚举值：Black-List、White-List               | String    | 是   |
| DomainList              | RefererConfiguration | 生效域名列表， 支持多个域名且为前缀匹配， 支持带端口的域名和 IP， 支持通配符`*`，做二级域名或多级域名的通配 | Container | 是   |
| Domain                  | DomainList           | 单条生效域名<br>例如`www.qq.com/example`，`192.168.1.2:8080`， `*.qq.com` | String    | 是   |
| EmptyReferConfiguration | RefererConfiguration | 是否允许空 Refer 访问，枚举值：Allow、Deny，默认值为 Deny | String    | 否   |


## 响应

#### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

#### 响应体

该响应体为空。

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
PUT /?referer HTTP 1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2017 04:10:22 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1547105134;32526689134&q-key-time=1547105134;32620001134&q-header-list=content-md5;content-type;host&q-url-param-list=referer&q-signature=0f7fef5b1d2180deaf6f92fa2ee0cf87ae83f0cd\
Content-MD5: kOz7g54LMJZjxKs070V9jQ==
Content-Type: application/xml

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

#### 响应

```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: keep-alive
Date: Fri, 25 Feb 2017 04:10:22 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw
```
