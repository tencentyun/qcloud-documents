This document describes how to integrate the TRTC SDK to an iOS device.
## Downloading Source Code
You can download the complete demo code used in this document.
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_import.zip)
## Procedure
### Create an iOS project
If you already have a project to integrate, skip to [Integrate the SDK](https://cloud.tencent.com/document/product/647/16809).
First, create a project with Xcode to integrate the SDK.
Open Xcode and click **File** -> **New** -> **Project**:
![](https://main.qcloudimg.com/raw/192e155a066ce28306a94063be358dbd.png)
Select **Single View App**
![](https://main.qcloudimg.com/raw/192e155a066ce28306a94063be358dbd.png)
Name the project as Demo01_integration SDK and select Objective-C as Language. Enter Team, Organization Name and Organization Identifier as needed. Click **Next**. Select a location to store the project, and then click **Create**.
### Integrate the SDK
#### Obtain the SDK
ILiveSDK is comprised of the following SDKs:
- BeautySDK: Provides beauty preprocessing
- IMSDK: Provides IM (Instant Messaging)
- AVSDK: Provides the underlying audio/video features
- ILiveSDK: Encapsulates audio/video APIs based on AVSDK to make them easy to use
- TILLiveSDK: Encapsulates LVB APIs based on ILiveSDK to allow users to access LVB features easily and quickly
Create a folder named ILiveSDK in the project directory to store the SDK.
#### Import the SDK
After the download is completed, right-click on **Project** -> **Add Files to "Demo01_integration SDK"** to import the SDK to the project:

Select the new **ILiveSDK** folder in the pop-up select box, and then click **Add**:

The added project directory is as follows:
  
#### Add system dependent libraries
Some system libraries relied on by SDKs in ILiveSDK need to be added to the project.
Click **PROJECT** -> **TARGETS** -> **General**. At the bottom of Linked Frameworks and Libraries section, click **+**, enter the system library name, and click **Add**.

List of system libraries to be added:
- Accelerate.framework
- AssetsLibrary.framework
- AVFoundation.framework
- CoreGraphics.framework
- CoreMedia.framework
- CoreTelephony.framework
- CoreVideo.framework
- ImageIO.framework
- JavaScriptCore.framework
- OpenAL.framework
- OpenGLES.framework
- QuartzCore.framework
- SystemConfiguration.framework
- VideoToolbox.framework
- libbz2.tbd
- libc++.tbd
- libiconv.tbd
- libicucore.tbd
- libprotobuf.tbd
- libresolv.tbd
- libsqlite3.tbd
- libstdc++.6.tbd
- libstdc++.tbd
- libz.tbd
All the added system libraries are stored in the Frameworks folder. To add these system libraries to your project in an easy manner, you can download our demo code ([Click to download](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_import.zip)) and directly drag the system libraries in the Frameworks folder to the Linked Frameworks and Libraries section under your project.
#### Configure the project
To use the SDK properly, you also need to make the following configurations:
-Configure ObjC
**Build Settings** -> **Other Linker Flags** -> **-ObjC**:

Configure Bitcode
**Build Settings** -> **Enable Bitcode** -> **No**:

### Run and check the SDK
After the above steps are completed, you can use ILiveSDK. Add the code to the viewDidLoad function of ViewController.m to obtain the version number:
```
//Import the header file
#import <ILiveSDK/ILiveCoreHeader.h>

//Obtain the version number
NSLog(@"ILiveSDK version:%@",[[ILiveSDK getInstance] getVersion]);
NSLog(@"AVSDK version:%@",[QAVContext getVersion]);
NSLog(@"IMSDK version:%@",[[TIMManager sharedInstance] GetVersion]);

//Print results
2018-03-27 15:22:37.187181+0800 Demo01_integration SDK[8182:16625633] ILiveSDK version:1.8.3.13017
2018-03-27 15:22:37.187692+0800 Demo01_integration SDK[8182:16625633] AVSDK version:1.9.6.47.OpenSDK_1.9.6- 34109
2018-03-27 15:22:37.189444+0800 Demo01_integration SDK[8182:16625633] IMSDK version:v2.5.6.11389.11327
```
You have successfully integrated ILiveSDK.
## Email
If you have any questions, send us an email to trtcfb@qq.com.

