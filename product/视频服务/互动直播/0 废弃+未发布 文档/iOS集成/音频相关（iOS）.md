## 一. 音频设备管理
音视频SDK中的所有与音频相关的功能和操作统一由音频控制器的封装类QAVAudioCtrl来管理，通过调用QAVContext类的方法getAudioCtrl可获得QAVAudioCtrl的实例。

```
QAVAudioCtrl *audioCtrl = [AVUtil sharedContext].audioCtrl;
```
## 二. 音频输入设备
### 1. 打开/关闭麦克风
iPhone手机音频输入的主要输入设备是麦克风，因此只需要调用QAVAudioCtrl类提供的enableMic方法就可以实现开关麦克风操作，接口声明如下：

```
-(BOOL)enableMic:(BOOL)isEnable;
```
示例代码：
```
QAVAudioCtrl *audioCtrl = [AVUtil sharedContext].audioCtrl;
[audioCtrl enableMic:YES];                //打开麦克风
```
### 2. 获取设备数字音量

```
int volumn = audioCtrl.volume;
```
### 3. 获取设备实时音量

```
int dynamicVolumn = audioCtrl.dynamicVolume;
```
## 三. 音频输出设备
音频输出模式分为扬声器模式和耳机模式。切换成扬声器模式，声音会外放；切换成耳机模式，SDK会按照有线耳机 > 蓝牙耳机 > 听筒的优先级枚举设备，播放声音。

### 1.切换音频输出设备播放音频
```
QAVAudioCtrl *audioCtrl = [AVUtil sharedContext].audioCtrl;
[audioCtrl setOutputMode:QAVOUTPUTMODE_SPEAKER];             //切换为扬声器模式
```
### 2. 打开/关闭扬声器（是否静音）
这个接口可以实现静音和开声音的功能，接口声明如下：
		
```
-(BOOL)enableSpeaker:(BOOL)bEnable; 
```
示例代码：
```
[[AVUtil sharedContext].audioCtrl enableSpeaker:YES];
```
## 四. 音频数据处理
### 1.音频数据透传
音视频SDK提供了音频数据委托协议（QAVAudioDataDelegate），音频数据透传分为以下两种情形：

1. 接收外部音频数据到本地

2. 从本地传输音频数据到外部

在注册了音频数据类型的回调后，这两种情形分别会将透传的音频数据类型回调到以下两个方法中：

外部传到本地：
```
-(QAVResult)audioDataComes:(QAVAudioFrame*)audioFrame type:(QAVAudioDataSourceType)type;
```
从本地传到外部：
```
-(QAVResult)audioDataShouInput:(QAVAudioFrame*)audioFrame type:(QAVAudioDataSourceType)type;
```


因此实现音频数据透传需要以下几步：

1.相应的ViewController实现QAVAudioDataDelegate这个协议

2.设置相应的delegate为self

```
[[AVUtil sharedContext].audioCtrl setAudioDataEventDelegate:self];
```
 3.注册监听某种音频数据源类型，示例代码为监听麦克风输出
```
[[AVUtil sharedContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_Mic];
```
4.实现协议中定义的方法
```
-(QAVResult)audioDataComes:(QAVAudioFrame*)audioFrame type:(QAVAudioDataSourceType)type{
    //接收外部数据并写入本地
}
 
- (QAVResult)audioDataShouInput:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
     //读取本地音频数据源并发送
}
```
### 2. 取消音频数据透传
当用户不需要音频数据透传的时候，就可以利用以下两个方法取消音频数据透传：

1.取消某种音频数据源类型的音频数据透传：

```
-(QAVResult)unregisterAudioDataCallback:(QAVAudioDataSourceType)type;
```
示例代码：

```
[[AVUtil sharedContext].audioCtrl unregisterAudioDataCallback:QAVAudioDataSource_Mic];
```

2 取消所有音频数据源的透传

```
-(QAVResult)unregisterAudioDataCallbackAll;
```
示例代码：
```
[[AVUtil sharedContext].audioCtrl unregisterAudioDataCallbackAll]; 
```
 

## 五. 音频统计信息
获取音视频通话的实时通话质量的相关信息。该方法主要用来查看实时通话质量、排查问题等，业务侧可以用其来做些提高用户体验的功能，如提示网络差，通话质量也较差。

获取音频统计信息的方法在QAVRoom里面，因此要先通过[AVUtil sharedContext].room来获取当前所在的房间，然后调用getStatParam方法获取，返回值为字典的形式，接口如下：
```
-(NSDictionary*)getStatParam; 
```
示例代码：

```
    QAVRoom *room = [AVUtil sharedContext].room;
    NSDictionary *statDictionary = [room getStatParam];
    NSLog(@"statistics = %@",statDictionary);
```