本章节将帮助您快速接入使用的 MTA 统计功能，高级功能接入请参考 [高级功能接入](/document/product/549/14976)或者 [接口说明](/document/product/549/12859) MTA.h 以及 MTAConfig.h 头文件。
使用 CocoaPods 的开发者可前往 [https://github.com/tegdata/mta](https://github.com/tegdata/mta)。

## 配置 Xcode 工程
1. 前往[【SDK 下载中心】](http://mta.qq.com/mta/ctr_index/download)下载对应压缩包到本地；
2. 解压 mta-ios-sdk-x.x.x.zip 到本地目录，可以看到其中 SDK 目录下的三个文件 libmtasdk.a，MTA.h，MTAConfig.h；
3. 将 MTA.h，MTAConfig.h 以及 libmtasdk.a 添加到工程；
4. 添加以下库或者 framework 的引用 libz.tbd，libsqlite3.tbd，QuartzCore.framework，Security.framework， CFNetwork.framework，SystemConfiguration.framework，CoreTelephony.framework[]()，UIKit.framework， Foundation.framework，CoreGraphics.framework 以及 libmtasdk.a，添加完成后，库的引用如下：
![](//mc.qcloudimg.com/static/img/2cbe5ee05515acbff5c3e05e98d777a9/image.png)
5. 在工程配置的 Other Linker Flags 中添加 '-ObjC' 参数，如下图：
![](//mc.qcloudimg.com/static/img/dbd8742a715f2e1b414b731b6b28743b/image.png)

## 嵌入 MTA 代码
1.切换到工程目录，打开 AppDelegate.m，在文件开头 import 部分增加 import：
```
#import "MTA.h"
#import "MTAConfig.h"
```
2.在启动方法内添加如下语句：
该启动方法为：

```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;
```
添加该语句：
```
[MTA startWithAppkey:@"xxxx"]; //xxxx为注册App时得到的APPKEY
```
添加完成后的代码如下：
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // ...
    [MTA startWithAppkey:@"ABCDEFGH"];
    // ...
}
```

## 验证数据上报
成功嵌入 SDK 后，在模拟器或手机运行您上面已经编译好的应用（确保已执行 MTA 代码），便会自动上报数据。
![](//mc.qcloudimg.com/static/img/4b864a1a4a7a2cfbb70e73a86a30fef3/image.png)
登录 MTA 前台，等待 5 秒钟左右再刷新 App 首页，实时指标将有变化，表示已成功上报；若超过 3 分钟指标仍未变化，请按以下顺序检查：
1. 手机的 WiFi 是否打开，是否正常联网；
2. APPKEY 设置是否正确；
3. 确保已触发 MTA 统计代码；
4. 查看 Xcode 的输出是否有错误信息。

## SDK 嵌入完成
到这里您已经顺利接入 MTA 的统计功能，需要获得更高级的服务功能，请参考 [接口说明](https://cloud.tencent.com/document/product/549/12859)。
