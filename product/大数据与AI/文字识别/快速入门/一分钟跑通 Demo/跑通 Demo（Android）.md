本文主要介绍如何快速运行腾讯云 文字识别 OCR Demo。



### 环境要求

- 最低兼容 Android 4.4（SDK API Level 19），建议使用 Android 5.0（SDK API Level 21）及以上版本
- Android Studio 4.0 及以上版本
- App 要求 Android 4.4 及以上的设备



### 前提条件

- 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629) 。
- 进入 [文字识别控制台](https://console.cloud.tencent.com/ocr/general)，即可开通相应服务，并在 [账号中心](https://console.cloud.tencent.com/cam/capi) 获取 API 密钥。
- 并将 SDK 的 demo 文件下载到本地。



### 操作步骤

#### 步骤1：导入工程

打开 Android Studio，选择导入工程选项

![](https://main.qcloudimg.com/raw/503fc290eed55b20d0e0430cd06c0ea2.png)

随后选择 demo 项目，将 demo 项目导入打开

![](https://main.qcloudimg.com/raw/ce53a6a750d61361beb5ff9ccab411a9.png)



#### 步骤2: 修改配置信息

打开文件 com.tencent.ocr.model.SecretPamera 类，将在后台获取到的 secretId、secretKey 更新为您的信息。

```java
/**
 * 密钥配置信息
 */
public class SecretPamera {
    public final static String secretId = "您的 secretId";
    public final static String secretKey = "您的 secretKey";
}
```

>! 
> 
> 本文提到的将 secretId、secretKey 直接配置到客户端中的方式，很容易被反编译逆向破解，一旦您的密钥泄密，攻击者可以使用您的 secretId、secretKey 信息进行 OCR 识别请求，给您造成损失。因此该方法**仅适用于本地跑通 Demo 和功能调试**
> 
> 我们建议您将 secretId、secretKey 配置到服务器端，同时客户端使用临时密钥兑换的方式进行 OCR 识别。具体流程可以参考 [临时密钥兑换流程](https://github.com/TencentCloud/tc-ocr-sdk/tree/master/%E4%B8%B4%E6%97%B6%E5%AF%86%E9%92%A5%E5%85%91%E6%8D%A2) 。



#### 步骤3:编译运行

完成配置之后可以单击 Android Studio 的运行按钮，体验 Demo。
