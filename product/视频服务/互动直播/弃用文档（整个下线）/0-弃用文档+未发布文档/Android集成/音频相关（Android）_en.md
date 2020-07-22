## Audio Device Management
All audio-related features and operations in audio/video SDK are controlled by the audio controller wrapper class AVAudioCtrl. You can acquire AVAudioCtrl instance by calling the getAudioCtrl method of AVContext class.

```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
```
 

## Audio Input Device Operations
### 1. Enable/disable microphone
Microphone is the main input device for iPhone audio input, and can be enabled by just calling enableMic method of QAVAudioCtrl class. The API declaration is as follows:

```
public boolean enableMic(boolean isEnable)
```
Sample code:
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
   audioCtrl.enableMic(true); //Enable the microphone
}
```
### 2. Acquire digital volume of microphone
 The getVolume method can be used to acquire microphone volume. The API declaration is as follows:
 
```
public native int getVolume();
```
Sample code:

```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
   int volumn = audioCtrl.getVolume(); //Acquire digital volume of microphone
}
```
### 3. Acquire real-time volume of microphone
 The getDynamicVolume method can be used to acquire real-time microphone volume. The API is declared is as follows:
```
public native int getDynamicVolume();
```
Sample code:
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 int dynamicVolumn = audioCtrl.getDynamicVolume(); //Acquire real-time volume of microphone
}
```

## Audio Output Device Operations
### 1. Disable/enable speaker (mute/unmute)
  The enableSpeaker method can be used to enable or disable speaker. The API declaration is as follows:
```
public boolean enableSpeaker(boolean isEnable)
```
Sample code:
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
  audioCtrl.enableSpeaker(true); //Enable speaker
}
```
### 2. Configure speaker output mode
  Audio output has two modes, speaker mode and headphone mode. In speaker mode, audio is played via speaker. In earphone mode, the SDK enumerates a device (priority: wired headphone > Bluetooth headphone > receiver) to play the audio.

  The enableSpeaker method can be used to enable or disable speaker. The API declaration is as follows:
```
public boolean setAudioOutputMode(int outputMode)
```
Sample code:
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
  audioCtrl.setAudioOutputMode(true); //Configure audio output mode
}
```
## Processing Audio Data
### 1. Transparent transmission of audio data
    Audio/Video SDK provides audio data callback API (RegistAudioDataCompleteCallback). There are three types of transparent transmissions of audio data:

(1) Transparently transmit audio data outputted by SDK.

(2) Transparently transmit audio data provided to SDK by the user.

(3) Audio data pre-processing. (For example, you can modify audio data in the callback to change sound effect)

The three transmission types will all call the transparently transmitted audio data back to the following method:
```
protected int onComplete(AudioFrame audioframe, int srcType) {
   /* do something */
   return AVError.AV_OK;
}
```
To achieve the transparent transmission of audio data, follow the steps below:

1. Inherit RegistAudioDataCompleteCallback and re-write the onComplete method.

2. Call registAudioDataCallback for the audio data type of your interest.
```
public native int registAudioDataCallback(int src_type,  RegistAudioDataCompleteCallback javacallback);
```
 Sample code:
```
AVAudioCtrl.RegistAudioDataCompleteCallback callback = new AVAudioCtrl.RegistAudioDataCompleteCallback() { 
 protected int onComplete(AudioFrame audioframe, int srcType ) {
   /* do something */
   return AVError.AV_OK;
 }
} 

AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 audioCtrl.registAudioDataCallback(AVAudioCtrl.AudioDataSourceType.AUDIO_DATA_SOUR CE_MIC, callback); //Register for microphone output callback capturing
}
```

### 2. Cancel transparent transmission of audio data
Users can use the following two approaches to cancel transparent transmission of audio data if they no longer need this feature:

#### (1) Cancel transparent transmission of audio data for a certain audio data source type:
```
public native int unregistAudioDataCallback(int src_type);
```
Sample code:
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 audioCtrl.unregistAudioDataCallback(AVAudioCtrl.AudioDataSourceType.AUDIO_DATA_SOUR CE_MIC); //Cancel registration for microphone output capturing
}
```
#### (2) Cancel transparent transmission for all audio data sources
```
public native int unregistAudioDataCallbackAll();
```
Sample code:
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 audioCtrl.unregistAudioDataCallbackAll(); //Cancel registration for all output callback
}
```

## Audio Statistics
getQualityTips can be used to acquire information regarding the real-time communication quality of audio/video calls. This method is mainly used to check the quality of real-time calls and troubleshooting problems. At business side, it can be used to improve the user experience, such as indicating a poor network condition or a poor call quality.
```
 public native String getQualityTips()
 ```
Sample code:
```
AVAudioCtrl audioCtrl = mAVContext.getAudioCtrl();
if(audioCtrl) {
 String tips = audioCtrl.getQualityTips(); //Acquire audio quality statistical parameters JSON format
}
```
