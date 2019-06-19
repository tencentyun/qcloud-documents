## 简介

提供获取对象 URL、获取请求预签名 URL 接口。

## 计算签名

COS XML API 的请求里，私有资源操作都需要鉴权凭证 Authorization，用于判断当前请求是否合法。

鉴权凭证使用方式有两种：

1. 放在 header 参数里使用，字段名：authorization
2. 放在 url 参数里使用，字段名：sign

COS.getAuthorization 方法用于计算鉴权凭证（Authorization），用以验证请求合法性的签名信息。

> !该方法推荐只在前端调试时使用，项目上线不推荐使用前端计算签名的方法，有暴露密钥的风险。

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

| 参数名    | 参数描述                                                     | 类型   | 必填 |
| --------- | ------------------------------------------------------------ | ------ | ---- |
| SecretId  | 用户的 SecretId                                              | String | 是   |
| SecretKey | 用户的 SecretKey                                             | String | 是   |
| Method    | 操作方法，如 get，post，delete， head 等 HTTP 方法           | String | 是   |
| Key       | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空 | String | 否   |
| Query     | 请求的 query 参数对象                                        | Object | 否   |
| Headers   | 请求的 header 参数对象                                       | Object | 否   |
| Expires   | 签名几秒后失效，默认900                                       | Number  | 否   |

#### 返回值说明

返回值是计算得到的鉴权凭证字符串 authorization。

## 获取请求预签名 URL

### 下载请求示例

示例一：获取不带签名 Object Url。

```js
var url = cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: false
});
```

示例二：获取带签名 Object Url。

```js
var url = cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg'
});
```

示例三：如果签名过程是异步获取，需要通过 callback 获取带签名 Url。

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: false
}, function (err, data) {
    console.log(err || data.Url);
});
```

示例四：指定链接有效时间

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: true,
    Expires: 3600, // 单位秒
}, function (err, data) {
    console.log(err || data.Url);
});
```

示例五：获取文件 Url 并下载文件。

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: true
}, function (err, data) {
    if (!err) return console.log(err);
    wx.downloadFile({
        url: data.Url, // 需要加 url 的域名作为下载白名单
        success (res) {
            console.log(res.statusCode, res.tempFilePath);
        },
        fail: function (err) {
            console.log(err);
        },
    });
});
```

### 上传请求说明

在小程序里上传只能通过 POST Object 接口上传文件。这里获取预签名 URL 不适合用在 POST Object接口
如果想自行上传文件，可参考 [小程序直传示例](https://cloud.tencent.com/document/product/436/34929)

### 参数说明

| 参数名  | 参数描述                                                     | 类型    | 必填 |
| ------- | ------------------------------------------------------------ | ------- | ---- |
| Bucket  | Bucket 的名称。命名规则为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | String  | 是   |
| Region  | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String  | 是   |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空 | String  | 是   |
| Sign    | 是否返回带有签名的 Url                                       | Boolean | 否   |
| Method  | 操作方法，如 get，post，delete， head 等 HTTP 方法，默认 get | String  | 否   |
| Query   | 参与签名计算的 query 参数对象                                | Object  | 否   |
| Headers | 参与签名计算的 header 参数对象                               | Object  | 否   |
| Expires | 签名几秒后失效，默认900                                      | Number  | 否   |

### 返回值说明

返回值是一个字符串，两种情况：

1. 如果签名计算可以同步计算（如：实例化传入了 SecretId 和 SecretKey），则默认返回带签名的 url。
2. 否则返回不带签名的 url。

### 回调函数说明

```
function(err, data) { ... }
```

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参阅 [错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| data   | 请求成功时返回的对象，如果请求发生错误，则为空               | Object |
| - Url  | 计算得到的 Url                                               | String |
