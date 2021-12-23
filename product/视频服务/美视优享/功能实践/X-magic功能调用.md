腾讯特效 SDK 核心接口类。用于初始化 SDK、更新美颜数值、调用动效等功能。

## Public 成员函数

| API                                                          | 描述                                                         |
| ----------- | ----------- |
| [XmagicApi](#xmagicapi)                                      | 构造函数。                                                   |
| [updateProperty](#updateproperty)                            | 更新属性, 可在任意线程调用。                                 |
| [updateProperties](#updateproperties)                        | 更新属性, 可在任意线程调用。                                 |
| [setTipsListener](#settipslistener)                          | 设置动效提示语回调函数，用于将提示语展示到前端页面上。       |
| [setYTDataListener](#setytdatalistener)                      | 设置人脸信息等数据回调。                                     |
| [onPause](#onpause)                                          | 暂停声音播放，可与 Activity onPause 生命周期绑定。           |
| [onResume](#onresume)                                        | 恢复渲染，可与 Activity onPause 生命周期绑定。               |
| [process](#process)                                          | SDK 渲染接受数据的方法。可在相机数据回调函数内使用。         |
| [onPauseAudio](#onpauseaudio)                                | 当仅需要停止音频，但不需要释放 GL 线程时调用此函数。         |
| [onPauseGL](#onpausegl)                                      | 当仅需要释放 GL 线程资源，但需要停止音频时调用此函数。       |
| [sensorChanged](#sensorchanged)                              | 用于判断当前手机旋转的角度，从而调整 AI 识别人脸的判断角度依据。 |
| [isDeviceSupport](#isdevicesupport)                          | 本地集成资源检测兼容性方案：将动效资源列表传入 SDK 中做检测，执行后XmagicProperty.isSupport 字段标识该原子能力是否可用。 |
| [getPropertyRequiredAbilities](#getpropertyrequiredabilities) | 网络获取资源检测兼容性方案：传入一个动效资源列表，返回每一个资源所使用到的 SDK 原子能力列表。 |
| [getDeviceAbilities](#getdeviceabilities)                    | 网络获取资源检测兼容性方案：返回所有原子能力在当前设备是否支持的配置表。 |
| [setXmagicErrorListener](#setxmagicerrorlistener)            | SDK 运行时的各种类型异常返回监听。                           |
| [isSupportBeauty](#issupportbeauty)                          | 判断当前机型是否支持美颜（OpenGL3.0）。                      |
| [isBeautyAuthorized](#isbeautyauthorized)                    | 判断当前的 lic 授权支持哪些美颜。                            |
| [setXmagicStreamType](#setxmagicstreamtype)                  | 设置输入数据类型，默认 Android camera 数据流。               |
| [checkBitmapLegal](#checkbitmaplegal)                        | 输入一张需要美颜的图片。                                     |

## 静态函数

| API               | 描述           |
| ----------------- | -------------- |
| setLibPathAndLoad | 设置 libPath。 |



## Public 成员函数说明

### XmagicApi

构造函数。

```
void XmagicApi(Context context, String resDir) 
```

#### 参数

| 参数            | 含义    |
| --------------- | ----------- |
| Context context | 上下文。                         |
| String resDir   | 资源文件目录，V1 版本固定写法 `XmagicResParser.getResPath()`。 |

------

### updateProperty

更改某一项美颜数值或者动效、滤镜。

```
void updateProperty(XmagicProperty<?> p) 
```

#### 参数

| 参数                | 含义    |
| ------------------- | ----------- |
| XmagicProperty<?> p | 美颜特效数据实体类，无需用户手动构造。可通过 `XmagicResParser.getProperties()` 获取所有美颜特效实体类。 |

------

### updateProperties

批量更改某一项美颜数值或者动效、滤镜。

```
void updateProperties(List<XmagicProperty<?>> properties)
```

#### 参数

| 参数    | 含义    |
| -----------------| ----------- |
| (List<XmagicProperty<?>> properties | 美颜特效数据列表，无需用户手动构造。可通过 `XmagicResParser.getProperties()` 获取所有美颜特效实体类。 |

***
### setTipsListener

设置动效提示语回调函数，用于将提示语展示到前端页面上。

```
void setTipsListener(XmagicApi.XmagicTipsListener effectTipsListener) 
```

#### 参数

| 参数                | 含义             |
| --------------- | ---------------- |
| XmagicApi.XmagicTipsListener effectTipsListener | 回调函数实现类。 |

------

### setYTDataListener

```java
void setYTDataListener(XmagicApi.XmagicYTDataListener ytDataListener)
设置人脸信息等数据回调

public interface XmagicYTDataListener {
    void onYTDataUpdate(String data)
}
onYTDataUpdate返回json string结构，最多返回5个人脸信息
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

| 字段                         | 类型  | 值域                          | 说明                       |
| :--------------------------- | :---- | :---------------------------- | :----------------------------------------------------- |
| trace_id                     | int   | [1,INF)                       | 人脸 ID，连续取流过程中，id相同的可以认为是同一张人脸。 |
| face_256_point               | float | [0,screenWidth] 或[0,screenHeight] | 共512个数，人脸256个关键点，屏幕左上角为(0,0)。        |
| face_256_visible             | float | [0,1]                         | 人脸256关键点可见度。      |
| out_of_screen                | bool  | true/false                    | 人脸是否出框。             |
| left_eye_high_vis_ratio      | float | [0,1]                         | 左眼高可见度点位占比。     |
| right_eye_high_vis_ratio     | float | [0,1]                         | 右眼高可见度点位占比。     |
| left_eyebrow_high_vis_ratio  | float | [0,1]                         | 左眉高可见度点位占比。     |
| right_eyebrow_high_vis_ratio | float | [0,1]                         | 右眉高可见度点位占比。     |
| mouth_high_vis_ratio         | float | [0,1]                         | 嘴高可见度点位占比。       |

#### 参数

| 参数              | 含义             |
| ------------- | ---------------- |
| XmagicApi.XmagicYTDataListener ytDataListener | 回调函数实现类。 |

------

### onPause

暂停渲染，可与 Activity onPause 生命周期绑定，内部调用 `onPauseAudio`，`onPauseGL`。

```
void onPause() 
```

------

### onResume

恢复渲染，可与 Activity onPause 生命周期绑定。

```
void onResume() 
```

------

### process

SDK 渲染接受数据的方法，可在相机数据回调函数内使用。

```
int process(int srcTextureId, int srcTextureWidth, int srcTextureHeight) 
```

#### 参数

| 参数                   | 含义                 |
| ---------------------- | -------------------- |
| int srcTextureId       | 需要被渲染的纹理。   |
| id int srcTextureWidth | 需要被渲染的纹理宽。 |
| int srcTextureHeight   | 需要被渲染的纹理高。 |

------

### onPauseAudio

当仅需要停止音频，但不需要释放 GL 线程时调用此函数。

```
void onPauseAudio() 
```

------

### onPauseGL

当仅需要释放 GL 线程资源，但需要停止音频时调用此函数。

```
void onPauseGL() 
```

------

### sensorChanged

用于判断当前手机旋转的角度，从而调整 AI 识别人脸的判断角度依据。

```
void sensorChanged(SensorEvent event, Sensor accelerometer) 
```

#### 参数

| 参数                 | 含义                        |
| -------------------- | ----------------------- |
| SensorEvent event    | 陀螺仪传感器回调函数 `onSensorChanged` 返回的事件实体类。 |
| Sensor accelerometer | 陀螺仪传感器示例。          |

------

### isDeviceSupport

**本地集成资源检测兼容性方案**：将动效资源列表传入 SDK 中做检测，执行后 `XmagicProperty.isSupport` 字段标识该原子能力是否可用。针对不支持本设备的设备进行检索，根据 `XmagicProperty.isSupport` 可 UI 层控制单击限制，或者直接从资源列表删除。

```
void isDeviceSupport(List<XmagicProperty<?>> assetsList)
```

#### 参数

| 参数      | 含义                     |
| ----------------- | ------------------------ |
| List<XmagicProperty<?>> assetsList | 需要检测的动效素材列表。 |

------

### getPropertyRequiredAbilities

**网络获取资源检测兼容性方案**：传入一个动效资源列表，返回每一个资源所使用到的 SDK 原子能力列表。宿主层可将返回的数据生成一个协议文件，上传至服务端，用于当前设备是否支持对应的原子能力比对。

> !如果对应的特效资源返回的能力列表是一个空列表，则表示当前素材不存在兼容性问题，默认兼容一切设备。

```
Map<XmagicProperty<?>,ArrayList<String>> getPropertyRequiredAbilities(List<XmagicProperty<?>> assets) 
```

#### 参数

| 参数                           | 含义    |
| ------------- | --------------- |
| List<XmagicProperty<?>> assets | 需要检测原子能力的动效资源列表。 |

#### 返回

返回值 `Map<XmagicProperty<?>,ArrayList<String>> `：

- key：动效资源素材实体类。
- value：所使用到的原子能力列表。


------

### getDeviceAbilities

**网络获取资源检测兼容性方案**：返回所有原子能力在当前设备是否支持的配置表，宿主层可将返回的数据传至服务端，用于判断当前设备支持哪些动效素材。

```
Map<String,Boolean> getDeviceAbilities() 
```

#### 返回

返回值 `Map<String,Boolean>`：

- key：原子能力名（与素材能力名字对应）。
- value：当前设备是否支持。


------

### setXmagicErrorListener

SDK 运行时的各种类型异常返回监听。

```
void setXmagicErrorListener(OnXmagicErrorListener errorListener)
```

#### 参数

| 参数    | 含义             |
| ------------------ | ---------------- |
| OnXmagicErrorListener errorListener | 回调函数实现类。 |

返回错误码含义对照表：

| 错误码 | 含义     |
| ------ | ---------------- |
| -1     | 未知错误。                        |
| -100   | 3D 引擎资源初始化失败。           |
| -200   | 不支持 GAN 素材。                 |
| -300   | 设备不支持此素材组件。            |
| -400   | 模板 Json 内容为空。             |
| -500   | SDK 版本过低。                    |
| -600   | 不支持分割。                      |
| -700   | 不支持 OpenGL。                   |
| -800   | 不支持脚本。                      |
| 5000   | 分割背景图片分辨率超过2160*3840。 |
| 5001   | 分割背景图片所需内存不足。        |
| 5002   | 分割背景视频解析失败。            |
| 5003   | 分割背景视频超过200秒。           |
| 5004   | 分割背景视频格式不支持。          |

------

### isSupportBeauty

判断当前机型是否支持美颜（OpenGL3.0）。

```
boolean isSupportBeauty() 
```

#### 返回

返回值 boolean：是否支持支持美颜。

------

### isBeautyAuthorized

判断当前的 lic 授权支持哪些美颜。 仅支持 BEAUTY 类型的美颜项检测。检测后的结果会赋值到各个美颜对象 `XmagicProperty.isAuthz` 字段中。

```
void isBeautyAuthorized(List<XmagicProperty<?>> properties) 
```

#### 参数

| 参数      | 含义               |
| ----------------- | ------------------ |
| List<XmagicProperty<?>> properties | 需要检测的美颜项。 |

------

### setXmagicStreamType

设置输入数据类型，默认 Android camera 数据流（XmagicApi.PROCESS_TYPE_CAMERA_STREAM）。

```
void setXmagicStreamType(int type)
```

#### 参数

| 参数     | 含义    |
| -------- | ----------- |
| int type | 数据源类型，有以下两种选择：<ul style="margin:0"><li/>'XmagicApi.PROCESS_TYPE_CAMERA_STREAM//相机数据源<li/>XmagicApi.PROCESS_TYPE_PICTURE_DATA//图片数据源'</ul> |

------

### checkBitmapLegal

输入一张需要美颜的图片。调用此接口前需要先调用 setXmagicStreamType，将数据源设置成 PROCESS_TYPE_PICTURE_DATA。

```
int checkBitmapLegal(Bitmap bitmap)
```

#### 参数

| 参数          | 含义             |
| ------------- | ---------------- |
| Bitmap bitmap | 需要美颜的图片。 |

#### 返回

返回值 int（输入图合法性）：

- 0：合法。
- -1：为空。
- -2：宽高不合法。

---

## 静态函数说明

### setLibPathAndLoad

设置 libPath。需要在 `new XmagicApi` 之前调用。否则将从默认路径加载 libs。该接口用于 so 库外部存放集成场景下使用。 

- 传入 null ：表示从默认路径加载 so，请确保 so 在包里是存在的。
- 传入非 null：如 `data/data/包名/files/xmagic_libs`，那么将从这个目录去加载 so。

```
static boolean setLibPathAndLoad(String path) 
```

#### 参数

| 参数        | 含义            |
| ----------- | --------------- |
| String path | so 库存放路径。 |