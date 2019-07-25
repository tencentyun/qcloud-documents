
## 开发准备

### SDK 获取

实时流式语音识别的 iOS SDK 以及 Demo 的下载地址：[QCloud SDK](https://main.qcloudimg.com/raw/777564552ff9e038b613f8cb96570a2d/QCloudSDK_v2.0.3.zip)。


### 使用须知

+ QCloudSDK 支持 **iOS 9.0** 及以上版本。
+ 实时流式语音识别，需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等）。
+ 从控制台获取 AppID、SecretID、SecretKey、ProjectId 详情参考 [基本概念](https://cloud.tencent.com/document/product/441/6194)。
+ 运行 Demo 必须设置 AppID、SecretID、SecretKey、ProjectId.
+ 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。

### SDK导入

iOS SDK 压缩包名称为： QCloudSDK_v2.0.3.zip，压缩包中包含 Sample Code 和 QCloudSDK。

### 工程配置

在工程` info.plist` 添加以下设置：
1. **设置 NSAppTransportSecurity 策略，添加如下内容：**
```objective-c
  <key>NSAppTransportSecurity</key>
  <dict>
	<key>NSExceptionDomains</key>
	<dict>
		<key>qcloud.com</key>
		<dict>
			<key>NSExceptionAllowsInsecureHTTPLoads</key>
			<true/>
			<key>NSExceptionMinimumTLSVersion</key>
			<string>TLSv1.2</string>
			<key>NSIncludesSubdomains</key>
			<true/>
			<key>NSRequiresCertificateTransparency</key>
			<false/>
		</dict>
	</dict>
    </dict>
```
2. **申请系统麦克风权限，添加如下内容：**
```objective-c
   <key>NSMicrophoneUsageDescription</key>
   <string>需要使用了的麦克风采集音频</string>
```
3. **在工程中添加依赖库，在 build Phases Link Binary With Libraries 中添加以下库：**
   + AVFoundation.framework
   + AudioToolbox.framework
   + QCloudSDK.framework
   + CoreTelephony.framework
   + libWXVoiceSpeex.a
   
添加完如图所示。
![](https://main.qcloudimg.com/raw/17ff6f4f4a27e0843de528eb070c2f32.png)
