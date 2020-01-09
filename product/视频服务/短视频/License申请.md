## 申请测试版 License
**您可以免费申请测试 License（基础版，有效期14天，可申请两次）体验测试，具体步骤如下**：
1. 登录腾讯云官网，进入 [云点播控制台](https://console.cloud.tencent.com/vod/license)，填写相应的信息，在 Package Name 中填写 Android 的包名，Bundle Id 中填写 iOS 的 BundleID。
![](https://main.qcloudimg.com/raw/bdd927a3b000daebb8f4b3b758517764.png)
2. 创建成功后页面会显示生成的 License 信息，这里需要记下 Key 和 LicenseUrl，在 SDK 的初始化时需要传入这两个参数。
![](https://main.qcloudimg.com/raw/2368a0969c19cd1884ef28de153d5039.png)

## 购买正式版 License
当您的测试 License 到期后，您需要进入 [云点播控制台](https://console.cloud.tencent.com/vod/license) 购买正式 License，其属于点播套餐包，根据不同的点播套餐包，我们会赠送您对应版本的 SDK 使用 License。
![](https://main.qcloudimg.com/raw/0ff40bb210ddcdc46b4703307cf2a4d2.png)

SDK 版本 License 与您需要购买的点播套餐包对应关系如下：

| SDK 版本 | 套餐包 |
|---------|---------|
| [精简版 SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播套餐精简版](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) | 
| [基础版 SDK（UGC）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播套餐基础版1或基础版2](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) | 
| [企业版 SDK（UGC_Enterprise）](https://cloud.tencent.com/document/product/584/9366#sdk) | 参见 [申请企业版本 License](#.E5.85.B3.E4.BA.8E.E4.BC.81.E4.B8.9A.E7.89.88.E6.9C.AC-license) | 
| [企业版 Pro SDK（EnterprisePro）](https://cloud.tencent.com/document/product/584/9366#sdk) | 参见 [申请企业版本 License](#.E5.85.B3.E4.BA.8E.E4.BC.81.E4.B8.9A.E7.89.88.E6.9C.AC-license) | 

>!**购买点播套餐包后，在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 测试 License 信息下面会有一键切换正式 License 按钮，当单击切换的时候，会再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请进行修改，一旦切换成功，License 信息不能再做修改。**

## License 使用方法
在调用 SDK 的相关接口前调用如下所示方法进行 License 的设置。

- iOS 建议在`- [AppDelegate application:didFinishLaunchingWithOptions:]`中添加：
```
[TXUGCBase setLicenceURL:LicenceUrl key:Key];
```
- Android 建议在 application 中添加：
```
TXUGCBase.getInstance().setLicence(context, LicenceUrl, Key);
```

## License 信息查看
在 License 设置成功后稍等一段时间（依据网络情况而定），可以通过调用以下方法查看 License 信息。

- iOS：
```
NSLog(@"%@", [TXUGCBase getLicenceInfo]);
```
- Android：
```
TXUGCBase.getInstance().getLicenceInfo(context);
```

## License 有效期与续费

可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看 License 的有效期，正式版本的 License 有效期一般为一年，到期后进入 [云点播控制台](https://console.cloud.tencent.com/vod/license) 单击购买链接即可。



## 关于企业版本 License

使用企业版本 License 可以开启优图实验室的 AI 功能，License 设置方法同上, 工程需要额外进行配置，具体配置请参见 [动效变脸](https://cloud.tencent.com/document/product/584/13509)。

[单击此处](https://cloud.tencent.com/product/x-magic) 申请企业版本 License。

## License 常见问题 FQA

1. 测试 License 到期后是否可以延期？
测试 License 试用期最多28天，是不能延期的，到期后请尽快购买正式 License。
2. 测试 License 能否更改 Android 的 PackageName 和 iOS 的 BundleID?
测试 License 是可以的，在控制台测试 License 信息右边有编辑按钮，可以单击编辑修改。
3. 正式 License 能否更改 Android 的 PackageName 和 iOS 的 BundleID?
当前版本，正式 License 不能更改 PackageName 和 BundleID，后续版本会加以支持。
4. License 可以同时支持多个 App 吗？
   一个 License 只能对应一个 PackageName 和 BundleID，不支持多个 App。
