## Preparations for Development

### Related Resources

[cos java sdk v4 github Project](https://github.com/tencentyun/cos-java-sdk-v4)

### Environment Dependency

JDK 1.7

### Installing SDK

- maven installation

Add dependencies to Pom.xml

```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>4.2</version>
</dependency>
```

- Source code installation

Download source codes from [cos java sdk v4 github](https://github.com/tencentyun/cos-java-sdk-v4)

### Uninstalling SDK

Delete pom dependencies or source codes

### Historical Version

Version 4.2 is specifically designed for the COS 4.X system whose APIs are basically the same as 3.x. If you need the historical version, please refer to [cos java sdk v3 github](https://github.com/tencentyun/cos-java-sdk/tree/master)

## Generating Client Object

### Initializing Key Information

```java
        long appId = 1000000;
        String secretId = "xxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String secretKey = "xxxxxxxxxxxxxxxxxxxxxxxxxx";
        // Set the bucket to be operated
        String bucketName = "xxxxxxxxx";
        // Initialize key information
        Credentials cred = new Credentials(appId, secretId, secretKey);
```

### Initializing Client Configuration (e.g. Set the Region)

```java
        // Initialize client configuration
        ClientConfig clientConfig = new ClientConfig();
        // Set the region of the bucket. For example, South China: "gz", North China: "tj" and East China: "sh";
        clientConfig.setRegion("gz");
```

### Generating the Client

```java
        // Initialize cosClient
        COSClient cosClient = new COSClient(clientConfig, cred);
```

## File-related Operations

### Uploading a File

#### Method Prototype

```java
String uploadFile(UploadFileRequest request);
```

#### Parameter Description

|   Parameter Name   |        Type         | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | UploadFileRequest |  None   | Uploading file request |

|    request Member    |       Type        |         Default Value         |    Setting Method    |                    Description                    |
| :-------------: | :-------------: | :-----------------: | :--------: | :--------------------------------------: |
|   bucketName    |     String      |          None          | Constructor or set method |                 bucket name                 |
|     cosPath     |     String      |          None          | Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |
|    localPath    |     String      |          None          | Constructor or set method |             The absolute path uploaded via disk files               |
|  contentBufer   |     byte[]      |          None          | Constructor or set method |             buffer content uploaded via memory              |
|     bizAttr     |     String      |          Null          | Constructor or set method |           Note for file, mainly the description of the use of the file            |
|   insertOnly    | InsertOnly (enumeration) | NO_OVER_WRITE (not overwrite) |   set method    | Indicate whether to insert only and not overwrite the existing file. NO_OVER_WRITE means inserting only and not overwriting the existing file; when the file exists, an error will be returned. OVER_WRITE means overwriting the existing file |
| enableSavePoint |     boolean     |        true         |   set method    | Indicate whether to enable savepoint for files. If enabled, one savepoint will be recorded locally. When upload failed, the resumed upload will skip the uploaded parts. But enabling savepoint may slow down the upload speed.  |
| enableShaDigest |     boolean     |        false        |   set method    | Indicate whether to calculate sha digest. If enabled, when there is a file containing same content under the bucket, instant upload will be triggered. Calculating sha consumes a certain CPU and time. Thus, it is recommended that you do not enable it for large files.  |
|     taskNum     |       int       |         16          |   set method    |                 Number of concurrent file uploads                 |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains related attributes. For details, refer to the Returned Value module |

#### Example

```java
UploadFileRequest uploadFileRequest = new UploadFileRequest(bucketName, 		"/sample_file.txt", "local_file_1.txt");
String uploadFileRet = cosClient.uploadFile(uploadFileRequest);
```



### Downloading a File

#### Method Prototype

```java
String getFileLocal(GetFileLocalRequest request);
```

#### Parameter Description

|   Parameter Name   |        Type         | Default Value  |  Description  |
| :-----: | :-----------------: | :--: | :----: |
| request | GetFileLocalRequest |  None   | Request for downloading files |

| request Member  |   Type    |      Default Value       |    Setting Method    |                    Description                    |
| :--------: | :-----: | :------------: | :--------: | :--------------------------------------: |
| bucketName | String  |       None        | Constructor or set method |                 bucket name                 |
|  cosPath   | String  |       None        | Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |
| localPath  | String  |       None        | Constructor or set method |                The local path to be downloaded                 |
|   useCDN   | boolean |      true      |   set method    |               Indicate whether to download from CDN                |
|  referer   | String  |       Empty string       |   set method    |     Referer configuration (for bucket that enables refer hotlink protection)      |
| rangeStart |  long   |       0        |   set method    |          Start of download range. Refer to Http Range           |
|  rangeEnd  |  long   | Long.MAX_VALUE |   set method    |          End of download range. Refer to Http Range           |

#### Example

```java
String localPathDown = "src/test/resources/local_file_down.txt";
GetFileLocalRequest getFileLocalRequest =
  new GetFileLocalRequest(bucketName, cosFilePath, localPathDown);
getFileLocalRequest.setUseCDN(false);
getFileLocalRequest.setReferer("*.myweb.cn");
String getFileResult = cosClient.getFileLocal(getFileLocalRequest);
```



### Moving a File

#### Method Prototype

```java
String moveFile(MoveFileRequest request);
```

#### Parameter Description

|   Parameter Name   |      Type       | Default Value  |  Description  |
| :-----: | :-------------: | :--: | :----: |
| request | MoveFileRequest |  None   | Request for moving files |

| request Member  |   Type   |         Default Value        |       Setting Method       |                    Description                    |
| :--------: | :----: | :-----------------: | :---------------: | :--------------------------------------: |
| bucketName | String |          None          |    Constructor or set method     |                 bucket name                 |
|  cosPath   | String |          None          |    Constructor or set method     | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |
| dstCosPath | String |          None          |    Constructor or set method     | Destination path for moving files, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt.move |
| overWrite  |  Enumeration type  | NO_OVER_WRITE (not overwrite) | set method setOverWrite |       When the moved target file already exists, you can choose to overwrite or not overwrite it. Not overwrite by default        |

#### Example

```java
String cosFilePath = "/sample_file.txt";
String dstCosFilePath = "/sample_file.txt.bak";
MoveFileRequest moveRequest =
  new MoveFileRequest(bucketName, cosFilePath, dstCosFilePath);
String moveFileResult = cosClient.moveFile(moveRequest);
```



### Getting File Attributes

#### Method Prototype

```java
String statFile(StatFileRequest request);
```

#### Parameter Description

|   Parameter Name   |      Type       | Default Value  |   Description   |
| :-----: | :-------------: | :--: | :------: |
| request | StatFileRequest | None | Getting file attribute request |

| request Member  |   Type   | Default Value  |    Setting Method    |                    Description                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  None   | Constructor or set method |                 bucket name                 |
|  cosPath   | String |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains related attributes. For details, refer to the Returned Value module |

#### Example

```java
StatFileRequest statFileRequest = new StatFileRequest(bucketName, "/sample_file.txt");
String statFileRet = cosClient.statFile(statFileRequest);

```



### Updating File Attributes

#### Method Prototype

```java
String updateFile(UpdateFileRequest request);
```

#### Parameter Description

|   Parameter Name   |       Type        | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | UpdateFileRequest |  None   | Updating file attribute request |

|     request Member      |     Type      | Default Value  |    Setting Method    |                    Description                    |
| :----------------: | :---------: | :--: | :--------: | :--------------------------------------: |
|     bucketName     |   String    |  None   | Constructor or set method |                 bucket name                 |
|      cosPath       |   String    |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |
|      bizAttr       |   String    |  None   |   set method    |           Note for file, mainly the description of the use of the file            |
|     authority      | String (enumeration) |  None   |   set method    | File permissions. The valid values of bucket permissions will be inherited by default: eInvalid (inherit bucket), eWRPrivate (private), eWPrivateRPublic (public-read) |
|    cacheControl    |   String    |  None   |   set method    |           Refer to the Cache-Control in HTTP header           |
|    contentType     |   String    |  None   |   set method    |           Refer to the Content-Type in HTTP header            |
|  contentLanguage   |   String    |  None   |   set method    |         Refer to the Content-Language in HTTP header          |
| contentDisposition |   String    |  None   |   set method    |        Refer to the Content-Disposition in HTTP header        |
|    x-cos-meta-     |   String    |  None   |   set method    | Customized HTTP header. Parameters must start with x-cos-meta-, and the value is defined by the user. Multiple values are allowed |

**Tips:** You can update only some of the attributes. For the HTTP headers cache_control, content_type, content_disposition and x-cos-meta-, if you just update some, other headers will be erased. That is, these four attributes are updated as a whole.

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```java
UpdateFileRequest updateFileRequest = new UpdateFileRequest(bucketName, "/sample_file.txt");

updateFileRequest.setBizAttr("Test directory");
updateFileRequest.setAuthority(FileAuthority.WPRIVATE);
updateFileRequest.setCacheControl("no cache");
updateFileRequest.setContentDisposition("cos_sample.txt");
updateFileRequest.setContentLanguage("english");
updateFileRequest.setContentType("application/json");
updateFileRequest.setXCosMeta("x-cos-meta-xxx", "xxx");
updateFileRequest.setXCosMeta("x-cos-meta-yyy", "yyy");

String updateFileRet = cosClient.updateFile(updateFileRequest);
```



### Deleting a File

#### Method Prototype

```java
String delFile(DelFileRequest request);
```

#### Parameter Description

|   Parameter Name   |      Type      | Default Value  |  Description  |
| :-----: | :------------: | :--: | :----: |
| request | DelFileRequest | None | Deleting file request |

| request Member  |   Type   | Default Value  |    Setting Method    |                    Description                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  None   | Constructor or set method |                 bucket name                 |
|  cosPath   | String |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```java
DelFileRequest delFileRequest = new DelFileRequest(bucketName, "/sample_file_move.txt");
String delFileRet = cosClient.delFile(delFileRequest);
```

------

------

## Directory-related Operations

### Creating a Directory

#### Method Prototype

```java
String createFolder(CreateFolderRequest request);	
```

#### Parameter Description

|   Parameter Name   |        Type         | Default Value  |  Description  |
| :-----: | :-----------------: | :--: | :----: |
| request | CreateFolderRequest |  None   | Creating directory request |

| request Member  |   Type   | Default Value  |    Setting Method    |                    Description                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  None   | Constructor or set method |                 bucket name                 |
|  cosPath   | String |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |
|  bizAttr   | String |  Null   |   set method    |            Note for directory, mainly the description of the use of the directory            |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```java
CreateFolderRequest createFolderRequest = new CreateFolderRequest(bucketName, "/sample_folder/");
String createFolderRet = cosClient.createFolder(createFolderRequest);
```



### Getting Directory Attributes

#### Method Prototype

```java
String statFolder(StatFolderRequest request);
```

#### Parameter Description

|   Parameter Name   |       Type        | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | StatFolderRequest |  None   | Getting directory attribute request |

| request Member  |   Type   | Default Value  |    Setting Method    |                    Description                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  None   | Constructor or set method |                 bucket name                 |
|  cosPath   | String |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains related attributes. For details, refer to the Returned Value module |

#### Example

```java
StatFolderRequest statFolderRequest = new StatFolderRequest(bucketName, "/sample_folder/");
String statFolderRet = cosClient.statFolder(statFolderRequest);
```



### Updating Directory Attributes

#### Method Prototype

```java
String updateFolder(UpdateFolderRequest request);
```

#### Parameter Description

|   Parameter Name   |        Type         | Default Value  |   Description   |
| :-----: | :-----------------: | :--: | :------: |
| request | UpdateFolderRequest |  None   | Updating directory attribute request |

| request Member  |   Type   | Default Value  |    Setting Method    |                    Description                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  None   | Constructor or set method |                 bucket name                 |
|  cosPath   | String |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |
|  bizAttr   | String |  Null   |   set method    |            Note for directory, mainly the description of the use of the directory            |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```java
UpdateFolderRequest updateFolderRequest = new UpdateFolderRequest(bucketName, "/sample_folder/");
updateFolderRequest.setBizAttr("This is a test directory");
String updateFolderRet = cosClient.updateFolder(updateFolderRequest);
```



### Getting List of Directories

#### Method Prototype

```java
String listFolder(ListFolderRequest request);
```

#### Parameter Description

|   Parameter Name   |       Type        | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | ListFolderRequest |  None   | Getting directory member request |

| request Member  |   Type   | Default Value  |    Setting Method    |                    Description                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  None   | Constructor or set method |                 bucket name                 |
|  cosPath   | String |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |
|    num     |  int   | 199  | Constructor or set method |             Number of members in the list obtained. The maximum is 199             |
|   prefix   | String |  Null   | Constructor or set method | Prefix of members for search. For example, if the prefix is test, it means only searching files or directories that start with test |
|  context   | String |  Null   | Constructor or set method |  Transparently transmitted field, which is obtained from the response content. If you want to query the first page, an empty string should be passed as context. To turn pages, the context in the returned content of the previous page should be transparently transmitted to the parameter |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains the member list. For details, refer to the Returned Value module |

#### Example

```java
ListFolderRequest listFolderRequest = new ListFolderRequest(bucketName, "/sample_folder/");
String listFolderRet = cosClient.listFolder(listFolderRequest);
```



### Deleting a Directory

#### Method Prototype

```java
String delFolder(DelFolderRequest request);
```

#### Parameter Description

|   Parameter Name   |       Type       | Default Value  |  Description  |
| :-----: | :--------------: | :--: | :----: |
| request | DelFolderRequest | None | Deleting directory request |

| request Member  |   Type   | Default Value  |    Setting Method    |                    Description                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  None   | Constructor or set method |                 bucket name                 |
|  cosPath   | String |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |

#### Returned Value

| Type of Returned Value  |                  Description of Returned Value                   |
| :----: | :--------------------------------------: |
| String  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```java
DelFolderRequest delFolderRequest = new DelFolderRequest(bucketName, "/sample_folder/");
String delFolderRet = cosClient.delFolder(delFolderRequest);
```

------

------

## Signature Management

The signature module provides APIs for generating multiple-time signature, one-time signature, and download signature. The multiple-time signature and one-time signature are used within the APIs of file-related and directory-related operations, so users do not need to care about them. The download signature is used to help users generate the signature for downloading the private bucket file.

### Multiple-time Signature

```java
String getPeriodEffectiveSign(String bucketName, String cosPath, Credentials cred, long expired)
```

#### Usage Scenarios

Uploading files, renaming files, creating directories, getting file and directory attributes, and pulling lists of directories

#### Parameter Description

| Parameter Name      |    Type     | Default Value  |                 Description                 |
| -------- | :---------: | :--: | :----------------------------------: |
| bucket   |   String    |  None   |               bucket name               |
| cos_path | unicode |  None   |              The cos path that needs a signature              |
| cred     | Credentials |  None   | User identity information, including appid, secretId, and secretkey |
| expired  |    long     |  None   |           Expiration time of the signature, Unix timestamp           |

#### Returned Value

String encoded with base64

#### Example

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
long expired = System.currentTimeMillis() / 1000 + 600;
String signStr = Sign.getPeriodEffectiveSign(bucketName, "/pic/test.jpg", cred, expired);
```

### One-time Signature

```java
String getOneEffectiveSign(String bucketName, String cosPath, Credentials cred)
```

#### Usage Scenarios

Deleting and updating files and directories

#### Parameter Description

|   Parameter Name    | Type     | Default Value  |                 Description                 |
| :------: | :---------: | :--: | :----------------------------------: |
|  bucket  |   unicode   |  None   |               bucket name               |
| cos_path |   unicode   |  None   |              The cos path that needs a signature               |
|   cred   | Credentials |  None   | User identity information, including appid, secretId, and secretkey |

#### Returned Value

String encoded with base64

#### Example

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
String signStr = Sign.getOneEffectiveSign(bucketName, "/pic/test.jpg", cred);
```

### Download Signature

```java
String getDownLoadSign(String bucketName, String cosPath, Credentials cred, long expired)
```

#### Usage Scenarios

Generating download signature of file for downloading private bucket files

#### Parameter Description

|   Parameter Name    | Type     | Default Value  |                 Description                 |
| :------: | :---------: | :--: | :----------------------------------: |
|  bucket  |   unicode   |  None   |               bucket name               |
| cos_path |   unicode   |  None   |              The cos path that needs a signature               |
|   cred   | Credentials |  None   | User identity information, including appid, secretId, and secretkey |
| expired  |    long     |  None   |           Expiration time of the signature, Unix timestamp           |

#### Returned Value

String encoded with base64

#### Example

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
long expired = System.currentTimeMillis() / 1000 + 600;
String signStr = Sign.getDownLoadSign(bucketName, "/pic/test.jpg", cred, expired);
```

------

------

## Returned Value

| Code |                  Meaning                  |
| :--: | :----------------------------------: |
|  0   |                 Operation succeeded                 |
|  -1  | Incorrect input parameter. For example, the local file path entered does not exist; cos file path does not conform to standards |
|  -2  |             Network error, such as 404              |
|  -3  |           An exception occurs while trying to connect cos, such as connection timeout           |

