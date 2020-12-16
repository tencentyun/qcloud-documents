

## iOS 音频相关接口

此部分接口使用 SetAdvanceParams 接口进行调用，在进房前调用。 
```
[[ITMGContext GetInstance] SetAdvanceParams:keyString value:_value]
```

| 参数      | 含义                             |
| --------- | -------------------------------- |
| keyString | 不同的 Key 代表不同的功能        |
| value     |<li> 0：代表关闭<li>1：代表开启 |

#### Key 
不同的 Key 代表不同的功能，参数 Key 可填写的字段如下：
- **OptionMixWithOthers**
混音选项。开启后可以把后台播放的音乐与前台通话语音同时播放。

- **OptionDuckOthers**
压低背景音。在 OptionMixWithOthers 开启的情况下，如果开启此功能，则开启扬声器播放语音时，将会压低其他后台背景声音。

- **ReleaseAudioFoucus**
释放音频焦点。
 -  如果开启，退房之后将会释放音频焦点，系统恢复后台其他音频相关应用。例如 QQ 音乐。
 - 如果关闭，退房之后将不会恢复其他音频相关应用。

## 设置最大混音路数

使用 SetRecvMixStreamCount 接口可以设置最高混音路数，在进房前调用。 各平台均有此接口，下面以 pc 端为例。
```
virtual int SetRecvMixStreamCount(int nCount) = 0;
```
**参数说明** 

| 参数      | 含义                             |
| --------- | -------------------------------- |
| nCount | 混音路数，最大为20        |


## 设置房间音频类型

进房前使用 SetForceUseMediaVol ，可以让流畅音质房间或者标准音质房间使用媒体音量。

```
[[ITMGContext GetInstance] SetAdvanceParams:SetForceUseMediaVol value:1]
```

#### value
不同的 value 代表不同的功能，可填的数值及其代表的含义如下：
- **1**：房间1开麦克风后为媒体音量（原为通话音量）。
- **2**：房间2开麦克风后为媒体音量（原为通话音量）。
- **3**：房间1与2都还原为开麦克风后音量为通话音量。
