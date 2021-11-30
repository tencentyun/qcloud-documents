## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。



## 滤镜特效

您可以为视频添加多种滤镜特效，我们目前支持11种滤镜特效，每种滤镜您也可以设置视频作用的起始时间和结束时间。如果同一个时间点设置了多种滤镜特效，SDK 会应用最后一种滤镜特效作为当前的滤镜特效。

### 设置方法

```
- (void) startEffect:(TXEffectType)type  startTime:(float)startTime;
- (void) stopEffect:(TXEffectType)type  endTime:(float)endTime;

//特效的类型（type 参数），在常量 TXEffectType 中有定义：
typedef  NS_ENUM(NSInteger,TXEffectType)
{
    TXEffectType_ROCK_LIGHT,  //动感光波
    TXEffectType_DARK_DRAEM,  //暗黑幻境
    TXEffectType_SOUL_OUT,    //灵魂出窍
    TXEffectType_SCREEN_SPLIT,//视频分裂
    TXEffectType_WIN_SHADOW,  //百叶窗
    TXEffectType_GHOST_SHADOW,//鬼影
    TXEffectType_PHANTOM,     //幻影
    TXEffectType_GHOST,       //幽灵
    TXEffectType_LIGHTNING,   //闪电
    TXEffectType_MIRROR,      //镜像
    TXEffectType_ILLUSION,    //幻觉
};

- (void) deleteLastEffect;
- (void) deleteAllEffect;
```
- 调用 deleteLastEffect() 删除最后一次设置的滤镜特效。 
- 调用 deleteAllEffect()  删除所有设置的滤镜特效。

### Demo 示例

在1s - 2s之间应用第一种滤镜特效，在3s - 4s之间应用第2种滤镜特效，删除3s - 4s设置的滤镜特效。

```
//在1-2s之间应用第一种滤镜特效
[_ugcEdit startEffect:TXEffectType_SOUL_OUT startTime:1.0];
[_ugcEdit stopEffect:TXEffectType_SOUL_OUT startTime:2.0)];

//在3-4s之间应用第2种滤镜特效
[_ugcEdit startEffect:TXEffectType_SPLIT_SCREEN startTime:3.0];
[_ugcEdit stopEffect:TXEffectType_SPLIT_SCREEN startTime:4.0];

//删除3-4s设置的滤镜特效
[_ugcEdit deleteLastEffect];
```
##  慢/快动作
您可以进行多段视频的慢速/快速播放。

### 设置方法
<dx-codeblock>
::: ios 

- (void) setSpeedList:(NSArray *)speedList;

//TXSpeed 的参数如下：
@interface TXSpeed: NSObject
@property (nonatomic, assign) CGFloat               startTime;      //加速播放起始时间(s)
@property (nonatomic, assign) CGFloat               endTime;        //加速播放结束时间(s)
@property (nonatomic, assign) TXSpeedLevel          speedLevel;     //加速级别
@end

// 目前支持变速速度的几种级别，在常量 TXSpeedLevel 中有定义：
typedef NS_ENUM(NSInteger, TXSpeedLevel) {
    SPEED_LEVEL_SLOWEST,       //极慢速
    SPEED_LEVEL_SLOW,          //慢速
    SPEED_LEVEL_NOMAL,         //正常速
    SPEED_LEVEL_FAST,          //快速
    SPEED_LEVEL_FASTEST,       //极快速
};
:::
</dx-codeblock>

### Demo 示例

<dx-codeblock>
::: ios 
// SDK 拥有支持多段变速的功能。 此 Demo 仅展示一段慢速播放
  TXSpeed *speed =[[TXSpeed alloc] init];
  speed.startTime = 1.0;
  speed.endTime = 3.0;
  speed.speedLevel = SPEED_LEVEL_SLOW;
  [_ugcEdit setSpeedList:@[speed]];
:::
</dx-codeblock>

## 倒放
您可以将视频画面倒序播放。

### 设置方法

```
- (void) setReverse:(BOOL)isReverse;
```
### Demo 示例

```
[_ugcEdit setReverse:YES];
```

## 重复视频片段
您可以设置重复播放一段视频画面，声音不会重复播放。  

### 设置方法

<dx-codeblock>
::: ios 
- (void) setRepeatPlay:(NSArray *)repeatList;

//TXRepeat 的参数如下：
@interface TXRepeat: NSObject
@property (nonatomic, assign) CGFloat               startTime;      //重复播放起始时间(s)
@property (nonatomic, assign) CGFloat               endTime;        //重复播放结束时间(s)
@property (nonatomic, assign) int                   repeatTimes;    //重复播放次数
@end
:::
</dx-codeblock>

### Demo 示例

```
TXRepeat *repeat = [[TXRepeat alloc] init];
repeat.startTime = 1.0;  
repeat.endTime = 3.0;
repeat.repeatTimes = 3;  //重复次数
[_ugcEdit setRepeatPlay:@[repeat]];
```
