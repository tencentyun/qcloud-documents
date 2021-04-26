腾讯云人脸核身针对 Android 端提供 SDK，开发人员可以将相应的 SDK 添加到项目工程中，直接调用 SDK 中提供的 OCR 识别、活体检测和1:1人脸比对服务。
![](https://main.qcloudimg.com/raw/ba6e243fdce04a0a9aea85f26516a3e6.png)

## 业务流程
![](https://main.qcloudimg.com/raw/d63b182923580043c11be2da419e3694.png)
1. 客户后端调用 [DetectAuth](https://cloud.tencent.com/document/api/1007/31816) 接口进行核身流程开启前鉴权，获取业务流水号（`BizToken`）。
2. 根据客户自身需求，在对应页面调用相关函数进入人脸核身流程，开始验证。
3. 人脸核身完成后，会触发回调函数，此时客户后端即可凭借回调中提供的`BizToken`调用 [GetDetectInfo](https://cloud.tencent.com/document/api/1007/31331) 接口获取本次核身的详细信息。

## SDK 说明
本 SDK 封装了实名核身的整体流程，包括身份证 OCR 识别和活体检测功能。

### 环境依赖
V3.0版本 SDK 适用于 Android4.0及以上版本。

### SDK 下载
本 SDK 暂不支持通过外部 npm 源下载，需线下对接获取该 SDK，您可以提交 [接入申请](https://cloud.tencent.com/apply/p/shcgszvmppc) 与我们取得联系。

### 文件说明
**AuthSdk.jar**：封装了实名核身的流程，包括身份证 OCR 识别和活体检测功能。
**AuthSdk.aar**：封装了实名核身的流程，包括身份证 OCR 识别和活体检测功能和所有需要的资源。
**res**：包含 SDK 所使用的资源文件。
**assets**：包含协议内容文件。目前使用的是《测试实名核身用户须知》。
**libcurl.so、libUlsFunction.so、libulsTracker_native.so**：人脸定位库。
**AuthDemo**：提供了实名核身接口调用方法及从后台拉取活体检测详细信息的方法。接入时可参考 Demo，这里提供了两个 Demo，对应两种接入方式。

## 接入流程
您可通过两种方式接入服务：
- （推荐）使用 aar 方式，可以在 Android Studio 中使用。
-  一种是使用 jar 包和资源的方式，可以用在 Eclipse 和 Android Studio 中。

### 使用 aar 接入
详情可参见 authdemo（authdemo 在线下对接时，会由腾讯云侧提供）。

#### 1. 添加 aar 包
将 AuthSdk.aar 包添加到接入方 App 中的 libs 目录下，如 Demo 所示。

#### 2. 配置 build
在接入方 App 的 build.gradle 中进行如下配置。
```js
//使用 aar 时必须要设置
repositories {
    flatDir {
        dirs 'libs'
    }
}
dependencies {
    compile fileTree(include: ['*.jar'], dir: 'libs')
compile (name:'AuthSdk', ext:'aar')
compile 'com.github.bumptech.glide:glide:3.7.0'
    compile 'com.android.support:appcompat-v7:23.4.0'
}
```

#### [3. 初始化 SDK 接口](id:aar)
在程序的 Application 中或在调用 SDK 之前初始化 SDK，设置相关配置，具体请参考 AuthDemo。**每次调用都需要从 [DetectAuth](https://cloud.tencent.com/document/api/1007/31816) 接口生成新的 BizToken**。
```
AuthConfig.Builder configBuilder = new AuthConfig.Builder(editText.getText().toString(), R.class.getPackage().getName());
```

**4. 调用实名核身**
```java
AuthSDKApi.startMainPage(this, configBuilder.build(), mListener);
```
**5. 验证结果回调**

```java
private IdentityCallback mListener = new IdentityCallback() {
        @Override
        public void onIdentityResult(Intent data) {
            boolean indexback = data.getBooleanExtra(AuthSDKApi.INDEX_BACK, false);
            boolean identityStatus = data.getBooleanExtra(AuthSDKApi.EXTRA_IDENTITY_STATUS, false);//验证结果标识 true：通过 false：不通过
            if (identityStatus) {
               //实名核身通过
            }
        }
    };
```
### 使用 jar 包和资源接入

详情可参见 authdemo_jar（authdemo_jar 在线下对接时，会由腾讯云侧提供）。

**1. 设置权限和 Manifest 配置**
在接入方 App 的 AndroidManifest.xml 中进行如下配置，具体可参见 AuthDemo。
设置权限：
``` xml
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<!-- 使用音视频录制的权限 -->
<uses-permission android:name="android.permission.RECORD_VIDEO" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<!-- 使用相机及自动对焦功能的权限 -->
<uses-permission android:name="android.permission.CAMERA" />

<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
<!-- 监听来电 -->
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.PROCESS_OUTGOING_CALLS" />
```

添加 Activity：
``` xml
<activity
    android:name="com.tencent.authsdk.activity.MainSdkActivity"
    android:launchMode="singleTask"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" >
</activity>
<activity
    android:name="com.tencent.authsdk.activity.IdcardOcrActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.IdcardOcrResultActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.CameraActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.AlbumActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.CropImageActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" >
</activity>
<activity
    android:name="com.tencent.authsdk.activity.IdentityDetectActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.RecordActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.LiveDetectActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.DetectResultActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
<activity
    android:name="com.tencent.authsdk.activity.PhoneVerityActivity"
    android:screenOrientation="portrait"
    android:theme="@style/SDKAppTheme" />
```

**2. 添加 jar 包和资源**
参照 AuthDemo，将 AuthSDK.jar 添加到接入方 App 中的 libs 目录下，将 res 目录下的资源文件添加到接入方 App 的 res 下的相应目录下，以及 assets 目录下的文件添加到 App 的assets 下，将libcurl.so、libUlsFunction.so、libulsTracker_native.so 添加到 jniLibs 下。

**3. 初始化 SDK 及调用实名核身接口**
具体流程跟上面 [aar 接入方式](#aar) 中的3 - 4步骤一致，此处不再赘述。

