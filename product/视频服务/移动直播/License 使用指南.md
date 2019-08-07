## 申请测试 License
您可以免费申请测试 License（基础版，有效期28天）体验测试，具体步骤如下：
1. 登录腾讯云官网，进入 [移动直播 License](https://console.cloud.tencent.com/live/license)。
2. 填写【Package Name】为 Android 的包名，【Bundle Id】为 iOS 的 Bundle ID。
![](https://main.qcloudimg.com/raw/cb1d13cbdd1dd661a3147172ff163fa0.jpg)
3. 单击【免费创建】。
 创建成功后，页面会显示生成的 License 信息。请记录 Key 和 LicenseUrl，便于在 SDK 初始化时使用。
![](https://main.qcloudimg.com/raw/b923c8f3c4e586a3977b6c8fe023e16f.jpg)

<span id="buy"></span>
## 购买正式 License

您可以通过 [购买移动直播套餐](https://buy.cloud.tencent.com/mobilelive) 免费获得一年 License 使用权限。
![](https://main.qcloudimg.com/raw/52004efac93e7e6c8f446e53830816a3.png)

> ! 购买“移动直播 SDK 套餐包”后，在 [移动直播 License](https://console.cloud.tencent.com/live/license) 页面会出现【一键切换普通版】按钮。
> 单击【一键切换普通版】后需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请进行修改，一旦切换成功将无法再修改 License 信息。

<span id="config"></span>
## 配置 License

在调用 SDK 的相关接口前，您需要调用如下方法配置 License：

- iOS
 建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加：
```
[TXLiveBase setLicenceURL:LicenceUrl key:Key];
```
- Android
 建议在 application 中添加：
```
TXLiveBase.getInstance().setLicence(context, LicenceUrl, Key);
```

##  查看 License 信息
License 设置成功后（需稍等一段时间，具体时间长短依据网络情况而定），您可以通过调用以下方法查看 License 信息：

- iOS
```
NSLog(@"%@", [TXLiveBase getLicenceInfo]);
```
- Android
```
TXLiveBase.getInstance().getLicenceInfo();
```

## License 的有效期与续费

您可以登录 [移动直播 License](https://console.cloud.tencent.com/live/license) 页面查看 License 的有效期，
正式版 License 有效期一般为一年。License 到期后您可以在 [移动直播 License](https://console.cloud.tencent.com/live/license)  页面再次购买。

## 商业版 License
相比于专业版，商业版增加了基于腾讯优图实验室专利技术的人脸特效功能。使用商业版 License 可以开启优图实验室的 AI 功能，更多详情请参见 [美颜特效](https://cloud.tencent.com/product/x-magic)。
使用商业版本 License 时，License 设置方法同 [配置 License](#config)，但工程需要额外进行配置，具体操作请参见：
- [AI 变脸和挂件（iOS）](https://cloud.tencent.com/document/product/454/9018) 
- [AI 变脸和挂件（Android）](https://cloud.tencent.com/document/product/454/9020)

## License 常见问题

### 测试 License 到期后是否可以延期？
测试 License 试用期最多28天，不支持延期，到期后请尽快 [购买正式 License](#buy)。

### 测试 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
测试 License 能更改 Android 的 Package Name 和 iOS 的 Bundle ID。具体操作：登录控制台，单击测试 License 信息右侧的【编辑】，进入编辑页面即可修改 Android 的 Package Name 和 iOS 的 Bundle ID。

### 正式 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
当前版本，正式 License 不能更改 Package Name 和 Bundle ID。后续版本将会新增相关功能。

### License 可以同时支持多个 App 吗？
一个 License 只能对应一个 Package Name 和一个 Bundle ID，暂不支持多个 App。
