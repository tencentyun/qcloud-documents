## 1. Overview
### 1.1 Background


**Why is video stitching needed?**

Switching from LVB to VOD is a common application scenario for LVB events. That is, record the LVB stream for VOD playback. This switching relies on LVB recording feature. A file URL is generated upon the completion of the LVB recording, and the video is available for VOD playback after the file URL is published.

Recording starts as push starts and ends when push is interrupted, in which case a recorded file and a file URL are generated.

Recording may be interrupted due to poor network, VJ-side exception or other factors, therefore, an LVB event may be recorded as multiple files. This means that multiple VOD URLs have to be published for end users to watch the entire video, which is obviously impractical. Therefore, multiple recorded files must be stitched into a complete file before publishing.
		
**Why is automatic stitching needed?**

   The old file stitching feature provided in Tencent Cloud LVB service requires manual calling of APIs, which takes long and costs a lot. To make file stitching more convenient and efficient, LVB service launches HLS automatic stitching feature.
   

### 1.2 Description

#### Automatic stitching

When the push is interrupted due to VJ-side exception, the recording module continues the recording as long as the push is resumed within a specified time frame, rather than creating a new recording file. When the push ends (no push occurs in a specified period), a complete recorded file (instead of multiple fragments) is generated.

#### Feature description

(1) **Requirements for automatic file stitching**
   * <font color='red'>The type of recorded files must be HLS, that is, the source files to be stitched must be HLS files.</font> MP4 and FLV files are not supported.
   * The files can only be stitched as HLS files. 
   * Audio files to be stitched must be consistent in encoding type, sampling rate, and number of tracks, and video files to be stitched must be consistent in encoding type. Otherwise player compatibility issues may occur.
   * The video files to be stitched may have different bitrates and resolutions

(2) **No limit on the number of times the recording is interrupted:**

No matter how many times a push is interrupted, the recording will continue as long as the push is resumed within a specified time frame.
  
(3) **Interruption period can be configured:**

You can configure the push interruption period supported by automatic stitching, which is limit to 5 minutes.
   
(4) **URL of recorded files:**

The URL of recorded files is m3u8 URL. A URL is generated each time the push is interrupted. The content of a m3u8 URL is the video content before the push is interrupted. The m3u8 URL generated when the push ends is the complete video content. 

(5) **When does automatic stitching not work?**

Generally, if the automatic stitching feature is enabled, files will be automatically stitched when the push is resumed from the interruption within a specific time frame. However, if **the push is interrupted by calling the stream suspension API, files will not be automatically stitched**, and the recording will restart after the push is resumed.

(6) **Obtain recorded files' URLs:**

The URLs of recorded files will be returned through callback. You will receive the URL of a recorded file each time the push is interrupted. Note: **To ensure the completeness of the published VOD file, we recommend that you publish the URL returned the last time if the push is not restarted during the interruption period.**

(7) **File display**
Like other recorded files, automatically stitched files are also displayed on the VOD console.
   
   
	 
## 2. Connection Procedure

After connecting to the Tencent LVB service, you need to enable the recording feature before enabling the automatic stitching feature.
**The specific procedure is as follows:**

(1) **Enable recording**

  ![](//mc.qcloudimg.com/static/img/f0ae825b082dac847640eb7b931eb927/image.png)

When enabling the recording feature, you need to **configure the recording file type as HLS** in order to use the automatic stitching feature.
For more information on how to configure and enable the recording feature (in LVB code mode only) via the console, please see [Cloud Recording](https://cloud.tencent.com/document/product/267/7963).

(2) **Configure a callback URL**

![](//mc.qcloudimg.com/static/img/5bffecf8b1e7c59680237a3c6a5e1aba/image.png)

Configure a callback URL in the console, and then the LVB service backend automatically calls back the URL of the recorded file to your service backend.
 **Note: The callback URL can be configured in the console only under the LVB code mode. In the channel mode, you need to call the API to query the recording URL or submit a ticket to request for configuration on the Cloud LVB service backend. Therefore, the LVB code mode is recommended.**

(3) **Configure the automatic stitching feature**

The automatic stitching feature and interruption period supported by automatic stitching can only be configured on the Cloud LVB service backend. To enable the automatic stitching feature, **submit a ticket or contact Tencent's service personnel. Tel: 4009-100-100**.

  

