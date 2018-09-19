## Reusing Existing UI
Video stitcher has a complicated interaction logic and thus its UI has a high complexity. Therefore, it is recommended to reuse the UI source codes from the SDK package. The UI-related source codes of the short video stitcher can be found under the videojoiner directory.
![image](https://mc.qcloudimg.com/static/img/56c9b39bef26c66449ca39ba14a4f588/short_video_joiner.png)

- TCVideoJoinerActivity is used to implement the video stitching list in the figure above, and supports the adjustment of sequence by dragging and dropping up and down.
- TCVideoJoinerPreviewActivity is used to preview the watching effect after video stitching.

## Implementing UI
If you do not want to reuse the UI-related codes in our package and decide to implement UI independently, you can perform interfacing by referring to the following guide:

### 1. Select Video Files  
Implement the file multi-selection feature independently

### 2. Set Preview View  
Video stitching requires the creation of TXVideoJoiner object. Similar to TXVideoEditer, the preview feature also needs a FrameLayout for preview provided by the upper layer:

```
//Prepare preview  View        
TXVideoEditConstants.TXPreviewParam param = new TXVideoEditConstants.TXPreviewParam();
param.videoView = mVideoView;
param.renderMode = TXVideoEditConstants.PREVIEW_RENDER_MODE_FILL_EDGE;

//Create TXUGCJoiner object and set preview view
TXVideoJoiner mTXVideoJoiner = new TXVideoJoiner(this);
mTXVideoJoiner.setTXVideoPreviewListener(this);
mTXVideoJoiner.initWithPreview(param);
// Configure the array (mVideoSourceList) of video files to be stitched, which are the files selected in the first step.
mTXVideoJoiner.setVideoPathList(mVideoSourceList);
```
After configuring the preview view and passing the array of video files to be stitched, you can start to play the preview. The stitching module provides a group of APIs for video playback preview:

- startPlay means video playback starts
- pausePlay manes video playback pauses
- resumePlay means video playback resumes

### 3. Generate Final Files
If you are satisfied with the preview, you can call the generation API to generate the stitched file:
```
mTXVideoJoiner.setVideoJoinerListener(this);
mTXVideoJoiner.joinVideo(TXVideoEditConstants.VIDEO_COMPRESSED_540P, mVideoOutputPath);
```
Specify the compression quality and output path during video stitching. You are notified of the output progress and result through the callback of TXVideoJoiner.TXVideoJoinerListener.

