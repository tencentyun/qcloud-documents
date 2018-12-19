## TXLivePushListener

### 1. How to obtain the push status data?
The onNetStatus callback of TXLivePushListener synchronizes the status metrics inside SDK at an interval of 1-2 seconds. The major metrics are as follows:

![](//mc.qcloudimg.com/static/img/07810dd6565d371a37892227bd174714/image.png)

| Push Status | Description |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE | CPU utilization of current process and overall CPU utilization of the machine |
| NET_STATUS_VIDEO_WIDTH | Width of the current video (in pixels) |
| NET_STATUS_VIDEO_HEIGHT | Height of the current video (in pixels) |
| NET_STATUS_NET_SPEED | Current transmission speed (in Kbps) |
| NET_STATUS_VIDEO_BITRATE | The output bitrate of the current video encoder, that is, the video data bits produced by the encoder per second (in Kbps) |
| NET_STATUS_AUDIO_BITRATE | The output bitrate of the current audio encoder, that is, the audio data bits produced by the encoder per second (in Kbps) |
| NET_STATUS_VIDEO_FPS | Current video frame rate, that is, the number of frames produced by video encoder per second |
| NET_STATUS_CACHE_SIZE | Accumulated audio/video data size. A value ≥ 10 indicates the current upstream bandwidth is not enough to consume the audio/video data produced |
| NET_STATUS_CODEC_DROP_CNT | The number of global packet drops. To avoid a vicious accumulation of delays, the SDK actively drops packets when the accumulated data exceeds the threshold. A higher number of packet drops means a more severe network problem.
| NET_STATUS_SERVER_IP | IP of the connected push server |

### 2. Which status metrics can be used for reference?

#### BITRATE vs NET_SPEED 
BITRATE( = VIDEO_BITRATE + AUDIO_BITRATE) refers to the number of audio/video data bits produced by the encoder for push per second; NET_SPEED refers to the number of data bits pushed actually per second.

- If BITRATE == NET_SPEED in most cases, the push quality is very good;

- If BITRATE >= NET_SPEED for a long time, audio and video data will accumulate on VJ's mobile phone and make CACHE_SIZE increase to such a point that the data is dropped by SDK to generate DROP_CNT.

#### CACHE_SIZE & DROP_CNT
In case of a slow upload speed at VJ end, it is likely that BITRATE >= NET_SPEED. In this case, the audio/video data build up on VJ's phone, with the severity indicated by the CACHE_SIZE value. When the CACHE_SIZE value exceeds the threshold, SDK drops some audio/video data, thus triggering an increment of DROP_CNT.

![](//mc.qcloudimg.com/static/img/3c10b3a268b4807a184b767b1cc4363c/image.png)

#### CPU_USAGE
- If **CPU utilization of system** exceeds 80%, the stability of audio/video encoding is affected, leading to random stutters in video image and sound.

- If **CPU utilization of system** reaches 100% frequently, the audio/video encoding frame rate will become insufficient, leading to serious stutters in video image and sound.

> It is very common that in the practical use of an App that performs well in per-launch test, the scrolling and refreshing of interactive messages of front rooms consume a significant amount of CPU and thus lead to serious stutters in LVB video image.

#### SERVER_IP
If the IP address of the VJ's SERVER_IP has a high ping value (for example, over 500 ms), the push quality cannot be guaranteed.**Access to the nearest** is what Tencent Cloud is expected to do. If you experience such a problem, please contact us for adjustments and optimization by our OPS team.

### 3. How to comprehend Tencent Cloud push chart?
In [LVB Console - Quality Control](https://console.cloud.tencent.com/live/livesdk), you can get a picture of the live rooms under your account and the push quality of each room:

- **VJ end - expected bitrate - Actual bitrate curve**
The blue curve is the statistical curve of BITRATE, i.e. the audio and video data bits produced by the SDK. The green curve indicates the data bits actually pushed via the network. A higher fit between the two curves means a better push quality.

![](//mc.qcloudimg.com/static/img/53773c13d29d39063a1fbd2ff228ab6a/image.png)

- **VJ end - Accumulation of audio/video data**
 + The consistent fit between the curve and 0 scale means the entire push is very smooth and no data is accumulated.
 + The points where the curve > 0 indicate accumulated data caused by network fluctuations, which may lead to slight stutters and asynchronization between video and audio at the viewer end;
 + If the accumulated data exceeds the red warning level, it means that some packets has been dropped, which will inevitably result in stutters and asynchronization between video and audio at the viewer end.
 
![](//mc.qcloudimg.com/static/img/665a7ae6063594d3e85c62b2eda4c1d1/image.png)

- **Cloud end - expected video duration - actual video duration curve**
This is the statistics curve for Tencent Cloud server end, and is the only chart visible to you if you do not use Tencent Cloud SDK for push (the first two charts are invisible to you because the data is provided by SDK). A higher fit between the blue and green curves indicates a better push quality.

![](//mc.qcloudimg.com/static/img/c07d5faa3df10ad774801aa3c79cc8a5/image.png)

## TXLivePlayListener

### 1. How to obtain the playback status data?
The onNetStatus callback of TXLivePlayListener synchronizes the status metrics inside SDK at an interval of 1-2 seconds. The major metrics are as follows:
![](//mc.qcloudimg.com/static/img/bc00f0c279a67282de0cc3ce69988e7c/image.png)

| Playback Status | Description |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | Current CPU utilization (instantaneous) | 
| NET_STATUS_VIDEO_WIDTH  | Video resolution - width |
| NET_STATUS_VIDEO_HEIGHT | Video resolution - height |
| NET_STATUS_NET_SPEED | Current download speed of network |
| NET_STATUS_VIDEO_FPS     | The video frame rate of the current stream media    |
| NET_STATUS_VIDEO_BITRATE | Video bitrate of the current stream media (in Kbps) |
| NET_STATUS_AUDIO_BITRATE | Audio bitrate of the current stream media (in Kbps) |
| NET_STATUS_CACHE_SIZE | Playback buffer (jitterbuffer) size. A smaller buffer size means a lower resistance against stutters. |
| NET_STATUS_SERVER_IP | IP of the connected server | 

### 2. Which status metrics can be used for reference?
#### NET_STATUS_CACHE_SIZE
This metric reflects the size of the playback buffer (jitterbuffer):
- The larger the CACHE_SIZE, the higher the delay, and the less likelihood of stutters in case of network fluctuations.
- The smaller the CACHE_SIZE, the lower the delay, and the more likelihood of stutters in case of network fluctuations.

TXLivePlayer comes with three modes for controlling the playback buffer size. For more information, please see [Basic Features - Playback] document:
![](//mc.qcloudimg.com/static/img/1d5a860ff74f9d026a36c04dd8bb27ef/image.jpg)

