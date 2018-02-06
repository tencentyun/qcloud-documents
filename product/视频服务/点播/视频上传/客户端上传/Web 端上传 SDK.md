## 简介

对于浏览器上传音视频的场景，腾讯云点播提供了 Web 上传 SDK 来实现。上传的流程可以参见[客户端上传指引](/document/product/266/9219)。


## Demo 下载

[http://video.qcloud.com/sdk/ugcuploader.html](http://video.qcloud.com/sdk/ugcuploader.html)

## 简单视频上传

### 引入 SDK 到页面中
```js
<script src="//imgcache.qq.com/open/qcloud/js/vod/sdk/ugcUploader.js"></script>
```
>SDK 依赖 jQuery 来发送请求，所以请把 jQuery 也引入到页面中。

###  定义获取上传签名的函数
```js
var getSignature = function(callback){
    $.ajax({
        url: 'yourinterface',  //获取客户端上传签名的 URL
        type: 'POST',
        dataType: 'json',
        success: function(result){//result 是派发签名服务器的回包
            //假设回包为 { "code": 0, "signature": "xxxx"  }
            //将签名传入 callback，SDK 则能获取这个上传签名，用于后续的上传视频步骤。
            callback(result.signature);
        }
    });
};
```
>`url` 是您派发签名服务的 URL，参见[客户端上传指引](/document/product/266/9219)。
>`signature` 计算规则可参考[客户端上传签名](/document/product/266/9221)。

###  上传视频

上传视频是通过调用 `qcVideo.ugcUploader.start` 来实现的。实例如下：

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,//视频，类型为 File
    getSignature: getSignature,//前文中所述的获取上传签名的函数
    error: function(result){//上传失败时的回调函数
        //...
        console.log('上传失败的原因：' + result.msg);
    },
    finish: function(result){//上传成功时的回调函数
        console.log('上传结果的fileId：' + result.fileId);
        console.log('上传结果的视频名称：' + result.videoName);
        console.log('上传结果的视频地址：' + result.videoUrl);
    }
});
```

## 高级功能

### 同时上传视频和封面

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    coverFile: coverFile,//封面, 类型为 File
    getSignature: getSignature,
    error: function(result){
        //...
        console.log('上传失败的原因：' + result.msg);
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

### 获取上传进度

SDK 支持以回调的形式展示当前的上传进度，如下：

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    coverFile: coverFile,//封面，类型为 File
    getSignature: getSignature,
    error: function(result){
        console.log('上传失败的文件类型：' + result.type);
        console.log('上传失败的原因：' + result.msg);
    },
    progress: function(result){
        console.log('上传进度：' + result.curr);
    },
    finish: function(result){
        console.log('上传结果的 fileId：' + result.fileId);
        console.log('上传结果的视频名称：' + result.videoName);
        console.log('上传结果的视频地址：' + result.videoUrl);
        console.log('上传结果的封面名称：' + result.coverName);
        console.log('上传结果的封面地址：' + result.coverUrl);
    }
});
```

### 取消上传
SDK 支持取消正在上传的视频或封面，可以通过调用 `qcVideo.ugcUploader.cancel` 实现。
```js

//用于实现取消上传的两个对象。
var uploadCos;//需要在 progress 回调中赋值。
var uploadTaskId;//需要在 progress 回调中赋值。

qcVideo.ugcUploader.start({
    videoFile: videoFile,//这个是视频，类型为 File
    getSignature: getSignature,//这个是第二步定义的函数
    error: function(result){
        console.log('上传失败的原因：' + result.msg);
    },
    progress: function(result){
        console.log('上传进度的文件类型：' + result.type);
        console.log('上传进度的文件名称：' + result.name);
        console.log('上传进度：' + result.curr);
        uploadCos = result.cos;
        uploadTaskId = result.taskId;
    },
    finish: function(result){
        console.log('上传结果的 fileId：' + result.fileId);
        console.log('上传结果的视频名称：' + result.videoName);
        console.log('上传结果的视频地址：' + result.videoUrl);
    }
});

// ...

// 取消上传
qcVideo.ugcUploader.cancel({
	cos: uploadCos,   
	taskId: uploadTaskId
});
```

### 断点续传

SDK 支持自动断点续传功能，无需做额外操作。当上传意外终止时，用户再次上传该文件，可以从中断处继续上传，减少重复上传时间。断点续传的有效时间是 1 天，即同一个视频上传被中断，那么 1 天内再次上传可以直接从断点处上传，超过 1 天则默认会重新上传完整视频。

## 接口描述

### 上传视频 `qcVideo.ugcUploader.start` 中的参数：

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| videoFile    | 是    | File     | 要上传的视频文件  |
| coverFile    | 否    | File     | 要上传的封面文件  |


### 回调函数说明

| 函数名          | 含义     | 参数类型     | 补充说明                                     |
| ------------ | ------ | -------- | ---------------------------------------- |
| getSignature | 获取签名回调 | Function | 回调参数 callback，实现时需要把获取到的签名传给 callback，用于后续上传视频步骤的鉴权 |
| error        | 上传失败回调 | Object   | 回调的 result 对象中：<br  />type 字段表示上传失败的文件种类，'video' 表示视频, 'cover' 表示封面<br /> msg 字段表示上传失败的原因。 |
| progress     | 上传进度回调 | Object   | 回调的 result 对象中：<br  /> type 字段表示上传失败的文件种类；<br  />video 字段表示视频或者 cover 字段表示封面 <br  />name 字段表示上传中的文件名<br  />curr 字段表示文件上传进度 |
| finish       | 上传结果回调 | Object   | 回调的 result 对象中：<br  /> fileId 字段表示视频文件 ID<br  />videoName 字段表示视频名称<br  />videoUrl 字段表示视频播放地址<br  />coverName 字段表示封面名称<br  />coverUrl 字段表示封面展示地址 |



## 其他
### 支持上传的文件类型

| 类型   | 支持格式                                     |
| ---- | ---------------------------------------- |
| 视频   | WMV、WM、ASF、ASX<br />RM、RMVB、RA、RAM<br />MPG、MPEG、MPE、VOB、DAT<br />MOV、3GP、MP4、MP4V、M4V、MKV、AVI、FLV、F4V |
| 图片   | JPG、JPEG、JPE<br />PSD<br />SVG、SVGZ<br />TIFF、TIF<br />BMP、GIF、PNG |
| 音频   | MP3、WAV       |

音频的上传方式跟视频一样，即 `qcVideo.ugcUploader.start` 中 `videoFile` 为音频文件即可。


## 常见问题

1. `File` 对象怎么获取？
使用 `input` 标签，`type` 为 `file` 类型，即可拿到 `File` 对象

2. 上传的文件是否有大小限制?
最大支持 60GB。

3. SDK 支持的浏览器版本有哪些？
chrome、firefox等支持 `HTML 5` 的主流浏览器，IE 方面支持的最低版本是 IE10。



  ​

  ​

  ​