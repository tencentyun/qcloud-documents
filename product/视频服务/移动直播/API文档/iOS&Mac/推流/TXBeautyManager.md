
美颜、美容、动效挂件类基础函数。

### setBeautyStyle 

设置美颜类型。 
```
- (void)setBeautyStyle:(TXBeautyStyle)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | TXBeautyStyle | 美颜风格，TXBeautyStyleSmooth表示光滑；TXBeautyStyleNature表示自然；TXBeautyStylePitu表示朦胧。 |


### setFilter

设置指定素材滤镜特效。
```
- (void)setFilter:(TXImage *)image 
```

>?滤镜图片一定要用 png 格式，Demo 用到的滤镜查找表图片位于 TXLiteAVDemo/Resource/Beauty/filter/FilterResource.bundle 中。

***

### setSpecialRatio

设置滤镜浓度。
```
- (void)setFilterStrength:(float)strength 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| strength | float | 取值范围0 - 1的浮点型数字，取值越大滤镜效果越明显，默认取值0.5。 |

__介绍__

在美女秀场等应用场景里，滤镜浓度的要求会比较高，以便更加突显主播的差异。 我们默认的滤镜浓度是0.5，如果您觉得滤镜效果不明显，可以使用下面的接口进行调节。

***

### setGreenScreenFile

设置绿幕背景视频（商业版有效，其它版本设置此参数无效）。
```
- (void)setGreenScreenFile:(NString *)file 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| file | NString * | 视频文件路径。支持 MP4；nil 表示关闭特效。 |

__介绍__

此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效。

### setBeautyLevel

设置美颜级别。
```
- (void)setBeautyLevel:(float)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 美颜级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setWhitenessLevel

设置美白级别。
```
- (void)setWhitenessLevel:(float)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setRuddyLevel

设置红润级别。
```
- (void)setRuddyLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setEyeScaleLevel

设置大眼级别（商业版有效，其它版本设置此参数无效）。
```
- (void)setEyeScaleLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 大眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setFaceSlimLevel

设置瘦脸级别（商业版有效，其它版本设置此参数无效）。
```
- (void)setFaceSlimLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 瘦脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setFaceVLevel

设置 V 脸级别（商业版有效，其它版本设置此参数无效）。
```
- (void)setFaceVLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | V 脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setChinLevel

设置下巴拉伸或收缩（商业版有效，其它版本设置此参数无效）。
```
- (void)setChinLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 下巴拉伸或收缩级别，取值范围-9 - 9；0表示关闭，小于0表示收缩，大于0表示拉伸。 |

### setFaceShortLevel

设置短脸级别（商业版有效，其它版本设置此参数无效）。
```
- (void)setFaceShortLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 短脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setNoseSlimLevel

设置瘦鼻级别（商业版有效，其它版本设置此参数无效）。
```
- (void)setNoseSlimLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 瘦鼻级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setEyeLightenLevel

设置亮眼 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setEyeLightenLevel:(float)level 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 亮眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setToothWhitenLevel

设置白牙 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setToothWhitenLevel:(float)level 
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 白牙级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setWrinkleRemoveLevel

设置祛皱 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setWrinkleRemoveLevel:(float)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 祛皱级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setPounchRemoveLevel
设置祛眼袋 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setPounchRemoveLevel:(float)level 
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 祛眼袋级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setSmileLinesRemoveLevel

设置祛法令纹 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setSmileLinesRemoveLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 祛法令纹级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setForeheadLevel
设置发际线 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setForeheadLevel:(float)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 发际线级别，取值范围-9 - 9；0表示关闭，小于0表示抬高，大于0表示降低。 |

### setEyeDistanceLevel
设置眼距 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setEyeDistanceLevel:(float)level 
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 眼距级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。|

### setEyeAngleLevel
设置眼角 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setEyeAngleLevel:(float)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 眼角级别，取值范围-9 - 9；0表示关闭，小于0表示降低，大于0表示抬高。 |


### setMouthShapeLevel
设置嘴型 （商用企业版有效，其它版本设置此参数无效）。

```
- (void)setMouthShapeLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 嘴型级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。 |

### setNoseWingLevel
设置鼻翼 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setNoseWingLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 鼻翼级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。|


### setNosePositionLevel
设置鼻子位置 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setNosePositionLevel:(float)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 鼻子位置级别，取值范围-9 - 9；0表示关闭，小于0表示抬高，大于0表示降低。 |

### setLipsThicknessLevel
设置嘴唇厚度 （商用企业版有效，其它版本设置此参数无效）。

```
- (void)setLipsThicknessLevel:(float)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 嘴唇厚度级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。 |

### setFaceBeautyLevel
设置脸型 （商用企业版有效，其它版本设置此参数无效）。
```
- (void)setFaceBeautyLevel:(float)level
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | float | 脸型级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setMotionTmpl

选择使用哪一款 AI 动效挂件（商业版有效，其它版本设置此参数无效）。
```
- (void)setMotionTmpl:(nullable NSString *)tmplName inDir:(nullable NSString *)tmplDir
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| tmplDir | NSString * | 动效所在目录。 |
| tmplName | NSString * | 动效名称。 |

### setMotionMute

设置动效静音（商业版有效，其它版本设置此参数无效）。有些挂件本身会有声音特效，通过此 API 可以关闭这些特效播放时所带的声音效果。
```
- (void)setMotionMute:(BOOL)motionMute
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| motionMute | BOOL | YES 表示静音；NO 表示不静音。 |

 

