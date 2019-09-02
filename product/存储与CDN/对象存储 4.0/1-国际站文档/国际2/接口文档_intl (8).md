For a successful COS XML JAVA SDK operation, a specific type for each API is returned. For a failed operation, an exception (CosClientException and CosServiceException) is reported. CosClientException refers to client exceptions, such as network exceptions and request sending failure. CosServiceException contains the reasons why the client request is identified as a failure by the server. For example, you do not have such permission, or the file you want to access does not exist. For more information, please see Exception Types.
The following describes how to use each API in the SDK. For the sake of brevity, subsequent examples only illustrate how to use the API rather than how to capture exceptions.

```java
try {
   // The bucket name entered must be in a format of {name}-{appid}.
   String bucketName = "movie-1251668577";
   String key = "abc/def.jpg";
   cosclient.deleteObject(bucket, key);
} catch (CosClientException cle) {
  // Custom exception handling, such as print exceptions
  log.error("del object failed.", cle);
  // ...
} catch (CosServiceException cse) {
   // Custom exception handling, such as print exceptions
  log.error("del object failed.", cse);
  // ...
}
```

## Bucket API Description

### Put Bucket
This API (Put Bucket) is used to create a Bucket. As a limited resource, Bucket is not the same as directory, and the number of files under a Bucket is unlimited, so it is recommended not to create too many Buckets. Generally, you do not need to create a Bucket frequently. You are advised to create a Bucket on the console and work with the Object using SDK.

- **Method prototype**

```java
public Bucket createBucket(String  bucketName) throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: Bucket type, including the description of Bucket (bucket name, owner, and creation date).

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
Bucket bucket = cosClient.createBucket(bucketName);
```

### Delete Bucket

This API (Delete Bucket) is used to delete the cleared Buckets.

- **Method prototype**

```java
 public void deleteBucket(String bucketName) throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
cosClient.deleteBucket(bucketName);
```

### Head Bucket

This API (Head Bucket) is used to query whether a bucket exists.

- **Method prototype**

```java
public boolean doesBucketExist(String bucketName) 
  throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: "true" is returned if the queried bucket exists. Otherwise, "false" is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
boolean bucketExistFlag = cosClient.doesBucketExist(bucketName);
```

### Get Bucket Location

This API (Get Bucket Location) is used to query the Region where a Bucket resides.

- **Method prototype**

```java
public String getBucketLocation(String bucketName) 
  throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: The Region where a Bucket resides is returned. 

	- Failed: CosClientException or CosServiceException is thrown when an error (such as Bucket does not exist) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String location = cosClient.getBucketLocation("movie-1251668577");
```

### Get Bucket (List Objects)

This API (Get Bucket) is used to obtain the file list on the COS.

- **Method prototype**

```java

public ObjectListing listObjects(ListObjectsRequest listObjectsRequest)
            throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ------------------ | -------- | ------------------ |
| listObjectsRequest | Request for obtaining a file list  ListObjectsRequest |

Request member description:

| Request Member | Setting Method | Description | Type |
| ---------- | ------------ | ---------------------------------------- | ------ |
| bucketName | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String |
| prefix     | Constructor or set method | Marks members prefixed with "prefix" in the list. By default, no restriction is set. That is, all members under the Bucket are included. <br> Default: "" |  String |
|   marker   | Constructor or the set method | Marks the starting position of the list. It is empty for the first time. Subsequently, the value returned by the previous list is the marker. | String  
| delimiter  | Constructor or set method | Delimiter. It indicates that the path that starts with "prefix" and ends with delimiter for the first time will be returned. | String  
|  maxKeys   | Constructor or set method | The maximum number of returned members (less than 1,000). <br>Default: 1,000 |Integer |  

- **Returned value**

	- Successful: Return ObjectListing type, including all members and nextMarker.  

	- Failed: CosClientException or CosServiceException is thrown. For more information, please see Exception Types.

-  **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";

// Obtain the bucket members (set delimiter)
ListObjectsRequest listObjectsRequest = new ListObjectsRequest();
listObjectsRequest.setBucketName(bucketName);
// Set a prefix for the list, indicating that all the file keys in the list start with this prefix
listObjectsRequest.setPrefix("");
// Set delimiter to /, indicating the direct members (excluding the recursive submembers) under the directory are obtained
listObjectsRequest.setDelimiter("/");
// Set marker (the first list marker is empty, and subsequent marker is obtained from the previous list)
listObjectsRequest.setMarker("");
// Set the maximum of number of members that can be listed to 100 (if not set, the default is 1,000, and a maximum of 1,000 keys can be listed at a time)
listObjectsRequest.setMaxKeys(100);

ObjectListing objectListing = cosClient.listObjects(listObjectsRequest);
// Obtain the marker for the next list
String nextMarker = objectListing.getNextMarker();
// Check whether the list is completed. If the list is completed, isTruncated is false, otherwise it is true.
boolean isTruncated = objectListing.isTruncated();
List<COSObjectSummary> objectSummaries = objectListing.getObjectSummaries();
for (COSObjectSummary cosObjectSummary : objectSummaries) {
    // File path
    String key = cosObjectSummary.getKey();
    // Obtain file length
    long fileSize = cosObjectSummary.getSize();
    // Obtain file ETag
    String eTag = cosObjectSummary.getETag();
    // Obtain the last modification time
    Date lastModified = cosObjectSummary.getLastModified();
    // Obtain file storage type
    String StorageClassStr = cosObjectSummary.getStorageClass();
}
```

### Bucket ACL

This API (Set Bucket ACL) is used to set the access control list of the Bucket.

If Set Bucket ACL is performed, existing permission configuration will be overwritten.

ACL includes a predefined permission policy (CannedAccessControlList) or a custom permission control (AccessControlList). If both of them are set, the predefined policy will be ignored and the custom policy prevails. For more information on permissions, please see the permission section.

- **Method prototype**

```java
// Method 1 (Set custom policy)
public void setBucketAcl(String bucketName, AccessControlList acl)
  throws CosClientException, CosServiceException;
// Method 2 (Set predefined policy)
public void setBucketAcl(String bucketName, CannedAccessControlList acl) throws CosClientException, CosServiceException;
// Method 3 (Encapsulation of the two methods above, including setting of these two policies. If both of them are set, the custom policy prevails.)
public void setBucketAcl(SetBucketAclRequest setBucketAclRequest) 
  throws CosClientException, CosServiceException;
```

- **Parameter description**

Parameters in Method 3 contain those in Method 1 and 2, so the following takes Method 3 as an example to describe these parameters.

| Parameter Name | Description | Type |
| ------------------- | ------- | ------------------- |
| setBucketAclRequest | Indicates permission configuration request  SetBucketAclRequest |
Request member description:

| Request Member | Setting Method | Description | Type |
| ---------- | ------------ | ---------------------------------------- | ----------------------- |
| bucketName | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String                  |
| acl        | Constructor or set method | Custom permission policy |  AccessControlList       |
| cannedAcl  | Constructor or set method | Predefined policies, such as public read, public read and write, private read |  CannedAccessControlList |

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
// Set a custom ACL
AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);
String id = "qcs::cam::uin/2779643970:uin/734505014";
UinGrantee uinGrantee = new UinGrantee("qcs::cam::uin/2779643970:uin/734505014");
uinGrantee.setIdentifier(id);
acl.grantPermission(uinGrantee, Permission.FullControl);
cosclient.setBucketAcl(bucketName, acl);

// Set a predefined ACL
// Set private read and write (New buckets are configured with private read and write by default)
cosclient.setBucketAcl(bucketName, CannedAccessControlList.Private);
// Set public read and private write
cosclient.setBucketAcl(bucketName, CannedAccessControlList.PublicRead);
// Set public read and write
cosclient.setBucketAcl(bucketName, CannedAccessControlList.PublicReadWrite);
```

### Get Bucket ACL

This API (Get Bucket ACL) is used to query the access policy ACL of a Bucket.

- **Method prototype**

```java
public AccessControlList getBucketAcl(String bucketName)
       throws CosClientException, CosServiceException
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: The ACL of a Bucket is returned. 

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
AccessControlList acl = cosclient.getBucketAcl(bucketName);
```

### Set Bucket CORS

This API (Set Bucket CORS) is used to set cross-origin access rules for a bucket.

- **Method prototype**

```java
public void setBucketCrossOriginConfiguration(String bucketName, BucketCrossOriginConfiguration bucketCrossOriginConfiguration);
```

- **Parameter description**

| Parameter Name | Description | Type |
| ------------------------------ | ---------------------------------------- | ------------------------------ |
| bucketName                     | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String                         |
| bucketCrossOriginConfiguration | The cross-origin access rules set for a bucket  BucketCrossOriginConfiguration |

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
BucketCrossOriginConfiguration bucketCORS = new BucketCrossOriginConfiguration();
List<CORSRule> corsRules = new ArrayList<>();
CORSRule corsRule = new CORSRule();
// Rule name
corsRule.setId("set-bucket-cors-test");  
// Allowed HTTP method
corsRule.setAllowedMethods(AllowedMethods.PUT, AllowedMethods.GET, AllowedMethods.HEAD);
corsRule.setAllowedHeaders("x-cos-grant-full-control");
corsRule.setAllowedOrigins("http://mail.qq.com", "http://www.qq.com",
        "http://video.qq.com");
corsRule.setExposedHeaders("x-cos-request-id");
corsRule.setMaxAgeSeconds(60);
corsRules.add(corsRule);
bucketCORS.setRules(corsRules);
cosclient.setBucketCrossOriginConfiguration(bucketName, bucketCORS);
```

### Get Bucket CORS

This API (Get Bucket CORS) is used to obtain the cross-origin access rules of a bucket.

- **Method prototype**

```java
public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(String bucketName)
     throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: The cross-origin rules of a Bucket are returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
BucketCrossOriginConfiguration corsGet = cosclient.getBucketCrossOriginConfiguration(bucketName);
List<CORSRule> corsRules = corsGet.getRules();
for (CORSRule rule : corsRules) {
    List<AllowedMethods> allowedMethods = rule.getAllowedMethods();
    List<String> allowedHeaders = rule.getAllowedHeaders();
    List<String> allowedOrigins = rule.getAllowedOrigins();
    List<String> exposedHeaders = rule.getExposedHeaders();
    int maxAgeSeconds = rule.getMaxAgeSeconds();
}
```

### Delete Bucket CORS

This API (Delete Bucket CORS) is used to delete the cross-origin access rules of a bucket.

- **Method prototype**

```java
public void deleteBucketCrossOriginConfiguration(String bucketName)
     throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
cosclient.deleteBucketCrossOriginConfiguration(bucketName);
```

### Set Bucket LifeCycle

This API (Set Bucket LifeCycle) is used to set the lifecycle rules of a bucket.

- **Method prototype**

```java
public void setBucketLifecycleConfiguration(String bucketName, BucketLifecycleConfiguration bucketLifecycleConfiguration) throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
List<Rule> rules = new ArrayList<>();
// Rule 1: Delete files whose paths start with hongkong_movie/ after 30 days
Rule deletePrefixRule = new Rule();
deletePrefixRule.setId("delete prefix xxxy after 30 days");
deletePrefixRule
        .setFilter(new LifecycleFilter(newLifecyclePrefixPredicate("hongkong_movie/")));
// Delete files that have been uploaded or modified for 30 days
deletePrefixRule.setExpirationInDays(30);
// Set rules to active
deletePrefixRule.setStatus(BucketLifecycleConfiguration.ENABLED);

// Rule 2: Put files into low frequency after 20 days and delete them after one year
Rule standardIaRule = new Rule();
standardIaRule.setId("standard_ia transition");
standardIaRule.setFilter(new LifecycleFilter(new LifecyclePrefixPredicate("standard_ia/")));
List<Transition> standardIaTransitions = new ArrayList<>();
Transition standardTransition = new Transition();
standardTransition.setDays(20);
standardTransition.setStorageClass(StorageClass.Standard_IA.toString());
standardIaTransitions.add(standardTransition);
standardIaRule.setTransitions(standardIaTransitions);
standardIaRule.setStatus(BucketLifecycleConfiguration.ENABLED);
standardIaRule.setExpirationInDays(365);
		
// Add two rules to the policy set
rules.add(deletePrefixRule);
rules.add(standardIaRule);

// Generate bucketLifecycleConfiguration
BucketLifecycleConfiguration bucketLifecycleConfiguration =
        new BucketLifecycleConfiguration();
bucketLifecycleConfiguration.setRules(rules);

// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
SetBucketLifecycleConfigurationRequest setBucketLifecycleConfigurationRequest =
      new SetBucketLifecycleConfigurationRequest(bucketName, bucketLifecycleConfiguration);

// Set the lifecycle
cosclient.setBucketLifecycleConfiguration(setBucketLifecycleConfigurationRequest);
```

### Get Bucket LifeCycle

This API (Get Bucket LifeCycle) is used to obtain the lifecycle rules of a bucket.

- **Method prototype**

```java
public BucketLifecycleConfiguration getBucketLifecycleConfiguration(String bucketName)
            throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: Return BucketLifecycleConfiguration type, including the lifecycle rules of the bucket.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
BucketLifecycleConfiguration queryLifeCycleRet =
        cosclient.getBucketLifecycleConfiguration(bucketName);
List<Rule> ruleLists = queryLifeCycleRet.getRules();
```

### Delete Bucket LifeCycle

This API (Delete Bucket LifeCycle) is used to delete the lifecycle rules of the cleared bucket.

- **Method prototype**

```java
public void deleteBucketLifecycleConfiguration(String bucketName)
         throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
cosclient.deleteBucketLifecycleConfiguration(bucketName);
```

## Object API Description

### PUT Object (Upload Object)

Upload a local file or input stream with a known length to COS. This is suitable for the upload of small files such as images below 20 MB. The maximum file size supported is 5 GB (inclusive). To upload a file greater than 5 GB, use multipart upload. If the object already exists on the COS, it will be overwritten.

- **Method prototype**

```java
// Method 1: Upload a local file to COS
public PutObjectResult putObject(String bucketName, String key, File file)
            throws CosClientException, CosServiceException;
// Method 2: Upload an input stream to COS
public PutObjectResult putObject(String bucketName, String key, InputStream input,
            ObjectMetadata metadata) throws CosClientException, CosServiceException;
// Method 3: Encapsulate the two methods above to support more fine-grained parameter control, such as content-type and content-disposition
public PutObjectResult putObject(PutObjectRequest putObjectRequest)
            throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------------- | ------ | ---------------- |
| putObjectRequest | File upload request | PutObjectRequest |
Request member description:

| Request Member | Setting Method | Description | Type |
| ---------- | ------------ | ---------------------------------------- | -------------- |
| bucketName | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String         |
| key        | Constructor or set method | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                | String         |.
| file       | Constructor or set method | Local file |  File           |
| input      | Constructor or set method | Input stream |  InputStream    |
| metadata   | Constructor or set method | Meta information of a file |  ObjectMetadata |

- **Returned value**

	- Successful: PutObjectResult, including the file ETag and other information.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
// Method 1: Upload a local file
File localFile = new File("/data/test.txt");
String key = "aaa.txt";
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, localFile);
// Obtain file ETag

// Method 2: Upload an input stream (The length of a input stream must be known in advance. Otherwise, it may cause OOM)
FileInputStream fileInputStream = new FileInputStream(localFile);
ObjectMetadata objectMetadata = new ObjectMetadata();
// Set the length of an input stream to 500
objectMetadata.setContentLength(500);  
// Set Content type. Default is application/octet-stream
objectMetadata.setContentType("application/pdf");
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, fileInputStream, objectMetadata);
String etag = putObjectResult.getETag();
// Close the input stream...

// Method 3: Provide more fine-grained control. Common settings are as follows
// 1. storage-class storage type, including standard (default), low frequency, and nearline
// 2. content-type. For local file upload, the files are mapped based on the suffix by default. For example, the jpg file is mapped //as image/jpeg
// For input stream upload, the default is application/octet-stream
// 3. Set permissions when uploading (or by calling API set object ACL)
File localFile = new File("/data/dog.jpg");
String key = "mypic.jpg";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, file);
// Set the storage type to low frequency
putObjectRequest.setStorageClass(StorageClass.Standard_IA);
// Set custom attributes (such as content-type, content-disposition)
ObjectMetadata objectMetadata = new ObjectMetadata();
// Set Content type. Default is application/octet-stream
objectMetadata.setContentType("image/jpeg");
putObjectRequest.setMetadata(objectMetadata);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
String etag = putObjectResult.getETag();  // Obtain file ETag
```

-  **Multipart upload**

Multipart upload is to split a file into multiple parts for upload. A maximum of 40 TB of parts can be uploaded concurrently.

The steps of multipart upload are as follows:

1. Initialize multipart upload, and obtain uploadid. (initiateMultipartUpload)
2. Upload data in parts (concurrently). (uploadPart)
3. Complete multipart upload. (completeMultipartUpload)

In addition, you can also obtain the uploaded parts (listParts) or terminate multipart upload (abortMultipartUpload). Multipart upload has complicated steps and high requirements for use, so it is recommended to use the following advanced and encapsulated API for upload.

- **Method prototype**

```java
// Method 1: Initialize multipart upload
public InitiateMultipartUploadResult initiateMultipartUpload(
    InitiateMultipartUploadRequest request) throws CosClientException, CosServiceException;
// Method 2: Upload data in parts
public UploadPartResult uploadPart(UploadPartRequest uploadPartRequest)
            throws CosClientException, CosServiceException;
// Method 3: Complete multipart upload
public CompleteMultipartUploadResult completeMultipartUpload(
            CompleteMultipartUploadRequest request) throws CosClientException, CosServiceException;
// Method 4: List uploaded parts
public PartListing listParts(ListPartsRequest request)
            throws CosClientException, CosServiceException;
// Method 5: Terminate multipart upload
public void abortMultipartUpload(AbortMultipartUploadRequest request)
            throws CosClientException, CosServiceException;
```

- **Returned value**

 - **Method 1 (initiateMultipartUpload)**

	 - Successful: Return InitiateMultipartUploadResult type, including the upload ID required for subsequent multipart upload.

	 - Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

 - **Method 2 (uploadPart)**

	 - Successful: Return UploadPartResult, including the Etag and partNumber of the part.

	 - Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

 - **Method 3 (completeMultipartUpload)**

	 - Successful: Return CompleteMultipartUploadResult, including the Etag of the entire file. 

	 - Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

 - **Method 4 (listParts)**

	 - Successful: Return PartListing, including the ETag and No. of each part as well as the starting marker of the next list.

	 - Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

 - **Method 5 (abortMultipartUpload)**

	 - Successful: No value is returned.

	 - Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
// Initialize multipart upload
InitiateMultipartUploadRequest initRequest =
                new InitiateMultipartUploadRequest(bucketName, key);
InitiateMultipartUploadResult initResponse = cosClient.initiateMultipartUpload(initRequest);
String uploadId = initResponse.getUploadId()
// Upload parts. A maximum of 1,000 parts can be uploaded concurrently. The size of each part should be between 1 MB and 5 GB.
// Set the size of each part to 4 MB. If there are a total of n parts, the size of part 1 to part n-1 is the same, and the last part is less than or equal to the size of previous parts.
List<PartETag> partETags = new ArrayList<PartETag>();
int partNumber = 1;
int partSize = 4 * 1024 * 1024;
// partStream represents the input stream of the part's data. The length of input stream is partSize.
UploadPartRequest uploadRequest =  new    UploadPartRequest().withBucketName(bucketName).
 withUploadId(uploadId).withKey(key).withPartNumber(partNumber).
  withInputStream(partStream).withPartSize(partSize);  
UploadPartResult uploadPartResult = cosClient.uploadPart(uploadRequest);
String eTag = uploadPartResult.getETag();  // Obtain the Etag of the part
partETags.add(new PartETag(partNumber, eTag));  // partETags records Etag information of all uploaded parts
partETags.add(new PartETag(partNumber, eTag));  // Upload parts with the partNumber of 2 to n

// Complete multipart upload.
CompleteMultipartUploadRequest compRequest = new CompleteMultipartUploadRequest(bucketName, key,
           uploadId, partETags);
CompleteMultipartUploadResult result =  cosClient.completeMultipartUpload(compRequest);

// ListPart is used to obtain the information of the uploaded part based on uploadId before the multipart upload is completed or aborted. It can be used to construct partEtags.
ListPartsRequest listPartsRequest = new ListPartsRequest(bucket, key, uploadId);
do {
      partListing = cosclient.listParts(listPartsRequest);
      for (PartSummary partSummary : partListing.getParts()) {
           partETags.add(new PartETag(partSummary.getPartNumber(), partSummary.getETag()));
      }
      listPartsRequest.setPartNumberMarker(partListing.getNextPartNumberMarker());
} while (partListing.isTruncated());

// abortMultipartUpload is used to abort an uncompleted multipart upload
AbortMultipartUploadRequest abortMultipartUploadRequest = 
  									new AbortMultipartUploadRequest(bucket, key, uploadId);
cosclient.abortMultipartUpload(abortMultipartUploadRequest);
```

### Get Object

Download files to local machine or obtain the download input streams for downloading files.

- **Method prototype**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
// Method 1: Download the file and get the input stream
public COSObject getObject(GetObjectRequest getObjectRequest)
            throws CosClientException, CosServiceException;
// Method 2: Download the file locally
public ObjectMetadata getObject(GetObjectRequest getObjectRequest, File destinationFile)
            throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------------- | ------- | ---------------- |
| getObjectRequest | File download request  GetObjectRequest |
| destinationFile  | File stored locally | File             |
Request member description:

| Request Member | Setting Method | Description | Type |
| ---------- | ------------ | ---------------------------------------- | ------ |
| bucketName | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String |
| key        | Constructor or set method | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                | String |.
| range      | Set method | The range of download |  Long[] |

- **Returned value**

 - **Method 1 (Get the input stream of the downloaded file)**

	 - Successful: Return COSObject type, including the input stream and file attributes.

	 - Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

 - **Method 2 (Download the file locally)**

	 - Successful: Return the file attribute objectMetadata, including the file's custom header, content-type and other attributes.

	 - Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
// Method 1: Get the input stream of the downloaded file
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
COSObject cosObject = cosClient.getObject(getObjectRequest);
COSObjectInputStream cosObjectInput = cosObject.getObjectContent();

// Method 2: Download the file locally
File downFile = new File("src/test/resources/mydown.txt");
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
ObjectMetadata downObjectMeta = cosClient.getObject(getObjectRequest, downFile);
```

### Delete Object

This API (Delete Object) is used to delete files on COS.

- **Method prototype**

```java
// Delete files
public void deleteObject(String bucketName, String key)
            throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |
| key        | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                     | String |.

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// Delete files on COS
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
cosclient.deleteObject(bucket, key);
```

### Head Object

This API (Head Object) is used to get the attributes of a file on COS.

- **Method prototype**

```java
// Obtain file attributes
public ObjectMetadata getObjectMetadata(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |
| key        | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                    | String |.

- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// Obtain the attributes of a file on COS
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
ObjectMetadata objectMetadata = cosclient.getObjectMetadata(bucketName, key);
```

### Put Object Copy

This API (Put Object Copy) is used to copy the Object to a new path or bucket. It supports cross-region/account/bucket copy, and needs the read permission to the source file and the write permission to the destination file. The maximum allowed file size is 5 GB. To copy files larger than 5 GB, use the advanced API.

- **Method prototype**

```java
// Obtain file attributes
public CopyObjectResult copyObject(CopyObjectRequest copyObjectRequest)
      throws CosClientException, CosServiceException
```

- **Parameter description**

| Parameter Name | Description | Type |
| ----------------- | ------ | ----------------- |
| copyObjectRequest | File copy request | CopyObjectRequest |

Request member description:

| Parameter Name | Description | Type |
| --------------------- | ---------------------------------------- | ------ |
| sourceBucketRegion    | Region of the source Bucket. Default: same with the region of the current clientconfig, which represents an intra-region copy |  String |
| sourceBucketName      | Source Bucket name. The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |
| sourceKey             | Source object key. Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                    | String |.
| sourceVersionId       | Version ID of the source file with multiple versions. Default: The latest version of the source file | String |
| destinationBucketName | Destination Bucket name. The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |
| destinationKey        | Destination object key. Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                   | String |.
| storageClass          | The storage type of the copied destination file (standard, low frequency, nearline). Default: Standard | String |

- **Returned value**

	- Successful: Return CopyObjectResult, including Etag and other information of the new file.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// Intra-region copy with the same account
// Source bucket. The bucket entered must be in a format of {name}-{appid}
String srcBucketName = "srcBucket-1251668577";
// The source file to copy
String srcKey = "aaa/bbb.txt";
// Destination bucket. The bucket entered must be in a format of {name}-{appid}
String destBucketName = "destBucket-1251668577";
// The destination file to copy
String destKey = "ccc/ddd.txt";
CopyObjectRequest copyObjectRequest = new CopyObjectRequest(srcBucketName, srcKey, destBucketName, destKey);
CopyObjectResult copyObjectResult = cosclient.copyObject(copyObjectRequest);

// Cross-account and cross-region copy (The read permission to source file and the write permission to destination file are required)
String srcBucketNameOfDiffAppid = "srcBucket-125100000";
Region srcBucketRegion = new Region("ap-shanghai");
copyObjectRequest = new CopyObjectRequest(srcBucketRegion, srcBucketNameOfDiffAppid, srcKey, destBucketName, destKey);
copyObjectResult = cosclient.copyObject(copyObjectRequest);
```

### Set Object ACL

This API (Set Object ACL) is used to set the Access Control List of the Object. If Set Bucket ACL is performed, existing permission configuration will be overwritten.
The object inherits the bucket permission by default. COS only supports setting 1,000 ACL rules for an account (appid), so it is recommended to set ACL only for objects with inconsistent bucket permission to prevent the number of permission from exceeding the threshold. The function of unlimited ACL is under development.

ACL includes a predefined permission policy (CannedAccessControlList) or a custom permission control (AccessControlList). If both of them are set, the predefined policy will be ignored and the custom policy prevails. For more information on permissions, please see the permission section.

- **Method prototype**

```java
// Method 1 (Set custom policy)
public void setObjectAcl(String bucketName, String key, AccessControlList acl)
       throws CosClientException, CosServiceException
 Method 2 (Set predefined policy)
public void setObjectAcl(String bucketName, String key, CannedAccessControlList acl)
       throws CosClientException, CosServiceException
 Method 3 (Encapsulation of the two methods above, including setting of these two policies. If both of them are set, the custom policy prevails.)
public void setObjectAcl(SetObjectAclRequest setObjectAclRequest)
  throws CosClientException, CosServiceException;
```

- **Parameter description**

	- Parameters in **Method 3** contain those in Method 1 and 2, so the following takes Method 3 as an example to describe these parameters.

| Parameter Name | Description | Type |
| ------------------- | ------- | ------------------- |
| SetObjectAclRequest | Request type | setObjectAclRequest |
Request member description:

| Request Member | Setting Method | Description | Type |
| ---------- | ------------ | ---------------------------------------- | ----------------------- |
| bucketName | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String                  |
| key        | Constructor or set method | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                 | String                  |.
| acl        | Constructor or set method | Custom permission policy |  AccessControlList       |
| cannedAcl  | Constructor or set method | Predefined policies, such as public read, public read and write, private read |  CannedAccessControlList |


- **Returned value**

	- Successful: No value is returned.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
// Set a custom ACL
AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);
String id = "qcs::cam::uin/2779643970:uin/734505014";
UinGrantee uinGrantee = new UinGrantee("qcs::cam::uin/2779643970:uin/734505014");
uinGrantee.setIdentifier(id);
acl.grantPermission(uinGrantee, Permission.FullControl);
cosclient.setObjectAcl(buckeName, key, acl);

// Set a predefined ACL
// Set private read and write (Object integrates permissions of Bucket by default)
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.Private);
// Set public read and private write
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicRead);
// Set public read and write
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicReadWrite);
```

### Get Object ACL

This API (Get Object ACL) is used to query the ACL of an Object.

- **Method prototype**

```java
public AccessControlList getObjectAcl(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------- | ---------------------------------------- | ------ |
| bucketName | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. | String |
| key        | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                     | String |.

- **Returned value**

	- Successful: Return the ACL to which the Object resides.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
AccessControlList acl = cosclient.getObjectAcl(bucketName, key);
```

## Generating a Pre-Signed URL

In COSClient, you can construct or generate a pre-signed URL that can be distributed to clients for download or upload.

- **Method prototype**

```java
// Construct a pre-signed URL
public URL generatePresignedUrl(GeneratePresignedUrlRequest req) throws CosClientException
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---- | ------ | --------------------------- |
| req  | Pre-signed request | GeneratePresignedUrlRequest |
Request member description:

| Request Member | Setting Method | Description | Type |
| --------------- | ------------ | ---------------------------------------- | ----------------------- |
| method          | Constructor or set method | HTTP method. Available values: PUT, GET, and DELETE | HttpMethodName          |
| bucketName      | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String                  |
| key             | Constructor or set method | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                 | String                  |.
| expiration      | set method | Signature expiration time |  Date                    |
| contentType     | set method | Content-Type in the request that needs a signature |  String                  |
| contentMd5      | set method | Content-Md5 in the request that needs a signature |  String                  |
| responseHeaders | set method | The returned http header to be overridden in the request to download a signature |  ResponseHeaderOverrides |

- **Returned value**

URL

- **Example**

Example 1. Generate a signed download URL. The sample code is as follows:

```java
// Generate a download URL
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "mybucket-1251668577";
String key = "aaa.txt";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// Set the signature expiration time (optional). If it is not set, the signature expiration time (5 minutes) in ClientConfig is used by default.
// The set signature will expire in half an hour
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
req.setExpiration(expirationDate);
URL downloadUrl = cosclient.generatePresignedUrl(req);
String downloadUrlStr = downloadUrl.toString();
```

Example 2. Generate a signed download URL and set to override the public headers (such as content-type and content-language) to be returned. The sample code is as follows:

```java
// The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. 
String bucketName = "mybucket-1251668577";
String key = "aaa.txt";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// Set the http header returned during download
ResponseHeaderOverrides responseHeaders = new ResponseHeaderOverrides();
String responseContentType = "image/x-icon";
String responseContentLanguage = "zh-CN";
String responseContentDispositon = "filename=\"abc.txt\"";
String responseCacheControl = "no-cache";
String cacheExpireStr =
        DateUtils.formatRFC822Date(new Date(System.currentTimeMillis() + 24L * 3600L * 1000L));
responseHeaders.setContentType(responseContentType);
responseHeaders.setContentLanguage(responseContentLanguage);
responseHeaders.setContentDisposition(responseContentDispositon);
responseHeaders.setCacheControl(responseCacheControl);
responseHeaders.setExpires(cacheExpireStr);
req.setResponseHeaders(responseHeaders);
// Set the signature expiration time (optional). If it is not set, the signature expiration time (5 minutes) in ClientConfig is used by default.
// The set signature will expire in half an hour
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
req.setExpiration(expirationDate);
URL url = cosclient.generatePresignedUrl(req);
```

Example 3. Generate public buckets (anonymous and readable) that do not need signed URLs. The sample code is as follows:

```java
// To generate an anonymous request signature, you need to reinitialize an anonymous COSClient
// 1. Initialize a user's identity information. For an anonymous identity, ak sk does not need to be input
COSCredentials cred = new AnonymousCOSCredentials();
// 2. Set the region where the bucket resides. For the abbreviations of COS regions, please see https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3. Generate the COS client
COSClient cosclient = new COSClient(cred, clientConfig);
// The bucket name must contain appid
String bucketName = "mybucket-1251668577";

String key = "aaa.txt";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
URL url = cosclient.generatePresignedUrl(req);

System.out.println(url.toString());

cosclient.shutdown();
```

Example 4. Generate some pre-signed upload URLs that can be directly distributed to the client for file uploads. The sample code is as follows:

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "mybucket-1251668577";

String key = "aaa.txt";
// Set the signature expiration time (optional). If it is not set, the signature expiration time (5 minutes) in ClientConfig is used by default.
// The set signature will expire in half an hour
Date expirationTime = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
URL url = cosclient.generatePresignedUrl(bucketName, key, expirationTime, HttpMethodName.PUT);
```


## Generating Signature

COSSigner provides a method to construct a COS signature which can be distributed to mobile SDKs for upload and download.
The signature path matches the key to be operated after distribution.

- **Method prototype**

```java

// Construct COS signature
public String buildAuthorizationStr(HttpMethodName methodName, String resouce_path,
        COSCredentials cred, Date expiredTime);

// Construct COS signature
//  Compared with first method, the second method provides additional signatures for some HTTP Headers and all parameters in the entered URL.
// It is used for more complicated signature control. The generated signature must also carry the corresponding header and param for upload and download operations.
public String buildAuthorizationStr(HttpMethodName methodName, String resouce_path,
        Map<String, String> headerMap, Map<String, String> paramMap, COSCredentials cred,
        Date expiredTime);
```

- **Parameter description**

| Parameter Name | Description | Type |
| ------------ | ---------------------------------------- | -------------- |
| methodName   | HTTP request method. Available values: PUT, GET, DELETE, HEAD, and POST | HttpMethodName |
| resouce_path | The path that needs a signature, starting with "/". Same as the key for file upload. | HttpMethodName |
| cred         | Key information | COSCredentials |
| expiredTime  | Expiration time | Date           |
| headerMap    | The HTTP Header map that needs a signature. Perform the signature only for entered Content-Type, Content-Md5, and header starting with "x" | Map            |
| paramMap     | URL Param map that needs a signature | Map            |

- **Returned value**

String

- **Example**

Example 1 Generate a upload signature
```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "mybucket-1251668577";
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
COSSigner signer = new COSSigner();
// Set the expiration time as 1 hour
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// The key that needs signature. The generated signature can only be used for uploading for the corresponding key.
String key = "/aaa.txt";
String sign = signer.buildAuthorizationStr(HttpMethodName.PUT, key, cred, expiredTime);
```

Example 2 Generate a download signature
```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "mybucket-1251668577";
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
COSSigner signer = new COSSigner();
// Set the expiration time as 1 hour
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// The key that needs signature. The generated signature can only be used for downloading for the corresponding key.
String key = "/aaa.txt";
String sign = signer.buildAuthorizationStr(HttpMethodName.GET, key, cred, expiredTime);
```

Example 3 Generate a deletion signature
```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "mybucket-1251668577";
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
COSSigner signer = new COSSigner();
// Set the expiration time as 1 hour
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// The key that needs signature. The generated signature can only be used for deletion for the corresponding key.
String key = "/aaa.txt";
String sign = signer.buildAuthorizationStr(HttpMethodName.DELETE, key, cred, expiredTime);
```


## File Upload via Advanced API (Recommended)

The advanced API encapsulates upload and download APIs using the TransferManger type. It has a thread pool inside to accept users' upload and download requests, so users can choose to submit tasks asynchronously.

```java
ExecutorService threadPool = Executors.newFixedThreadPool(32);
// Input a threadpool. If no thread pool is input, TransferManager will generate a single-thread pool by default.
TransferManager transferManager = new TransferManager(cosclient, threadPool);
// ..... (submit upload/download requests as described below)
// Close TransferManger
transferManager.shutdownNow();
```

### Uploading File

The upload API automatically selects simple upload or multipart upload based on the size of users' files, making it easy for users to use. Besides, you do not need to care about each step of the multipart upload.

- **Method prototype**

```java
// Upload files
public Upload upload(final PutObjectRequest putObjectRequest)
            throws CosServiceException, CosClientException;
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------------- | ------ | ---------------- |
| putObjectRequest | File upload request | PutObjectRequest |
Request member description:

| Request Member | Setting Method | Description | Type |
| ---------- | ------------ | ---------------------------------------- | -------------- |
| bucketName | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String         |
| key        | Constructor or set method | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                | String         |.
| file       | Constructor or set method | Local file |  File           |
| input      | Constructor or set method | Input stream |  InputStream    |
| metadata   | Constructor or set method | Meta information of a file |  ObjectMetadata |

- **Returned value**

	- Successful: Return Upload. You can query whether the upload is completed, or wait until the upload finishes synchronously.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
String key = "/mypic.jpg";
File localFile = new File("/data/dog.jpg");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, file);
// Local file upload
Upload upload = transferManager.upload(putObjectRequest);
// Wait for the transfer to finish (call waitForCompletion if you want to wait for the upload to finish synchronously)
UploadResult uploadResult = upload.waitForUploadResult();
```


### Downloading File

Download files on COS locally.

- **Method prototype**

```java
// Download files
public Download download(final GetObjectRequest GetObjectRequest, final File file);
```

- **Parameter description**

| Parameter Name | Description | Type |
| ---------------- | --------- | ---------------- |
| getObjectRequest | File download request  GetObjectRequest |
| file             | File to be downloaded locally | File             |
Request member description:

| Request Member | Setting Method | Description | Type |
| ---------- | ------------ | ---------------------------------------- | ------ |
| bucketName | Constructor or set method | The bucket should be named in a format of {name}-{appid}, where name should be comprised of letters, numbers, and dashes. |  String |
| key        | Constructor or set method | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                | String |.
| range      | Set method | The range of download |  Long[] |

- **Returned value**

	- Successful: Return Download. You can query whether the download is completed, or wait until the download finishes synchronously.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "movie-1251668577";
String key = "/mypic.jpg";
File localDownFile = new File("/data/dog.jpg");
GetObjectRequest getObjectRequest = new GetObjectRequest(bucket, key);
// Download files
Download download = transferManager.download(getObjectRequest, localDownFile);
 // Wait for the transfer to finish (call waitForCompletion if you want to wait for the upload to finish synchronously)
download.waitForCompletion();
```

### Copying File

The copy API automatic selects copy or multipart copy based on file size. Users do not need to care about the size of the file to be copied.

- **Method prototype**

```java
// Upload files
public Copy copy(final CopyObjectRequest copyObjectRequest);
```

- **Parameter description**

| Parameter Name | Description | Type |
| ----------------- | ------ | ----------------- |
| copyObjectRequest | File copy request | CopyObjectRequest |

Request member description:

| Parameter Name | Description | Type |
| --------------------- | ---------------------------------------- | ------ |
| sourceBucketRegion    | Region of the source Bucket. Default: same with the region of the current clientconfig, which represents an intra-region copy |  String |
| sourceBucketName      | Source bucket. The bucket entered must be in a format of {name}-{appid} | String |
| sourceKey             | Source object key. Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                    | String |.
| sourceVersionId       | Version ID of the source file with multiple versions. Default: The latest version of the source file | String |
| destinationBucketName | Destination bucket. The bucket entered must be in a format of {name}-{appid} | String |
| destinationKey        | Destination object key. Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324)                                   | String |.
| storageClass          | The storage type of the copied destination file (standard, low frequency, nearline). Default: Standard | String |

- **Returned value**

	- Successful: Return Copy. You can query whether the copy is completed, or wait until the copy finishes synchronously.

	- Failed: CosClientException or CosServiceException is thrown when an error (such as authentication failure) occurs. For more information, please see Exception Types.

- **Example**

```java
// The region of bucket to copy. Cross-region copy is supported.
Region srcBucketRegion = new Region("ap-shanghai");
// Source bucket. The bucket entered must be in a format of {name}-{appid}
String srcBucketName = "srcBucket-1251668577";
// The source file to copy
String srcKey = "aaa/bbb.txt";
// Destination bucket. The bucket entered must be in a format of {name}-{appid}
String destBucketName = "destBucket-1251668577";
// The destination file to copy
String destKey = "ccc/ddd.txt";

// Generate srcCOSClient to get source file information
COSClient srcCOSClient = new COSClient(cred, new ClientConfig(srcBucketRegion));
CopyObjectRequest copyObjectRequest = new CopyObjectRequest(srcBucketRegion, srcBucketName,
        srcKey, destBucketName, destKey);
try {
    Copy copy = transferManager.copy(copyObjectRequest, srcCOSClient, null);
// Return an asynchronous result copy. You can synchronously call waitForCopyResult to wait for copy to end. If successful, CopyResult is returned, and an exception will be thrown if failed.
    CopyResult copyResult = copy.waitForCopyResult();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
} catch (InterruptedException e) {
    e.printStackTrace();
}
```

## Permission Configuration

Permissions to access files on COS can be configured and obtained through SET/GET Object ACL and SET/GET Bucket ACL. The mainly used two types are AccessControlList and CannedAccessList. The following is the detailed description: The object inherits the bucket permission by default. COS only supports setting 1,000 ACL rules for an account (appid), so it is recommended to set ACL only for objects with inconsistent bucket permission to prevent the number of permission from exceeding the threshold. The function of unlimited ACL is under development.

### AccessControlList

Custom access control policy is used to set policy control to a user.

Members of AccessControlList type

| Member Name | Description | Type |
| -------------- | ----------------------- | ------ |
| List&lt;Grant> | Contains information of all users to be authorized | Array |
| owner          | The owner of the Object or Owner | Owner class |

Members of Grant type

| Member Name | Description | Type |
| ---------- | --------------------- | ---------- |
| grantee    | Identity information of an authorized user | Grantee    |
| permission | Authorized permission information (such as readable, writable, readable & writable) | Permission |

Members of Owner type

| Member Name | Description | Type |
| ----------- | ----------------- | ------ |
 Permission | Identity information of an owner | String |
| displayname | Owner's name (same as id) | String |

- **Example**

```
// The identity information in the permission must be in the required format. The format for the root account and subaccount is as follows:
// Both root_uin and sub_uin below must be valid QQ numbers
// The root account qcs::cam::uin/<root_uin>:uin/<root_uin> indicates that the root_uin is granted to the root account (that is, the first and second uin are the same)
// For example, qcs::cam::uin/2779643970:uin/2779643970
// The sub-account qcs::cam::uin/<root_uin>:uin/<sub_uin> indicates that the sub_uin is granted to the root_uin.
// For example, qcs::cam::uin/2779643970:uin/73001122 

AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
// Set the owner information. Owner can only be a root account.
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);

// Grant the root account 73410000 the read and write permissions
UinGrantee uinGrantee1 = new UinGrantee("qcs::cam::uin/73410000:uin/73410000");
acl.grantPermission(uinGrantee1, Permission.FullControl);
// Grant the sub-account 72300000 of 2779643970 the read permission
UinGrantee uinGrantee2 = new UinGrantee("qcs::cam::uin/2779643970:uin/72300000");
acl.grantPermission(uinGrantee2, Permission.Read);
// Grant the sub-account 7234444 of 2779643970 the write permission
UinGrantee uinGrantee3 = new UinGrantee("qcs::cam::uin/7234444:uin/7234444");
acl.grantPermission(uinGrantee3, Permission.Write);

// Set object's ACL
cosclient.setObjectAcl(bucket, key, acl);
```

### CannedAccessControlList

CannedAccessControlList represents a preset policy for everyone. It is an enumeration type with the following enumerated values.

| Enumerated Value | Description |
| --------------- | ---------------------------- |
| Private         | Private read and write (only owner can read and write) |
| PublicRead      | Public read and private write (owner can read and write, and other users can read) |
| PublicReadWrite | Public read and write (everyone can read and write) |


## Client Encryption
The Java SDK supports client encryption feature that encrypts files before uploading, and decrypts them for downloading. Client encryption supports symmetric AES and asymmetric RSA encryption.
The symmetry and asymmetry here are only used to encrypt the generated random keys. AES256 is always used to encrypt file data symmetrically.
Client encryption is suitable for users who store sensitive data. client encryption may sacrifice certain upload speed, and the SDK may use serial method for multipart upload.

### Preparation for client encryption

Aes256 is used in client encryption to encrypt data. By default, the earlier versions, such as JDK6 - JDK8, do not support 256-bit encryption. If an exception `java.security.InvalidKeyException: Illegal key size or default parameters` is reported during runtime, we must supplement Oracle's JCE unlimited permission file and deploy it in the JRE environment. Download the corresponding files based on the current JDK version and decompress and save them in the jre/lib/security directory under JAVA_HOME.

1. [JDK6 JCE supplement package](http://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html)
2. [JDK7 JCE supplement package](http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html)
3. [JDK8 JCE supplement package](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)


### Upload encryption process
1. Before uploading a file object, we randomly generate a symmetric encryption key. The random key is encrypted by the symmetric or asymmetric key provided by the user, and the encrypted result is encoded with base64 and stored in the meta information of the object.
2. When the file object is uploaded, AES256 algorithm is used to encrypt the file object in memory.

### Download decryption process
1. Obtain the necessary encryption information in the meta information of the file, and decrypt the information decoded with base64 using the user key to obtain the key of the encrypted data
2. Use the key to decrypt the downloaded input stream using AES256 to obtain the decrypted file input stream.

- **Example**

Use symmetric AES256 encryption to generate a random key example. For more information on the complete sample code, please see [Complete Example of Symmetric Client Key Encryption](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/SymmetricKeyEncryptionClientDemo.java)
```java
// Initialize user authentication information (secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXXXXXXXXXX",
		"YYZZZZZZZZZZZZZZZZZ");
// Set the region where the bucket resides. For the abbreviations of COS regions, please see https://www..com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));

// Load the key saved in the file. If it does not exist, use buildAndSaveSymmetricKey to generate the key first.
// buildAndSaveSymmetricKey();
SecretKey symKey = loadSymmetricAESKey();

EncryptionMaterials encryptionMaterials = new EncryptionMaterials(symKey);
// Use the AES/GCM mode and store the encrypted information in the meta information of the file.
CryptoConfiguration cryptoConf = new CryptoConfiguration(CryptoMode.AuthenticatedEncryption)
		.withStorageMode(CryptoStorageMode.ObjectMetadata);

// Generate encryption client (EncryptionClient). The COSEncryptionClient is a subclass of COSClient, and all APIs supported by COSClient are also available.
// EncryptionClient overwrites the COSClient upload and download logic. It will perform the encryption operation internally. The other operations execution logic is consistent with that of the COSClient.
COSEncryptionClient cosEncryptionClient =
		new COSEncryptionClient(new COSStaticCredentialsProvider(cred),
				new StaticEncryptionMaterialsProvider(encryptionMaterials), clientConfig,
				cryptoConf);

// Upload files
// Here is an example of putObject. For advanced API upload, use the COSEncryptionClient object when generating TransferManager.
String bucketName = "mybucket-1251668577";
String key = "xxx/yyy/zzz.txt";
File localFile = new File("src/test/resources/plain.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
cosEncryptionClient.putObject(putObjectRequest);
```

Use symmetric RSA encryption to generate a random key example. For more information on the complete sample code, please see [Complete Example of Symmetric Client Key Encryption](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/AsymmetricKeyEncryptionClientDemo.java)
```java
// Initialize user authentication information (secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXXXXXXXXXXXXXX",
		"YYZZZZZZZZZZZZZZZZZZ");
// Set the region where the bucket resides. For the abbreviations of COS regions, please see https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));


// Load the key saved in the file. If it does not exist, use buildAndSaveAsymKeyPair to generate the key first.
buildAndSaveAsymKeyPair();
KeyPair asymKeyPair = loadAsymKeyPair();

EncryptionMaterials encryptionMaterials = new EncryptionMaterials(asymKeyPair);
// Use the AES/GCM mode and store the encrypted information in the meta information of the file.
CryptoConfiguration cryptoConf = new CryptoConfiguration(CryptoMode.AuthenticatedEncryption)
		.withStorageMode(CryptoStorageMode.ObjectMetadata);

// Generate encryption client (EncryptionClient). The COSEncryptionClient is a subclass of COSClient, and all APIs supported by COSClient are also available.
// EncryptionClient overwrites the COSClient upload and download logic. It will perform the encryption operation internally. The other operations execution logic is consistent with that of the COSClient.
COSEncryptionClient cosEncryptionClient =
		new COSEncryptionClient(new COSStaticCredentialsProvider(cred),
				new StaticEncryptionMaterialsProvider(encryptionMaterials), clientConfig,
				cryptoConf);

// Upload files
// Here is an example of putObject. For advanced API upload, use the COSEncryptionClient object when generating TransferManager.
String bucketName = "mybucket-1251668577";
String key = "xxx/yyy/zzz.txt";
File localFile = new File("src/test/resources/plain.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
cosEncryptionClient.putObject(putObjectRequest);
```

## Exception Description

When the SDK fails, the exceptions thrown are all RuntimeExcpetion. The common SDK exceptions are CosClientException, CosServiceException, and IllegalArgumentException.

### CosClientException

Client exceptions refer to server interaction failures caused by unexpected client issues such as failure to connect to the server, failure to parse the data returned by the server, and the occurrence of I/O exception when reading a local file. Inherited from RuntimeException, CosClientException has no custom member variables, and is used in the same way as RuntimeException.

### CosServiceException

CosServiceException service exception refers to scenarios in which interaction is completed but the operation failed. For example, the client accesses a bucket that does not exist, delete a file that does not exist, or does not have the permission to perform an operation, or the server failed. CosServiceException contains the status code returned by the server, requestid, error details, and so on. After an exception is captured, it is recommended to print the entire exception. The exception contains the necessary troubleshooting factors. Member variables of exception are described as follows:

| request Member | Description | Type |
| ------------ | ---------------------------------------- | --------- |
| requestId    | Request ID to specify a request. It is very important for troubleshooting. | String    |
| traceId      | ID for troubleshooting | String    |
| statusCode   | Status code of the response. 4xx represents the request failure caused by the client, and 5xx represents the failure caused by the server exception For more information, please see [COS Error Message] (https://cloud.tencent.com/document/product/436/7730) | String    |
| errorType    | Enumeration type, indicating the type of exception (Client, Service, and Unknown) | ErrorType |
| errorCode    | Error Code returned by body when request fails. For more information, please see [COS Error Message](https://cloud.tencent.com/document/product/436/7730) | String    |
| errorMessage | Error Message returned by body when request fails. For more information, please see [COS Error Message](https://cloud.tencent.com/document/product/436/7730) | String    |



## FAQ

1. Why does java.lang.NoSuchMethodError appear when I run the SDK?
A JAR packet conflict may occur. For example, the JAR package for http in the user's project does not have method A, but the SDK-dependent JAR package has method A. The loading order goes wrong. The http library in the user project is loaded. When the SDK is running, the NoSuchMethodError exception is thrown. Solution: Change the version of the package that causes NoSuchMethodError in the contained project to the version of the corresponding library in the pom.xml in the SDK.
2. Upload using SDK is very slow,Logs frequently display IOException？
Causes and solutions: 
 a. Check whether you were accessing COS over the public network. For COS access in the same region, it is recommended to use the private network. (IP address range 10,100,169 is resolved from the private network domain name.For more information on COS domains, please see [Available Regions for COS](https://cloud.tencent.com/document/product/436/6224)). If the public network is used, check whether the outbound bandwidth is small or whether other programs occupy bandwidth resources. 
 b. Ensure that the log level in the production environment is not debug. INFO log is recommended. For information on log configuration of log4j, please see [log4j log configuration template](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/resources/log4j.properties). 
 c. The speed of simple upload can reach 10 MB. When you use an advanced API and  32 concurrency level, the speed can reach 60 MB. If your speed is far less than these two value. Refer to a and b. 
 d. If warn log displays IOException, ignore it. The SDK will retry. If it fails after multiple attempts of retries, the log displays IOException, which may be caused by too slow speed. For the cause, please see a and b.
3. How do I create a directory using the SDK? 
Files and directories in COS are objects, and directories are objects ending with "/". When you create a file, you do not need to create a directory. For example, if you create a file with an object key of xxx/yyy/zzz.txt, just set the key to xxx/yyy/zzz.txt instead of creating an xxx/yyy/ object. Separate directories with "/" to display the hierarchy on the console. However, these directory objects may not exist. If you want to create a directory object, use the following sample code.

```java
String bucketName = "mybucket-125166000";=
String key = "xxx/yyy/";
//A directory object is an empty file ending with "/". Upload a byte stream with a length of 0.
InputStream input = new ByteArrayInputStream(new byte[0]);
ObjectMetadata objectMetadata = new ObjectMetadata();
objectMetadata.setContentLength(0);

PutObjectRequest putObjectRequest =
new PutObjectRequest(bucketName, key, input, objectMetadata);
PutObjectResult putObjectResult = cosclient.putObject(putObjectRequest);
```

