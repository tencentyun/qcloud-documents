小程序端上传视频的 SDK。上传流程请参见 [客户端上传指引](/document/product/266/9219)。

- 如果您需要 SDK 源码，可访问 [SDK 源码](https://github.com/tencentyun/vod-wx-sdk-v2/)。
- 如果您需要 Demo 源码，可访问 [Demo 源码](https://github.com/tencentyun/vod-wx-sdk-v2/tree/master/demo)。

## 上传视频步骤

**1. 引入 SDK**

- 直接引入文件
```js
const VodUploader = require('../../lib/vod-wx-sdk-v2.js');
```
- npm 安装
```bash
npm i vod-wx-sdk-v2
```

**2. 定义获取上传签名的函数**

```js
getSignature: function(callback) {
    wx.request({
        /**
        * 此处省略部分代码
        */
        url: url,
        success: function(res) {
            callback(signature)
        }
    });
}
```

>?
>- `url` 是您派发签名服务的 URL，参见 [客户端上传指引](https://cloud.tencent.com/document/product/266/9219)。
>- `signature` 计算规则可参考 [客户端上传签名](https://cloud.tencent.com/document/product/266/9221)。

**3. 上传视频**
上传视频是通过调用`VodUploader.start`来实现的，选择视频则通过微信小程序 API 中的`wx.chooseVideo`方法实现。示例如下：

```js
 const uploader = VodUploader.start({
    // 必填，把 wx.chooseVideo 回调的参数(file)传进来
    mediaFile: videoFile, 
    // 必填，获取签名的函数
    getSignature: getSignature, 
    // 选填，视频名称，强烈推荐填写(如果不填，则默认为“来自小程序”)
    mediaName: fileName, 
    // 选填，视频封面，把 wx.chooseImage 回调的参数(file)传进来
    coverFile: coverFile, 
    // 上传中回调，获取上传进度等信息
    progress: function(result) {
        console.log('progress');
        console.log(result);
    },
    // 上传完成回调，获取上传后的视频 URL 等信息
    finish: function(result) {
        console.log('finish');
        console.log(result);
        wx.showModal({
            title: '上传成功',
            content: 'fileId:' + result.fileId + '\nvideoName:' + result.videoName,
            showCancel: false
        });
    },
    // 上传错误回调，处理异常
    error: function(result) {
        console.log('error');
        console.log(result);
        wx.showModal({
            title: '上传失败',
            content: JSON.stringify(result),
            showCancel: false
        });
    },
});
```
>?如需上传至指定子应用下，请参见 [子应用体系 - 客户端上传](https://cloud.tencent.com/document/product/266/14574#.E5.AE.A2.E6.88.B7.E7.AB.AF.E4.B8.8A.E4.BC.A0)。

## 接口描述

### VodUploader.start

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| getSignature    | 是    | Function     | 获取上传签名的函数  |
| mediaFile | 是 | file | wx.chooseVideo 回调返回的文件对象
| reportId    | 否    | number     | 填入后，会携带上报至点播后台  |
| mediaName | 否 | string | 视频名称，推荐填写（如果不填，则默认为“来自小程序”）
| coverFile | 否 | file | 视频封面，wx.chooseImage 回调返回的文件对象
| [progress](#y1) | 是 | Function | 上传 progress 事件回调，返回上传进度等信息
| [finish](#y2) | 是 | Function | 上传结束回调，返回 fileId 等信息
| [error](#y3) | 是 | Function | 错误处理回调

### `progress`回调[](id:y1)

| 字段名 | 类型 | 字段描述 |
| ------- | ------- | ------- |
| loaded | number | 已上传大小 |
| percent | number | 已上传大小百分比 |
| speed | number | 上传速度 |
| total | number | 总大小 |

### `finish`回调[](id:y2)

| 字段名 | 类型 | 字段描述 |
| ------- | ------- | ------- |
| coverUrl | string | 封面图 URL，如未上传封面则此处为 undefined |
| fileId | string | 视频 fileId |
| videoName | string | 视频名称 |
| videoUrl | string | 视频链接 |

### `error`回调[](id:y3)

| 字段名 | 类型 | 字段描述 |
| ------- | ------- | ------- |
| code | number | 错误码 |
| message | string | 错误信息 |

## 其他说明

1. 由于小程序没有获取真实文件名的 API，所以需要在上传视频时指定视频名称。如不传入`mediaName`，SDK 会设置视频名称为“来自小程序”。
2. 默认支持断点续传和分片上传。
3. 小程序域名信息中，`request`和`uploadFile`为合法域名，只需加上`vod2.qcloud.com`即可。
