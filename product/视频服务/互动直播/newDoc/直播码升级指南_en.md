## LVB Code Mode Upgrade Guide

### New Features of LVB Code Mode

1. Both automatic non-interactive broadcasting and automatic recording are supported, **thus greatly reducing the risk of failure of non-interactive broadcasting and recording caused by wrong timing of API calling.**
2. URL generation and LVB stream are highly free and customized.
3. Multiple recording types are supported. Event callback is performed after recording is completed.
4. Prerequisites of stream mixing.

## How to Upgrade LVB Code Mode

![](https://mc.qcloudimg.com/static/img/2bcf5926caa034e205b96ad0b85bc24d/C9F9849C-7E9C-4BFA-85EB-CCC266F8B15F.png)<br/>

## How to Determine Whether the Current Mode is Channel Mode or LVB Code Mode

In Tencent Cloud console, select `"LVB" -> "LVB Code Access (Recommended)"`. If you see a similar page to the figure below, the current mode is still **Channel Mode**, otherwise it is **LVB Code Mode**.

![](https://mc.qcloudimg.com/static/img/488c132a42470912ec4c49091a041cb9/4.png)<br/>

#### If it is still channel mode, you must submit a ticket according to the flow chart, and do not change the mode to LVB code mode directly in the console, nor to create a new SDKAppID for the test.

## How to Submit a Ticket to Apply for Compatible LVB Code Mode

1. In the console, select **Submit Ticket** to create a ILVB ticket.
2. Select **Other Problems** for problem type. Write the following information in **Problem Description**:

* Title: Apply to activate compatible LVB code mode
* Content 1: Company's appid (not SDKAppID, developers can find it in LVB console or ILVB console)
* Content 2: Whether to automatically start non-interactive broadcasting when you create a room during ILVB.

## How to Switch to LVB Code Mode in LVB Console

1. Check whether LVB service is activated<br/>

[Select `LVB` tab in Tencent Cloud console](https://console.cloud.tencent.com/live). If the service has not been activated yet, the following page appears:<br/>
![](https://mc.qcloudimg.com/static/img/c40ff3b85b3ad9c0cb03170948d93555/image.png)<br/>
Click **Request for Activation**, then go to Tencent Cloud's manual review stage. Upon the approval of Tencent Cloud, the service is activated.

2. After the LVB service is activated, select `LVB Code Access` in `Access Management` of `LVB` tab in the console. The following options is shown in the page at the right side:<br/>

![](https://mc.qcloudimg.com/static/img/973b21b88bf24bf02eb276c8e0e9efb3/1.png)<br/>

The options are described as follows:<br/>

Configuration Option  | Available Value Range | Description | Detailed Documentation
:-----: | :-----: | :-----:|:-----: 
LVB Recording | Enable OR Disable | After it is enabled, all non-interactive broadcasting videos are recorded by default.  | [Supplementary document address](https://cloud.tencent.com/document/product/454/7917)
Push hotlink protection key | 32-bit lower-case string | The key used to calculate push hotlink protection address | [DOC](https://cloud.tencent.com/document/product/454/7917)
API authentication key | 32-bit lower-case string | The parameter required for authentication information when business server and Tencent Cloud backend call each other's API | [DOC](https://cloud.tencent.com/document/product/454/7920#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5)
Callback URL | URL of HTTP | Callback URL of business server. Notification of push and recording events is sent via this URL. HTTPS is not supported | [DOC](https://cloud.tencent.com/document/product/267/5957)

3. After the configuration is completed based on your business needs, click `Confirm to Access`. Now, the LVB Code mode is activated.

## Automatic Stream Mixing of Non-interactive Broadcasting under LVB Code Mode

Under LVB code mode, audio/video data of VJ and viewer who joins broadcasting can be mixed into one channel of audio/video stream for playback.<br/>
Users can `select "Enable" in non-interactive broadcasting configurations` in the ILVB console.

### Notes on Automatic Steam Mixing of Non-interactive Broadcasting

1. Automatic stream mixing takes effect after 15 minutes upon enabling
2. The roles of VJ and viewer who joins broadcasting should be correctly configured in App code
3. Currently, only two channels are supported. The viewer who joins broadcasting is fixed at the bottom right corner
4. After the audio/video streams of non-interactive broadcasting are successfully mixed, the corresponding recorded files are also mixed.





