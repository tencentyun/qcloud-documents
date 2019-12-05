## LVB Feature
- **RTMP-UDP Acceleration**
Tencent Cloud provides a standard RTMP UDP acceleration capability. When you use the RTMP push feature in the SDK to push to Tencent Cloud servers, you can enable the UDP acceleration, which can improve the push quality with a better network fluctuation resistance capability than the standard RTMP push, and can speed up the push. Thus, viewers can get a better LVB viewing experience with the reduced global stutter rate. The following is a set of results of a comparison test performed at the customer site:
![](https://mc.qcloudimg.com/static/img/12e966a39dc5eba5701cb2e310b16ccb/image.jpg)

- **Basic Beauty Filter**
In the thorough reconstruction of the basic beauty filter module (free), the original dermabrasion feature and the filter feature are greatly optimized and integrated. Thus the GPU usage is further reduced while the beauty effect is improved, so the device heating-up problem is relieved.
![](//mc.qcloudimg.com/static/img/aac647073cf0641141900e775e929418/image.png)
	
- **AI Effects**
The SDK commercial version realized a series of **beautifying effects** (such as face slimming, eyes beautifying, V-shaped face and nose re-shaping) and **dynamic stickers**, etc. in combination with Tencent YouTu Lab and Pitu.

- **LVB Joint Broadcasting**
The SDK integrates the TRAE acoustic processing component, the pride of Tencent Audio/Video Lab, for the in-depth optimization of LVB joint broadcasting based on the difference between LVB and the video chat scenario, and realized the real-time audio/video call technology which is more suitable for the joint broadcasting scenario.
  
## VOD Feature
- **Playback Speed Control**
The VOD player supports playback speed control. You can set the VOD playback speed, such as 0.5X, 1.0X, 1.2X, 2X, using the API `setRate` to speed up or slow down the playback.
![](https://mc.qcloudimg.com/static/img/8666305d62167cfb7c1e670d14fbd689/image.png)

- **Local Cache**
The VOD player supports the video cache to avoid extra traffic consumption in the second playback of the video played before. You can customize the cache size or the number of files using the API `config`.

- **Encrypted Playback**
The video encryption scheme is mainly used for such scenarios as online education, which need to protect the video copyright. It supports the encryption schemes specified by the HLS standard protocol, so this scheme has a strong universality.

- **Preloading**
When a video is in playback, the next video to be played is preloaded in the background, thus greatly improving the video switching experience when viewing a video. Preloading can also be used in the pre-roll ads scenario. Preloading the video to be played when playing an ad video is also a basic user experience requirement.


## UGSV Feature
- **Excellent Interface Interaction**
Compared to the video processing features which need professional audio/video experience, the UI implementation of the video processing is not very difficult, but it also takes lots of development workload to build a UGSV feature. This SDK provides a set of open source UI implementations while providing the basic video processing features to make you stand on a higher starting point and speed up the coming-out of the product.
![](https://mc.qcloudimg.com/static/img/12b5b35b03b820c5ececa4120e8fc33a/image.png)

- **Segmented Recording and Deletion**
With the `pauseRecord` and `resumeRecord` features of `TXUGCRecord`, a video recording process can be segmented into multiple segments. If the recording effect is not satisfied, you can delete the last segment using `deleteLastPart` instead of recording the entire video from the starting, thus greatly improving the use experience.

- **Fast Clipping and Stitching**
APIs for fast video clipping and stitching (`quickGenerateVideo` and `quickJoinVideo`) are provided for IOS. The video clipping and stitching can be completed within 1s.


