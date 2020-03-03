## 参数定制
如果您希望定制视频编码参数，音频编码参数等等，您可以通过设置Config对象实现您的自定义需求，目前我们支持的setting接口如下：

| 参数名           |    含义                                          |   默认值  | 
| :-------------- | :-----------------------------------------------| :------: |
| audioSampleRate|   音频采样率：录音设备在一秒钟内对声音信号的采集次数   |  44100   |  
| enableNAS          |   噪声抑制：开启后可以滤掉背景杂音（32000以下采样率有效） |  关闭     |
| enableHWAcceleration|   视频硬编码：开启后最高可支持720p， 30fps视频采集   |  开启   |  
| videoFPS     |   视频帧率：即视频编码器每秒生产出多少帧画面，注意由于大部分机器性能不足以支持30FPS以上的编码，推荐您设置FPS为20           |  20      |
| videoResolution|   视频分辨率：目前提供四种16：9分辨率可供您选择      |  640 * 360 |
| videoBitratePIN |   视频比特率：即视频编码器每秒生产出多少数据，单位 kbps |  800|
| enableAutoBitrate |   带宽自适应：该功能会根据当前网络情况，自动调整视频比特率 |   关闭|
| videoBitrateMax| 最大输出码率：只有开启自适应码率, 该设置项才能启作用 |   1200|
| videoBitrateMin| 最小输出码率：只有开启自适应码率, 该设置项才能启作用 |   800|
| videoEncodeGop | 关键帧间隔（单位：秒）即多少秒出一个I帧 | 3s |
| homeOrientation| 设置视频图像旋转角度，比如是否要横屏推流  |   home在右边（0）home在下面（1）home在左面（2）home在上面（3）   |
| beautyFilterDepth| 美颜级别：支持1~9 共9个级别，级别越高，效果越明显。0表示关闭  |   关闭   |
| frontCamera | 默认是前置还是后置摄像头 | 前置 |
| watermark | 水印图片（UIImage对象） | 腾讯云Logo（demo）  |    
| watermarkPos | 水印图片相对左上角坐标的位置 | （0, 0）  |                                                                        


## 设置方法
这些参数的设置推荐您在启动推流之前就指定，因为大部分设置项是在重新推流之后才能生效的。参考代码如下：

```objectivec
//成员变量中声明 _config 和 _pusher
....
//初始化 _config
_config = [[TXLivePushConfig alloc] init];

// 修改参数设置为声音44100采样率，视频800固定码率
_config.audioSampleRate = 44100;
_config.enableAutoBitrate = NO;
_config.videoBitratePIN = 800;

//初始化 _pusher
_pusher = [[TXLivePush alloc] initWithConfig: _config];
```
