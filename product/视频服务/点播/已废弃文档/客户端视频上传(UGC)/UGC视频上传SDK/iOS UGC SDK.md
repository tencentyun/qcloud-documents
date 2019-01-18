## SDK集成

### 下载SDK
下载[TVCClientSDK.framework](https://mc.qcloudimg.com/static/archive/968464cff8b4e4238a93cec6fe177c46/TVCClientSDK.framework_ios_1.0.2.zip)。

### 引入依赖包

![](http://mc.qcloudimg.com/static/img/397fddc2dffe71787a849e279e8864b1/image.png)

### 配置项目
Build Settings -> Other Linker Flags

![](http://mc.qcloudimg.com/static/img/1363842b36c56ecee4230c9e86fec473/image.png)

**注意事项：**

* libCOSClient.a有模拟器和真机版本，请在不同的开发环境使用对应的版本
* 务必强制加载libCOSClient.a静态库，否则会导致crash

## 本地视频上传

### Step1：生成上传对象

```objectivec
TVCConfig *config = [[TVCConfig alloc] init];
config.signature = signature;
config.secretId = secretId;
config.forceHttps = NO;
self.client = [[TVCClient alloc] initWithConfig:config];
```

### Step2：生成上传参数

```objectivec
TVCUploadParam *param = [[TVCUploadParam alloc] init];
param.videoPath = videoPath;
param.coverPath = coverPath;
```

### Step3：视频上传

```objectivec
[ws.client uploadVideo:param result:^(TVCUploadResponse *resp) {
        NSLog(@"result : %d-%@-%@-%@-%@",
                resp.retCode,
                resp.descMsg,
                resp.videoId,resp.videoURL,
                resp.coverURL);
} progress:^(NSInteger bytesUpload, NSInteger bytesTotal) {
        NSLog(@"progress : %ld-%ld",
                (long)bytesUpload,
                (long)bytesTotal);
}];
```

**注意事项：**

* TVCConfig参数字段不能为空；
* TVCUploadParam参数字段video路径不能为空，cover字段为空表示不上传封面预览图；
* 苹果规定2017年后所有上架App强制使用ATS，目前Http或https服务均可配置使用，苹果强制使用ATS后可在TVCConfig中配置使用Https协议。
