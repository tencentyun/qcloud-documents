小程序端上传视频的 SDK。

>?
- 如果您需要 SDK 源码，可访问 [SDK 源码](https://github.com/tencentyun/vod-wx-sdk-v2/)。
- 如果您需要 Demo 源码，可访问 [Demo 源码](https://github.com/tencentyun/vod-wx-sdk-v2/tree/master/demo)。

## 上传视频步骤

**1. 引入 SDK**

```
const VodUploader = require('../../lib/vod-wx-sdk-v2.js');
```

**2. 定义获取上传签名的函数**

```
getSignature: function(callback) {
    wx.request({
        url: 'https://xzb.qcloud.com/get_vod_sign',
        method: 'POST',
        data: {
            Action: 'GetVodSignatureV2'
        },
        dataType: 'json',
        success: function(res) {
            if (res.data && res.data.data.signature) {
                callback(res.data.data.signature);
            } else {
                return '获取签名失败';
            }
        }
    });
}
```

>?
- `url`是您派发签名服务的 URL，参见 [客户端上传指引](https://cloud.tencent.com/document/product/266/9219)。
- `signature`计算规则可参考 [客户端上传签名](https://cloud.tencent.com/document/product/266/9221)。

**3. 上传视频**
上传视频是通过调用`VodUploader.start`来实现的，选择视频则通过微信小程序 API 中的`wx.chooseVideo`方法实现。示例如下：

```
 VodUploader.start({
    mediaFile: videoFile, //必填，把chooseVideo回调的参数(file)传进来
    getSignature: getSignature, //必填，获取签名的函数

    mediaName: fileName, //选填，视频名称，强烈推荐填写(如果不填，则默认为“来自微信小程序”)
    coverFile: coverFile, // 选填，视频封面
    success: function(result) {
        console.log('success');
        console.log(result);
    },
    error: function(result) {
        console.log('error');
        console.log(result);
        wx.showModal({
            title: '上传失败',
            content: JSON.stringify(result),
            showCancel: false
        });
    },
    progress: function(result) {
        console.log('progress');
        console.log(result);
    },
    finish: function(result) {
        console.log('finish');
        console.log(result);
        wx.showModal({
            title: '上传成功',
            content: 'fileId:' + result.fileId + '\nvideoName:' + result.videoName,
            showCancel: false
        });
    }
});
```

## 其他

1. 因为小程序没有获取真实文件名的 API，所以需要在上传视频之前，输入视频名称。如果不输入，SDK 会设置视频名称为“来自小程序”。
1. 不支持断点续传和分片上传。
1. 小程序域名信息中，request 和 uploadFile 合法域名，只需加上`vod2.qcloud.com`即可。
