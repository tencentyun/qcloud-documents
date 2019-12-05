<!-- ## Overview

Apps collect a large number of excellent videos from various channels and may store these video resources directly in their servers. Next, the Apps will plan to further process the videos (such as transcoding, taking screenshots, applying watermarks and so on) and publish them into the Content Delivery Network (CDN), so that users can watch the videos and create profit for Apps. Tencent Cloud VOD allows users to upload video files stored in servers directly onto the cloud, while providing seamless integration with the video processing features of VOD service, including transcoding, screenshot, hotlink protection and so on.

## Upload Process

![Image](//mc.qcloudimg.com/static/img/d751bf5e65346dee3a698f097ac2bfdd/image.png)

The figure above shows the process of uploading videos from server, which involves three elements: App backend, Tencent Cloud VOD and Tencent Cloud COS. The steps shown in the figure are described as follows:

### Step 1: App Backend Initiates Upload Operation to VOD

Before uploading files to COS, the APP server needs to acquire the information such as the target COS Bucket and path. The server initiates an upload to VOD and acquires information necessary to upload files to COS. VOD distributes upload information to the server after it has verified the request from the server.

When the server requests for upload information, it can choose to upload the video only (only request for upload information of the video file) or upload both video and cover image (request upload information for both the video file and cover image file).

### Step 2: App Backend Uploads File to COS

The App backend calls the COS uploading API to upload files based on the upload information acquired when initiating the upload operation.

### Step 3: App Backend Confirms Upload Process with VOD

After the App backend uploads files to COS successfully, it needs to initiate a confirmation request to VOD. Upon receiving the request for confirming upload, VOD returns video information such as fileId, playback address, and cover image address (if any) and processes the videos as required by user including transcoding, applying watermarks, and capturing screenshots.

## Upload Method

### API

* [API for App Backend to Initiate Upload Operation to VOD](/document/product/266/9756)
* [API for App Backend to Upload Files to COS](/document/product/266/9758)
* [API for App Backend to Confirm Upload Process with VOD](/document/product/266/9757)

### SDK

Cloud VOD service provides SDKs of different language platforms to make it easier for users to develop their client upload features:

* [PHP SDK](/document/product/266/9725)
* [Java SDK](/document/product/266/10276)

Based on Cloud Image APIs and COS, the SDKs encapsulate elements of interactions between servers and VOD/COS. You can complete Step 1 through Step 3 of the upload process by simply calling a single API in the SDK. Therefore, it is ***highly recommended*** to reference the SDK provided by VOD into your App to achieve upload from server.

<!-- 
## Upload Videos from Server
Uploading videos from sever means that the App's **Backend Operators" upload the videos in local server to the VOD platform. Compared to uploading from client, it is typically performed by App internal personnel, so the API key (SecretId and SecretKey) can be used directly.

The process of upload from sever is shown as below. Steps 1, 2 and 3 are initiated by the App server, while Steps 4, 5 and 6 by the VOD backend.

## Video Upload

The video upload is divided into [Upload Application](/document/product/266/9756), [Upload Files](/document/product/266/9758), and [Upload Confirmation](/document/product/266/9757), which respectively correspond to step 1, 2, and 3 in the chart above.

![Flow Chart](//mc.qcloudimg.com/static/img/965ca99592cdd4567a953638e3f14f9f/image.jpg)

Cloud VOD service provides DEMOs based on SDKs of different language platforms to make it easier for users to develop their client upload features.

* [PHP SDK](/document/product/266/9725)
* [Java SDK](/document/product/266/10276)

**Notes:**
> The video uploading process is so complicated that it is strongly recommended that the developer use the video upload SDK provided by VOD for uploading.

### Upload Application

See the Step 1 in the flow chart for uploading from server.

The main purpose of the upload application is:
1. Obtain the storage information of video file;
2. If you need to upload a local image as the cover, this API also returns the storage information of the video cover;
3. Specify the processing method after the video is uploaded.

For more information, please see:
Server API: [Upload Application](/document/product/266/9756).

### Uploading Files

See the Step 2 in the flow chart for uploading from server.

Uploading files is to upload the local video files to the VOD storage service. The upload APIs of VOD are the same as those of the Tencent Cloud Object Storage Service (COS), so you need to use the same APIs or SDKs as those of COS for uploading.

For more information, please see:
[File Upload](/doc/product/266/9758).

### Confirming Uploads

See the Step 3 in the flow chart for uploading from server.

Upload confirmation is mainly to inform the VOD system that the file has been uploaded, and then the VOD system can correctly update the media information and process the corresponding video based on the parameters specified in upload application.

If the calling is successful, the API returns:
1. Video FileID;
2. Video file URL;
3. Video cover URL (if the cover is specified in the upload application);
4. Video processing task ID (if the video processing method is specified in the upload application, namely the parameter "procedure").

For more information, please see:
Server API: [Upload Confirmation](/document/product/266/9757).

## Video Upload Event Notification

See the Step 4 in the flow chart for uploading from server.

If the video upload completion notification is configured on the console, VOD will initiate an event notification using the specified method after the App backend confirms that the upload is successful.

For more information, please see [Event Notification - Video Upload Completed](/document/product/266/7830). -->


Uploading videos from sever means the **backend** of App uploads videos to the VOD platform. The process of uploading videos from sever is shown as below.

![Chart of Uploading Videos from Server](//mc.qcloudimg.com/static/img/be38e6902ce7c2d1654c2dea70881d94/image.png)


## Preparations

### Activating Service
Activate the VOD service first, if you have not activated it yet. For more information, please see [Purchase Process](/document/product/266/2839).

### Obtaining cloud API keys
Uploading from Server involves multiple server-side APIs, so you need to obtain security credentials (SecretId and SecretKey) required for calling the server-side APIs first. The specific steps are as follows:

**Step1:** Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/).

**Step2:** Click "Cloud Products", and select "Cloud API Keys" under "Monitor & Management" to access the Cloud API key management page, as shown below:
![Cloud API Keys](//mccdn.qcloud.com/img568f5fb824757.png)

**Step3:** Obtain the cloud API keys as shown below. If you have not created the keys, click "New" to create a pair of SecretId/SecretKey.
![SecretID and SecretKey](//mc.qcloudimg.com/static/img/23f95aaa97adf3eeae3bf90470fe5122/image.png)

## Initiating Upload

The video upload is divided into [Upload Application](/document/product/266/31767), [Upload Files](/document/product/266/31784), and [Upload Confirmation]((/document/product/266/31766), which respectively correspond to step 1, 2, and 3 in the upload flow chart.

### Initiating Upload with the VOD SDK for Uploading from Server
Tencent Cloud VOD provides the Demos based on SDKs of different language platforms to make it easier for users to develop their upload features. See: 

* [PHP SDK](/document/product/266/9725);
* [JAVA SDK](/document/product/266/10276).

### Initiating Upload with Server APIs
If the language used in the App backend is not included in the upload SDK provided by VOD, the App backend needs to call the server APIs of VOD for uploading videos. It is recommended not to use this method as the first choice due to its complexity. The complete business flow chart of API-based upload is as follows:
![Flow Chart of Uploading Videos from Server APIs](//mc.qcloudimg.com/static/img/60561bf5cb67fceaaff79aa510f0a19c/image.png)


Compared to the SDK-based upload, the API-based uploading from server needs to complete [Upload Application], [Video File Upload] and other steps itself. Furthermore, [Video File Upload] is not as convenient as the SDK-based upload for it needs to perform multipart upload for large files. For more information, please see:

- [Server API: Upload Application](/document/product/266/31767);
- [Server API: File Upload](/document/product/266/31784);
- [Server API: Upload Confirmation](/document/product/266/31766).

## Event Notification
After a video file is uploaded successfully, Tencent Cloud VOD initiates an [Event Notification - Video Upload Completed](/document/product/266/7830) to the App backend, and the App backend becomes aware of the upload based on the notification.

To receive event notifications, the event notification needs to be enabled in the VOD console first, as shown below:
![Chart of Configuring Callback on Upload Completion](//mc.qcloudimg.com/static/img/f3383f3bed5aa3ce0015fa16d7cabb29/image.png)

[Event Notification - Video Upload Completed](/document/product/266/7830) contains the following information:

- FileId and URL of new video file;
- VOD supports specifying the transparently transmitted fields for uploading videos. VOD sends the transparently transmitted information to the App backed upon completion of upload. The event notification contains two fields: `SourceType` and `SourceCopntext`. `SourceType` is specified as `ServerUpload` by Tencent Cloud, which indicates the upload source is always server. `SourceContext` is a user-defined transparently transmitted field, and is specified by the App backend when the backend distributes upload signature to server. It corresponds to the parameter `sourceContext` in upload signature of server;
- VOD supports processing videos automatically when the videos are uploaded successfully. If you have specified [Video Processing Task Flow](/document/product/266/11700) for the upload, the event notification contains the task ID (field "data.procedureTaskId" in the event notification).

For more information, please see:
- [Task Management and Event Notification](/document/product/266/7829);
- [Event Notification - Video Upload Completed](/document/product/266/7830).

## Advanced Features

### Specifying the Task Flow When Uploading

After the video is uploaded, the developer can configure the parameter `procedure` when calling the server API [Upload Application](/document/product/266/9756) to automatically initiate [Video Processing Task Flow](https://cloud.tencent.com/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81), such as transcoding and screencapping.

**Example 1:** Perform video transcoding based on configurations in "Global Settings" -> ["Transcode Settings"](https://cloud.tencent.com/document/product/266/14058#.E8.BD.AC.E7.A0.81.E8.AE.BE.E7.BD.AE) in console after upload is completed, and apply the default watermark in the ["Watermark Management"](https://cloud.tencent.com/document/product/266/14059):

<pre>
procedure=QCVB_SimpleProcessFile(1,1)
</pre>

**Example 2:** Perform transcoding using [Transcoding Template](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF) 10, 20 after the video upload is completed; during the transcoding process, use [Watermark Template](https://cloud.tencent.com/document/product/266/11701#.E6.B0.B4.E5.8D.B0.E6.A8.A1.E6.9D.BF) 150 to apply watermarks; use the [Templates for Capturing Screenshots at Specified Time](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF) 10 to capture the first frame as cover; use the [Sampling Screenshot Template](https://cloud.tencent.com/document/product/266/11702#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF) 10 for the sampling screenshots.

<pre>
procedure=QCVB_SimpleProcessFile({10,20},150,10,10)
</pre>

The value of parameter `procedure` can also be other VOD built-in task flows, or custom task flows provided by the developer (for custom task flow, you need to submit a ticket to apply for it).

### Specifying the Storage Area When Uploading

The videos uploaded from server are stored in Guangzhou by default, but VOD also supports other areas. You can submit a ticket to apply for other storage areas for storage. Then you can specify the area when uploading videos. See:

* [PHP SDK](/document/product/266/9725);
* [JAVA SDK](/document/product/266/10276).


For more information, please see:

- [Parameter Templates and Task Flows](/document/product/266/11700);
- VOD built-in task flow [QCVB_SimpleProcessFile](/document/product/266/11700#qcvb_simpleprocessfile).

