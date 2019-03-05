## File类

### 属性
#### File.mediaInfo

返回：MediaInfo对象。

该属性为File对象的只读属性（即：对该对象的任何操作均会被任务流忽略），任务流可以据此获得文件的一些基本信息，例如视频流和音频流信息、文件来源等。

<!--#### File.mediaProperty

返回：MediaProperty对象。
开发者可以通过该对象设置的视频属性信息，主要是媒资相关信息。-->

#### File.aiReviewActionSet

#### File.manualReviewActionSet

#### File.processActionSet

返回：ActionSet对象。

开发者可以通过该属性指定视频文件的处理动作，可以进行的动作包括：

- 转码动作：TranscodeAction；
- 采样截图动作：SampleSnapshotAction；
- 雪碧图截图动作：ImageSpriteAction；
- 使用截图设置封面动作：CoverBySnapshotAction。

<!--#### File.publishActionSet

返回：ActionSet对象。
开发者可以通过该属性指定视频文件的分发动作。

#### File.publishProperty
返回：PublishProperty对象。
开发者可以通过该属性指定视频文件的分发属性。-->

### 方法
无。

## MediaInfo类
MediaInfo是一个Lua Table，其中包含了视频的各种基本信息。典型的MediaInfo如下：

```lua
{
    metaData = { -- 视频元数据
        size = 123,  -- 视频大小，单位字节
        container = "m4a", -- 视频的封装格式
        duration = 3601,  -- 视频时长（视频流总时长与音频流总时长的最大值）
        bitrate = 2500, -- 视频码率，单位为kbps
        height = 480,  -- 视频分辨率中的高度，如果视频包含多种分辨率，则该值为所有分辨率高度的最大值
        width = 640,  -- 视频分辨率中的宽度，如果视频包含多种分辨率，则该值为所有分辨率宽度的最大值
        videoStreamList = {  -- 视频流
            {
                bitrate = 246000,  -- 视频流码率
                height = 480,  -- 视频流分辨率中的高度
                width = 640,  -- 视频流分辨率中的宽度
                codec = "h264",  -- 视频编码方式
                fps = 222  -- TODO
            }
        },
        audioStreamList = {
            {
                codec = "als",  -- 音频编码方式
                samplingRate = 200,  -- 音频采样率，单位HZ
                bitrate = 35  -- 音频码率，单位kbps
            }
        }
    },
    sourceType = "RECORD",  -- 视频来源
    sourceContext = "rtmp://www.example/path/to/a/stream?key=value"  -- 视频来源上下文
}
```

<!--## MediaProperty类
开发者可以通过该对象设置的视频属性信息，主要是媒资相关信息。

### 属性
#### MediaProperty.classificationId

返回：Integer。

开发者可以通过该属性设置视频的分类ID。

### 方法
无。

## PublishProperty类

### 属性
无。

### 方法
无。-->

## ActionSet类
动作集合。

### 属性
无。

### 方法
#### ActionSet.addAction(action)
功能：增加动作。

返回：无。

参数：
* action: 动作。

## TranscodeAction类

开发者可以通过该类指定视频转码动作的各种参数，包括转码模板、加密模板、水印模板等。

### 属性
### TranscodeAction.transcodeDefinition
返回：转码输出模板ID，类型为数组。

可以通过该属性设置转码输出模板。


#### TranscodeAction.watermarkDefinition

返回：转码水印模板ID。

可以通过该属性设置水印模板。

#### TranscodeAction.disableHigherBitrate

返回：是否禁止将低码率视频转为高码率视频，类型为Bool。
如果将该属性设置为True，则点播后台会根据视频文件的当前码率，智能过滤掉码率较高的转码模板。

#### TranscodeAction.drm

返回：DRM对象。
可以通过该属性控制视频加密。

### 方法
#### TranscodeAction.addTranscodeDefinition(definition)

功能：增加转码模板ID。

返回：无。

参数：
* definition: 转码模板ID。重复的转码模板ID将被忽略。

#### TranscodeAction.clearTranscodeDefinition()

功能：清空已经设置的转码模板。

返回：无。

参数：无。

## SampleSnapshotAction类
采样截图动作。

### 属性
#### SampleSnapshotAction.definition

返回：采样截图参数模板ID。

可以通过该属性控制视频的采样截图动作。

### 方法
无。

## ImageSpriteAction

雪碧图截图动作。

### 属性
#### ImageSpriteAction.definition

返回：雪碧图截图参数模板ID。

可以通过该属性控制视频的雪碧图截图动作。

### 方法
无。

## CoverBySnapshotAction

### 属性
#### CoverBySnapshotAction.definition
返回：截图参数模板ID。

可以通过该属性控制如何将视频指定位置的截图设置为其封面。

### 方法
无。

## DRM类
控制视频加密方式。

### 属性
#### DRM.definition

返回：视频加密参数模板ID。

可以通过该属性设置视频加密参数模板。

### 方法
无。