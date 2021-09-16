对于浏览器上传音视频的场景，云点播提供了 Web 上传 SDK。如果您需要 SDK 源码，可访问 [SDK 源码](https://github.com/tencentyun/vod-js-sdk-v6)。

## 简单视频上传

### 引入 SDK

#### script 引入方式
未使用 webpack 的情况下，可通过 script 标签方式引入，该方式会暴露全局的`TcVod`变量。script 引入有下面两种方式：
- **下载到本地**
	下载 [SDK 源码](https://github.com/tencentyun/vod-js-sdk-v6) 到本地，然后按以下方式引入：
```html
<script src="./vod-js-sdk-v6.js"></script>
```
>?引入路径请自行调整为您本地保存的路径。
- **使用 CDN 资源**
	使用 CDN 资源，可直接按以下方式引入：
```html
<script src="https://cdn-go.cn/cdn/vod-js-sdk-v6/latest/vod-js-sdk-v6.js"></script>
```

请 [单击此处](https://tencentyun.github.io/vod-js-sdk-v6/) 查看 script 方式引入的 Demo，请 [单击此处](https://github.com/tencentyun/vod-js-sdk-v6/blob/master/docs/index.html) 查看 Demo 源码。

#### npm 引入方式
使用 webpack 的情况下（如使用 Vue 或者 React），可通过 npm 引入：
```js
// npm install vod-js-sdk-v6 之后，在页面中直接 import 引入
import TcVod from 'vod-js-sdk-v6'
```

请 [单击此处](https://github.com/tencentyun/vod-js-sdk-v6/tree/master/docs/import-demo) 查看 npm 方式引入的 Demo 源码。

>!SDK 依赖 Promise，请在低版本浏览器中自行引入。


###  定义获取上传签名的函数

```js
function getSignature() {
  return axios.post(url).then(function (response) {
    return response.data.signature;
  })
};
```

>? `url`是您派发签名服务的 URL，更多相关信息请参见 [客户端上传指引](https://cloud.tencent.com/document/product/266/9219#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)。
> `signature`计算规则请参见 [客户端上传签名](/document/product/266/9221)。

###  上传视频示例



```js
// 通过 import 引入的话，new TcVod(opts) 即可
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

>?
>- `new TcVod(opts)`中的 opts 指该接口的相关参数，详细请参见 [TcVod 接口描述](#.E6.8E.A5.E5.8F.A3.E6.8F.8F.E8.BF.B0)。
>- 上传方法根据用户文件的长度，自动选择普通上传以及分片上传，用户不用关心分片上传的每个步骤，即可实现分片上传。
>- 如需上传至指定子应用下，请参见 [子应用体系 - 客户端上传](https://cloud.tencent.com/document/product/266/14574#.E5.AE.A2.E6.88.B7.E7.AB.AF.E4.B8.8A.E4.BC.A0)。

## 高级功能

### 同时上传视频和封面

```js
const uploader = tcVod.upload({
  mediaFile: mediaFile,
  coverFile: coverFile,
})

uploader.done().then(function (doneResult) {
  // deal with doneResult
})
```

### 获取上传进度

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

`xxx_upload`与`xxx_progress`的回调值请参见 [分块上传/复制任务操作]( https://cloud.tencent.com/document/product/436/35649#.E4.B8.8A.E4.BC.A0.E5.88.86.E5.9D.97)。

### 取消上传

SDK 支持取消正在上传的视频或封面：

```js
const uploader = tcVod.upload({
  mediaFile: mediaFile,
  coverFile: coverFile,
})

uploader.cancel()
```

### 断点续传

SDK 支持自动断点续传功能，无需做额外操作。当上传意外终止时（如浏览器关闭、网络中断等），您再次上传该文件，可以从中断处继续上传，减少重复上传时间。

## 接口描述

### TcVod

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| getSignature    | 是    | Function     | 获取上传签名的函数。  |
| appId    | 否    | number     | 填入后，内置的统计上报会自动带上。  |
| reportId    | 否    | number     | 填入后，内置的统计上报会自动带上。  |

### TcVod.upload

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| mediaFile    | 否    | File     | 媒体文件（视频或音频或图片）。  |
| coverFile    | 否    | File     | 封面文件。  |
| mediaName    | 否    | string     | 覆盖媒体文件元信息中的文件名。  |
| fileId    | 否    | string     | 当修改封面时传入。  |
| reportId    | 否    | number     | 填入后，内置的统计上报会自动带上。会覆盖构造函数中的设置。  |

### 事件

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
4. **如何实现类似暂停上传或恢复上传的功能？**
SDK 底层已经自动实现了断点续传的功能，因此暂停的本质即是调用`uploader.cancel()`这个方法。同理，暂停后的恢复上传也是调用初始的`tcVod.upload`方法，区别在于恢复上传时调用该方法的参数，应该是之前缓存起来的参数（例如可以在启动上传时全局变量存储一份参数，上传完成后再清掉）。

