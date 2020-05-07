## Download SDK
You can download the ILVB SDK from [Tencent Cloud Official Website](http://cloud.tencent.com/product/ilvb.html).
> http://cloud.tencent.com/product/ilvb.html

## Directory Description
The SDK you downloaded from the official website mainly contains the following folders:

| Folder | Description |
|---------|---------|
| docs | Contains certain development documents. We will soon ask our HR to migrate them to Tencent Cloud document center so developers can consult the documents conveniently.  |
| libs | SDK is provided to App in the form of "Framework". The "libs" folder contains all these Frameworks.  |
## SDK File Introduction
The "libs" folder contains the Frameworks for two major SDKs:

| Name | Description |
|---------|---------|
| AVSDK | Used to realize core audio/video communication capabilities.  |
| IMSDK | Used to realize capabilities used in audio/video communication such as third-party account system access, account login authentication and so on. It's also integrated with crash reporting module.  |

**Note:** There are certain dependencies between the Frameworks for both SDKs when compiling (the files call each other during operations). Thus App developers must make sure that all Frameworks listed below are complete when updating and replacing SDKs. Replacing only some of the Frameworks may introduce exceptions.

For more information about IMSDK, please see the link below:
> http://cloud.tencent.com/product/im.html

## SDK File List
### 1. AVSDK file list
| Serial Number | Name | Description |
|---------|---------|---------|
| 1 | AVFoundationEx.framework | AVFoundation Extension Package. |
| 2 | QAVSDK .framework | Audio/Video Core Feature Pack. |
**Note:** App developers must make sure that all Frameworks mentioned above are complete when updating and replacing SDKs. Replacing only some of the Frameworks may introduce exceptions.
### 2. IMSDK file list
| Serial Number | Name | Description |
|---------|---------|---------|
| 1 | Analytics.framework | Lighthouse Statistics SDK. |
| 2 | IMCore.framework | IMSDK Internal Core Package. |
| 3 | ImSDK.framework | Instant Messaging SDK (Encapsulating IMCore). |
| 4 | IMSDKBugly.framework | Bugly Report. |
| 5 | QALSDK.framework |  Networking layer SDK, which implements the secure connection channel between the app and the background. |
| 6  | TLSSDK.framework | Tencent Cloud TLS Login Package. |
**Note:** App developers must make sure that all Frameworks mentioned above are complete when updating and replacing SDKs. Replacing only some of the Frameworks may introduce exceptions.
