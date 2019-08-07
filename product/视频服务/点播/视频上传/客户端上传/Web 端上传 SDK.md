对于浏览器上传音视频的场景，云点播提供了 Web 上传 SDK。

- 如果您需要 SDK 源码，可访问 [SDK 源码](https://tencentyun.github.io/vod-js-sdk-v6/)。
- 如果您需要 Demo 源码，可访问 [Demo 源码](https://github.com/tencentyun/vod-js-sdk-v6/blob/master/docs/index.html)。

## 简单视频上传

#### 引入 SDK 到页面中

```html
<script src="//unpkg.com/vod-js-sdk-v6"></script>
```

```js
import TcVod from 'vod-js-sdk-v6'
```

>? SDK 依赖 Promise，请在低版本浏览器中自行引入。

####  定义获取上传签名的函数

```js
function getSignature() {
  return axios.post(url).then(function (response) {
    return response.data.signature;
  })
};
```

>? `url`是您派发签名服务的 URL，详细请参见 [客户端上传指引](/document/product/266/9219)。
> `signature`计算规则请参见 [客户端上传签名](/document/product/266/9221)。

####  上传视频示例



```js
// 通过 import 引入的话，new TcVod(opts) 即可。
// new TcVod.default(opts) 是 script 引入 的用法
const tcVod = new TcVod.default({
  getSignature: getSignature // 前文中所述的获取上传签名的函数
})

const uploader = tcVod.upload({
  mediaFile: mediaFile, // 媒体文件（视频或音频或图片），类型为 File
})
uploader.on('media_progress', function(info) {
  console.log(info.percent) // 进度
})

// 回调结果说明
// type doneResult = {
//   fileId: string,
//   video: {
//     url: string
//   },
//   cover: {
//     url: string
//   }
// }
uploader.done().then(function (doneResult) {
  // deal with doneResult
}).catch(function (err) {
  // deal with error
})


```

## 高级功能

#### 同时上传视频和封面

```js
const uploader = tcVod.upload({
  mediaFile: mediaFile,
  coverFile: coverFile,
})

uploader.done().then(function (doneResult) {
  // deal with doneResult
})
```

#### 获取上传进度

SDK 支持以回调的形式展示当前的上传进度：

```js
const uploader = tcVod.upload({
  mediaFile: mediaFile,
  coverFile: coverFile,
})
// 视频上传完成时
uploader.on('media_upload', function(info) {
  uploaderInfo.isVideoUploadSuccess = true;
})
// 视频上传进度
uploader.on('media_progress', function(info) {
  uploaderInfo.progress = info.percent;
})
// 封面上传完成时
uploader.on('cover_upload', function(info) {
  uploaderInfo.isCoverUploadSuccess = true;
})
// 封面上传进度
uploader.on('cover_progress', function(info) {
  uploaderInfo.coverProgress = info.percent;
})

uploader.done().then(function (doneResult) {
  // deal with doneResult
})
```

`xxx_upload`与`xxx_progress`的回调值请参见 [分块上传/复制任务操作]( https://cloud.tencent.com/document/product/436/35649#.E5.88.86.E7.89.87.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1)。

#### 取消上传

SDK 支持取消正在上传的视频或封面：

```js
const uploader = tcVod.upload({
  mediaFile: mediaFile,
  coverFile: coverFile,
})

uploader.cancel()
```

#### 断点续传

SDK 支持自动断点续传功能，无需做额外操作。当上传意外终止时（如浏览器关闭、网络中断等），您再次上传该文件，可以从中断处继续上传，减少重复上传时间。

## 接口描述

#### TcVod

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| getSignature    | 是    | Function     | 获取上传签名的函数。  |
| appId    | 否    | number     | 填入后，内置的统计上报会自动带上。  |
| reportId    | 否    | number     | 填入后，内置的统计上报会自动带上。  |

#### TcVod.upload

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| mediaFile    | 否    | File     | 媒体文件（视频或音频或图片）。  |
| coverFile    | 否    | File     | 封面文件。  |
| mediaName    | 否    | string     | 覆盖媒体文件元信息中的文件名。  |
| fileId    | 否    | string     | 当修改封面时传入。  |
| reportId    | 否    | number     | 填入后，内置的统计上报会自动带上。会覆盖构造函数中的设置。  |

#### 事件

| 事件名称         | 必填   |  事件描述      |
| ------------ | ---- |  --------- |
| media_upload    | 否    |  媒体文件上传成功时。  |
| cover_upload    | 否    |  封面上传成功时。  |
| media_progress    | 否    |  媒体文件上传进度。  |
| cover_progress    | 否    |  封面文件上传进度。  |

## 常见问题

1. **`File`对象怎么获取？**
使用`input`标签，`type`为`file`类型，即可拿到`File`对象。

2. **上传的文件是否有大小限制?**
最大支持60GB。

3. **SDK 支持的浏览器版本有哪些？**
Chrome、Firefox 等支持`HTML5`的主流浏览器，IE 方面支持的最低版本是 IE10。


