## 初始化
进行操作之前需要实例化 CosXmlService 和 CosXmlServiceConfig。
> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

### 实例化 CosXmlServiceConfig
调用 CosXmlServiceConfig.Builder().build() 实例化 CosXmlServiceConfig 对象。

#### 参数说明
| 参数名称   |参数描述   | 类型 |必填 | 
| -------------- | -------------- | -- | ----------- |
| appid           |  对象存储的服务 APPID |String          | 是  |
| region          | 存储桶 所在的地域 |String          | 是  | 


#### 其它配置设置方法
|   方法   |     方法描述   |
|----------|-----------|
|   setAppidAndRegion(String, String) |设置 appid 和 bucket 所属地域   |
|   isHttps(boolean)  | true：https请求； false：http请求； 默认 http 请求|
|   setConnectionTimeout(int) |     连接超时设置   |
|   setSocketTimeout(int)   |     读写超时设置   |
|   setMaxRetryCount(int)  |     失败请求重试次数   |


#### 示例
```java
String appid = "对象存储的服务 APPID";
String region = "存储桶所在的地域"; //所属地域：在创建好存储桶后，可通过对象存储控制台查看
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
       .setAppidAndRegion(appid, region)
       .setDebuggable(true)
       .setConnectionTimeout(45000)
       .setSocketTimeout(30000)
       .build();
```

### 实例化 CosXmlService
调用 `CosXmlService(Context context, CosXmlServiceConfig serviceConfig, CosXmlCredentialProvider cloudCredentialProvider)` 构造方法，实例化 CosXmlService 对象。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------------- | -------------- | -- | ----------- |
| context         | application 上下文 | Context         | 是  |
| serviceConfig   |  SDK 的配置设置类 |CosXmlServiceConfig    | 是  |
| basicLifecycleCredentialProvider   |服务请求的签名获取类 | BasicLifecycleCredentialProvider   | 是  | 

#### 示例
```java
String appid = "对象存储的服务 APPID";
String region = "存储桶所在的地域"; 

//创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
       .setAppidAndRegion(appid, region)
       .setDebuggable(true)
       .setConnectionTimeout(45000)
       .setSocketTimeout(30000)
       .build();

/**
* 
* 创建 LocalCredentialProvider 签名获取类对象，用于使用对象存储服务时计算签名. 
* 参考 SDK 提供签名格式，可实现自己的签名方法(extends BasicLifecycleCredentialProvider 以及实现       * * fetchNewCredentials() 方法).
* 此处使用SDK提供的默认签名计算方法.
*
*/
String secretId = "云 API 密钥 secretId";
String secretKey ="云 API 密钥 secretKey";
long keyDuration = 600; //secretKey 的有效时间,单位秒
LocalCredentialProvider localCredentialProvider = new LocalCredentialProvider(secretId, secretKey, keyDuration);

//创建 CosXmlService 对象，实现对象存储服务各项操作.
Context context = getApplicationContext()； //应用的上下文
CosXmlService cosXmlService = new CosXmlService(context,cosXmlServiceConfig, localCredentialProvider);

```

## 生成签名

签名具体的生成和使用请参照 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文章。SDK 中已提供了签名获取类，用户只需要继承 BasicLifecycleCredentialProvider 类，并重写 fetchNewCredentials() 方法。

#### 示例
```java
public class LocalCredentialProvider extends BasicLifecycleCredentialProvider{
    private String secretKey;
    private long keyDuration;
    private String secretId;

     public LocalCredentialProvider(String secretId, String secretKey, long keyDuration) {
        this.secretId = secretId;
        this.secretKey = secretKey;
        this.keyDuration = keyDuration;
     }

     @Override
     public QCloudLifecycleCredentials fetchNewCredentials() throws CosXmlClientException {
         long current = System.currentTimeMillis() / 1000L;
         long expired = current + duration;
         String keyTime = current+";"+expired;
         return new BasicQCloudCredentials(secretId, secretKeyToSignKey(secretKey, keyTime), keyTime);
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
1. 调用 `PutObjectRequest（String, String, String）` 构造方法，实例化 PutObjectRequest 对象。
2. 调用 CosXmlService 的 putObject 方法，传入 PutObjectRequest，返回 PutObjectResult 对象。
   （或者调用 putObjectAsync 方法，传入 PutObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| srcPath   | 本地文件的绝对路径   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   |Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| qCloudProgressListener   | 上传进度回调     |QCloudProgressListener          | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 PutObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- |----------- |
| accessUrl   |  请求成功时，返回访问文件的地址|String          |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";
String srcPath = "本地文件的绝对路径";

PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);
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
	
	Log.w("TEST","success: " + putObjectResult.accessUrl);

  } catch (CosXmlClientException e) {

	   //抛出异常
       Log.w("TEST","CosXmlClientException =" + e.toString());
  } catch (CosXmlServiceException e) {

	   //抛出异常
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调上传**
/**

cosXmlService.putObjectAsync(putObjectRequest, new CosXmlResultListener() {
     @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});
*/
```


## 分片上传

### 初始化分片

调用此接口实现初始化分片上传，成功执行此请求以后会返回 UploadId 用于后续的 Upload Part 请求。具体步骤如下：
1. 调用 `InitMultipartUploadRequest（String, String）`构造方法，实例化 InitMultipartUploadRequest 对象。
2. 调用 CosXmlService 的 initMultipartUpload 方法，传入 InitMultipartUploadRequest，返回 InitMultipartUploadResult 对象。
   （或者调用 initMultipartUploadAsync 方法，传入 InitMultipartUploadRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 InitMultipartUploadResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | --------------  | ----------- |
| initMultipartUpload   |[请求成功的返回结果](https://cloud.tencent.com/document/product/436/7746)| InitMultipartUpload          |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";

InitMultipartUploadRequest initMultipartUploadRequest = new InitMultipartUploadRequest(bucket, cosPath);
initMultipartUploadRequest.setSign(signDuration,null,null);

String uploadId = null;

//使用同步方法请求
try {
    InitMultipartUploadResult initMultipartUploadResult = cosXmlService.initMultipartUpload(initMultipartUploadRequest);
	
    Log.w("TEST","success");
	uploadId =initMultipartUploadResult.initMultipartUpload.uploadId;

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.initMultipartUploadAsync(initMultipartUploadRequest, new CosXmlResultListener() {
       @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
		uploadId = ((InitMultipartUploadResult)cosXmlResult).initMultipartUpload.uploadId;
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

### 上传分片

调用此接口实现分块上传，支持的块的数量为 1 到 10000，块的大小为 1 MB 到 5 GB。具体步骤如下：
1. 调用 `UploadPartRequest（String, String, int, String, String）` 构造方法，实例化 UploadPartRequest 对象.
2. 调用 CosXmlService 的 uploadPart 方法，传入 UploadPartRequest，返回 UploadPartResult 对象。
   （或者调用 uploadPartAsync 方法，传入 UploadPartRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的 uploadId   |String           | 是  |
| partNumber   |分片块的编号，从 1 开始起| Int           | 是  |
| srcPath   | 本地文件的绝对路径   |String           | 是  |
| fileOffset   |该分片在文件的中起始位置   | Long           | 否  |
| contentLength   | 该分片的内容大小 |Long           | 否  |
| signDuration    |签名的有效期，单位为秒 | Long           | 否  |
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| qCloudProgressListener   |上传进度回调     | QCloudProgressListener          | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 

#### 返回结果说明
通过 UploadPartResult 对象的成员变量返回请求结果。

| 成员变量名称 | 类型     | 变量说明    |
| ---- | --------------  | ----------- |
| eTag   | 请求成功，返回分片文件的 MD5 值，用于最后完成分片|String          | 
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = "初始化分片返回的 uploadId";
int partNumber = 1;//此次上传分片的编号，从 1 开始
String srcPath = "本地文件的绝对路径";

UploadPartRequest uploadPartRequest = new UploadPartRequest(bucket, cosPath, partNumber, srcPath, uploadId);
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
    
    Log.w("TEST","success");
	eTag =uploadPartResult.getETag();
	
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**使用异步回调请求**
/**

cosXmlService.uploadPartAsync(uploadPartRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
        eTag =((UploadPartResult)cosXmlResult).getETag();
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

### 完成整个分片上传

当上传完所有分块以后，必须调用此接口用来实现完成整个分块上传。具体步骤如下：
1. 调用 `CompleteMultiUploadRequest（String, String, String, Map<Integer, String>）`构造方法，实例化 CompleteMultiUploadRequest 对象。
2. 调用 CosXmlService 的 completeMultiUpload 方法，传入 CompleteMultiUploadRequest，返回 CompleteMultiUploadResult 对象。
   （或者调用 completeMultiUploadAsync 方法，传入 CompleteMultiUploadRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的 uploadId   |String           | 是  |
| partNumberAndETag    | 分片编号 和对应的分片 MD5 值  |Map&lt;Integer,String>           | 是  | 
| signDuration    | 签名的有效期，单位为秒   | Long           | 是  |
| checkHeaderListForSign    |签名中需要验证的请求头    | Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   |上传结果回调     | CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 CompleteMultiUploadResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | -------------- | ----------- |
| completeMultipartUpload   |  [请求成功的返回结果](https://cloud.tencent.com/document/product/436/7742)|CompleteMultipartResult          |
| accessUrl   |  请求成功时，返回访问文件的地址|String          |

#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = "初始化分片返回的 uploadId";
int partNumber = 1;
String etag = "编号为 partNumber 对应分片上传结束返回的 etag ";
Map<Integer, String> partNumberAndETag = new HashMap<>();
partNumberAndETag.put(partNumber, etag);

CompleteMultiUploadRequest completeMultiUploadRequest = new CompleteMultiUploadRequest(bucket, cosPath, uploudId, 

partNumberAndETag);
completeMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法请求
try {
    CompleteMultiUploadResult completeMultiUploadResult = cosXmlService.completeMultiUpload(completeMultiUploadRequest);
	
	Log.w("TEST","success: "+ completeMultiUploadResult.completeMultipartUpload.toString()());
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.completeMultiUploadAsync(completeMultiUploadRequest, new CosXmlResultListener() {
     @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

### 列举已上传的分片

调用此接口用来查询特定分块上传中的已上传的块，即罗列出指定 UploadId 所属的所有已上传成功的分块。
1. 调用` ListPartsRequest（String, String, String）`构造方法，实例化 ListPartsRequest 对象。
2. 调用 CosXmlService 的 listParts 方法，传入 ListPartsRequest，返回 ListPartsResult 对象。
   （或者调用 listPartsAsync 方法，传入 ListPartsRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的 uploadId   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 

#### 返回结果说明
通过 ListPartsResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | --------------  | ----------- |
| listParts  | [请求成功返回的结果](https://cloud.tencent.com/document/product/436/7747)     | ListParts             |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = "初始化分片返回的 uploadId";

ListPartsRequest listPartsRequest = new ListPartsRequest(bucket, cosPath, uploadId);
listPartsRequest.setSign(signDuration,null,null);

//使用同步方法请求
try {
    ListPartsResult listPartsResult = cosXmlService.listParts(listPartsRequest);
	
    Log.w("TEST","success: " + listPartsResult.listParts.toString());
       
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.listPartsAsync(listPartsRequest, new CosXmlResultListener() {
       @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

### 舍弃并删除已上传的分片
调用此接口用来用来实现舍弃一个分块上传并删除已上传的块。
1. 调用 `AbortMultiUploadRequest（String, String, String）`构造方法，实例化 AbortMultiUploadRequest 对象。
2. 调用 CosXmlService 的 abortMultiUpload 方法，传入 AbortMultiUploadRequest，返回 AbortMultiUploadResult 对象。
   （或者调用 abortMultiUploadAsync 方法，传入 AbortMultiUploadRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   | 参数描述   | 类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| uploadId    | 初始化分片上传，返回的 uploadId   |String           | 是  |
| signDuration    |  签名的有效期，单位为秒   |Long           | 是  |
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 AbortMultiUploadResult 对象的成员变量返回请求结果。

| 成员变量名称 |变量说明    | 类型     | 
| ---- | -------------- | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java
String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = "初始化分片返回的 uploadId";

AbortMultiUploadRequest abortMultiUploadRequest = new AbortMultiUploadRequest(bucket, cosPath, uploadId);
abortMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法请求
try {
    AbortMultiUploadResult abortMultiUploadResult = cosXmlService.abortMultiUpload(abortMultiUploadRequest);
	Log.w("TEST", "success");
       
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**使用异步回调请求**
/**

cosXmlService.abortMultiUploadAsync(abortMultiUploadRequest, new CosXmlResultListener() {
     @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 删除文件

### 删除单个文件

调用此接口可以在指定的 Bucket 中将一个文件删除。具体步骤如下：
1. 调用 `DeleteObjectRequest（String, String)` 构造方法，实例化 DeleteObjectRequest 对象。
2. 调用 CosXmlService 的 completeMultiUpload 方法，传入 DeleteObjectRequest，返回 DeleteObjectResult 对象。
   （或者调用 deleteObjectAsync 方法，传入 DeleteObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   |远端路径，即存储到 COS 上的绝对路径   | String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      | Set&lt;String>           | 否  |
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 DeleteObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";

DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(bucket, cosPath);
completeMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法删除
try {
    DeleteObjectResult deleteObjectResult = cosXmlService.deleteObject(deleteObjectRequest);
    Log.w("TEST","success ");

  } catch (CosXmlClientException e) {
      Log.w("TEST","CosXmlClientException =" + e.toString());
   } catch (CosXmlServiceException e) {
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.deleteObjectAsync(deleteObjectRequest, new CosXmlResultListener() {
     @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

### 删除多个文件

调用此接口可以在指定存储桶中批量删除文件，单次请求最大支持批量删除 1000 个 文件。具体步骤如下：
1. 调用 DeleteMultiObjectRequest（String, List&lt;String>）构造方法，实例化 DeleteMultiObjectRequest 对象。
2. 调用 CosXmlService 的 deleteMultiObject 方法，传入 DeleteMultiObjectRequest，返回 DeleteMultiObjectResult 对象。
   （或者调用 deleteMultiObjectAsync 方法，传入 DeleteMultiObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| quiet   | true：只返回删除报错的文件信息； false：返回每个文件的删除结果  |Boolean           | 是  |
| objectList   | 需要删除的文件路径列表|List&lt;String> | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 

#### 返回结果说明
通过 DeleteMultiObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java

String bucket = "bucket";
List<String> objectList = new ArrayList<String>();
objectList.add("/2/test.txt");

DeleteMultiObjectRequest deleteMultiObjectRequest = new DeleteMultiObjectRequest();
deleteMultiObjectRequest.setQuiet(quiet);
completeMultiUploadRequest.setSign(signDuration,null,null);

//使用同步方法删除
try {
   DeleteMultiObjectResult deleteMultiObjectResult =cosXmlService.deleteMultiObject(deleteMultiObjectRequest);
	
   Log.w("TEST","success： " + deleteMultiObjectResult.deleteResult.toString());
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.deleteMultiObjectAsync(deleteMultiObjectRequest, new CosXmlResultListener() {
     @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 下载文件

调用此接口将指定Bucket 中的一个文件下载至本地。具体步骤如下：
1. 调用 `GetObjectRequest（String, String, String）` 构造方法，实例化 GetObjectRequest 对象。
2. 调用 CosXmlService 的 getObject 方法，传入 GetObjectRequest，返回 GetObjectResult 对象。
   （或者调用 getObjectAsync 方法，传入 GetObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |参数描述   | 类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath   | 远端路径，即存储到 COS 上的绝对路径   |String           | 是  |
| savaPath   |文件下载到本地文件夹的绝对路径|String | 是  |
| start   |请求文件的开始位置|Long | 否  |
| end   |请求文件的结束位置|Long | 否  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| qCloudProgressListener   | 下载进度回调     |QCloudProgressListener          | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 

#### 返回结果说明
通过 GetObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";
String savePath = "savePath";

GetObjectRequest getObjectRequest = GetObjectRequest(bucket, cosPath, savePath);

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
	
	Log.w("TEST","success： " + getObjectResult.xCOSStorageClass);
       
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.getObjectAsync(getObjectRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 复制对象

调用此接口实现将一个文件从源路径复制到目标路径，建议文件大小 1 M 到 5 G，超过 5 G 的文件请使用分块上传 Upload - Copy 。具体步骤如下：
1. 调用 `CopyObjectRequest（String，String, CopySourceStruct）`构造方法，实例化 CopyObjectRequest 对象。
2. 调用 CosXmlService 的 copyObject 方法，传入 CopyObjectRequest，返回 CopyObjectResult 对象。
   （或者调用 copyObjectAsync 方法，传入 CopyObjectRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| cosPath    | 目标路径，即存储到 COS 上的绝对路径  |String           | 是  |
| copySourceStruct    | 源路径结构体  |CopySourceStruct           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 CopyObjectResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    | 类型     |
| ---- | -------------- | ----------- |
|copyObject |返回复制结果信息 | CopyObject| 
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java

String bucket = "bucket";
String cosPath = "cosPath";
CopyObjectRequest.CopySourceStruct copySourceStruct = new CopyObjectRequest.CopySourceStruct("源文件的appid",
"源文件的bucket", "源文件的region", "源文件的cosPath");

CopyObjectRequest copyObjectRequest = new CopyObjectRequest(bucket, cosPath, copySourceStruct);
copyObjectRequest.setSign(signDuration,null,null);

//使用同步方法
try {
    CopyObjectResult copyObjectResult = cosXmlService.copyObject(copyObjectRequest);
       //成功
	  Log.w("TEST","success:" + copyObjectResult.copyObject);

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.copyObjectAsync(copyObjectRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 创建一个 Bucket

调用此接口将在指定账号下创建一个 Bucket。具体步骤如下：
1. 调用 `PutBucketRequest(String)` 构造方法，实例化 PutBucketRequest 对象。
2. 调用 CosXmlService 的 putBucket 方法，传入 PutBucketRequest，返回 PutBucketResult 对象。
   （或者调用 putBucketAsync 方法，传入 PutBucketRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 PutBucketResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
PutBucketRequest putBucketRequest = new PutBucketRequest(bucket);
putBucketRequest.setSign(signDuration,null,null);

//定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private	
putBucketRequest.setXCOSACL("private");

//赋予被授权者读的权限
ACLAccounts readACLS = new ACLAccounts();
ACLAccount readAccount = new ACLAccount("OwnerUin", "SubUin");
readACLS.addACLAccount(readAccount);
putBucketRequest.setXCOSGrantRead(readACLS);

//赋予被授权者写的权限
ACLAccounts writeACLS = new ACLAccounts();
ACLAccount writeAccount = new ACLAccount("OwnerUin", "SubUin");
writeACLS.addACLAccount(writeAccount);
putBucketRequest.setXCOSGrantRead(writeACLS);

//赋予被授权者读写的权限
ACLAccounts writeandReadACLS = new ACLAccounts();
ACLAccount writeandReadAccount = new ACLAccount("OwnerUin", "SubUin");
writeandReadACLS.addACLAccount(writeandReadAccount);
putBucketRequest.setXCOSGrantRead(writeandReadACLS);

//使用同步方法
try {
    PutBucketResult putBucketResult = cosXmlService.putBucket(putBucketRequest);
       //成功
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.putBucketAsync(putBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

    @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 确认 Bucket 是否存在

调用此接口将确认指定存储桶是否存在。具体步骤如下：
1. 调用 HeadBucketRequest（String）构造方法，实例化 HeadBucketRequest 对象。
2. 调用 CosXmlService 的 headBucket 方法，传入 HeadBucketRequest，返回 HeadBucketResult 对象。
   （或者调用 headBucketAsync 方法，传入 HeadBucketRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   | 类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   |Long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 PutBucketResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
HeadBucketRequest headBucketRequest = new HeadBucketRequest(bucket);
headBucketRequest.setSign(signDuration,null,null);

//使用同步方法
try {
     HeadBucketResult headBucketResult = cosXmlService.headBucket(headBucketRequest);
       //成功
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.headBucketAsync(headBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 列举 Bucket 

调用此接口将列出该 Bucket 下的部分或者全部 Object。具体步骤如下：
1. 调用 `GetBucketRequest(String)` 构造方法，实例化 GetBucketRequest 对象。
2. 调用 CosXmlService 的 getBucket 方法，传入 GetBucketRequest，返回 GetBucketResult 对象。
   （或者调用 getBucketAsync 方法，传入 GetBucketRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   | Long           | 是  |
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 GetBucketResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | --------------  | ----------- |
| listBucket |保存 Get Bucket 请求结果的所有信息 | ListBucket | 
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java
GetBucketRequest getBucketRequest = new GetBucketRequest(bucket);
getBucketRequest.setSign(signDuration,null,null);

//前缀匹配，用来规定返回的文件前缀地址
getBucketRequest.setPrefix("prefix");

//单次返回最大的条目数量，默认 1000
getBucketRequest.setMaxKeys(100);

//定界符为一个符号，如果有 Prefix，
//则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，
//然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始
getBucketRequest.setDelimiter('c');

//使用同步方法
try {
     GetBucketResult getBucketResult = cosXmlService.getBucket(getBucketRequest);
       //成功
	  Log.w("TEST","success :" + getBucketResult.listBucket.toString());

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.getBucketAsync(getBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 删除 Bucket 

调用此接口可以在指定账号下删除 Bucket，删除之前要求 Bucket 内的内容为空，只有删除了 Bucket 内的信息，才能删除 Bucket 本身。具体步骤如下：
1. 调用 `DeleteBucketRequest(String)` 构造方法，实例化 DeleteBucketRequest 对象。
2. 调用 CosXmlService 的 deleteBucket 方法，传入 DeleteBucketRequest，返回 DeleteBucketResult 对象。
   （或者调用 deleteBucketAsync 方法，传入 DeleteBucketRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   | Long           | 是  |
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 DeleteBucketResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java
DeleteBucketRequest deleteBucketRequest = new DeleteBucketRequest(bucket);
deleteBucketRequest.setSign(signDuration,null,null);

//使用同步方法
try {
     DeleteBucketResult deleteBucketResult = cosXmlService.deleteBucket(deleteBucketRequest);
       //成功
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.deleteBucketAsync(deleteBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 设置 Bucket ACL

调用此接口可以指定 Bucket 的访问控制权限。具体步骤如下：
1. 调用 `PutBucketACLRequest(String)` 构造方法，实例化 PutBucketACLRequest 对象。
2. 调用 CosXmlService 的 putBucketACL 方法，传入 PutBucketACLRequest，返回 PutBucketACLResult 对象。
   （或者调用 putBucketACLAsync 方法，传入 PutBucketACLRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| xcosACL    | 设置 Bucket 访问权限，有效值为：private，public-read-write，public-read；默认值：private  |String           | 否  |
| xcosGrantRead    | 赋予被授权者读的权限   |ACLAccounts           | 否  |
| xcosGrantWrite    |赋予被授权者写的权限   | ACLAccounts           | 否  |
| xcosGrantRead    | 赋予被授权者读写的权限   |ACLAccounts           | 否  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    |签名中需要验证的请求头    | Set&lt;String>           | 否  | 
| checkParameterListForSing   |签名中需要验证的请求参数      | Set&lt;String>           | 否  | 
| cosXmlResultListener   |   上传结果回调     |CosXmlResultListener          |否  |
#### 返回结果说明
通过 DeleteBucketResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
PutBucketACLRequest putBucketACLRequest = new PutBucketACLRequest(bucket);
putBucketACLRequest.setSign(signDuration,null,null);

//设置 bucket 访问权限
putBucketACLRequest.setXCOSACL("public-read");

//设置赋予被授权者读的权限
ACLAccounts readAccounts = new ACLAccounts();
readAccounts.addACLAccount(new ACLAccount("OwnerUin", "OwnerUin or SubUin"));
putBucketACLRequest.setXCOSGrantRead(readAccounts);

//设置赋予被授权者写的权限
ACLAccounts writeAccounts = new ACLAccounts();
writeAccounts.addACLAccount(new ACLAccount("OwnerUin", "OwnerUin or SubUin"));
putBucketACLRequest.setXCOSGrantWrite(writeAccounts);

//设置赋予被授权者读写的权限
ACLAccounts readAndWriteAccounts = new ACLAccounts();
readAndWriteAccounts.addACLAccount(new ACLAccount("OwnerUin", "OwnerUin or SubUin"));
putBucketACLRequest.setXCOSReadWrite(readAndWriteAccounts)

//使用同步方法
try {
     PutBucketACLResult putBucketACLResult = cosXmlService.putBucketACL(putBucketACLRequest);
       //成功
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}


//**使用异步回调请求**
/**

cosXmlService.putBucketACLAsync(putBucketACLRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

    @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```
## 获取 Bucket ACL

调用此接口用来获取 Bucket 的 ACL。具体步骤如下：
1. 调用 `GetBucketACLRequest(String)` 构造方法，实例化 GetBucketACLRequest 对象。
2. 调用 CosXmlService 的 getBucketACL 方法，传入 GetBucketACLRequest，返回 GetBucketACLResult 对象。
   （或者调用 getBucketACLAsync 方法，传入 GetBucketACLRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   |Long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 GetBucketACLResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | -------------- | ----------- |
| accessControlPolicy  |  [被授权者信息与权限信息](https://cloud.tencent.com/document/product/436/7733)|AccessControlPolicy             |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
GetBucketACLRequest getBucketACLRequest = new DeleteBucketRequest(bucket);
getBucketACLRequest.setSign(signDuration,null,null);

//使用同步方法
try {
     GetBucketACLResult getBucketACLResult = cosXmlService.getBucketACL(getBucketACLRequest);
       //成功
	  Log.w("TEST","success: " +getBucketACLResult.accessControlPolicy.toString() );

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.getBucketACLAsync(getBucketACLRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

    @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```


## 设置跨域访问配置

调用此接口将指定 Bucket 中设置跨域访问配置信息。具体步骤如下：
1. 调用 `PutBucketCORSRequest（String）` 构造方法，实例化 PutBucketCORSRequest 对象。
2. 调用 CosXmlService 的 putBucketCORS 方法，传入 PutBucketCORSRequest，返回 PutBucketCORSResult 对象。
   （或者调用 putBucketCORSAsync 方法，传入 PutBucketCORSRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    |  存储桶名称   |String           |是|
| cORSRule    | 跨域访问配置信息   |CORSRule           | 是|
| signDuration    | 签名的有效期，单位为秒   | Long           | 是  |
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   |签名中需要验证的请求参数      | Set&lt;String>           | 否  | 
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 PutBucketCORSResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | -------------- | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
PutBucketCORSRequest putBucketCORSRequest = new PutBucketCORSRequest(bucket);

/**
cORSRule: 跨域访问配置信息
corsRule.id： 配置规则的 ID
cORSRule.allowedOrigin: 允许的访问来源，支持通配符 * , 格式为：协议://域名[:端口]如：http://www.qq.com
corsRule.maxAgeSeconds: 设置 OPTIONS 请求得到结果的有效期
corsRule.allowedMethod: 允许的 HTTP 操作，如：GET，PUT，HEAD，POST，DELETE
corsRule.allowedHeader：在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 *
corsRule.exposeHeader： 设置浏览器可以接收到的来自服务器端的自定义头部信息
*/
CORSRule corsRule = new CORSRule();

corsRule.id = "123";
corsRule.allowedOrigin = "https://cloud.tencent.com";
corsRule.maxAgeSeconds = "5000";

List<String> methods = new LinkedList<>();
methods.add("PUT");
methods.add("POST");
methods.add("GET");
corsRule.allowedMethod = methods;

List<String> headers = new LinkedList<>();
headers.add("host");
headers.add("content-type");
corsRule.allowedHeader = headers;

List<String> exposeHeaders = new LinkedList<>();
headers.add("x-cos-metha-1");
corsRule.exposeHeader = headers;

//设置跨域访问配置信息
putBucketCORSRequest.addCORSRule(corsRule);

putBucketCORSRequest.setSign(signDuration,null,null);

//使用同步方法
try {
   PutBucketCORSResult putBucketCORSResult = cosXmlService.putBucketCORS(putBucketCORSRequest);
       //成功
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.putBucketCORSAsync(putBucketCORSRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 获取跨域访问配置

调用此接口将指定 Bucket 中获取跨域访问配置信息。具体步骤如下：
1. 调用 `GetBucketCORSRequest(String)` 构造方法，实例化 GetBucketCORSRequest 对象。
2. 调用 CosXmlService 的 getBucketCORS 方法，传入 GetBucketCORSRequest，返回 GetBucketCORSResult 对象。
   （或者调用 getBucketCORSAsync 方法，传入 GetBucketCORSRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    | 签名的有效期，单位为秒   |Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      | Set&lt;String>           | 否  |
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 GetBucketCORSResult 对象的成员变量返回请求结果。

| 成员变量名称 | 类型     | 变量说明    |
| ---- | --------------  | ----------- |
| cORSConfiguration  |  [跨域资源共享配置的所有信息](https://cloud.tencent.com/document/product/436/8274)|CORSConfiguration             |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
GetBucketCORSRequest getBucketCORSRequest = new GetBucketCORSRequest(bucket);
getBucketCORSRequest.setSign(signDuration,null,null);

//使用同步方法
try {
    GetBucketCORSResult getBucketCORSResult = cosXmlService.getBucketCORS(getBucketCORSRequest);
       //成功
	  Log.w("TEST","success :" + getBucketCORSResult.corsConfiguration.toString());

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.getBucketCORSAsync(getBucketCORSRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

        GetBucketCORSResult getBucketCORSResult = (GetBucketCORSResult)result;
		Log.w("TEST","success:" + getBucketCORSResult.corsConfiguration.toString()););
     }

    @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 删除跨域访问配置

调用此接口将指定 Bucket 中删除跨域访问配置信息.具体步骤如下：
1. 调用 `DeleteBucketCORSRequest(String)` 构造方法，实例化 DeleteBucketCORSRequest 对象。
2. 调用 CosXmlService 的 deleteBucketCORS 方法，传入 DeleteBucketCORSRequest，返回 DeleteBucketCORSResult 对象 
   （或者调用 deleteBucketCORSAsync 方法，传入 DeleteBucketCORSRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 DeleteBucketCORSResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
DeleteBucketCORSRequest deleteBucketCORSRequest = new DeleteBucketCORSRequest(bucket);
deleteBucketCORSRequest.setSign(signDuration,null,null);

//使用同步方法
try {
   DeleteBucketCORSResult deleteBucketCORSResult = cosXmlService.deleteBucketCORS(deleteBucketCORSRequest);
       //成功
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.deleteBucketCORSAsync(deleteBucketCORSRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

   @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 获取 Bucket 地域信息

调用此接口用于获取 Bucket 所在的地域信息。具体步骤如下：
1. 调用 `GetBucketLocationRequest(String)` 构造方法，实例化 GetBucketLocationRequest 对象。
2. 调用 CosXmlService 的 getBucketLocation 方法，传入 GetBucketLocationRequest，返回 GetBucketLocationResult 对象。
   （或者调用 getBucketLocationAsync 方法，传入 GetBucketLocationRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    |  签名的有效期，单位为秒   |Long           | 是  |
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 GetBucketLocationResult 对象的成员变量返回请求结果。

| 成员变量名称 |变量说明    | 类型     | 
| ---- | --------------  | ----------- |
| region|  Bucket 所在区域 |String |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
GetBucketLocationRequest getBucketLocationRequest = new DeleteBucketCORSRequest(bucket);
getBucketLocationRequest.setSign(signDuration,null,null);

//使用同步方法
try {
   GetBucketLocationResult getBucketLocationResult = cosXmlService.getBucketLocation(getBucketLocationRequest);
       //成功
	  Log.w("TEST","success : " + getBucketLocationResult.region);

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.getBucketLocationAsync(getBucketLocationRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 设置 Bucket 生命周期

调用此接口用于获取 Bucket 所在的地域信息。具体步骤如下：
1. 调用 `PutBucketLifecycleRequest(String)` 构造方法，实例化 PutBucketLifecycleRequest 对象。
2. 调用 CosXmlService 的 putBucketLifecycle 方法，传入 PutBucketLifecycleRequest，返回 PutBucketLifecycleResult 对象。
   （或者调用 putBucketLifecycleAsync 方法，传入 PutBucketLifecycleRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| rule    | 生命周期配置规则 |Rule           | 是  |
| signDuration    | 签名的有效期，单位为秒   | Long           | 是  |
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 PutBucketLifecycleResult 对象的成员变量返回请求结果。

| 成员变量名称 |  变量说明    |类型     |
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
PutBucketLifecycleRequest putBucketLifecycleRequest = new PutBucketLifecycleRequest(bucket);
putBucketLifecycleRequest.setSign(signDuration,null,null);

//声明周期配置规则信息
Rule rule = new Rule();
rule.id = "Lifecycle ID";
Filter filter = new Filter();
filter.prefix = "prefix/";
rule.filter = filter;
rule.status = "Enabled or Disabled";
Transition transition = new Transition();
transition.days = 100;
transition.storageClass = COSStorageClass.NEARLINE.getStorageClass();
putBucketLifecycleRequest.setRuleList(rule);

//使用同步方法
try {
   PutBucketLifecycleResult putBucketLifecycleResult = cosXmlService.putBucketLifecycle(putBucketLifecycleRequest);
       //成功
	  Log.w("TEST","success : " + getBucketLocationResult.region);

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.putBucketLifecycleAsync(putBucketLifecycleRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

    @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 获取 Bucket 生命周期

调用此接口用于获取 Bucket 所在的地域信息。具体步骤如下：
1. 调用 `GetBucketLifecycleRequest(String)` 构造方法，实例化 GetBucketLifecycleRequest 对象。
2. 调用 CosXmlService 的 getBucketLifecycle 方法，传入 GetBucketLifecycleRequest，返回 GetBucketLifecycleResult 对象。
   （或者调用 getBucketLifecycleAsync 方法，传入 GetBucketLifecycleRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   |  签名中需要验证的请求参数      |Set&lt;String>           | 否  |
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 


#### 返回结果说明
通过 getBucketLifecycle 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | --------------  | ----------- |
|lifecycleConfiguration| 生命周期配置信息|LifecycleConfiguration| 
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
GetBucketLifecycleRequest getBucketLifecycleRequest = new DeleteBucketCORSRequest(bucket);
getBucketLifecycleRequest.setSign(signDuration,null,null);

//使用同步方法
try {
   GetBucketLifecycleResult getBucketLifecycleResult = cosXmlService.getBucketLifecycle(getBucketLifecycleRequest);
       //成功
	  Log.w("TEST","success : " + getBucketLifecycleResult.lifecycleConfiguration.toString());

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.getBucketLifecycleAsync(getBucketLifecycleResult, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 删除 Bucket 生命周期

调用此接口用于获取 Bucket 所在的地域信息。具体步骤如下：
1. 调用 `DeleteBucketLifecycleRequest(String)` 构造方法，实例化 DeleteBucketLifecycleRequest 对象。
2. 调用 CosXmlService 的 deleteBucketLifecycle 方法，传入 DeleteBucketLifecycleRequest，返回 DeleteBucketLifecycleResult 对象。
   （或者调用 deleteBucketLifecycleAsync 方法，传入 DeleteBucketLifecycleRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明
| 参数名称   |  参数描述   |类型 | 必填 |
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    |  签名中需要验证的请求头    |Set&lt;String>           | 否  |
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   | 上传结果回调     |CosXmlResultListener          | 否  | 

#### 返回结果说明
通过 DeleteBucketLifecycleResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    |类型     | 
| ---- | --------------  | ----------- |
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |

#### 示例
```java
DeleteBucketLifecycleRequest deleteBucketLifecycleRequest = new DeleteBucketCORSRequest(bucket);
deleteBucketLifecycleRequest.setSign(signDuration,null,null);

//使用同步方法
try {
   DeleteBucketLifecycleResult deleteBucketCORSResult = cosXmlService.deleteBucketLifecycle(deleteBucketLifecycleRequest);
       //成功
	  Log.w("TEST","success "）;

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.deleteBucketLifecycleAsync(deleteBucketLifecycleRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

    @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```

## 查询 Bucket 中正在上传的分块

调用此接口用于获取 Bucket 中正在进行中的分块上传，单次请求操作最多列出 1000 个正在进行中的分块上传。具体步骤如下：
1. 调用 `ListMultiUploadsRequest(String)` 构造方法，实例化 ListMultiUploadsRequest 对象。
2. 调用 CosXmlService 的 listMultiUploads 方法，传入 ListMultiUploadsRequest，返回 ListMultiUploadsResult 对象。
   （或者调用 listMultiUploadsAsync 方法，传入 ListMultiUploadsRequest 和 CosXmlResultListener 进行异步回调操作）。

#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------- | --------------- | -- | ----------- |
| bucket    | 存储桶名称   |String           | 是  |
| signDuration    |签名的有效期，单位为秒   | Long           | 是  | 
| checkHeaderListForSign    | 签名中需要验证的请求头    |Set&lt;String>           | 否  | 
| checkParameterListForSing   | 签名中需要验证的请求参数      |Set&lt;String>           | 否  | 
| cosXmlResultListener   |  上传结果回调     |CosXmlResultListener          | 否  |


#### 返回结果说明
通过 ListMultiUploadsResult 对象的成员变量返回请求结果。

| 成员变量名称 | 变量说明    | 类型     |
| ---- | --------------  | ----------- |
| listMultipartUploads |所有分块上传的信息 | ListMultipartUploads | 
| httpCode  |[200, 300)之间请求成功， 否则请求失败| Int             |


#### 示例
```java
ListMultiUploadsRequest listMultiUploadsRequest = new ListMultiUploadsRequest(bucket);
listMultiUploadsRequest.setSign(signDuration,null,null);

//使用同步方法
try {
   ListMultiUploadsResult listMultiUploadsResult = cosXmlService.listMultiUploads(listMultiUploadsRequest);
       //成功
	  Log.w("TEST","success： " + listMultiUploadsResult.listMultipartUploads.toString()）;

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**使用异步回调请求**
/**

cosXmlService.listMultiUploadsAsync(listMultiUploadsRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {

		Log.w("TEST","success");
     }

    @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException 

serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
```