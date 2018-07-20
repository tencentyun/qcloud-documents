

For COS XML API Python SDK operation, a dict or None is returned if it succeeds, and an exception (CosClientError and CosServiceError) is thrown if it fails. The exception class provides relevant error information, as described in the exception type description at the end of the article.
> For the meanings and acquisition methods of names like SecretId, SecretKey, Bucket, etc., please refer to: [COS Terminology](https://cloud.tencent.com/document/product/436/7751)

## Bucket API Description
### Create a Bucket

#### Description

Create a new Bucket under the specified account and return an error when the Bucket already exists.

#### Method prototype

```
Create_bucket(Bucket, **kwargs)
```
#### Request example

```python
Response = client.create_bucket(
     Bucket='test01-123456789',
     ACL='private'|'public-read'|'public-read-write',
     GrantFullControl='string',
     GrantRead='string',
     GrantWrite='string'
)
```

#### Parameter Description

| Parameter Name | Parameter Description | Type | Required |
| -------------- | -------------- |---------- | ----------- |
|Bucket | The name of the Bucket to be created, in the foramt of bucketname-appid |String| Yes |
| ACL | Set Bucket ACLs such as 'private', 'public-read', 'public-read-write' | String| No |
| GrantFullControl | Grant READ and WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|GrantRead | Grant READ access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| GrantWrite| Grant WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|

#### Return Result
The method returns a value of None.

### Remove Bucket

#### Function Description

Delete an existing Bucket under the specified account. When deleting, Bucket must be empty.

#### Method prototype

```
Delete_bucket(Bucket)
```
#### Request example

```python
Response = client.delete_bucket(
     Bucket='test01-123456789'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type | Required |
| -------------- | -------------- |---------- | ----------- |
|Bucket | Name of the bucket to be deleted, in the format of bucketname-appid |String|Yes|

#### Return Result 
The method returns a value of None.

### Query whether Bucket exists

#### Function Description

Query if a bucket exists or has access.

#### Method prototype

```
Head_bucket(Bucket)
```
#### Request example

```python
Response = client.head_bucket(
     Bucket='test01-123456789'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type | Required |
| -------------- | -------------- |---------- | ----------- |
|Bucket | Name of the bucket to be queried, in the format of bucketname-appid |String|Yes|

#### Return result description
The method returns a value of None.

### Get Bucket Location

#### Function Description

Query information about the region in which a bucket is located.

#### Method prototype

```
Get_bucket_location(Bucket)
```
#### Request example

```python
Response = client.get_bucket_location(
     Bucket='test01-123456789'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type | Required |
| -------------- | -------------- |---------- | ----------- |
|Bucket | Name of the Bucket to be queried, in the format of bucketname-appid |String|Yes|

#### Return result description

Bucket territory information, of type dict.
```python
{
     'LocationConstraint': 'ap-beijing-1'|'ap-beijing'|'ap-shanghai'|'ap-guangzhou'|'ap-chengdu'|'ap-chongqing'|'ap-singapore'|'ap -hongkong'|'na-toronto'|'eu-frankfurt'|'ap-mumbai'|'ap-seoul'|'na-siliconvalley'|'na-ashburn'
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
|LocationConstraint |Bucket Location Information|String|

### List all files under Bucket

#### Function Description

Get all the Objects under the specified Bucket.

#### Method prototype

```
List_objects(Bucket, Delimiter="", Marker="", MaxKeys=1000, Prefix="", EncodingType="", **kwargs)
```
#### Request example

```python
Response = client.list_objects(
     Bucket='test01-123456789',
     Delimiter='string',
     Marker='string',
     MaxKeys=100,
     Prefix='string',
     EncodingType='url'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type | Required |
| -------------- | -------------- |---------- | ----------- |
| Bucket | Bucket name in the format of bucketname-appid | String | Yes |
|Delimiter | Default is empty. You can set the separator, such as set "/" to simulate the folder | String| No |
| Marker | By default, entries are listed in UTF-8 binary order, marking the starting position of the list that returns objects | String | No |
| MaxKeys | Maximum number of objects returned, defaults to the maximum 1000 | Int | No |
Prefix | Defaults to null, filters objects by their keys to find the ones match the prefix | String | No |
| EncodingType | Default is not encoded, specifies the encoding of the return value. Value: url | String | No |

#### Return result description

Get the meta information of objects, in the type of dict:

```python
{
    'MaxKeys': '1000', 
    'Prefix': 'string',
    'Delimiter': 'string',
    'Marker': 'string',
    'NextMarker': 'string',
    'Name': 'test04-1252448703',  
    'IsTruncated': 'false'|'true',
    'EncodingType': 'url',
    'Contents':[
        {
            'ETag': '"a5b2e1cfb08d10f6523f7e6fbf3643d5"', 
            'StorageClass': 'STANDARD', 
            'Key': 'zh.cn.txt'
            'Owner': {
                'DisplayName': '1252448703',
                'ID': '1252448703'
            }, 
            'LastModified': '2017-08-08T09:43:35.000Z', 
            'Size': '23'
        },
    ],
    'CommonPrefixes':[
        {
            'Prefix': 'string'
        },
    ],
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
|MaxKeys | The maximum number of objects returned, the default is 1000 | String |
| Prefix | Defaults to null, filters the key of the object, matches the prefix prefix objects | String|
|Delimiter | Default is empty, set the separator, such as set "/" to simulate the folder | String|
| Marker | By default, entries are listed in UTF-8 binary order, marking the starting position of the list that returns objects | String |
|NextMarker| When IsTruncated is true, the starting position of the list that returns the next object is marked | String |
| Name | Bucket name, in the format of bucketname-appid | String |
|IsTruncated | Indicates whether the returned objects are truncated | String|
| EncodingType | Default is not encoded, specifies the encoding of the return value, optional value: url | String | No |
|Contents | List containing all objects meta information, including 'ETag', 'StorageClass', 'Key', 'Owner', 'LastModified', 'Size', etc. |List|
|CommonPrefixes |All Keys starting with Prefix and ending with Delimiter are grouped into the same class|List|

### List all multipart uploads under Bucket

#### Function Description

Get all on-going multipart upload tasks under the specified Bucket.

#### Method prototype

```
List_multipart_uploads(Bucket, Prefix="", Delimiter="", KeyMarker="", UploadIdMarker="", MaxUploads=1000, EncodingType="", **kwargs)
```
#### Request example

```python
Response = client.list_multipart_uploads(
     Bucket='test01-123456789',
     Prefix='string',
     Delimiter='string',
     KeyMarker='string',
     UploadIdMarker='string'
     MaxUploads=100,
     EncodingType='url'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type | Required |
| -------------- | -------------- |---------- | ----------- |
| Bucket | Bucket name, in the format of bucketname-appid | String | Yes |
|Prefix | Default is empty, filter the key uploaded by the block, match the prefix with prefix prefix | String | No|
| Delimiter | Default is empty, set separator | String| No|
|KeyMarker | Used with UploadIdMarker to indicate the starting position of the block upload | String | No |
| UploadIdMarker | Used with KeyMarker to indicate the starting position of the multipart upload. If KeyMarker is not specified, UploadIdMarker will be ignored | String | No |
|MaxUploads | The maximum number of chunked uploads returned, the default is 1000 | Int | No |
| EncodingType | Default is not encoded, specifies the encoding of the return value, optional value: url | String | No |

#### Return result description

Get the information multipart upload (type: dict)

```python
{
    'Bucket': 'test04-1252448703',
    'Prefix': 'string',
    'Delimiter': 'string',
    'KeyMarker': 'string',
    'UploadIdMarker': 'string',
    'NextKeyMarker': 'string',
    'NextUploadIdMarker': 'string',
    'MaxUploads': '1000',
    'IsTruncated': 'true'|'false',,
    'EncodingType': 'url',
    'Upload':[
        {
            'UploadId': 'string',
            'Key': 'string',
            'Initiated': 'string',
            'StorageClass': 'STANDARD',
            'Owner': {
                'DisplayName': 'string',
                'ID': 'string'
            },
            'Initiator': {
                'ID': 'string',
                'DisplayName': 'string'
            }
        },
    ],
    'CommonPrefixes':[
        {
            'Prefix': 'string'
        },
    ],
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | 
|Prefix | Default is empty, filter the key uploaded by the block, match the prefix with prefix prefix | String | No|
| Delimiter | Default is empty, set separator | String| No|
|KeyMarker | Used with UploadIdMarker to indicate the starting position of the block upload | String | No |
| UploadIdMarker | Used with KeyMarker to indicate the starting position of the uploadid that lists the multipart upload. If KeyMarker is not specified, UploadIdMarker will be ignored | String |
|NextKeyMarker | When IsTruncated is true, indicates the starting position of the key for the next multipart upload | String |
| NextUploadIdMarker | When IsTruncated is true, indicates the starting position of the uploadid that lists the next block upload | String |
|MaxUploads | The maximum number of multipart uploads returned, the default is 1000 | Int |
| IsTruncated | Indicates whether the returned multipart upload was truncated | String|
| EncodingType | Default is not encoded, specifies the encoding of the return value, optional value: url | String |
|Upload | Contains all Information of the parts uploaded, including 'UploadId', 'StorageClass', 'Key', 'Owner', 'Initiator', 'Initiated' and other information|List|
|CommonPrefixes |All Keys starting with Prefix and ending with Delimiter are grouped into the same class|List|

### Setting Bucket ACL information

#### Description

Set the ACL information of the Bucket, set the ACL by using the ACL, GrantFullControl, GrantRead, GrantWrite headers, or pass the body through the AccessControlPolicy to set the ACL. You can only select one of the two methods, otherwise the conflict will be returned.

#### Method Prototype

```
put_bucket_acl(Bucket, AccessControlPolicy={}, **kwargs)
```
#### Request Example

```python
response = client.put_bucket_acl(
    Bucket='test01-123456789',
    ACL='private'|'public-read'|'public-read-write',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    AccessControlPolicy={
        'Grant': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'Type': 'CanonicalUser'|'Group',
                    'ID': 'string',
                    'URI': 'string'
                },
                'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
            },
        ],
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        }
    }
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| ACL |Set Bucket ACL. Values: 'private'，'public-read'，'public-read-write' |String|No|
| GrantFullControl | Grant READ and WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|GrantRead | Grant READ access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| GrantWrite| Grant WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|

#### Return result description
Thio method returns a value of None.

### Get Bucket ACL Information

#### Description

Get ACL information of the specified Bucket

#### Method Prototype

```
get_bucket_acl(Bucket, **kwargs)
```
#### Request Example

```python
response = client.get_bucket_acl(
    Bucket='test01-123456789',
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket name, in the format of bucketname-appid |String|Yes|


#### Return result description

Bucket ACL information （type: dict)
```python
{
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },
    'Grant': [
        {
            'Grantee': {
                'DisplayName': 'string',
                'Type': 'CanonicalUser'|'Group',
                'ID': 'string',
                'URI': 'string'
            },
            'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
        },
    ]
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- | 
| Owner | Information of Bucket owner, including DisplayName and ID|Dict|
| Grant |Infomration of Bucket permission grantees including Grantee and Permission|List|
|Grantee | Infomration of permission grantee, including DisplayName, Type, ID, and URI|Dict|
| DisplayName | Name of the grantee | String|
| Type | The type of permission grantee, CanonicalUser or Group|String|
|ID |When the Type is CanonicalUser, the corresponding grantee's ID|String|
| URI |When the Type is Group,  the corresponding grantee's URI|String|
|Permission | Permissions granted to the grantee. Values: FULL_CONTROL, WRITE, READ | String|

### Setting up Bucket cross-origin configuration

#### Description
Set the cross-origin resource configuration for the specified Bucket.
#### Method Prototype

```
put_bucket_cors(Bucket, CORSConfiguration={}, **kwargs)
```
#### Request Example

```python
response = client.put_bucket_cors(
    Bucket='test01-123456789',
    CORSConfiguration={
        'CORSRule': [
            {
                'ID': 'string',
                'MaxAgeSeconds': 100,
                'AllowedOrigin': [
                    'string',
                ],
                'AllowedMethod': [
                    'string',
                ],
                'AllowedHeader': [
                    'string',
                ],
                'ExposeHeader': [
                    'string',
                ]
            }
        ]
    },
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| CORSRule | Set the corresponding cross-origin rules, including ID, MaxAgeSeconds, AllowedOrigin, AllowedMethod, AllowedHeader, ExposeHeader|List| Yes |
|ID | Set Rule ID|String|No|
| MaxAgeSeconds | Set the validity period of the OPTIONS request to get results | Int|No|
| AllowedOrigin | Set the allowed access sources, such as `"http://cloud.tencent.com"`, support wildcards * |Dict|Yes |
| AllowedMethod | Set allowed methods, such as GET, PUT, HEAD, POST, DELETE|Dict| is |
| AllowedHeader | Set which custom HTTP request headers can be used by the request, support wildcards * |Dict|No|
| ExposeHeader |Set custom header information from the server that the browser can receive |Dict|No|

#### Return result description
This method returns a value of None.

### Getting Bucket cross-origin configuration

#### Description
Get the cross-origin configuration of the specified Bucket.

#### Method Prototype

```
get_bucket_cors(Bucket, **kwargs)
```
#### Request Example

```python
response = client.get_bucket_cors(
    Bucket='test01-123456789',
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |

#### Return result description

Bucket cross-origin configuration (type: dict)
```python
{
    'CORSRule': [
        {
            'ID': 'string',
            'MaxAgeSeconds': 100,
            'AllowedOrigin': [
                'string',
            ],
            'AllowedMethod': [
                'string',
            ],
            'AllowedHeader': [
                'string',
            ],
            'ExposeHeader': [
                'string',
            ],
        }
    ]
}
```

| Paramater Name | Paramater Description |Type |
| -------------- | -------------- |---------- |
| CORSRule | Cross-origin rules, including ID, MaxAgeSeconds, AllowedOrigin, AllowedMethod, AllowedHeader, ExposeHeader | List |
| ID | ID of the rule | String |
|MaxAgeSeconds | OPTIONS Request Validity of Results | String |
| AllowedOrigin | Allowed access sources, such as `"http://cloud.tencent.com"`, support wildcards * | Dict |
| AllowedMethod | Allowed methods, such as GET, PUT, HEAD, POST, DELETE | Dict |
| AllowedHeader | Request which custom HTTP request headers can be used, support wildcards * | Dict |
|ExposeHeader | Custom Header Information Received from the Browser by the Browser | Dict | 

### Delete Bucket cross-origin configuration

#### Description
Delete the cross-origin configuration of the specified Bucket.

#### Method Prototype

```
delete_bucket_cors(Bucket, **kwargs)
```
#### Request Example

```python
response = client.delete_bucket_cors(
    Bucket='test01-123456789',
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |

#### Return result description

This method returns a value of None.

### Setting Bucket Lifecycle Configuration

#### Description
Set the lifecycle configuration of the specified Bucket.

#### Method Prototype

```
put_bucket_lifecycle(Bucket, LifecycleConfiguration={}, **kwargs)
```
#### Request Example

```python
from qcloud_cos import get_date
response = client.put_bucket_lifecycle(
    Bucket='test01-123456789',
    LifecycleConfiguration={
        'Rule': [
            {
                'ID': 'string',
                'Filter': {
                    'Prefix': 'string',
                    'Tag': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        }
                    ]
                },
                'Status': 'Enabled'|'Disabled',
                'Expiration': {
                    'Days': 100,
                    'Date': get_date(2018, 4, 20)
                },
                'Transition': [
                    {
                        'Days': 100,
                        'Date': get_date(2018, 4, 20),
                        'StorageClass': 'Standard_IA'|'Archive'
                    },
                ],
                'NoncurrentVersionExpiration': {
                    'NoncurrentDays': 100
                },
                'NoncurrentVersionTransition': [
                    {
                        'NoncurrentDays': 100,
                        'StorageClass': 'Standard_IA'
                    },
                ],
                'AbortIncompleteMultipartUpload': {
                    'DaysAfterInitiation': 100
                }
            }
        ]   
    }
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Rule | Set the corresponding rules, including ID, Filter, Status, Expiration, Transition, NoncurrentVersionExpiration, NoncurrentVersionTransition, AbortIncompleteMultipartUpload | List | Yes |
|ID | Set the ID of the rule | String | No |
|Filter | A collection of Objects that describe the impact of the rule. To set all the objects in the bucket, set the Prefix to be empty ''| Dict | Yes |
| Status | Set whether Rule is enabled. Value: Enabled or Disabled | Dict | Yes |
|Expiration | Set the Object expiration rule, you can specify the number of days or the Date (GMT ISO 8601). It is recommended to use the get_date method to specify the specific date | Dict |
|Transition | Set the rules for how the Object switches storage type. You can specify the number of days or the date (GMT ISO 8601). It is recommended to use the get_date method to specify a specific date. StorageClass can be Standard_IA, Archive. You can set multiple similar rules at the same time | List | No |
| NoncurrentVersionExpiration | Set the expiration rule for non-current version Object. You can specify the number of days NoncurrentDays | Dict | No |
|NoncurrentVersionTransition | Set the rules for how the non-current Object switches storage type.  You can specify the number of days in NoncurrentDays. StorageClass can be Standard_IA, Archive. You can set multiple similar rules at the same time | List | No |
| AbortIncompleteMultipartUpload | Indicates how many days after the start of the multipart upload must be completed | Dict | No |


#### Return result description

This method returns a value of None.

### Getting Bucket Lifecycle Configuration

#### Description
Gets the lifecycle configuration of the specified Bucket.

#### Method Prototype

```
get_bucket_lifecycle(Bucket, **kwargs)
```
#### Request Example

```python
response = client.get_bucket_lifecycle(
    Bucket='test01-123456789',
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |

#### Return result description

Bucket lifecycle configuration (Type: dict)
```python
{
    'Rule': [
        {
            'ID': 'string',
            'Filter': {
                'Prefix': 'string',
                'Tag': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        }
                ]
            },
            'Status': 'string',
            'Expiration': {
                'Days': 100,
                'Date': 'string'
            },
            'Transition': [
                {
                    'Days': 100,
                    'Date': 'string',
                    'StorageClass': 'STANDARD_IA'|'Archive'
                },
            ],
            'NoncurrentVersionExpiration': {
                'NoncurrentDays': 100
            },
            'NoncurrentVersionTransition': [
                {
                    'NoncurrentDays': 100,
                    'StorageClass': 'STANDARD_IA'
                },
            ],
            'AbortIncompleteMultipartUpload': {
                'DaysAfterInitiation': 100
            }
        }
    ]   
}
```

| Paramater Name   | Paramater Description   |Type |
| -------------- | -------------- |---------- | 
| Rule | Corresponding rules, including ID, Filter, Status, Expiration, Transition, NoncurrentVersionExpiration, NoncurrentVersionTransition, AbortIncompleteMultipartUpload | List |
| ID | ID of the rule | String |
| Filter | Must be used to describe the set of Objects affected by the rule | Dict |
| Status | Rule is enabled, the optional value is Enabled or Disabled | Dict |
|Expiration |Object Expiration rule, you can specify the number of days Days or specify the date Date | Dict |
|Transition | Object Convert Storage Type rules, you can specify the number of days Days or specify the date Date, StorageClass optional STANDARD_IA,Archive| List |
| NoncurrentVersionExpiration | Non-current version Object expiration rule, you can specify the number of days NoncurrentDays | Dict |
|NoncurrentVersionTransition | Non-current version Object conversion stores Type rules, you can specify the number of days NoncurrentDays, StorageClass Optional STANDARD_IA| List |
| AbortIncompleteMultipartUpload | How many days after the block upload starts to be uploaded | Dict |

### Delete Bucket Lifecycle Configuration

#### Description

Delete the lifecycle configuration of the specified Bucket.

#### Method Prototype

```
delete_bucket_lifecycle(Bucket, **kwargs)
```
#### Request Example

```python
response = client.delete_bucket_lifecycle(
    Bucket='test01-123456789',
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |

#### Return result description

This method returns a value of None.

## Object API Description

### Simple file upload

#### Description

Support for uploading local files or inputting streams to a specified Bucket. It is recommended to upload small files of no more than 20 MB. The single upload size is limited to 5 GB. For large file uploads, use multipart upload.

#### Method Prototype

```
put_object(Bucket, Body, Key, **kwargs)
```
#### Request Example

```python
response = client.put_object(
    Bucket='test01-123456789',
    Body=b'abc'|file,
    Key='test.txt',
)
```
#### All parameter request example
```python
Response = client.put_object(
     Bucket='test01-123456789',
     Body=b'abc'|file,
     Key='test.txt',
     ACL='private'|'public-read'|'public-read-write'
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    StorageClass='STANDARD'|'STANDARD_IA',
    Expires='string',
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    ContentLength='123',
    ContentMD5='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
```
#### Parameter Description


| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Body | Upload file contents, which can be file stream or byte stream | file/bytes | yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
| ACL | Set file ACL, such as 'private', 'public-read', 'public-read-write' | String| No |
| GrantFullControl | Grant READ and WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|GrantRead | Grant READ access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| GrantWrite| Grant WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| StorageClass | Set File Storage Type, STANDARD, STANDARD_IA, Default: STANDARD | String | No |
| Expires | Settings Content-Expires | String| No |
| CacheControl | Cache Policy, Setting Cache-Control | String | No |
| ContentType | Content Type, Set Content-Type | String | No |
| ContentDisposition | File Name, Settings Content-Disposition | String | No |
| ContentEncoding | Encoding format, setting Content-Encoding | String | No |
| ContentLanguage | Language Type, set Content-Language | String | No |
| ContentLength | Set Transfer Length | String | No |
| ContentMD5 | Set the MD5 value of the uploaded file for verification | String | No |
|Metadata | User-defined file meta information, must start with x-cos-meta, otherwise it will be ignored | Dict | No |

#### Return result description
Attribute of the uploaded file (Type: dict)

```python
{
    'ETag': 'string',
    'x-cos-expiration': 'string'
}
```


| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
| ETag | Upload file MD5 value | String |
| x-cos-expiration | Return file expiration rules after setting the lifecycle | String |
	
### Download Files

#### Description
Download the files from the specified Bucket to the local.

#### Method Prototype

```
 get_object(Bucket, Key, **kwargs)
```
#### Request Example

```python
response = client.get_object(
    Bucket='test01-123456789',
    Key='test.txt',
    Range='string',
    IfMatch='string',
    IfModifiedSince='string',
    IfNoneMatch='string',
    IfUnmodifiedSince='string',
    ResponseCacheControl='string',
    ResponseContentDisposition='string',
    ResponseContentEncoding='string',
    ResponseContentLanguage='string',
    ResponseContentType='string',
    ResponseExpires='string',
    VersionId='string'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
| Range | Set the scope of the downloaded file in the format bytes=first-last | String | No |
| IfMatch | Returns when the ETag matches the specified content |String | No |
| IfModifiedSince | Returns when the file is being modified after the specified time | String | No |
| IfNoneMatch | Returns when ETag does not match the specified content. | String | No |
| IfUnmodifiedSince | Returns when the file is modified earlier than or equal to the specified time. | String | No|
| ResponseCacheControl | Set response header Cache-Control | String | No |
| ResponseContentDisposition | Set response header Content-Disposition | String | No |
| ResponseContentEncoding | Set response header Content-Encoding | String | No |
| ResponseContentLanguage | Set the response header Content-Language | String | No |
| ResponseContentType | Set response header Content-Type | String | No |
| ResponseExpires | Set response header Content-Expires | String | No |
| VersionId | Specify the version of the downloaded file | String | No | 

#### Return result description

Body and metadata of the downloaded file (Type: dict)

```python
{
    'Body': StreamBody(),
    'Accept-Ranges': 'bytes',
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'Content-Disposition': 'attachment; filename="filename.jpg"',
    'Content-Range': 'bytes 0-16086/16087',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'x-cos-request-id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ=='
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- | 
| Body | Contents of the downloaded file. You can use `get_raw_stream` method can get a file stream, or use `get_stream_to_file` method to download the file content to the specified local file | StreamBody |
 | File Meta Information | Download meta information of files, including Etag and x-cos-request-id, and also return the set file meta information | String |


### Get a pre-signed download link

#### Description
Get a pre-signed download link for direct download.

#### Method Prototype

```
get_presigned_download_url(Bucket, Key, Expired=300)
```
#### Request Example

```python
response = client.get_presigned_download_url(
    Bucket='test01-123456789',
    Key='test.txt'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes | 
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
  |Expired| Signature expiration time in seconds | Int| No|

#### Return result description
This method returns a pre-signed URL.

### File deletion

#### Description
Delete the corresponding file in the specified Bucket.

#### Method Prototype

```
delete_object(Bucket, Key, **kwargs)
```
#### Request Example

```python
response = client.delete_object(
    Bucket='test01-123456789',
    Key='test.txt'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | 是 | 
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |

#### Return result description
This method returns a value of None.

### Delete Files in Batch

#### Description
Delete files in the specified Bucket in batches.

#### Method Prototype

```
delete_objects(Bucket, Delete={}, **kwargs)
```
#### Request Example

```python
response = client.delete_objects(
    Bucket='test01-123456789',
    Delete={
        'Object': [
            {
                'Key': 'string',
            },
        ],
        'Quiet': 'true'|'false'
    }
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes | 
| Delete | Describe the return result mode and objects to be deleted| Dict | Yes |
| Object | Description of each object to be deleted | List | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg| String|No|
| Quiet | Indicates the method of returning the result of the deletion. The optional value is 'true', 'false', and the default is 'false'. Set to 'true' to return only failed error messages, set to 'false' to return all information for success and failure. |String|No|

#### Return result description
The result of deleting files in batches. Type is dict:
```python
{
    'Deleted': [
        {
            'Key': 'string',
        },
    ],
    'Error': [
        {
            'Key': 'string',
            'Code': 'string',
            'Message': 'string'
        },
    ]
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
| Deleted | Information of deleted objects | List |
| Key | Path of deleted objects|
| Error | Delete failed Object information | List |
| Key | Delete the path of the failed Object | String|
| Code | Delete the error code corresponding to the failed Object | String|
| Message | Delete the error message corresponding to the failed Object | String|


### Get file attributes
#### Description
Get the meta information of the specified file.

#### Method Prototype

```
head_object(Bucket, Key, **kwargs)
```
#### Request Example

```python
response = client.head_object(
    Bucket='test01-123456789',
    Key='test.txt',
    IfModifiedSince='string'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg |String | Yes |
| IfModifiedSince | Returns if the file is modified after the specified time | String | No |

#### Return result description

Get the meta information of the file, Type is dict:

```python
{
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'x-cos-request-id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ=='
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- | 
| File Meta Information | Get the meta information of the file, including information such as Etag and x-cos-request-id, and also the file meta information set | String|

### Create multipart upload

#### Description

Create a new multipart upload task and return the UploadId.

#### Method Prototype

```
create_multipart_upload(Bucket, Key, **kwargs):
```
#### Request Example

```python
response = client.create_multipart_upload(
    Bucket='test01-123456789',
    Key='multipart.txt',
    StorageClass='STANDARD'|'STANDARD_IA',
    Expires='string'
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    },
    ACL='private'|'public-read'|'public-read-write',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string'
)
# 获取UploadId供后续接口使用
uploadid = response['UploadId']
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
| StorageClass | Set File Storage Type, STANDARD, STANDARD_IA, Default: STANDARD | String | No |
| Expires | Settings Content-Expires | String| No |
| CacheControl | Cache Policy, Setting Cache-Control | String | No |
| ContentType | Content Type, Set Content-Type | String | No |
| ContentDisposition | File Name, Settings Content-Disposition | String | No |
| ContentEncoding | Encoding format, setting Content-Encoding | String | No |
| ContentLanguage | Language Type, set Content-Language | String | No |
|Metadata | User-Defined File Meta Information | Dict | No |
| ACL | Set file ACLs such as 'private', 'public-read', 'public-read-write' | String| No |
| GrantFullControl | Grant READ and WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|GrantRead | Grant READ access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| GrantWrite| Grant WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|

#### Return result description

Get the initialization information of the multipart upload. Type is dict:

```python
{
    'UploadId': '150219101333cecfd6718d0caea1e2738401f93aa531a4be7a2afee0f8828416f3278e5570',
    'Bucket': 'test01-123456789', 
    'Key': 'multipartfile.txt' 
}

```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
|UploadId | The ID of the multipart upload task||
|Bucket |Bucket name, in the format of bucket-appid |String|
|Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg|String|

### Abort Multipart Upload

#### Description
Abort a multipart upload task and delete all uploaded parts.

#### Method Prototype

```
abort_multipart_upload(Bucket, Key, UploadId, **kwargs)
```
#### Request Example

```python
response = client.abort_multipart_upload(
    Bucket='test01-123456789',
    Key='multipart.txt',
    UploadId=uploadid
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket | Bucket name, in the format of bucketname-appid | String | Yes |
|Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg|String| yes |
|UploadId |Identifies the ID of the block upload ID|String| Yes |

#### Return result description
This method returns a value of None.

### Upload Parts
#### Description
Upload a part to the specified UploadId, no more than 5 GB in size.

#### Method Prototype

```
upload_part(Bucket, Key, Body, PartNumber, UploadId, **kwargs)
```
#### Request Example

```python
# Up to 10000 parts can be uploaded
response = client.upload_part(
    Bucket='test01-123456789',
    Key='multipart.txt',
    Body=b'abc'|file,
    PartNumber=1,
    UploadId='string',
    ContentLength=123,
    ContentMD5='string'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
| Body | Upload Part content, either for local file stream or input stream | file/bytes | yes |
| PartNumber | Serial number of the uploaded part | Int | Yes |
| UploadId | ID of the multipart upload task | String | Yes |
| ContentLength | Set Transfer Length | Int | No |
| ContentMD5 | Set the MD5 value of the uploaded file for verification | String | No |
 
#### Return result description

Attribute of the uploaded part. Type is dict:

```python
{
    'ETag': 'string'
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- | 
| ETag | MD5 value of the upload part. |String|

### List Upload Parts
#### Description
Lists information about the uploaded parts in the task with the specified UploadId.

#### Method Prototype

```
list_parts(Bucket, Key, UploadId, MaxParts=1000, PartNumberMarker=0, EncodingType='', **kwargs)
```
#### Request Example

```python
response = client.list_parts(
    Bucket='test01-123456789',
    Key='multipart.txt',
    UploadId=uploadid,
    MaxParts=1000,
    PartNumberMarker=100,
    EncodingType='url'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
|Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg|String| yes |
|UploadId |ID of the multipart upload task|String| Yes |
|MaxParts |The maximum number of parts. The default is the maximum 1000|Int| No|
|PartNumberMarker | List parts from the part next to the PartNumberMarker. Defaults to 0 (lists from the first part.|Int| No|
|EncodingType | Default is not encoded, specifies the encoding method of the return value, optional value: url | String | No |

#### Return result description

Information of all uploaded parts. Type is dict:

```python
{
    'Bucket': 'test01-123456789', 
    'Key': 'multipartfile.txt', 
    'UploadId': '1502192444bdb382add546a35b2eeab81e06ed84086ca0bb75ea45ca7fa073fa9cf74ec4f2', 
    'EncodingType': None, 
    'MaxParts': '1000',
    'IsTruncated': 'true',
    'PartNumberMarker': '0', 
    'NextPartNumberMarker': '1000', 
    'StorageClass': 'Standard',
    'Part': [
        {
            'LastModified': '2017-08-08T11:40:48.000Z',
            'PartNumber': '1',
            'ETag': '"8b8378787c0925f42ccb829f6cc2fb97"',
            'Size': '10485760'
        },
    ], 
    'Initiator': {
        'DisplayName': '3333333333', 
        'ID': 'qcs::cam::uin/3333333333:uin/3333333333'
    }, 
    'Owner': {
        'DisplayName': '124564654654',
        'ID': '124564654654'
    }
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- | 
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String |
| UploadId | ID of the upload task| String |
| EncodingType | Default is not encoded, specifies the encoding of the return value, optional value: url | String |
| MaxParts | The maximum number of parts returned, the default is 1000 | String |
| IsTruncated | Indicates whether the returned chunk is truncated | String|
|PartNumberMarker | List parts from the part next to the PartNumberMarker. Defaults to 0 (lists from the first part.|Int| No|
| NextPartNumberMarker | Indicates the starting position of the next time the parts are listed | String |
| StorageClass | File Storage Type, STANDARD, STANDARD_IA, Default: STANDARD | String |
| Part | Upload part information, including ETag, PartNumber, Size, LastModified | String |
| Initiator | The creator of the upload task, including DisplayName and ID | Dict |
| Owner | File owner information, including DisplayName and ID | Dict |


### Complete Multipart Upload

#### Description

Assemble all the parts in the specified upload task as a complete file. The final size of the file must be greater than 1 MB, otherwise an error will be returned.

#### Method Prototype

```
complete_multipart_upload(Bucket, Key, UploadId, MultipartUpload={}, **kwargs)
```
#### Request Example

```python
response = client.complete_multipart_upload(
    Bucket='test01-123456789',
    Key='multipart.txt',
    UploadId=uploadid,
    MultipartUpload={
        'Part': [
            {
                'ETag': 'string',
                'PartNumber': 1
            },
            {
                'ETag': 'string',
                'PartNumber': 2
            },
        ]
    },
)

```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- |----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
| UploadId | ID of the upload task | String | Yes |
| MultipartUpload | ETag and PartNumber information for all parts | Dict | Yes |

#### Return result description

Information about the assembled file. Type is dict:

```python
{
    'ETag': '"3f866d0050f044750423e0a4104fa8cf-2"', 
    'Bucket': 'test01-123456789', 
    'Location': 'test01-123456789.cn-north.myqcloud.com/multipartfile.txt', 
    'Key': 'multipartfile.txt'
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- | 
| ETag | The unique tag value of the merged object, which is not the MD5 checksum of the object's content, and can only be used to check object uniqueness. To verify the contents of the file, you can verify the ETag value of a single part during the upload process. | String |
|Bucket | Bucket name, in the format of bucketname-appid | String | Yes |
 | Location | URL Address | String |
 | Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String |

### Setting Object ACL Information

#### Description

Set the ACL information of the file. You can set the ACL by passing headers via ACL, GrantFullControl, GrantRead, GrantWrite, or by passing body via AccessControlPolicy. You can only select one of the two methods, otherwise the conflict will be returned.

#### Method Prototype

```
put_object_acl(Bucket, Key, AccessControlPolicy={}, **kwargs)
```
#### Request Example

```python
response = client.put_object_acl(
    Bucket='test01-123456789',
    Key='test.txt',
    ACL='private'|'public-read'|'public-read-write',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    AccessControlPolicy={
        'Grant': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'Type': 'CanonicalUser'|'Group',
                    'ID': 'string',
                    'URI': 'string'
                },
                'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
            },
        ],
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        }
    }
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
| ACL | Set file ACLs such as 'private', 'public-read', 'public-read-write' | String| No |
| GrantFullControl | Grant READ and WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|GrantRead | Grant READ access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| GrantWrite| Grant WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|AccessControlPolicy | Grant access to the file to the specified account. For details, see get object acl return result description | Dict | No |


#### Return result description

This method returns a value of None.

### Get Object ACL Information

#### Description
Get the ACL information of the specified file.

#### Method Prototype

```
get_object_acl(Bucket, Key, **kwargs)
```
#### Request Example

```python
response = client.get_object_acl(
    Bucket='test01-123456789',
    Key='test.txt'
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
|Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg|String|Yes |


#### Return result description

Bucket ACL inforamtion. Type is Dict.
```python
{
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },
    'Grant': [
        {
            'Grantee': {
                'DisplayName': 'string',
                'Type': 'CanonicalUser'|'Group',
                'ID': 'string',
                'URI': 'string'
            },
            'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
        },
    ]
}
```

| Paramater Name   | Paramater Description   |Type |
| -------------- | -------------- |---------- | 
| Owner | File owner information, including DisplayName and ID | Dict |
| Grant | Information about file permission grantee, including Grantee and Permission | List |
|Grantee | Information about file permission grantee, including DisplayName, Type, ID, and URI | Dict |
| DisplayName | Name of the rights grantee | String |
| Type | Type of permission grantee, Type is CanonicalUser or Group | String |
| ID | If Type is CanonicalUser, the ID of the corresponding grantee | String |
| URI |If Type is Group, the URI of the corresponding  grantee | String |
|Permission | Permissions granted to the grantee. Available values are FULL_CONTROL, WRITE, READ | String |

### Copy Files

#### Description
Copy a file from the source path to the target path. During the copy process, the file meta attributes and ACLs can be modified. If the object is larger than 5 GB and the source and target objects are not in the same region, please use create_multipart_upload() API to create a multipart upload task. Then use the upload_part_copy() API to copy the parts and use complete_multipart_upload( ) to complete the multipart upload. If the object to be copied is less than or equal to 5GB or only copied within the same region, just call copy_object().

#### Method Prototype

```
copy_object(Bucket, Key, CopySource, CopyStatus='Copy', **kwargs)
```
#### Request Example

```python
response = client.copy_object(
    Bucket='test01-123456789',
    Key='test.txt',
    CopySource={
        'Appid': '1252408340',
        'Bucket': 'test02', 
        'Key': 'test.txt', 
        'Region': 'ap-guangzhou'
    },
    CopyStatus='Copy'|'Replaced',
    ACL='private'|'public-read'|'public-read-write',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    StorageClass='STANDARD'|'STANDARD_IA',
    Expires='string'
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String|
|CopySource | Path to the source file, including Appid, Bucket, Key, Region | Dict | Yes |
|CopyStatus | Values: 'Copy', 'Replaced'. When set to 'Copy', the user metadata information of the ignored setting is copied directly. When set to 'Replaced', the metadata is modified according to the set meta information. When the path is the same as the source path, it must be set to 'Replaced' | String| Yes |
| ACL | Set file ACL, such as 'private', 'public-read', 'public-read-write' | String| No |
| GrantFullControl | Grant READ and WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|GrantRead | Grant READ access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| GrantWrite| Grant WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| StorageClass | Set File Storage Type, STANDARD, STANDARD_IA, Default: STANDARD | String| No |
 | Expires | Settings Content-Expires | String| No |
 |CacheControl | Cache Policy, Setting Cache-Control| String| No |
 | ContentType | Content Type, Set Content-Type | String| No |
| ContentDisposition | File Name, Settings Content-Disposition | String| No |
| ContentEncoding | Encoding format, setting Content-Encoding | String| No |
| ContentLanguage | Language Type, set Content-Language | String| No |
|Metadata | User-Defined File Meta Information | Dict | No |
#### Return result description

The attribute of the uploaded file. Type is dict:

```python
{
    'ETag': 'string',
    'LastModified': 'string',
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
| ETag | MD5 Value of Copy File | String|
| LastModified | Last modified time of copy file | String|

### Copy upload parts

#### Description
Copy the parts of a file from the source path to the target path.

#### Method Prototype

```
upload_part_copy(Bucket, Key, PartNumber, UploadId, CopySource, CopySourceRange='', **kwargs)
```
#### Request Example

```python
response = client.upload_part_copy(
    Bucket='test01-123456789',
    Key='test.txt',
    PartNumber=100,
    UploadId='string',
    CopySource={
        'Appid': '1252408340',
        'Bucket': 'test02', 
        'Key': 'test.txt', 
        'Region': 'ap-guangzhou'
    },
    CopySourceRange='string',
    CopySourceIfMatch='string',
    CopySourceIfModifiedSince='string',
    CopySourceIfNoneMatch='string',
    CopySourceIfUnmodifiedSince='string'
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String|
| PartNumber | Serial number of the uploaded part | Int | Yes |
| UploadId | ID of the upload task| String | Yes |
|CopySource | Path to the source file, including Appid, Bucket, Key, Region | Dict | Yes |
|CopySourceRange| Describes the scope of file to be copied, in the format bytes=first-last. When not specified, copy the entire source file by default |String|No|
|CopySourceIfMatch| The Etag of the source file is copied when it is the same as the given value |String|No|
|CopySourceIfModifiedSince| The source file is modified after a given time to copy |String|No|
|CopySourceIfNoneMatch| The Etag of the source file is not the same as the given value. |String|No|
|CopySourceIfUnmodifiedSince| The source file is copied after a given time without modification. |String|No|

#### Return result description

Attribute of the copied part. Type is dict:

```python
{
    'ETag': 'string',
    'LastModified': 'string',
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
| ETag | Copy Blocked MD5 Value | String|
| LastModified | Last modified time of the copied part | String|

### Restore archive file

#### Description
Recover an object that is archived as an archive type by COS.

#### Method Prototype

```
restore_object(Bucket, Key, RestoreRequest={}, **kwargs)
```
#### Request Example

```python
response = client.restore_object(
    Bucket='test01-123456789',
    Key='test.txt',
    RestoreRequest={
        'Days': 100,
        'CASJobParameters': {
            'Tier': 'Expedited'|'Standard'|'Bulk'
        }

    }
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
|Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg|String|Yes |
|RestoreRequest| Describes the rules for retrieving temporary files | Dict|Yes|
|Days| Describe the expiration time of temporary files | Int|Yes|
|CASJobParameters| Description of configuration information for recovery Type | Dict|No|
|Tier| Describes the mode for retrieving temporary files. The optional values are 'Expedited', 'Standard', 'Bulk', which correspond to fast, standard, and slow modes respectively | String|No|

#### Return result description
This method returns a value of None.

## High-level API Description (recommended)

### File upload (breakpoint resume)

#### Description
The file upload API automatically selects simple upload and multipart upload according to the size of the file. It calls simple upload for files less than or equal to 20MB, and calls Multipart Upload for files larger than 20MB. The unfinished files uploaded by the block are automatically broken. Continue to pass.

#### Method Prototype

```
upload_file(Bucket, Key, LocalFilePath, PartSize=1, MAXThread=5, **kwargs)
```
#### Request Example

```python
response = client.upload_file(
    Bucket='test01-123456789',
    Key='test.txt',
    LocalFilePath='local.txt'
)
```

#### All parameter request example
```python
Response = client.upload_file(
     Bucket='test01-123456789',
     Key='test.txt',
     LocalFilePath='local.txt',
     PartSize=1,
     MAXThread=5,
     ACL='private'|'public-read'|'public-read-write', 
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    StorageClass='STANDARD'|'STANDARD_IA',
    Expires='string',
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    ContentLength='123',
    ContentMD5='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
```
#### Parameter Description


| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket name, in the format of bucketname-appid | String | Yes |
| Key | The object key (Key) is the unique identifier of the object in the bucket. For example, in the object's access domain name ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg `, the object key is doc1/pic1.jpg | String | Yes |
| LocalFilePath | Pathname of local file | String | Yes |
|PartSize | Part size, default is 1MB | Int | No |
|MAXThread | Maximum number of uploading parts. Default is 5 | Int | No |
| ACL | Set file ACLs such as 'private', 'public-read', 'public-read-write' | String| No |
| GrantFullControl | Grant READ and WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
|GrantRead | Grant READ access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| GrantWrite| Grant WRITE access to the specified account. The format is `id=" ", id=" "`. For a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`, for example `'id="qcs::cam::uin/123:uin/456", Id="qcs::cam::uin/123:uin/123"'`|String|No|
| StorageClass | Set File Storage Type, STANDARD, STANDARD_IA, Default: STANDARD | String | No |
 | Expires | Settings Content-Expires | String| No |
| CacheControl | Cache Policy, Setting Cache-Control | String | No |
| ContentType | Content Type, Set Content-Type | String | No |
| ContentDisposition | File Name, Settings Content-Disposition | String | No |
| ContentEncoding | Encoding format, setting Content-Encoding | String | No |
 | ContentLanguage | Language Type, set Content-Language | String | No |
 | ContentLength | Set Transfer Length | String | No |
| ContentMD5 | Set the MD5 value of the uploaded file for verification | String | No |
| Metadata | User-defined file meta information | Dict | No |

#### Return result description
The attribute of the uploaded file. Type is dict:

```python
{
    'ETag': 'string',
    'x-cos-expiration': 'string'
}
```

| Parameter Name | Parameter Description | Type |
| -------------- | -------------- |---------- |
| ETag | Upload file MD5 value | String |
| x-cos-expiration | Return file expiration rules after setting the lifecycle | String |

## Signature Get API Description

### Signature acquisition

#### Description
Get the signature of the specified operation, which is often used for signature distribution on the mobile side.

#### Method Prototype

```
get_auth(Method, Bucket, Key, Expired=300, Headers={}, Params={})
```
#### Request Example

```python
response = client.get_auth(
    Method='GET'|'POST'|'GET'|'DELETE'|'HEAD',
    Bucket='test01-123456789',
    Key='test.txt',
    Expired=300,
    Headers={
        'Content-Length': 'string',
        'Content-MD5': 'string'
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    }
)
```
#### Parameter Description

| Parameter Name | Parameter Description | Type |Required | 
| -------------- | -------------- |---------- | ----------- |
| Method | The method corresponding to the operation, the optional values are 'GET', 'POST', 'GET', 'DELETE', 'HEAD'| String | Yes |
|Bucket | Bucket name, in the format of bucketname-appid | String | Yes |
|Key | For bucket operation, fill in the root path /, For object operation, fills in the path of the file | String | Yes |
|Expired| Signature expiration time in seconds | Int| No|
|Headers| Request headers that need to be signed in | Dict| No|
|Params | Request parameters that need to be signed in | Dict| No|

#### Return result description
The method returns a value that is the signature value of the corresponding operation.

## Exception Type Description
Includes CosClientError and CosServiceError for SDK client errors and COS server errors, respectively.

### CosClientError
CosClientError generally refers to a client error such as timeout, which can be retried or otherwise manipulated after user capture.

### CosServiceError
CosServiceError provides specific information returned by the server. For more information on obtaining error codes, please refer to: [COS Error Code] (https://cloud.tencent.com/document/product/436/7730)

```python
#except CosServiceError as e
E.get_origin_msg() # Get the original error message in the format XML
E.get_digest_msg() # Get the processed error message in the format dict
E.get_status_code() # Get http error code (such as 4XX, 5XX)
E.get_error_code() # Get the error code defined by Cos
E.get_error_msg() # Get a detailed description of the Cos error code
E.get_trace_id() # Get the requested trace_id
E.get_request_id() # Get the requested request_id
E.get_resource_location() # Get the URL address
```
