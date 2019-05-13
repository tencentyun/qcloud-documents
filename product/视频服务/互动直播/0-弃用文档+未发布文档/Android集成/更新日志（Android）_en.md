## SDK1.8.1
**1. Add**

- The aspect ratio 16:9 is now supported when capturing videos.
- Uplink bitrate is added for audio 2s reporting.


**2. Modify**
- Aspect ratio for capturing videos is aligned with the aspect ratio in cloud configuration. You can switch between 4:3 and 16:9;
- Encoding effects for video software under VJ mode have been optimized.

**3. Fix**
- Issues regarding blurred screen, green screen, reversed playback in videos have been fixed;
- Issues regarding occasional inconsistency between display and sound have been fixed;
- Issues regarding video display being reduced/stretched on certain models have been fixed;
- Previously, when video is closed, audio is also stopped briefly. This issue has been fixed;
- When video bitrate is high, the actual bitrate is lower than the bitrate configured in the cloud. This issue has been fixed;
- Serveral Crash issues have been fixed.

**4. API Changes**
(1) AVRoom
- The API name of getQualityParas method has been changed to getQualityParam.
- Added getStatisticsParam method which is used to acquire distribution and average value information of audios and videos without reference scores.

(2) AVEndpoint
- Added getLastVideoStampRecv method which is used to acquire video frame receiving time stamps.
- Added getLastVideoStampSend method which is used to acquire video frame sending time stamps.

(3) AVVideoCtrl
- The enableBeauty method has been deleted. When you call the isEnableBeauty to determine if Beauty Filter is supported, you can directly call the inputBeautyparam API to pass parameters and enable Beauty Filter.

## API Changes for SDK1.8.0 and 1.7
1. AVAudioCtrl
	- A new enumerated value "AUDIO_DATA_SOURCE_VOICEDISPOSE" has been added for AudioDataSourceType, which is a microphone audio data pre-processing option used to customize audio pre-processing.
2. AVContext
 - The "createContext" method has been renamed to "createInstance";
 - The static method "destroyContext" has been adjusted to instance method "destroy";
 - The "startContext" method has been renamed to "start";
 - The "stopContext" method has been renamed to "stop";
 - The API "StartContextCallback" has been rename to "StartCallback";
 - The API "StopContextCallback" has been rename to "StopCallback";
 - The "GetSDKVersion" method has been renamed to "GetVersion";
 - The "onPause" method has been deleted;
 - The "onResume" method has been deleted.
3. AVEndpoint
 - Added getLastAudioStampSend method which is used to acquire the uplink time stamp of current audio;
 - Added getLastAudioStampRecv method which is used to acquire the downlink time stamp of current audio;
4. AVRoomMulti
 - Added ChangeAVControlRole method which is used to dynamically change the stream-controlled role in room chats; 
5. AVRoomMulti.EnterRoomParam
 - Added videoRecvMode parameter which is used to control video receive mode.
6. AVRoom.Delegate
 - Added OnSemiAutoRecvCameraVideo method which is used to receive camera video event notifications in semi-auto mode.
7. AVVideoCtrl
 - Added isEnableBeauty method which is used to query (externally) whether Beauty Filter is supported for the model.
