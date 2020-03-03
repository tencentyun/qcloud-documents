## SDK Information

You can update the [LVB SDK](https://cloud.tencent.com/document/product/454/7873) on Tencent Cloud's official website, which has the following versions:

| Version | Feature |
| ------ | ---------------------------- |
| LVB simplified version | Supports push, LVB, and VOD |
| Independent player version | Supports LVB and VOD |
| Short video feature version | Supports short video and VOD |
| Full-featured professional version | Supports push, LVB, VOD, joint broadcasting, and short video |
| Commercial enterprise version | Motion effect sticker, eyes beautifying and face slimming, and green screen keying-out features are added on the basis of full-featured professional version |

In professional version, for example, the decompressed SDK is composed as follows:

![](//mc.qcloudimg.com/static/img/5ef04a5e101beea834813e58fc5115ec/androidzippkg.png)

| File Name | Description | 
|---------|---------|
| SDK | Contains the SDK directory of framework | 
| Demo | The simplified demo based on framework, including a simple demonstration of UI and main SDK features. Use Xcode to quickly import the demo and try it out. |
| iOS package user guide.pdf | Describes the basic features of SDK |

## Xcode Project Settings

### 1. Supported platform

+ SDK is supported on iOS 8.0 or above.

### 2. Development environment

+ Xcode 9 or above
+ OS X 10.10 or above

### 3. Xcode project settings

Here, we use an iOS Application project to show you how to configure SDK in an Xcode project.

### 3.1 Copy SDK file

In this example, we create an iOS project named HelloSDK and copy the downloaded `TXLiteAVSDK_Professional.framework` to the project directory. The figure below shows the directory structure:

![](//mc.qcloudimg.com/static/img/d2b95540742662c006039adabb44188a/RTX20170811-210804.png)

### 3.2 Add framework

Add `TXLiteAVSDK_Professional.framework` to the project, and also add the following dependent libraries:

> (1) libz.tbd
> (2) libstdc++.tbd
> (3) libresolv.tbd
> (4) Accelerate.framework

### 3.3 Add header file
Add the header file search path to **Build Settings** -> **Search Paths** -> **User Header Search Paths**. Please note that this operation is not required. If you do not add the header file search path for TXLiteAVSDK_Professional, "TXLiteAVSDK_Professional/" needs to be added before the SDK-related header file when the header file is referenced, as shown below:
```
#import "TXLiteAVSDK_Professional/TXLivePush.h"
```

### 4. Verification

Call SDK API in the HelloSDK code and obtain SDK version information to verify whether the project is correctly configured.

### 4.1 Reference header file

Reference the SDK header file at the beginning of ViewController.m:

```
#import "TXLiteAVSDK_Professional/TXLiveBase.h"
```

### 4.2 Add calling code

Add the following code to viewDidLoad method:

```
- (void)viewDidLoad {
    [super viewDidLoad];
    //Print SDK version information
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
```

### 4.3 Compile and run the project

If all of the above steps are performed correctly, the HelloSDK project can be compiled successfully. Run the App in Debug mode. SDK version information is output in Xcode's Console pane.

> 2017-08-11 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 3.0.1185

Now, the project configuration is completed.

## Printing LOG
The code used to configure whether to print log from the console and set the log level in TXLiveBase is described as follows:
- **setConsoleEnabled**
Configures whether to print the output of SDK from the Xcode console.

- **setLogLevel**
Configures whether to allow SDK to print local log. By default, SDK writes log to the **Documents/logs** folder of the current App.
To get technical support, you are recommended to enable printing and provide the log file when a problem occurs. Thank you for your support.

- **View log file**
To reduce the storage size of logs, Mini LVB SDK encrypts local log files and limits the number of logs. Therefore, the log [decompression tool](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py) is required to view the text content of logs.

```
[TXLiveBase setConsoleEnabled:YES];
[TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```

- **SDK log callback**: You can print the logs to your log file by implementing the method in `TXLiveBaseDelegate` callback:

```
-(void) onLog:(NSString*)log LogLevel:(int)level WhichModule:(NSString*)module
```
