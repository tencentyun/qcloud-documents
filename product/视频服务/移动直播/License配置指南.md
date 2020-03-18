若您使用的测试版/正式版 License，在调用 SDK 的相关接口前，您需要调用如下方法配置 License：

- **iOS**
 建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加：
```
[TXLiveBase setLicenceURL:LicenceUrl key:Key];
```
-  **Android**
 建议在 application 中添加：
```
TXLiveBase.getInstance().setLicence(context, LicenceUrl, Key);
```

### 查看 License 信息
License 设置成功后（需稍等一段时间，具体时间长短依据网络情况而定），您可以通过调用以下方法查看 License 信息：

- **iOS**
```
NSLog(@"%@", [TXLiveBase getLicenceInfo]);
```
- **Android**
```
TXLiveBase.getInstance().getLicenceInfo();
```


### 配置企业版 License 
使用企业版本 License 时，License 设置方法同 [配置 License](#config)，但工程需要额外进行配置，具体操作请参见：
- [AI 变脸和挂件（iOS）](https://cloud.tencent.com/document/product/454/9018) 
- [AI 变脸和挂件（Android）](https://cloud.tencent.com/document/product/454/9020)
