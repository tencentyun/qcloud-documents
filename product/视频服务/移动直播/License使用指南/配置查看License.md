[](id:config)
## 配置方法
调用 SDK 的相关接口前，您需要调用如下方法配置 License：
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

>!使用企业版本 License 时，License 设置方法如上，但工程需要额外进行配置，具体操作请参见：
- [AI 变脸和挂件（iOS）](https://cloud.tencent.com/document/product/454/9018) 
- [AI 变脸和挂件（Android）](https://cloud.tencent.com/document/product/454/9020)


## 查看方法
License 设置成功后（需稍等一段时间，具体时间长短依据网络情况而定），您可以通过调用如下方法查看 License 信息：

- **iOS**
```
NSLog(@"%@", [TXLiveBase getLicenceInfo]);
```
- **Android**
```
TXLiveBase.getInstance().getLicenceInfo();
```

 
