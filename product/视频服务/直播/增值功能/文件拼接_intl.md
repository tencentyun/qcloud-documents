## 1. Feature Overview
### 1.1 What is file stitching?
File stitching is to stitch some fragments into a complete video file.
To realize switching from LVB to VOD and LVB replay, Tencent Cloud LVB provides recording and stitching features. Recording is to record a live video and output video files in FLV, MP4, and HLS format. Due to the duration limitation of a recorded fragment, multiple fragments will be recorded for a live video. The file stitching feature can combine these fragments into a complete video file.

### 1.2 Why do I need to stitch recorded fragments?
If you do not stitch files, each file has a playback URL. After recording a live video to a VOD file, you need to publish its playback URL. However, it is impractical to publish that of every fragment. Instead, you must publish the playback URL of a complete VOD file. Therefore, file stitching can help you get a complete video for publishing.

### 1.3 How do I implement file stitching?
Since the cloud platform cannot accurately determine which files need to be stitched into a complete file, you must call relevant API for file stitching. For more information, please see "**2. Procedure**" section in this document.
This feature will be available in the console soon.

**Process of switching from LVB to VOD:**

Push streams > LVB recording > File stitching > Return the playback URL of a complete file > The video websites/Apps publish this URL as an VOD playback URL

**Supported file formats:**

FLV, MP4, and HLS files are supported for file stitching.

## 2. Procedure
**2.1 Activate Tencent Cloud LVB and VOD services first.**

The VOD service must be activated because the recording feature is supported by the backend cluster of Tencent Cloud VOD service. Recorded videos are stored in the VOD service, and the video information is also displayed in the **Video Management** of the VOD console. You only need to activate the VOD service, and no additional configurations are needed. For more information on LVB recording billing, please [click here](https://cloud.tencent.com/document/product/267/2818). Please note that recording will use VOD storage, and playback will consume VOD bandwidth. If you do not purchase a VOD package, VOD storage bills will be generated. For more information on VOD billing information, please [click here](https://cloud.tencent.com/product/vod#features).

*Follow the procedure below to activate LVB and VOD services:*
* Log in to the console, select **Cloud Products** -> **Video Service** -> **LVB** to go to the LVB console, and then click **Apply**. The application needs to go through manual audit at the backend and will take some time.

![](//mc.qcloudimg.com/static/img/8ef6dc8f0b0570e7e8e386bdea91de86/image.png)
* Log in to the console, select **Cloud Products** -> **Video Service** -> **VOD** to go to the VOD console, and then click **Verify**. The application needs to go through manual audit at the backend and will take some time.

![](//mc.qcloudimg.com/static/img/a7db7b4868396fed9260ec455232bfda/image.png)

**2.2 Enable recording**

Recording feature can be enabled by the following ways:

(1) Enable the recording feature globally in the console (only applicable to LVB code mode). **This method is recommended if you are using the LVB code mode**.

![](//mc.qcloudimg.com/static/img/6c000f311e6082bf9e826a63ab6960b3/image.png)

(2) Selectively enable the feature via URL parameters. This method has no limit on LVB mode, **which is recommended if you are using the channel mode**. For more information, please see "2.2 Selective Enabling" section of LVB [Cloud Recording](https://cloud.tencent.com/document/product/267/7963) document.
(3) Enable recording feature by calling the API, which is suitable for the channel mode. For more information, please see [Create Recording Task](https://cloud.tencent.com/document/product/267/4723)

**2.3 Get the information of recorded files**

The id (file_id) of the file to be stitched needs to be specified for the file stitching API. You need to know which fragments are generated using the recording feature before calling the API to stitch these fragments. **The file_id of a recorded file** can be obtained in the following two ways:

(1) You can obtain it via event message notification. For specific method and introduction, please [click here](https://cloud.tencent.com/document/product/267/5957).
(2) You can also periodically check if there is a new recorded file generated via the Tencent Cloud API for querying recorded files. For the API description, please [click here](https://cloud.tencent.com/document/product/267/5823).
(3) The recorded files generated are displayed on the VOD console with detailed recording information. The video ID column shows the file_id. Please click [here](https://console.cloud.tencent.com/video/videolist) to go to the VOD control.

**2.4 File stitching**

After obtaining the file ID, you can stitch files. API should be called for file stitching. Only the stitching API for HLS files is fully available. For more information, please see [File Stitching]().
Stitching APIs for other file types are not available. If necessary, please contact the customer service or submit a ticket. We will process it as soon as possible.

**2.5 How can I get the playback URL**

After the files are stitched, you can get the video playback URL and publish the complete stitched file.
You can obtain the playback URL of the stitched file by the following ways:
(1) Log in to the VOD console, go to the **Video Management**, and click the video to get the flash playback URL of the video.

![](//mc.qcloudimg.com/static/img/ac61247b7f178fb357f34c974146dbd1/image.png)

