## Overview

Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. This document provides project configuration that makes it easy for iOS developers to debug and integrate the APIs for GME.

## SDK Preparation

You can obtain the SDK by the following way:

### 1. Please download applicable Demo and SDK from [Downloading Instruction](https://cloud.tencent.com/document/product/607/18521).

### 2. Pinpoint the SDK resource for iOS on the page.

### 3. Click the **Download** button.

The decompressed SDK resource is composed as follows:

| Name | Description   
| ------------- |:-------------:|
| GMESDK.framework			| Game Multimedia Engine related resources

## System Requirement

You can run the SDK on iOS 7.0 or later.

## Preparations

### 1. Import SDK file

Add the following dependent library to the Link Binary With Libraries of Xcode as needed, and set Framework Search Paths to point to the directory where the SDK resides, as shown below:  

![](https://main.qcloudimg.com/raw/9dd8d458734bc6e475581049e6cf26b1.png)

### 2. Add dependent libraries

Refer to the figure below:  

![](https://main.qcloudimg.com/raw/b6156b8c7a596248c148607070e38f67.png)

### 3. Disable Bitcode

Bitcode should be supported by all class libraries that the project depends on. Bitcode is not supported by the SDK, so it can be disabled.
To disable Bitcode, search Bitcode under **Targets** -> **Build Settings** and set the corresponding option to NO.
See the figure below:  
![](https://main.qcloudimg.com/raw/82c628e8a7d9a4bebc842c8545d9563a.png)

### 4. Apply for permissions

Tencent Cloud Audio/Video Engine requires the following permissions on iOS:

| key | Description   
| ------------- |:-------------:|
| Required background modes | Allows running in the background |
| Microphone Usaeg Description | Allows microphone permission |

### 5. Allow Arbitrary Loads

![image](https://main.qcloudimg.com/raw/1aebf9111fd95e3e6b6fb4eb08193a26.png)