This chapter helps you quickly integrate the MTA statistics feature. For more information on how to integrate the advanced feature, please see [Advanced Function Integration](/document/product/549/14976) or [API Description](/document/product/549/12859) MTA.h and MTAConfig.h header files.
Developers using CocoaPods can go to [https://github.com/tegdata/mta](https://github.com/tegdata/mta).

## Configuring Xcode Project
1. Go to [[SDK Download Center]](http://mta.qq.com/mta/ctr_index/download) to download the corresponding package to your local computer.
2. Decompress mta-ios-sdk-x.x.x.zip to the local directory, and then libmtasdk.a, MTA.h, and MTAConfig.h display in the SDK directory.
3. Add MTA.h, MTAConfig.h and libmtasdk.a to the project.
4. Add the following libraries or framework references: libz.tbd, libsqlite3.tbd, QuartzCore.framework, Security.framework, CFNetwork.framework, SystemConfiguration.framework, CoreTelephony.framework[](), UIKit.framework, Foundation.framework, CoreGraphics.framework, and libmtasdk.a. After that, the library references are as follows:
![](//mc.qcloudimg.com/static/img/2cbe5ee05515acbff5c3e05e98d777a9/image.png)
5. Add '-ObjC' parameter in Other Linker Flags of the project configuration, as shown below:
![](//mc.qcloudimg.com/static/img/dbd8742a715f2e1b414b731b6b28743b/image.png)

## Embedding MTA Code
1. Open AppDelegate.m in the project directory, and add import at the import part (beginning) of the file:
```
#import "MTA.h"
#import "MTAConfig.h"
```
2. Add the following statement in the launch method:
The launch method is as follows:

```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;
```
Add the following statement:
```
[MTA startWithAppkey:@"xxxx"]; //xxxx is the APPKEY obtained when you register the App
```
New code is as follows:
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // ...
    [MTA startWithAppkey:@"ABCDEFGH"];
    // ...
}
```

## Checking Data Reporting
After the SDK is embedded successfully, run the compiled App above (make sure that the MTA code has been executed) on the emulator or the phone, and then it will automatically report the data.
![](//mc.qcloudimg.com/static/img/4b864a1a4a7a2cfbb70e73a86a30fef3/image.png)
Log in to the MTA frontend, and refresh the App homepage about 5 seconds later. If the real-time metrics change, it means that the data have been successfully reported. If nothing changes for more than 3 minutes, check the followings in order:
1. Whether WiFi of the phone is enabled and whether the mobile is connected with the network;
2. Whether the APPKEY is set correctly;
3. Make sure that the MTA statistics code has been triggered;
4. Check Xcode's output for error messages.

## Completion of SDK Embedding
Now you have successfully integrated the MTA statistics feature. For more information on advanced service features, please see [API Description](https://cloud.tencent.com/document/product/549/12859).

