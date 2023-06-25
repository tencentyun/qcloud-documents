## 简介

Node.js SDK 提供获取对象 URL、获取请求预签名 URL 接口，详细操作请查看本文说明和示例。

关于使用预签名 URL 上传的说明请参见 [预签名授权上传](https://cloud.tencent.com/document/product/436/14114)， 使用预签名 URL 下载的说明请参见 [预签名授权下载](https://cloud.tencent.com/document/product/436/14116)。

> ?
>
> - 建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄露目标存储桶或对象之外的资源。申请临时密钥的 action 需添加 `"name/cos:GetObject"` 权限。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。

## 计算签名

COS XML API 的请求里，私有资源操作都需要鉴权凭证 Authorization，用于判断当前请求是否合法。

鉴权凭证使用方式有两种：

1. 放在 header 参数里使用，字段名：authorization。
2. 放在 url 参数里使用，字段名：sign。

COS.getAuthorization 方法用于计算鉴权凭证（Authorization），用以验证请求合法性的签名信息。

> ! 该方法推荐只在前端调试时使用，项目上线不推荐使用前端计算签名的方法，有暴露密钥的风险。

#### 使用示例

获取文件下载的鉴权凭证：

[//]: # (.cssg-snippet-get-authorization)

```js
// SECRETID 和 SECRETKEY 请登录 https://console.cloud.tencent.com/cam/capi 进行查看和管理
var COS = require('cos-nodejs-sdk-v5');
var Authorization = COS.getAuthorization({
  SecretId: process.env.SecretId, // 推荐使用环境变量获取；用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
  SecretKey: process.env.SecretKey, // 推荐使用环境变量获取；用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
  Method: 'get',
  Key: 'a.jpg',
  Expires: 60,
  Query: {},
  Headers: {},
});
```

#### 参数说明

| 参数名    | 参数描述                                                                                                                              | 类型   | 是否必填 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- |
| SecretId  | 用户的 SecretId                                                                                                                       | String | 是       |
| SecretKey | 用户的 SecretKey                                                                                                                      | String | 是       |
| Method    | 操作方法，如 get，post，delete， head 等 HTTP 方法                                                                                    | String | 是       |
| Key       | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于存储桶，则为空 | String | 否       |
| Query     | 签名中要签入的请求参数，{key: 'val'} 的格式                                                                                           | Object | 否       |
| Headers   | 签名中要签入的请求头部，{key: 'val'} 的格式                                                                                           | Object | 否       |
| Expires   | 签名几秒后失效，默认为 900 秒                                                                                                         | Number | 否       |

#### 返回值说明

返回值是计算得到的鉴权凭证字符串 authorization。

## 获取请求预签名 URL

### 下载请求示例

示例一：获取不带签名 Object Url

[//]: # (.cssg-snippet-get-presign-download-url-nosign)

```js
var url = cos.getObjectUrl({
  Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
  Region: 'COS_REGION', /* 存储桶所在地域，例如 ap-beijing，必须字段 */
  Key: '1.jpg', /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段 */
  Sign: false,
});
```

示例二：获取带签名 Object Url

[//]: # (.cssg-snippet-get-presign-download-url)

```js
var url = cos.getObjectUrl({
  Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
  Region: 'COS_REGION', /* 存储桶所在地域，例如 ap-beijing，必须字段 */
  Key: '头像.jpg', /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段 */
});
```

示例三：如果签名过程是异步获取，需要通过 callback 获取带签名 Url

[//]: # (.cssg-snippet-get-presign-download-url-callback)

```js
cos.getObjectUrl(
  {
    Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
    Region: 'COS_REGION', /* 存储桶所在地域，例如 ap-beijing，必须字段 */
    Key: '头像.jpg', /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段 */
    Sign: false,
  },
  function (err, data) {
    console.log(err || data.Url);
  }
);
```

示例四：指定链接有效时间

[//]: # (.cssg-snippet-get-presign-download-url-expiration)

```js
cos.getObjectUrl(
  {
    Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
    Region: 'COS_REGION', /* 存储桶所在地域，例如 ap-beijing，必须字段 */
    Key: '头像.jpg', /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段 */
    Sign: true,
    Expires: 3600, // 单位秒
  },
  function (err, data) {
    console.log(err || data.Url);
  }
);
```

示例五：获取文件 Url 并下载文件

[//]: # (.cssg-snippet-get-presign-download-url-then-fetch)

```js
var request = require('request');
var fs = require('fs');
cos.getObjectUrl(
  {
    Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
    Region: 'COS_REGION', /* 存储桶所在地域，例如 ap-beijing，必须字段 */
    Key: '头像.jpg', /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段 */
    Sign: true,
  },
  function (err, data) {
    if (err) return console.log(err);
    console.log(data.Url);
    var req = request(data.Url, function (err, response, body) {
      console.log(err || body);
    });
    var writeStream = fs.createWriteStream(__dirname + '/1.jpg');
    req.pipe(writeStream);
  }
);
```

示例六：生成预签名 URL，并在签名中携带 Query 和 Header

[//]: # (.cssg-snippet-get-obejct-url-with-params)

```js
cos.getObjectUrl(
  {
    Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
    Region: 'COS_REGION', /* 存储桶所在地域，例如 ap-beijing，必须字段 */
    Key: '头像.jpg', /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段 */
    Sign: true,
    /* 传入的请求参数需与实际请求相同，能够防止用户篡改此 HTTP 请求的参数 */
    Query: {
      'imageMogr2/thumbnail/200x/': '',
    },
    /* 传入的请求头部需包含在实际请求中，能够防止用户篡改签入此处的 HTTP 请求头部 */
    Headers: {
      host: 'xxx', /* 指定 host 访问，非指定的 host 访问会报错403 */
    },
  },
  function (err, data) {
    console.log(err || data.Url);
  }
);
```

### 上传请求示例

示例一：获取预签名 Put Object 上传 Url

[//]: # (.cssg-snippet-get-presign-upload-url)

```js
var request = require('request');
var fs = require('fs');
cos.getObjectUrl(
  {
    Bucket: 'examplebucket-1250000000', /* 填入您自己的存储桶，必须字段 */
    Region: 'COS_REGION', /* 存储桶所在地域，例如 ap-beijing，必须字段 */
    Key: '头像.jpg', /* 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段 */
    Method: 'PUT',
    Sign: true,
  },
  function (err, data) {
    if (err) return console.log(err);
    console.log(data.Url);
    var readStream = fs.createReadStream(__dirname + '/1.jpg');
    var req = request(
      {
        method: 'PUT',
        url: data.Url,
      },
      function (err, response, body) {
        console.log(err || body);
      }
    );
    readStream.pipe(req);
  }
);
```

### 参数说明

| 参数名   | 参数描述                                                                                                                              | 类型    | 是否必填 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| Bucket   | 存储桶的名称，命名规则为 BucketName-APPID，此处填写的存储桶名称必须为此格式                                                           | String  | 是       |
| Region   | 存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)                                    | String  | 是       |
| Key      | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于存储桶，则为空 | String  | 是       |
| Sign     | 是否返回带有签名的 Url，默认为 true                                                                                                   | Boolean | 否       |
| Protocol | 可选填为 `http:` 或 `https:`，默认为 `http:`（带冒号）                                                                                    | String  | 否       |
| Domain   | 存储桶访问域名，默认为 {BucketName-APPID}.cos.{Region}.myqcloud.com                                                                   | String  | 否       |
| Method   | 操作方法，如 get，post，delete， head 等 HTTP 方法，默认为 get                                                                        | String  | 否       |
| Query    | 签名中要签入的请求参数，{key: 'val'} 的格式                                                                                           | Object  | 否       |
| Headers  | 签名中要签入的请求头部，{key: 'val'} 的格式                                                                                           | Object  | 否       |
| Expires  | 签名几秒后失效，默认为 900 秒                                                                                                         | Number  | 否       |

### 返回值说明

返回值是一个字符串，两种情况：

1. 如果签名计算可以同步计算（如：实例化传入了 SecretId 和 SecretKey），则默认返回带签名的 url。
2. 否则返回不带签名的 url。

### 回调函数说明

```
function(err, data) { ... }
```

| 参数名 | 参数描述                                                                                                                                                | 类型   |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误，如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档 | Object |
| data   | 请求成功时返回的对象，如果请求发生错误，则为空                                                                                                          | Object |
| - Url  | 计算得到的 Url                                                                                                                                          | String |
