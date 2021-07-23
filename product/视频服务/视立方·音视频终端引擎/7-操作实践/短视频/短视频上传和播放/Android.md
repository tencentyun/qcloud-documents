## SDK 版本
本页文档所描述功能，在 SDK 版本中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 纯播放 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/dev/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/dev/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/dev/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/dev/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/dev/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/dev/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978?!preview&!editLang=zh)。



## 对接流程 

短视频发布是将 MP4 文件上传到腾讯视频云，并获得在线观看 URL， 腾讯视频云满足视频观看的就近调度、秒开播放、动态加速以及海外接入等要求，确保了优质的观看体验。
![](https://main.qcloudimg.com/raw/e2bb82d070e95745ae83d30fe19e07ef.png)

1. 使用 TXUGCRecord 接口录制一段小视频，录制结束后会生成一个小视频文件（MP4）回调给客户。
2. App 向您的业务服务器申请上传签名（App 将 MP4 文件上传到腾讯云视频分发平台的“许可证”）。为了确保安全性，上传签名由您的业务 Server 进行签发，而不能由终端 App 生成。
3. 使用 TXUGCPublish 接口发布视频，发布成功后，SDK 会将观看地址的 URL 回调给您。

## 注意事项

- App 不能把计算上传签名的 SecretID 和 SecretKey 写在客户端代码里，这两个关键信息泄露将导致安全隐患，如果恶意攻击者通过破解 App 来获取该信息，则可以免费使用您的流量和存储服务。
- 正确的做法是在您的服务器上，用  SecretID 和 SecretKey 生成一次性的上传签名，然后将签名交给 App。
- 发布短视频时，请务必正确传递 Signature 字段，否则会发布失败。

## 对接攻略
![](https://main.qcloudimg.com/raw/bbad8084d65a3ad14cd5d089978b6628.png)

请参见 [Android 上传 SDK](https://cloud.tencent.com/document/product/266/9539) 来接入短视频上传功能。

[](id:step1)
### 1. 选择视频
将录制、编辑、拼接后的视频进行上传，或者选择本地视频进行上传。

[](id:step2)
### 2. 压缩视频
 - 压缩视频会减小视频文件的大小，同时也会降低视频的清晰度，您可以按需决定是否进行压缩。
 - 对视频进行压缩，使用 [TXVideoEditer.generateVideo(int videoCompressed, String videoOutputPath)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#af3f16bcb21f26c608c980b91671e386e) 接口，支持4种分辨率的压缩，后续会增加自定义码率的压缩。

[](id:step3)
### 3. 发布视频
将生成的 MP4 文件发布到腾讯云上，App 需要拿到上传文件的短期有效上传签名，详细请参见 [签名派发](https://cloud.tencent.com/document/product/1449/59084?!preview&!editLang=zh)。TXUGCPublish（位于 TXUGCPublish.java）负责将 MP4 文件发布到腾讯云视频分发平台上，以满足视频观看的就近调度、秒开播放、动态加速以及海外接入等要求。
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
发布的过程和结果通过 TXRecordCommon.ITXVideoPublishListener（位于 TXRecordCommon.java 头文件中）接口反馈：
- onPublishProgress 用于反馈发布进度，参数 uploadBytes 表示已上传的字节数，参数 totalBytes 表示需要上传的总字节数。
```java
void onPublishProgress(long uploadBytes, long totalBytes);
```
- onPublishComplete 用于反馈发布结果。
```java
void onPublishComplete(TXPublishResult result);
```
	参数 TXPublishResult 中的字段及含义如下表所示：
	<table border=0 cellpadding="0" cellspacing="0">
	<thead><tr><th>字段</th><th align="center">含义</th></tr></thead>
	<tbody><tr>
	<td>errCode</td>
	<td >错误码。</td>
	</tr> <tr>
	<td>descMsg</td>
	<td >错误描述信息。</td>
	</tr> <tr>
	<td>videoURL</td>
	<td >短视频的点播地址。</td>
	</tr> <tr>
	<td>coverURL</td>
	<td >视频封面的云存储地址。</td>
	</tr> <tr>
	<td>videoId</td>
	<td >视频文件云存储 ID，您可以通过这个 ID 调用云点播 <a href = "https://cloud.tencent.com/document/product/266/7788">服务端 API 接口</a>。</td>
	</tr>
	</tbody></table> 
- 通过 [错误码表](https://cloud.tencent.com/document/product/584/10176) 来确认短视频的发布结果。

[](id:step4)

### 4. 播放视频

[第3步](#step3) 发布视频成功后，会返回视频的 fileId、播放地址 URL 及封面 URL，然后在 [点播播放器](https://cloud.tencent.com/document/product/584/9373) 中传入 fileId 或 URL 进行视频播放。
