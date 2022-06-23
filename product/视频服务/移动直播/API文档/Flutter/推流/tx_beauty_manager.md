
美颜、美容、动效挂件类基础函数。

### setBeautyStyle 

设置美颜类型。 
```dart
  Future<void> setBeautyStyle(TXBeautyStyle beautyStyle)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| beautyStyle | TXBeautyStyle | 美颜风格，tXBeautyStyleSmooth表示光滑；tXBeautyStyleNature表示自然；tXBeautyStylePitu表示朦胧。 |

### setBeautyLevel

设置美颜级别。
```dart
  Future<void> setBeautyLevel(int beautyLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| beautyLevel | int | 美颜级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setWhitenessLevel

设置美白级别。
```dart
  Future<void> setWhitenessLevel(int whitenessLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| whitenessLevel | int | 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setRuddyLevel

设置红润级别。
```dart
  Future<void> setRuddyLevel(int ruddyLevel) 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| ruddyLevel | int | 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

### setFilter

设置指定素材滤镜特效。
```
  Future<int?> setFilter(String assetUrl) 
```

>? assetUrl可以为flutter中定义的asset资源地址如'images/watermark_img.png'，也可以为网络图片地址

***

### setFilterStrength

设置滤镜浓度
```dart
  Future<void> setFilterStrength(double strength)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| strength | double | 取值范围从0到1，越大滤镜效果越明显，默认值为0.5。 |


 

