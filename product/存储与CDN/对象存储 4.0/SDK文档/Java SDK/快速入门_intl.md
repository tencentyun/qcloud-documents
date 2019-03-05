## Preparation for Development
### Related resources
Download the XML Java SDK resources of COS service from [XML Java SDK](https://github.com/tencentyun/cos-java-sdk-v5).
### Environment dependencies

- The SDK supports JDK 1.7, 1.8 or above.
- For more information on how to install JDK, please see [Java Installation and Configuration](/document/product/436/10865).

> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](/document/product/436/7751).

### Installing SDK
There are two ways to install the SDK: installation using maven and installation using source code.

- Installation using maven
Add dependencies using pom.xml in maven project, as shown below:

```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>5.4.4</version>
</dependency>
```

- Installation using source code
Download the source code from [XML Java SDK](https://github.com/tencentyun/cos-java-sdk-v5) and import it via maven. For example, for eclipse, select **File** -> **Import** -> **maven** -> **Existing Maven Projects**.

### Uninstalling SDK
Uninstall the SDK by removing the pom dependencies or source code.

## Getting Started

### Initializing client cosclient

Set the user authentication information, including appid, the region where the bucket resides, and bucket name

```java
// 1 Initialize user authentication information (secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 Set the region where the bucket resides. For the abbreviations of COS regions, please see https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 Generate the COS client
COSClient cosclient = new COSClient(cred, clientConfig);
// The bucket name entered must be in a format of {name}-{appid}.
String bucketName = "mybucket-1251668577";
```

### Uploading files

Upload a local file or input stream with a known length to COS. This is suitable for the upload of small files such as images below 20 MB. The maximum file size supported is 5 GB (inclusive). To upload a file greater than 5 GB, use multipart upload or advanced API. If most of your local files are greater than 20 MB, it is recommended to use an advanced API by referring to the relevant API document. If the object already exists on the COS, it will be overwritten. Because the directory does not exist in the Cloud Object Storage, if you want to create a directory object, see the FAQ in API document. 

```java
// Simple upload of file. The maximum file size supported is 5 GB. This is suitable for the upload of small files. It is recommended to use this API for the files less than 20 MB.
// To upload a large file, see "Upload Using Advanced API" in the API document.
File localFile = new File("src/test/resources/len5M.txt");
// Specify the object key to be uploaded to COS
// Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. For more information, please see [Object Key](https://cloud.tencent.com/document/product/436/13324).
String key = "upload_single_demo.txt";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
```

### Downloading files

Download files to local machine or obtain the download input streams for downloading files.

```java
// Specify the local path to which the file is downloaded
File downFile = new File("src/test/resources/mydown.txt");
// Specify the bucket where the file to be downloaded is located and the object key
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
ObjectMetadata downObjectMeta = cosClient.getObject(getObjectRequest, downFile);
```

### Deleting files

Delete the files under the specified path on the COS.

```java
// Specify the bucket and object key to be deleted
cosClient.deleteObject(bucketName, key);
```

### Shutting down client

Shut down cosclient and release the backend thread (manager thread of HTTP connection).

```
// Shut down the client (close the backend thread)
cosClient.shutdown();
```


