## Preparations for Development

### Related Resources

[cos php sdk v4 github Project](https://github.com/tencentyun/cos-php-sdk-v4)

### Development Environment

1. PHP 5.3.0 or above is supported
2. Get APP ID, SecretID and SecretKey from the Console, and modify configurations in cos-php-sdk-v4/cloudcos/conf.php.



### Configuring SDK

After the SDK is downloaded, load cos-php-sdk-v4/include.php and set the global timeout and the region of COS when using the SDK.

``` php
require('cos-php-sdk-v4/include.php'); 
use qcloudcos\Cosapi;

Cosapi::setTimeout(180);

// Set the region of COS, wherein:
//     South China  -> gz
//     East China -> sh
//     North China  -> tj
Cosapi::setRegion('gz');
```

If HTTPS is required to be supported, modify the value of API_COSAPI_END_POINT in conf.php as follows:

``` php
const API_COSAPI_END_POINT = 'https://region.file.myqcloud.com/files/v2/';
```

## Generating Signature

### Multiple-time Signature

#### Method Prototype

``` php
public static function createReusableSignature($expiration, $bucket, $filepath);
```

#### Parameter Description

| Parameter Name        | Type     | Required   | Description         |
| ---------- | ------ | ---- | ------------ |
| expiration | long   | Yes    | Expiration time, Unix timestamp |
| bucket     | String | Yes    | bucket name    |
| filepath   | String | No    | File path         |

#### Example

``` php
$expiration = time() + 60;	
$bucket = 'testbucket';
$sign = Auth::appSign($expiration, $bucket);
```

### One-time Signature

#### Method Prototype

``` php
public static function createNonreusableSignature($bucket, $filepath);
```

#### Parameter Description

| Parameter Name      | Type     | Required   | Description                                     |
| -------- | ------ | ---- | ---------------------------------------- |
| bucket   | String | Yes    | bucket name                                |
| Filepath | String | Yes | File path shall begin with a forward slash. For example, /filepath/filename is the full path of the file under the bucketname |

#### Example

``` php
$bucket = 'testbucket';
$filepath = "/myFloder/myFile.rar";
$sign = Auth::createNonreusableSignature($bucket, $path);
```

## Directory-related Operations

### Creating a Directory

API Description: It is used to create a directory. A directory can be created under specified bucket through this API.

#### Method Prototype

``` php
public static function createFolder($bucketName, $path, $bizAttr = null);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**      |
| ---------- | ------ | ------ | ------------- |
| bucketName | String | Yes      | bucket name     |
| path       | String | Yes      | Full path of a directory         |
| bizAttr    | String | No      | Directory attributes, maintained by a business server|

#### Returned Result (json)

| **Parameter Name** | **Type** | Required   | **Description**                                 |
| ------- | ------ | ---- | ---------------------------------------- |
| code    | Int    | Yes    | Error code, 0 indicates success                                |
| message | String | Yes     | Error message                                     |
| data    | Array  | No    | Returned data, refer to ["Restful API Directory Creation"](/document/product/436/6061) |

#### Example

``` php
$bizAttr = "attr_folder";
$result  = Cosapi::createFolder($bu	cketName, $path,$bizAttr)
```

### Updating Directory

API Description: It is used to update the custom attribute of directory business. The custom attribute field of business can be updated through this API.

#### Method Prototype

``` php
public static function updateFolder($bucketName, $path, $bizAttr = null);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | Yes      | bucket name |
| path       | String | Yes      |Directory path      |
| bizAttr    | String | No      | Directory attribute    |

#### Returned Result (json)

| **Parameter Name** | **Type** | Required   | **Description**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | Yes    | Error code, 0 indicates success |
| message | String | Yes    | Error message      |

#### Example

``` php
$bizAttr = "folder new attribute";
$result  = Cosapi::updateFolder($bucketName, $path, $bizAttr)
```

### Querying a Directory

API Description: It is used to query the directory attribute. The attribute of a directory can be queried through this API.

#### Method Prototype

``` php
public static function statFolder($bucketName, $path);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | Yes      | bucket name |
| path       | String | Yes      |Directory path      |

#### Returned Result (json)

| **Parameter Name** | **Type** | Required   | **Description**                                 |
| ------- | ------ | ---- | ---------------------------------------- |
| code    | Int    | Yes    | Error code, 0 indicates success                                |
| message | String | Yes     | Error message                                     |
| data    | Array  | No    | Directory attributes, refer to ["Restful API Query for Directory"](/document/product/436/6063) |

#### Example

``` php
$result = Cosapi::statFolder($bucketName, $path);
```

### Deleting a Directory

API Description: It is used to delete a directory. An empty directory can be deleted through this API, but a directory with valid files or directories cannot be deleted.

#### Method Prototype

``` php
public static function delFolder($bucketName, $path);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | Yes      | bucket name |
| path       | String | Yes      | Full path of a directory     |

#### Returned Result (json)

| **Parameter Name** | **Type** | Required   | **Description**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | Yes    | Error code, 0 indicates success |
| message | String | Yes    | Error message      |

#### Example

``` php
$result = Cosapi::delFolder($bucketName, $path);
```

### Listing Files and Directories under a Directory

API Description: It is used to list the files and directories under a directory. The attributes of the files and directories under a directory can be queried through this API.

#### Method Prototype

``` php
public static function listFolder($bucketName, $path, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| bucketName | String | Yes      | bucket name                                 |
| path       | String | Yes      | Full path of a directory                                   |
| num      | string | Yes      | Number of directories/files to be queried                              |
| context    | String | No      | Transparently transmitted field. If you want to query the first page, an empty string should be passed. To turn pages, please transmit context in the returned values of the previous page to the parameters in a transparent way. "order" is used to specify the page-turning order. If "order" = 0, a page-forward action will be performed from the current page; if "order" = 1, a page-back action will be performed from the current page |
| order      | int    | No      | 0 = Page forward (default), 1 = Page back                          |
| pattern    | String | No      | eListBoth: list both files and directories; eListDirOnly: list directories only; eListFileOnly: list files only |

#### Returned Result (json)

| **Parameter Name** | **Type** | **Required** | **Description**                                 |
| ------- | ------ | ------ | ---------------------------------------- |
| code    | Int    | Yes      | API error code, 0 indicates success                            |
| message | String | Yes      | Error message                                     |
| data    | Array  | Yes      | Returned data, refer to ["Restful API List of Directories"](/document/product/436/6062) |

#### Example

``` php
$result = Cosapi::listFolder($bucketName, $path, 20, 'eListBoth',0);
```

### Listing Files and Directories with Specified Prefixes under a Directory

API Description: It is used to list the files and directories with specified prefixes under a directory. The data of the files and directories with specified prefixes under a directory can be queried through this API.

#### Method Prototype

``` php
public static function prefixSearch($bucketName, $prefix, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| bucketName | String | Yes      | bucket name. To create a bucket, refer to [Create Bucket](/document/product/436/6245) |
| prefix     | String | Yes      | List all files with this prefix (with full path)                        |
| num      | string | Yes      | Number of directories/files to be queried                              |
| context    | String | No      | Transparently transmitted field. If you want to query the first page, an empty string should be passed. To turn pages, please transmit context in the returned values of the previous page to the parameters in a transparent way. "order" is used to specify the page-turning order. If "order" = 0, a page-forward action will be performed from the current page; if "order" = 1, a page-back action will be performed from the current page |
| order      | int    | No      | 0 = Page forward (default), 1 = Page back                          |
| pattern    | String | No      | eListBoth: list both files and directories; eListDirOnly: list directories only; eListFileOnly: list files only |

#### Returned Result (json)

| **Parameter Name** | **Type** | **Required** | **Description**                                 |
| ------- | ------ | ------ | ---------------------------------------- |
| code    | Int    | Yes      | Error code, 0 indicates success                                |
| message | String | Yes      | API error code                                 |
| data    | Array  | Yes      | Returned data, refer to ["Restful API List of Directories"](/document/product/436/6062) |

#### Example

``` php
$prefix= "/myFolder/2015-";
$result = Cosapi::prefixSearch($bucketName, $prefix, 20, 'eListBoth',0);
```

## File-related Operations

### Uploading a File

API Description: Uniform API for file upload. Where a file is larger than 20 M, it will be uploaded in parts within the SDK.

#### Method Prototype

``` php
public static function upload($bucketName, $srcPath, $dstPath, 
               $bizAttr = null, $slicesize = null, $insertOnly = null);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| bucketName | String | Yes      | bucket name. To create a bucket, refer to [Create Bucket](/document/product/436/6245) |
| srcPath    | String | Yes      | Full path of local files to be uploaded                              |
| dstPath    | String | Yes      | Full path of a file on COS server, excluding /appid/bucketname       |
| bizAttr    | String | No      |  File attribute, maintained by a business server                                |
| slicesize  | int    | No      | File part size. Where a file is larger than 20 M, it will be uploaded in parts within the SDK. The default part size is 1 M. The maximum part size is 3 M |
| insertOnly | int    | No      | Whether overwriting a file with the same name is allowed. 0: Allowed; 1: Not Allowed                     |

#### Returned Result (json)

| **Parameter Name** | **Type** | Required   | **Description**                                 |
| ------- | ------ | ---- | ---------------------------------------- |
| code    | Int    | Yes    | Error code, 0 indicates success                                |
| message | String | Yes     | Error message                                     |
| data    | Array  | Yes    | Returned data, refer to [Restful API File Creation](/document/product/436/6066) |

#### Example

``` php
$dstPath = "/myFolder/test.mp4";
$bizAttr = "";
$insertOnly = 0;
$sliceSize = 3 * 1024 * 1024;
$result = Cosapi::upload($srcPath,$bucketName,dstPath ,"biz_attr");
```

### Updating File Attributes

API Description: It is used to update the custom attribute of a directory business. The custom attribute field of a business can be updated through this API.

#### Method Prototype

``` php
public static function update($bucketName, $path, 
                  $bizAttr = null, $authority=null,$customer_headers_array=null);
```

#### Parameter Description

| **Parameter Name**                | **Type** | **Required** | **Description**                                 |
| ---------------------- | ------ | ------ | ---------------------------------------- |
| bucketName             | String | Yes      | bucket name                                |
| path                   | String | Yes      | Full path of a file on a file server, excluding /appid/bucketname        |
| bizAttr                | String | No      | File attribute to be updated                               |
| authority              | String | No      | eInvalid (inherit the read/write permission of bucket); eWRPrivate (private read/write permissions); eWPrivateRPublic (public read permission and private write permission) |
| customer_headers_array | String | No      | User-defined header. Available parameters: 'Cache-Control', 'Content-Type', 'Content-Disposition', 'Content-Language', and parameters with the prefix of 'x-cos-meta-' |

#### Returned Result (json)

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |

#### Example

``` php
$bizAttr = "";
$authority = "eWPrivateRPublic";
$customer_headers_array = array(
    'Cache-Control' => "no",
    'Content-Language' => "ch",
);
$result = Cosapi::update($bucketName, $dstPath, $bizAttr,$authority, $customer_headers_array);
```

### Querying a File

API Description: It is used to query a file. Attributes of a file can be queried through this API.

#### Method Prototype

``` php
 public static function stat($bucketName, $path); 
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**     |
| ---------- | ------ | ------ | ------------ |
| bucketName | String | Yes      | bucket name    |
| path       | String | Yes      | Full path of a file on a file server |

#### Returned Result (json)

| **Parameter Name** | **Type** | **Required** | **Description**                                 |
| ------- | ------ | ------ | ---------------------------------------- |
| code    | Int    | Yes      | Error code, 0 indicates success                                |
| message | String | Yes      | Error message                                     |
| data    | Array  | No    | File attributes, refer to [Restful API Query for File](/document/product/436/6069) |

#### Example

``` php
$result = Cosapi::stat($bucketName, $path);
```

### Deleting a File

API Description: It is used to delete a file. An uploaded file can be deleted through this API.

#### Method Prototype

``` php
public static function delFile($bucketName, $path);
```

#### Parameter Description

| **Parameter Name**    | **Type** | **Required** | **Description**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | Yes      | bucket name |
| path       | String | Yes      | Full path of a file    |

#### Returned Result (json)

| **Parameter Name** | **Type** | **Required** | **Description**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | Yes      | Error code, 0 indicates success |
| message | String | Yes      | Error message      |

#### Example

``` php
$result = Cosapi::delFile($bucketName, $path);
```

