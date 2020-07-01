## 开发准备

请参考 [接入准备](https://cloud.tencent.com/document/product/1214/45793) 。


## Android 端扫码 SDK 介绍

SDK 文件为 **QBarCode-v0.1.2.aar**，该文件里面封装了智能扫码接口、so 文件、检测与超分模型的资源文件。

功能：提供实时识别一维码、二维码、和图片内一二维码检测的服务。

## 环境依赖

当前版本的 SDK 适用于 API 19(Android 4.4) 及以上版本

## 接入步骤

1. 将 **QBarCode-v0.1.2.aar** 包添加到您的工程文件中的 **libs** 目录下。

2. 配置 **build**

   - 权限设置

   ```xml
   <uses-permission
           android:name="android.permission.CAMERA"
           android:required="true" />
       <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
       <uses-feature android:name="android.hardware.camera" />
       <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
   ```

   - 在您的工程文件中的 **build.gradle** 中进行如下配置：

   ```groovy
   //使用 aar 时必须要设置
   android {
       //**
       defaultConfig {
          /***/
           ndk {
               abiFilters "armeabi-v7a" //暂时仅支持 armeabi-v7a
           }
       }
     sourceSets {
           main {
             jniLibs.srcDirs = ['libs/jniLibs']
           }
       }
   }
   dependencies {
       compile fileTree(include: ['*.jar'], dir: 'libs')
       api files('libs/QBarCode-v0.1.2.aar')
   }
   ```


3. 接入 SDK
**模式一：仅调用接口返回数据，需要自定义布局和接口解码** 

   - sdk 初始化：

   ```java
   private QBarCodeKit qBarCodeKit;
   
   //Android 6及以上动态申请权限，权限通过后再初始化
   qBarCodeKit = QBarCodeKit.getInstance();
   qBarCodeKit.initQBarCodeKit(SECRET_ID, SECRET_KEY, MainActivity2.this, new QBarCodeKit.OnSdkKitInitCallback (){
     @Override
     public void onInitResult(String errCode) {
       android.util.Log.d("onInitResult：", errCode); //initAuth 执行时间可能有1-2s，当返回 SUCCESS(0) 说明授权成功，再进行后面的操作
    Toast.makeText(MainActivity2.this, errCode, Toast.LENGTH_SHORT).show();
     }
   });
   ```
   
   - 摄像头数据实时识别-接入
   
   ```xml
   <com.tencent.scanlib.ui.ScanCodeDetectView
       android:id="@+id/scan_view"
    android:layout_width="match_parent"
       android:layout_height="match_parent"
   		app:show="false"/><!--show 设置 false-->
   ```
   
   ```java
   scanView.setScanCallBack(new ScanCodeView.ScanCallBack() {
       @Override
       public void onScanSuccess(Bundle result) {
           if (result != null) {
           String resultString = result.getString(ScanCodeView.RESULT_CONTENT, "");
               scanView.onResume();
           }
    }
   });
   scanView.onCreate();
   ```
   
   ```java
   //scanView Life cycle
   scanView.onCreate();
   scanView.onResume();
   scanView.onPause();
   scanView.onStop();
   scanView.onDestroy();
   ```
   
   - 图片识别-接入
   
   ```java
   List<QBar.QBarResult> results = qBarCodeKit.qbarDecodeWithImage(bitmap, MainActivity.this);
   ```
   
   **模式二：已封装好扫码页面，无需用户自定义**
   
   - sdk 初始化：
   
   ```java
   QBarSdkKit.initQBarSdkKit(SECRET_ID, SECRET_KEY, MainActivity.this, new QBarSdkKit.OnSdkKitInitCallback (){
       @Override
       public void onInitResult(String errCode) {
        Log.d("onInitResult：", errCode); //initAuth 执行时间可能有1-2s，当返回 SUCCESS(0) 说明授权成功，再进行后面的操作
           Toast.makeText(MainActivity.this, errCode, Toast.LENGTH_SHORT).show();
    }
   });
   ```
   
   - 进入扫码主页面
   
   ```java
   QBarSdkKit.startMainPage(MainActivity.this, new QBarSdkCallback() {
       @Override
       public void onIdentityResult(Intent data) {//结果
       String content = data.getStringExtra(QBarSDKConfig.SCAN_CONTENT);//识别内容
       String type_name = data.getStringExtra(QBarSDKConfig.SCAN_TYPE_NAME);//二维码/条码 类型
    String charset = data.getStringExtra(QBarSDKConfig.SCAN_CHARSET);//字符集
       }
    });
   ```

4. 混淆规则

    ```
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
    -keep class com.tencent.scanlib.kit.QBarCodeKit {*;}
    ```

