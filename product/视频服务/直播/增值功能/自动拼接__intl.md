## 1. Overview
### 1.1 Description


**Why is video stitching needed?**

In LVB applications, transferring LVB to VOD is very common, that is, recording LVB stream for VOD playback. Transferring LVB to VOD depends on LVB recording. After recording an LVB file, you can release the generated file URL for VOD playback.

Current recording mechanism: The recording starts once the push begins and ends once the push is interrupted. After that, a recording file and a file URL are generated.

At present, recording may be interrupted due to network instability, VJ end errors or other factors. Therefore, an LVB video may often be recorded into multiple VOD files. In this case, you need to release multiple VOD URLs to enable end users to watch a complete video file. Obviously, this is unreasonable, so you need stitch multiple recorded files into a complete file before release.
		
**Why is automatic stitching needed?**

   Tencent Cloud LVB service features file stitching currently. However, you need manually call the API to achieve the feature, which is time-consuming and needs high access cost. To make stitching more convenient and efficient, LVB provides HLS automatic stitching.
   

### 1.2 Description

#### Automatic stitching overview

After the push at VJ end is interrupted for errors, as long as the push is continued during the specified time, the recording module will resume the recording rather than starting all over again. After the push ends (no push during the specified time), you can get a complete recorded file instead of multiple fragmental files.

#### Description

1. **Requirements for file automatic stitching**
   * The recorded file, namely, the stitched source file, must be HLS type. Currently, recorded MP4 and FLV files cannot be stitched.
   *The stitched​target file can only be HLS type. 
   *Requirements for audios or videos recorded in two consecutive pushes: For audios, their encoding type, sampling rate, the number of channels should be consistent. For videos, their encoding type should be the same. Otherwise, player incompatibility may occur.
   *For videos, their bitrate and resolution in two consecutive pushes can be different

2. **No limit to the number of recording interruptions**

If the push is interrupted, the recording can continue as long as you start push again during the specified duration. There is no limit to the number of interruptions.
  
3. **Configurable interruption duration**

You can configure push interruption duration that automatic stitching supports. The recommended duration is 0-5 minutes.
   
4. **URL of the recoded file**

The URL of the recoded file is M3U8 type. Each push interruption can generate a M3U8 URL, which includes the video content before the interruption. The M3U8 URL generated when the last push ends includes all the video content. 

5. **Automatic stitching does not occur after push interruption**

Generally, if automatic stitching is enabled, stitching will begin automatically when you start push again during the specified duration after push interruption. However, if push interruption is caused by**the calling of API for disabling playback, automatic stitching will not occur**, and recording will start all over again after re-push.

6. **Get URL of the recoded file**

The URL of the recorded file will be returned to you through callback. Currently, you can get a callback for the URL of the recoded file after each push interruption. Note: **To ensure that you get the VOD file with complete video content, we recommend you to release the last callback URL when no re-push occurs during the configured interruption duration**.
   
   
	 
## 2. Access Procedure

After accessing Tencent LVB service, you need to enable recording feature before enabling automatic stitching.
**You can enable recording feature as follows:**

1. **Enable recording feature**

  ![](//mc.qcloudimg.com/static/img/f0ae825b082dac847640eb7b931eb927/image.png)

When enabling the recording feature, you need **configure the recording file type to HLS** to use the automatic stitching feature.
Configure and enable the recording feature on the console. Currently, this is available only in LVB code mode. For more information, please see [Cloud Recording](https://www.qcloud.com/document/product/267/7963)

2. **Configure the callback URL**

![](//mc.qcloudimg.com/static/img/5bffecf8b1e7c59680237a3c6a5e1aba/image.png)

Configure the callback URL on the console, and LVB service backend will automatically call back the URL of recorded file to your service backend.
 **Note: Currently this is available only in LVB code mode. Therefore, in channel mode, you need call the API to query the URL of recorded file or submit a ticket to configure it on LVB cloud service backend. Therefore, we recommend you to use LVB code mode for access.**

3. **Configure automatic stitching**

Currently, you can configure automatic stitching and specify push interruption duration only on LVB cloud service backend. If you need enable automatic stitching, **submit a ticket or contact Tencent commercial personnel. Tel: 4009-100-100**.

  

