> For more information on the definitions of SecretId, SecretKey, Bucket, and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

Link to Node.js SDK github: [tencentyun/cos-nodejs-sdk-v5](https://github.com/tencentyun/cos-nodejs-sdk-v5)

## Service Operation

### Get Service

#### Feature description

Get Service API is used to obtain the list of all Buckets under the current account. This API requires Authorization signature for verification and can only obtain the Bucket list under the account to which the AccessID in signature belongs.

#### Method Prototype

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

#### Operation Parameter Description

* **No special parameters** 

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| Owner |Information of the Bucket owner |Object|
| uin |UIN of the Bucket owner |String|	
| Buckets |Information of the Bucket lists returned this time |Array|
| Name|Bucket Name |String|
| CreateDate |Bucket creation time, in ISO8601 format |String|

## Bucket Operations

### Head Bucket

#### Feature description

Head Bucket request is used to determine whether the Bucket and the permission to access the Bucket exist. Head and Read have the same permission.

#### Method Prototype

Call Head Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/* Required  */
	Region : 'STRING_VALUE'		/*  Required */
};

cos.headBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it failed, leave it empty |  Object  | 
| BucketExist|Whether a Bucket exists |Boolean| 
|BucketAuth |Whether a user has the Bucket permission |Boolean| 


###  Get Bucket

#### Feature description 

Get Bucket request is equivalent to List Object request. It is used to list partial or all of the Objects under the Bucket. Read permission is required to initiate this request.

#### Method Prototype

Call Get Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required  */
	Region : 'STRING_VALUE',	/*  Required  */
	Prefix : 'STRING_VALUE',	/*  Not required  */
	Delimiter : 'STRING_VALUE', /*  Not required  */
	Marker : 'STRING_VALUE',	/*  Not required  */
	MaxKeys : 'STRING_VALUE',	/* Not required  */
	EncodingType : 'STRING_VALUE',	/*  Not required  */
};

cos.getBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|
|   Prefix |Prefix match, used to specify the prefix address of the returned object key | String |No |
|   Delimiter |Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path |   String|No |
|   Marker |Entries are listed using UTF-8 binary order by default, starting from the marker |  String|No |
|   MaxKeys |Maximum number of entries returned at a time. Default is 1,000 |  String| No |
|   EncodingType |The encoding method of the returned value |  String|No |



#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|   CommonPrefixes |The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix |   Array| 
|   Prefix |Prefix match, used to specify the prefix address of the returned object key | String |No |
|   Name |Bucket Name |  String| 
|   Prefix | Prefix of an object key | String| No |
|   Marker |Entries are listed using UTF-8 binary order by default, starting from the marker | String | 
|   MaxKeys |Maximum number of entries returned at a time |  String|   
|   IsTruncated |Indicate whether the returned entry is truncated. Value: 'true' or 'false' |  String| 
|   NextMarker |If the returned entry is truncated, NextMarker represents the starting point of the next entry |  String| 
|   Encoding-Type |Encoding type of Delimiter, used for Marker, Prefix, NextMarker, Key |  String| 
|   Contents |Metadata information |   Array|  
|   ETag |SHA-1 algorithm check value for the file |  String| 
|   Size |File size (in bytes) |  String| 
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |
|   LastModified |Last modified time of the object |   String| 
|   Owner |Information of the Bucket owner |   Object| 
|   ID |Bucket Owner's UID |   String|  



###  Put Bucket

#### Feature description

Put Bucket request is used to create a Bucket under the specified account.

#### Method Prototype

Call Put Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required */
	Region : 'STRING_VALUE',	/*  Required  */
	ACL : 'STRING_VALUE',	/*  Not required  */
	GrantRead : 'STRING_VALUE', /*  Not required  */
	GrantWrite : 'STRING_VALUE',	/*  Not required  */
	GrantFullControl : 'STRING_VALUE'	/*  Not required  */
};

cos.putBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|
| ACL |Allow users to define file permissions. Valid values: private, public-read, public-read-write. Default value is private. | String| No |
| GrantRead |Grant read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". | String| No |
|GrantWrite |Grant write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". | String| No |
| GrantFullControl | Grant read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". | String| No |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| Location|Operation address of Bucket after it is created successfully |String| 

###  Delete Bucket

#### Feature description

Delete Bucket request is used to delete a Bucket under the specified account. The Bucket must be empty before it can be deleted.

#### Method Prototype

 Call Delete Bucket:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required  */
	Region : 'STRING_VALUE'		/*  Required  */
};

cos.deleteBucket(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| DeleteBucketSuccess| Whether deletion is successful |Boolean| 


###  Get Bucket ACL

#### Feature description

This API is used to read the ACL of a Bucket. Only the Bucket owner is allowed to perform the action.

#### Method Prototype

Call Get Bucket ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required  */
	Region : 'STRING_VALUE'		/*  Required  */
};

cos.getBucketAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| Owner |Owner of the identified resources |  Object|
|uin |QQ number of the user |  String|    
| AccessControlList | Information of authorized user and permissions |    Object|   
|Grant |Detailed authorized information |  Array| 
| Permission |Permission information. Enumerated values: READ, WRITE, FULL_CONTROL |   String| 
|Grantee |Resource information of the authorized user |  Object| 
| uin |QQ number of the authorized user or 'anonymous' |  String| 
| Subacount |QQ number of the sub-account |   String| 


### Put Bucket ACL

#### Feature description

This API is used to Write ACL for a Bucket. Importing a new ACL using Put Bucket ACL operation will overwrite the existing ACL. Only the owner is allowed to perform the operation.

#### Method Prototype

Call Put Bucket ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',			/*  Required  */
	Region : 'STRING_VALUE',			/*  Required  */
	ACL : 'STRING_VALUE',				/*  Not required  */
	GrantRead : 'STRING_VALUE', 		/*  Not required  */
	GrantWrite : 'STRING_VALUE',		/*  Not required  */
	GrantFullControl : 'STRING_VALUE'	/*  Not required  */
};

cos.putBucketAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|
|   ACL |Allow users to define file permissions. Valid values: private, public-read. Default value: private |   String| No |
|   GrantRead |Grant read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". |   String| No |
|   GrantWrite |Grant write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". |   String| No |
|   GrantFullControl | Grant read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". |    String| No |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|BucketGrantSuccess | Whether authorization is successful |Boolean| 


###  Get Bucket CORS

#### Feature description

Get Bucket CORS is used to read cross-domain access configurations.

#### Method Prototype

Call Get Bucket CORS:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required */
	Region : 'STRING_VALUE'		/*  Required  */
};

cos.getBucketCors(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes|

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|CORSRule |A collection of configurations |Array| 
| AllowedMethod | Allowed HTTP operations. Enumerated values: Get, Put, Head, Post, Delete |Array| 
| AllowedOrigin| Allowed access source. The wildcard "*" is supported |Array| 
| AllowedHeader | When sending an OPTIONS request, notify the server end about which custom HTTP request headers are allowed to be used by subsequent requests |Array| 
| ExposeHeader|Configure the custom header information that can be received by the browser from the server end |Array| 
|MaxAgeSeconds | Configure the valid period of the results obtained by OPTIONS request |String|
| ID|Rule name |String| 


### Put Bucket CORS

#### Feature description

Put Bucket CORS is used to read and write cross-domain access configurations.

#### Method Prototype

Call Put Bucket CORS:

```js

var params = {
	Bucket : 'STRING_VALUE',		/*  Required  */
	Region : 'STRING_VALUE',		/*  Required  */
	CORSRules : [
		{
			ID : 'STRING_VALUE',	/*  Not required  */
			AllowedMethods: [ 		/* Required */
			  'STRING_VALUE',
			  ...
			],
			AllowedOrigins: [		 /*  Required */
			  'STRING_VALUE',
			  ...
			],
			AllowedHeaders: [		/*  Not required */
			  'STRING_VALUE',
			  ...
			],
			ExposeHeaders: [		/*  Not required  */
				'STRING_VALUE',
				...
			],
			MaxAgeSeconds: 'STRING_VALUE'	/*  Not required  */
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

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|   CORSRules |A collection of cross-origin rules |  Array|No |
|   ID |Rule name |   String|No |
|   AllowedMethods | Allowed HTTP operations. Enumerated values: Get, Put, Head, Post, Delete |   Array|Yes |
|   AllowedOrigins | Allowed access source. The wildcard "*" is supported. The protocol, port and domain must be consistent |  Array|Yes |
|   AllowedHeaders | When sending an OPTIONS request, notify the server end about which custom HTTP request headers are allowed to be used by subsequent requests. The wildcard "*" is supported |  Array|No |
|   ExposeHeaders | Configure the custom header information that can be received by the browser from the server end |  Array|No |
|   MaxAgeSeconds | Configure the valid period of the results obtained by OPTIONS request |   String|No |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| PutBucketCorsSucesss | Whether Bucket CORS is configured successfully |Boolean|


###  Delete Bucket CORS

#### Feature description

Delete Bucket CORS is used to delete cross-domain access configurations.

#### Method Prototype

Call Delete Bucket CORS:

```js

var params = {
	Bucket : 'STRING_VALUE',		/*  Required  */
	Region : 'STRING_VALUE'			/*  Required  */
};

cos.deleteBucketCors(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| DeleteBucketCorsSuccess | Whether Bucket CORS is deleted successfully |Boolean|  


### Get Bucket Location

#### Feature description

Get Bucket Location is used to obtain the region information of the Bucket. Only the Bucket owner is allowed to read the information.

#### Method Prototype

Call Get Bucket Location:

```js

var params = {
	Bucket : 'STRING_VALUE',		/*  Required */
	Region : 'STRING_VALUE'			/*  Required  */
};

cos.getBucketLocation(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| LocationConstraint | Region where the Bucket resides. Enumerated values: china-east, china-south, china-north, china-west, singapore |String|  


### Get Bucket Tagging

#### Feature description

Get Bucket Tagging is used to obtain tags of a specified Bucket.

#### Method Prototype
Call Get Bucket Tagging:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required  */
	Region : 'STRING_VALUE'		/*  Required */
};

cos.getBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| Tags  |A collection of Bucket tags | Array |
| Key  |Type name of Tag | String | 
| Value |Value of Tag |  String |


###  Put Bucket Tagging

#### Feature description

Put Bucket Tagging is used to tag a specified Bucket.

#### Operation Parameter Description

 Call Put Bucket Tagging:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required  */
	Region : 'STRING_VALUE',	/* Required  */
	Tags :  [
		{
			Key : 'key1',		/*  Required  */
			Value : 'value1'	/*  Required  */
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

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
| Tags  |A collection of Bucket tags | Array |Yes |
| Key  |Type name of Tag | String |Yes |
| Value |Value of Tag |  String |Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| PutBucketTaggingSuccess |Whether Tag is configured successfully |Boolean|	


### Delete Bucket Tagging

#### Feature description

Delete Bucket Tagging is used to delete tags of a specified Bucket.

#### Method Prototype

Call Delete Bucket Tagging:

```js

var params = {
	Bucket : 'STRING_VALUE',	/*  Required  */
	Region : 'STRING_VALUE'		/*  Required  */
};

cos.deleteBucketTagging(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|DeleteBucketTaggingSuccess |Whether Bukcet tag is deleted successfully |Boolean|	


## Object Operations
### Head Object

#### Feature description

Head Object request is used to retrieve the metadata of corresponding Object. Head has the same permissions as those of Get.

#### Method Prototype
Call Head Object:

```js

var params = {
	Bucket : 'STRING_VALUE',		/*  Required  */
	Region : 'STRING_VALUE',		/*  Required  */
	Key : 'STRING_VALUE',			/*  Required  */
	IfModifiedSince : 'STRING_VALUE'	/*  Not required  */
};

cos.headObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
| Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
| IfModifiedSince |If Object is modified after the specified time, the Object meta information is returned |String|No |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| x-cos-object-type |Indicate whether the Object is appendable for upload. Enumerated values: normal or appendable |  String|  	
|   x-cos-storage-class |Storage class of an Object. Enumerated values: Standard, Standard_IA |  String|  
|   x-cos-meta- *   |User-defined metadata |  String| 
|   NotModified |If IfModifiedSince is used for request and the file is not modified, the value is true |  Boolean| 


### Get Object

#### Feature description

Delete Object request is used to download a file (Object) locally. This action requires that the user has the read permission for the target Object or the read permission for the target Object has been made available for everyone (public-read).

#### Method Prototype

Call Get Object:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Key : 'STRING_VALUE',							/*  Required  */
	ResponseContentType : 'STRING_VALUE',			/*  Not required  */
	ResponseContentLanguage : 'STRING_VALUE',		/*  Not required  */
	ResponseExpires : 'STRING_VALUE',				/*  Not required  */
	ResponseCacheControl : 'STRING_VALUE',			/*  Not required  */
	ResponseContentDisposition : 'STRING_VALUE',	/*  Not required  */
	ResponseContentEncoding : 'STRING_VALUE',		/*  Not required  */
	Range : 'STRING_VALUE',							/*  Not required  */
	IfModifiedSince : 'STRING_VALUE',				/*  Not required  */
	Output : 'STRING_VALUE' || 'WRITE_STRING'		/*  Required  */
};

cos.getObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|  Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
|  ResponseContentType |Set the Content-Type parameter in the response header |  String|No |
|  ResponseContentLanguage |Set the Content-Language parameter in the response header |  String|No |
|  ResponseExpires | Set the Content-Expires parameter in the response header |  String|No |
|  ResponseCacheControl |Set the Cache-Control parameter in the response header |  String|No |
|  ResponseContentDisposition |Set the Content-Disposition parameter in the response header |  String|No |
|  ResponseContentEncoding |Set the Content-Encoding parameter in the response header |  String|No |
|  Range |The specified range of file download defined in RFC 2616 (in bytes) |  String|No |
|  IfModifiedSince |Return the contents of the file if the file is modified later than the specified time |  String|No |
|  Output |A file path that needs outputting or a write stream |   String / WriteStream|Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|   x-cos-object-type |Indicate whether the Object is appendable for upload. Enumerated values: normal or appendable |   String|  	
 |   x-cos-storage-class |Storage class of an Object. Enumerated values: Standard, Standard_IA |  String| 
 |   x-cos-meta- * |User-defined metadata |   String|  
 |   NotModified |If IfModifiedSince is used for request and the file is not modified, the value is true |  Boolean|  

### Put Object

#### Feature description

Put Object request is used to upload a file (Object) to the specified Bucket.

>**Note:**, Key (File name) should not end with `/`. Otherwise, it will be identified as a folder.

#### Method Prototype

Call Put Object:

```js
cos.putObject({
    Bucket : 'STRING_VALUE',                        /*  Required  */
    Region : 'STRING_VALUE',                        /*  Required  */
    Key : 'STRING_VALUE',                           /*  Required  */
    Body: fs.createReadStream('./a.zip'),           /*  Required  */
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

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
|   CacheControl |The caching policy defined in RFC 2616, which will be saved as Object metadata. |   String|No |
|   ContentDisposition |The file name defined in RFC 2616, which will be saved as Object metadata |   String|No |
|   ContentEncoding |The encoding format defined in RFC 2616, which is saved as Object metadata. |  String|No |
|   ContentLength |HTTP request content length defined in RFC 2616 (in bytes) |  String|Yes |
|   ContentType |The content type (MIME) defined in RFC 2616, which is saved as Object metadata |   String|No |
|   Expect |If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server |  String|No |
|   Expires |The expiration time defined in RFC 2616, which is saved as Object metadata |   String|No |
|   ContentSha1 |160-bit content SHA-1 algorithm check value defined in RFC 3174 |   String|No |
|   ACL |Allow users to define file permission. Valid value: private, public-read |   String|No |
|   GrantRead |Grant read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID" |  String|No |
|   GrantWrite |Grant write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID" |   String|No |
|   GrantFullControl |Grant read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID" |   String|No |
|   x-cos-meta- * |The header information allowed to be defined by users, which is returned as Object metadata. The size is limited to 2K. |    String|No |
|   Body |Input file path or file stream |   String/ Stream|Yes |
|   onProgress |Progress callback function. Callback is an object which includes progress information |   Function|No |



#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| ETag|MD5 algorithm check value for the returned file. ETag value can be used to check whether the Object content has changed |String|

###  Delete Object
#### Feature description

Delete Object request is used to delete a file (Object).

#### Method Prototype

Call Delete Object:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Key : 'STRING_VALUE'							/*  Required  */
};

cos.deleteObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|DeleteObjectSuccess|Whether the file is deleted successfully |Boolean|	
|BucketNotFound |If the specific Bucket is not found, the value is true |Boolean|


###  Options Object

#### Feature description

Options Object is used to implement a pre-request for cross-origin access. That is , an OPTIONS request is sent to the server to verify whether cross-domain operations are possible.

#### Method Prototype

Call Options Object:

```js

var params = {
	Bucket : 'STRING_VALUE',		/*  Required  */
	Region : 'STRING_VALUE',		/*  Required  */
	Key : 'STRING_VALUE',			/*  Required  */
	Origin : 'STRING_VALUE', 		/*  Required  */
	AccessControlRequestMethod : 'STRING_VALUE', 		/*  Required  */
	AccessControlRequestHeaders : 'STRING_VALUE'		/*  Not required  */
};

cos.optionsObject(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
|Origin |Simulate the domain from which the request for cross-origin access is sent |String|Yes |
|AccessControlRequestMethod|Simulate the HTTP method of the request for cross-origin access |String|Yes |
| AccessControlRequestHeaders |Simulate the header of the request for cross-origin access |String|Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|AccessControlAllowOrigin  |Simulate the domain from which the request for cross-origin access is sent. If the origin is not allowed, the header will not be returned |String |	
| AccessControlAllowMethods  |Simulate the HTTP method of the request for cross-origin access. If the method is not allowed, the header will not be returned |String |
| AccessControlAllowHeaders  |Simulate the header of the request for cross-origin access. If the simulation of any request header is not allowed, the header will not be returned |String |
| AccessControlExposeHeaders  |It is supported to return headers in cross-origin requests and headers are separated by commas |String |
| AccessControlMaxAge  | Configure the valid period of the results obtained by OPTIONS request |String |


### Get Object ACL

#### Feature description

Get Object ACL is used to read the Object ACL. Only the Object owner is allowed to perform the action.

#### Method Prototype

Call Get Object ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Key : 'STRING_VALUE'							/*  Required  */
};

cos.getObjectAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|   Owner |Owner of the identified resources |  Object|  
|   uin |QQ number of the user |  String|  
|   AccessControlList |About authorized users and their permissions |  Object|  
|   Grant |Detailed authorized information |  Array|  
|   Permission |Permission information. Enumerated values: READ, WRITE, FULL_CONTROL |  String| 
|   Grantee |Resource information of the authorized user |  Object|  
|   uin |QQ number of the authorized user or 'anonymous' |  String|  
|   Subacount |QQ number of the sub-account |   String|  


### Put Object ACL

#### Feature description

Put Object ACL is used to write ACL for an Object.

#### Method Prototype

 Call Put Object ACL:

```js

var params = {
	Bucket : 'STRING_VALUE',			/*  Required  */
	Region : 'STRING_VALUE',			/*  Required  */
	Key : 'STRING_VALUE',				/*  Required  */
	ACL : 'STRING_VALUE',				/*  Not required  */
	GrantRead : 'STRING_VALUE', 		/*  Not required  */
	GrantWrite : 'STRING_VALUE',		/*  Not required  */
	GrantFullControl : 'STRING_VALUE'	/*  Not required  */
};

cos.putObjectAcl(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
|ACL |Allow users to define file permissions. Valid values: private, public-read, public-read-write. Default value is private. |   String|No |
|   GrantRead |Grant read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". |  String|No |
  |   GrantWrite |Grant write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID". |  String|No |
|   GrantFullControl | Grant read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; When you need to authorize the root account, uin="RootAcountID". |  String|No |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  |


### Delete Multiple Object

#### Feature description

Delete Multiple Object request is used for batch deletion of files. A maximum of 1000 files are allowed to be deleted at a time. COS provides two modes for returned results: Verbose and Quiet. Verbose mode will return the result of deletion of each Object, while Quiet mode only returns the information of the Objects with an error.


#### Method Prototype

 Call Delete Multiple Object:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Quiet : 'BOOLEAN_VALUE',						/*  Not required  */
	Objects :  [
	    {
	        Key : 'STRING_VALUE'					/*  Required  */
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

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
| Quiet |Boolean. Indicate whether the Quiet mode is enabled. True means Quiet mode is enabled, and False means Verbose mode is enabled. Default is False. |Boolean|No |
| Objects |List of files to be deleted |Array| 否|
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|   Deleted |Indicate the information of Object that has been deleted successfully |  Array| 
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |
|   Error |Indicate the information of Object that failed to be deleted |  Array| 
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |
|   Code |Error code that failed to be deleted |  String|   
|   Message |Message indicating the deletion error |  String|  


## Multipart Upload Operations
### Initiate Multipart Upload

#### Feature description

Initiate Multipart Upload request is used for the initialization of multipart upload. After the execution of this request, Upload ID is returned for the subsequent Upload Part requests.

#### Method Prototype
 Call Initiate Multipart Upload:

```js
cos.multipartInit({
    Bucket : 'STRING_VALUE',						/*  Required  */
    Region : 'STRING_VALUE',						/*  Required  */
    Key : 'STRING_VALUE',							/*  Required  */
}, function(err, data) {
    if(err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|  Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes | 
|   CacheControl |The caching policy defined in RFC 2616, which will be saved as Object metadata. |  String|No |
|   ContentDisposition |The file name defined in RFC 2616, which will be saved as Object metadata |  String|No |
|   ContentEncoding |The encoding format defined in RFC 2616, which is saved as Object metadata. |   String|No |
|   ContentType |The content type (MIME) defined in RFC 2616, which is saved as Object metadata |  String|No |
|   Expires |The expiration time defined in RFC 2616, which is saved as Object metadata |  String|No |
|   ACL |Allow users to define file permission. Valid value: private, public-read |   String|No |
|   GrantRead |Grant read permission to the authorized user. Format: x-cos-grant-read: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID" |   String|No |
|   GrantWrite |Grant write permission to the authorized user. Format: x-cos-grant-write: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID" |   String|No |
|   GrantFullControl |Grant read and write permissions to the authorized user. Format: x-cos-grant-full-control: uin=" ",uin=" "<br> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID";<br>when you need to authorize the root account, uin="RootAcountID" |   String|No |
|   StorageClass |Set the storage class of Object. Enumerated values: Standard, Standard_IA, Nearline. Default is Standard (this is only supported for South China region) |  String|No |
|   x-cos-meta- * |The header information allowed to be defined by users, which is returned as Object metadata. The size is limited to 2 K. |  String|No |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| Bucket |The target Bucket for multipart upload |String| 
|Key |Object name |String| 
| UploadId |ID used in subsequent uploads |String| 

### Upload Part

#### Feature description

Upload Part request is used to implement the multipart upload after initialization. The allowed number of parts is limited to 10000, and the size of part should be between 1 MB and 5 GB. Upload Part should be used with partNumber and uploadID. partNumber is the part No. and supports out-of-order upload.

#### Method Prototype

Call Upload Part:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Key : 'STRING_VALUE',							/*  Required  */
	ContentLength : 'STRING_VALUE',					/*  Required  */
	Expect : 'STRING_VALUE',						/*  Not required  */
	ContentSha1 : 'STRING_VALUE',					/*  Not required  */
	PartNumber : 'STRING_VALUE',					/*  Required  */
	UploadId : 'STRING_VALUE',						/*  Required  */
};

cos.multipartUpload(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|  Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
| ContentLength |HTTP request content length defined in RFC 2616 (in bytes) |String|Yes |
| Expect |If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server |String|No |
| ContentSha1|160-bit content SHA-1 algorithm check value defined in RFC 3174 |String|No |
| PartNumber |Part number |String|Yes |
| UploadId |Upload task number |String|Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| ETag|ETag value of part, which is sha1 check value |String|


### Complete Multipart Upload

#### Feature description

Complete Multipart Upload is used to complete the entire multipart upload. You can use this API to complete the upload operation when you have uploaded all parts using Upload Parts. When using this API, you need to provide the PartNumber and ETag for every part in Body, to verify the accuracy of parts.

#### Method Prototype

Call Complete Multipart Upload:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Key : 'STRING_VALUE',							/*  Required  */
	UploadId : 'STRING_VALUE',						/*  Required  */
	Parts : [
		{
			PartNumber : 'STRING_VALUE',			/*  Required  */
			ETag : 'STRING_VALUE'					/*  Required  */
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

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|  Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
| UploadId |Upload task number |String|Yes |
|Parts |ETag information of a part |Array|Yes |
| PartNumber |Part number |String|Yes |
| ETag|ETag value of a part, which is sha1 check value. It must be enclosed in double quotes, such as: "3a0f1fd698c235af9cf098cb74aa25bc". |String|Yes |

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| Location|Domain name for public network access of the created Object |String| 
| Bucket |The target Bucket for multipart upload|String| 
|Key |Object name |String|  
|ETag |MD5 algorithm check value for the file |String| 


### List Parts

#### Feature description

List Parts is used to query the uploaded parts in a specific multipart upload process.

#### Method Prototype

Call List Parts:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Key : 'STRING_VALUE',							/*  Required  */
	UploadId : 'STRING_VALUE',						/*  Required  */
	EncodingType : 'STRING_VALUE',					/*  Not required  */
	MaxParts : 'STRING_VALUE',						/*  Not required  */
	PartNumberMarker : 'STRING_VALUE'				/*  Not required  */
};

cos.multipartListPart(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|  Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
|UploadId |Upload task number |String|Yes |
|EncodingType |The encoding method of the returned value |String|No |
| MaxParts |Maximum number of entries returned at a time. Default is 1,000 |String| No |
| PartNumberMarker |ntries are listed using UTF-8 binary order by default, starting from the marker |String| No |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|   Bucket |The target Bucket for multipart upload|  String|  
|   Encoding-type |The encoding method of the returned value |  String| 
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |
|   UploadID |The ID of current multipart upload |  String| 
|   Initiator |Indicate the information of the initiator of current upload. Child node includes UID |   Object|   
|   UID |Developer's APPID |  String| 
|   Owner |Indicate the information of the owner of these uploaded parts. Child node includes UID |  Object| 
|   UID |Owner's QQ Number |  String| 
|   StorageClass |The storage class of uploaded parts. Enumerated values: Standard, Standard_IA |  String|  
 |   PartNumberMarker |Entries are listed using UTF-8 binary order by default, starting from the marker |  String|    
  |   NextPartNumberMarker |If the returned entry is truncated, NextMarker represents the starting point of the next entry |  String|   
  |   MaxParts |Maximum number of entries returned at a time |  String|  
  |   IsTruncated |Indicate whether the returned entry is truncated. Value: 'true' or 'false' |   String| 
  |   Part |A collection of part information |  Array|  
 |   PartNumber |Part number |  String| 
 |   LastModified |Last modified time of the part |  String| 
 |   Etag |SHA-1 algorithm check value for the part |  String| 
|   Size |Part size (in bytes) |String| 


### Abort Multipart Upload

#### Feature description

Abort Multipart Upload is used to abort a multipart upload operation and delete parts that are already uploaded. When Abort Multipart Upload is called, the Upload Parts returns failure to any request that is using the Upload Parts.

#### Method Prototype
Call Abort Multipart Upload:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Key : 'STRING_VALUE',							/*  Required  */
	UploadId : 'STRING_VALUE'						/*  Required  */
};

cos.multipartAbort(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|  Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
| UploadId |Upload task number |String|Yes |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|MultipartAbortSuccess |Whether Multipart Abort is successful |Boolean| 


### List Multipart Uploads

#### Feature description

List Multiparts Uploads is used to query multipart upload operations that are still in process. Up to 1000 such operations can be listed each time.

#### Method Prototype

Call List Multipart Uploads:

```js

var params = {
	Bucket : 'STRING_VALUE',						/*  Required  */
	Region : 'STRING_VALUE',						/*  Required  */
	Delimiter : 'STRING_VALUE',						/*  Not required  */
	EncodingType : 'STRING_VALUE',					/*  Not required  */
	Prefix : 'STRING_VALUE',						/*  Not required  */
	MaxUploads : 'STRING_VALUE',					/*  Not required  */
	KeyMarker : 'STRING_VALUE',						/*  Not required  */
	UploadIdMarker : 'STRING_VALUE'					/*  Not required  */
};

cos.multipartList(params, function(err, data) {
	if(err) {
		console.log(err);
	} else {
		console.log(data);
	}
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
| Delimiter |Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path |   String|No |
|   EncodingType |The encoding method of the returned value |  String|No |
|   Prefix |Prefix match, used to specify the prefix address of the returned object key | String |No |
|   MaxUploads |Maximum number of entries returned at a time. Default is 1,000 |  String| No |
|   KeyMarker |Used together with upload-id-marker.<br><li>If upload-id-marker is not specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed.<br><li>If upload-id-marker is specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed,<br>and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. | String|No |
|   UploadIdMarker |Used together with key-marker.<br><li>If key-marker is not specified,<br> upload-id-marker will be ignored.<br><li> If key-marker is specified,<br> entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed,<br> and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. |   String|No |
</li>

#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
|   Bucket |The target Bucket for multipart upload|String|   
|   Encoding-type |The encoding method of the returned value |  String| 
|   KeyMarker |Entries will be listed starting from this key value |  String| 
|   UploadIdMarker |Entries will be listed starting from this UploadId value |  String| 
|   NextKeyMarker |If the returned entry is truncated, NextKeyMarker represents the starting point of the next entry |   String|  
|   NextUploadIdMarker |If the returned entry is truncated, UploadId represents the starting point of the next entry |   String|  
|   IsTruncated |Indicate whether the returned entry is truncated. Value: 'true' or 'false' |   String| 
|   delimiter |Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path. |   String| 
|   CommonPrefixs |The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix |  Array| 
|   Prefix |Prefix match, used to specify the prefix address of the returned object key | String |No |
|   Upload |A collection of Information about Upload |   Array| 
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |
|   UploadID |The ID of current multipart upload |  String| 
|   StorageClass |The storage class of uploaded parts. Enumerated values: Standard, Standard_IA |  String|   
|   Initiator |Indicate the information of the initiator of current upload. Child node includes UID |   Object|   
|   UID |Developer's APPID |   String|  
|   Owner |Indicate the information of the owner of these uploaded parts. Child node includes UID |  Object|  
|   UID |Owner's QQ Number |  String|   
|   Initiated |Start time of the multipart upload |  String| 


###  Slice Upload File

#### Feature description

Slice Upload File is used to upload a file in parts.

#### Method Prototype

Call Slice Upload File:

```js
var params = {
	Bucket: 'STRING_VALUE',	/*  Required  */
	Region: 'STRING_VALUE',	/*  Required  */
	Key: 'STRING_VALUE',	/*  Required  */
	FilePath: 'STRING_VALUE',	/*  Required  */
	SliceSize: 'STRING_VALUE',	/*  Not required  */
	AsyncLimit: 'NUMBER_VALUE',	/*  Not required  */
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

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes | 
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
|   Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
|   FilePath | Path to the local file |  String|Yes |
|   SliceSize |Part size |   String|No |
|   AsyncLimit |Number of parts uploaded concurrently |  String|No |
|   onHashProgress |Progress callback function to calculate a file's sha1 value. Callback is an object which includes progress information |  Function|No |
|   onProgress |Progress callback function. Callback is an object which includes progress information |  Function|No |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |  
|--------|---------|--------|
|err   |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |   
|data   |Object returned when a request is successful. If it fails, leave it empty |  Object  | 
| Location |Domain name for public network access of the created Object |String|
| Bucket |The target Bucket for multipart upload|String|
| Key|Object name |String|
|ETag |SHA-1 algorithm check value for the file |String|


#### Progress Callback Parameters

| Parameter Name | Description | Type |  
|--------|---------|--------|
| SliceSize |Part size |String| 
| PartNumber |Number of parts uploaded successfully |Number| 
| FileSize | Total file size |Number|


###  Slice Copy File

#### Feature description

Slice Copy File request is used to copy a file from source path to the destination path. In the process of copying, file meta-attributes and ACLs can be modified. Users can use this API to move or rename a file, modify file attributes and create a copy.

#### Method Prototype

Call Slice Copy File:

```js
cos.sliceCopyFile({
    Bucket: 'STRING_VALUE',                               /*  Required  */
    Region: 'STRING_VALUE',                               /*  Required  */
    Key: 'STRING_VALUE',                                  /*  Required  */
    CopySource: 'STRING_VALUE', 			  /*  Required  */
    SliceSize: 'NUMBER_VALUE',                            /*  Not required  */
    onProgress:function (progressData) {                  /*  Not required  */
        console.log(JSON.stringify(progressData));
    }
},function (err,data) {
    console.log(err || data);
});

```

#### Operation Parameter Description

| Parameter Name | Description | Type | Required |
|--------|---------|--------|--------|
| Bucket| Bucket Name. The bucket entered must be in a format of {name}-{appid} |   String|Yes |
| Region | The region where the Bucket resides. For enumeration values, please see [Bucket Region](https://cloud.tencent.com/document/product/436/6224)|String|Yes |
| Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |Yes |
| CopySource |The path of source file URL. You can specify the history version with the versionid sub-resource | String |Yes |
| ChunkSize |Indicates the size of each part for multipart copy, which defaults to 1048576 (1MB) | Number |No |
| SliceSize |Default size of a file using multipart copy is 5G | Number |No |
| onProgress |Progress callback function. Callback is an object which includes progress information | Function |No |


#### Callback Function Description

```js
function(err, data) { ... }
```
#### Callback Parameter Description

| Parameter Name | Description | Type |
|--------|---------|--------|
| err |Object returned when a request fails, including network error and business error. If the request is successful, leave it empty. [Error Code Documentation](https://cloud.tencent.com/document/product/436/7730)  |  Object  |
| data |Object returned when a request is successful. If it fails, leave it empty | Object|
| Location |Domain name for public network access of the created Object | String |
| Bucket |The target Bucket for multipart upload| String |
| Key | Object key is the unique identifier of the object in the bucket. [Object Key Description](https://cloud.tencent.com/document/product/436/13324) | String |
| ETag |MD5 algorithm check value for the file | String |

