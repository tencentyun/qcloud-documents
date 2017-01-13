## Downloading SDK

You can download the mobile end [LVB SDK](https://www.qcloud.com/doc/api/258/6172) from the official website of Tencent Cloud, and get `TXRTMPSDK.framework` after decompression. At present, all the SDK functions are integrated in this framework.

## Xcode Project Settings

### I. Supported Platform

+ SDK supports the iOS 7.0 or above.

### II. Development Environment

+ Xcode 7 or a later version
+ OS X 10.10 or a later version

### III. Xcode Project Settings

A simple iOS Application project is provided below to describe how to configure the SDK in the Xcode project.

### 1. Copying the SDK file

In this example, an iOS project named HelloSDK is created, and the downloaded `TXRTMPSDK.framework` is copied to the project directory. The figure below shows the directory structure.

![](//mccdn.qcloud.com/static/img/235308a7d33f2f8c921a048737899c24/image.png)

### 2. Adding the framework

Add `TXRTMPSDK.framework` to the project. Meanwhile, add the following system dependency libraries:

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

The project dependency is shown below after all are added:

![](//mc.qcloudimg.com/static/img/0e012a7ab67e833eb33aec1e02f5d86b/image.jpg)

Close the Bitcode option of the project.

![](//mccdn.qcloud.com/static/img/4298f90507a749625d7e92cc9004c1b1/image.png)

### 3. Adding the header file
Add the header file search path to Build Settings -> Search Paths -> User Header Search Paths.  Note that this operation is not mandatory. If you didn't add the header file search path of TXRTMPSDK, "TXRTMPSDKSDK/" needs to be added before the header file when the related header file of SDK is quoted, as shown below:
```
#import "TXRTMPSDK/TXLivePush.h"
```

### III. Verifying

The SDK API is invoked below in the code of HelloSDK to get the SDK version information and verify whether the project settings are correct.

### 1. Quoting the header file

Quote the header file at the beginning of ViewController.m:

```
#import "TXRTMPSDK/TXLivePush.h"
```

### 2. Adding the invoking code

Add the code into the viewDidLoad method:

```
- (void)viewDidLoad {
    [super viewDidLoad];
    //Print the SDK version information
    NSLog(@"SDK Version = %@", [[TXLivePush getSDKVersion] componentsJoinedByString:@"."]);
}
```

### 3. Compiling for operation

If the operations in all the above steps are correct, the HelloSDK project can be smoothly compiled. Run the App in the Debug mode. The Console pane of Xcode will print the SDK version information.

> 2016-07-12 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 1.4.1

Now, the project configuration is completed.
