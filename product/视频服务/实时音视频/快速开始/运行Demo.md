本文主要介绍如何快速地将腾讯云实时音视频Demo工程运行起来，您只需参考如下步骤依次执行即可。

## 创建新的应用

进入腾讯云实时音视频[控制台](https://console.cloud.tencent.com/rav)，如果您还

## 购买测试套餐

## 下载Demo源码包



## 下载私钥文件（PrivateKey）

<font color='red'>【安全风险】</font>


## 修改Demo源文件

#### iOS

#### Android

#### Windows

#### WebRTC

#### 小程序

## 编译运行

## 常见问题
### 1. 开发环境要求
#### iOS
- Xcode 9.0+
- 请确保你的项目已设置有效的开发者签名。

#### Android
- Android SDK API Level Level ≥ 16
- Android Studio 2.0 或以上版本
- App 要求 Android 4.1 或以上设备

#### Windows
- 操作系统： Microsoft Windows 7+
- 编译器：Microsoft Visual C++ 2013+
- 开发环境：Microsoft Visual Studio 2015 （推荐）

#### WebRTC
- 请使用最新版的 Chrome 浏览器

#### 小程序
- 微信 App iOS 最低版本要求：6.5.21
- 微信 App Android 最低版本要求：6.5.19
- 小程序基础库最低版本要求：1.7.0

### 2. 是否支持iPhone模拟器调试
SDK 能在 iPhone 模拟器下通过编译，但由于模拟器无法提供跟 iPhone 一致的摄像头等硬件能力，所以SDK在模拟器下运行会有各种异常，请使用真机进行调试。

### 3. 防火墙限制
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请联系贵司的网络管理员，将如下端口加入防火墙的安全白名单中。
<font color='red'>【TO-DO】</font>



