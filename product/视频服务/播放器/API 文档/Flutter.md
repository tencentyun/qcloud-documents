## SuperPlayerPlugin类

### setGlobalLicense

**说明**

设置 License

申请到 License 后，通过下面的接口初始化 License，建议在启动的时候进行，如果没有设置 License，将会播放视频失败。

**接口**

```dart
static Future<void> setGlobalLicense(String licenceUrl, String licenceKey) async;
```

**参数说明**

| 参数名     | 类型   | 描述           |
| ---------- | ------ | -------------- |
| licenceUrl | String | licence 的 url |
| licenceKey | String | licence 的 key |

**返回值**

无


### createVodPlayer

**说明**

创建原生层的点播播放器实例，如果使用`TXVodPlayerController`，其中已经集成，不需要额外创建。

**接口**

```dart
static Future<int?> createVodPlayer() async;
```

**参数说明**

无

**返回值**

| 返回值 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| playerId | int | 播放器ID |


### createLivePlayer

**说明**

创建原生层的点播播放器实例，如果使用`TXVodPlayerController`，其中已经集成，不需要额外创建

**接口**

```dart
static Future<int?> createLivePlayer() async;
```

**参数说明**

无

**返回值**

| 返回值 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| playerId | int | 播放器ID |


### setConsoleEnabled

**说明**

打开或关闭播放器原生 log 输出

**接口**

```dart
static Future<int?> setConsoleEnabled() async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| enabled | bool | 开启或关闭播放器 log |

**返回值**

无


### releasePlayer

**说明**

释放对应播放器的资源。

**接口**

```dart
static Future<int?> releasePlayer(int? playerId) async;
```

**参数说明**

无

**返回值**

无


### setGlobalMaxCacheSize

**说明**

设置播放引擎的最大缓存大小。设置后会根据设定值自动清理 Cache 目录的文件

**接口**

```dart
static Future<void> setGlobalMaxCacheSize(int size) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| size | int | 最大缓存大小（单位：MB) |

**返回值**

无


### setGlobalCacheFolderPath

**说明**

该缓存路径默认设置到 App 沙盒目录下，参数只需要传递相对缓存目录即可，不需要传递整个绝对路径。

**接口**

```dart
static Future<bool> setGlobalCacheFolderPath(String postfixPath) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| postfixPath | String | 缓存目录,该缓存路径默认设置到 app 沙盒目录下，postfixPath 只需要传递相对缓存目录即可，不需要传递整个绝对路径。Android 平台：视频将会缓存到 sdcard的Android/data/your-pkg-name/files/testCache 目录。iOS 平台视频将会缓存到沙盒的 Documents/testCache 目录。 |

**返回值**

无


### setLogLevel

**说明**

设置log输出级别

**接口**

```dart
static Future<void> setLogLevel(int logLevel) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| logLevel | int | 0:输出所有级别的 log </br> 1:输出 DEBUG,INFO,WARNING,ERROR 和 FATAL 级别的 log </br> 2:输出 INFO,WARNNING,ERROR 和 FATAL 级别的 log </br> 3:输出 WARNNING,ERROR 和 FATAL 级别的log </br> 4:输出 ERROR 和 FATAL 级别的log </br> 5:只输出 FATAL 级别的log </br> 6:不输出任何 sdk log|

**返回值**

无


### setBrightness

**说明**

设置亮度，仅适用于当前 app

**接口**

```dart
static Future<void> setBrightness(double brightness) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| brightness | double | 亮度取值范围 0.0~1.0 |

**返回值**

无


### restorePageBrightness

**说明**

恢复界面亮度，仅适用于当前 app

**接口**

```dart
static Future<void> restorePageBrightness() async;
```

**参数说明**

无

**返回值**

无


### getBrightness

**说明**

获得当前界面的亮度值

**接口**

```dart
static Future<double> getBrightness() async;
```

**参数说明**

无

**返回值**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| brightness | double | 亮度取值范围 0.0~1.0 |


### setSystemVolume

**说明**

设置当前系统的音量

**接口**

```dart
static Future<void> setSystemVolume(double volume) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| volume | double | 音量取值范围 0.0~1.0 |

**返回值**

无


### getSystemVolume

**说明**

设置当前系统的音量

**接口**

```dart
static Future<double> getSystemVolume() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| volume | double | 音量取值范围 0.0~1.0 |


### abandonAudioFocus

**说明**

释放音频焦点，仅适用于Android

**接口**

```dart
static Future<double> abandonAudioFocus() async;
```

**参数说明**

无

**返回值**

无


### requestAudioFocus

**说明**

请求获取音频焦点，仅适用于Android

**接口**

```dart
static Future<void> requestAudioFocus() async ;
```

**参数说明**

无

**返回值**

无


### isDeviceSupportPip

**说明**

判断当前设备是否支持画中画模式

**接口**

```dart
static Future<int> isDeviceSupportPip() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isDeviceSupportPip | int | 0 可开启画中画模式</br> -101  android版本过低 </br>  -102  画中画权限关闭/设备不支持画中画 </br> -103  当前界面已销毁|


### getLiteAVSDKVersion

**说明**

获得当前原生层播放器 SDK 的版本号

**接口**

```dart
static Future<String?> getLiteAVSDKVersion() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| sdkVersion | String | 当前播放器 SDK 版本 |


### setGlobalEnv

**说明**

设置 liteav SDK 接入的环境。
腾讯云在全球各地区部署的环境，按照各地区政策法规要求，需要接入不同地区接入点。

**注意**

目标市场为中国大陆的客户请不要调用此接口，如果目标市场为海外用户，请通过技术支持联系我们，了解 env_config 的配置方法，以确保 App 遵守 GDPR 标准。

**接口**

```dart
static Future<int> setGlobalEnv(String envConfig) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| envConfig | String | 需要接入的环境，SDK 默认接入的环境是：默认正式环境 |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | int | 1 设置成功， 2 设置失败 |



## TXVodPlayerController类


### initialize

**说明**

初始化 controller，请求分配共享纹理

**接口**

```dart
Future<void> initialize({bool? onlyAudio}) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| onlyAudio | bool | 选填，是否是纯音频播放器 |

**返回值说明**

无


### startVodPlay

**注意**

10.7版本开始，startPlay 变更为 startVodPlay，需要通过 {@link SuperPlayerPlugin#setGlobalLicense} 设置 Licence 后方可成功播放， 否则将播放失败（黑屏），全局仅设置一次即可。直播 Licence、短视频 Licence 和视频播放 Licence 均可使用，若您暂未获取上述 Licence ，可[快速免费申请测试版 Licence](https://cloud.tencent.com/act/event/License) 以正常播放，正式版 License 需[购买](https://cloud.tencent.com/document/product/881/74588#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E6.96.B0.E5.BB.BA.E6.AD.A3.E5.BC.8F.E7.89.88-license)。

**说明**

通过播视频url进行播放。

**接口**

```dart
Future<bool> startVodPlay(String url) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| url | String | 要播放的视频url |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | bool | 创建是否成功 |


### startVodPlayWithParams

**注意**

10.7版本开始，startPlay 变更为 startVodPlay，需要通过 {@link SuperPlayerPlugin#setGlobalLicense} 设置 Licence 后方可成功播放， 否则将播放失败（黑屏），全局仅设置一次即可。直播 Licence、短视频 Licence 和视频播放 Licence 均可使用，若您暂未获取上述 Licence ，可[快速免费申请测试版 Licence](https://cloud.tencent.com/act/event/License) 以正常播放，正式版 License 需[购买](https://cloud.tencent.com/document/product/881/74588#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E6.96.B0.E5.BB.BA.E6.AD.A3.E5.BC.8F.E7.89.88-license)。

**说明**

通过视频 field 进行播放。

**接口**

```dart
Future<void> startVodPlayWithParams(TXPlayInfoParams params) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| appId | int | 应用 appId。必填 |
| fileId | String | 文件 id。必填 |
| timeout | String | 加密链接超时时间戳，转换为16进制小写字符串，腾讯云 CDN 服务器会根据该时间判断该链接是否有效 |
| exper | String | 试看时长，单位：秒 |
| us | String | 唯一标识请求，增加链接唯一性 |
| sign | String | 防盗链签名，参考防盗链产品文档: https://cloud.tencent.com/document/product/266/11243 |
| https | String | 是否用 https 请求。默认 false |

**返回值说明**

无


### pause

**说明**

暂停当前正在播放的视频

**接口**

```dart
Future<void> pause() async;
```

**参数说明**

无

**返回值说明**

无


### resume

**说明**

将当前处于暂停状态的视频恢复播放

**接口**

```dart
Future<void> resume() async;
```

**参数说明**

无

**返回值说明**

无


### stop

**说明**

停止当前正在播放的视频

**接口**

```dart
Future<bool> stop({bool isNeedClear = false}) async;
```
**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isNeedClear | bool | 是否清除最后一帧画面 |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | bool | 停止是否成功 |


### setIsAutoPlay

**说明**

设置即将播放的视频，在 startVodPlay 加载视频地址之后，是否直接自动播放

**接口**

```dart
Future<void> setIsAutoPlay({bool? isAutoPlay}) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isAutoPlay | bool | 是否自动播放 |

**返回值说明**

无


### isPlaying

**说明**

当前播放器是否正在播放

**接口**

```dart
Future<bool> isPlaying() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isPlaying | bool | 是否正在播放 |


### setMute

**说明**

设置当前播放是否静音

**接口**

```dart
Future<void> setMute(bool mute) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| mute | bool | 是否静音 |

**返回值说明**

无


### setLoop

**说明**

视频播放完成之后是否循环播放

**接口**

```dart
Future<void> setLoop(bool loop) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| loop | bool | 是否循环播放 |

**返回值说明**

无


### seek

**说明**

将进度调整到指定位置

**接口**

```dart
_controller.seek(progress);
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| progress | double | 需要调整到的播放时间，单位 秒。|

**返回值说明**

无


### setRate

**说明**

设置视频播放的速率

**接口**

```dart
Future<void> setRate(double rate) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| rate | double | 视频的播放速率。默认1.0 |

**返回值说明**

无


### getSupportedBitrates

**说明**

获得当前正在播放的视频支持的码率

**接口**

```dart
Future<List?> getSupportedBitrates() async;
```

**参数说明**

无

**返回值说明**

| 返回值 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| index | int | 码率序号 |
| width | int | 码率对应视频宽度 |
| height | int | 码率对应视频高度 |
| bitrate | int | 码率值 |

### getBitrateIndex

**说明**

获得设置过的码率序号

**接口**

```dart
Future<int> getBitrateIndex() async;
```

**参数说明**

无

**返回值说明**

| 返回值 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| index | int | 码率序号 |


### setBitrateIndex

**说明**

通过码率序号，设置当前码率

**接口**

```dart
Future<void> setBitrateIndex(int index) async;
```

**参数说明**

| 返回值 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| index | int | 码率序号。 传入-1时，表示开启码流自适应。 |

**返回值说明**

无


### setStartTime

**说明**

指定播放开始时间

**接口**

```dart
Future<void> setStartTime(double startTime) async;
```

**参数说明**

| 返回值 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| startTime | double | 播放开始时间，单位 秒 |

**返回值说明**

无


### setAudioPlayoutVolume

**说明**

设置视频的声音大小

**接口**

```dart
Future<void> setAudioPlayoutVolume(int volume) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| volume | int | 视频声音大小，范围0~100 |

**返回值说明**

无


### setRequestAudioFocus

**说明**

请求获得音频焦点，适用于Android

**接口**

```dart
Future<bool> setRequestAudioFocus(bool focus) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| focus | bool | 是否设置焦点 |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | bool | 设置焦点是否成功 |


### setConfig

**说明**

给播放器进行配置

**接口**

```dart
Future<void> setConfig(FTXVodPlayConfig config) async ;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| config | FTXVodPlayConfig | 请参考 `FTXVodPlayConfig类` |


**返回值说明**

无


### getCurrentPlaybackTime

**说明**

获得当前播放时间,单位 秒

**接口**

```dart
Future<double> getCurrentPlaybackTime() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| playbackTime | double | 当前播放时间，单位 秒 |


### getBufferDuration

**说明**

获得当前视频已缓存的时间，单位 秒

**接口**

```dart
 Future<double> getBufferDuration();
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| playbackTime | double | 当前视频已缓存的时间，单位 秒 |


### getPlayableDuration

**说明**

获得当前正在播放视频的可播放时间,单位 秒

**接口**

```dart
 Future<double> getPlayableDuration() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| playableDuration | double | 当前视频可播放时，单位 秒 |


### getWidth

**说明**

获得当前正在播放视频的宽度

**接口**

```dart
Future<int> getWidth() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| width | int | 当前视频宽度 |


### getHeight

**说明**

获得当前正在播放视频的高度

**接口**

```dart
Future<int> getHeight() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| height | int | 当前视频高度 |


### setToken

**说明**

加密HLS的token。设置此值后，播放器自动在URL中的文件名之前增加voddrm.token

**接口**

```dart
Future<void> setToken(String? token) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| token | String | 播放视频的token |

**返回值说明**

无


### isLoop

**说明**

获得当前播放器是否循环播放的状态

**接口**

```dart
Future<bool> isLoop() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isLoop | bool | 播放器是否处于循环播放状态 |


### enableHardwareDecode

**说明**

开启/关闭硬解播放，设置后不会立即生效，需要重新播放才可生效

**接口**

```dart
Future<bool> enableHardwareDecode(bool enable);
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| enable | bool | 是否开启硬解 |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | bool | 硬解/软解设置结果 |


### dispose

**说明**

销毁controller，调用该方法会销毁掉所有通知事件，释放掉播放器

**接口**

```dart
void dispose() async;
```

**参数说明**

无

**返回值说明**

无


### getDuration

**说明**

获取视频总时长

**接口**

```dart
Future<double> getDuration() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| duration | double | 视频总时长，单位 秒 |


### enterPictureInPictureMode

**说明**

进入画中画模式

**接口**

```dart
Future<int> enterPictureInPictureMode({String? backIconForAndroid, String? playIconForAndroid, String? pauseIconForAndroid, String? forwardIconForAndroid}) async;
```

**参数说明**

该参数只适用于 android 平台

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| backIcon | String | 回退按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |
| playIcon | String | 播放按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |
| pauseIcon | String | 暂停按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |
| forwardIcon | String | 快进按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |

**返回值说明**

| 参数名 | 值   | 描述               |
| ------ | ------ | ------------------ |
| NO_ERROR | 0 | 启动成功，没有错误 |
| ERROR_PIP_LOWER_VERSION | -101 | android 版本过低，不支持画中画模式 |
| ERROR_PIP_DENIED_PERMISSION | -102 | 画中画模式权限未打开，或者当前设备不支持画中画 |
| ERROR_PIP_ACTIVITY_DESTROYED | -103 | 当前界面已经销毁 |
| ERROR_IOS_PIP_DEVICE_NOT_SUPPORT | -104 | 设备或系统版本不支持（iPad iOS9+ 才支持PIP），只适用于 iOS
| ERROR_IOS_PIP_PLAYER_NOT_SUPPORT | -105 | 播放器不支持，只适用于 iOS
| ERROR_IOS_PIP_VIDEO_NOT_SUPPORT | -106 | 视频不支持，只适用于 iOS
| ERROR_IOS_PIP_IS_NOT_POSSIBLE | -107 | PIP控制器不可用，只适用于 iOS
| ERROR_IOS_PIP_FROM_SYSTEM | -108 | PIP控制器报错，只适用于 iOS
| ERROR_IOS_PIP_PLAYER_NOT_EXIST | -109 | 播放器对象不存在，只适用于 iOS
| ERROR_IOS_PIP_IS_RUNNING | -110 | PIP功能已经运行，只适用于 iOS
| ERROR_IOS_PIP_NOT_RUNNING | -111 | PIP功能没有启动，只适用于 iOS



## FTXVodPlayConfig类

#### 属性配置说明


| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| connectRetryCount | int | 播放器重连次数，当 SDK 与服务器异常断开连接时,SDK 会尝试与服务器重连.通过该值设置 SDK 重连次数 |
| connectRetryInterval | int | 播放器重连间隔，当 SDK 与服务器异常断开连接时,SDK 会尝试与服务器重连.通过该值设置两次重连间隔时间 |
| timeout | int | 播放器连接超时时间 |
| playerType | int | 播放器类型,0 点播，1 直播，2 直播回看 |
| headers | Map | 自定义 http headers |
| enableAccurateSeek | bool | 是否精确 seek，默认 true |
| autoRotate | bool | 播放mp4文件时，若设为 true 则根据文件中的旋转角度自动旋转。旋转角度可在 PLAY_EVT_CHANGE_ROTATION 事件中获得。默认 true |
| smoothSwitchBitrate | bool | 平滑切换多码率HLS，默认 false。设为 false时，可提高多码率地址打开速度; 设为 true，在 IDR 对齐时可平滑切换码率 |
| cacheMp4ExtName | String | 缓存 mp4文件扩展名,默认mp4 |
| progressInterval | int | 设置进度回调间隔,若不设置，SDK 默认间隔0.5秒回调一次,单位毫秒 |
| maxBufferSize | int | 最大播放缓冲大小，单位 MB。此设置会影响 playableDuration，设置越大，提前缓存的越多|
| maxPreloadSize | int | 预加载最大缓冲大小，单位：MB|
| firstStartPlayBufferTime | int | 首缓需要加载的数据时长，单位ms，默认值为100ms|
| nextStartPlayBufferTime | int | 缓冲时（缓冲数据不够引起的二次缓冲，或者seek引起的拖动缓冲）最少要缓存多长的数据才能结束缓冲，单位ms，默认值为250ms|
| overlayKey | String | HLS安全加固加解密 key|
| overlayIv | String | HLS安全加固加解密 Iv|
| extInfoMap | Map | 一些不必周知的特殊配置|
| enableRenderProcess | bool | 是否允许加载后渲染后处理服务,默认开启，开启后超分插件如果存在，默认加载|
| preferredResolution | int | 优先播放的分辨率，preferredResolution = width * height|


## TXLivePlayerController类


### initialize

**说明**

初始化 controller，请求分配共享纹理

**接口**

```dart
Future<void> initialize({bool? onlyAudio}) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| onlyAudio | bool | 选填，是否是纯音频播放器 |

**返回值说明**

无


### startLivePlay

**注意**

10.7版本开始，startPlay变更为startLivePlay，需要通过 {@link SuperPlayerPlugin#setGlobalLicense} 设置 Licence 后方可成功播放， 否则将播放失败（黑屏），全局仅设置一次即可。直播 Licence、短视频 Licence 和视频播放 Licence 均可使用，若您暂未获取上述 Licence ，可[快速免费申请测试版 Licence](https://cloud.tencent.com/act/event/License) 以正常播放，正式版 License 需[购买](https://cloud.tencent.com/document/product/881/74588#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E6.96.B0.E5.BB.BA.E6.AD.A3.E5.BC.8F.E7.89.88-license)。

**说明**

通过播视频url进行播放。

**接口**

```dart
Future<bool> play(String url, {int? playType}) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| url | String | 要播放的视频url |
| playType | int | 选填，支持的播放类型，默认RTMP直播，支持LIVE_RTMP、LIVE_FLV、LIVE_RTMP_ACC以及VOD_HLS，详见 TXPlayType |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | bool | 创建是否成功 |


### pause

**说明**

暂停当前正在播放的视频

**接口**

```dart
Future<void> pause() async;
```

**参数说明**

无

**返回值说明**

无


### resume

**说明**

将当前处于暂停状态的视频恢复播放


**接口**

```dart
Future<void> resume() async;
```

**参数说明**

无

**返回值说明**

无


### stop

**说明**

停止当前正在播放的视频

**接口**

```dart
Future<bool> stop({bool isNeedClear = false}) async;
```
**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isNeedClear | bool | 是否清除最后一帧画面 |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | bool | 停止是否成功 |


### setIsAutoPlay

**说明**

设置即将播放的视频，在 startVodPlay 加载视频地址之后，是否直接自动播放

**接口**

```dart
Future<void> setIsAutoPlay({bool? isAutoPlay}) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isAutoPlay | bool | 是否自动播放 |

**返回值说明**

无


### isPlaying

**说明**

当前播放器是否正在播放

**接口**

```dart
Future<bool> isPlaying() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| isPlaying | bool | 是否正在播放 |


### setMute

**说明**

设置当前播放是否静音

**接口**

```dart
Future<void> setMute(bool mute) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| mute | bool | 是否静音 |

**返回值说明**

无


### setVolume

**说明**

设置视频的声音大小

**接口**

```dart
 Future<void> setVolume(int volume);
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| volume | int | 视频声音大小，范围0~100 |

**返回值说明**

无


### setLiveMode

**说明**

设置直播模式

**接口**

```dart
Future<void> setLiveMode(TXPlayerLiveMode mode) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| mode | int | 直播模式，自动模式、极速模式、流畅模式 |

**返回值说明**

无


### setAppID

**说明**

设置 appID，云控使用

**接口**

```dart
Future<void> setAppID(int appId) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| appId | int | appId |

**返回值说明**

无


### resumeLive

**说明**

停止时移播放，返回直播

**接口**

```dart
Future<int> resumeLive() async;
```

**参数说明**

无

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | int | 1 成功， 0 失败 |


### setConfig

**说明**

给播放器进行配置

**接口**

```dart
Future<void> setConfig(FTXLivePlayConfig config) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| config | FTXLivePlayConfig | 请参考`FTXLivePlayConfig类` |

**返回值说明**

无


### enableHardwareDecode

**说明**

开启/关闭硬解播放，设置后不会立即生效，需要重新播放才可生效

**接口**

```dart
Future<bool> enableHardwareDecode(bool enable);
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| enable | bool | 是否开启硬解 |

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | bool | 硬解/软解设置结果 |


### enterPictureInPictureMode

**说明**

进入画中画模式，仅支持 Android 端，iOS 端直播目前暂不支持画中画模式

**接口**

```dart
Future<int> enterPictureInPictureMode({String? backIconForAndroid, String? playIconForAndroid, String? pauseIconForAndroid, String? forwardIconForAndroid}) async;
```

**参数说明**

该参数只适用于 android 平台

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| backIcon | String | 回退按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |
| playIcon | String | 播放按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |
| pauseIcon | String | 暂停按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |
| forwardIcon | String | 快进按钮图标，由于 android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标 |

**返回值说明**

| 参数名 | 值   | 描述               |
| ------ | ------ | ------------------ |
| NO_ERROR | 0 | 启动成功，没有错误 |
| ERROR_PIP_LOWER_VERSION | -101 | android版本过低，不支持画中画模式 |
| ERROR_PIP_DENIED_PERMISSION | -102 | 画中画模式权限未打开，或者当前设备不支持画中画 |
| ERROR_PIP_ACTIVITY_DESTROYED | -103 | 当前界面已经销毁 |
| ERROR_IOS_PIP_DEVICE_NOT_SUPPORT | -104 | 设备或系统版本不支持（iPad iOS9+ 才支持PIP），只适用于 iOS
| ERROR_IOS_PIP_PLAYER_NOT_SUPPORT | -105 | 播放器不支持，只适用于 iOS
| ERROR_IOS_PIP_VIDEO_NOT_SUPPORT | -106 | 视频不支持，只适用于 iOS
| ERROR_IOS_PIP_IS_NOT_POSSIBLE | -107 | PIP控制器不可用，只适用于 iOS
| ERROR_IOS_PIP_FROM_SYSTEM | -108 | PIP控制器报错，只适用于 iOS
| ERROR_IOS_PIP_PLAYER_NOT_EXIST | -109 | 播放器对象不存在，只适用于 iOS
| ERROR_IOS_PIP_IS_RUNNING | -110 | PIP功能已经运行，只适用于 iOS
| ERROR_IOS_PIP_NOT_RUNNING | -111 | PIP功能没有启动，只适用于 iOS


### dispose

**说明**

销毁 controller，调用该方法会销毁掉所有通知事件，释放掉播放器

**接口**

```dart
void dispose() async;
```

**参数说明**

无

**返回值说明**

无



### switchStream

**说明**

切换播放流

**接口**

```dart
Future<int> switchStream(String url) async;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| url | String | 需要切换的视频源|

**返回值说明**

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| result | int | 切换结果 |


## FTXLivePlayConfig类

#### 属性配置说明

| 参数名 | 类型   | 描述               |
| ------ | ------ | ------------------ |
| cacheTime | double | 播放器缓存时间，单位秒，取值需要大于0，默认值：5 |
| maxAutoAdjustCacheTime | double | 播放器缓存自动调整的最大时间，单位秒，取值需要大于0，默认值：5 |
| minAutoAdjustCacheTime | double | 播放器缓存自动调整的最小时间，单位秒，取值需要大于0，默认值为1 |
| videoBlockThreshold | int | 播放器视频卡顿报警阈值，单位毫秒,只有渲染间隔超过这个阈值的卡顿才会有 PLAY_WARNING_VIDEO_PLAY_LAG 通知 |
| connectRetryCount | int | 播放器遭遇网络连接断开时 SDK 默认重试的次数，取值范围1 - 10，默认值：3。 |
| connectRetryInterval | int | 网络重连的时间间隔，单位秒，取值范围3 - 30，默认值：3。 |
| autoAdjustCacheTime | bool | 是否自动调整播放器缓存时间，默认值：true。true：启用自动调整，自动调整的最大值和最小值可以分别通过修改 maxCacheTime 和 minCacheTime 来设置。false：关闭自动调整，采用默认的指定缓存时间(1s)，可以通过修改 cacheTime 来调整缓存时间 |
| enableAec | bool | 是否开启回声消除， 默认值为 false |
| enableMessage | bool | 是否开启消息通道， 默认值为 true |
| enableMetaData | bool | 是否开启 MetaData 数据回调，默认值为 NO。 true：SDK 通过 EVT_PLAY_GET_METADATA 消息抛出视频流的 MetaData 数据；false：SDK 不抛出视频流的 MetaData 数据。 |
| flvSessionKey | String | 是否开启 HTTP 头信息回调，默认值为 “” |
