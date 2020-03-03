为方便开发者调试和接入腾讯云游戏多媒体引擎产品，这里向您介绍适用于使用windows平台第三方播放器伴奏功能的相关技术文档。

## 配置头文件
首先参考 [配置文档](https://cloud.tencent.com/document/product/607/19068) 配置好 GME 工程，然后将文件 tmg_adv_win.h 放在GME SDK(For Windows)的其他头文件同一目录下。

点击[下载](http://dldir1.qq.com/hudongzhibo/QCloud_TGP/GME/pubilc/GME_Accompany_Plugin.zip)，将两个dll文件下载下来，路径与其他库文件一致。导出可执行文件之后应与可执行文件同目录。

## 接口调用
### 开始播放
调用此参数，将挂钩整个系统的声音，或者某播放器的声音。
#### 函数原型
```
virtual int StartAccompany(const char* playerPath, int playerPathLength, const char* mediaFilePath, int mediaFilePathLenght, GMEAccompany_SourceType sourceType) = 0
```

|参数     | 类型         |含义|
| ------------- |:-------------:|-------------|
| playerPath|const char*|播放器路径|
| playerPathLength|int|播放器路径长度|
| mediaFilePath|const char*|音频资源路径，可以是某音频文件，也可以是音频文件夹，可以不传（NULL）|
| mediaFilePathLenght|int|音频资源路径长度|
| sourceType|GMEAccompany_SourceType|设置采集对象，详细见下表|

|参数     | 类型         |
| ------------- |:-------------:|
|AV_ACCOMPANY_SOURCE_TYPE_NONE = 0|代表不开启|
|AV_ACCOMPANY_SOURCE_TYPE_SYSTEM = 1|代表挂钩整个系统的声音，此时可以不传音频资源路径，但需要传一个已知文件路径作为播放器路径参数及播放器路径长度参数|
|AV_ACCOMPANY_SOURCE_TYPE_PROCESS = 2|代表挂钩某进程的声音，比如qq音乐播放器|

#### 示例代码
```
const char* file = "C:\\1.txt";//当挂钩系统声音时，需要传入一个已知文件路径，请确保此文件存在
int ret = ITMGAdcanceGetInstance()->StartAccompany(file, strlen(file), NULL, 0, AV_ACCOMPANY_SOURCE_TYPE_SYSTEM);
```

### 停止播放
调用此参数，将停止挂钩。
#### 函数原型
virtual int StopAccompany() = 0


### 设置声音音量
调用此参数，将设置挂钩的声音音量大小，数值 100 表示音量不增大也不衰减。数值范围为 0 到200。
#### 函数原型
virtual int SetAccompanyVolume(int value) = 0;

### 获取声音音量
调用此参数，将获取挂钩的声音音量大小。
#### 函数原型
virtual int GetAccompanyVolume(int* pVolume) = 0;

### 获取实时声音音量
调用此参数，将获取挂钩的实时声音音量，可以用来展示实时音量能量条。
#### 函数原型
virtual int GetAccompanyVolumeDynamic(int* pVolume) = 0;

### 设置采集设备音量
调用此参数，设置采集设备声音音量，默认数值为 100，数值范围为 0 到 100，0代表静音。
#### 函数原型
virtual int SetMicDeviceVolume(int vol)=0;

### 获取采集设备音量
调用此参数，将获取采集设备声音音量。
#### 函数原型
virtual int GetMicDeviceVolume()=0;
	
### 设置播放设备音量
调用此参数，设置播放设备声音音量，默认数值为 100，数值范围为 0 到 100，0代表静音。
#### 函数原型
virtual int SetSpeakerDeviceVolume(int vol)=0;

### 获取播放设备音量
调用此参数，将获取播放设备声音音量。
#### 函数原型
virtual int GetSpeakerDeviceVolume()=0;