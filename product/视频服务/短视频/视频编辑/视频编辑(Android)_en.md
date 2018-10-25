# Short Video Editing Overview
Video editing includes video clipping acceleration, beauty filter, music mixing, caption adding and other features. We have implemented a set of UI source codes for reference and experience in the Demo of SDK package. The interface of each feature is as follows:

![](https://mc.qcloudimg.com/static/img/fe456c2f70519ec31eefc008f6e14791/androidedit1.png)

![](https://mc.qcloudimg.com/static/img/edc4f6add127d240259fc310bf40ddd6/androidedit2.png)
- Figure 1 is the interface for video clipping acceleration
- Figure 2 is the interface for filter adding
- Figure 3 is the interface for music accompaniment adding
- Figure 4-6 are the interfaces for caption adding

To compile and run the Demo, download the [complete Android package](https://cloud.tencent.com/document/product/454/7873) from Download Resources, decompress it and run the RTMPAndroidDemoSrc project. By clicking the video editing on the running main interface, you can select the video and experience the editing feature.

## 1. Reuse the Existing UI
Video editing has a complicated interaction logic and thus its UI has a high complexity. Therefore, it is recommended to reuse the UI source codes from the SDK package. During use, copy the following folder from Demo to your own project:

1. Codes under shortvideo/editor
2. VideoEditor resources under res/
3. "jar" and "so" under jniLibs/
4. Declare these Activities in AndroidManifest.xml, and declare the permissions

```
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

```
<activity
    android:name=".shortvideo.choose.TCVideoChooseActivity"
    android:screenOrientation="portrait"
    />
<activity
    android:name=".shortvideo.editor.TCVideoEditerActivity"
    android:screenOrientation="portrait">
```

## 2. Implement UI
If you do not want to reuse the UI-related codes in our package and decide to implement UI independently, you can perform interfacing by referring to the following guide:
### 1 Preview Image Group
You can get some basic information of a specified video file by using the **getVideoFileInfo** method of **TXVideoInfoReader**, and a specified number of preview images using **getSampleImages**:

```objective-c
// Get the information of video file
getVideoFileInfo(String videoPath){...}

// Pre-read the video file, and evenly generate "count" preview image groups
getSampleImages(int count, String videoPath, TXVideoInfoReader.OnSampleProgrocess listener)
```
In the package, TCVideoEditerActivity gets 10 thumbnails using getSampleImages to build a progress bar made up of video previews.

### 2 Effect Preview
Video editing provides a preview mode: **Interval Preview** (play a video clip within a certain time period "A<=>B" on a loop). You need to bind the SDK with a FrameLayout to display video images.

- **Bind FrameLayout**
  The initWithPreview function of TXVideoEditer is used to bind SDK with a FrameLayout to render video images. When binding, you need to specify one of the following two modes: **Adaptive** and **Fill**.
```
PREVIEW_RENDER_MODE_FILL_SCREEN - Fill pattern: the screen is filled as much as possible with no black edge left, so part of the images may be cut out.
PREVIEW_RENDER_MODE_FILL_EDGE - Adaptive pattern: the image is kept as complete as possible, but black edges may appear in case of inappropriate aspect ratio.
```

- **Interval Preview**
  The startPlayFromTime function of TXVideoEditer is used to play a video clip within a certain time period "A<=>B" on a loop.

### 3 Video Clipping
Operations in video editing are in conformity with the same principle: first set the operational instructions, and finally use generateVideo to execute all instructions in order, so as to avoid unnecessary quality loss due to repeated video compressions.

```objective-c
mTXVideoEditer.initWithPreview(param);
// Set the start time and end time of clipping
 mTXVideoEditer.setCutFromTime(mEditPannel.getSegmentFrom(), mEditPannel.getSegmentTo());
// ...
// Generate the final video file
mTXVideoEditer.setVideoGenerateListener(this);
mTXVideoEditer.generateVideo(TXVideoEditConstants.VIDEO_COMPRESSED_540P, mVideoOutputPath);
```
Specify the file compression quality and output path during output. You are notified of the output progress and result through the callback of `TXVideoEditer.TXVideoGenerateListener`.

### 4 Filter Effects
You can add filter effects to your videos such as whitening, romantic, fresh, etc. Demo offers 9 filter options, and you can also set the custom filters.
Call the **setFilter** method of **TXVideoEditer** to set filters:

```
void setFilter(Bitmap bmp)
```
"image" is the filter map. If it is set to nil, the filter effect is removed.

### 5 Audio Track Processing
You can add your favorite background music to the videos, and also select the start time and end time for music playback. If the time period of music playback is less than that of the video, the music is played on a loop until the video ends. In addition, you can also set the volume of both video and background music to get the desired sound synthesis.

The method to set background music is:
```
public int setBGM(String path);
```
"mBGMPath" is the music file path, Returned value: 0: Successful; other values: Failed, for example: unsupported audio format.
The method to set the start/end time of BGM is:
```
public void setBGMStartTime(long startTime, long endTime);
```
The start/end time is set in millisecond.

The method to set the volume of video and background music is:
```
public void setVideoVolume(float volume);
public void setBGMVolume(float volume);
```
"volume" indicates the sound level. Value range: 0 (mute) to 1 (original sound).

Demo example:
```
mTXVideoEditer.setBGM(mBGMPath);
mTXVideoEditer.setBGMStartTime(startTime, endTime);
mTXVideoEditer.setBGMVolume(0.5f);
mTXVideoEditer.setVideoVolume(0.5f);
```
### 6. Video Acceleration
You can set the video playback acceleration to implement the effect of fast playback.

The method to set video playback acceleration is:

```
public void setSpeedLevel(float speed);
```
"level" indicates the acceleration level. Value range: 1 (original speed) to 4 (four times the speed).

Demo example:
```
mTXVideoEditer.setSpeedLevel(2.0f);
```
### 7 Set Watermark
You can set the watermark for a video, and specify its location.

The method to set watermark is:

```
public void setWaterMark(Bitmap waterMark, TXVideoEditConstants.TXRect rect);
```
"waterMark" indicates the watermark image. "rect" is the normalized frame relative to the video image. The value ranges of x, y, width and height of frame are all from 0 to 1.

Demo example:
```
TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
rect.x = 0.5f;
rect.y = 0.5f;
rect.width = 0.5f;
mTXVideoEditer.setWaterMark(mWaterMarkLogo, rect);
```
### 8 Set Tail Watermark

You can set the tail watermark for a video, and specify its location.

The method to set tail watermark is:

```
setTailWaterMark(Bitmap tailWaterMark, TXVideoEditConstants.TXRect txRect, int duration);
```

"tailWterMark" indicates the tail watermark image. "txRect" is the normalized txRect relative to the video image, and the value ranges of x, y and width of txRect are all from 0 to 1. "duration" means the duration of watermark (in sec).

Demo example: Set the watermark in the middle of the tail for 3 seconds.

```
Bitmap tailWaterMarkBitmap = BitmapFactory.decodeResource(getResources(), R.drawable.tcloud_logo);
TXVideoEditConstants.TXRect txRect = new TXVideoEditConstants.TXRect();
txRect.x = (mTXVideoInfo.width - tailWaterMarkBitmap.getWidth()) / (2f * mTXVideoInfo.width);
txRect.y = (mTXVideoInfo.height - tailWaterMarkBitmap.getHeight()) / (2f * mTXVideoInfo.height);
txRect.width = tailWaterMarkBitmap.getWidth() / (float) mTXVideoInfo.width;
mTXVideoEditer.setTailWaterMark(tailWaterMarkBitmap, txRect, 3);
```

### 9 Subtitle Overlay

Adding subtitles to videos is supported. You can add subtitles for each video frame, or set the start/end time of a video for each subtitle. All of the subtitles form a subtitle list. You can pass the subtitle list to SDK, and then SDK automatically overlays the video and subtitle at the right time.

The method to set subtitle is:

```
public void setSubtitleList(List<TXVideoEditConstants.TXSubtitle> subtitleList);

//The parameters of TXSubtitle are as follows:
public final static class TXSubtitle {
		public Bitmap titleImage;                                 // Subtitle image
		public TXRect frame;                                      // Subtitle frame
		public long startTime;                                    // Subtitle start time (in ms)
		public long endTime;                                      // Subtitle end time (in ms)
}

public final static class TXRect {
		public float x;
		public float y;
		public float width;
}
```
Note:
titleImage: Subtitle image. If the upper layer uses TextView or other controls, covert the control into Bitmap first. For more information, please see the sample codes of Demo.
frame: Subtitle frame. Please note that this frame is the one relative to the rendering view (the view specified during initWithPreview) frame. For more information, please see the sample codes of Demo.
startTime: The start time of subtitle.
endTime: The end time of subtitle.

Since the UI logic of subtitle is complicated, we already have a set of implementation methods in Demo layer. You can directly use Demo implementation as a reference, so as to greatly reduce the access cost.

Demo example:
```
mSubtitleList.clear();
for (int i = 0; i < mWordInfoList.size(); i++) {
    TCWordOperationView view = mOperationViewGroup.getOperationView(i);
    TXVideoEditConstants.TXSubtitle subTitle = new TXVideoEditConstants.TXSubtitle();
    subTitle.titleImage = view.getRotateBitmap(); //Obtain Bitmap
    TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
    rect.x = view.getImageX(); // Obtain the x coordinate of the relative parent view
    rect.y = view.getImageY(); // Obtain the y coordinate of the relative parent view
    rect.width = view.getImageWidth(); // Picture width
    subTitle.frame = rect;
    subTitle.startTime = mWordInfoList.get(i).getStartTime(); // Set the start time
    subTitle.endTime = mWordInfoList.get(i).getEndTime();	// Set the end time
    mSubtitleList.add(subTitle);
}
mTXVideoEditer.setSubtitleList(mSubtitleList); // Set the subtitle list
```

