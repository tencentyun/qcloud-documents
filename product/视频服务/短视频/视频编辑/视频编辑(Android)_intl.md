Video editing supports video clipping, time effects (slow motion, reverse, repeated playback), filter effects (dynamic light-wave, darkness and phantom, soul out, cracked screen), filter styles (artistic, tender, blue), music mixing, dynamic stickers, static stickers, bubble subtitles and other features. We have implemented a set of UI source codes for reference and experience in the Demo of SDK package. The interface of each feature is as follows:

![](https://mc.qcloudimg.com/static/img/c6e09fde931290f5ffb103a9c9c5b5e1/90F32A4D-CD14-4A9D-A9C4-14EEF31E8F7C.png)
![](https://mc.qcloudimg.com/static/img/2ddfddb8a48a0dff65f11987bc085600/50BB2E7D-F46F-41B2-8E38-F5080DA5BDF6.png)

- Figure 1 is the interface for video clipping
- Figure 2 is the interface for time effects
- Figure 3 is the interface for dynamic filter
- Figure 4 is the interface for beauty filter
- Figure 5 is the interface for background music
- Figure 6 is the interface for static and dynamic stickers
- Figure 7 is the interface for bubble subtitles


To compile and run the Demo, download the [complete Android package](https://cloud.tencent.com/document/product/454/7873) from Download Resources, decompress it and run the Demo project. By clicking the video editing on the running main interface, you can select the video and experience the editing feature.
The code of the editing feature for Android is placed under the package name com.tencent.liteav.demo.shortvideo. Where, choose.TCVideoChooseActivity is the interface for local video list; editor.TCVideoPreprocessActivity is the interface for video preprocessing; TCVideoEditerActivity is the interface for video editing; editor.bgm package is used to implement background music; editor.bubble package is used to implement bubble subtitles; editor.cutter package is used to implement video clipping; editor.filter package is used to implement static filter; editor.motion package is used to implement dynamic filter; editor.paster package is used to implement dynamic/static stickers; and editor.time package is use to implement time effect.

## Reusing Existing UI
Video editing has a complicated interaction logic and thus its UI has a high complexity. Therefore, it is recommended to reuse the UI source code from the SDK package. During use, copy the following folder from Demo to your own project:

1. Code under shortvideo/editor
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
    android:name=".shortvideo.editor.TCVideoPreprocessActivity"
        android:launchMode="singleTop"
    android:screenOrientation="portrait" />
<activity
    android:name=".shortvideo.editor.TCVideoEditerActivity"
    android:screenOrientation="portrait">
<activity
    android:name=".shortvideo.editor.paster.TCPasterActivity"
        android:screenOrientation="portrait" />
<activity
    android:name=".shortvideo.editor.bubble.TCWordEditActivity"
    android:windowSoftInputMode="adjustResize|adjustPan"
    android:screenOrientation="portrait" />
```

## Implementing UI
If you do not want to reuse the UI-related codes in our package and decide to implement UI independently, you can perform interfacing by referring to the following guide:
### 1. Preview Image Group
You can get some basic information of a specified video file by using the **getVideoFileInfo** method of **TXVideoInfoReader**, and a specified number of preview images using **getSampleImages**:

```objective-c
// Get the information of video file
getVideoFileInfo(String videoPath){...}

//Pre-read the video file, and evenly generate "count" preview image groups
getSampleImages(int count, String videoPath, TXVideoInfoReader.OnSampleProgrocess listener)
//Or call this API
getSampleImage(int count, String videoPath)
```
In the package, TCVideoEditerActivity gets 10 thumbnails using getSampleImages to build a progress bar made up of video previews.

### 2. Effect Preview
Video editing provides a preview mode: **Interval Preview** (play a video clip within a certain time period "A<=>B" on a loop). You need to bind the SDK with a FrameLayout to display video images.

- **Bind FrameLayout**
  The initWithPreview function of TXVideoEditer is used to bind SDK with a FrameLayout to render video images. When binding, you need to specify one of the following two modes: **Adaptive** and **Fill**.
```
PREVIEW_RENDER_MODE_FILL_SCREEN - Fill pattern: the screen is filled as much as possible with no black edge left, so part of the images may be cut out.
PREVIEW_RENDER_MODE_FILL_EDGE  -Adaptive pattern: the image is kept as complete as possible, but black edges may appear in case of inappropriate aspect ratio.
```

- **Interval Preview**
  The startPlayFromTime function of TXVideoEditer is used to play a video clip within a certain time period "A<=>B" on a loop.

### 3. Video Clipping
Operations in video editing are in conformity with the same principle: first set the operational instructions, and finally use generateVideo to execute all instructions in order, so as to avoid unnecessary quality loss due to repeated video compressions.

```objective-c
mTXVideoEditer.initWithPreview(param);
//Set the start time and end time of clipping
mTXVideoEditer.setCutFromTime(mEditPannel.getSegmentFrom(), mEditPannel.getSegmentTo());
// ...
//Generate the final video file
mTXVideoEditer.setVideoGenerateListener(this);
mTXVideoEditer.generateVideo(TXVideoEditConstants.VIDEO_COMPRESSED_540P, mVideoOutputPath);
```
Specify the file compression quality and output path during output. You are notified of the output progress and result through the callback of `TXVideoEditer.TXVideoGenerateListener`.
>Note: Create an empty file outside the path of the original video as the output file path, and pass in the absolute path. Do not use the same path as the original video.

### 4. Beauty Filter
You can add filter effects to your videos such as whitening, romantic, fresh, etc. Demo offers 9 filter options, and you can also set the custom filters.
Call the **setFilter** method of **TXVideoEditer** to set filters:

```
void setFilter(Bitmap bmp)
```
"image" is the filter map. If it is set to nil, the filter effect is removed.

### 5. Audio Track Processing
You can add your favorite background music to the videos, and also select the start time and end time for music playback. If the time period of music playback is less than that of the video, the music is played on a loop until the video ends. In addition, you can also set the volume of both video and background music to get the desired sound synthesis.

The method to set background music is:
```
public int setBGM(String path);
```
"mBGMPath" is the music file path, Returned value: 0: successful; other values: failed, for example, unsupported audio format.

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

Set the start time of background music in the video
```
public void setBGMAtVideoTime(long videoStartTime);
```

Set whether background music is looped: true - on a loop, false - no loop
```
public void setBGMLoop(boolean looping);
```

Demo:
```
mTXVideoEditer.setBGM(mBGMPath);
mTXVideoEditer.setBGMStartTime(startTime, endTime);
mTXVideoEditer.setBGMVolume(0.5f);
mTXVideoEditer.setVideoVolume(0.5f);
```
### 6. Set Watermark
You can set the watermark for a video, and specify its location.

The method to set watermark is:
```
public void setWaterMark(Bitmap waterMark, TXVideoEditConstants.TXRect rect);
```
"waterMark" indicates the watermark image. "rect" is the normalized frame relative to the video image. The value ranges of x, y, width and height of frame are all from 0 to 1.

Demo:
```
TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
rect.x = 0.5f;
rect.y = 0.5f;
rect.width = 0.5f;
mTXVideoEditer.setWaterMark(mWaterMarkLogo, rect);
```
### 7. Set Tail Watermark
You can set the tail watermark for a video, and specify its location.
The method to set tail watermark is:

```
setTailWaterMark(Bitmap tailWaterMark, TXVideoEditConstants.TXRect txRect, int duration);
```

"tailWterMark" indicates the tail watermark image. "txRect" is the normalized txRect relative to the video image, and the value ranges of x, y and width of txRect are all from 0 to 1. "duration" means the duration of watermark (in sec).
Demo: Set the watermark in the middle of the tail for 3 seconds.
```
Bitmap tailWaterMarkBitmap = BitmapFactory.decodeResource(getResources(), R.drawable.tcloud_logo);
TXVideoEditConstants.TXRect txRect = new TXVideoEditConstants.TXRect();
txRect.x = (mTXVideoInfo.width - tailWaterMarkBitmap.getWidth()) / (2f * mTXVideoInfo.width);
txRect.y = (mTXVideoInfo.height - tailWaterMarkBitmap.getHeight()) / (2f * mTXVideoInfo.height);
txRect.width = tailWaterMarkBitmap.getWidth() / (float) mTXVideoInfo.width;
mTXVideoEditer.setTailWaterMark(tailWaterMarkBitmap, txRect, 3);
```
### 8. Video Preprocessing
To implement the filter effects and time effects (including reverse, repeated playback, slow motion), you need to preprocess video.
After preprocessing, you can accurately seek to each time point of the video and view the corresponding image. Preprocessing can also accurately generate the video thumbnail of the current time point.

1. Generate an accurate thumbnail:
```
public void setThumbnail(TXVideoEditConstants.TXThumbnail thumbnail);

//TXThumbnailParameters are as follows:
public final static class TXThumbnail{
    public int count;        // Number of thumbnails
    public int width;        //Thumbnail width
    public int height;      //Thumbnail height
}
```
Note:
- The **setTumbnail** method must be called before using the **processVideo** method to generate an accurate thumbnail.
- Do not set the width and height of the video as that of the thumbnail, because the scaling implemented in SDK is more efficient.

2. Perform preprocessing:

```
//Preprocessing method
public void processVideo();

//Set video preprocessing callback
public void setVideoProcessListener(TXVideoProcessListener listener);

```
3. Accurately seek to each time point of the preprocessed video:

```
public void previewAtTime(long timeMs);
```

Demo:

```
int thumbnailCount = (int) mTXVideoEditer.getTXVideoInfo().duration / 1000;  //Number of thumbnails generated depending on video duration

TXVideoEditConstants.TXThumbnail thumbnail = new TXVideoEditConstants.TXThumbnail();
thumbnail.count = thumbnailCount;
thumbnail.width = 100;
thumbnail.height = 100;

mTXVideoEditer.setThumbnail(thumbnail);  //Set preprocessed thumbnails
mTXVideoEditer.setThumbnailListener(mThumbnailListener);

mTXVideoEditer.setVideoProcessListener(this);
mTXVideoEditer.processVideo();          //Perform preprocessing
```

### 9. Filter Effects
You can add multiple filter effects to your videos. Four types of filter effects are supported. You can also set the start time and end time in the video for each filter effect. If multiple filter effects are set at the same time point, the SDK uses the last filter effect as the current filter effect.

The method to set filter effects is:
```
public void startEffect(int type, long startTime);
public void stopEffect(int type, long endTime)

//The filter effect type (type parameter), which is defined in the constant TXVideoEditConstants:
TXEffectType_SOUL_OUT          - Filter effect 1
TXEffectType_SPLIT_SCREEN      - Filter effect 2
TXEffectType_DARK_DRAEM        - Filter effect 3
TXEffectType_ROCK_LIGHT        - Filter effect 4

public void deleteLastEffect();
public void deleteAllEffect();
```
Call deleteLastEffect() to delete the last filter effect.
Call deleteAllEffect() to delete all filter effects.


Demo:
Apply the first filter effect between 1-2s, apply the second filter effect between 3-4s, and remove the filter effect set for 3-4s.

```
//Apply the first filter effect between 1-2s
mTXVideoEditer.startEffect(TXVideoEditConstants.TXEffectType_SOUL_OUT, 1000);
mTXVideoEditer.stopEffect(TXVideoEditConstants.TXEffectType_SOUL_OUT, 2000);
//Apply the second filter effect between 3-4s
mTXVideoEditer.startEffect(TXVideoEditConstants.TXEffectType_SPLIT_SCREEN, 3000);
mTXVideoEditer.stopEffect(TXVideoEditConstants.TXEffectType_SPLIT_SCREEN, 4000);
//Remove the filter effect set for 3-4s
mTXVideoEditer.deleteLastEffect();
```
### 10. Slow/Fast Motion
You can slow down/speed up the playback of multiple video fragments. The method to set slow/fast playback is:

```
public void setSpeedList(List speedList)；

//TXSpeed's parameters are as follows:
public final static class TXSpeed {
    public int speedLevel;                                    // Speed level
    public long startTime;                                    // Start time
    public long endTime;                                      // End time
}

// The following speed levels defined in the constant TXVideoEditConstants are supported:
SPEED_LEVEL_SLOWEST    -Very slow
SPEED_LEVEL_SLOW        -Slow
SPEED_LEVEL_NORMAL      - Normal
SPEED_LEVEL_FAST        - Fast
SPEED_LEVEL_FASTEST    - Very fast
```

Demo:
```
//SDK supports changing speed of multiple video fragments. This DEMO only shows the slow playback of a video fragment.
List list = new ArrayList<>(1);
TXVideoEditConstants.TXSpeed speed = new TXVideoEditConstants.TXSpeed();
speed.startTime = startTime;                                //Start time
speed.endTime = mTXVideoEditer.getTXVideoInfo().duration;  //End time
speed.speedLevel = TXVideoEditConstants.SPEED_LEVEL_SLOW;  //Slow
//Add to the list of speeds for fragment playback
list.add(speed);

mTXVideoEditer.setSpeedList(list);
```
### 11. Reverse
You can play videos in reverse order. Call **setReverse(true)** to start a reverse playback, and call **setReverse(false)** to end the reverse playback.
Note: You do not need to call **setTXVideoReverseListener()** to monitor whether the reverse playback is completed for the first time in the new version of SDK compared to the old version.

Demo:
```
mTXVideoEditer.setTXVideoReverseListener(mTxVideoReverseListener);
mTXVideoEditer.setReverse(true);
```

### 12. Repeated Playback
You can set the repeated playback of a video frame, but the sound will not be played repeatedly. On Android, only one video frame is allowed to be played repeatedly for three times.
Call **setRepeatPlay(null)** to cancel the repeated playback set previously.

Set repeated playback:
```
public void setRepeatPlay(List repeatList);

//TXRepeat's parameters are as follows:
public final static class TXRepeat {
    public long startTime;              //Start time (in ms) of repeated playback
    public long endTime;                //End time (in ms) of repeated playback
    public int  repeatTimes;            //Number of times for repeated playback
}
```

Demo:
```
long currentPts = mVideoProgressController.getCurrentTimeMs();

List repeatList = new ArrayList<>();
TXVideoEditConstants.TXRepeat repeat = new TXVideoEditConstants.TXRepeat();
repeat.startTime = currentPts;
repeat.endTime = currentPts + DEAULT_DURATION_MS;
repeat.repeatTimes = 3;  //A video frame can only be played repeatedly for 3 times
repeatList.add(repeat);  //Only a video frame within a certain time period can be played repeatedly
mTXVideoEditer.setRepeatPlay(repeatList);
```

### 13. Static/Dynamic Stickers
You can set static or dynamic stickers for your video.
Set a static sticker:

```
public void setPasterList(List pasterList);

//TXPaster's parameters are as follows:
public final static class TXPaster {
    public Bitmap pasterImage;                                //Sticker image
    public TXRect frame;                                      //Sticker frame (the coordinates of the frame here are relative to those of the rendering view)
    public long startTime;                                    //Start time of sticker (in ms)
    public long endTime;                                      //End time of sticker (in ms)
}

```

Set a dynamic sticker:

```
public void setAnimatedPasterList(List animatedPasterList);

//TXAnimatedPaster's parameters are as follows:
public final static class TXAnimatedPaster {
    public String animatedPasterPathFolder;                  //Address of the dynamic sticker image
    public TXRect frame;                                      //Dynamic sticker frame (the coordinates of the frame here are relative to those of the rendering view)
    public long startTime;                                    //Start time of dynamic sticker (in ms)
    public long endTime;                                      //End time of dynamic sticker (in ms)
    public float rotation;
}
```
Demo:

```
List animatedPasterList = new ArrayList<>();
List pasterList = new ArrayList<>();
for (int i = 0; i < mTCLayerViewGroup.getChildCount(); i++) {
    PasterOperationView view = (PasterOperationView) mTCLayerViewGroup.getOperationView(i);
    TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
    rect.x = view.getImageX();
    rect.y = view.getImageY();
    rect.width = view.getImageWidth();
    TXCLog.i(TAG, "addPasterListVideo, adjustPasterRect, paster x y = " + rect.x + "," + rect.y);

    int childType = view.getChildType();
    if (childType == PasterOperationView.TYPE_CHILD_VIEW_ANIMATED_PASTER) {
        TXVideoEditConstants.TXAnimatedPaster txAnimatedPaster = new TXVideoEditConstants.TXAnimatedPaster();

        txAnimatedPaster.animatedPasterPathFolder = mAnimatedPasterSDcardFolder + view.getPasterName() + File.separator;
        txAnimatedPaster.startTime = view.getStartTime();
        txAnimatedPaster.endTime = view.getEndTime();
        txAnimatedPaster.frame = rect;
        txAnimatedPaster.rotation = view.getImageRotate();

        animatedPasterList.add(txAnimatedPaster);
        TXCLog.i(TAG, "addPasterListVideo, txAnimatedPaster startTimeMs, endTime is : " + txAnimatedPaster.startTime + ", " + txAnimatedPaster.endTime);
    } else if (childType == PasterOperationView.TYPE_CHILD_VIEW_PASTER) {
        TXVideoEditConstants.TXPaster txPaster = new TXVideoEditConstants.TXPaster();

        txPaster.pasterImage = view.getRotateBitmap();
        txPaster.startTime = view.getStartTime();
        txPaster.endTime = view.getEndTime();
        txPaster.frame = rect;

        pasterList.add(txPaster);
        TXCLog.i(TAG, "addPasterListVideo, txPaster startTimeMs, endTime is : " + txPaster.startTime + ", " + txPaster.endTime);
    }
}

mTXVideoEditer.setAnimatedPasterList(animatedPasterList);  //Set a dynamic sticker
mTXVideoEditer.setPasterList(pasterList);                  //Set a static sticker
```

#### How to customize dynamic stickers?
Dynamic sticker is designed to insert **a set of images** into video frames at **specified intervals** in **a certain order** to produce a dynamic sticker effect.

##### Encapsulation Format
Take a dynamic sticker in Demo as an example:
```
{
  "name":"glass",                        // Sticker name
  "count":6,                             // Number of stickers
  "period":480,                          // Playback period: Time taken to play a dynamic sticker (in ms)
  "width":444,                           // Sticker width
  "height":256,                          // Sticker height
  "keyframe":6,                          // Key image that can represent the dynamic sticker
  "frameArray": [                        //Collection of all images
                 {"picture":"glass0"},
                 {"picture":"glass1"},
                 {"picture":"glass2"},
                 {"picture":"glass3"},
                 {"picture":"glass4"},
                 {"picture":"glass5"}
               ]
}
```
SDK obtains the config.json of dynamic sticker, and displays the dynamic sticker in the format defined in json.

>**Note: This encapsulation format is used to describe the dynamic sticker as required by SDK.**

### 14. Bubble Subtitles
Adding bubble subtitles to videos is supported. You can add bubble subtitles for each video frame, or set the start/end time of a video for each subtitle. All of the subtitles form a subtitle list. You can pass the subtitle list to SDK, and then SDK automatically overlays the video and subtitle at the right time.

The method to set bubble subtitles is:
```
public void setSubtitleList(List subtitleList);

//TXSubtitle 's parameters are as follows:
public final static class TXSubtitle {
        public Bitmap titleImage;                                //Subtitle image
        public TXRect frame;                                      //Subtitle frame
        public long startTime;                                    //Start time of subtitle (in ms)
        public long endTime;                                      //End time of subtitle (in ms)
}

public final static class TXRect {
        public float x;
        public float y;
        public float width;
}
```
Where:
titleImage: Subtitle image. If the upper layer uses TextView or other controls, covert the control into Bitmap first. For more information, please see the sample code of Demo.
frame: Subtitle frame. Please note that this frame is the one relative to the rendering view (the view specified during initWithPreview) frame. For more information, please see the sample code of Demo.
startTime: The start time of subtitle.
endTime: The end time of subtitle.

Since the UI logic of subtitle is complicated, we already have a set of implementation methods in Demo layer. You can directly use Demo implementation as a reference to greatly reduce your access cost.

Demo:
```
mSubtitleList.clear();
for (int i = 0; i < mWordInfoList.size(); i++) {
    TCWordOperationView view = mOperationViewGroup.getOperationView(i);
    TXVideoEditConstants.TXSubtitle subTitle = new TXVideoEditConstants.TXSubtitle();
    subTitle.titleImage = view.getRotateBitmap();  //Obtain Bitmap
    TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
    rect.x = view.getImageX();        // Obtain the x coordinate of the relative parent view
    rect.y = view.getImageY();        // Obtain the y coordinate of the relative parent view
    rect.width = view.getImageWidth(); // Image width
    subTitle.frame = rect;
    subTitle.startTime = mWordInfoList.get(i).getStartTime();  //Set the start time
    subTitle.endTime = mWordInfoList.get(i).getEndTime();      //Set the end time
    mSubtitleList.add(subTitle);
}
mTXVideoEditer.setSubtitleList(mSubtitleList); //Set the subtitle list
```

#### How to customize bubble subtitles?
Parameters required for bubble subtitles
* Size of text area: top, left, right, bottom
* Default font size
* Width and height

**Note: The above parameters are measured in px**

##### Encapsulation Format
Since bubble subtitle comes with multiple parameters, we recommend that you encapsulate relevant parameters at the Demo layer, for example, in .json format used in Tencent Cloud Demo.

```
{
  "name":"boom",     //Name of bubble subtitle
  "width": 376,      //Width
  "height": 335,     //Height
  "textTop":121,     //Top margin of text area
  "textLeft":66,     //Left margin of text area
  "textRight":69,    // Right margin of text area
  "textBottom":123,  // Bottom margin of text area
  "textSize":40      //Font size
}
```
**Note: The encapsulation format can be customized, which is not specified by SDK.**

##### How to process a long subtitle?
If a subtitle is too long, how to merge it with a bubble to realize aesthetic effect?

We provide an automatic layout control in the Demo. If the subtitle with the current font size is too long, the control automatically reduces the font size until the bubble can accommodate all characters in the subtitle.

You can also modify the source code of the relevant control to meet your business needs.

### 15. Custom Video Output
Set the compression resolution and the output path of the generated video.
```
public void generateVideo(int videoCompressed, String videoOutputPath) 
```
The parameter videoCompressed can be set as a constant in TXVideoEditConstants.
```
VIDEO_COMPRESSED_360P - compressed to 360P resolution (360*640)
VIDEO_COMPRESSED_480P - compressed to 480P resolution (640*480)
VIDEO_COMPRESSED_540P - compressed to 540P resolution (960*540)
VIDEO_COMPRESSED_720P - compressed to 720P resolution (1280*720)
```
The resolution of the source video is used if it is less than the configured constant.
If the resolution of the source video is greater than the configured constant, compress the video to the appropriate resolution.

Custom video bitrates are supported. The recommended bitrate range is 600-12,000 Kbps. If the bitrate is set, SDK will first select this bitrate for video compression. Note: the bitrate should not be too large or too small. Large bitrate results in large video, and small bitrate makes video unclear.
```
public void setVideoBitrate(int videoBitrate);
```

### 16. Release
When you no longer use the mTXVideoEditer object, be sure to call **releasee()** to release it.

