## 开发准备

### SDK 获取

COS 服务的 JS SDK V4 版本的 [GitHub 地址](https://github.com/tencentyun/cos-js-sdk-v4.git)。

### 开发环境

1. 使用 SDK 需要浏览器支持 HTML 5。
2. 请您登录 [腾讯云控制台](https://console.cloud.tencent.com/cos) 获取您的项目 ID（APPID），bucket，secret_id 和 secret_key。
3. 请您登录 [对象存储控制台](https://console.cloud.tencent.com/cos) 针对您要操作的 bucket 进行跨域（CORS）设置。

>?本版本 SDK 基于 JSON API 封装组成。

### SDK 配置

直接下载 github 上提供的源代码，使用 SDK 之前，加载 dist 目录里的 cos-js-sdk-v4.js 文件即可。

```javascript
<script type="text/javascript" src="cos-js-sdk-v4.js"></script>

```

### 初始化

```js

	//初始化逻辑
	//特别注意: JS-SDK使用之前请先到console.cloud.tencent.com/cos 对相应的Bucket进行跨域设置
	var cos = new CosCloud({
		appid: appid,// APPID 必填参数
		bucket: bucket,//bucketName 必填参数
		region: 'sh',//地域信息 必填参数 华南地区填gz 华东填sh 华北填tj
		getAppSign: function (callback) {//获取签名 必填参数

			//下面介绍获取签名的几种办法

			//1.搭建一个鉴权服务器，自己构造请求参数获取签名，推荐实际线上业务使用，优点是安全性好，不会暴露自己的私钥
			//拿到签名之后记得调用callback
			/**
			 $.ajax('SIGN_URL').done(function (data) {
				var sig = data.sign;
				callback(sig);
			});
			 **/

			//2.直接在浏览器前端计算签名，需要获取自己的accessKey和secretKey, 一般在调试阶段使用
			//拿到签名之后记得调用callback
			//var res = getAuth(); //这个函数自己根据签名算法实现
			//callback(res);


			//3.直接复用别人算好的签名字符串, 一般在调试阶段使用
			//拿到签名之后记得调用callback
			//callback('YOUR_SIGN_STR')
			//

		},
		getAppSignOnce: function (callback) {//单次签名，必填参数，参考上面的注释即可
			//填上获取单次签名的逻辑
		}
	});


```


#### 初始化参数说明

| **参数名**        | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------------- | -------- | -------- | ------- | ---------------------------------------- |
| appid          | int      | 是        | 无       | appid                                    |
| bucket         | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](https://cloud.tencent.com/document/product/436/6232) |
| region         | String   | 是        | 'gz'    | 地域信息，必填参数 华南地区填gz 华东填sh 华北填tj            |
| getAppSign     | Function | 是        | 无       | 获取多次签名的函数，建议从服务器端获取签名字符串                 |
| getAppSignOnce | Function | 是        | 无       | 获取单次签名的函数，建议从服务器端获取签名字符串                 |


#### 返回结果说明

返回值：cos object 对象，初始化之后可以用这个 cos object 对象进行内置接口调用例如 uploadFile，deleteFile 等。

## 文件操作

### 普通文件上传

接口说明：通常用于较小文件(一般小于20MB)的上传，可以通过此接口上传较小的文件并获得文件的url，如果文件大于20M则本接口内部会去调用分片上传接口。

#### 方法原型

```js

cos.uploadFile(successCallBack, errorCallBack, progressCallBack, bucket, path, file, insertOnly);

```

#### 参数说明

| **参数名**          | **类型**   | **是否必填** | **默认值** | **参数描述**                            |
| ---------------- | -------- | -------- | ------- | ----------------------------------- |
| successCallBack  | Function | 是        | 无       | 上传成功的回调                             |
| errorCallBack    | Function | 是        | 无       | 上传失败的回调                             |
| progressCallBack | Function | 是        | 无       | 上传过程进度的回调，比如文件1M已经上传了100K则会回调进度0.1  |
| bucket           | String   | 是        | 无       | bucket名称                            |
| path             | String   | 是        | 无       | 文件在COS服务端的路径                        |
| file             | File     | 是        | 无       | 本地要上传文件的文件对象（二进制数据）                 |


#### 返回结果说明（json字符串）

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 提示信息                       |
| data               | Object | 是          | 返回数据                       |
| data.access_url    | String | 是          | 生成的文件CDN下载url              |
| data.source_url    | String | 是          | 生成的文件COS源站url              |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

#### 示例

```js

	var myFolder = '/111/';//需要操作的目录
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

### 大文件分片上传

接口说明：通常用于较大文件(一般大于20MB)的上传，可以通过此接口大的文件并获得文件的url。

#### 方法原型

```js

cos.sliceUploadFile(successCallBack, errorCallBack, progressCallBack, bucket, path, file, insertOnly);

```

#### 参数说明

| **参数名**          | **类型**   | **是否必填** | **默认值** | **参数描述**                            |
| ---------------- | -------- | -------- | ------- | ----------------------------------- |
| successCallBack  | Function | 是        | 无       | 上传成功的回调                             |
| errorCallBack    | Function | 是        | 无       | 上传失败的回调                             |
| progressCallBack | Function | 是        | 无       | 上传过程进度的回调，比如文件1M已经上传了100K则会回调进度0.1  |
| bucket           | String   | 是        | 无       | bucket名称                            |
| path             | String   | 是        | 无       | 文件在COS服务端的路径                        |
| file             | File     | 是        | 无       | 本地要上传文件的文件对象（二进制数据）                 |


#### 返回结果说明(json字符串)

需要注意的是大文件上传会经多个接口处理，以下是最后一片上传成功才会触发的回调

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 提示信息                       |
| data               | Object | 是          | 返回数据                       |
| data.access_url    | String | 是          | 生成的文件CDN下载url              |
| data.source_url    | String | 是          | 生成的文件COS源站url              |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

#### 示例

```js

	var myFolder = '/111/';//需要操作的目录
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
		//大文件也可以直接调用uploadFile
		cos.uploadFile(successCallBack, errorCallBack, progressCallBack, bucket, myFolder+file.name, file, 0);
		//也可以用sliceUploadFile，选一个即可
		//cos.sliceUploadFile(successCallBack, errorCallBack, progressCallBack, bucket, myFolder+file.name, file, 0);
		return false;
	});


```

### 删除文件

接口说明：删除文件

#### 方法原型

```js
cos.deleteFile(successCallBack, errorCallBack, bucket, path);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**     |
| --------------- | -------- | -------- | ------- | ------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调      |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调      |
| bucket          | String   | 是        | 无       | bucket名称     |
| path            | String   | 是        | 无       | 文件在COS服务端的路径 |


#### 返回结果说明(json字符串)

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 提示信息      |


#### 示例

```js

	//删除文件
	$('#deleteFile').on('click', function () {
		var myFile = myFolder+'2.txt';//填您自己实际存在的文件
		cos.deleteFile(successCallBack, errorCallBack, bucket, myFile);
	});

```

### 获取文件属性

接口说明：通过此接口查询文件的各项属性信息。

#### 方法原型

```js
cos.getFileStat(successCallBack, errorCallBack, bucket, path);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**     |
| --------------- | -------- | -------- | ------- | ------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调      |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调      |
| bucket          | String   | 是        | 无       | bucket名称     |
| path            | String   | 是        | 无       | 文件在COS服务端的路径 |


#### 返回结果说明（json字符串）

| **参数名**             | **类型** | **是否必然返回** | **参数描述**                                 |
| ------------------- | ------ | ---------- | ---------------------------------------- |
| code                | Int    | 是          | 错误码，成功时为0                                |
| message             | String | 是          | 错误信息                                     |
| data                | Object | 是          | 文件属性数据                                   |
| data.name           | String | 是          | 文件或目录名                                   |
| data.biz_attr       | String | 是          | 文件属性，业务端维护                               |
| data.ctime          | String | 是          | 文件的创建时间，unix时间戳                          |
| data.mtime          | String | 是          | 文件的修改时间，unix时间戳                          |
| data.filesize       | Int    | 是          | 文件大小                                     |
| data.filelen        | Int    | 是          | 文件已传输大小                                  |
| data.sha            | String | 是          | 文件文件sha                                  |
| data.access_url     | String | 是          | 生成的文件下载url                               |
| data.authority      | String | 否          | eInvalid,eWRPrivate,eWPrivateRPublic,文件可以与bucket拥有不同的权限类型，已经设置过权限的文件如果想要撤销，直接赋值为eInvalid，则会采用bucket的权限 |
| data.custom_headers | String | 否          | 自定义header对象                              |


#### 示例

```js

	//获取文件属性
	$('#getFileStat').on('click', function () {
		var myFile = myFolder+'2.txt';//填您自己实际存在的文件
		cos.getFileStat(successCallBack, errorCallBack, bucket, myFile);
	});

```

### 更新文件属性

接口说明：通过此接口更新文件的属性信息。

#### 方法原型

```js
cos.updateFile(successCallBack, errorCallBack, bucket, path, bizAttr);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**     |
| --------------- | -------- | -------- | ------- | ------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调      |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调      |
| bucket          | String   | 是        | 无       | bucket名称     |
| path            | String   | 是        | 无       | 文件在COS服务端的路径 |
| bizAttr         | String   | 是        | 无       | 文件的自定义属性     |


#### 返回结果说明（json字符串）

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```js

	//更新文件属性
	$('#updateFile').on('click', function () {
		var myFile = myFolder+'2.txt';//填您自己实际存在的文件
		cos.updateFile(successCallBack, errorCallBack, bucket, myFile, 'my new file attr');
	});

```

### 拷贝文件

接口说明：通过此接口把文件拷贝（即复制）到另一个路径。

#### 方法原型

```js
cos.copyFile(successCallBack, errorCallBack, bucket, path, destPath, overWrite);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**              |
| --------------- | -------- | -------- | ------- | --------------------- |
| successCallBack | Function | 是        | 无       | 操作成功的回调               |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调               |
| bucket          | String   | 是        | 无       | bucket名称              |
| path            | String   | 是        | 无       | 需要复制的文件在COS服务端的路径     |
| destPath        | String   | 是        | 无       | 复制的目标的路径              |
| overWrite       | Int      | 是        | 无       | 是否覆盖同名文件，0表示不覆盖，1表示覆盖 |


#### 返回结果说明（json字符串）

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```js

	//拷贝文件，从源文件地址复制一份到新地址
	$('#copyFile').on('click', function () {

		var myFile = '111/2.txt';//填您自己实际存在的文件

		//注意目标的路径，这里如果填333/2.txt 则表示文件复制到111/333/2.txt
		//如果填/333/2.txt 则表示文件复制到bucket根目录下的333/2.txt
		var newFile = '/333/2.txt';
		var overWrite = 1;//0 表示不覆盖 1表示覆盖
		cos.copyFile(successCallBack, errorCallBack, bucket, myFile, newFile, overWrite);
	});

```

### 移动文件

接口说明：通过此接口把文件移动（剪切）到另一个路径，如果是移动到相同路径的话，可以达到修改文件名的效果。

#### 方法原型

```js
cos.moveFile(successCallBack, errorCallBack, bucket, path, destPath, overWrite);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**              |
| --------------- | -------- | -------- | ------- | --------------------- |
| successCallBack | Function | 是        | 无       | 操作成功的回调               |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调               |
| bucket          | String   | 是        | 无       | bucket名称              |
| path            | String   | 是        | 无       | 需要移动的文件在COS服务端的路径     |
| destPath        | String   | 是        | 无       | 移动的目标的路径              |
| overWrite       | Int      | 是        | 无       | 是否覆盖同名文件，0表示不覆盖，1表示覆盖 |


#### 返回结果说明（json字符串）

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```js

	//移动文件，把源文件移动到新地址，如果是同一个目录移动且文件名不同的话，相当于改了一个文件名
	//如果是移动到新目录，相当于剪切当前的文件，粘贴到了新目录
	$('#moveFile').on('click', function () {

		var myFile = '/111/2.txt';//填您自己实际存在的文件

		//注意目标的路径，这里如果填333/2.txt 则表示文件移动到111/333/2.txt
		//如果填/333/2.txt 则表示文件移动到bucket根目录下的333/2.txt
		//如果填/111/3.txt 则相当于把2.txt改名成3.txt
		var newFile = '/333/2.txt';
		var overWrite = 1;//0 表示不覆盖 1表示覆盖
		cos.moveFile(successCallBack, errorCallBack, bucket, myFile, newFile, overWrite);
	});

```

## 文件夹（目录）操作


### 新增文件夹

接口说明：通过此接口增加一个指定的文件夹。

#### 方法原型

```js
cos.createFolder(successCallBack, errorCallBack, bucket, path);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调            |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调            |
| bucket          | String   | 是        | 无       | bucket名称           |
| path            | String   | 是        | 无       | 需要操作的文件夹在COS服务端的路径 |


#### 返回结果说明（json字符串）

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```js

	$('#createFolder').on('click', function () {
		var newFolder = '/333/';//填您需要创建的文件夹
		cos.createFolder(successCallBack, errorCallBack, bucket, newFolder);
	});


```

### 删除文件夹

接口说明：通过此接口删除指定的文件夹。

#### 方法原型

```js
cos.deleteFolder(successCallBack, errorCallBack, bucket, path);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调            |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调            |
| bucket          | String   | 是        | 无       | bucket名称           |
| path            | String   | 是        | 无       | 需要操作的文件夹在COS服务端的路径 |


#### 返回结果说明（json字符串）

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```js

	//删除文件夹
	$('#deleteFolder').on('click', function () {
		var newFolder = '/333/';//填您需要删除的文件夹
		cos.deleteFolder(successCallBack, errorCallBack, bucket, newFolder);
	});

```

### 获取文件夹属性

接口说明：通过此接口获取指定的文件夹属性。

#### 方法原型

```js
cos.getFolderStat(successCallBack, errorCallBack, bucket, path);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调            |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调            |
| bucket          | String   | 是        | 无       | bucket名称           |
| path            | String   | 是        | 无       | 需要操作的文件夹在COS服务端的路径 |


#### 返回结果说明（json字符串）

| **参数名**       | **类型** | **是否必然返回** | **参数描述**   |
| ------------- | ------ | ---------- | ---------- |
| code          | Int    | 是          | 错误码，成功时为0  |
| message       | String | 是          | 错误信息       |
| data          | Object | 是          | 文件夹属性信息对象  |
| data.biz_attr | String | 是          | 文件夹属性信息字符串 |


#### 示例

```js

	//获取文件夹属性
	$('#getFolderStat').on('click', function () {
		cos.getFolderStat(successCallBack, errorCallBack, bucket, '/333/');
	});

```

### 更新文件夹属性

接口说明：通过此接口更新指定的文件夹属性。

#### 方法原型

```js
cos.updateFolder(successCallBack, errorCallBack, bucket, path, bizAttr);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调            |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调            |
| bucket          | String   | 是        | 无       | bucket名称           |
| path            | String   | 是        | 无       | 需要操作的文件夹在COS服务端的路径 |
| bizAttr         | String   | 是        | 无       | 新的属性信息             |


#### 返回结果说明（json字符串）

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |


#### 示例

```js

	//更新文件夹属性
	$('#updateFolder').on('click', function () {
		cos.updateFolder(successCallBack, errorCallBack, bucket, '/333/', 'new attr');
	});

```

### 获取文件夹内列表

接口说明：通过此接口获取指定的文件夹内的文件列表。

#### 方法原型

```js
cos.getFolderList(successCallBack, errorCallBack, bucket, path);
```

#### 参数说明

| **参数名**         | **类型**   | **是否必填** | **默认值** | **参数描述**           |
| --------------- | -------- | -------- | ------- | ------------------ |
| successCallBack | Function | 是        | 无       | 操作成功的回调            |
| errorCallBack   | Function | 是        | 无       | 操作失败的回调            |
| bucket          | String   | 是        | 无       | bucket名称           |
| path            | String   | 是        | 无       | 需要操作的文件夹在COS服务端的路径 |


#### 返回结果说明（json字符串）

| **参数名**               | **类型** | **是否必然返回**   | **参数描述**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
| code                  | Int    | 是            | API 错误码，成功时为0                            |
| message               | String | 是            | 错误信息                                     |
| data                  | Array  | 是            | 返回数据                                     |
| data.listover         | Bool   | 是            | 是否有内容可以继续往前/往后翻页                         |
| data.context          | String | 是            | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| data.infos            | Array  | 是            | 文件、目录集合，可以为空                             |
| data.infos.name       | String | 是            | 文件或目录名                                   |
| data.infos.biz_attr   | String | 是            | 目录或文件属性，业务端维护                            |
| data.infos.ctime      | String | 是            | 目录或文件的创建时间，unix时间戳                       |
| data.infos.mtime      | String | 是            | 目录或文件的修改时间，unix时间戳                       |
| data.infos.filesize   | Int    | 否(当类型为文件时返回) | 文件大小                                     |
| data.infos.filelen    | Int    | 否(当类型为文件时返回) | 文件已传输大小(通过与filesize对比可知文件传输进度)           |
| data.infos.sha        | String | 否(当类型为文件时返回) | 文件sha                                    |
| data.infos.access_url | String | 否(当类型为文件时返回) | 生成的文件下载url                               |
| data.infos.authority  | String | 否            | eInvalid,eWRPrivate,eWPrivateRPublic,文件可以与bucket拥有不同的权限类型，已经设置过权限的文件如果想要撤销，直接赋值为eInvalid，则会采用bucket的权限 |


#### 示例

```j
	//获取指定文件夹内的列表,默认每次返回20条
	$('#getFolderList').on('click', function () {
		cos.getFolderList(successCallBack, errorCallBack, bucket, myFolder);
	});
```
