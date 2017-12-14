## 一. 音频设备管理
音视频SDK中的所有与音频相关的功能和操作统一由音频控制器的封装类AVAudioCtrl来管理，通过调用AVContext类的方法getAudioCtrl可获得AVAudioCtrl的实例。

```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
```
 

## 二. 音频输入设备操作
### 1. 打开/关闭麦克风
iPhone手机音频输入的主要输入设备是麦克风，因此只需要调用QAVAudioCtrl类提供的enableMic方法就可以实现开关麦克风操作，接口声明如下：

```
public boolean enableMic(boolean isEnable)
```
示例代码：
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
   audioCtrl.enableMic(true); //打开麦克风
}
```
### 2. 获取麦克风数字音量
 getVolume方法就可以获取麦克风音量，接口声明如下：
 
```
public native int getVolume();
```
示例代码：

```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
   int volumn = audioCtrl.getVolume(); //获取麦克风数字音量
}
```
### 3. 获取麦克风实时音量
 getDynamicVolume方法就可以获取麦克风实时音量，接口声明如下：
```
public native int getDynamicVolume();
```
示例代码：
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 int dynamicVolumn = audioCtrl.getDynamicVolume(); //获取麦克风实时音量
}
```

## 三. 音频输出设备操作
### 1. 打开/关闭扬声器（是否静音）
  enableSpeaker方法可以打开和关闭扬声器，接口声明如下：
```
public boolean enableSpeaker(boolean isEnable)
```
示例代码：
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
  audioCtrl.enableSpeaker(true); //打开扬声器
}
```
### 2. 设置扬声器输出模式
  音频输出模式分为扬声器模式和耳机模式。切换成扬声器模式，声音会外放；切换成耳机模式，SDK会按照有线耳机 > 蓝牙耳机 > 听筒的优先级枚举设备，播放声音。

  enableSpeaker方法可以打开和关闭扬声器，接口声明如下：
```
public boolean setAudioOutputMode(int outputMode)
```
示例代码：
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
  audioCtrl.setAudioOutputMode(true); //设置音频输出模式
}
```
## 四. 音频数据处理
### 1.音频数据透传
    音视频SDK提供了音频数据回调（RegistAudioDataCompleteCallback），音频数据透传分为以下三种类型：

1. SDK输出的音频数据透传类型。

2. 使用者输入给SDK的音频数据透传类型。

3. 音频数据预处理类型。(例如可在回调中对音频数据进行修改，改变声音效果)

三种类型都会将透传的音频数据类型回调到以下方法中：
```
protected int onComplete(AudioFrame audioframe, int srcType) {
   /* do something */
   return AVError.AV_OK;
}
```
使用音频数据透传功能需要以下几步：

1.继承RegistAudioDataCompleteCallback，重写onComplete方法

2.针对感兴趣音频数据类型，调用registAudioDataCallback
```
public native int registAudioDataCallback(int src_type,  RegistAudioDataCompleteCallback javacallback);
```
 示例代码：
```
AVAudioCtrl.RegistAudioDataCompleteCallback callback = new AVAudioCtrl.RegistAudioDataCompleteCallback() { 
 protected int onComplete(AudioFrame audioframe, int srcType ) {
   /* do something */
   return AVError.AV_OK;
 }
} 

AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 audioCtrl.registAudioDataCallback(AVAudioCtrl.AudioDataSourceType.AUDIO_DATA_SOUR CE_MIC, callback); //注册麦克风采集输出回调
}
```

### 2. 取消音频数据透传
当用户不需要音频数据透传的时候，就可以利用以下两个方法取消音频数据透传：

#### （1）取消某种音频数据源类型的音频数据透传：
```
public native int unregistAudioDataCallback(int src_type);
```
示例代码：
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 audioCtrl.unregistAudioDataCallback(AVAudioCtrl.AudioDataSourceType.AUDIO_DATA_SOUR CE_MIC); //取消注册麦克风采集输出回调
}
```
#### （2） 取消所有音频数据源的透传
```
public native int unregistAudioDataCallbackAll();
```
示例代码：
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 audioCtrl.unregistAudioDataCallbackAll(); //取消注册所有输出回调
}
```

## 五. 音频统计信息
getQualityTips获取音视频通话的实时通话质量的相关信息。该方法主要用来查看实时通话质量、排查问题等，业务侧可以用其来做些提高用户体验的功能，如提示网络差，通话质量也较差。
```
 public native String getQualityTips()
 ```
示例代码：
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 String tips = audioCtrl.getQualityTips(); //获取音频质量统计参数。json格式
}
```