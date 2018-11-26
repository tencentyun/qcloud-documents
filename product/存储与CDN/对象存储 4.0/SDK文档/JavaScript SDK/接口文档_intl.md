> This article provides a detailed description of the APIs for the JavaScript SDK.

URL to JavaScript SDK github: [tencentyun/cos-js-sdk-v5](https://github.com/tencentyun/cos-js-sdk-v5)

In codes described in the following sections, "COS" indicates the class of SDK, and "cos" the SDK instance.

For more information on the definitions of SecretId, SecretKey, Bucket, Region and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

The "`-`" preceding the parameter name indicates a "sub-parameter".

## Constructor

### new COS({})

When being referenced directly with a script tag, the SDK occupies the global variable name "COS". By using the constructor of this "COS", you can create an SDK instance.

#### Use Case

Create a COS SDK instance:

- Format 1 (recommended): Use the temporary key format:
```js
var cos = new COS({
    // Required
    getAuthorization: function (options, callback) {
        $.get('http://example.com/server/sts.php', {
            bucket: options.Bucket,
            region: options.Region,
        }, function (data) {
            callback({
                TmpSecretId: data.TmpSecretId,
                TmpSecretKey: data.TmpSecretKey,
                XCosSecurityToken: data.XCosSecurityToken,
                ExpiredTime: data.ExpiredTime,
            });
        });
    }
});
```

- Format 2: Request a signature from the backend if it is required for every request from the frontend.
```js
var cos = new COS({
    // Required
    getAuthorization: function (options, callback) {
        $.get('http://example.com/server/auth.php', {
            method: options.Method,
            pathname: '/' + options.Key,
        }, function (Authorization) {
            callback({
                Authorization: Authorization
                // XCosSecurityToken: data.XCosSecurityToken, // If the signature is calculated with the temporary key, XCosSecurityToken is required.
            });
        });
    },
    // Optional
    FileParallelLimit: 3,    // Limits the number of concurrent file uploads
    ChunkParallelLimit: 3,   // Limits the number of concurrent multipart uploads under a single file
    ProgressInterval: 1000,  // Limits the intervals between onProgress callbacks for upload
});
```

- Format 3: A fixed key is used and the signature calculated at the frontend (To protect the key from leakage, we recommend that you use it for debugging only).
```js
var cos = new COS({
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
});
```

#### Parameters of the constructor

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| SecretId | Indicates the user's SecretId | String | No |
| SecretKey | Indicates the user's SecretKey. To protect the key from leakage, we recommend that you use it for debugging at the frontend only. | String | No |
| FileParallelLimit | Indicates the number of concurrent file uploads under one instance, which defaults to 3. | Number | No |
| ChunkParallelLimit | Indicates the number of concurrent multipart uploads under one file, which defaults to 3. | Number | No |
| ChunkSize | Indicates the size of each part for multipart upload, which defaults to 1048576 (1MB) | Number | No |
| ProgressInterval | Indicates the frequency at which onProgress, the callback method for upload progress, is called back, which is in ms and defaults to 1000 | Number | No |
| Protocol | Indicates a custom request protocol. Options include `https:` and `http:`. `http:` is used if the page is identified to be an `http:` one. Otherwise, `https:` is used. | String | No |
| getAthorization | Indicates the callback method for acquiring signature. This parameter is required if no SecretId or SecretKey is available. | Function | No |


#### Details on the getAuthorization callback function (use Format 1)

```js
getAuthorization: function(options, callback) { ... }
```

Callback parameters for getAuthorization:

| Parameter Name | Description | Type |
|--------|----------|------|
| options | Parameter objects required to acquire the temporary key | Function |
| - Bucket | Bucket name. The bucket name entered must be in a format of {name}-{appid}. | String |
| - Region | The region where the Bucket resides. For enumerated values, please see [Bucket Region].(https://cloud.tencent.com/document/product/436/6224) | String |
| callback | Indicates the postback method after the temporary key is acquired | Function |

Callback posts back an object after the temporary key is acquired. Here is a list of the attributes of this object:

| Attribute Name | Parameter Description | Type | Required |
|--------|----------|------|------|
| TmpSecretId | Indicates the tmpSecretId for the acquired temporary key | String | Yes |
| TmpSecretKey | Indicates the tmpSecretKey for the acquired temporary key | String | No |
| XCosSecurityToken | Indicates the sessionToken for the acquired temporary key, which corresponds to the x-cos-security-token field of the header | String | No |
| ExpiredTime | Indicates the expiredTime for the acquired temporary key, which means the timeout length | String | No |


#### Details on the getAuthorization callback function (use Format 2)

```js
getAuthorization: function(options, callback) { ... }
```

Callback parameters for getAuthorization:

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| options | Parameter objects required to acquire the signature | Function |
| - Method | Indicates the method for the current request | Function | No |
| - Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | No |
| - Query | The query parameter object for the current request, in a format of {key: 'val'} | Object | No |
| - Headers | The header parameter object for the current request, in a format of {key: 'val'} | Function | No |
| callback | Indicates the callback after the temporary key is acquired | Function | No |

After the calculation is completed with getAuthorization, callback posts back a signature string or an object:
Posting back the signature string posts back a string value, requesting Authorization, the authentication header credential field to be used.
Here is a list of the attributes of the posted back object:

| Attribute Name | Parameter Description | Type | Required |
|--------|----------|------|------|
| Authorization | Indicates the Authorization information for the acquired temporary key | String | Yes |
| XCosSecurityToken | Indicates the sessionToken for the acquired temporary key, which corresponds to the x-cos-security-token field of the header | String | No |


#### Acquire authentication credentials

You have three ways to acquire the authentication credentials for your instance by passing in different parameters during instantiation:
1. Pass in SecretId and SecretKey. This allows the signature, every time it is required, to be calculated within the instance.
2. Pass in the getAuthorization callback. This allows the signature, every time it is required, to be calculated and returned to the instance by this callback.
3. Pass in the getSTS callback. This allows the temporary key, every time it is required, to be returned to the instance by this callback and the signature, every time it is required, to be calculated with the temporary key within the instance.


## Static Methods

### COS.getAuthorization

For COS XML API requests, the authentication credential Authorization is required for all operations on private resources to identify whether the current request is valid.

There are two ways to use authentication credentials:
1. Use them in header parameters, with the field name of "authorization".
2. Use them in URL parameters, with the field name of "sign".

The COS.getAuthorization method is used to calculate authentication credentials, i.e., the signature information used to verify the validity of requests.
>**Note**:
>We recommend that you use this method for debugging at the frontend only. Calculating the signature at the frontend is not recommended for launching projects, because this may cause the key to be leaked.

#### Use Case

Acquire the authentication credentials for uploading files:
```js
var Authorization = COS.getAuthorization({
    SecretId: 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    SecretKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    Method: 'get',
    Key: 'a.jpg',
    Expires: 60,
    Query: {},
    Headers: {}
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| SecretId | Indicates the user's SecretId | String | Yes |
| SecretKey | Indicates the user's SecretKey | String | Yes |
| Method | Indicates the operation method, such as get, post, delete, head, and other HTTP methods | String | Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. **If the requested operation is on a file, this parameter indicates the file name and is required**. If the operation is on a bucket, it is left empty. | String | No |
| Expires | Indicates the length signature timeout in seconds, which defaults to 900 seconds | Number | No |
| Query | Indicates the requested query parameter object | Object | No |
| Headers | Indicates the requested header parameter object | Object | No |

#### Returned Result

The calculated authentication credential string "authorization" is returned.

## Tool-based Methods

### Get Auth

The cos.getAuth method is equivalent to the edition of COS.getAuthorization mounted to the instance. The difference is that cos.getAuth does not require passing in SecretId and SecretKey, but uses the method to acquire authentication credentials for the object itself instead.

#### Use Case

```js
var authorization = cos.getAuth({
    Method: 'get',
    Key: '1.jpg'
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Method | Indicates the operation method, such as get, post, delete, head, and other HTTP methods | String | Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. **If the requested operation is on a file, this parameter indicates the file name and is required**. If the operation is on a bucket, it is left empty. | String | No |
| Expires | Indicates the length signature timeout in seconds, which defaults to 900 seconds | Number | No |
| Query | Indicates the requested query parameter object | Object | No |
| Headers | Indicates the requested header parameter object | Object | No |

#### Returned Result

The calculated authentication credential string "authorization" is returned.




### Get Object Url

#### Use Case

// Acquire an unsigned object URL
```js
var url = cos.getObjectUrl({
    Key: '1.jpg',
    Sign: false
});
```

// Acquire a signed object URL
```js
cos.getObjectUrl({
    Key: '1.jpg',
    Sign: true
}, function (err, data) {
    console.log(err || data.Url);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. **If the requested operation is on a file, this parameter indicates the file name and is required**. If the operation is on a bucket, it is left empty. | String | Yes |
| Sign | Whether to return a signed URL | Boolean | No |
| Method | Indicates the operation method, such as get, post, delete, head, and other HTTP methods, which defaults to "get". | String | No |
| Query | Indicates the query parameter object involved in signature calculation | Object | No |
| Headers | Indicates the header parameter object involved in signature calculation | Object | No |

#### Returned Result

A string is returned in either of the two ways:
1. If signature calculation can be performed synchronously, (for example, SecretId and SecretKey are passed in during instantiation), a signed URL is returned by default.
2. Otherwise, an unsigned URL is returned.

#### Callback Function Description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - Url | Indicates the calculated URL | String |


## Bucket Operations


### Head Bucket

The Head Bucket request is used to determine whether the Bucket and the permission to access the Bucket exist. The same permission applies to Head and Read. HTTP status code 200 will be returned if the Bucket exists, 403 if there is no permission, and 404 if the Bucket does not exist.

#### Use Case

```js
cos.headBucket({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',     /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |

#### Callback Function Description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number |
| - headers | Indicates the header information returned for a request | Object |
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number |
| - headers | Indicates the header information returned for a request | Object |


### Get Bucket

Get Bucket request is identical to List Object request. It is used to list partial or all of the Objects under the Bucket. The caller of this API requires Read permission for the Bucket.

#### Use Case

List all the files under the "a" directory
```js
cos.getBucket({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',     /* Required */
    Prefix: 'a/',           /* Not required */
}, function(err, data) {
    console.log(err || data);
});
```

List files under the "a" directory, without deep traversal
```js
cos.getBucket({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou'     /* Required */
    Prefix: 'a/',              /* Not required*/
    Delimiter: '/',            /* Not required*/
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Prefix | Indicates the prefix match, which is used to specify the prefix address of the returned file | String | No |
| Delimiter |Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path. | String | No |
| Marker |Entries are listed using UTF-8 binary order by default, starting from the marker | String | No |
| MaxKeys | Maximum number of entries returned at a time. Default is 1,000 | String | No |
| EncodingType |Indicates the encoding method of the returned value. Available value: url | String |No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - headers | Indicates the header information returned for a request | Object|
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - CommonPrefixes | The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix | Array |
| - - Prefix | Indicates a single Common prefix | String |
| - - Name | Provides the information of Bucket | String |
| - Prefix | Indicates the prefix match, which is used to specify the prefix address of the returned file | String |
| - Marker | Entries are listed using UTF-8 binary order by default, starting from the marker | String |
| - MaxKeys | Maximum number of entries of the result returned for response request each time | String |
| - IsTruncated | Indicates whether the returned entry is truncated. String value: 'true' or 'false' | String |
| - NextMarker | If the returned entry is truncated, NextMarker represents the starting point of the next entry | String |
| - Encoding-Type | Encoding type of Delimiter, which is used for Marker, Prefix, NextMarker, and Key | String |
| - Contents | Metadata information | Array |
| - - ETag | The MD-5 algorithm check value of the file, such as `"22ca88419e2ed4721c23807c678adbe4c08a7880"`. **Be sure to enclose the value in double quotation marks** | String |
| - - Size | Indicates the file size (in bytes) | String |
| - - Key | Object name | String |
| - - LastModified | Indicates the time when Object was last modified, such as 2017-06-23T12:33:27.000Z | String |
| - - Owner | Information of the Bucket owner | Object |
| - ID | AppID of the Bucket | String |
| - StorageClass | The storage level of Object. Enumerated values: STANDARD, STANDARD_IA | String |

### Delete Bucket


Delete Bucket API request is used to delete a Bucket under a specified account. The Bucket must be empty before it can be deleted. The Bucket can be deleted only if its content is removed. The HTTP status code 200 or 204 is returned upon a successful deletion.

#### Use Case

```js
cos.deleteBucket({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou'     /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|


### Get Bucket ACL

This API (Get Bucket ACL) is used to obtain the ACL (access control list) of the Bucket. Only the Bucket owner has the access to this API.

#### Use Case

```js
cos.getBucketAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou'     /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| - Owner | Information of the Bucket owner | Object |
| - - DisplayName | Name of the Bucket owner | String |
| - - ID | ID of the Bucket owner. <br>Format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>; <br>in case of root account, &lt;OwnerUin> and &lt;SubUin> are of the same value | String |
| - Grants | Lists information of authorized users and their permissions | Array |
| - - Permission | Indicates the permissions granted to authorized users. Enumerated values: READ, WRITE, and FULL_CONTROL | String |
| - - Grantee | Indicates information of authorized users. "type" can be RootAccount and Subaccount.<br> In case of RootAccount, ID is specified as root account.<br> In case of Subaccount, ID is specified as sub-account | Object |
| - - - DisplayName | Indicates the username | String |
| - - - ID | Indicates the user ID. <br>In case of root account, format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin> <br>or qcs::cam::anyone:anyone (all users). <br>In case of sub-account, format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> | String |


### Put Bucket ACL

The API Put Bucket ACL is used to write ACL for a Bucket. You can import ACL information either by using Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control", or by using body in XML format.

#### Use Case

## Set Public Read for Buckets

```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    ACL: 'public-read'
}, function(err, data) {
    console.log(err || data);
});
```

Grants a user the permission to read and write buckets.
```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    GrantFullControl: 'id="qcs::cam::uin/1001:uin/1001",id="qcs::cam::uin/1002:uin/1002"' // 1001 represents a uin
}, function(err, data) {
    console.log(err || data);
});
```

Grants a user the permission to read and write buckets.
```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    GrantFullControl: 'id="qcs::cam::uin/1001:uin/1001",id="qcs::cam::uin/1002:uin/1002"' // 1001 represents a uin
}, function(err, data) {
    console.log(err || data);
});
```

Changes Bucket permissions using AccessControlPolicy
```js
cos.putBucketAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    AccessControlPolicy: {
        "Owner": { // AccessControlPolicy must contain "owner".
            "ID": 'qcs::cam::uin/459000000:uin/459000000' // 459000000 represents the QQ number of the Bucket user.
        },
        "Grants": [{
            "Grantee": {
                "ID": "qcs::cam::uin/10002:uin/10002", // 10002 repsents a QQ number
            },
            "Permission": "WRITE"
        }]
    }
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| ACL |Defines the ACL attribute of Object. Valid values: private, public-read, public-read-write. Default value is private. | String | No |
| GrantRead | Grants read permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantWrite | Grants write permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantFullControl | Grants read and write permissions to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| AccessControlPolicy | Provides all configuration information of cross-origin resource sharing | Object | No |
| - Owner | Indicates the object representing the Bucket owner | Object | No |
| - - ID | Indicates the string representing the user ID, for example, qcs::cam::uin/1001:uin/1001, where 1001 represents a uin | Object | No |
| - Grants | Provides all configuration information of cross-origin resource sharing | Object | No |
| - - Permission | Provides all configuration information of cross-origin resource sharing. Options include READ, WRITE, FULL_CONTROL, READ_ACP, and WRITE_ACP. | String | No |
| - - Grantee | Provides all configuration information of cross-origin resource sharing | Array | No |
| - - - ID | Indicates the string representing the user ID, for example, qcs::cam::uin/1001:uin/1001, where 1001 represents a uin | String | No |
| - - - DisplayName | Indicates the string representing the username, which is usually entered as a string matching the user ID. | String | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|


### Get Bucket CORS

This API (Get Bucket CORS) is used by the Bucket owner to configure cross-origin resource sharing on a bucket. (Cross-origin Resource Sharing (CORS) is a W3C standard.) By default, the Bucket owner has the permission of this API and can grant it to others.

#### Use Case

```js
cos.getBucketCors({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - CORSRules | Provides all configuration information of cross-origin resource sharing | Array |
| - - AllowedMethods |Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE. | Array |
| - - AllowedOrigins |Allowed access source. The wildcard "*" is supported. Format: protocol://domain name[:port], for example, `http://www.qq.com` | Array |
| - - AllowedHeaders | When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. | Array |
| - - ExposeHeaders |Sets the custom header information that can be received by the browser from the server end. | Array |
| - - MaxAgeSeconds |Sets the validity period of the results obtained by OPTIONS | String |
| - - ID | Sets rule ID | String |


### Put Bucket CORS

> **Note:**
> 1. To change the `cross-origin access configuration`, make sure the Bucket provides cross-origin support. Go to the `console` to make `cross-origin access configuration`. For more information, please see [Development Environment](#Development Environment).
> 2. Make sure that changing `cross-origin access configuration` does not affect the cross-origin requests under the current origin.

The API Put Bucket CORS is used to set cross-origin resource sharing permission for your Bucket. You can do so by importing configuration files of XML format (file size limit: 64 KB). By default, the Bucket owner has the permission of this API and can grant it to others.

#### Use Case

```js
cos.putBucketCors({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    CORSRules: [{
        "AllowedOrigin": ["*"],
        "AllowedMethod": ["GET", "POST", "PUT", "DELETE", "HEAD"],
        "AllowedHeader": ["*"],
        "ExposeHeader": ["ETag", "x-cos-acl", "x-cos-version-id", "x-cos-delete-marker", "x-cos-server-side-encryption"],
        "MaxAgeSeconds": "5"
    }]
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| CORSRules | Provides all configuration information of cross-origin resource sharing | Array | No |
| - ID | Sets rule ID (optional) | String | No |
| - AllowedMethods | Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE. | Array | Yes |
| - AllowedOrigins | Allowed access source. The wildcard "*" is supported. Format: protocol://domain name[:port], for example, `http://www.qq.com` | Array | Yes |
| - AllowedHeaders | When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. | Array | No |
| - ExposeHeaders | Configures the custom header information that can be received by the browser from the server end. | Array | No |
| - MaxAgeSeconds | Sets the validity period of the results obtained by OPTIONS | String | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|


### Delete Bucket CORS

>**Note:**
>1. Deleting the `cross-origin access configuration` information of the current Bucket may cause all the cross-origin requests to fail. Please proceed with caution.
>2. This method is not recommend for use at the browser end.

Delete Bucket CORS API request is used to delete configuration information of cross-domain access.

#### Use Case

```js
cos.deleteBucketCors({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|


### Get Bucket Location

This API (Get Bucket Location) is used to obtain the information of the region where the Bucket resides. This GET operation returns the region where the Bucket resides via the location sub-resource. Only the Bucket owner is allowed to operate on this API.

#### Use Case

```js
cos.getBucketLocation({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| - LocationConstraint |The region where the Bucket resides. For enumerated values, please see [Bucket Region].(https://cloud.tencent.com/document/product/436/6224) | String |



## Object Operations

### Head Object

The Head Object request is used to obtain the metadata of the corresponding Object. The same permission applies to Head and Get.

#### Use Case

```js
cos.headObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',               /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| IfModifiedSince| If Object is modified after the specified time, the Object meta information is returned, otherwise 304 is returned | String | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200 and 304. If the change has not been modified since the specified time, 304 is returned. | Number|
| - headers | Indicates the header information returned for a request | Object|
| - x-cos-object-type | Indicates whether the Object is appendable for upload. Enumerated values: normal or appendable | String |
| - x-cos-storage-class | The storage level of Object. Enumerated values: STANDARD, STANDARD_IA | String |
| - x-cos-meta- * | User-defined meta information | String |
| - NotModified | Indicates whether the Object is left unmodified since the specified time |Boolean|

### Get Object

Get Object API request is used to download one file (Object) in Bucket of COS to the local computer. This action requires that the user has the read permission for the target Object or the read permission for the target Object has been made available for everyone (public-read).

#### Use Case

```js
cos.getObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
}, function(err, data) {
    console.log(err || data.Body);
});
```

Specify the range to obtain file content
```js
cos.getObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    Range: 'bytes=1-3',        /* Not required */
}, function(err, data) {
    console.log(err || data.Body);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| ResponseContentType | Sets the Content-Type parameter in the response header | String | No |
| ResponseContentLanguage | Sets the Content-Language parameter in the returned header | String | No |
| ResponseExpires | Sets the Content-Expires parameter in the returned header | String | No |
| ResponseCacheControl | Sets the Cache-Control in the returned header | String | No |
| ResponseContentDisposition | Sets the Content-Disposition parameter in the returned header | String | No |
| ResponseContentEncoding | Sets the Content-Encoding parameter in the returned header | String | No |
| Range | The specified range of file download defined in RFC 2616 (in bytes), such as Range: 'bytes=1-3' | String | No |
| IfModifiedSince | If Object is modified after the specified time, the Object meta information is returned, otherwise 304 is returned | String | No |
| IfUnmodifiedSince | The file content is returned if the file has been modified at or before the specified time. If not, 412 (precondition failed) is returned | String | No |
| IfMatch | The file is returned if Etag is the same as the specified value. If not, 412 (precondition failed) is returned | String | No |
| IfNoneMatch | The file is returned if Etag is different from the specified value. Otherwise 304 is returned (not modified) | String | No |
	

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 304, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| - x-cos-object-type | Indicates whether the Object is appendable for upload. Enumerated values: normal or appendable | String |
| - x-cos-storage-class | The storage level of Object. Enumerated values: STANDARD, STANDARD_IA. <br>**Note: If this header is not returned, it means the file is at a STANDARD storage level**. | String |
| - x-cos-meta- * | User-defined metadata | String |
| - NotModified | If IfModifiedSince is used for request and the file is not modified, the value is true. Otherwise, it is false. | Boolean|
| - Body | The returned file conten, which is in string format by default | String |


### Put Object

Put Object request allows you to upload a local file (Object) to the specified Bucket. This action requires that the user has the WRITE permission for the Bucket.

>**Notes:**
>1. Key (file name) should not end with `/`. Otherwise, it will be identified as a folder.
>2. A maximum of 1,000 ACL policies are allowed under a single Bucket. Therefore, set the ACL permission for no more than 999 files under one Bucket.

#### Use Case

```js
cos.putObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    StorageClass: 'STANDARD',
    Body: file, // Upload file objects
    onProgress: function(progressData) {
        console.log(JSON.stringify(progressData));
    }
}, function(err, data) {
    console.log(err || data);
});
```

Upload strings as file content:
```js
cos.putObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    Body: 'hello!',
}, function(err, data) {
    console.log(err || data);
});
```

Upload strings as file content:
```js
cos.putObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    Body: 'hello!',
}, function(err, data) {
    console.log(err || data);
});
```

Create a directory
```js
cos.putObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: 'a/',              /* Required */
    Body: '',
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| CacheControl | Cache-Control, the caching policy defined in RFC 2616 and saved as Object metadata | String | No |
| ContentDisposition | The file name defined in RFC 2616, which will be saved as Object metadata. | String | No |
| ContentEncoding | The encoding format defined in RFC 2616, which is saved as Object metadata | String | No |
| ContentLength | HTTP request content length defined in RFC 2616 (in bytes) | String | No |
| ContentType | The content type (MIME) defined in RFC 2616, which is saved as Object metadata | String | No |
| Expect | If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server | String | No |
| Expires |The expiration time defined in RFC 2616, which is saved as Object metadata | String | No |
| ACL |Defines the ACL attribute of Object. Valid values: private, public-read, public-read-write. Default value is private. | String | No |
| GrantRead | Grants read permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantWrite | Grants write permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantFullControl | Grants read and write permissions to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| StorageClass | Sets the storage level of Object. Enumerated values: STANDARD, STANDARD_IA. Default value: STANDARD | String | No |
| x-cos-meta- * | The header information allowed to be defined by users， which will be returned as Object metadata. The size is limited to 2K. | String | No |
| Body | The content of the file uploaded, which can be `strings`, `File objects` or `Blob objects` | String \ File\ Blob| No |
| onProgress | Callback function for progress. Below is a list of attributes for the progress callback response object (progressData) | Function| No |
| progressData.loaded | Indicates the size of the downloaded portion of the file in bytes | Number| No |
| progressData.total | Indicates the size of the entire file in bytes | Number| No |
| progressData.speed | Indicates the download speed in bytes/s | Number| No |
| progressData.percent | The percentage of file downloaded in decimal, for example, 0.5 for 50% | Number| No |


#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| - ETag |Returns the MD5 algorithm check value for the file. The ETag value can be used to check whether the Object is corrupted in the upload process. <br>**Note: The ETag value must be enclosed in double quotation marks, such as `"09cba091df696af91549de27b8e7d0f6"`** | String |

### Delete Object

Delete Object API request is used to delete one file (Object) in Bucket of COS. This action requires that the user has the WRITE permission for the Bucket.

#### Use Case

```js
cos.deleteObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg'                            /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |


#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 204, 403 and 404. **If the deletion is successful or the file does not exist, 204 or 200 is returned. If the specified Bucket is not found, 404 is returned.**|Number|
| - headers | Indicates the header information returned for a request | Object|

### Options Object

This API (Options Object) is used to implement a pre-request for cross-origin access configuration. This is how it works. Before any cross-origin request is sent, an OPTIONS request, along with the specific source origin, HTTP method and header information, to COS to determine whether a true cross-origin request can be sent. When the CORS configuration does not exist, 403 Forbidden is returned for the request.
**Use the Put Bucket CORS API to enable CORS support for the Bucket.**

#### Use Case

```js
cos.optionsObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    Origin: 'https://www.qq.com',      /* Required */
    AccessControlRequestMethod: 'PUT', /* Required */
    AccessControlRequestHeaders: 'origin,accept,content-type' /* Not required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| Origin | Simulates the origin from which the request for cross-origin access is sent | String | Yes |
| AccessControlRequestMethod |Simulates the HTTP method of the request for cross-origin access | String | Yes |
| AccessControlRequestHeaders | Simulates the origin from which the request for cross-origin access is sent | String | Yes |

#### Callback function description

```js
function(err, data) { ... }
```
| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - headers | Indicates the header information returned for a request | Object|
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - AccessControlAllowOrigin | Simulates the name of the origin from which the request for cross-origin access is sent, separated by commas. If the origin is not allowed, the header will not be returned. For example: \* | String |
| - AccessControlAllowMethods | Simulates the HTTP method of the request for cross-origin access, separated by commas. If the method is not allowed, the header will not be returned. Examples include PUT, GET, POST, DELETE, and HEAD | String |
| - AccessControlAllowHeaders | Simulates the header of the request for cross-origin access, separated by commas. If the simulation of any request header is not allowed, the header will not be returned. Examples include accept, content-type, origin, and authorization | String |
| - AccessControlExposeHeaders | Returned headers supported by cross-origin request, separated by commas. For example: ETag | String |
| - AccessControlMaxAge | Sets the validity period of the results obtained by OPTIONS for example: 3600 | String |
| - OptionsForbidden | Indicates whether an OPTIONS request is forbidden. If the HTTP status code 403 is returned, the value is true | Boolean|


### Get Object ACL

The API Get Object ACL is used to obtain access permission of an Object under a Bucket. Only the Bucket owner is allowed to perform the action.

#### Use Case

```js
cos.getObjectAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| - Owner |Owner of the identified resources | Object|
| - ID | ID of the Object owner. Format: qcs::cam::uin/&lt;OwnerUin>:uin/lt;SubUin>; <br>in case of root account, &lt;OwnerUin> and &lt;SubUin> are of the same value | String |
| - DisplayName | Name of the Object owner | String |
| - Grants | Lists information of authorized users and their permissions | Array |
| - Permission | Indicates the permissions granted to authorized users. Enumerated values: READ, WRITE, and FULL_CONTROL | String |
| - Grantee | Indicates information of authorized users. "type" can be RootAccount and Subaccount. In case of RootAccount, ID is specified as root account. In case of Subaccount, ID is specified as sub-account | Object|
| - DisplayName | Indicates the username | String |
| - ID | Indicates the user ID. In case of root account, format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin> <br>or qcs::cam::anyone:anyone (all users). In case of sub-account, <br>format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin> | String |


### Put Object ACL

This API (Put Object ACL) is used to configure ACL for an Object in a Bucket.
**The number of ACL policies under a single Bucket is limited to 1000. Therefore, under a single Bucket, up to 999 files can be set with ACL permissions.**

#### Use Case

```js
cos.putObjectAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    ACL: 'public-read',        /* Not required */
}, function(err, data) {
    console.log(err || data);
});
```

Grants a user the permission to read and write files.
```js
cos.putObjectAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    GrantFullControl: 'id="qcs::cam::uin/1001:uin/1001",id="qcs::cam::uin/1002:uin/1002"' // 1001 represents a uin
}, function(err, data) {
    console.log(err || data);
});
```

Changes Bucket permissions using AccessControlPolicy
```js
cos.putObjectAcl({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    AccessControlPolicy: {
        "Owner": { // AccessControlPolicy must contain "owner".
            "ID": 'qcs::cam::uin/459000000:uin/459000000' // 459000000 represents the QQ number of the Bucket user.
        },
        "Grants": [{
            "Grantee": {
                "ID": "qcs::cam::uin/10002:uin/10002", // 10002 repsents a QQ number
            },
            "Permission": "WRITE"
        }]
    }
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| ACL |Defines the ACL attribute of Object. Valid values: private, public-read, public-read-write. Default value is private. | String | No |
| GrantRead | Grants read permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantWrite | Grants write permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantFullControl | Grants read and write permissions to the authorized user.<br> Format: id=" ",id=" ". For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 204, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request | Object|


### Delete Multiple Object

This API (Delete Multiple Object) is used to delete files in batches in specific Bucket. A maximum of 1,000 Objects are allowed to be deleted in batches at a time. COS provides two modes for returned results: Verbose and Quiet. Verbose mode returns the result of deletion of each Object, while Quiet mode only returns the information of the Objects with an error.

#### Use Case

Deleting multiple files:
```js
cos.deleteMultipleObject({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Objects: [
        {Key: '1.jpg'},
        {Key: '2.zip'},
    ]
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| Quiet | Boolean. Indicates whether the Quiet mode is enabled. True means Quiet mode is enabled, and False means Verbose mode is enabled. The default is False | Boolean| No |
| Objects | The file list to be deleted | Array | Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 204, 403, and 404. |Number|
| - headers | Indicates the header information returned for a request | Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 204, 403, and 404. |Number|
| - headers | Indicates the header information returned for a request | Object|
| - Deleted|Indicates the information of Object that has been deleted successfully | Array |
| - Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| - Error |Indicates the information of Object that fail to be deleted | Array |
| - Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| - Code | Error code for failed deletion | String |
| - Message | Message indicating the deletion error | String |


### Put Object Copy

This API (Put Object Copy) is used to copy a file from source path to the destination path. The recommended file size is 1 MB-5 GB. For any file above 5 GB, please use multipart upload (Upload - Copy). In the process of copying, file meta-attributes and ACLs can be modified. Users can use this API to move or rename a file, modify file attributes and create a copy.

#### Use Case

```js
cos.putObjectCopy({
    Bucket: 'test-1250000000',                               /* Required */
    Region: 'ap-guangzhou',                                  /* Required */
    Key: '1.jpg',                                            /* Required */
    CopySource: 'test1.cos.ap-guangzhou.myqcloud.com/2.jpg', /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| CopySource | The path of source file URL. You can specify the history version with the versionid sub-resource | String | Yes |
| ACL |Defines the ACL attribute of Object. Valid values: private, public-read, public-read-write. Default value is private. | String | No |
| GrantRead | Grants read permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantWrite | Grants write permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantFullControl | Grants read and write permissions to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| MetadataDirective | Indicates whether to copy metadata. Enumerated values: Copy, Replaced. Default is Copy. If it is marked as Copy, the copying action will be performed directly, with the user metadata in the Header ignored; if it is marked as Replaced, the metadata will be modified based on the Header information.** If the destination path and the source path are the same, that is, the user attempts to modify the metadata, the value must be Replaced** | String | No |
| CopySourceIfModifiedSince | The action is performed if the Object has been modified since the specified time, otherwise error code 412 is returned.** It can be used with CopySourceIfNoneMatch. Using it with other conditions can cause a conflict.** | String | No |
| CopySourceIfUnmodifiedSince | The action is performed if the Object has not been modified since the specified time, otherwise error code 412 is returned.** It can be used with CopySourceIfMatch. Using it with other conditions can cause a conflict.** | String | No |
| CopySourceIfMatch | The action is performed if the Etag of Object is the same as the given one, otherwise error code 412 is returned.** It can be used with CopySourceIfUnmodifiedSince. Using it with other conditions can cause a conflict.** | String | No |
| CopySourceIfNoneMatch | The action is performed if the Etag of Object is different from the given one, otherwise error code 412 is returned.** It can be used with CopySourceIfModifiedSince. Using it with other conditions can cause a conflict.** | String | No |
| StorageClass | Indicates the storage class. Enumerated values: Standard, Standard_IA; the default is Standard | String | No |
| x-cos-meta- * | Indicates other custom file headers | String | No |
| CacheControl | Specifies the instructions that all caching mechanisms must obey throughout the request/response chain | String | No |
| ContentDisposition | Indicates an extension of MIME protocol. The MIME protocol instructs the MIME user agent how to display attached files | String | No |
| ContentEncoding | A pair of header fields used in HTTP to negotiate the "encoding format for text transmission" | String | No |
| ContentType | HTTP request content type defined in RFC 2616 (MIME), for example: `text/plain` | String | No |
| Expect | Indicates the specific server behavior requested | String | No |
| Expires | Response expiration date and time | String | No |
	

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| - ETag| The MD-5 algorithm check value of the file, such as `"22ca88419e2ed4721c23807c678adbe4c08a7880"`. **Be sure to enclose the value in double quotation marks** | String |
| - LastModified| Indicates the time when Object was last modified, such as 2017-06-23T12:33:27.000Z | String |



## Multipart Upload Operations


### Initiate Multipart Upload

This API (Initiate Multipart Upload) is used to initialize multipart upload. After the request is executed successfully, Upload ID is returned for the subsequent Upload Part requests.

#### Use Case

```js
cos.multipartInit({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| CacheControl | Cache-Control, the caching policy defined in RFC 2616 and saved as Object metadata | String | No |
| ContentDisposition | The file name defined in RFC 2616, which will be saved as Object metadata. | String | No |
| ContentEncoding | The encoding format defined in RFC 2616, which is saved as Object metadata | String | No |
| ContentType | The content type (MIME) defined in RFC 2616, which is saved as Object metadata | String | No |
| Expires | The expiration time defined in RFC 2616, which is saved as Object metadata | String | No |
| ACL |Defines the ACL attribute of Object. Valid values: private, public-read, public-read-write. Default value is private. | String | No |
| GrantRead | Grants read permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantWrite | Grants write permission to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| GrantFullControl | Grants read and write permissions to the authorized user. Format: id=" ",id=" ". <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; <br>for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>".<br> For example: 'id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"' | String | No |
| StorageClass | Set the storage level of Object. Enumerated values: STANDARD, STANDARD_IA. Default: STANDARD | String | No |
| x-cos-meta- * | The header information allowed to be defined by users， which will be returned as Object metadata. The size is limited to 2 KB. | String | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| Bucket | The target Bucket for multipart upload | String |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| UploadId | ID used in subsequent uploads | String |


### Upload Part

Upload Part request is used to implement the multipart upload after initialization. The allowed number of parts is limited to 10,000, and the size of part should be between 1 MB and 5 GB.
You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file. Upload Part should be used with partNumber and uploadId. partNumber is the part No. and supports out-of-order upload.
If the uploadId and partNumber are the same, the parts uploaded later will overwrite the parts uploaded earlier. A 404 error "NoSuchUpload" will be returned if the uploadId does not exist.

#### Use Case

```js
cos.multipartUpload({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',       /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| ContentLength | HTTP request content length defined in RFC 2616 (in bytes) | String | Yes |
| PartNumber | Part No. | String | Yes |
| UploadId | Upload task No. | String | Yes |
| Body | The content of the uploaded part, which can be`string`, `File object` or `Blob object` | String \ File \ Blob| Yes |
| Expect | When `Expect: 100-continue` is used, the request content will not be sent until the receipt of response from server | String | No |
| ContentMD5 | Indicates the 128-bit content MD5 check value encoded using Base64, defined in RFC 1864. This header is used to check whether the file content has changed | String | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| - ETag | The MD-5 algorithm check value of the file, such as `"22ca88419e2ed4721c23807c678adbe4c08a7880"`. **Be sure to enclose the value in double quotation marks** | String |


### Complete Multipart Upload

This API (Complete Multipart Upload) is used to complete the entire multipart upload. You must use this API to complete the multipart upload operation of the entire file when you have uploaded all parts using Upload Parts. When using this API, you need to provide the PartNumber and ETag for every part in request Body, to verify the accuracy of parts.
The merging of parts is required and takes several minutes, thus COS returns status code 200 immediately when the merging process begins. During merging, COS may returns blank information periodically to keep the connection active, until the merging process completes, upon which the COS will return the content of the merged parts in Body.
- When this API is called, "400 EntityTooSmall" is returned if the uploaded part is smaller than 1 MB.
- "400 InvalidPart" is returned if the numbers of uploaded parts are discontinuous.
- "400 InvalidPartOrder" is returned if the part information entries in the request Body are not sorted in ascending order according to their numbers.
- "404 NoSuchUpload" is returned if the UploadId does not exist when this API is called.

#### Use Case

```js
cos.multipartComplete({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.zip',                           /* Required */
    UploadId: '1521389146c60e7e198202e4e6670c5c78ea5d1c60ad62f1862f47294ec0fb8c6b7f3528a2',                      /* Required */
    Parts: [
        {PartNumber: '1', ETag: '"0cce40bdbaf2fa0ff204c20fc965dd3f"'},
    ]
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| UploadId |Upload task No. | String | Yes |
| Parts |Used to describe the block information list in this block upload | Array | Yes |
| PartNumber|Part No. | String | Yes |
| ETag| The MD5 algorithm check value of the multipart, such as `"22ca88419e2ed4721c23807c678adbe4c08a7880"`. **Be sure to enclose the value in double quotation marks** | String | Yes |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number |
| - headers | Indicates the header information returned for a request | Object |
| - Location | Domain name for public network access of the created Object | String |
| - Bucket | The target Bucket for multipart upload | String |
| - Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| - ETag | The MD5 algorithm check value of the merged file, such as `"22ca88419e2ed4721c23807c678adbe4c08a7880"`. **Be sure to enclose the value in double quotation marks** | String |


### List Parts

This API (List Parts) is used to query the uploaded file chunks in a specific multipart upload, listing all the uploaded chunks under the specified UploadId.

#### Use Case

```js
cos.multipartListPart({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.jpg',              /* Required */
    UploadId: '1521389146c60e7e198202e4e6670c5c78ea5d1c60ad62f1862f47294ec0fb8c6b7f3528a2',                      /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| UploadId | The ID of current multipart upload. You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file. | String | Yes |
| EncodingType | Indicates the encoding method of the returned value. | String | No |
| MaxParts | Maximum number of entries returned at a time. Default is 1,000 | String | No |
| PartNumberMarker |Entries are listed using UTF-8 binary order by default, starting from the marker | String | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| - Bucket | The target Bucket for multipart upload | String |
| - Encoding-type | The encoding method of the returned value | String |
| - Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| - UploadId | Indicates the ID of current multipart upload. | String |
| - Initiator | Indicates the information of the initiator of current upload | Object|
| - - DisplayName | Indicates the name of the initiator of the upload | String |
| - - ID | Indicates the ID of the initiator of the upload. Format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>; <br>in case of root account, &lt;OwnerUin> and &lt;SubUin> are of the same value | String |
| - Owner | Indicates the information of the owner of these parts | Object|
| - - DisplayName | Name of the Bucket owner | String |
| - - ID | Indicates the ID of the Bucket owner, typically the user's UIN | String |
| - StorageClass | The storage class of uploaded parts. Enumerated values: Standard, Standard_IA | String |
| - PartNumberMarker | Entries are listed using UTF-8 binary order by default, starting from the marker | String |
| - NextPartNumberMarker | If the returned entry is truncated, NextMarker represents the starting point of the next entry | String |
| - MaxParts | Maximum number of entries returned at a time | String |
| - IsTruncated | Indicates whether the returned entry is truncated. Value: 'true' or 'false' | String |
| - Part | Indicates the list of information about parts | Array |
| - - PartNumber | Indicates the part No. | String |
| - - LastModified | Indicates the time when the part was last modified | String |
| - - ETag | Indicates the MD5 algorithm check value of the part | String |
| - - Size | Indicates the part size (in bytes) | String |


### Abort Multipart Upload

This API (Abort Multipart Upload) is used to abort a multipart upload operation and delete uploaded file chunks. When Abort Multipart Upload is called, the Upload Parts returns failure to any request that is using the Upload Parts. "404 NoSuchUpload" is returned if the UploadID does not exist.

**It is recommended that you complete multipart upload in time or abort the upload operation for the reason that parts that have been uploaded but not aborted can take up storage, incurring cost.**

#### Use Case

```js
cos.multipartAbort({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.zip',                           /* Required */
    UploadId: '1521389146c60e7e198202e4e6670c5c78ea5d1c60ad62f1862f47294ec0fb8c6b7f3528a2'                       /* Required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| UploadId | The ID of current multipart upload. You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file. | String | Yes |


#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|


### List Multipart Uploads

This API (List Multiparts Uploads) is used to query multipart upload operations that are still in process. Up to 1000 such operations can be listed each time.

#### Use Case

Gets an unfinished UploadId list with a prefix of 1.zip
```js
cos.multipartList({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Prefix: '1.zip',                        /* Not required */
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Delimiter | Delimiter is a sign. Objects that contain the same string between the prefix, if specified, and the first occurrence of the delimiter after the prefix are grouped under a single result element: common prefix. If Prefix does not exist, the listing process starts from the beginning of the path. | String | No |
| EncodingType |Indicates the encoding format of the returned value. Valid value: url | String | No |
| Prefix | The returned Object key must be prefixed with Prefix. Note that the returned key will still contain Prefix when querying with prefix | String | No |
| MaxUploads | Set the maximum number of multipart returned. Valid values: 1-1,000. Default: 1,000 | String | No |
| KeyMarker | Used together with upload-id-marker.<br> <li> If upload-id-marker is not specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed.<br><li>If upload-id-marker is specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed,<br>and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. | String | No |
| UploadIdMarker | Used together with key-marker.<br><li>If key-marker is not specified,<br>upload-id-marker will be ignored.<br><li>If key-marker is specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed,<br> and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. | String | No |</li>

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number|
| - headers | Indicates the header information returned for a request | Object|
| - Bucket | The target Bucket for multipart upload | String |
| - Encoding-Type | Indicates the encoding format of the returned value. Valid value: url | String |
| - KeyMarker | Entries will be listed starting from this key value | String |
| - UploadIdMarker | Entries will be listed starting from this UploadId value | String |
| - NextKeyMarker | If the returned entry is truncated, NextKeyMarker represents the starting point of the next entry | String |
| - NextUploadIdMarker | If the returned entry is truncated, UploadId represents the starting point of the next entry | String |
| - MaxUploads | Sets the maximum number of multipart returned. Valid values: 1-1,000 | String |
| - IsTruncated | Indicates whether the returned entry is truncated. Value: 'true' or 'false' | String |
| - Delimiter | Delimiter is a sign. Objects that contain the same string between the prefix, if specified, and the first occurrence of the delimiter after the prefix are grouped under a single result element: common prefix. If Prefix does not exist, the listing process starts from the beginning of the path.| String |
| - Prefix | The returned Object key must be prefixed with Prefix. Note that the returned key will still contain Prefix when querying with prefix | String |
| - CommonPrefixs | The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix | Array |
| - Prefix | Displays detailed CommonPrefixs | String |
| - Upload | A collection of information about Upload | Array |
| - - Key | Object name | String |
| - - UploadId | Indicates the ID of current multipart upload | String |
| - StorageClass | Indicates the storage class of uploaded parts. Enumerated values: Standard, Standard_IA | String |
| - Initiator | Indicates the information of the initiator of current upload | Object|
| - - DisplayName | Indicates the name of the initiator of the upload | String |
| - - ID | ID of the initiator of the upload. Format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>; in case of root account, &lt;OwnerUin> and &lt;SubUin> are of the same value | String |
| - Owner | Indicates the information of the owner of these parts | Object|
| - - DisplayName | Name of the Bucket owner | String |
| - - ID | ID of the Bucket owner. Format: qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>; in case of root account, &lt;OwnerUin> and &lt;SubUin> are of the same value | String |
| - Initiated | Indicates the starting time for multipart upload | String |



## Multipart Upload/Replication Task

This kind of method is the encapsulation of the above native method, realizes the whole process of multipart uploading/replication, supports concurrent multipart uploading/replication, resuming upload from breakpoint, and the cancellation, suspension and restart of upload tasks.


### Slice Upload File

This API (Slice Upload File) is used to upload a file in parts.

#### Use Case

```js
cos.sliceUploadFile({
    Bucket: 'test-1250000000', /* Required */
    Region: 'ap-guangzhou',    /* Required */
    Key: '1.zip',              /* Required */
    Body: file,                /* Required */
    TaskReady: function(taskId) {                   /* Not required */
        console.log(taskId);
    },
    onHashProgress: function (progressData) {       /* Not required */
        console.log(JSON.stringify(progressData));
    },
    onProgress: function (progressData) {           /* Not required */
        console.log(JSON.stringify(progressData));
    }
}, function(err, data) {
    console.log(err || data);
});
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| Bucket | Bucket name. The bucket entered must be in a format of {name}-{appid} | String | Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |  String |Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| Body | The content of the file uploaded, which can be File objects or Blob objects | File \ Blob| Yes |
| SliceSize | Indicates the size of part | String | No |
| AsyncLimit | Indicates the number of concurrent parts | String | No |
| StorageClass | The storage level of Object. Enumerated values: STANDARD, STANDARD_IA | String | No |
| TaskReady | Indicates the callback function when the upload task is created, returns a taskId that uniquely identifies the upload task, which can be used to cancel  (cancelTask), pause (pauseTask), and restart (restartTask) the upload task. | Function| No |
| - taskId | Indicates the number of task to be uploaded | String | No |
| onHashProgress | Indicates the progress callback function to calculate a file's MD5 value. The callback parameter is the progress object progressData | Function| No |
| - progressData.loaded | Indicates the size of the verified portion of the file in bytes | Number| No |
| - progressData.total | Indicates the size of the entire file in bytes | Number| No |
| - progressData.speed | Indicates the verification speed in bytes/s | Number| No |
| - progressData.percent | The percentage of file verified in decimal, for example, 0.5 for 50% | Number| No |
| onProgress | Indicates the progress callback function of the uploaded file. The callback parameter is the progress object progressData | Function| No |
| - progressData.loaded | Indicates the size of the uploaded portion of the file in bytes | Number| No |
| - progressData.total | Indicates the size of the entire file in bytes | Number| No |
| - progressData.speed | Indicates the upload speed in bytes/s | Number| No |
| - progressData.percent | The percentage of file uploaded in decimal, for example, 0.5 for 50% | Number| No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|----------|------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object |
| - statusCode |Indicates the HTTP status code returned for a request, such as 200, 403, and 404 |Number|
| - headers | Indicates the header information returned for a request |Object|
| - Location | Domain name for public network access of the created Object | String |
| - Bucket | The target Bucket for multipart upload | String |
| - Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| - ETag | The MD5 algorithm check value of the merged file, such as `"22ca88419e2ed4721c23807c678adbe4c08a7880"`. **Be sure to enclose the value in double quotation marks** | String |

### Cancel Task

This API (Cancel Task) is used to cancel the multipart upload task based on the taskid.

#### Use Case

```js
var taskId = 'xxxxx';                   /* Required */
cos.cancelTask(taskId);
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| taskId | Indicates the number of the file upload task. When the sliceUploadFile method is called, its TaskReady callback returns the taskId of the upload task. | String | Yes |

### Pause Task

This API (Pause Task) is used to pause the multipart upload task based on the taskid.

#### Use Case

```js
var taskId = 'xxxxx';                   /* Required */
cos.pauseTask(taskId);
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| taskId | Indicates the number of the file upload task. When the sliceUploadFile method is called, its TaskReady callback returns the taskId of the upload task. | String | Yes |


### Restart Task

This API (Get Service) is used to restart the upload task based on the taskid, including the upload task that the user manually stopped (stop by calling pauseTask) or stopped because of an upload error.

#### Use Case

```js
var taskId = 'xxxxx';                   /* Required */
cos.restartTask(taskId);
```

#### Parameters

| Parameter Name | Description | Type | Required |
|--------|----------|------|------|
| taskId | Indicates the number of the file upload task. When the sliceUploadFile method is called, its TaskReady callback returns the taskId of the upload task. | String | Yes |


###  Slice Copy File

This API (Slice Copy File) is used to copy a file from the source path to the destination path through multipart copy. In the process of copying, file meta-attributes and ACLs can be modified. Users can use this API to move or rename a file, modify file attributes and create a copy.

#### Method prototype

Call Slice Copy File:

```js
cos.sliceCopyFile({
    Bucket: 'test-1250000000',                               /* Required */
    Region: 'ap-guangzhou',                                  /* Required */
    Key: '1.zip',                                            /* Required */
    CopySource: 'test1.cos.ap-guangzhou.myqcloud.com/2.zip', /* Required */
    onProgress:function (progressData) {                     /* Not required */
        console.log(JSON.stringify(progressData));
    }
},function (err,data) {
    console.log(err || data);
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| CopySource | The path of source file URL. You can specify the history version with the versionid sub-resource | String | Yes |
| ChunkSize | Indicates the size of each part for multipart copy, which defaults to 1048576 (1 MB) | Number | No |
| SliceSize | Indicates the file size for multipart copy, which defaults to 5 GB | Number | No |
| onProgress | Indicates the progress callback function of the uploaded file. The callback parameter is the progress object progressData | Function | No |
| - progressData.loaded | Indicates the size of the uploaded portion of the file in bytes | Number | No |
| - progressData.total | Indicates the size of the entire file in bytes | Number | No |
| - progressData.speed | Indicates the upload speed in bytes/s | Number | No |
| - progressData.percent | The percentage of file uploaded in decimal, for example, 0.5 for 50% | Number | No |

#### Callback function description

```js
function(err, data) { ... }
```

| Parameter Name | Description | Type |
|--------|---------|--------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document]  Object  |
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number |
| - headers | Indicates the header information returned for a request | Object |
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object|
| - statusCode | Indicates the HTTP status code returned for a request, such as 200, 403, and 404 | Number |
| - headers | Indicates the header information returned for a request | Object |
| - Location | Domain name for public network access of the created Object | String |
| - Bucket | The target Bucket for multipart upload | String |
| - Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| - ETag | The MD5 algorithm check value of the merged file, such as "22ca88419e2ed4721c23807c678adbe4c08a7880". Be sure to enclose the value in double quotation marks | String |

