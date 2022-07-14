短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台上对短视频 SDK 进行新增、升级和续期。详细的短视频 SDK 功能请访问 [ 短视频 UGSV](https://cloud.tencent.com/document/product/584 )

## 申请测试版 License

 **您可以免费申请测试 License 体验测试，具体步骤如下：**

1. 登录腾讯云官网，进入 [云点播控制台](https://console.cloud.tencent.com/vod/license)，填写相应的信息，在 Package Name 中填写 Android 的包名，Bundle ID 中填写 iOS 的 BundleID。
![](https://main.qcloudimg.com/raw/bdd927a3b000daebb8f4b3b758517764.png)
2. 创建成功后页面会显示生成的 License 信息，这里需要记下 Key 和 LicenseUrl，在 SDK 的初始化时需要传入这两个参数。
![](https://main.qcloudimg.com/raw/1c181ff0fe99c93f9c01d09bd1b3ca65.png)
>? 基础版 License，有效期为14天，可申请两次。

## 购买正式版 License

当您的测试 License 到期后，您需要进入 [云点播控制台](https://console.cloud.tencent.com/vod/license) 创建正式 License。如您购买 [流量资源包10T](https://buy.cloud.tencent.com/vod)、[流量资源包50T](https://buy.cloud.tencent.com/vod)、[流量资源包200T](https://buy.cloud.tencent.com/vod) 中的任意一种，云点播都会赠送一个 License，该 License 需在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 和 [流量资源包](https://cloud.tencent.com/document/product/266/14667#2.-.E6.B5.81.E9.87.8F.E8.B5.84.E6.BA.90.E5.8C.85) 绑定后才可以创建成功，且该 License 的有效期和资源包的有效期一致，支持对 License 进行升级、续期、变更。

**SDK 版本 License 与您需要购买的点播套餐包对应关系如下：**

| SDK 版本 | 套餐包 | 
|---------|---------|
| [精简版 SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 10TB](https://buy.cloud.tencent.com/vod?t=ugsv&amp;from=console-license-bottom-ugsv) | 
| [基础版 SDK（UGC）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 50TB 或 200TB](https://buy.cloud.tencent.com/vod?t=ugsv&amp;from=console-license-bottom-ugsv) | 

>!购买点播套餐包并绑定 License 后，请确认 Bundle ID 和 Package Name 无误，一旦提交，License 的信息不能再做修改。

## 新增短视频 License

1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license) ，单击【新增 License】，进入短视频 License 新增页。
2. 选择当前账户可绑定的资源包。若无已购买资源包，请单击【购买页】前往选购 [流量资源包10TB](https://buy.cloud.tencent.com/vod)、[流量资源包50TB](https://buy.cloud.tencent.com/vod)、[流量资源包200TB](https://buy.cloud.tencent.com/vod) 中的任意一种。
![](https://main.qcloudimg.com/raw/07384dc91eca502e3ba77469ab2affeb.png)
3. 单击【确认并继续完成 License 设置】跳转到 License 设置页。
4. 录入信息，单击【确定】即可。
![](https://main.qcloudimg.com/raw/f4bc43f4f3220dfc493e9758afd2b4f8.png)

>? 创建成功后您可以在 [License 管理页](https://console.cloud.tencent.com/vod/license) 上查阅详细信息。

## 续期短视频 License

您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看 License 的有效期，正式版本的 License 有效期为一年。如您需要对指定的 License 续期，请确保已购买资源包的情况下，进行如下操作：

1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license) ，选择您需要续期的 License，单击右上角的【续期】，进入短视频 License 续期页。
2. 选择当前账户可绑定的资源包， **License 有效时间和对应的绑定资源包有效时间一致** 。
3. 单击【确认续期】即可。
	![](https://main.qcloudimg.com/raw/5d1d551707a5a41e69f201ca00ef549d.png)

#### 示例

- 用户于2019-02-02购买 [流量资源包50TB](https://buy.cloud.tencent.com/vod)（有效期：2019-02-02至2020-02-01），赠送基础版 License 有效期则为：2019-02-02至2020-02-01。
- 若用户需要进行续期，续期流量资源包200TB（2019-07-02至2020-07-01），则 License 的有效期为：2019-07-02至2020-07-01。

## 升级短视频 License

目前仅支持短视频 License 由精简版升级至基础版，升级 License 为 [对应资源包赠送的 License 规格](https://cloud.tencent.com/document/product/584/9368#.E8.B4.AD.E4.B9.B0.E8.AF.B4.E6.98.8E)。

#### 示例

用户购买 [流量资源包10TB](https://buy.cloud.tencent.com/vod)（赠送精简版 License），如需升级至基础版 License，则 [云点播控制台](https://console.cloud.tencent.com/vod/license) 需要存在50TB或200TB资源包。

## License 使用方法

在调用 SDK 的相关接口前调用如下所示方法进行 License 的设置。

- iOS 建议在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中添加：
 `[TXUGCBase setLicenceURL:LicenceUrl key:Key];` 
- Android 建议在 application 中添加：
 `TXUGCBase.getInstance().setLicence(context, LicenceUrl, Key);` 

## License 信息查看

在 License 设置成功后稍等一段时间（依据网络情况而定），可以通过调用以下方法查看 License 信息。

- iOS：
 ```
 NSLog(@"%@", [TXUGCBase getLicenceInfo]);```
 
- Android：
 ```
 TXUGCBase.getInstance().getLicenceInfo(context);
 ```


## 常见问题

1.  **测试 License 到期后是否可以延期？**
测试 License 试用期最多28天，不能延期，到期后请尽快购买正式 License。

2.  **测试 License 能否更改 Android 的 PackageName 和 iOS 的 BundleID?**
测试 License 支持更改，在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 选择测试 License 信息右边的编辑按钮，可单击编辑修改。

3.  **正式 License 能否更改 Android 的 PackageName 和 iOS 的 BundleID?**
当前版本，正式 License 不能更改 PackageName 和 BundleID，后续版本会加以支持。

4.  **License 可以同时支持多个 App 吗？**
一个 License 只能对应一个 PackageName 和 BundleID，不支持多个 App。