## Description on SDK Exceptions

In the SDK, if an API call fails to operate on a COS object, a CosXmlClientException or CosXmlServiceException will be thrown.

### CosXmlClientException

Client exceptions refer to server interaction failures caused by unexpected client issues such as failure to connect to the server, failure to parse the data returned by the server, and the occurrence of I/O exception when reading a local file. Inherited from Exception, CosXmlClientException has no custom member variables, and is used in the same way as Exception.

### CosXmlServiceException

CosXmlServiceException refers to scenarios in which interaction is completed but the operation failed. For example, the client accesses a bucket that does not exist, delete a file that does not exist, or does not have the permission to perform an operation, or the server failed. CosXmlServiceException contains the status code, requestid, and error details returned by the server. After an exception is captured, it is recommended to print the entire exception. The exception contains the necessary troubleshooting factors. Member variables of exception are described as follows:

| request Member | Description | Type |
| ------------ | ---------------------------------------- | --------- |
| requestId    | Request ID to specify a request. It is very important for troubleshooting. | String    |
| statusCode | Status code of the response. 4xx represents the request failure caused by the client, and 5xx represents the failure caused by the server exception. Please see [COS Error Messages](https://cloud.tencent.com/document/product/436/7730) | String |
| errorCode    | Error Code returned in the body when request fails. Please see [COS Error Messages](https://cloud.tencent.com/document/product/436/7730)               | String    |
| errorMessage | Error Message returned in the body when request fails. Please see [COS Error Messages](https://cloud.tencent.com/document/product/436/7730)           | String    |



## Initialization
You need to instantiate CosXmlService and CosXmlServiceConfig before performing operations.
> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

### Instantiating CosXmlServiceConfig
Call CosXmlServiceConfig.Builder().builder() to instantiate the CosXmlServiceConfig object.

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------------- | -------------- | -- | ----------- |
| appid           | COS service APPID String          | Yes |
| region          | The region where the bucket resides String          | Yes | 


#### Other configuration methods
| Method | Description |
|----------|-----------|
|   setAppidAndRegion(String, String) |Sets the region to which the "appid" and the "bucket" belongs |
|   isHttps(boolean)  | true: https request; false: http request (default) |
|   setDebuggable(boolean)  |debug log mode on or off |


#### Example
```java
String appid = "COS service APPID";
String region = "The region where the bucket resides"; //Region: You can view the created bucket via COS console
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
	   .isHttps(true)
       .setAppidAndRegion(appid, region)
       .setDebuggable(true)
       .builder();
```

### Instantiating CosXmlService
Call the `CosXmlService(Context context, CosXmlServiceConfig serviceConfig, QCloudCredentialProvider cloudCredentialProvider)` construction method to instantiate the CosXmlService object.

#### Parameters
| Parameter Name | Description | Type | Required |
| -------------- | -------------- | -- | ----------- |
| context         | Context of application |  Context         | Yes |
| serviceConfig   | Class for configuring SDK |CosXmlServiceConfig    | Yes |
| basicLifecycleCredentialProvider   |Class for getting signature of service request | BasicLifecycleCredentialProvider   | Yes | 

#### Example
```java
String appid = "COS service APPID";
String region = "The region where the bucket is located"; 

//Create a CosXmlServiceConfig object to modify the default configuration parameter as needed
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
	   .isHttps(true)
       .setAppidAndRegion(appid, region)
       .setDebuggable(true)
       .builder();

/**
* 
* Create an object of the class for getting signature ShortTimeCredentialProvider to calculate the signature when using COS. 
* Implement your own signature method (extends BasicLifecycleCredentialProvider and the       * * fetchNewCredentials() method) by applying the signature format provided in SDK.
* The default signature algorithm provided in the SDK is used here.
*
*/
String secretId = "Cloud API key secretId";
String secretKey ="Cloud API key secretKey";
long keyDuration = 600; //Validity of SecretKey (in sec)
ShortTimeCredentialProvider localCredentialProvider = new ShortTimeCredentialProvider(secretId, secretKey, keyDuration);

//Create a CosXmlService object to implement the COS operations.
Context context = getApplicationContext(); //Context of the application
CosXmlService cosXmlService = new CosXmlService(context,cosXmlServiceConfig, localCredentialProvider);

```

## Generating Signature

For more information on how to generate and use a signature, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778). The SDK has provided the class for getting signature. You simply need to inherit the BasicLifecycleCredentialProvider class and override the fetchNewCredentials() method. For more information on how to obtain a temporary key, please see [Quick Setup of Mobile Application Transfer Service](/document/product/436/9068).

#### Example
```java
/**
Method 1: Signing using a permanent key
*/
public class LocalCredentialProvider extends BasicLifecycleCredentialProvider{
    private String secretKey;
    private long keyDuration;
    private String secretId;

     public LocalCredentialProvider(String secretId, String secretKey, long keyDuration) {
        this.secretId = secretId;
        this.secretKey = secretKey;
        this.keyDuration = keyDuration;
     }

     /**
     BasicQCloudCredentials is returned
	 */
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

/**
Method 2: Signing using a temporary key (recommended). This assumes that you have obtained a temporary key tempSecretKey, tempSecrekId,
sessionToken and expiredTime.
*/
public class LocalSessionCredentialProvider extends BasicLifecycleCredentialProvider{
    private String tempSecretId;
    private String tempSecretKey;
    private String sessionToken;
    private long expiredTime;

     public LocalSessionCredentialProvider(String tempSecretId, String tempSecretKey, String sessionToken, long expiredTime) {
        this.tempSecretId = tempSecretId;
        this.tempSecretKey = tempSecretKey;
	    this.sessionToken = sessionToken;
        this.expiredTime = keyDuration;
     }

     /**
     SessionQCloudCredential is returned
	 */
     @Override
     public QCloudLifecycleCredentials fetchNewCredentials() throws CosXmlClientException {
         return new SessionQCloudCredentials(tmpSecretId, tmpSecretKey, sessionToken, expiredTime);
     }
}

```
## Simple upload of files

This API can be used to upload local files to the specified Bucket. The steps are as follows:
1. Call the `PutObjectRequest(String, String, String)` construction method to instantiate the PutObjectRequest object.
2. Call putObject method of CosXmlService, input PutObjectRequest, and get the returned PutObjectResult object.
   (Alternatively, call the putObjectAsync method, and input PutObjectRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket | bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) | String | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| srcPath   | Absolute path to the local file |String           | Yes |
| signDuration    |Validity of the signature (in sec)  |Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| qCloudProgressListener   | Callback for upload progress |CosXmlProgressListener                   | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request result is returned through member variables of PutObjectResult object.

| Member Variable Name | Description | Type | 
| ---- | -------------- |----------- |
| accessUrl   | Return URL for accessing file when the request is successful |String          |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";
String srcPath = "Absolute path to the local file";

PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);
putObjectRequest.setSign(signDuration,null,null);

putObjectRequest.setProgressListener(new CosXmlProgressListener() {
    @Override
    public void onProgress(long progress, long max) {
        float result = (float) (progress * 100.0/max);
        Log.w("TEST","progress =" + (long)result + "%");
    }
});

//Upload using synchronization method
try {
    PutObjectResult putObjectResult = cosXmlService.putObject(putObjectRequest);
	
	Log.w("TEST","success: " + putObjectResult.accessUrl);

  } catch (CosXmlClientException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlClientException =" + e.toString());
  } catch (CosXmlServiceException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Upload using asynchronous callback**
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


## Multipart Upload (UploadServer is recommended)

### Initializing multipart upload

This API is used to initialize multipart upload. After the execution of this request, UploadId will be returned for the subsequent Upload Part requests. The steps are as follows:
1. Call the `InitMultipartUploadRequest(String, String)` construction method to instantiate the InitMultipartUploadRequest object.
2. Call the initMultipartUpload method of CosXmlService, input InitMultipartUploadRequest, and get the returned InitMultipartUploadResult object.
   (Alternatively, call the initMultipartUploadAsync method, and input InitMultipartUploadRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request result is returned through member variables of InitMultipartUploadResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| initMultipartUpload   |[Result returned by successful request](https://cloud.tencent.com/document/product/436/7746)| InitMultipartUpload          |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";

InitMultipartUploadRequest initMultipartUploadRequest = new InitMultipartUploadRequest(bucket, cosPath);
initMultipartUploadRequest.setSign(signDuration,null,null);

String uploadId = null;

//Request using synchronization method
try {
    InitMultipartUploadResult initMultipartUploadResult = cosXmlService.initMultipartUpload(initMultipartUploadRequest);
	
    Log.w("TEST","success");
	uploadId =initMultipartUploadResult.initMultipartUpload.uploadId;

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

### Multipart upload

This API is used to implement multipart upload. The allowed number of parts is limited to 10,000, and the size of part should be between 1 MB and 5 GB. The steps are as follows:
1. Call the `UploadPartRequest(String, String, int, String, String)` construction method to instantiate the UploadPartRequest object.
2. Call the uploadPart method of CosXmlService, Iinput UploadPartRequest, and get the returned UploadPartResult object.
   (Alternatively, call the uploadPartAsync method, and input UploadPartRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| uploadId    | uploadId returned when multipart upload is initialized | String           | Yes |
| partNumber   |Part No., which starts from 1 | Int           | Yes |
| srcPath   | Absolute path to the local file |String           | Yes |
| fileOffset   |Where the part starts in the file | Long           | No |
| contentLength   | Size of the part |Long           | No |
| signDuration    |Validity of the signature (in sec)  | Long           | No |
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| qCloudProgressListener   | Callback for upload progress | CosXmlProgressListener          | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 

#### Returned result
Request result is returned through member variables of UploadPartResult object.

| Member Variable Name | Type | Description |
| ---- | --------------  | ----------- |
| eTag   | Return the MD5 value of the part if the request is successful. It is used to complete the sharding. |String          | 
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = " uploadId returned when multipart upload is initialized | ";
int partNumber = 1;// The number of the part to be uploaded, starting from 1
String srcPath = "Absolute path to the local file";

UploadPartRequest uploadPartRequest = new UploadPartRequest(bucket, cosPath, partNumber, srcPath, uploadId);
uploadPartRequest.setSign(signDuration,null,null);

uploadPartRequest.setProgressListener(new CosXmlProgressListener() {
    @Override
    public void onProgress(long progress, long max) {
        float result = (float) (progress * 100.0/max);
        Log.w("TEST","progress =" + (long)result + "%");
    }
});

String eTag = null;

//Upload using synchronization method
try {
    UploadPartResult uploadPartResult = cosXmlService.uploadPart(uploadPartRequest);
    
    Log.w("TEST","success");
    eTag = uploadPartResult.eTag; // Get the eTag of the part
	
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**Use an asynchronous callback request**
/**

cosXmlService.uploadPartAsync(uploadPartRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {

		Log.w("TEST","success");
        eTag =((UploadPartResult)cosXmlResult).eTag;
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

### Completing multipart upload

After all parts are uploaded, this API must be called to complete the entire multipart upload. The steps are as follows:
1. Call the `CompleteMultiUploadRequest(String, String, String, Map<Integer, String>)` construction method to instantiate the CompleteMultiUploadRequest object.
2. Call the completeMultiUpload method of CosXmlService, input CompleteMultiUploadRequest, and get the returned CompleteMultiUploadResult object.
   (Alternatively, call the completeMultiUploadAsync method, and input CompleteMultiUploadRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| uploadId    | uploadId returned when multipart upload is initialized | String           | Yes |
| partNumberAndETag    | Part No. and the corresponding MD5 value |Map&lt;Integer,String>           | Yes | 
| signDuration    |Validity of the signature (in sec)  | Long           | Yes |
| checkHeaderListForSign    | Request header in signature for verification | Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result | CosXmlResultListener          | No | 


#### Returned result
Request result is returned through member variables of CompleteMultiUploadResult object.

| Member Variable Name | Description | Type |
| ---- | -------------- | ----------- |
| completeMultipartUpload   | [Result returned by successful request](https://cloud.tencent.com/document/product/436/7742)|CompleteMultipartResult          |
| accessUrl   | Return URL for accessing file when the request is successful |String          |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = " uploadId returned when multipart upload is initialized | ";
int partNumber = 1;
String etag = "The etag returned after the part with the No. of partNumber is uploaded";
Map<Integer, String> partNumberAndETag = new HashMap<>();
partNumberAndETag.put(partNumber, etag);

CompleteMultiUploadRequest completeMultiUploadRequest = new CompleteMultiUploadRequest(bucket, cosPath, uploudId, 

partNumberAndETag);
completeMultiUploadRequest.setSign(signDuration,null,null);

//Request using synchronization method
try {
    CompleteMultiUploadResult completeMultiUploadResult = cosXmlService.completeMultiUpload(completeMultiUploadRequest);
	
	Log.w("TEST","success: "+ completeMultiUploadResult.completeMultipartUpload.toString()());
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

### Listing uploaded parts

This API is used to query the uploaded parts when uploading particular parts, which lists all the uploaded parts under a specified UploadId.
1. Call the `ListPartsRequest(String, String, String)` construction method to instantiate the ListPartsRequest object.
2. Call the listParts method of CosXmlService, input ListPartsRequest, and get the returned ListPartsResult object.
   (Alternatively, call the listPartsAsync method, and input ListPartsRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| uploadId    | uploadId returned when multipart upload is initialized | String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 

#### Returned result
Request result is returned through member variables of ListPartsResult object.

| Member Variable Name | Description | Type | 
| ---- | --------------  | ----------- |
| listParts  | [Result returned by successful request](https://cloud.tencent.com/document/product/436/7747)     | ListParts             |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = " uploadId returned when multipart upload is initialized | ";

ListPartsRequest listPartsRequest = new ListPartsRequest(bucket, cosPath, uploadId);
listPartsRequest.setSign(signDuration,null,null);

//Request using synchronization method
try {
    ListPartsResult listPartsResult = cosXmlService.listParts(listPartsRequest);
	
    Log.w("TEST","success: " + listPartsResult.listParts.toString());
       
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

### Aborting and deleting uploaded parts
This API is used to abort a multipart upload operation and delete parts that are already uploaded.
1. Call the `AbortMultiUploadRequest(String, String, String)` construction method to instantiate the AbortMultiUploadRequest object.
2. Call the abortMultiUpload method of CosXmlService, input AbortMultiUploadRequest, and get the returned AbortMultiUploadResult object.
   (Alternatively, call the abortMultiUploadAsync method, and input AbortMultiUploadRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| uploadId    | uploadId returned when multipart upload is initialized | String           | Yes |
| signDuration    | Validity of the signature (in sec)  |Long           | Yes |
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request result is returned through member variables of AbortMultiUploadResult object.

| Member Variable Name | Description | Type | 
| ---- | -------------- | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
String bucket = "bucket";
String cosPath = "cosPath";
String uploadId = " uploadId returned when multipart upload is initialized | ";

AbortMultiUploadRequest abortMultiUploadRequest = new AbortMultiUploadRequest(bucket, cosPath, uploadId);
abortMultiUploadRequest.setSign(signDuration,null,null);

//Request using synchronization method
try {
    AbortMultiUploadResult abortMultiUploadResult = cosXmlService.abortMultiUpload(abortMultiUploadRequest);
	Log.w("TEST", "success");
       
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**Use an asynchronous callback request**
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

## Deleting Files

### Deleting a single file

This API is used to delete a file in the specified bucket. The steps are as follows:
1. Call the `DeleteObjectRequest(String, String)` construction method to instantiate the DeleteObjectRequest object.
2. Call the completeMultiUpload method of CosXmlService, input DeleteObjectRequest, and get the returned DeleteObjectResult object.
   (Alternatively, call the deleteObjectAsync method, and input DeleteObjectRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS | String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification | Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request result is returned through member variables of DeleteObjectResult object.

| Member Variable Name | Description | Type | 
| ---- | -------------- | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";

DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(bucket, cosPath);
deleteObjectRequest.setSign(signDuration,null,null);

//Delete using synchronous method
try {
    DeleteObjectResult deleteObjectResult = cosXmlService.deleteObject(deleteObjectRequest);
    Log.w("TEST","success ");

  } catch (CosXmlClientException e) {
      Log.w("TEST","CosXmlClientException =" + e.toString());
   } catch (CosXmlServiceException e) {
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

### Deleting multiple files

This API is used to delete files in a specified bucket in batches. A maximum of 1,000 files can be deleted for a single request. The steps are as follows:
1. Call the DeleteMultiObjectRequest(String, List&lt;String>) construction method to instantiate the DeleteMultiObjectRequest object.
2. Call the deleteMultiObject method of CosXmlService, input DeleteMultiObjectRequest, and get the returned DeleteMultiObjectResult object.
   (Alternatively, call the deleteMultiObjectAsync method, and input DeleteMultiObjectRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| quiet   | true: Only information of the file that failed to be deleted is returned; false: Deletion result of each file is returned |Boolean           | Yes |
| objectList   | The list of [object keys](https://cloud.tencent.com/document/product/436/13324)to delete |List&lt;String> | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 

#### Returned result
Request result is returned through member variables of DeleteMultiObjectResult object.

| Member Variable Name | Description | Type | 
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
List<String> objectList = new ArrayList<String>();
objectList.add("/2/test.txt");

DeleteMultiObjectRequest deleteMultiObjectRequest = new DeleteMultiObjectRequest();
deleteMultiObjectRequest.setQuiet(quiet);
deleteMultiObjectRequest.setSign(signDuration,null,null);

//Delete using synchronous method
try {
   DeleteMultiObjectResult deleteMultiObjectResult =cosXmlService.deleteMultiObject(deleteMultiObjectRequest);
	
   Log.w("TEST","success: " + deleteMultiObjectResult.deleteResult.toString());
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Downloading a File

This API is used to download a file in the specified bucket locally. The steps are as follows:
1. Call the `GetObjectRequest(String, String, String)` construction method to instantiate the GetObjectRequest object.
2. Call the getObject method of CosXmlService, input GetObjectRequest, and get the returned GetObjectResult object.
   (Alternatively, call the getObjectAsync method, and input GetObjectRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath   | [Object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| savaPath   |Absolute path to the file downloaded locally |String | Yes |
| start   |Where the requested file starts |Long | No |
| end   |Where the requested file ends |Long | No |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| qCloudProgressListener   | Callback for download progress |CosXmlProgressListener          | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 

#### Returned result
Request result is returned through member variables of GetObjectResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |


>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";
String savePath = "savePath";

GetObjectRequest getObjectRequest = GetObjectRequest(bucket, cosPath, savePath);

getObjectRequest.setSign(signDuration,null,null);
getObjectRequest.setProgressListener(new CosXmlProgressListener() {
    @Override
    public void onProgress(long progress, long max) {
        float result = (float) (progress * 100.0/max);
        Log.w("TEST","progress =" + (long)result + "%");
    }
});

//Upload using synchronization method
try {
   GetObjectResult getObjectResult =cosXmlService.getObject(getObjectRequest);
	
	Log.w("TEST","success: " + getObjectResult.xCOSStorageClass);
       
  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Copying Objects

This API is used to copy a file from the source path to the destination path. The recommended file size is from 1M to 5G. Files larger than 5G will adopt multipart upload using Upload - Copy. The steps are as follows:
1. Call the `CopyObjectRequest(String,String, CopySourceStruct)` construction method to instantiate the CopyObjectRequest object.
2. Call the copyObject method of CosXmlService, input CopyObjectRequest, and get the returned CopyObjectResult object.
   (Alternatively, call the copyObjectAsync method, and input CopyObjectRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cosPath    | Target [object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS |String           | Yes |
| copySourceStruct    | Source path structure |CopySourceStruct           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request result is returned through member variables of CopyObjectResult object.

| Member Variable Name | Description | Type |
| ---- | -------------- | ----------- |
|copyObject |Returns the copy result | CopyObject| 
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java

String bucket = "bucket";
String cosPath = "cosPath";
CopyObjectRequest.CopySourceStruct copySourceStruct = new CopyObjectRequest.CopySourceStruct("Source file's appid",
"Source file's bucket", "Source file's region", "Source file's cosPath");

CopyObjectRequest copyObjectRequest = new CopyObjectRequest(bucket, cosPath, copySourceStruct);
copyObjectRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
    CopyObjectResult copyObjectResult = cosXmlService.copyObject(copyObjectRequest);
       //Successful
	  Log.w("TEST","success:" + copyObjectResult.copyObject);

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Creating a Bucket

This API is used to create a Bucket under the specified account. The steps are as follows:
1. Call the `PutBucketRequest(String)` construction method to instantiate the PutBucketRequest object.
2. Call putBucket method of CosXmlService, input PutBucketRequest, and get the returned PutBucketResult object.
   (Alternatively, call the putBucketAsync method, and input PutBucketRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request request is returned through member variables of PutBucketResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
PutBucketRequest putBucketRequest = new PutBucketRequest(bucket);
putBucketRequest.setSign(signDuration,null,null);

//Define the ACL attribute of Object. Valid values: private, public-read-write, public-read; Default: private	
putBucketRequest.setXCOSACL("private");

//Grant read permission to the authorized user
ACLAccount readACLS = new ACLAccount();
readACLS.addACLAccount("OwnerUin", "SubUin");
putBucketRequest.setXCOSGrantRead(readACLS);

//Grant write permission to the authorized user
ACLAccount writeACLS = new ACLAccount();
writeACLS.addACLAccount("OwnerUin", "SubUin");
putBucketRequest.setXCOSGrantRead(writeACLS);

//Grant read and write permissions to the authorized user
ACLAccount writeandReadACLS = new ACLAccount();
writeandReadACLS.addACLAccount("OwnerUin", "SubUin");
putBucketRequest.setXCOSGrantRead(writeandReadACLS);

//Use synchronization method
try {
    PutBucketResult putBucketResult = cosXmlService.putBucket(putBucketRequest);
       //Successful
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Checking Whether Bucket Exists

This API is used to confirm the existence of the specified bucket. The steps are as follows:
1. Call the HeadBucketRequest(String) construction method to instantiate the HeadBucketRequest object.
2. Call the headBucket method of CosXmlService, input HeadBucketRequest, and get the returned HeadBucketResult object.
   (Alternatively, call the headBucketAsync method, and input HeadBucketRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    | Validity of the signature (in sec)  |Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request request is returned through member variables of PutBucketResult object.

| Member Variable Name | Description | Type | 
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
HeadBucketRequest headBucketRequest = new HeadBucketRequest(bucket);
headBucketRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
     HeadBucketResult headBucketResult = cosXmlService.headBucket(headBucketRequest);
       //Successful
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Listing Bucket 

This API is used to list some or all of the objects under the Bucket. The steps are as follows:
1. Call the `GetBucketRequest(String)` construction method to instantiate the GetBucketRequest object.
2. Call getBucket method of CosXmlService, input GetBucketRequest, and get the returned GetBucketResult object.
   (Alternatively, call the getBucketAsync method, and input GetBucketRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    | Validity of the signature (in sec)  | Long           | Yes |
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request request is returned through member variables of GetBucketResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| listBucket |Store all the information of Get Bucket request result | ListBucket | 
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
GetBucketRequest getBucketRequest = new GetBucketRequest(bucket);
getBucketRequest.setSign(signDuration,null,null);

//Indicates the prefix match, which is used to specify the prefix address of the returned file
getBucketRequest.setPrefix("prefix");

//Maximum number of entries returned at a time. Default is 1,000
getBucketRequest.setMaxKeys(100);

//The delimiter is a sign. If Prefix exists,
//the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix,
//and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path.
getBucketRequest.setDelimiter('c');

//Use synchronization method
try {
     GetBucketResult getBucketResult = cosXmlService.getBucket(getBucketRequest);
       //Successful
	  Log.w("TEST","success :" + getBucketResult.listBucket.toString());

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Deleting Bucket 

This API is used to delete a Bucket under a specified account. The Bucket must be empty before it can be deleted. The Bucket can be deleted only if its content is removed. The steps are as follows:
1. Call the `DeleteBucketRequest(String)` construction method to instantiate the DeleteBucketRequest object.
2. Call the deleteBucket method of CosXmlService, input DeleteBucketRequest, and get the returned DeleteBucketResult object.
   (Alternatively, call the deleteBucketAsync method, and input DeleteBucketRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    | Validity of the signature (in sec)  | Long           | Yes |
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of DeleteBucketResult object.

| Member Variable Name | Description | Type | 
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |


>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
DeleteBucketRequest deleteBucketRequest = new DeleteBucketRequest(bucket);
deleteBucketRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
     DeleteBucketResult deleteBucketResult = cosXmlService.deleteBucket(deleteBucketRequest);
       //Successful
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Setting Bucket ACL

This API is used to specify the Bucket's access permission. The steps are as follows:
1. Call the `PutBucketACLRequest(String)` construction method to instantiate the PutBucketACLRequest object.
2. Call putBucketACL method of CosXmlService, input PutBucketACLRequest, and get the returned PutBucketACLResult object.
   (Alternatively, call the putBucketACLAsync method, and input PutBucketACLRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| xcosACL    | Sets Bucket's access permissions. Valid values: private, public-read-write, public-read; Default: private |String           | No |
| xcosGrantRead    | Grants read permission to the authorized user |ACLAccount           | No |
| xcosGrantWrite    | Grants write permission to the authorized user | ACLAccount           | No |
| xcosGrantRead    | Grants read and write permission to the authorized user |ACLAccount           | No |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification | Set&lt;String>           | No | 
| checkParameterListForSing   |Request parameters in signature for verification | Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |
#### Returned result
Request result is returned through member variables of DeleteBucketResult object.

| Member Variable Name | Description | Type | 
| ---- | -------------- | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
PutBucketACLRequest putBucketACLRequest = new PutBucketACLRequest(bucket);
putBucketACLRequest.setSign(signDuration,null,null);

//Set access permission to the bucket
putBucketACLRequest.setXCOSACL("public-read");

//Grant read permission to the authorized user
ACLAccount readACLS = new ACLAccount();
readACLS.addACLAccount("OwnerUin", "SubUin");
putBucketRequest.setXCOSGrantRead(readACLS);

//Grant write permission to the authorized user
ACLAccount writeACLS = new ACLAccount();
writeACLS.addACLAccount("OwnerUin", "SubUin");
putBucketRequest.setXCOSGrantRead(writeACLS);

//Grant read and write permissions to the authorized user
ACLAccount writeandReadACLS = new ACLAccount();
writeandReadACLS.addACLAccount("OwnerUin", "SubUin");
putBucketRequest.setXCOSGrantRead(writeandReadACLS);

//Use synchronization method
try {
     PutBucketACLResult putBucketACLResult = cosXmlService.putBucketACL(putBucketACLRequest);
       //Successful
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}


//**Use an asynchronous callback request**
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
## Obtaining Bucket ACL

This API is used to obtain the Bucket ACL. The steps are as follows:
1. Call the `GetBucketACLRequest(String)` construction method to instantiate the GetBucketACLRequest object.
2. Call getBucketACL method of CosXmlService, input GetBucketACLRequest, and get the returned GetBucketACLResult object.
   (Alternatively, call the getBucketACLAsync method, and input GetBucketACLRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  |Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request request is returned through member variables of GetBucketACLResult object.

| Member Variable Name | Description | Type |
| ---- | -------------- | ----------- |
| accessControlPolicy  | [About authorized users and their permissions](https://cloud.tencent.com/document/product/436/7733)|AccessControlPolicy             |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
GetBucketACLRequest getBucketACLRequest = new DeleteBucketRequest(bucket);
getBucketACLRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
     GetBucketACLResult getBucketACLResult = cosXmlService.getBucketACL(getBucketACLRequest);
       //Successful
	  Log.w("TEST","success: " +getBucketACLResult.accessControlPolicy.toString() );

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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


## Setting Cross-domain Access Configuration

This API is used to configure cross-origin access for the specified Bucket. The steps are as follows:
1. Call the `PutBucketCORSRequest(String)` construction method to instantiate the PutBucketCORSRequest object.
2. Call putBucketCORS method of CosXmlService, input PutBucketCORSRequest, and get the returned PutBucketCORSResult object.
   (Alternatively, call the putBucketCORSAsync method, and input PutBucketCORSRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| cORSRule    | Configurations on cross-origin access |CORSConfiguration.CORSRule           | Yes |
| signDuration    | Validity of the signature (in sec)  | Long           | Yes |
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   |Request parameters in signature for verification | Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request request is returned through member variables of PutBucketCORSResult object.

| Member Variable Name | Description | Type | 
| ---- | -------------- | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
PutBucketCORSRequest putBucketCORSRequest = new PutBucketCORSRequest(bucket);

/**
CORSConfiguration.cORSRule: Configurations on cross-origin access
corsRule.id: Sets rule ID
cORSRule.allowedOrigin: Allowed access sources. The wildcard "*" is supported. Format: protocol://domain_name[:port], for example, http://www.qq.com
corsRule.maxAgeSeconds: Configure the valid period of the results obtained by OPTIONS request
corsRule.allowedMethod: Allowed HTTP operations, such as GET, PUT, HEAD, POST, and DELETE
corsRule.allowedHeader: When sending an OPTIONS request, notify the server end about which custom HTTP request headers are allowed to be used by subsequent requests. The wildcard "*" is supported.
corsRule.exposeHeader: Configure the custom header information that can be received by the browser from the server end
*/
CORSConfiguration.CORSRule corsRule = new CORSConfiguration.CORSRule();

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

//Configure cross-origin access
putBucketCORSRequest.addCORSRule(corsRule);

putBucketCORSRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
   PutBucketCORSResult putBucketCORSResult = cosXmlService.putBucketCORS(putBucketCORSRequest);
       //Successful
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Obtaining Cross-domain Access Configuration

This API is used to obtain configurations on cross-origin access to the specified Bucket. The steps are as follows:
1. Call the `GetBucketCORSRequest(String)` construction method to instantiate the GetBucketCORSRequest object.
2. Call getBucketCORS method of CosXmlService, input GetBucketCORSRequest, and get the returned GetBucketCORSResult object.
   (Alternatively, call the getBucketCORSAsync method, and input GetBucketCORSRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    | Validity of the signature (in sec)  |Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification | Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request request is returned through member variables of GetBucketCORSResult object.

| Member Variable Name | Type | Description |
| ---- | --------------  | ----------- |
| cORSConfiguration  | [All configurations on cross-origin resource sharing](https://cloud.tencent.com/document/product/436/8274)|CORSConfiguration             |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
GetBucketCORSRequest getBucketCORSRequest = new GetBucketCORSRequest(bucket);
getBucketCORSRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
    GetBucketCORSResult getBucketCORSResult = cosXmlService.getBucketCORS(getBucketCORSRequest);
       //Successful
	  Log.w("TEST","success :" + getBucketCORSResult.corsConfiguration.toString());

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Deleting Cross-domain Access Configuration

This API is used to delete the cross-domain access configuration information of the specified Bucket. Specific steps are as follows:
1. Call the `DeleteBucketCORSRequest(String)` construction method to instantiate the DeleteBucketCORSRequest object.
2. Call the deleteBucketCORS method of CosXmlService, input DeleteBucketCORSRequest, and get the returned DeleteBucketCORSResult object. 
   (Alternatively, call the deleteBucketCORSAsync method, and input DeleteBucketCORSRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variable of DeleteBucketCORSResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
DeleteBucketCORSRequest deleteBucketCORSRequest = new DeleteBucketCORSRequest(bucket);
deleteBucketCORSRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
   DeleteBucketCORSResult deleteBucketCORSResult = cosXmlService.deleteBucketCORS(deleteBucketCORSRequest);
       //Successful
	  Log.w("TEST","success");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Obtaining Bucket's Region Information

This API is used to obtain the region where the Bucket resides. The steps are as follows:
1. Call the `GetBucketLocationRequest(String)` construction method to instantiate the GetBucketLocationRequest object.
2. Call getBucketLocation method of CosXmlService, input GetBucketLocationRequest, and get the returned GetBucketLocationResult object.
   (Alternatively, call the getBucketLocationAsync method, and input GetBucketLocationRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    | Validity of the signature (in sec)  |Long           | Yes |
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of GetBucketLocationResult object.

| Member Variable Name | Description | Type | 
| ---- | --------------  | ----------- |
| locationConstraint| The region where the Bucket resides |LocationConstraint |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
GetBucketLocationRequest getBucketLocationRequest = new DeleteBucketCORSRequest(bucket);
getBucketLocationRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
   GetBucketLocationResult getBucketLocationResult = cosXmlService.getBucketLocation(getBucketLocationRequest);
       //Successful
	  Log.w("TEST","success : " + getBucketLocationResult.LocationConstraint.location);

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Configuring Bucket Lifecycle

This API is used to set the lifecycle of a bucket. The steps are as follows:
1. Call the `PutBucketLifecycleRequest(String)` construction method to instantiate the PutBucketLifecycleRequest object.
2. Call putBucketLifecycle method of CosXmlService, input PutBucketLifecycleRequest, and get the returned PutBucketLifecycleResult object.
   (Alternatively, call the putBucketLifecycleAsync method, and input PutBucketLifecycleRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| rule    | Rules for configuring a life cycle |LifecycleConfiguration.Rule           | Yes |
| signDuration    | Validity of the signature (in sec)  | Long           | Yes |
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of PutBucketLifecycleResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
PutBucketLifecycleRequest putBucketLifecycleRequest = new PutBucketLifecycleRequest(bucket);
putBucketLifecycleRequest.setSign(signDuration,null,null);

//Declare lifecycle configuration rules
LifecycleConfiguration.Rule rule = new LifecycleConfiguration.Rule();
rule.id = "Lifecycle ID";
LifecycleConfiguration.Filter filter = new LifecycleConfiguration.Filter();
filter.prefix = "prefix/";
rule.filter = filter;
rule.status = "Enabled or Disabled";
LifecycleConfiguration.Transition transition = new LifecycleConfiguration.Transition();
transition.days = 100;
transition.storageClass = COSStorageClass.STANDARD.getStorageClass();
putBucketLifecycleRequest.setRuleList(rule);

//Use synchronization method
try {
   PutBucketLifecycleResult putBucketLifecycleResult = cosXmlService.putBucketLifecycle(putBucketLifecycleRequest);
       //Successful
	  Log.w("TEST","success : " + getBucketLocationResult.region);

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Obtaining Bucket Lifecycle

This API is used to obtain the lifecycle configuration of a bucket. The steps are as follows:
1. Call the `GetBucketLifecycleRequest(String)` construction method to instantiate the GetBucketLifecycleRequest object.
2. Call getBucketLifecycle method of CosXmlService, input GetBucketLifecycleRequest, and get the returned GetBucketLifecycleResult object.
   (Alternatively, call the getBucketLifecycleAsync method, and input GetBucketLifecycleRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No |
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 


#### Returned result
Request result is returned through member variables of getBucketLifecycle object.

| Member Variable Name | Description | Type | 
| ---- | --------------  | ----------- |
|lifecycleConfiguration| Lifecycle configurations |LifecycleConfiguration| 
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
GetBucketLifecycleRequest getBucketLifecycleRequest = new DeleteBucketCORSRequest(bucket);
getBucketLifecycleRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
   GetBucketLifecycleResult getBucketLifecycleResult = cosXmlService.getBucketLifecycle(getBucketLifecycleRequest);
       //Successful
	  Log.w("TEST","success : " + getBucketLifecycleResult.lifecycleConfiguration.toString());

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Deleting Bucket Lifecycle

This API is used to delete the lifecycle configuration of a bucket. The steps are as follows:
1. Call the `DeleteBucketLifecycleRequest(String)` construction method to instantiate the DeleteBucketLifecycleRequest object.
2. Call the deleteBucketLifecycle method of CosXmlService, input DeleteBucketLifecycleRequest, and get the returned DeleteBucketLifecycleResult object.
   (Alternatively, call the deleteBucketLifecycleAsync method, and input DeleteBucketLifecycleRequest and CosXmlResultListener for asynchronous callback).

#### Parameters
| Parameter Name | Description | Type | Required |
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No |
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No | 

#### Returned result
Request result is returned through member variables of DeleteBucketLifecycleResult object.

| Member Variable Name | Description | Type | 
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
DeleteBucketLifecycleRequest deleteBucketLifecycleRequest = new DeleteBucketCORSRequest(bucket);
deleteBucketLifecycleRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
   DeleteBucketLifecycleResult deleteBucketCORSResult = cosXmlService.deleteBucketLifecycle(deleteBucketLifecycleRequest);
       //Successful
	  Log.w("TEST","success ");

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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

## Querying Parts being Uploaded in Bucket

This API is used to obtain multipart upload operations that are still in process. A maximum of 1,000 such operations can be listed at a time. The steps are as follows:
1. Call the `ListMultiUploadsRequest(String)` construction method to instantiate the ListMultiUploadsRequest object.
2. Call the listMultiUploads method of CosXmlService, input ListMultiUploadsRequest, and get the returned ListMultiUploadsResult object.
   (Alternatively, call the listMultiUploadsAsync method, and input ListMultiUploadsRequest and CosXmlResultListener for asynchronous callback).

#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of ListMultiUploadsResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| listMultipartUploads |Information on all multipart upload operations | ListMultipartUploads | 
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
ListMultiUploadsRequest listMultiUploadsRequest = new ListMultiUploadsRequest(bucket);
listMultiUploadsRequest.setSign(signDuration,null,null);

//Use synchronization method
try {
   ListMultiUploadsResult listMultiUploadsResult = cosXmlService.listMultiUploads(listMultiUploadsRequest);
       //Successful
	  Log.w("TEST","success: " + listMultiUploadsResult.listMultipartUploads.toString());

  } catch (CosXmlClientException e) {

      Log.w("TEST","CosXmlClientException =" + e.toString());

   } catch (CosXmlServiceException e) {

       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//**Use an asynchronous callback request**
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


## Setting up Multiple Versions

This API is used to setup version control for a Bucket. The steps are as follows:
1. Call the PutBucketVersioningRequest construction method to instantiate the PutBucketVersioningRequest object.
2. Call the putBucketVersioning(PutBucketVersioningRequest) synchronization method of CosXmlService, input PutBucketVersioningRequest, and get the returned PutBucketVersioningResult object. (Alternatively, call the putBucketVersionAsync method, and input PutBucketVersioningRequest and CosXmlResultListener for asynchronous callback).


#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| isEnable    | Whether to enable multi-version control. Use true to enable or false to disable |boolean           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of PutBucketVersioningResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
String bucket = "bucket";
PutBucketVersioningRequest request = new PutBucketVersioningRequest(bucket);
request.setEnableVersion(true);//Enable
request.setSign(signDuration,null,null); //Signature
try {
     PutBucketVersioningResult result = cosXmlService.putBucketVersioning(request);
     Log.w("TEST","success");
} catch (CosXmlClientException e) {
     Log.w("TEST","CosXmlClientException =" + e.toString());
} catch (CosXmlServiceException e) {
     Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**Use an asynchronous callback request**
/**

cosXmlService.putBucketVersionAsync(request, new CosXmlResultListener() {
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

## Retrieving Version Control Configuration
This API is used to obtain the version control configuration of the specified Bucket.
1. Call the GetBucketVersioningRequest construction method to instantiate the GetBucketVersioningRequest object.
2. Call the getBucketVersioning(GetBucketVersioningRequest) synchronization method of CosXmlService, input GetBucketVersioningRequest, and get the returned GetBucketVersioningResult object. (Alternatively, call the getBucketVersioningAsync method, and input GetBucketVersioningRequest and CosXmlResultListener for asynchronous callback).


#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of GetBucketVersioningResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| versioningConfiguration |Version control configuration | VersioningConfiguration | 
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
String bucket = "bucket";
GetBucketVersioningRequest request = new GetBucketVersioningRequest(bucket);
request.setSign(signDuration,null,null); //Signature
try {
     GetBucketVersioningResult result = cosXmlService.getBucketVersioning(request);
     Log.w("TEST","success");
} catch (CosXmlClientException e) {
     Log.w("TEST","CosXmlClientException =" + e.toString());
} catch (CosXmlServiceException e) {
     Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**Use an asynchronous callback request**
/**

cosXmlService.getBucketVersioningAsync(request, new CosXmlResultListener() {
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

#### Setting Up cross-origin replication
This API is used to configure asynchronous replication between buckets in different domains. 
1. Call the PutBucketReplicationRequest construction method to instantiate the PutBucketReplicationRequest object.
2. Call the putBucketReplication(PutBucketReplicationRequest) synchronization method of CosXmlService, input PutBucketReplicationRequest, and get the returned PutBucketReplicationResult object. (Alternatively, call the putBucketReplicationAsync method, and input PutBucketReplicationRequest and CosXmlResultListener for asynchronous callback).


#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| ownerUin    | Sets Owner Uin for identifying the replication initiator |String           | Yes |
| subUin    | Sets sub Uin for identifying the replication initiator |String           | Yes |
| ruleStruct    |Cross-domain configurations. A maximum of 1,000 rules are supported. All rules must directed to one destination bucket. |RuleStruct           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of PutBucketReplicationResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
String bucket = "bucket";
PutBucketReplicationRequest request = new PutBucketReplicationRequest(bucket);
PutBucketReplicationRequest.RuleStruct ruleStruct = new PutBucketReplicationRequest.RuleStruct();
ruleStruct.id = "replication_id";
ruleStruct.isEnable = true;
ruleStruct.appid = "1253960454";
ruleStruct.bucket = "replicationtest";
ruleStruct.region = "ap-beijing";
request.setReplicationConfigurationWithRule(ruleStruct);
request.setReplicationConfigurationWithRole("ownerUin", "subUin");
request.setSign(signDuration,null,null); //Signature
try {
     PutBucketReplicationResult result = cosXmlService.putBucketReplication(request);
     Log.w("TEST","success");
} catch (CosXmlClientException e) {
     Log.w("TEST","CosXmlClientException =" + e.toString());
} catch (CosXmlServiceException e) {
     Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**Use an asynchronous callback request**
/**

cosXmlService.putBucketReplicationAsync(request, new CosXmlResultListener() {
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

## Retrieving Cross-origin Configuration
This API is used to obtain the cross-origin configuration of the specified Bucket.
1. Call the GetBucketReplicationRequest construction method to instantiate the GetBucketReplicationRequest object.
2. Call the getBucketReplication(GetBucketReplicationRequest) synchronization method of CosXmlService, input GetBucketReplicationRequest, and get the returned GetBucketReplicationResult object. (Alternatively, call the getBucketReplicationAsync method, and input GetBucketReplicationRequest and CosXmlResultListener for asynchronous callback).


#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of GetBucketReplicationResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| replicationConfiguration |Cross-origin configuration | ReplicationConfiguration | 
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
String bucket = "bucket";
GetBucketReplicationRequest request = new GetBucketReplicationRequest(bucket);
request.setSign(signDuration,null,null); //Signature
try {
     GetBucketReplicationResult result = cosXmlService.getBucketReplication(request);
     Log.w("TEST","success");
} catch (CosXmlClientException e) {
     Log.w("TEST","CosXmlClientException =" + e.toString());
} catch (CosXmlServiceException e) {
     Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**Use an asynchronous callback request**
/**

cosXmlService.getBucketReplicationAsync(request, new CosXmlResultListener() {
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

## Deleting Cross-origin Replication
This API is used to delete the cross-origin configuration of the specified Bucket.
1. Call the DeleteBucketReplicationRequest construction method to instantiate the DeleteBucketReplicationRequest object.
2. Call the deleteBucketReplication(DeleteBucketReplicationRequest) synchronization method of CosXmlService, input DeleteBucketReplicationRequest, and get the returned DeleteBucketReplicationResult object. (Alternatively, call the deleteBucketReplicationAsync method, and input DeleteBucketReplicationRequest and CosXmlResultListener for asynchronous callback).


#### Parameters

| Parameter Name | Description | Type | Required | 
| -------- | --------------- | -- | ----------- |
| bucket    | Bucket name (bucket format of cos v5: xxx-appid, such as test-1253960454) |String           | Yes |
| signDuration    |Validity of the signature (in sec)  | Long           | Yes | 
| checkHeaderListForSign    | Request header in signature for verification |Set&lt;String>           | No | 
| checkParameterListForSing   | Request parameters in signature for verification |Set&lt;String>           | No | 
| cosXmlResultListener   | Callback for upload result |CosXmlResultListener          | No |


#### Returned result
Request result is returned through member variables of DeleteBucketReplicationResult object.

| Member Variable Name | Description | Type |
| ---- | --------------  | ----------- |
| httpCode  |Request is successful when it is in [200, 300), otherwise request failed |  Int             |

>  If an exception CosClientException or CosServiceException is thrown, please see **Description on SDK Exceptions** at the beginning.

#### Example
```java
String bucket = "bucket";
DeleteBucketReplicationRequest request = new DeleteBucketReplicationRequest(bucket);
request.setSign(signDuration,null,null); //Signature
try {
     DeleteBucketReplicationResult result = cosXmlService.deleteBucketReplication(request);
     Log.w("TEST","success");
} catch (CosXmlClientException e) {
     Log.w("TEST","CosXmlClientException =" + e.toString());
} catch (CosXmlServiceException e) {
     Log.w("TEST","CosXmlServiceException =" + e.toString());
}
//**Use an asynchronous callback request**
/**

cosXmlService.deleteBucketReplicationAsync(request, new CosXmlResultListener() {
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

