

For a successful operation of COS XML API Python SDK, dict or None is returned. For a failed operation, an exception (CosClientError and CosServiceError) is thrown. An error message is provided for the corresponding exception type. For more information, please see Exception Types at the end of this document.
> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

## Bucket APIs
### Create Bucket

#### Feature description

This API is used to create a Bucket under the specified account. An error is returned if a bucket exists.

#### Method prototype

```
create_bucket(Bucket, **kwargs)
```
#### Request example

```python
response = client.create_bucket(
    Bucket='test01-123456789',
    ACL='private'|'public-read'|'public-read-write',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string'	
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |The name of the bucket to be created, in the format of bucketname-appid |String|Yes |
| ACL |Sets the bucket ACL, such as 'private', 'public-read', and 'public-read-write' |String| No |
| GrantFullControl |Grants the specified account the permission to read and write buckets in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
|GrantRead |Grants the specified account the permission to read buckets in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| GrantWrite|Grants the specified account the permission to write buckets in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |

#### Returned result
The returned value for this method is None.

### Delete Bucket

#### Feature description

This API is used to delete an existing Bucket under the specified account. The Bucket must be empty before it can be deleted.

#### Method prototype

```
delete_bucket(Bucket)
```
#### Request example

```python
response = client.delete_bucket(
    Bucket='test01-123456789'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Name of the Bucket to be deleted, in the format of bucketname-appid |String|Yes |

#### Returned result
The returned value for this method is None.

### Check whether a Bucket exists

#### Feature description

This API is used to check whether a bucket exists or whether you have the access to it.

#### Method prototype

```
head_bucket(Bucket)
```
#### Request example

```python
response = client.head_bucket(
    Bucket='test01-123456789'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |The name of the Bucket to be queried, in the format of bucketname-appid |String|Yes |

#### Returned result
The returned value for this method is None.

### Obtain the Bucket's region information

#### Feature description

This API is used to query the information on the region in which a bucket resides.

#### Method prototype

```
get_bucket_location(Bucket)
```
#### Request example

```python
response = client.get_bucket_location(
    Bucket='test01-123456789'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |The name of the Bucket to be queried, in the format of bucketname-appid |String|Yes |

#### Returned result

The Bucket's region information. Type is dict.
```python
{
    'LocationConstraint': 'ap-beijing-1'|'ap-beijing'|'ap-shanghai'|'ap-guangzhou'|'ap-chengdu'|'ap-chongqing'|'ap-singapore'|'ap-hongkong'|'na-toronto'|'eu-frankfurt'|'ap-mumbai'|'ap-seoul'|'na-siliconvalley'|'na-ashburn'
}
```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
| LocationConstraint |The information on the region in which the Bucket resides |String|

### List all files under the Bucket 

#### Feature description

This API is used to get all Objects under the specified Bucket.

#### Method prototype

```
list_objects(Bucket, Delimiter="", Marker="", MaxKeys=1000, Prefix="", EncodingType="", **kwargs)
```
#### Request example

```python
response = client.list_objects(
    Bucket='test01-123456789',
    Delimiter='string',
    Marker='string',
    MaxKeys=100,
    Prefix='string',
    EncodingType='url'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   | Bucket name, in the format of bucketname-appid | String  | Yes | 
| Delimiter   | Sets a delimiter, for example, as "/" to simulate a folder. It is left empty by default. | String| No |
| Marker   | Marks the starting point of the list of returned objects. Entries are listed using UTF-8 binary order by default. | String  | No | 
| MaxKeys   | The maximum number of returned objects. Default is 1,000. | Int  | No | 
| Prefix   | Filters the keys of objects by matching the objects prefixed with this parameter. It is left empty by default. | String  | No | 
| EncodingType   | Indicates the encoding method of the returned value. The value is not encoded by default. Available value: url | String  | No |

#### Returned result

The meta information of objects. Type is dict:

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

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- |
| MaxKeys   | The maximum number of returned objects. Default is 1,000. | String |
| Prefix   | Filters the keys of objects by matching the objects prefixed with this parameter. It is left empty by default. | String|
| Delimiter   | Sets a delimiter, for example, as "/" to simulate a folder. It is left empty by default. | String|
| Marker   | Marks the starting point of the list of returned objects. Entries are listed using UTF-8 binary order by default. | String  |
| NextMarker| Marks the starting point of the next list of returned if IsTruncated is true. | String  |
| Name   | Bucket name, in the format of bucketname-appid | String  | 
| IsTruncated   | Indicates whether the returned objects are truncated | String|
| EncodingType   | Indicates the encoding method of the returned value. The value is not encoded by default. Available value: url | String  | 
|Contents |The list containing the meta information of all objects, including 'ETag', 'StorageClass', 'Key', 'Owner', 'LastModified', 'Size', etc. |List|
|CommonPrefixes |All keys starting with Prefix and ending with Delimiter are grouped into the same type |List| 

### List all multipart uploads under the Bucket

#### Feature description

This API is used to get all multipart uploads in progress under the specified Bucket.

#### Method prototype

```
list_multipart_uploads(Bucket, Prefix="", Delimiter="", KeyMarker="", UploadIdMarker="", MaxUploads=1000, EncodingType="", **kwargs)
```
#### Request example

```python
response = client.list_multipart_uploads(
    Bucket='test01-123456789',
    Prefix='string',
    Delimiter='string',
    KeyMarker='string',
    UploadIdMarker='string'
    MaxUploads=100,
    EncodingType='url'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   | Bucket name, in the format of bucketname-appid | String  | Yes |
| Prefix   | Filters the keys of multipart uploads by matching the multipart uploads prefixed with this parameter. It is left empty by default. | String  | No | 
| Delimiter   | Sets a delimiter. It is left empty by default. | String| No |
| KeyMarker   | Marks the starting point of a multipart upload task. It is used with UploadIdMarker. | String  | No |
| UploadIdMarker   | Marks the starting point of a multipart upload task. It is used with KeyMarker. If KeyMarker is not specified, UploadIdMarker will be ignored. | String  | No |
| MaxUploads   | The maximum number of returned multipart uploads. Default is 1,000. | Int  | No | 
| EncodingType   | Indicates the encoding method of the returned value. The value is not encoded by default. Available value: url | String  | No |

#### Returned result

The information of a multipart upload task. Type is dict:

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

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- |
| Bucket   | Bucket name, in the format of bucketname-appid | String  | 
| Prefix   | Filters the keys of multipart uploads by matching the multipart uploads prefixed with this parameter. It is left empty by default. | String  |
| Delimiter   | Sets a delimiter. It is left empty by default. | String|
| KeyMarker   | Marks the starting point of a multipart upload task. It is used with UploadIdMarker. | String  |
| UploadIdMarker   | Marks the starting point of uploadid for a multipart upload task. It is used with KeyMarker. If KeyMarker is not specified, UploadIdMarker will be ignored. | String  |
| NextKeyMarker   | Marks the starting point of the next list of keys of multipart uploads | String  |
| NextUploadIdMarker   | Marks the starting point of the next list of uploadid of multipart uploads | String  |
| MaxUploads   | The maximum number of returned multipart uploads. Default is 1,000. | Int  |
| IsTruncated   | Indicates whether the returned multipart uploads are truncated | String|
| EncodingType   | Indicates the encoding method of the returned value. The value is not encoded by default. Available value: url | String  |
|Upload |The list containing information of all multipart uploads, including 'UploadId', 'StorageClass', 'Key', 'Owner', 'Initiator', 'Initiated', etc. |List|
|CommonPrefixes |All keys starting with Prefix and ending with Delimiter are grouped into the same type |List|

### Set Bucket ACL information

#### Feature description

This API is used to set the Bucket ACL information by passing header through ACL, GrantFullControl, GrantRead, GrantWrite or by passing body through AccessControlPolicy. You can only use one of these two methods, otherwise a conflict is returned.

#### Method prototype

```
put_bucket_acl(Bucket, AccessControlPolicy={}, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket | Bucket name, in the format of bucketname-appid |String|Yes |
| ACL |Sets the bucket ACL, such as 'private', 'public-read', and 'public-read-write' |String| No |
| GrantFullControl |Grants the specified account the permission to read and write buckets in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
|GrantRead |Grants the specified account the permission to read buckets in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| GrantWrite|Grants the specified account the permission to write buckets in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| AccessControlPolicy|Grants the specified account the access to buckets. For more information on the format, please see the response for "get bucket acl". |Dict|No |

#### Returned result
The returned value for this method is None.

### Get Bucket ACL information

#### Feature description

This API is used to set the ACL information of the specified Bucket.

#### Method prototype

```
get_bucket_acl(Bucket, **kwargs)
```
#### Request example

```python
response = client.get_bucket_acl(
    Bucket='test01-123456789',
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket name, in the format of bucketname-appid |String|Yes |


#### Returned result

Bucket ACL information. Type is dict.
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

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
| Owner |Information of the Bucket owner, including DisplayName and ID |Dict|
| Grant |Information of a user granted the Bucket permissions, including Grantee and Permission |List|
| Grantee |Information of grantee, including DisplayName, Type, ID and URI |Dict|
| DisplayName |Name of grantee |String|
| Type |Type of grantee: CanonicalUser and Group |String|
| ID |ID of grantee when Type is CanonicalUser |String|
| URI |URI of grantee when Type is Group |String|
| Permission |Bucket permissions of grantee. Available values: FULL_CONTROL (read and write permissions), WRITE (write permission), and READ (read permission) |String|

### Set Bucket cross-origin configuration

#### Feature description
This API is used to set the cross-origin resource configuration for the specified Bucket.

#### Method prototype

```
put_bucket_cors(Bucket, CORSConfiguration={}, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |Bucket name, in the format of bucketname-appid |String| Yes |
| CORSRule |Sets the appropriate cross-origin rules, including ID, MaxAgeSeconds, AllowedOrigin, AllowedMethod, AllowedHeader, and ExposeHeader |List|Yes |
| ID |Sets rule ID |String|No |
| MaxAgeSeconds |Sets the validity period of the results obtained by OPTIONS |Int|No |
| AllowedOrigin |Sets allowed access sources, e.g. `"http://cloud.tencent.com"`. The wildcard "*" is supported. |Dict|Yes |
| AllowedMethod |Sets allowed methods, including GET, PUT, HEAD, POST, and DELETE |Dict|Yes |
| AllowedHeader |Sets the custom HTTP request headers that are allowed to be used by requests. The wildcard "*" is supported. |Dict|No |
| ExposeHeader |Sets the custom header information that can be received by the browser from the server end. |Dict|No |

#### Returned result
The returned value for this method is None.

### Get Bucket cross-origin configuration

#### Feature description
This API is used to get the cross-origin configuration of the specified Bucket.

#### Method prototype

```
get_bucket_cors(Bucket, **kwargs)
```
#### Request example

```python
response = client.get_bucket_cors(
    Bucket='test01-123456789',
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|Bucket name, in the format of bucketname-appid |String| Yes |

#### Returned result

Bucket cross-origin configuration. Type is dict.
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

| Parameter Name | Description | Type |
| -------------- | -------------- |---------- |
 | CORSRule  | Cross-origin rules, including ID, MaxAgeSeconds, AllowedOrigin, AllowedMethod, AllowedHeader, and ExposeHeader |  List | 
 | ID  | Rule ID | String | 
 | MaxAgeSeconds  | The validity period of the results obtained by OPTIONS request | String |
 | AllowedOrigin  | Allowed access sources, e.g. `"http://cloud.tencent.com"`. The wildcard "*" is supported. | Dict | 
 | AllowedMethod  | Allowed methods, including GET, PUT, HEAD, POST, and DELETE | Dict |
 | AllowedHeader  |The custom HTTP request headers that are allowed to be used by requests. The wildcard "*" is supported. |  Dict | 
 | ExposeHeader  | Sets the custom header information that can be received by the browser from the server end. | Dict | 

### Delete Bucket cross-origin configuration

#### Feature description
This API is used to delete the cross-origin configuration of the specified Bucket.

#### Method prototype

```
delete_bucket_cors(Bucket, **kwargs)
```
#### Request example

```python
response = client.delete_bucket_cors(
    Bucket='test01-123456789',
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket | Bucket name, in the format of bucketname-appid |String|Yes

#### Returned result

The returned value for this method is None.

### Set Bucket lifecycle configuration

#### Feature description
This API is used to set the lifecycle configuration of the specified Bucket.

#### Method prototype

```
put_bucket_lifecycle(Bucket, LifecycleConfiguration={}, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  | Bucket name, in the format of bucketname-appid | String | Yes | 
 |  Rule  | Sets the appropriate rules, including ID, Filter, Status, Expiration, Transition, NoncurrentVersionExpiration, NoncurrentVersionTransition, and AbortIncompleteMultipartUpload | List | Yes |
 |  ID  | Sets rule ID | String | No |
 |  Filter  | Describes a collection of Objects that are subject to the rules. To set rules for all objects in the bucket, leave Prefix empty. | Dict | Yes | 
 |  Status  | Sets whether Rule is enabled. Available values: Enabled or Disabled | Dict | Yes | 
 |  Expiration  | Sets the expiration rule for Object. You can specify the number of days (Days) or the specified date (Date). The format of Date must be GMT ISO 8601. You can specify the date using get_date method. | Dict | No |
 |  Transition  | Sets the rule for changing the storage type of Object. You can specify the number of days (Days) or the specified date (Date). The format of Date must be GMT ISO 8601. You can specify the date using get_date method. Available values for StorageClass: Standard_IA and Archive. Multiple rules can be set at a time. | List | No | 
 |  NoncurrentVersionExpiration  | Sets the expiration rule for noncurrent Object versions. You can specify the number of days (NoncurrentDays). |  Dict | No |
 |  NoncurrentVersionTransition  | Sets the rule for changing the storage type of noncurrent Object versions. You can specify the number of days (NoncurrentDays). Available value for StorageClass: Standard_IA. Multiple rules can be set at a time. | List | No | 
 |  AbortIncompleteMultipartUpload  |Indicates the number of days within which the multipart upload must be completed after the upload starts. |  Dict | No | 


#### Returned result

The returned value for this method is None.

### Get Bucket lifecycle configuration

#### Feature description
This API is used to get the lifecycle configuration of the specified Bucket.

#### Method prototype

```
get_bucket_lifecycle(Bucket, **kwargs)
```
#### Request example

```python
response = client.get_bucket_lifecycle(
    Bucket='test01-123456789',
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket | Bucket name, in the format of bucketname-appid |String|Yes |

#### Returned result

Bucket lifecycle configuration. Type is dict.
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

| Parameter Name | Description | Type |
| -------------- | -------------- |---------- | 
 |  Rule  | Rules, including ID, Filter, Status, Expiration, Transition, NoncurrentVersionExpiration, NoncurrentVersionTransition, and AbortIncompleteMultipartUpload | List | 
 |  ID  | Rule ID | String | 
 |  Filter  | Describes a collection of Objects that are subject to the rules. | Dict |
 |  Status  | Indicates whether the rule is enabled. Available values: Enabled and Disabled | Dict |
 |  Expiration  | Expiration rule for Object. You can specify the number of days (Days) or the specified date (Date). |  Dict | 
 |  Transition  | Rule for changing the storage type of Object. You can specify the number of days (Days) or the specified date (Date). Available values for StorageClass: Standard_IA and Archive. | List | 
 |  NoncurrentVersionExpiration  | Expiration rule for noncurrent Object versions. You can specify the number of days (NoncurrentDays). |  Dict |
 |  NoncurrentVersionTransition  | Rule for changing the storage type of noncurrent Object versions. You can specify the number of days (NoncurrentDays). Available value for StorageClass: Standard_IA. | List | 
 |  AbortIncompleteMultipartUpload  | Number of days within which the multipart upload must be completed after the upload starts. | Dict |

### Delete Bucket lifecycle configuration

#### Feature description

This API is used to delete the lifecycle configuration of the specified Bucket.

#### Method prototype

```
delete_bucket_lifecycle(Bucket, **kwargs)
```
#### Request example

```python
response = client.delete_bucket_lifecycle(
    Bucket='test01-123456789',
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket | Bucket name, in the format of bucketname-appid |String|Yes |

#### Returned result

The returned value for this method is None.

## Object APIs

### Simple Upload of File

#### Feature description

This API is used to upload a local file or an input stream to the specified Bucket. It is recommended to upload small files not larger than 20 MB. The file size for a single upload is limited to 5 GB. Use multipart upload to upload larger files.

#### Method prototype

```
put_object(Bucket, Body, Key, **kwargs)
```
#### Request example

```python
response = client.put_object(
    Bucket='test01-123456789',
    Body=b'abc'|file,
    Key='test.txt',
)
```
#### Request example for all parameters
```python
response = client.put_object(
    Bucket='test01-123456789',
    Body=b'abc'|file,
    Key='test.txt',
    ACL='private'|'public-read'|'public-read-write',  # Use this parameter with caution. Otherwise, a limit of 1,000 ACL rules may be reached.
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
#### Parameters


| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  | Bucket name, in the format of bucketname-appid | String |Yes |
 |  Body  | The content of the uploaded file, which can be a file stream or a byte stream |  file/bytes |  Yes |
 |  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String | Yes | 
| ACL | Sets file ACL, such as 'private', 'public-read', and 'public-read-write' |String| No |
| GrantFullControl |Grants the specified account the permission to read and write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
|GrantRead |Grants the specified account the permission to read files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| GrantWrite|Grants the specified account the permission to write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
 |  StorageClass  | Sets file storage type: STANDARD and STANDARD_IA. Default: STANDARD | String |   No |
 |  Expires  | Sets Content-Expires | String| No | 
 |  CacheControl  | Cache policy. Sets Cache-Control | String | No |
 |  ContentType  | Content type. Sets Content-Type |String | No |  
 |  ContentDisposition  | File name. Sets Content-Disposition | String | No |
 |  ContentEncoding  | Encoding format. Sets Content-Encoding | String | No |
 |  ContentLanguage  | Language type. Sets Content-Language | String | No |
 |  ContentLength  | Sets transmission length | String |   No | 
 |  ContentMD5  | Sets MD5 of the uploaded file for verification | String | No | 
 |  Metadata | User-defined file meta information. It must start with x-cos-meta. Otherwise, it will be ignored. | Dict | No |

#### Returned result
Attributes of the uploaded file. Type is dict:

```python
{
    'ETag': 'string',
    'x-cos-expiration': 'string'
}
```


| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- |
|  ETag   | MD5 of the uploaded file | String  |
|  x-cos-expiration   | After the lifecycle is set, the file expiration rule is returned | String  | 
	
### Download files

#### Feature description
This API is used to download the files of the specified Bucket locally.

#### Method prototype

```
 get_object(Bucket, Key, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  | Bucket name, in the format of bucketname-appid | String  | Yes | 
 |  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String  | Yes | 
 |  Range  | Sets the range of the downloaded file, in the format of bytes=first-last. | String  | No | 
 |  IfMatch  | The file is returned if ETag is identical to the specified value |String  | No |  
 |  IfModifiedSince  | The file is returned after it has been modified since the specified time | String  | No |
 |  IfNoneMatch  | The file is returned if ETag is different from the specified value | String  | No | 
 |  IfUnmodifiedSince  | The file is returned if it has been modified at or before the specified time | String  | No |
 |  ResponseCacheControl  | Sets response header Cache-Control | String  | No | 
 |  ResponseContentDisposition  | Sets Content-Disposition in the response header | String  | No | 
 |  ResponseContentEncoding  | Sets Content-Encoding in the response header | String  | No |
 |  ResponseContentLanguage  | Sets Content-Language in the response header | String  | No | 
 |  ResponseContentType  | Sets Content-Type in the response header | String  | No |
 |  ResponseExpires  | Sets Content-Expires in the response header |   String  | No | 
 |  VersionId  | Specifies the version of the downloaded file |  String  | No | 

#### Returned result

Body and meta information of the download file. Type is dict:

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

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
 | Body  | The content of the downloaded file. You can get a file stream by means of get_raw_stream, and download the file content to the specified local file using `get_stream_to_file`. | StreamBody |
 | File meta information | Meta information of the downloaded file, including Etag and x-cos-request-id. The meta information of the configured file is also returned. | String |


### Get pre-signed download URL

#### Feature description
This API is used to get a pre-signed download URL to directly download a file.

#### Method prototype

```
get_presigned_download_url(Bucket, Key, Expired=300)
```
#### Request example

```python
response = client.get_presigned_download_url(
    Bucket='test01-123456789',
    Key='test.txt'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |Bucket name, in the format of bucketname-appid |  String | Yes | 
 | Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String | Yes | 
 |Expired| Signature expiration time (in seconds) | Int| No |

#### Returned result
The returned value for this method is pre-signed URL.

### Delete a file

#### Feature description
This API is used to delete a file in the specified Bucket.

#### Method prototype

```
delete_object(Bucket, Key, **kwargs)
```
#### Request example

```python
response = client.delete_object(
    Bucket='test01-123456789',
    Key='test.txt'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |Bucket name, in the format of bucketname-appid |  String | Yes | 
 | Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String | Yes | 

#### Returned result
The returned value for this method is None.

### Batch deletion of files

#### Feature description
This API is used to delete the files in the specified Bucket in batches.

#### Method prototype

```
delete_objects(Bucket, Delete={}, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket name, in the format of bucketname-appid |  String | Yes | 
 | Delete  | Indicates the method by which the result is returned for the deletion and the target Object | Dict | Yes | 
 | Object  | Provides the information of each target Object to be deleted | List | Yes | 
 | Key     | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String| No |
 | Quiet   |Indicates the method by which the result is returned for the deletion. Available values: 'true' and 'false'. Default is 'false'. If it is set to 'true', only error message for failed deletion is returned. If it is set to 'false', messages indicating successful and failed deletion are returned. | String| No |

#### Returned result
Result of batch deletion of files. Type is dict:
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

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- |
 | Deleted  | The information of the Object that has been deleted |  List |
 | Key     | The path of the Object that has been deleted | String|
 | Error  | The information of the Object that failed to be deleted | List |
 | Key     | The path of the Object that failed to be deleted | String|
 | Code     | The error code for the Object that failed to be deleted | String|
 | Message   | The error message for the Object that failed to be deleted | String|


### Obtain file attributes
#### Feature description
This API is used to obtain the meta information of the specified file.

#### Method prototype

```
head_object(Bucket, Key, **kwargs)
```
#### Request example

```python
response = client.head_object(
    Bucket='test01-123456789',
    Key='test.txt',
    IfModifiedSince='string'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
  | Bucket   | Bucket name, in the format of bucketname-appid | String  | Yes | 
  | Key   | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. |String  | Yes |
  | IfModifiedSince   | The file is returned after it has been modified since the specified time | String  | No | 

#### Returned result

The meta information of the file obtained. Type is dict:

```python
{
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'x-cos-request-id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ=='
}
```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
| File meta information | Meta information of the file obtained, including ETag and x-cos-request-id. The meta information of the configured file is also included. | String|

### Create multipart upload

#### Feature description

This API is used to create a new multipart upload task. UploadId is returned.

#### Method prototype

```
create_multipart_upload(Bucket, Key, **kwargs):
```
#### Request example

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
# Obtain UploadId for use by subsequent APIs
uploadid = response['UploadId']
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket name, in the format of bucketname-appid |  String | Yes |
 | Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String | Yes |
 | StorageClass  | Sets file storage type: STANDARD and STANDARD_IA. Default: STANDARD | String |   No | 
 | Expires  | Sets Content-Expires | String| No |
 | CacheControl  | Cache policy. Sets Cache-Control | String | No | 
 | ContentType  | Content type. Sets Content-Type | String | No | 
 | ContentDisposition  | File name. Sets Content-Disposition | String | No | 
 | ContentEncoding  | Encoding format. Sets Content-Encoding | String | No | 
 | ContentLanguage  | Language type. Sets Content-Language |  String | No |
 | Metadata | User-defined file meta information | Dict | No |
 | ACL | Sets file ACL, such as 'private', 'public-read', and 'public-read-write' |String| No |
| GrantFullControl |Grants the specified account the permission to read and write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
|GrantRead |Grants the specified account the permission to read files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| GrantWrite|Grants the specified account the permission to write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |

#### Returned result

The initialization information of the multipart upload task obtained. Type is dict:

```python
{
    'UploadId': '150219101333cecfd6718d0caea1e2738401f93aa531a4be7a2afee0f8828416f3278e5570',
    'Bucket': 'test01-123456789', 
    'Key': 'multipartfile.txt' 
}

```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- |
|UploadId | Indicates the ID of multipart upload |String|
|Bucket |Bucket name, in the format of bucket-appid |String|
|Key | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. |String|

### Abort multipart upload

#### Feature description
This API is used to abort a multipart upload task, and all uploaded parts are deleted.

#### Method prototype

```
abort_multipart_upload(Bucket, Key, UploadId, **kwargs)
```
#### Request example

```python
response = client.abort_multipart_upload(
    Bucket='test01-123456789',
    Key='multipart.txt',
    UploadId=uploadid
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket name, in the format of bucketname-appid |String| Yes |
|Key |Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. |String| Yes |
|UploadId |Indicates the ID of multipart upload |String| Yes |

#### Returned result
The returned value for this method is None.

### Upload a part
#### Feature description
This API is used to upload a part to the specified UploadId. The size of a part is limited to 5 GB.

#### Method prototype

```
upload_part(Bucket, Key, Body, PartNumber, UploadId, **kwargs)
```
#### Request example

```python
# Note: The maximum number of parts to be uploaded is 10,000.
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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket name, in the format of bucketname-appid | String | Yes |
 | Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String | Yes |
 | Body  | The content of the uploaded part, which can be a local file stream or an input stream | file/bytes | Yes |
 | PartNumber  |Indicates the number of the uploaded part |  Int | Yes |
 | UploadId  | Indicates the ID of multipart upload | String | Yes |
 | ContentLength  | Sets transmission length |  Int |  No |
 | ContentMD5  | Sets MD5 of the uploaded file for verification | String | No |
 
#### Returned result

Attributes of the uploaded part. Type is dict:

```python
{
    'ETag': 'string'
}
```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
| ETag |MD5 of the uploaded part. | String|

### List uploaded parts
#### Feature description
This API is used to list the information of the uploaded parts in the specified UploadId.

#### Method prototype

```
list_parts(Bucket, Key, UploadId, MaxParts=1000, PartNumberMarker=0, EncodingType='', **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket name, in the format of bucketname-appid |String| Yes |
|Key |Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. |String| Yes |
|UploadId |Indicates the ID of multipart upload |String| Yes |
|MaxParts | The maximum number of returned parts. Default is 1,000. |Int| No |
|PartNumberMarker |Indicates that the parts are listed from the one following PartNumberMarker. Default is 0, which means the parts are listed from the first one. |Int| No |
|EncodingType | Indicates the encoding method of the returned value. The value is not encoded by default. Available value: url |String| No |

#### Returned result

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

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
| Bucket   | Bucket name, in the format of bucketname-appid | String  |
|  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String | 
|  UploadId  | Indicates the ID of multipart upload | String | 
| EncodingType   | Indicates the encoding method of the returned value. The value is not encoded by default. Available value: url | String  |
| MaxParts   | The maximum number of returned parts. Default is 1,000. | String  |
| IsTruncated   | Indicates whether the returned parts are truncated | String|
| PartNumberMarker   | Indicates that the parts are listed from the one following PartNumberMarker. Default is 0, which means the parts are listed from the first one. | String  |
| NextPartNumberMarker   | Marks the starting point of the next list of parts | String  |
 |  StorageClass  | File storage type: STANDARD and STANDARD_IA. Default: STANDARD | String |
|  Part |Information of the uploaded part, including ETag, PartNumber, Size, and LastModified | String |
 |  Initiator  | Creator of the multipart upload, including DisplayName and ID | Dict | 
 |  Owner  | Information of the file owner, including DisplayName and ID | Dict | 


### Complete multipart upload

#### Feature description

This API is used to construct all parts in the specified UploadId into a complete file. The size of the resulting file must be larger than 1 MB, otherwise an error is returned.

#### Method prototype

```
complete_multipart_upload(Bucket, Key, UploadId, MultipartUpload={}, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | Bucket name, in the format of bucketname-appid | String | Yes | 
|  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String  | Yes | 
|  UploadId  | Indicates the ID of multipart upload | String  | Yes | 
|  MultipartUpload  |ETag and PartNumber information for all parts. |  Dict | Yes | 

#### Returned result

Information about the constructed file. Type is dict:

```python
{
    'ETag': '"3f866d0050f044750423e0a4104fa8cf-2"', 
    'Bucket': 'test01-123456789', 
    'Location': 'test01-123456789.cn-north.myqcloud.com/multipartfile.txt', 
    'Key': 'multipartfile.txt'
}
```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
 |  ETag  | The unique tag of the resulting object. It is not the MD5 check value for the object content, but is only used to check the uniqueness of the object. To verify the file content, you can check the ETag of each part during the process of upload. |   String | 
 |  Bucket  |Bucket name, in the format of bucketname-appid |  String | 
 |  Location  | URL |  String | 
 |  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String |

### Set Object ACL information

#### Feature description

This API is used to set the file ACL information by passing header through ACL, GrantFullControl, GrantRead, and GrantWrite or by passing body through AccessControlPolicy. You can only choose one method, otherwise a conflict error is returned.

#### Method prototype

```
put_object_acl(Bucket, Key, AccessControlPolicy={}, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   | Bucket name, in the format of bucketname-appid | String  | Yes |
| Key   | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String  | Yes | 
| ACL | Sets file ACL, such as 'private', 'public-read', and 'public-read-write' |String| No | 
| GrantFullControl |Grants the specified account the permission to read and write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
|GrantRead |Grants the specified account the permission to read files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| GrantWrite|Grants the specified account the permission to write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| AccessControlPolicy   | Grants the specified account the access to files. For more information on the format, please see the response for "get object acl". | Dict  | No | 


#### Returned result

The returned value for this method is None.

### Get Object ACL information

#### Feature description
This API is used to get the ACL information of the specified file.

#### Method prototype

```
get_object_acl(Bucket, Key, **kwargs)
```
#### Request example

```python
response = client.get_object_acl(
    Bucket='test01-123456789',
    Key='test.txt'
)
```
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|Bucket name, in the format of bucketname-appid |String| Yes |
|Key |Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. |String|Yes |


#### Returned result

Bucket ACL information. Type is Dict.
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

| Parameter Name | Description | Type |
| -------------- | -------------- |---------- | 
 |  Owner  | Information of the file owner, including DisplayName and ID | Dict | 
 |  Grant  | Information of a user granted the file permissions, including Grantee and Permission | List | 
 |  Grantee  |Information of grantee, including DisplayName, Type, ID and URI |  Dict | 
 |  DisplayName  | Name of grantee | String |
 |  Type  | Type of grantee: CanonicalUser and Group | String |
 |  ID  | ID of grantee when Type is CanonicalUser | String | 
 |  URI  | URI of grantee when Type is Group |  String | 
 |  Permission  | File permissions of grantee. Available values: FULL_CONTROL (read and write permissions), WRITE (write permission), and READ (read permission) | String |

### Copy a file

#### Feature description
This API is used to copy a file from the source path to the destination path, during which the file meta attributes and ACL can be modified. To copy an object, if it is larger than 5 GB and the source and destination objects are in different regions, you must use the API create_multipart_upload() to create a multipart upload, then use upload_part_copy() to copy parts, and use complete_multipart_upload() to complete the multipart upload. If the object to be copied is smaller than or equal to 5 GB, or the source and destination objects are in the same region, you can just call copy_object().

#### Method prototype

```
copy_object(Bucket, Key, CopySource, CopyStatus='Copy', **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  | Bucket name, in the format of bucketname-appid | String| Yes |
 |  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String| Yes | 
 |  CopySource  | Indicates the path of the copied source file, including Appid, Bucket, Key, and Region |  Dict | Yes |
 |  CopyStatus  | Available values: 'Copy' and 'Replaced'. When it is set to 'Copy', ignore the configured user metadata information and copy the file directly. When it is set to 'Replaced', modify the metadata according to the configured meta information. If the destination path is identical to the source path, it must be set to 'Replaced'. | String| Yes |
| ACL | Sets file ACL, such as 'private', 'public-read', and 'public-read-write' |String| No |
| GrantFullControl |Grants the specified account the permission to read and write files in the format of `id=" ",id=" "`. <**eci**> For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
|GrantRead |Grants the specified account the permission to read files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| GrantWrite|Grants the specified account the permission to write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
 |  StorageClass  | Sets file storage type: STANDARD and STANDARD_IA. Default: STANDARD | String|No |
 |  Expires  | Sets Content-Expires | String| No | 
 |  CacheControl  | Cache policy. Sets Cache-Control | String| No | 
 |  ContentType  | Content type. Sets Content-Type | String| No | 
 |  ContentDisposition  | File name. Sets Content-Disposition | String| No |
 |  ContentEncoding  | Encoding format. Sets Content-Encoding | String| No | 
 |  ContentLanguage  | Language type. Sets Content-Language | String| No |
 |  Metadata | User-defined file meta information | Dict | No | 
#### Returned result

Attributes of the uploaded file. Type is dict:

```python
{
    'ETag': 'string',
    'LastModified': 'string',
}
```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
| ETag | MD5 of the copied file |String|
| LastModified |The time when the copied file was last modified |String|

### Copy parts

#### Feature description
This API is used to copy the parts of a file from source path to the destination path.

#### Method prototype

```
upload_part_copy(Bucket, Key, PartNumber, UploadId, CopySource, CopySourceRange='', **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | Bucket name, in the format of bucketname-appid | String| Yes |
|  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String| Yes |
| PartNumber  |Indicates the number of the uploaded part |  Int | Yes |
| UploadId  | Indicates the ID of multipart upload | String | Yes |
|  CopySource  | Indicates the path of the copied source file, including Appid, Bucket, Key, and Region |  Dict | Yes |
|CopySourceRange| Indicates the range of the copied file, in the format of bytes=first-last. If it is not specified, the entire source file is copied by default. |String|No |
|CopySourceIfMatch| The file is copied when the ETag of the source file is identical to the specified value |String| No |
|CopySourceIfModifiedSince| The source file is copied after it has been modified since the specified time |String| No |
|CopySourceIfNoneMatch| The file is copied when the ETag of the source file is different from the specified value |String| No |
|CopySourceIfUnmodifiedSince| The source file is copied after it is not modified since the specified time |String| No |

#### Returned result

Attributes of the copied part. Type is dict:

```python
{
    'ETag': 'string',
    'LastModified': 'string',
}
```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- | 
| ETag |MD5 of the copied part |String|
| LastModified | The time when the copied part was last modified |String|

### Restore an archive file

#### Feature description
This API is used to restore an object that has been archived as "archive" via COS.

#### Method prototype

```
restore_object(Bucket, Key, RestoreRequest={}, **kwargs)
```
#### Request example

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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|Bucket name, in the format of bucketname-appid |String| Yes |
|Key |Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. |String|Yes |
|RestoreRequest| Describes the rule for restoring temporary files | Dict| Yes |
|Days| Describes the validity period of a temporary file | Int|Yes |
|CASJobParameters| Describes the configuration information of restore type | Dict| No |
|Tier| Describes the mode of restoring temporary files. Available values: 'Expedited' (fast), 'Standard' (moderate), and 'Bulk' (slow). | String| No |

#### Returned result
The returned value for this method is None.

## High-level API

### Upload files (resuming upload from breakpoint)

#### Feature description
This API for file upload selects easy upload or multipart upload according to the file length. Easy upload is used for files smaller than or equal to 20 MB. Multipart upload is used for files larger than 20 MB. If the upload of a part is not completed, you can resume the upload from the breakpoint.

#### Method prototype

```
upload_file(Bucket, Key, LocalFilePath, PartSize=1, MAXThread=5, **kwargs)
```
#### Request example

```python
response = client.upload_file(
    Bucket='test01-123456789',
    Key='test.txt',
    LocalFilePath='local.txt'
)
```

#### Request example for all parameters
```python
response = client.upload_file(
    Bucket='test01-123456789',
    Key='test.txt',
    LocalFilePath='local.txt',
    PartSize=1,
    MAXThread=5,
    ACL='private'|'public-read'|'public-read-write', # Please use this parameter with caution. Otherwise, a limit of 1,000 ACL rules may be reached.
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
#### Parameters


| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  | Bucket name, in the format of bucketname-appid | String |Yes |
 |  Key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. | String | Yes | 
|  LocalFilePath  |Name of the path to the local file |  String | Yes |
|  PartSize  | Part size in multipart upload. Default is 1 MB. |  Int |  No |
|  MAXThread  |The maximum number of parts to be uploaded at a time. Default is 5. Parts are uploaded through threads |  Int | No |
| ACL | Sets file ACL, such as 'private', 'public-read', and 'public-read-write' |String| No |
| GrantFullControl |Grants the specified account the permission to read and write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
|GrantRead |Grants the specified account the permission to read files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
| GrantWrite|Grants the specified account the permission to write files in the format of `id=" ",id=" "`. For authorization to a sub-account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`. For authorization to a root account, the format is `id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`. For example, `'id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"'` |String|No |
 |  StorageClass  | Sets file storage type: STANDARD and STANDARD_IA. Default: STANDARD | String |   No |
 |  Expires  | Sets Content-Expires | String| No | 
 |  CacheControl  | Cache policy. Sets Cache-Control | String | No |
 |  ContentType  | Content type. Sets Content-Type |String | No |  
 |  ContentDisposition  | File name. Sets Content-Disposition | String | No |
 |  ContentEncoding  | Encoding format. Sets Content-Encoding | String | No |
 |  ContentLanguage  | Language type. Sets Content-Language | String | No |
 |  ContentLength  | Sets transmission length | String |   No | 
 |  ContentMD5  | Sets MD5 of the uploaded file for verification | String | No | 
 |  Metadata | User-defined file meta information | Dict | No |

#### Returned result
Attributes of the uploaded file. Type is dict:

```python
{
    'ETag': 'string',
    'x-cos-expiration': 'string'
}
```

| Parameter Name | Description | Type | 
| -------------- | -------------- |---------- |
|  ETag   | MD5 of the uploaded file | String  |
|  x-cos-expiration   | After the lifecycle is set, the file expiration rule is returned | String  | 

## API for Obtaining Signature

### Obtain a signature

#### Feature description
This API is used to obtain the signature of the specified operation, which is commonly used for signature distribution.

#### Method prototype

```
get_auth(Method, Bucket, Key, Expired=300, Headers={}, Params={})
```
#### Request example

```python
response = client.get_auth(
    Method='PUT'|'POST'|'GET'|'DELETE'|'HEAD',
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
#### Parameters

| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
 | Method  | Indicates the method of the operation. Available values: 'PUT', 'POST', 'GET', 'DELETE', and 'HEAD'. |  String | Yes | 
 | Bucket  |Bucket name, in the format of bucketname-appid |  String | Yes | 
 | Key  | For bucket operations, enter a root path "/". For object operations, enter a file path. | String | Yes | 
 |Expired| Signature expiration time (in seconds) | Int| No |
 |Headers| Indicates the request header required in the signature | Dict| No |
 |Params | Indicates the request parameters required in the signature | Dict| No |

#### Returned result
The returned value for this method is the signature value of the corresponding operation.

## Exception Types
Exceptions include CosClientError (SDK client error) and CosServiceError (COS server error).

### CosClientError
CosClientError generally refers to a client error caused by the reasons such as timeout. When capturing such an error, you can choose to retry or perform other operations.

### CosServiceError
CosServiceError provides the message returned by the server. For more information on error codes, please see [COS Error Codes](https://cloud.tencent.com/document/product/436/7730).

```python
#except CosServiceError as e
e.get_origin_msg()  # Get original error message in XML format
e.get_digest_msg()  # Get the processed error message in dict format
e.get_status_code()# Get http error code (e.g. 4XX, 5XX)
e.get_error_code()  # Get COS-defined error code
e.get_error_msg()   # Get a detailed description of the COS error code
e.get_trace_id()   # Get the trace_id of the request
e.get_request_id() # Get the request_id of the request
e.get_resource_location()# Get the URL
```

