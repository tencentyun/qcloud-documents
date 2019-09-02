## 功能描述
COS 支持用户以生命周期配置的方式来管理 Bucket 中 Object 的生命周期。生命周期配置包含一个或多个将应用于一组对象规则的规则集 (其中每个规则为 COS 定义一个操作)。
这些操作分为以下两种：
- **转换操作：**定义对象转换为另一个存储类的时间。例如，您可以选择在对象创建30天后将其转换为低频存储（STANDARD_IA，适用于不常访问) 存储类别。同时也支持将数据沉降到归档存储（Archive，成本更低，目前支持国内地域）。具体参数查看请求示例说明中 Transition 项。
- **过期操作：**指定 Object 的过期时间。COS 将会自动为用户删除过期的 Object。

### 细节分析

PUT Bucket lifecycle 用于为 Bucket 创建一个新的生命周期配置。如果该 Bucket 已配置生命周期，使用该接口创建新的配置的同时则会覆盖原有的配置。

## 请求
### 请求示例

```shell
PUT /?lifecycle HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Content-Length: length
Date: GMT Date
Authorization: Auth String 
Content-MD5: MD5
```
>Authorization： Auth String （详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

**必选头部**
该请求操作的实现使用如下必选头部：

| 名称               | 描述      | 类型     | 必选   |
| ---------------- | ----------- | ------ | ---- |
| Content-MD5       | RFC 1864 中定义的经过 **Base64** 编码的 128-bit 内容 MD5 校验值。此头部用来校验文件内容是否发生变化。| String | 是    |


### 请求体
该 API 接口请求的请求体具体节点内容为：

```shell
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Filter>
      <Prefix></Prefix>
    </Filter>
    <Status></Status>
    <Transition>
      <Days></Days>
      <StorageClass></StorageClass>
    </Transition>
    <NoncurrentVersionExpiration>
      <NoncurrentDays></NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
  <Rule>
    <ID></ID>
    <Filter>
      <Prefix></Prefix>
    </Filter>
    <Status></Status>
    <Transition>
      <Days></Days>
      <StorageClass></StorageClass>
    </Transition>
    <NoncurrentVersionTransition>
      <NoncurrentDays></NoncurrentDays>
      <StorageClass></StorageClass>
    </NoncurrentVersionTransition>
  </Rule>
  <Rule>
    <ID></ID>
    <Filter>
      <Prefix></Prefix>
    </Filter>
    <Status></Status>
    <Expiration>
      <ExpiredObjectDeleteMarker></ExpiredObjectDeleteMarker>
    </Expiration>
    <NoncurrentVersionExpiration>
      <NoncurrentDays></NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
</LifecycleConfiguration>
```

具体内容描述如下：

|节点名称（关键字）|    父节点|    描述    |类型|    必选|
|---|---|---|---|---|
|LifecycleConfiguration    |无    |生命周期配置    |Container    |是|
|Rule|    LifecycleConfiguration    |规则描述    |Container|    是|
|Filter    |LifecycleConfiguration.Rule    |Filter 用于描述规则影响的 Object 集合    |Container    |是|
|Status    |LifecycleConfiguration.Rule    |指明规则是否启用，枚举值：Enabled，Disabled     |Container    |是|
|ID    |LifecycleConfiguration.Rule|用于唯一地标识规则，长度不能超过255个字符    |String    |否|
|And    |LifecycleConfiguration.Rule.Filter    |用于组合 Prefix    |Container    |否|
|Prefix    |LifecycleConfiguration.Rule.Filter<br>或 LifecycleConfiguration.Rule.Filter.And    |指定规则所适用的前缀。匹配前缀的对象受该规则影响，Prefix 最多只能有一个   |Container    |否|
|Expiration    |LifecycleConfiguration.Rule    |规则过期属性    |Container    |否|
|Transition    |LifecycleConfiguration.Rule    |规则转换属性，对象何时转换为 Standard_IA 或 Archive   |Container    |否|
|Days    |LifecycleConfiguration.Rule.Transition<br>或 Expiration    |指明规则对应的动作在对象最后的修改日期过后多少天操作，如果是 Transition，该字段有效值是非负整数；如果是 Expiration，该字段有效值为正整数，最大支持3650天    |Integer    |否|
|Date    |LifecycleConfiguration.Rule.Transition<br>或 Expiration    |指明规则对应的动作在何时操作    |String    |否|
|ExpiredObjectDeleteMarker    |LifecycleConfiguration.Rule.Expiration    |删除过期对象删除标记，枚举值 true，false    |String    |否|
|AbortIncompleteMultipartUpload    |LifecycleConfiguration.Rule    |设置允许分片上传保持运行的最长时间    |Container    |否|
|DaysAfterInitiation    |LifecycleConfiguration.Rule<br>.AbortIncompleteMultipartUpload    |指明分片上传开始后多少天内必须完成上传    |Integer    |是|
|NoncurrentVersionExpiration    |LifecycleConfiguration.Rule    |指明非当前版本对象何时过期    |Container    |否|
|NoncurrentVersionTransition    |LifecycleConfiguration.Rule    |指明非当前版本对象何时转换为 STANDARD_IA 或 ARCHIVE   |Container   |否|
|NoncurrentDays    |LifecycleConfiguration.Rule<br>.NoncurrentVersionExpiration<br>或 NoncurrentVersionTransition    |指明规则对应的动作在对象变成非当前版本多少天后执行，如果是 Transition，该字段有效值是非负整数；如果是Expiration，该字段有效值为正整数，最大支持3650天 |Integer   |否|
|StorageClass    |LifecycleConfiguration.Rule.Transition<br>或 NoncurrentVersionTransition    |指定 Object 转储到的目标存储类型，枚举值： STANDARD_IA, ARCHIVE   |String    |是|


## 响应
### 响应头

#### 公共响应头 
该响应使用公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为空。

### 错误码
以下描述此请求可能会发生的一些特殊的且常见的错误情况。具体的错误原因可参考返回的 message 进行排查。获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

|错误码|HTTP 状态码|描述|
|--------|--------|----------|
|NoSuchBucket|404 Not Found|当访问的 Bucket 不存在|
|MalformedXML|400 Bad Request| XML 格式不合法，请跟 restful api 文档仔细比对 |
|InvalidRequest|400 Bad Reques|请求不合法，如果错误描述中显示"Conflict lifecycle rule"，那么表示xml数据中的多条 rule 有相互冲突的部分。|
|InvalidArgument|400 Bad Reques|请求参数不合法，如果错误描述中显示"Rule ID must be unique. Found same ID for more than one rule"， 那么表示有多个 Rule 的 ID 字段相同。|

## 实际案例

### 请求
```shell
PUT /?lifecycle HTTP/1.1
Host:examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 16 Aug 2017 11:59:33 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1502855771;1502935771&q-key-time=1502855771;1502935771&q-header-list=content-md5;host&q-url-param-list=lifecycle&q-signature=f3aa2c708cfd8d4d36d658de56973c9cf1c24654
Content-MD5: LcNUuow8OSZMrEDnvndw1Q==
Content-Length: 348
Content-Type: application/x-www-form-urlencoded

<LifecycleConfiguration>
  <Rule>
    <ID>id1</ID>
    <Filter>
       <Prefix>documents/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <Days>100</Days>
      <StorageClass>ARCHIVE</StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID>id2</ID>
    <Filter>
       <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>10</Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```

### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed, 16 Aug 2017 11:59:33 GMT
Server: tencent-cos
x-cos-request-id: NTk5NDMzYTRfMjQ4OGY3Xzc3NGRfMWY=
```
