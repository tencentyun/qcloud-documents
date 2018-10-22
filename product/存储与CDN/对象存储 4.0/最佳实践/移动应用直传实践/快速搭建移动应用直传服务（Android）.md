## 背景
本文主要介绍如何在 Android 环境下快速搭建一个基于 COS 的应用传输服务，在腾讯云 COS 上实现应用数据的上传下载，在您的服务器上只需要部署您自己的业务、生成和管理临时密钥。

## 环境要求

- 一台服务端机器；
- 一台 Android 4.0（api level 15）及以上版本的手机；
- Android Studio 开发环境。

> 如果您暂时没有服务端机器，那么将无法接入临时密钥服务，您可以参考 [快速入门](https://cloud.tencent.com/document/product/436/12159) 中，通过永久密钥进行授权（不建议），同时您也可以运行本文底部的体验 demo 来访问您的 COS 服务。

## 准备

- 在 [COS 控制台](https://console.cloud.tencent.com/cos/bucket) 上创建一个 Bucket；
- [接入临时密钥服务](https://cloud.tencent.com/document/product/436/19134)。

> 为了您永久密钥的安全性，我们强烈建议您通过接入临时密钥服务来进行授权。

## 搭建 COS 传输服务

### 第一步：集成 COS SDK

1、在您的项目根目录下的 build.gradle 文件中添加 maven 仓库：

```
 allprojects {

    repositories {
        ...
        // 添加如下 maven 仓库地址
        maven {
            url "https://dl.bintray.com/tencentqcloudterminal/maven"
        }
    }
}
```
2、在应用的根目录下的 build.gradle 中添加依赖：

```
 dependencies {
    ...
    // 增加这行
    implementation 'com.tencent.qcloud:cosxml:5.4.+'
}
```
### 第二步：增加权限

1、声明权限

COS SDK 需要网络、存储等相关的一些访问权限，可在 AndroidManifest.xml 中增加如下权限声明（Android 5.0 以上还需要动态获取权限）：

```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

2、添加动态请求权限代码

如果您的 app 需要运行在 Android 6.0 及其以上版本，则需要增加如下代码来动态获取文件读写权限：

```
private void requestPermissions() {

    if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE)
            != PackageManager.PERMISSION_GRANTED) {

        ActivityCompat.requestPermissions(this,
                new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},
                PERMISSIONS_REQUEST_WRITE_EXTERNAL_STORAGE);
    }
}
```

### 第三步：初始化 COS 服务传输类

您在通过 COS 服务进行上传下载时，必须首先依次初始化 COS 服务类 `CosXmlService` 和传输类 `TransferManager`，其中 `TransferManager` 传输管理类封装了进一步封装了 `CosXmlService` 的上传和下载接口，当您需要上传文件到 COS 或者从 COS 下载文件时，请优先使用 `TransferManager`。

1、分别定义 `CosXmlService` 和 `TransferManager` 类型的成员变量

```
private CosXmlService cosXmlService;
private TransferManager transferManager;

```

2、初始化 COS 服务传输类

在使用 COS 传输服务前，您可以调用如下代码来进行初始化：

```
 /**
 * 初始化 COS 服务类和传输类对象。
 *
 * @params appid  appid
 * @params region bucket 的地域
 * @params signUrl 临时密钥的访问地址（在接入临时密钥服务处获得）
 */
private void initCosService(String appid, String region, String signUrl) {

    CosXmlServiceConfig cosXmlServiceConfig = new CosXmlServiceConfig.Builder()
            .setAppidAndRegion(appid, region)
            .setDebuggable(true)
            .builder();

    URL url = null;

    try {
        url = new URL(signUrl);
    } catch (MalformedURLException e) {
        e.printStackTrace();
    }

    /**
     * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥。
     */
    QCloudCredentialProvider credentialProvider = new SessionCredentialProvider(new HttpRequest.Builder<String>()
            .url(url)
            /**
             * 注意这里的 HTTP method 为 GET，请根据您自己密钥服务的发布方式进行修改
             */
            .method("GET")
            .build());

    cosXmlService = new CosXmlService(this, cosXmlServiceConfig, credentialProvider);

    TransferConfig transferConfig = new TransferConfig.Builder().build();
    transferManager = new TransferManager(cosXmlService, transferConfig);
}

```


### 第四步：上传和下载文件

#### 上传文件

您可以调用如下代码将本地文件上传到 COS 上：

```
/**
 * 上传
 *
 * @params bucket  bucket 名称
 * @params cosPath 上传到 COS 的路径
 * @params localPath 本地文件路径
 */
public void upload(String bucket, String cosPath, String localPath) {

    // 开始上传，并返回生成的 COSXMLUploadTask
    COSXMLUploadTask cosxmlUploadTask = transferManager.upload(bucket, cosPath,
            localPath, null);

    // 设置上传状态监听
    cosxmlUploadTask.setTransferStateListener(new TransferStateListener() {
        @Override
        public void onStateChanged(final TransferState state) {
            // TODO: 2018/10/22
        }
    });

    // 设置上传进度监听
    cosxmlUploadTask.setCosXmlProgressListener(new CosXmlProgressListener() {
        @Override
        public void onProgress(final long complete, final long target) {
            // TODO: 2018/10/22
        }
    });

    // 设置结果监听
    cosxmlUploadTask.setCosXmlResultListener(new CosXmlResultListener() {
        @Override
        public void onSuccess(CosXmlRequest request, CosXmlResult result) {
            // TODO: 2018/10/22
        }

        @Override
        public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
            // TODO: 2018/10/22
        }
    });
}

```


#### 下载文件

您可以调用如下代码从 COS 上下载文件：

```
/**
 * 下载
 *
 * @params bucket  bucket 名称
 * @params cosPath COS 的下载路径
 * @params localPath 本地保存的文件目录
 */
public void download(String bucket, String cosPath, String localDirPath) {

    // 开始下载，并返回生成的 COSXMLDownloadTask
    COSXMLDownloadTask cosxmlDownloadTask = transferManager.download(this, bucket, cosPath,
            localDirPath);

    // 设置下载状态监听
    cosxmlDownloadTask.setTransferStateListener(new TransferStateListener() {
        @Override
        public void onStateChanged(final TransferState state) {
            // TODO: 2018/10/22
        }
    });

    // 设置下载进度监听
    cosxmlDownloadTask.setCosXmlProgressListener(new CosXmlProgressListener() {
        @Override
        public void onProgress(final long complete, final long target) {
            // TODO: 2018/10/22
        }
    });

    // 设置下载结果监听
    cosxmlDownloadTask.setCosXmlResultListener(new CosXmlResultListener() {
        @Override
        public void onSuccess(CosXmlRequest request, CosXmlResult result) {
            // TODO: 2018/10/22
        }

        @Override
        public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
            // TODO: 2018/10/22
        }
    });
}

```

### 运行传输项目

完成以上四个步骤接入 COS 服务后，您可以调用上传和下载代码来进行传输测试，上传成功后，您可以在 [COS 控制台](https://console.cloud.tencent.com/cos/bucket) 上查看您上传的文件，或者在本地查看你下载成功的文件，如果您开启了 Debug 模式，那么您也可以在 logcat 中查看传输日志。

[项目 Github 地址 >>](https://github.com/tencentyun/qcloud-sdk-android-samples/tree/master/COSTransfer)

## 体验

搭建好临时密钥服务后，您可以安装我们提供的 demo 即可快速体验 COS 服务：

> 体验 demo 也可以使用永久密钥授权，但不建议您在生产环境下使用

### 下载 APK 文件

您可以用 Android 手机扫描二维码直接下载 apk 文件：

![](https://main.qcloudimg.com/raw/2687b91ad1d02d335a9f264411275318.png)
 

[项目 GitHub 地址 >>](https://github.com/tencentyun/qcloud-sdk-android-samples/tree/master/COSTransferPractice)
