## 初始化
进行操作之前需要实例化 CosXmlService 和 CosXmlServiceConfig。
> 关于文章中出现的 SecretID、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

#### 实例化 CosXmlServiceConfig
调用 `CosXmlServiceConfig(String appid, String region)`构造方法，实例化 CosXmlServiceConfig 对象。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| appid           | 对象存储 的服务 APPID |String          | 是  | 
| region          |  存储桶 所在的地域 |String          | 是  |

#### 其它配置设置方法
|   方法   |     方法描述   |
|---------|-----------|
|   setHttpProtocol(boolean)  | true：https请求； false：http请求； 默认 http 请求|
|   setConnectionTimeout(int) |     连接超时设置   |
|  setSocketTimeout(int)   |     读写超时设置   |
|   setMaxRetryCount(int)  |     失败请求重试次数   |

#### 示例
```java
String appid = "对象存储的服务 APPID";
String region = "存储桶所在的地域"; //所属地域：在创建好存储桶后，可通过对象存储控制台查看
CosXmlServiceConfig cosXmlServiceConfig = new CosXmlServiceConfig(appid,region);
```

#### 实例化 CosXmlService
调用 `CosXmlService(Context context, CosXmlServiceConfig serviceConfig, CosXmlCredentialProvider cloudCredentialProvider)` 构造方法，实例化 CosXmlService 对象。

#### 参数说明
| 参数名称   |参数描述   | 类型 | 必填 | 
| -------------- | -------------- | -- | ----------- |
| context         |  上下文 |Context         | 是  |
| serviceConfig   | SDK 的配置设置类 |CosXmlServiceConfig    | 是  | 
| cloudCredentialProvider   |  服务请求的签名获取类 |CosXmlCredentialProvider    | 是  |

#### 示例
```java
String appid = "对象存储的服务 APPID";
String region = "存储桶所在的地域"; 

//创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
CosXmlServiceConfig cosXmlServiceConfig = new CosXmlServiceConfig(appid,region);

/**
* 
* 创建 CosXmlCredentialProvider 签名获取类对象，用于使用对象存储服务时计算签名。
* 参考 SDK 提供签名格式，可实现自己的签名方法。
* 此处使用 SDK 提供的默认签名计算方法。
*
*/
String secretId = "云 API 密钥 SecretId";
String secretKey ="云 API 密钥 SecretKey";
long keyDuration = 600; //SecretKey 的有效时间,单位秒
CosXmlCredentialProvider cosXmlCredentialProvider = new CosXmlLocalCredentialProvider(secretId, secretKey, keyDuration);

//创建 CosXmlService 对象，实现对象存储服务各项操作。
Context context = getApplicationContext()； //应用的上下文
CosXmlService cosXmlService = new CosXmlService(context,cosXmlServiceConfig, cosXmlCredentialProvider);

```

## 生成签名

签名具体的生成和使用请参照 [签名流程](https://cloud.tencent.com/document/product/436/7778)。
SDK 中已提供了签名获取类，用户只需要继承 CosXmlCredentialProvider 类，并重写 `signaturePair()` 方法。

#### 示例
```java
public class CosXmlLocalCredentialProvider extends CosXmlCredentialProvider{
     private String secretKey;
     private long duration;

     public CosXmlLocalCredentialProvider(String secretId, String secretKey, long keyDuration) {
          super(secretId);
          this.secretKey = secretKey;
          this.duration = keyDuration;
     }

     @Override
     public CosXmlSignaturePair signaturePair() throws QCloudException {
         long current = System.currentTimeMillis() / 1000;
         long expired = current + duration;
         String keyTime = current+";"+expired;
         return new CosXmlSignaturePair(secretKeyToSignKey(secretKey, keyTime), keyTime);
     }

     private String secretKeyToSignKey(String secretKey, String keyTime) {
         String signKey = null;
         try {
              if (secretKey == null) {
                   throw new IllegalArgumentException("secretKey is null");
              }
              if (keyTime == null) {
                    throw new IllegalArgumentException("qKeyTime is null");
              }
         } catch (IllegalArgumentException e) {
                e.printStackTrace();
         }
         try {
             byte[] byteKey = secretKey.getBytes("utf-8");
             SecretKey hmacKey = new SecretKeySpec(byteKey, "HmacSHA1");
             Mac mac = Mac.getInstance("HmacSHA1");
             mac.init(hmacKey);
             signKey = StringUtils.toHexString(mac.doFinal(keyTime.getBytes("utf-8")));
        } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
        } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
        } catch (InvalidKeyException e) {
                e.printStackTrace();
        }
      return signKey;
    }
}
```
## 简单上传文件

调用此接口可以将本地的文件上传至指定 Bucket 中。具体步骤如下：
1. 调用 `PutObjectRequest()`构造方法，实例化 PutObjectRequest 对象。
2. 调用 CosXmlService 的 getService 方法，传入 PutObjectRequest，返回 PutObjectResult 对象。
   （或者 调用 putObjectAsync 方法，传入 PutObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | ----- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| srcPath   | 本地文件的绝对路径   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    | Set&lt;String>           | 否  |
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| qCloudProgressListener   | 上传进度回调     |QCloudProgressListener          | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 PutObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | ----- | 
| error  |[请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     | COSXMLError             | 
| accessUrl   | 请求成功时，返回访问文件的地址|String          | 

#### 示例
```java
PutObjectRequest putObjectRequest = new PutObjectRequest();
putObjectRequest.setBucket(bucket);
putObjectRequest.setCosPath(cosPath);
putObjectRequest.setSrcPath(srcPath);
putObjectRequest.setSign(signDuration,null,null);
putObjectRequest.setProgressListener(new QCloudProgressListener() {
    @Override
    public void onProgress(long progress, long max) {
        float result = (float) (progress * 100.0/max);
        Log.w("TEST","progress =" + (long)result + "%");
    }
});

//使用同步方法上传
try {
    PutObjectResult putObjectResult = cosXmlService.putObject(putObjectRequest);
	
	//上传失败， 返回 httpCode 不在【200，300）之内；
	if(putObjectResult.getHttpCode() >= 300 || putObjectResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(putObjectResult.error.code)
				.append(putObjectResult.error.message)
				.append(putObjectResult.error.resource)
				.append(putObjectResult.error.requestId)
				.append(putObjectResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//上传成功
	if(putObjectResult.getHttpCode() >= 200 && putObjectResult.getHttpCode() < 300){
		//上传成功后，则可以拼接访问此文件的地址，格式为：bucket-appid.region.myqcloud.com.cosPath;
		
		Log.w("TEST","accessUrl =" + putObjectResult.accessUrl);
	}
       
  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}

//**使用异步回调上传**
/**

cosXmlService.putObjectAsync(putObjectRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {
      	 Log.w("TEST","accessUrl =" + result.accessUrl);
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/

```
## 分片上传
### 初始化分片

调用此接口实现初始化分片上传，成功执行此请求以后会返回 UploadId 用于后续的 Upload Part 请求。具体步骤如下：
1. 调用 `InitMultipartUploadRequest()`构造方法，实例化 InitMultipartUploadRequest 对象。
2. 调用 CosXmlService 的 initMultipartUpload 方法，传入 InitMultipartUploadRequest，返回 InitMultipartUploadResult 对象。
   （或者 调用 initMultipartUploadAsync 方法，传入 InitMultipartUploadRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   | long           | 是  |
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 InitMultipartUploadResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | -- | 
| error  | [请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     |COSXMLError             | 
| initMultipartUpload   |  [请求成功的返回结果](https://cloud.tencent.com/document/product/436/7746)|InitMultipartUpload          |

#### 示例
```java
InitMultipartUploadRequest initMultipartUploadRequest = new InitMultipartUploadRequest();
initMultipartUploadRequest.setBucket(bucket);
initMultipartUploadRequest.setCosPath(cosPath);
initMultipartUploadRequest.setSign(signDuration,null,null);

String uploadId = null;

//使用同步方法请求
try {
    InitMultipartUploadResult initMultipartUploadResult = cosXmlService.initMultipartUpload(initMultipartUploadRequest);
	
	//请求失败， 返回 httpCode 不在【200，300）之内；
	if(initMultipartUploadResult.getHttpCode() >= 300 || initMultipartUploadResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(initMultipartUploadResult.error.code)
				.append(initMultipartUploadResult.error.message)
				.append(initMultipartUploadResult.error.resource)
				.append(initMultipartUploadResult.error.requestId)
				.append(initMultipartUploadResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//请求成功
	if(initMultipartUploadResult.getHttpCode() >= 200 && initMultipartUploadResult.getHttpCode() < 300){
		
		uploadId =initMultipartUploadResult.initMultipartUpload.uploadId;
		Log.w("TEST","请求成功");
	}

  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}

//**使用异步回调请求**
/**

cosXmlService.initMultipartUploadAsync(initMultipartUploadRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {

      	 uploadId =initMultipartUploadResult.initMultipartUpload.uploadId;
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```

### 上传分片

调用此接口实现分块上传，支持的块的数量为 1 到 10000，块的大小为 1 MB 到 5 GB。具体步骤如下：
1. 调用 `UploadPartRequest()`构造方法，实例化 UploadPartRequest 对象。
2. 调用 CosXmlService 的 uploadPart 方法，传入 UploadPartRequest，返回 UploadPartResult 对象。
   （或者调用 uploadPartAsync 方法，传入 UploadPartRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的uploadId   |String           | 是  |
| partNumber   |分片块的编号，从 1 开始起| int           | 是  |
| srcPath   | 本地文件的绝对路径   |String           | 是  |
| fileOffset   | 该分片在文件的中起始位置   |long           | 是  |
| contentLength   | 该分片的内容大小 |long           | 否  |
| signDuration    | 签名的有效期，单位为秒 |long           | 否  |
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| qCloudProgressListener   | 上传进度回调     |QCloudProgressListener          | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 UploadPartResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | ------ |
| error  |  [请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     |COSXMLError             |
| eTag   |  请求成功,返回分片文件的 MD5 值，用于最后完成分片|String          |

#### 示例
```java
UploadPartRequest uploadPartRequest = new UploadPartRequest();
uploadPartRequest.setBucket(bucket);
uploadPartRequest.setCosPath(cosPath);
uploadPartRequest.setUploadId(uploadId);
uploadPartRequest.setPartNumber(partNumber); //此次上传分片的编号，从 1 开始
uploadPartRequest.setSrcPath(srcPath, fileOffset, contentLength); //fileOffset 该分片的起始位置，contentLength 该分片的大小
uploadPartRequest.setSign(signDuration,null,null);
uploadPartRequest.setProgressListener(new QCloudProgressListener() {
    @Override
    public void onProgress(long progress, long max) {
        float result = (float) (progress * 100.0/max);
        Log.w("TEST","progress =" + (long)result + "%");
    }
});

String eTag = null;

//使用同步方法上传
try {
    UploadPartResult uploadPartResult = cosXmlService.uploadPart(uploadPartRequest);
	
	//上传失败， 返回 httpCode 不在【200，300）之内；
	if(uploadPartResult.getHttpCode() >= 300 || uploadPartResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(uploadPartResult.error.code)
				.append(uploadPartResult.error.message)
				.append(uploadPartResult.error.resource)
				.append(uploadPartResult.error.requestId)
				.append(uploadPartResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//上传成功
	if(uploadPartResult.getHttpCode() >= 200 && uploadPartResult.getHttpCode() < 300){
		
		eTag =uploadPartResult.getETag();
		Log.w("TEST","请求成功");
	}
       

  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}

//**使用异步回调请求**
/**

cosXmlService.uploadPartAsync(uploadPartRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {

      	 eTag =result.getETag();
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```

### 完成整个分片上传

当上传完所有分块以后，必须调用此接口用来实现完成整个分块上传。具体步骤如下：
1. 调用 `CompleteMultiUploadRequest()`构造方法，实例化 CompleteMultiUploadRequest 对象。
2. 调用 CosXmlService 的 completeMultiUpload 方法，传入 CompleteMultiUploadRequest，返回 CompleteMultiUploadResult 对象。
   （或者调用 completeMultiUploadAsync 方法，传入 CompleteMultiUploadRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | ------ | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的 uploadId   |String           | 是  |
| partNumberAndETag    |分片编号 和对应的分片 MD5 值  | Map&lt;Integer,String>           | 是  | 
| signDuration    | 签名的有效期，单位为秒   |long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 CompleteMultiUploadResult 对象的成员变量返回请求结果。

| 成员变量名称 | 类型     | 变量说明    |
| ---- | -------------- | ------ | 
| error  |[请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     | COSXMLError             | 
| completeMultipartUpload   |  [请求成功的返回结果](https://cloud.tencent.com/document/product/436/7742)|CompleteMultipartResult          |
| accessUrl   | 请求成功时，返回访问文件的地址|String          | 

#### 示例
```java
CompleteMultiUploadRequest completeMultiUploadRequest = new CompleteMultiUploadRequest();
completeMultiUploadRequest.setBucket(bucket);
completeMultiUploadRequest.setCosPath(cosPath);
completeMultiUploadRequest.setUploadId(uploadId);
completeMultiUploadRequest.setPartNumberAndETag(partNumberAndETag);
completeMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法请求
try {
    CompleteMultiUploadResult completeMultiUploadResult = cosXmlService.completeMultiUpload(completeMultiUploadRequest);
	
	//请求失败， 返回 httpCode 不在【200，300）之内；
	if(completeMultiUploadRequest.getHttpCode() >= 300 || completeMultiUploadRequest.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(completeMultiUploadRequest.error.code)
				.append(completeMultiUploadRequest.error.message)
				.append(completeMultiUploadRequest.error.resource)
				.append(completeMultiUploadRequest.error.requestId)
				.append(completeMultiUploadRequest.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//请求成功
	if(completeMultiUploadRequest.getHttpCode() >= 200 && completeMultiUploadRequest.getHttpCode() < 300){
		
		String accessUrl =completeMultiUploadResult.accessUrl;
		Log.w("TEST","请求成功 " + completeMultiUploadResult.completeMultipartUpload.toString());
	}
       

  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}


//**使用异步回调请求**
/**

cosXmlService.completeMultiUploadAsync(completeMultiUploadRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {
		String accessUrl =completeMultiUploadResult.accessUrl;
		Log.w("TEST","请求成功 " + completeMultiUploadResult.completeMultipartUpload.toString());
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```

### 列举已上传的分片

调用此接口用来查询特定分块上传中的已上传的块，即罗列出指定 UploadId 所属的所有已上传成功的分块。
1. 调用 `ListPartsRequest()` 构造方法，实例化 ListPartsRequest 对象。
2. 调用 CosXmlService 的 listParts 方法，传入 ListPartsRequest，返回 ListPartsResult 对象。
   （或者调用 listPartsAsync 方法，传入 ListPartsRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的 uploadId   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   | long           | 是  |
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 ListPartsResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | ------- |
| error  |  [请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     |COSXMLError             |
| listParts  | [请求成功返回的结果](https://cloud.tencent.com/document/product/436/7747)     | ListParts             |


#### 示例
```java
ListPartsRequest listPartsRequest = new ListPartsRequest();
listPartsRequest.setBucket(bucket);
listPartsRequest.setCosPath(cosPath);
listPartsRequest.setUploadId(uploadId);
listPartsRequest.setSign(signDuration,null,null);

//使用同步方法请求
try {
    ListPartsResult listPartsResult = cosXmlService.listParts(listPartsRequest);
	
	//请求失败， 返回httpCode 不在【200，300）之内；
	if(listPartsResult.getHttpCode() >= 300 || listPartsResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(listPartsResult.error.code)
				.append(listPartsResult.error.message)
				.append(listPartsResult.error.resource)
				.append(listPartsResult.error.requestId)
				.append(listPartsResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//请求成功
	if(listPartsResult.getHttpCode() >= 200 && listPartsResult.getHttpCode() < 300){
		
		Log.w("TEST","请求成功  " + listPartsResult.listParts.toString());
	}
       
  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}

//**使用异步回调请求**
/**

cosXmlService.listPartsAsync(listPartsRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","请求成功 " + listPartsResult.listParts.toString());
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```

### 舍弃并删除已上传的分片
调用此接口用来用来实现舍弃一个分块上传并删除已上传的块。
1. 调用 `AbortMultiUploadRequest()` 构造方法，实例化 AbortMultiUploadRequest 对象。
2. 调用 CosXmlService 的 abortMultiUpload 方法，传入 AbortMultiUploadRequest，返回 AbortMultiUploadResult 对象。
   （或者调用 abortMultiUploadAsync 方法，传入 AbortMultiUploadRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | ------- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的 uploadId   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   |long           | 是  | 
| checkHeaderListForSign    |签名中需要验证的请求头    | Set&lt;String>           | 否  | 
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 AbortMultiUploadResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ------- | -------------- | -------- | 
| error  |  [请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     |COSXMLError             |
| httpCode  | [请求成功返回的结果](https://cloud.tencent.com/document/product/436/7740)     | int             |


#### 示例
```java
AbortMultiUploadRequest abortMultiUploadRequest = new AbortMultiUploadRequest();
abortMultiUploadRequest.setBucket(bucket);
abortMultiUploadRequest.setCosPath(cosPath);
abortMultiUploadRequest.setUploadId(uploadId);
abortMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法请求
try {
    AbortMultiUploadResult abortMultiUploadResult = cosXmlService.abortMultiUpload(abortMultiUploadRequest);
	
	//请求失败， 返回 httpCode 不在【200，300）之内；
	if(abortMultiUploadResult.getHttpCode() >= 300 || abortMultiUploadResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(abortMultiUploadResult.error.code)
				.append(abortMultiUploadResult.error.message)
				.append(abortMultiUploadResult.error.resource)
				.append(abortMultiUploadResult.error.requestId)
				.append(abortMultiUploadResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//请求成功
	if(abortMultiUploadResult.getHttpCode() >= 200 && abortMultiUploadResult.getHttpCode() < 300){
		
		Log.w("TEST","请求成功  ");
	}
       
  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}

//**使用异步回调请求**
/**

cosXmlService.abortMultiUploadAsync(abortMultiUploadRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","请求成功 ");
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```


## 删除文件

### 删除单个文件

调用此接口可以在指定的存储桶中将一个文件删除。具体步骤如下：
1. 调用 `DeleteObjectRequest()` 构造方法，实例化 DeleteObjectRequest 对象。
2. 调用 CosXmlService 的 completeMultiUpload 方法，传入 DeleteObjectRequest，返回 DeleteObjectResult 对象。
   （或者调用 deleteObjectAsync 方法，传入 DeleteObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | ---------------- | ------- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   | long           | 是  |
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 DeleteObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | ---------- |
| error  |  [请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     |COSXMLError             |
| httpCode  | [请求成功返回的结果](https://cloud.tencent.com/document/product/436/7743)     |int             | 


#### 示例
```java
DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest();
deleteObjectRequest.setBucket(bucket);
deleteObjectRequest.setCosPath(cosPath);
completeMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法删除
try {
    DeleteObjectResult deleteObjectResult = cosXmlService.deleteObject(deleteObjectRequest);
	
	//删除失败， 返回 httpCode 不在【200，300）之内；
	if(deleteObjectResult.getHttpCode() >= 300 || deleteObjectResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(deleteObjectResult.error.code)
				.append(deleteObjectResult.error.message)
				.append(deleteObjectResult.error.resource)
				.append(deleteObjectResult.error.requestId)
				.append(deleteObjectResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//删除成功
	if(deleteObjectResult.getHttpCode() >= 200 && deleteObjectResult.getHttpCode() < 300){
		
		Log.w("TEST","请求成功 ");
	}
       

  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}

//**使用异步回调请求**
/**

cosXmlService.deleteObjectAsync(deleteObjectRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","请求成功 ");
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```

### 删除多个文件

调用此接口可以在指定存储桶中批量删除文件，单次请求最大支持批量删除 1000 个 文件。具体步骤如下：
1. 调用 `DeleteMultiObjectRequest()` 构造方法，实例化 DeleteMultiObjectRequest 对象。
2. 调用 CosXmlService 的 deleteMultiObject 方法，传入 DeleteMultiObjectRequest，返回 DeleteMultiObjectResult 对象。
   （或者调用 deleteMultiObjectAsync 方法，传入 DeleteMultiObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | ------ | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| quiet   | true：只返回删除报错的文件信息； false：返回每个文件的删除结果  |boolean           | 是  |
| objectList   | 需要删除的文件路径列表|List&lt;String> | 是  |
| signDuration    | 签名的有效期，单位为秒   | long           | 是  |
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 DeleteMultiObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 | 类型     | 变量说明    |
| ----- | -------------- | ----------- | 
| error  | [请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     |COSXMLError             | 
| httpCode  |[请求成功返回的结果](https://cloud.tencent.com/document/product/436/7743)     | int             | 


#### 示例
```java
DeleteMultiObjectRequest deleteMultiObjectRequest = new DeleteMultiObjectRequest();
deleteMultiObjectRequest.setBucket(bucket);
deleteMultiObjectRequest.setQuiet(quiet);
deleteMultiObjectRequest.setObjectList(objectList); // 每个文件均是绝对路径，如 /2/test.txt;
completeMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法删除
try {
   DeleteMultiObjectResult deleteMultiObjectResult =cosXmlService.deleteMultiObject(DeleteMultiObjectRequest);
	
	//删除失败， 返回 httpCode 不在【200，300）之内；
	if(deleteMultiObjectResult.getHttpCode() >= 300 || deleteMultiObjectResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(deleteMultiObjectResult.error.code)
				.append(deleteMultiObjectResult.error.message)
				.append(deleteMultiObjectResult.error.resource)
				.append(deleteMultiObjectResult.error.requestId)
				.append(deleteMultiObjectResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//删除成功
	if(deleteMultiObjectResult.getHttpCode() >= 200 && deleteMultiObjectResult.getHttpCode() < 300){
		
		Log.w("TEST","删除成功： " + deleteMultiObjectResult.deleteResult.toString());
		
	}
       

  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}


//**使用异步回调请求**
/**

cosXmlService.deleteMultiObjectAsync(DeleteMultiObjectResult, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","删除成功： " + deleteMultiObjectResult.deleteResult.toString());
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```

## 下载文件

调用此接口将指定存储桶中的一个文件下载至本地。具体步骤如下：
1. 调用 `GetObjectRequest(String)`构造方法，实例化 GetObjectRequest 对象。
2. 调用 CosXmlService 的 getObject 方法，传入 GetObjectRequest，返回 GetObjectResult 对象。
   （或者调用 getObjectAsync 方法，传入 GetObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   | 类型 | 必填 |
| -------- | --------------- | ------ | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   |远端路径，即存储到cos上的绝对路径   | String           | 是  |
| savaPath   |文件下载到本地文件夹的绝对路径|String | 否  |
| start   |请求文件的开始位置|long | 否  |
| end   |请求文件的结束位置|long | 否  |
| signDuration    |签名的有效期，单位为秒   | long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| qCloudProgressListener   |  下载进度回调     |QCloudProgressListener          | 否  |
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 GetObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ----- | --------------- | --- |
| error  | [请求失败的返回结果](https://cloud.tencent.com/document/product/436/7730)     |COSXMLError             | 
| httpCode  |  [请求成功返回的结果](https://cloud.tencent.com/document/product/436/7753)     |int             |


#### 示例
```java
GetObjectRequest getObjectRequest = GetObjectRequest(**savePath**);
getObjectRequest.setBucket(bucket);
getObjectRequest.setCosPath(cosPath);
getObjectRequest.setSign(signDuration,null,null);
getObjectRequest.setProgressListener(new QCloudProgressListener() {
    @Override
    public void onProgress(long progress, long max) {
        float result = (float) (progress * 100.0/max);
        Log.w("TEST","progress =" + (long)result + "%");
    }
});

//使用同步方法下载
try {
   GetObjectResult getObjectResult =cosXmlService.getObject(getObjectRequest);
	
	//下载失败， 返回 httpCode 不在【200，300）之内；
	if(getObjectResult.getHttpCode() >= 300 || getObjectResult.getHttpCode() < 200){
		StringBuilder stringBuilder = new StringBuilder("Error\n");
		stringBuilder.append(getObjectResult.error.code)
				.append(getObjectResult.error.message)
				.append(getObjectResult.error.resource)
				.append(getObjectResult.error.requestId)
				.append(getObjectResult.error.traceId);
		Log.w("TEST",stringBuilder.toString());
	}

	//下载成功
	if(getObjectResult.getHttpCode() >= 200 && getObjectResult.getHttpCode() < 300){
		
		Log.w("TEST","下载成功： " + getObjectResult.xCOSStorageClass);
		
	}
       
  } catch (QCloudException e) {

	   //抛出异常
       Log.w("TEST","exception =" + e.getExceptionType() + "; " + e.getDetailMessage());
}

//**使用异步回调请求**
/**

cosXmlService.getObjectAsync(getObjectRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","下载成功： " + getObjectResult.xCOSStorageClass);
     }

     @Override
     public void onFail(CosXmlRequest request, CosXmlResult result) {
         StringBuilder stringBuilder = new StringBuilder("Error\n");
		 stringBuilder.append(result.error.code)
				.append(result.error.message)
				.append(result.error.resource)
				.append(result.error.requestId)
				.append(result.error.traceId);
		Log.w("TEST",stringBuilder.toString());
    }
});

*/
```

