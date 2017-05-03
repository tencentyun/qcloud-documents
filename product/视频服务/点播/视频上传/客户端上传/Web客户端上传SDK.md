## UGC-Uplader SDK

###Demo
[https://video.qcloud.com/sdk/ugcuploader.html](https://video.qcloud.com/sdk/ugcuploader.html)

### SDK功能概览
1.仅上传视频
2.上传视频和封面
3.展示上传进度
4.上传成功与失败回调
5.获取上传后的有效地址

### 开发准备

#### 开发环境
1.使用SDK需要浏览器支持HTML 5
2.请您到[https://console.qcloud.com/capi](https://console.qcloud.com/capi)获取您的secretId与secretKey
3.请在后台服务器计算签名，确保secretKey的保密性

#### 计算签名
计算签名文档：
UGC上传签名工具：[https://video.qcloud.com/signature/ugcgenerate.html](https://video.qcloud.com/signature/ugcgenerate.html)
UGC签名解析校验工具：[https://video.qcloud.com/signature/ugcdecode.html](https://video.qcloud.com/signature/ugcdecode.html)

#### SDK配置
在页面引入ugcuploader.js即可
```js
<script src="//imgcache.qq.com/open/qcloud/js/vod/sdk/ugcUploader.js"></script>
```
### API
方法：qcVideo.ugcUploader.start

####功能
仅上传视频或上传视频和封面
#### 参数说明
| 参数名       | 类型       | 是否必填 | 默认值  | 参数描述      |
| --------- | -------- | ---- | ---- | --------- |
| videoFile | File     | 是    | 无    | 要上传的视频文件  |
| coverFile | File     | 否    | 无    | 要上传的封面文件  |
| getSignature | Function   | 是    | 无    | 获取签名的函数回调 |
| success   | Function | 否    | 无    | 上传成功回调    |
| error     | Function | 否    | 无    | 上传失败回调    |
| progress  | Function | 否    | 无    | 上传进度回调    |
| finish    | Function | 否    | 无    | 上传结果回调    |

#### 回调函数说明
| 函数名      | 说明     | 参数     | 参数描述                                     |
| -------- | ------------ | ------ | ---------------------------------------- |
| getSignature  | 获取签名的函数回调 | Function | callbak：把算好的签名作为callback函数的参数调用<br  />如：callback(signature);                               |
| success  | 上传成功回调 | Object | type：上传文件类型（'video'，'cover'）                              |
| error    | 上传失败回调 | Object | type：上传文件类型（'video'，'cover'）  <br  /> msg：上传错误信息                   |
| progress | 上传进度回调 | Object | type：上传文件类型（'video'，'cover'）  <br  />name：上传文件名称<br  />curr：上传文件进度      |
| finish   | 上传结果回调 | Object | fileId：文件在腾讯云点播控制台上的fileId<br  />videoName：视频文件名称<br  />videoUrl：视频文件地址<br  />coverName：封面文件名称<br  />coverUrl：封面文件地址 |

#### 后台错误返回值 
| 返回码       | 返回值       | 
| --------- | -------- | 
| 10004 | 请求签名校验失败    | 
| 10000-19999 |   请求错误   | 
| 20000-29999 |   服务错误   | 


#### 示例
##### 示例：获取签名
```js
/** 
 * 计算签名
**/
var getSignature = function(callback){
    // 正式使用必须要从服务端获取签名
    // 调用后台服务器接口，返回签名
    $.ajax({
        url: 'http://yourinterface',
        type: 'POST',
        dataType: 'json',
        success: function(result){
            callback(result.returnData.signature);
        }

    });
};

```
##### 示例1：仅上传视频
```html
<form id="form1">
    <input id="uploadVideoNow-file" type="file" accept="video/*" style="display:none;"/>
</form>
<div style="padding:20px;">
    <h3>示例1：仅上传视频</h3>
</div>
<div style="padding:20px;">
    <a id="uploadVideoNow" href="javascript:void(0);">直接上传视频</a>
</div>
```
```js
/** 
 * uploadVideoNow-file文件变更时立即调用qcVideo.ugcUploader.start函数
**/
$('#uploadVideoNow-file').on('change', function (e) {
    var videoFile = this.files[0];
    qcVideo.ugcUploader.start({
        videoFile: videoFile,
        getSignature: getSignature,
        success: function(result){
            // 上传成功回调
            // result.type：文件类型
        },
        error: function(result){
            // 上传失败回调
            // result.type：文件类型
            // result.msg：失败原因
        },
        progress: function(result){
            // 上传进度回调
            // result.type：文件类型
            // result.name：文件名称
            // result.curr：上传进度
        },
        finish: function(result){
            // 上传结果回调
            // result.fileId：fileId
            // result.videoName：视频文件名称
            // result.videoUrl：视频文件地址
        }
    });
    $('#form1')[0].reset();
});
/** 
 * 点击uploadVideoNow按钮时触发uploadVideoNow-file的click事件
**/
$('#uploadVideoNow').on('click', function () {
    $('#uploadVideoNow-file').click();
});
```

##### 示例2：上传视频和封面
1.上传视频和封面：直接调用qcVideo.ugcUploader.start即可上传视频+封面（封面为非必须）。
2.批量上传视频和封面：该例子把qcVideo.ugcUploader.start封装成startUploader方法，当前一个视频+封面上传完成后，在finish回调函数中把videoFileList[0]与coverFileList[0]剔除，然后再调用startUploader方法实现批量上传，当队列为空时，上传结束。
```html
<form id="form2">
    <input id="addVideo-file" type="file" accept="video/*" style="display:none;"/>
    <input id="addCover-file" type="file" accept="image/*" style="display:none;"/>
</form>
<div>
    <h3>示例2：上传视频和封面</h3>
</div>
<div>
    <div>
        <a id="addVideo" href="javascript:void(0);">添加视频</a>
    </div>
    <div>
        <a id="addCover" href="javascript:void(0);">添加封面</a>
    </div>
    <div>
        <a id="uploadFile" href="javascript:void(0);">上传视频和封面</a>
    </div>
</div>

```

```js
/** 
 * videoFileList：存放视频文件列表
 * coverFileList：存放封面文件列表
 * 可实现文件批量上传
**/
var videoFileList = [];
var coverFileList = [];

// 给addVideo添加监听事件
$('#addVideo-file').on('change', function (e) {
    var videoFile = this.files[0];
    videoFileList.push(videoFile);
});
$('#addVideo').on('click', function () {
    $('#addVideo-file').click();
});

// 给addCover添加监听事件
$('#addCover-file').on('change', function (e) {
    var coverFile = this.files[0];
    coverFileList.push(coverFile);
});
$('#addCover').on('click', function () {
    $('#addCover-file').click();
});

/**
 * 上传视频和封面
 * 上传的文件为videoFileList[0]和coverFileList[0]
 * 上传完成之后把文件从队列剔除
 * 若使用批量上传，则当队列为空时上传结束
**/
var startUploader = function(){
    if(videoFileList.length){
        qcVideo.ugcUploader.start({
            videoFile: videoFileList[0],
            coverFile: coverFileList[0],
            getSignature: getSignature,
            success: function(result){
                // 上传成功回调
                // result.type：文件类型
            },
            error: function(result){
                // 上传失败回调
                // result.type：文件类型
                // result.msg：失败原因
            },
            progress: function(result){
                // 上传进度回调
                // result.type：文件类型
                // result.name：文件名称
                // result.curr：上传进度
            },
            finish: function(result){
                // 上传结果回调
                // result.fileId：fileId
                // result.videoName：视频文件名称
                // result.videoUrl：视频文件地址
                // result.coverName：封面文件名称
                // result.coverUrl：封面文件地址
                videoFileList.shift();
                coverFileList.shift();
                startUploader();
            }
        });
    }
    
}

/** 
 * 上传按钮点击事件
 * 调用startUploader可实现文件批量上传
**/
$('#uploadFile').on('click', function () {
    startUploader();
    $('#form2')[0].reset();
});

```
