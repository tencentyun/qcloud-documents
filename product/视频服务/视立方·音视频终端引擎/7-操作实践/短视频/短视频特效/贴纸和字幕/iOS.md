## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。



## 静态贴纸


<dx-codeblock>
::: iOS 
- (void) setPasterList:(NSArray *)pasterList;

// TXPaster 的参数如下：
@interface TXPaster: NSObject
@property (nonatomic, strong) UIImage*              pasterImage;    //贴纸图片
@property (nonatomic, assign) CGRect                frame;          //贴纸 frame（注意这里的 frame 坐标是相对于渲染 view 的坐标）
@property (nonatomic, assign) CGFloat               startTime;      //贴纸起始时间(s)
@property (nonatomic, assign) CGFloat               endTime;        //贴纸结束时间(s)
@end
:::
</dx-codeblock>

## 动态贴纸

### 设置方法

<dx-codeblock>
::: iOS 
- (void) setAnimatedPasterList:(NSArray *)animatedPasterList;

// TXAnimatedPaster 的参数如下：
@interface TXAnimatedPaster: NSObject
@property (nonatomic, strong) NSString*             animatedPasterpath;  //动图文件路径
@property (nonatomic, assign) CGRect                frame;          //动图的 frame（注意这里的 frame 坐标是相对于渲染 view 的坐标）
@property (nonatomic, assign) CGFloat               rotateAngle;    //动图旋转角度 (0 ~ 360)
@property (nonatomic, assign) CGFloat               startTime;      //动图起始时间(s)
@property (nonatomic, assign) CGFloat               endTime;        //动图结束时间(s)
@end
:::
</dx-codeblock>

### Demo 示例

<dx-codeblock>
::: iOS 

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
:::
</dx-codeblock>

## 自定义动态贴纸
动态贴纸的本质是：将**一串图片**，按照**一定的顺序**以及**时间间隔**，插入到视频画面中去，形成一个动态贴纸的效果。

### 自定义贴纸

以工具包 Demo 中一个动态贴纸为例：

<dx-codeblock>
::: iOS 
{
  "name":"glass",                        // 贴纸名称
  "count":6,                             // 贴纸数量
  "period":480,                          // 播放周期：播放一次动态贴纸的所需要的时间(ms)
  "width":444,                           // 贴纸宽度
  "height":256,                          // 贴纸高度
  "keyframe":6,                          // 关键图片：能够代表该动态贴纸的一张图片
  "frameArray": [                        // 所有图片的集合
                 {"picture":"glass0"},
                 {"picture":"glass1"},
                 {"picture":"glass2"},
                 {"picture":"glass3"},
                 {"picture":"glass4"},
                 {"picture":"glass5"}
               ]
}
:::
</dx-codeblock>

SDK 内部将获取到该动态贴纸对应的 `config.json`，并且按照 JSON 中定义的格式进行动态贴纸的展示。
>?该封装格式为 SDK 内部强制性要求，请严格按照该格式描述动态贴纸。

## 添加字幕
### 气泡字幕
您可以为视频添加字幕，我们支持对每一帧视频添加字幕，每个字幕您也可以设置视频作用的起始时间和结束时间。所有的字幕组成了一个字幕列表， 您可以把字幕列表传给 SDK 内部，SDK 会自动在合适的时间对视频和字幕做叠加。

#### 设置方法

<dx-codeblock>
::: iOS 
- (void) setSubtitleList:(NSArray *)subtitleList;

TXSubtitle 的参数如下：
@interface TXSubtitle: NSObject
@property (nonatomic, strong) UIImage*              titleImage;     //字幕图片   （这里需要客户把承载文字的控件转成 image 图片）
@property (nonatomic, assign) CGRect                frame;          //字幕的 frame（注意这里的 frame 坐标是相对于渲染 view 的坐标）
@property (nonatomic, assign) CGFloat               startTime;      //字幕起始时间(s)
@property (nonatomic, assign) CGFloat               endTime;        //字幕结束时间(s)
@end
:::
</dx-codeblock>

| 参数 | 说明 | 
|---------|---------|
| titleImage | 表示字幕图片，如果上层使用的是 UILabel 之类的控件，请先把控件转成 UIImage，具体方法可以参照 [Demo](#demo) 的示例代码。  | 
| frame | 表示字幕的 frame，注意这个 frame 是相对于渲染 view（initWithPreview 时候传入的 view）的 frame，具体可以参照 Demo 的示例代码。 | 
| startTime | 字幕作用的起始时间。   | 
| endTime | 字幕作用的结束时间。   | 


因为字幕这一块的 UI 逻辑比较复杂，我们已经在 Demo 层有一整套的实现方法，推荐客户直接参考 [Demo](https://cloud.tencent.com/document/product/1449/56977) 实现， 可以大大降低您的接入成本。

[](id:demo)
#### Demo 示例

<dx-codeblock>
::: iOS 
@interface VideoTextInfo : NSObject
@property (nonatomic, strong) VideoTextFiled* textField;
@property (nonatomic, assign) CGFloat startTime; //in seconds
@property (nonatomic, assign) CGFloat endTime;
@end

videoTextInfos = @[VideoTextInfo1, VideoTextInfo2 ...];

 for (VideoTextInfo* textInfo in videoTextInfos) {
        TXSubtitle* subtitle = [TXSubtitle new];
        subtitle.titleImage = textInfo.textField.textImage;  //UILabel（UIView） -> UIImage
        subtitle.frame = [textInfo.textField textFrameOnView:_videoPreview]; //计算相对于渲染 view 的坐标
        subtitle.startTime = textInfo.startTime;  //字幕起始时间
        subtitle.endTime = textInfo.endTime;      //字幕结束时间
        [subtitles addObject:subtitle];           //添加字幕列表
  }    
    
 [_ugcEditer setSubtitleList:subtitles];          //设置字幕列表
:::
</dx-codeblock>

### 自定义气泡字幕
#### 气泡字幕所需要参数
* 文字区域大小： top、left、right、bottom
* 默认的字体大小
* 宽、高

>?以上单位均为 px。

#### 封装格式
由于气泡字幕中携带参数较多，建议您在 Demo 层封装相关的参数。如腾讯云 Demo 中使用的 JSON 格式封装：
<dx-codeblock>
::: iOS 
{
  "name":"boom",     // 气泡字幕名称
  "width": 376,      // 宽度
  "height": 335,     // 高度
  "textTop":121,     // 文字区域上边距
  "textLeft":66,     // 文字区域左边距
  "textRight":69,    // 文字区域右边距
  "textBottom":123,  // 文字区域下边距
  "textSize":40      // 字体大小
}
:::
</dx-codeblock>

>?该封装格式用户可以自行决定，非 SDK 强制性要求。

#### 字幕过长
我们的 [Demo](https://cloud.tencent.com/document/product/1449/56977) 提供了一个自动排版的控件，在当前字体大小下，且字幕过长时，控件将自动缩小字号，直到能够恰好放下所有字幕文字为止。使用该控件即可**实现字幕若输入过长情况下，通过排版使字幕与气泡美观地合并。**
您也可以修改相关控件源代码，来满足自身的业务要求。 

