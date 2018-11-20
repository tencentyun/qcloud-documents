### Set push URL
If you get the following push URL: `rtmp://3891.livepush.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F`

You need to set two parts of the push URL separately:
The first part is: `rtmp://3891.livepush.myqcloud.com/live/`, which is called FMS URL.
The second part is: `3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F`, which is called streaming code.

#### OBS push URL settings

Click **Settings**, select **Broadcasting Settings**, and then set **Mode** to **LVB Stream**, **Streaming Service** to **Custom**, **FMS URL** to the first part of push URL, and **Playback Path/Streaming Code** to the second part. You're recommended to check **Automatic Reconnection**, which means push reconnection is triggered automatically when OBS detects an exception (such as network disconnection).
![](//mc.qcloudimg.com/static/img/8f5dabbdea9882531464017385648e0c/image.png)
![](//mc.qcloudimg.com/static/img/88024aaff126c5e34f4e96b9cd7e37c2/image.png)

#### OBS Studio push URL settings
Click **Settings** in the lower right corner of the page, select **Stream**, and then set **Streaming Type** to **Custom Streaming Media Server**, **URL** to the first part of the push URL, and **Stream Key** to the second part.
![](//mc.qcloudimg.com/static/img/023f599e7fe3e22a8d348a6b4b7b0720/image.png)
### Set audio/video sources
Audio/video sources are like the contents of the package you want to deliver. There are three types of audio/video sources:
- From video capture devices (such as camera or video recording devices);
- From PC windows or game sources;
- From media files stored in PC (such as video images).

#### OBS audio/video source settings
**Note**: Right-click in the **Source** box. The **Add** menu pops up, which is followed by **Acquire from Window**, **Acquire from Screen**, **Image Source**, **Slide Show**, **Text Source**, **CLR Browser**, **Video Capture Device**, and **Game Source**, etc. **Acquire from Window** and **Video Capture Device** are commonly used. The settings vary with different sources. The following describes the settings of **Video Capture Device**.
![](//mc.qcloudimg.com/static/img/c2f5a64918807e99aad4bd7778259e62/image.png)
![](//mc.qcloudimg.com/static/img/6f15746021918db02fbaefa6dc56c22b/image.png)
![](//mc.qcloudimg.com/static/img/d60b1a9c246d381a5e698bafac8c3f4e/image.png)

#### OBS Studio audio/video source settings
For more information, please see "OBS audio/video source settings".

### Set audio/video formats
After the video source is set, although the audio/video signals can be obtained, the original audio and video signals are not suitable for transmission over network because of their high requirement for bandwidth. Therefore, it is very important to set audio/video encoding parameters before live broadcasting.

| Configuration Item | Feature | 
|:--------:|---------|
|x264| Recommended. The h264 encoder is most commonly used in the industry and allows a higher video compression ratio for the same image quality. |
|Nvidia NVENC| Encoding using the video processing core dedicated to nv graphics card. Nvidia graphics card is required. |
|Quick Sync| Use Intel Quick Sync Video technology to support hardware encoding with a high encoding speed and image quality. But it has a poor compatibility and high bitrate. |
|CBR| This is one of video encoding bitrate control modes and is called constant bitrate control. With a consistent bitrate, it is more suitable for network transmission. It is recommended to check this option. |
| AAC | This is the most widely used live audio encoding format. It is recommended to select this option. |

#### OBS audio/video format settings
![](//mc.qcloudimg.com/static/img/eb91f2e51ca3b3d8c39028262b4eae21/image.png)

#### OBS Studio audio/video format settings
![](//mc.qcloudimg.com/static/img/1d473aed08fcdc7611d8de599184e75c/image.png)
![](//mc.qcloudimg.com/static/img/baa533b47d920f70ca08b12771ee3158/image.png)
