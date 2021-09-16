## 直播推流 License

### 配置方法

调用 SDK 的相关接口前，您需要调用如下方法配置 License：
- **iOS：**建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加： 
```
[TXLiveBase setLicenceURL:LicenceUrl key:Key];
```
- **Android：**建议在 application 中添加：
```
TXLiveBase.getInstance().setLicence(context, LicenceUrl, Key);
```

> !使用美颜特效功能时，License 设置方法如上，但工程需要额外进行配置，具体操作请参见：
> - [直播美颜特效（iOS）](https://cloud.tencent.com/document/product/1449/57132)
> - [直播美颜特效（Android）](https://cloud.tencent.com/document/product/1449/57134)


### 查看方法
License 设置成功后（需稍等一段时间，具体时间长短依据网络情况而定），您可以通过调用如下方法查看 License 信息：

- **iOS：**
```
NSLog(@"%@", [TXLiveBase getLicenceInfo]);
```
- **Android：**
```
TXLiveBase.getInstance().getLicenceInfo();
```

 

## 短视频 License

### 配置方法

在调用 SDK 的相关接口前调用如下所示方法进行 License 的设置。

- **iOS：**  建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加：
```
[TXUGCBase setLicenceURL:LicenceUrl key:Key];
```
- **Android：** 建议在 application 中添加：
```
TXUGCBase.getInstance().setLicence(context, LicenceUrl, Key);
```

### 查看方法

在 License 设置成功后稍等一段时间（依据网络情况而定），可以通过调用以下方法查看 License 信息。

- **iOS：**
```
NSLog(@"%@", [TXUGCBase getLicenceInfo]);
```
- **Android：**
```
TXUGCBase.getInstance().getLicenceInfo(context);
```

