## 简介

信鸽 iOS SDK 是一个能够提供 Push 服务的开发平台，提供给开发者简便、易用的 API 接口，方便快速接入。

## 接入方法

(1) 获取 AppId 和 AppKey。
(2) 工程配置。

### 获取 AppId 和 AppKey

前往 http://xg.qq.com 注册并获取 AppKey。

### 工程配置

1.下载信鸽 SDK，解压缩。注：使用 CocoaPods 的用户可以通过如下名称管理信鸽：

```
pod 'QQ_XGPush'
```
2.将 XGSetting.h，XGPush.h 以及 libXG-SDK.a 添加到工程。

3.添加以下库/framework 的引用 CoreTelephony.framework, SystemConfiguration.framework， UserNotifications.framework, libXG-SDK.a 以及 libz.tbd.添加完成以后，库的引用如下：
![](//mc.qcloudimg.com/static/img/06ef5cec690338d76d913538ac7a0598/image.png)
4.在工程配置和后台模式中打开推送，如下图。
![](//mc.qcloudimg.com/static/img/e875b2b189be94311d65b5c70a17b730/image.png)
5.参考 Demo，添加相关代码。









