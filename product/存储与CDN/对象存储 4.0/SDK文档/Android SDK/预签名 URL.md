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
#### 参数说明
|参数名称|类型|描述|
|-----|-----|----|
|cosXmlRequest|CosXmlRequest|请求对象|
|presignedUrlRequest |PresignedUrlRequest |预签名 URL 实例|
|checkParameterListForSing |`Set<String>`|签名中需要验证的请求头|
|checkHeaderListForSign  |`Set<String>`|签名中需要验证的请求参数|

#### PresignedUrlRequest 结构体说明
通过 PresignedUrlRequest 对象获取对应预签名请求 URL，用于发送请求。

|参数名称|类型|描述|
|-----|-----|----|
|bucket|string|COS XML API 的存储桶名称，格式为：`<BucketName-APPID>`<br>例如 examplebucket-1250000000 |
|requestMethod|string|HTTP 请求方法，例如 GET（下载）|
|cosPath |string|对象键，即对象在存储桶中的位置标识符|
|checkParameterListForSing |`Set<String>`|签名中需要验证的请求头|
|checkHeaderListForSign  |`Set<String>`|签名中需要验证的请求参数|

## 获取请求预签名示例

```java
方法一： 使用 PresignedUrlRequest 构造预请求
try{
String bucket = "examplebucket-1250000000"; //存储桶名称
String cosPath = "exampleobject"; //即对象在存储桶中的位置标识符。如 cosPath = "text.txt";
String method = "GET"; //请求HTTP方法，如下载 GET, PUT 上传.
PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
presignedUrlRequest.setRequestMethod(method);

//Set<String> checkParameterListForSing = new HashSet<String>();
//Set<String> checkHeaderListForSign = new HashSet<String>();
//presignedUrlRequest.setSignParamsAndHeaders(checkParameterListForSing, checkHeaderListForSign);

String urlWithSign = cosXmlService.getPresignedURL(presignedUrlRequest);
}catch(Exception ex){
Log.d("TEST", ex.getMessage());
}


方法二： 直接使用对应的请求，如 PutObjectRequest, GetObjectRequest等
try{
PutObjectRequest putObjectRequest;
String urlWithSign = cosXmlService.getPresignedURL(putObjectRequest);
}catch(Exception ex){
Log.d("TEST", ex.getMessage());
}
```
## 永久密钥预签名请求示例

#### 上传请求示例
```java
try {
	//使用永久密钥初始化 CosXmlService
	Context context = getApplicationContext(); // application context
	String bucket = "examplebucket-1250000000"; //存储桶名称
	String region = Region.AP_Guangzhou.getRegion();
	String appid = "1250000000";
	String secretId = "COS_SECRETID"; //"云 API 密钥 SecretId";
	String secretKey = "COS_SECRETKEY"; //"云 API 密钥 SecretKey";
	long durationSecond = 600;  //secretKey 有效时长,单位为 秒
	//初始化 config
	CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
					.isHttps(true)  //设置 https 请求, 默认 http 请求
					.setRegion(region)
					.setDebuggable(true)
					.builder();
	//使用永久密钥初始化QCloudCredentialProvider
	QCloudCredentialProvider qCloudCredentialProvider = new ShortTimeCredentialProvider(secretId, secretKey, durationSecond);
	//初始化CosXmlService
	CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, qCloudCredentialProvider);

	String cosPath = "exampleobject"; //即对象在存储桶中的位置标识符。如 cosPath = "text.txt";
	String method = "PUT"; //请求 HTTP 方法.
	PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath){
	    @Override
        public RequestBodySerializer getRequestBody() throws CosXmlClientException {
            //用于计算 put 等需要带上  body 的请求的签名URL
            return RequestBodySerializer.string("text/plain", "this is test"); 
         }
    };
	presignedUrlRequest.setRequestMethod(method);

	String urlWithSign = cosXmlService.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	//String urlWithSign = cosXmlService.getPresignedURL(putObjectRequest)； //直接使用 PutObjectRequest

	String srcPath = Environment.getExternalStorageDirectory().getPath() + "/exampleobject";
	PutObjectRequest putObjectRequest = new PutObjectRequest(null, null, srcPath);
	//设置上传请求预签名 URL
	putObjectRequest.setRequestURL(urlWithSign);
	//设置进度回调
	putObjectRequest.setProgressListener(new CosXmlProgressListener() {
			@Override
			public void onProgress(long progress, long max) {
					// todo Do something to update progress...
			}
	});
	// 使用同步方法上传
	PutObjectResult putObjectResult = cosXmlService.putObject(putObjectRequest);
	} catch (CosXmlClientException e) {
	e.printStackTrace();
	} catch (CosXmlServiceException e) {
	e.printStackTrace();
}
```

#### 下载请求示例
```java
try
{
	//使用永久密钥初始化 CosXmlService
	Context context = getApplicationContext(); // application context
	String bucket = "examplebucket-1250000000"; //存储桶名称
	String region = Region.AP_Guangzhou.getRegion();
	String appid = "1250000000";
	String secretId = "COS_SECRETID"; //"云 API 密钥 SecretId";
	String secretKey = "COS_SECRETKEY"; //"云 API 密钥 SecretKey";
	long durationSecond = 600;  //secretKey 有效时长,单位为 秒
	//初始化 config
	CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
					.isHttps(true)  //设置 https 请求, 默认 http 请求
					.setRegion(region)
					.setDebuggable(true)
					.builder();
	//使用永久密钥初始化 QCloudCredentialProvider
	QCloudCredentialProvider  qCloudCredentialProvider = new ShortTimeCredentialProvider(secretId, secretKey, durationSecond);
	//初始化CosXmlService
	CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, qCloudCredentialProvider);

	String cosPath = "exampleobject"; //即对象在存储桶中的位置标识符。如 cosPath = "text.txt";
	String method = "GET"; //请求 HTTP 方法.
	PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
	presignedUrlRequest.setRequestMethod(method);

	String urlWithSign = cosXmlService.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	//String urlWithSign = cosXmlService.getPresignedURL(getObjectRequest)； //直接使用 GetObjectRequest

	String savePath = Environment.getExternalStorageDirectory().getPath()；//本地路径
	String saveFileName = "exampleobject"; //本地文件名
	GetObjectRequest getObjectRequest = new GetObjectRequest(null, null, savePath, saveFileName);

	//设置上传请求预签名 URL
	getObjectRequest.setRequestURL(urlWithSign);
	//设置进度回调
	getObjectRequest.setProgressListener(new CosXmlProgressListener() {
			@Override
			public void onProgress(long progress, long max) {
					// todo Do something to update progress...
			}
	});
	// 使用同步方法下载
	GetObjectResult getObjectResult =cosXmlService.getObject(getObjectRequest);
	} catch (CosXmlClientException e) {
	e.printStackTrace();
	} catch (CosXmlServiceException e) {
	e.printStackTrace();
}
```


## 临时密钥预签名请求示例

#### 上传请求示例
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
		.isHttps(true)  //设置 https 请求, 默认 http 请求
		.setAppid(appid)
		.setRegion(region)
		.setDebuggable(true)
		.builder();
	//使用临时密钥初始化QCloudCredentialProvider
	QCloudCredentialProvider  qCloudCredentialProvider = new BasicLifecycleCredentialProvider() {
          @Override
          protected QCloudLifecycleCredentials fetchNewCredentials() throws QCloudClientException {
              return new SessionQCloudCredentials(secretId, secretKey, sessionToken, startTime, expiredTime);
          }
      };
	//初始化CosXmlService
	CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, qCloudCredentialProvider);

	String cosPath = "exampleobject"; //即对象在存储桶中的位置标识符。如 cosPath = "text.txt";
	String method = "PUT"; //请求 HTTP 方法.
	PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath){
	    @Override
        public RequestBodySerializer getRequestBody() throws CosXmlClientException {
            //用于计算 put 等需要带上  body 的请求的签名URL
            return RequestBodySerializer.string("text/plain", "this is test"); 
         }
    };	
	presignedUrlRequest.setRequestMethod(method);
	
	String urlWithSign = cosXmlService.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

	//String urlWithSign = cosXmlService.getPresignedURL(putObjectRequest)； //直接使用PutObjectRequest

	string srcPath = Environment.getExternalStorageDirectory().getPath() + "/exampleobject";
	PutObjectRequest putObjectRequest = new PutObjectRequest(null, null, srcPath);
	//设置上传请求预签名 URL
	putObjectRequest.setRequestURL(urlWithSign);
	//设置进度回调
	putObjectRequest.setProgressListener(new CosXmlProgressListener() {
	    @Override
	    public void onProgress(long progress, long max) {
	        // todo Do something to update progress...
	    }
	});
	// 使用同步方法上传
	PutObjectResult putObjectResult = cosXmlService.putObject(putObjectRequest);
} catch (CosXmlClientException e) {
	e.printStackTrace();
} catch (CosXmlServiceException e) {
	e.printStackTrace();
}
```

#### 下载请求示例
```java
try
{
	//使用临时密钥初始化 CosXmlService
	Context context = getApplicationContext(); // application context
	String bucket = "examplebucket-1250000000"; //存储桶名称
	String region = Region.AP_Guangzhou.getRegion();
	String appid = "1250000000";
	String secretId = "COS_SECRETID"; //临时密钥 SecretId
	String secretKey = "COS_SECRETKEY"; //临时密钥 SecretKey
	String sessionToken = "TOKEN"; // 临时密钥 Token
	long startTime = 1555054436;  //临时密钥有效起始时间戳
	long expiredTime = 1555055036;//临时密钥有效截止时间戳
	//初始化 config
	CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
					.isHttps(true)  //设置 https 请求, 默认http请求
					.setRegion(region)
					.setDebuggable(true)
					.builder();
	//使用临时密钥初始化QCloudCredentialProvider
	QCloudCredentialProvider  qCloudCredentialProvider = new BasicLifecycleCredentialProvider() {
	@Override
	protected QCloudLifecycleCredentials fetchNewCredentials() throws QCloudClientException {
			return new SessionQCloudCredentials(secretId, secretKey, sessionToken, startTime, expiredTime);
	}
	};
	//初始化CosXmlService
    CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, qCloudCredentialProvider);

    String cosPath = "exampleobject"; //即对象在存储桶中的位置标识符。如 cosPath = "text.txt";
    String method = "GET"; //请求 HTTP 方法.
    PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
    presignedUrlRequest.setRequestMethod(method);

    String urlWithSign = cosXmlService.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

    //String urlWithSign = cosXmlService.getPresignedURL(getObjectRequest)； //直接使用 GetObjectRequest

    String savePath = Environment.getExternalStorageDirectory().getPath()；//本地路径
    String saveFileName = "exampleobject"; //本地文件名
    GetObjectRequest getObjectRequest = new GetObjectRequest(null, null, savePath, saveFileName);

    //设置上传请求预签名 URL
    getObjectRequest.setRequestURL(urlWithSign);
    //设置进度回调
    getObjectRequest.setProgressListener(new CosXmlProgressListener() {
            @Override
            public void onProgress(long progress, long max) {
                    // todo Do something to update progress...
            }
    });
    // 使用同步方法下载
    GetObjectResult getObjectResult =cosXmlService.getObject(getObjectRequest);
    } catch (CosXmlClientException e) {
    e.printStackTrace();
    } catch (CosXmlServiceException e) {
    e.printStackTrace();
}
```
