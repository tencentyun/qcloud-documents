本文主要介绍如何快速运行腾讯云人脸核身 demo。

## 环境要求
- 最低兼容 Android 4.4（SDK API Level 19），建议使用 Android 5.0（SDK API Level 21）及以上版本。
- Android Studio 4.0及以上版本。
- App 要求 Android 4.4及以上的设备。


## 前提条件
- 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
- 并将 SDK 的演示 demo 文件下载到本地。
- 已申请到授权 License 文件。


## 操作步骤
### 步骤1：导入工程
1. 打开Android Studio，选择导入工程选项。
![](https://qcloudimg.tencent-cloud.cn/raw/c62340baf7ccf2cf19a0b98d63c5eae5.png)
2. 之后选择 demo 项目，将 demo 项目导入打开
![](https://qcloudimg.tencent-cloud.cn/raw/cccccc14e2ca2ead2c1d1e25c9810868.png)

### 步骤2：导入 License 文件
您需要申请授权 License 后，并将 License 导入 demo 中，如下图的位置即可。
![](https://qcloudimg.tencent-cloud.cn/raw/18beb924079519f6b0d3beeeabe599e7.png)
此 License 暂时可以 [联系客服](https://cloud.tencent.com/document/product/1007/56130) 进行 License 申请。

### 步骤3: 设置 FaceIdToken
在 [GetFaceIdToken](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=DetectAuth&SignVersion=) 接口获取 FaceIdToken 后，设置到 getCustomerFaceIdToken 的返回值。
```java
// 测试添加FaceID的方法
HuiYanAuth.setFaceIdTokenCreateFunction(new CreateFaceIdToken() {
    @Override
    public String getCustomerFaceIdToken() {
        return currentToken;
    }
});
```
>? FaceIdToken 是 SDK 与后台服务之间的交互凭证，由于 FaceIdToken 的生成需要使用到 secretId、secretKey，因此我们强烈建议将 FaceIdToken 的生成放到您的服务器端，您在 App 中可以与您的服务器产生交互获取 FaceIdToken。在您获取到 FaceIdToken 之后，将 FaceIdToken 的值设置到 currentToken 中即可。具体过程可以参考 sendRequestToGetFaceIdToken() 方法。

### 步骤4：编译运行
完成配置之后可以点击 Android Studio 的运行按钮，体验 Demo。


## demo 合规声明
由于 Demo 运行方式与正式 App 运行方式有所差异，为实现 Demo 正常运行以便向您提供尽可能全面的 SDK 功能体验，我们在 Demo 中引用了部分依赖库（okhttp），且仅限于在 Demo 场景下使用。当您接入正式 SDK 产品时请按照 SDK 正式 [集成文档](https://cloud.tencent.com/document/product/1007/85566) 进行操作。
```xml
<!-- Demo注册的可选权限  -->
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />

<!-- 仅Demo使用的三方库：com.squareup.okhttp3:okhttp:3.12.1  -->
```

