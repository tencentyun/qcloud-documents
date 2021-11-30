## 计算上传签名
客户端视频上传，是指 App 的最终用户将本地视频直接上传到腾讯云点播。客户端上传的详细介绍请参见点播 [客户端上传指引](https://cloud.tencent.com/document/product/266/9219)，本文将以最简洁的方式介绍客户端上传的签名生成方法。

### 总体介绍
客户端上传的整体流程如下图所示：
![图片描述](https://main.qcloudimg.com/raw/3c9b427ba32f5f23c352d339a3e45af8.jpg)
为了支持客户端上传，开发者需要搭建两个后台服务：签名派发服务和事件通知接收服务。

* 客户端首先向签名派发服务请求上传签名。
* 签名派发服务校验该用户是否有上传权限，若校验通过，则生成签名并下发；否则返回错误码，上传流程结束。
* 客户端拿到签名后使用短视频 SDK 中集成的上传功能来上传视频。
* 上传完成后，点播后台会发送 [上传完成事件通知](https://cloud.tencent.com/document/product/266/7830) 给开发者的事件通知接收服务。
* 如果签名派发服务在签名中指定了视频处理 [任务流](https://cloud.tencent.com/document/product/266/33475#.E4.BB.BB.E5.8A.A1.E6.B5.81)，点播服务会在视频上传完成后根据指定流程自动进行视频处理。短视频场景下的视频处理一般为 [AI 鉴黄](https://cloud.tencent.com/document/product/266/33498)。
* 视频处理完成之后，点播后台会发送 [任务流状态变更事件通知](https://cloud.tencent.com/document/product/266/9636) 给开发者的事件通知接收服务。

至此整个视频上传-处理流程结束。

### 签名生成
有关客户端上传签名的详细介绍请参见点播 [客户端上传签名](https://cloud.tencent.com/document/product/266/9221)。

### 签名派发服务实现示例

``` 
/**
 * 计算签名
 */
function createFileUploadSignature({ timeStamp = 86400, procedure = '', classId = 0, oneTimeValid = 0, sourceContext = '' }) {
    // 确定签名的当前时间和失效时间
    let current = parseInt((new Date()).getTime() / 1000)
    let expired = current + timeStamp;  // 签名有效期：1天
    // 向参数列表填入参数
    let arg_list = {
        //required
        secretId: this.conf.SecretId,
        currentTimeStamp: current,
        expireTime: expired,
        random: Math.round(Math.random() * Math.pow(2, 32)),
        //opts
        procedure,
        classId,
        oneTimeValid,
        sourceContext
    }
    // 计算签名
    let orignal = querystring.stringify(arg_list);
    let orignal_buffer = new Buffer(orignal, "utf8");
    let hmac = crypto.createHmac("sha1", this.conf.SecretKey);
    let hmac_buffer = hmac.update(orignal_buffer).digest();
    let signature = Buffer.concat([hmac_buffer, orignal_buffer]).toString("base64");
    return signature;
}
/**
 * 响应签名请求
 */
function getUploadSignature(req, res) {
    res.json({
        code: 0,
        message: 'ok',
        data: {
            signature: gVodHelper.createFileUploadSignature({})
        }
    });
}
``` 

## 对接流程
#### 短视频发布
将 MP4 文件上传到腾讯视频云，并获得在线观看 URL， 腾讯视频云支持视频观看的就近调度、秒开播放、动态加速 以及海外接入等要求，从而确保优质的观看体验。
![](https://main.qcloudimg.com/raw/8b3e157465338369bc8b72ec2b7d7d0e.png)

* 第一步：使用 TXUGCRecord 接口录制一段小视频，录制结束后会生成一个小视频文件（MP4）回调给客户。
* 第二步：您的 App 向您的业务服务器申请上传签名。上传签名是 App 将 MP4 文件上传到腾讯云视频分发平台的“许可证”，为了确保安全性，这些上传签名都要求由您的业务 Server 进行签发，而不能由终端 App 生成。
* 第三步：使用 TXUGCPublish 接口发布视频，发布成功后 SDK 会将观看地址的 URL 回调给您。

### 特别注意

- App 千万不要把计算上传签名的 SecretID 和 SecretKey 写在客户端的代码里，这两个关键信息泄露将导致安全隐患，如恶意攻击者一旦破解 App 获取该信息，就可以免费使用您的流量和存储服务。
- 正确的做法是在您的服务器上用  SecretID 和 SecretKey 生成一次性的上传签名然后将签名交给 App。因为服务器一般很难被攻陷，所以安全性是可以保证的。
- 发布短视频时，请务必保证正确传递 Signature 字段，否则会发布失败。

### 对接攻略
![](https://main.qcloudimg.com/raw/a74a7a7ed81525b8ecb9e2ab5d841a46.png)

#### 1. 选择视频
可以接着上篇文档中的录制或者编辑，把生成的视频进行上传，或者可以选择手机本地的视频进行上传。
#### 2. 压缩视频
对选择的视频进行压缩，使用 TXVideoEditer.generateVideo(int videoCompressed, String videoOutputPath) 接口，支持4种分辨率的压缩，后续会增加自定义码率的压缩。
#### 3. 发布视频
把刚才生成的 MP4 文件发布到腾讯云上，App 需要拿到上传文件用的短期有效上传签名，这部分有独立的文档介绍，详情请参考 [签名派发](https://cloud.tencent.com/document/product/584/9371)。
TXUGCPublish（位于 TXUGCPublish.h）负责将 MP4 文件发布到腾讯云视频分发平台上，以确保视频观看的就近调度、秒开播放、动态加速以及海外接入等需求。

```ObjectiveC
TXPublishParam * param = [[TXPublishParam alloc] init];

param.signature = _signature;                                // 需要填写第四步中计算的上传签名

// 录制生成的视频文件路径 TXVideoRecordListener 的 onRecordComplete 回调中可以获取
param.videoPath = _videoPath;  
// 录制生成的视频首帧预览图路径。值为通过调用 startRecord 指定的封面路径，或者指定一个路径，然后将TXVideoRecordListener 的 onRecordComplete 回调中获取到的 UIImage 保存到指定路径下，可以置为 nil。
param.coverPath = _coverPath; 

TXUGCPublish *_ugcPublish = [[TXUGCPublish alloc] init];
// 文件发布默认是采用断点续传
_ugcPublish.delegate = self;                                 // 设置 TXVideoPublishListener 回调
[_ugcPublish publishVideo:param];
``` 

发布的过程和结果是通过 TXVideoPublishListener（位于 TXUGCPublishListener.h 头文件中定义）接口反馈出来的：

- onPublishProgress 用于反馈文件发布的进度，参数 uploadBytes 表示已经上传的字节数，参数 totalBytes 表示需要上传的总字节数。
```ObjectiveC 
@optional
-(void) onPublishProgress:(NSInteger)uploadBytes totalBytes: (NSInteger)totalBytes;
```
- onPublishComplete 用于反馈发布结果，TXPublishResult 的字段 errCode 和 descMsg 分别表示错误码和错误描述信息，videoURL 表示短视频的点播地址，coverURL 表示视频封面的云存储地址，videoId 表示视频文件云存储 Id，您可以通过这个 Id 调用点播 [服务端API接口](https://cloud.tencent.com/document/product/266/7788)。
``` C 
@optional
-(void) onPublishComplete:(TXPublishResult*)result;
```
- 发布结果
通过 [错误码表](https://cloud.tencent.com/document/product/584/10176) 来确认短视频发布的结果。


#### 4. 播放视频

第**3**步上传成功后，会返回视频的 fileId，播放地址 URL，封面 URL。用 [点播播放器](https://cloud.tencent.com/document/product/584/9372) 可以直接传入 fileId 播放，或者 URL 播放。
