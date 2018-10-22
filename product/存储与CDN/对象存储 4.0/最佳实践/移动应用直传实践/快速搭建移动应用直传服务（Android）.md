## 背景
本文主要介绍如何在 Android 环境下快速搭建一个基于 COS 的应用传输服务，在腾讯云 COS 上实现应用数据的上传下载，在您的服务器上只需要部署您自己的业务、生成和管理临时密钥。

## 环境要求

- 一台安装了 Python3 环境的服务器；
- 一台 Android 4.0（api level 15）及以上版本的手机；
- Android Studio 开发环境。

## 准备

- 在 [COS 控制台](https://console.cloud.tencent.com/cos/bucket) 上创建一个 Bucket；

## 搭建临时密钥服务

### 安装 cossign

cossign 目前只支持 Python3，它可以给您提供临时密钥服务，您可以直接使用 pip 进行安装：

```
pip3 install cossign
```
### 运行 cossign

安装后，您可以运行如下命令启动临时密钥服务（您可以不指定端口号，默认为 5000）：

```
cossign --secret_id your_secret_id --secret_key your_secret_key --port 5000
```

### 测试服务

运行成功后，您可以直接 curl 如下地址：`http://your_server_ip:5000/sign`

若返回如下信息，则说明服务已经成功运行：

```
 {
 "code":0,
 "message":"",
 "codeDesc":"Success",
 "data":{
  "credentials":{
   "sessionToken":"634aa09dccc3274045ba413ec081c1df64007f0a30001",
   "tmpSecretId":"AKIDwxHZGTUvXAfcbLaOedJUQuwBXWUXG4m3",
   "tmpSecretKey":"kriDdZsOuuF9zrZPlSAVVG0Sg4RXZu6M"},
  "expiredTime":1530515889}
 }
```

更多搭建临时密钥服务，请参考 [搭建临时密钥服务](https://cloud.tencent.com/document/product/436/19134)。


## 创建 COS 传输项目

### 第一步：创建一个空的 Android 工程

利用 Android Studio 创建一个空的 Android 工程，并命名为 COSTranferPractice。

### 第二步：集成 COS SDK

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
### 第三步：配置权限

#### 声明权限

使用该 SDK 需要网络、存储等相关的一些访问权限，可在 AndroidManifest.xml 中增加如下权限声明（Android 5.0 以上还需要动态获取权限）：

```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

#### 给 `MainActivity` 添加动态请求权限代码

```
public class MainActivity extends AppCompatActivity {

    private final int PERMISSIONS_REQUEST_WRITE_EXTERNAL_STORAGE = 10001;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        requestPermissions();
    }

    private void requestPermissions() {

        if (ContextCompat.checkSelfPermission(this,
                Manifest.permission.WRITE_EXTERNAL_STORAGE)
                != PackageManager.PERMISSION_GRANTED) {

            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},
                    PERMISSIONS_REQUEST_WRITE_EXTERNAL_STORAGE);
        }
    }
}
```

### 第四步：修改 `activity_main.xml` 增加上传下载按钮

```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/upload"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_marginBottom="8dp"
        android:layout_marginEnd="8dp"
        android:layout_marginLeft="8dp"
        android:layout_marginRight="8dp"
        android:layout_marginStart="8dp"
        android:onClick="onUploadClick"
        android:text="上传"
        app:layout_constraintBottom_toTopOf="@+id/download"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent" />

    <Button
        android:id="@+id/download"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_marginBottom="8dp"
        android:layout_marginEnd="8dp"
        android:layout_marginLeft="8dp"
        android:layout_marginRight="8dp"
        android:layout_marginStart="8dp"
        android:onClick="onDownloadClick"
        android:text="下载"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent" />

</android.support.constraint.ConstraintLayout>
```

### 第五步：初始化 COS 服务传输类

在 `MainActivity` 中定义 COS 服务类 `CosXmlService` 和传输类 `TransferManager`，其中 `TransferManager` 传输管理类封装了进一步封装了 `CosXmlService` 的上传和下载接口，当您需要上传文件到 COS 或者从 COS 下载文件时，请优先使用这个类。

> 注意修改 appid、region 和 signUrl 三个参数

```
public class MainActivity extends AppCompatActivity {

    private final int PERMISSIONS_REQUEST_WRITE_EXTERNAL_STORAGE = 10001;

    private CosXmlService cosXmlService; // COS 服务类
    private TransferManager transferManager; // 传输类

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initCosService();
        requestPermissions();
    }

	/**
     * 初始化 COS 服务类和传输类对象。
     */
    private void initCosService() {

        String appid = "1252386093"; // appid
        String region = "ap-guangzhou"; // bucket 的地域
        String signUrl = "https://rickenwang-1252386093.cos.ap-guangzhou.myqcloud.com/sign.json"; // 临时密钥服务地址

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
}
```


### 第六步：增加上传下载点击回调

给上传下载按钮分别添加点击响应函数 `onUploadClick` 和 `onDownloadClick`：

> 注意需要分别修改上传和下载时的 bucket、cosPath、localPath 和 localDirPath 参数。

```
public class MainActivity extends AppCompatActivity {

    private final int PERMISSIONS_REQUEST_WRITE_EXTERNAL_STORAGE = 10001;

    private CosXmlService cosXmlService;
    private TransferManager transferManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
		 initCosService();
        requestPermissions();
    }

    /**
     * 点击上传按钮回调函数
     */
    public void onUploadClick(View view) {

        String bucket = "rickenwang-1252386093"; // bucket 名称
        String cosPath = "10Mfile.txt"; // 上传到 COS 的路径
        String localPath = Environment.getExternalStorageDirectory() + "/download_10Mfile.txt"; // 本地文件路径

        TransferConfig transferConfig = new TransferConfig.Builder().build();
        TransferManager transferManager = new TransferManager(cosXmlService, transferConfig);

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

    /**
     * 点击下载按钮回调函数
     */
    public void onDownloadClick(View view) {

        String bucket = "rickenwang-1252386093"; // bucket 名称
        String cosPath = "10Mfile.txt"; // COS 的下载路径
        String localDirPath = Environment.getExternalStorageDirectory().getAbsolutePath(); // 本地保存的文件目录

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

}
```

### 运行传输项目

完成以上六个步骤后，您可以依次点击上传和下载按钮来进行传输测试，上传成功后，您可以在 [COS 控制台](https://console.cloud.tencent.com/cos/bucket) 上查看您上传的文件，或者在本地查看你下载成功的文件，如果您开启了 Debug 模式，那么您也可以在 logcat 中查看传输日志。

[项目 Github 地址 >>](https://github.com/tencentyun/qcloud-sdk-android-samples/tree/master/COSTransfer)

## 体验

搭建好临时密钥服务后，您可以安装我们提供的 demo 即可快速体验 COS 服务：

> 体验 demo 也可以使用永久密钥授权，但不建议您在生产环境下使用

### 下载 APK 文件

您可以用 Android 手机扫描二维码直接下载 apk 文件：

![](https://main.qcloudimg.com/raw/2687b91ad1d02d335a9f264411275318.png)
 

[项目 GitHub 地址 >>](https://github.com/tencentyun/qcloud-sdk-android-samples/tree/master/COSTransferPractice)
