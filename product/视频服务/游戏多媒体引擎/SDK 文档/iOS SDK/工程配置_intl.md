Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes project configuration for iOS development so that iOS developers can easily debug and access APIs for Tencent Cloud GME.

## SDK Acquisition
You can obtain the SDK as follows.

### Download the SDK. 
Click the Tencent Cloud [Game Multimedia Engine](https://cloud.tencent.com/product/tmg?idx=1).  
![](https://main.qcloudimg.com/raw/4adb8befc9875a0823d1512f28ae046d.png)

On the displayed page, click "Developer Resources". Download the SDK resource package for iOS.
![](https://main.qcloudimg.com/raw/d7285fefc196e41aeedbf0193a9fc138.png)

Click **Download**. Decompress the downloaded SDK resource package. The following figure shows the folders in the package.

![](https://main.qcloudimg.com/raw/9202c60916f2ed826c050ec6144f20df.png)

## OS Requirements
The SDK can be run in iOS 7.0 and later versions.

## Preparation
### Import the SDK files.  
Add dependent libraries as required to "Link Binary With Libraries" in Xcode and set "Framework Search Paths" to the directory of the SDK, as shown in the following figure.  
![](https://main.qcloudimg.com/raw/9dd8d458734bc6e475581049e6cf26b1.png)

There are three framework folders in the **TMG_SDK** folder as follows.
>TMG.framework:

This audio-video SDK is mandatory.
>QAVSDKAuthBuffer.framework:

This SDK is used to generate encryption strings for voice chat room permissions. It can be deployed at the backend during formal deployment. Therefore, this SDK is not mandatory during project configuration.
>QAVSDKTlsSig.framework:

This SDK is used to generate encryption verification strings for PTT. If PTT is not used, this SDK is not required during project configuration.

### Add dependent libraries.  
For more information, see the following figure.  
![](https://main.qcloudimg.com/raw/8540aa69fc68da27341b785bbd9f031c.png)
  
### Disable Bitcode. 
Bitcode must be supported by all dependent class libraries of a project. As the SDK temporarily does not support Bitcode, it can be disabled for now.
To disable Bitcode, you need to search for Bitcode on "Targets" -> "Build Settings", and then set "Enable Bitcode" to "No".
An example is shown in the following figure.  
![](https://main.qcloudimg.com/raw/82c628e8a7d9a4bebc842c8545d9563a.png)
