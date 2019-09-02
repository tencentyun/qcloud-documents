
## Short Video License Integration
- After obtaining the license for basic short video SDK, you need to rename it to TXUgcSDK.licence and link it to Xcode project. If your license expires, log in to Tencent Cloud VOD console to obtain the latest license and replace the license in the application with it.
- Note: The name of license is "TXUgcSDK.licence". License is linked to Xcode project to ensure that license information can be read in SDK.

## Xcode Project Settings

### Supported Platform

+ SDK is supported on iOS 8.0 or above.

### Development Environment

+ Xcode 9 or above
+ OS X 10.10 or above

### Xcode Project Settings

Here, we use an iOS Application project sample to show you how to configure SDK in an Xcode project.

#### Copying SDK File

In this example, create an iOS project named HelloSDK, and copy the downloaded `TXLiteAVSDK_UGC.framework` to the project directory. The figure below shows the directory structure:
![](//mc.qcloudimg.com/static/img/d2b95540742662c006039adabb44188a/RTX20170811-210804.png)

#### Adding Framework

Add `TXLiteAVSDK_UGC.framework` and the following dependent libraries to the project:

> 1. libz.tbd
> 2. Accelerate.framework
> 3. Bugly.framework

After the above libraries are added, the project dependency shows as follows:
![](//mc.qcloudimg.com/static/img/98f026d48d92df36eaa23f8304b84eaf/image.png)

#### Adding Header File
Add the search path for header file to **Build Settings** -> **Search Paths** -> **User Header Search Paths**. Please note that this operation is not required. If you do not add the header file search path for TXLiteAVSDK_UGC, "TXLiteAVSDK_UGC/" needs to be added before the SDK-related header file when the header file is referenced, as shown below:

```	objc
#import "TXLiteAVSDK_UGC/TXUGCRecord.h"
```

#### Integration of Short Video Publishing

Short video publishing feature is provided in source code. You need to integrate the source code into your project manually.

- Copy the source code directory Demo/TXLiteAVDemo/VideoUpload to your project directory.

- Drag VideoUpload directory to the proper location in Xcode project. Select **Added floders: Create groups** in the pop-up box, then select the target to which the directory is added, and click **Finish**.
![](https://main.qcloudimg.com/raw/39a08faa6d2d98049c894ba8a2d371d5.png)

- Add the following system libraries:

> 1. CoreTelephony
> 2. Foundation
> 3. SystemConfiguration
> 4. libstdc++.tbd

#### Adding -ObjC
To load class methods used in the SDK, you need to add -ObjC in **Build Settings** -> **Linking** -> **Other Linker Flags** of your project. Otherwise, an error may occur when you run the project because class method cannot be found.

 
#### Verification
Call SDK API in the HelloSDK code and obtain SDK version information to verify whether the project is correctly configured.

##### Referencing Header File

Reference SDK header file before ViewController.m:

```	objc
#import "TXLiteAVSDK_UGC/TXLiveBase.h"
```

#### Adding Calling Code

Add the following code to viewDidLoad method:

```	objc
- (void)viewDidLoad {
    [super viewDidLoad];
    // Print SDK version information
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
```

#### Compiling and Running Project

If all of the above steps are performed correctly, HelloSDK project can be compiled successfully. Run the App in Debug mode. SDK version information is output in Xcode's Console pane.

> 2017-09-26 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 3.4.1761 

Now, the project configuration is completed.

## Printing LOG
Configure whether to print log from the console and set the log level in TXLiveBase. Codes are described as follows:
- **setConsoleEnabled**
Configure whether to print the output of SDK in the Xcode console.

- **setLogLevel**
Configure whether to allow SDK to print local log. By default, SDK writes log to the **Documents/logs** folder of the current App.
To get technical support, you are recommended to enable printing and provide the log file when a problem occurs. Thank you for your support.

- **View log file**
To reduce the storage size of logs, Mini LVB SDK encrypts local log files and limits the number of logs. Therefore, the log [decompression tool](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py) is required to view the text content of logs.

```	objc
[TXLiveBase setConsoleEnabled:YES];
[TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```

