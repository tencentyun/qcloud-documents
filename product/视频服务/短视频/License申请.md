## License申请

### 1. 申请测试License
您可以免费申请测试license（基础版，有效期28天）体验测试，具体步骤如下:
1 .登录腾讯云官网，进入 [点播控制台](https://console.cloud.tencent.com/video/license)，填写相应的信息，在 Package Name 中填写 Android 的包名，Bundle Id 中填写 iOS 的 bundleId。
   ![](https://main.qcloudimg.com/raw/148ea8cee25d6faea2d90bac30685d1c.png)

2 .创建成功后页面会显示生成的 License 信息，这里需要记下 Key 和 LicenseUrl，在SDK的初始化时需要传入这两个参数。

   ![](https://main.qcloudimg.com/raw/e45994fd46982632ad4e29469e67f64f.png)

### 2. 购买正式License
当您的测试License过期了，您需要进入 [点播控制台](https://console.cloud.tencent.com/video/license) 点击购买正式License，注意，您购买的是点播套餐包，根据点播套餐包，我们会赠送您对应版本SDK使用License，点播套餐包的购买截图如下：
 ![](https://main.qcloudimg.com/raw/01f8e581617aeaea3fc87fbbab16b075.png)

SDK版本License与您需要购买的点播套餐包对应关系如下：

| SDK版本 | 套餐包 |
|---------|---------|
| [精简版SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366) | 点播套餐精简版 | 
| [基础版SDK（UGC）](https://cloud.tencent.com/document/product/584/9366) | 点播套餐基础版1或者2 | 
| [商业版SDK（UGC_Enterprise）](https://cloud.tencent.com/document/product/584/9366) | 参考目录6申请商业版本License | 
| [商业版Pro SDK（EnterprisePro）](https://cloud.tencent.com/document/product/584/9366) | 参考目录6申请商业版本License | 

**注意: 购买点播套餐包后，在 [点播控制台](https://console.cloud.tencent.com/video/license) 测试License信息下面会有一键切换正式License按钮，当点击切换的时候，会再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请进行修改，一旦切换成功，License信息不能再做修改。**

### 3. License的使用方法
在调用SDK的相关接口前调用如下所示方法进行license的设置



iOS建议在`- [AppDelegate application:didFinishLaunchingWithOptions:]`中添加
```
[TXUGCBase setLicenceURL:LicenceUrl key:Key];
```

Android建议在 application 中添加:
```
TXLiveBase.getInstance().setLicence(context, LicenceUrl, Key);
```

### 4. License信息的查看
在license设置成功后稍等一段时间(依据网络情况而定), 可以通过调用以下方法查看License信息

iOS:
```
NSLog(@"%@", [TXUGCBase getLicenceInfo]);
```

Android:
```
TXLiveBase.getInstance().getLicenceInfo();
```

### 5.  License的有效期与续费

可以在 [点播控制台](https://console.cloud.tencent.com/video/license)查看License的有效期，正式版本的License有效期一般为一年，到期后进入 [点播控制台](https://console.cloud.tencent.com/video/license) 点击购买链接即可。



### 6.  关于商业版本License

使用商业版本 license 可以开启优图实验室的 AI 功能，License 设置方法同上, 工程需要额外进行配置，具体配置参考 [动效变脸](https://cloud.tencent.com/document/product/584/13509)。

单击此处 [申请商业版本 license](https://cloud.tencent.com/product/x-magic)。

### 7. License常见问题QA

1. 测试License到期后是否可以延期？

   测试License试用期最多28天是不能延期的，到期后请尽快购买正式License

2. 测试License能否更改Android的PackageName和iOS的BundleID?

   测试License是可以的，在控制台测试License信息右边有编辑按钮，可以点击编辑修改

3. 正式License能否更改Android的PackageName和iOS的BundleID?

   当前版本，正式License不能更改PackageName和BundleID，后续版本会加以支持

4. License可以同时支持多个APP吗？
   
   一个License只能对应一个PackageName和BundleID，不支持多个APP
