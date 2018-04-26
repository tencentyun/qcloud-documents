## Overview
Short video industry grows very rapidly and has become a new trend following LVB. To help developers quickly create and release short video applications, Tencent Cloud VOD launched a **one-stop short video solution** that covers video generation, upload, processing, distribution, playback and other processes.

### VOD Activation and Billing
Before using the short video solution, you need to activate **Tencent Cloud VOD**. For more information, please see:

* [VOD Overview](https://cloud.tencent.com/document/product/266/2833)
* [VOD Prices](https://cloud.tencent.com/document/product/266/2838)
* [VOD Purchase Process](https://cloud.tencent.com/document/product/266/2839)

### Module Diagram of the Solution
The following figure illustrates the functional modules involved in this document:

![](https://mc.qcloudimg.com/static/img/984742edd098b6d0e2eeb1c265d0a01a/image.jpg)

## Short Video Generation
### Short Video SDK Overview
In UGC short video scenario, the video content is generally collected and edited on the mobile terminal. Tencent Cloud provides a **short video SDK** for developers to quickly realize capturing, clipping, remixing, sound effects, subtitle, sticker and other features in their applications, as well as experience Demos for Android and iOS. For more information, please see:

* [Feature List](https://cloud.tencent.com/document/product/584/9457)
* [Demo](https://cloud.tencent.com/document/product/584/9365)

### Activation and Billing
Short video SDK is not included in the VOD service, and needs **to be activated and billed separately**. For more information, please see:

* [Price Overview](https://cloud.tencent.com/document/product/584/9368)
* [Purchase Process](https://cloud.tencent.com/document/product/584/9678)

### How to Use Short Video SDK
Short video SDK is supported on Android and iOS platforms. For more information, please see:

* [Short Video SDK for Android](https://cloud.tencent.com/document/product/584/11631)
* [Short Video SDK for iOS](https://cloud.tencent.com/document/product/584/11638) 

## Short Video Upload
### Overview of Uploading from Client
After finishing the short video production in the mobile terminal, you can upload it directly to the VOD storage for subsequent video processing and distribution via **Upload from VOD Client**. VOD service provides the client upload SDK to simplify developers' tasks and relevant Demo for reference. For more information, please see:

* [How to Upload from Client](https://cloud.tencent.com/document/product/266/9219)
* [Upload Signature of Client](https://cloud.tencent.com/document/product/266/9221)

### Activation and Billing
Developers can use the client upload feature and relevant SDK by activating the VOD service. The space occupied by the uploaded video files will be billed. For more information, please see:

* [VOD Storage Billing](https://cloud.tencent.com/document/product/266/2838#.E8.A7.86.E9.A2.91.E5.AD.98.E5.82.A8).

### How to Use Client Upload SDK
The upload SDK of VOD client is supported on Android, iOS and Web platforms. For related documentation and reference Demo, please see:

* [Upload SDK for Android](https://cloud.tencent.com/document/product/266/9539)
* [Upload SDK for iOS](https://cloud.tencent.com/document/product/266/13793)
* [Upload SDK for Web](https://cloud.tencent.com/document/product/266/9239)

## Porn Detection
In UGC short video scenario, the video uploaded by users is unpredictable and may contain non-compliant content which will lead to negative impact on developers. So developers often need to review the uploaded video and process and distribute it only after it is confirmed to be compliant. Tencent Cloud VOD service provides developers with the AI porn detection capability for efficient and reliable porn detection.

### Activation and Billing
Developers can use the AI porn detection feature (free for now) by activating the VOD service.

### How to Use AI Porn Detection
The Cloud VOD task flow `QCVB_ProcessUGCFile` developed specifically for UGC short video scenarios integrates the AI porn detection feature. For more information, please see:

* [How to Use AI Porn Detection](https://cloud.tencent.com/document/product/266/11701#.E4.BD.BF.E7.94.A8-ai-.E9.89.B4.E9.BB.84)

### Manual Review
It is subjective to some degree to determine whether a video is non-compliant, so the judgment of AI porn detection may not completely meet the requirements of developers. Developers can manually review the video judged as porn content, and process and distribute it as normal if it is confirmed to be compliant. For more information on manual review, please see:

* [Manual Review](https://cloud.tencent.com/document/product/266/11701#ai-.E9.89.B4.E9.BB.84.E9.85.8D.E5.90.88.E4.BA.BA.E5.B7.A5.E5.AE.A1.E6.A0.B8)

## Short Video Transcoding
### Short Video Transcoding Overview
UGC short videos uploaded by end users often carry inappropriate parameters (such as high bitrate), have no cover, or do not conform to the requirements in other ways. To ensure better viewing experience, developers transcode the video to a format suitable for playback on various devices, and then distribute the video. Cloud VOD service provides the perfect transcoding capability, and supports a variety of video output specifications as well as watermark, screenshot, cover setting and other features. For more information, please see:

* [Video Transcoding Overview](https://cloud.tencent.com/document/product/266/11701)

### Activation and Billing
Developers can use video transcoding feature by activating the VOD service. The transcoding feature is billed by the output specifications and duration. The storage space occupied by the transcoded files will also be billed. For more information, please see:

* [Video Transcoding Billing](https://cloud.tencent.com/document/product/266/2838#.E8.A7.86.E9.A2.91.E8.BD.AC.E7.A0.81)
* [Video Storage Billing](https://cloud.tencent.com/document/product/266/2838#.E8.A7.86.E9.A2.91.E5.AD.98.E5.82.A8)

### How to Use Transcoding
#### Task Flow and Event Notification
To make it easy for developers to conduct video processing all at once rather than step by step, Cloud VOD service puts forward the concept of **task flow** that integrates transcoding, watermarking, screenshot, cover setting and other operations. This feature is based on the VOD **video processing task flow** mechanism and **event notification** mechanism. For more information, please see:

* [Parameter Template and Task Flow](https://cloud.tencent.com/document/product/266/11700)
* [Event Notification Overview](https://cloud.tencent.com/document/product/266/7829#.E4.BA.8B.E4.BB.B6.E9.80.9A.E7.9F.A5.E7.AE.80.E4.BB.8B)
* [Task Flow Status Change](https://cloud.tencent.com/document/product/266/9636)

#### Preset Task Flow for Short Video Scenarios
For UGC short video scenarios, Cloud VOD service specially provides a task flow `QCVB_ProcessUGCFile` for developers to streamline video processing business logic. For more information, please see:

* [QCVB_ProcessUGCFile Task Flow](https://cloud.tencent.com/document/product/266/11700#qcvb_processugcfile)

#### Triggering Task Flows Automatically

* [Uploading specific task flows from Client](https://cloud.tencent.com/document/product/266/9219#.E4.B8.8A.E4.BC.A0.E6.97.B6.E6.8C.87.E5.AE.9A.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E6.96.B9.E5.BC.8F)

#### Triggering Task Flows on Request
In addition to triggering task flows automatically, Developers can also initiate a task flow request using the server API. In this mode, developers need to use the unique identifier `FileId` to specify which video to process. `FileId` can be acquired from the event notification for uploaded videos. For more information, please see:

* [Event Notification for Uploaded Videos](https://cloud.tencent.com/document/product/266/7830)

For more information on how to use the server API to initiate the task flow for a video with specified `FileId`, please see:

* [Server API Overview](https://cloud.tencent.com/document/product/266/10688)
* [Processing Video Using Task Flows](https://cloud.tencent.com/document/product/266/11030)

Except the triggering mode, the task flow parameter format and event notification are the same as those of automatic transcoding.

## Video Distribution and Playback
#### Video Distribution
After the video processing task flow `QCVB_ProcessUGCFile` is completed, developers can obtain the transcoded video's URL and the cover's URL from the task flow event notification, and publish them in the short video application. For more information, please see:

* [Task Flow Status Change](https://cloud.tencent.com/document/product/266/9636)

### Video Playback
Cloud VOD provides player SDKs for Android, iOS and Web platforms. For more information, please see:

* [VOD Player Overview](https://cloud.tencent.com/document/product/266/7836)
* [VOD Player SDK and Demo for Android](https://cloud.tencent.com/document/product/266/7938)
* [VOD Player SDK and Demo for iOS](https://cloud.tencent.com/document/product/266/9237)
* [VOD Player SDK Download](https://cloud.tencent.com/document/product/266/5236)



