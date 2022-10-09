[](id:config)
## 配置方法
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

>!直播 License 集成使用腾讯特效（美颜特效）功能时，License 设置方法如上，但工程需要额外进行配置，具体操作请参见：
>- [AI 变脸和挂件（iOS）](https://cloud.tencent.com/document/product/454/9018) 
>- [AI 变脸和挂件（Android）](https://cloud.tencent.com/document/product/454/9020)


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
