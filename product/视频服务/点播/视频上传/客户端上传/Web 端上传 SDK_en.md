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
async function getSignature() {
  const response = await axios.post(url)
  const signature = response.data.signature
  return signature
};
```

> `url` Your url which can return signature. Refer to [客户端上传指引](/document/product/266/9219)。
> `signature` Refer to for the computation of signature [客户端上传签名](/document/product/266/9221)。

### Upload video

example:

```js
async () => {
  const tcVod = new TcVod.default({
    getSignature: getSignature // mentioned above
  })

  const uploader = tcVod.upload({
    videoFile: videoFile, // video. type should be File
    progress(info) {
      console.log(info.percent)
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

## Advanced

### Upload both video and cover

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
})

const doneResult = await uploader.done()
```

### Get upload progress

Use callback to get progress

```js
const uploader = tcVod.upload({
  videoFile: videoFile,
  coverFile: coverFile,
  // when video upload finish
  cosSuccess(info) {
    uploaderInfo.isVideoUploadSuccess = true;
  },
  // video progress
  progress(info) {
    uploaderInfo.progress = info.percent;
  },
  // when cover upload finish
  cosCoverSuccess(info) {
    uploaderInfo.isCoverUploadSuccess = true;
  },
  // cover progress
  coverProgress(info) {
    uploaderInfo.coverProgress = info.percent;
  },
})

const doneResult = await uploader.done()
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
| cosSuccess    | N    | Function     | callback when video upload success  |
| cosCoverSuccess    | N    | Function     | callback when cover upload success  |
| progress    | N    | Function     | video progress callback   |
| coverProgress    | N    | Function     | cover progress callback  |
| videoName    | N    | string     | specify a name other than File meta info  |
| fileId    | N    | string     | provide when alter cover  |

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