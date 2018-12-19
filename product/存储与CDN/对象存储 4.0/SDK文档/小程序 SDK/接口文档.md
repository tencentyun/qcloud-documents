> 本文针对 小程序 SDK 的接口做详细的介绍说明

小程序 SDK github 地址：[tencentyun/cos-wx-sdk-v5](https://github.com/tencentyun/cos-wx-sdk-v5)

下文中在代码里出现的 COS 代表 SDK 的 类名，cos 代表 SDK 的实例。

下文中出现的 SecretId、SecretKey、Bucket、Region 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

下文中参数名称前的`-`代表"子参数"。

## 构造函数

### new COS({})

直接 script 标签引用 SDK 时，SDK 占用了全局变量名 COS，通过它的构造函数可以创建 SDK 实例。

#### 使用示例

创建一个 COS SDK 实例：
- 格式一（推荐）：使用临时密钥格式：
```js
var cos = new COS({
    // 必选参数
    getAuthorization: function (options, callback) {
        wx.request({
            method: 'GET',
            url: 'https://example.com/server/sts.php',
            dataType: 'json',
            success: function(result) {
                var data = result.data;
                callback({
                    TmpSecretId: data.credentials && data.credentials.tmpSecretId,
                    TmpSecretKey: data.credentials && data.credentials.tmpSecretKey,
                    XCosSecurityToken: data.credentials && data.credentials.sessionToken,
                    ExpiredTime: data.expiredTime,
                });
            }
        });
    }
});
```
- 格式二：前端每次请求都向后端获取签名
```js
var cos = new COS({
    // 必选参数
    getAuthorization: function (options, callback) {
        wx.request({
            url: 'https://example.com/server/sts-auth.php',
            data:{
                method: options.Method,
                filename: options.Key,
            },
            dataType: 'text',
            success: function (result) {
                var data = result.data;
                callback({
                    Authorization: data.Authorization
                    // XCosSecurityToken: data.XCosSecurityToken, // 如果是临时密钥计算出来的签名，需要提供 XCosSecurityToken
                });
            }
        });
    },
    // 可选参数
    FileParallelLimit: 3,    // 控制文件上传并发数
    ProgressInterval: 1000,  // 控制上传的 onProgress 回调的间隔
});
```
- 格式三：前端使用固定密钥，前端计算签名（建议只在调试使用，避免泄露密钥）：
```js
var cos = new COS({
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
});
```

#### 构造函数参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| SecretId | 用户的 SecretId | String | 否 |
| SecretKey | 用户的 SecretKey，建议只在前端调试时使用，避免暴露密钥 | String | 否 |
| FileParallelLimit | 同一个实例下上传的文件并发数，默认值 3 | Number | 否 |
| ProgressInterval | 上传进度的回调方法 onProgress 的回调频率，单位 ms ，默认值 1000 | Number | 否 |
| Protocol | 自定义的请求协议，可选项 `https:`、`http:`，默认判断当前页面是 `http:` 时使用 `http:`，否则使用 `https:` | String | 否 |
| getAthorization | 获取签名的回调方法，如果没有 SecretId、SecretKey 时，这个参数必选 | Function | 否 |


#### getAuthorization 回调函数说明 的函数说明（使用格式一）

```js
getAuthorization: function(options, callback) { ... }
```

getAuthorization 的回调参数说明：

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| options | 获取临时密钥需要的参数对象 | Function |
| - Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String |
| - Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String |
| callback | 临时密钥获取完成后的回传方法 | Function |

获取完临时密钥后，callback 回传一个对象，回传对象的属性列表如下：

| 属性名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| TmpSecretId | 获取回来的临时密钥的 tmpSecretId | String | 是 |
| TmpSecretKey | 获取回来的临时密钥的 tmpSecretKey | String | 否 |
| XCosSecurityToken | 获取回来的临时密钥的 sessionToken，对应 header 的 x-cos-security-token 字段 | String | 否 |
| ExpiredTime | 获取回来的临时密钥的 expiredTime，超时时间 | String | 否 |


#### getAuthorization 回调函数说明（使用格式二）

```js
getAuthorization: function(options, callback) { ... }
```

getAuthorization 的函数说明回调参数说明：

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| options | 获取签名需要的参数对象 | Function | 否 |
| - Method | 当前请求的 Method | Function | 否 |
| - Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 否 |
| - Query | 当前请求的 query 参数对象，{key: 'val'} 的格式 | Object | 否 |
| - Headers | 当前请求的 header 参数对象，{key: 'val'} 的格式 | Function | 否 |
| callback | 临时密钥获取完成后的回调 | Function | 否 |

getAuthorization 计算完成后，callback 回传一个签名字符串或一个对象：
回传签名字符串时，回传字符串类型，是请求要用的鉴权 Header 凭证字段 Authorization。
回传对象时，回传对象属性列表如下：

| 属性名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Authorization | 获取回来的临时密钥的 | String | 是 |
| XCosSecurityToken | 获取回来的临时密钥的 sessionToken，对应 header 的 x-cos-security-token 字段 | String | 否 |


#### 获取鉴权凭证

实例本身鉴权凭证可以通过实例化时传入的参数控制如何或获取，有三种获取方式：
1. 实例化时传入 SecretId、SecretKey，每次需要签名都由实例内部计算。
2. 实例化时，传入 getAuthorization 回调，每次需要签名通过这个回调计算完返回签名给实例。
3. 实例化时，传入 getSTS 回调，每次需要临时密钥通过这个回调回去完返回给实例，在每次请求时实例内部使用临时密钥计算得到签名。


## 静态方法
### COS.getAuthorization

COS XML API 的请求里，私有资源操作都需要鉴权凭证 Authorization，用于判断当前请求是否合法。

鉴权凭证使用方式有两种：
1. 放在 header 参数里使用，字段名: authorization
2. 放在 url 参数里使用，字段名：sign

COS.getAuthorization 方法用于计算鉴权凭证（Authorization），用以验证请求合法性的签名信息。
>**注意**：
>该方法推荐只在前端调试时使用，项目上线不推荐使用前端计算签名的方法，有暴露密钥的风险。

#### 使用示例

获取文件下载的鉴权凭证：
```js
var Authorization = COS.getAuthorization({
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    Method: 'get',
    Key: 'a.jpg',
    Expires: 60,
    Query: {},
    Headers: {}
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| SecretId | 用户的 SecretId | String | 是 |
| SecretKey | 用户的 SecretKey | String | 是 |
| Method | 操作方法，如 get，post，delete， head 等 HTTP 方法 | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空 | String | 否 |
| Expires | 签名超时秒数，默认 900 秒 | Number | 否 |
| Query | 请求的 query 参数对象 | Object | 否 |
| Headers | 请求的 header 参数对象 | Object | 否 |

#### 返回值说明
返回值是计算得到的鉴权凭证字符串 authorization。

## 工具方法
### Get Auth
cos.getAuth 方法是 COS.getAuthorization 挂在实例上的版本，区别是 cos.getAuth 不需要传入 SecretId 和 SecretKey，会使用对象本身获取鉴权凭证的方法。

#### 使用示例

```js
var authorization = cos.getAuth({
    Method: 'get',
    Key: '1.jpg'
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Method | 操作方法，如 get，post，delete， head 等 HTTP 方法 | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空 | String | 否 |
| Expires | 签名超时秒数，默认 900 秒 | Number | 否 |
| Query | 请求的 query 参数对象 | Object | 否 |
| Headers | 请求的 header 参数对象 | Object | 否 |

#### 返回值说明

返回值是计算得到的鉴权凭证字符串 authorization


### Get Object Url

#### 使用示例

// 获取不带签名 Object Url
```js
var url = cos.getObjectUrl({
    Key: '1.jpg',
    Sign: false
});
```

// 获取带签名的 Object Url
```js
cos.getObjectUrl({
    Key: '1.jpg',
    Sign: true
}, function (err, data) {
    console.log(err || data.Url);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空 | String | 是 |
| Sign | 是否返回带有签名的 Url | Boolean | 否 |
| Method | 操作方法，如 get，post，delete， head 等 HTTP 方法，默认 get | String | 否 |
| Query | 参与签名计算的 query 参数对象 | Object | 否 |
| Headers | 参与签名计算的 header 参数对象 | Object | 否 |

#### 返回值说明

返回值是一个字符串，两种情况：
1. 如果签名计算可以同步计算（如：实例化传入了 SecretId 和 SecretKey），则默认返回带签名的 url
2. 否则返回不带签名的 url

#### 回调函数说明

```js
function(err, data) { ... }
```

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - Url | 计算得到的 Url | String |


## Bucket 操作


### Head Bucket

#### 功能说明

Head Bucket 请求可以确认该 Bucket 是否存在，是否有权限访问。Head 的权限与 Read 一致。当该 Bucket 存在时，返回 HTTP 状态码 200；当该 Bucket 无访问权限时，返回 HTTP 状态码 403；当该 Bucket 不存在时，返回 HTTP 状态码 404。

#### 使用示例

```js
cos.headBucket({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',     /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |

#### 回调函数说明

```js
function(err, data) { ... }
```

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number |
| - headers | 请求返回的头部信息 | Object |
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number |
| - headers | 请求返回的头部信息 | Object |


### Get Bucket

#### 功能说明

Get Bucket 请求等同于 List Object 请求，可以列出该 Bucket 下的部分或者全部 Object。此 API 调用者需要对 Bucket 有 Read 权限。

#### 使用示例

列出目录 a 的所有文件
```js
cos.getBucket({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',     /* 必须 */
    Prefix: 'a/',           /* 非必须 */
}, function(err, data) {
    console.log(err || data);
});
```

列出目录 a 的文件，不深度遍历
```js
cos.getBucket({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou'     /* 必须 */
    Prefix: 'a/',              /* 非必须 */
    Delimiter: '/',            /* 非必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Prefix | 前缀匹配，用来规定返回的文件前缀地址 | String | 否 |
| Delimiter | 定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始 | String | 否 |
| Marker | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始 | String | 否 |
| MaxKeys | 单次返回最大的条目数量，默认1000 | String | 否 |
| EncodingType | 规定返回值的编码方式，可选值：url | String | 否 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - headers | 请求返回的头部信息 | Object|
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - CommonPrefixes | 将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix | Array |
| - - Prefix | 单条 Common 的前缀 | String |
| - - Name | 说明 Bucket 的信息 | String |
| - Prefix | 前缀匹配，用来规定返回的文件前缀地址 | String |
| - Marker | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始 | String |
| - MaxKeys | 单次响应请求内返回结果的最大的条目数量 | String |
| - IsTruncated | 响应请求条目是否被截断，字符串，'true' 或者 'false' | String |
| - NextMarker | 假如返回条目被截断，则返回NextMarker就是下一个条目的起点 | String |
| - Encoding-Type | 返回值的编码方式，作用于Delimiter，Marker，Prefix，NextMarker，Key | String |
| - Contents | 元数据信息 | Array |
| - - ETag | 文件的 MD-5 算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`， ** 注意前后携带双引号 ** | String |
| - - Size | 说明文件大小，单位是 Byte | String |
| - - Key | Object名称 | String |
| - - LastModified | 说明 Object 最后被修改时间，如 2017-06-23T12:33:27.000Z | String |
| - - Owner | Bucket 持有者信息 | Object |
| - ID | Bucket 的 AppID | String |
| - StorageClass | Object 的存储级别，枚举值：STANDARD，STANDARD_IA | String |

### Delete Bucket


#### 功能说明

Delete Bucket 接口请求可以在指定账号下删除 Bucket，删除之前要求 Bucket 内的内容为空，只有删除了 Bucket 内的信息，才能删除 Bucket 本身。注意，如果删除成功，则返回的 HTTP 状态码为 200 或 204 。

#### 使用示例

调用 Delete Bucket 操作：

```js
cos.deleteBucket({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou'     /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|


### Get Bucket ACL

#### 功能说明

Get Bucket ACL 接口用来获取 Bucket 的 ACL(access control list)， 即存储桶（Bucket）的访问权限控制列表。 此 API 接口只有 Bucket 的持有者有权限操作。

#### 使用示例

```js
cos.getBucketAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou'     /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|
| - Owner | Bucket 持有者信息 | Object |
| - - DisplayName | Bucket 持有者的名称 | String |
| - - ID | Bucket 持有者 ID，<br>格式：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> <br>如果是根帐号，&lt;OwnerUin> 和 &lt;SubUin> 是同一个值 | String |
| - Grants | 被授权者信息与权限信息列表 | Array |
| - - Permission | 指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL | String |
| - - Grantee | 说明被授权者的信息。type 类型可以为 RootAccount， Subaccount；<br>当 type 类型为 RootAccount 时，ID 中指定的是根帐号；<br>当 type 类型为 Subaccount 时，ID 中指定的是子帐号 | Object |
| - - - DisplayName | 用户的名称 | String |
| - - - ID | 用户的 ID，<br>如果是根帐号，格式为：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin> <br>或 qcs::cam::anyone:anyone （指代所有用户）<br>如果是子帐号，格式为： qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> | String |


### Put Bucket ACL

#### 功能说明

Put Bucket ACL 接口用来写入 Bucket 的 ACL 表，您可以通过 Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"，"x-cos-grant-full-control" 传入 ACL 信息，或者通过 Body 以 XML 格式传入 ACL 信息。

#### 使用示例

设置 Bucket 公有读
```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    ACL: 'public-read'
}, function(err, data) {
    console.log(err || data);
});
```

为某个用户赋予 Bucket 读写权限
```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    GrantFullControl: 'id="qcs::cam::uin/1001:uin/1001",id="qcs::cam::uin/1002:uin/1002"' // 1001 是 uin
}, function(err, data) {
    console.log(err || data);
});
```

为某个用户赋予 Bucket 读写权限
```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    GrantFullControl: 'id="qcs::cam::uin/1001:uin/1001",id="qcs::cam::uin/1002:uin/1002"' // 1001 是 uin
}, function(err, data) {
    console.log(err || data);
});
```

通过 AccessControlPolicy 修改 Bucket 权限
```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    AccessControlPolicy: {
        "Owner": { // AccessControlPolicy 里必须有 owner
            "ID": 'qcs::cam::uin/459000000:uin/459000000' // 459000000 是 Bucket 所属用户的 QQ 号
        },
        "Grants": [{
            "Grantee": {
                "ID": "qcs::cam::uin/10002:uin/10002", // 10002 是 QQ 号
            },
            "Permission": "WRITE"
        }]
    }
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| ACL | 定义 Object 的 ACL 属性。有效值：private、public-read、public-read-write；默认值：private | String | 否 |
| GrantRead | 赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantWrite | 赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantFullControl | 赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| AccessControlPolicy | 说明跨域资源共享配置的所有信息列表 | Object | 否 |
| - Owner | 代表存储桶所有者的对象 | Object | 否 |
| - - ID | 代表用户 ID 的字符串，格式如 qcs::cam::uin/1001:uin/1001，1001 是 uin | Object | 否 |
| - Grants | 说明跨域资源共享配置的所有信息列表 | Object | 否 |
| - - Permission | 说明跨域资源共享配置的所有信息列表，可选项 READ、WRITE、FULL_CONTROL、READ_ACP、WRITE_ACP | String | 否 |
| - - Grantee | 说明跨域资源共享配置的所有信息列表 | Array | 否 |
| - - - ID | 代表用户 ID 的字符串，格式如 qcs::cam::uin/1001:uin/1001，1001 是 uin | String | 否 |
| - - - DisplayName | 代表用户名称的字符串，一般填写成和 ID 一致的字符串 | String | 否 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|


### Get Bucket CORS

#### 功能说明

Get Bucket CORS 接口实现 Bucket 持有者在 Bucket 上进行跨域资源共享的信息配置。（CORS 是一个 W3C 标准，全称是"跨域资源共享"（Cross-origin Resource Sharing））。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

#### 使用示例
调用 Get Bucket CORS 操作：

```js
cos.getBucketCors({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - CORSRules | 说明跨域资源共享配置的所有信息列表 | Array |
| - - AllowedMethods | 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE | Array |
| - - AllowedOrigins | 允许的访问来源，支持通配符 * 格式为：协议://域名[:端口]如：`http://www.qq.com` | Array |
| - - AllowedHeaders | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * | Array |
| - - ExposeHeaders | 设置浏览器可以接收到的来自服务器端的自定义头部信息 | Array |
| - - MaxAgeSeconds | 设置 OPTIONS 请求得到结果的有效期 | String |
| - - ID | 配置规则的 ID | String |


### Put Bucket CORS

> **注意：**
> 1. 如果要在前端修改`跨域访问配置`，需要该 Bucket 本身支持跨域，可以在`控制台`进行`跨域访问配置`，详情见 [开发环境](#开发环境)。
> 2. 在修改`跨域访问配置`时，请注意不要影响到当前的 Origin 下的跨域请求。

#### 功能说明

Put Bucket CORS 接口用来请求设置 Bucket 的跨域资源共享权限，您可以通过传入 XML 格式的配置文件来实现配置，文件大小限制为64 KB。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

#### 使用示例

调用 Put Bucket CORS 操作：

```js
cos.putBucketCors({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    CORSRules: [{
        "AllowedOrigin": ["*"],
        "AllowedMethod": ["GET", "POST", "PUT", "DELETE", "HEAD"],
        "AllowedHeader": ["*"],
        "ExposeHeader": ["ETag", "x-cos-acl", "x-cos-version-id", "x-cos-delete-marker", "x-cos-server-side-encryption"],
        "MaxAgeSeconds": "5"
    }]
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| CORSRules | 说明跨域资源共享配置的所有信息列表 | Array | 否 |
| - ID | 配置规则的 ID，可选填 | String | 否 |
| - AllowedMethods | 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE | Array | 是 |
| - AllowedOrigins | 允许的访问来源，支持通配符 * 格式为：协议://域名[:端口]如：`http://www.qq.com` | Array | 是 |
| - AllowedHeaders | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * | Array | 否 |
| - ExposeHeaders | 设置浏览器可以接收到的来自服务器端的自定义头部信息 | Array | 否 |
| - MaxAgeSeconds | 设置 OPTIONS 请求得到结果的有效期 | String | 否 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|


### Delete Bucket CORS

>注意：
>1. 删除当前 Bucket 的`跨域访问配置`信息，会导致所有请求跨域失败，请谨慎操作。
>2. 不推荐在浏览器端使用该方法。

#### 功能说明

Delete Bucket CORS 接口请求实现删除跨域访问配置信息。

#### 使用示例

调用 Delete Bucket CORS 操作：

```js
cos.deleteBucketCors({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|


### Get Bucket Location

#### 功能说明

Get Bucket Location 接口用于获取 Bucket 所在的地域信息，该 GET 操作使用 location 子资源返回 Bucket 所在的区域，只有 Bucket 持有者才有该 API 接口的操作权限。

#### 使用示例

调用 Get Bucket Location 操作：

```js
cos.getBucketLocation({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|
| - LocationConstraint |Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String |



## Object 操作
### Head Object
#### 功能说明
Head Object 接口请求可以获取对应 Object 的 meta 信息数据，Head 的权限与 Get 的权限一致。

#### 使用示例
调用 Head Object 操作：
```js
cos.headObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',               /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| IfModifiedSince| 当 Object 在指定时间后被修改，则返回对应 Object 的 meta 信息，否则返回 304 | String | 否 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，304 等，如果在指定时间后未被修改，则返回 304| Number|
| - headers | 请求返回的头部信息| Object|
| - x-cos-object-type | 用来表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable | String |
| - x-cos-storage-class | Object 的存储级别，枚举值：STANDARD, STANDARD_IA | String |
| - x-cos-meta- * | 用户自定义的 meta | String |
| - NotModified | Object 是否在指定时间后未被修改|Boolean|

### Get Object
#### 功能说明

Get Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）下载至本地。该操作需要请求者对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

#### 使用示例
调用 Get Object 操作：

```js
cos.getObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
}, function(err, data) {
    console.log(err || data.Body);
});
```

指定 Range 获取文件内容
```js
cos.getObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    Range: 'bytes=1-3',        /* 非必须 */
}, function(err, data) {
    console.log(err || data.Body);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| ResponseContentType | 设置响应头部中的 Content-Type 参数 | String | 否 |
| ResponseContentLanguage | 设置返回头部中的 Content-Language 参数 | String | 否 |
| ResponseExpires | 设置返回头部中的 Content-Expires 参数 | String | 否 |
| ResponseCacheControl | 设置返回头部中的 Cache-Control 参数 | String | 否 |
| ResponseContentDisposition | 设置返回头部中的 Content-Disposition 参数 | String | 否 |
| ResponseContentEncoding | 设置返回头部中的 Content-Encoding 参数 | String | 否 |
| Range | RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位，如 Renge: 'bytes=1-3' | String | 否 |
| IfModifiedSince | 当Object在指定时间后被修改，则返回对应 Object meta 信息，否则返回 304 | String | 否 |
| IfUnmodifiedSince | 如果文件修改时间早于或等于指定时间，才返回文件内容。否则返回 412 (precondition failed) | String | 否 |
| IfMatch | 当 ETag 与指定的内容一致，才返回文件。否则返回 412（precondition failed） | String | 否 |
| IfNoneMatch | 当 ETag 与指定的内容不一致，才返回文件。否则返回 304（not modified） | String | 否 |


#### 回调函数说明
```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，304，403，404 等| Number|
| - headers | 请求返回的头部信息| Object|
| - x-cos-object-type | 用来表示 object 是否可以被追加上传，枚举值：normal 或者 appendable | String |
| - x-cos-storage-class | Object 的存储级别，枚举值：STANDARD，STANDARD_IA，<br>**注意：如果没有返回该头部，则说明文件存储级别为 STANDARD （标准存储）** | String |
| - x-cos-meta- * | 用户自定义的元数据 | String |
| - NotModified | 如果请求时带有 IfModifiedSince 则返回该属性，如果文件未被修改，则为 true，否则为 false| Boolean|
| - Body | 返回的文件内容，默认为 String 形式 | String |


### Put Object
#### 功能说明

Put Object 接口请求可以将本地的文件（Object）上传至指定 Bucket 中。该操作需要请求者对 Bucket 有 WRITE 权限。

>**注意：**
>1. Key（文件名）不能以 `/` 结尾，否则会被识别为文件夹。
>2. 当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承Bucket权限。

#### 使用示例

调用 Put Object 上传文件：
```js
cos.putObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    StorageClass: 'STANDARD',
    Body: file, // 上传文件对象
    onProgress: function(progressData) {
        console.log(JSON.stringify(progressData));
    }
}, function(err, data) {
    console.log(err || data);
});
```

上传字符串作为文件内容：
```js
cos.putObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    Body: 'hello!',
}, function(err, data) {
    console.log(err || data);
});
```

上传字符串作为文件内容：
```js
cos.putObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    Body: 'hello!',
}, function(err, data) {
    console.log(err || data);
});
```

创建目录：
```js
cos.putObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: 'a/',              /* 必须 */
    Body: '',
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| CacheControl | RFC 2616 中定义的缓存策略，将作为 Object 元数据保存 | String | 否 |
| ContentDisposition | RFC 2616 中定义的文件名称，将作为 Object 元数据保存 | String | 否 |
| ContentEncoding | RFC 2616 中定义的编码格式，将作为 Object 元数据保存 | String | 否 |
| ContentLength | RFC 2616 中定义的 HTTP 请求内容长度（字节） | String | 否 |
| ContentType | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存 | String | 否 |
| Expect | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容 | String | 否 |
| Expires |RFC 2616 中定义的过期时间，将作为 Object 元数据保存 | String | 否 |
| ACL | 定义 Object 的 ACL 属性。有效值：private、public-read、public-read-write；默认值：private | String | 否 |
| GrantRead | 赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantWrite | 赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantFullControl | 赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| StorageClass | 设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA，默认值：STANDARD | String | 否 |
| x-cos-meta- * | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制 2K | String | 否 |
| Body | 上传文件的内容，可以为`字符串`，`File 对象`或者 `Blob 对象` | String \ File\ Blob| 是 |
| onProgress | 进度的回调函数，进度回调响应对象（progressData）属性如下| Function| 否 |
| progressData.loaded | 已经下载的文件部分大小，以字节（bytes）为单位| Number| 否 |
| progressData.total | 整个文件的大小，以字节（Bytes）为单位| Number| 否 |
| progressData.speed | 文件的下载速度，以字节/秒（Bytes/s）为单位| Number| 否 |
| progressData.percent | 文件下载的百分比，以小数形式呈现，例如：下载 50% 即为 0.5| Number| 否 |


#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number|
| - headers | 请求返回的头部信息 | Object|
| - ETag |返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 在上传过程中是否有损坏，<br>**注意：这里的 ETag 值字符串前后带有双引号，例如 `"09cba091df696af91549de27b8e7d0f6"`** | String |

### Delete Object
#### 功能说明

Delete Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）删除。该操作需要请求者对 Bucket 有 WRITE 权限。

#### 使用示例
调用 Delete Object 操作：

```js
cos.deleteObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg'                            /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明
| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |


#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，204，403，404 等，**如果删除成功或者文件不存在则返回 204 或 200，如果找不到指定的 Bucket，则返回 404**|Number|
| - headers | 请求返回的头部信息 | Object|

### Options Object

#### 功能说明

Options Object 接口实现 Object 跨域访问配置的预请求。即在发送跨域请求之前会发送一个 OPTIONS 请求并带上特定的来源域，HTTP 方法和 HEADER 信息等给 COS，以决定是否可以发送真正的跨域请求。当 CORS 配置不存在时，请求返回 403 Forbidden。
**可以通过 Put Bucket CORS 接口来开启 Bucket 的 CORS 支持。**

#### 使用示例
调用 Options Object 操作：

```js
cos.optionsObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    Origin: 'https://www.qq.com',      /* 必须 */
    AccessControlRequestMethod: 'PUT', /* 必须 */
    AccessControlRequestHeaders: 'origin,accept,content-type' /* 非必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为 {name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| Origin | 模拟跨域访问的请求来源域名 | String | 是 |
| AccessControlRequestMethod |模拟跨域访问的请求 HTTP 方法 | String | 是 |
| AccessControlRequestHeaders |模拟跨域访问的请求头部 | String | 否 |

#### 回调函数说明
```js
function(err, data) { ... }
```

#### 回调参数说明
| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - headers | 请求返回的头部信息| Object|
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等| Number|
| - AccessControlAllowOrigin | 模拟跨域访问的请求来源域名，中间用逗号间隔，当来源不允许的时候，此Header不返回。例如：\* | String |
| - AccessControlAllowMethods | 模拟跨域访问的请求HTTP方法，中间用逗号间隔，当请求方法不允许的时候，此Header不返回。例如：PUT，GET，POST，DELETE，HEAD | String |
| - AccessControlAllowHeaders | 模拟跨域访问的请求头部，中间用逗号间隔，当模拟任何请求头部不允许的时候，此 Header 不返回该请求头部。例如：accept，content-type，origin，authorization | String |
| - AccessControlExposeHeaders | 跨域支持返回头部，中间用逗号间隔。例如：ETag | String |
| - AccessControlMaxAge | 设置 OPTIONS 请求得到结果的有效期。例如：3600 | String |
| - OptionsForbidden | OPTIONS 请求是否被禁止，如果返回的 HTTP 状态码为 403，则为 true| Boolean|


### Get Object ACL

#### 功能说明
Get Object ACL 接口用来获取某个 Bucket 下的某个 Object 的访问权限。只有 Bucket 的持有者才有权限操作。

#### 使用示例

调用 Get Object ACL 操作：

```js
cos.getObjectAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为 {name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等| Number|
| - headers | 请求返回的头部信息| Object|
| - Owner | 标识资源的所有者| Object|
| - ID | Object 持有者 ID，格式：qcs::cam::uin/&lt;OwnerUin>:uin/lt;SubUin> <br>如果是根帐号，&lt;OwnerUin> 和&lt;SubUin> 是同一个值 | String |
| - DisplayName | Object 持有者的名称 | String |
| - Grants | 被授权者信息与权限信息列表 | Array |
| - Permission | 指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL | String |
| - Grantee | 说明被授权者的信息。type 类型可以为 RootAccount， Subaccount；当 type 类型为 RootAccount 时，ID 中指定的是根帐号;当 type 类型为 Subaccount 时，ID 中指定的是子帐号| Object|
| - DisplayName | 用户的名称 | String |
| - ID | 用户的 ID，如果是根帐号，格式为：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin> <br>或 qcs::cam::anyone:anyone （指代所有用户）如果是子帐号，<br>格式为： qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> | String |


### Put Object ACL
#### 功能说明

Put Object ACL 接口用来对某个 Bucket 中的某个的 Object 进行 ACL 表的配置。当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承Bucket权限。

#### 使用示例
调用 Put Object ACL 修改文件权限：
```js
cos.putObjectAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    ACL: 'public-read',        /* 非必须 */
}, function(err, data) {
    console.log(err || data);
});
```

为某个用户赋予文件读写权限
```js
cos.putObjectAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    GrantFullControl: 'id="qcs::cam::uin/1001:uin/1001",id="qcs::cam::uin/1002:uin/1002"' // 1001 是 uin
}, function(err, data) {
    console.log(err || data);
});
```

通过 AccessControlPolicy 修改 Bucket 权限
```js
cos.putObjectAcl({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Key: '1.jpg',              /* 必须 */
    AccessControlPolicy: {
        "Owner": { // AccessControlPolicy 里必须有 owner
            "ID": 'qcs::cam::uin/459000000:uin/459000000' // 459000000 是 Bucket 所属用户的 QQ 号
        },
        "Grants": [{
            "Grantee": {
                "ID": "qcs::cam::uin/10002:uin/10002", // 10002 是 QQ 号
            },
            "Permission": "WRITE"
        }]
    }
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为 {name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| ACL | 定义 Object 的 ACL 属性。有效值：private、public-read、public-read-write；默认值：private | String | 否 |
| GrantRead | 赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantWrite | 赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantFullControl | 赋予被授权者读写权限。<br>格式：id=" ",id=" "；当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |

#### 回调函数说明
```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，204，403，404等，|Number|
| - headers | 请求返回的头部信息 | Object|


### Delete Multiple Object
#### 功能说明
Delete Multiple Object 接口请求实现在指定 Bucket 中批量删除 Object，单次请求最大支持批量删除 1000 个 Object。对于响应结果，COS 提供 Verbose 和 Quiet 两种模式：Verbose 模式将返回每个 Object 的删除结果；Quiet 模式只返回报错的 Object 信息。

#### 使用示例
删除多个文件：
```js
cos.deleteMultipleObject({
    Bucket: 'test-1250000000', /* 必须 */
    Region: 'ap-guangzhou',    /* 必须 */
    Objects: [
        {Key: '1.jpg'},
        {Key: '2.zip'},
    ]
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明
| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| Quiet | 布尔值，这个值决定了是否启动 Quiet 模式。值为 true 启动 Quiet 模式，值为 false 则启动 Verbose 模式，默认值为 false | Boolean| 否 |
| Objects |要删除的文件列表 | Array | 是 |

#### 回调函数说明
```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，204，403，404 等，|Number|
| - headers | 请求返回的头部信息 | Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，204，403，404 等，|Number|
| - headers | 请求返回的头部信息 | Object|
| - Deleted|说明本次删除的成功 Object 信息 | Array |
| - Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| - Error |说明本次删除的失败 Object 信息 | Array |
| - Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| - Code |删除失败的错误码 | String |
| - Message | 删除错误信息 | String |


### Put Object Copy
#### 功能说明

Put Object Copy 请求实现将一个文件从源路径复制到目标路径。建议文件大小 1MB 到 5GB，超过 5GB 的文件请使用分块上传 Upload - Copy。在拷贝的过程中，文件元属性和 ACL 可以被修改。用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。

#### 使用示例

调用 Put Object Copy 操作：

```js
cos.putObjectCopy({
    Bucket: 'test-1250000000',                               /* 必须 */
    Region: 'ap-guangzhou',                                  /* 必须 */
    Key: '1.jpg',                                            /* 必须 */
    CopySource: 'test1.cos.ap-guangzhou.myqcloud.com/2.jpg', /* 必须 */
}, function(err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名 | 参数描述 | 类型 | 必填 |
|--------|----------|------|------|
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是 |
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是 |
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| CopySource | 源文件 URL 路径，可以通过 versionid 子资源指定历史版本 | String | 是 |
| ACL | 定义 Object 的 ACL 属性。有效值：private、public-read、public-read-write；默认值：private | String | 否 |
| GrantRead | 赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantWrite | 赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| GrantFullControl | 赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | 否 |
| MetadataDirective | 是否拷贝元数据，枚举值：Copy, Replaced，默认值 Copy。假如标记为 Copy，忽略 Header 中的用户元数据信息直接复制；假如标记为 Replaced，按 Header 信息修改元数据。**当目标路径和原路径一致，即用户试图修改元数据时，必须为 Replaced** | String | 否 |
| CopySourceIfModifiedSince | 当 Object 在指定时间后被修改，则执行操作，否则返回 412。**可与 CopySourceIfNoneMatch 一起使用，与其他条件联合使用返回冲突** | String | 否 |
| CopySourceIfUnmodifiedSince | 当 Object 在指定时间后未被修改，则执行操作，否则返回 412。**可与 CopySourceIfMatch 一起使用，与其他条件联合使用返回冲突** | String | 否 |
| CopySourceIfMatch | 当 Object 的 Etag 和给定一致时，则执行操作，否则返回 412。**可与CopySourceIfUnmodifiedSince 一起使用，与其他条件联合使用返回冲突** | String | 否 |
| CopySourceIfNoneMatch | 当 Object 的 Etag 和给定不一致时，则执行操作，否则返回 412。**可与 CopySourceIfModifiedSince 一起使用，与其他条件联合使用返回冲突** | String | 否 |
| StorageClass | 存储级别，枚举值：存储级别，枚举值：Standard, Standard_IA；默认值：Standard | String | 否 |
| x-cos-meta- * | 其他自定义的文件头部 | String | 否 |
| CacheControl | 指定所有缓存机制在整个请求/响应链中必须服从的指令 | String | 否 |
| ContentDisposition | MIME 协议的扩展，MIME 协议指示 MIME 用户代理如何显示附加的文件 | String | 否 |
| ContentEncoding | HTTP 中用来对「采用何种编码格式传输正文」进行协定的一对头部字段 | String | 否 |
| ContentType | RFC 2616 中定义的 HTTP 请求内容类型（MIME），例如`text/plain` | String | 否 |
| Expect | 请求的特定的服务器行为 | String | 否 |
| Expires | 响应过期的日期和时间 | String | 否 |


#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述 | 类型 |
|--------|----------|------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，[错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等|Number|
| - headers | 请求返回的头部信息|Object|
| - ETag|文件的 MD-5 算法校验值，如 `"22ca88419e2ed4721c23807c678adbe4c08a7880"`，**注意前后携带双引号** | String |
| - LastModified| 说明 Object 最后被修改时间，如 2017-06-23T12:33:27.000Z | String |


## 分块复制任务操作

###  Slice Copy File

#### 功能说明

Slice Copy File 可用于实现通过分块复制将一个文件从源路径复制到目标路径。在拷贝的过程中，文件元属性和 ACL 可以被修改。用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。

#### 操作方法原型

调用 Slice Copy File 操作：

```js
cos.sliceCopyFile({
    Bucket: 'test-1250000000',                               /* 必须 */
    Region: 'ap-guangzhou',                                  /* 必须 */
    Key: '1.zip',                                            /* 必须 */
    CopySource: 'test1.cos.ap-guangzhou.myqcloud.com/2.zip', /* 必须 */
    onProgress:function (progressData) {                     /* 非必须 */
        console.log(JSON.stringify(progressData));
    }
},function (err,data) {
    console.log(err || data);
});

```

#### 操作参数说明

|参数名|   参数描述|      类型|    必填|
|--------|---------|--------|--------|
| Bucket| Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 |   String|   是|
| Region | Bucket 所在区域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224)|String|是|
| Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是 |
| CopySource | 源文件 URL 路径，可以通过 versionid 子资源指定历史版本 | String | 是 |
| ChunkSize | 分片复制时，每片的大小字节数，默认值 1048576 (1MB) | Number | 否 |
| SliceSize | 使用分片复制的文件大小，默认值 5G | Number | 否 |
| onProgress | 上传文件的进度回调函数，回调参数为进度对象 progressData | Function | 否 |
| - progressData.loaded | 已经上传的文件部分大小，以字节（bytes）为单位 | Number | 否 |
| - progressData.total | 整个文件的大小，以字节（bytes）为单位 | Number | 否 |
| - progressData.speed | 文件的上传速度，以字节/秒（bytes/s）为单位 | Number | 否 |
| - progressData.percent | 文件的上传百分比，以小数形式呈现，例如：下载 50% 即为 0.5 | Number | 否 |

#### 回调函数说明

```js
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 |  参数描述 | 类型 |
|--------|---------|--------|
| err | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空，错误码文档 |  Object  |
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number |
| - headers | 请求返回的头部信息 | Object |
| data | 请求成功时返回的对象，如果请求发生错误，则为空 | Object|
| - statusCode | 请求返回的 HTTP 状态码，如 200，403，404 等 | Number |
| - headers | 请求返回的头部信息 | Object |
| - Location | 创建的 Object 的外网访问域名 | String |
| - Bucket | 分块上传的目标 Bucket | String |
| - Key | 对象键（Object 的名称），对象在存储桶中的唯一标识，[对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| - ETag | 合并后文件的 MD5 算法校验值，如 "22ca88419e2ed4721c23807c678adbe4c08a7880"，注意前后携带双引号 | String |
