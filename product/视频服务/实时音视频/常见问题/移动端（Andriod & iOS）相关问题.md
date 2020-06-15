### TRTC 移动端（Andriod/iOS）支持哪几种系统音量模式？
支持2种系统音量类型，即通话音量类型和媒体音量类型：
- 通话音量，手机专门为通话场景设计的音量类型，使用手机自带的回声抵消功能，音质相比媒体音量类型较差， 无法通过音量按键将音量调成零，但是支持蓝牙耳机上的麦克风。
- 媒体音量，手机专门为音乐场景设计的音量类型，音质相比于通话音量类型要好，通过通过音量按键可以将音量调成零。 使用媒体音量类型时，如果要开启回声抵消（AEC）功能，SDK 会开启内置的声学处理算法对声音进行二次处理。 在媒体音量模式下，蓝牙耳机无法使用自带的麦克风采集声音，只能使用手机上的麦克风进行声音采集。

### TRTC 移动端 SDK 推流怎么设置1080p分辨率？
1080P在 TX_Enum_Type_VideoResolution 定义是114，直接设置分辨率传枚举值即可。

### 实时音视频在小程序端创建了一个房间，移动端能否进入该房间？
可以，实时音视频支持全平台互通。

### TRTC Android 端能不能支持64位的 arm64-v8a 架构？
TRTC 6.3 版本开始已提供 arm64-v8a 架构 ABI 支持。

### TRTC 在 Android 端怎么实现动态加载 so 库？
具体的操作步骤请参考 [Android 端实现动态加载 so 库](https://cloud.tencent.com/developer/article/1541517)。


### TRTC 在 iOS 端是否支持 Swift 集成？
支持，直接按照支持集成三方库的流程集成 SDK 即可，还可以参考 [跑通Demo(iOS&Mac)](https://cloud.tencent.com/document/product/647/32396)。


### TRTC SDK 是否支持 iOS 后台运行？
支持，您只需选中当前工程项目，在 **Capabilities** 下的设置  **Background Modes** 为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture**即可实现后台运行，详情如下图所示：
![](https://main.qcloudimg.com/raw/d960dfec88388936abce2d4cb77ac766.jpg)
