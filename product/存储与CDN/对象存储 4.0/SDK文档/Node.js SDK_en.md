## Preparations for Development

### Acquiring SDK

You can download COS service of js sdk v4 version from  [https://github.com/tencentyun/cos-js-sdk-v4.git](https://github.com/tencentyun/cos-js-sdk-v4.git)

### Development Environment

1. SKD is usable on browsers that support HTML5.
2. Get your appid, bucket, secret_id and secret_key at https://console.qcloud.com/cos.
3. Set a CORS configuration on the bucket at https://console.qcloud.com/cos.


### Configuring SDK

Download the source code from github, load the cos-js-sdk-v4.js file in the dist directory, and then you can use SDK.

```javascript
<script type="text/javascript" src="cos-js-sdk-v4.js"></script>

```

### Initialization

```js

	//Initialization logic
	//Note: You should set a CORS configuration on the Bucket in console.qcloud.com/cos before enabling JS-SDK.
	var cos = new CosCloud({
		appid: appid,// APPID (required)
		bucket: bucket,//bucketName (required)
		region: 'sh',//Region (required): gz for South China, sh for East China, and tj for North China
		getAppSign: function (callback) {//Get signatures (required)

			//How to get signatures

			//1. By building an authentication server to construct your own request parameters. This method is suitable for online businesses, which is of good security and will not expose your private key
			//Remember to call the callback after getting the signature
			/**
			 $.ajax('SIGN_URL').done(function (data) {
				var sig = data.sign;
				callback(sig);
			});
			 **/

			//2. By calculating the signature at the frontend of the browser, provided that you have your accessKey and secretKey. This method is commonly used in debugging
			//Remember to call the callback after getting the signature
			//var res = getAuth(); //This function is implemented using a signature algorithm
			//callback(res);


			//3. By using the signature string calculated by someone else. This method is commonly used in debugging
			//Remember to call the callback after getting the signature
			//callback('YOUR_SIGN_STR')
			//

		},
		getAppSignOnce: function (callback) {//One-time signature is required. You can refer to the above note
			//Enter the logic to get one-time signature
		}
	});


```


#### Initialization Parameter

| **Parameter Name**        | **Type**   | **Required** | **Default Value** | **Description**                                 |
| -------------- | -------- | -------- | ------- | ---------------------------------------- |
| appid          | int      | Yes        | None       | appid                                    |
| bucket         | String   | Yes        | None       | bucket name. To create a bucket, refer to [Create Bucket](https://www.qcloud.com/document/product/436/6232) |
| region         | String   | Yes        | 'gz'    | Region (required): gz for South China, sh for East China, and tj for North China            |
| getAppSign     | Function | Yes        | None       | Get the function for multiple-time signature. It is recommended to get the signature string from the server                  |
|getAppSignOnce     | Function | Yes        | None       | Get the function for one-time signature. It is recommended to get the signature string from the server                  |


#### Returned Result

Returned value: cos object, which can used for built-in API calls such as uploadFile and deleteFile after initialization.

## File-related Operations

### Uploading an Ordinary File

API Description: It is used to upload files smaller than 20 MB and get file url. If the file is greater than 20 M, the multipart upload API will be called within this API.

#### Method Prototype

```js

CosCloud.prototype.uploadFile(successCallBack, errorCallBack, progressCallBack, bucket, path, file, insertOnly);

```

#### Parameter Description

| **Parameter Name**          | **Type**   | **Required** | **Default Value** | **Description**                            |
| ---------------- | -------- | -------- | ------- | ----------------------------------- |
| successCallBack  | Function | Yes        | None       | Callback for successful upload                             |
| errorCallBack    | Function | Yes        | None       | Callback for failed upload                             |
| progressCallBack | Function | Yes        | None       | Callback for upload progress, for example, for a 1M file, if 100kb has been uploaded, the callback will show 0.1  |
| bucket           | String   | Yes        | None       | bucket name                            |
| path             | String   | Yes        | None       | The path of the file on COS server                        |
| file             | File     | Yes        | None       | The object of the local file to be uploaded (binary data)                 |
| insertOnly       | Int      | No        | None       | 0: overwriting allowed ; 1: not allowed; other values shall be ignored |

#### Returned Result (json string)

| **Parameter Name**            | **Type** | **Required** | **Description**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | Yes          | Error code, 0 indicates success                  |
| message            | String | Yes          | Message                       |
| data               | Object | Yes          | Returned data                       |
| data.access_url    | String | Yes          |  Generated CDN download url of the file              |
| data.source_url    | String | Yes          | Generated COS origin server url of the file              |
| data.url           | String | Yes          | URL for file operation                   |
| data.resource_path | String | Yes          | Resource path. Format: /appid/bucket/xxx |

#### Example

```js

	var myFolder = '/111/';//Directory to be operated
	var successCallBack = function (result) {
		$("#result").val(JSON.stringify(result));
	};

	var errorCallBack = function (result) {
		result = result || {};
		$("#result").val(result.responseText || 'error');
	};

	var progressCallBack = function(curr){
		$("#result").val('uploading... curr progress is '+curr);
	};

	$('#js-file').off('change').on('change', function (e) {
		var file = e.target.files[0];
		cos.uploadFile(successCallBack, errorCallBack, progressCallBack, bucket, myFolder+file.name, file, 0);
		return false;
	});


```

### Uploading a Large File in Multipart Mode

API Description: It is used to upload files larger than 20MB and get file url.

#### Method Prototype

```js

CosCloud.prototype.sliceUploadFile(successCallBack, errorCallBack, progressCallBack, bucket, path, file, insertOnly);

```

#### Parameter Description

| **Parameter Name**          | **Type**   | **Required** | **Default Value** | **Description**                            |
| ---------------- | -------- | -------- | ------- | ----------------------------------- |
| successCallBack  | Function | Yes        | None       | Callback for successful upload                             |
| errorCallBack    | Function | Yes        | None       | Callback for failed upload                             |
| progressCallBack | Function | Yes        | None       | Callback for upload progress, for example, for a 1M file, if 100kb has been uploaded, the callback will show 0.1  |
| bucket           | String   | Yes        | None       | bucket name                            |
| path             | String   | Yes        | None       | The path of the file on COS server                        |
| file             | File     | Yes        | None       | The object of the local file to be uploaded (binary data)                 |
| insertOnly       | Int      | No        | None       | 0: overwriting allowed ; 1: not allowed; other values shall be ignored |

#### Returned Result (json string)

Note: Multiple APIs are involved when uploading large files. The following callbacks are triggered by the successful upload of the last part of the file

| **Parameter Name**            | **Type** | **Required** | **Description**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | Yes          | Error code, 0 indicates success                  |
| message            | String | Yes          | Message                       |
| data               | Object | Yes          | Returned data                       |
| data.access_url    | String | Yes          |  Generated CDN download url of the file              |
| data.source_url    | String | Yes          | Generated COS origin server url of the file              |
| data.url           | String | Yes          | URL for file operation                   |
| data.resource_path | String | Yes          | Resource path. Format: /appid/bucket/xxx |

#### Example

```js

	var myFolder = '/111/';//Directory to be operated
	var successCallBack = function (result) {
		$("#result").val(JSON.stringify(result));
	};

	var errorCallBack = function (result) {
		result = result || {};
		$("#result").val(result.responseText || 'error');
	};

	var progressCallBack = function(curr){
		$("#result").val('uploading... curr progress is '+curr);
	};

	$('#js-file').off('change').on('change', function (e) {
		var file = e.target.files[0];
		//You can directly call uploadFile for large files.
		cos.uploadFile(successCallBack, errorCallBack, progressCallBack, bucket, myFolder+file.name, file, 0);
		//You can also use sliceUploadFile. Either is OK
		//cos.sliceUploadFile(successCallBack, errorCallBack, progressCallBack, bucket, myFolder+file.name, file, 0);
		return false;
	});


```

### Deleting a File

API Description: It is used to delete files

#### Method Prototype

```js
CosCloud.prototype.deleteFile(successCallBack, errorCallBack, bucket, path);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**     |
| --------------- | -------- | -------- | ------- | ------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation      |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation      |
| bucket          | String   | Yes        | None       | bucket name     |
| path            | String   | Yes        | None       | The path of the file on COS server |


#### Returned Result (json string)

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code, 0 indicates success |
| message | String | Yes          | Message      |


#### Example

```js

	//Deleting a File
	$('#deleteFile').on('click', function () {
		var myFile = myFolder+'2.txt';//Enter your existing file
		cos.deleteFile(successCallBack, errorCallBack, bucket, myFile);
	});

```

### Getting File Attributes

API Description: It is used to query file attributes.

#### Method Prototype

```js
CosCloud.prototype.getFileStat(successCallBack, errorCallBack, bucket, path);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**     |
| --------------- | -------- | -------- | ------- | ------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation      |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation      |
| bucket          | String   | Yes        | None       | bucket name     |
| path            | String   | Yes        | None       | The path of the file on COS server |


#### Returned Result (json string):

| **Parameter Name**             | **Type** | **Required** | **Description**                                 |
| ------------------- | ------ | ---------- | ---------------------------------------- |
| code                | Int    | Yes          | Error code, 0 indicates success                                |
| message             | String | Yes          | Error message                                      |
| data                | Object | Yes          | File attribute                                   |
| data.name           | String | Yes          | File/Directory name                                   |
| data.biz_attr       | String | Yes          | File attribute, maintained by a business server                               |
| data.ctime          | String | Yes          | File creation time, unix timestamp                          |
| data.mtime          | String | Yes          | File modification time, unix timestamp                          |
| data.filesize       | Int    | Yes          | File size                                     |
| data.filelen        | Int    | Yes          | Transmitted size of a file                                   |
| data.sha            | String | Yes          | File sha                                  |
| data.access_url     | String | Yes          | Generated download url of the file              |
| data.authority      | String | No          | eInvalid, eWRPrivate, eWPrivateRPublic. File and bucket may have different permission types. If you want to revoke the permission of a file, directly assign eInvalid and the permission of this file will be the same as that of the bucket |
| data.custom_headers | String | No          | Custom header object                              |


#### Example

```js

	//Getting File Attributes
	$('#getFileStat').on('click', function () {
		var myFile = myFolder+'2.txt';//Enter your existing file
		cos.getFileStat(successCallBack, errorCallBack, bucket, myFile);
	});

```

### Updating File Attributes

API Description: It is used to update file attributes.

#### Method Prototype

```js
CosCloud.prototype.updateFile(successCallBack, errorCallBack, bucket, path, bizAttr);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**     |
| --------------- | -------- | -------- | ------- | ------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation      |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation      |
| bucket          | String   | Yes        | None       | bucket name     |
| path            | String   | Yes        | None       | The path of the file on COS server |
| bizAttr         | String   | Yes        | No       | Custom attribute of the file     |


#### Returned Result (json string):

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code, 0 indicates success |
| message | String | Yes          | Error message      |

#### Example

```js

	//Updating File Attributes
	$('#updateFile').on('click', function () {
		var myFile = myFolder+'2.txt';//Enter your existing file
		cos.updateFile(successCallBack, errorCallBack, bucket, myFile, 'my new file attr');
	});

```

### Copying Files

API Description: It is used to copy a file to a different path.

#### Method Prototype

```js
CosCloud.prototype.copyFile(successCallBack, errorCallBack, bucket, path, destPath, overWrite);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**              |
| --------------- | -------- | -------- | ------- | --------------------- |
| successCallBack | Function | Yes        | None       | Callback for successful operation               |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation               |
| bucket          | String   | Yes        | None       | bucket name              |
| path            | String   | Yes        | None       | The path of the file to copy on COS server     |
| destPath        | String   | Yes        | None       | The destination path of the file to copy               |
| overWrite       | Int      | Yes        | None       | Whether overwriting a file with the same name is allowed. 0: Not Allowed; 1: Allowed |


#### Returned Result (json string):

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code, 0 indicates success |
| message | String | Yes          | Error message      |

#### Example

```js

	//Copy a file from the source path to a new path
	$('#copyFile').on('click', function () {

		var myFile = '111/2.txt';//Enter your existing file

		//Pay attention to the destination path. If you enter 333/2.txt here, the file will be copied to 111/333/2.txt
		//If you enter 333/2.txt, the file will be copied to 333/2.txt under the bucket root directory
		var newFile = '/333/2.txt';
		var overWrite = 1;//0: Not Overwrite; 1: Overwrite
		cos.copyFile(successCallBack, errorCallBack, bucket, myFile, newFile, overWrite);
	});

```

### Moving a File

API Description: It is used to move (cut) a file to a different path. If the designation path is the current path, and a new name is specified for the file, it is equivalent to renaming the file.

#### Method Prototype

```js
CosCloud.prototype.moveFile(successCallBack, errorCallBack, bucket, path, destPath, overWrite);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**              |
| --------------- | -------- | -------- | ------- | --------------------- |
| successCallBack | Function | Yes        | None       | Callback for successful operation               |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation               |
| bucket          | String   | Yes        | None       | bucket name              |
| path            | String   | Yes        | None       | The path of the file to move on COS server     |
| destPath        | String   | Yes        | None       | The destination path of the file to move               |
| overWrite       | Int      | Yes        | None       | Whether overwriting a file with the same name is allowed. 0: Not Allowed; 1: Allowed |


#### Returned Result (json string):

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code, 0 indicates success |
| message | String | Yes          | Error message      |

#### Example

```js

	//Move a file from the source path to a new path. If the designation path is the current path, and a new name is specified for the file, it is equivalent to renaming the file.
	//If a file is moved to a new directory, it is equivalent to cutting the current file and pasting it into a new directory
	$('#moveFile').on('click', function () {

		var myFile = '/111/2.txt';//Enter your existing file

		//Pay attention to the destination path. If you enter 333/2.txt here, the file will be moved to 111/333/2.txt
		//If you enter 333/2.txt, the file will be moved to 333/2.txt under the bucket root directory
		//If you enter /111/3.txt, it is equivalent to changing the name of 2.txt to 3.txt
		var newFile = '/333/2.txt';
		var overWrite = 1;//0: Not Overwrite; 1: Overwrite
		cos.moveFile(successCallBack, errorCallBack, bucket, myFile, newFile, overWrite);
	});

```

## Folder (Directory) Operations


### Adding a Folder

API Description: It is used to add a specified folder.

#### Method Prototype

```js
CosCloud.prototype.createFolder(successCallBack, errorCallBack, bucket, path);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation            |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation            |
| bucket          | String   | Yes        | None       | bucket name           |
| path            | String   | Yes        | None       | The path of the folder to operate on COS server |


#### Returned Result (json string):

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code, 0 indicates success |
| message | String | Yes          | Error message      |

#### Example

```js

	$('#createFolder').on('click', function () {
		var newFolder = '/333/';//Enter the name of the folder to be created, and remember to enclose it in forward slashes
		cos.createFolder(successCallBack, errorCallBack, bucket, newFolder);
	});


```

### Deleting a Folder

API Description: It is used to delete a specified folder.

#### Method Prototype

```js
CosCloud.prototype.deleteFolder(successCallBack, errorCallBack, bucket, path);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation            |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation            |
| bucket          | String   | Yes        | None       | bucket name           |
| path            | String   | Yes        | None       | The path of the folder to operate on COS server |


#### Returned Result (json string):

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code, 0 indicates success |
| message | String | Yes          | Error message      |

#### Example

```js

	//Deleting a Folder
	$('#deleteFolder').on('click', function () {
		var newFolder = '/333/';//Enter the name of the folder to be deleted, and remember to enclose it in forward slashes
		cos.deleteFolder(successCallBack, errorCallBack, bucket, newFolder);
	});

```

### Getting Folder Attributes

API Description: It is used to get specified folder attributes.

#### Method Prototype

```js
CosCloud.prototype.getFolderStat(successCallBack, errorCallBack, bucket, path);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation            |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation            |
| bucket          | String   | Yes        | None       | bucket name           |
| path            | String   | Yes        | None       | The path of the folder to operate on COS server |


#### Returned Result (json string):

| **Parameter Name**       | **Type** | **Required** | **Description**   |
| ------------- | ------ | ---------- | ---------- |
| code          | Int    | Yes          | Error code, 0 indicates success  |
| message       | String | Yes          | Error message       |
| data          | Object | Yes          | Folder attribute object  |
| data.biz_attr | String | Yes          | Folder attribute string|


#### Example

```js

	//Getting Folder Attributes
	$('#getFolderStat').on('click', function () {
		cos.getFolderStat(successCallBack, errorCallBack, bucket, '/333/');
	});

```

### Updating Folder Attributes

API Description: It is used to update specified folder attributes.

#### Method Prototype

```js
CosCloud.prototype.updateFolder(successCallBack, errorCallBack, bucket, path, bizAttr);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation            |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation            |
| bucket          | String   | Yes        | None       | bucket name           |
| path            | String   | Yes        | None       | The path of the folder to operate on COS server |
| bizAttr         | String   | Yes        | None       | New attribute             |


#### Returned Result (json string):

| **Parameter Name** | **Type** | **Required** | ** Description**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | Yes          | Error code, 0 indicates success |
| message | String | Yes          | Error message      |


#### Example

```js

	//Updating Folder Attributes
	$('#updateFolder').on('click', function () {
		cos.updateFolder(successCallBack, errorCallBack, bucket, '/333/', 'new attr');
	});

```

### Getting Lists in the Folder

API Description: It is used to get specified file lists in the folder.

#### Method Prototype

```js
CosCloud.prototype.getFolderList(successCallBack, errorCallBack, bucket, path);
```

#### Parameter Description

| **Parameter Name**         | **Type**   | **Required** | **Default Value** | **Description**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | Yes        | None       | Callback for successful operation            |
| errorCallBack   | Function | Yes        | None       | Callback for failed operation            |
| bucket          | String   | Yes        | None       | bucket name           |
| path            | String   | Yes        | None       | The path of the folder to operate on COS server |


#### Returned Result (json string):

| **Parameter Name**               | **Type** | **Required**   | **Description**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
| code                  | Int    | Yes            | API error code, 0 indicates success                            |
| message               | String | Yes            | Error message                                     |
| data                  | Array  | Yes            | Returned data                                     |
| data.listover         | Bool   | Yes            | Indicate whether it can perform page forward/back                          |
| data.context          | String | Yes            | Transparently transmitted field. If you want to query the first page, an empty string should be passed. To turn pages, please transmit context in the returned values of the previous page to the parameters in a transparent way. "order" is used to specify the page-turning order. If "order" = 0, a page-forward action will be performed from the current page; if "order" = 1, a page-back action will be performed from the current page |
| data.infos            | Array  | Yes            | File/Directory collection can be empty                             |
| data.infos.name       | String | Yes            | File/Directory name                                   |
| data.infos.biz_attr   | String | Yes         | Directory/File attribute, maintained by a business server                            |
| data.infos.ctime      | String | Yes            | Directory/File creation time, unix timestamp                       |
| data.infos.mtime      | String | Yes            | Directory/File modification time, unix timestamp                       |
| data.infos.filesize   | Int    | No (return when it's a file) | File size                                     |
| data.infos.filelen    | Int    | No (return when it's a file) | Transmitted size of a file (you can get the transmission progress by comparing it with the file size)           |
| data.infos.sha        | String | No (return when it's a file) | File sha                                    |
| data.infos.access_url | String | No (return when it's a file) | Generated Download url of the file                               |
| data.infos.authority  | String | No            | eInvalid, eWRPrivate, eWPrivateRPublic. File and bucket may have different permission types. If you want to revoke the permission of a file, directly assign eInvalid and the permission of this file will be the same as that of the bucket |


#### Example

```js

	//Get the lists in the specified folder; 20 lists are returned at a time by default
	$('#getFolderList').on('click', function () {
		cos.getFolderList(successCallBack, errorCallBack, bucket, myFolder);
	});

```
