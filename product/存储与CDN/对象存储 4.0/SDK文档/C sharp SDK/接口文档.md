对象存储服务 XML C# SDK 操作成功会返回各个 API 对应的类型，失败会抛 CosClientException
 和 CosServerException。其中 CosClientException 是指客户端异常，如参数为空，网络连接失败等； CosServerException 是指服务端处理一些不符合要求的客户端请求所返回的错误，如访问不存在的文件，没有访问文件的权限等。详细请查看 [SDK 异常说明](#COS_EXCEPTION)。

SDK 中为各个 API 请求提供了同步和异步两种请求方法。

## Service API 描述

### 获取存储桶列表

#### 功能说明

用来获取指定账号下所有存储桶列表（Bucket list）.

#### 方法原型
```C#
GetServiceResult GetService(GetServiceRequest request);

void GetService(GetServiceRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	GetServiceRequest request = new GetServiceRequest();
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	GetServiceResult result = cosXml.GetService(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{	
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
GetServiceRequest request = new GetServiceRequest();
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
cosXml.GetService(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		GetServiceResult result = cosResult as GetServiceResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetServiceResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|listAllMyBuckets|[ListAllMyBuckets](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/ListAllMyBuckets.cs)|返回指定账号下的存储桶列表的信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

## Bucket API 描述

### 创建存储桶

#### 功能说明

创建一个存储桶 (Put Bucket).

#### 方法原型
```C#
PutBucketResult PutBucket(PutBucketRequest request);

void PutBucket(PutBucketRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	PutBucketRequest request = new PutBucketRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	PutBucketResult result = cosXml.PutBucket(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
PutBucketRequest request = new PutBucketRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
cosXml.PutBucket(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		PutBucketResult result = cosResult as PutBucketResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 PutBucketResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 删除存储桶

#### 功能说明

删除指定的存储桶 (Delete Bucket).

#### 方法原型
```C#
DeleteBucketResult DeleteBucket(DeleteBucketRequest request);

void DeleteBucket(DeleteBucketRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	DeleteBucketRequest request = new DeleteBucketRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	DeleteBucketResult result = cosXml.DeleteBucket(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
DeleteBucketRequest request = new DeleteBucketRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
cosXml.DeleteBucket(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		DeleteBucketResult result = cosResult as DeleteBucketResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 DeleteBucketResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 检索存储桶

#### 功能说明

检索指定存储桶是否存在 (Head Bucket).

#### 方法原型
```C#
HeadBucketResult HeadBucket(HeadBucketRequest request);

void HeadBucket(HeadBucketRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	HeadBucketRequest request = new HeadBucketRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	HeadBucketResult result = cosXml.HeadBucket(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
HeadBucketRequest request = new HeadBucketRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
cosXml.HeadBucket(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		HeadBucketResult result = cosResult as HeadBucketResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 HeadBucketResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 获取对象列表

#### 功能说明

获取指定存储桶中所有的对象 (Object List).

#### 方法原型
```C#
GetBucketResult GetBucket(GetBucketRequest request);

void GetBucket(GetBucketRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	GetBucketRequest request = new GetBucketRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	GetBucketResult result = cosXml.GetBucket(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
GetBucketRequest request = new GetBucketRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
cosXml.GetBucket(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		GetBucketResult result = cosResult as GetBucketResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetBucketResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|listBucket|[ListBucket](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/ListBucket.cs)|返回 Bucket 对象列表信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 获取存储桶地域

#### 功能说明

获取指定存储桶所在的地域信息 (Get Bucket Location).

#### 方法原型
```C#
GetBucketLocationResult GetBucketLocation(GetBucketLocationRequest request);

void GetBucketLocation(GetBucketLocationRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	GetBucketLocationRequest request = new GetBucketLocationRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	GetBucketLocationResult result = cosXml.GetBucketLocation(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
GetBucketLocationRequest request = new GetBucketLocationRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
cosXml.GetBucketLocation(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		GetBucketLocationResult result = cosResult as GetBucketLocationResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetBucketLocationResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|locationConstraint|[LocationConstraint](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/LocationConstraint.cs)|返回 Bucket 地域信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常


### 设置存储桶 ACL

#### 功能说明

设置指定存储桶访问权限控制列表 (ACL)  (Put Bucket ACL).

#### 方法原型
```C#
PutBucketACLResult PutBucketACL(PutBucketACLRequest request);

void PutBucketACL(PutBucketACLRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	PutBucketACLRequest request = new PutBucketACLRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置私有读写权限
	request.SetCosACL(CosACL.PRIVATE);
	//授予1131975903账号读权限
	COSXML.Model.Tag.GrantAccount readAccount = new COSXML.Model.Tag.GrantAccount();
	readAccount.AddGrantAccount("1131975903", "1131975903");
	request.setXCosGrantRead(readAccount);
	//执行请求
	PutBucketACLResult result = cosXml.PutBucketACL(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
PutBucketACLRequest request = new PutBucketACLRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置私有读写权限
request.SetCosACL(CosACL.PRIVATE);
//授予1131975903账号读权限
COSXML.Model.Tag.GrantAccount readAccount = new COSXML.Model.Tag.GrantAccount();
readAccount.AddGrantAccount("1131975903", "1131975903");
request.setXCosGrantRead(readAccount);
//执行请求
cosXml.PutBucketACL(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		PutBucketACLResult result = cosResult as PutBucketACLResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|cosAcl|SetCosAcl|设置存储桶的acl权限|string|
|grandtAccout|SetXCosGrantRead 或 SetXCosGrantWrite 或 SetXCosReadWrite|授予用户读写权限|GrantAccount|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 PutBucketACLResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 获取存储桶 ACL

#### 功能说明

获取指定存储桶的访问权限控制列表 (ACL) (Get Bucket ACL).

#### 方法原型
```C#
GetBucketACLResult GetBucketACL(GetBucketACLRequest request);

void GetBucketACL(GetBucketACLRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	GetBucketACLRequest request = new GetBucketACLRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	GetBucketACLResult result = cosXml.GetBucketACL(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
GetBucketACLRequest request = new GetBucketACLRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
cosXml.GetBucketACL(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		GetBucketACLResult result = cosResult as GetBucketACLResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetBucketACLResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|accessControlPolicy|[AccessControlPolicy](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/AccessControlPolicy.cs)|返回 Bucket 访问权限列表信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 设置存储桶的跨域访问配置

#### 功能说明

设置指定存储桶的跨域访问配置信息 (CORS) (Put Bucket CORS).

#### 方法原型
```C#
PutBucketCORSResult PutBucketCORS(PutBucketCORSRequest request);

void PutBucketCORS(PutBucketCORSRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	PutBucketCORSRequest request = new PutBucketCORSRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置跨域访问配置CORS
	COSXML.Model.Tag.CORSConfiguration.CORSRule corsRule = new COSXML.Model.Tag.CORSConfiguration.CORSRule();
	corsRule.id = "corsconfigureId";
	corsRule.maxAgeSeconds = 6000;
	corsRule.allowedOrigin = "http://cloud.tencent.com";

	corsRule.allowedMethods = new List<string>();
	corsRule.allowedMethods.Add("PUT");

	corsRule.allowedHeaders = new List<string>();
	corsRule.allowedHeaders.Add("Host");

	corsRule.exposeHeaders = new List<string>();
	corsRule.exposeHeaders.Add("x-cos-meta-x1");

	request.SetCORSRule(corsRule);

	//执行请求
	PutBucketCORSResult result = cosXml.PutBucketCORS(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
 	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
PutBucketCORSRequest request = new PutBucketCORSRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);

//设置跨域访问配置CORS
COSXML.Model.Tag.CORSConfiguration.CORSRule corsRule = new COSXML.Model.Tag.CORSConfiguration.CORSRule();
corsRule.id = "corsconfigureId";
corsRule.maxAgeSeconds = 6000;
corsRule.allowedOrigin = "http://cloud.tencent.com";

corsRule.allowedMethods = new List<string>();
corsRule.allowedMethods.Add("PUT");

corsRule.allowedHeaders = new List<string>();
corsRule.allowedHeaders.Add("Host");

corsRule.exposeHeaders = new List<string>();
corsRule.exposeHeaders.Add("x-cos-meta-x1");

request.SetCORSRule(corsRule);

cosXml.PutBucketCORS(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		PutBucketCORSResult result = cosResult as PutBucketCORSResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|corsRule|SetCORSRule|设置存储桶的跨域访问配|CORSConfiguration.CORSRule|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 PutBucketCORSResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 获取存储桶跨域访问配置

#### 功能说明

获取指定存储桶的跨域访问配置信息 (CORS) (Get Bucket CORS).

#### 方法原型
```C#
GetBucketCORSResult GetBucketCORS(GetBucketCORSRequest request);

void GetBucketCORS(GetBucketCORSRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	GetBucketCORSRequest request = new GetBucketCORSRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	GetBucketCORSResult result = cosXml.GetBucketCORS(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
GetBucketCORSRequest request = new GetBucketCORSRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.GetBucketCORS(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		GetBucketCORSResult result = cosResult as GetBucketCORSResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetBucketCORSResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|corsConfiguration|[CORSConfiguration](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/CORSConfiguration.cs)|返回 Bucket 跨域资源共享配置的信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 删除存储桶跨域访问配置

#### 功能说明

删除指定存储桶的跨域访问配置 (CORS) (Delete Bucket CORS).

#### 方法原型
```C#
DeleteBucketCORSResult DeleteBucketCORS(DeleteBucketCORSRequest request);

void DeleteBucketCORS(DeleteBucketCORSRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	DeleteBucketCORSRequest request = new DeleteBucketCORSRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	DeleteBucketCORSResult result = cosXml.DeleteBucketCORS(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
DeleteBucketCORSRequest request = new DeleteBucketCORSRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.DeleteBucketCORS(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		DeleteBucketCORSResult result = cosResult as DeleteBucketCORSResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 DeleteBucketCORSResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常


### 设置存储桶的生命周期

#### 功能说明

设置指定存储桶的生命周期配置信息 (Lifecycle) (Put Bucket LifeCycle).

#### 方法原型
```C#
PutBucketLifecycleResult PutBucketLifecycle(PutBucketLifecycleRequest request);

void PutBucketLifecycle(PutBucketLifecycleRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	PutBucketLifecycleRequest request = new PutBucketLifecycleRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置 lifecycle
	COSXML.Model.Tag.LifecycleConfiguration.Rule rule = new COSXML.Model.Tag.LifecycleConfiguration.Rule();
	rule.id = "lfiecycleConfigureId";
	rule.status = "Enabled"; //Enabled，Disabled

	rule.filter = new COSXML.Model.Tag.LifecycleConfiguration.Filter();
	rule.filter.prefix = "2/";

	//指定分片过期删除操作
	rule.abortIncompleteMultiUpload = new COSXML.Model.Tag.LifecycleConfiguration.AbortIncompleteMultiUpload();
	rule.abortIncompleteMultiUpload.daysAfterInitiation = 2;

	request.SetRule(rule);

	//执行请求
	PutBucketLifecycleResult result = cosXml.PutBucketLifecycle(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
PutBucketLifecycleRequest request = new PutBucketLifecycleRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置 lifecycle
COSXML.Model.Tag.LifecycleConfiguration.Rule rule = new COSXML.Model.Tag.LifecycleConfiguration.Rule();
rule.id = "lfiecycleConfigureId";
rule.status = "Enabled"; //Enabled，Disabled

rule.filter = new COSXML.Model.Tag.LifecycleConfiguration.Filter();
rule.filter.prefix = "2/";

rule.abortIncompleteMultiUpload = new COSXML.Model.Tag.LifecycleConfiguration.AbortIncompleteMultiUpload();
rule.abortIncompleteMultiUpload.daysAfterInitiation = 2;

request.SetRule(rule);

//执行请求
cosXml.PutBucketLifecycle(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		PutBucketLifecycleResult result = cosResult as PutBucketLifecycleResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|rule|SetRule|设置存储桶的生命周期配置|LifecycleConfiguration.Rule|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 PutBucketLifecycleResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 获取存储桶的生命周期

#### 功能说明

获取指定存储桶的的生命周期 (Lifecycle) (Get Bucket Lifecycle).

#### 方法原型
```C#
GetBucketLifecycleResult GetBucketLifecycle(GetBucketLifecycleRequest request);

void GetBucketLifecycle(GetBucketLifecycleRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	GetBucketLifecycleRequest request = new GetBucketLifecycleRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	GetBucketLifecycleResult result = cosXml.GetBucketLifecycle(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
GetBucketLifecycleRequest request = new GetBucketLifecycleRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.GetBucketLifecycle(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		 GetBucketLifecycleResult result = cosResult as GetBucketLifecycleResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetBucketLifecycleResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|lifecycleConfiguration|[LifecycleConfiguration](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/LifecycleConfiguration.cs)|返回 Bucket 的生命周期配置信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 删除存储桶的生命周期

#### 功能说明

删除指定存储桶的的生命周期 (Lifecycle) (Delete Bucket Lifecycle).

#### 方法原型
```C#
DeleteBucketLifecycleResult DeleteBucketLifecycle(DeleteBucketLifecycleRequest request);

void DeleteBucketLifecycle(DeleteBucketLifecycleRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	DeleteBucketLifecycleRequest request = new DeleteBucketLifecycleRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	DeleteBucketLifecycleResult result = cosXml.DeleteBucketLifecycle(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
DeleteBucketLifecycleRequest request = new DeleteBucketLifecycleRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.DeleteBucketLifecycle(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		DeleteBucketLifecycleResult result = cosResult as DeleteBucketLifecycleResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 DeleteBucketLifecycleResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 查询分片上传

#### 功能说明

查询指定存储桶中正在进行的分片上传 (List Multipart Uploads).

#### 方法原型
```C#
ListMultiUploadsResult ListMultiUploads(ListMultiUploadsRequest request);

void ListMultiUploads(ListMultiUploadsRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //格式：bucketname-appid
	ListMultiUploadsRequest request = new ListMultiUploadsRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	ListMultiUploadsResult result = cosXml.ListMultiUploads(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //格式：bucketname-appid
ListMultiUploadsRequest request = new ListMultiUploadsRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.ListMultiUploads(request, 
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		ListMultiUploadsResult result = cosResult as ListMultiUploadsResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 ListMultiUploadsResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|listMultipartUploads|[ListMultipartUploads](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/ListMultipartUploads.cs)|返回 Bucket 中所有正在进行分块上传的信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

## Object API 描述

### 简单上传对象

#### 功能说明

上传对象到指定的存储桶中 (Put Object).

#### 方法原型
```C#
PutObjectResult PutObject(PutObjectRequest request);

void PutObject(PutObjectRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	string srcPath = @"F:\test.txt"；//本地文件路径
	PutObjectRequest request = new PutObjectRequest(bucket, key, srcPath);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
	});
	//执行请求
	PutObjectResult result = cosXml.PutObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string srcPath = @"F:\test.txt";  //本地文件路径
PutObjectRequest request = new PutObjectRequest(bucket, key, srcPath);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置进度回调
request.SetCosProgressCallback(delegate(long completed, long total)
{
	Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
});
//执行请求
cosXml.PutObject(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		PutObjectResult result = cosResult as PutObjectResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|srcPath|构造方法|用于上传到 cos 的本地文件的绝对路径|string|
|data|构造方法|用于上传到 cos 的 byte 数组|byte[]|
|progressCallback|SetCosProgressCallback|设置上传进度回调|Callback.OnProgressCallback|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 PutObjectResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|eTag|string|返回 对象 的 eTag|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 分片上传对象

分片上传对象可包括的操作：

分片上传对象： 初始化分片上传，  上传分片块， 完成所有分片块上传.

分片续传：查询已上传的分片块， 上传分片块，完成所有分片块上传.

删除已上传分片块.

#### <span id = "INIT_MULIT_UPLOAD"> 初始化分片上传 </span>

##### 功能说明

初始化分片上传，获取对应的uploadId. (Initiate Multipart Upload).

##### 方法原型
```C#
InitMultipartUploadResult InitMultipartUpload(InitMultipartUploadRequest request);

void InitMultipartUpload(InitMultipartUploadRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

##### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	InitMultipartUploadRequest request = new InitMultipartUploadRequest(bucket, key);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	InitMultipartUploadResult result = cosXml.InitMultipartUpload(request);
	//请求成功
	string uploadId = result.initMultipartUpload.uploadId; //用于后续分片上传的 uploadId
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
InitMultipartUploadRequest request = new InitMultipartUploadRequest(bucket, key);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.InitMultipartUpload(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		InitMultipartUploadResult result = cosResult as InitMultipartUploadResult;
		string uploadId = result.initMultipartUpload.uploadId; //用于后续分片上传的 uploadId
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

##### 返回结果说明
通过 InitMultipartUploadResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|initMultipartUpload|[InitiateMultipartUpload](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/InitiateMultipartUpload.cs)|返回 对象 初始化分片上传的 uploadId |

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

#### <span id = "LIST_MULIT_UPLOAD"> 查询已上传的分片块 </span>

##### 功能说明

查询指定uploadId 已上传的分片块 (List Parts).

##### 方法原型
```C#
ListPartsResult ListParts(ListPartsRequest request);

void ListParts(ListPartsRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

##### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
	ListPartsRequest request = new ListPartsRequest(bucket, key, uploadId);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	ListPartsResult result = cosXml.ListParts(request);
	//请求成功
	//列举已上传的分片块
	List<COSXML.Model.Tag.ListParts.Part> alreadyUploadParts = result.listParts.parts;
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
ListPartsRequest request = new ListPartsRequest(bucket, key, uploadId);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.ListParts(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		ListPartsResult result = cosResult as ListPartsResult;
		//列举已上传的分片块
		List<COSXML.Model.Tag.ListParts.Part> alreadyUploadParts = result.listParts.parts;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	 {	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|uploadId|构造方法 或 SetUploadId|标识指定分片上传的 uploadId |string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

##### 返回结果说明
通过 ListPartsResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|listParts|[ListParts](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/ListParts.cs)|返回指定 uploadId 分块上传中的已上传的块信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

#### <span id = "MULIT_UPLOAD_PART"> 上传分片块 </span>

上传分片块 (Upload Part).

##### 方法原型
```C#
UploadPartResult UploadPart(UploadPartRequest request);

void UploadPart(UploadPartRequest, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

##### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
	int partNumber = 1; //分片块编号，必须从1开始递增
	string srcPath = @"F:\test.txt"; //本地文件路径
	UploadPartRequest request = new UploadPartRequest(bucket, key, partNumber, uploadId, srcPath);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {0:##.##}%",  completed * 100.0 / total));
	});
	//执行请求
	UploadPartResult result = cosXml.UploadPart(request);
	//请求成功
	//获取返回分片块的eTag,用于后续CompleteMultiUploads
	string eTag = result.eTag;
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
int partNumber = 1; //分片块编号，必须从1开始递增
string srcPath = @"F:\test.txt"; //本地文件路径
UploadPartRequest request = new UploadPartRequest(bucket, key, partNumber, uploadId, srcPath);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置进度回调
request.SetCosProgressCallback(delegate(long completed, long total)
{
	Console.WriteLine(String.Format("progress = {0:##.##}%",  completed * 100.0 / total));
});
//执行请求
cosXml.UploadPart(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		UploadPartResult result = cosResult as UploadPartResult;
		//获取返回分片块的eTag,用于后续CompleteMultiUploads
		string eTag = result.eTag;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|uploadId|构造方法 或 SetUploadId|标识指定分片上传的 uploadId |string|
|partNumber|构造方法 或 SetPartNumber|标识指定分片的编号，必须 >= 1|int|
|srcPath|构造方法|用于上传到 cos 的本地文件的绝对路径|string|
|data|构造方法|用于上传到 cos 的 byte 数组|byte[]|
|progressCallback|SetCosProgressCallback|设置上传进度回调|Callback.OnProgressCallback|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

##### 返回结果说明
通过 UploadPartResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|eTag|string|返回 对象的分片块的 eTag|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

#### <span id = "COMPLETE_MULIT_UPLOAD"> 完成所有分片块上传 </span>

##### 功能说明

实现完成整个分块上传 (Complete Multipart Upload).

##### 方法原型
```C#
CompleteMultiUploadResult CompleteMultiUpload(CompleteMultiUploadRequest request);

void CompleteMultiUpload(CompleteMultiUploadRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

##### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
	CompleteMultiUploadRequest request = new CompleteMultiUploadRequest(bucket, key, uploadId);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置已上传的parts,必须有序，按照partNumber递增
	request.SetPartNumberAndETag(1, "partNumber1 eTag");
	//执行请求
	CompleteMultiUploadResult result = cosXml.CompleteMultiUpload(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
CompleteMultiUploadRequest request = new CompleteMultiUploadRequest(bucket, key, uploadId);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置已上传的parts,必须有序，按照partNumber递增
request.SetPartNumberAndETag(1, "partNumber1 eTag");
//执行请求
cosXml.CompleteMultiUpload(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		CompleteMultiUploadResult result = result as CompleteMultiUploadResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
   {	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|uploadId|构造方法 或 SetUploadId|标识指定分片上传的 uploadId |string|
|partNumber|SetPartNumberAndETag|标识指定分片块的编号，必须 >= 1|int|
|eTag|SetPartNumberAndETag|标识指定分片块的上传返回的 eTag |string|
|partNumberAndETags|SetPartNumberAndETag|标识分片块的编号和上传返回的 eTag |`Dictionary<int, string> `|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

##### 返回结果说明
通过 CompleteMultiUploadResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|completeMultipartUpload|[CompleteMultipartUploadResult](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/CompleteMultipartUploadResult.cs)|返回所有分片块上传成功信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

#### <span id = "ABORT_MULIT_UPLOAD"> 删除已上传的分片块 </span>

##### 功能说明

舍弃一个分块上传并删除已上传的块(Abort Multipart Upload).

##### 方法原型
```C#
AbortMultiUploadResult AbortMultiUpload(AbortMultiUploadRequest request);

void AbortMultiUpload(AbortMultiUploadRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

##### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
	AbortMultiUploadRequest request = new AbortMultiUploadRequest(bucket, key, uploadId);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	AbortMultiUploadResult result = cosXml.AbortMultiUpload(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string uploadId ="xxxxxxxx"; //初始化分片上传返回的uploadId
AbortMultiUploadRequest request = new AbortMultiUploadRequest(bucket, key, uploadId);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.AbortMultiUpload(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		AbortMultiUploadResult result = result as AbortMultiUploadResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|uploadId|构造方法 或 SetUploadId|标识指定分片上传的 uploadId |string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

##### 返回结果说明
通过 AbortMultiUploadResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### Post 上传对象

#### 功能说明

使用表单形式上传对象 (Post Object).

#### 方法原型
```C#
PostObjectResult PostObject(PostObjectRequest request);

void PostObject(PostObjectRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	string srcPath = @"F:\test.txt"；//本地文件路径
	PostObjectRequest request = new PostObjectRequest(bucket, key, srcPath);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
	});
	//执行请求
	PostObjectResult result = cosXml.PostObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string srcPath = @"F:\test.txt";  //本地文件路径
PostObjectRequest request = new PostObjectRequest(bucket, key, srcPath);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置进度回调
request.SetCosProgressCallback(delegate(long completed, long total)
{
	Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
});
//执行请求
cosXml.PostObject(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		PostObjectResult result = cosResult as PostObjectResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|srcPath|构造方法|用于上传到 cos 的本地文件的绝对路径|string|
|data|构造方法|用于上传到 cos 的 byte 数组|byte[]|
|progressCallback|SetCosProgressCallback|设置上传进度回调|Callback.OnProgressCallback|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 PostObjectResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|eTag|string|返回 对象 的 eTag|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 检索对象

#### 功能说明

查询存储桶中是否存在指定的对象 (Head Object).

#### 方法原型
```C#
HeadObjectResult HeadObject(HeadObjectRequest request);

void HeadObject(HeadObjectRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	HeadObjectRequest request = new HeadObjectRequest(bucket, key);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	HeadObjectResult result = cosXml.HeadObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
HeadObjectRequest request = new HeadObjectRequest(bucket, key);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.HeadObject(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		HeadObjectResult result = cosResult as HeadObjectResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 HeadObjectResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|eTag|string|返回 对象 的 eTag|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 下载对象

#### 功能说明

下载对象到本地 (Get Object).

#### 方法原型
```C#
GetObjectResult GetObject(GetObjectRequest request);

void GetObject(GetObjectRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	string localDir = @"F:\"；//下载到本地指定文件夹
	string localFileName = "test.txt"; //指定本地保存的文件名
	GetObjectRequest request = new GetObjectRequest(bucket, key, localDir, localFileName);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
	});
	//执行请求
	GetObjectResult result = cosXml.GetObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
 	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string localDir = @"F:\"；//下载到本地指定文件夹
string localFileName = "test.txt"; //指定本地保存的文件名
GetObjectRequest request = new GetObjectRequest(bucket, key, localDir, localFileName);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置进度回调
request.SetCosProgressCallback(delegate(long completed, long total)
{
	Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
});
//执行请求
cosXml.GetObject(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		GetObjectResult result = cosResult as GetObjectResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|localDir|构造方法|下载对象到本地保存的绝对文件夹路径|string|
|localFileName|构造方法|下载对象到本地保存的文件名|string|
|progressCallback|SetCosProgressCallback|设置下载进度回调|Callback.OnProgressCallback|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetObjectResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|eTag|string|返回 对象 的 eTag |

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 复制对象

复制对象操作包括：简单复制（适用于 1M 到 5G）；分片复制（适用于大文件拷贝，如 5G）

##### 简单复制

将一个对象复制到另一个对象 (Put Object Copy).

##### 方法原型
```C#
CopyObjectResult CopyObject(CopyObjectRequest request);

void CopyObject(CopyObjectRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

##### 请求示例
```C#
try
{
	string sourceAppid = "1253960454"; //账号 appid
	string sourceBucket = "source-1253960454"; //"源对象所在的存储桶
	string sourceRegion = "ap-beijing"; //源对象的存储桶所在的地域
	string sourceKey = "test.txt"; //源对象键
	//构造源对象属性
	COSXML.Model.Tag.CopySourceStruct copySource = new CopySourceStruct(sourceAppid, sourceBucket, sourceRegion, sourceKey);

	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "copy_test.txt"; //对象在存储桶中的位置，即称对象键.
	CopyObjectRequest request =  new CopyObjectRequest(bucket, key);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置拷贝源
	request.SetCopySource(copySource);
	//设置是否拷贝还是更新,此处是拷贝
	request.SetCopyMetaDataDirective(COSXML.Common.CosMetaDataDirective.COPY);
	//执行请求
	CopyObjectResult result = cosXml.CopyObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string sourceAppid = "1253960454"; //账号 appid
string sourceBucket = "source-1253960454"; //"源对象所在的存储桶
string sourceRegion = "ap-beijing"; //源对象的存储桶所在的地域
string sourceKey = "test.txt"; //源对象键
//构造源对象属性
COSXML.Model.Tag.CopySourceStruct copySource = new CopySourceStruct(sourceAppid, sourceBucket, sourceRegion, sourceKey);

string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "copy_test.txt"; //对象在存储桶中的位置，即称对象键.
CopyObjectRequest request =  new CopyObjectRequest(bucket, key);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置拷贝源
request.SetCopySource(copySource);
//设置是否拷贝还是更新,此处是拷贝
request.SetCopyMetaDataDirective(COSXML.Common.CosMetaDataDirective.COPY);
//执行请求
cosXml.CopyObject(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		CopyObjectResult result = cosResult as CopyObjectResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|copySource|SetCopySource|复制的数据源路径描述|CopySourceStruct|
|metaDataDirective|SetCopyMetaDataDirective|是否拷贝源文件的元数据或者更新源文件的元数据|CosMetaDataDirective|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

##### 返回结果说明
通过 CopyObjectResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|copyObject|[CopyObject](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/CopyObject.cs)|返回成功复制的对象信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

##### 分片复制

分片复制对象操作包含：
1、初始化分片上传，得到uploadId，详细请查看 [InitMultipartUpload](#INIT_MULIT_UPLOAD) ;
2、根据uploadId，进行分片复制;
3、完成所有分片复制，详细请查看 [CompleteMultiUpload](#COMPLETE_MULIT_UPLOAD) .

##### 方法原型
```C#
UploadPartCopyResult PartCopy(UploadPartCopyRequest request);

void PartCopy(UploadPartCopyRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

##### 请求示例
```C#
try
{
	string sourceAppid = "1253960454"; //账号 appid
	string sourceBucket = "source-1253960454"; //"源对象所在的存储桶
	string sourceRegion = "ap-beijing"; //源对象的存储桶所在的地域
	string sourceKey = "test.txt"; //源对象键
	//构造源对象属性
	COSXML.Model.Tag.CopySourceStruct copySource = new CopySourceStruct(sourceAppid, sourceBucket, sourceRegion, sourceKey);

	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "copy_test.txt"; //对象在存储桶中的位置，即称对象键.
	string uploadId = "1505706248ca8373f8a5cd52cb129f4bcf85e11dc8833df34f4f5bcc456c99c42cd1ffa2f9 "； //初始化分片上传的 uploadId
	int partNumber = 1; // partNumber >= 1
	UploadPartCopyRequest request = new UploadPartCopyRequest(bucket, key, partNumber, uploadId);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置拷贝源
	request.SetCopySource(copySource);
	//设置复制分片块
	request.SetCopyRange(0, 1024 * 1024);
	//执行请求
	UploadPartCopyResult result = cosXml.PartCopy(request);
	//请求成功
	//获取该分片块返回的eTag,用于CompleteMultiUpload
	string eTag = result.copyObject.eTag;
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string sourceAppid = "1253960454"; //账号 appid
string sourceBucket = "source-1253960454"; //"源对象所在的存储桶
string sourceRegion = "ap-beijing"; //源对象的存储桶所在的地域
string sourceKey = "test.txt"; //源对象键
//构造源对象属性
COSXML.Model.Tag.CopySourceStruct copySource = new CopySourceStruct(sourceAppid, sourceBucket, sourceRegion, sourceKey);

string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "copy_test.txt"; //对象在存储桶中的位置，即称对象键.
string uploadId = "1505706248ca8373f8a5cd52cb129f4bcf85e11dc8833df34f4f5bcc456c99c42cd1ffa2f9 "； //初始化分片上传的 uploadId
int partNumber = 1; // partNumber >= 1
UploadPartCopyRequest request = new UploadPartCopyRequest(bucket, key, partNumber, uploadId);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置拷贝源
request.SetCopySource(copySource);
//设置是否拷贝还是更新,此处是拷贝
request.SetCopyMetaDataDirective(COSXML.Common.CosMetaDataDirective.COPY);
//执行请求
cosXml.PartCopy(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		UploadPartCopyResult getObjectResult = result as UploadPartCopyResult;
		//获取该分片块返回的eTag,用于CompleteMultiUpload
		string eTag = result.copyObject.eTag;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|partNumber|构造方法|分片块的编号, partNumber >= 1|int|
|uploadId|构造方法|标识分片复制的 uploadId |string|
|copySource|SetCopySource|复制的数据源路径描述|CopySourceStruct|
|start|SetCopyRange|复制的内容的范围的起始位置|long|
|end|SetCopyRange|复制的内容范围的结束位置|long|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

##### 返回结果说明
通过 UploadPartCopyResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|copyObject|[CopyObject](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/CopyObject.cs)|返回 成功复制的 对象分片块信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 删除对象

#### 功能说明

删除指定的对象 (Delete Object).

#### 方法原型
```C#
DeleteObjectResult DeleteObject(DeleteObjectRequest request);

void DeleteObject(DeleteObjectRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	DeleteObjectRequest request = new DeleteObjectRequest(bucket, key);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	DeleteObjectResult result = cosXml.DeleteObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
DeleteObjectRequest request = new DeleteObjectRequest(bucket, key);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.DeleteObject(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		DeleteObjectResult getObjectResult = result as DeleteObjectResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 DeleteObjectResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 批量删除对象

#### 功能说明

删除指定存储桶中多个对象 (Delete Multi Objects).

#### 方法原型
```C#
DeleteMultiObjectResult DeleteMultiObjects(DeleteMultiObjectRequest request);

void DeleteMultiObjects(DeleteMultiObjectRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	DeleteMultiObjectRequest request = new DeleteMultiObjectRequest(bucket);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置返回结果形式
	request.SetDeleteQuiet(false);
	//删除多个对象
	List<string> keys = new List<string>();
	keys.Add("test1.txt");
	keys.Add("test2.txt");
	request.SetObjectKeys(keys);
	//执行请求
	DeleteMultiObjectResult result = cosXml.DeleteMultiObjects(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
DeleteMultiObjectRequest request = new DeleteMultiObjectRequest(bucket);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置返回结果形式
request.SetDeleteQuiet(false);
//删除多个对象
List<string> keys = new List<string>();
keys.Add("test1.txt");
keys.Add("test2.txt");
request.SetObjectKeys(keys);

//执行请求
cosXml.DeleteMultiObjects(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		DeleteMultiObjectResult result = cosResult as DeleteMultiObjectResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|quiet|SetDeleteQuiet|设定批量上传返回结果模式, true: 返回每个 key 的删除情况，false：只返回删除失败的 key 的情况|bool|
|key|SetDeleteKey|需要删除 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|versionId|SetDeleteKey|需要删除 cos 上 Object 的指定版本|string|
|keys|SetObjectKeys|需要删除 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)集合|`List<string>`|
|versionIdAndKey|SetObjectKeys|需要删除 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)和指定版本的集合|Dictionary<string, string>|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 DeleteMultiObjectResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|deleteResult|[DeleteResult](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/DeleteResult.cs)|返回批量删除 对象 的信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 设置对象 ACL

#### 功能说明

设置对象访问权限控制列表 (ACL)  (Put Object ACL).

#### 方法原型
```C#
PutObjectACLResult PutObjectACL(PutObjectACLRequest request);

void PutObjectACL(PutObjectACLRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	PutObjectACLRequest request = new PutObjectACLRequest(bucket, key);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//设置私有读写权限 
	request.SetCosACL(CosACL.PRIVATE); 
	//授予1131975903账号读权限 
	COSXML.Model.Tag.GrantAccount readAccount = new COSXML.Model.Tag.GrantAccount(); 
	readAccount.AddGrantAccount("1131975903", "1131975903"); 
	request.setXCosGrantRead(readAccount);
	//执行请求
	PutObjectACLResult result = cosXml.PutObjectACL(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
PutObjectACLRequest request = new PutObjectACLRequest(bucket, key);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//设置私有读写权限 
request.SetCosACL(CosACL.PRIVATE); 
//授予1131975903账号读权限 
COSXML.Model.Tag.GrantAccount readAccount = new COSXML.Model.Tag.GrantAccount(); 
readAccount.AddGrantAccount("1131975903", "1131975903"); 
request.setXCosGrantRead(readAccount);
//执行请求
cosXml.PutObjectACL(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		PutObjectACLResult result = cosResult as PutObjectACLResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|cosAcl|SetCosAcl|设置存储桶的acl权限|string|
|grandtAccout|SetXCosGrantRead 或 SetXCosGrantWrite 或 SetXCosReadWrite|授予用户读写权限|GrantAccount|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 PutObjectACLResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

### 获取对象 ACL

#### 功能说明

获取对象访问权限控制列表 (ACL)  (Get Object ACL).

#### 方法原型
```C#
GetObjectACLResult GetObjectACL(GetObjectACLRequest request);

void GetObjectACL(GetObjectACLRequest request, COSXML.Callback.OnSuccessCallback<CosResult> successCallback, COSXML.Callback.OnFailedCallback failCallback);
```

#### 请求示例
```C#
try
{
	string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
	string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
	GetObjectACLRequest request = new GetObjectACLRequest(bucket, key);
	//设置签名有效时长
	request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
	//执行请求
	GetObjectACLResult result = cosXml.GetObjectACL(request);
	//请求成功
    Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}

/**
//异步方法
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
GetObjectACLRequest request = new GetObjectACLRequest(bucket, key);
//设置签名有效时长
request.SetSign(TimeUtils.GetCurrentTime(TimeUnit.SECONDS), 600);
//执行请求
cosXml.GetObjectACL(request,
	delegate(COSXML.Model.CosResult cosResult)
	{
		//请求成功
		GetObjectACLResult result = cosResult as GetObjectACLResult;
		Console.WriteLine(result.GetResultInfo());

	}, 
	delegate(COSXML.CosException.CosClientException clientEx, COSXML.CosException.CosServerException serverEx)
	{	
		//请求失败
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
});
*/
```

#### 参数说明
|参数名称|设置方法|描述|类型|
|-----|-----|-----|------|
|bucket|构造方法|存储桶名称，格式：bucketname-appid|string|
|key|构造方法 或 SetCosPath|存储于 cos 上 Object 的[对象键](https://cloud.tencent.com/document/product/436/13324)|string|
|signStartTimeSecond|SetSign|签名有效期起始时间|long|
|durationSecond|SetSign|签名有效期时长|long|
|headerKeys|SetSign|签名是否校验header|`List<string>`|
|queryParameterKeys|SetSign|签名是否校验请求url中查询参数|`List<string>`|

#### 返回结果说明
通过 GetObjectACLResult 返回请求结果.

|成员变量|类型|描述|
|-----|-----|----|
|httpCode|int|HTTP Code， [200, 300)之间表示操作成功，否则表示操作失败|
|accessControlPolicy|[AccessControlPolicy](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/Model/Tag/AccessControlPolicy.cs)|返回 对象 的访问权限列表信息|

> 操作失败会抛出 [CosClientException](#COS_CLIENT_EXCEPTION) 或 [CosServerException](#COS_SERVER_EXCEPTION) 异常

## 高级 API 

### 高级 API 文件上传（推荐）

**TransferManager**、**COSXMLUploadTask** 封装了简单上传、分片上传接口的异步请求
```go
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string srcPath = @"F:\test.txt"; //文件的本地位置
COSXMLUploadTask uploadTask = new COSXMLUploadTask(bucket, null, key)
{	
	//进度回调
	successCallback = delegate (CosResult cosResult)
	{
		Console.WriteLine(String.Format("progress ={0:##.##}%",completed * 100.0 / total));
	},
	//成功回调
	successCallback = delegate (CosResult cosResult)
	{
		COSXML.Transfer.COSXMLUploadTask.UploadTaskResult result = cosResult as COSXML.Transfer.COSXMLUploadTask.UploadTaskResult;
		Console.WriteLine(result.GetResultInfo());
	},
	//失败回调
	failCallback = delegate (CosClientException clientEx, CosServerException serverEx)
	{
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	}
};
//设置上传源
long offset = 0; //从源文件0位置开始
long  sendContentLength  =  -1; //上传整个文件， (或者上传部分内容, sendContentLength > -1)
uploadTask.SetSrcPath(srcPath, offset, sendContentLength);
//执行请求
transferManager.Upload(uploadTask);
```

### 高级 API 文件下载（推荐）

**TransferManager**、**COSXMLDownloadTask** 封装了下载接口的异步请求
```go
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "test.txt"; //对象在存储桶中的位置，即称对象键.
string localDir = @"F:\"; //下载文件到本地保存的文件夹路径
string localFileNmae = "test.txt"; //下载文件到本地的文件名
COSXMLDownloadTask downloadTask = new COSXMLDownloadTask(bucket, null, key, localDir, localFileName)
{	
	//进度回调
	successCallback = delegate (CosResult cosResult)
	{
		Console.WriteLine(String.Format("progress ={0:##.##}%",completed * 100.0 / total));
	},
	//成功回调
	successCallback = delegate (CosResult cosResult)
	{
		COSXML.Transfer.COSXMLDownloadTask.DownloadTaskResult result = cosResult as COSXML.Transfer.COSXMLDownloadTask.DownloadTaskResult;
		Console.WriteLine(result.GetResultInfo());
	},
	//失败回调
	failCallback = delegate (CosClientException clientEx, CosServerException serverEx)
	{
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	}
};

//执行请求
transferManager.Download(downloadTask);
```

### 高级 API 文件复制（推荐）

**TransferManager**、**COSXMLCopyTask** 封装了简单复制、分片复制接口的异步请求
```go
string sourceAppid = "1253960454"; //账号 appid
string sourceBucket = "source-1253960454"; //"源对象所在的存储桶
string sourceRegion = "ap-beijing"; //源对象的存储桶所在的地域
string sourceKey = "test.txt"; //源对象键
//构造源对象属性
COSXML.Model.Tag.CopySourceStruct copySource = new CopySourceStruct(sourceAppid, sourceBucket, sourceRegion, sourceKey);
string bucket = "test-1253960454"; //存储桶，格式：bucketname-appid
string key = "copy_test.txt"; //对象在存储桶中的位置，即称对象键.
COSXMLCopyTask copyTask = new COSXMLCopyTask(bucket, null, key, copySource)
{	
	//成功回调
	successCallback = delegate (CosResult cosResult)
	{
		COSXML.Transfer.COSXMLCopyTask.CopyTaskResult result = cosResult as COSXML.Transfer.COSXMLCopyTask.CopyTaskResult;
		Console.WriteLine(result.GetResultInfo());
	},
	//失败回调
	failCallback = delegate (CosClientException clientEx, CosServerException serverEx)
	{
		if (clientEx != null)
		{
			Console.WriteLine("CosClientException: " + clientEx.Message);
		}
		else if (serverEx != null)
		{
			Console.WriteLine("CosServerException: " + serverEx.GetInfo());
		}
	}
};
//执行请求
transferManager.Copy(copyTask);
```

## <span id="COS_EXCEPTION"> SDK 异常说明 </span>

SDK 中，若是调用接口操作 cos 对象失败，会抛出 CosXmlClientException 异常 或者 CosXmlServiceException 异常

### <span id="COS_CLIENT_EXCEPTION"> [CosXmlClientException](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/CosException/CosClientException.cs) </span>

客户端异常，用于指因为客户端原因导致无法和服务端完成正常的交互而导致的失败， 如客户端无法连接到服务端，无法解析服务端返回的数据， 读取本地文件发生 IO 异常等。
CosClientException 集成自 System.ApplicationException, 使用方法同 System.ApplicationException， 同时添加一个额外的成员 errorCode，如下:

|成员|描述|类型|
| ---- | ---- | ---- |
|errorCode|客户端错误码,如 10000 表示参数检验失败|int|


### <span id="COS_SERVER_EXCEPTION"> [CosXmlServiceException](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXML/CosException/CosServerException.cs) </span>

CosServerException 服务异常， 用于指交互正常完成，但是操作失败的场景。例如客户端访问一个不存在 Bucket， 删除一个不存在的文件，没有权限进行某个操作， 服务端故障异常等。
CosServerException 包含了服务端返回的状态码， requestid， 出错明细等。捕获异常后， 建议对整个异常进行打印， 异常包含了必须的排查因素。以下是异常成员变量的描述：

| 成员   | 描述 | 类型 |
| ------------ | ---------------------------------------- | --------- |
| requestId    | 请求 ID，用于表示一个请求，对于排查问题十分重要.| string    |
| statusCode   | response 的 status 状态码，4xx 是指请求因客户端而失败，5xx 是服务端异常导致的失败。 请参照 [COS错误信息](https://cloud.tencent.com/document/product/436/7730)。 | string    |
| errorCode | 请求失败时 body 返回的 Error Code 请参照 [COS错误信息](https://cloud.tencent.com/document/product/436/7730).| string |
| errorMessage | 请求失败时 body 返回的 Error Message  请参照 [COS错误信息](https://cloud.tencent.com/document/product/436/7730).| string |
