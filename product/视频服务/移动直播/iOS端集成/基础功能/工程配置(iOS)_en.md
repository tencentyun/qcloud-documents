## Download SDK
You can download the [LVB SDK](https://cloud.tencent.com/document/product/454/7873) for mobile devices from Tencent Cloud's official website. Decompress the downloaded file to acquire `TXRTMPSDK.framework`. Currently, all features of the SDK are integrated inside this framework.

## Xcode Project Settings

### I. Supported Platforms

+ The SDK supports iOS 7.0 or above.

### Ⅱ. Development Environment

+ Xcode 7 or above
+ OS X 10.10 or above

### Ⅲ. Xcode Project Settings

A simple iOS Application project is shown below to illustrate how to configure SDK in an Xcode project.

### 1. Copy SDK file

In this example, we create an iOS project named HelloSDK and copy the downloaded `TXRTMPSDK.framework` to the project directory. The figure below shows the directory structure:

![](//mccdn.qcloud.com/static/img/235308a7d33f2f8c921a048737899c24/image.png)

### 2. Add Framework

Add `TXRTMPSDK.framework` to the project. At the same time, add the following dependent libraries

> 1. VideoToolbox.framework
> 2. SystemConfiguration.framework
> 3. CoreTelephony.framework
> 4. AVFoundation.framework
> 5. CoreMedia.framework
> 6. CoreGraphics.framework
> 7. libstdc++.tbd
> 8. libz.tbd
> 9. libiconv.tbd
> 10. libresolv.tbd

After you've added the contents above, the project dependency will look like this:

![](//mc.qcloudimg.com/static/img/0e012a7ab67e833eb33aec1e02f5d86b/image.jpg)

Disable the Bitcode option of the project.

![](//mccdn.qcloud.com/static/img/4298f90507a749625d7e92cc9004c1b1/image.png)

### 3. Add Header File
Add header file search path in "Build Settings" -> "Search Paths" -> "User Header Search Paths". Note that this operation is not mandatory. If you do not add the header file search path for TXRTMPSDK, then you need to add "TXRTMPSDKSDK/" when you reference header files, as shown below:
```
#import "TXRTMPSDK/TXLivePush.h"
```

### III. Verify

Next, call the SDK API in the codes of HelloSDK to obtain SDK version information and verify whether the project is correctly configured.

### 1. Reference the Header File

Reference the SDK header file at the beginning of ViewController.m:

```
#import "TXRTMPSDK/TXLivePush.h"
```

### 2. Add Calling Code

Add the following code to the viewDidLoad method:

```
- (void)viewDidLoad {
    [super viewDidLoad];
    // Print SDK version information
    NSLog(@"SDK Version = %@", [[TXLivePush getSDKVersion] componentsJoinedByString:@"."]);
}
```

### 3. Compile and Run

The HelloSDK project can be successfully compiled and run if you performed the previous steps correctly. Run the App in Debug mode. SDK version information will be printed in Xcode's Console panel.

> 2016-07-12 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 1.4.1

Now, the project configuration is completed.

