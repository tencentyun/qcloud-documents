## Overall Process
![](//mc.qcloudimg.com/static/img/2bbbdbba7baec530e40e05f15ea52fc0/image.gif)
1. VJ A pushes LVB stream with the LVB Code of streamA.
2. VJ B pushes LVB stream with the LVB Code of streamB.
3. VJ B sends a request to VJ A for joint broadcasting with his/her push URL streamB.
4. VJ A accepts the request by sending a response to VJ B. At the same time, VJ A pulls the stream of streamB for playback (player is set to PLAY_TYPE_LIVE_RTMP_ACC)
5. VJ B pulls the stream of streamA for playback (player is set to PLAY_TYPE_LIVE_RTMP_ACC)
6. VJ A (or VJ B) notifies the server to mix the streams as needed to allow viewers on CDN to watch the superimposed videos of two VJs.

## Overall Connection
### Step 1: Push by VJ A
VJ A gets the push hotlink protection URL streamA from your business backend, and then pushes streams with [TXLivePusher](https://cloud.tencent.com/document/product/454/7885).

Before joint broadcasting, the setVideoQuality of push needs to be switched to VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER, in which the Acoustic Echo Chancellor (AEC) is enabled to avoid echoing during joint broadcasting.

> setVideoQuality supports directly changing scenario mode in a push.

### Step 2: Push by VJ B
VJ B gets the push hotlink protection URL streamB from your business backend, and then pushes streams with [TXLivePusher](https://cloud.tencent.com/document/product/454/7885).

Before joint broadcasting, the setVideoQuality of push needs to be switched to VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER, in which the Acoustic Echo Chancellor (AEC) is enabled to avoid echoing during joint broadcasting.

> The resolution and bitrate of SUB_PUBLISHER should be lower than those of MAIN_PUBLISHER, because there is no need to use a high resolution for a small window.

### Step 3: Initiate a request for joint broadcasting
VJ B sends a request to VJ A for joint broadcasting. The request can be transferred by your business server or sent with Tencent Cloud IM solution. The push LVB Code of VJ B must be included in the request, otherwise VJ A cannot play VJ B's video stream.

> The source code of Mini LVB implements a handshake of the request for joint broadcasting with Tencent Cloud IM solution.

### Step 4: VJ A plays streamB
If VJ A accepts the request of VJ B, he/she gives a response to VJ B.

At this point, VJ A needs to use [TXLivePlayer](https://cloud.tencent.com/document/product/454/7886) to play the **low-delay** URL of streamB. Note: The playback of ordinary CDN URL is not allowed. The delay of the low-delay URL is within 500 ms, while the delay of CDN is generally over 2s. This means the CDN URL can only be used for watching ordinary videos, and cannot be used for joint broadcasting between VJs.

To achieve a low delay of about 500 ms during playback:

- **4.1 Add a [Hotlink Protection Signature](https://cloud.tencent.com/document/product/454/9875) to Playback URL**
Low-delay linkage uses the BGP resources of core data center of Tencent Cloud, which can only be accessed using the rtmp-liveplay URL with a hotlink protection signature. Therefore, both VJ A and VJ B must add the hotlink protection signature (txTime and txSecret ) to the playback URL for a low-delay playback. The following is a correct low-delay playback URL:
<table><tbody valign="middle"><tr><td height='80px'>rtmp://8888.liveplay.myqcloud.com/live/8888_streamB?bizid=8888&txSecret=xxxxx&txTime=5C2A3CFF</td></tr></tbody></table>

- **4.2 Use PLAY_TYPE_LIVE_RTMP_ACC playback mode of [TXLivePlayer](https://cloud.tencent.com/document/product/454/7886)**
In the LIVE_RTMP_ACC mode, the accurate delay control module built in the player is enabled, and the requirements for buffering and audio-video synchronization are higher than those of ordinary LVB.

### Step 5: VJ B plays streamA
After receiving the response of VJ A, VJ B begins to play the **low-delay** URL of streamA. Similarly, the following operations are needed:
- Add a hotlink protection signature to the playback URL

- Use [TXLivePlayer](https://cloud.tencent.com/document/product/454/7886) for the playback and set the playback mode to PLAY_TYPE_LIVE_RTMP_ACC.

### Step 6: Mix streams on the cloud
Low-delay linkage uses BGP resources of core data center of Tencent Cloud, thus allowing a low delay but consuming a high cost. Therefore, for viewers who only need to watch ordinary videos, it is recommended to use an ordinary CDN URL.

Tencent Cloud's stream mixing technology is about superimposing the video streams of one or more (1+3 is supported now) secondary VJs on the video stream of primary VJ (including audio mixing). This solution allows viewers to watch the joint broadcasting without changing the player.

For more information, please see [API for Stream Mixing on the Cloud](https://cloud.tencent.com/document/product/454/9859).

