## What is Joint Broadcasting?
Joint broadcasting is a popular LVB feature of the year. It means apart from the original VJ, viewers and VJs from other rooms may participate in the LVB and perform video interaction with the VJ, to make the LVB more interesting.

<video style="width:830px;height:470px;"src=" http://200024424.vod.myqcloud.com/200024424_78c4dc2ebdf811e6ad39991f76a4df69.f30.mp4" controls="controls">
Sorry, your browser does not support online MP4 playback.
</video>
 
## From "Single Channel" to "Multiple Channels"

Let's start with ordinary LVB mode. Currently, a standard LVB process follows the mode shown in the figure below: The VJ end (TXLivePusher) pushes audio/video data to the cloud server, while multiple viewer ends (TXLivePlayer) pull the stream from the cloud and play the audio/video data.

![](//mc.qcloudimg.com/static/img/a9b501afb5555e5ab790bfe8ad5268d3/image.png)

To use joint broadcasting, a line in the opposite direction is necessary. Here, we suppose the **Viewer A** becomes a secondary VJ, then a new LVB stream will be added into the figure below (red dotted line):

![](//mc.qcloudimg.com/static/img/5579e666d8ba1ee80c753f15ffbff3d1/image.png)

> Tencent Cloud RTMP LVB feature supports **cross-room** joint broadcasting interaction, thus secondary VJ(s) may be the viewers in the original room, or a VJ from another room.

It seems simple to change from "single channel" to "multiple channels", besides, this is doable by using RTMP SDK. But it's difficult for the actual result to meet commercial standards because there are two critical problems:

- **Latency**
In standard LVB solutions, the latency between pushing end and player end is usually 2-3 seconds. However, in joint broadcasting scenarios, a harmonious communication is basically impossible if the latency between primary VJ and secondary VJ exceeds 1 second.

- **Echo**
In standard LVB solutions, the voice is one-way (VJ speaks to viewers) so there is no need for AEC (Acoustic Echo Cancellation). But in joint broadcasting scenarios, voice communication is two-way (or multi-way), if we don't implement AEC, the primary VJ's voice will be transmitted to secondary VJ's speakers, collected by microphone and then transmitted back to the primary VJ.

- **Stream mixing**
If the latency and echo problems are solved, the primary VJ can interact with the secondary VJ(s), but we still need to let the viewers watch the LVB before we can call it a success. Thus we need to mix the streams of multiple displays to present the pictures on viewer players.

## How to Reduce Latency?
To solve latency issues, we first need to understand the cause of latency.
![](//mc.qcloudimg.com/static/img/ddf657b4af791b3cb8b7ad2ed62f57be/image.png)
The main sources of latency in the entire linkage are marked by red markers in the figure above. In an LVB with a latency of around 3 seconds, 80% of the total latency was "contributed" by these three modules.

### 1. Encoding Module
- **Reason for latency:**
The main task for the encoding module is to further process the audio/video data pushed by the VJ. At the same time, this module also needs to worry about your demands regarding multiple resolutions (ultra high definition, high definition, standard definition) and multiple formats (such as HLS format suitable for web playback).

- **Solution:**
In joint broadcasting scenarios, if the linkages between primary VJ and secondary VJ(s) are all established using RTMP protocol, then the process does not need to involve the encoding cluster, eliminating such latency.

### 2. CDN Cluster
- **Reason for latency:**
CDN clusters are used to **distribute** data streams. If a VJ is located in Shanghai, he/she will be pushing to the server in Shanghai to ensure optimal upload quality. The problems is, what should viewers from Guilin or Harbin do? Do they pull streams from the Shanghai server too? That's apparently not a good idea. A feasible solution is to distribute the audio/video streams to Guilin and Harbin through CDN distribution cluster as necessary.

- **Solution:**
In joint broadcasting scenarios, if the connections between primary VJ and secondary VJ(s) don't go through the CDN cluster, then the latency between them can become much smaller. But how do we solve the distance problems? Suppose two VJs are interacting via joint broadcasting, one lives in Beijing, the other lives in Shenzhen. That's about 2,000 kilometers apart, how to establish a high-quality LVB linkage with low latency?

 Tencent Cloud uses **RtmpAcc Accelerated Nodes** as solution. This is an acceleration cluster with extremely low latency we specially established for joint broadcasting scenarios. The nodes are deployed among all major network nodes within China. These accelerated nodes are all connected through direct connections, and their only task is to provide reliable linkages with best quality and low latency to VJs in different regions and under different ISPs.
![](//mc.qcloudimg.com/static/img/323efdd148ffa623a34c6870a98a0b7e/image.png)
 
### 3. Player Buffer
- **Reason for latency:**
Every player will more or less buffer the videos they're playing, because it's impossible for the downlink network to stay completely smooth without jitter. A longer buffer length means less vulnerability against network jitter, smoother video playback, as well as a bigger video delay. In standard solutions, we configure player buffer length as 500 ms or 1000 ms or above.

- **Solution:**
 We need to configure a more radical buffer length in joint broadcasting scenarios, such as 200 ms. Meanwhile, **delay correction** is usually not available for players with standard open-source solutions, which means delay will increase as more stutters occur. In joint broadcasting scenarios, delay is not tolerable, thus delay correction and relevant radical policies are mandatory.

## Acoustic Echo Cancellation (AEC)
AEC is mandatory in two-way audio communication scenarios. We introduced AEC module to iOS and Android platforms starting from RTMP SDK 1.8.2, in order to prevent VJs from hearing his or her own voice from one second ago through their phone speakers.
![](//mc.qcloudimg.com/static/img/31fb2031789350bc88e886b75c03a02d/image.png)

As you can see from the figure above, the AEC module is hidden inside the RTMP SDK, so you don't need to do any extra coding.

## Multi-Stream Mixing
Tencent Cloud has two stream mixing technologies: client stream mixing and server stream mixing.
- **Client stream mixing**
Multi-instance playback became supported starting from RTMP SDK 1.8.2, which means multiple LVB URLs can be played concurrently and multiple video views can be overlaid. With this technology, client stream mixing can be achieved once the viewer end acquires multiple URLs from different VJs.

- **Server stream mixing**
Server stream mixing is a new solution developed recently. It is currently supported by the Internet. This solution is an extra module in the Tencent Cloud video encoding cluster, which directly mixes the streams of multiple videos into a single stream on the cloud, reducing downlink bandwidth load.

| Stream Mixing Solution | Advantage | Drawback | Key Factor | 
|---------|-----------|------|------------|
| Client stream mixing | More flexible interface arrangement is available since the performance on the viewer end is controlled by the App | Multiple streams in the downlink data resulting in higher bandwidth usage than server stream mixing method.  | The buffer of TXLivePlayer must use Speedy Mode + fixed buffer length of 1 second |
| Server stream mixing | Only one stream in the downlink data, effectively reducing bandwidth usage in LVB scenarios with high concurrency. | Currently, 1v3 stream mixing can be achieved at best.  | Need to call the stream mixing CGI and configure stream mixing parameters correctly | 

## Interfacing Guide
- [Joint Video Broadcasting (iOS)](https://cloud.tencent.com/document/product/454/8871)
- [Joint Video Broadcasting (Android)](https://cloud.tencent.com/document/product/454/8872)
