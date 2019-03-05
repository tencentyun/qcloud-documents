## Overview
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

To compile and run the Demo, download the [SDK package](https://cloud.tencent.com/document/product/584/9366) from Download Resources, decompress it and run the Demo project RTMPiOSDemo.xcodeproj. By clicking the video editing on the running main interface, you can select the video and experience the editing feature.

## Reusing Existing UI
Video editing has a complicated interaction logic and thus its UI has a high complexity. Therefore, it is recommended to reuse the UI source code from the SDK package. During use, copy the following folder from Demo to your own project:    
1. VideoEditor (code)  
2. VideoEditor and FilterResource.bundle under Resource (resources)  
3. Common and Third (the common code that the whole Demo relies on. You can delete or modify it based on your own needs)

UI source code description
Since each interface component in the source code is independent, you can modify and process the interface according to your product demands.
Description of main interface components:  
1. VideoCutView: The video clipping interface, including video clipping, time effects, filter effects and other features. To customize clipping interface, you can modify or replace this class.  
2. FilterSettingView: The video filtering interface, including 9 filters. To make modifications, you can change or replace this class.  
3.MusicMixView: The video sound mixing interface, including music file selection, music information display, music length cutting, volume adjustment of original and accompanying sounds. To make modifications, you can change or replace this class.  
4. TextAddView: The video subtitle adding interface, which only contains the button to redirect to VideoTextViewController. In practice, you can add subtitles or perform other operations in VideoTextViewController. This interface can be modified or removed as needed.  
5. VideoTextField: The subtitle input component, including subtitle text input, subtitle dragging, enlargement, rotation, deletion, adding subtitle background styles. This component in VideoTextViewController is mainly used to add and delete subtitles.  
6. VideoPasterView: The sticker input component, including dynamic/static sticker input, sticker dragging, enlargement, rotation, deletion and other features. This component in VideoPasterViewController is mainly used to add and delete stickers.  

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
   PREVIEW_RENDER_MODE_FILL_EDGE   - Adaptive pattern: the image is kept as complete as possible, but black edges may appear in case of inappropriate aspect ratio.   
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

Demo:
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
- (void) setBGM:(NSString *)path result:(void(^)(int))result;
```
"path" is the music file path.

The method to set the start time and the end time of the background music is:
```
- (void) setBGMStartTime:(float)startTime endTime:(float)endTime;
```
"startTime" is the start time of music playback. "endTime" is the end time of music playback.

The method to set whether the background music is played on a loop:
```
- (void) setBGMLoop:(BOOL)isLoop;
```
"isLoop" specifies whether the music is played on a loop.

The method to set the start time of the background music in the video:
```
- (void) setBGMAtVideoTime:(float)time;
```
"time" is the start time of the music in the video.

The method to set the volume of video and background music is: 
```
- (void) setVideoVolume:(float)volume;  
- (void) setBGMVolume:(float)volume;
```   
"volume" indicates the sound level. Value range: 0 (mute) to 1 (original sound).

Demo:

```
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:@"defalut.mp3"];
[_ugcEdit setBGM:_BGMPath result:^(int result) {
    if (result == 0) {
        [_ugcEdit setBGMStartTime:0 endTime:10];
        [_ugcEdit setBGMVolume:1];
        [_ugcEdit setVideoVolume:1];
     }
}];
```

### 6. Set Global Watermark
You can set the watermark for a video, and specify its location.

The method to set watermark is:  

```
- (void) setWaterMark:(UIImage *)waterMark  normalizationFrame:(CGRect)normalizationFrame;
```  
"waterMark" indicates the watermark image. "normalizationFrame " is the normalized frame relative to the video image. The value ranges of x, y, width and height of frame are all from 0 to 1.

Demo:
```
UIImage *image = [UIImage imageNamed:@"watermark"];  
[_ugcEdit setWaterMark:image normalizationFrame:CGRectMake(0, 0, 0.3 , 0.3 * image.size.height / image.size.width)];//The watermark size accounts for 30% of the video width, and the height is adaptive according to the width.
```
### 7. Set Tail Watermark
You can set the tail watermark for a video, and specify its location.
The method to set tail watermark is:  

```
- (void) setTailWaterMark:(UIImage *)tailWaterMark normalizationFrame:(CGRect)normalizationFrame 
                          duration:(CGFloat)duration;
```  
"tailWaterMark " indicates the tail watermark image. "normalizationFrame " is the normalized frame relative to the video image. The value ranges of x, y, width and height of frame are all from 0 to 1.
 "duration" indicates the duration of watermark.
Demo: Set the watermark in the middle of the tail for 1 second.

```
UIImage *tailWaterimage = [UIImage imageNamed:@"tcloud_logo"];
float w = 0.15;
float x = (1.0 - w) / 2.0;
float width = w * videoMsg.width;
float height = width * tailWaterimage.size.height / tailWaterimage.size.width;
float y = (videoMsg.height - height) / 2 / videoMsg.height;
[_ugcEdit setTailWaterMark:tailWaterimage normalizationFrame:CGRectMake(x,y,w,0) duration:1];   

```

### 8. Filter Effects
You can add multiple filter effects to your videos. Four types of filter effects are supported. You can also set the start time and end time in the video for each filter effect. If multiple filter effects are set at the same time point, the SDK uses the last filter effect as the current filter effect.

The method to set filter effects is:

```
- (void) startEffect:(TXEffectType)type  startTime:(float)startTime;
- (void) stopEffect:(TXEffectType)type  endTime:(float)endTime;

//The filter effect type (type parameter), which is defined in the constant TXEffectType:
typedef  NS_ENUM(NSInteger,TXEffectType)
{
    TXEffectType_ROCK_LIGHT,  //Dynamic light-wave
    TXEffectType_DARK_DRAEM,  //Darkness and phantom
    TXEffectType_SOUL_OUT,    //Soul out
    TXEffectType_SCREEN_SPLIT,//Cracked screen
};

- (void) deleteLastEffect;
- (void) deleteAllEffect;
```
Call deleteLastEffect() to delete the last filter effect.  
Call deleteAllEffect() to delete all filter effects.

Demo:
Apply the first filter effect between 1-2s, apply the second filter effect between 3-4s, and remove the filter effect set for 3-4s.

```
//Apply the first filter effect between 1-2s
[_ugcEdit startEffect(TXEffectType_SOUL_OUT, 1.0);
[_ugcEdit stopEffect(TXEffectType_SOUL_OUT, 2.0);
//Apply the second filter effect between 3-4s
[_ugcEdit startEffect(TXEffectType_SPLIT_SCREEN, 3.0);
[_ugcEdit stopEffect(TXEffectType_SPLIT_SCREEN, 4.0);
//Remove the filter effect set for 3-4s
[_ugcEdit deleteLastEffect];
```
### 9. Slow/Fast Motion
You can slow down/speed up the playback of multiple video fragments. The method to set slow/fast playback is:

```
- (void) setSpeedList:(NSArray *)speedList;

//TXSpeed's parameters are as follows:
@interface TXSpeed: NSObject
@property (nonatomic, assign) CGFloat               startTime;      //Start time of fast playback (in sec)
@property (nonatomic, assign) CGFloat               endTime;        //End time of fast playback (in sec)
@property (nonatomic, assign) TXSpeedLevel          speedLevel;     //Speed level
@end

// The following speed levels defined in the constant TXSpeedLevel are supported:
typedef NS_ENUM(NSInteger, TXSpeedLevel) {
    SPEED_LEVEL_SLOWEST,       //Very slow
    SPEED_LEVEL_SLOW,          //Slow
    SPEED_LEVEL_NOMAL,         //Normal
    SPEED_LEVEL_FAST,          //Fast
    SPEED_LEVEL_FASTEST,       //Very fast
};
```
Demo:

```
// SDK supports changing speed of multiple video fragments. This DEMO only shows the slow playback of a video fragment.
  TXSpeed *speed =[[TXSpeed alloc] init];
  speed.startTime = 1.0;
  speed.endTime = 3.0;
  speed.speedLevel = SPEED_LEVEL_SLOW;
  [_ugcEdit setSpeedList:@[speed]];
```
### 10. Reverse
You can play videos in reverse order. The method to set reverse is:

```
- (void) setReverse:(BOOL)isReverse;
```
Demo:

```
[_ugcEdit setReverse:YES];
```

### 11. Repeated Playback
You can set the repeated playback of a video frame, but the sound will not be played repeatedly.  
Set repeated playback:

```
- (void) setRepeatPlay:(NSArray *)repeatList;

//TXRepeat's parameters are as follows:
@interface TXRepeat: NSObject
@property (nonatomic, assign) CGFloat               startTime;      //Start time (in sec) of the repeated playback
@property (nonatomic, assign) CGFloat               endTime;        //End time (in sec) of the repeated playback
@property (nonatomic, assign) int                   repeatTimes;    //Number of times for repeated playback
@end
```

Demo:

```
TXRepeat *repeat = [[TXRepeat alloc] init];
repeat.startTime = 1.0;  
repeat.endTime = 3.0;
repeat.repeatTimes = 3;  //Number of times for repeated playback
[_ugcEdit setRepeatPlay:@[repeat]];
```

### 12. Static/Dynamic Stickers

You can set static or dynamic stickers for your video.

Set a static sticker:

```
- (void) setPasterList:(NSArray *)pasterList;

//TXPaster's parameters are as follows:
@interface TXPaster: NSObject
@property (nonatomic, strong) UIImage*              pasterImage;    //Sticker image
@property (nonatomic, assign) CGRect                frame;          //Sticker frame (the coordinates of the frame here are relative to those of the rendering view)
@property (nonatomic, assign) CGFloat               startTime;      //Start time of sticker (in sec)
@property (nonatomic, assign) CGFloat               endTime;        //End time of sticker (in sec)
@end

```

Set a dynamic sticker:

```
- (void) setAnimatedPasterList:(NSArray *)animatedPasterList;

// TXAnimatedPaster's parameters are as follows:
@interface TXAnimatedPaster: NSObject
@property (nonatomic, strong) NSString*             animatedPasterpath;  //Path of the dynamic sticker image
@property (nonatomic, assign) CGRect                frame;          //Dynamic sticker frame (the coordinates of the frame here are relative to those of the rendering view)
@property (nonatomic, assign) CGFloat               rotateAngle;    //Dynamic sticker's rotation angle (0-360)
@property (nonatomic, assign) CGFloat               startTime;      //Start time of dynamic sticker (in sec)
@property (nonatomic, assign) CGFloat               endTime;        //End time of dynamic sticker (in sec)
@end
```

Demo:

```
- (void)setVideoPasters:(NSArray*)videoPasterInfos
{
    NSMutableArray* animatePasters = [NSMutableArray new];
    NSMutableArray* staticPasters = [NSMutableArray new];
    for (VideoPasterInfo* pasterInfo in videoPasterInfos) {
        if (pasterInfo.pasterInfoType == PasterInfoType_Animate) {
            TXAnimatedPaster* paster = [TXAnimatedPaster new];
            paster.startTime = pasterInfo.startTime;
            paster.endTime = pasterInfo.endTime;
            paster.frame = [pasterInfo.pasterView pasterFrameOnView:_videoPreview];
            paster.rotateAngle = pasterInfo.pasterView.rotateAngle * 180 / M_PI;
            paster.animatedPasterpath = pasterInfo.path;
            [animatePasters addObject:paster];
        }
        else if (pasterInfo.pasterInfoType == PasterInfoType_static){
            TXPaster *paster = [TXPaster new];
            paster.startTime = pasterInfo.startTime;
            paster.endTime = pasterInfo.endTime;
            paster.frame = [pasterInfo.pasterView pasterFrameOnView:_videoPreview];
            paster.pasterImage = pasterInfo.pasterView.staticImage;
            [staticPasters addObject:paster];
        }
    }
    [_ugcEditer setAnimatedPasterList:animatePasters];
    [_ugcEditer setPasterList:staticPasters];
}
```
#### How to customize dynamic stickers?
Dynamic sticker is designed to insert **a set of images** into video frames at **specified intervals** in **a certain order** to produce a dynamic sticker effect.

##### Encapsulation Format
Take a dynamic sticker in Demo as an example:

```
{
  "name":"glass",                        //Sticker name
  "count":6,                             //Number of stickers
  "period":480,                          //Playback period: Time taken to play a dynamic sticker (in ms)
  "width":444,                           //Sticker width
  "height":256,                          //Sticker height
  "keyframe":6,                          //Key image that can represent the dynamic sticker
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

**Note: This encapsulation format is used to describe the dynamic sticker as required by SDK.**


### 13. Bubble Subtitles
Adding bubble subtitles to videos is supported. You can add bubble subtitles for each video frame, or set the start/end time of a video for each subtitle. All of the subtitles form a subtitle list. You can pass the subtitle list to SDK, and then SDK automatically overlays the video and subtitle at the right time.

The method to set subtitle is:  

```
- (void) setSubtitleList:(NSArray *)subtitleList;

TXSubtitle 's parameters are as follows:
@interface TXSubtitle: NSObject
@property (nonatomic, strong) UIImage*              titleImage;     //Subtitle image (text control needs to be converted to image)
@property (nonatomic, assign) CGRect                frame;          //Subtitle frame (the coordinates of the frame here are relative to those of the rendering view)
@property (nonatomic, assign) CGFloat               startTime;      //Subtitle start time (in sec)
@property (nonatomic, assign) CGFloat               endTime;        //Subtitle end time (in sec)
@end
```  
Where:  
titleImage: Subtitle image. If the upper layer uses UILabel or other controls, covert the control into UIImage first. For more information, please see the sample codes of Demo.  
frame: Subtitle frame. Please note that this frame is the one relative to the rendering view (the view specified during initWithPreview) frame. For more information, please see the sample code of Demo.  
startTime: The start time of subtitle.  
endTime: The end time of subtitle.  

Since the UI logic of subtitle is complicated, we already have a set of implementation methods in Demo layer. You can directly use Demo implementation as a reference, so as to greatly reduce the access cost.
Demo:

```
@interface VideoTextInfo : NSObject
@property (nonatomic, strong) VideoTextFiled* textField;
@property (nonatomic, assign) CGFloat startTime; //in seconds
@property (nonatomic, assign) CGFloat endTime;
@end

videoTextInfos = @[VideoTextInfo1, VideoTextInfo2 ...];

 for (VideoTextInfo* textInfo in videoTextInfos) {
        TXSubtitle* subtitle = [TXSubtitle new];
        subtitle.titleImage = textInfo.textField.textImage;  //UILabel（UIView） -> UIImage
        subtitle.frame = [textInfo.textField textFrameOnView:_videoPreview]; //Calculate the coordinates relative to the rendered view
        subtitle.startTime = textInfo.startTime;  //Subtitle start time
        subtitle.endTime = textInfo.endTime;      //Subtitle end time
        [subtitles addObject:subtitle];           //Add the subtitle list
  }    
    
 [_ugcEditer setSubtitleList:subtitles];          //Set the subtitle list
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
  "name":"boom",     // Name of bubble subtitle
  "width": 376,      // Width
  "height": 335,     // Height
  "textTop":121,     // Top margin of text area
  "textLeft":66,     // Left margin of text area
  "textRight":69,    // Right margin of text area
  "textBottom":123,  // Bottom margin of text area
  "textSize":40      // Font size
}
```
**Note: The encapsulation format can be customized, which is not specified by SDK.**

##### How to process a long subtitle?
If a subtitle is too long, how to merge it with a bubble to realize aesthetic effect?
We provide an automatic layout control in the Demo. If the subtitle with the current font size is too long, the control automatically reduces the font size until the bubble can accommodate all characters in the subtitle.
You can also modify the source code of the relevant control to meet your business needs. 

