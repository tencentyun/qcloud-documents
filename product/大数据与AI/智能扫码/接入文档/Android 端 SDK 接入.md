## 开发准备

1. 注册腾讯云账号，提交智能扫码服务的申请，等待审核通过后，获得专属密钥。（申请地址：[智能扫码申请](https://console.cloud.tencent.com/ocr/is)）
2. 从 SDK 下载链接中下载智能扫码 SDK 到本地准备集成。



## Android 端智能扫码 SDK 接入流程

### Android 端智能扫码 SDK 介绍

SDK 文件为 **QBarCode-v0.1.2.aar**，该文件里面封装了智能扫码接口、so 文件、检测与超分模型的资源文件。

功能：提供实时识别一维码、二维码和图片内一、二维码检测识别的服务。



### 环境依赖

当前 Android 端智能扫码 SDK 适用于 API 19 (Android 4.4) 及以上版本。



### 接入步骤

1. 将 **QBarCode-v0.1.2.aar** 包添加到您的工程文件中的**libs**目录下。
2. 配置 **build**
在您的工程文件中的 **build.gradle** 中进行如下配置：
```groovy
   //使用 aar 时必须要设置
   android {
       //**
       defaultConfig {
          /***/
           ndk {
               abiFilters "armeabi-v7a","arm64-v8a"
           }
       }
     sourceSets {
           main {
             jniLibs.srcDirs = ['libs/jniLibs']
           }
       }
   }
   dependencies {
       implementation files('libs/QBarCode-v0.1.2.aar')
       // 智能扫码依赖第三方库
       implementation 'commons-io:commons-io:2.6'
   }
```
3. 权限申请
需要在 AndroidManifest.xml 文件中声明权限
```xml
   <!--摄像头使用权限-->
   <uses-feature android:name="android.hardware.camera" />
   <uses-permission
       android:name="android.permission.CAMERA"
       android:required="true" />
   <!--文件存储使用权限-->
   <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
   <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
   <uses-permission android:name="android.permission.INTERNET"/>
```

对于需要兼容 Android 6.0 以上的用户，以上权限除了需要在 AndroidManifest.xml 文件中声明权以外，还需使用代码动态申请权限。



### SDK 接口说明

#### sdk 初始化：

用户初始化智能扫码 SDK，SECRET_ID 与 SECRET_KEY 传入云服务后台申请的密钥信息（申请地址：[智能扫码申请](https://console.cloud.tencent.com/ocr/is)）
```java
   private QBarCodeKit qBarCodeKit;
   
   //Android 6及以上动态申请权限，权限通过后再初始化
   qBarCodeKit = QBarCodeKit.getInstance();
   qBarCodeKit.initQBarCodeKit(SECRET_ID, SECRET_KEY, MainActivity2.this, new QBarCodeKit.OnSdkKitInitCallback (){
     @Override
     public void onInitResult(String errCode, String errMsg) {
       //initAuth 执行时间可能有1-2s，当返回SUCCESS(0) 说明授权成功，再进行后面的操作
       Log.d("onInitResult：", "errCode:" + errCode + " errMsg:" + errMsg);
     }
});
```

#### 摄像头数据实时识别：

扫描 SDK 提供了 ScanCodeDetectView，用来方便您在自定义的 UI 界面里使用智能扫描功能。首先您需要在 UI 界面的布局文件中添加ScanCodeDetectView：
```xml
<com.tencent.scanlib.ui.ScanCodeDetectView
   android:id="@+id/scan_view"
   android:layout_width="match_parent"
   android:layout_height="match_parent"
   app:show="false"/><!--show 设置false-->
```
然后只需要在对应的界面代码中为 ScanCodeDetectView 设置结果回调即可。
```java
scanView.setScanCallBack(new QBarSdkCallback() {
  @Override
  public void onIdentityResult(ScanResult result) {
    String data = result.getData(); // 识别内容
    String charset = result.getTypeName(); // 内容信息字符集
    String typeName = result.getCharset(); // 扫码类型
  }
});
scanView.onCreate(); // 构建ScanCodeDetectView
```
ScanCodeDetectView 的声明周期如下，请在对应的生命周期阶段进行调用。
```java
//scanView Life cycle
scanView.onCreate();
scanView.onResume();
scanView.onPause();
scanView.onStop();
scanView.onDestroy();
```

#### 默认扫描界面识别：

如果您只关注扫码功能不需要支持自定义 UI 界面，可以使用智能扫码 SDK 内自带的默认界面完成扫描操作。
```java
qBarCodeKit.startDefaultQBarScan(MainActivity.this, new QBarSdkCallback() {
  @Override
  public void onIdentityResult(ScanResult result) {
    String data = result.getData(); // 识别内容
    String charset = result.getTypeName(); // 内容信息字符集
    String typeName = result.getCharset(); // 扫码类型
  }
  
  @Override
  public void onFail(final int errorCode, final String errorMsg) {
 		// 智能扫码的错误
    runOnUiThread(new Runnable() {
    	@Override
      public void run() {
      	Toast.makeText(MainActivity.this, "code: " + errorCode + " msg: " + errorMsg,
                         Toast.LENGTH_SHORT).show();
      }
    });
});
```

#### 传入图片识别：

除了主动扫描以外，智能扫码 SDK 还支持图片识别功能，只需传入需要识别的图像即可：
```java
/*
 * bitmap 图片大小建议小于1M，避免OOM
 */
List<ScanResult> results = qBarCodeKit.decodeImageWithQBar(bitmap, MainActivity.this);
```
图片识别功能具体使用范例如下：
```java
   /*
   * bitmap 获取
   * filePath 源图片路径
   */
    BitmapFactory.Options sizeOptions = new BitmapFactory.Options();
    sizeOptions.inJustDecodeBounds = true;
    BitmapFactory.decodeFile(filePath, sizeOptions);
    BitmapFactory.Options decodeOptions = new BitmapFactory.Options();
    if (sizeOptions.outWidth * sizeOptions.outHeight * 3 > 10 * 1024 * 1024) {
        Log.i("MainActivity2", String.format("bitmap too large %d x %d, sample",sizeOptions.outWidth, sizeOptions.outHeight));
        decodeOptions.inSampleSize = 2;
    }
    Bitmap bitmap = BitmapFactory.decodeFile(filePath, decodeOptions);
    /*
    * bitmap 图片大小建议小于1M，避免OOM
    */
   List<ScanResult> results = qBarCodeKit.decodeImageWithQBar(bitmap, MainActivity.this);
   for (ScanResult result : results) {
     String data = result.getData(); // 识别内容
     String charset = result.getTypeName(); // 内容信息字符集
     String typeName = result.getCharset(); // 扫码类型
   }

```



### 混淆规则配置

如果您的应用开启了混淆功能，为确保扫描 SDK 的正常使用，请把以下部分添加到您的混淆文件中。

```java
-keep public interface com.tencent.scanlib.camera.Auth$OnInitCallback { *; }
-keep public interface com.tencent.scanlib.decoder.FileDecodeQueue$FileDecodeCallBack { *; }
-keep public interface com.tencent.scanlib.ui.ScanCodeView$ScanCallBack { *; }
-keep class com.tencent.scanlib.decoder.FileDecodeQueue { *; }
-keep class com.tencent.scanlib.decoder.FileDecodeQueue$* { *; }
-keep class com.tencent.scanlib.decoder.QBar$QBarResult { *; }
-keep class com.tencent.scanlib.decoder.QBarConstants { *; }
-keep class com.tencent.scanlib.ui.ScanCodeView { *; }
-keep class com.tencent.cloud.auth.lib.Error {*;}
-keep class com.tencent.qbar.** {*;}
-keep class com.tencent.scanlib.kit.** {*;}
-keep class com.tencent.cloud.auth.lib.Jni$AuthResult {*;}
-keep class com.tencent.scanlib.model.ScanResult {*;}
-keep class com.tencent.scanlib.model.ScanResultWithDetect {*;}

```

