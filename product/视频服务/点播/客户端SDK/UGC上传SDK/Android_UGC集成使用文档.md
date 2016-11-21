#UGC集成使用文档

> * 下载SDK
> * SDK集成
> * 使用流程

##下载SDK

### iOS
点击下载[TVCClientSDK.framework](https://www.qcloud.com/doc/product/266/6965)和[libCOSClient.a](https://www.qcloud.com/doc/product/436/6530)。
### Android
点击下载[tvcsdk.zip](https://mc.qcloudimg.com/static/archive/ab5853a171024359000887545e260c2c/tvcsdk_201611041102.zip)

##SDK集成

### iOS
#####1. 引入依赖包

![](http://mc.qcloudimg.com/static/img/397fddc2dffe71787a849e279e8864b1/image.png)

#####2. 配置项目
Build Settings -> Other Linker Flags

![](http://mc.qcloudimg.com/static/img/1363842b36c56ecee4230c9e86fec473/image.png)

### Android

解压zip包，配置工程导入其中的jar包:
>* tvcsdk.jar
>* okio-1.6.0.jar
>* okhttp-3.2.0.jar
>* cos-sdk-android-1.4.2.jar

SDK需要网络访问相关的一些权限，需要在AndroidManifest.xml中增加如下权限说明:

```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

**注意事项：**

* libCOSClient.a有模拟器和真机版本，请在不同的开发环境使用对应的版本
* 务必强制加载libCOSClient.a静态库，否则会导致crash

##使用流程

### iOS
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

### Android
#####1. 创建上传对象

```java
TVCClient client = new TVCClient(getApplicationContext(), SecretId, Signature);
```

参数名称|参数类型|参数说明
:--|:--|:--:
context|Context|上下文
scretId|String|密钥
signature|String|签名

#####2. 创建上传配置

```java
TVCUploadInfo info = new TVCUploadInfo("mp4", videoPath, "jpg", coverPath);
```

参数名称|参数类型|参数说明
:--|:--|:--:
fileType|String|视频文件类型
filePath|String|视频文件路径
coverType|String|封面图片类型
coverPath|String|封面图片路径

#####3. 开始上传

```java
client.uploadVideo(info, new TVCUploadListener() {
            @Override
            public void onSucess(String fileId, String playUrl, String coverUrl) {
                Log.v(TAG, "uploadVideo->fileId:"+fileId);
                Log.v(TAG, "uploadVideo->playUrl:"+playUrl);
                Log.v(TAG, "uploadVideo->coverUrl:"+coverUrl);
            }

            @Override
            public void onFailed(int errCode, String errMsg) {
                Toast.makeText(MainActivity.this, "err " + errCode + "" 
                        + errMsg, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onProgress(long currentSize, long totalSize) {
                double percent = (double) currentSize / (double) totalSize;
                NumberFormat nt = NumberFormat.getPercentInstance();
                nt.setMinimumFractionDigits(2);
                Log.i("onProgess", "onProgress: " + nt.format(percent));
            }
        });
```

**注意事项：**

* coverType字段和coverPath字段传null表示不上传封面预览图