## 简介

C# SDK 提供获取对象 URL、计算签名和获取请求预签名 URL 接口。

## 获取对象 URL 

```C#
string GetAccessURL(CosRequest request);
```

## 计算签名

```C#
string GenerateSign(string method, string path, Dictionary<string, string> queryParameters, Dictionary<string, string> headers, long signDurationSecond);
```

## 获取请求预签名 URL 

```C#
string GenerateSignURL(PreSignatureStruct preSignatureStruct);
```

#### 参数说明

| 参数名称           | 类型                         | 描述                            |
| ------------------ | ---------------------------- | ------------------------------- |
| request            | CosRequest                   | 请求对象                        |
| preSignatureStruct | PreSignatureStruct           | 预签名 URL 实例                 |
| method             | string                       | HTTP 请求方法                   |
| path               | string                       | HTTP 请求路径，即对象键         |
| headers            | `Dictionary<string, string>` | 签名是否校验 header             |
| queryParameters    | `Dictionary<string, string>` | 签名是否校验请求 url 中查询参数 |
| signDurationSecond | long                         | 签名有效期时长（单位为秒），例如签名有效时期为1分钟：60          |

#### PreSignatureStruct 结构体说明

通过 PreSignatureStruct 对象获取对应预签名请求 URL，用于发送请求。

| 参数名称           | 类型                         | 描述                               |
| ------------------ | ---------------------------- | ---------------------------------- |
| appid              | string                       | 腾讯云账号 APPID                   |
| bucket             | string                       | 存储桶                             |
| region             | string                       | 存储桶所在地域                     |
| method             | string                       | HTTP 请求方法                      |
| isHttps            | bool                         | true：HTTPS 请求，false：HTTP 请求 |
| key                | string                       | 对象键                             |
| headers            | `Dictionary<string, string>` | 签名是否校验 header                |
| queryParameters    | `Dictionary<string, string>` | 签名是否校验请求 url 中查询参数    |
| signDurationSecond | long                         | 签名有效期时长（单位为秒），例如签名有效时期为1分钟：60               |

## 永久密钥预签名请求示例

#### 上传请求示例

```C#
try
{
	//使用永久密钥初始化 CosXml
	CosXmlConfig config = new CosXmlConfig.Builder()
	.SetConnectionTimeoutMs(60000)  //设置连接超时时间，单位毫秒 ，默认45000ms
	.SetReadWriteTimeoutMs(40000)  //设置读写超时时间，单位毫秒 ，默认45000ms
	.IsHttps(true)  //设置默认 https 请求
	.SetAppid("1250000000")  //设置腾讯云账户的账户标识 APPID
	.SetRegion("ap-beijing")  //设置一个默认的存储桶地域
	.SetDebugLog(true)  //显示日志
	.Build();  //创建 CosXmlConfig 对象
	string secretId = "COS_SECRETID"; //"云 API 密钥 SecretId";
	string secretKey = "COS_SECRETKEY"; //"云 API 密钥 SecretKey";
	long durationSecond = 600;  //secretKey 有效时长,单位为 秒
	QCloudCredentialProvider cosCredentialProvider  =  new DefaultQCloudCredentialProvider(secretId, secretKey, durationSecond);
	CosXmlServer cosXml = new CosXmlServer(config, cosCredentialProvider);

	PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
	preSignatureStruct.appid = "1250000000";//腾讯云账号 appid
	preSignatureStruct.region = "ap-beijing"; //存储桶地域
	preSignatureStruct.bucket = "examplebucket-1250000000"; //存储桶
	preSignatureStruct.key = "exampleobject"; //对象键
	preSignatureStruct.httpMethod = "PUT"; //http 请求方法
	preSignatureStruct.isHttps = true; //生成 https 请求URL
	preSignatureStruct.signDurationSecond = 600; //请求签名时间为 600s
	preSignatureStruct.headers = null;//签名中需要校验的header
	preSignatureStruct.queryParameters = null; //签名中需要校验的URL中请求参数
	
	string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	string srcPath = @"F:\exampleobject";//本地文件绝地路径
	PutObjectRequest request = new PutObjectRequest(null, null, srcPath);
	//设置上传请求预签名 UR L
	request.RequestURLWithSign = requestSignURL;
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {0:##.##}%", completed * 100.0 / total));
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
```

#### 下载请求示例

```C#
try
{
	//使用永久密钥初始化 CosXml
	CosXmlConfig config = new CosXmlConfig.Builder()
	.SetConnectionTimeoutMs(60000)  //设置连接超时时间，单位毫秒 ，默认 45000ms
	.SetReadWriteTimeoutMs(40000)  //设置读写超时时间，单位毫秒 ，默认 45000ms
	.IsHttps(true)  //设置默认 https 请求
	.SetAppid("1250000000")  //设置腾讯云账户的账户标识 APPID
	.SetRegion("ap-beijing")  //设置一个默认的存储桶地域
	.SetDebugLog(true)  //显示日志
	.Build();  //创建 CosXmlConfig 对象
	string secretId = "COS_SECRETID"; //"云 API 密钥 SecretId";
	string secretKey = "COS_SECRETKEY"; //"云 API 密钥 SecretKey";
	long durationSecond = 600;  //secretKey 有效时长,单位为 秒
	QCloudCredentialProvider cosCredentialProvider  =  new DefaultQCloudCredentialProvider(secretId, secretKey, 600);
	CosXmlServer cosXml = new CosXmlServer(config, cosCredentialProvider);

	PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
	preSignatureStruct.appid = "1250000000";//腾讯云账号 appid
	preSignatureStruct.region = "ap-beijing"; //存储桶地域
	preSignatureStruct.bucket = "examplebucket-1250000000"; //存储桶
	preSignatureStruct.key = "exampleobject"; //对象键
	preSignatureStruct.httpMethod = "GET"; //http 请求方法
	preSignatureStruct.isHttps = true; //生成 https 请求URL
	preSignatureStruct.signDurationSecond = 600; //请求签名时间为 600s
	preSignatureStruct.headers = null;//签名中需要校验的header
	preSignatureStruct.queryParameters = null; //签名中需要校验的URL中请求参数
	
	string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct); //载请求预签名 URL (使用永久密钥方式计算的签名 URL )
	
	string localDir = @"F:\";//下载到本地指定文件夹
	string localFileName = "exampleobject"; //指定本地保存的文件名
	GetObjectRequest request = new GetObjectRequest(null, null, localDir, localFileName);
	//设置下载请求预签名 UR L
	request.RequestURLWithSign = requestSignURL;
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {0:##.##}%", completed * 100.0 / total));
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
```

## 临时密钥预签名请求示例

#### 上传请求示例

```C#
try
{
	//使用临时密钥初始化 CosXml
	CosXmlConfig config = new CosXmlConfig.Builder()
	.SetConnectionTimeoutMs(60000)  //设置连接超时时间，单位毫秒 ，默认45000ms
	.SetReadWriteTimeoutMs(40000)  //设置读写超时时间，单位毫秒 ，默认45000ms
	.IsHttps(true)  //设置默认 https 请求
	.SetAppid("1250000000")  //设置腾讯云账户的账户标识 APPID
	.SetRegion("ap-beijing")  //设置一个默认的存储桶地域
	.SetDebugLog(true)  //显示日志
	.Build();  //创建 CosXmlConfig 对象
	string tmpSecretId = "COS_SECRETID"; //"临时密钥 SecretId";
	string tmpSecretKey = "COS_SECRETKEY"; //"临时密钥 SecretKey";
	string tmpToken = "COS_TOKEN"; //"临时密钥 token";
	long tmpExpireTime = 1546862502;//临时密钥有效截止时间
	QCloudCredentialProvider cosCredentialProvider = new DefaultSessionQCloudCredentialProvider(tmpSecretId,tmpSecretKey,tmpExpireTime,tmpToken);
	CosXmlServer cosXml = new CosXmlServer(config, cosCredentialProvider);

	PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
	preSignatureStruct.appid = "1250000000";//腾讯云账号 APPID
	preSignatureStruct.region = "ap-beijing"; //存储桶地域
	preSignatureStruct.bucket = "examplebucket-1250000000"; //存储桶
	preSignatureStruct.key = "exampleobject"; //对象键
	preSignatureStruct.httpMethod = "PUT"; //http 请求方法
	preSignatureStruct.isHttps = true; //生成 https 请求URL
	preSignatureStruct.signDurationSecond = 600; //请求签名时间为600s
	preSignatureStruct.headers = null;//签名中需要校验的header
	preSignatureStruct.queryParameters = null; //签名中需要校验的URL中请求参数
	
	string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct); //上传预签名 URL (使用临时密钥方式计算的签名 URL )

	string srcPath = @"F:\exampleobject";//本地文件绝地路径
	PutObjectRequest request = new PutObjectRequest(null, null, srcPath);
	//设置上传请求预签名 UR L
	request.RequestURLWithSign = requestSignURL;
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {0:##.##}%", completed * 100.0 / total));
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
```

#### 下载请求示例

```C#
try
{
	//使用临时密钥初始化 CosXml
	CosXmlConfig config = new CosXmlConfig.Builder()
	.SetConnectionTimeoutMs(60000)  //设置连接超时时间，单位毫秒 ，默认45000ms
	.SetReadWriteTimeoutMs(40000)  //设置读写超时时间，单位毫秒 ，默认45000ms
	.IsHttps(true)  //设置默认 https 请求
	.SetAppid("1250000000")  //设置腾讯云账户的账户标识 APPID
	.SetRegion("ap-beijing")  //设置一个默认的存储桶地域
	.SetDebugLog(true)  //显示日志
	.Build();  //创建 CosXmlConfig 对象
	string tmpSecretId = "COS_SECRETID"; //"临时密钥 SecretId";
	string tmpSecretKey = "COS_SECRETKEY"; //"临时密钥 SecretKey";
	string tmpToken = "COS_TOKEN"; //"临时密钥 token";
	long tmpExpireTime = 1546862502;//临时密钥有效截止时间
	QCloudCredentialProvider cosCredentialProvider = new DefaultSessionQCloudCredentialProvider(tmpSecretId,tmpSecretKey,tmpExpireTime,tmpToken);
	CosXmlServer cosXml = new CosXmlServer(config, cosCredentialProvider);

	PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
	preSignatureStruct.appid = "1250000000";//腾讯云账号 appid
	preSignatureStruct.region = "ap-beijing"; //存储桶地域
	preSignatureStruct.bucket = "examplebucket-1250000000"; //存储桶
	preSignatureStruct.key = "exampleobject"; //对象键
	preSignatureStruct.httpMethod = "GET"; //http 请求方法
	preSignatureStruct.isHttps = true; //生成 https 请求URL
	preSignatureStruct.signDurationSecond = 600; //请求签名时间为600s
	preSignatureStruct.headers = null;//签名中需要校验的header
	preSignatureStruct.queryParameters = null; //签名中需要校验的URL中请求参数
	
	string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct); //载请求预签名 URL (使用临时密钥方式计算的签名 URL )
	
	string localDir = @"F:\";//下载到本地指定文件夹
	string localFileName = "exampleobject"; //指定本地保存的文件名
	GetObjectRequest request = new GetObjectRequest(null, null, localDir, localFileName);
	//设置下载请求预签名 UR L
	request.RequestURLWithSign = requestSignURL;
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {0:##.##}%", completed * 100.0 / total));
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
```
