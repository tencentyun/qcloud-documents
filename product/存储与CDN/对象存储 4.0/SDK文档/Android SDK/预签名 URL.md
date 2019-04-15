## 简介
Android SDK 提供获取对象 URL、获取请求预签名 URL 接口。

## 获取对象 URL 
```java
string getAccessUrl(CosXmlRequest cosXmlRequest);
```

## 获取请求预签名 URL 
```java
String getPresignedURL(CosXmlRequest cosXmlRequest) throws CosXmlClientException;
```
### 参数说明
|参数名称|类型|描述|
|-----|-----|----|
|cosXmlRequest|CosXmlRequest|请求对象|
|presignedUrlRequest |PresignedUrlRequest |预签名 URL 实例|
|checkParameterListForSing |`Set<String>`|签名中需要验证的请求头|
|checkHeaderListForSign  |`Set<String>`|签名中需要验证的请求参数|

### PresignedUrlRequest 结构体说明
通过 PresignedUrlRequest 对象获取对应预签名请求 URL，用于发送请求。

|参数名称|类型|描述|
|-----|-----|----|
|bucket|string|存储桶名称（COS XML API 的 bucket格式为：`<BucketName-APPID>`，如 examplebucket-1250000000 |
|requestMethod|string|HTTP 请求方法，如下载 GET|
|cosPath |string|对象键，即存储到 COS 上的绝对路径|
|checkParameterListForSing |`Set<String>`|签名中需要验证的请求头|
|checkHeaderListForSign  |`Set<String>`|签名中需要验证的请求参数|

## 获取请求预签名示例

```java
方法一： 使用 PresignedUrlRequest 构造预请求
try{
String bucket = "examplebucket-1250000000"; //存储桶名称
String cosPath = "exampleobject"; //即存储到 COS 上的绝对路径";如 cosPath = "test.txt";
String method = "GET"; //请求HTTP方法，如下载 GET, PUT 上传.
PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
presignedUrlRequest.setRequestMethod(method);

//Set<String> checkParameterListForSing = new HashSet<String>();
//Set<String> checkHeaderListForSign = new HashSet<String>();
//presignedUrlRequest.setSignParamsAndHeaders(checkParameterListForSing, checkHeaderListForSign);

String urlWithSign = cosXml.getPresignedURL(presignedUrlRequest);
}catch(Exception ex){
Log.d("TEST", ex.getMessage());
}


方法二： 直接使用对应的请求，如 PutObjectRequest, GetObjectRequest等
try{
PutObjectRequest putObjectResutl;
String urlWithSign = cosXml.getPresignedURL(putObjectResutl);
}catch(Exception ex){
Log.d("TEST", ex.getMessage());
}
```
## 临时密钥预签名请求示例

### 上传请求示例
```java
try
{
	//使用永久密钥初始化 CosXmlService
	Context context = getApplicationContext(); // application context
	String bucket = "examplebucket-1250000000"; //存储桶名称
	String region = Region.AP_Guangzhou.getRegion();
	String appid = "1250000000";
	string secretId = "COS_SECRETID"; //"云 API 密钥 SecretId";
	string secretKey = "COS_SECRETKEY"; //"云 API 密钥 SecretKey";
	long durationSecond = 600;  //secretKey 有效时长,单位为 秒
	//初始化 config
	CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
		.isHttps(true)  //设置 https 请求, 默认http请求
		.setAppid(appid)
		.setRegion(region)
		.setDebuggable(true)
		.builder();
	//使用永久密钥初始化QCloudCredentialProvider
	QCloudCredentialProvider  qCloudCredentialProvider = new ShortTimeCredentialProvider(secretId, secretKey, durationSecond); 
	//初始化CosXmlService
	CosXmlServer cosXmlService = new CosXmlServer(context, serviceConfig, qCloudCredentialProvider);

	String cosPath = "exampleobject"; //即存储到 COS 上的绝对路径";如 cosPath = "test.txt";
	String method = "PUT"; //请求HTTP方法.
	PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
	presignedUrlRequest.setRequestMethod(method);
	
	String urlWithSign = cosXml.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	//String urlWithSign = cosXml.getPresignedURL(putObjectResutl)； //直接使用PutObjectRequest

	string srcPath = @"F:\exampleobject"；//本地文件绝地路径
	PutObjectRequest request = new PutObjectRequest(null, null, srcPath);
	//设置上传请求预签名 UR L
	putObjectRequest.setRequestURL(urlWithSign);
	//设置进度回调
	putObjectRequest.setProgressListener(new CosXmlProgressListener() {
	    @Override
	    public void onProgress(long progress, long max) {
	        // todo Do something to update progress...
	    }
	});
	// 使用同步方法上传
	try {
	    PutObjectResult putObjectResult = cosXmlService.putObject(putObjectRequest);
	} catch (CosXmlClientException e) {
	    e.printStackTrace();
	} catch (CosXmlServiceException e) {
	    e.printStackTrace();
	}
```

### 下载请求示例
```java
try
{
	//使用永久密钥初始化 CosXmlService
	Context context = getApplicationContext(); // application context
	String bucket = "examplebucket-1250000000"; //存储桶名称
	String region = Region.AP_Guangzhou.getRegion();
	String appid = "1250000000";
	string secretId = "COS_SECRETID"; //"云 API 密钥 SecretId";
	string secretKey = "COS_SECRETKEY"; //"云 API 密钥 SecretKey";
	long durationSecond = 600;  //secretKey 有效时长,单位为 秒
	//初始化 config
	CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
		.isHttps(true)  //设置 https 请求, 默认http请求
		.setAppid(appid)
		.setRegion(region)
		.setDebuggable(true)
		.builder();
	//使用永久密钥初始化QCloudCredentialProvider
	QCloudCredentialProvider  qCloudCredentialProvider = new ShortTimeCredentialProvider(secretId, secretKey, durationSecond); 
	//初始化CosXmlService
	CosXmlServer cosXmlService = new CosXmlServer(context, serviceConfig, qCloudCredentialProvider);

	String cosPath = "exampleobject"; //即存储到 COS 上的绝对路径";如 cosPath = "test.txt";
	String method = "GET"; //请求HTTP方法.
	PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
	presignedUrlRequest.setRequestMethod(method);
	
	String urlWithSign = cosXml.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	//String urlWithSign = cosXml.getPresignedURL(getObjectResutl)； //直接使用GetObjectRequest

	string savePath = Environment.getExternalStorageDirectory().getPath()；//本地路径
	String saveFileName = "exampleobject"; //本地文件名
	GetObjectRequest getObjectRequest = new GetObjectRequest(null, null, savePath, saveFileName);
	
	//设置上传请求预签名 UR L
	getObjectRequest.setRequestURL(urlWithSign);
	//设置进度回调
	getObjectRequest.setProgressListener(new CosXmlProgressListener() {
	    @Override
	    public void onProgress(long progress, long max) {
	        // todo Do something to update progress...
	    }
	});
	// 使用同步方法上传
	try {
	    GetObjectResult getObjectResult =cosXmlService.getObject(getObjectRequest);
	} catch (CosXmlClientException e) {
	    e.printStackTrace();
	} catch (CosXmlServiceException e) {
	    e.printStackTrace();
	}
```


## 临时密钥预签名请求示例

### 上传请求示例
```java
try
{
	//使用临时密钥初始化 CosXmlService
	Context context = getApplicationContext(); // application context
	String bucket = "examplebucket-1250000000"; //存储桶名称
	String region = Region.AP_Guangzhou.getRegion();
	String appid = "1250000000";
	string secretId = "COS_SECRETID"; //临时密钥 SecretId
	string secretKey = "COS_SECRETKEY"; //临时密钥 SecretKey
	String sessionToken = "TOKEN"; // 临时密钥 Token
	long startTime = 1555054436;  //临时密钥有效起始时间戳
	long expiredTime = 1555055036;//临时密钥有效截止时间戳
	//初始化 config
	CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
		.isHttps(true)  //设置 https 请求, 默认http请求
		.setAppid(appid)
		.setRegion(region)
		.setDebuggable(true)
		.builder();
	//使用临时密钥初始化QCloudCredentialProvider
	QCloudCredentialProvider  qCloudCredentialProvider = new SessionQCloudCredentials(secretId, secretKey, sessionToken, startTime, expiredTime); 
	//初始化CosXmlService
	CosXmlServer cosXmlService = new CosXmlServer(context, serviceConfig, qCloudCredentialProvider);

	String cosPath = "exampleobject"; //即存储到 COS 上的绝对路径";如 cosPath = "test.txt";
	String method = "PUT"; //请求HTTP方法.
	PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
	presignedUrlRequest.setRequestMethod(method);
	
	String urlWithSign = cosXml.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	//String urlWithSign = cosXml.getPresignedURL(putObjectResutl)； //直接使用PutObjectRequest

	string srcPath = @"F:\exampleobject"；//本地文件绝地路径
	PutObjectRequest request = new PutObjectRequest(null, null, srcPath);
	//设置上传请求预签名 UR L
	putObjectRequest.setRequestURL(urlWithSign);
	//设置进度回调
	putObjectRequest.setProgressListener(new CosXmlProgressListener() {
	    @Override
	    public void onProgress(long progress, long max) {
	        // todo Do something to update progress...
	    }
	});
	// 使用同步方法上传
	try {
	    PutObjectResult putObjectResult = cosXmlService.putObject(putObjectRequest);
	} catch (CosXmlClientException e) {
	    e.printStackTrace();
	} catch (CosXmlServiceException e) {
	    e.printStackTrace();
	}
```

### 下载请求示例
```java
try
{
	//使用临时密钥初始化 CosXmlService
	Context context = getApplicationContext(); // application context
	String bucket = "examplebucket-1250000000"; //存储桶名称
	String region = Region.AP_Guangzhou.getRegion();
	String appid = "1250000000";
	string secretId = "COS_SECRETID"; //临时密钥 SecretId
	string secretKey = "COS_SECRETKEY"; //临时密钥 SecretKey
	String sessionToken = "TOKEN"; // 临时密钥 Token
	long startTime = 1555054436;  //临时密钥有效起始时间戳
	long expiredTime = 1555055036;//临时密钥有效截止时间戳
	//初始化 config
	CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
		.isHttps(true)  //设置 https 请求, 默认http请求
		.setAppid(appid)
		.setRegion(region)
		.setDebuggable(true)
		.builder();
	//使用临时密钥初始化QCloudCredentialProvider
	QCloudCredentialProvider  qCloudCredentialProvider = new SessionQCloudCredentials(secretId, secretKey, sessionToken, startTime, expiredTime); 
	//初始化CosXmlService
	CosXmlServer cosXmlService = new CosXmlServer(context, serviceConfig, qCloudCredentialProvider);

	String cosPath = "exampleobject"; //即存储到 COS 上的绝对路径";如 cosPath = "test.txt";
	String method = "GET"; //请求HTTP方法.
	PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
	presignedUrlRequest.setRequestMethod(method);
	
	String urlWithSign = cosXml.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	//String urlWithSign = cosXml.getPresignedURL(getObjectResutl)； //直接使用GetObjectRequest

	string savePath = Environment.getExternalStorageDirectory().getPath()；//本地路径
	String saveFileName = "exampleobject"; //本地文件名
	GetObjectRequest getObjectRequest = new GetObjectRequest(null, null, savePath, saveFileName);
	
	//设置上传请求预签名 UR L
	getObjectRequest.setRequestURL(urlWithSign);
	//设置进度回调
	getObjectRequest.setProgressListener(new CosXmlProgressListener() {
	    @Override
	    public void onProgress(long progress, long max) {
	        // todo Do something to update progress...
	    }
	});
	// 使用同步方法上传
	try {
	    GetObjectResult getObjectResult =cosXmlService.getObject(getObjectRequest);
	} catch (CosXmlClientException e) {
	    e.printStackTrace();
	} catch (CosXmlServiceException e) {
	    e.printStackTrace();
	}
```
