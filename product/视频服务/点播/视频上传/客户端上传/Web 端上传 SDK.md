## 简介

对于浏览器上传音视频的场景，腾讯云点播提供了 Web 上传 SDK 来实现。上传的流程可以参见[客户端上传指引](/document/product/266/9219)。


## Demo

[https://tencentyun.github.io/vod-js-sdk-v6/](https://tencentyun.github.io/vod-js-sdk-v6/)

## 简单视频上传

### 引入 SDK 到页面中

```html
<script src="//unpkg.com/vod-js-sdk-v6"></script>
```
> SDK 依赖 Promise，请在低版本浏览器中自行引入。

###  定义获取上传签名的函数

```js
async function getSignature() {
  const response = await axios.post(url)
  const signature = response.data.signature
  return signature
};
```

> `url` 是您派发签名服务的 URL，参见[客户端上传指引](/document/product/266/9219)。
> `signature` 计算规则可参考[客户端上传签名](/document/product/266/9221)。

###  上传视频

示例如下：

```js
async () => {
  const tcVod = new TcVod.default({
    getSignature: getSignature // 前文中所述的获取上传签名的函数
  })

  const uploader = tcVod.upload({
    videoFile: videoFile, // 视频，类型为 File
    progress(info) {
      console.log(info.percent) // 进度
    },
  })

  // type doneResult = {
  //   fileId: string,
  //   video: {
  //     url: string
  //   },
  //   cover: {
  //     url: string
  //   }
  // }
  const doneResult = await uploader.done()
}

```

## 高级功能

### 同时上传视频和封面

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
})

const doneResult = await uploader.done()
```

### 获取上传进度

SDK 支持以回调的形式展示当前的上传进度，如下：

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
  // 视频上传完成时
  cosSuccess(info) {
    uploaderInfo.isVideoUploadSuccess = true;
  },
  // 视频上传进度
  progress(info) {
    uploaderInfo.progress = info.percent;
  },
  // 封面上传完成时
  cosCoverSuccess(info) {
    uploaderInfo.isCoverUploadSuccess = true;
  },
  // 封面上传进度
  coverProgress(info) {
    uploaderInfo.coverProgress = info.percent;
  },
})

const doneResult = await uploader.done()
```

### 取消上传

SDK 支持取消正在上传的视频或封面

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
})

uploader.cancel()
```

### 断点续传

SDK 支持自动断点续传功能，无需做额外操作。当上传意外终止时，用户再次上传该文件，可以从中断处继续上传，减少重复上传时间。

## 接口描述

### TcVod

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| getSignature    | 是    | Function     | 获取上传签名的函数  |

### TcVod.upload

| 参数名称         | 必填   | 类型       | 参数描述      |
| ------------ | ---- | -------- | --------- |
| videoFile    | 否    | File     | 视频文件  |
| coverFile    | 否    | File     | 封面文件  |
| cosSuccess    | 否    | Function     | 视频文件上传成功时  |
| cosCoverSuccess    | 否    | Function     | 封面上传成功时  |
| progress    | 否    | Function     | 视频文件上传进度  |
| coverProgress    | 否    | Function     | 封面文件上传进度  |
| videoName    | 否    | string     | 覆盖视频文件元信息中的文件名  |
| fileId    | 否    | string     | 当修改封面时传入  |

## 常见问题

1. `File` 对象怎么获取？
使用 `input` 标签，`type` 为 `file` 类型，即可拿到 `File` 对象

2. 上传的文件是否有大小限制?
最大支持 60GB。

3. SDK 支持的浏览器版本有哪些？
Chrome、Firefox等支持 `HTML 5` 的主流浏览器，IE 方面支持的最低版本是 IE10。



  ​

  ​

  ​