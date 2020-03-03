## Basic APIs
> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

### Obtain Bucket list
#### Method prototype
```php
public Guzzle\Service\Resource\Model listBucket(array $args = array())
```

#### Request example

```php
//Obtain bucket list
$result = $cosClient->listBuckets();
```
#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [Owner] => Array
                (
                    [ID] => qcs::cam::uin/3210232098:uin/3210232098
                    [DisplayName] => 3210232098
                )

            [Buckets] => Array
                (
                    [0] => Array
                        (
                            [Name] => accesslog-10055004
                            [Location] => ap-shanghai
                            [CreationDate] => 2016-07-29T03:09:54Z
                        )

                    [1] => Array
                        (
                            [Name] => accesslogbj-10055004
                            [Location] => ap-beijing
                            [CreationDate] => 2017-08-02T04:00:24Z
                        )

                )

            [RequestId] => NWE3YzgxZmFfYWZhYzM1MGFfMzc3MF9iOGY5OQ==
        )

)
```
### Create Bucket

#### Method prototype

```php
// Create a bucket
public Guzzle\Service\Resource\Model createBucket(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :---------: |    :-----------------: | :--------:   | :-------------: |
| Bucket   |      Bucket name    |    string     |  Yes              |
| Acl      | ACL permission control |    string     | No | 

#### Request example

```php
//Create a bucket
//The bucket name entered must be in a format of {name}-{appid}
$result = $cosClient->createBucket(array('Bucket' => 'testbucket-125000000'));
```
#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [Location] => 
            [RequestId] => NWE3YzgzMTZfMTdiMjk0MGFfNTQ1OF8xNjEyYmE=
        )
)
```
### Delete Bucket

#### Method prototype

```php
// Delete a bucket
public Guzzle\Service\Resource\Model deleteBucket(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: |    :------------: |  :--------:   | :----------------------------------: |
| Bucket  |  Bucket name        |     string         |               Yes               |

#### Request Example

```php
//Delete a bucket
//The bucket name entered must be in a format of {name}-{appid}
$result = $cosClient->deleteBucket(array('Bucket' => 'testbucket-125000000'));
```
#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [RequestId] => NWE3YzgzMTZfMTdiMjk0MGFfNTQ2MF8xNjBjZTI=
        )
)
```
### Simple upload of file

#### Method prototype

```php
public Guzzle\Service\Resource\Model putObject(array $args = array())
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  | Bucket name, which is composed of numbers, lowercase letters and "-". | string | Yes |
 |  Body  | The content of the uploaded file, which can be a file stream or a byte stream |  file/string |  Yes |
 |  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. | string |  Yes | 
 |  ACL  | Sets file ACL, such as 'private', 'public-read', and 'public-read-write' | string | No | 
 |  GrantFullControl  |Grants the specified account the permission to read and write files |  string | No | 
 |  GrantRead  | Grants the specified account the permission to read files | string | No |
 |  GrantWrite  | Grants the specified account the permission to write files |  string | No |
 |  StorageClass  | Sets file storage type: STANDARD and STANDARD_IA. Default: STANDARD | String |   No |
 |  Expires  | Sets Content-Expires |  string | No | 
 |  CacheControl  | Cache policy. Sets Cache-Control |  string | No |
 |  ContentType  | Content type. Sets Content-Type |string | No |  
 |  ContentDisposition  | File name. Sets Content-Disposition |  string | No |
 |  ContentEncoding  | Encoding format. Sets Content-Encoding |  string | No |
 |  ContentLanguage  | Language type. Sets Content-Language |  string | No |
 |  ContentLength  | Sets transmission length | string |   No | 
 |  ContentMD5  | Sets MD5 of the uploaded file for verification | string | No | 
 |  Metadata | User-defined file meta information | array | No |
 |  ServerSideEncryption | Server-side encryption method | string |   No |
#### Request example

```php
# Upload a file
## putObject (API for upload. File size is limited to 5 GB)
### Upload strings in memory
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => 'Hello World!'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### Upload file stream
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => fopen($local_path, 'rb')));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### Set header and meta
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => fopen($local_path, 'rb'),
        'ACL' => 'string',
        'CacheControl' => 'string',
        'ContentDisposition' => 'string',
        'ContentEncoding' => 'string',
        'ContentLanguage' => 'string',
        'ContentLength' => integer,
        'ContentType' => 'string',
        'Expires' => 'mixed type: string (date format)|int (unix timestamp)|\DateTime',
        'GrantFullControl' => 'string',
        'GrantRead' => 'string',
        'GrantWrite' => 'string',
        'Metadata' => array(
            'string' => 'string',
        ),
        'StorageClass' => 'string'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [Expiration] => 
            [ETag] => "ed076287532e86365e841e92bfc50d8c"
            [ServerSideEncryption] => AES256
            [VersionId] => 
            [SSECustomerAlgorithm] => 
            [SSECustomerKeyMD5] => 
            [SSEKMSKeyId] => 
            [RequestCharged] => 
            [RequestId] => NWE3Yzg0M2NfOTcyMjViNjRfYTE1YV8xNTQzYTY=
            [ObjectURL] => http://testbucket-1252448703.cos.cn-south.myqcloud.com/11%2F%2F32%2F%2F43
        )
)
```
### Multipart upload

This API is used to split a file (limited to 40 TB) into multiple parts for upload. Concurrent upload of multiple parts is allowed.

The steps of multipart upload are as follows:

1. Initialize multipart upload, and obtain uploadid. (createMultipartUpload)
2. Upload data in parts concurrently. (uploadPart)
3. Complete multipart upload. (completeMultipartUpload)

The steps of multipart upload also include obtaining uploaded parts (listParts) and terminating multipart upload (abortMultipartUpload).

#### Method prototype

```php
// Initialize multipart upload
public Guzzle\Service\Resource\Model createMultipartUpload(array $args = array());

// Upload data in parts
public Guzzle\Service\Resource\Model uploadPart(array $args = array());
            
// Complete multipart upload
public Guzzle\Service\Resource\Model completeMultipartUpload(array $args = array());

// List uploaded parts
public Guzzle\Service\Resource\Model listParts(array $args = array());

// Abort multipart upload
public Guzzle\Service\Resource\Model abortMultipartUpload(array $args = array());
```
### Upload files
#### Request example
```php
## Upload (Advanced API for upload. Multipart upload is used by default. File size is limited to 50 TB)
### Upload strings in memory
try {
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = 'Hello World!');
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### Upload file stream
try {
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = fopen($local_path, 'rb'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### Set header and meta
try {
    $result = $cosClient->upload(
        $bucket= $bucket,
        $key = $key,
        $body = fopen($local_path, 'rb'),
        $options = array(
            'ACL' => 'string',
            'CacheControl' => 'string',
            'ContentDisposition' => 'string',
            'ContentEncoding' => 'string',
            'ContentLanguage' => 'string',
            'ContentLength' => integer,
            'ContentType' => 'string',
            'Expires' => 'mixed type: string (date format)|int (unix timestamp)|\DateTime',
            'GrantFullControl' => 'string',
            'GrantRead' => 'string',
            'GrantWrite' => 'string',
            'Metadata' => array(
                'string' => 'string',
            ),
            'StorageClass' => 'string'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

```
For a file smaller than 5 MB, use single upload.
Otherwise, use multipart upload.

#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [Location] => testbucket-1252448703.cos.cn-south.myqcloud.com/111.txt
            [Bucket] => testbucket
            [Key] => 111.txt
            [ETag] => "715691804ee474f2eb94adb2c5c01155-1"
            [Expiration] => 
            [ServerSideEncryption] => AES256
            [VersionId] => 
            [SSEKMSKeyId] => 
            [RequestCharged] => 
            [RequestId] => NWE3Yzg0YTRfOTUyMjViNjRfNWYyZF8xNTI5ZDQ=
        )
)
```
### Download files

This API is used to download files locally or to memory.

#### Method prototype

```php
// Download a file
public Guzzle\Service\Resource\Model getObject(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: |    :------------:   | :--------:   | :----------------------------------: |
| Bucket   |      Bucket name    |   string     |  Yes              |       
| Key      | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. |    string      |  Yes |       
| SaveAs   | Local file path |   string      | No |
| VersionId     |   Version number of Object        |   string      | No           |       

#### Request Example

```php
# Download a file
## getObject (Download file)
### Download the file to memory
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key));
    echo($result['Body']);
} catch (\Exception $e) {
    echo "$e\n";
}

### Download the file locally
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'SaveAs' => $local_path));
} catch (\Exception $e) {
    echo "$e\n";
}

### Specify the range of file download
/*
 * Range format: 'bytes=a-b'
 */
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Range' => 'bytes=0-10',
        'SaveAs' => $local_path));
} catch (\Exception $e) {
    echo "$e\n";
}

### Set response header
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'ResponseCacheControl' => 'string',
        'ResponseContentDisposition' => 'string',
        'ResponseContentEncoding' => 'string',
        'ResponseContentLanguage' => 'string',
        'ResponseContentType' => 'string',
        'ResponseExpires' => 'mixed type: string (date format)|int (unix timestamp)|\DateTime',
        'SaveAs' => $local_path));
} catch (\Exception $e) {
    echo "$e\n";
}
```
#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [Body] =>
            [DeleteMarker] => 
            [AcceptRanges] => bytes
            [Expiration] => 
            [Restore] => 
            [LastModified] => Fri, 09 Feb 2018 01:10:56 GMT
            [ContentLength] => 5242880
            [ETag] => "715691804ee474f2eb94adb2c5c01155-1"
            [MissingMeta] => 
            [VersionId] => 
            [CacheControl] => private
            [ContentDisposition] => attachment; filename*="UTF-8''111.txt"
            [ContentEncoding] => 
            [ContentLanguage] => 
            [ContentRange] => 
            [ContentType] => text/plain; charset=utf-8
            [Expires] => 
            [WebsiteRedirectLocation] => 
            [ServerSideEncryption] => AES256
            [SSECustomerAlgorithm] => 
            [SSECustomerKeyMD5] => 
            [SSEKMSKeyId] => 
            [StorageClass] => 
            [RequestCharged] => 
            [ReplicationStatus] => 
            [RequestId] => NWE3Yzg4ODlfMThiMjk0MGFfMmI3OV8xNWQxNDg=
        )
)
```

### Deleting Files

This API is used to delete objects on COS.

#### Method prototype

```php
// Delete a file
public Guzzle\Service\Resource\Model deleteObject(array $args = array());
```

#### Request parameters

$args is an associate array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   | 
| Bucket   |      Bucket name    |   string     |  Yes              | 
| Key      | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. |  string     |  Yes |   
| VersionId      |   Version number of Object        |   string    | No           |  

#### Request example

```php
// Delete an object on COS
$result = $cosClient->deleteObject(array(
    //The bucket name entered must be in a format of {name}-{appid}
    'Bucket' => 'testbucket-125000000',
    'Key' => 'hello.txt'));
```
#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [DeleteMarker] => 
            [VersionId] => 
            [RequestCharged] => 
            [RequestId] => NWE3Yzg5MzJfY2FhMzNiMGFfNDVjOV8yY2QyMzg=
        )
)
```


### Obtaining object attributes

Obtain the attributes of an object on COS.

#### Method prototype

```php
// Obtain file attributes
public Guzzle\Service\Resource\Model headObject(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |    string   |  Yes              |   
| Key      | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. |    string   |  Yes |    
| VersionId      |   Version number of Object        |   string    | No           | 

#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [DeleteMarker] => 
            [AcceptRanges] => 
            [Expiration] => 
            [Restore] => 
            [LastModified] => Thu, 08 Feb 2018 17:34:53 GMT
            [ContentLength] => 12
            [ETag] => "ed076287532e86365e841e92bfc50d8c"
            [MissingMeta] => 
            [VersionId] => 
            [CacheControl] => 
            [ContentDisposition] => 
            [ContentEncoding] => 
            [ContentLanguage] => 
            [ContentType] => application/octet-stream
            [Expires] => 
            [WebsiteRedirectLocation] => 
            [ServerSideEncryption] => AES256
            [SSECustomerAlgorithm] => 
            [SSECustomerKeyMD5] => 
            [SSEKMSKeyId] => 
            [StorageClass] => 
            [RequestCharged] => 
            [ReplicationStatus] => 
            [RequestId] => NWE3YzhhM2RfMWViZTk0MGFfNWMzMF8xNTFiZDg=
        )
)
```

#### Request example

```php
// Obtain the attributes of a file on COS
 //The bucket name entered must be in a format of {name}-{appid}
$result $cosClient->headObject(array('Bucket' => 'testbucket-125000000', 'Key' => 'hello.txt'));
```

### Check whether a Bucket exists

Check whether a bucket on COS exists.

#### Method prototype

```php
// Obtain file attributes
public Guzzle\Service\Resource\Model headBucket(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |   Version number of Object        |   string   | No           |      



#### Request example

```php
// Obtain the attributes of a file on COS
 //The bucket name entered must be in a format of {name}-{appid}
$result $cosClient->headBucket(array('Bucket' => 'testbucket-125000000'));
```
#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [RequestId] => NWE3YzhhN2VfY2VhMzNiMGFfMmNmXzJjNzc3Zg==
        )
)
```

### Obtaining file list

Obtain the list of files on COS.

#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model listObjects(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |    string     |  Yes              |     
| Delimiter      |      Delimiter         |    string     |  No          |    
| Marker      |          Marker        |   string     |  No          | 
| MaxKeys      |           Maximum number of objects         |  int     |   No          | 
| Prefix      |            Prefix         |string     |  No           |  

#### Request example

```php
// Obtain the bucket members
//The bucket name entered must be in a format of {name}-{appid}
$result = $cosClient->listObjects(array('Bucket' => 'testbucket-125000000'));
```
#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [Name] => testbucket-1252448703
            [Prefix] => 
            [Marker] => 
            [MaxKeys] => 1000
            [IsTruncated] => 
            [Contents] => Array
                (
                    [0] => Array
                        (
                            [Key] => 11/32/43
                            [LastModified] => 2018-02-08T17:09:16.000Z
                            [ETag] => "ed076287532e86365e841e92bfc50d8c"
                            [Size] => 12
                            [Owner] => Array
                                (
                                    [ID] => 1252448703
                                    [DisplayName] => 1252448703
                                )

                            [StorageClass] => STANDARD
                        )

                    [1] => Array
                        (
                            [Key] => 111
                            [LastModified] => 2018-02-08T17:41:11.000Z
                            [ETag] => "ed076287532e86365e841e92bfc50d8c"
                            [Size] => 12
                            [Owner] => Array
                                (
                                    [ID] => 1252448703
                                    [DisplayName] => 1252448703
                                )

                            [StorageClass] => STANDARD
                        )

                    [2] => Array
                        (
                            [Key] => 111.txt
                            [LastModified] => 2018-02-08T17:11:00.000Z
                            [ETag] => "715691804ee474f2eb94adb2c5c01155-1"
                            [Size] => 5242880
                            [Owner] => Array
                                (
                                    [ID] => 1252448703
                                    [DisplayName] => 1252448703
                                )

                            [StorageClass] => STANDARD
                        )

                )

            [RequestId] => NWE3YzhiYjdfMWJiMjk0MGFfMzA4M18xNjdiNDM=
        )
)
```

### putBucketACL

#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model putBucketACL(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |     string      |  Yes              | 
| ACL      | ACL permission control |   string       | No |   
| GrantRead | Grants read permission to the authorized user. Format: id=" ", id=" ". For authorization to a subaccount, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"; for authorization to the root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>". For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' |  string       | No |     
| GrantWrite | Grants write permission to the authorized user. Format: id=" ", id=" ". For authorization to a subaccount, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"; for authorization to the root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>". For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' |     string        | No |      
| GrantFullControl | Grants read and write permissions to the authorized user. Format: id=" ", id=" ". For authorization to a subaccount, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"; for authorization to the root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>". For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' |   string       | No |          


#### Request example

```php
#putBucketACL
try {
    $result = $cosClient->PutBucketAcl(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' => 'testbucket-125000000',
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/327874225:uin/327874225',
                    'ID' => 'qcs::cam::uin/327874225:uin/327874225',
                    'Type' => 'CanonicalUser',
                ),
                'Permission' => 'FULL_CONTROL',
            ),
            // ... repeated
        ),
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/3210232098:uin/3210232098',
            'ID' => 'qcs::cam::uin/3210232098:uin/3210232098',
        ),));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [RequestId] => NWE3YzhiZTZfZDRiMjk0MGFfODMwXzJjODllYw==
        )
)
```


### getBucketACL
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model getBucketACL(array $args = array());
```

#### Request parameters

| Field Name | Type | Default | Required | Description |
| :------: |    :------------: | :--:   | :--------:   | :----------------------------------: |
| Bucket   |     string     |  None    | Yes           |               Bucket name               |



#### Request example
```php
#getBucketACL
try {
    $result = $cosClient->GetBucketAcl(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' => 'testbucket-125000000',));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [Owner] => Array
                (
                    [ID] => qcs::cam::uin/3210232098:uin/3210232098
                    [DisplayName] => qcs::cam::uin/3210232098:uin/3210232098
                )

            [Grants] => Array
                (
                    [0] => Array
                        (
                            [Grantee] => Array
                                (
                                    [ID] => qcs::cam::uin/327874225:uin/327874225
                                    [DisplayName] => qcs::cam::uin/327874225:uin/327874225
                                )

                            [Permission] => FULL_CONTROL
                        )

                )

            [RequestId] => NWE3YzhjMTRfYzdhMzNiMGFfYjdiOF8yYzZmMzU=
        )
)
```

### putObjectACL
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model putObjectACL(array $args = array());
```

#### Request parameters
| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |     string      |  Yes              | 
 |  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. | string |  Yes | 
| ACL      | ACL permission control |   string       | No |   
| GrantRead | Grants read permission to the authorized user. Format: id=" ", id=" ". For authorization to a subaccount, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"; for authorization to the root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>". For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' |  string       | No |     
| GrantWrite | Grants write permission to the authorized user. Format: id=" ", id=" ". For authorization to a subaccount, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"; for authorization to the root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>". For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' |     string        | No |      
| GrantFullControl | Grants read and write permissions to the authorized user. Format: id=" ", id=" ". For authorization to a subaccount, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"; for authorization to the root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>". For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' |   string       | No |          


#### Request example
```php
#putObjectACL
try {
    $result = $cosClient->PutObjectAcl(array(
        'Bucket' => 'testbucket-1252448703',
        'Key' => '111.txt',
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/327874225:uin/327874225',
                    'ID' => 'qcs::cam::uin/327874225:uin/327874225',
                    'Type' => 'CanonicalUser',
                ),
                'Permission' => 'FULL_CONTROL',
            ),
            // ... repeated
        ),
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/3210232098:uin/3210232098',
            'ID' => 'qcs::cam::uin/3210232098:uin/3210232098',
        ),));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### getObjectACL
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model getObjectACL(array $args = array());
```

#### Request parameters

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |   string     |  Yes              |        
| Key | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. |    string   |  Yes |        

#### Request example
```php
#getObjectACL
try {
    $result = $cosClient->getObjectAcl(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' => 'testbucket-125000000',
        'Key' => '11'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [Owner] => Array
                (
                    [ID] => qcs::cam::uin/3210232098:uin/3210232098
                    [DisplayName] => qcs::cam::uin/3210232098:uin/3210232098
                )

            [Grants] => Array
                (
                    [0] => Array
                        (
                            [Grantee] => Array
                                (
                                    [ID] => qcs::cam::uin/327874225:uin/327874225
                                    [DisplayName] => qcs::cam::uin/327874225:uin/327874225
                                )

                            [Permission] => FULL_CONTROL
                        )

                )

            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjU5OF8yYzlkMmE=
        )
)
```

### putBucketCors
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model putBucketCors(array $args = array());
```
#### Request parameters

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |    string        |  Yes              |         
| CORSRules |        CORS rules        |    array     | Yes            | 
| AllowedMethods | Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE. |    array   | No           |  
| AllowedOrigins | Allowed access sources. The wildcard "*" is supported. Format: protocol://domain_name[:port], for example, http://www.qq.com |   array   | No           |
| AllowedHeaders | When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. |   array    | No |    
| ExposeHeaders | Sets the custom header information that can be received by the browser from the server end. |    array    | No |   
| MaxAgeSeconds | Sets the validity period of the results obtained by OPTIONS |   string       | No |       
| ID | Sets rule ID                 | string   | No |    
#### Request example

```php
###putBucketCors
try {
    $result = $cosClient->putBucketCors(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' => 'testbucket-125000000',
        // CORSRules is required
        'CORSRules' => array(
            array(
                'AllowedHeaders' => array('*',),
            // AllowedMethods is required
            'AllowedMethods' => array('Put', ),
            // AllowedOrigins is required
            'AllowedOrigins' => array('*', ),
            'ExposeHeaders' => array('*', ),
            'MaxAgeSeconds' => 1,
        ),
        // ... repeated
    ),
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### getBucketCors
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model getBucketCors(array $args = array());
```
#### Request parameters



| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |     string     |  Yes              | 
#### Request example

```php
#getBucketCors
try {
    $result = $cosClient->getBucketCors(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' => 'testbucket-125000000',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Response Example
```php
Array
(
    [data:protected] => Array
        (
            [CORSRules] => Array
                (
                    [0] => Array
                        (
                            [ID] => 1234
                            [AllowedHeaders] => Array
                                (
                                    [0] => *
                                )

                            [AllowedMethods] => Array
                                (
                                    [0] => PUT
                                )

                            [AllowedOrigins] => Array
                                (
                                    [0] => http://www.qq.com
                                )

                        )

                )

            [RequestId] => NWE3YzhkMmRfMTdiMjk0MGFfNTQzZl8xNWUwMGU=
        )
)
```

### deleteBucketCors
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model deleteBucketCors(array $args = array());
```
#### Request parameters

* **params** (Object): Parameter list
  * Bucket - (String): Bucket name   
#### Request example

```php
#deleteBucketCors
try {
    $result = $cosClient->deleteBucketCors(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' => 'testbucket-125000000',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### Copy objects
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model copyObject(array $args = array());
```

#### Request parameters
| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | Bucket name, which is composed of numbers, lowercase letters and "-". | string | Yes |
|  CopySource  | Copies the source object     |  string |  Yes |
|  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. | string |  Yes | 
|  ACL  | Sets file ACL, such as 'private', 'public-read', and 'public-read-write' | string | No | 
|  GrantFullControl  |Grants the specified account the permission to read and write files |  string | No | 
|  GrantRead  | Grants the specified account the permission to read files | string | No |
|  GrantWrite  | Grants the specified account the permission to write files | string | No |
|  StorageClass  | Sets file storage type: STANDARD and STANDARD_IA. Default: STANDARD | String |   No |
|  Expires  | Sets Content-Expires | string| No | 
|  CacheControl  | Cache policy. Sets Cache-Control | string | No |
|  ContentType  | Content type. Sets Content-Type |string | No |  
|  ContentDisposition  | File name. Sets Content-Disposition | string | No |
|  ContentEncoding  | Encoding format. Sets Content-Encoding | string | No |
|  ContentLanguage  | Language type. Sets Content-Language | string | No |
|  ContentLength  | Sets transmission length | string |   No | 
|  ContentMD5  | Sets MD5 of the uploaded file for verification | string | No | 
|  Metadata | User-defined file meta information | array | No |
|  ServerSideEncryption | Server-side encryption method | string |   No |
#### Request example

```php
#copyobject
# API for simple copy
try {
    $result = $cosClient->copyObject(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' => 'testbucket-125000000',
        // CopySource is required
        'CopySource' => 'lewzylu03-1252448703.cos.ap-guangzhou.myqcloud.com/tox.ini',
        // Key is required
        'Key' => 'string',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

#copy
#For files larger than 5 GB, multipart copy is used by default.
try {
    $result = $cosClient->Copy($bucket = 'lewzylu01-1252448703',
        $key = 'string',
        $copysource = 'lewzylu02-1252448703.cos.ap-guangzhou.myqcloud.com/test1G',
        $options = array('VersionId'=>'MTg0NDY3NDI1NTk0MzUwNDQ1OTg'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### putBucketLifecycle
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model putBucketLifecycle(array $args = array());
```
#### Request parameters
| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | Bucket name, which is composed of numbers, lowercase letters and "-". | string | Yes |
|  Rules  | Sets the appropriate rules, including ID, Filter, Status, Expiration, Transition, NoncurrentVersionExpiration, NoncurrentVersionTransition, AbortIncompleteMultipartUpload |  array | Yes |
|  ID     | Sets rule ID                 | string | No | 
|  Filter  | Describes a collection of Objects that are subject to the rules. | array | Yes | 
|  Status  | Sets whether Rule is enabled. Available values: Enabled or Disabled |  string | Yes | 
|  Expiration  | Sets the expiration rule for Object. You can specify the number of days (Days) or a date (Date). | array | No |
|  Transition  | Sets the rule for changing the storage type of Object. You can specify the number of days (Days) or a date (Date). Available value for StorageClass: Standard_IA. | array | No |


#### Request example

```php
#putBucketLifecycle
try {
    $result = $cosClient->putBucketLifecycle(array(
    //The bucket name entered must be in a format of {name}-{appid}
    'Bucket' => 'testbucket-125000000',
    // Rules is required
    'Rules' => array(
        array(
            'Expiration' => array(
                'Days' => 1,
            ),
            'ID' => 'id1',
            'Filter' => array(
                'Prefix' => 'documents/'
            ),
            // Status is required
            'Status' => 'Enabled',
            'Transitions' => array(
                array(
                    'Days' => 200,
                    'StorageClass' => 'Standard_IA')),
            // ... repeated
        ),
    )));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### getBucketLifecycle
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model getBucketLifecycle(array $args = array());
```
#### Request parameters

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |   string   |  Yes              |    
#### Request example

```php
#getBucketLifecycle
try {
    $result = $cosClient->getBucketLifecycle(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' =>'testbucket-125000000',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [Rules] => Array
                (
                    [0] => Array
                        (
                            [ID] => id1
                            [Filter] => Array
                                (
                                    [Prefix] => documents/
                                )

                            [Status] => Enabled
                            [Transition] => Array
                                (
                                    [Days] => 200
                                    [StorageClass] => Standard_IA
                                )

                            [Expiration] => Array
                                (
                                    [Days] => 1000
                                )

                        )

                )

            [RequestId] => NWE3YzhlZjNfY2FhMzNiMGFfNDVkNF8yZDIxODE=
        )
)
```

### deleteBucketLifecycle
#### Method prototype

```php
// Obtain a file list
public Guzzle\Service\Resource\Model deleteBucketLifecycle(array $args = array());
```
#### Request parameters

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |      string    |  Yes              |   
#### Request example

```php
#deleteBucketLifecycle
try {
    $result = $cosClient->deleteBucketLifecycle(array(
        //The bucket name entered must be in a format of {name}-{appid}
        'Bucket' =>'testbucket-125000000',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### Obtain object download URL

Obtain a signed download URL of an object

#### Request example

```php
//Obtain object download URL
//The bucket name entered must be in a format of {name}-{appid}
$bucket =  'testbucket-125000000';
$key = 'hello.txt';
$region = 'cn-south';
$url = "/{$key}";
$request = $cosClient->get($url);
$signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
```
### Use a temporary key

```php
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => 'cn-south',
        'timeout' => ,
        'credentials'=> array(
            'appId' => '',
            'secretId'    => '',
            'secretKey' => '',
            'token' => '')));
```


### Restore an archived file

#### Method prototype

```php
// Restore an archived file
public Guzzle\Service\Resource\Model deleteObject(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:


| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |  string    |  Yes              |  
| Key      | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. |  string   |  Yes |      
| Days      |        Storage duration        |   integer |  Yes          |   
| Tier   |         Restoration type        | string |   No          |    

#### Request example

```php
  try {
    $result = $cosClient->restoreObject(array(
        // Bucket is required
        'Bucket' => 'lewzylu02',
        // Objects is required
        'Key' => '11',
        'Days' => 7,
        'CASJobParameters' => array(
            'Tier' =>'Bulk'
        )
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```


### Enable multiple versions

#### Method prototype

```php
// Enable multiple versions
public Guzzle\Service\Resource\Model putBucketVersioning(array $args = array());
```

#### Request parameters

$args is an associate array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |    string        |  Yes              |     
| Status   |          Multi-version status              |   string       | Yes           |       
#### Request example

```php
#putBucketVersioning
try {
    $result = $cosClient->putBucketVersioning(
    array('Bucket' => 'lewzylu02',
    'Status' => 'Enabled')
    );
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### Obtain bucket version

#### Method prototype

```php
// Obtain bucket version
public Guzzle\Service\Resource\Model getBucketVersioning(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |    string  |  Yes              |        

#### Request example

```php
try {
    $result = $cosClient->getBucketVersioning(
        array('Bucket' => 'lewzylu02',)
    );
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

```

#### Example of returned result
```php
Array
(
    [data:protected] => Array
        (
            [Status] => Enabled
            [RequestId] => NWE3YzhmZTVfNjIyNWI2NF80YzQ3XzJkNjU4NQ==
        )
)
```

### Print the file lists of different versions

#### Method prototype

```php
// Print the file lists of different versions
public Guzzle\Service\Resource\Model listObjectVersions(array $args = array());
```

#### Request parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |      Bucket name    |  string      |  Yes              |          
| Delimiter      |      Delimiter         |   string      |  No          |      
| Marker      |          Marker        |   string       |  No          |      
| MaxKeys      |           Maximum number of objects         |  int        |   No          |       
| Prefix      |            Prefix         |   string       |  No           | 

#### Request example

```php
try {
    $result = $cosClient->listObjectVersions(
        array('Bucket' => 'lewzylu02',
            'Prefix'=>'test1G')
    );
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

```
#### Example of returned result
```php
Array
(
   [data:protected] => Array
        (
            [Name] => lewzylu02-1252448703
            [Prefix] => test1G
            [KeyMarker] => 
            [VersionIdMarker] => 
            [MaxKeys] => 1000
            [IsTruncated] => 
            [Versions] => Array
                (
                    [0] => Array
                        (
                            [Key] => test1G
                            [VersionId] => MTg0NDY3NDI1NTg1ODc4Nzk3NjI
                            [IsLatest] => 1
                            [LastModified] => 2018-01-05T03:07:51.000Z
                            [ETag] => "202cb962ac59075b964b07152d234b70"
                            [Size] => 3
                            [StorageClass] => STANDARD
                            [Owner] => Array
                                (
                                    [UID] => 1252448703
                                )

                        )

                    [1] => Array
                        (
                            [Key] => test1G
                            [VersionId] => MTg0NDY3NDI1NTk0MzI3NDU3NTk
                            [IsLatest] => 
                            [LastModified] => 2017-12-26T08:26:50.000Z
                            [ETag] => "13ddf6552868644926ba606cd287106b-1"
                            [Size] => 5242880
                            [StorageClass] => STANDARD
                            [Owner] => Array
                                (
                                    [UID] => 1252448703
                                )

                        )

                    [2] => Array
                        (
                            [Key] => test1G
                            [VersionId] => MTg0NDY3NDI1NTk0MzI3ODAzODc
                            [IsLatest] => 
                            [LastModified] => 2017-12-26T08:26:16.000Z
                            [ETag] => "3c86b7371340b2174b875fa7bcc0bd9a-1"
                            [Size] => 5242880
                            [StorageClass] => STANDARD
                            [Owner] => Array
                                (
                                    [UID] => 1252448703
                                )

                        )
                )

            [RequestId] => NWE3YzkwMGFfMTliYjk0MGFfMWUwOWRfMmJlZWIx
        )
)
```

