## Preparations for Development

### Related Resources

[github Project](https://github.com/tencentyun/cos-cpp-sdk-v4)

### Development Environment

1. Install the library and header files of openssl [http://www.openssl.org/source/](http://www.openssl.org/source/) 
2. Install the library and header files of curl https://curl.haxx.se/download.html
3. Install the library and header files of jsoncpp [https://github.com/open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp) 
4. Install the library and header files of boost [http://www.boost.org/](http://www.boost.org/) 
5. Install cmake tools [http://www.cmake.org/download/](http://www.cmake.org/download/) 
6. Get APP ID, SecretID, SecretKey from the console.

Note:

1. The sdk provides the library and header files of curl and jsoncpp, which can be replaced when the libraries above are complied. If the libraries above have been installed to the system, you can also delete the corresponding library and header files in the sdk.
2. By default, curl does not support multithreaded environments. If the project uses multithreading, when executing "configure" during the compiling of curl, the parameter "--enable-ares" needs to be specified to enable asynchronous DNS resolution. This can be achieved through a c-ares library, and if the system does not have one, you can download it from [http://c-ares.haxx.se/](http://c-ares.haxx.se/) for installation.
3. Version 1.y.x of jsoncpp needs the support of c++11. If it is not supported by the compiler, you can use version 0.y.x.


### Configuring SDK

Download the source code from github, and integrate it into your development environment. 

Execute the following command:

``` 
cd ${cos-cpp-sdk} 
mkdir -p build 
cd build 
cmake .. 
make 
```

There are examples of common APIs in cos_demo.cpp. The generated cos_demo can be run directly, and the generated static library name is libcossdk.a. Put the generated libcossdk.a under the lib path of your own project, and copy the include directory to the include path of your own project. 



## Generating Signature

### Multiple-time Signature

#### Method Prototype

``` c++
static string AppSignMuti(const uint64_t appId, 
                          const string &secretId, 
                          const string &secretKey, 
                          const uint64_t expired_time, 
                          const string &bucketName); 
```

#### Parameter Description

| Parameter Name          | **Type**   | **Required** | **Default Value** | **Description**     |
| ------------ | -------- | -------- | ------- | ------------ |
| appId        | uint64_t | Yes        | None       | APP ID of the project     |
| secretId     | String   | Yes        | None       | Secret ID of the user |
| secretKey    | String   | Yes        | None       | SecretKey of the user |
| expired_time | uint64_t | No        | None       | Expiration time, Unix timestamp |
| bucketName   | String   | No        | None       | bucket name     |

#### Returned Result

Return value: signature string

#### Example

``` c++
uint64_t expired = time(NULL) + 60;
string sign = Auth::AppSignMuti(10000000,"SecretId","SecretKey",expired,"bucketName");
```

### One-time Signature

#### Method Prototype

``` c++
static string AppSignOnce(const uint64_t appId, 
                          const string &secretId, 
                          const string &secretKey, 
                          const string &path, 
                          const string &bucketName); 
```

#### Parameter Description

| **Parameter Name**    | **Type**   | **Required** | **Default Value** | **Description**                                 |
| ---------- | -------- | ------ | ------- | ---------------------------------------- |
| appId      | uint64_t | Yes      | None       | APP ID of the project                                |
| secretId   | String   | Yes      | None       | SecretId of the project                              |
| secretKey  | String   | Yes      | None       | SecretKey of the project                             |
| bucketName | String   | No      | None       | bucket name                                 |
| path       | String   | Yes      | None       | File path, which shall begin with a forward slash. For example, /filepath/filename is the full path of the file under the bucketname |

#### Returned Result

Return value: signature string

#### Example

``` c++
string path= "/myFloder/myFile.rar";
sign = Auth::AppSignOnce(10000000, "SecretId", "SecretKey", path, bucketName);
```

## Initialization-related Operations

### Initialization

API description: Before using COS, you need to set COS system parameters, and then create CosConfig and CosAPI objects respectively. All the COS operations are based on CosAPI objects.

### Configuring File

``` c++
"AppID":********,
"SecretID":"*********************************",
"SecretKey":"********************************",
"Region":"sh",   //COS region. East China region: sh; South China region: gz; North China region: tj. Both upload and download domains are related to it, so it has to be correct
"SignExpiredTime":360, //Signature timeout
"CurlConnectTimeoutInms":180,  //http timeout
"CurlGlobalConnectTimeoutInms":360, //
"UploadSliceSize":1048576, //File part size. Available values include 524288, 1048576, 2097152, and 3145728
"IsUploadTakeSha":0, //Indicate whether the file is uploaded with sha value. 0: Without, 1: With
"DownloadDomainType":2, //Download domain type. 1: cdn, 2: cos, 3: innercos, 4: Custom domain
"SelfDomain":"",//Custom domain
"UploadThreadPoolSize":5, //Thread pool size for uploading a single file in multipart
"AsynThreadPoolSize":2, //Thread pool size for asynchronous upload and download
"LogoutType":1 //Log output type. 0: Not output, 1: Output to screen, 2: Output to syslog
```

### COS API Object Construction Prototype

``` c++
CosConfig(const string& config_file);
CosAPI(CosConfig& config);
```

## Directory-related Operations

### Creating a Directory

API Description: It is used to create a directory. A directory can be created under specified bucket through this API.

#### Method Prototype

``` c++
string CosAPI::FolderCreate(FolderCreateReq& request);        
```

#### Parameter Description

| **Parameter Name** | **Type**          | **Default Value** | **Description** |
| ------- | --------------- | ------- | -------- |
| request | FolderCreateReq | None       | Directory creation request |

| request Member | Type     | Default Value  | Setting Method | Description        |
| --------- | ------ | ---- | ---- | -------- |
| bucket    | string | None    | Constructor | bucket name |
| cosPath   | string | None    | Constructor | Destination path for uploading  |
| bizAttr   | string | Empty string | Constructor | Folder attribute    |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Description**                   |
| ------- | ------ | -------------------------- |
| code    | Int    | Error code. 0 indicates success                  |
| message | String | Description information                       |
| data    | Array  | Returned data. Refer to "Restful API Directory Creation" |

#### Example

``` c++
FolderCreateReq folderCreateReq(bucket,folder,folder_biz_attr);
string rsp = cos.FolderCreate(folderCreateReq);
```

### Updating Directory

API Description: It is used to update the custom attribute of a directory business. The custom attribute field of a business can be updated through this API.

#### Method Prototype

``` c++
string FolderUpdate(FolderUpdateReq& request);                    
```

#### Parameter Description

| **Parameter Name** | **Type**          | **Default Value** | **Description** |
| ------- | --------------- | ------- | -------- |
| request | FolderUpdateReq | None       | Directory update request |

| **Parameter Name** | **Type** | **Default Value** | **Setting Method** | **Description** |
| ------- | ------ | ------- | -------- | -------- |
| bucket  | String | None       | Constructor     | bucket name |
| cosPath | String | None       | Constructor     | Full path of a directory   |
| bizAttr | string | Null       | Constructor     | Folder attribute    |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Description**                   |
| ------- | ------ | -------------------------- |
| code    | Int    | Error code. 0 indicates success                  |
| message | String | Description information                       |
| data    | Array  | Returned data. Refer to "Restful API Directory Update" |

#### Example

``` 
FolderUpdateReq folderUpdateReq(bucket,folder, folder_biz_attr);
string rsp = cos.FolderUpdate(folderUpdateReq);
```

### Querying a Directory

API Description: It is used to query the directory attribute. The attribute of a directory can be queried through this API.

#### Method Prototype

``` c++
string CosAPI::FolderStat(FolderStatReq& request);
```

#### Parameter Description

| **Parameter Name** | **Type**        | **Default Value** | **Description** |
| ------- | ------------- | ------- | -------- |
| request | FolderUpdateReq | None       | Directory query request |

| **Parameter Name** | **Type** | **Default Value** | **Setting Method** | **Description** |
| ------- | ------ | ------- | -------- | -------- |
| bucket  | String | None       | Constructor     | bucket name |
| cosPath | String | None       | Constructor     | Full path of a directory   |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Description**  |
| ------- | ------ | --------- |
| code    | Int    | Error code. 0 indicates success |
| message | String | Description information      |

#### Example

``` c++
FolderStatReq folderStatReq(bucket,folder);
string rsp = cos.FolderStat(folderStatReq);
```

### Deleting a Directory

API Description: It is used to delete a directory. Empty directories can be deleted through this API, but a directory with valid files or directories cannot be deleted.

#### Method Prototype

``` c++
string CosAPI::FolderDelete(FolderDeleteReq& request);
```

#### Parameter Description

| **Parameter Name** | **Type**          | **Default Value** | **Description** |
| ------- | --------------- | ------- | -------- |
| request | FiledeleteReq | None       | File deletion request |

| **Parameter Name** | **Type** | **Default Value** | **Setting Method** | **Description** |
| ------- | ------ | ------- | -------- | -------- |
| bucket  | String | None       | Constructor     | bucket name |
| cosPath | String | None       | Constructor     | Full path of a directory   |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Description**  |
| ------- | ------ | --------- |
| code    | Int    | Error code. 0 indicates success |
| message | String | Description information      |

#### Example

``` c++
FolderDeleteReq folderDeleteReq(bucket,folder);
string rsp = cos.FolderDelete(folderDeleteReq);
```

### List of Directories

API Description: It is used to list the files and directories under a directory. The attributes of the files and directories under a directory can be queried through this API.

#### Method Prototype

``` c++
string CosAPI::FolderList(FolderListReq& request);
```

#### Parameter Description

| **Parameter Name** | **Type**        | **Default Value** | **Description** |
| ------- | ------------- | ------- | -------- |
| request | FolderUpdateReq | None       | Directory list request |

| **Parameter Name** | **Type** | **Default Value** | **Setting Method** | **Description**                                 |
| ------- | ------ | ------- | -------- | ---------------------------------------- |
| bucket  | String | None       | Constructor     | bucket name                                 |
| cosPath | String | None       | Constructor     | Full path of a directory                                   |
| listNum | int    | 1000    | Constructors     | Number of entries for the query. The maximum is 1000                             |
| context | string | Empty string    | Constructor     | Query context. If you want to query the first page, an empty string should be passed. To turn pages, "context" in the query response of the previous page needs to be set in the parameter |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Required** | **Description**                   |
| ------- | ------ | ---------- | -------------------------- |
| code    | Int    | Yes          | Error code. 0 indicates success                  |
| message | String | Yes          | Description information                       |
| data    | Array  | Yes          | Returned data, refer to "Restful API List of Directories" |

#### Example

``` c++
FolderListReq folderListReq(bucket,folder);
string rsp = cos.FolderList(folderListReq);
```

## File-related Operations

### Uploading a File

API description: File upload, including single file upload and multipart upload (Files over 8 M need to be uploaded in parts).

#### Method Prototype

``` c++
string CosAPI::FileUpload(FileUploadReq& request);
```

#### Parameter Description

| **Parameter Name** | **Type**          | **Default Value** | **Description** |
| ------- | --------------- | ------- | -------- |
| request | FileUploadReq | None       | File upload request |

| **Parameter Name**    | **Type** | **Default Value** | **Setting Method**             | **Description**                               |
| ---------- | ------ | ------- | -------------------- | -------------------------------------- |
| bucket     | String | None       | Constructor                 | bucket name                               |
| srcPath    | String | None       | Constructor                 | Path of local file to be uploaded                             |
| cosPath    | String | None       | Constructor                 | Full path of a file                                 |
| bizAttr    | string | None       | setBizAttr()         | File attribute                                   |
| insertOnly | int    | 1       | Constructor and setInsertOnly() | Indicate whether to overwrite the file with the same name. 0 means overwriting the file with the same name. 1 means not overwriting, and when the file exists, an error will be returned |
| sliceSize  | int    | 1048576 | setSliceSize()       | Size of a part. Available values include 512K, 1M (default), 2M, and 3M. It needs to be converted to bytes   |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Required** | **Description**                   |
| ------- | ------ | ---------- | -------------------------- |
| code    | Int    | Yes          | Error code. 0 indicates success                  |
| message | String | Yes          | Description information                       |
| data    | Array  | No          | Returned data. Refer to "Restful API File Upload" |

#### Example

``` c++
FileUploadReq fileUploadReq(bucket, srcPath, dstPath);
string rsp = cos.FileUpload(fileUploadReq);
```

### Updating a File

API Description: It is used to update the custom attribute of a directory business. The custom attribute field of a business can be updated through this API.

#### Method Prototype

``` C++
string CosAPI::FileUpdate(FileUpdateReq& request);
```

#### Parameter Description

| **Parameter Name** | **Type**        | **Default Value** | **Description** |
| ------- | ------------- | ------- | -------- |
| request | FileUpdateReq | None       | File update request |

| **Parameter Name**       | **Type** | **Required** | **Setting Method**          | **Description**                                 |
| ------------- | ------ | -------- | ----------------- | ---------------------------------------- |
| bucket        | String | Yes        | Constructor              | bucket name                                 |
| cosPath       | String | Yes        | Constructor              | Path of the file in Cloud Object Storage                            |
| bizAttr       | string | No        | setBizAttr()      | File attribute                                     |
| authority     | string | No        | setAuthority()    | File permission. The valid values of bucket permissions will be inherited by default: eInvalid (inherit bucket), eWRPrivate (private), eWPrivateRPublic (public-read) |
| forbid        | int    | No        | setForbid()       | Flag of being banned for a file                                   |
| custom_header | map    | No        | setCustomHeader() | Custom attribute                                  |

custom_header Description

| **Parameter Name**             | **Type** | **Required** | **Description**                                 |
| ------------------- | ------ | -------- | ---------------------------------------- |
| Cache-Control       | string | No        | Refer to the Cache-Control in HTTP header                     |
| Content-Type        | string | No        | Refer to the Content-Type in HTTP header                      |
| Content-Disposition | string | No        | Refer to the Content-Language in HTTP header                  |
| Content-Language    | string | No        | Refer to the Content-Disposition in HTTP header               |
| Content-Encoding    | string | No        | Refer to the Content-Encoding in HTTP header                  |
| x-cos-meta-         | string |  No        | Customized HTTP header. Parameters must start with x-cos-meta-, and the value is defined by the user. Multiple values are allowed |

**Tips:** custom_header is updated as a whole, i.e., you can choose to update some of the attributes, and if you just update some, other attributes will be erased.

#### Returned Result

The json string of the request result from the function return value will be returned:

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code. 0 indicates success |
| message | String | Yes          | Description information      |

#### Example

``` c++
FileUpdateReq fileUpdateReq(bucket,dstpath);
fileUpdateReq.setBizAttr(file_biz_attr);
fileUpdateReq.setAuthority(auth);
fileUpdateReq.setForbid(0);
fileUpdateReq.setCustomHeader(custom_header);
string rsp = cos.FileUpdate(fileUpdateReq);
```

### Querying a File

API Description: It is used to query a file. Attributes of a file can be queried through this API.

#### Method Prototype

``` c++
string CosAPI::FileStat(FileStatReq& request)
```

#### Parameter Description

| **Parameter Name** | **Type**      | **Default Value** | **Description** |
| ------- | ----------- | ------- | -------- |
| request | FileStatReq | None       | File query list request |

FileStatReq

| **Parameter Name** | **Type** | **Required** | **Default Value** | **Description**       |
| ------- | ------ | -------- | ------- | -------------- |
| bucket  | String | Yes        | None       | bucket name       |
| cosPath | String | Yes        | None       | Full path of the file in Cloud Object Storage |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Required** | **Description**                   |
| ------- | ------ | -------- | -------------------------- |
| code    | Int    | Yes        | Error code. 0 indicates success                  |
| message | String | Yes        | Error message                       |
| data    | Array  | Yes        | Returned data. Refer to "Restful API Query for File" |

#### Example

``` c++
FileStatReq fileStatReq(bucket,dstpath);
string rsp = cos.FileStat(fileStatReq);
```

### Deleting a File

API Description: It is used to delete a file. An uploaded file can be deleted through this API.

#### Method Prototype

``` c++
FileDeleteReq fileDeleteReq(bucket,dstpath);
string rsp = cos.FileDelete(fileDeleteReq);
```

#### Parameter Description

| **Parameter Name** | **Type**          | **Default Value** | **Description** |
| ------- | --------------- | ------- | -------- |
| request | FiledeleteReq | None       | File deletion request |

FiledeleteReq

| **Parameter Name** | **Type** | **Required** | **Default Value** | **Description**       |
| ------- | ------ | -------- | ------- | -------------- |
| bucket  | String | Yes        | None       | bucket name       |
| cosPath | String | Yes        | None       | Full path of the file in Cloud Object Storage |

#### Returned Result

The json string of the request result from the function return value will be returned

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code. 0 indicates success |
| message | String | Yes          | Description information      |

#### Example

``` c++
FileDeleteReq fileDeleteReq(bucket,dstpath);
string rsp = cos.FileDelete(fileDeleteReq);
```

