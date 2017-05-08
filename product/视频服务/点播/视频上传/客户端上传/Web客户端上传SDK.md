### 简介

用于浏览器文件上传的SDK，可向腾讯云点播系统上传视频和封面文件。

### Demo
[https://video.qcloud.com/sdk/ugcuploader.html](https://video.qcloud.com/sdk/ugcuploader.html)

### 开发环境

1. 使用SDK需要浏览器支持HTML 5
2. 需要APP服务器派发客户端上传签名，生成签名的方法请见[这里](/document/product/266/9221)

### 集成方式

在页面引入ugcuploader.js即可。
```js
<script src="//imgcache.qq.com/open/qcloud/js/vod/sdk/ugcUploader.js"></script>
```
### 本地视频上传步骤

####  第一步：获取签名操作
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

####  第二步：指定上传目标
指定上传目标的参数有视频文件、封面文件和获取签名函数等回调函数。如果只上传视频，则封面参数可不填。<br  /><br  />


| 参数名称 |  必填 |类型 | 参数描述 |
| ------ | ------ | ------ | ------ | ------ |
| videoFile | 是 | File |  要上传的视频文件 |
| coverFile |否 | File | 要上传的封面文件 |
| getSignature |是| Function |  获取签名的回调函数 |
| success   | 否 |Function | 上传成功的回调函数 |
| error     |否 | Function | 上传失败的回调函数 |
| progress  |否 | Function |  上传进度的回调函数 |
| finish    | 否 |Function | 上传结果的回调函数 |

#####  回调函数说明

| 函数名 | 说明 | 参数类型 | 参数含义 |
| ------ | ------ | ------ | ------ |
| getSignature | 获取签名回调 | Function | callbak：把获取到的签名作为callback函数的参数（如：callback(signature)）; |
| success | 上传成功回调 | Object | type：上传成功的文件种类，'video'（视频）或者'cover'（封面）|
| error | 上传失败回调 | Object | type：上传失败的文件种类，'video'（视频）或者'cover'（封面）|
| progress | 上传进度回调 | Object | type：上传进行中的文件种类，'video'（视频）或者'cover'（封面）<br  />name：上传中的文件名<br  />curr：文件上传进度 |
| finish   | 上传结果回调 | Object | fileId：视频文件Id<br  />videoName：视频名称<br  />videoUrl：视频播放地址<br  />coverName：封面名称<br  />coverUrl：封面展示地址 |

#### 第三步：执行上传操作
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
