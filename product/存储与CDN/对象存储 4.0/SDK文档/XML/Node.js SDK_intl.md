## 开发准备

### 相关资源

COS服务的Node.js SDK v5版本的GitHub下载地址： [https://github.com/tencentyun/cos-nodejs-sdk-v5.git](https://github.com/tencentyun/cos-nodejs-sdk-v5.git) 
（本版本SDK基于XML API封装组成）

大部分接口的使用 demo 在这里： [demo](https://github.com/tencentyun/cos-nodejs-sdk-v5/blob/master/demo/demo.js)

### npm 引入

```shell
npm i cos-nodejs-sdk-v5 --save
```


### 开发环境

1. 使用SDK需要您的运行环境包含nodejs 以及npm , nodejs版本建议7.0版本以上
2. 安装好 npm 之后记得在sdk的解压目录npm install 一次（安装依赖包）；
3. 去您的控制台获取 AppId, SecretId, SecretKey, 地址在 https://console.cloud.tencent.com/capi


### SDK配置

```js
var COS = require('cos-nodejs-sdk-v5');
var cos = new COS({
    AppId: '1250000000',
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
});
```


## Service操作

### Get Service

#### 功能说明

Get Service接口实现获取该用户下所有Bucket列表。该API接口需要使用Authorization签名认证，且只能获取签名中AccessID所属账户的Bucket列表。

#### 操作方法原型

* 调用 Get Service 操作

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

* **无特殊参数** 

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。 
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * Owner —— (Object) ：	说明Bucket所有者的信息
      * uin —— (String) ：	Bucket所有者的UIN
      * Buckets —— (Array) ：说明本次返回的Bucket列表的所有信息
      * Name —— (String) ：Bucket名称
      * CreateDate —— (String) ：Bucket创建时间，ISO8601格式



## Bucket操作


### Head Bucket

#### 功能说明

Head Bucket请求可以确认是否存在该Bucket，是否有权限访问，Head的权限与Read一致。

#### 操作方法原型

* 调用 Head Bucket 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称			
    * Region —— (String) ： 地域名称		

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * BucketExist —— (Boolean)  ：  Bucket 是否存在
  * BucketAuth —— (Boolean)  ： 是否拥有该 Bucket 的权限


###  Get Bucket

#### 功能说明 

Get Bucket请求等同于 List Object请求，可以列出该Bucekt下部分或者所有Object，发起该请求需要拥有Read权限。

#### 操作方法原型

* 调用 Get Bucket 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称	
    * Prefix —— (String) : 前缀匹配，用来规定返回的文件前缀地址 
      * Delimiter —— (String) ：定界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始
      * Marker —— (String) ：默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始 
      * MaxKeys —— (String) ：单次返回最大的条目数量，默认1000
      * EncodingType —— (String) ：规定返回值的编码方式 

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * CommonPrefixes —— (Array)  ：  将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix
    * Prefix —— (String) ：前缀名称
  * Name —— (String)   ：  Bucket名字
  * Prefix —— (String)  ： 前缀匹配，用来规定返回的文件前缀地址
  * Marker —— (String)  ： 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始
  * MaxKeys —— (String)  ： 单次返回最大的条目数量
  * IsTruncated —— (String)  ： 返回条目是否被截断，'true' 或者 'false'
  * NextMarker —— (String)   ： 假如返回条目被截断，则返回NextMarker就是下一个条目的起点
  * Encoding-Type —— (String)  ： 编码类型，作用于Delimiter，Marker，Prefix，NextMarker，Key
  * Contents —— (Array)  ： 元数据信息
    * ETag —— (String)  ： 文件的 SHA-1 算法校验值
    * Size —— (String)  ： 文件大小，单位Byte
    * Key —— (String)  ： Object名称
    * LastModified —— (String)  ： Object最后修改时间
    * Owner —— (Object)  ： Bucket所有者信息
      * ID —— (String)  ： Bucket 拥有者的 UID 信息



###  Put Bucket

#### 功能说明

Put Bucket请求可以在指定账号下创建一个Bucket。

#### 操作方法原型

* 调用 Put Bucket 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称	
  * ACL —— (String)  ： 允许用户自定义文件权限。有效值：private，public-read默认值：private。
  * GrantRead —— (String)  ： 赋予被授权者读的权限，格式 x-cos-grant-read: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。
    * GrantWrite —— (String)  ： 赋予被授权者写的权限，格式 x-cos-grant-write: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。
      * GrantFullControl —— (String)  ： 赋予被授权者读写权限，格式 x-cos-grant-full-control: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Location —— (String)  ：  创建成功后，Bucket 的操作地址



###  Delete Bucket

#### 功能说明

Delete Bucket 请求可以在指定账号下删除 Bucket，删除之前要求 Bucket为空。

#### 操作方法原型

* 调用 Delete Bucket 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * DeleteBucketSuccess —— (Boolean)  ：  删除是否成功


###  Get Bucket ACL

#### 功能说明

使用API读取 Bucket 的 ACL 表，只有所有者有权操作。

#### 操作方法原型

* 调用 Get Bucket ACL 操作

```js

var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
};

cos.getBucketACL(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Owner —— (Object)  ：  标识资源的所有者
    * uin —— (String)  ：  用户QQ号
  * AccessControlList —— (Object)  ：  被授权者信息与权限信息
    * Grant —— (Array)  ：  具体的授权信息
      * Permission —— (String)  ：  权限信息，枚举值：READ，WRITE，FULL_CONTROL
      * Grantee —— (Object)  ：  被授权者资源信息
        * uin —— (String)  ：  被授权者的 QQ 号码或者 'anonymous' 
        * Subacount —— (String)  ： 子账户 QQ 账号 





### Put Bucket ACL

#### 功能说明

使用API写入Bucket的ACL表，Put Bucket ACL 是一个覆盖操作，传入新的ACL将覆盖原有ACL。只有所有者有权操作。

#### 操作方法原型

* 调用 Put Bucket ACL 操作

```js

var params = {
	Bucket : 'STRING_VALUE',			/* 必须 */
	Region : 'STRING_VALUE',			/* 必须 */
	ACL : 'STRING_VALUE',				/* 非必须 */
	GrantRead : 'STRING_VALUE', 		/* 非必须 */
	GrantWrite : 'STRING_VALUE',		/* 非必须 */
	GrantFullControl : 'STRING_VALUE'	/* 非必须 */
};

cos.putBucketACL(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * ACL —— (String)  ： 允许用户自定义文件权限。有效值：private，public-read默认值：private。
  * GrantRead —— (String)  ： 赋予被授权者读的权限，格式 x-cos-grant-read: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。
    * GrantWrite —— (String)  ： 赋予被授权者写的权限，格式 x-cos-grant-write: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。
    * GrantFullControl —— (String)  ： 赋予被授权者读写权限，格式 x-cos-grant-full-control: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * BucketGrantSuccess —— (Boolean)  ：  授权是否成功




###  Get Bucket CORS

#### 功能说明

Get Bucket CORS 实现跨域访问读取。

#### 操作方法原型

* 调用 Get Bucket CORS 操作

```js

var params = {
	Bucket : 'STRING_VALUE',	/* 必须 */
	Region : 'STRING_VALUE'		/* 必须 */
};

cos.getBucketCORS(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * CORSRule —— (Array)  ：  配置的信息集合
    * AllowedMethod —— (Array)  ：  允许的HTTP操作，枚举值：Get，Put，Head，Post，Delete。
    * AllowedOrigin —— (Array)  ：  允许的访问来源，支持『*』通配符。
    * AllowedHeader —— (Array)  ：  在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部。
    * ExposeHeader —— (Array)  ：  设置浏览器可以接收到的来自服务器端的自定义头部信息。
    * MaxAgeSeconds —— (String)  ：  设置 OPTIONS 请求得到结果的有效期。
    * ID —— (String)  ：  规则名称。


### Put Bucket CORS

#### 功能说明

Put Bucket CORS 实现跨域访问读写。

#### 操作方法原型

* 调用 Put Bucket CORS 操作

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

cos.putBucketCORS(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称
  * CORSRules —— (Array) ： 跨域规则集合
    * ID —— (String) ： 规则名称
    * AllowedMethods —— (Array) ： 允许的HTTP操作，枚举值：Get，Put，Head，Post，Delete
    * AllowedOrigins —— (Array) ： 允许的访问来源，支持『*』通配符，协议，端口和域名必须一致
    * AllowedHeaders —— (Array) ： 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持『*』通配符
    * ExposeHeaders —— (Array) ：  设置浏览器可以接收到的来自服务器端的自定义头部信息
    * MaxAgeSeconds —— (String) ： 设置 OPTIONS 请求得到结果的有效期

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * PutBucketCorsSucesss —— (Boolean)  ：  设置Bucket CORS 是否成功


###  Delete Bucket CORS

#### 功能说明

Delete Bucket CORS 实现跨域访问读取。

#### 操作方法原型

* 调用 Delete Bucket CORS 操作

```js

var params = {
	Bucket : 'STRING_VALUE',		/* 必须 */
	Region : 'STRING_VALUE'			/* 必须 */
};

cos.deleteBucketCORS(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * DeleteBucketCorsSuccess —— (Boolean)  ：  删除 Bucket CORS 是否成功



### Get Bucket Location

#### 功能说明

Get Bucket Location接口获取Bucket所在地域信息，只有Bucket所有者有权限读取信息。

#### 操作方法原型

* 调用 Get Bucket Location 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * LocationConstraint —— (String)  ：  Bucket所在区域，枚举值：china-east，china-south，china-north，china-west，singapore




### Get Bucket Tagging

#### 功能说明

Get Bucket Tagging接口实现获取指定Bucket的标签。

#### 操作方法原型

* 调用 Get Bucket Tagging 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * Tags —— (Array)：	Bucket 的标签集合
      * Key —— (String)：	Tag的类别名称
        * Value —— (String)：Tag的值


###  Put Bucket Tagging

#### 功能说明

Put Bucket Tagging接口实现给用指定Bucket打标签。

#### 操作参数说明

* 调用 Put Bucket Tagging 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称
  * Tags —— (Array) ： 设置的 Tag 集合
    * Key —— (String) ： Tag的类别名称	
    * Value —— (String) ： Tag的值


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * PutBucketTaggingSuccess —— (Boolean)：	设置 Tag 是否成功




### Delete Bucket Tagging

#### 功能说明

Delete Bucket Tagging接口实现删除指定Bucket的标签

#### 操作方法原型

* 调用 Delete Bucket Tagging 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
    * Region —— (String) ： 地域名称

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * DeleteBucketTaggingSuccess —— (Boolean)：	删除 Bukcet 标签是否成功








## Object操作
### Head Object

#### 功能说明

Head Object 请求可以取回对应 Object 的元数据，Head的权限与 Get 的权限一致

#### 操作方法原型

* 调用 Head Object 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * IfModifiedSince —— (String) ： 当Object在指定时间后被修改，则返回对应Object元信息

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * x-cos-object-type —— (String) ：	用来表示object是否可以被追加上传，枚举值：normal或者appendable
      * x-cos-storage-class —— (String) ：Object的存储级别，枚举值：Standard，Standard_IA，Nearline
      * x-cos-meta-* —— (String) ：用户自定义的元数据
      * NotModified —— (Boolean) ：如果请求时带有 IfModifiedSince ，且文件未被修改，则为 true



### Get Object

#### 功能说明

Get Object 请求可以将一个文件（Object）下载至本地。该操作需要对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

#### 操作方法原型

* 调用 Get Object 操作

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
	Output : 'STRING_VALUE' || 'WRITE_STRING'		/* 必须 */
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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * ResponseContentType —— (String) ： 设置返回头部中的 Content-Type 参数
  * ResponseContentLanguage —— (String) ： 设置返回头部中的 Content-Language 参数
  * ResponseExpires —— (String) ： 设置返回头部中的 Content-Expires 参数
  * ResponseCacheControl —— (String) ： 设置返回头部中的 Cache-Control 参数
  * ResponseContentDisposition —— (String) ： 设置返回头部中的 Content-Disposition 参数
  * ResponseContentEncoding —— (String) ： 设置返回头部中的 Content-Encoding 参数
  * Range —— (String) ： RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位
  * IfModifiedSince —— (String) ： 如果文件修改时间晚于指定时间，才返回文件内容
  * Output —— (String || WriteStream) ： 需要输出的文件路径或者一个写流


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * x-cos-object-type —— (String) ：	用来表示object是否可以被追加上传，枚举值：normal或者appendable
      * x-cos-storage-class —— (String) ：Object的存储级别，枚举值：Standard，Standard_IA，Nearline
      * x-cos-meta-* —— (String) ：用户自定义的元数据
      * NotModified —— (Boolean) ：如果请求时带有 IfModifiedSince ，且文件未被修改，则为 true


### Put Object

#### 功能说明

Put Object请求可以将一个文件（Oject）上传至指定Bucket。

**注意，Key(文件名) 不能以 `/` 结尾，否则会被识别为文件夹 **

#### 操作方法原型

* 调用 Put Object 操作

```js
var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE',							/* 必须 */
	CacheControl : 'STRING_VALUE',					/* 非必须 */
	ContentDisposition : 'STRING_VALUE',			/* 非必须 */
	ContentEncoding : 'STRING_VALUE',				/* 非必须 */
	ContentLength : 'STRING_VALUE',					/* 必须 */
	ContentType : 'STRING_VALUE',					/* 非必须 */
	Expect : 'STRING_VALUE',						/* 非必须 */
	Expires : 'STRING_VALUE',						/* 非必须 */
	ContentSha1 : 'STRING_VALUE',					/* 非必须 */
	ACL : 'STRING_VALUE',							/* 非必须 */
	GrantRead : 'STRING_VALUE',						/* 非必须 */
	GrantWrite : 'STRING_VALUE',					/* 非必须 */
	GrantFullControl : 'STRING_VALUE',				/* 非必须 */
	'x-cos-meta-*' : 'STRING_VALUE',				/* 非必须 */
	Body: fs.createReadStream('./a.zip'),           /* 必须 */
    onProgress: function (progressData) {
        console.log(progressData);
    },
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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * CacheControl —— (String) ： RFC 2616 中定义的缓存策略，将作为 Object 元数据保存
  * ContentDisposition —— (String) ： RFC 2616 中定义的文件名称，将作为 Object 元数据保存
  * ContentEncoding —— (String) ： RFC 2616 中定义的编码格式，将作为 Object 元数据保存
  * ContentLength —— (String) ： RFC 2616 中定义的 HTTP 请求内容长度（字节）
  * ContentType —— (String) ： RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存
  * Expect —— (String) ： 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容
  * Expires —— (String) ： RFC 2616 中定义的过期时间，将作为 Object 元数据保存
  * ContentSha1 —— (String) ： RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值
  * ACL —— (String) ： 允许用户自定义文件权限，有效值：private，public-read
  * GrantRead —— (String) ： 赋予被授权者读的权限，格式x-cos-grant-read: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"
  * GrantWrite —— (String) ： 赋予被授权者写的权限，格式x-cos-grant-write: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"
  * GrantFullControl —— (String) ： 赋予被授权者读写权限，格式x-cos-grant-full-control: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"
  * x-cos-meta-* —— (String) ： 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K。
  * Body —— (String | Stream)  ： 传入文件路径或文件流
  * onProgress —— (Function)  ： 进度回调函数，回调是一个对象，包含进度信息



#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * ETag —— (String) ：	返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化。



###  Delete Object

#### 功能说明

Delete Object请求可以将一个文件（Object）删除。

#### 操作方法原型

* 调用 Delete Object 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * DeleteObjectSuccess —— (Boolean) ：	删除文件是否成功
      * BucketNotFound —— (Boolean) ：如果找不到指定的 Bucket，则为 true






###  Options Object

#### 功能说明

Options Object请求实现跨域访问的预请求。即发出一个 OPTIONS 请求给服务器以确认是否可以进行跨域操作。

#### 操作方法原型

* 调用 Options Object 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * Origin —— (String) ： 模拟跨域访问的请求来源域名
    * AccessControlRequestMethod —— (String) ： 模拟跨域访问的请求HTTP方法
  * AccessControlRequestHeaders —— (String) ： 模拟跨域访问的请求头部

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * AccessControlAllowOrigin —— (String) ：	模拟跨域访问的请求来源域名，当来源不允许的时候，此Header不返回。
      * AccessControlAllowMethods —— (String) ：模拟跨域访问的请求HTTP方法，当请求方法不允许的时候，此Header不返回。
      * AccessControlAllowHeaders —— (String) ：模拟跨域访问的请求头部，当模拟任何请求头部不允许的时候，此Header不返回该请求头部。
      * AccessControlExposeHeaders —— (String) ：跨域支持返回头部，用逗号区分。
      * AccessControlMaxAge —— (String) ：设置 OPTIONS 请求得到结果的有效期。





### Get Object ACL

#### 功能说明

Get Object ACL接口实现使用API读取Object的ACL表，只有所有者有权操作。

#### 操作方法原型

* 调用 Get Object ACL 操作

```js

var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE'							/* 必须 */
};

cos.getObjectACL(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Owner —— (Object)  ：  标识资源的所有者
    * uin —— (String)  ：  用户QQ号
  * AccessControlList —— (Object)  ：  被授权者信息与权限信息
    * Grant —— (Array)  ：  具体的授权信息
      * Permission —— (String)  ：  权限信息，枚举值：READ，WRITE，FULL_CONTROL
      * Grantee —— (Object)  ：  被授权者资源信息
        * uin —— (String)  ：  被授权者的 QQ 号码或者 'anonymous' 
        * Subacount —— (String)  ： 子账户 QQ 账号 


### Put Object ACL

#### 功能说明

Put Object ACL使用 API 写入 Object 的 ACL 表

#### 操作方法原型

* 调用 Put Object ACL 操作

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

cos.putObjectACL(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### 操作参数说明

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * ACL —— (String)  ： 允许用户自定义文件权限。有效值：private，public-read默认值：private。
  * GrantRead —— (String)  ： 赋予被授权者读的权限，格式 x-cos-grant-read: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。
    * GrantWrite —— (String)  ： 赋予被授权者写的权限，格式 x-cos-grant-write: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。
  * GrantFullControl —— (String)  ： 赋予被授权者读写权限，格式 x-cos-grant-full-control: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"。


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * PutObjectACLSuccess —— (Boolean)  ：  设置文件的访问权限是否成功，如果成功为 true, 否则为 false。



### Delete Multiple Object

#### 功能说明

Delete Multiple Object请求实现批量删除文件，最大支持单次删除1000个文件。对于返回结果，COS提供Verbose和Quiet两种结果模式。Verbose模式将返回每个Object的删除结果；Quiet模式只返回报错的Object信息。


#### 操作方法原型

* 调用 Delete Multiple Object 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Quiet —— (Boolean)  ： 布尔值，这个值决定了是否启动Quiet模式，True启动Quiet模式，False启动Verbose模式，默认False
    父节点：Delete
  * Objects —— (Array) ： 要删除的文件列表
    * Key —— (String) ： 要删除的文件名


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Deleted —— (Array)  ： 说明本次删除的成功Object信息
    * Key —— (String)  ： Object的名称
  * Error —— (Array)  ： 说明本次删除的失败Object信息
    * Key —— (String)  ： Object的名称
    * Code —— (String)  ： 删除失败的错误码
    * Message —— (String)  ： 删除错误信息



## 分块上传操作
### Initiate Multipart Upload

#### 功能说明

Initiate Multipart Upload请求实现初始化分片上传，成功执行此请求以后会返回Upload ID用于后续的Upload Part请求

#### 操作方法原型

* 调用 Initiate Multipart Upload 操作

```js

var params = {
	Bucket : 'STRING_VALUE',						/* 必须 */
	Region : 'STRING_VALUE',						/* 必须 */
	Key : 'STRING_VALUE',							/* 必须 */
	CacheControl : 'STRING_VALUE',					/* 非必须 */
	ContentDisposition : 'STRING_VALUE',			/* 非必须 */
	ContentEncoding : 'STRING_VALUE',				/* 非必须 */
	ContentType : 'STRING_VALUE',					/* 非必须 */
	Expires : 'STRING_VALUE',						/* 非必须 */
	ACL : 'STRING_VALUE',							/* 非必须 */
	GrantRead : 'STRING_VALUE',						/* 非必须 */
	GrantWrite : 'STRING_VALUE',					/* 非必须 */
	GrantFullControl : 'STRING_VALUE',				/* 非必须 */
	StorageClass : 'STRING_VALUE',					/* 非必须 */
	'x-cos-meta-*' : 'STRING_VALUE'					/* 非必须 */
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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * CacheControl —— (String) ： RFC 2616 中定义的缓存策略，将作为 Object 元数据保存
  * ContentDisposition —— (String) ： RFC 2616 中定义的文件名称，将作为 Object 元数据保存
  * ContentEncoding —— (String) ： RFC 2616 中定义的编码格式，将作为 Object 元数据保存
  * ContentType —— (String) ： RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存
  * Expires —— (String) ： RFC 2616 中定义的过期时间，将作为 Object 元数据保存
  * ACL —— (String) ： 允许用户自定义文件权限，有效值：private，public-read
  * GrantRead —— (String) ： 赋予被授权者读的权限，格式x-cos-grant-read: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"
  * GrantWrite —— (String) ： 赋予被授权者写的权限，格式x-cos-grant-write: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"
  * GrantFullControl —— (String) ： 赋予被授权者读写权限，格式x-cos-grant-full-control: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID"
  * StorageClass —— (String) ： 设置Object的存储级别，枚举值：Standard，Standard_IA，Nearline，默认值：Standard（目前只支持华南园区）
  * x-cos-meta-* —— (String) ： 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K。


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Bucket —— (String)  ：  分片上传的目标Bucket
    * Key —— (String)  ： 	Object的名称	
  * UploadId —— (String)  ：  在后续上传中使用的ID




### Upload Part

#### 功能说明

Upload Part请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1 MB 到5 GB。在每次请求Upload Part时候，需要携带partNumber和uploadID，partNumber为块的编号，支持乱序上传。


#### 操作方法原型

* 调用 Upload Part 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * ContentLength —— (String) ： RFC 2616 中定义的 HTTP 请求内容长度（字节）
  * Expect —— (String) ： 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容。
  * ContentSha1 —— (String) ： RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值
  * PartNumber —— (String) ： 分块的编号
  * UploadId —— (String) ： 上传任务编号


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * ETag —— (String)  ：  分块的 ETag 值，为 sha1 校验值



### Complete Multipart Upload

#### 功能说明

Complete Multipart Upload用来实现完成整个分块上传。当您已经使用Upload Parts上传所有块以后，你可以用该API完成上传。在使用该API时，您必须在Body中给出每一个块的PartNumber和ETag，用来校验块的准确性。

#### 操作方法原型

* 调用 Complete Multipart Upload 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * UploadId —— (String) ： 上传任务编号
  * Parts —— (Array) ： 分块的ETag 信息
    * PartNumber —— (String) ： 分块的编号
    * ETag —— (String) ： 分块的ETag 值，为 sha1 校验值，需要在校验值前后加上双引号，如 "3a0f1fd698c235af9cf098cb74aa25bc"

#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Location —— (String)  ：  创建的Object的外网访问域名
  * Bucket —— (String)  ：  分块上传的目标Bucket
    * Key —— (String)  ：  Object的名称
    * ETag —— (String)  ：  合并后文件的 MD5算法校验值



### List Parts

#### 功能说明

List Parts用来查询特定分块上传中的已上传的块

#### 操作方法原型

* 调用 List Parts 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * UploadId —— (String) ： 上传任务编号
  * EncodingType —— (String) ： 规定返回值的编码方式
  * MaxParts —— (String) ： 单次返回最大的条目数量，默认1000
    * PartNumberMarker —— (String) ： 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Bucket —— (String)  ：  分块上传的目标Bucket
  * Encoding-type —— (String)  ：  规定返回值的编码方式
  * Key —— (String)  ：  Object的名称
  * UploadID —— (String)  ：  标示本次分块上传的ID
  * Initiator —— (Object)  ：  用来表示本次上传发起者的信息，子节点包括UID
    * UID —— (String)  ：  开发商APPID
  * Owner —— (Object)  ：  用来表示这些分块所有者的信息，子节点包括UID
    * UID —— (String)  ：  拥有者 qq
  * StorageClass —— (String)  ：  用来表示这些分块的存储级别，枚举值：Standard，Standard_IA，Nearline
  * PartNumberMarker —— (String)  ：  默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始
  * NextPartNumberMarker —— (String)  ：  假如返回条目被截断，则返回NextMarker就是下一个条目的起点
  * MaxParts —— (String)  ：  单次返回最大的条目数量
  * IsTruncated —— (String)  ：  返回条目是否被截断，'true' 或者 'false'
  * Part —— (Array)  ： 分块信息集合
    * PartNumber —— (String)  ： 分块编号
    * LastModified —— (String)  ： 块最后修改时间 
    * Etag —— (String)  ： 块的 SHA-1 算法校验值
      * Size —— (String)  ： 块大小，单位Byte	


### Abort Multipart Upload

#### 功能说明

Abort Multipart Upload用来实现舍弃一个分块上传并删除已上传的块。当您调用Abort Multipart Upload时，如果有正在使用这个Upload Parts上传块的请求，则Upload Parts会返回失败。

#### 操作方法原型

* 调用 Abort Multipart Upload 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Key —— (String) ： 文件名称
  * UploadId —— (String) ： 上传任务编号


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * MultipartAbortSuccess —— (Boolean)  ： Multipart Abort 是否成功


### List Multipart Uploads

#### 功能说明

List Multiparts Uploads用来查询正在进行中的分块上传。单次最多列出1000个正在进行中的分块上传。

#### 操作方法原型

* 调用 List Multipart Uploads 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称		
  * Region —— (String) ： 地域名称
  * Delimiter —— (String) ： 界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始
  * EncodingType —— (String) ： 规定返回值的编码方式
  * Prefix —— (String) ： 前缀匹配，用来规定返回的文件前缀地址
  * MaxUploads —— (String) ： 单次返回最大的条目数量，默认1000
  * KeyMarker —— (String) ： 与upload-id-marker一起使用
    当upload-id-marker未被指定时，ObjectName字母顺序大于key-marker的条目将被列出
    当upload-id-marker被指定时，ObjectName字母顺序大于key-marker的条目被列出，ObjectName字母顺序等于key-marker同时UploadID大于upload-id-marker的条目将被列出。
  * UploadIdMarker —— (String) ： 与key-marker一起使用
    当key-marker未被指定时，upload-id-marker将被忽略
    当key-marker被指定时，ObjectName字母顺序大于key-marker的条目被列出，ObjectName字母顺序等于key-marker同时UploadID大于upload-id-marker的条目将被列出。


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
  * Bucket —— (String)  ：  分块上传的目标Bucket
  * Encoding-type —— (String)  ：  规定返回值的编码方式
  * KeyMarker —— (String)  ：  列出条目从该key值开始
  * UploadIdMarker —— (String)  ：  列出条目从该UploadId值开始
  * NextKeyMarker —— (String)  ：  假如返回条目被截断，则返回NextKeyMarker就是下一个条目的起点
  * NextUploadIdMarker —— (String)  ：  假如返回条目被截断，则返回UploadId就是下一个条目的起点
  * IsTruncated —— (String)  ：  返回条目是否被截断，'true' 或者 'false'
  * delimiter —— (String)  ：  定界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始
  * CommonPrefixs —— (Array)  ：  将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix
    * Prefix —— (String)  ：  具体的 Prefix 值
  * Upload —— (Array)  ：  Upload的信息集合
    * Key —— (String)  ：  Object的名称
    * UploadID —— (String)  ： 标示本次分块上传的ID
    * StorageClass —— (String)  ：  用来表示分块的存储级别，枚举值：Standard，Standard_IA，Nearline 
    * Initiator —— (Object)  ：  用来表示本次上传发起者的信息，子节点包括UID
      * UID —— (String)  ：  开发商APPID
    * Owner —— (Object)  ：  用来表示这些分块所有者的信息，子节点包括UID
      * UID —— (String)  ：  拥有者 qq
    * Initiated —— (String)  ：  分块上传的起始时间




###  Slice Upload File

#### 功能说明

Slice Upload File 可用于实现文件的分块上传。

#### 操作方法原型

* 调用 Slice Upload File 操作

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

* **params** (Object) ： 参数列表
  * Bucket —— (String) ： Bucket 名称			
  * Region —— (String) ： 地域名称
  * Key —— (String) ： Object名称
  * FilePath —— (String) ： 本地文件路径
  * SliceSize —— (String) ： 分块大小
  * AsyncLimit —— (String) ： 分块的并发量
  * onHashProgress —— (Function)  ： 计算文件 sha1 值的进度回调函数，回调是一个对象，包含进度信息
  * onProgress —— (Function)  ： 进度回调函数，回调是一个对象，包含进度信息


#### 回调函数说明

```js
function(err, data) { ... }
```
#### 回调参数说明

* **err** —— (Object) 	：	请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空。 
  * **data** —— (Object)：	请求成功时返回的对象，如果请求发生错误，则为空。
    * Location —— (String) ：	创建的Object的外网访问域名
      * Bucket —— (String) ：分块上传的目标Bucket
      * Key —— (String) ：Object的名称
        * ETag —— (String) ：合并后文件的 SHA-1 算法校验值


#### 进度回调参数

* **progressData** (Object) ： 进度参数列表
  * SliceSize —— (String) ： 分块大小
  * PartNumber —— (Number) ： 上传成功的分块编号
  * FileSize —— (Number) ： 文件总大小
