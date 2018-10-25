## PC LVB Overview

![](//mc.qcloudimg.com/static/img/f47bf4ef0fcb96bdccf6f302b274afce/image.png)

Tencent Cloud PC LVB is used to push compressed and encoded images (such as **live events**, **teaching**, **projection** or **games**) to the **push URL** of Tencent **Video Cloud** by using push software (**OBS (recommended)** or **XSplit**) installed on PCs (**windows/mac**). Meanwhile, viewers can see **real-time images** using the playback URL corresponding to the push URL.


## PC LVB Procedure
PC LVB has a simple procedure, including the following steps:
- Get a **push URL** and 3 playback URLs from Tencent Cloud LVB console, to determine **push direction**.
- Use third-party push software, and set push audio and video sources and encoding parameters, to determine *push content*.
- Viewer can watch LVB using our RTMP DEMO to set playback URL. This helps **push the content to the viewers**.

![](//mc.qcloudimg.com/static/img/617e7cc6ae3313a2456e2672535e4097/image.png)


## 1. Before LVB
- Activate cloud LVB service on Tencent Cloud.
If you have not activate this service, click here to [apply for activation](https://console.cloud.tencent.com/live) of cloud LVB service.
![](//mc.qcloudimg.com/static/img/f45715687e787ee9a8e18154d1e13b92/image.png)

### 1.2 Generate push URL
If you don't have a **push URL**, you can generate a **push URL** and 3 playback URLs by clicking ["Access Management" -> "LVB Code Access" -> "Access Configuration"](https://console.cloud.tencent.com/live).

The one whose domain name is **livepush.myqcloud.com** is the push URL:
![](//mc.qcloudimg.com/static/img/98b9b659be67a9ac32384b606ace943f/image.png)

### 1.3 Select the network for LVB
- **Network selection**

| Network type | Accessibility | Stability |
|--|--|--|
| Cable | Poor | Good |
| WIFI | Good | Poor |
It is recommended to use cable network if possible, which is more stable than WIFI to make signals less disruptive. For event LVB, it is recommended to use WIFI for convenience.

- **Uplink bandwidth test**
The requirement for uplink bandwidth is determined by video quality and resolution. Generally, better video quality indicates higher resolution, so the requirement for uplink bandwidth would be higher. The uplink bandwidth should not be less than 1 Mbps. To check the uplink bandwidth, it is recommended to use [speedtest](http://www.speedtest.net/) for testing.
![](//mc.qcloudimg.com/static/img/b5724af9873220c395e295894205e4ad/image.png)

### 1.4 Install push software
- **OBS installation**
You can download an installation package on [OBS official website](https://obsproject.com/download) to install according to default settings. OBS is supported in such systems as Windows/Mac/Linux. You should make sure it is Open Broadcaster Software. OBS also provides OBS Studio which is not discussed in this document.
![](//mc.qcloudimg.com/static/img/dcbb929e364b1d8e80c04e326a756a26/image.png)

- **XSplit Installation**
You can download an installation package on [XSplit official website](https://www.xsplit.com/zh_cn/) to install according to default settings.
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
Click **Broadcasting Settings** in **Settings**, and set the Mode as **LVB Stream**, Stream Service as **Custom**, FMS URL as **the front part of push URL**, and Playback Path/Stream Code as the latter part of push URL. Automatic reconnection can trigger push connection automatically when OBS detects an exception (such as network disconnection). We recommend you to check this option.
![](//mc.qcloudimg.com/static/img/88024aaff126c5e34f4e96b9cd7e37c2/image.png)

### 2.2 Set audio and video sources
Audio and video sources are just like the contents of the package to be sent. There are three formats:
- From video capturing devices, such as camera or professional video equipments.
- From PC windows or game sources.
- From media files stored in PC, such as video images.

- **OBS audio and video sources configuration**
**Note**: **Click the right mouse button** in Source box. The left button is not applicable. The Add menu is popped up, followed by **Acquire from Window**, **Acquire from Screen**, Image Source, Slide Show, Text Source, CLR Browser, **Video Capturing Device**, Game Source, etc. We generally use Acquire from Window and Video Capturing Device. Other sources are configured in a different way. Next, we will introduce how to configure **Video Capturing Device**.
![](//mc.qcloudimg.com/static/img/c2f5a64918807e99aad4bd7778259e62/image.png)
![](//mc.qcloudimg.com/static/img/6f15746021918db02fbaefa6dc56c22b/image.png)
![](//mc.qcloudimg.com/static/img/d60b1a9c246d381a5e698bafac8c3f4e/image.png)

### 2.3 Set audio and video formats
After the video source is configured, even though you can get the audio and video signals, the original ones are not applicable for spreading in the network because they need more bandwidth. Therefore, it is important to configure the audio and video encoding parameters before LVB starts.

| Configuration Item | Feature | 
|:--------:|---------|
| **x264** | The h246 encoder is most commonly used in the industry with a higher video compression ratio under the same image quality. **It is recommended to check this option**. |
| Nvidia NVENC | It performs encoding using video processing core exclusively used by nv graphics card. It needs the support from Nvidia graphics card. |
| Quick Sync | Intel Quick Sync Video technology and hardware encoding are used, with high encoding efficiency and image quality, but poor compatibility and high bitrate. |
| **CBR** | One of video encoding bitrate control modes, which is called constant bitrate control. Stable bitrate is more suitable for network transmission. **It is recommended to check this option**. |
| **AAC** | The most popular LVB audio encoding format. **It is recommended to check this option**. |

- **OBS audio and video formats configuration**
![](//mc.qcloudimg.com/static/img/eb91f2e51ca3b3d8c39028262b4eae21/image.png)

## 3. Playback verification

### 3.1 Confirm playback URL
If the push URL (livepush) is:
> rtmp://3891.**<font color='blue'>livepush</font>**.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F

Then the playback URL (liveplay) is:

| Playback Protocol | Playback URL | 
|---------|---------|
| FLV |  `rtmp://3891.liveplay</font>.myqcloud.com/live/3891_test` |
| RTMP | `http://3891.liveplay</font>.myqcloud.com/live/3891_test.flv` |
| HLS(m3u8) | `http://3891.liveplay</font>.myqcloud.com/live/3891_test.m3u8` |


### 3.2 RTMP DEMO playback verification
[Download](https://cloud.tencent.com/document/product/454/6555) RTMP DEMO, and generate a QR by putting the playback URL into the online QR [generator](http://cli.im/), and then you can scan the QR for playback.

### 3.3 VLC playback verification
Click here for [VLC Download URL](http://www.videolan.org/vlc/). You can install according to the default settings. Open the software, click **Media Menu**, select **Open Network Stream**, enter the playback URL, and click **Play**.
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)




