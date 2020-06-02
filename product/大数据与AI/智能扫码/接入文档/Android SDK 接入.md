## Android SDK 介绍

### 内容
- QBarCode-v0.1.1.aar - aar文件，封装了扫码接口、so 文件和模型文件。

### 功能
实时识别二维码/条形码，图形二维码/条形码识别、检测。

### 环境依赖
SDK 可在 [智能扫码控制台](https://console.cloud.tencent.com/ocr/is) 申请后下载。

## Android SDK 接入
1. 使用 AAR 接入，将 QBarCode-v0.1.1.aar 包添加到接入方 App 中的 libs 目录下，如 Demo 所示。
2. 配置 build
1）权限设置

```
<uses-permissionandroid:name="android.permission.CAMERA"android:required="true" /><uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" /><uses-feature android:name="android.hardware.camera" /><uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

```

2）在接入方 App 的 build.gradle 中进行如下配置：

```
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
  	implementation 'commons-io:commons-io:2.6'//io 依赖库，建议版本与 SDK 一样
    api files('libs/QBarCode-v0.1.1.aar')
}

```

3. SDK 初始化

```
PermissionsHandler.getInstance().checkPermissions(this, permissions, new PermissionsHandler.IPermissionsResult() {
  @Overridepublic void passPermissions() {
    //权限通过  SDK 初始化需要文件读写和网络权限，android 6.0 以上需动态申请权限
    QBarSdkKit.initQBarSdkKit(SECRET_ID, SECRET_KEY, MainActivity.this, new Auth.OnInitCallback() {
      @Overridepublic void onInitResult(String errCode) {
        Log.e("onInitResult：", errCode); //initAuth 有耗时操作，当返回SUCCESS(0) 说明授权成功，再进行后面的操作
     Toast.makeText(MainActivity.this, errCode, Toast.LENGTH_SHORT).show();
        authTipsTv.setText(errCode);
     		openQBarSDK.setEnabled(true);
      }
    });
  }

  @Overridepublic void forbidPermissions() {
    Toast.makeText(MainActivity.this, "手机权限未通过！", Toast.LENGTH_SHORT).show();
  }
});

```


```
//图片二维码/条形码识别
  QBarSdkKit.startMainPage(MainActivity.this, new QBarSdkCallback() {
    @Overridepublic void onIdentityResult(Intent data) {
      Intent intent = new Intent(MainActivity.this, ContentActivity.class);
      intent.putExtra(QBarSDKConfig.SCAN_CONTENT, data.getStringExtra(QBarSDKConfig.SCAN_CONTENT));//识别内容
      intent.putExtra(QBarSDKConfig.SCAN_TYPE_NAME, data.getStringExtra(QBarSDKConfig.SCAN_TYPE_NAME));//二维码/条码 类型
      intent.putExtra(QBarSDKConfig.SCAN_CHARSET, data.getStringExtra(QBarSDKConfig.SCAN_CHARSET));//字符集
   startActivity(intent);
    }
});

```
