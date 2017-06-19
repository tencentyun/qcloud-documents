## Release Notes
- Version number: 2.0.3.3039 @ 2017-05-27
- iOS & Android: Optimized audio and video kernels to improve image quality and definition.
- iOS: Optimized exposure mechanism to address overexposure problems. Exposure will look more natural.
- Android: Added UGC cropping/stitching features.
- Android: Optimized player and render views. Animation, floating window and big/small screen switching features become supported.
- Android: Added "Auto" option for software/hardware encoding. The SDK will automatically choose hardware or software encoding based on mobile phone performance.
- iOS & Android: Added [Dynamic] option to setVideoQuality for scenarios with great network condition variances, such as overseas broadcasting.
- iOS & Android: Optimized directory and code structure for Demos, reducing interfacing cost. Added simple-to-use Demos for short video recording, cropping, stitching and joint broadcasting.
- See [Update History](https://www.qcloud.com/document/product/454/7878) for features in previous versions.


## Future Releases
- Version 2.0.4 is expected to be released by the beginning of June
- Filter editing is expected to be added, which is used to create filter effects for local video files.
- Speed editing is expected to be added, which is used to increase the speed of local videos to 2x, 4x or other speed.
- Sound track editing is expected to be added, which is used to replace and edit the sound tracks of local videos.

## Document Index

| Mobile Phone Platform | Document Index |
|:-------:|---------|
| iOS Platform | [Push Feature](https://www.qcloud.com/document/product/454/7879) &nbsp; [Playback Feature](https://www.qcloud.com/document/product/454/7880) &nbsp; [Joint Broadcasting](https://www.qcloud.com/document/product/454/8090) &nbsp; [Advanced Usage](https://www.qcloud.com/document/product/454/7884) &nbsp; [ReplayKit](https://www.qcloud.com/document/product/454/7883)  | 
| Android Platform | [Push Feature](https://www.qcloud.com/document/product/454/7885) &nbsp; [Playback Feature](https://www.qcloud.com/document/product/454/7886) &nbsp; [Joint Broadcasting](https://www.qcloud.com/document/product/454/8091) &nbsp; [Advanced Usage](https://www.qcloud.com/document/product/454/7890) &nbsp; [Phone Screencap](https://www.qcloud.com/document/product/454/7889) | 

## Test Result
- Kernel test cases: Total number of cases - 56, number of passed cases - 56, number of failed cases - 0
- System test cases: Total number of cases - 307, number of passed cases - 307, number of failed cases - 0
- Full-function test cases: Total number of cases - 718, number of passed cases - 697, number of failed cases - 21 

## Download Links
<style>
table th:nth-of-type(1) {  width:  150px; }
table th:nth-of-type(2) {  width:  550px; }
table th:nth-of-type(3) {  width:  100px; }
</style>

- **iOS Platform (2.0.3.3039)**

| Type | Description | Download Link |
| :---------: |  ---- | :----: | 
| Full Version  |  Includes all features such as stream push, LVB, VOD, joint broadcasting, screencap and so on.  | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOS2.0.3.3039.zip)  |
| Simplified Version  |  Removed non-core features based on the full version, with an increase of 900 KB in code volume. Player has lower compatibility compared to full version; does not support iOS 7.0; backend pause image push is not supported for iOS 10 or below.  | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSSimple2.0.3.3039.zip)  |
| rename version  |  Renamed symbols for open source components such as ffmpeg, based on the full version. Use this version if symbol conflict occurs due to ffmpeg in your project, or if crush occurs in the internal functions of ffmpeg.  | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSRename2.0.3.3039.zip) |

- **Android Platform (2.0.3.3039)**

| Type | Description | Download Link |
| :---------: |  ---- | :----: | 
| Full Version  | Includes all features such as stream push, LVB, VOD, joint broadcasting, screencap and so on.  | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroid2.0.3.3039.zip)  |
| Simplified version  | Removed joint broadcasting feature based on the full version, suitable to be used together with ILVB iLiveSDK.  | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple2.0.3.3039.zip)  |

- **Commercial Version (2.0.3.3039)**

| OS | Version Description | Download Link |
| :---------: |  ---- | :----: | 
| iOS Platform  | Implemented special effects such as eye enlarging, face slimming, motion effect sticker and green screen based on patented AI technologies developed by YouTu Lab. For instructions, see [Special Effects](https://www.qcloud.com/document/product/454/9018).  | [ZIP](http://downloadfix-1252463788.cosgz.myqcloud.com/RTMPSDKIOSPitu.zip) |
| Android Platform  | Implemented special effects such as eye enlarging, face slimming, motion effect sticker and green screen based on patented AI technologies developed by YouTu Lab. For instructions, see [Special Effects](https://www.qcloud.com/document/product/454/9018).  | [ZIP](http://downloadfix-1252463788.cosgz.myqcloud.com/RTMPSDKAndroidPitu.zip) |

## Contact Us
We have a professional testing team to perform tests and verifications for every version to ensure the usability and stability of basic features. If you encounter any technical issues during interfacing process, feel free to [Contact Us](https://www.qcloud.com/document/product/454/7998).


