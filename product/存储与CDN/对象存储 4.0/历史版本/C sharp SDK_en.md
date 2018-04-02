## Preparations for Development

### Related Resources

[github Project](https://github.com/tencentyun/cos-donet-sdk-v4)

### Preparations for Development

1. C# 4.0 or later version is supported for SDK. It is recommended to use the same version.
2 . Get APP ID, SecretID, and SecretKey from the Console.
3. Modify the URL of the region in CosCloud.cs, for example, East China: `http://sh.file.myqcloud.com/files/v2/` ; North China: `http://tj.file.myqcloud.com/files/v2/` ; South China: `http://gz.file.myqcloud.com/files/v2/`



### Configuring SDK

Download the source code from github, and integrate it into the development environment. 

If HTTPS is needed, change http in the variable COSAPI_CGI_URL of the file cos_dotnet_sdk/Api/CosCloud.cs to https.

## Generating Signature

### Multiple-time Signature

#### Method Prototype

``` c#
public static string Signature(int appId, string secretId, string secretKey, long expired, string bucketName)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| appId      | int    | Yes      | AppId                                    |
| secretId   | string | Yes      | Secret Id                                |
| secretKey  | string | Yes      | Secret Key. The parameters described above can be obtained from [Console](/document/product/436/6238).  |
| expired    | long   | Yes      | Expiration time, Unix timestamp                             |
| bucketName | string | Yes      | bucket name. To create a bucket, refer to [Create Bucket](/document/product/436/6245) |

#### Example

``` c#
var sign = Sign.Signature(appId, secretId, secretKey, expired, bucketName); 
```

### One-time Signature

#### Method Prototype

``` c#
public static string SignatureOnce(int appId, string secretId, string secretKey, string remotePath, string bucketName)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| appId      | int    | Yes      | AppId                                    |
| secretId   | string | Yes      | Secret Id                                |
| secretKey  | string | Yes      | Secret Key. The parameters described above can be obtained from [Console](/document/product/436/6238).  |
| bucketName | string | Yes      | bucket name. To create a bucket, refer to [Create Bucket](/document/product/436/6245) |
| remotePath | string | Yes      | Unique ID of a file. Format: /appid/bucketname/filepath/filename, in which /filepath/filename is the full path of the file under the current bucket name. |

#### Example

``` c#
var sign = Sign.SignatureOnce(appId, secretId, secretKey,remotePath, bucketName); 
```

For more information on signature, refer to [Permission Control](/document/product/436/6247).

## Directory-related Operations

### Creating a Directory

API Description: It is used to create a directory. A directory can be created under specified bucket through this API.

#### Method Prototype

``` c#
public string CreateFolder(string bucketName, string remotePath, Dictionary<string, string> parameterDic = null)
```

#### Parameter Description

| **Parameter Name**      | **Type** | **Required** | **Description**   |
| ------------ | ------ | ------ | ---------- |
| bucketName   | string | Yes      | bucket name   |
| remotePath   | string | Yes      | The full path under which the directory will be created |
| parameterDic | string | No      | Attribute dictionary       |

Attribute dictionary

| Parameter Name      | Type     | Required   | Description |
| -------- | ------ | ---- | ---- |
| biz_attr | string | No    | Directory attribute |

#### Returned Result

| **Parameter Name** | **Type** | Required   | **Description**                   |
| ------- | ------ | ---- | -------------------------- |
| code    | Int    | Yes    | Error code, 0 indicates success                  |
| message | String | Yes    | Error message                       |
| data    | Array  | No    | Returned data, refer to "Restful API Directory Creation" |

#### Example

``` c#
var createFolderParasDic = new Dictionary<string, string>();                
    createFolderParasDic.Add(CosParameters.PARA_BIZ_ATTR,"new attribute");
var result = cos.CreateFolder(bucketName, folder, createFolderParasDic);
```

### Updating Directory

API Description: It is used to update the custom attribute of a directory business. The custom attribute field of a business can be updated through this API.

#### Method Prototype

``` c#
public string UpdateFolder(string bucketName, string remotePath, Dictionary<string, string>  parameterDic = null) 
```

#### Parameter Description

| **Parameter Name**      | **Type** | **Required** | **Description**   |
| ------------ | ------ | ------ | ---------- |
| bucketName   | string | Yes      | bucket name   |
| remotePath   | string | Yes      | The full path under which the directory will be created |
| parameterDic | string | Yes      | Parameter dictionary for updating directories   |

Parameter dictionary for updating directories

| Parameter Name      | Type     | Required   | Description |
| -------- | ------ | ---- | ---- |
| biz_attr | string | No    | Directory attribute |

#### Returned Result

| **Parameter Name** | **Type** | Required   | **Description**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | Yes    | Error code, 0 indicates success |
| message | String | Yes    | Error message      |

#### Example

``` c#
var updateParasDic = new Dictionary<string, string>();                
    updateParasDic.Add(CosParameters.PARA_BIZ_ATTR,"new attribute");
var result = cos.UpdateFolder(bucketName, folder, updateParasDic);
```

### Querying a Directory

API Description: It is used to query the directory attribute. The attribute of a directory can be queried through this API.

#### Method Prototype

``` c#
public string GetFolderStat(string bucketName, string remotePath)  
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description** |
| ---------- | ------ | ------ | -------- |
| bucketName | string | Yes      | bucket name |
| remotePath | string | Yes      | Full path of a directory   |

#### Returned Result

| **Parameter Name** | **Type** | Required   | **Description**                     |
| ------- | ------ | ---- | ---------------------------- |
| code    | Int    | Yes    | Error code, 0 indicates success                    |
| message | String | Yes    | Error message                         |
| data    | Array  | No    | Directory attributes, refer to "Restful API Query for Directory" |

#### Example

``` c#
var result = cos.GetFolderStat(bucketName, folder);
```

### Deleting a Directory

API Description: It is used to delete a directory. Empty directories can be deleted through this API, but a directory with valid files or directories cannot be deleted.

#### Method Prototype

``` c#
public string DeleteFolder(string bucketName, string remotePath)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description** |
| ---------- | ------ | ------ | -------- |
| bucketName | string | Yes      | bucket name |
| remotePath | string | Yes      | Full path of a directory   |

#### Returned Result

| **Parameter Name** | **Type** | Required   | **Description**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | Yes    | Error code, 0 indicates success |
| message | String | Yes    | Error message      |

#### Example

``` c#
var result = cos.DeleteFolder(bucketName, folder);
```

### Listing Files and Directories under a Directory

API Description: It is used to list the files and directories under a directory. The attributes of the files and directories under a directory can be queried through this API.

#### Method Prototype

``` c#
public string GetFolderList(string bucketName, string remotePath, Dictionary<string, string>  parameterDic = null)
```

#### Parameter Description

| **Parameter Name**      | **Type**                     | **Required** | **Description** |
| ------------ | -------------------------- | ------ | -------- |
| bucketName   | string                     | Yes      | bucket name |
| remotePath   | string                     | Yes      | Full path of a directory   |
| parameterDic | Dictionary<string, string> | Yes      | Parameter dictionary for listing directories |

Parameter dictionary for listing directories

| Parameter Name      | **Type** | **Required** | Description                         |
| -------- | ------ | ------ | ---------------------------- |
| num      | string | Yes      | Number of directories/files to be queried. Maximum is 1000           |
| listFlag | string | No      | listFlag: Return all data if the value is greater than 0, otherwise return partial data  |
| context  | String | No      | Transparently transmitted field, which is used to turn pages. The front-end don't need to process the field, but just transmit it back in a transparent way when you want to turn to next page |
| prefix   | string | No      | Prefix search                         |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**                   |
| ------- | ------ | ------ | -------------------------- |
| code    | Int    | Yes      | API error code, 0 indicates success              |
| message | String | Yes      | Error message                       |
| data    | Array  | Yes      | Returned data, refer to "Restful API List of Directories" |

#### Example

``` c#
var folderlistParasDic = new Dictionary<string, string>();                
	folderlistParasDic.Add(CosParameters.PARA_NUM,"100");
var result = cos.GetFolderList(bucketName, folder, folderlistParasDic);
```

## File-related Operations

### Uploading a File

API Description: Uniform API for file upload. Where a file is larger than 8 M, it will be uploaded in parts within the SDK. The upload cannot be resumed from a savepoint. You need to use multipart upload API to resume the upload.

#### Method Prototype

``` c#
public string UploadFile(string bucketName, string remotePath, string localPath, 	Dictionary<string, string>  parameterDic = null)
```

#### Parameter Description

| **Parameter Name**      | **Type**                     | **Required** | **Description**                                 |
| ------------ | -------------------------- | ------ | ---------------------------------------- |
| bucketName   | string                     | Yes      | bucket name. To create a bucket, refer to [Create Bucket](/document/product/430/5887) |
| remotePath   | string                     | Yes      | Full path of a file on server                               |
| localPath    | string                     | Yes      | Local path of a file                                   |
| parameterDic | Dictionary<string, string> | No      | Parameter dictionary for uploading files                                 |

Parameter dictionary for uploading files

| Parameter Name        | Type     | Required   | Description                                     |
| ---------- | ------ | ---- | ---------------------------------------- |
| biz_attr   | string | No    | File attribute                                     |
| insertOnly | string | No    | Whether to overwrite the file with the same name. 0: Allowed; 1: Not Allowed (default)                  |
| slice_size | string | No    | Available values: 64*1024 512*1024, 1*1024*1024 (default), 2*1024*1024, and 3*1024*1024 |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**                   |
| ------- | ------ | ------ | -------------------------- |
| code    | Int    | Yes      | Error code, 0 indicates success                  |
| message | String | Yes      | Error message                       |
| data    | Array  | Yes      | Returned data, refer to "Restful API File Creation" |

#### Example

``` c#
var uploadParasDic = new Dictionary<string, string>();                
uploadParasDic.Add(CosParameters.PARA_BIZ_ATTR,"file attribute");
uploadParasDic.Add(CosParameters.PARA_INSERT_ONLY,"0");
uploadParasDic.Add(CosParameters.PARA_SLICE_SIZE,SLICE_SIZE.SLIZE_SIZE_3M.ToString());
result = cos.UploadFile(bucketName, remotePath, localPath, uploadParasDic);
```

### Updating File Attributes

API Description: It is used to update the custom attribute of a directory business. The custom attribute field of a business can be updated through this API.

#### Method Prototype

``` c#
public string UpdateFile(string bucketName, string remotePath, Dictionary<string, string> parameterDic = null)
```

#### Parameter Description

| **Parameter Name**      | **Type** | **Required** | **Description**   |
| ------------ | ------ | ------ | ---------- |
| bucketName   | string | Yes      | bucket name   |
| remotePath   | string | Yes      | Full path of a file on COS |
| parameterDic | string | No      | Parameter dictionary for updating files   |

Parameter dictionary for updating files

| Parameter Name                 | Type     | Required   | Description                                     |
| ------------------- | ------ | ---- | ---------------------------------------- |
| biz_attr            | string | No    | File attribute to be updated                               |
| authority           | string | No    | eInvalid (inherit the read/write permissions of bucket); eWRPrivate (private read/write permissions); eWPrivateRPublic (public read permission and private write permission) |
| Cache-Control       | string | No    | Cache mechanism followed by specified requests and responses, e.g. no-cache; max-age=200    |
| Content-Type        | string | No    | MIME type of response content, e.g. text/html                  |
| Content-Disposition | string | No    | A default file name will be given when saving the response content from the user request as a file, e.g. attachment; filename="fname.ext" |
| Content-Language    | string | No    | Language used, e.g. zh-CN                            |
| x-cos-meta- custom content    | string | No    | A parameter that starts with "x-cos-meta-". Users can, based on business scenarios, set the parameters in Header. |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |

#### Example

``` c#
var optionParasDic = new Dictionary<string, string>();
	optionParasDic.Add(CosParameters.PARA_BIZ_ATTR,"new attribute");
    optionParasDic.Add(CosParameters.PARA_AUTHORITY,AUTHORITY.AUTHORITY_PRIVATEPUBLIC);
	optionParasDic.Add(CosParameters.PARA_CACHE_CONTROL,"no");
	optionParasDic.Add(CosParameters.PARA_CONTENT_TYPE,"application/text");
	optionParasDic.Add(CosParameters.PARA_CONTENT_DISPOSITION,"filename=\"test.pdf\"");
	optionParasDic.Add(CosParameters.PARA_CONTENT_LANGUAGE,"en");
	optionParasDic.Add("x-cos-meta-test","test");
result = cos.UpdateFile(bucketName, remotePath, optionParasDic);
```

### Querying a File

API Description: It is used to query a file. Attributes of a file can be queried through this API.

#### Method Prototype

``` c#
public string GetFileStat(string bucketName, string remotePath)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | Yes      | bucket name   |
| remotePath | string | Yes      | Full path of a file on COS |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**                     |
| ------- | ------ | ------ | ---------------------------- |
| code    | Int    | Yes      | Error code, 0 indicates success                    |
| message | String | Yes      | Error message                         |
| data    | Array  | Yes      | File attributes, refer to "Restful API Query for File" |

#### Example

``` c#
var result = cos.GetFileStat(bucketName, remotePath);
```

### Deleting a File

API Description: It is used to delete a file. An uploaded file can be deleted through this API.

#### Method Prototype

``` c#
public string DeleteFile(string bucketName, string remotePath) 
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | Yes      | bucket name   |
| remotePath | string | Yes      | Full path of a file on server |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |

#### Example

``` c#
var result = cos.DeleteFile(bucketName, remotePath);
```

### Multipart Upload list

API Description: It is used to query the status of multipart upload

#### Method Prototype

``` c#
public string UploadSliceList(string bucketName, string remotePath)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | Yes      | bucket name   |
| remotePath | string | Yes      | Full path of a file on server |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |
| data    | Array  | Yes      | Information of multipart upload    |

data description when upload has been completed

| **Parameter Name**       | **Type** | **Required** | **Description**                   |
| ------------- | ------ | ------ | -------------------------- |
| url           | String | Yes      | URL for file operation                   |
| access_url    | String | Yes      | Generated download url of the file                 |
| source_url    | String | Yes      | Source address                        |
| resource_path | String | Yes      | Resource path. Format: /appid/bucket/xxx |
| preview_url   | String | No      | Preview address                       |

data description when upload has not been completed

| **Parameter Name**    | **Type**     | **Required** | **Description**                                 |
| ---------- | ---------- | ------ | ---------------------------------------- |
| session    | String     | Yes      | Session ID returned by init                                 |
| filesize   | Int        | Yes      | File size                                     |
| slice_size | Int        | Yes      | Size of a part (64K-3M). If it is larger than 1 M, the size must be an integral multiple of 1M               |
| sha        | String     | No      | Full text sha value of a file. The value will be returned if it's used during init                     |
| listparts  | Json Array | Yes      | Part that has been uploaded, e.g. [{"offset":0, "datalen":1024}, {}, {}]. |

#### Example

``` c#
var fileSha = SHA1.GetFileSHA1(localPath);
var result = SliceUploadInit(bucketName, remotePath, localPath, fileSha, bizAttribute, sliceSize, insertOnly);
```

### Multipart Upload init

API Description: The first handshake in multipart upload. If the last part has not been uploaded, {"code":-4019,"message":"_ERROR_FILE_NOT_FINISH_UPLOAD"}init will be returned

API Description: The first handshake in multipart upload

#### Method Prototype

``` c#
public string SliceUploadInit(string bucketName, string remotePath, string localPath, string fileSha,string bizAttribute = "", int sliceSize = SLICE_SIZE.SLIZE_SIZE_1M, int insertOnly = 1)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | Yes      | bucket name   |
| remotePath | string | Yes      | Full path of a file on server |
| localPath  | string | Yes      | Local path of a file     |
| fileSha    | string | Yes      | Sha value of a file    |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |
| data    | Array  | Yes      | Information of multipart upload    |

data Description

| **Parameter Name**       | **Type**     | **Required** | **Description**                           |
| ------------- | ------ | ------ | ---------------------------------- |
| session       | string | No      | (Available in most cases of non-instant upload) Unique ID to identify the transmission progress of current file       |
| slice_size    | Int    | No      | (Available in most cases of non-instant upload) Size of a part                 |
| serial_upload | int    | No      | (Available in most cases of non-instant upload) 1: Only serial multipart upload is supported; others: Parallel multipart upload is supported |

#### Example

``` c#
var fileSha = SHA1.GetFileSHA1(localPath);
var result = SliceUploadInit(bucketName, remotePath, localPath, fileSha, bizAttribute, sliceSize, insertOnly);
```



### Multipart Upload

API Description: Data of multipart upload

#### Method Prototype

``` c#
public string SliceUploadData(string bucketName, string remotePath, string localPath, string fileSha, string session, long offset,int sliceSise,string sign)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**       |
| ---------- | ------ | ------ | -------------- |
| bucketName | string | Yes      | bucket name       |
| remotePath | string | Yes      | Full path of a file on server     |
| localPath  | string | Yes      | Local path of a file         |
| fileSha    | string | Yes      | Sha value of a file        |
| session    | string | Yes      | Unique ID to identify the transmission progress of current file |
| offset     | int    | Yes      | Offset of the part         |
| sliceSize  | int    | Yes      | Size of a part          |
| sign       | string | Yes      | Signature (multiple-time)         |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |
| data    | Array  | Yes      | Information of multipart upload    |

data Description

| **Parameter Name**       | **Type**     | **Required** | **Description**                           |
| ------------- | ------ | ------ | ---------------------------------- |
| session       | string | Yes     | (Available in most cases of non-instant upload) Unique ID used to identify the transmission progress of the current file       |
| offset        | Int    | Yes      | Offset of current part                        |
| datalen       | int    | Yes      | The part length (slice_size); returned `datalen` is the size of current part                       |
| serial_upload | int    | No      | (Available in most cases of non-instant upload) 1: Only serial multipart upload is supported; others: Parallel multipart upload is supported |

#### Example

``` c#
var fileSha = SHA1.GetFileSHA1(localPath);
var result = SliceUploadDataInit(bucketName, remotePath, localPath, fileSha, session, offset, sliceSize,sign);
```



### Multipart Upload finish

API Description: It is used to indicate that all multipart upload operations are successfully performed

#### Method Prototype

``` c#
public string SliceUploadFinish(string bucketName, string remotePath, string localPath, string fileSha, string session)
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**       |
| ---------- | ------ | ------ | -------------- |
| bucketName | string | Yes      | bucket name       |
| remotePath | string | Yes      | Full path of a file on server     |
| localPath  | string | Yes      | Local path of a file         |
| fileSha    | string | Yes      | Sha value of a file        |
| session    | string | Yes      | Unique ID to identify the transmission progress of current file |

#### Returned Result

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |
| data    | Array  | Yes      | Information of multipart upload    |

data Description

| **Parameter Name** | **Type** | **Required** | **Description**                     |
| ------- | ------ | ------ | ---------------------------- |
| session | string | Yes      | (Available in most cases of non-instant upload) Unique ID to identify the transmission progress of current file |
| offset  | Int    | Yes      | Offset of current part                  |
| datalen | int    | Yes      | Length of a part                       |

#### Example

``` c#
result = SliceUploadFinish(bucketName,remotePath,localPath,fileSha, sessionbizAttribute, sliceSize, insertOnly);
```

