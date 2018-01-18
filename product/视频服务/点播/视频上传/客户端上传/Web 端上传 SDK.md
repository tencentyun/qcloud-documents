## 简介

用于浏览器的客户端上传 SDK，可向腾讯云点播系统上传视频和封面文件。

## 集成方式

### 开发环境

* 使用 SDK 需要浏览器支持 HTML 5
* 需要 APP 服务器派发客户端上传签名，生成签名的方法请见[上传签名](/document/product/266/9221)

### 集成

在页面引入ugcuploader.js即可。
```js
<script src="//imgcache.qq.com/open/qcloud/js/vod/sdk/ugcUploader.js"></script>
```

### Demo

[http://video.qcloud.com/sdk/ugcuploader.html](http://video.qcloud.com/sdk/ugcuploader.html)

## 上传步骤

###  第一步：获取上传签名
```js
var getSignature = function(callback){
    $.ajax({
        url: 'yourinterface',  //服务器获取客户端上传签名的URL
        type: 'POST',
        dataType: 'json',
        success: function(result){
            //result.returnData.signature为获取到的签名
            callback(result.returnData.signature);
        }
    });
};

```

###  第二步：指定上传目标

上传目标有视频和封面信息。如果只上传视频，则封面参数可不填。

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| videoFile    | 是    | File     | 要上传的视频文件  |
| coverFile    | 否    | File     | 要上传的封面文件  |
| getSignature | 是    | Function | 获取签名的回调函数 |
| success      | 否    | Function | 上传成功的回调函数 |
| error        | 否    | Function | 上传失败的回调函数 |
| progress     | 否    | Function | 上传进度的回调函数 |
| finish       | 否    | Function | 上传结果的回调函数 |

回调函数说明

| 函数名          | 说明     | 参数类型     | 参数含义                                     |
| ------------ | ------ | -------- | ---------------------------------------- |
| getSignature | 获取签名回调 | Function | callback：把获取到的签名作为 callback 函数的参数，即callback(signature); |
| success      | 上传成功回调 | Object   | type：上传成功的文件种类，'video'（视频）或者'cover'（封面）  |
| error        | 上传失败回调 | Object   | type：上传失败的文件种类，'video'（视频）或者'cover'（封面）  |
| progress     | 上传进度回调 | Object   | type：上传进行中的文件种类，'video'（视频）或者'cover'（封面）<br  />name：上传中的文件名<br  />curr：文件上传进度 |
| finish       | 上传结果回调 | Object   | fileId：视频文件 ID<br  />videoName：视频名称<br  />videoUrl：视频播放地址<br  />coverName：封面名称<br  />coverUrl：封面展示地址 |

### 第三步：执行上传操作

#### 仅上传视频

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    getSignature: getSignature,
    success: function(result){
        console.log('上传成功的文件类型：' + result.type);
    },
    error: function(result){
        console.log('上传失败的文件类型：' + result.type);
        console.log('上传失败的原因：' + result.msg);
    },
    progress: function(result){
        console.log('上传进度的文件类型：' + result.type);
        console.log('上传进度的文件名称：' + result.name);
        console.log('上传进度：' + result.curr);
        console.log('cos对象：' + result.cos);
        console.log('taskId：' + result.taskId);
    },
    finish: function(result){
        console.log('上传结果的fileId：' + result.fileId);
        console.log('上传结果的视频名称：' + result.videoName);
        console.log('上传结果的视频地址：' + result.videoUrl);
    }
});
```

#### 同时上传视频和封面

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    coverFile: coverFile,
    getSignature: getSignature,
    success: function(result){
        console.log('上传成功的文件类型：' + result.type);
    },
    error: function(result){
        console.log('上传失败的文件类型：' + result.type);
        console.log('上传失败的原因：' + result.msg);
    },
    progress: function(result){
        console.log('上传进度的文件类型：' + result.type);
        console.log('上传进度的文件名称：' + result.name);
        console.log('上传进度：' + result.curr);
        console.log('cos对象：' + result.cos);
        console.log('taskId：' + result.taskId);
    },
    finish: function(result){
        console.log('上传结果的fileId：' + result.fileId);
        console.log('上传结果的视频名称：' + result.videoName);
        console.log('上传结果的视频地址：' + result.videoUrl);
        console.log('上传结果的封面名称：' + result.coverName);
        console.log('上传结果的封面地址：' + result.coverUrl);
    }
});
```

## 其他接口
### 取消上传
正在上传中的视频支持取消上传。

| 参数     | 说明                 |
| ------ | ------------------ |
| cos    | progress中返回的cos对象  |
| taskId | progress中返回的taskId |

```js
qcVideo.ugcUploader.cancel({
	cos: cos,   
	taskId: taskId  
});
```
### 断点续传

SDK支持断点续传功能，无需做任何操作。

**内部实现：**文件上传过程中，SDK会在COOKIE中记录该文件的vodSessionKey，键名以webugc_开头，如：webugc_dab2bfc5cfcd8d8561c44f7c68961edd9bbcxxxx，重新上传文件的时候SDK通过COOKIE判断该文件是否上传过，如果是则可以拿到vodSessionKey进行断点续传，否则正常上传。vodSessionKey的有效时间为一天。

### 上传文件类型

| 类型   | 支持格式                                     |
| ---- | ---------------------------------------- |
| 视频   | WMV、WM、ASF、ASX<br />RM、RMVB、RA、RAM<br />MPG、MPEG、MPE、VOB、DAT<br />MOV、3GP、MP4、MP4V、M4V、MKV、AVI、FLV、F4V |
| 音频   | MP3、WMA、WAV、ASF、AU、SND、RAW、AFC、ACC       |
| 图片   | JPG、JPEG、JPE<br />PSD<br />SVG、SVGZ<br />TIFF、TIF<br />BMP、GIF、PNG |

### 后台错误码列表

| 错误码         | 说明                |
| ----------- | ----------------- |
| 10005       | 断点续传已过期           |
| 10000-19999 | 请求错误              |
| 20000-29999 | 服务错误              |
| 31001       | 用户请求session_key错误 |
| 31002       | 用户请求中的VOD签名重复     |
| 31003       | 上传文件不存在           |
| 32001       | 服务错误              |

### 前端错误信息列表

| 接口                         | 错误信息                                     |
| -------------------------- | ---------------------------------------- |
| qcVideo.ugcUploader.start  | 文件名不得包含 / : * ? "  < > 等字符               |
|                            | 参数必须为对象类型                                |
|                            | 需要videoFile或者fileId字段                    |
|                            | 需要getSignature字段                         |
|                            | fileId格式错误                               |
|                            | 需要coverFile字段                            |
|                            | getSignature必须为函数，如果有success、error、progress、finish，也必须为函数 |
|                            | videoFile必须为视频文件                         |
|                            | coverFile必须为图片文件                         |
| qcVideo.ugcUploader.cancel | 参数必须为对象类型                                |
|                            | cos/taskId不能为空                           |
|                            | taskId格式错误                               |
|                            | cos格式错误                                  |

### FAQ

- File对象怎么获取？

  使用input标签，type为file类型，即可拿到File对象

- 一个 10MB文件，上传了 50%，断点续传是从 20%开始的？

  上传是按分片上传的，断点续传是以已经上传完成的分片为准的，比如说正在上传是3个分片，完成的分片2个，那么断点续传的时候就是以完成2个分片的状态为准的。

- 上传最大支持多少G？

  最大支持60G

- web上传时，如何自动转码？

  签名里面带上任务流参数（控制台上传的话，勾选转码即可）

- web上传支持的最低版本

  最低版本为IE10


  ​

  ​

  ​