## 功能描述
GET Object acl 接口用来获取某个存储桶下的某个对象的访问权限，只有存储桶的持有者才有权限操作。

## 版本
默认情况下，该 GET 操作返回对象的当前版本。您如果需要返回不同的版本，请使用 version Id 子资源。

## 请求
#### 语法示例

**shell:** 

```shell
# You can also use curl
curl -X GET http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}/?acl \
  -H 'Accept: application/xml'

```

**http:** 

```http
GET http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}/?acl HTTP/1.1
Host: 

Accept: application/xml

```

### 请求行

```
GET /{ObjectName}/?acl HTTP/1.1
```

该 API 接口接受 `GET` 请求。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部


该请求操作无特殊的请求头部信息。

### 请求体
该请求请求体为空。
## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头


该请求操作无特殊的响应头部信息。

### 响应体
获取 ACL 配置成功。
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<AccessControlPolicy/>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
AccessControlPolicy|无|保存 Get Bucket ACL 结果的容器|Container|是

### 错误码

错误码|描述|http 状态码|
---|---|---|---|
NoSuchBucket|当访问的 Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## 实际案例

### 请求

```
GET /test?acl HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b40652
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 266
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/12345:uin/12345</ID>
    <DisplayName>qcs::cam::uin/12345:uin/12345</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"CanonicalUser\">
        <ID>qcs::cam::uin/12345:uin/12345</ID>
        <DisplayName>qcs::cam::uin/12345:uin/12345</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"Group\">
        <URI>http://cam.qcloud.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

