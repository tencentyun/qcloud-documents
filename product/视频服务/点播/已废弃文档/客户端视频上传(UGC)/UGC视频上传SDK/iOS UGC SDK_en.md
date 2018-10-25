## SDK Integration

### Download SDK
Download [TVCClientSDK.framework](https://cloud.tencent.com/doc/product/266/6965).

### Import Dependent Packages

![](http://mc.qcloudimg.com/static/img/397fddc2dffe71787a849e279e8864b1/image.png)

### Configure Project
Build Settings -> Other Linker Flags

![](http://mc.qcloudimg.com/static/img/1363842b36c56ecee4230c9e86fec473/image.png)

**Note:**

* There are both simulator version and real machine version for libCOSClient.a, please choose the corresponding version according to your development environment
* Make sure to force load the static library libCOSClient.a, otherwise crash will occur

## Local Video Upload

### Step1: Generate Upload Object

```objectivec
TVCConfig *config = [[TVCConfig alloc] init];
config.signature = signature;
config.secretId = secretId;
config.forceHttps = NO;
self.client = [[TVCClient alloc] initWithConfig:config];
```

### Step2: Generate Upload Parameter

```objectivec
TVCUploadParam *param = [[TVCUploadParam alloc] init];
param.videoPath = videoPath;
param.coverPath = coverPath;
```

### Step3: Upload Video

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

**Note:**

* TVCConfig parameter field cannot be empty;
* The video path of TVCUploadParam parameter field cannot be empty. An empty cover field means do not upload preview cover image;
* According to the regulations of Apple, all Apps put up in the Store after the start of 2017 are required to use ATS. Currently, both HTTP and HTTPS services can be configured for use. After Apple enforces the use of ATS, you can configure to use HTTPS protocol in TVCConfig.

