> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

## 鉴权操作

### Get Authorization

#### 功能说明

Get Authorization 用于计算鉴权信息（Authorization）， 用以验证请求合法性的签名信息。
>**注意：**该方法推荐在前端调试时使用，项目上线不推荐使用前端计算签名的方法，有暴露秘钥的风险。

#### 操作方法原型
调用 Get Authorization 操作：

```js

var params = {
  method: 'STRING_VALUE',                          /* 必须 */
  pathname: 'STRING_VALUE',                        /* 非必须 */
  SecretId: 'STRING_VALUE',                        /* 必须 */
  SecretKey: 'STRING_VALUE',                       /* 必须 */
};

var Authorization = COS.getAuthorization(params);

```

#### 操作参数说明

|参数名|   参数 描述|      类型|    必填|
|--------|---------|--------|--------|
|method |操作方法，如 get，post，delete， head 等 HTTP 方法|String |是|
|pathname |操作的 object 名称，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空|String| 否|
|SecretId |用户的 SecretId|String| 是|
|SecretKey | 用户的 SecretKey|String|是|

#### 返回值说明

|参数名|    参数描述|      类型|   
|--------|---------|--------|
|Authorization | 操作的鉴权签名|String|

## Bucket操作

### Head Bucket

#### 功能说明

Head Bucket 请求可以确认该 Bucket 是否存在，是否有权限访问。Head 的权限与 Read 一致。当该 Bucket 存在时，返回 HTTP 状态码 200；当该 Bucket 无访问权限时，返回 HTTP 状态码 403；当该 Bucket 不存在时，返回 HTTP 状态码 404。

#### 操作方法原型

 调用 Head Bucket 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',    /* 必须 */
  Region : 'STRING_VALUE'     /* 必须 */
};

cos.headBucket(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
| BucketExist   |    Bucket 是否存在  |  Boolean  |  
| BucketAuth   |   是否拥有该 Bucket 的权限  |   Boolean  | 
| headers   |   请求返回的头部信息  |   Object  |    
| statusCode   |    请求返回的 HTTP 状态码，如 200，403，404 等  |  Number  | 

###  Get Bucket

#### 功能说明 

Get Bucket 请求等同于 List Object 请求，可以列出该 Bucket 下的部分或者全部 Object。此 API 调用者需要对 Bucket 有 Read 权限。

#### 操作方法原型

调用 Get Bucket 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',        /* 必须 */
  Region : 'STRING_VALUE',        /* 必须 */
  Prefix : 'STRING_VALUE',        /* 非必须 */
  Delimiter : 'STRING_VALUE',     /* 非必须 */
  Marker : 'STRING_VALUE',        /* 非必须 */
  MaxKeys : 'STRING_VALUE',       /* 非必须 */
  EncodingType : 'STRING_VALUE',  /* 非必须 */
};

cos.getBucket(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
|   Prefix   |   前缀匹配，用来规定返回的文件前缀地址  |   String  | 否|
|   Delimiter   |   定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始  |  String  | 否|
|   Marker   |  默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始  |  String  |  否|
|   MaxKeys   |  单次返回最大的条目数量，默认1000  |   String  | 否|
|   EncodingType   |  规定返回值的编码方式，可选值：url  |  String  |  否|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   CommonPrefixes   |    将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix  |   Array  | 
 |   Prefix   | 单条 Common 的前缀  |   String  |  
 |   Name   |   说明 Bucket 的信息  |  String| 
 |   Prefix   |   前缀匹配，用来规定返回的文件前缀地址  |  String  |  
 |   Marker   |    默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始  |  String  | 
 |   MaxKeys   |  单次响应请求内返回结果的最大的条目数量  |   String  |  
 |   IsTruncated   |   响应请求条目是否被截断，字符串，'true' 或者 'false'  |  String  |  
 |   NextMarker   |   假如返回条目被截断，则返回NextMarker就是下一个条目的起点  |  String| 
 |   Encoding-Type   |  返回值的编码方式，作用于Delimiter，Marker，Prefix，NextMarker，Key  |   String  |  
 |   Contents   |    元数据信息  |  Array  | 
 |   ETag   |   文件的 MD-5 算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`， **注意前后携带双引号 **   |   String  |  
 |   Size   |   说明文件大小，单位是 Byte  |   String  | 
 |   Key   |    Object名称  |  String  | 
 |   LastModified   |    说明 Object 最后被修改时间，如 2017-06-23T12:33:27.000Z  |  String  | 
|   Owner   |    Bucket 持有者信息  |  Object  | 
|   ID   |     Bucket 的 AppID  |  String  |
|   StorageClass   | Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE  |   String  |   
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 


###  Delete Bucket

#### 功能说明

Delete Bucket 接口请求可以在指定账号下删除 Bucket，删除之前要求 Bucket 内的内容为空，只有删除了 Bucket 内的信息，才能删除 Bucket 本身。注意，如果删除成功，则返回的 HTTP 状态码为 200 或 204 。

#### 操作方法原型

调用 Delete Bucket 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',    /* 必须 */
  Region : 'STRING_VALUE'     /* 必须 */
};

cos.deleteBucket(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 


###  Get Bucket ACL

#### 功能说明

Get Bucket ACL 接口用来获取 Bucket 的 ACL(access control list)， 即用户空间（Bucket）的访问权限控制列表。 此 API 接口只有 Bucket 的持有者有权限操作。

#### 操作方法原型

 调用 Get Bucket ACL 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',    /* 必须 */
  Region : 'STRING_VALUE'     /* 必须 */
};

cos.getBucketAcl(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   Owner   |    Bucket 持有者信息  |  Object  |  
|  DisplayName   |     Bucket 持有者的名称  |  String  | 
|   ID   |    Bucket 持有者 ID，<br>格式：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> <br>如果是根帐号，&lt;OwnerUin> 和 &lt;SubUin> 是同一个值  |  String  |  
|  Grants   |     被授权者信息与权限信息列表  |  Array  | 
|  Permission   |    指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL  |  String  |  
|  Grantee   | 说明被授权者的信息。type 类型可以为 RootAccount， Subaccount；<br>当 type 类型为 RootAccount 时，ID 中指定的是根帐号；<br>当 type 类型为 Subaccount 时，ID 中指定的是子帐号  |   Object  |    
|  DisplayName   |     用户的名称  |  String  | 
|  ID   |    用户的 ID，<br>如果是根帐号，格式为：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin> <br>或 qcs::cam::anyone:anyone （指代所有用户）<br>如果是子帐号，格式为： qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>  |  String  | 
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 


### Put Bucket ACL

#### 功能说明

Put Bucket ACL 接口用来写入 Bucket 的 ACL 表，您可以通过 Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"，"x-cos-grant-full-control" 传入 ACL 信息，或者通过 Body 以 XML 格式传入 ACL 信息。

#### 操作方法原型

 调用 Put Bucket ACL 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',            /* 必须 */
  Region : 'STRING_VALUE',            /* 必须 */
  ACL : 'STRING_VALUE',               /* 非必须 */
  GrantRead : 'STRING_VALUE',         /* 非必须 */
  GrantWrite : 'STRING_VALUE',        /* 非必须 */
  GrantFullControl : 'STRING_VALUE'   /* 非必须 */
};

cos.putBucketAcl(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
  |   ACL |    定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|  String| 否|
  |   GrantRead | 赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|   String|   否|
  |   GrantWrite |     赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String|否|
  |   GrantFullControl |   赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String|  否|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 

###  Get Bucket CORS

#### 功能说明

Get Bucket CORS 接口实现 Bucket 持有者在 Bucket 上进行跨域资源共享的信息配置。（CORS 是一个 W3C 标准，全称是"跨域资源共享"（Cross-origin resource sharing））。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

#### 操作方法原型

调用 Get Bucket CORS 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',    /* 必须 */
  Region : 'STRING_VALUE'     /* 必须 */
};

cos.getBucketCors(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
 |   CORSRules |   说明跨域资源共享配置的所有信息列表|   Array| 
    |   AllowedMethods |   允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE|   Array|  
    |   AllowedOrigins |  允许的访问来源，支持通配符 * 格式为：协议://域名[:端口]如：`http://www.qq.com`|   Array|   
    |   AllowedHeaders |   在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * |   Array|  
    |   ExposeHeaders |    设置浏览器可以接收到的来自服务器端的自定义头部信息|   Array| 
    |   MaxAgeSeconds |    设置 OPTIONS 请求得到结果的有效期|  String|  
    |   ID |     配置规则的 ID|  String| 


### Put Bucket CORS
> **注意：**
> 1. 如果要在前端修改`跨域访问配置`，需要该 Bucket 本身支持跨域，可以在`控制台`进行`跨域访问配置`，详情见 [开发环境](#开发环境)。
> 2. 在修改`跨域访问配置`时，请注意不要影响到当前的 Origin 下的跨域请求。

#### 功能说明

Put Bucket CORS 接口用来请求设置 Bucket 的跨域资源共享权限，您可以通过传入 XML 格式的配置文件来实现配置，文件大小限制为64 KB。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

#### 操作方法原型

调用 Put Bucket CORS 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',              /* 必须 */
  Region : 'STRING_VALUE',              /* 必须 */
  CORSRules : [
    {
      ID : 'STRING_VALUE',              /* 非必须 */
      AllowedMethods: [                 /* 必须 */
        'STRING_VALUE',
        ...
      ],
      AllowedOrigins: [                 /* 必须 */
        'STRING_VALUE',
        ...
      ],
      AllowedHeaders: [                 /* 非必须 */
        'STRING_VALUE',
        ...
      ],
      ExposeHeaders: [                  /* 非必须 */
        'STRING_VALUE',
        ...
      ],
      MaxAgeSeconds: 'STRING_VALUE'     /* 非必须 */
    },
    ....
  ]
};

cos.putBucketCors(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
|   CORSRules |  说明跨域资源共享配置的所有信息列表|   Array| 否|
|   ID |    配置规则的 ID，可选填|  String| 否|
|   AllowedMethods |   允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE|  Array|  是|
|   AllowedOrigins |    允许的访问来源，支持通配符 * 格式为：协议://域名[:端口]如：`http://www.qq.com`|  Array| 是|
|   AllowedHeaders |    在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，**暂不支持通配符 "*"** |  Array| 否|
|   ExposeHeaders |     设置浏览器可以接收到的来自服务器端的自定义头部信息|  Array| 否|
 |   MaxAgeSeconds |   设置 OPTIONS 请求得到结果的有效期|  String|  否|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 


###  Delete Bucket CORS

>** 注意：**
>1. 删除当前 Bucket 的`跨域访问配置`信息，会导致所有请求跨域失败，请谨慎操作。
>2. 不推荐在浏览器端使用该方法。

#### 功能说明

Delete Bucket CORS 接口请求实现删除跨域访问配置信息。

#### 操作方法原型

 调用 Delete Bucket CORS 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',        /* 必须 */
  Region : 'STRING_VALUE'         /* 必须 */
};

cos.deleteBucketCors(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 


### Get Bucket Location

#### 功能说明

Get Bucket Location 接口用于获取 Bucket 所在的地域信息，该 GET 操作使用 location 子资源返回 Bucket 所在的区域，只有 Bucket 持有者才有该 API 接口的操作权限。

#### 操作方法原型

 调用 Get Bucket Location 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',        /* 必须 */
  Region : 'STRING_VALUE'         /* 必须 */
};

cos.getBucketLocation(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|LocationConstraint |Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 

## Object 操作
### Head Object

#### 功能说明

Head Object 接口请求可以获取对应 Object 的 meta 信息数据，Head 的权限与 Get 的权限一致。

#### 操作方法原型

调用 Head Object 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',            /* 必须 */
  Region : 'STRING_VALUE',            /* 必须 */
  Key : 'STRING_VALUE',               /* 必须 */
  IfModifiedSince : 'STRING_VALUE'    /* 非必须 */
};

cos.headObject(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
| IfModifiedSince| 当 Object 在指定时间后被修改，则返回对应 Object 的 meta 信息，否则返回 304|String|否|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|  headers |    请求返回的头部信息| Object|   
|  x-cos-object-type |    用来表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable|String| 
|   x-cos-storage-class |  Object 的存储级别，枚举值：STANDARD, STANDARD_IA, NEARLINE|String| 
|  x-cos-meta- * |  用户自定义的 meta|String|
| statusCode |   请求返回的 HTTP 状态码，如 200，304 等，如果在指定时间后未被修改，则返回 304| Number| 
|  NotModified |  Object 是否在指定时间后未被修改|Boolean|

### Get Object

#### 功能说明

Get Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）下载至本地。该操作需要请求者对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

#### 操作方法原型

调用 Get Object 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  ResponseContentType : 'STRING_VALUE',           /* 非必须 */
  ResponseContentLanguage : 'STRING_VALUE',       /* 非必须 */
  ResponseExpires : 'STRING_VALUE',               /* 非必须 */
  ResponseCacheControl : 'STRING_VALUE',          /* 非必须 */
  ResponseContentDisposition : 'STRING_VALUE',    /* 非必须 */
  ResponseContentEncoding : 'STRING_VALUE',       /* 非必须 */
  Range : 'STRING_VALUE',                         /* 非必须 */
  IfModifiedSince : 'STRING_VALUE',               /* 非必须 */
  IfUnmodifiedSince : 'STRING_VALUE',             /* 非必须 */
  IfMatch : 'STRING_VALUE',                       /* 非必须 */
  IfNoneMatch : 'STRING_VALUE',                   /* 非必须 */
};

cos.getObject(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
  |   ResponseContentType |     设置响应头部中的 Content-Type 参数|  String|否|
  |   ResponseContentLanguage |    设置返回头部中的 Content-Language 参数|  String| 否|
  |   ResponseExpires |     设置返回头部中的 Content-Expires 参数|String|  否|
  |   ResponseCacheControl |   设置返回头部中的 Cache-Control 参数|  String|  否|
  |   ResponseContentDisposition |     设置返回头部中的 Content-Disposition 参数|  String|否|
  |   ResponseContentEncoding |    设置返回头部中的 Content-Encoding 参数|  String| 否|
  |   Range |    RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位|  String| 否|
  |   IfModifiedSince |   当Object在指定时间后被修改，则返回对应 Object meta 信息，否则返回304|  String|  否|
  |   IfUnmodifiedSince |   如果文件修改时间早于或等于指定时间，才返回文件内容。否则返回 412 (precondition failed)|  String|  否|
  |   IfMatch |    当 ETag 与指定的内容一致，才返回文件。否则返回 412（precondition failed）|  String| 否|
  |   IfNoneMatch |    当 ETag 与指定的内容不一致，才返回文件。否则返回304（not modified）|  String| 否|
	

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers |    请求返回的头部信息| Object|   
|   x-cos-object-type |     用来表示 object 是否可以被追加上传，枚举值：normal 或者 appendable|  String|  
|   x-cos-storage-class |  Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE，<br>**注意：如果没有返回该头部，则说明文件存储级别为 STANDARD （标准存储）**|  String|  
|   x-cos-meta- * |   用户自定义的元数据|  String| 
|   NotModified |   如果请求时带有 IfModifiedSince 则返回该属性，如果文件未被修改，则为 true，否则为 false|  Boolean| 
|   statusCode |    请求返回的 HTTP 状态码，如 200，304，403，404 等|  Number| 
|   Body |    返回的文件内容，默认为 String 形式|  String| 


### Put Object

#### 功能说明

Put Object 接口请求可以将本地的文件（Object）上传至指定 Bucket 中。该操作需要请求者对 Bucket 有 WRITE 权限。

>**注意：**
>1. Key(文件名) 不能以 `/` 结尾，否则会被识别为文件夹。
>2. 单个 Bucket 下 acl 策略限制 1000 条，因此在单个 bucket 下，最多允许对 999 个文件设置 acl 权限。

#### 操作方法原型

调用 Put Object 操作：

```js
var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  ContentLength : 'STRING_VALUE',                 /* 必须 */
  CacheControl : 'STRING_VALUE',                  /* 非必须 */
  ContentDisposition : 'STRING_VALUE',            /* 非必须 */
  ContentEncoding : 'STRING_VALUE',               /* 非必须 */
  ContentType : 'STRING_VALUE',                   /* 非必须 */
  Expect : 'STRING_VALUE',                        /* 非必须 */
  Expires : 'STRING_VALUE',                       /* 非必须 */
  ACL : 'STRING_VALUE',                           /* 非必须 */
  GrantRead : 'STRING_VALUE',                     /* 非必须 */
  GrantWrite : 'STRING_VALUE',                    /* 非必须 */
  GrantFullControl : 'STRING_VALUE',              /* 非必须 */
  StorageClass : 'STRING_VALUE',                  /* 非必须 */
  'x-cos-meta-*' : 'STRING_VALUE',                /* 非必须 */
  Body: 'String || File || Blob',                 /* 必须 */
  onProgress : function(progressData) {           /* 非必须 */
    console.log(JSON.stringify(progressData));
  }
};
cos.putObject(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
|   CacheControl |   RFC 2616 中定义的缓存策略，将作为 Object 元数据保存|   String| 是|
|   ContentDisposition |    RFC 2616 中定义的文件名称，将作为 Object 元数据保存|  String| 否|
|   ContentEncoding | RFC 2616 中定义的编码格式，将作为 Object 元数据保存|   String|  否| 
|   ContentLength |   RFC 2616 中定义的 HTTP 请求内容长度（字节）|   String| 否|
|    ContentType |    RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存|  String| 否|
|   Expect |    当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容|  String| 否|
|   Expires |RFC 2616 中定义的过期时间，将作为 Object 元数据保存|    String|   否|
|    ACL | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|   String| 否|
| GrantRead |  赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String| 否|
|   GrantWrite |  赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String| 否|
|   GrantFullControl |   赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String|否|
|   StorageClass |    设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE，默认值：STANDARD|  String| 否|
|   x-cos-meta- * |   允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制 2K|  String|  否|
|    Body |  上传文件的内容，可以为`字符串`，`File 对象`或者 `Blob 对象`|  String \ File\ Blob| 是|
|   onProgress |    进度的回调函数，进度回调响应对象（progressData）属性如下|  Function| 否|
|   progressData.loaded |    已经下载的文件部分大小，以字节（bytes）为单位|  Number| 否|
|   progressData.total |    整个文件的大小，以字节（bytes）为单位|  Number| 否|
|   progressData.speed |   文件的下载速度，以字节/秒（bytes/s）为单位|  Number|  否|
|   progressData.percent |  文件下载的百分比，以小数形式呈现，例如：下载 50% 即为 0.5|  Number|   否|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers   |    请求返回的头部信息  |  Object|  
|   statusCode   | 请求返回的 HTTP 状态码，如 200，403，404 等  |   Number| 
|ETag |返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 在上传过程中是否有损坏，<br>**注意：这里的 ETag 值字符串前后带有双引号，例如 `"09cba091df696af91549de27b8e7d0f6"`**|String|  


###  Delete Object

#### 功能说明

Delete Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）删除。该操作需要请求者对 Bucket 有 WRITE 权限。

#### 操作方法原型

 调用 Delete Object 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE'                            /* 必须 */
};

cos.deleteObject(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers   |    请求返回的头部信息  |  Object|  
|statusCode |请求返回的 HTTP 状态码，如 200，204，403，404等，**如果删除成功或者文件不存在则返回 204 或 200，如果找不到指定的 Bucket，则返回 404**|Number| 
 | BucketNotFound |如果找不到指定的 Bucket，则为 true|Boolean|

###  Options Object

#### 功能说明

Options Object 接口实现 Object 跨域访问配置的预请求。即在发送跨域请求之前会发送一个 OPTIONS 请求并带上特定的来源域，HTTP 方法和 HEADER 信息等给 COS，以决定是否可以发送真正的跨域请求。当 CORS 配置不存在时，请求返回 403 Forbidden。
**可以通过 Put Bucket CORS 接口来开启 Bucket 的 CORS 支持**

#### 操作方法原型

 调用 Options Object 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                            /* 必须 */
  Region : 'STRING_VALUE',                            /* 必须 */
  Key : 'STRING_VALUE',                               /* 必须 */
  Origin : 'STRING_VALUE',                            /* 必须 */
  AccessControlRequestMethod : 'STRING_VALUE',        /* 必须 */
  AccessControlRequestHeaders : 'STRING_VALUE'        /* 非必须 */
};

cos.optionsObject(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
| Origin | 模拟跨域访问的请求来源域名|String|是|
| AccessControlRequestMethod |模拟跨域访问的请求 HTTP 方法|String| 是|
| AccessControlRequestHeaders |模拟跨域访问的请求头部|String| 否|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
 |   AccessControlAllowOrigin |     模拟跨域访问的请求来源域名，中间用逗号间隔，当来源不允许的时候，此Header不返回。例如：\*|   String|
  |   AccessControlAllowMethods |    模拟跨域访问的请求HTTP方法，中间用逗号间隔，当请求方法不允许的时候，此Header不返回。例如：PUT,GET,POST,DELETE,HEAD|  String|
  |   AccessControlAllowHeaders |   模拟跨域访问的请求头部，中间用逗号间隔，当模拟任何请求头部不允许的时候，此Header不返回该请求头部。例如：accept，content-type，origin，authorization|  String| 
  |   AccessControlExposeHeaders |  跨域支持返回头部，中间用逗号间隔。例如：ETag|   String| 
  |   AccessControlMaxAge |    设置 OPTIONS 请求得到结果的有效期。例如：3600|  String|
  |   OptionsForbidden |    OPTIONS 请求是否被禁止，如果返回的 HTTP 状态码为 403，则为 true|  Boolean|
  |   headers |      请求返回的头部信息|  Object|  
  |   statusCode |  请求返回的 HTTP 状态码，如 200，403，404 等|   Number|  


### Get Object ACL

#### 功能说明

Get Object ACL 接口用来获取某个 Bucket 下的某个 Object 的访问权限。只有 Bucket 的持有者才有权限操作。

#### 操作方法原型

调用 Get Object ACL 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE'                            /* 必须 */
};

cos.getObjectAcl(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   Owner |    标识资源的所有者|   Object| 
|   ID |     Object 持有者 ID，格式：qcs::cam::uin/&lt;OwnerUin>:uin/lt;SubUin> <br>如果是根帐号，&lt;OwnerUin> 和&lt;SubUin> 是同一个值|  String| 
|   DisplayName |    Object 持有者的名称|   String| 
|   Grants |    被授权者信息与权限信息列表|  Array|  
|  Permission |    指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL|String|  
|  Grantee | 说明被授权者的信息。type 类型可以为 RootAccount， Subaccount；当 type 类型为 RootAccount 时，ID 中指定的是根帐号;当 type 类型为 Subaccount 时，ID 中指定的是子帐号|   Object|    
|  DisplayName |    用户的名称|  String|  
|   ID |    用户的 ID，如果是根帐号，格式为：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin> <br>或 qcs::cam::anyone:anyone （指代所有用户）如果是子帐号，<br>格式为： qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>|String|   
|   headers |   请求返回的头部信息|   Object|  
|  statusCode |  请求返回的 HTTP 状态码，如 200，403，404 等|  Number| 


### Put Object ACL

#### 功能说明

Put Object ACL 接口用来对某个 Bucket 中的某个的 Object 进行 ACL 表的配置
**单个 Bucket 下 acl 策略限制 1000 条，因此在单个 bucket 下，最多允许对 999 个文件设置 acl 权限**

#### 操作方法原型

 调用 Put Object ACL 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',            /* 必须 */
  Region : 'STRING_VALUE',            /* 必须 */
  Key : 'STRING_VALUE',               /* 必须 */
  ACL : 'STRING_VALUE',               /* 非必须 */
  GrantRead : 'STRING_VALUE',         /* 非必须 */
  GrantWrite : 'STRING_VALUE',        /* 非必须 */
  GrantFullControl : 'STRING_VALUE'   /* 非必须 */
};

cos.putObjectAcl(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
|   ACL |   定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|  String|  否|
|   GrantRead |     赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String|否|
|   GrantWrite |    赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String| 否|
|   GrantFullControl |    赋予被授权者读写权限。<br>格式：id=" ",id=" "；当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String| 否|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers   |    请求返回的头部信息  |  Object|  
|statusCode |请求返回的 HTTP 状态码，如 200，204，403，404等，|Number| 


### Delete Multiple Object

#### 功能说明

Delete Multiple Object 接口请求实现在指定 Bucket 中批量删除 Object，单次请求最大支持批量删除 1000 个 Object。对于响应结果，COS 提供 Verbose 和 Quiet 两种模式：Verbose 模式将返回每个 Object 的删除结果；Quiet 模式只返回报错的 Object 信息。


#### 操作方法原型

 调用 Delete Multiple Object 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Quiet : 'BOOLEAN_VALUE',                        /* 非必须 */
  Objects :  [                                    /* 必须 */
    {
      Key : 'STRING_VALUE'                        /* 必须 */
    },
    ...
  ]
};

cos.deleteMultipleObject(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |要删除的文件名称|String| 是|
|Quiet |  布尔值，这个值决定了是否启动 Quiet 模式。值为 true 启动 Quiet 模式，值为 false 则启动 Verbose 模式，默认值为 false|Boolean| 否|
| Objects |要删除的文件列表|Array| 是|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|Deleted|说明本次删除的成功 Object 信息|Array| 
|Key |Object 的名称|String| 
|Error |说明本次删除的失败 Object 信息|Array| 
| Key | Object 的名称|String|
| Code |删除失败的错误码|String| 
|Message | 删除错误信息|String|
|   headers   |    请求返回的头部信息  |  Object|  
|statusCode |请求返回的 HTTP 状态码，如 200，204，403，404 等，|Number| 

### Put Object Copy

#### 功能说明

Put Object Copy 请求实现将一个文件从源路径复制到目标路径。建议文件大小 1M 到 5 G，超过 5 G 的文件请使用分块上传 Upload - Copy。在拷贝的过程中，文件元属性和 ACL 可以被修改。用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。


#### 操作方法原型

调用 Put Object Copy 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  CopySource : 'STRING_VALUE',                    /* 必须 */
  ACL : 'STRING_VALUE',                           /* 非必须 */
  GrantRead : 'STRING_VALUE',                     /* 非必须 */
  GrantWrite : 'STRING_VALUE',                    /* 非必须 */
  GrantFullControl : 'STRING_VALUE',              /* 非必须 */
  MetadataDirective : 'STRING_VALUE',             /* 非必须 */
  CopySourceIfModifiedSince : 'STRING_VALUE',     /* 非必须 */
  CopySourceIfUnmodifiedSince : 'STRING_VALUE',   /* 非必须 */
  CopySourceIfMatch : 'STRING_VALUE',             /* 非必须 */
  CopySourceIfNoneMatch : 'STRING_VALUE',         /* 非必须 */
  StorageClass : 'STRING_VALUE',                  /* 非必须 */
  CacheControl : 'STRING_VALUE',                  /* 非必须 */
  ContentDisposition : 'STRING_VALUE',            /* 非必须 */
  ContentEncoding : 'STRING_VALUE',               /* 非必须 */
  ContentType : 'STRING_VALUE',                   /* 非必须 */
  Expect : 'STRING_VALUE',                        /* 非必须 */
  Expires : 'STRING_VALUE',                       /* 非必须 */
  'x-cos-meta-*' : 'STRING_VALUE',                /* 非必须 */
};

cos.putObjectCopy(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
|   CopySource |  源文件 URL 路径，可以通过 versionid 子资源指定历史版本|   String|  是|
|   ACL |    定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|String|  否| 
|   GrantRead |  赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|   String|   否| 
 |   GrantWrite |   赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String|   否| 
|   GrantFullControl |   赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String|   否| 
|   MetadataDirective |   是否拷贝元数据，枚举值：Copy, Replaced，默认值 Copy。假如标记为 Copy，忽略 Header 中的用户元数据信息直接复制；假如标记为 Replaced，按 Header 信息修改元数据。**当目标路径和原路径一致，即用户试图修改元数据时，必须为 Replaced**|   String|  否| 
|   CopySourceIfModifiedSince |    当 Object 在指定时间后被修改，则执行操作，否则返回 412。**可与 CopySourceIfNoneMatch 一起使用，与其他条件联合使用返回冲突**|  String|  否| 
|   CopySourceIfUnmodifiedSince |   当 Object 在指定时间后未被修改，则执行操作，否则返回 412。**可与 CopySourceIfMatch 一起使用，与其他条件联合使用返回冲突**|  String|   否| 
|   CopySourceIfMatch |   当 Object 的 Etag 和给定一致时，则执行操作，否则返回 412。**可与CopySourceIfUnmodifiedSince 一起使用，与其他条件联合使用返回冲突**|  String|   否| 
|   CopySourceIfNoneMatch |    当 Object 的 Etag 和给定不一致时，则执行操作，否则返回 412。**可与 CopySourceIfModifiedSince 一起使用，与其他条件联合使用返回冲突**|  String|  否| 
|   StorageClass |  存储级别，枚举值：存储级别，枚举值：Standard, Standard_IA，Nearline；默认值：Standard|  String|    否| 
 |   x-cos-meta- * |    其他自定义的文件头部|  String|   否| 
|   CacheControl |    指定所有缓存机制在整个请求/响应链中必须服从的指令|  String|   否| 
 |   ContentDisposition |  MIME 协议的扩展，MIME 协议指示 MIME 用户代理如何显示附加的文件|   String|   否| 
 |   ContentEncoding |    HTTP 中用来对「采用何种编码格式传输正文」进行协定的一对头部字段|  String|  否| 
 |   ContentType |    RFC 2616 中定义的 HTTP 请求内容类型（MIME），例如`text/plain`|  String|  否| 
 |   Expect |   请求的特定的服务器行为|   String|  否| 
 |   Expires |   响应过期的日期和时间|  String|   否| 
	

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|ETag|文件的 MD-5 算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`，**注意前后携带双引号**|String| 
| LastModified| 说明 Object 最后被修改时间，如 2017-06-23T12:33:27.000Z|String|
| headers |    请求返回的头部信息|Object|
| statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等|Number|


## 分块上传操作
### Initiate Multipart Upload

#### 功能说明

Initiate Multipart Upload请求实现初始化分片上传，成功执行此请求以后会返回Upload ID用于后续的Upload Part请求

#### 操作方法原型

调用 Initiate Multipart Upload 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  CacheControl : 'STRING_VALUE',                  /* 非必须 */
  ContentDisposition : 'STRING_VALUE',            /* 非必须 */
  ContentEncoding : 'STRING_VALUE',               /* 非必须 */
  ContentType : 'STRING_VALUE',                   /* 非必须 */
  Expires : 'STRING_VALUE',                       /* 非必须 */
  ACL : 'STRING_VALUE',                           /* 非必须 */
  GrantRead : 'STRING_VALUE',                     /* 非必须 */
  GrantWrite : 'STRING_VALUE',                    /* 非必须 */
  GrantFullControl : 'STRING_VALUE',              /* 非必须 */
  StorageClass : 'STRING_VALUE',                  /* 非必须 */
  'x-cos-meta-*' : 'STRING_VALUE'                 /* 非必须 */
};

cos.multipartInit(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
 |   CacheControl |  RFC 2616 中定义的缓存策略，将作为 Object 元数据保存|  String|   否|
 |   ContentDisposition |   RFC 2616 中定义的文件名称，将作为 Object 元数据保存|  String|  否|
 |   ContentEncoding |   RFC 2616 中定义的编码格式，将作为 Object 元数据保存|  String|  否|
 |   ContentType |  RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存|  String|   否|
 |   Expires |    RFC 2616 中定义的过期时间，将作为 Object 元数据保存|  String| 否|
 |   ACL |   定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|  String|  否|
 |   GrantRead |  赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|   String|  否|
 |   GrantWrite |    赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|  String| 否|
 |   GrantFullControl |   赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"'|   String| 否|
 |   StorageClass |   设置Object的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE，默认值：STANDARD|  String|  否|
 |   x-cos-meta- * |    允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K |  String| 否|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
| Bucket| 分片上传的目标 Bucket|String|
| Key | Object 的名称|String| 
| UploadId |  在后续上传中使用的 ID|String|


### Upload Part

#### 功能说明

Upload Part 接口请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1 MB 到5 GB。
使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置。在每次请求 Upload Part 时候，需要携带 partNumber 和 uploadId，partNumber为块的编号，支持乱序上传。
当传入 uploadId 和 partNumber 都相同的时候，后传入的块将覆盖之前传入的块。当 uploadId 不存在时会返回 404 错误，NoSuchUpload。


#### 操作方法原型

 调用 Upload Part 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  ContentLength : 'STRING_VALUE',                 /* 必须 */
  PartNumber : 'STRING_VALUE',                    /* 必须 */
  UploadId : 'STRING_VALUE',                      /* 必须 */
  Body: 'String || File || Blob',                 /* 必须 */
  Expect : 'STRING_VALUE',                        /* 非必须 */
  ContentMD5 : 'STRING_VALUE',                    /* 非必须 */
};

cos.multipartUpload(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明


|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
|   ContentLength |     RFC 2616 中定义的 HTTP 请求内容长度（字节）|String|是|
|   PartNumber |   分块的编号| String| 是|
|   UploadId |   上传任务编号| String| 是|
|   Body |  上传文件分块的内容，可以为`字符串`，`File 对象`或者 `Blob 对象`|String \ File \ Blob| 是|
|   Expect |  当使用 `Expect: 100-continue` 时，在收到服务端确认后，才会发送请求内容|String|   否|
|   ContentMD5 |   RFC 1864 中定义的经过 Base64 编码的128-bit 内容 MD5 校验值。此头部用来校验文件内容是否发生变化| String| 否|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
| ETag |  文件的 MD-5 算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`，**注意前后携带双引号**|String|
|headers |  请求返回的头部信息|Object|  
| statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number| 


### Complete Multipart Upload

#### 功能说明

Complete Multipart Upload 接口请求用来实现完成整个分块上传。当使用 Upload Parts 上传完所有块以后，必须调用该 API 来完成整个文件的分块上传。在使用该 API 时，您必须在请求 Body 中给出每一个块的 PartNumber 和 ETag，用来校验块的准确性。
由于分块上传完后需要合并，而合并需要数分钟时间，因而当合并分块开始的时候，COS 就立即返回 200 的状态码，在合并的过程中，COS 会周期性的返回空格信息来保持连接活跃，直到合并完成，COS会在 Body 中返回合并后块的内容。
- 当上传块小于 1 MB 的时候，在调用该 API 时，会返回 400 EntityTooSmall；
- 当上传块编号不连续的时候，在调用该 API 时，会返回 400 InvalidPart；
- 当请求 Body 中的块信息没有按序号从小到大排列的时候，在调用该 API 时，会返回 400 InvalidPartOrder；
- 当 UploadId 不存在的时候，在调用该 API 时，会返回 404 NoSuchUpload。

#### 操作方法原型

调用 Complete Multipart Upload 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  UploadId : 'STRING_VALUE',                      /* 必须 */
  Parts : [
    {
      PartNumber : 'STRING_VALUE',                /* 必须 */
      ETag : 'STRING_VALUE'                       /* 必须 */
    },
    ...
  ]
};

cos.multipartComplete(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
| UploadId |上传任务编号|String| 是|
| Parts |用来说明本次分块上传中块的信息列表|Array| 是|
| PartNumber|分块的编号|String| 是|
| ETag| 每个块文件的 MD5 算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`，**注意前后携带双引号**|String|是|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|Location  |  创建的 Object 的外网访问域名 | String |  
| Bucket  |  分块上传的目标 Bucket | String |  
| Key  |   Object 的名称 | String | 
| ETag  |   合并后文件的 MD5算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`，**注意前后携带双引号** | String | 
| headers  |     请求返回的头部信息 | Object | 
|statusCode  |  请求返回的 HTTP 状态码，如 200，403，404 等 | Number | 


### List Parts

#### 功能说明

List Parts 用来查询特定分块上传中的已上传的块，即罗列出指定 UploadId 所属的所有已上传成功的分块。

#### 操作方法原型

 调用 List Parts 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  UploadId : 'STRING_VALUE',                      /* 必须 */
  EncodingType : 'STRING_VALUE',                  /* 非必须 */
  MaxParts : 'STRING_VALUE',                      /* 非必须 */
  PartNumberMarker : 'STRING_VALUE'               /* 非必须 */
};

cos.multipartListPart(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
| UploadId| 标识本次分块上传的 ID。使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置。|String|是|
| EncodingType | 规定返回值的编码方式|String|否|
| MaxParts|单次返回最大的条目数量，默认 1000|String|否|
| PartNumberMarker|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|String| 否|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   Bucket |  分块上传的目标 Bucket|   String|  
|   Encoding-type |    规定返回值的编码方式|  String| 
|   Key |   Object 的名称|  String|  
|   UploadId |   标识本次分块上传的 ID|  String|  
|   Initiator |     用来表示本次上传发起者的信息|  Object|  
|   DisplayName |   上传发起者的名称|  String|  
|   ID |   上传发起者 ID，格式：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> <br>如果是根帐号，&lt;OwnerUin> 和 &lt;SubUin> 是同一个值|  String|  
|   Owner |    用来表示这些分块所有者的信息|  Object| 
|   DisplayName |  Bucket 持有者的名称|  String|   
|   ID |  Bucket 持有者 ID，一般为用户的 UIN|  String|   
|   StorageClass |   用来表示这些分块的存储级别，枚举值：Standard，Standard_IA，Nearline|  String|  
|   PartNumberMarker |  默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|   String| 
|   NextPartNumberMarker |  假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点|  String|   
|   MaxParts |   单次返回最大的条目数量|  String|  
|   IsTruncated |   返回条目是否被截断，'true' 或者 'false'|  String|  
|   Part |   分块信息列表|  Array| 
|   PartNumber |   块的编号|  String| 
|   LastModified |   块最后修改时间|   String|
|   ETag |   块的 MD5 算法校验值|   String|
 |   Size |   块大小，单位 Byte|  String| 
 |   headers |    请求返回的头部信息|  Object|  
 |   statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等|   Number| 


### Abort Multipart Upload

#### 功能说明

Abort Multipart Upload 用来实现舍弃一个分块上传并删除已上传的块。当您调用 Abort Multipart Upload 时，如果有正在使用这个 Upload Parts 上传块的请求，则 Upload Parts 会返回失败。当该 UploadId 不存在时，会返回 404 NoSuchUpload。

**建议您及时完成分块上传或者舍弃分块上传，因为已上传但是未终止的块会占用存储空间进而产生存储费用。**

#### 操作方法原型

 调用 Abort Multipart Upload 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Key : 'STRING_VALUE',                           /* 必须 */
  UploadId : 'STRING_VALUE'                       /* 必须 */
};

cos.multipartAbort(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key |文件名称|String| 是|
| UploadId |标识本次分块上传的 ID。使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置|String| 是|


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   headers |    请求返回的头部信息|  Object|  
|   statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等|   Number| 


### List Multipart Uploads

#### 功能说明

List Multiparts Uploads 用来查询正在进行中的分块上传。单次最多列出 1000 个正在进行中的分块上传。

#### 操作方法原型

调用 List Multipart Uploads 操作：

```js

var params = {
  Bucket : 'STRING_VALUE',                        /* 必须 */
  Region : 'STRING_VALUE',                        /* 必须 */
  Delimiter : 'STRING_VALUE',                     /* 非必须 */
  EncodingType : 'STRING_VALUE',                  /* 非必须 */
  Prefix : 'STRING_VALUE',                        /* 非必须 */
  MaxUploads : 'STRING_VALUE',                    /* 非必须 */
  KeyMarker : 'STRING_VALUE',                     /* 非必须 */
  UploadIdMarker : 'STRING_VALUE'                 /* 非必须 */
};

cos.multipartList(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
|   Delimiter |   定界符为一个符号，对 Object 名字包含指定前缀且第一次出现 delimiter 字符之间的 Object 作为一组元素：common prefix。如果没有 prefix，则从路径起点开始|  String|   否|
  |   EncodingType |    规定返回值的编码格式，合法值：url|  String|  否|
  |   Prefix |   限定返回的 Object key 必须以 Prefix 作为前缀。注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix|  String|   否|
  |   MaxUploads |  设置最大返回的 multipart 数量，合法取值从1到1000，默认1000|  String|   否|
  |   KeyMarker |    与 upload-id-marker 一起使用，<br> <li> 当 upload-id-marker 未被指定时：<br>ObjectName 字母顺序大于 key-marker 的条目将被列出，<br><li>当upload-id-marker被指定时：<br>ObjectName 字母顺序大于key-marker的条目被列出，<br>ObjectName 字母顺序等于 key-marker 且 UploadID 大于 upload-id-marker 的条目将被列出。|  String|  否|
  |   UploadIdMarker |  与 key-marker 一起使用，<br><li>当 key-marker 未被指定时：<br>upload-id-marker 将被忽略，<br><li>当 key-marker 被指定时：<br>ObjectName字母顺序大于 key-marker 的条目被列出，<br>ObjectName 字母顺序等于 key-marker 且 UploadID 大于 upload-id-marker 的条目将被列出。|  String|  否|</li>


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
|   Bucket |   分块上传的目标 Bucket|   String|  
|   Encoding-Type |    规定返回值的编码格式，合法值：url|   String| 
|   KeyMarker |  列出条目从该 key 值开始|  String|    
|   UploadIdMarker |   列出条目从该 UploadId 值开始|   String|  
|   NextKeyMarker |  假如返回条目被截断，则返回 NextKeyMarker 就是下一个条目的起点|  String|    
|   NextUploadIdMarker |     假如返回条目被截断，则返回 UploadId 就是下一个条目的起点|String|   
 |   MaxUploads |   设置最大返回的 multipart 数量，合法取值从 1 到 1000|   String|  
|   IsTruncated |   返回条目是否被截断，'true' 或者 'false'|   String|  
|   Delimiter |  定界符为一个符号，对 object 名字包含指定前缀且第一次出现 delimiter 字符之间的 object 作为一组元素：common prefix。如果没有 prefix，则从路径起点开始|  String|    
|   Prefix |     限定返回的 Object key 必须以 Prefix 作为前缀。注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix|  String| 
 |   CommonPrefixs |    将 prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix|  Array|  
 |   Prefix |      显示具体的 CommonPrefixs|  String|
 |   Upload |    Upload 的信息集合|   Array| 
 |   Key |   Object 的名称|   String|  
 |   UploadId |    标示本次分块上传的 ID|  String| 
 |   StorageClass |    用来表示分块的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE|   String| 
|   Initiator |    用来表示本次上传发起者的信息|   Object|  
 |   DisplayName |   上传发起者的名称|  String|   
 |   ID |    上传发起者 ID，格式：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> 如果是根帐号，&lt;OwnerUin> 和 &lt;SubUin> 是同一个值|  String|  
  |   Owner |    用来表示这些分块所有者的信息|   Object| 
  |   DisplayName |    Bucket 持有者的名称|   String| 
 |   ID |  Bucket 持有者 ID，格式：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> 如果是根帐号，&lt;OwnerUin> 和 &lt;SubUin> 是同一个值|  String|    
 |   Initiated |     分块上传的起始时间|  String| 
  |   headers |     请求返回的头部信息|  Object|   
  |   statusCode |    请求返回的 HTTP 状态码，如 200，403，404 等|  Number| 

## 分块上传任务操作

该类方法是对上面原生方法的封装，实现了分块上传的全过程，支持并发分块上传，支持断点续传，支持上传任务的取消，暂停和重新开始等。

###  Slice Upload File

#### 功能说明

Slice Upload File 可用于实现文件的分块上传。

#### 操作方法原型

调用 Slice Upload File 操作：

```js
var params = {
  Bucket: 'STRING_VALUE',                         /* 必须 */
  Region: 'STRING_VALUE',                         /* 必须 */
  Key: 'STRING_VALUE',                            /* 必须 */
  Body: 'File || Blob',                           /* 必须 */
  SliceSize: 'STRING_VALUE',                      /* 非必须 */
  StorageClass: 'STRING_VALUE',                   /* 非必须 */
  AsyncLimit: 'NUMBER',                           /* 非必须 */
  TaskReady: function(taskId) {                   /* 非必须 */
    console.log(taskId);
  },
  onHashProgress: function (progressData) {       /* 非必须 */
    console.log(JSON.stringify(progressData));
  },
  onProgress: function (progressData) {           /* 非必须 */
    console.log(JSON.stringify(progressData));
  }
};

cos.sliceUploadFile(params, function(err, data) {
  if(err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称 |   String|   是| 
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
 |   Key |   Object 名称|   String| 是|
  |   Body |  上传文件的内容，可以为  File 对象  或者  Blob 对象  |  File \ Blob| 是|
  |   SliceSize |    分块大小|  String| 否|
  |   AsyncLimit |    分块的并发量|  String| 否|
  |   StorageClass |   Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE|  String|  否|
  |   TaskReady |   上传任务创建时的回调函数，返回一个 taskId，唯一标识上传任务，可用于上传任务的取消（cancelTask），停止（pauseTask）和重新开始（restartTask）|  Function|否|
 |   taskId |  上传任务的编号|   String|  否|
|   onHashProgress |  计算文件 MD5 值的进度回调函数，回调参数为进度对象 progressData|   Function|否|
 |   progressData.loaded |  已经校验的文件部分大小，以字节（bytes）为单位|   Number|  否|
 |   progressData.total |   整个文件的大小，以字节（bytes）为单位|  Number|  否|
|   progressData.speed |  文件的校验速度，以字节/秒（bytes/s）为单位|  Number|  否| 
|   progressData.percent |  文件的校验百分比，以小数形式呈现，例如：下载 50% 即为 0.5|    Number| 否|
 |   onProgress |  上传文件的进度回调函数，回调参数为进度对象 progressData|  Function| 否|
|   progressData.loaded | 已经上传的文件部分大小，以字节（bytes）为单位|   Number|   否|
 |   progressData.total |   整个文件的大小，以字节（bytes）为单位|   Number| 否|
|   progressData.speed |   文件的上传速度，以字节/秒（bytes/s）为单位|   Number| 否|
|   progressData.percent |   文件的上传百分比，以小数形式呈现，例如：下载 50% 即为 0.5|   Number| 否|

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

|参数名|   参数描述|      类型|  
|--------|---------|--------|
|err   |    请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空  |  Object  |   
|data   |    请求成功时返回的对象，如果请求发生错误，则为空  |  Object  | 
| Location | 创建的 Object 的外网访问域名|String|
|Bucket | 分块上传的目标 Bucket|String| 
| Key |Object的名称|String| 
| ETag | 合并后文件的 MD5 算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`，**注意前后携带双引号**|String| 
| headers |   请求返回的头部信息|Object| 
| statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number| 


### Cancel Task

#### 功能说明

根据 taskId 取消分块上传任务。

#### 操作方法原型

调用 Cancel Task 操作。

```js

var taskId = 'xxxxx';                   /* 必须 */

cos.cancelTask(taskId);

```

#### 操作参数说明

|参数名|   参数描述|      类型|  必填|
|--------|---------|--------|----------|
|taskId|文件上传任务的编号，在调用 sliceUploadFile 方法时，其 TaskReady 回调会返回该上传任务的 taskId |String|是|

### Pause Task

#### 功能说明

根据 taskId 暂停分块上传任务。

#### 操作方法原型

调用 Pause Task 操作。

```js

var taskId = 'xxxxx';                   /* 必须 */

cos.pauseTask(taskId);

```

#### 操作参数说明

|参数名|   参数描述|      类型|  必填|
|--------|---------|--------|------|
|taskId|文件上传任务的编号，在调用 sliceUploadFile 方法时，其 TaskReady 回调会返回该上传任务的 taskId| String|是|


### Restart Task

#### 功能说明

根据 taskId 重新开始上传任务，可以用于开启用户手动停止的（调用 pauseTask 停止）或者因为上传错误而停止的上传任务。


#### 操作方法原型

调用 Restart Task 操作：

```js

var taskId = 'xxxxx';                   /* 必须 */

cos.restartTask(taskId);

```

#### 操作参数说明

|参数名|   参数描述|      类型|  必填|
|--------|---------|--------|-------|
|taskId|文件上传任务的编号，在调用 sliceUploadFile 方法时，其 TaskReady 回调会返回该上传任务的 taskId |String|是|
