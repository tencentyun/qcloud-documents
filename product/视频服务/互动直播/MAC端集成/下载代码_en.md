## I. Download Demo
Click to download the code for [Mac Demo](https://github.com/zhaoyang21cn/iLiveSDK_Mac_Suixinbo), demonstrating a complete live video broadcasting process covering interfaces and interactions at backend.<br/>

## II. Decompress the SDK package

Because there is a file upload limit of 100MB on Github, so QAVSDK will be compressed and then uploaded in the FreeShow project. To make the FreeShow operate normally, please ask the developers to decompress iLiveSDK_Mac_Suixinbo/SuixinboForMac/FrameworksMac/AVSDK.zip to the current directory. After the decompression, the file directory is as follows:

![](http://mc.qcloudimg.com/static/img/e70b619d7c575b395680c4242f528f4f/image.png)

## III. Run the project

1. Run the installation package directly (In the downloaded Demo project, SuiXinBoForMac.dmg can be run directly).

2. Compile source codes to run the project(Supported for MacOS 10.7 or above). 

The actual images are shown in the following figure:

* <div align=center>
<img src="http://mc.qcloudimg.com/static/img/2b146c664a2d0d74f3a57a79d8c06a2b/image.png"/>

* <div align=center>
<img src="http://mc.qcloudimg.com/static/img/d34af5a50720dca145728112d2195522/image.png"/>

## IV. Integrate into developer's code project
### 1. Introduce and import SDK to the project 

Refer to the second step above, and add all the SDKs in FrameworksMac to your own project. 

### 2. Modify the project configuration
* Copy the downloaded SDKs to the project directory by right-clicking the project directory and clicking " Add Files to 'your projectname'", as shown below:

(1) Go to "Build Settings"->"Linking"-> "Other Linker Flags", and then add -ObjC configuration, as shown below:
![](http://mc.qcloudimg.com/static/img/9e48e62964428b6b12e11c262ff29178/image.png)

(2) Go to "Build Settings"->"macOS Deployment Target"->"macOS 10.7" to set the lowest version greater than or equal to 10.7, as shown below:

![](http://mc.qcloudimg.com/static/img/592954bf985115b7089147800a3667c8/image.png)

If the above steps are correctly performed, the project can be compiled successfully.

### 3. Add system libraries
You can add the following system libraries by simply dragging the SystemLibrarys group from suixinbo project to your own project directory.

| The system libraries to be added |
|------------|
|QuartzCore.framework|
|CoreTelephony.framework|
|CoreWLAN.framework|
|Foundation.framework|
|SystemConfiguration.framework|
|libc++.tbd|
|libiconv.tbd|
|libresolv.9.tbd|
|libsqlite3.tbd|
|libstdc++.6.tbd|
|libz.tbd|

### 4. Add Tencent's dependent libraries

| No. | Name | Folder | Description | Required |
|--|--|--|--|--|
| 1 | QAVSDK.framework | FrameworksMac/AVSDK/ | Audio/video SDK | Yes |
| 2 | xplatform.framework | FrameworksMac/AVSDK/ | Audio/video cross-platform support library | Yes |
| 3 | IMCore.framework | FrameworksMac/IMSDK/ | IM Core Library | Yes |
| 4 | ImSDK.framework | FrameworksMac/IMSDK/ | IM Mac platform encapsulation library | Yes |
| 5 | QALSDK.framework | FrameworksMac/IMSDK/ | IM network module SDK | Yes |
| 6 | TLSSDK.framework | FrameworksMac/IMSDK/ | IM Login Service SDK | Yes |
| 7 | ILiveSDK.framework | FrameworksMac/ | ILVB Basic Features SDK | Yes |
| 8 | TILFilterSDK.framework | FrameworksMac/ | ILVB beauty filter dependent library | No |


