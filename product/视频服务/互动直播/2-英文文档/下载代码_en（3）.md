## Download Demo
Click to download the code for [iOS Demo]https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos). The code contains two samples:<br/>

1. Under the tdemolive directory is the simplest ILVB sample demonstrating how to call the key APIs. For more information on how to use it, please see the instructions on github.
2. Under the suixinbo directory is the new version of FreeShow code  demonstrating a complete live video broadcasting process covering interfaces and interactions at backend.


## Download and import SDKs to Frameworks
* [Download ILiveSDK, TILLiveSDK, AVSDK, IMSDK]https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos), and decompress them to the project directory suixinbo/Frameworks. The resulting directory of the project is as follows:
Frameworks directory

  ![Frameworks directory]http://mc.qcloudimg.com/static/img/139b6e97a13c9274c7371a6af6a0a530/image.png)
  
  AVSDK directory
  
  ![AVSDK directory]http://mc.qcloudimg.com/static/img/73d52880bdd252174f75e964b7d9c8eb/image.png)
  
  IMSDK directory
  
  ![IMSDK directory]http://mc.qcloudimg.com/static/img/819ee738975ccf61b510a58a9469b4ea/image.png)

* Import to Frameworks: copy the downloaded SDKs to the project directory by right-clicking the project directory and clicking " Add Files to 'your projectname'", as shown below:

  ![Import SDK to project ](http://mc.qcloudimg.com/static/img/7922154e7bdbbd0a6c24756d5b0a8866/image.png)

## Run the project
Compile and run the project (If xcode8 compiler fails, modify the Bundle Identifier, because the Bundle Identifier in the FreeShow project may not work on the user's machine. You just need to modify the Bundle Identifier by, for example, appending 1 to the original ID.)

* <div align=center>
<img src="https://mc.qcloudimg.com/static/img/1be6185cdb0f61756c85e230a9fc0514/2.png"/>
</div>
* ![](https://mc.qcloudimg.com/static/img/ccf7ca496a22ec0aed9d4446f30ba85f/1.png)

## Integrate into developer's code project
### 1. Introduce and import SDK to the project 

Refer to Step 2 above 

### 2. Modify the project configuration
* Copy the downloaded SDKs to the project directory by right-clicking the project directory and clicking **Add Files to 'your projectname'**, as shown below:

(1) Go to **Build Settings** -> **Linking** -> **Other Linker Flags**, and then add -ObjC configuration, as shown below:
![](http://mc.qcloudimg.com/static/img/9e48e62964428b6b12e11c262ff29178/image.png)


(2) Go to **Build Settings** -> **Linking** -> **Bitcode**, add Bitcode configuration, and then set it to NO, as shown below:
![](http://mc.qcloudimg.com/static/img/f473f6c580a4196af7d3d33edf140bdb/image.png)

(3) For iOS10 and above, you need to add device access configuration in the Info.plist.
![](http://mc.qcloudimg.com/static/img/e7b7897cb79a5cb9a984938dd4b3fda3/image.png)
If the above steps are correctly performed, the project can be compiled successfully.

### 3. Modify the backend address
Currently, FreeShow backend is mainly used to maintain the live room list. If you want to reuse FreeShow client code, you need to modify the backend address of FreeShow to the server address deployed at the business side. <br />     

| Request Class | Description | Modified File | Modification Method |
|---------|---------|---------|---------|
| LiveAVRoomIDRequest | Get the room number you assign | LiveAVRoomIDRequest.m | - (NSString *)url |
| LiveStartRequest | Create a new room | LiveStartRequest.m | - (NSString *)url |
| LiveEndRequest | Exit the room | LiveEndRequest.m | - (NSString *)url |
| LiveListRequest | Get room list | LiveListRequest.m | - (NSString *)url |
| LiveHostHeartBeatRequest | Room heartbeat | LiveHostHeartBeatRequest.m | - (NSString *)url |
| LiveImageSignRequest | Image upload-related | LiveImageSignRequest.m | - (NSString *)url |

### 4. Add system libraries
You can add the following system libraries by simply dragging the SystemLibrarys group from FreeShow project to your own project directory.

| The system libraries to be added |
|------------|
|libc++.tbd|
|libstdc++.tbd|
|libstdc++.6.tbd|
|libz.tbd|
|libbz2.tbd|
|libiconv.tbd|
|libresolv.tbd|
|libsqlite3.tbd|
|libprotobuf.tbd|
|UIKit.framework|
|CoreVideo.framework|
|CoreMedia.framework|
|Accelerate.framework|
|Foundation.framework|
|AVFoundation.framework|
|VideoToolbox.framework|
|CoreGraphics.framework|
|CoreTelephony.framework|
|SystemConfiguration.framework|

## Library Classes
------
| Frameworks Folder | Description |
|---|---|
| AVSDK | All audio/video-related SDKs |
| IMSDK | All IM-related SDKs |
| ILiveSDK | ILiveSDK and TILLiveSDK |

### Library class list
| No. | Name | Folder | Description |
|---|---|---|---|
| 1 | QAVSDK.framework | Frameworks/AVSDK/ | Audio/video SDK |
| 2 | xplatform.framework | Frameworks/AVSDK/ | SDKs for audio/video SDKs |
| 3 | IMCore.framework | Frameworks/IMSDK/ | IM Core Library |
| 4 | ImSDK.framework | Frameworks/IMSDK/ | IM SDK |
| 5 | IMSDKBugly.framework | Frameworks/IMSDK/ | Reporting SDK |
| 6 | QALSDK.framework | Frameworks/IMSDK/ | IM network module SDK |
| 7 | TLSSDK.framework | Frameworks/IMSDK/ | Login Service SDK |
| 8 | ILiveSDK.framework | Frameworks/ILiveSDK/ | ILVB Basic Features SDK |
| 9 | TILLiveSDK.framework | Frameworks/ILiveSDK/ | LVB SDK (SDK wrapped for LVB scenarios, including interactive joint broadcasting and other features) |

