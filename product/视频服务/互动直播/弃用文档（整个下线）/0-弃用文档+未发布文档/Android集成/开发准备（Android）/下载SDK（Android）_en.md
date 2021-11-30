## Download SDK
You can download the ILVB SDK from [Tencent Cloud Official Website](http://cloud.tencent.com/product/ilvb.html).
> http://cloud.tencent.com/product/ilvb.html

## Directory Description
The SDK you downloaded from the official website mainly contains the following folders:

| Folder | Description |
|---------|---------|
| docs | Contains certain development documents. We will soon ask our HR to migrate them to Tencent Cloud document center so developers can consult the documents conveniently.  |
| libs | SDK is provided to App in the form of "jar" and "so" files. The libs folder contains all these files.  |
## SDK File Introduction
The libs folder contains "jar" and "so" files for two major SDKs:

| SDK Name | Description |
|---------|---------|
| AVSDK | Used to realize core audio/video communication capabilities.  |
| IMSDK | Used to realize capabilities used in audio/video communication such as third-party account system access, account login authentication and so on. It's also integrated with crash reporting module.  |

**Note:** There are certain dependencies between the files for these two major SDKs when compiling (the files call each other during operations), thus App developers must make sure that all files listed below are complete when updating and replacing SDKs. Replacing only some of the files may introduce exceptions.

For more information about IMSDK, please see the link below:
> http://cloud.tencent.com/product/im.html

## SDK File List
### 1. AVSDK file list
| No.  | Name | Folder | Description |
|---------|---------|---------|---------|
| 1 | qavsdk.jar | libs\jar | Audio/video SDK. |
| 2 | libhwcodec.so | libs\armeabi | Encode/decode.  |
| 3 | libqav_graphics.so | libs\armeabi | Audio/video graphical interface. |
| 4 | libqavsdk.so | libs\armeabi |  Audio/video SDK. |
| 5 | libstlport_shared.so | libs\armeabi | Audio/video base library.  |
| 6 | libTcVpxDec.so | libs\armeabi | Video component. |
| 7 | libTcVpxEnc.so | libs\armeabi | Video component.  |
| 8 | libtraeimp-armeabi-v7a.so | libs\armeabi | Audio component. |
| 9 | libxplatform.so | libs\armeabi | Audio/video base library. | 
**Note:** App developers must make sure that all files mentioned above are complete when updating and replacing SDKs. Replacing only some of the files may introduce exceptions.

### 2. IMSDK file list
| No.  | Name | Folder | Description |
|---------|---------|---------|---------|
| 1 | beacon_1.5.3_imsdk_release.jar | libs\jar | Audio/video SDK. |
| 2 | bugly_1.2.8_imsdk_release.jar | libs\jar | Instant messaging crash report.
| 3 | imsdk.jar | libs\jar | Instant messaging SDK. |
| 4 | mobilepb.jar | libs\jar | protouf encode/decode related. |
| 5 | qalsdk.jar | libs\jar | imsdk network layer. |
| 6 | tls_sdk.jar | libs\jar | Login related. |
| 7 | wup-1.0.0-SNAPSHOT.jar | libs\jar | imSdk related dependent package. |
| 8 | lib_imcore_jni_gyp.so | libs\armeabi |  Instant messaging. |
| 9 | libBugly.so | libs\armeabi | Crash report. |
| 10 | libqalcodecwrapper.so | libs\armeabi | qalsdk related. |
| 11 | libqalmsfboot.so | libs\armeabi | qalsdk related. |
| 12 | libwtcrypto.so | libs\armeabi | Login dependency. |
**Note:** App developers must make sure that all files mentioned above are complete when updating and replacing SDKs. Replacing only some of the files may introduce exceptions.
