> For more information on the definitions of SecretId, SecretKey, Bucket, and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

URL to Node.js SDK github: [tencentyun/cos-nodejs-sdk-v5](https://github.com/tencentyun/cos-nodejs-sdk-v5)

## Service Operation

### Get Service

#### Feature description

This API (Get Service) is used to obtain the list of all Buckets under the current account. This API requires Authorization signature for verification and can only obtain the Bucket list under the account to which the AccessID in signature belongs.

#### Method prototype

Call Get Service:

```js

cos.getService(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

* **No special parameters** 

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| Owner | Provides the information of the Bucket owner |Object|
| uin |UIN of the Bucket owner |String|	
| Buckets |Provides the information of the Bucket list returned this time |Array|
| Name|Bucket name |String|
| CreateDate |Date on which the Bucket was created. It takes on an ISO8601 format. |String|

## Bucket Operations

### Head Bucket

#### Feature description

This API (Head Bucket) is used to determine whether the Bucket and the permission to access the Bucket exist. Head and Read have the same permission.

#### Method prototype

Call Head Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE'		/* Required */
};

cos.headBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| BucketExist| Indicates whether a Bucket exists |Boolean| 
|BucketAuth |Indicates whether a user has the Bucket permission |Boolean| 


###  Get Bucket

#### Feature description 

This API (Get Bucket) is equivalent to List Object. It is used to list some or all of the Objects under the Bucket. Read permission is required to initiate this request.

#### Method prototype

Call Get Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE',	/* Required */
	Prefix : 'STRING_VALUE',	/* Not required */
	Delimiter : 'STRING_VALUE', /* Not required */
	Marker : 'STRING_VALUE',	/* Not required */
	MaxKeys : 'STRING_VALUE',	/* Not required */
	EncodingType : 'STRING_VALUE',	/* Not required */
};

cos.getBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   Prefix | Indicates the prefix match, which is used to specify the prefix address of the returned object key | String | No |
|   Delimiter |Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path |   String| No |
|   Marker | Entries are listed using UTF-8 binary order by default, starting from the marker |  String| No |
|   MaxKeys | Maximum number of entries returned at a time. Default is 1,000 |  String| No |
|   EncodingType | Indicates the encoding method of the returned value. |  String| No |



#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|   CommonPrefixes | The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix |   Array| 
|   Prefix | Indicates the prefix match, which is used to specify the prefix address of the returned object key | String | No |
|   Name | Bucket name |  String| 
|   Prefix | Prefix of an object key | String| No |
|   Marker | Entries are listed using UTF-8 binary order by default, starting from the marker | String | 
|   MaxKeys | Maximum number of entries returned at a time |  String|   
|   IsTruncated | Indicates whether the returned entry is truncated. Value: 'true' or 'false' |  String| 
|   NextMarker | If the returned entry is truncated, NextMarker represents the starting point of the next entry |  String| 
|   Encoding-Type | Encoding type of Delimiter, which is used for Marker, Prefix, NextMarker, and Key |  String| 
|   Contents | Metadata information |   Array|  
|   ETag | The SHA-1 algorithm check value of the file |  String| 
|   Size | File size (in bytes) |  String| 
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
|   LastModified | Indicates the time when Object was last modified |   String| 
|   Owner |Information of the Bucket owner |   Object| 
|   ID |Bucket Owner's UID |   String|  



###  Put Bucket

#### Feature description

This API (Put Bucket) is used to create a Bucket under the specified account.

#### Method prototype

Call Put Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE',	/* Required */
	ACL : 'STRING_VALUE',	/* Not required */
	GrantRead : 'STRING_VALUE', /* Not required */
	GrantWrite : 'STRING_VALUE',	/* Not required */
	GrantFullControl : 'STRING_VALUE'	/* Not required */
};

cos.putBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
| ACL | Allows users to define file permissions. Valid values: private, public-read, and public-read-write. Default value is private. |String|No |
| GrantRead |Grants read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |String| No |
|GrantWrite |Grants write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |String| No |
| GrantFullControl |Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |String| No |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| Location| Operation address of Bucket after it is created successfully |String| 

###  Delete Bucket

#### Feature description

This API (Delete Bucket) is used to delete a Bucket under the specified account. The Bucket must be empty before it can be deleted.

#### Method prototype

 Call Delete Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE'		/* Required */
};

cos.deleteBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| DeleteBucketSuccess| Indicates whether the deletion is successful |Boolean| 


###  Get Bucket ACL

#### Feature description

This API is used to read the ACL of a Bucket. Only the Bucket owner is allowed to perform the operation.

#### Method prototype

Call Get Bucket ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE'		/* Required */
};

cos.getBucketAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| Owner | Indicates the owner of the resource |  Object|
|uin |QQ number of the user |  String|    
| AccessControlList | Information of the authorized user and permissions |    Object|   
|Grant | Specific authorization information |  Array| 
| Permission | Permission information. Enumerated values: READ, WRITE, and FULL_CONTROL |   String| 
|Grantee | Resource information of the authorized user |  Object| 
| uin | QQ number of the authorized user or 'anonymous' |  String| 
| Subacount | QQ number of the sub-account |   String| 


### Put Bucket ACL

#### Feature description

This API is used to write ACL for a Bucket. Importing a new ACL using Put Bucket ACL operation will overwrite the existing ACL. Only the owner is allowed to perform the operation.

#### Method prototype

Call Put Bucket ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',			/* Required */
	Region : 'STRING_VALUE',			/* Required */
	ACL : 'STRING_VALUE',				/* Not required */
	GrantRead : 'STRING_VALUE', 		/* Not required */
	GrantWrite : 'STRING_VALUE',		/* Not required */
	GrantFullControl : 'STRING_VALUE'	/* Not required */
};

cos.putBucketAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   ACL | Allows users to define file permissions. Valid values: private and public-read. Default value: private. |  String| No |
|   GrantRead |Grants read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |  String| No |
|   GrantWrite |Grants write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |  String| No |
|   GrantFullControl | Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |   String| No |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|BucketGrantSuccess | Whether authorization is successful |Boolean| 


###  Get Bucket CORS

#### Feature description

This API (Get Bucket CORS) is used to read cross-origin access configurations.

#### Method prototype

Call Get Bucket CORS:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE'		/* Required */
};

cos.getBucketCors(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|CORSRule | A collection of configurations |Array| 
| AllowedMethod | Allowed HTTP operations. Enumerated values: Get, Put, Head, Post, and Delete |Array| 
| AllowedOrigin| Allowed access sources. The wildcard "*" is supported. |Array| 
| AllowedHeader | When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. |Array| 
| ExposeHeader| Sets the custom header information that can be received by the browser from the server end |Array| 
|MaxAgeSeconds |Sets the validity period of the results obtained by OPTIONS |String|
| ID|Rule name |String| 


### Put Bucket CORS

#### Feature description

This API (Put Bucket CORS) is used to read and write cross-origin access configurations.

#### Method prototype

Call Put Bucket CORS:

```js

var params = {
	Bucket : 'STRING_VALUE',		/* Required */
	Region : 'STRING_VALUE',		/* Required */
	CORSRules : [
		{
			ID : 'STRING_VALUE',	/* Not required */
			AllowedMethods: [ 		/* Required */
			  'STRING_VALUE',
			  ...
			],
			AllowedOrigins: [		 /* Required */
			  'STRING_VALUE',
			  ...
			],
			AllowedHeaders: [		/* Not required */
			  'STRING_VALUE',
			  ...
			],
			ExposeHeaders: [		/* Not required */
				'STRING_VALUE',
				...
			],
			MaxAgeSeconds: 'STRING_VALUE'	/* Not required */
		  },
		  ....
	]
};

cos.putBucketCors(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   CORSRules | A collection of cross-origin rules |  Array| No |
|   ID | Rule name |   String| No |
|   AllowedMethods | Allowed HTTP operations. Enumerated values: Get, Put, Head, Post, and Delete |   Array| Yes |
|   AllowedOrigins | Allowed access sources. The wildcard "*" is supported. The protocol, port and domain name must be consistent. |  Array| Yes |
|   AllowedHeaders | When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. |  Array| No |
|   ExposeHeaders | Sets the custom header information that can be received by the browser from the server end |  Array| No |
|   MaxAgeSeconds | Sets the validity period of the results obtained by OPTIONS |   String| No |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| PutBucketCorsSucesss | Whether Bucket CORS is configured successfully |Boolean|


###  Delete Bucket CORS

#### Feature description

This API (Delete Bucket CORS) is used to delete cross-origin access configurations.

#### Method prototype

Call Delete Bucket CORS:

```js

var params = {
	Bucket : 'STRING_VALUE',		/* Required */
	Region : 'STRING_VALUE'			/* Required */
};

cos.deleteBucketCors(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| DeleteBucketCorsSuccess | Whether Bucket CORS is deleted successfully |Boolean|  


### Get Bucket Location

#### Feature description

This API (Get Bucket Location) is used to obtain the region information of the Bucket. Only the Bucket owner is allowed to read the information.

#### Method prototype

Call Get Bucket Location:

```js

var params = {
	Bucket : 'STRING_VALUE',		/* Required */
	Region : 'STRING_VALUE'			/* Required */
};

cos.getBucketLocation(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| LocationConstraint | Region where the Bucket resides. Enumerated values: china-east, china-south, china-north, china-west, and singapore |String|  


### Get Bucket Tagging

#### Feature description

This API (Get Bucket Tagging) is used to obtain tags of a specified Bucket.

#### Method prototype
Call Get Bucket Tagging:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE'		/* Required */
};

cos.getBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| Tags  | A collection of Bucket tags | Array |
| Key  | Type name of Tag | String | 
| Value | Tag's value |  String |


###  Put Bucket Tagging

#### Feature description

This API (Put Bucket Tagging) is used to tag a specified Bucket.

#### Operation parameter description

 Call Put Bucket Tagging:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE',	/* Required */
	Tags :  [
		{
			Key : 'key1',		/* Required */
			Value : 'value1'	/* Required */
		},
		...
	]
};

cos.putBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
| Tags  | A collection of Bucket tags | Array |Yes |
| Key  | Type name of Tag | String | Yes |
| Value | Tag's value |  String |Yes |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| PutBucketTaggingSuccess |Whether Tag is configured successfully |Boolean|	


### Delete Bucket Tagging

#### Feature description

This API (Delete Bucket Tagging) is used to delete tags of a specified Bucket.

#### Method prototype

Call Delete Bucket Tagging:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required */
	Region : 'STRING_VALUE'		/* Required */
};

cos.deleteBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|DeleteBucketTaggingSuccess |Whether Bucket tag is deleted successfully |Boolean|	


## Object Operations
### Head Object

#### Feature description

This API (Head Object) is used to get the metadata of an Object. It has the same permissions as Get Object.

#### Method prototype
Call Head Object:

```js

var params = {
	Bucket : 'STRING_VALUE',		/* Required */
	Region : 'STRING_VALUE',		/* Required */
	Key : 'STRING_VALUE',			/* Required */
	IfModifiedSince : 'STRING_VALUE'	/* Not required */
};

cos.headObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| IfModifiedSince |If Object is modified after the specified time, the Object meta information is returned |String| No |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| x-cos-object-type | Indicates whether the Object is appendable for upload. Enumerated values: normal or appendable |  String|  	
|   x-cos-storage-class | The storage level of Object. Enumerated values: Standard, and Standard_IA |  String|  
|   x-cos-meta- *   | User-defined metadata |  String| 
|   NotModified | If IfModifiedSince is used for request and the file is not modified, the value is true |  Boolean| 


### Get Object

#### Feature description

This API (Delete Object) is used to download a file (Object) locally. This operation requires that the user have the read permission for the target Object or the read permission for the target Object be available for everyone (public-read).

#### Method prototype

Call Get Object:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Key : 'STRING_VALUE',							/* Required */
	ResponseContentType : 'STRING_VALUE',			/* Not required */
	ResponseContentLanguage : 'STRING_VALUE',		/* Not required */
	ResponseExpires : 'STRING_VALUE',				/* Not required */
	ResponseCacheControl : 'STRING_VALUE',			/* Not required */
	ResponseContentDisposition : 'STRING_VALUE',	/* Not required */
	ResponseContentEncoding : 'STRING_VALUE',		/* Not required */
	Range : 'STRING_VALUE',							/* Not required */
	IfModifiedSince : 'STRING_VALUE',				/* Not required */
	Output : 'STRING_VALUE' || 'WRITE_STRING'		/* Required */
};

cos.getObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|  Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
|  ResponseContentType | Sets the Content-Type parameter in the response header |  String| No |
|  ResponseContentLanguage | Sets the Content-Language parameter in the response header |  String| No |
|  ResponseExpires | Sets the Content-Expires parameter in the response header |  String| No |
|  ResponseCacheControl | Sets the Cache-Control parameter in the response header |  String| No |
|  ResponseContentDisposition | Sets the Content-Disposition parameter in the response header |  String| No |
|  ResponseContentEncoding | Sets the Content-Encoding parameter in the response header |  String| No |
|  Range | The specified range of file download defined in RFC 2616 (in bytes) |  String| No |
|  IfModifiedSince | The file content is returned if the file has been modified after the specified time |  String| No |
|  Output | A file path that needs outputting or a write stream |   String / WriteStream| Yes |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|   x-cos-object-type | Indicates whether the Object is appendable for upload. Enumerated values: normal or appendable |   String|  	
 |   x-cos-storage-class | The storage level of Object. Enumerated values: Standard, and Standard_IA |  String| 
 |   x-cos-meta- * | User-defined metadata |   String|  
 |   NotModified |If IfModifiedSince is used for request and the file is not modified, the value is true |  Boolean|  

### Put Object

#### Feature description

This API (Put Object) is used to upload a file (Object) to the specified Bucket.

>**Note:** Key (File name) cannot end with `/`. Otherwise, it will be identified as a folder.

#### Method prototype

Call Put Object:

```js
cos.putObject({
    Bucket : 'STRING_VALUE',                        /* Required */
    Region : 'STRING_VALUE',                        /* Required */
    Key : 'STRING_VALUE',                           /* Required */
    Body: fs.createReadStream('./a.zip'),           /* Required */
    onProgress: function (progressData) {
        console.log(progressData);
    },
}, function(err, data) {
    if(err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
|   CacheControl | The caching policy defined in RFC 2616, which is saved as Object metadata |   String| No |
|   ContentDisposition | The file name defined in RFC 2616, which is saved as Object metadata |   String|No |
|   ContentEncoding | The encoding format defined in RFC 2616, which is saved as Object metadata |  String| No |
|   ContentLength | HTTP request content length defined in RFC 2616 (in bytes) |  String| Yes |
|   ContentType | The content type (MIME) defined in RFC 2616, which is saved as Object metadata |   String| No |
|   Expect | If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server |  String| No |
|   Expires | The expiration time defined in RFC 2616, which is saved as Object metadata |   String| No |
|   ContentSha1 | The 160-bit content SHA-1 algorithm check value defined in RFC 3174 |   String| No |
|   ACL | Allows users to define file permission. Valid values: private, and public-read |   String| No |
|   GrantRead | Grants read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID" |  String| No |
|   GrantWrite | Grants write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID" |   String| No |
|   GrantFullControl | Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID" |   String| No |
|   x-cos-meta- * | The header information that can be defined by users, which is returned as Object metadata. The size is limited to 2K. |    String| No |
|   Body | Input file path or file stream |   String/ Stream| Yes |
|   onProgress | Progress callback function. Callback is an object which includes progress information |   Function| No |



#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| ETag| Returns the MD5 algorithm check value of the file. ETag value can be used to check whether the Object content has changed |String|

###  Delete Object
#### Feature description

This API (Delete Object) is used to delete a file (Object).

#### Method prototype

Call Delete Object:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Key : 'STRING_VALUE'							/* Required */
};

cos.deleteObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|DeleteObjectSuccess| Whether a file is deleted successfully |Boolean|	
|BucketNotFound | If the specific Bucket is not found, the value is true |Boolean|


###  Options Object

#### Feature description

This API (Options Object) is used to implement a pre-request for cross-origin access. That is , an OPTIONS request is sent to the server to verify whether cross-origin operations are possible.

#### Method prototype

Call Options Object:

```js

var params = {
	Bucket : 'STRING_VALUE',		/* Required */
	Region : 'STRING_VALUE',		/* Required */
	Key : 'STRING_VALUE',			/* Required */
	Origin : 'STRING_VALUE', 		/* Required */
	AccessControlRequestMethod : 'STRING_VALUE', 		/* Required */
	AccessControlRequestHeaders : 'STRING_VALUE'		/* Not required */
};

cos.optionsObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
|Origin | Simulates the origin from which the request for cross-origin access is sent |String|Yes |
|AccessControlRequestMethod|Simulates the HTTP method of the request for cross-origin access |String| Yes |
| AccessControlRequestHeaders |Simulates the header of the request for cross-origin access |String| No |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|AccessControlAllowOrigin  |Simulates the origin from which the request for cross-origin access is sent. If the origin is not allowed, the header will not be returned |String |	
| AccessControlAllowMethods  |Simulates the HTTP method of the request for cross-origin access. If the method is not allowed, the header will not be returned |String |
| AccessControlAllowHeaders  |Simulates the header of the request for cross-origin access. If the simulation of any request header is not allowed, the header will not be returned |String |
| AccessControlExposeHeaders  |Returned headers supported by cross-origin request, separated by commas |String |
| AccessControlMaxAge  |Sets the validity period of the results obtained by OPTIONS |String |


### Get Object ACL

#### Feature description

This API (Get Object ACL) is used to read the Object ACL. Only the Object owner is allowed to perform the operation.

#### Method prototype

Call Get Object ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Key : 'STRING_VALUE'							/* Required */
};

cos.getObjectAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|   Owner | Indicates the owner of the resource |  Object|  
|   uin | QQ number of the user |  String|  
|   AccessControlList | Information of the authorized user and permissions |  Object|  
|   Grant | Specific authorization information |  Array|  
|   Permission | Permission information. Enumerated values: READ, WRITE, and FULL_CONTROL |  String| 
|   Grantee | Resource information of the authorized user |  Object|  
|   uin | QQ number of the authorized user or 'anonymous' |  String|  
|   Subacount | QQ number of the sub-account |   String|  


### Put Object ACL

#### Feature description

This API (Put Object ACL) is used to write ACL for an Object.

#### Method prototype

 Call Put Object ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',			/* Required */
	Region : 'STRING_VALUE',			/* Required */
	Key : 'STRING_VALUE',				/* Required */
	ACL : 'STRING_VALUE',				/* Not required */
	GrantRead : 'STRING_VALUE', 		/* Not required */
	GrantWrite : 'STRING_VALUE',		/* Not required */
	GrantFullControl : 'STRING_VALUE'	/* Not required */
};

cos.putObjectAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
|ACL | Allows users to define file permissions. Valid values: private, public-read, and public-read-write. Default value is private. |   String| No |
|   GrantRead | Grants read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |  String| No |
  |   GrantWrite | Grants write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID". |  String| No |
|   GrantFullControl | Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".For authorization to the root account, uin="RootAcountID". |  String| No |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  |


### Delete Multiple Object

#### Feature description

This API (Delete Multiple Object) is used for batch deletion of files. A maximum of 1,000 files can be deleted at a time. COS provides two modes for returned results: Verbose and Quiet. Verbose mode will return the result of deletion of each Object, while Quiet mode only returns the information of the Objects with an error.


#### Method prototype

 Call Delete Multiple Object:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Quiet : 'BOOLEAN_VALUE',						/* Not required */
	Objects :  [
	    {
	        Key : 'STRING_VALUE'					/* Required */
        }
    ]
};

cos.deleteMultipleObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
| Quiet |Boolean. Indicates whether the Quiet mode is enabled. True means Quiet mode is enabled, and False means Verbose mode is enabled. Default is False. |Boolean| No |
| Objects |List of files to be deleted |Array| No |
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|   Deleted | Indicates the information of Object that has been deleted successfully |  Array| 
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
|   Error | Indicates the information of Object that failed to be deleted |  Array| 
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
|   Code | Error code for failed deletion |  String|   
|   Message | Message indicating the deletion error |  String|  


## Multipart Upload Operations
### Initiate Multipart Upload

#### Feature description

This API (Initiate Multipart Upload) is used to initialize multipart upload. After the request is executed successfully, Upload ID is returned for the subsequent Upload Part requests.

#### Method prototype
 Call Initiate Multipart Upload:

```js
cos.multipartInit({
    Bucket : 'STRING_VALUE',						/* Required */
    Region : 'STRING_VALUE',						/* Required */
    Key : 'STRING_VALUE',							/* Required */
}, function(err, data) {
    if(err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|  Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes | 
|   CacheControl | The caching policy defined in RFC 2616, which is saved as Object metadata |  String| No |
|   ContentDisposition | The file name defined in RFC 2616, which is saved as Object metadata |  String| No |
|   ContentEncoding | The encoding format defined in RFC 2616, which is saved as Object metadata |   String| No |
|   ContentType | The content type (MIME) defined in RFC 2616, which is saved as Object metadata |  String| No |
|   Expires | The expiration time defined in RFC 2616, which is saved as Object metadata |  String| No |
|   ACL | Allows users to define file permission. Valid values: private and public-read |   String| No |
|   GrantRead | Grants read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID" |   String| No |
|   GrantWrite | Grants write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID" |   String| No |
|   GrantFullControl | Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" ".<br>For authorization to a sub-account, uin="RootAcountID/SubAccountID".<br>For authorization to the root account, uin="RootAcountID" |   String| No |
|   StorageClass | Sets the storage level of Object. Enumerated values: Standard and Standard_IA. Default is Standard (this is only supported for South China region) |  String| No |
|   x-cos-meta- * | The header information that can be defined by users, which is returned as Object metadata. The size is limited to 2K. |  String| No |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| Bucket | The target Bucket for multipart upload |String| 
|Key | Object name |String| 
| UploadId | ID used in subsequent uploads |String| 

### Upload Part

#### Feature description

This API (Upload Part) is used to implement multipart upload after initialization. A file can be split into 10000 chunks at most (minimum is 1) for multipart upload, and the size of each file chunk should be between 1 MB and 5 GB. Upload Part should be used with partNumber and uploadID. partNumber is the part No. and supports out-of-order upload.

#### Method prototype

Call Upload Part:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Key : 'STRING_VALUE',							/* Required */
	ContentLength : 'STRING_VALUE',					/* Required */
	Expect : 'STRING_VALUE',						/* Not required */
	ContentSha1 : 'STRING_VALUE',					/* Not required */
	PartNumber : 'STRING_VALUE',					/* Required */
	UploadId : 'STRING_VALUE',						/* Required */
};

cos.multipartUpload(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|  Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| ContentLength |HTTP request content length defined in RFC 2616 (in bytes) |String| Yes |
| Expect |If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server |String| No |
| ContentSha1| The 160-bit content SHA-1 algorithm check value defined in RFC 3174 |String|No |
| PartNumber |Part No. |String| Yes |
| UploadId | Upload task No. |String|Yes |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| ETag| ETag value of a part, which is sha1 check value |String|


### Complete Multipart Upload

#### Feature description

This API (Complete Multipart Upload) is used to complete the entire multipart upload. After you have uploaded all the file chunks using Upload Parts, you can use this API to complete the upload. When using this API, you need to provide the PartNumber and ETag for every chunk in Body, to verify the accuracy of chunks.

#### Method prototype

Call Complete Multipart Upload:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Key : 'STRING_VALUE',							/* Required */
	UploadId : 'STRING_VALUE',						/* Required */
	Parts : [
		{
			PartNumber : 'STRING_VALUE',			/* Required */
			ETag : 'STRING_VALUE'					/* Required */
		},
		...
	]
};

cos.multipartComplete(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|  Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| UploadId |Upload task No. |String| Yes |
|Parts |ETag information of a part |Array| Yes |
| PartNumber |Part No. |String| Yes |
| ETag| ETag value of a part, which is sha1 check value. It must be enclosed in double quotes, such as: "3a0f1fd698c235af9cf098cb74aa25bc". |String|Yes |

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| Location| Domain name for public network access of the created Object |String| 
| Bucket |The target Bucket for multipart upload |String| 
|Key |Object name |String|  
|ETag | The MD5 algorithm check value of the file |String| 


### List Parts

#### Feature description

This API (List Parts) is used to query the uploaded parts in a specific multipart upload process.

#### Method prototype

Call List Parts:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Key : 'STRING_VALUE',							/* Required */
	UploadId : 'STRING_VALUE',						/* Required */
	EncodingType : 'STRING_VALUE',					/* Not required */
	MaxParts : 'STRING_VALUE',						/* Not required */
	PartNumberMarker : 'STRING_VALUE'				/* Not required */
};

cos.multipartListPart(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|  Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
|UploadId |Upload task No. |String| Yes |
|EncodingType | Indicates the encoding method of the returned value |String| No |
| MaxParts |Maximum number of entries returned at a time. Default is 1,000 |String| No |
| PartNumberMarker |Entries are listed using UTF-8 binary order by default, starting from the marker |String| No |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|   Bucket | The target Bucket for multipart upload |  String|  
|   Encoding-type | The encoding method of the returned value |  String| 
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
|   UploadID | Indicates the ID of current multipart upload |  String| 
|   Initiator | Indicates the information of the initiator of current upload. Child node includes UID |   Object|   
|   UID | Developer's APPID |  String| 
|   Owner | Indicates the information of the owner of these uploaded parts. Child node includes UID |  Object| 
|   UID | Owner's QQ number |  String| 
|   StorageClass | The storage class of uploaded parts. Enumerated values: Standard, Standard_IA |  String|  
 |   PartNumberMarker | Entries are listed using UTF-8 binary order by default, starting from the marker |  String|    
  |   NextPartNumberMarker | If the returned entry is truncated, NextMarker represents the starting point of the next entry |  String|   
  |   MaxParts | Maximum number of entries returned at a time |  String|  
  |   IsTruncated | Indicates whether the returned entry is truncated. Value: 'true' or 'false' |   String| 
  |   Part | A collection of information about parts |  Array|  
 |   PartNumber | Part No. |  String| 
 |   LastModified | Indicates the time when the part was last modified |  String| 
 |   Etag | Indicates the SHA-1 algorithm check value of the part |  String| 
|   Size | Indicates the part size (in bytes) |String| 


### Abort Multipart Upload

#### Feature description

This API (Abort Multipart Upload) is used to abort a multipart upload operation and delete uploaded file chunks. When Abort Multipart Upload is called, a failure is returned for any request that is using Upload Parts.

#### Method prototype
Call Abort Multipart Upload:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Key : 'STRING_VALUE',							/* Required */
	UploadId : 'STRING_VALUE'						/* Required */
};

cos.multipartAbort(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|  Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| UploadId |Upload task No. |String| Yes |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|MultipartAbortSuccess |Whether Multipart Abort is successful |Boolean| 


### List Multipart Uploads

#### Feature description

This API (List Multiparts Uploads) is used to query multipart upload operations that are still in process. Up to 1000 such operations can be listed each time.

#### Method prototype

Call List Multipart Uploads:

```js

var params = {
	Bucket : 'STRING_VALUE',						/* Required */
	Region : 'STRING_VALUE',						/* Required */
	Delimiter : 'STRING_VALUE',						/* Not required */
	EncodingType : 'STRING_VALUE',					/* Not required */
	Prefix : 'STRING_VALUE',						/* Not required */
	MaxUploads : 'STRING_VALUE',					/* Not required */
	KeyMarker : 'STRING_VALUE',						/* Not required */
	UploadIdMarker : 'STRING_VALUE'					/* Not required */
};

cos.multipartList(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
| Delimiter | Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path |   String| No |
|   EncodingType | Indicates the encoding method of the returned value |  String| No |
|   Prefix | Indicates the prefix match, which is used to specify the prefix address of the returned object key | String | No |
|   MaxUploads | Maximum number of entries returned at a time. Default is 1,000 |  String| No |
|   KeyMarker | Used together with upload-id-marker.<br><li>If upload-id-marker is not specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed.<br><li>If upload-id-marker is specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed,<br>and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. | String| No |
|   UploadIdMarker | Used together with key-marker.<br><li>If key-marker is not specified,<br> upload-id-marker will be ignored.<br><li> If key-marker is specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed,<br> and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. |   String|No |
</li>

#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
|   Bucket | The target Bucket for multipart upload |String|   
|   Encoding-type | The encoding method of the returned value |  String| 
|   KeyMarker | Entries will be listed starting from this key value |  String| 
|   UploadIdMarker | Entries will be listed starting from this UploadId value |  String| 
|   NextKeyMarker | If the returned entry is truncated, NextKeyMarker represents the starting point of the next entry |   String|  
|   NextUploadIdMarker | If the returned entry is truncated, UploadId represents the starting point of the next entry |   String|  
|   IsTruncated | Indicates whether the returned entry is truncated. Value: 'true' or 'false' |   String| 
|   delimiter | Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path. |   String| 
|   CommonPrefixs | The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix |  Array| 
|   Prefix | Indicates the prefix match, which is used to specify the prefix address of the returned object key | String | No |
|   Upload | A collection of information about Upload |   Array| 
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
|   UploadID | Indicates the ID of current multipart upload |  String| 
|   StorageClass | Indicates the storage class of uploaded parts. Enumerated values: Standard, Standard_IA |  String|   
|   Initiator | Indicates the information of the initiator of current upload. Child node includes UID |   Object|   
|   UID | Developer's APPID |   String|  
|   Owner | Indicates the information of the owner of these uploaded parts. Child node includes UID |  Object|  
|   UID | Owner's QQ number |  String|   
|   Initiated | Indicates the starting time for multipart upload |  String| 


###  Slice Upload File

#### Feature description

This API (Slice Upload File) is used to upload a file in parts.

#### Method prototype

Call Slice Upload File:

```js
var params = {
	Bucket: 'STRING_VALUE',	/* Required */
	Region: 'STRING_VALUE',	/* Required */
	Key: 'STRING_VALUE',	/* Required */
	FilePath: 'STRING_VALUE',	/* Required */
	SliceSize: 'STRING_VALUE',	/* Not required */
	AsyncLimit: 'NUMBER_VALUE',	/* Not required */
    onHashProgress: function (progressData) {
        console.log(JSON.stringify(progressData));
    },
    onProgress: function (progressData) {
        console.log(JSON.stringify(progressData));
    },
};

cos.sliceUploadFile(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation parameter description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
|   Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
|   FilePath | Path to the local file |  String| Yes |
|   SliceSize | Indicates the size of part |   String| No |
|   AsyncLimit | Indicates the number of concurrent parts |  String| No |
|   onHashProgress | Progress callback function to calculate a file's sha1 value. Callback is an object which includes progress information |  Function| No |
|   onProgress | Progress callback function. Callback is an object which includes progress information |  Function| No |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   | Indicates the object returned when a request is successful. If the request fails, it is left empty. |  Object  | 
| Location | Domain name for public network access of the created Object |String|
| Bucket |The target Bucket for multipart upload |String|
| Key|Object name |String|
|ETag | The SHA-1 algorithm check value of the file |String|


#### Progress callback parameters

| Parameter Name | Description | Type |  
|--------|---------|--------|
| SliceSize | Indicates the size of part |String| 
| PartNumber |No. of parts uploaded successfully |Number| 
| FileSize | Total size of the file |Number|


###  Slice Copy File

#### Feature description

This API (Slice Copy File) is used to copy a file from the source path to the destination path. In the process of copying, file meta-attributes and ACLs can be modified. You can use this API to move or rename a file, modify file attributes and create a copy.

#### Method prototype

Call Slice Copy File:

```js
cos.sliceCopyFile({
    Bucket: 'STRING_VALUE',                               /* Required */
    Region: 'STRING_VALUE',                               /* Required */
    Key: 'STRING_VALUE',                                  /* Required */
    CopySource: 'STRING_VALUE', 			  /* Required */
    SliceSize: 'NUMBER_VALUE',                            /* Not required */
    onProgress:function (progressData) {                  /* Not required */
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
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224) |String|Yes |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String | Yes |
| CopySource | The path of source file URL. You can specify the history version with the versionid sub-resource | String | Yes |
| ChunkSize | Indicates the size of each part for multipart copy, which defaults to 1048576 (1 MB) | Number | No |
| SliceSize | Indicates the file size for multipart copy, which defaults to 5 GB | Number | No |
| onProgress | Progress callback function. Callback is an object which includes progress information | Function | No |


#### Callback function description

```js
function(err, data) { ... }
```
#### Callback parameter description

| Parameter Name | Description | Type |
|--------|---------|--------|
| err | Indicates the object returned when a request fails, including network error and business error. If the request is successful, it is left empty. [Error Code Document](https://cloud.tencent.com/document/product/436/7730)  |  Object  |
| data | Indicates the object returned when a request is successful. If the request fails, it is left empty. | Object|
| Location | Domain name for public network access of the created Object | String |
| Bucket | The target Bucket for multipart upload | String |
| Key | Indicates the object key (object name), which is the unique identifier of the object in the bucket. [Object key description](https://cloud.tencent.com/document/product/436/13324) | String |
| ETag | The MD5 algorithm check value of the file | String |

