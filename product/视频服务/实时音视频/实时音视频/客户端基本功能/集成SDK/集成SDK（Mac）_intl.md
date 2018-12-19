This document describes how to integrate the TRTC SDK to a Mac device.
## Downloading Source Code
You can download the complete demo code used in this document.
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/MAC_TRTC.zip)
## Procedure
### Create a Mac project
If you already have a project to integrate, skip to [Integrate the SDK](https://cloud.tencent.com/document/product/647/19554).
First, create a project with Xcode to integrate the SDK.
Open Xcode and click **File** -> **New** -> **Project**:
![](https://main.qcloudimg.com/raw/07cdd8293bdeb83e0be5bd2452f6a06e.png)
Select **macOS** -> **Cocoa App**
![](https://main.qcloudimg.com/raw/d78e4346ec09d699fc8af3afb48e3337.png)
Name the project as TRTCMac Integration SDK and select Objective-C as Language. Enter Team, Organization Name and Organization Identifier as needed. Click **Next**. Select a location to store the project, and then click **Create**.
#### Integrate the SDK
#### Obtain the SDK
ILiveSDK for Mac is comprised of the following SDKs:
- IMSDK: Provides IM (Instant Messaging)
- AVSDK: Provides the underlying audio/video features
- ILiveSDK: Encapsulates audio/video APIs based on AVSDK to make them easy to use

Create a folder named FrameworksMac in the project directory to store the SDK. As ILiveSDK has multiple SDKs, an [SDK download script](http://dldir1.qq.com/hudongzhibo/ILiveSDK/LoadSDK.sh) is provided for you to obtain all these SDKs.
Click the download script and place it under the FrameworksMac folder you just created:
![](https://main.qcloudimg.com/raw/c2abae1c483861e7c8117d25673d1915.png)
Run the download script (Open the terminal, run the cd command to go to the FrameworksMac directory, and then run sh LoadSDK.sh) to download all the SDKs. After a moment, the downloaded package will be automatically decompressed and deleted.
#### Import the SDK
After the download is completed, right-click on **Project** -> **Add Files to "TRTCMac"** to import the SDK to the project:
![](https://main.qcloudimg.com/raw/fda07853f441f7838717ef065b11f84f.png)
Select the new **FrameworksMac** folder in the pop-up select box, and then click **Add**:
![](https://main.qcloudimg.com/raw/2d5cdd40be02fce97889e40971f8aa6b.png)
The added project directory is as follows:
![](https://main.qcloudimg.com/raw/a3a3c5861d56dad4150cda6608af6a85.png)  
#### Add system dependent libraries
Some system libraries relied on by SDKs in ILiveSDK need to be added to the project.
Click **PROJECT** -> **TARGETS** -> **General**. At the bottom of Linked Frameworks and Libraries section, click **+**, enter the system library name, and click **Add**.
![](https://main.qcloudimg.com/raw/6afac63510536fe9d4542ab8a38425ca.png)
List of system libraries to be added
- libsqlite3.tbd
- libiconv.tbd
- libstdc++.6.tbd
- libc++.tbd
- libz.tbd
- libresolve.9.tbd
- CoreWLAN.framework
- QuartzCore.framework
- QAVSDK.framework
- TLSSDK.framework
- QALSDK.framework
- ILiveSDK.framework
- IMCore.framework
- IliveLogReport.framework
- TILFilterSDK.framework
- ImSDK.framework

All the added system libraries are stored in the Frameworks folder. To add these system libraries to your project in an easy manner, you can download our demo code ([Click to download](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_import.zip)) and directly drag the system libraries in the Frameworks folder to the Linked Frameworks and Libraries section under your project.
#### Configure the project
To use the SDK properly, you also need to make the following configurations:
-Configure ObjC
**Build Settings** -> **Other Linker Flags** -> **-ObjC**:
![](https://main.qcloudimg.com/raw/3a8c59d55d750e13260809e83d5b6029.png)

#### Run and check the SDK
After the above steps are completed, you can use ILiveSDK. Add the code to the viewDidLoad function of ViewController.m to obtain the version number:
```
//Import the header file
#import <ILiveSDK/ILiveCoreHeader.h>

//Obtain the version number
NSLog(@"ILiveSDK version:%@",[[ILiveSDK getInstance] getVersion]);
NSLog(@"AVSDK version:%@",[QAVContext getVersion]);
NSLog(@"IMSDK version:%@",[[TIMManager sharedInstance] GetVersion]);

//Print results
2018-09-03 11:49:28.060945+0800 TRTCMac[73399:23447259] ILiveSDK version:1.9.3.13966
2018-09-03 11:49:28.060956+0800 TRTCMac[73399:23447259] AVSDK version:1.9.9.1012.Local
2018-09-03 11:49:28.060969+0800 TRTCMac[73399:23447259] IMSDK version:v2.5.4.10421.10420
```
You have successfully integrated ILiveSDK.
## Email
If you have any questions, send us an email to trtcfb@qq.com.

