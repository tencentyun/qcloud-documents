## Audio Device Management
All audio-related features and operations in the audio/video SDK are managed by the wrapper class QAVAudioCtrl of audio controller. The instance of QAVAudioCtrl can be obtained by calling getAudioCtrl method of QAVContext class.

```
QAVAudioCtrl *audioCtrl = [AVUtil sharedContext].audioCtrl;
```
## Audio Input Device
### 1. Enable/disable the microphone
Microphone is the main input device for iPhone audio input, and can be enabled by just calling enableMic method of QAVAudioCtrl class. The API declaration is as follows:

```
-(BOOL)enableMic:(BOOL)isEnable;
```
Sample code:
```
QAVAudioCtrl *audioCtrl = [AVUtil sharedContext].audioCtrl;
[audioCtrl enableMic:YES];//Enable the microphone
```
### 2. Acquire the digital volume of device 

```
int volumn = audioCtrl.volume;
```
### 3. Acquire the real-time volume of device

```
int dynamicVolumn = audioCtrl.dynamicVolume;
```
## Audio Output Device
Audio output has two modes, speaker mode and headphone mode. In speaker mode, audio is played via speaker. In earphone mode, the SDK enumerates a device (priority: wired headphone > Bluetooth headphone > receiver) to play the audio.

### 1. Switch between audio output devices to play the audio
```
QAVAudioCtrl *audioCtrl = [AVUtil sharedContext].audioCtrl;
[audioCtrl setOutputMode:QAVOUTPUTMODE_SPEAKER];//Switch to speaker mode
```
### 2. Enable/disable the speaker (mute or unmute)
This API is used for muting and unmuting, declared as follows:
		
```
-(BOOL)enableSpeaker:(BOOL)bEnable; 
```
Sample code:
```
[[AVUtil sharedContext].audioCtrl enableSpeaker:YES];
```
## Audio Data Processing
### 1. Transparent transmission of audio data
Audio/video SDK provides audio data delegation protocol (QAVAudioDataDelegate). Transparent transmission of audio data involves the following two scenarios:

(1) Receive external audio data to the local device

(2) Transfer audio data from the local to the external

In either of the two scenarios, after the callback of audio data type is registered, transparently transmitted audio data type can be called back to the following two methods:

External to local:
```
-(QAVResult)audioDataComes:(QAVAudioFrame*)audioFrame type:(QAVAudioDataSourceType)type;
```
Local to external:
```
-(QAVResult)audioDataShouInput:(QAVAudioFrame*)audioFrame type:(QAVAudioDataSourceType)type;
```


Transparent transmission of audio data involves the following steps:

(1) Implement QAVAudioDataDelegate protocol with ViewController

(2) Set "delegate" to "self"

```
[[AVUtil sharedContext].audioCtrl setAudioDataEventDelegate:self];
```
 (3) Register to listen for an audio data source type, with the sample code for listening for the microphone output
```
[[AVUtil sharedContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_Mic];
```
(4) Implement the method defined in the protocol
```
-(QAVResult)audioDataComes:(QAVAudioFrame*)audioFrame type:(QAVAudioDataSourceType)type{
    //Receive external data and write to local device
}
 
- (QAVResult)audioDataShouInput:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
     //Read the local audio data source and send it
}
```
### 2. Cancel the transparent transmission of audio data
When the transparent transmission of audio data is not needed, you can cancel it using the following two methods:

(1) Cancel the transparent transmission of audio data from an audio data source:

```
-(QAVResult)unregisterAudioDataCallback:(QAVAudioDataSourceType)type;
```
Sample code:

```
[[AVUtil sharedContext].audioCtrl unregisterAudioDataCallback:QAVAudioDataSource_Mic];
```

(2) Cancel the transparent transmission of all the audio data sources

```
-(QAVResult)unregisterAudioDataCallbackAll;
```
Sample code:
```
[[AVUtil sharedContext].audioCtrl unregisterAudioDataCallbackAll];
```
 

## Audio Statistics
Obtain the information about real-time call quality for audio and video calls. This method is mainly used to check the quality of real-time calls and troubleshoot problems. At business side, it can be used to improve the user experience, such as indicating a poor network condition or a poor call quality.

The method for obtaining the audio statistics is in QAVRoom, so first you need to obtain the current room using [AVUtil sharedContext].room, and then call getStatParam method to obtain the statistics, with the returned value taking a form of dictionary. The API is as follows:
```
-(NSDictionary*)getStatParam; 
```
Sample code:

```
    QAVRoom *room = [AVUtil sharedContext].room;
    NSDictionary *statDictionary = [room getStatParam];
    NSLog(@"statistics = %@",statDictionary);
```
