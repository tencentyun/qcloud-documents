## Preparations for Development

### Obtaining SDK
Download the XML Android SDK resources of COS service from [XML Android SDK](https://github.com/tencentyun/qcloud-sdk-android/releases).
Download Demo from: [XML Android SDK Demo](https://github.com/tencentyun/qcloud-sdk-android-samples).

### Preparations for development

1. Android 2.2 or above is supported by the SDK.
2. Your mobile phone must be connected to a network such as GPRS, 3G or WiFi;
3. Some features may not function if there is no enough storage on the mobile phone;
4. Obtain APPID, SecretId and SecretKey from [COS v5 Console](https://console.cloud.tencent.com/cos4/secret).

> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

### Configuring SDK

The following JAR files need to be imported into the project and stored in the libs folder:

- cos-android-sdk-V5.4.4.jar
- qcloud-foundation.1.3.0.jar
- okhttp-3.8.1.jar
- okio-1.13.0.jar

Or use Gradle to integrate the SDK into your project as follows:

- compile 'com.tencent.qcloud:cosxml:5.4.4'


The use of the SDK requires the access permissions related to network, storage, etc. You can add the following permission statement in AndroidManifest.xml (For Android 5.0 or above, dynamic permissions are also needed):
```html
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```


## Getting Started 

### Initialization 

You need to instantiate CosXmlService and CosXmlServiceConfig before performing any operation.
- CosXmlServiceConfig: configuration parameters;
- CosXmlService: The service class provided by the SDK for operating various COS services;

````java
String appid = "COS service APPID";
String region = "The region where the bucket resides"; 

String secretId = "Cloud API key SecretId";
String secretKey ="Cloud API key SecretKey";
long keyDuration = 600; //Validity of SecretKey (in sec)

//Create a CosXmlServiceConfig object to modify the default configuration parameter as needed
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
       .setAppidAndRegion(appid, region)
       .setDebuggable(true)
       .builder();

//Create a class for getting signature (see the following example for generating a signature, or refer to the ShortTimeCredentialProvider class provided in SDK)
LocalCredentialProvider localCredentialProvider = new LocalCredentialProvider(secretId, secretKey, keyDuration);

//Create a CosXmlService object to implement the COS operations.
Context context = getApplicationContext(); //Context of the application

CosXmlService cosXmlService = new CosXmlService(context,cosXmlServiceConfig, localCredentialProvider);
````

### Simple upload of files

````java
String bucket = "bucket name"; //bucket format of cos v5: xxx-appid, such as test-1253960454
String cosPath = "[object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS"; //for example: cosPath = "test.txt";
String srcPath = "absolute path to the local file"; //for example: srcPath = Environment.getExternalStorageDirectory().getPath() + "/test.txt";
long signDuration = 600; //Validity of the signature (in sec)

PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);

putObjectRequest.setSign(signDuration,null,null); //If it is not called, sign duration (60s) in the SDK is used by default

/*Set progress display
  Implement the CosXmlProgressListener.onProgress(long progress, long max) method,
  progress indicates the uploaded size, and max indicates the total size of the file
*/
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

//Upload using an asynchronous callback: SDK provides an asynchronous callback method for the COS services
/**

cosXmlService.putObjectAsync(putObjectRequest, new CosXmlResultListener() {
     @Override
     public void onSuccess(CosXmlRequest request, CosXmlResult result) {
      	 Log.w("TEST","success =" + result.accessUrl);
     }

     @Override
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException)  {
        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/

````

### Multipart upload

Multipart upload generally involves three steps: initializing multipart upload -> performing multipart upload -> completing upload.

````java
String bucket = "bucket name"; //bucket format of cos v5: xxx-appid, such as test-1253960454
String cosPath = "[object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS";


//First, initialize the multipart upload to obtain the uploadId, which is used for subsequent multipart uploads, completion of uploads, etc.

String uploadId = null;

InitMultipartUploadRequest initMultipartUploadRequest =  new InitMultipartUploadRequest(bucket, cosPath);

initMultipartUploadRequest.setSign(600,null,null);
try {
	InitMultipartUploadResult initMultipartUploadResult =
                  cosXmlService.initMultipartUpload(initMultipartUploadRequest);

	//If the initialization is successful, get the uploadId;
   Log.w("TEST","success");
   uploadId = initMultipartUploadResult.initMultipartUpload.uploadId;

} catch (CosXmlClientException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlClientException =" + e.toString());
  } catch (CosXmlServiceException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

//Second, multipart upload requires the parameters uploadId and partNumber; the corresponding eTag number is also needed. This example only shows the upload of the first part in a multipart upload.
//Part number: The number of current part among all parts, which starts from 1
//etag: The combination of MD5 returned when the part is uploaded successfully and the part number.

String srcPath = "Absolute path to the local file";
int partNumber = 1; //number of the part to be uploaded, starting from 1; this example shows the upload of the first part

String eTag = null;

UploadPartRequest uploadPartRequest = new UploadPartRequest(bucket, cosPath, partNumber,
srcPath, uploadId);

uploadPartRequest.setSign(600,null,null);

/*Set progress display
  Implement the CosXmlProgressListener.onProgress(long progress, long max) method,
  progress indicates the uploaded size, and max indicates the total size of the file
*/
uploadPartRequest.setProgressListener(new CosXmlProgressListener() {
	 @Override
	 public void onProgress(long progress, long max) {
	     float result = (float) (progress * 100.0/max);
	     Log.w("TEST","progress =" + (long)result + "%");
	   }
	});

try {
	UploadPartResult uploadPartResult = cosXmlService.uploadPart(uploadPartRequest); 
	
	Log.w("TEST","success");	
	eTag = uploadPartResult.eTag; //Get the eTag of the part

  } catch (CosXmlClientException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlClientException =" + e.toString());
  } catch (CosXmlServiceException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}


//Third, when all the parts have been uploaded, complete the multipart upload by calling CompleteMultiUploadRequest.
//The parameters uploadId, partNumber, and the eTag value for each part are required

CompleteMultiUploadRequest completeMultiUploadRequest = new CompleteMultiUploadRequest(bucket, cosPath, uploadId, null);

completeMultiUploadRequest.setPartNumberAndEtag(partNumber, eTag); //This example only shows the upload of one part

completeMultiUploadRequest.setSign(600,null,null);
try {
	CompleteMultiUploadResult completeMultiUploadResult =
	                    cosXmlService.completeMultiUpload(completeMultiUploadRequest);
											
	Log.w("TEST","success: " + completeMultiUploadResult.accessUrl );

  } catch (CosXmlClientException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlClientException =" + e.toString());
  } catch (CosXmlServiceException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}
````

### UploadService is recommended for multipart upload

````java
//UploadService encapsulates the classes for a series of procedures for the above multipart upload request

 UploadService.ResumeData resumeData = new UploadService.ResumeData();
 resumeData.bucket = "bucket name";
 resumeData.cosPath = "[object key](https://cloud.tencent.com/document/product/436/13324),, which is the absolute path to the storage on COS"; //for example: cosPath = "test.txt";
 resumeData.srcPath = "absolute path to the local file"; //for example: srcPath =Environment.getExternalStorageDirectory().getPath() + "/test.txt";
 resumeData.sliceSize = 1024 * 1024; //size of each part
 resumeData.uploadId = null; //For a resumed upload, uploadId cannot be empty


 UploadService uploadService = new UploadService(cosXmlService, resumeData);

/*Set progress display
  Implement the CosXmlProgressListener.onProgress(long progress, long max) method,
  progress indicates the uploaded size, and max indicates the total size of the file
*/
uploadService.setProgressListener(new CosXmlProgressListener() {
    @Override
    public void onProgress(long progress, long max) {
        float result = (float) (progress * 100.0/max);
        Log.w("TEST","progress =" + (long)result + "%");
    }
});
try {
	CosXmlResult cosXmlResult = uploadService.upload();
									
	Log.w("TEST","success: " + cosXmlResult.accessUrl );

  } catch (CosXmlClientException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlClientException =" + e.toString());
  } catch (CosXmlServiceException e) {

	   //Throw an exception
       Log.w("TEST","CosXmlServiceException =" + e.toString());
}

````

 
### Downloading files
````java
String bucket = "bucket name"; //bucket format of cos v5: xxx-appid, such as test-1253960454
String cosPath = "[object key](https://cloud.tencent.com/document/product/436/13324), which is the absolute path to the storage on COS";
String savePath = "path to the file downloaded to the local machine";

GetObjectRequest getObjectRequest = GetObjectRequest(bucket, cosPath, savePath);
getObjectRequest.setSign(signDuration,null,null);

/*Set progress display
  Implement the CosXmlProgressListener.onProgress(long progress, long max) method,
  progress indicates the uploaded size, and max indicates the total size of the file
*/
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
     public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException)  {        
		String errorMsg = clientException != null ? clientException.toString() : serviceException.toString();
		Log.w("TEST",errorMsg);
    }
});

*/
````

## Generating Signature

For more information on how to generate a signature, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778).
The SDK you are using has provided the class for getting signature. You simply need to inherit the BasicLifecycleCredentialProvider class and override the fetchNewCredentials() method to obtain the SecretId, SecretKey, and SecretKey Duration. To send the request using the temporary key, you need to obtain the tempSecretKey, tempSecrekId, sessionToken and expiredTime. For more information on how to obtain a temporary key via CAM, please see [Quick Setup of Mobile Application Transfer Service](/document/product/436/9068).

#### Example
````java
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

     public LocalCredentialProvider(String tempSecretId, String tempSecretKey, String sessionToken, long expiredTime) {
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
````

