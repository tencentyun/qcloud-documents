## 1. LVB Management

**Click "LVB" -> "LVB Management" to enter LVB**

On the LVB Management page, you can view the information of your current LVB channels, including LVB name, ID, status, creation time and operations. You can search for LVB by name/ID, and start, close or delete LVB channels in batches. After an LVB channel is created, it is displayed in the list. The relevant status is as follows:

- No input stream: The current LVB channel has started, but no input stream is found. The LVB channel can be closed or tested under this status.
- During LVB: The current LVB channel has started, and an input stream is found. The LVB channel can be closed or tested under this status.
- Closed: The current LVB channel is closed. The system does not receive the input stream nor distribute the output stream.

![](//mccdn.qcloud.com/img569df1b901a98.png)

**View and modify LVB channel settings**

When an LVB channel is closed, you can click on its name to check the LVB configuration and output address, or modify the configuration of the LVB channel.

LVB configurations are shown as follows. You can make modifications by clicking the Edit button next to Settings. Note: the configurations of an LVB channel can be modified only when it is closed.

![](//mccdn.qcloud.com/img569df1fc3c8bd.png)

**View and edit the player code for LVB publishing**

You can view the player code for LVB publishing, so as to easily integrate the LVB display capability with Web Apps. This code supports playback on PC and in mobile device.

![](//mccdn.qcloud.com/img569df21d0be24.png)

Click **Edit** to modify the following code, and the updated player code shows after you save the edited content.

Player size: The size of the player border. Commonly used size and custom size are supported.

Player password: Basic security features are provided. You can set an 8-digit alphanumeric (case-sensitive) password. Viewers need to enter the correct password to watch LVB. Note: this feature does not take effect if viewers do not use the player.

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunzhiboshiyong-6.png)

## 2. Create a Channel
Click **Create Channel** on the left navigation menu, or click the **Create Channel** button in the LVB Management interface.

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunzhiboshiyong-7.jpg)

Configure the basic information of LVB, including channel name and channel description.

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunzhiboshiyong-8.jpg)

## 2.1 Transcode Configuration
Select whether to transcode in real time. After selecting, you can get the corresponding link addresses in subsequent steps.
![](//mccdn.qcloud.com/static/img/ef23686f2cc4314bcc09a1601aefcf81/image.png)
HD: Resolution 1280x720. Bitrate 900 Kbps
SD: Resolution 960x540. Bitrate 550 Kbps
Original: Original resolution. Bitrate is the original bitrate (always presented).

After the resolution is specified, the backend provides different addresses corresponding to different bitrates when it generates the playback address, so that you can choose one to call. Since the generated video resolution is strictly in line with the above ratio, the original push resolution should be as close as possible to the above ratio to avoid extension or distortion of views.

When users access a new bitrate address for the first time, the user who first triggers the link may experience a long load time, which is normal. Users who access the address subsequently can enjoy a consistent experience.

**You can use the real-time transcoding feature by following the method below:**
1. If you use Tencent Cloud Web player SDK, after the real-time transcoding is enabled, the player automatically displays the appropriate bitrate according to the channel settings at the location where the resolution is selected in the lower right corner. You can make manual adjustments. The default determination logic is:
	1. PC: The original resolution is preferred.
	2. Mobile: High definition with resolution of 900 Kbps is preferred. If it is not available, the original resolution is used.
2. Directly access to the corresponding bitrate address, and play videos using a third-party player.

## 2.2 LVB Source Settings
Enter information for LVB source settings.
The followings can be set:

LVB source name: Used as an ID. The system supports only one LVB source.

Protocol type: RTMP push and FLV/HLS/RTMP pull features are supported.

If RTMP push is selected, the system automatically generates a push address. This address is displayed after the configuration is completed. You can copy this address and configure it on an existing server, RTMP encoder or software.

If FLV/HLS/RTMP pull is selected, you need to enter the existing FLV/HLS/RTMP public network address, so that the system can pull the video stream from that address.

![](//mccdn.qcloud.com/static/img/716dc322dcd2cfe6a856cbe6214261fc/image.png)

## 2.3 Settings of Receiver's Multi-protocol and Multi-bitrate
Configure receiver settings:

The distribution of HLS and RTMP/FLV protocols is supported. After selecting, you can get the corresponding link addresses in subsequent steps.
![](//mccdn.qcloud.com/static/img/ed068b7e91bda288a5b4f362a1a8255b/image.png)

For example, if multi-bitrate and multi-protocol are configured, you can get the following addresses:
![](//mccdn.qcloud.com/static/img/78d759181198e280f4ccb19b583b6132/image.png)

## 2.4 Apply Watermarks to Channels
You can choose a watermark (including pattern and location) in Global Settings. The watermark needs to be set when the channel is created or closed. It cannot be modified after the LVB starts.

As shown below:
![](//mccdn.qcloud.com/static/img/f2ab2e03ce562b566a3be3f2d2db9127/image.png)

## 3. Statistical analysis

You can select the statistical analysis feature in the menu to view the information such as bandwidth, traffic, number of requests and number of LVB channels by date.

You can also view statistics for all LVB channels of your account. As shown below:

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/zhiboliucheng-1.png)

## 4. Recording

You can record LVB channels through the API. For more information, please see [LVB API](http://cloud.tencent.com/doc/api/258/API%E6%A6%82%E8%A7%88).

Recorded files are automatically stored on the VOD platform. Therefore, before using the recording feature, you need to activate VOD service in advance and purchase space and traffic for storing and playing recorded video files. For more information, please see [Video on Demand](http://cloud.tencent.com/product/vod.html).

Steps:
1. Activate VOD service.
2. Use the API for creating a recording task.
3. Use the API for ending a recording task.
4. Use the API for querying recorded fragments to get fileID.
5. Obtain the playback address or perform operations such as transcoding on the VOD platform according to fileID (optional).

For more information on APIs for performing operations on files on the VOD platform, please see [VOD API Overview](https://cloud.tencent.com/document/product/266/7788).

Specifications:
1. Videos are recorded based on the original LVB bitrate. The output format is FLV.
2. Recording format: The maximum recording length of a single file is 30 minutes. A new file is created for recording if the limit is exceeded.
3. The maximum recording length of a single recording task is 24 hours.
4. During the LVB, you can obtain a recorded file in about 5 minutes upon the end of recording process. For example, if an LVB is recorded from 12:00, the corresponding fragment from 12:00 to 12:30 is available around 12:35, and so on.
5. Note: Fees for the recorded file are generated in the VOD platform. Pay attention to the relevant costs based on your actual needs. For more information on billing methods, please see [Video on Demand](http://cloud.tencent.com/product/vod.html).

## 5. Screenshot

**How to activate**
1. You can take screenshots of LVB channels through the API. For more information on how to use API for creating screenshot task, please see [Create Screenshot Task](https://cloud.tencent.com/document/product/267/4726).
   To end a screenshot task in time, use the API for ending screenshot task. For more information, please see [End Screenshot Task](https://cloud.tencent.com/document/product/267/4727).
2. You can also start a screenshot task on the console (recommended).
![](//mc.qcloudimg.com/static/img/b3f3257b8f13e4b0be956ccceb0a916f/image.png)

*Note: Due to historical reasons, for some registered customers, the screenshots are stored in the COS platform. Therefore, before using the screenshot feature, these users need to activate COS service in advance and purchase space and traffic for storing and downloading screenshot files.
Now, the screenshot feature has been optimized for Tencent Cloud LVB service. Customers can directly activate screenshot feature instead of activating COS service.*

**Query screenshots**
You can get screenshot information by using the queue query API.
This service must be activated separately for the queue query API. You can submit a request through the after-sales QQ number 514025596 to activate the service. You can send the request by simply indicating that "Request to activate the LVB screenshot queue query API service" as well as the account information in the message. The service will be activated within one business day.

Specifications:
1. Screenshots are captured based on the original LVB bitrate. The frequency is one screenshot every 10 seconds, which is fixed and cannot be modified.
2. The output format is JPG.
3. When the task starts, you can get the screenshot file after 20 seconds upon the start of LVB process.
4. Reminder: Fees for the screenshot file are generated in the COS platform. Pay attention to the relevant costs based on your actual needs. For more information on billing methods, please see [Cloud Object Storage](http://cloud.tencent.com/product/cos.html).

## 6. Global Watermark Settings

You can set the watermark style in Global Settings, including pattern and location. Watermark images in PNG format are supported with maximum file size of 200 KB and pixel size of 200*200. After the configuration is completed, you can apply it to channels in Channel Configuration or Channel Status Modification interface.
You can set one of the watermarks as the default watermark. Once the default watermark is set, all newly created channels use the watermark by default. You can also choose another watermark in the configuration via the drop-down box, or select not to use watermark.

As shown below:
![](//mccdn.qcloud.com/static/img/b7404365dcecfff268e031c386964cc6/image.png)



