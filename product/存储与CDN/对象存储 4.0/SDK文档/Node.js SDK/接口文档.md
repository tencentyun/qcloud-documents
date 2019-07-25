>?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

Node.js SDK github 地址：[COS-Node.js-SDK-v5](https://github.com/tencentyun/cos-nodejs-sdk-v5)。

## Service操作

### Get Service

#### 功能说明

Get Service 接口实现获取该用户下所有 Bucket 列表。该 API 接口需要使用 Authorization 签名认证，且只能获取签名中 AccessID 所属账户的 Bucket 列表。

#### 操作方法原型

调用 Get Service 操作：

```js
cos.getService(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

>无特殊参数。

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| err        | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data       | 请求成功时返回的对象，请求错误则为空                         | Object |
| Owner      | 说明 Bucket 所有者的信息                                     | Object |
| uin        | Bucket 所有者的 UIN                                          | String |
| Buckets    | 说明本次返回的 Bucket 列表的所有信息                         | Array  |
| Name       | Bucket 名称                                                  | String |
| CreateDate | Bucket 创建时间，ISO8601 格式                                | String |



## 工具方法

### 获取预签名链接

#### 使用示例

示例一：获取不带签名 Object Url。

```js
var url = cos.getObjectUrl({
    Key: '1.jpg',
    Sign: false
});
```

示例二：获取带签名 Object Url。

```js
var url = cos.getObjectUrl({
    Key: '1.jpg'
});
```

示例三：如果签名过程是异步获取，需要通过 callback 获取带签名 Url。

```js
cos.getObjectUrl({
    Key: '1.jpg',
    Sign: false
}, function (err, data) {
    console.log(err || data.Url);
});
```

示例四：获取预签名 Put Object 上传 Url。

```js
cos.getObjectUrl({
    Method: 'PUT',
    Key: '1.jpg',
    Sign: true
}, function (err, data) {
    console.log(err || data.Url);
});
```

#### 参数说明

| 参数名  | 参数描述                                                     | 类型    | 必填 |
| ------- | ------------------------------------------------------------ | ------- | ---- |
| Bucket  | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String  | 是   |
| Region  | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String  | 是   |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空 | String  | 是   |
| Sign    | 是否返回带有签名的 Url                                       | Boolean | 否   |
| Method  | 操作方法，如 get，post，delete， head 等 HTTP 方法，默认 get | String  | 否   |
| Query   | 参与签名计算的 query 参数对象                                | Object  | 否   |
| Headers | 参与签名计算的 header 参数对象                               | Object  | 否   |

#### 返回值说明

返回值是一个字符串，两种情况：

1. 如果签名计算可以同步计算（如：实例化传入了 SecretId 和 SecretKey），则默认返回带签名的 URL。
2. 否则返回不带签名的 URL。

#### 回调函数说明

```
function(err, data) { ... }
```

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data   | 请求成功时返回的对象，请求错误则为空                         | Object |
| - Url  | 计算得到的 Url                                               | String |



## Bucket操作

### Head Bucket

#### 功能说明

Head Bucket 请求可以确认是否存在该 Bucket，是否有权限访问，Head 的权限与 Read 一致。

#### 操作方法原型

调用 Head Bucket 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名      | 参数描述                                                     | 类型    |
| ----------- | ------------------------------------------------------------ | ------- |
| err         | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data        | 请求成功时返回的对象，请求错误则为空                         | Object  |
| BucketExist | Bucket 是否存在                                              | Boolean |
| BucketAuth  | 是否拥有该 Bucket 的权限                                     | Boolean |

### Get Bucket

#### 功能说明 

Get Bucket 请求等同于 List Object 请求，可以列出该 Bucekt 下部分或者所有 Object，发起该请求需要拥有 Read 权限。

#### 操作方法原型

调用 Get Bucket 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE',	/* 必须 */
	Prefix : 'STRING_VALUE',	/* 非必须 */
	Delimiter : 'STRING_VALUE', /* 非必须 */
	Marker : 'STRING_VALUE',	/* 非必须 */
	MaxKeys : 'STRING_VALUE',	/* 非必须 */
	EncodingType : 'STRING_VALUE',	/* 非必须 */
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

| 参数名       | 参数描述                                                     | 类型   | 必填 |
| ------------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket       | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region       | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Prefix       | 前缀匹配，用来规定返回的对象键前缀地址                       | String | 否   |
| Delimiter    | 定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始 | String | 否   |
| Marker       | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从marker开始    | String | 否   |
| MaxKeys      | 单次返回最大的条目数量，默认1000                            | String | 否   |
| EncodingType | 规定返回值的编码方式                                         | String | 否   |



#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名         | 参数描述                                                     | 类型     |
| -------------- | ------------------------------------------------------------ | -------- |
| err            | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object   |
| data           | 请求成功时返回的对象，请求错误则为空                         | Object   |
| CommonPrefixes | 将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix | Array    |
| Prefix         | 前缀匹配，用来规定返回的对象键前缀地址                       | String   |
| Name           | Bucket 名字                                                  | String   |
| Prefix         | 对象键的前缀                                                 | String   |
| Marker         | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始    | String |
| MaxKeys        | 单次返回最大的条目数量                                       | String   |
| IsTruncated    | 返回条目是否被截断，'true' 或者 'false'                      | String   |
| NextMarker     | 假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点   | String   |
| Encoding-Type  | 编码类型，作用于Delimiter，Marker，Prefix，NextMarker，Key   | String   |
| Contents       | 元数据信息                                                   | Array    |
| ETag           | 文件的 SHA-1 算法校验值                                      | String   |
| Size           | 文件大小，单位 Byte                                          | String   |
| Key            | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String   |
| LastModified   | Object 最后修改时间                                          | String   |
| Owner          | Bucket 所有者信息                                            | Object   |
| ID             | Bucket 拥有者的 UID 信息                                     | String   |



### Put Bucket

#### 功能说明

Put Bucket 请求可以在指定账号下创建一个 Bucket。

#### 操作方法原型

调用 Put Bucket 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE',	/* 必须 */
	ACL : 'STRING_VALUE',	/* 非必须 */
	GrantRead : 'STRING_VALUE', /* 非必须 */
	GrantWrite : 'STRING_VALUE',	/* 非必须 */
	GrantFullControl : 'STRING_VALUE'	/* 非必须 */
};

cos.putBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

| 参数名           | 参数描述                                                     | 类型   | 必填 |
| ---------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket           | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region           | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| ACL              | 允许用户自定义文件权限。有效值：private、public-read、public-read-write，默认值：private | String | 否   |
| GrantRead        | 赋予被授权者读的权限，格式 x-cos-grant-read: uin=" ",uin=" "<br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"<br>当需要给根账户授权时，uin="RootAcountID" | String | 否   |
| GrantWrite       | 赋予被授权者写的权限，格式 x-cos-grant-write: uin=" ",uin=" "<br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"<br>当需要给根账户授权时，uin="RootAcountID" | String | 否   |
| GrantFullControl | 赋予被授权者读写权限，格式 x-cos-grant-full-control: uin=" ",uin=" "<br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"<br>当需要给根账户授权时，uin="RootAcountID" | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名   | 参数描述                                                     | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| err      | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data     | 请求成功时返回的对象，请求错误则为空                         | Object |
| Location | 创建成功后，Bucket 的操作地址                                | String |

### Delete Bucket

#### 功能说明

Delete Bucket 请求可以在指定账号下删除 Bucket，删除之前要求 Bucket为空。

#### 操作方法原型

 调用 Delete Bucket 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名              | 参数描述                                                     | 类型    |
| ------------------- | ------------------------------------------------------------ | ------- |
| err                 | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data                | 请求成功时返回的对象，请求错误则为空                         | Object  |
| DeleteBucketSuccess | 删除是否成功                                                 | Boolean |

### Get Bucket ACL

#### 功能说明

使用 API 读取 Bucket 的 ACL 表，只有所有者有权操作。

#### 操作方法原型

调用 Get Bucket ACL 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名            | 参数描述                                                     | 类型   |
| ----------------- | ------------------------------------------------------------ | ------ |
| err               | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data              | 请求成功时返回的对象，请求错误则为空                         | Object |
| Owner             | 标识资源的所有者                                             | Object |
| uin               | 用户 QQ 号                                                     | String |
| AccessControlList | 被授权者信息与权限信息                                       | Object |
| Grant             | 具体的授权信息                                               | Array  |
| Permission        | 权限信息，枚举值：READ，WRITE，FULL_CONTROL                  | String |
| Grantee           | 被授权者资源信息                                             | Object |
| uin               | 被授权者的 QQ 号码或者 'anonymous'                           | String |
| Subacount         | 子账户 QQ 账号                                               | String |

### Put Bucket ACL

#### 功能说明

使用 API 写入 Bucket 的 ACL 表，Put Bucket ACL 是一个覆盖操作，传入新的 ACL 将覆盖原有 ACL。只有所有者有权操作。

#### 操作方法原型

调用 Put Bucket ACL 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',			/* 必须 */
	Region : 'STRING_VALUE',			/* 必须 */
	ACL : 'STRING_VALUE',				/* 非必须 */
	GrantRead : 'STRING_VALUE', 		/* 非必须 */
	GrantWrite : 'STRING_VALUE',		/* 非必须 */
	GrantFullControl : 'STRING_VALUE'	/* 非必须 */
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

| 参数名           | 参数描述                                                     | 类型   | 必填 |
| ---------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket           | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region           | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| ACL              | 允许用户自定义文件权限。有效值：private，public-read，public-read-write。默认值：private。 | String | 否   |
| GrantRead        | 赋予被授权者读的权限，格式：id="[OwnerUin]"   | String | 否   |
| GrantWrite       | 赋予被授权者写的权限，格式：id="[OwnerUin]"   | String | 否   |
| GrantFullControl | 赋予被授权者读写权限，格式：id="[OwnerUin]"   | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名             | 参数描述                                                     | 类型    |
| ------------------ | ------------------------------------------------------------ | ------- |
| err                | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data               | 请求成功时返回的对象，请求错误则为空                         | Object  |
| BucketGrantSuccess | 授权是否成功                                                 | Boolean |

### Get Bucket CORS

#### 功能说明

Get Bucket CORS 实现跨域访问读取。

#### 操作方法原型

调用 Get Bucket CORS 操作
```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名        | 参数描述                                                     | 类型   |
| ------------- | ------------------------------------------------------------ | ------ |
| err           | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data          | 请求成功时返回的对象，请求错误则为空                         | Object |
| CORSRule      | 配置的信息集合                                               | Array  |
| AllowedMethod | 允许的 HTTP 操作，枚举值：Get，Put，Head，Post，Delete       | Array  |
| AllowedOrigin | 允许的访问来源，支持『 * 』通配符                            | Array  |
| AllowedHeader | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部 | Array  |
| ExposeHeader  | 设置浏览器可以接收到的来自服务器端的自定义头部信息           | Array  |
| MaxAgeSeconds | 设置 OPTIONS 请求得到结果的有效期                            | String |
| ID            | 规则名称                                                     | String |

### Put Bucket CORS

#### 功能说明

Put Bucket CORS 实现跨域访问读写。

#### 操作方法原型

调用 Put Bucket CORS 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',		/* 必须 */
	Region : 'STRING_VALUE',		/* 必须 */
	CORSRules : [
		{
			ID : 'STRING_VALUE',	/* 非必须 */
			AllowedMethods: [ 		/* 必须 */
			  'STRING_VALUE',
			  ...
			],
			AllowedOrigins: [		 /* 必须 */
			  'STRING_VALUE',
			  ...
			],
			AllowedHeaders: [		/* 非必须 */
			  'STRING_VALUE',
			  ...
			],
			ExposeHeaders: [		/* 非必须 */
				'STRING_VALUE',
				...
			],
			MaxAgeSeconds: 'STRING_VALUE'	/* 非必须 */
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

| 参数名         | 参数描述                                                     | 类型   | 必填 |
| -------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket         | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region         | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| CORSRules      | 跨域规则集合                                                 | Array  | 否   |
| ID             | 规则名称                                                     | String | 否   |
| AllowedMethods | 允许的HTTP操作，枚举值：Get，Put，Head，Post，Delete         | Array  | 是   |
| AllowedOrigins | 允许的访问来源，支持`* `通配符，协议，端口和域名必须一致  | Array  | 是   |
| AllowedHeaders | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持 `*` 通配符 | Array  | 否   |
| ExposeHeaders  | 设置浏览器可以接收到的来自服务器端的自定义头部信息           | Array  | 否   |
| MaxAgeSeconds  | 设置 OPTIONS 请求得到结果的有效期                            | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名               | 参数描述                                                     | 类型    |
| -------------------- | ------------------------------------------------------------ | ------- |
| err                  | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data                 | 请求成功时返回的对象，请求错误则为空                         | Object  |
| PutBucketCorsSucesss | 设置Bucket CORS 是否成功                                     | Boolean |

### Delete Bucket CORS

#### 功能说明

Delete Bucket CORS 实现跨域访问读取。

#### 操作方法原型

调用 Delete Bucket CORS 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',		/* 必须 */
	Region : 'STRING_VALUE'			/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名                  | 参数描述                                                     | 类型    |
| ----------------------- | ------------------------------------------------------------ | ------- |
| err                     | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data                    | 请求成功时返回的对象，请求错误则为空                         | Object  |
| DeleteBucketCorsSuccess | 删除 Bucket CORS 是否成功                                    | Boolean |

### Get Bucket Location

#### 功能说明

Get Bucket Location 接口获取 Bucket 所在地域信息，只有 Bucket 所有者有权限读取信息。

#### 操作方法原型

调用 Get Bucket Location 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',		/* 必须 */
	Region : 'STRING_VALUE'			/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名             | 参数描述                                                     | 类型   |
| ------------------ | ------------------------------------------------------------ | ------ |
| err                | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data               | 请求成功时返回的对象，请求错误则为空                         | Object |
| LocationConstraint | Bucket 所在地域，枚举值：china-east，china-south，china-north，china-west，singapore | String |

### Get Bucket Tagging

#### 功能说明

Get Bucket Tagging 接口实现获取指定 Bucket 的标签。

#### 操作方法原型

调用 Get Bucket Tagging 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
};

cos.getBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});
```

#### 操作参数说明

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data   | 请求成功时返回的对象，请求错误则为空                         | Object |
| Tags   | Bucket 的标签集合                                            | Array  |
| Key    | Tag 的类别名称                                               | String |
| Value  | Tag 的值                                                     | String |

### Put Bucket Tagging

#### 功能说明

Put Bucket Tagging 接口实现给用指定 Bucket 打标签。

#### 操作参数说明

 调用 Put Bucket Tagging 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE',	/* 必须 */
	Tags :  [
		{
			Key : 'key1',		/* 必须 */
			Value : 'value1'	/* 必须 */
		},
		...
	]
};

cos.putBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});
```

#### 操作参数说明

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Tags   | Bucket 的标签集合                                            | Array  | 是   |
| Key    | Tag 的类别名称                                               | String | 是   |
| Value  | Tag 的值                                                     | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名                  | 参数描述                                                     | 类型    |
| ----------------------- | ------------------------------------------------------------ | ------- |
| err                     | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)，请求成功则为空 | Object  |
| data                    | 请求成功时返回的对象，请求错误则为空                         | Object  |
| PutBucketTaggingSuccess | 设置 Tag 是否成功                                            | Boolean |

### Delete Bucket Tagging

#### 功能说明

Delete Bucket Tagging 接口实现删除指定 Bucket 的标签。

#### 操作方法原型

调用 Delete Bucket Tagging 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
};

cos.deleteBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});
```

#### 操作参数说明

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名                     | 参数描述                                                     | 类型    |
| -------------------------- | ------------------------------------------------------------ | ------- |
| err                        | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data                       | 请求成功时返回的对象，请求错误则为空                         | Object  |
| DeleteBucketTaggingSuccess | 删除 Bukcet 标签是否成功                                     | Boolean |

## Object操作

### Head Object

#### 功能说明

Head Object 请求可以取回对应 Object 的元数据，Head 的权限与 Get 的权限一致。

#### 操作方法原型

调用 Head Object 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',		/* 必须 */
	Region : 'STRING_VALUE',		/* 必须 */
	Key : 'STRING_VALUE',			/* 必须 */
	IfModifiedSince : 'STRING_VALUE'	/* 非必须 */
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

| 参数名          | 参数描述                                                     | 类型   | 必填 |
| --------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket          | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region          | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key             | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| IfModifiedSince | 当 Object 在指定时间后被修改，则返回对应 Object 元信息       | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名              | 参数描述                                                     | 类型    |
| ------------------- | ------------------------------------------------------------ | ------- |
| err                 | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data                | 请求成功时返回的对象，请求错误则为空                         | Object  |
| x-cos-object-type   | 用来表示 Object 是否可以被追加上传，枚举值：norma l或者 appendable | String  |
| x-cos-storage-class | Object 的存储类型，枚举值：STANDARD，STANDARD_IA，ARCHIVE              | String  |
| x-cos-meta-*       | 用户自定义的元数据                                           | String  |
| NotModified         | 如果请求时带有 IfModifiedSince ，且文件未被修改，则为 true   | Boolean |

### Get Object

#### 功能说明

Get Object 请求可以将一个文件（Object）下载至本地。该操作需要对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

#### 操作方法原型

调用 Get Object 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE',							/* 必须 */
	ResponseContentType : 'STRING_VALUE',			/* 非必须 */
	ResponseContentLanguage : 'STRING_VALUE',		/* 非必须 */
	ResponseExpires : 'STRING_VALUE',				/* 非必须 */
	ResponseCacheControl : 'STRING_VALUE',			/* 非必须 */
	ResponseContentDisposition : 'STRING_VALUE',	/* 非必须 */
	ResponseContentEncoding : 'STRING_VALUE',		/* 非必须 */
	Range : 'STRING_VALUE',							/* 非必须 */
	IfModifiedSince : 'STRING_VALUE',				/* 非必须 */
	Output : 'STRING_VALUE' || 'WRITE_STRING'		/* 非必须 */
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

| 参数名                     | 参数描述                                                     | 类型                 | 必填 |
| -------------------------- | ------------------------------------------------------------ | -------------------- | ---- |
| Bucket                     | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String               | 是   |
| Region                     | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String               | 是   |
| Key                        | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String               | 是   |
| ResponseContentType        | 设置返回头部中的 Content-Type 参数                           | String               | 否   |
| ResponseContentLanguage    | 设置返回头部中的 Content-Language 参数                       | String               | 否   |
| ResponseExpires            | 设置返回头部中的 Content-Expires 参数                        | String               | 否   |
| ResponseCacheControl       | 设置返回头部中的 Cache-Control 参数                          | String               | 否   |
| ResponseContentDisposition | 设置返回头部中的 Content-Disposition 参数                    | String               | 否   |
| ResponseContentEncoding    | 设置返回头部中的 Content-Encoding 参数                       | String               | 否   |
| Range                      | RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位     | String               | 否   |
| IfModifiedSince            | 如果文件修改时间晚于指定时间，才返回文件内容                 | String               | 否   |
| Output                     | 输出的文件路径或者一个写流，若不传入，则将完整内容写入回调函数 data   | String/WriteStream | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名              | 参数描述                                                     | 类型    |
| ------------------- | ------------------------------------------------------------ | ------- |
| err                 | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)，请求成功则为空 | Object  |
| data                | 请求成功时返回的对象，请求错误则为空                         | Object  |
| x-cos-object-type   | 用来表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable | String  |
| x-cos-storage-class | Object 的存储类型，枚举值：STANDARD，STANDARD_IA              | String  |
| x-cos-meta-*       | 用户自定义的元数据                                           | String  |
| NotModified         | 如果请求时带有 IfModifiedSince ，且文件未被修改，则为 true   | Boolean |

### Put Object

#### 功能说明

Put Object 请求可以将一个文件（Oject）上传至指定 Bucket。

>!
>1. Key（文件名）不能以 `/` 结尾，否则会被识别为文件夹 。
>2. 当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请在上传时不要设置，默认继承 Bucket 权限。

#### 操作方法原型

调用 Put Object 操作：

```js
cos.putObject({
    Bucket : 'STRING_VALUE',                        /* 必须 */
    Region : 'STRING_VALUE',                        /* 必须 */
    Key : 'STRING_VALUE',                           /* 必须 */
    Body: fs.createReadStream('./a.zip'),           /* 必须 */
    onProgress: function (progressData) {
        console.log(progressData);
    },
}, function(err, data) {
    if(err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
```

#### 操作参数说明

| 参数名             | 参数描述                                                     | 类型           | 必填 |
| ------------------ | ------------------------------------------------------------ | -------------- | ---- |
| Bucket             | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String         | 是   |
| Region             | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String         | 是   |
| Key                | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String         | 是   |
| CacheControl       | RFC 2616 中定义的缓存策略，将作为 Object 元数据保存          | String         | 否   |
| ContentDisposition | RFC 2616 中定义的文件名称，将作为 Object 元数据保存          | String         | 否   |
| ContentEncoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据保存          | String         | 否   |
| ContentLength      | RFC 2616 中定义的 HTTP 请求内容长度（字节）                  | String         | 否   |
| ContentType        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存  | String         | 否   |
| Expect             | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容 | String         | 否   |
| Expires            | RFC 2616 中定义的过期时间，将作为 Object 元数据保存          | String         | 否   |
| ContentSha1        | RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值              | String         | 否   |
| ACL                | 允许用户自定义文件权限，有效值：private，public-read         | String         | 否   |
| GrantRead          | 赋予被授权者读的权限。格式：id="[OwnerUin]"   | String         | 否   |
| GrantFullControl   | 赋予被授权者所有的权限。格式：id="[OwnerUin]" | String         | 否   |
| x-cos-meta-*      | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K | String         | 否   |
| Body               | 传入文件路径或文件流                                         | String/ Stream | 是   |
| onProgress         | 进度回调函数，回调是一个对象，包含进度信息                   | Function       | 否   |
| StorageClass       | 设置 Object 的存储类型，枚举值：STANDARD，STANDARD_IA，ARCHIVE  |String         | 否   |


#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data   | 请求成功时返回的对象，请求错误则为空                         | Object |
| ETag   | 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化 | String |

### Delete Object

#### 功能说明

Delete Object 请求可以将一个文件（Object）删除。

#### 操作方法原型

调用 Delete Object 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE'							/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key    | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名              | 参数描述                                                     | 类型    |
| ------------------- | ------------------------------------------------------------ | ------- |
| err                 | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data                | 请求成功时返回的对象，请求错误则为空                         | Object  |
| DeleteObjectSuccess | 删除文件是否成功                                             | Boolean |
| BucketNotFound      | 如果找不到指定的 Bucket，则为 true                           | Boolean |

### Options Object

#### 功能说明

Options Object 请求实现跨域访问的预请求。即发出一个 OPTIONS 请求给服务器以确认是否可以进行跨域操作。

#### 操作方法原型

调用 Options Object 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',		/* 必须 */
	Region : 'STRING_VALUE',		/* 必须 */
	Key : 'STRING_VALUE',			/* 必须 */
	Origin : 'STRING_VALUE', 		/* 必须 */
	AccessControlRequestMethod : 'STRING_VALUE', 		/* 必须 */
	AccessControlRequestHeaders : 'STRING_VALUE'		/* 非必须 */
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

| 参数名                      | 参数描述                                                     | 类型   | 必填 |
| --------------------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket                      | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region                      | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key                         | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| Origin                      | 模拟跨域访问的请求来源域名                                   | String | 是   |
| AccessControlRequestMethod  | 模拟跨域访问的请求 HTTP 方法                                   | String | 是   |
| AccessControlRequestHeaders | 模拟跨域访问的请求头部                                       | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名                     | 参数描述                                                     | 类型   |
| -------------------------- | ------------------------------------------------------------ | ------ |
| err                        | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data                       | 请求成功时返回的对象，请求错误则为空                         | Object |
| AccessControlAllowOrigin   | 模拟跨域访问的请求来源域名，当来源不允许的时候，此 Header 不返回 | String |
| AccessControlAllowMethods  | 模拟跨域访问的请求 HTTP 方法，当请求方法不允许的时候，此 Header 不返回 | String |
| AccessControlAllowHeaders  | 模拟跨域访问的请求头部，当模拟任何请求头部不允许的时候，此 Header 不返回该请求头部 | String |
| AccessControlExposeHeaders | 跨域支持返回头部，用逗号区分                                 | String |
| AccessControlMaxAge        | 设置 OPTIONS 请求得到结果的有效期                            | String |

### Get Object ACL

#### 功能说明

Get Object ACL 接口实现使用 API 读取 Object 的 ACL 表，只有所有者有权操作。

#### 操作方法原型

调用 Get Object ACL 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE'							/* 必须 */
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

| 参数名 | 参数描述                                                     | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key    | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名            | 参数描述                                                     | 类型   |
| ----------------- | ------------------------------------------------------------ | ------ |
| err               | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data              | 请求成功时返回的对象，请求错误则为空                         | Object |
| Owner             | 标识资源的所有者                                             | Object |
| uin               | 用户 QQ 号                                                     | String |
| AccessControlList | 被授权者信息与权限信息                                       | Object |
| Grant             | 具体的授权信息                                               | Array  |
| Permission        | 权限信息，枚举值：READ，WRITE，FULL_CONTROL                  | String |
| Grantee           | 被授权者资源信息                                             | Object |
| uin               | 被授权者的 QQ 号码或者 'anonymous'                           | String |
| Subacount         | 子账户 QQ 账号                                               | String |

### Put Object ACL

#### 功能说明

Put Object ACL使用 API 写入 Object 的 ACL 表。当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承 Bucket 权限。

#### 操作方法原型

 调用 Put Object ACL 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',			/* 必须 */
	Region : 'STRING_VALUE',			/* 必须 */
	Key : 'STRING_VALUE',				/* 必须 */
	ACL : 'STRING_VALUE',				/* 非必须 */
	GrantRead : 'STRING_VALUE', 		/* 非必须 */
	GrantWrite : 'STRING_VALUE',		/* 非必须 */
	GrantFullControl : 'STRING_VALUE'	/* 非必须 */
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

| 参数名           | 参数描述                                                     | 类型   | 必填 |
| ---------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket           | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region           | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key              | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| ACL              | 允许用户自定义文件权限。有效值：private、public-read。默认值：private。 | String | 否   |
| GrantRead        | 赋予被授权者读的权限。格式：id="[OwnerUin]"   | String | 否   |
| GrantFullControl | 赋予被授权者所有的权限。格式：id="[OwnerUin]" | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data   | 请求成功时返回的对象，请求错误则为空                         | Object |

### Delete Multiple Object

#### 功能说明

Delete Multiple Object 请求实现批量删除文件，最大支持单次删除1000个文件。对于返回结果，COS 提供 Verbose 和 Quiet 两种结果模式，Verbose 模式将返回每个 Object 的删除结果，Quiet 模式只返回报错的 Object 信息。

#### 操作方法原型

 调用 Delete Multiple Object 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Quiet : 'BOOLEAN_VALUE',						/* 非必须 */
	Objects :  [
	    {
	        Key : 'STRING_VALUE'					/* 必须 */
        }
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

| 参数名  | 参数描述                                                     | 类型    | 必填 |
| ------- | ------------------------------------------------------------ | ------- | ---- |
| Bucket  | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String  | 是   |
| Region  | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String  | 是   |
| Quiet   | 布尔值，这个值决定了是否启动 Quiet 模式，True 启动 Quiet 模式，False 启动 Verbose 模式，默认 False | Boolean | 否   |
| Objects | 要删除的文件列表                                             | Array   | 否   |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String  | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名  | 参数描述                                                     | 类型   |
| ------- | ------------------------------------------------------------ | ------ |
| err     | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data    | 请求成功时返回的对象，请求错误则为空                         | Object |
| Deleted | 说明本次删除的成功 Object 信息                               | Array  |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| Error   | 说明本次删除的失败 Object 信息                               | Array  |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| Code    | 删除失败的错误码                                             | String |
| Message | 删除错误信息                                                 | String |

## 分块上传操作

### Initiate Multipart Upload

#### 功能说明

Initiate Multipart Upload 请求实现初始化分片上传，成功执行此请求以后会返回 Upload ID 用于后续的 Upload Part 请求。

#### 操作方法原型

 调用 Initiate Multipart Upload 操作：

```js
cos.multipartInit({
    Bucket : 'STRING_VALUE',						/* 必须 */
    Region : 'STRING_VALUE',						/* 必须 */
    Key : 'STRING_VALUE',							/* 必须 */
}, function(err, data) {
    if(err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
```

#### 操作参数说明

| 参数名             | 参数描述                                                     | 类型   | 必填 |
| ------------------ | ------------------------------------------------------------ | ------ | ---- |
| Bucket             | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region             | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key                | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| CacheControl       | RFC 2616 中定义的缓存策略，将作为 Object 元数据保存          | String | 否   |
| ContentDisposition | RFC 2616 中定义的文件名称，将作为 Object 元数据保存          | String | 否   |
| ContentEncoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据保存          | String | 否   |
| ContentType        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存  | String | 否   |
| Expires            | RFC 2616 中定义的过期时间，将作为 Object 元数据保存          | String | 否   |
| ACL                | 允许用户自定义文件权限，有效值：private，public-read         | String | 否   |
| GrantRead          | 赋予被授权者读的权限，格式x-cos-grant-read: uin=" ",uin=" "，<br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"，<br>当需要给根账户授权时，uin="RootAcountID" | String | 否   |
| GrantWrite         | 赋予被授权者写的权限，格式x-cos-grant-write: uin=" ",uin=" "，<br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"，<br>当需要给根账户授权时，uin="RootAcountID" | String | 否   |
| GrantFullControl   | 赋予被授权者读写权限，格式x-cos-grant-full-control: uin=" ",uin=" "，<br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"，<br>当需要给根账户授权时，uin="RootAcountID" | String | 否   |
| StorageClass       | 设置 Object 的存储类型，枚举值：STANDARD，STANDARD_IA，ARCHIVE。默认值：STANDARD | String | 否   |
| x-cos-meta-*      | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名   | 参数描述                                                     | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| err      | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data     | 请求成功时返回的对象，请求错误则为空                         | Object |
| Bucket   | 分片上传的目标 Bucket                                        | String |
| Key      | Object 的名称                                                | String |
| UploadId | 在后续上传中使用的 ID                                         | String |

### Upload Part

#### 功能说明


Upload Part 请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1MB到5GB。在每次请求Upload Part 时候，需要携带 partNumber 和 uploadID，partNumber 为块的编号，支持乱序上传。

#### 操作方法原型

调用 Upload Part 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE',							/* 必须 */
	ContentLength : 'STRING_VALUE',					/* 必须 */
	Expect : 'STRING_VALUE',						/* 非必须 */
	ContentSha1 : 'STRING_VALUE',					/* 非必须 */
	PartNumber : 'STRING_VALUE',					/* 必须 */
	UploadId : 'STRING_VALUE',						/* 必须 */
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

| 参数名        | 参数描述                                                     | 类型   | 必填 |
| ------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket        | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region        | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key           | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| ContentLength | RFC 2616 中定义的 HTTP 请求内容长度（字节）                  | String | 是   |
| Expect        | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容 | String | 否   |
| ContentSha1   | RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值              | String | 否   |
| PartNumber    | 分块的编号                                                   | String | 是   |
| UploadId      | 上传任务编号                                                 | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data   | 请求成功时返回的对象，请求错误则为空                         | Object |
| ETag   | 分块的 ETag 值，为 SHA1 校验值                               | String |

### Complete Multipart Upload

#### 功能说明

Complete Multipart Upload 用来实现完成整个分块上传。当您已经使用 Upload Parts 上传所有块以后，您可以用该 API 完成上传。在使用该 API 时，您必须在 Body 中给出每一个块的 PartNumber 和 ETag，用来校验块的准确性。

#### 操作方法原型

调用 Complete Multipart Upload 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE',							/* 必须 */
	UploadId : 'STRING_VALUE',						/* 必须 */
	Parts : [
		{
			PartNumber : 'STRING_VALUE',			/* 必须 */
			ETag : 'STRING_VALUE'					/* 必须 */
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

| 参数名     | 参数描述                                                     | 类型   | 必填 |
| ---------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket     | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region     | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key        | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| UploadId   | 上传任务编号                                                 | String | 是   |
| Parts      | 分块的 ETag 信息                                              | Array  | 是   |
| PartNumber | 分块的编号                                                   | String | 是   |
| ETag       | 分块的 ETag 值，为 SHA1 校验值，需要在校验值前后加上双引号，如 "3a0f1fd698c235af9cf098cb74aa25bc" | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名   | 参数描述                                                     | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| err      | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data     | 请求成功时返回的对象，请求错误则为空                         | Object |
| Location | 创建的 Object 的外网访问域名                                 | String |
| Bucket   | 分块上传的目标 Bucket                                        | String |
| Key      | Object 的名称                                                | String |
| ETag     | 合并后文件的 MD5 算法校验值                                  | String |

### List Parts

#### 功能说明

List Parts用来查询特定分块上传中的已上传的块。

#### 操作方法原型

调用 List Parts 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE',							/* 必须 */
	UploadId : 'STRING_VALUE',						/* 必须 */
	EncodingType : 'STRING_VALUE',					/* 非必须 */
	MaxParts : 'STRING_VALUE',						/* 非必须 */
	PartNumberMarker : 'STRING_VALUE'				/* 非必须 */
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

| 参数名           | 参数描述                                                     | 类型   | 必填 |
| ---------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket           | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region           | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key              | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| UploadId         | 上传任务编号                                                 | String | 是   |
| EncodingType     | 规定返回值的编码方式                                         | String | 否   |
| MaxParts         | 单次返回最大的条目数量，默认1000                             | String | 否   |
| PartNumberMarker | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始  | String | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名               | 参数描述                                                     | 类型   |
| -------------------- | ------------------------------------------------------------ | ------ |
| err                  | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data                 | 请求成功时返回的对象，请求错误则为空                         | Object |
| Bucket               | 分块上传的目标 Bucket                                        | String |
| Encoding-type        | 规定返回值的编码方式                                         | String |
| Key                  | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| UploadID             | 标示本次分块上传的 ID                                        | String |
| Initiator            | 用来表示本次上传发起者的信息，子节点包括 UID                 | Object |
| UID                  | 开发商 APPID                                                 | String |
| Owner                | 用来表示这些分块所有者的信息，子节点包括 UID                 | Object |
| UID                  | 拥有者 qq                                                    | String |
| StorageClass         | 用来表示这些分块的存储类型，枚举值：STANDARD，STANDARD_IA，ARCHIVE    | String |
| PartNumberMarker     | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始  | String |
| NextPartNumberMarker | 假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点   | String |
| MaxParts             | 单次返回最大的条目数量                                       | String |
| IsTruncated          | 返回条目是否被截断，'true' 或者 'false'                      | String |
| Part                 | 分块信息集合                                                 | Array  |
| PartNumber           | 分块编号                                                     | String |
| LastModified         | 块最后修改时间                                               | String |
| Etag                 | 块的 SHA-1 算法校验值                                        | String |
| Size                 | 块大小，单位 Byte                                            | String |

### Abort Multipart Upload

#### 功能说明

Abort Multipart Upload 用来实现舍弃一个分块上传并删除已上传的块。当您调用 Abort Multipart Upload 时，如果有正在使用这个 Upload Parts 上传块的请求，则 Upload Parts 会返回失败。

#### 操作方法原型

调用 Abort Multipart Upload 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE',							/* 必须 */
	UploadId : 'STRING_VALUE'						/* 必须 */
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

| 参数名   | 参数描述                                                     | 类型   | 必填 |
| -------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket   | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region   | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Key      | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String | 是   |
| UploadId | 上传任务编号                                                 | String | 是   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名                | 参数描述                                                     | 类型    |
| --------------------- | ------------------------------------------------------------ | ------- |
| err                   | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object  |
| data                  | 请求成功时返回的对象，请求错误则为空                         | Object  |
| MultipartAbortSuccess | Multipart Abort 是否成功                                     | Boolean |

### List Multipart Uploads

#### 功能说明

List Multiparts Uploads 用来查询正在进行中的分块上传。单次最多列出1000个正在进行中的分块上传。

#### 操作方法原型

调用 List Multipart Uploads 操作：

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Delimiter : 'STRING_VALUE',						/* 非必须 */
	EncodingType : 'STRING_VALUE',					/* 非必须 */
	Prefix : 'STRING_VALUE',						/* 非必须 */
	MaxUploads : 'STRING_VALUE',					/* 非必须 */
	KeyMarker : 'STRING_VALUE',						/* 非必须 */
	UploadIdMarker : 'STRING_VALUE'					/* 非必须 */
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

| 参数名         | 参数描述                                                     | 类型   | 必填 |
| -------------- | ------------------------------------------------------------ | ------ | ---- |
| Bucket         | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String | 是   |
| Region         | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String | 是   |
| Delimiter      | 界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始 | String | 否   |
| EncodingType   | 规定返回值的编码方式                                         | String | 否   |
| Prefix         | 前缀匹配，用来规定返回的对象键前缀地址                       | String | 否   |
| MaxUploads     | 单次返回最大的条目数量，默认1000                             | String | 否   |
| KeyMarker      | 与upload-id-marker一起使用，<br><li>当 upload-id-marker 未被指定时，<br>ObjectName 字母顺序大于 key-marker 的条目将被列出；<br> <li>当 upload-id-marker 被指定时，<br>ObjectName 字母顺序大于 key-marker 的条目被列出，<br>ObjectName 字母顺序等于 key-marker 且 UploadID 大于 upload-id-marker 的条目将被列出。 | String | 否   |
| UploadIdMarker | 与key-marker一起使用<br><li>当key-marker未被指定时，<br>upload-id-marker将被忽略；<br><li>当key-marker被指定时，<br>ObjectName字母顺序大于key-marker的条目被列出，<br>ObjectName字母顺序等于 key-marker 且 UploadID 大于 upload-id-marker 的条目将被列出 | String | 否   |

</li>

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名             | 参数描述                                                     | 类型   |
| ------------------ | ------------------------------------------------------------ | ------ |
| err                | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data               | 请求成功时返回的对象，请求错误则为空                         | Object |
| Bucket             | 分块上传的目标 Bucket                                        | String |
| Encoding-type      | 规定返回值的编码方式                                         | String |
| KeyMarker          | 列出条目从该 key 值开始                                      | String |
| UploadIdMarker     | 列出条目从该 UploadId 值开始                                 | String |
| NextKeyMarker      | 假如返回条目被截断，则返回 NextKeyMarker 就是下一个条目的起点 | String |
| NextUploadIdMarker | 假如返回条目被截断，则返回 UploadId 就是下一个条目的起点     | String |
| IsTruncated        | 返回条目是否被截断，'true' 或者 'false'                      | String |
| delimiter          | 定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始 | String |
| CommonPrefixs      | 将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix | Array  |
| Prefix             | 前缀匹配，用来规定返回的对象键前缀地址                       | String |
| Upload             | Upload 的信息集合                                            | Array  |
| Key                | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| UploadID           | 标示本次分块上传的 ID                                        | String |
| StorageClass       | 用来表示分块的存储类型，枚举值：STANDARD，STANDARD_IA，ARCHIVE        | String |
| Initiator          | 用来表示本次上传发起者的信息，子节点包括 UID                 | Object |
| UID                | 开发商 APPID                                                 | String |
| Owner              | 用来表示这些分块所有者的信息，子节点包括 UID                 | Object |
| UID                | 拥有者 qq                                                    | String |
| Initiated          | 分块上传的起始时间                                           | String |

### Slice Upload File

#### 功能说明

Slice Upload File 可用于实现文件的分块上传。

#### 操作方法原型

调用 Slice Upload File 操作：

```js
var params = {
	Bucket: 'STRING_VALUE',	/* 必须 */
	Region: 'STRING_VALUE',	/* 必须 */
	Key: 'STRING_VALUE',	/* 必须 */
	FilePath: 'STRING_VALUE',	/* 必须 */
	SliceSize: 'STRING_VALUE',	/* 非必须 */
	AsyncLimit: 'NUMBER_VALUE',	/* 非必须 */
    onHashProgress: function (progressData) {
        console.log(JSON.stringify(progressData));
    },
    onProgress: function (progressData) {
        console.log(JSON.stringify(progressData));
    },
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

| 参数名         | 参数描述                                                     | 类型     | 必填 |
| -------------- | ------------------------------------------------------------ | -------- | ---- |
| Bucket         | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String   | 是   |
| Region         | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String   | 是   |
| Key            | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String   | 是   |
| FilePath       | 本地文件路径                                                 | String   | 是   |
| SliceSize      | 分块大小                                                     | String   | 否   |
| AsyncLimit     | 分块的并发量                                                 | String   | 否   |
| onHashProgress | 计算文件 sha1 值的进度回调函数，回调是一个对象，包含进度信息 | Function | 否   |
| onProgress     | 进度回调函数，回调是一个对象，包含进度信息                   | Function | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名   | 参数描述                                                     | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| err      | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data     | 请求成功时返回的对象，请求错误则为空                         | Object |
| Location | 创建的 Object 的外网访问域名                                 | String |
| Bucket   | 分块上传的目标 Bucket                                        | String |
| Key      | Object 的名称                                                | String |
| ETag     | 合并后文件的 SHA-1 算法校验值                                | String |

#### 进度回调参数

| 参数名     | 参数描述           | 类型   |
| ---------- | ------------------ | ------ |
| SliceSize  | 分块大小           | String |
| PartNumber | 上传成功的分块编号 | Number |
| FileSize   | 文件总大小         | Number |

### Slice Copy File

#### 功能说明

Slice Copy File 可用于实现将一个文件从源路径复制到目标路径。在拷贝的过程中，文件元属性和 ACL 可以被修改。用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。

#### 操作方法原型

调用 Slice Copy File 操作：

```js
cos.sliceCopyFile({
    Bucket: 'STRING_VALUE',                               /* 必须 */
    Region: 'STRING_VALUE',                               /* 必须 */
    Key: 'STRING_VALUE',                                  /* 必须 */
    CopySource: 'STRING_VALUE', 			  /* 必须 */
    SliceSize: 'NUMBER_VALUE',                            /* 非必须 */
    onProgress:function (progressData) {                  /* 非必须 */
        console.log(JSON.stringify(progressData));
    }
},function (err,data) {
    console.log(err || data);
});

```

#### 操作参数说明

| 参数名     | 参数描述                                                     | 类型     | 必填 |
| ---------- | ------------------------------------------------------------ | -------- | ---- |
| Bucket     | Bucket 的名称。命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String   | 是   |
| Region     | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String   | 是   |
| Key        | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String   | 是   |
| CopySource | 源文件 URL 路径，可以通过 versionid 子资源指定历史版本       | String   | 是   |
| ChunkSize  | 分片复制时，每片的大小字节数，默认值 1048576（1MB）           | Number   | 否   |
| SliceSize  | 使用分片复制的文件大小，默认值5G                            | Number   | 否   |
| onProgress | 进度回调函数，回调是一个对象，包含进度信息                   | Function | 否   |

#### 回调函数说明

```
function(err, data) { ... }
```

#### 回调参数说明

| 参数名   | 参数描述                                                     | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| err      | 请求发生错误时返回的对象，包括网络错误和业务错误，处理措施请参考 [错误码文档](https://cloud.tencent.com/document/product/436/7730)。请求成功则为空 | Object |
| data     | 请求成功时返回的对象，请求错误则为空                         | Object |
| Location | 创建的 Object 的外网访问域名                                 | String |
| Bucket   | 分块上传的目标 Bucket                                        | String |
| Key      | 对象键（Object 的名称），对象在存储桶中的唯一标识，了解更多请阅读 [对象键说明](https://cloud.tencent.com/document/product/436/13324) | String |
| ETag     | 合并后文件的 MD5 算法校验值                                  | String |
