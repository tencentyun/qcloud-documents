
## Xcode Project Settings

### I. Supported Platform

+ SDK supports iOS 8.0 or above.

### II. Development Environment

+ Xcode 8 or above
+ OS X 10.10 or above

### III. Xcode Project Settings

A simple iOS Application project is shown below to illustrate how to configure SDK in an Xcode project.

### 1. Copy SDK File

In this example, an iOS project named HelloSDK is created, and the downloaded `TXLiteAVSDK_UGC.framework` is copied to the project directory. The figure below shows the directory structure.

![](//mc.qcloudimg.com/static/img/d2b95540742662c006039adabb44188a/RTX20170811-210804.png)

### 2. Add Framework

Add `TXLiteAVSDK_UGC.framework` to the project. At the same time, add the following dependent libraries:

> 1. libz.tbd
> 2. Accelerate.framework
> 3. Bugly.framework

After you've added the above libraries, the project dependency shows as follows:

![](//mc.qcloudimg.com/static/img/98f026d48d92df36eaa23f8304b84eaf/image.png)

### 3. Add Header File
Add the search path for header file to "Build Settings" -> "Search Paths" -> "User Header Search Paths". Please note that this operation is not required. If you do not add the header file search path for TXLiteAVSDK_UGC, "TXLiteAVSDK_UGC/" needs to be added before the SDK-related header file when the header file is referenced, as shown below:
```
#import "TXLiteAVSDK_UGC/TXUGCRecord.h"
```

### IV. Verification

Next, call the SDK API in the codes of HelloSDK to obtain SDK version information and verify whether the project is correctly configured.

### 1. Reference the Header File

Reference the SDK header file at the beginning of ViewController.m:

```
#import "TXLiteAVSDK_UGC/TXLiveBase.h"
```

### 2. Add Calling Code

Add the following code to the viewDidLoad method:

```
- (void)viewDidLoad {
    [super viewDidLoad];
    // Print SDK version information
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
```

### 3. Compile and Run

If all of the above steps are performed correctly, the HelloSDK project can be compiled successfully. Run the App in the Debug mode. SDK version information is output in Xcode's Console pane.

> 2017-09-26 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 3.4.1761 

Now, the project configuration is completed.

## Printing LOG
Configure whether to print log in the console and set the log level in TXLiveBase. Codes are described as follows:
- **setConsoleEnabled**
Configure whether to print the output of SDK in the Xcode console.

- **setLogLevel**
Configure whether to allow SDK to print local log. By default, SDK writes log to the **Documents/logs** folder of the current App.
For technical support, you are recommended to enable the sub-switch and provide the log file after a problem occurs. Thank you for your support.

- **View log file**
To reduce the storage volume of logs, Mini LVB SDK encrypts the log files stored locally and limits the number of logs. Therefore, you need to use the log [Decompression Tool](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py) to view the text content of log.

```
[TXLiveBase setConsoleEnabled:YES];
[TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```

