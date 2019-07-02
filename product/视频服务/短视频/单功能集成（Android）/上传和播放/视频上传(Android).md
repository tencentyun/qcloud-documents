
## 对接流程

- **短视频发布**：
  即将 MP4 文件上传到腾讯视频云，并获得在线观看 URL， 腾讯视频云支持视频观看的就近调度、秒开播放、动态加速 以及海外接入等要求，从而确保优质的观看体验。
![](//mc.qcloudimg.com/static/img/283c8d7fe0a5a316097ae687a2bf6c5a/image.png)

* 第一步：使用 TXUGCRecord 接口录制一段小视频，录制结束后会生成一个小视频文件（MP4）回调给客户；
* 第二步：您的 App 向您的业务服务器申请上传签名。上传签名是 App 将 MP4 文件上传到腾讯云视频分发平台的 “许可证”，为了确保安全性，这些上传签名都要求由您的业务 Server 进行签发，而不能由终端 App 生成。
* 第三步：使用 TXUGCPublish 接口发布视频，发布成功后 SDK 会将观看地址的 URL 回调给您。

## 特别注意

- App 千万不要把计算上传签名的 SecretID 和 SecretKey 写在客户端的代码里，这两个关键信息泄露将导致安全隐患，比如恶意攻击者一旦破解 App 获取该信息，就可以免费使用您的流量和存储服务。
- 正确的做法是在您的服务器上用  SecretID 和 SecretKey 生成一次性的上传签名然后将签名交给 App。因为服务器一般很难被攻陷，所以安全性是可以保证的。
- 发布短视频时，请务必保证正确传递 Signature 字段，否则会发布失败；

## 对接攻略
![](https://main.qcloudimg.com/raw/b3023cee1814e777e8458aa9b1047cbb.png)

您可以参考此篇文档进行短视频上传功能的接入：[云点播 - Android 上传 SDK](https://cloud.tencent.com/document/product/266/9539)。

### 1、选择视频
可以接着上几篇文档中的录制或者编辑或者拼接，把生成的视频进行上传，也可以选择手机本地的视频进行上传
### 2、压缩视频
 - 压缩视频会减小视频大小，但是也会降低视频的清晰度，您可以根据自己的需求决定是否进行压缩。
 - 对选择的视频进行压缩，使用TXVideoEditer.generateVideo(int videoCompressed, String videoOutputPath)接口，支持4种分辨率的压缩，后续会增加自定义码率的压缩。

### 3、发布视频
把刚才生成的 MP4 文件发布到腾讯云上，App 需要拿到上传文件用的短期有效上传签名，这部分有独立的文档介绍，详情请参考 [签名派发](https://cloud.tencent.com/document/product/584/9371)。
TXUGCPublish（位于 TXUGCPublish.java）负责将 MP4 文件发布到腾讯云视频分发平台上，以确保视频观看的就近调度、秒开播放、动态加速 以及海外接入等需求。

```java
mVideoPublish = new TXUGCPublish(TCVideoPublisherActivity.this.getApplicationContext());
// 文件发布默认是采用断点续传
TXUGCPublishTypeDef.TXPublishParam param = new TXUGCPublishTypeDef.TXPublishParam();
param.signature = mCosSignature;						// 需要填写第四步中计算的上传签名
// 录制生成的视频文件路径, ITXVideoRecordListener 的 onRecordComplete 回调中可以获取
param.videoPath = mVideoPath;
// 录制生成的视频首帧预览图，ITXVideoRecordListener 的 onRecordComplete 回调中可以获取
param.coverPath = mCoverPath;
mVideoPublish.publishVideo(param);
```

发布的过程和结果是通过 TXRecordCommon.ITXVideoPublishListener（位于 TXRecordCommon.java 头文件中定义）接口反馈出来的：

- onPublishProgress 用于反馈文件发布的进度，参数 uploadBytes 表示已经上传的字节数，参数 totalBytes 表示需要上传的总字节数。
```java
void onPublishProgress(long uploadBytes, long totalBytes);
```
- onPublishComplete 用于反馈发布结果，TXPublishResult 的字段 errCode 和 descMsg 分别表示错误码和错误描述信息，videoURL 表示短视频的点播地址，coverURL 表示视频封面的云存储地址，videoId 表示视频文件云存储 Id，您可以通过这个Id调用点播 [服务端 API 接口](https://cloud.tencent.com/document/product/266/1965)。
```java
void onPublishComplete(TXPublishResult result);
```
- 通过 [错误码表](https://cloud.tencent.com/document/product/584/10176) 来确认短视频发布的结果。



### 4、播放视频

- 第 3 步上传成功后，会返回视频的 fileId，播放地址 url，封面 url。用 [点播播放器](https://cloud.tencent.com/document/product/584/9373) 可以直接传入fileId播放，或者url播放。
