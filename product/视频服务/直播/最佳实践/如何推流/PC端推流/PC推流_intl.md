## PC LVB Overview

![](https://main.qcloudimg.com/raw/4ed8b74a5f1dd5e36ff2b70c82adb25a.png)

Tencent Cloud PC LVB is used to push compressed and encoded images (such as **live events**, **teaching**, **projection** or **games**) to the **push URL** of Tencent **Video Cloud** by using push software (**OBS (recommended)** or **XSplit**) installed on PCs (**windows/mac**). Meanwhile, viewers can see **real-time images** using the playback URL corresponding to the push URL.


## PC LVB Procedure
You can implement PC LVB easily by following the steps below:
- **Where are the streams pushed to**: Get a **push URL** and 3 playback URLs from Tencent Cloud LVB console.
- **What is pushed**: Set audio/video sources for push and encoding parameters in the third-party push software.
- Viewer can watch LVB using our RTMP DEMO to set playback URL. This helps **push the content to the viewers**.

![](https://main.qcloudimg.com/raw/fece166faaa92f7e907b64581cff220c.png)


## 1. Before LVB
- Activate cloud LVB service on Tencent Cloud.
If you have not activated the Tencent Cloud LVB service, click here to [apply for the service](https://console.cloud.tencent.com/live).
![](https://main.qcloudimg.com/raw/2ff750be6832f364645a7ac8ee736f5b.png)

### 1.2 Generate push URL
If you don't have a **push URL**, you can generate a **push URL** and 3 playback URLs by clicking [**Access Management** -> **LVB Code Access** -> **Access Configuration**](https://console.cloud.tencent.com/live).

The one whose domain name is **livepush.myqcloud.com** is the push URL:
![](https://main.qcloudimg.com/raw/049318c003544a79d45ad51281041252.png)

### 1.3 Select the network for LVB
- **Network selection**

| Network Type | Accessibility | Stability |
|--|--|--|
| Wired network | Low | High |
|WIFI| High | Low |
It is recommended to use cable network if possible, which is more stable than WIFI to make signals less disruptive. For event LVB, it is recommended to use WIFI for convenience.

- **Upstream bandwidth test**
The requirement for upstream bandwidth depends on the video quality and resolution. Generally, a better video quality with a higher resolution means a higher requirement for upstream bandwidth. The upstream bandwidth should not be less than 1 Mbps. To check the condition of upstream bandwidth, you can conduct a test using [speedtest](http://www.speedtest.net/).
![](//mc.qcloudimg.com/static/img/b5724af9873220c395e295894205e4ad/image.png)

### 1.4 Install push software
- **OBS installation**
You can download an installation package on [OBS official website](https://obsproject.com/download) to install according to default settings. OBS is supported in such systems as Windows/Mac/Linux. You should make sure it is Open Broadcaster Software. OBS also provides OBS Studio which is not discussed in this document.
![](//mc.qcloudimg.com/static/img/dcbb929e364b1d8e80c04e326a756a26/image.png)

- **XSplit Installation**
You can download an installation package on [XSplit official website](https://www.xsplit.com/zh_cn/) to install it according to default settings.
XSplit is not a free software. As an alternative, you can use OBS (**Free**). For game LVB, XSplit has a separate installation package. It is recommended to use BroadCaster for non-game LVB.
![](//mc.qcloudimg.com/static/img/18c47cb7646e189acc168e6a5e8e4714/image.png)

## 2. Software parameter configuration
### 2.1 Set push URL
If you get the following push URL:
> rtmp://3891.livepush.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F

You need to set two parts separately:
> The front part of the push URL **"rtmp://3891.livepush.myqcloud.com/live/"** is called **FMS URL**
> The latter part of the push URL **"3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F"** is called **stream code**.

- **OBS push URL configuration**
![](//mc.qcloudimg.com/static/img/8f5dabbdea9882531464017385648e0c/image.png)
Click **Settings**, select **Broadcasting Settings**, and then set **Mode** to **LVB Stream**, **Streaming Service** to **Custom**, **FMS URL** to the first part of push URL, and **Playback Path/Streaming Code** to the second part. You're recommended to check **Automatic Reconnection**, which means push reconnection is triggered automatically when OBS detects an exception (such as network disconnection).
![](//mc.qcloudimg.com/static/img/88024aaff126c5e34f4e96b9cd7e37c2/image.png)

- **OBS Studio push URL settings**
![](//mc.qcloudimg.com/static/img/023f599e7fe3e22a8d348a6b4b7b0720/image.png)
Click **Settings** in the lower right corner of the page, select **Stream**, and then set **Streaming Type** to **Custom Streaming Media Server**, **URL** to the first part of the push URL, and **Stream Key** to the second part.

### 2.2 Set audio and video sources
Audio and video sources are just like the contents of the package to be sent. There are three formats:
- From video capturing devices, such as camera or video recording devices.
- From PC windows or game sources;
- From media files stored in PC, such as video images.

- **OBS audio and video sources settings**
**Note**: **Click the right mouse button** in Source box. The left button is not applicable. The Add menu is popped up, followed by **Acquire from Window**, Acquire from Screen, Image Source, Slide Show, Text Source, CLR Browser, **Video Capturing Device**, Game Source, etc. We generally use Acquire from Window and Video Capturing Device. Other sources are configured in a different way. Next, we will introduce how to configure **Video Capturing Device**.
![](//mc.qcloudimg.com/static/img/c2f5a64918807e99aad4bd7778259e62/image.png)
![](//mc.qcloudimg.com/static/img/6f15746021918db02fbaefa6dc56c22b/image.png)
![](//mc.qcloudimg.com/static/img/d60b1a9c246d381a5e698bafac8c3f4e/image.png)

- **OBS Studio audio/video source settings**
For more information, please see **OBS audio and video sources settings**.

### 2.3 Set audio and video formats
After the video source is configured, even though you can get the audio and video signals, the original ones are not applicable for spreading in the network because they need more bandwidth. Therefore, it is important to configure the audio and video encoding parameters before LVB starts.

| Configuration Item | Feature | 
|:--------:|---------|
|**x264**| The h264 encoder is most commonly used in the industry with a higher video compression ratio under the same image quality. **It is recommended to select this option**. |
|Nvidia NVENC| It performs encoding using the video processing core dedicated to nv graphics card. Nvidia graphics card is required. |
|Quick Sync| Use Intel Quick Sync Video technology to support hardware encoding with a high encoding speed and image quality. But it has a <font color='red'>poor compatibility</font> and high bitrate. |
|**CBR**| This is one of video encoding bitrate control modes and is called constant bitrate control. With a consistent bitrate, it is more suitable for network transmission. **It is recommended to select this option**. |
| **AAC** | This is the most widely used live audio encoding format. **It is recommended to select this option**. |

- **OBS audio and video formats configuration**
![](//mc.qcloudimg.com/static/img/eb91f2e51ca3b3d8c39028262b4eae21/image.png)

- **OBS Studio audio/video format settings**
![](//mc.qcloudimg.com/static/img/1d473aed08fcdc7611d8de599184e75c/image.png)
![](//mc.qcloudimg.com/static/img/baa533b47d920f70ca08b12771ee3158/image.png)

## 3. Playback verification

### 3.1 Confirm playback URL
If the push URL (livepush) is:
> rtmp://3891.**<font color='blue'>livepush</font>**.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F

the playback URL (liveplay) is:

| Playback Protocol | Playback URL | 
|---------|---------|
| FLV |  `rtmp://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test` |
| RTMP | `http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.flv` |
| HLS(m3u8) | `http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.m3u8` |


### 3.2 RTMP DEMO playback verification
[Download](https://cloud.tencent.com/document/product/454/6555) RTMP DEMO, generate a QR code from the playback URL using the online QR code [generator](http://cli.im/), and then scan the QR for playback.

### 3.3 VLC playback verification
Click here for [VLC Download URL](http://www.videolan.org/vlc/). You can install according to the default settings. Open the software, click **Media Menu**, select **Open Network Stream**, enter the playback URL, and click **Play**.
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)




