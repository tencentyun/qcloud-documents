腾讯特效 SDK Flutter版本核心接口类 `TencentEffectApi`，更新美颜数值、调用动效等功能。

## Public 成员函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [initXmagic](#initxmagic)                                    | 初始化美颜数据，使用美颜前必须先调用此方法                    |
| [setLicense](#setlicense)                                    | 进行美颜授权                                                 |
| [setXmagicLogLevel](#setxmagicloglevel)                      | 设置 SDK 的 log 等级，建议开发调试时设为 Log.DEBUG，正式发布时设置为 Log.WARN，如果正式发布设置为 Log.DEBUG，大量的日志会影响性能  |
| [onResume](#onresume)                                        | 恢复渲染，页面可见时调用                                     |
| [onPause](#onpause)                                          | 暂停渲染，页面不可见时调用                                   |
| [updateProperty](#updateproperty)                            | 更新美颜属性， 可在任意线程调用                    |
| [setOnCreateXmagicApiErrorListener](#setoncreatexmagicapierrorlistener) | 设置创建美颜对象时的回调接口（如果出错会回调此接口）         |
| [setTipsListener](#settipslistener)                          | 设置动效提示语回调函数，用于将提示语展示到前端页面上                    |
| [setYTDataListener](#setytdatalistener)                      | 设置人脸点位信息等数据回调（S1-05 和 S1-06 套餐才会有回调）  |
| [setAIDataListener](#setaidatalistener)                      | 设置人脸、手势、身体检测状态回调                    |
| [isBeautyAuthorized](#isbeautyauthorized)                    | 判断当前的 lic 授权支持哪些美颜。 仅支持 BEAUTY 和 BODY_BEAUTY 类型的美颜项检测。检测后的结果会赋值到各个美颜对象 XmagicProperty.isAuth 字段中  |
| [isSupportBeauty](#issupportbeauty)                          | 判断当前机型是否支持美颜（OpenGL3.0）                    |
| [getDeviceAbilities](#getdeviceabilities)                    | 返回当前设备支持的原子能力表                                 |
| [isDeviceSupport](#isdevicesupport)                          | 将动效资源列表传入 SDK 中做检测，执行后 XmagicProperty.isSupport 字段标识该原子能力是否可用。 根据 XmagicProperty.isSupport 可 UI 层控制单击限制，或者直接从资源列表删除  |
| [getPropertyRequiredAbilities](#getpropertyrequiredabilities) | 传入一个动效资源列表，返回每一个资源所使用到的 SDK 原子能力列表  |

##  

## 成员函数说明

### initXmagic

初始化方法。
```dart
void initXmagic(String xmagicResDir,InitXmagicCallBack callBack);

typedef InitXmagicCallBack = void Function(bool reslut);
```

#### 参数
| 参数                        | 含义               |
| --------------------------- | ------------------ |
| String xmagicResDir         | 资源文件放置的目录 |
| InitXmagicCallBack callBack | 初始化回调接口     |

------

### setLicense

设置鉴权数据，进行美颜授权

```dart
  ///美颜进行鉴权处理
void setLicense(String licenseKey, String licenseUrl, LicenseCheckListener checkListener);
///授权校验的结果回调方法
typedef LicenseCheckListener = void Function(int errorCode, String msg);
```

#### 参数

| 参数                               | 含义             |
| ---------------------------------- | :--------------- |
| String licenseKey                  | 鉴权的 LicenseKey |
| String licenseUrl                  | 鉴权的 LicenseUrl |
| LicenseCheckListener checkListener | 授权结果回调接口 |

------

### setXmagicLogLevel

设置 SDK 的 log 等级

```dart
void setXmagicLogLevel(int logLevel);
```

#### 参数

| 参数         | 含义                               |
| ------------ | :--------------------------------- |
| int logLevel | 可使用 LogLevel 定义好的类型进行设置 |

------

### onResume

恢复美颜处理

```dart
void onResume();
```

### onPause

暂停美颜处理

```dart
void onPause();
```

------

### updateProperty

设置某一项美颜数值或者动效、滤镜，可在任意线程调用。

```dart
void updateProperty(XmagicProperty xmagicProperty);
```

#### 参数

| 参数                          | 含义             |
| ----------------------------- | :--------------- |
| XmagicProperty xmagicProperty | 美颜属性封装对象 |

------

### setOnCreateXmagicApiErrorListener

设置美颜对象创建时的错误回调接口

```dart
  void setOnCreateXmagicApiErrorListener(OnCreateXmagicApiErrorListener? errorListener);
///创建美颜实例时的错误回调方法
typedef OnCreateXmagicApiErrorListener = void Function(String errorMsg, int code);
```

#### 参数

| 参数                                          | 含义                           |
| --------------------------------------------- | :----------------------------- |
| OnCreateXmagicApiErrorListener? errorListener | 创建美颜对象时错误信息回调接口 |

返回错误码含义对照表：

| 错误码  | 含义                    |
| ---- | --------------------- |
| -1   | 未知错误                    |
| -100 | 3D 引擎资源初始化失败                    |
| -200 | 不支持 GAN 素材           |
| -300 | 设备不支持此素材组件          |
| -400 | 模板 JSON 内容为空           |
| -500 | SDK 版本过低              |
| -600 | 不支持分割                    |
| -700 | 不支持 OpenGL                    |
| -800 | 不支持脚本                    |
| 5000 | 分割背景图片分辨率超过 2160×3840  |
| 5001 | 分割背景图片所需内存不足                    |
| 5002 | 分割背景视频解析失败。           |
| 5003 | 分割背景视频超过200秒                    |
| 5004 | 分割背景视频格式不支持                    |

------

### setTipsListener

设置动效提示语回调函数，用于将提示语展示到前端页面上。比如某些素材会提示用户点点头、伸出手掌、比心等。

```dart
void setTipsListener(XmagicTipsListener? xmagicTipsListener);

abstract class XmagicTipsListener {
  /// 显示tips。Show the tip.
  /// @param tips tips字符串。Tip's content
  /// @param tipsIcon tips的icon。Tip's icon
  /// @param type tips类别，0表示字符串和icon都展示，1表示是pag素材只展示icon。tips category, 0 means that both strings and icons are displayed, 1 means that only the icon is displayed for the pag material
  /// @param duration tips显示时长, 毫秒。Tips display duration, milliseconds
  void tipsNeedShow(String tips, String tipsIcon, int type, int duration);

  /// *
  /// 隐藏tips。Hide the tip.
  /// @param tips tips字符串。Tip's content
  /// @param tipsIcon tips的icon。Tip's icon
  /// @param type tips类别，0表示字符串和icon都展示，1表示是pag素材只展示icon。tips category, 0 means that both strings and icons are displayed, 1 means that only the icon is displayed for the pag material
  void tipsNeedHide(String tips, String tipsIcon, int type);
}
```

#### 参数

| 参数                                  | 含义             |
| ------------------------------------- | ---------------- |
| XmagicTipsListener xmagicTipsListener | 回调函数实现类  |

------

### setYTDataListener

设置人脸点位信息等数据回调。
```dart
  ///设置人脸点位信息等数据回调（S1-05 和 S1-06 套餐才会有回调）
void setYTDataListener(XmagicYTDataListener? xmagicYTDataListener);
设置人脸信息等数据回调

abstract class XmagicYTDataListener {
  //优图AI数据回调。
  void onYTDataUpdate(String data);
}
```
onYTDataUpdate 返回 JSON string 结构，最多返回5个人脸信息：
```
{
 "face_info":[{
  "trace_id":5,
  "face_256_point":[
    180.0,
    112.2,
    ...
  ],
  "face_256_visible":[
    0.85,
    ...
  ],
  "out_of_screen":true,
  "left_eye_high_vis_ratio:1.0,
  "right_eye_high_vis_ratio":1.0,
  "left_eyebrow_high_vis_ratio":1.0,
  "right_eyebrow_high_vis_ratio":1.0,
  "mouth_high_vis_ratio":1.0
 },
 ...
 ]
}
```

#### 字段含义

| 字段                           | 类型    | 值域                           | 说明                            |
| -------------------------- |-------------------------- | --------------------------- | --------------------------- |
| trace_id                     | int   | [1,INF)                      | 人脸 ID，连续取流过程中，ID 相同的可以认为是同一张人脸  |
| face_256_point               | float | [0,screenWidth] 或 [0,screenHeight] | 共512个数，人脸256个关键点，屏幕左上角为(0,0)  |
| face_256_visible             | float | [0,1]                        | 人脸256关键点可见度                    |
| out_of_screen                | bool  | true/false                   | 人脸是否出框                    |
| left_eye_high_vis_ratio      | float | [0,1]                        | 左眼高可见度点位占比                    |
| right_eye_high_vis_ratio     | float | [0,1]                        | 右眼高可见度点位占比                    |
| left_eyebrow_high_vis_ratio  | float | [0,1]                        | 左眉高可见度点位占比                    |
| right_eyebrow_high_vis_ratio | float | [0,1]                        | 右眉高可见度点位占比                    |
| mouth_high_vis_ratio         | float | [0,1]                        | 嘴高可见度点位占比                    |

#### 参数

| 参数                                           | 含义             |
| ---------------------------------------------- | ---------------- |
| XmagicYTDataListener      xmagicYTDataListener | 回调函数实现类  |

------

### setAIDataListener

检测到人脸、身体、手势时，会回调这些部位的点位信息

```dart
void setAIDataListener(XmagicAIDataListener? aiDataListener);
  
abstract class XmagicAIDataListener {
  void onFaceDataUpdated(String faceDataList);

  void onHandDataUpdated(String handDataList);

  void onBodyDataUpdated(String bodyDataList);
}
```

------

### isBeautyAuthorized

判断当前的 License 授权支持哪些美颜或美体项。 仅支持 BEAUTY 和 BODY_BEAUTY 类型的美颜项检测。检测后的结果会赋值到各个美颜对象 `XmagicProperty.isAuth` 字段中。如果 isAuth 字段为 false，可以在 UI 上屏蔽这些项的入口。

```
Future<List<XmagicProperty>> isBeautyAuthorized(
      List<XmagicProperty> properties);
```

#### 参数

| 参数                            | 含义               |
| ------------------------------- | ------------------ |
| List&lt;XmagicProperty> properties | 需要检测的美颜项  |

------

### isSupportBeauty

判断当前机型是否支持美颜（OpenGL3.0）。

```dart
  Future&lt;bool> isSupportBeauty();
```

#### 返回

返回值 bool：是否支持支持美颜。

------

### getDeviceAbilities

返回当前设备支持的原子能力表。与 getPropertyRequiredAbilities 方法搭配使用.

```
  Future<Map<String, bool>> getDeviceAbilities();
```

#### 返回

返回值 `Map&lt;String,bool>`：

- key：原子能力名（与素材能力名字对应）。
- value：当前设备是否支持。

------

### getPropertyRequiredAbilities

传入一个动效资源列表，返回每一个资源所使用到的 SDK 原子能力列表。
方法的使用场景为：
您购买或制作了若干款动效素材，调用这个方法，会返回每一个素材需要使用的原子能力列表。例如素材1需要使用能力 A、B、C，素材2需要使用能力 B、C、D，然后您把这样的能力列表保持在服务器上。之后，当用户要从服务器下载动效素材时，用户先通过 getDeviceAbilities 方法获取他手机具备的原子能力列表（比如这台手机具备能力 A、B、C，但不具备能力 D），把他的能力列表传给服务器，服务器判断该设备不具备能力 D，因此不给该用户下发素材2。

```dart
Future<Map<XmagicProperty, List<String>?>> getPropertyRequiredAbilities(
    List<XmagicProperty> assetsList);
```

#### 参数

| 参数                             | 含义               |
| ------------------------------ | ---------------- |
| List&lt;XmagicProperty> assetsList | 需要检测原子能力的动效资源列表  |

#### 返回

返回值 Map&lt;XmagicProperty, List&lt;String>?> ：

- key：动效资源素材实体类。
- value：所使用到的原子能力列表。

------

###  isDeviceSupport

将动效资源列表传入 SDK 中做检测，执行后 `XmagicProperty.isSupport` 字段标识该素材是否可用。根据`XmagicProperty.isSupport` 可 UI 层控制单击限制，或者直接从资源列表删除。

```dart
 Future&lt;List<XmagicProperty>> isDeviceSupport(List<XmagicProperty> assetsList);
```

#### 参数

| 参数                            | 含义                     |
| ------------------------------- | ------------------------ |
| List&lt;XmagicProperty> assetsList | 需要检测的动效素材列表  |








