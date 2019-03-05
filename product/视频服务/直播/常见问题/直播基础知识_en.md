
### 1. What are Push, LVB and VOD?
- **Push**
   This refers to the process in which VJs push local video and audio sources to Tencent Video Cloud servers. It is also known as "RTMP Publish" in some cases.

- **LVB**
	 LVB's video source is generated in real time, and only makes sense when someone pushes the LVB stream. Therefore, once the VJ stops broadcasting, the LVB URL will become invalid. Since the video is played in real time, no progress bar is displayed on the player during the LVB.
	 
- **VOD**
VOD's</font> video source is a file on cloud, which can be played at any time as long as it has not been deleted by the provider (such as Youku Tudou, iQIYI and Tencent Video). Since the entire video file is stored on the server, a progress bar will be displayed during the playback.

### 2. What are the popular LVB protocols?
Currently, there are three widely used LVB protocols: RTMP, FLV and HLS.
- **RTMP**
The multi-purpose RTMP protocol can be used for both push and LVB. Its core concept is to break large video and audio frames into smaller fragments, and transmit small packets over the Internet. RTMP supports encryption, and thus provides a good privacy. However, the complicated fragmentation and reassembling bring about some unforeseeable stability issues to RTMP in case of a high-concurrency environment.
	
- **FLV**
FLV protocol is mainly developed by Adobe Systems. It simply place header information to the large video and audio frame headers. This simplicity makes FLV a sophisticated format in terms of latency and high-concurrency performance. The only disadvantage of FLV is its limited supports on mobile browsers. However, it's suitable for LVB on mobile App.
	
- **HLS**
HLS is a solution from Apple Inc. It splits videos into small segments, each 5-10 seconds, and manages them with an m3u8 index. Since the videos downloaded on clients are complete data files with a 5-10s duration, the video smoothness can be ensured, but this leads to a great latency (typically the latency of HLS is around 10-30 seconds). Compared with FLV, HLS provides a better support on iPhone and most Android browsers, thus is commonly used for sharing URLs via QQ and in WeChat's "Moments".

 ![](//mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

### 3. What are the popular VOD protocols?
Currently, there are three widely used VOD formats: MP4, HLS and FLV.
-  **MP4**
MP4 is a classic format well supported on both mobile devices and PC browsers. (The default browser on iOS and most android devices support MP4. On PC it can be played in a FLASH widget). However, the complexity of MP4 video file structure makes it time-consuming to handle the file. Furthermore, the complexity of file index can cause a slow load when a long MP4 file (e.g. half an hour) is played online.

-  **HLS**
Launched by Apple Inc., HLS is well supported on mobile browsers. But on IE, the support for HLS depends on secondary development of FLASH. (You're recommended to use Tencent Video Cloud's FLASH player). Unlike MP4, HLS's compact m3u8 index structure allows a fast indexing, which makes it a good choice for VOD.

-  **FLV**
As a format launched by Adobe Systems, FLV currently is the most popular wrapper format on LVB platforms. On PC, it's well supported by FLASH. However, on mobile devices FLV is only supported by APPs which implement its player (or use this player). Most mobile browsers don't support FLV. Currently, Tencent Video Cloud uses FLV for LVB recording.
 ![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

### 4. What are the popular push protocols?
  Even though RTMP is not commonly used in LVB, it is the leading format in push service, i.e. pushing data from VJs to the servers. Currently, RTMP is the main push protocol employed by all domestic video cloud services. Because the first feature supported by Tencent Video Cloud SDK is VJ Push, the SDK is also called RTMP SDK.

### 5. Which features and protocols does Tencent RTMP SDK support?
  Tencent Video Cloud RTMP SDK supports push, LVB and VOD.
  - **Push** - The SDK supports RTMP publish protocol, as well as powerful features such as hardware acceleration, beauty filter, bandwidth adaption and video resolution adjustment.
  - **LVB** - The SDK supports FLV (recommended) and RTMP protocols, as well as instant broadcasting optimization, automatic delay control and highly adaptive hardware-decoding.
  - **VOD**. The SDK supports streaming MP4\HLS\FLV on-demand. Please note that the old versions of SDK support only FLV VOD.


