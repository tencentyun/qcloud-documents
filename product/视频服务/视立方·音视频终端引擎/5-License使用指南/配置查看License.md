## 直播和视频播放 License

### 配置方法

调用 SDK 的相关接口前，您需要调用如下方法配置 License：
- **iOS**
 建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加： 
```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSString * const licenceURL = @"<获取到的licenseUrl>";
    NSString * const licenceKey = @"<获取到的key>";

    // V2TXLivePremier 位于 "V2TXLivePremier.h" 头文件中
    [V2TXLivePremier setLicence:licenceURL key:licenceKey];
    [V2TXLivePremier setObserver:self];
    NSLog(@"SDK Version = %@", [V2TXLivePremier getSDKVersionStr]);
    return YES;
}

#pragma mark - V2TXLivePremierObserver
- (void)onLicenceLoaded:(int)result Reason:(NSString *)reason {
    NSLog(@"onLicenceLoaded: result:%d reason:%@", result, reason);
}
@end
```
-  **Android**
 建议在 application 中添加：
```
public class MApplication extends Application {

@Override
public void onCreate() {
    super.onCreate();
    String licenceURL = ""; // 获取到的 licence url
    String licenceKey = ""; // 获取到的 licence key
    V2TXLivePremier.setLicence(this, licenceURL, licenceKey);
    V2TXLivePremier.setObserver(new V2TXLivePremierObserver() {
            @Override
            public void onLicenceLoaded(int result, String reason) {
                Log.i(TAG, "onLicenceLoaded: result:" + result + ", reason:" + reason);
            }
        });
}
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
- **iOS**
 建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加： 
```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSString * const licenceURL = @"<获取到的licenseUrl>";
    NSString * const licenceKey = @"<获取到的key>";

    //TXUGCBase 位于 "TXUGCBase.h" 头文件中
    [TXUGCBase setLicenceURL:licenceURL key:licenceKey]; 
    NSLog(@"SDK Version = %@", [TXUGCBase getSDKVersionStr]);
    return YES;
}

- (void)onLicenceLoaded:(int)result Reason:(NSString *)reason {
    NSLog(@"onLicenceLoaded: result:%d reason:%@", result, reason);
}
@end
```
-  **Android**
 建议在 application 中添加：
```
public class MApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        String licenceURL = ""; // 获取到的 licence url
        String licenceKey = ""; // 获取到的 licence key
        TXUGCBase.getInstance().setLicence(this, licenceURL, licenceKey);
        TXUGCBase.setListener(new TXUGCBaseListener() {
            @Override
            public void onLicenceLoaded(int result, String reason) {
                Log.i(TAG, "onLicenceLoaded: result:" + result + ", reason:" + reason);
            }
        });
    }
}
```

>? 直播 License、短视频 License 和视频播放 License ，若 licenceURL 一样，全局仅设置一次即可，无需重复设置。若您暂未获取上述 License ，可 [快速免费申请测试版 License](https://cloud.tencent.com/act/event/License) 以正常播放，正式版 License 需 [购买](https://cloud.tencent.com/document/product/454/34750)。

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
