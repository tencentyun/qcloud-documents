

## 简介

Android平台的客户端上传SDK，可向腾讯云点播系统上传视频和封面文件。

### 集成方式

下载[TVCClientSDK.framework]()，引入依赖包。

![](http://mc.qcloudimg.com/static/img/397fddc2dffe71787a849e279e8864b1/image.png)

### 配置项目

位置：Build Settings -> Other Linker Flags

![](http://mc.qcloudimg.com/static/img/1363842b36c56ecee4230c9e86fec473/image.png)

**注意**

* libCOSClient.a有模拟器和真机版本，请根据开发环境使用对应的版本
* 务必强制加载libCOSClient.a静态库，否则会导致crash

## 本地视频上传步骤

### 第一步：初始化

初始化操作，指定上传使用的密钥、签名等信息。

| 参数名称 | 必填 | 类型 | 含义 |
| --- | --- | --- | --- |
| secretId | 是 | String | [云API密钥](https://console.qcloud.com/capi)的Secret ID |
| signature | 是 | String | 从APP服务器获取的[客户端签名]() |
| forceHttps | 否 | Bool | 是否只允许使用HTTPS协议 |

```objectivec
TVCConfig *config = [[TVCConfig alloc] init];
config.secretId = secretId;
config.signature = signature;
config.forceHttps = NO;
self.client = [[TVCClient alloc] initWithConfig:config];
```

### 第二步：指定上传目标

指定上传目标的参数有视频和封面信息。如果只上传视频，则封面路径参数填空字符串。

| 参数名称 | 必填 |类型 | 含义 |
| --- | --- | --- | --- |
| videoPath | 是 | String | 视频文件路径 |
| coverPath| 否 | String | 封面图片路径，不填则默认为空字符串 |

仅上传视频：

```objectivec
TVCUploadParam *param = [[TVCUploadParam alloc] init];
param.videoPath = videoPath;
param.coverPath = coverPath;
```

同时上传视频和封面：

```objectivec
TVCUploadParam *param = [[TVCUploadParam alloc] init];
param.videoPath = videoPath;
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