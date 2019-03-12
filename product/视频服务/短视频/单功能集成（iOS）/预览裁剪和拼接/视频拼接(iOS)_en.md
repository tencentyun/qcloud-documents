
## Reusing the Existing UI
Video stitcher has a complicated interaction logic and thus its UI has a high complexity. Therefore, it is recommended to reuse the UI source codes from the SDK package. The UI-related source codes of the short video stitcher can be found under the VideoJoiner directory.

![](//mc.qcloudimg.com/static/img/fc1ac59ce503b64b32ee0ece996e1765/image.jpg)

- VideoJoinerController is used to implement the video stitching list in the figure above, and supports the adjustment of sequence by dragging and dropping up and down.
- VideoJoinerController is used to implement every video fragment of the video stitching list.
- VideoEditPrevController is used to preview the watching effect after video stitching.

## Implementing UI
If you do not want to reuse the UI-related codes in our package and decide to implement UI independently, you can perform interfacing by referring to the following guide:
 
### 1. Select Video Files
As an open source library, QBImagePicker used in Demo implements file multi-selection feature. Related codes are displayed in MainViewController of Demo.

### 2. Set Preview View
Video stitching requires the creation of TXUGCJoiner object. Similar to TXUGCEditer, the preview feature also needs a UIView for preview provided by the upper layer:

```objective-c
//Prepare Preview View
TXPreviewParam *param = [[TXPreviewParam alloc] init];
param.videoView = _videoPreview.renderView;
param.renderMode = PREVIEW_RENDER_MODE_FILL_EDGE;

// Create TXUGCJoiner object and set preview view
TXUGCJoiner* _ugcJoin = [[TXUGCJoiner alloc] initWithPreview:param];
_ugcJoin.previewDelegate = _videoPreview;

// Configure the array (_composeArray) of video files to be stitched, which are the files selected in the first step.
[_ugcJoin setVideoPathList:_composeArray];
```

After configuring the preview view and passing the array of video files to be stitched, you can start to play the preview. The stitching module provides a group of APIs for video playback preview:

*  `startPlay`means video playback starts
*  `pausePlay`manes video playback pauses
*  `resumePlay`means video playback resumes

### 3. Generate Final Files
If you are satisfied with the preview, you can call the generation API to generate the stitched file:
```objective-c
_ugcJoin.joinerDelegate = self;
[_ugcJoin joinVideo:VIDEO_COMPRESSED_540P videoOutputPath:_outFilePath];
```

Specify the compression quality and output path during video stitching. You are notified of the output progress and result through the callback of `joinerDelegate`.
