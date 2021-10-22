为方便开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍 GME SDK 高级接口。

<dx-alert infotype="alarm" title="调用须知">
此文档接口属于高级接口，非必要无需调用。接口调用前请咨询 GME 开发人员。
</dx-alert>

## 音频相关高级接口

### iOS 音频相关接口

此部分接口使用 SetAdvanceParams 接口进行调用，在进房前调用。 

```
[[ITMGContext GetInstance] SetAdvanceParams:keyString value:_value]
```

| 参数      | 含义                            |
| --------- | ------------------------------- |
| keyString | 不同的 Key 代表不同的功能       |
| value     | <li> 0：代表关闭<li>1：代表开启 |

#### Key 

不同的 Key 代表不同的功能，参数 Key 可填写的字段如下：

- **OptionMixWithOthers**
  混音选项。开启后可以把后台播放的音乐与前台通话语音同时播放。
- **OptionDuckOthers**
  压低背景音。在 OptionMixWithOthers 开启的情况下，如果开启此功能，则开启扬声器播放语音时，将会压低其他后台背景声音。
- **ReleaseAudioFoucus**
  释放音频焦点。
- 如果开启，退房之后将会释放音频焦点，系统恢复后台其他音频相关应用。例如 QQ 音乐。
- 如果关闭，退房之后将不会恢复其他音频相关应用。

### 检查iPhone静音键是否开启

<dx-alert infotype="explain" title="说明">
此接口在 GME 2.8.4 以上版本 SDK 上生效。
</dx-alert>

#### 函数原型

```
CheckDeviceMuteState();
```

返回值为 0 代表关闭物理静音键，返回值为 1 代表打开物理静音键。

### 检查麦克风设备状态

<dx-alert infotype="explain" title="说明">
此接口在 GME 2.8.4 以上版本 SDK 上生效
</dx-alert>

#### 函数原型

```
TestMic();
```

#### 返回值处理

| 返回值                               | 含义                | 处理                                                         |
| ------------------------------------ | ------------------- | ------------------------------------------------------------ |
| ITMG_TEST_MIC_STATUS_AVAILABLE = 0   | 正常可用            | 无需处理                                                     |
| ITMG_TEST_MIC_STATUS_NO_GRANTED = 2  | 未获得/拒绝授权权限 | 需要在打开麦克风之前获取下权限                               |
| ITMG_TEST_MIC_STATUS_INVALID_MIC = 3 | 没有可用的设备      | 一般是PC设备上，没有可用的麦克风设备会报此错误，请提示插入耳机或麦克风 |
| ITMG_TEST_MIC_STATUS_NOT_INIT = 5    | 没有初始化          | 在Init之后调用 EnableMic 接口                                |

### 设置 Android 蓝牙设备适配

<dx-alert infotype="explain" title="说明">
此接口在 GME 2.8.4 以上版本 SDK 上生效。
</dx-alert>

调用此接口可以解决蓝牙耳机在开关麦的时候漏声音的问题，以及 Android 设备在连接蓝牙耳机后切换连接状态后导致的从扬声器播放问题。

```
SetAdvanceParams(“BluetoothUseMedia”, “1”);
```

### 设置最大混音路数

使用 SetRecvMixStreamCount 接口可以设置最高混音路数，在进房前调用。 各平台均有此接口，下面以 pc 端为例。

```
virtual int SetRecvMixStreamCount(int nCount) = 0;
```

**参数说明** 

| 参数   | 含义               |
| ------ | ------------------ |
| nCount | 混音路数，最大为20 |



## 房间相关高级接口

### 设置房间音频类型

进房前使用 SetForceUseMediaVol ，可以让流畅音质房间或者标准音质房间使用媒体音量。

```
[[ITMGContext GetInstance] SetAdvanceParams:SetForceUseMediaVol value:1]
```

#### value

不同的 value 代表不同的功能，可填的数值及其代表的含义如下：

- **1**：房间1开麦克风后为媒体音量（原为通话音量）。
- **2**：房间2开麦克风后为媒体音量（原为通话音量）。
- **3**：房间1与2都还原为开麦克风后音量为通话音量。

### 获取房间内成员说话音量

调用 TrackingVolume 接口之后，监听 `TIMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_USER_VOLUMES` 事件，里面的键值对为 uin-volume，通过此接口可以根据房间内某 uin 说话的音量强度画出相应的能量柱状图。

如果不再获取，请调用 StopTrackingVolume 接口。

```
//TMGAudioCtrl
public int TrackingVolume(float fTrackingTimeS)
public int StopTrackingVolume();
```

| 参数           | 类型  | 含义                        |
| -------------- | ----- | --------------------------- |
| fTrackingTimeS | float | 监听的秒数，建议设置为 0.5f |

## 通用高级接口

### 修复打印日志大小

<dx-alert infotype="explain" title="说明">
此接口在 GME 2.8.4 以上版本 SDK 上生效。
</dx-alert>

在 GME Init 初始化接口前调用此接口，用于修改默认日志文件大小。目前日志文件单个为50m，最多存在3个日志文件。

#### 函数原型

```
SetAdvanceParams（const char* key, const char* object）
```

| 参数   | 类型        | 含义                                                         |
| ------ | ----------- | ------------------------------------------------------------ |
| key    | const char* | MAX_LOG_FILE_SIZE_MB 和 MAX_LOG_FILE_COUNT，分别代表单个日志的大小和日志的数量 |
| object | const char* | 当key 为 MAX_LOG_FILE_SIZE_MB 时，object 为Log文件大小默认值，取值范围（单位M）：5至50；当key 为 MAX_LOG_FILE_COUNT 时，object 为Log文件个数默认值，取值范围：1至3。 |

<dx-alert infotype="notice" title="参数范围">
当输入的 object 超过取值范围上限时，则设置为上限值；当输入的 object 小于取值范围下限时，则设置为下限值。
</dx-alert>

#### 示例代码

```
SetAdvanceParams("MAX_LOG_FILE_SIZE_MB", "5");
SetAdvanceParams("MAX_LOG_FILE_COUNT", "1");
```

