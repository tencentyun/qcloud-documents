<!-- ## Overview

With the increasing demand for individualization of end users, simple text interaction can no longer satisfy users' needs for sharing contents. Tencent Cloud VOD allows users to directly upload video files stored in clients to the cloud, while supporting seamless integration with other features of VOD, including transcoding, screencapping and hotlink protection.

## Upload Process

![](//mc.qcloudimg.com/static/img/1cb47b70ba7ab12ddf161f9576ca6849/image.png)

The figure above shows the process of uploading videos from client, which involves four elements: client, App server, Tencent Cloud VOD and Tencent Cloud COS. The steps shown in the figure are described as follows:

### Step 1: Client obtains signature from App server

Before video files are uploaded to Tencent Cloud from the client, VOD needs to verity if the upload from client has been authorized by App server. Therefore, client needs to obtain the upload signature from the App server first, and then transfers it to VOD when requesting for upload information. VOD allows the upload from client only if it verifies that the signature is valid.

For more information on how App server generates signatures, please see [Upload Signature of Client](/document/product/266/9221).

***Note***: ***DO NOT*** disclose API keys (Secret ID and Secret Key) to the client. Any disclosure of the keys can cause serious security issues. API keys should be kept by App server only.

### Step 2: Client initiates upload to VOD

Before uploading files to COS, the client needs to acquire the information such as the target COS Bucket and path. The client initiates an upload to VOD and acquires information necessary to upload files to COS. VOD distributes upload information to the client after it has verified the validity of the signature.

When the client requests upload information, it can choose to upload video only (only request for upload information of video file) or upload both video and cover (request upload information for both video file and cover file).

### Step 3: Client uploads files to COS

The client calls the COS API for upload to upload the files based on the upload information acquired when initiating the upload.

### Step 4: Client confirms upload with VOD

After the client uploads files to COS successfully, it needs to initiate a confirmation request to VOD. Upon receiving the request for confirming upload, VOD returns video information such as fileId, playback address, and cover image address (if any) and processes the videos as required by user including transcoding, applying watermarks, and capturing screenshots.

## Upload Method

### SDK

Tencent Cloud VOD provides SDKs for various platforms to make it easier for users to develop client upload features:

* [Android SDK](/document/product/266/9237)
* [iOS SDK](/document/product/266/9238)
* [Web SDK](/document/product/266/9239)

The SDKs encapsulate elements of interactions between clients and VOD/COS. You can complete Step 2 through Step 4 of the upload process by simply calling a single API in the SDK. Therefore, it is ***highly recommended*** to integrate the SDK provided by VOD into your App to achieve upload from client.



<!-- 
## Upload Videos from Client

Uploading videos from client means the **end user** of App uploads local videos in the App to the VOD platform. Unlike upload from server, upload from client is generally performed by the end user of App. The App **should not** and **must not** expose the API keys (SecretId and SecretKey) to the client.

The process of upload from client is shown as below. Steps 1 and 2 are initiated by the App server, while Steps 3, 4 and 5 by the VOD backend.

![Flow Chart](//mc.qcloudimg.com/static/img/434ab4671cfee79a7556ebcc0abdf49c/image.jpg)

### Obtain signature

See the Step 1 in the flow chart for uploading videos from client
The VOD server needs to verify all video upload requests, but the App should not expose the API keys to the client. Therefore, the client needs to apply for an upload signature to the App backend before initiating the video upload. In addition to using the signature as authentication credential, you can also set other information such as video attributes and processing method of uploaded videos in the signature.

For more information, please see [Upload Signature of Client](/document/product/266/9221).

### Upload videos using SDK

See the Step 2 in the flow chart for uploading videos from client.
VOD provides SDKs for uploading videos on iOS/Android/Web platforms.

1. [iOS SDK](/document/product/266/7836);
2. [Android SDK](/document/product/266/7837);
3. [Web SDK](/document/product/266/7938).

## Video Upload Event Notification

See the Step 3 in the flow chart for uploading videos from client.
After the video is uploaded successfully, VOD initiates an event notification if the App has been configured with video upload completion notification.
For more information, please see [Event Notification - Video Upload Completed](/document/product/266/7830).

## Security

### One-off signature

When the client requests an upload with an upload signature obtained from the signature distribution server, the VOD backend verifies the validity of the signature and records that the signature has been used. When the client requests another upload, it needs to obtain upload signature again from the signature distribution server. This can prevent the client from uploading videos repeatedly with a single signature.

### Size limit of files to be uploaded
Not available. -->



Uploading videos from client means the **end user** of App uploads local videos to the VOD platform. The process of uploading videos from client is shown as below.
![Flow Chart of Uploading Videos from Client](//mc.qcloudimg.com/static/img/3ae581b8979639214fa9f355d03e940b/image.png)


## Preparations

### Activate service
Activate the VOD service first, if you have not activated it yet. For more information, please see [Purchase Process](/document/product/266/2839).

### Obtain cloud API keys
When client requests an upload signature, Tencent Cloud keys (SecretId and SecretKey) are needed.

The steps are as follows:
Step1: Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).
Step2: Click "Cloud Products", and select "Cloud API Keys" under "Monitor & Management" to access the Cloud API key management page, as shown below:
![Cloud API Keys](//mccdn.qcloud.com/img568f5fb824757.png)
Step3: Obtain the cloud API keys as shown below. If you have not created the keys, click "New" to create a pair of SecretId/SecretKey.
![SecretID and SecretKey](//mc.qcloudimg.com/static/img/23f95aaa97adf3eeae3bf90470fe5122/image.png)

## Set Up Signature Distribution Service

The client uploads video files directly to the Tencent Cloud VOD without going through App server. Therefore, Tencent Cloud VOD needs to authenticate the client that initiates the request. SecretKey carries a very high permission, so the App must not expose the SecretKey to the client to avoid serious security issues.
The client must apply for an upload signature from the App's signature distribution service before initiating an upload, as shown in the Step 1 in the flow chart. This step can be performed via any secure tunnel between the App's client and server.
For more information on how App server generates upload signatures, please see [Upload Signature of Client](/document/product/266/9221).

For the sample code for generation of signatures in different languages, please see:

- [Example of PHP Signature Generation](/document/product/266/10638#php-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B);
- [Example of Java Signature Generation](/document/product/266/10638#java-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B);
- [Example of Node.js Signature Generation](/document/product/266/10638#node.js-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B);
- [Example of C# Signature Generation](/document/product/266/10638#c.23-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B).

After the service is set up, developers can verify the validity of signature using the tool provided by Tencent Cloud VOD:

- [Signature Generation Tool](https://video.qcloud.com/signature/ugcgenerate.html): Generate signatures quickly based on parameters and keys;
- [Signature Verification Tool](https://video.qcloud.com/signature/ugcdecode.html): Parse the signature to obtain parameters required to generate the signature.

## Client Integration
For upload scenario, VOD provides SDKs for Android, iOS and Web platforms to make it easier for customers to access the feature. See:
- [SDK for Upload on Android](/document/product/266/9539);
- [SDK for Upload on iOS](/document/product/266/13793);
- [SDK for Upload on Web](/document/product/266/9239).


## Event Notification

After a video file is uploaded successfully, Tencent Cloud VOD initiates an [Event Notification - Video Upload Completed](/document/product/266/7830) to the App backend as shown in Step 3 in the flow chart, and App backend becomes aware of the upload based on the notification.
To allow your App to receive event notifications, you need to activate event notifications for the App on VOD console. For more information, please see [Callback Configuration](/document/product/266/14058#.E5.9B.9E.E8.B0.83.E9.85.8D.E7.BD.AE)
 [Event Notification - Video Upload Completed](/document/product/266/7830) contains the following information:

- FileId and URL of new video file;
- VOD supports specifying custom transparently transmitted information for uploading videos. VOD sends the transparently transmitted information to the App backed upon completion of upload. Specifically, the event notification contains two fields: `SourceType` and `SourceCopntext`. `SourceType` is specified as `ClientUpload` by Tencent Cloud, which indicates the upload source is always client. `SourceContext` is a user-defined transparently transmitted field, and is specified by the App backend when the backend distributes upload signature to client. It corresponds to the parameter `sourceContext` in [Upload Signature of Client](/document/product/266/9221), and is transmitted back transparently in the callback of upload event.
- VOD supports processing videos automatically when the videos are uploaded successfully. If you have specified [Video Processing Task Flow](/document/product/266/11700) for the upload, the event notification contains the task ID (field `data.procedureTaskId` in the event notification).

For more information, please see:
- [Task Management and Event Notification](/document/product/266/7829);
-  [Event Notification - Video Upload Completed](/document/product/266/7830).

## Advanced Features

### Specify the processing method for uploaded videos
In VOD, the video processing mentioned above is based on [Video Processing Task Flow](/document/product/266/11700). If the App needs to process the uploaded video automatically (such as transcoding and screencapping), you can specify the video processing method using the parameter `procedure` in [Upload Signature of Client](/document/product/266/9221).

**Example 1:**Transcode the video as configured in "Global Settings" -> "Transcode Settings" in console after upload is completed, and apply the default watermark in the "Watermark Management": Specify the value of `procedure` as follows:

<pre>
QCVB_SimpleProcessFile(1, 1)
</pre>

**Example 2:**Use the transcoding templates 10 and 20 for transcoding; use the watermark template 150 to set watermarks in transcoding process; use the screenshot template 10 to capture the first frame as cover; and use the sampling screenshot template 10 for sampling screenshots: Specify the value of `procedure` as follows:

<pre>
QCVB_SimpleProcessFile({10, 20}, 150, 10, 10)
</pre>

Parameter `procedure` can also be set to other task flows built in VOD, or task flows defined by App.

For more information, please see:

 - [Parameter Templates and Task Flows](/document/product/266/11700);
- VOD built-in task flow [QCVB_SimpleProcessFile](/document/product/266/11700#qcvb_simpleprocessfile).

### Upload cover along with video
VOD allows uploading cover along with video by entering the cover path in the upload SDK API. See:
- [SDK for Upload on Android](/document/product/266/9539);
- [SDK for Upload on iOS](/document/product/266/13793);
- [SDK for Upload on Web](/document/product/266/9239).


### One-off signature

In the process of video upload, the signature distributed by App backend can be used for many times within the valid period by default. If the App has a high requirement for the security of video upload, you can specify one-off signature that is only valid for once. This means the signature can only be used once. Please note that although this signature method is more secure, it requires additional actions of App in case of an exception. For example, in case of an upload error, in addition to retrying the Step 2 "Upload videos using SDK" in the flow chart, you need to perform Step 1 again. This means the App backend server needs to redistribute the signature. You can use one-off signature by specifying parameter `oneTimeValid` as 1 when the App backend distributes signature. See:
- [Upload Signature of Client](/document/product/266/9221)

### Resume upload from breakpoint
VOD supports resuming upload from breakpoint. When an upload is interrupted unexpectedly, you can upload the file again from the point where the upload is interrupted to avoid repeated upload. The validity period for resuming upload from breakpoint is one day. If an interrupted upload is resumed within one day after the interruption, it is resumed from the breakpoint. If it is resumed after one day, the video is uploaded from scratch by default. To use this feature, you simply need to specify the enabling of this feature as follows:
- [SDK for Upload on Android](/document/product/266/9539): Set `enableResume` to True;
- [SDK for Upload on iOS](/document/product/266/13793). Set `enableResume` to True;
- [SDK for Upload on Web](/document/product/266/9239). Resuming upload from breakpoint is a built-in feature. No operation is required.


### Pause/resume/cancel upload
VOD SDK allows pausing, resuming, canceling an upload in progress. See:
- [SDK for Upload on Android](/document/product/266/9539);
- [SDK for Upload on iOS](/document/product/266/13793);
- [SDK for Upload on Web](/document/product/266/9239).

## FAQ

### How to initiate transcoding automatically after a video is uploaded?
You can specify the processing method for uploaded videos using the parameter `procedure` in the upload signature of client. For more information, please see [Specify processing method for uploaded videos](#.E4.B8.8A.E4.BC.A0.E6.97.B6.E6.8C.87.E5.AE.9A.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E6.96.B9.E5.BC.8F).

### How does App backend identify which client uploaded the video when it receives video upload completion notification?
Add 'sourceContext` parameter in the upload signature of client to indicate the user identity information. The parameter is sent to the App backend with the upload completion notification. For more information, please see [Event Notification](#.E4.BA.8B.E4.BB.B6.E9.80.9A.E7.9F.A5).

