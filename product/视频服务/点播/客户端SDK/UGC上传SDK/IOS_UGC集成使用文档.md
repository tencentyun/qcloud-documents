#UGC集成使用文档

> * 下载SDK
> * SDK集成
> * 使用流程

##下载SDK
点击下载[TVCClientSDK.framework](https://www.qcloud.com/doc/product/266/6965)和[libCOSClient.a](https://www.qcloud.com/doc/product/436/6530)。

##SDK集成
#####1. 引入依赖包

![](http://mc.qcloudimg.com/static/img/397fddc2dffe71787a849e279e8864b1/image.png)

#####2. 配置项目
Build Settings -> Other Linker Flags

![](http://mc.qcloudimg.com/static/img/1363842b36c56ecee4230c9e86fec473/image.png)

**注意事项：**

* libCOSClient.a有模拟器和真机版本，请在不同的开发环境使用对应的版本
* 务必强制加载libCOSClient.a静态库，否则会导致crash

##使用流程

#####1. 生成上传对象

```
TVCConfig *config = [[TVCConfig alloc] init];
config.signature = signature;
config.secretId = secretId;
config.forceHttps = NO;
self.client = [[TVCClient alloc] initWithConfig:config];
```

#####2. 生成上传参数

```
TVCUploadParam *param = [[TVCUploadParam alloc] init];
param.videoPath = videoPath;
param.coverPath = coverPath;
```

#####3. 开始上传

```
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

* TVCConfig参数字段不能为空
* TVCUploadParam参数字段video路径不能为空，cover字段为空表示不上传封面预览图
* 苹果规定2017年后所有上架App强制使用ATS，目前仅提供Http服务，提供Https服务后可在TVCConfig中配置使用Https协议