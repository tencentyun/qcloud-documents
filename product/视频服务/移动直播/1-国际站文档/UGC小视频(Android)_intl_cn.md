
## 功能概述 
随着终端用户个性化的需求愈加丰富，简单的文字交互和图片上传已经不能满足展示与分享信息的诉求，UGC(User Generated Content)小视频也就应运而生。RTMP SDK目前已经支持 UGC 小视频的录制和发布（编辑功能尚在开发中），如下文档将介绍如何使用这个功能。

## 对接流程
UGC小视频录制与发布的整体流程分为如下三步：

![](http://mc.qcloudimg.com/static/img/283c8d7fe0a5a316097ae687a2bf6c5a/image.png)

* 第一步：使用 TXUGCRecord 接口录制一段小视频，录制结束后会生成一个小视频文件（MP4）回调给客户；

* 第二步：您的 APP 向您的业务服务器申请上传签名。上传签名是 APP 将 MP4 文件上传到腾讯云视频分发平台的 “许可证”，为了确保安全性，这些上传签名都是需要服务器签发并且做到单次有效。

* 第三步：使用 TXUGCPublish 接口发布视频，发布成功后 SDK 会将观看地址的 URL 回调给您，腾讯云视频分发平台会确保视频观看的就近调度、秒开播放、动态加速 以及海外接入等需要大成本投入才能实现的能力。

## 特别注意

- APP 千万不要把计算上传签名的 SecretID 和 SecretKey 写在客户端的代码里，这两个关键信息泄露将导致安全隐患，比如恶意攻击者一旦破解 APP 获取该信息，就可以免费使用您的流量和存储服务。

- 正确的做法是在您的服务器上用  SecretID 和 SecretKey 生成一次性的上传签名然后将签名交给 APP。因为服务器一般很难被攻陷，所以安全性是可以保证的。

- 发布小视频时，请务必保证正确传递 SecretID 和 Signature 字段，否则会发布失败；

- 对视频录制接口 startRecord 和 stopRecord 的调用必须保证配对；

- 视频录制时长由客户您的代码来控制，基于性能考虑，为了保证良好的用户体验，建议录制时长最长不超过60秒。


## 接口介绍 
RTMP SDK 提供了相关接口用来实现短视频的录制与发布，其详细定义如下：

|  接口文件 |  功能 |
| ------| --------|
| `TXUGCRecord.java` |实现小视频的录制功能|
| `TXUGCPublish.java` | 实现小视频的上传发布 |
| `TXRecordCommon.java` | 基本参数定义，包括了小视频录制回调及发布回调接口 |

## 对接攻略

![](http://mc.qcloudimg.com/static/img/6b21b033259c1b5124648b73e88fb243/image.png)


### 1. 画面预览
TXUGCRecord（位于 TXUGCRecord.java） 负责小视频的录制功能，我们的第一个工作是先把预览功能实现。startCameraSimplePreview函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```java
mTXCameraRecord = TXUGCRecord.getInstance(this.getApplicationContext());
mTXCameraRecord.setVideoRecordListener(this);					//设置录制回调
mVideoView = (TXCloudVideoView) findViewById(R.id.video_view);	//准备一个预览摄像头画面的TXCloudVideoView
mVideoView.enableHardwareDecode(true);
TXRecordCommon.TXUGCSimpleConfig param = new TXRecordCommon.TXUGCSimpleConfig();
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_LOW;		// 360p
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;		// 540p
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_HIGH;		// 720p
param.isFront = true;											//是否前置摄像头，使用 switchCamera 可以切换
mTXCameraRecord.startCameraSimplePreview(param,mVideoView);
```

### 2. 画面特效
不管是录制前，还是录制中，您都可以使用 TXUGCRecord 里的特效开关来为视频画面添加一些特效，或者是对摄像头本身进行控制。

```java
//////////////////////////////////////////////////////////////////////////
//                      以下为 1.9.1 版本后均支持的特效
//////////////////////////////////////////////////////////////////////////
//
// 切换前后摄像头 参数 mFront 代表是否前置摄像头 默认前置
mTXCameraRecord.switchCamera(mFront);

// 设置美颜 和 美白 效果级别
// beautyDepth     : 美颜级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
// whiteningDepth  : 美白级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
mTXCameraRecord.setBeautyDepth(beautyDepth, whiteningDepth);

// 设置颜色滤镜：浪漫、清新、唯美、粉嫩、怀旧...
// Bitmap     : 指定滤镜用的颜色查找表。注意：一定要用png格式！！！
// demo用到的滤镜查找表图片位于RTMPAndroidDemo/app/src/main/res/drawable-xxhdpi/目录下。
// setSpecialRatio : 用于设置滤镜的效果程度，从0到1，越大滤镜效果越明显，默认取值0.5
mTXCameraRecord.setFilter(filterBitmap);
mTXCameraRecord.setSpecialRatio(0.5);

// 是否打开闪光灯 参数 mFlashOn 代表是否打开闪关灯 默认关闭
mTXCameraRecord.toggleTorch(mFlashOn);

//////////////////////////////////////////////////////////////////////////
//                       以下为仅特权版才支持的特效
// （由于采用优图团队的知识产权，我们无法对外免费提供，需要使用特权版 SDK 才能支持）
//////////////////////////////////////////////////////////////////////////

// 设置动效贴纸 motionTmplPath 动效文件路径： 空String "" 则取消动效
mTXCameraRecord.setMotionTmp(motionTmplPath);
```


### 3. 文件录制
调用 TXUGCRecord 的 startRecord 函数即可开始录制，调用 stopRecord 函数即可结束录制，startRecord 和 stopRecord 的调用一定要配对。
```java
mTXCameraRecord.startRecord();
mTXCameraRecord.stopRecord();
``` 

录制的过程和结果是通过 TXRecordCommon.ITXVideoRecordListener（位于 TXRecordCommon.java 中定义）接口反馈出来的：

- onRecordProgress 用于反馈录制的进度，参数millisecond表示录制时长，单位毫秒:
```java
@optional
void onRecordProgress(long milliSecond);
``` 

- onRecordComplete 反馈录制的结果，TXRecordResult 的 retCode 和 descMsg 字段分别表示错误码和错误描述信息，videoPath 表示录制完成的小视频文件路径，coverImage 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。
```java   
@optional
void onRecordComplete(TXRecordResult result);
```     

### 4. 文件预览
使用 [播放SDK](https://cloud.tencent.com/document/product/454/7886) 即可预览刚才生成的 MP4 文件，需要在调用 startPlay 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/454/7886#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE.E5.99.A86) 。

### 5. 获取签名
要把刚才生成的 MP4 发布到腾讯云视频分发 CDN 上，就需要 **SecretID** 和 **Signature**，它的作用类似用户名和密码一样来确保您的云存储服务安全，避免您的流量和存储空间被其它攻击者盗用。

- **SecretID （密钥ID）**
你可以在 [云 API 密钥](https://console.cloud.tencent.com/capi) 管理里获取或者创建一个 SecretID，如下图红框标注部分：
![](http://mc.qcloudimg.com/static/img/23f95aaa97adf3eeae3bf90470fe5122/image.png)

- **Signature（上传签名）**
上传签名就是基于从腾讯云获取的 SecretID 和 SecretKey ，用一套标准的签名算法，算出的一段一次性有效的字符串。

 为了确保安全，需要您将计算签名的程序放在您的后台服务器上，而不是把计算函数写在 APP 里，因为破解 APP 并获取签名用的 SecretKey 是比较容易的事情，而要攻破您的服务器则并非是一般能力的攻击者能做得到的。

 签名计算方法参考：[如何生成签名？](https://cloud.tencent.com/document/product/266/7835) 生成发布签名时，<font color='red'>FileName、FileSha 以及 uid 字段都可以留空不填写。</font>

### 6. 文件发布
TXUGCPublish（位于 TXUGCPublish.java）负责将 MP4 文件发布到腾讯云视频分发平台上，以确保视频观看的就近调度、秒开播放、动态加速 以及海外接入等需求。

```java
mVideoPublish.setListener(this);      //设置发布回调
TXRecordCommon.TXPublishParam param = new TXRecordCommon.TXPublishParam();
param.secretId = "sdIDeqtlGihED4oqjRP2324seJn1313MLnxx"; // 需要填写您的 SecretId
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

- onPublishComplete 用于反馈发布结果，TXPublishResult 的字段 errCode 和 descMsg 分别表示错误码和错误描述信息，videoURL表示短视频的点播地址，coverURL表示视频封面的云存储地址，videoId表示视频文件云存储Id，您可以通过这个Id调用点播 [服务端API接口](https://cloud.tencent.com/document/product/266/1965)。
```java 
void onPublishComplete(TXPublishResult result);
```
