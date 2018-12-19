## 简介

iOS 平台的客户端上传 SDK，可向腾讯云点播系统上传视频和封面文件。

## 集成方式
### 下载 SDK

下载 [iOS SDK](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSSimple2.0.2.2801.zip)，引入依赖包。

![](http://mc.qcloudimg.com/static/img/397fddc2dffe71787a849e279e8864b1/image.png)

### 配置项目

位置：***Build Settings -> Other Linker Flags***

![](http://mc.qcloudimg.com/static/img/1363842b36c56ecee4230c9e86fec473/image.png)

***注意***

* libCOSClient.a 有模拟器和真机版本，请根据开发环境使用对应的版本
* 务必强制加载 libCOSClient.a 静态库，否则会导致 crash

## 上传步骤

### 第一步：初始化

初始化操作，指定上传使用的密钥、签名等信息。

| 参数名称 | 必填 | 类型 | 含义 |
| --- | --- | --- | --- |
| secretId | 是 | String | [云 API 密钥](https://console.cloud.tencent.com/capi)的 Secret ID |
| signature | 是 | String | 从 APP 服务器获取的[上传签名](/document/product/266/9221) |
| forceHttps | 是 | Bool | 是否只允许使用 HTTPS 协议 |

```objectivec
TVCConfig *config = [[TVCConfig alloc] init];
config.secretId = secretId;
config.signature = signature;
config.forceHttps = YES;
self.client = [[TVCClient alloc] initWithConfig:config];
```

### 第二步：指定上传目标

上传目标有视频和封面信息，如果只上传视频，则封面信息参数填空字符串。

| 参数名称 | 必填 |类型 | 含义 |
| --- | --- | --- | --- |
| videoPath | 是 | String | 视频文件路径 |
| coverPath| 否 | String | 封面图片路径，不填则默认为空字符串 |

仅上传视频：

```objectivec
TVCUploadParam *param = [[TVCUploadParam alloc] init];
param.videoPath = videoPath;
```

同时上传视频和封面：

```objectivec
TVCUploadParam *param = [[TVCUploadParam alloc] init];
param.videoPath = videoPath;
param.coverPath = coverPath;
```

### 第三步：执行上传操作

```objectivec
[ws.client uploadVideo:param result:^(TVCUploadResponse *resp) {
        NSLog(@"错误码：%d, 错误信息：%@, "，
               "上传成功的视频文件ID：%@, ",
               "上传视频的播放地址：%@, ",
               "上传封面的展示地址：%@, ",
                resp.retCode, resp.descMsg,
                resp.videoId, resp.videoURL, resp.coverURL);
} progress:^(NSInteger bytesUpload, NSInteger bytesTotal) {
        NSLog(@"上传进度: 已完成%ld，总数%ld",
                (long)bytesUpload,
                (long)bytesTotal);
}];
```