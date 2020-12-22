## License 使用方法

在调用 SDK 的相关接口前调用如下所示方法进行 License 的设置。

- iOS 建议在：`[AppDelegate application:didFinishLaunchingWithOptions:] `添加如下：
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
 NSLog(@"%@", [TXUGCBase getLicenceInfo]);```
 
- Android：
 ```
 TXUGCBase.getInstance().getLicenceInfo(context);
 ```
