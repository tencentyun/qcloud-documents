## Supported Platforms
- The SDK supports iOS 7.0 or above.

## Development Environment
- Xcode 7 or above;
- iOS SDK 7.0 or above.

## Xcode Project Settings
Below, we use a simple project of "Single View Application" to show you how to integrate SDK into the Xcode project.
### 1. Copy SDK file
In this example, the name of project is called HelloSDK, as shown below, and you copy the "libs" folder that contains all Frameworks (shown in "[Download SDK](http://cloud.tencent.com/doc/product/268/%E4%B8%8B%E8%BD%BDSDK%EF%BC%88iOS%EF%BC%89)") to the project folder:
![](//mccdn.qcloud.com/static/img/7a8b064e23365eeffefa67626d476147/image.png)

### 2. Set Framework Search Paths
Add $(PROJECT_DIR)/libs in "Build Settings > Search Paths > Framework Search Paths", as shown below:
![](//mccdn.qcloud.com/static/img/0fdb7f23372c3c75a4c2da3b2261950d/image.png)

### 3. Add SDK Framework
Add SDK Framework to the project, as shown below:
![](//mccdn.qcloud.com/static/img/2331e2f9a7be2af9c623dc71c6d8e453/image.png)

### 4. Add Other System Libraries
Add the SDK-dependent system libraries to the project, as shown below:
![](//mccdn.qcloud.com/static/img/3a161b0ef3c70f6cfb03441786697705/image.png)
The SDK-dependent system libraries are listed in alphabetical order below:
> 1. AVFoundation.framework
> 2. AudioToolBox.framework
> 3. CoreGraphics.framework
> 4. CoreMedia.framework
> 5. CoreTelephony.framework
> 6. CoreVideo.framework
> 7. Foundation.framework
> 8. libstdc++.6.tbd
> 9. libsqlite3.tbd
> 10. libz.tbd
> 11. libiconv.tbd
> 12. libc++.tbd
> 13. UIKit.framework


### 5. Close Bitcode
SDK does not support Bitcode. Set "Build Setting> Build Options> Enable Bitcode" to No, as shown below:
![](//mccdn.qcloud.com/static/img/c9967ba6ceb232d1cc4fd27bda7f541a/image.png)

## Verification
Next, call the SDK API in the codes of HelloSDK to obtain SDK version information and verify whether the project is correctly configured.
### 1. Reference the header file
Reference the header file of SDK at the beginning of ViewController.m:
`#import "QAVSDK/QAVSDK.h"`

### 2. Add calling code
Add the following code to the viewDidLoad method:
```
- (void)viewDidLoad {
    [super viewDidLoad];
    // Print SDK version information
    NSLog(@"SDK Version = %@", [QAVContext getVersion]);
}
```
### 3. Compile and run
The HelloSDK project can be successfully compiled and run if you performed the previous steps correctly. Run the App in Debug mode. SDK version information will be printed in Xcode's Console panel.
> 2016-04-26 11:35:05.807 HelloSDK[5288:358268] SDK Version = 1.8.0.258

