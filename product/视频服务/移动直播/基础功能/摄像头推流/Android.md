## 功能概述
摄像头推流，是指采集手机摄像头的画面以及麦克风的声音，进行编码之后再推送到直播云平台上。腾讯云 LiteAVSDK 通过 TXLivePusher 接口提供摄像头推流能力，如下是 LiteAVSDK 的简单版 Demo 中演示摄像头推流的相关操作界面：
![](https://main.qcloudimg.com/raw/2e38fc03bbd8a0963c880e468c38571a.jpg)

## 特别说明
- **不绑定腾讯云**
 SDK 不绑定腾讯云，如果要推流到非腾讯云地址，请在推流前设置 TXLivePushConfig 中的 `enableNearestIP`为 false。但当您要推流的地址为腾讯云地址时，请务必在推流前将其设置为 YES，否则 SDK 针对腾讯云的协议优化将不能发挥作用。

- **真机调试**
由于 SDK 大量使用 Android 系统的音视频接口，这些接口在仿真模拟器下往往不能工作，推荐您尽量使用真机调试。

## 示例代码

| 所属平台 | GitHub 地址 | 关键类 |
|:---------:|:--------:|:---------:|
| iOS | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/Demo/TXLiteAVDemo/LVB/CameraPush) | CameraPushViewController.m |
| Android | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/XiaoZhiBo/app/src/main/java/com/tencent/qcloud/xiaozhibo/anchor/screen/TCScreenAnchorActivity.java ) | TCScreenAnchorActivity.java |


## 功能对接

### 1. 下载 SDK 开发包
[下载](https://cloud.tencent.com/document/product/454/7873) SDK 开发包，并按照 [SDK 集成指引](https://cloud.tencent.com/document/product/454/7877) 将 SDK 嵌入您的 App 工程中。


### 2. 给 SDK 配置 License 授权
单击 [License 申请](https://console.cloud.tencent.com/live/license) 获取测试用 License，您会获得两个字符串：其中一个字符串是 licenseURL，另一个字符串是解密 key。

在您的 App 调用企业版 SDK 相关功能之前（建议在 Application类中）进行如下设置：

```java
public class MApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        String licenceURL = ""; // 获取到的 licence url
        String licenceKey = ""; // 获取到的 licence key
        TXLiveBase.getInstance().setLicence(this, licenceURL, licenceKey);
    }
}
```

### 3. 初始化 TXLivePusher 组件
首先创建一个`TXLivePushConfig`对象。该对象可以指定一些高级配置参数，但一般情况下我们不建议您操作该对象，因为我们已经在其内部配置好了所有需要校调的参数。之后再创建一个 `TXLivePusher` 对象，该对象负责完成推流的主要工作。

```java   
 TXLivePushConfig mLivePushConfig  = new TXLivePushConfig();     
 TXLivePusher mLivePusher = new TXLivePusher(this); 
 
 // 一般情况下不需要
