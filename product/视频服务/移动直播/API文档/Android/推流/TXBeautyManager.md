
美颜、美容、动效挂件类基础函数。

### setBeautyStyle

设置美颜类型。
```
void setBeautyStyle(int beautyStyle) 
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| beautyStyle | int | 美颜风格，0表示光滑，1表示自然，2表示朦胧。 |

### setFilter

设置指定素材滤镜特效。
```
void setFilter(Bitmap bmp)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bmp | Bitmap | 滤镜图片。 |

>?滤镜图片一定要用 png 格式，demo 用到的滤镜查找表图片位于 app/src/main/res/drawable-xxhdpi/ 中。

***

### setFilterStrength

设置滤镜浓度。
```
void setFilterStrength(float strength)
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
boolean setGreenScreenFile(String path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | String | 视频文件路径。支持 MP4；null 表示关闭特效。 |

__介绍__

此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效。

### setBeautyLevel

设置美颜级别。
```
void setBeautyLevel(int beautyLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| beautyLevel | int | 美颜级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setWhitenessLevel

设置美白级别。
```
void setWhitenessLevel(int whitenessLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| whitenessLevel | int | 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setRuddyLevel

设置红润级别。
```
void setRuddyLevel(int ruddyLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| ruddyLevel | int | 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setEyeScaleLevel

设置大眼级别（商业版有效，其它版本设置此参数无效）。
```
void setEyeScaleLevel(int eyeScaleLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eyeScaleLevel | int | 大眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setFaceSlimLevel

设置瘦脸级别（商业版有效，其它版本设置此参数无效）。
```
void setFaceSlimLevel(int faceSlimLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceSlimLevel | int | 瘦脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setFaceVLevel

设置 V 脸级别（商业版有效，其它版本设置此参数无效）。
```
void setFaceVLevel(int faceVLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceVLevel | int | V 脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setChinLevel

设置下巴拉伸或收缩（商业版有效，其它版本设置此参数无效）。
```
void setChinLevel(int chinLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| chinLevel | int | 下巴拉伸或收缩级别，取值范围-9 - 9；0 表示关闭，小于0表示收缩，大于0表示拉伸。 |

### setFaceShortLevel

设置短脸级别（商业版有效，其它版本设置此参数无效）。
```
void setFaceShortLevel(int faceShortlevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceShortlevel | int | 短脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setNoseSlimLevel

设置瘦鼻级别（商业版有效，其它版本设置此参数无效）。
```
void setNoseSlimLevel(int noseSlimLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| noseSlimLevel | int | 瘦鼻级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setEyeLightenLevel

设置亮眼 （商用企业版有效，其它版本设置此参数无效）。
```
void setEyeLightenLevel(int eyeLightenLevel) 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eyeLightenLevel | int | 亮眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setToothWhitenLevel

设置白牙 （商用企业版有效，其它版本设置此参数无效）。
```
void setToothWhitenLevel(int toothWhitenLevel) 
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| toothWhitenLevel | int | 白牙级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setWrinkleRemoveLevel

设置祛皱 （商用企业版有效，其它版本设置此参数无效）。
```
void setWrinkleRemoveLevel(int wrinkleRemoveLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| wrinkleRemoveLevel | int | 祛皱级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setPounchRemoveLevel
设置祛眼袋 （商用企业版有效，其它版本设置此参数无效）。
```
void setPounchRemoveLevel(int pounchRemoveLevel) 
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pounchRemoveLevel | int | 祛眼袋级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setSmileLinesRemoveLevel

设置祛法令纹 （商用企业版有效，其它版本设置此参数无效）。
```
void setSmileLinesRemoveLevel(int smileLinesRemoveLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| smileLinesRemoveLevel | int | 祛法令纹级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setForeheadLevel
设置发际线 （商用企业版有效，其它版本设置此参数无效）。
```
void setForeheadLevel(float foreheadLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| foreheadLevel | float | 发际线级别，取值范围-9 - 9；0表示关闭，9表示效果最明显。 |

### setEyeDistanceLevel
设置眼距 （商用企业版有效，其它版本设置此参数无效）。
```
void setEyeDistanceLevel(float eyeDistanceLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eyeDistanceLevel  |float | 眼距级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。 |

### setEyeAngleLevel
设置眼角调整级别 （商用企业版有效，其它版本设置此参数无效）。
```
void setEyeAngleLevel(float eyeAngleLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eyeAngleLevel | float | 眼角调整级别，取值范围-9 - 9；0表示关闭，9表示效果最明显。 |

### setMouthShapeLevel
设置嘴型调整级别（商用企业版有效，其它版本设置此参数无效）。

```
void setMouthShapeLevel(float mouthShapeLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mouthShapeLevel  | float | 嘴型级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。 |

### setNoseWingLevel 
设置鼻翼调整级别（商用企业版有效，其它版本设置此参数无效）。
```
void setNoseWingLevel(float noseWingLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| noseWingLevel | float | 鼻翼调整级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。|

### setNosePositionLevel
设置鼻子位置 （商用企业版有效，其它版本设置此参数无效）。
```
void setNosePositionLevel(float nosePositionLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nosePositionLevel | float | 鼻子位置级别，取值范围-9 - 9；0表示关闭，小于0表示抬高，大于0表示降低。 |

### setLipsThicknessLevel
设置嘴唇厚度 （商用企业版有效，其它版本设置此参数无效）。

```
void setLipsThicknessLevel(float lipsThicknessLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| lipsThicknessLevel | float | 嘴唇厚度级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。 |

### setFaceBeautyLevel
设置脸型 （商用企业版有效，其它版本设置此参数无效）。
```
void setFaceBeautyLevel(int faceBeautyLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceBeautyLevel | int | 脸型级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setMotionTmpl

选择使用哪一款 AI 动效挂件（商业版有效，其它版本设置此参数无效）。
```
void setMotionTmpl(String motionPath)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| motionPath | String | 动效所在路径。 |


### setMotionMute

设置动效静音（商业版有效，其它版本设置此参数无效）。有些挂件本身会有声音特效，通过此 API 可以关闭这些特效播放时所带的声音效果。
```
void setMotionMute(boolean motionMute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| motionMute | boolean | true 表示静音；false 表示不静音。 |




