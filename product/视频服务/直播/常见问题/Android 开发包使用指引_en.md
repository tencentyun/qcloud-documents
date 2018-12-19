## Push
Decompress the SDK package, enter Push directory, and then check how PublishViewController implements push:
1. Create a TXLivePush object (currently, this object has only a single instance).
2. Call startPreview method to preview the camera image.
3. Call setVideoQuality method to set image quality level. VIDEO_QUALITY_HIGH_DEFINITION is recommended for ordinary LVBs. 
3. Call startPush method to start push. Activate Tencent Cloud [LVB](https://console.cloud.tencent.com/live) service to obtain the push URL.
4. For advanced features such as beauty filter, watermark, pause image push at background, background music, microphone feedback and audio mixer, please see our [official documentation](https://cloud.tencent.com/document/product/454/7879).

## LVB and VOD
In LVB, the video source is the VJ pushing the live stream, while in VOD (Video On-demand), the video source is a video file on a server (e.g. Youku Tudou).

Decompress the SDK package, enter Play directory, and check how PlayViewController implements playback. PlayerViewController supports both LVB playback (without a progress bar on UI) and VOD playback (with a progress bar on UI):

1. Create a TXLivePlayer object (this object can have multiple instances, but each Player must have its own View).
2. Call setupVideoWidget method to set the UIView on which video image is rendered.
3. Call startPlay method to start playback. The protocol used depends on startPlay. Protocols starting with LIVE\_ are used for LVB, those with VOD\_ are for VOD, and those with LOCAL_VIDEO are for local videos.
4. For advanced features such as screen-shot, video capture (capture a part of the video and encode it as MP4), please see our [official documentation](https://cloud.tencent.com/document/product/454/7880).

## Joint Broadcasting with VJ
In a LVB, the viewers (or the VJs in other rooms) can have a *real-time video/audio chat** with the current VJ, and the **mixing multiple streams** is allowed on the server so that viewers can see multiple images. This is called "Joint Broadcasting".

- **Sample Codes**
Decompress the SDK package, enter directory LinkMic. The code under this directory shows how to construct a bi-directional or multi-directional real-time chat with the SDK.
 + LinkMicViewController - implements the main logic of the primary screen.
 + LinkMicPlayItem - implements the logic of the secondary screens.
 + StreamUrlScanner - adds URLs of new secondary screens.
 
- **Real-time Chat**
 + In a real-time chat, every user has one up-link (to push the user's audio and video to the cloud) and multiple down-links (to fetch other users' audio and video from the cloud).
 + The up-link is implemented by the TXLivePush module, and down-link by the TXLivePlayer module. In both cases, echo cancellation should be enabled (TXLivePushConfig::enableAEC).
 Both up-link and down-link use RTMP protocol. However, instead of fetching audio/video streams from ordinary CDNs, primary and secondary VJs all use the super link of our core IDC, with the average delay from the server to mobile phone being as low as tens of milliseconds.
 + The URLs of hyperlinks are constructed in a different way than those of ordinary CDNs. For more information, please see [official documentation](https://cloud.tencent.com/document/product/454/8871).

- **Mixing Multiple Streams**
 + You can use Tencent Cloud [API](https://cloud.tencent.com/document/product/454/8871#.E6.AD.A5.E9.AA.A4.E4.B8.89.EF.BC.9A.E5.90.AF.E5.8A.A8.E6.B7.B7.E6.B5.8110) to mix multiple video streams. Use the API parameters to set mixing options, such as the location of the secondary screen.

## Video Recording
Decompress the SDK package, enter VideoRecord directory to learn how to record videos.
1. Create a TXUGCRecord object. Use TXUGCSimpleConfig to set options such as short video quality and watermark.
2. Call startRecord method to start recording. Call stopRecord method to stop recording.
3. The recorded MP4 file and vedio cover image will be passed to TXVideoRecordListener callback.
4. Use TXUGCPublish to publish the video to the specified cloud platform.

For more information, please see our [official documentation](https://cloud.tencent.com/document/product/584/9367).


## Video Editing
Video editor has a complicated interactive logic and thus its UI has a high complexity. Therefore, it's recommended to reuse the UI source codes from the SDK package. The UI-related codes of the short video editor can be found under VideoEditor directory.

To customize the UI, please see our [official documentation](https://cloud.tencent.com/document/product/584/9375).


## Video Stitching
Video stitcher has a complicated interactive logic and thus its UI has a high complexity. Therefore, it's recommended to reuse the UI source codes from the SDK package. The UI-related codes of the short video stitcher can be found under VideoJoiner directory.

To customize the UI, please see our [official documentation](https://cloud.tencent.com/document/product/584/9370).

