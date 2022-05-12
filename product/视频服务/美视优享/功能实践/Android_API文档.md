腾讯特效 SDK 核心接口类 `XmagicApi.java`，用于初始化 SDK、更新美颜数值、调用动效等功能。

## Public 成员函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [XmagicApi](#xmagicapi)                                      | 构造函数。                                                   |
| [updateProperty](#updateproperty)                            | 更新属性， 可在任意线程调用。                                |
| [updateProperties](#updateproperties)                        | 更新属性，可在任意线程调用。                                 |
| [setTipsListener](#settipslistener)                          | 设置动效提示语回调函数，用于将提示语展示到前端页面上。       |
| [setYTDataListener](#setytdatalistener)                      | 设置人脸点位信息等数据回调（S1-05 和 S1-06 套餐才会有回调）。 |
| [setAIDataListener](#setaidatalistener)                      | 设置人脸、手势、身体检测状态回调。                           |
| [onPause](#onpause)                                          | 暂停声音播放，可与 Activity onPause 生命周期绑定。           |
| [onResume](#onresume)                                        | 恢复渲染，可与 Activity onResume 生命周期绑定。              |
| [onDestroy](#ondestroy)                                      | 销毁 xmagic，需要在 GL 线程中调用                            |
| [process](#process)                                          | SDK 渲染接受数据的方法，可在相机数据回调函数内使用。         |
| [onPauseAudio](#onpauseaudio)                                | 当仅需要停止音频，但不需要释放 GL 线程时调用此函数。         |
| [sensorChanged](#sensorchanged)                              | 用于判断当前手机旋转的角度，从而调整 AI 识别人脸的判断角度依据。 |
| [isDeviceSupport](#isdevicesupport)                          | 将动效资源列表传入 SDK 中做检测，执行后 XmagicProperty.isSupport 字段标识该原子能力是否可用。 根据 XmagicProperty.isSupport 可 UI 层控制单击限制，或者直接从资源列表删除。 |
| [getPropertyRequiredAbilities](#getpropertyrequiredabilities) | 传入一个动效资源列表，返回每一个资源所使用到的 SDK 原子能力列表。 |
| [getDeviceAbilities](#getdeviceabilities)                    | 返回当前设备支持的原子能力表                                 |
| [isSupportBeauty](#issupportbeauty)                          | 判断当前机型是否支持美颜（OpenGL3.0）。                      |
| [isBeautyAuthorized](#isbeautyauthorized)                    | 判断当前的 lic 授权支持哪些美颜。 仅支持 BEAUTY 和 BODY_BEAUTY 类型的美颜项检测。检测后的结果会赋值到各个美颜对象 XmagicProperty.isAuth 字段中。 |
| [setXmagicStreamType](#setxmagicstreamtype)                  | 设置输入数据类型，默认 Android camera 数据流。               |
| [setXmagicLogLevel](#setxmagicloglevel)                      | 设置 SDK 的 log 等级，建议开发调试时设为 `Log.DEBUG`，正式发布时设置为 `Log.WARN`，如果正式发布设置为 `Log.DEBUG`，大量的日志会影响性能。<br><b>在 new XmagicApi() 之后调用。</b> |

## 静态函数

| API               | 描述         |
| ----------------- | ---------- |
| [setLibPathAndLoad](#setlibpathandload) | 设置 libPath。 |

## Public 成员函数说明

### XmagicApi

构造函数。
```
XmagicApi(Context context, String resDir)
XmagicApi(Context context, String resDir,OnXmagicPropertyErrorListener xmagicPropertyErrorListener)
```

#### 参数
<table>
<thead>
<tr>
<th>参数</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>Context context</td>
<td>上下文。</td>
</tr>
<tr>
<td>String resDir</td>
<td>资源文件目录。<ul style="margin:0">
<li>如果 SDK 资源文件是内置在 assets 的，那么首次使用 SDK 之前，需要把资源 copy 到 App 的私有目录：先通过 <code>XmagicResParser.setResPath(new File(getFilesDir(), "xmagic").getAbsolutePath())</code> 设置资源路径，再通过 <code>XmagicResParser.copyRes(getApplicationContext())</code> 完成资源拷贝，详见 Demo 的 <code>LaunchActivity.java</code>。</li>
<li>如果 SDK 资源文件是联网下载的，下载成功后，通过 <code>XmagicResParser.setResPath(validAssetsDirectory)</code> 设置资源路径</li>
<li>通过 <code>XmagicResParser.getResPath()</code> 获取先前设置的路径。</li></ul></td>
</tr>
<tr>
<td>OnXmagicPropertyErrorListener xmagicPropertyErrorListener</td>
<td>错误回调接口。</td>
</tr>
</tbody></table>
返回错误码含义对照表：

| 错误码  | 含义                    |
| ---- | --------------------- |
| -1   | 未知错误。                 |
| -100 | 3D 引擎资源初始化失败。          |
| -200 | 不支持 GAN 素材。             |
| -300 | 设备不支持此素材组件。           |
| -400 | 模板 JSON 内容为空。           |
| -500 | SDK 版本过低。              |
| -600 | 不支持分割。                |
| -700 | 不支持 OpenGL。            |
| -800 | 不支持脚本。                |
| 5000 | 分割背景图片分辨率超过 2160×3840。 |
| 5001 | 分割背景图片所需内存不足。         |
| 5002 | 分割背景视频解析失败。           |
| 5003 | 分割背景视频超过200秒。         |
| 5004 | 分割背景视频格式不支持。          |

------

### updateProperty

更改某一项美颜数值或者动效、滤镜，可在任意线程调用。

```
void updateProperty(XmagicProperty<?> p) 
```

#### 参数
<table>
<thead>
<tr>
<th>参数</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>XmagicProperty&lt;?&gt; p</td>
<td>腾讯特效数据实体类。
<ul style="margin:0"><li>以"磨皮"为例，可以按如下方式 new 一个实例：<br><code>new XmagicProperty&lt;&gt;(Category.BEAUTY,  null,  null,  BeautyConstant.BEAUTY_SMOOTH, new XmagicPropertyValues(0, 100, 50, 0, 1)));</code>。</li><li>以“2D 动效兔兔酱”为例，可以按如下方式 new 一个实例：<br><code>new XmagicProperty&lt;&gt;(Category.MOTION, "video_tutujiang" ,  "动效的文件路径",  null, null);</code>。<br>更多的例子，请参考 Demo 工程的 <code>XmagicResParser.java</code>。</li></ul></td>
</tr>
</tbody></table>

***

### updateProperties

批量更改某一项美颜数值或者动效、滤镜，可在任意线程调用。

```
void updateProperties(List<XmagicProperty<?>> properties)
```

#### 参数

| 参数                                | 含义                         |
| ----------------------------------- | ---------------------------- |
| (List&lt;XmagicProperty&lt;?>> properties | 详见 updateProperty 方法的说明。 |

***

### setTipsListener

设置动效提示语回调函数，用于将提示语展示到前端页面上。比如某些素材会提示用户点点头、伸出手掌、比心等。

```
void setTipsListener(XmagicApi.XmagicTipsListener effectTipsListener) 
```

#### 参数

| 参数                                            | 含义                                 |
| ----------------------------------------------- | ------------------------------------ |
| XmagicApi.XmagicTipsListener effectTipsListener | 回调函数实现类，回调不一定在主线程。 |

------

### setYTDataListener
设置人脸点位信息等数据回调。
```
void setYTDataListener(XmagicApi.XmagicYTDataListener ytDataListener)
设置人脸信息等数据回调

public interface XmagicYTDataListener {
    void onYTDataUpdate(String data)
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
| trace_id                     | int   | [1,INF)                      | 人脸 ID，连续取流过程中，ID 相同的可以认为是同一张人脸。 |
| face_256_point               | float | [0,screenWidth] 或 [0,screenHeight] | 共512个数，人脸256个关键点，屏幕左上角为(0,0)。 |
| face_256_visible             | float | [0,1]                        | 人脸256关键点可见度。                  |
| out_of_screen                | bool  | true/false                   | 人脸是否出框。                       |
| left_eye_high_vis_ratio      | float | [0,1]                        | 左眼高可见度点位占比。                   |
| right_eye_high_vis_ratio     | float | [0,1]                        | 右眼高可见度点位占比。                   |
| left_eyebrow_high_vis_ratio  | float | [0,1]                        | 左眉高可见度点位占比。                   |
| right_eyebrow_high_vis_ratio | float | [0,1]                        | 右眉高可见度点位占比。                   |
| mouth_high_vis_ratio         | float | [0,1]                        | 嘴高可见度点位占比。                    |

#### 参数

| 参数                                            | 含义       |
| --------------------------------------------- | -------- |
| XmagicApi.XmagicYTDataListener ytDataListener | 回调函数实现类。 |

------

### setAIDataListener

检测到人脸、身体、手势时，会回调这些部位的点位信息

```
public interface OnAIDataListener {

    void onFaceDataUpdated(List<FaceData> faceDataList);
    void onHandDataUpdated(List<HandData> handDataList);
    void onBodyDataUpdated(List<BodyData> bodyDataList);

}
```

### onPause

暂停渲染，可与 Activity onPause 生命周期绑定，目前内部仅调用`onPauseAudio`。

```
void onPause() 
```

------

### onResume

恢复渲染，可与 Activity onResume 生命周期绑定。

```
void onResume() 
```

------

### onDestroy

清理GL线程资源，需要在 GL 线程内调用。示例代码：

```java
//示例代码见 MainActivity.java
glSurfaceView.queueEvent(() -> {
                if (mXmagicApi != null) {
                    mXmagicApi.onPause();
                    mXmagicApi.onDestroy();
                }
            });
            
//示例代码见 ImageInputActivity.java
@Override
protected void onDestroy() {

    if (mHandler != null) {
        mHandler.destroy(() -> {
            if (mXmagicApi != null) {
                mXmagicApi.onPause();
                mXmagicApi.onDestroy();
        		}
    		});
    		mHandler.waitDone();
    }

    XmagicPanelDataManager.getInstance().clearData();
    super.onDestroy();
}
```

### process

SDK 渲染接受数据的方法，可在相机数据回调函数内使用。

```
//渲染纹理
int process(int srcTextureId, int srcTextureWidth, int srcTextureHeight) 
//渲染bitmap
Bitmap process(Bitmap bitmap, boolean needReset){
```

#### 参数

| 参数                   | 含义                                                         |
| ---------------------- | ------------------------------------------------------------ |
| int srcTextureId       | 需要被渲染的纹理。                                           |
| id int srcTextureWidth | 需要被渲染的纹理宽。                                         |
| int srcTextureHeight   | 需要被渲染的纹理高。                                         |
| Bitmap bitmap          | 建议最大尺寸 2160×4096。超过这个尺寸的图片人脸识别效果不佳或无法识别到人脸，同时容易引起 OOM 问题，建议把大图缩小后再传入。 |
| boolean needReset      | <li/>切换图片。<li/>首次使用分割。<li/>首次使用动效。<li/>首次使用美妆。<br>这几种场景 needReset 设置为 true。 |

------

### onPauseAudio

当仅需要停止音频，但不需要释放 GL 线程时调用此函数。

```
void onPauseAudio() 
```

------

### sensorChanged

用于判断当前手机旋转的角度，从而调整 AI 识别人脸的判断角度依据，需在陀螺仪传感器回调函数内调用。

```
void sensorChanged(SensorEvent event, Sensor accelerometer) 
```

#### 参数

| 参数                   | 含义                                   |
| -------------------- | ------------------------------------ |
| SensorEvent event    | 陀螺仪传感器回调函数 `onSensorChanged` 返回的事件实体类。 |
| Sensor accelerometer | 陀螺仪传感器示例。                            |

------

### isDeviceSupport

将动效资源列表传入 SDK 中做检测，执行后 `XmagicProperty.isSupport` 字段标识该素材是否可用。根据`XmagicProperty.isSupport` 可 UI 层控制单击限制，或者直接从资源列表删除。

```
void isDeviceSupport(List<XmagicProperty<?>> assetsList)
```

#### 参数

| 参数                                 | 含义           |
| ---------------------------------- | ------------ |
| List&lt;XmagicProperty&lt;?>> assetsList | 需要检测的动效素材列表。 |

------

### getPropertyRequiredAbilities

传入一个动效资源列表，返回每一个资源所使用到的 SDK 原子能力列表。
方法的使用场景为：
您购买或制作了若干款动效素材，调用这个方法，会返回每一个素材需要使用的原子能力列表。例如素材1需要使用能力 A、B、C，素材2需要使用能力 B、C、D，然后您把这样的能力列表保持在服务器上。之后，当用户要从服务器下载动效素材时，用户先通过 getDeviceAbilities 方法获取他手机具备的原子能力列表（比如这台手机具备能力 A、B、C，但不具备能力 D），把他的能力列表传给服务器，服务器判断该设备不具备能力 D，因此不给该用户下发素材2。

#### 参数

| 参数                             | 含义               |
| ------------------------------ | ---------------- |
| List&lt;XmagicProperty&lt;?>> assets | 需要检测原子能力的动效资源列表。 |

#### 返回

返回值 `Map<XmagicProperty<?>,ArrayList<String>>` ：

- key：动效资源素材实体类。
- value：所使用到的原子能力列表。

------

### getDeviceAbilities

返回当前设备支持的原子能力表。与 getPropertyRequiredAbilities 方法搭配使用，详见 getPropertyRequiredAbilities 的说明。

```
Map<String,Boolean> getDeviceAbilities() 
```

#### 返回

返回值 `Map<String,Boolean>`：
- key：原子能力名（与素材能力名字对应）。
- value：当前设备是否支持。

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

判断当前的 License 授权支持哪些美颜或美体项。 仅支持 BEAUTY 和 BODY_BEAUTY 类型的美颜项检测。检测后的结果会赋值到各个美颜对象 `XmagicProperty.isAuth` 字段中。如果 isAuth 字段为 false，可以在 UI 上屏蔽这些项的入口。

```
void isBeautyAuthorized(List<XmagicProperty<?>> properties) 
```

#### 参数

| 参数                                 | 含义        |
| ---------------------------------- | --------- |
| List&lt;XmagicProperty&lt;?>> properties | 需要检测的美颜项。 |

------

### setXmagicStreamType

设置输入数据类型，默认 Android camera 数据流（XmagicApi.PROCESS_TYPE_CAMERA_STREAM）。

```
void setXmagicStreamType(int type)
```

#### 参数

| 参数       | 含义                                                                                                                                        |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| int type | 数据源类型，有以下两种选择：<ul style="margin:0"><li/><code>XmagicApi.PROCESS_TYPE_CAMERA_STREAM</code>：相机数据源。<li/><code>XmagicApi.PROCESS_TYPE_PICTURE_DATA</code>：图片数据源。</ul> |

------

## 静态函数说明

### setLibPathAndLoad

设置 so 的路径，并触发加载。如果 so 是内置在 assets 里的，则无需调用此方法。如果 so 是动态下载的，则需要在鉴权和 `new XmagicApi` 之前调用。 
- 传入 null ：表示从默认路径加载 so，请确保 so 是内置在 APK 包里的。
- 传入非 null：如 `data/data/包名/files/xmagic_libs`，将从这个目录去加载 so。

```
static boolean setLibPathAndLoad(String path) 
```

#### 参数

| 参数          | 含义      |
| ----------- | ------- |
| String path | so 库存放路径。 |

