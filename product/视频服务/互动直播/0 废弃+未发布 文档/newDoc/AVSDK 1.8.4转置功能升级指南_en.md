## Guide for Upgrading Rotation Feature of AVSDK 1.8.4

### Glossary

* Rotation: the process in which an terminal App rotates captured video content based on the gyroscope sensor's feedback to keep the video upright.

### Background

Because video capture devices and playback devices have independent rotation angles, often what the users see on these two types of devices are different. This seemingly simple problem becomes extraordinary tricky after taking factors such as front/back camera switching, cropping and resizing, recording and difference in playback requirements into consideration.

To solve this problem, AVSDK has gradually improved the handling of rotation in video capture and playback since version 1.8.2. As of version 1.8.4, a complete solution is provided.

This document is intended to provide developers with solutions to compatibility issues when upgrading AVSDK to version 1.8.4.

##### If you are currently using iLive SDK, you can ignore the problem.

## Potential Compatibility Issues about Rotation After Upgrading to AVSDK 1.8.4

When using previous versions of AVSDKs without enabling client rotation to view videos captured by AVSDK 1.8.4 with client rotation enabled, the video may appear to be resized or rotated.


## How to Solve the Problem

### Upgrade from Versions Lower than 1.8.1 (including 1.8.1)

It's recommended to upgrade to 1.8.2 before upgrading to 1.8.4, instead of upgrading to 1.8.4 directly. The steps are as follows:

1. Upgrade AVSDK to 1.8.2, and disable rotation. (on iOS, set autoRotateVideo of QAVMultiParam to NO; on Android, set AVRoomMulti.EnterParam.Builder.isDegreeFixed to false)
2. Refer to the upgrade guide of iOS OpenGL rendering code in appendix.
3. Perform joint debugging the new App with previously released Apps that use AVSDK 1.8.1. Debug rendering logic and fix compatibility issues between iOS and Android.
4. After the App that uses AVSDK 1.8.2 has become mainstream, upgrade to AVSDK 1.8.4.
5. Submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB) in Tencent Cloud's console, choose `Other Problems` for problem type, and in problem description, write `Application for adding rotation whitelist-company name-Tencent Cloud account (XXXXXXX)-sdkappid to apply whitelist (XXXXXXX)`.
6. After the ticket has been handled, upgrade to AVSDK 1.8.4 and fix compatibility issues between iOS and Android, and run compatibility tests with previously released versions.
7. After the App that uses AVSDK 1.8.4 has become mainstream, submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB), choose `Other Problems` for problem type, and write in problem description, write `Application for removing rotation whitelist-company name-Tencent Cloud account (XXXXXXX)-sdkappid to remove whitelist status (XXXXXXX)`；



### Upgrade from Version 1.8.2

If rotation is disabled on clients (on iOS, autoRotateVideo of QAVMultiParam is set to NO; on Android, AVRoomMulti.EnterParam.Builder.isDegreeFixed is set to false), follow these steps:

1. Submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB) in Tencent Cloud's console, choose `Other Problems` for problem type, and in problem description, write `Application for adding rotation whitelist-company name-Tencent Cloud account (XXXXXXX)-sdkappid to apply whitelist (XXXXXXX)`.
2. After the ticket has been handled, upgrade to AVSDK 1.8.4, and refer to the upgrade guide of iOS OpenGL rendering code in appendix.
3. Fix compatibility issues between iOS and Android, and run compatibility tests with previously released versions.
5. After the App that uses AVSDK 1.8.4 has become mainstream, submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB), choose `Other Problems` for problem type, and write in problem description, write `Application for removing rotation whitelist-company name-Tencent Cloud account (XXXXXXX)-sdkappid to remove whitelist status (XXXXXXX)`；


Otherwise:

1. Upgrade to AVSDK 1.8.4, and refer to the upgrade guide of iOS OpenGL rendering code in appendix.
2. After the App that uses AVSDK 1.8.4 has become mainstream, submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB), choose `Other Problems` for problem type, and write in problem description, write `Application for removing rotation whitelist-company name-Tencent Cloud account (XXXXXXX)-sdkappid to remove whitelist status (XXXXXXX)`；

### Upgrade from Version 1.8.3

1. Submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB) in Tencent Cloud's console, choose `Other Problems` for problem type, and in problem description, write `Query about rotation whitelist-company name-Tencent Cloud account (XXXXXXX)-sdkappid to apply whitelist (XXXXXXX)`.
2. After the ticket has been replied,

**If rotation is enabled**

* Upgrade to AVSDK 1.8.4, and refer to the upgrade guide of iOS OpenGL rendering code in appendix.
* Ensure compatibility between iOS and Android, and run compatibility tests with previously released versions.
* After the tests, release the new version of App that uses AVSDK 1.8.4.

**If rotation is disabled**

* Ensure compatibility between iOS and Android, and run compatibility tests with previously released versions.
* After the tests, release the new version of App that uses AVSDK 1.8.4.
* After the App that uses AVSDK 1.8.4 has become mainstream, submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=37&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD%20%20ILVB), choose `Other Problems` for problem type, and write in problem description, write `Application for removing rotation whitelist-company name-Tencent Cloud account (XXXXXXX)-sdkappid to remove whitelist status (XXXXXXX)`;

### Custom Capture and Rendering

Common pitfalls in custom capture:

* When fillExternalCaptureFrame is called on iOS, the SDK's low-level components would automatically adjust the rotation.
* On Android, the rotation value needs to be provided manually. (For specific options, please refer to [Setting Rotation](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E8%A7%86%E9%A2%91%E6%9C%8D%E5%8A%A1/%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD/newDoc/%E8%A7%92%E5%BA%A6%E6%96%B9%E6%A1%88.md)). ** To ensure that the SDK correctly rotates screens across devices, Android clients need to set appropriate values based on [Setting Rotation](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E8%A7%86%E9%A2%91%E6%9C%8D%E5%8A%A1/%E4%BA%92%E5%8A%A8%E7%9B%B4%E6%92%AD/newDoc/%E8%A7%92%E5%BA%A6%E6%96%B9%E6%A1%88.md).
* When rotation is disabled, the viewers receive the same rotation value passed to fillExternalCaptureFrame.
* When rotation is enabled, the SDK would rotate the video and set rotation value to 0 after the VJ host calls fillExternalCaptureFrame, and then upload video data. Therefore the clients would always receive 0, and need to determine by resolution that if the video is in landscape mode. 

Common pitfalls in custom rendering:

* Because all previous video data have rotation values attached, applications determine video orientations mainly by rotation values.
* In AVSDK 1.8.4, before rotation is enabled, the rotation value is always 0. Therefore, the clients need to determine the orientation of the video by resolution: `width > height for landscape mode`, `width < height` for portrait mode. Developers need to add code that checks the orientation of the video in the rendering logics adapted previously.

**If only custom capture is implemented and custom rendering is not, the rendering code can still be upgraded as it's explained in the upgrade guide of iOS OpenGL rendering code in appendix.**

After the above two parts are correctly modified, run compatibility tests with old versions and release a new version of App.


## Appendix: OpenGL Code Upgrade Guide

1. Upgrade [FreeShow](https://github.com/zhaoyang21cn/iOS_Suixinbo)'s code.
2. Refer to FreeShow's OpenGL code, and replace the following contents:
	
	![](https://mc.qcloudimg.com/static/img/94f24136772e38c77fe40a1968163539/mergeopengl.png)
	
3. If you are using a modified version of rendering code, refer to the substitution in step 2 and change it accordingly based on your needs (the core logics are in TCAVFrameDispatcher and AVGLCustomRenderView).
