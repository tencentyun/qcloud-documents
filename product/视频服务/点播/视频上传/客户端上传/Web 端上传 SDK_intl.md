## Intro

Web SDK for Tencent Cloud Video Service. Used in browser.

Detail upload process can refer to [客户端上传指引](/document/product/266/9219)。

source code：[https://github.com/tencentyun/vod-js-sdk-v6](https://github.com/tencentyun/vod-js-sdk-v6)


## Demo

[https://tencentyun.github.io/vod-js-sdk-v6/](https://tencentyun.github.io/vod-js-sdk-v6/)

Demo source code: [https://github.com/tencentyun/vod-js-sdk-v6/blob/master/docs/index.html](https://github.com/tencentyun/vod-js-sdk-v6/blob/master/docs/index.html)

## Simple video upload

### import SDK in the page

```html
<script src="//unpkg.com/vod-js-sdk-v6"></script>
```
> We use Promise in the source code. You should imoprt Promise polyfill when target legacy browsers.

### define a function to get signature

```js
function getSignature() {
  return axios.post(url).then(function (response) {
    return response.data.signature;
  })
};
```

> `url` Your url which can return signature. Refer to [客户端上传指引](/document/product/266/9219)。
> `signature` Refer to for the computation of signature [客户端上传签名](/document/product/266/9221)。

### Upload video

example:

```js
const tcVod = new TcVod.default({
  getSignature: getSignature // mentioned above
})

const uploader = tcVod.upload({
  videoFile: videoFile, // video. type should be Filev
})
uploader.on('video_progress', function(info) {
  console.log(info.percent)
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
uploader.done().then(function (doneResult) {
  // deal with doneResult
})

```

## Advanced

### Upload both video and cover

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
})

uploader.done().then(function (doneResult) {
  // deal with doneResult
})
```

### Get upload progress

Use callback to get progress

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
})
// when video upload finish
uploader.on('video_upload', function(info) {
  uploaderInfo.isVideoUploadSuccess = true;
})
// video progress
uploader.on('video_progress', function(info) {
  uploaderInfo.progress = info.percent;
})
// when cover upload finish
uploader.on('cover_upload', function(info) {
  uploaderInfo.isCoverUploadSuccess = true;
})
// cover progress
uploader.on('cover_progress', function(info) {
  uploaderInfo.coverProgress = info.percent;
})

uploader.done().then(function (doneResult) {
  // deal with doneResult
})

```

### Cancel upload

You can cancel upload when uploading video or cover

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
})

uploader.cancel()
```

### Resume from break point

SDk support resume from break point automatically. When upload break accidently, just re-upload the same file.

## Interface

### TcVod

| arg name         | required   | type       | description      |
| ------------ | ---- | -------- | --------- |
| getSignature    | Y    | Function     | 获取上传签名的函数  |

### TcVod.upload

| arg name         | required   | type       | description      |
| ------------ | ---- | -------- | --------- |
| videoFile    | N    | File     | video to upload   |
| coverFile    | N    | File     | cover to upload   |
| videoName    | N    | string     | specify a name other than File meta info  |
| fileId    | N    | string     | provide when alter cover  |

### Events

| event name         | required   |  description      |
| ------------ | ---- |  --------- |
| video_upload    | 否    |  when video upload success  |
| cover_upload    | 否    |  callback when cover upload success  |
| video_progress    | 否    |  video progress callback  |
| cover_progress    | 否    |  cover progress callback  |


## FAQ

1. How can I get a `File` object？
Use html `input` tag

2. Is there any file size limit?
Yes. Max is 60GB

3. Which browser do you support？
Any browser has ES5 engine.



  ​

  ​

  ​