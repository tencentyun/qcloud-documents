本文主要介绍如何快速运行腾讯云即时通信 IM Demo（React Native）。

## 环境要求

|   | 版本 |
|---------|---------|
| React Native | 0.63.4 版本以上|
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 帐号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
### 步骤1：创建应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
>同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5a.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/febed2f15dee6ff09f066ba228c7fc27.png)
3. 请保存 SDKAppID 信息。可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、标签、创建时间以及到期时间。
    ![](https://main.qcloudimg.com/raw/ed34d9294a485d8d06b3bb7e0cc5ae59.png)
4. 单击创建后的应用，左侧导航栏单击**辅助工具**>**UserSig 生成&校验**，创建一个 UserID 及其对应的 UserSig，复制签名信息，后续登录使用。
![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

[](id:step2)
### 步骤2：下载源码安装依赖并运行
1. 下载 IM 即时通信 [源码](https://github.com/TencentCloud/TIMSDK/tree/master/ReactNative/IMSDK/react-native-tim-js)
2. 安装项目依赖：
```javascript
yarn
```
3. 项目运行：
```javascript
// Android
yarn example android

// iOS
yarn example ios
```

## 联系我们
如果您在接入使用过程中有任何疑问，请加入QQ群：437955475 咨询。
