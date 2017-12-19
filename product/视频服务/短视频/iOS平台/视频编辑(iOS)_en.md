## Overview
Video editing includes video clipping acceleration, beauty filter, music mixing, caption adding and other features. We have implemented a set of UI source codes for reference and experience in the Demo of SDK package. The interface of each feature is as follows:

![](//mc.qcloudimg.com/static/img/c89588c66500984f5ed790a1a25696cc/IOSVideoEditIOS.jpg)

![](//mc.qcloudimg.com/static/img/304285e91495e5fa463e8512411b6185/IOSVideoEditsubtitle.jpg)
Figure 1 is the interface for video clipping acceleration. Figure 2 is the interface for filter adding. Figure 3 is the interface for music accompaniment adding. Figure 4-6 are the interfaces for caption adding.

To compile and run the Demo, download the [SDK package](https://cloud.tencent.com/document/product/584/9366) from Download Resources, decompress it and run the Demo project RTMPiOSDemo.xcodeproj. By clicking the video editing on the running main interface, you can select the video and experience the editing feature.

## Reusing the Existing UI
Video editing has a complicated interaction logic and thus its UI has a high complexity. Therefore, it is recommended to reuse the UI source codes from the SDK package. During use, copy the following folder from Demo to your own project: 
1. VideoEditor (code)
2. VideoEditor and FilterResource.bundle under Resource (resources)
3. Common and Third (the common code that the whole Demo relies on. You can delete or modify it based on your own needs)

UI source code description
Since each interface component in the source code is independent, you can modify and process the interface according to your product demands.
Description of main interface components:
1. VideoCutView: The video clipping interface, including video clipping and acceleration features. To customize clipping interface, you can modify or replace this class.
2. FilterSettingView: The video filtering interface, including 9 filters. To make modifications, you can change or replace this class.
3.MusicMixView: The video sound mixing interface, including music file selection, music information display, music length cutting, volume adjustment of original and accompanying sounds. To make modifications, you can change or replace this class.
4. TextAddView: The video subtitle adding interface, which only contains the button to redirect to VideoTextViewController. In practice, you can add subtitles or perform other operations in VideoTextViewController. This interface can be modified or removed as need.
5. VideoTextField: The subtitle input component, including subtitle text input, subtitle dragging, enlargement, rotation, deletion, adding subtitle background styles. This component in VideoTextViewController is mainly used to add and delete subtitles.

VideoEditViewController is only used to join these interfaces and the preview interface "VideoPreview" together, and handle the interactions and responses between interfaces by combining the SDK. You can make modifications to the overall structure in this class.


## Implementing UI
If you do not want to reuse the UI-related codes in our package and decide to implement UI independently, you can perform interfacing by referring to the following guide:

### 1. Preview Image Group

You can get some basic information of a specified video file by using the getVideoInfo method of TXVideoInfoReader, and a specified number of preview images using getSampleImages:

```objective-c
// Get the information of video file
+ (TXVideoInfo *)getVideoInfo:(NSString *)videoPath;

// Pre-read the video file, and evenly generate "count" preview image groups
+ (void)getSampleImages:(int)count
              videoPath:(NSString *)videoPath
               progress:(sampleProcess)sampleProcess;
```

In the package, VideoRangeSlider gets 10 thumbnails using getSampleImages to build a progress bar made up of video previews.

### 2. Effect Preview
Video editing provides two preview modes: **Fixed-point Preview** (freeze the video image at a certain point in time) and **Interval Preview** (play a video clip within a certain time period "A<=>B" on a loop). You need to bind the SDK with a UIView to display video images.

- **Bind UIView**
The initWithPreview function of TXVideoEditer is used to bind SDK with a UIView to render video images. When binding, you need to specify one of the following two modes: **Adaptive** and **Fill**.
```
   PREVIEW_RENDER_MODE_FILL_SCREEN - Fill pattern: the screen is filled as much as possible with no black edge left, so part of the images may be cut out.
   PREVIEW_RENDER_MODE_FILL_EDGE - Adaptive pattern: the image is kept as complete as possible, but black edges may appear in case of inappropriate aspect ratio.
```

- **Fixed-point Preview**
The previewAtTime function of TXVideoEditer is used to freeze and display the video image at a certain point in time.

- **Interval Preview**
The startPlayFromTime function of TXVideoEditer is used to play a video clip within a certain time period "A<=>B" on a loop.

### 3. Video Clipping
Operations in video editing are in conformity with the same principle: first set the operational instructions, and finally use generateVideo to execute all instructions in order, so as to avoid unnecessary quality loss due to repeated video compressions.

```objective-c
TXUGCEditer* _ugcEdit = [[TXUGCEditer alloc] initWithPreview:param];
// Set the start time and end time of clipping
[_ugcEdit setCutFromTime:_videoRangeSlider.leftPos toTime:_videoRangeSlider.rightPos];
// ...
// Generate the final video file
_ugcEdit.generateDelegate = self;
[_ugcEdit generateVideo:VIDEO_COMPRESSED_540P videoOutputPath:_videoOutputPath];
```
Specify the file compression quality and output path during output. You are notified of the output progress and result through the callback of `generateDelegate`.

### 4. Filter Effects
You can add filter effects to your videos such as whitening, romantic, fresh, etc. Demo offers 9 filter options, and you can also set the custom filters.  
The method to set filter is:

```
- (void) setFilter:(UIImage *)image;
```
"image" is the filter map. If it is set to nil, the filter effect is removed.

Demo example:
```
TXVideoEditer     *_ugcEdit;
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:@"langman.png"];
UIImage* image = [UIImage imageWithContentsOfFile:path];
[_ugcEdit setFilter:image];
```
### 5. Audio Track Processing
You can add your favorite background music to the videos, and also select the start time and end time for music playback. If the time period of music playback is less than that of the video, the music is played on a loop until the video ends. In addition, you can also set the volume of both video and background music to get the desired sound synthesis.

The method to set background music is:

```
- (void) setBGM:(NSString *)path startTime:(float)startTime endTime:(float)endTime;
```
"path" is the music file path. "startTime" is the start time of music playback. "endTime" is the end time of music playback.

The method to set the volume of video and background music is: 
 
```
- (void) setVideoVolume:(float)volume;  
- (void) setBGMVolume:(float)volume;
```   
"volume" indicates the sound level. Value range: 0 (mute) to 1 (original sound).

Demo example:
```
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:@"defalut.mp3"];
[_ugcEdit setBGM:path startTime:1 endTime:10];
[_ugcEdit setVideoVolume:0.5];
[_ugcEdit setBGMVolume:0.5];
```
### 6. Video Acceleration
You can set the video playback acceleration to implement the effect of fast playback.

The method to set video playback acceleration is:  

```
- (void) setSpeedLevel:(float)level;
```  
"level" indicates the acceleration level. Value range: 1 (original speed) to 4 (four times the speed).

Demo example:
```
[_ugcEdit setSpeedLevel:2];//Double Acceleration
```
### 7. Set Global Watermark
You can set the watermark for a video, and specify its location.

The method to set watermark is:  

```
- (void) setWaterMark:(UIImage *)waterMark  normalizationFrame:(CGRect)normalizationFrame;
```  
"waterMark" indicates the watermark image. "normalizationFrame " is the normalized frame relative to the video image. The value ranges of x, y, width and height of frame are all from 0 to 1.

Demo example:
```
UIImage *image = [UIImage imageNamed:@"watermark"];
[_ugcEdit setWaterMark:image normalizationFrame:CGRectMake(0, 0, 0.3 , 0.3 * image.size.height / image.size.width)];//The watermark size accounts for 30% of the video width, and the height is adaptive according to the width.
```
### 8. Set Tail Watermark
You can set the tail watermark for a video, and specify its location.

The method to set tail watermark is:  

```
- (void) setTailWaterMark:(UIImage *)tailWaterMark normalizationFrame:(CGRect)normalizationFrame 
                          duration:(CGFloat)duration;
```  
"tailWaterMark " indicates the tail watermark image. "normalizationFrame " is the normalized frame relative to the video image. The value ranges of x, y, width and height of frame are all from 0 to 1.
 "duration" indicates the duration of watermark.
Demo example: Set the watermark in the middle of the tail for 1 second.
```
UIImage *tailWaterimage = [UIImage imageNamed:@"tcloud_logo"];
float w = 0.15;
float x = (1.0 - w) / 2.0;
float width = w * videoMsg.width;
float height = width * tailWaterimage.size.height / tailWaterimage.size.width;
float y = (videoMsg.height - height) / 2 / videoMsg.height;
[_ugcEdit setTailWaterMark:tailWaterimage normalizationFrame:CGRectMake(x,y,w,0) duration:1];

```

### 9. Subtitle Overlay
Adding subtitles to videos is supported. You can add subtitles for each video frame, or set the start/end time of a video for each subtitle. All of the subtitles form a subtitle list. You can pass the subtitle list to SDK, and then SDK automatically overlays the video and subtitle at the right time.

The method to set subtitle is:  

```
- (void) setSubtitleList:(NSArray<TXSubtitle *> *)subtitleList;

The parameters of TXSubtitle are as follows:
@interface TXSubtitle: NSObject
@property (nonatomic, strong) UIImage*              titleImage;     //Subtitle image (text control needs to be converted to image)
@property (nonatomic, assign) CGRect                frame;          //Subtitle frame (the frame coordinates here are relative to the rendering view coordinates)
@property (nonatomic, assign) CGFloat               startTime;      //Subtitle start time (in sec)
@property (nonatomic, assign) CGFloat               endTime;        //Subtitle end time (in sec)
@end
```  
Note:  
titleImage: Subtitle image. If the upper layer uses UILabel or other controls, covert the control into UIImage first. For more information, please see the sample codes of Demo.  
frame: Subtitle frame. Please note that this frame is the one relative to the rendering view (the view specified during initWithPreview) frame. For more information, please see the sample codes of Demo.  
startTime: The start time of subtitle.  
endTime: The end time of subtitle.  

Since the UI logic of subtitle is complicated, we already have a set of implementation methods in Demo layer. You can directly use Demo implementation as a reference, so as to greatly reduce the access cost.

Demo example:
```
@interface VideoTextInfo : NSObject
@property (nonatomic, strong) VideoTextFiled* textField;
@property (nonatomic, assign) CGFloat startTime; //in seconds
@property (nonatomic, assign) CGFloat endTime;
@end

videoTextInfos = @[VideoTextInfo1, VideoTextInfo2 ...];

 for (VideoTextInfo* textInfo in videoTextInfos) {
        TXSubtitle* subtitle = [TXSubtitle new];
        subtitle.titleImage = textInfo.textField.textImage;  //UILabel(UIView) -> UIImage
        subtitle.frame = [textInfo.textField textFrameOnView:_videoPreview]; //Calculate the coordinates relative to the rendered view
        subtitle.startTime = textInfo.startTime;  //Subtitle start time
        subtitle.endTime = textInfo.endTime;      //Subtitle end time
        [subtitles addObject:subtitle];           //Add the subtitle list
  }    
    
 [_ugcEditer setSubtitleList:subtitles];          //Set the subtitle list
```

