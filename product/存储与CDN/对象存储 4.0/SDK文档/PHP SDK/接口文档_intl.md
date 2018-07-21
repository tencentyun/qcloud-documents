## Description
> For the meanings and acquisition methods of SecretId, SecretKey, Bucket, etc. appearing in the article, please refer to: [COS Terminology](https://cloud.tencent.com/document/product/436/7751)

### Getting Bucket List
#### Method prototype
```php
Public Guzzle\Service\Resource\Model listBucket(array $args = array())
```

#### Request example

```php
/ / Get the bucket list
$result = $cosClient->listBuckets();
```
#### Return result example
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
// Create bucket
Public Guzzle\Service\Resource\Model createBucket(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required |
|---------|----------------|-----|--------:|
|Bucket | bucket name | string | yes |
|Acl | ACL Permission Control | string | No |

#### Request example

```php
/ / Create a bucket
//bucket's naming convention is {name}-{appid} , the bucket name filled in here must be this format
$result = $cosClient->createBucket(array('Bucket' => 'testbucket-125000000'));
```
#### Return result example
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
// Delete the bucket
Public Guzzle\Service\Resource\Model deleteBucket(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required Field |
| :------: | :------------: | :--------: | :------------------------------: |
|Bucket | bucket name | string | yes |

#### Request example

```php
/ / Delete the bucket
//bucket's naming convention is {name}-{appid} , the bucket name filled in here must be this format
$result = $cosClient->deleteBucket(array('Bucket' => 'testbucket-125000000'));
```
#### Return result example
```php
Array
(
     [data:protected] => Array
         (
             [RequestId] => NWE3YzgzMTZfMTdiMjk0MGFfNTQ2MF8xNjBjZTI=
         )
)
```
### Simple file upload

#### Method prototype

```php
Public Guzzle\Service\Resource\Model putObject(array $args = array())
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required Field |
| -------------- | -------------- |---------- | -------- |
|Bucket | Bucket name, consisting of numbers and lowercase letters and the underscore "-" | string | yes |
| Body | Upload file contents, which can be file stream or byte stream | file/string | yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |
| ACL | Set the ACL of the file, such as 'private, public-read', 'public-read-write' | string |
|GrantFullControl |  Grant READ and WRITE access to the specified account| string | no |
| GrantRead | Grant READ access to the specified account| string | no |
| GrantWrite |  Grant WRITE access to the specified account| string | no |
| StorageClass | Set the storage type of the file, STANDARD, STANDARD_IA, default: STANDARD | String | No |
| Expires | Setting Content-Expires | string| No |
| CacheControl | Cache Policy, Setting Cache-Control | string | No |
| ContentType | Content Type, Settings Content-Type |string | No |
| ContentDisposition | File Name, Settings Content-Disposition | string | No |
| ContentEncoding | Encoding format, set Content-Encoding | string | No |
| ContentLanguage | Language type, setting Content-Language | string | No |
| ContentLength | Set Transfer Length | string | No |
| ContentMD5 | Set the MD5 value of the uploaded file for verification | string | no |
| Metadata | User-defined file meta information | array | no |
| ServerSideEncryption | Server Side Encryption Method | string | No |
#### Request

```php
# Upload files
## putObject(Upload API, max file size: 5G files)
### Uploading a string in memory
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => 'Hello World!'));
    Print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### Uploading a file stream
Try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => fopen($local_path, 'rb')));
    Print_r($result);
} catch (\Exception $e) {
    Echo "$e\n";
}

### Setting header and meta
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
    Print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
#### Response
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
### Multipart Upload

Multipart Upload is to slice a large file into multiple small parts, and upload the file parts concurrently. Total size of the file parts can be 40TB.

Steps for multipart upload:

1. Initialize the multipart upload task and get the uploadid (createMultipartUpload)
2. Upload file parts (uploadPart)
3. Complete multipart upload. (completeMultipartUpload)

It also includes getting uploaded parts (listParts) and aborting upload tasks (abortMultipartUpload).

#### Method prototype

```php
/ / Initialize the block upload
Public Guzzle\Service\Resource\Model createMultipartUpload(array $args = array());

/ / Upload data block
Public Guzzle\Service\Resource\Model uploadPart(array $args = array());
            
/ / Complete the block upload
Public Guzzle\Service\Resource\Model completeMultipartUpload(array $args = array());

// Listed uploaded blocks
Public Guzzle\Service\Resource\Model listParts(array $args = array());

/ / Stop the block upload
Public Guzzle\Service\Resource\Model abortMultipartUpload(array $args = array());
```
### Upload files
#### Request example
```php
## Upload (Advanced upload API, It defaults to use multipart upload and supports up to 50T)
### Uploading a string in memory
try {
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = 'Hello World!');
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### Uploading a file stream
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
Use Upload Object for a file smaller than 5MB. 
Otherwise use Multipart Upload

#### Return result example
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
### Download File

Download the file locally or download it to memory.

#### Method prototype

```php
// download file
Public Guzzle\Service\Resource\Model getObject(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required Field |
| :------: | :------------: | :--------: | :--------------------------------: |
|Bucket | bucket name | string | yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |
| SaveAs | Local part to save the file| string | No |
| VersionId | Object version number | string | no |

#### Request Example

```php
# Download file
## getObject(download file)
### Download to memory

try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key));
    echo($result['Body']);
} catch (\Exception $e) {
    echo "$e\n";
}

### Download to local
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'SaveAs' => $local_path));
} catch (\Exception $e) {
    echo "$e\n";
}

### Specify download range
/*
 * Format of Range filed: 'bytes=a-b'
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

### Delete Files

Delete the object on the COS.

#### Method prototype

```php
// Delete Files
Public Guzzle\Service\Resource\Model deleteObject(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required Field |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |
| VersionId | Object version number | string | no |

#### Request example

```php
// delete the COS object
$result = $cosClient->deleteObject(array(
    //bucket name format: {name}-{appid} 
    'Bucket' => 'testbucket-125000000',
    'Key' => 'hello.txt'));
```
#### Reponse example
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


### Get object properties

Query object properties on COS

#### Method prototype

```php
/ / Get file attributes
Public Guzzle\Service\Resource\Model headObject(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required Field |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |
| VersionId | Object version number | string | no |

#### Response example
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
// Get COS file data
 //bucket name format: {name}-{appid}
$result $cosClient->headObject(array('Bucket' => 'testbucket-125000000', 'Key' => 'hello.txt'));
```

### Query whether the bucket exists

Query whether the bucket exsits COS

#### Method prototype

```php
/ / Get file attributes
public Guzzle\Service\Resource\Model headBucket(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required Field |
| :------: | :------------: | :--: | :--------: |
|Bucket | Object version number | string | yes |



#### Request Example

```php
// Get the COS file attribute
 //bucket name format: {name}-{appid}
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

### Get file list

Query the list of files on COS

#### Method prototype

```php
// Get the file list
public Guzzle\Service\Resource\Model listObjects(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | yes |
| Delimiter | Delimiter | string | No |
| Marker | Tag | string | No |
|MaxKeys | Maximum number of objects | int | No |
| Prefix | Prefix |string | No |

#### Request Example

```php
// Get members in the bucket
 //bucket name format: {name}-{appid}
$result = $cosClient->listObjects(array('Bucket' => 'testbucket-125000000'));
```
#### Response Example
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
// Get file list
public Guzzle\Service\Resource\Model putBucketACL(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | yes |
| ACL | ACL Permission Control | string | no |
| GrantRead | Grant READ access to the specified acccount in the format: id=" ", id=" ". For a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>". For a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>", For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam ::uin/123:uin/456"' | string | no|
| GrantWrite | Grant WRITE access to the specified acccount in the format: id=" ", id=" ". For a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>". For a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>", For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam ::uin/123:uin/456"' | string | no|
|GrantFullControl | Grant READ and WRITE access to the specified acccount in the format: id=" ", id=" ". For a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>". For a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>", For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam ::uin/123:uin/456"' | string | no|     


#### Request Example

```php
#putBucketACL
try {
    $result = $cosClient->PutBucketAcl(array(
 //bucket name format: {name}-{appid}
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
// Get file list
public Guzzle\Service\Resource\Model getBucketACL(array $args = array());
```

#### Request Parameters

| Name   |       Type     | Default | Required |                  Description                  |
| :------: |    :------------: | :--:   | :--------:   | :----------------------------------: |
| Bucket   |     string     |  None    | Yes           |               bucket name               |



#### Request Example
```php
#getBucketACL
try {
    $result = $cosClient->GetBucketAcl(array(
 //bucket name format: {name}-{appid}
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
// Get file list
public Guzzle\Service\Resource\Model putObjectACL(array $args = array());
```

#### Request Parameters
| Parameter Name   | Description   | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
|Bucket | bucket name | string | yes |
 | Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |
| ACL | ACL Permission Control | string | no |
| GrantRead | Grant READ access to the specified acccount in the format: id=" ", id=" ". For a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>". For a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>", For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam ::uin/123:uin/456"' | string | no|
| GrantWrite | Grant WRITE access to the specified acccount in the format: id=" ", id=" ". For a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>". For a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>", For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam ::uin/123:uin/456"' | string | no|
|GrantFullControl | Grant READ and WRITE access to the specified acccount in the format: id=" ", id=" ". For a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>". For a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>", For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam ::uin/123:uin/456"' | string | no|     


#### Request Example
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
// Get file list
public Guzzle\Service\Resource\Model getObjectACL(array $args = array());
```

#### Request Parameters

| Parameter Name   | Description   | Type | Required |  
| :------: | :------------: | :--:   | :--------:   |
| Bucket | bucket name | string | yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |

#### Request Example
```php
#getObjectACL
try {
    $result = $cosClient->getObjectAcl(array(
 //bucket name format: {name}-{appid}
        'Bucket' => 'testbucket-125000000',
        'Key' => '11'));
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

            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjU5OF8yYzlkMmE=
        )
)
```

### putBucketCors
#### Method prototype

```php
// Get file list
public Guzzle\Service\Resource\Model putBucketCors(array $args = array());
```
#### Request Parameters

| Parameter Name | Description | Type | Required |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | yes |
| CORSRules | CORS Rules | array | yes |
|AllowedMethods | Allowed HTTP operations, enumeration values: GET, PUT, HEAD, POST, DELETE | array |
|AllowedOrigins | Allowed access sources, wildcards supported * Format: protocol://domain name[:port] eg: http://www.qq.com | array | no |
|AllowedHeaders | Tell the server when sending OPTIONS requests which custom HTTP request headers can be used for subsequent requests, support wildcards * | array | no |
|ExposeHeaders | Set custom header information from the server that the browser can receive | array | no |
|MaxAgeSeconds | Set the validity period of the OPTIONS request to get results | string | no |
| ID | Configure Rule ID | string | No |
#### Request Example

```php
###putBucketCors
try {
    $result = $cosClient->putBucketCors(array(
 //bucket name format: {name}-{appid}
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

### getBucketCors
#### Method prototype

```php
// Get file list
public Guzzle\Service\Resource\Model getBucketCors(array $args = array());
```
#### Request Parameters



| Parameter Name   | Description   | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |       bucket Name            |     string     | Yes          | 
#### Request Example

```php
#getBucketCors
try {
    $result = $cosClient->getBucketCors(array(
 //bucket name format: {name}-{appid}
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
// Get file list
public Guzzle\Service\Resource\Model deleteBucketCors(array $args = array());
```
#### Request Parameters

* **params** (Object) : List of parameters
 * Bucket - (String) : Bucket name
#### Request Example

```php
#deleteBucketCors
try {
    $result = $cosClient->deleteBucketCors(array(
 //bucket name format: {name}-{appid}
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
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### copyObject
#### Method prototype

```php
// Get file list
public Guzzle\Service\Resource\Model copyObject(array $args = array());
```

#### Request Parameters
| Parameter Name   | Description   | Type | Required |  
| -------------- | -------------- |---------- | ----------- |
|Bucket | Bucket name, consisting of numbers and lowercase letters and the underscore "-" | string | yes |
|CopySource | Copy Source | string | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |
| ACL | Set the ACL of the file, such as 'private, public-read', 'public-read-write' | string |
|GrantFullControl | Grant READ and WRITE access to the specified account| string | no |
| GrantRead |  Grant READ access to the specified account | string | no |
| GrantWrite |  Grant WRITE access to the specified account | string | no |
| StorageClass | Set the storage type of the file, STANDARD, STANDARD_IA, default: STANDARD | String | No |
| Expires | Setting Content-Expires | string| No |
| CacheControl | Cache Policy, Setting Cache-Control | string | No |
| ContentType | Content Type, Settings Content-Type |string | No |
| ContentDisposition | File Name, Settings Content-Disposition | string | No |
| ContentEncoding | Encoding format, set Content-Encoding | string | No |
| ContentLanguage | Language type, setting Content-Language | string | No |
| ContentLength | Set Transfer Length | string | No |
| ContentMD5 | Set the MD5 value of the uploaded file for verification | string | no |
| Metadata | User-defined file meta information | array | no |
| ServerSideEncryption | Server Side Encryption Method | string | No |
#### Request Example

```php
#copyobject
#Copy object
try {
    $result = $cosClient->copyObject(array(
         //bucket name format: {name}-{appid}
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
#use multipart copy for files larger than 5G
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
// Get file list
public Guzzle\Service\Resource\Model putBucketLifecycle(array $args = array());
```
#### Request Parameters
| Parameter Name   | Description   | Type | Required |  
| -------------- | -------------- |---------- | --------- |
|Bucket | Bucket name, consisting of numbers and lowercase letters and the underscore "-" | string | yes |
| Rules | Set the corresponding rules, including ID, Filter, Status, Expiration, Transition, NoncurrentVersionExpiration, NoncurrentVersionTransition, AbortIncompleteMultipartUpload | array |
| ID | Configure Rule ID | string | No |
| Filter | Object collection used to describe the impact of rules | array | yes |
| Status | Sets whether Rule is enabled. The optional value is Enabled or Disabled | string | Yes |
| Expiration | Set Object expiration rules, you can specify the number of days Days or specify the date Date | array |
| Transition | Set Object to convert storage type rules, you can specify the number of days Days or specify the date Date, StorageClass optional Standard_IA| array | No |


#### Request Example

```php
#putBucketLifecycle
try {
    $result = $cosClient->putBucketLifecycle(array(
     //bucket name format: {name}-{appid}
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

### getBucketLifecycle
#### Method prototype

```php
// Get file list
public Guzzle\Service\Resource\Model getBucketLifecycle(array $args = array());
```
#### Request Parameters

| Parameter Name   | Description   | Type | Required |  
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |              bucket名称               |   string   | 是           |    
#### Request Example

```php
#getBucketLifecycle
try {
    $result = $cosClient->getBucketLifecycle(array(
         //bucket name format: {name}-{appid}
        'Bucket' =>'testbucket-125000000',
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
// Get file list
public Guzzle\Service\Resource\Model deleteBucketLifecycle(array $args = array());
```
#### Request Parameters

| Parameter Name   | Description   | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |            bucket 名称               |      string    | 是           |   
#### Request Example

```php
#deleteBucketLifecycle
try {
    $result = $cosClient->deleteBucketLifecycle(array(
         //bucket name format: {name}-{appid}
        'Bucket' =>'testbucket-125000000',
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
            [RequestCharged] => 
            [RequestId] => NWE3YzhjZDdfY2JhMzNiMGFfNjVhOV8yZDJhNjY=
        )
)
```

### getObjectUrl

Get download URL of the object

#### Request Example

```php
//Get download URL of the object
 //bucket name format: {name}-{appid}
$bucket =  'testbucket-125000000';
$key = 'hello.txt';
$region = 'cn-south';
$url = "/{$key}";
$request = $cosClient->get($url);
$signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
```
### Use Temp Key

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


### restoreObject

#### Method prototype

```php
//  Restore archived files
public Guzzle\Service\Resource\Model deleteObject(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:


| Parameter Name | Description | Type | Required |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg | string | yes |
| Days | Save Time | integer | Yes |
|Tier | Recovery Type | string | No |

#### Request Example

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


### putBucketVersioning

#### Method prototype

```php
// Enable versioning
public Guzzle\Service\Resource\Model putBucketVersioning(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | Yes |
| Status | Versioning | string | Yes |
#### Request Example

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

### getBucketVersioning

#### Method prototype

```php
// Get bucket version
public Guzzle\Service\Resource\Model getBucketVersioning(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name   | Description   | Type | Required | 
| :------: | :------------: | :--:   | :--------:   |
| Bucket   |        bucket name               |    string  | Yes           |        

#### Request Example

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

#### Response Example
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

### listObjectVersions

#### Method prototype

```php
// List file lists of all versions
public Guzzle\Service\Resource\Model listObjectVersions(array $args = array());
```

#### Request Parameters

$args is an associative array containing the following fields:

| Parameter Name | Description | Type | Required |
| :------: | :------------: | :--: | :--------: |
|Bucket | bucket name | string | yes |
| Delimiter | Delimiter | string | No |
| Marker | Tag | string | No |
|MaxKeys | Maximum number of objects | int | No |
| Prefix | Prefix | string | No |

#### Request Example

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
#### Response Example
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
