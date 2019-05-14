### 1. What are Push, LVB and VOD?
- **Push**: This refers to the process in which VJs push local video and audio sources to Tencent Video Cloud servers. It is also known as "RTMP Publishing" in some cases.
- **LVB**: LVB video source is generated in real time. It is only meaningful if someone pushes the live streams. Once the VJ stops broadcasting, the LVB URL becomes invalid, and since the live streams are played in real time, no progress bar is displayed on the player during the playback.   
- **VOD**: VOD's video source is a file on cloud, which can be played at any time as long as it has not been deleted by the provider (such as Youku Tudou, iQIYI and Tencent Video). Since the entire video file is stored on the server, a progress bar is displayed during the playback.

### 2. What are the popular LVB protocols?
Three LVB protocols are commonly used: RTMP, FLV and HLS.
- **RTMP**: The RTMP protocol can be used for both push and live broadcasting. It involves breaking large video and audio frames into smaller fragments and transmitting them as small packets over the Internet. RTMP supports encryption, and thus provides a good privacy. However, the complicated fragmentation and reassembling bring about some unforeseeable stability issues to RTMP in case of a high-concurrency scenario. 
- **FLV**: FLV protocol is mainly implemented by Adobe Systems. It simply places header information to the large video and audio frame headers. This simplicity makes it a sophisticated format in terms of delay control and high-concurrency performance. Its only disadvantage is the limited capability on mobile browsers. However, it's suitable for LVB on mobile Apps.  
- **HLS**: HLS is a solution from Apple Inc. It splits videos into 5-10s fragments and manages them with an m3u8 index table. Since the videos downloaded on clients are complete data files with a 5-10s duration, the video smoothness can be ensured, but this leads to a great delay (typically the delay is around 10-30s when HLS is used). HLS is supported better than FLV on iPhone and most Android browsers, so it is often used for sharing URLs in QQ or WeChat's "Moments".
 ![](https://main.qcloudimg.com/raw/3dbcee6d6015660fd2d12b05829e22bd.png)

### 3. What are the popular VOD protocols?
Three VOD formats are commonly used: MP4, HLS and FLV.
-  **MP4**: MP4 is a classic format that is well supported on both mobile devices and PC browsers (The default browsers of iOS and most Android devices support MP4. On PC it can be played in a FLASH widget). However, MP4 video files are formatted in a complicated manner, which makes it time-consuming to process the files. Furthermore, the complexity of index table can cause a slow load when a long MP4 file (e.g. half an hour) is played online.
-  **HLS**: HLS is implemented by Apple Inc., and is well supported on mobile browsers. But on IE, the support for HLS depends on the secondary development of FLASH. (You're recommended to use Tencent Video Cloud's FLASH player). Unlike MP4 that has a slow indexing, HLS's compact m3u8 index structure allows a fast indexing, which makes it an ideal choice for VOD.
-  **FLV**: Implemented by Adobe Systems, FLV is the most popular wrapper format on live broadcasting platforms. On PC, it's well supported by FLASH. However, on mobile devices, it is only supported by the Apps which implement their players (or use this player). Most mobile browsers don't support FLV. Tencent Video Cloud uses FLV for LVB recording.
 ![](https://main.qcloudimg.com/raw/8192bcc0bb12ead16b7693b24749aa2d.png)

### 4. What are the popular push protocols?
Although RTMP is not commonly used in live broadcasting, but it is dominant in push service (pushing data from **VJ** to **servers**). Domestic video cloud services use RTMP as the main push protocol. Tencent Video Cloud SDK's first module is VJ push, so the SDK is also called RTMP SDK.

### 5. Which features and protocols are supported by the Tencent RTMP SDK?
Tencent Video Cloud RTMP SDK supports Push, LVB and VOD.
- **Push**: Supports **RTMP publishing protocol**, as well as features such as hardware acceleration, beauty filter, bandwidth adaption and resolution adjustment.
- **LVB**: Supports **FLV (recommended)** and RTMP protocols, as well as instant broadcasting optimization, auto delay control and highly adaptive hardware-decoding.
- **VOD**: Supports **online** or **local** VOD services for **MP4\HLS\FLV** files. Note: The earlier versions of SDK only support FLV-based VOD.

### 6. Is it mandatory to obtain the "License for Dissemination of Audio-Visual Programs through Information Network" for LVB?

Any applications that provide live broadcasting and other audio/video services over Internet are required to have the "License for Dissemination of Audio-Visual Programs through Information Network" issued by the relevant authority.
