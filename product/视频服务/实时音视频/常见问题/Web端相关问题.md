### 实时音视频 Web 端示例代码？
有关实时音视频 Web 端 __示例代码__ 的内容，详情请点击 [这里](https://cloud.tencent.com/document/product/647/16924) 查看。

### 实时音视频 Web 端如何集成 SDK？
有关实时音视频 Web 端 __集成SDK__ 的内容，详情请点击 [这里](https://cloud.tencent.com/document/product/647/16863) 查看。

### 实时音视频 Web 端如何进房连麦？
有关实时音视频 Web 端  __进房连麦__ 的内容，详情请点击 [这里](https://cloud.tencent.com/document/product/647/16864) 查看。

### 实时音视频 Web 端 API 相关内容有哪些？
有关实时音视频web端 __API__ 内容如下：

-  [API 概览](https://cloud.tencent.com/document/product/647/17249) 
-  [基础功能接口](https://cloud.tencent.com/document/product/647/17251) 
-  [基础事件通知](https://cloud.tencent.com/document/product/647/17248) 
-  [高级功能接口](https://cloud.tencent.com/document/product/647/17250) 
-  [高级事件通知](https://cloud.tencent.com/document/product/647/17252)

### 实时音视频 Web 端如何屏幕分享？
有关实时音视频 Web 端 __屏幕分享__ 的内容，详情请点击 [这里](https://cloud.tencent.com/document/product/647/17847) 查看。

### 实时音视频 Web 端如何截图？
截图接口的调用实例是HTMLVideoElement

 __HTMLVideoElement.takeSnapshot__ 


``` 
/*
 * params:
 *   DeviceObject device
 * return:
 *   null
 */
    var video = document.getElementById("video")
    video.takeSnapshot(function(data){
        var img = document.createElement('img');
        img.src = data;
        $("#some_div_id").append( img );
    });
```
