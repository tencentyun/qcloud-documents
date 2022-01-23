## 开发准备

1. 注册腾讯云账号，单击进入 [文字识别控制台](https://console.cloud.tencent.com/ocr/general)，即可开通相应服务。
2. 在 [账号中心](https://console.cloud.tencent.com/cam/capi) 获取 API 密钥。
3. 从 OCR SDK 下载链接中下载 SDK 到本地准备集成。



## Android 端 OCR SDK 接入流程

### Android 端OCR SDK 介绍

SDK提供的文件为 [OCR_Android_SDK_V1.0.9](https://ai-sdk-release-1254418846.cos.ap-guangzhou.myqcloud.com/ocr/1.0.9/sdk/OCR_Android_SDK_V1.0.9.zip)，该文件封装了 OCR 识别终端能力。目前包括了身份证识别、银行卡识别、名片识别、车辆Vin码识别、车牌识别、驾驶证识别以及行驶证识别。



### 环境依赖

当前 Android 端 OCR 识别 SDK 适用于 API 19 (Android 4.4) 及以上版本。



### 接入步骤

1. 将 **OcrSDKv1.0.2-alpha.aar** 添加到您工程目录的 libs 目录下。
![](https://main.qcloudimg.com/raw/817e191497ae168a2f9890e5d85ce936.png)

2. 在您工程的 **build.gradle** 中进行如下配置：
```groovy
dependencies {
  // 依赖腾讯云的 OcrSDK 的 aar
  implementation files('libs/OcrSDKv1.0.2-alpha.aar')
  // OCR SDK 返回实体对象需要的依赖
  implementation 'com.google.code.gson:gson:2.8.5'
}
```

3. 同时需要在 AndroidManifest.xml 文件中进行必要的权限声明
```xml
<!--摄像头使用权限-->
<uses-feature android:name="android.hardware.camera" />
<uses-permission
  android:name="android.permission.CAMERA"
  android:required="true" />
<!--文件存储使用权限-->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<!--网络访问权限-->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

对于需要兼容 Android 6.0 以上的用户，以上权限除了需要在 AndroidManifest.xml 文件中声明权以外，还需使用代码动态申请权限。



### SDK 接口使用说明

#### SDK 初始化：

使用 OCR SDK 之前需要进行初始化，您可以按照您的需求设置默认值。

```java
// 启动参数配置
OcrModeType modeType = OcrModeType.OCR_DETECT_AUTO_MANUAL; // 设置默认的业务识别模式自动 + 手动步骤模式
OcrType ocrType = OcrType.BankCardOCR; // 设置默认的业务识别，银行卡
OcrSDKConfig configBuilder = OcrSDKConfig.newBuilder(SecretPamera.secretId, SecretPamera.secretKey, null)
                .ocrType(ocrType)
                .setModeType(modeType)
                .build();
// 初始化 SDK
OcrSDKKit.getInstance().initWithConfig(this.getApplicationContext(), configBuilder);
```

目前 OCR SDK 支持的业务模式：

| OcrModeType 类型        | 代表含义                                            |
| ---------------------- | --------------------------------------------------- |
| OCR_DETECT_MANUAL      | 手动拍摄模式                                        |
| OCR_DETECT_AUTO_MANUAL | 自动识别模式（tips：20s后提示，是否切换到手动拍摄） |



#### 更新临时密钥

OCR SDK 支持使用临时密钥接口，使用临时密钥的好处主要有以下两点，第一将固定密钥与终端分离可以增加安全性；第二因为兑换临时密钥是您完全可控的行为，因此您可以根据自定义规则来控制最终用户的接口访问权限。因此建议您使用临时密钥的方式，具体可以参考文档 [(**临时密钥文档与流程链接**)](https://github.com/TencentCloud/tc-ocr-sdk/tree/master/%E4%B8%B4%E6%97%B6%E5%AF%86%E9%92%A5%E5%85%91%E6%8D%A2)

```java
OcrSDKKit.getInstance().updateFederationToken(tmpSecretId, tmpSecretKey, token);
```



#### OCR 识别（返回 Json 字符串）：

当您需要使用 OCR 识别的功能的时候，您可以直接调用识别接口，进行 OCR 业务识别。

```java
// 启动 ocr 识别，识别类型为身份证正面
OcrSDKKit.getInstance().startProcessOcr(MainActivity.this, OcrType.IDCardOCR_FRONT, customConfigUi, new ISDKKitResultListener() {
    @Override
    public void onProcessSucceed(String response, String srcBase64Image, String requestId) {
        popTip(response, "Succeed"); // 展示 ocr 识别结果
    }

    @Override
    public void onProcessFailed(String errorCode, String message, String requestId) {
        popTip(message, errorCode); // 展示 ocr 识别错误信息
    }
});
```

#### OCR 识别（返回对象实体类）：

当您需要使用 OCR 识别功能，同时需要直接获取实体对象而非 JsonString 时，可以使用此方法。

```java
OcrSDKKit.getInstance().startProcessOcrResultEntity(OcrTypeIdCardActivity.this,
        OcrType.IDCardOCR_FRONT, null, IdCardOcrResult.class,
        new ISdkOcrEntityResultListener<IdCardOcrResult>() {
            @Override
            public void onProcessSucceed(IdCardOcrResult idCardOcrResult, String base64Str) {
                Log.e(TAG, "IdCardOcrResult:" + idCardOcrResult.toString()); // OCR 识别成功 IdCardOcrResult
            }

            @Override
            public void onProcessFailed(String errorCode, String message, String requestId) {
                Log.e(TAG, "errorCode:" + errorCode + " message:" + message); // OCR 识别失败 IdCardOcrResult
            }
        });
```

目前 OCR SDK 支持五种类型的识别模式如下表所示，以及对应的实体类返回结果。

| OcrType 类型             | 代表含义               | 对应结果实体类          |
| ----------------------- | ---------------------- | ----------------------- |
| OcrType.IDCardOCR_FRONT | 身份证人像面识别模式   | IdCardOcrResult         |
| OcrType.IDCardOCR_BACK  | 身份证国徽面识别模式   | IdCardOcrResult         |
| OcrType.BankCardOCR     | 银行卡正面识别模式     | BankCardOcrResult       |
| OcrType.BusinessCardOCR | 名片卡正面识别模式     | BusinessCardOcrResult   |
| OcrType.MLIdCardOCR     | 马来西亚身份证识别模式 | MalaysiaIdCardOcrResult |
| OcrType.VinOCR | 车辆的 VIN 识别模式 | VinOcrResult |
| OcrType.LicensePlateOCR | 车辆的车牌识别模式 | CarLicensePlateResult |
| OcrType.DriverLicenseOCR_FRONT | 驾驶证主页识别模式 | DriverLicenseCardResult |
| OcrType.DriverLicenseOCR_BACK | 驾驶证副页识别模式 | DriverLicenseCardResult |
| OcrType.VehicleLicenseOCR_FRONT | 行驶证主页识别模式 | VehicleLicenseCardResult |
| OcrType.VehicleLicenseOCR_BACK | 行驶证副页识别模式 | VehicleLicenseCardResult |



#### SDK 版本号获取：

OCR SDK 提供了直接获取 SDK 版本号的接口，您可以调用此接口获取。

```java
OcrSDKKit.getInstance().getVersion()
```



#### SDK 资源释放：

在您 App 退出使用或者需要重启加载 OCR 功能的时候，可以调用 SDK 资源释放接口。

```java
@Override
protected void onDestroy() {
    if (mDialog != null) {
        mDialog.dismiss();
    }
    // 释放 OCR SDK 的资源
    OcrSDKKit.getInstance().release();
    super.onDestroy();
}
```

### 混淆规则配置

如果您的应用开启了混淆功能，为确保 SDK 的正常使用，请把以下部分添加到您的混淆文件中。
```java
#保留自定义的 OcrSDKKit 类和类成员不被混淆
-keep class com.tencent.ocr.sdk.** {*;}

#第三方 jar 包不被混淆
-keep class com.tencent.youtu.** {*;}

```



### 常见问题

1. 如同时集成其余 SDK，出现 **More than one file was found with OS independent path 'lib/armeabi-v7a/libc++_shared.so'.**  的问题。
主要是 OCR SDK 和其余 SDK 都添加了 `libc++_shared.so` 这个库，解决办法可以在 build.gradle 中添加如下配置：
```groovy
android {
		...
		    // 过滤重复定义 so 的问题
    packagingOptions{
        pickFirst 'lib/armeabi-v7a/libc++_shared.so'
    }
}
```

2. 如果集成方使用了 AndResGuard 的混淆工具，可以添加混淆配置：
```groovy
// for OCR SDK
"R.string.ocr_*",
"R.string.rst_*",
"R.string.net_*",
"R.string.msg_*",

```

3. 集成 OCR SDK 后如果出现 **Invoke-customs are only supported starting with Android O (--min-api 26)** 错误？
需要在 build.gradle 中添加如下配置：
```groovy
// java 版本支持1.8
compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
}
```

